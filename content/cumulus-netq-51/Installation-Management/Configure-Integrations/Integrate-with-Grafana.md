---
title: Integrate NetQ with Grafana
author: NVIDIA
weight: 550
toc: 3
---

The NetQ integration with Grafana allows you to create customized dashboards and to visualize metrics across your network devices. To view data in Grafana, first configure security between NetQ and OTel clients, configure OpenTelemetry (OTel) on the devices in your network, then configure the data sources in Grafana. <!--test-->

{{%notice note%}}
The Grafana integration is in beta and supported for on-premises deployments only.
{{%/notice%}}

## Requirements and Support

- Switches must have a Spectrum-2 or later ASIC. The number of supported switches varies based on the deployment model and reflects an environment where each switch is configured with OpenTelemetry and running the NetQ agent.
   - Standalone: 5 switches
   - Cluster: 50 switches
   - 3-node scale cluster: 500 switches
   - 5-node scale cluster: 1,000 switches
- For switches, you must enable OpenTelemetry to collect and export each metric that you want to monitor, as described in the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Open-Telemetry-Export/" text="Cumulus Linux documentation">}}.
- DPUs and ConnectX hosts must be running DOCA Telemetry Service (DTS) version 1.18 or later.
- Before you get started with the steps below, {{<exlink url="https://grafana.com/docs/grafana/latest/setup-grafana/installation/" text="install Grafana">}} and {{<exlink url="https://grafana.com/docs/grafana/latest/setup-grafana/start-restart-grafana/" text="start the Grafana server">}}.
- NetQ retains OTLP metrics for fifteen days.

## Secure OpenTelemetry Export

NetQ is configured with OTLP secure mode with TLS by default and expects clients to secure data with a certificate. You can configure NetQ and your client devices to use your own generated CA certificate, NetQ's self-signed certificate, or set the connections to insecure mode.

{{<tabs "certificate options">}}

{{<tab "TLS with a CA Certificate">}}

{{<tabs "ca-cert-sub-tabs">}}

{{<tab "Cumulus Linux Switches">}}

### TLS with a CA Certificate

NVIDIA recommends using your own generated CA certificate. To configure a CA certificate:

1. Copy your certificate files to the NetQ server in the `/mnt/admin` directory. For example, copy the certificate and key to `/mnt/admin/certs/server.crt` and `/mnt/admin/certs/server.key` 

2. Import your certificate on your switches using the `nv action import system security ca-certificate <cert-id> [data <data> | uri <path>]` command. Define the name of the certificate in `<cert-id>` and either provide the raw PEM string of the certificate as `<data>` or provide a path to the certificate file containing the public key as `<path>`.

3. After importing your certificate, set OTLP insecure mode to `disabled` on your switches:

    ```
   nvidia@switch:~$ nv set system telemetry export otlp grpc insecure disabled
   nvidia@switch:~$ nv config apply
   ```

{{</tab>}}

{{<tab "DPUs and NICs">}}

### TLS with a CA Certificate

NVIDIA recommends using your own generated CA certificate. To configure a CA certificate:

1. Copy your certificate files to the NetQ server in the `/mnt/admin` directory. For example, copy the certificate and key to `/mnt/admin/certs/server.crt` and `/mnt/admin/certs/server.key` 

2. Copy your certificate to your DPU or NIC in the `/opt/mellanox/doca/services/telemetry/config/certs/` directory.

3. Change permissions on the certificate with the `chmod 644 /opt/mellanox/doca/services/telemetry/config/certs/ca.pem` command to make the certificate readable to all users.

4. [Configure OpenTelemetry](#configure-and-enable-opentelemetry-on-devices) on your DPU or NIC and include an additional line referencing the certificate in `/opt/mellanox/doca/services/telemetry/config/dts_config.ini`:

```
open-telemetry-ca-file=/config/certs/ca.pem
```

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "TLS with NetQ's Self-signed Certificate" >}}

{{<tabs "netq-self-cert-sub-tabs">}}

{{<tab "Cumulus Linux Switches">}}
### TLS with NetQ's Self-signed Certificate

To run on the switch in secure mode with NetQ's self-signed certificate:

1. From the NetQ server, display the certificate using `netq show otlp tls-ca-cert dump` command. Copy the certificate from the output.

2. On the switch, import the certificate with the `nv action import system security ca-certificate <cert-id> data <data>` command. Define the name of the certificate in `<cert-id>` and replace `<data>` with the certificate data you generated in the preceding step.

3. Configure the certificate to secure the OTel connection. Replace `ca-certificate` with the name of your certificate; this is the `<cert-id>` from the previous step.

   ```
   nvidia@switch:~$ nv set system telemetry export otlp grpc cert-id <ca-certificate>
   nvidia@switch:~$ nv config apply
   ```

4. Next, disable `insecure` mode and apply the change:
    
    ```
   nvidia@switch:~$ nv set system telemetry export otlp grpc insecure disabled
   nvidia@switch:~$ nv config apply
   ```
5. Run `nv show system telemetry health` to display the destination port and IP address, along with connectivity status.

{{</tab>}}

{{<tab "DPUs and NICs">}}

### TLS with NetQ's Self-signed Certificate

To run on a DPU or NIC in secure mode with NetQ's self-signed certificate:

1. From the NetQ server, display the certificate using `netq show otlp tls-ca-cert dump` command. Copy the certificate from the output. 

2. Copy the certificate content from step 1 to a file on your DPU or NIC in the `/opt/mellanox/doca/services/telemetry/config/certs/` directory. For example, copy the output content into `/opt/mellanox/doca/services/telemetry/config/certs/ca.pem`

3. Change permissions on the certificate with the `chmod 644 /opt/mellanox/doca/services/telemetry/config/certs/ca.pem` command to make the certificate readable to all users.

4. [Configure OpenTelemetry](#configure-and-enable-opentelemetry-on-devices) on your DPU or NIC and include an additional line referencing the certificate in `/opt/mellanox/doca/services/telemetry/config/dts_config.ini`:

```
open-telemetry-ca-file=/config/certs/ca.pem
```

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "Insecure Mode" >}}

{{<tabs "insecure-sub-tabs">}}

{{<tab "Cumulus Linux Switches">}}
### Insecure Mode

To use insecure mode and disable TLS:

1. On your NetQ server, run the `netq set otlp security-mode insecure` command.

2. On your switches, configure insecure mode:

    ```
   nvidia@switch:~$ nv set system telemetry export otlp grpc insecure disabled
   nvidia@switch:~$ nv config apply
   ```
{{</tab>}}

{{<tab "DPUs and NICs">}}
### Insecure Mode

To use insecure mode and disable TLS:

1. On your NetQ server, run the `netq set otlp security-mode insecure` command.

2. On your DPU or NIC, [Configure OpenTelemetry](#configure-and-enable-opentelemetry-on-devices) but do not include a `open-telemetry-ca-file=` line in the `/opt/mellanox/doca/services/telemetry/config/dts_config.ini` configuration file.

{{</tab>}}

{{</tabs>}}

{{</tabs>}}

{{</tabs>}}
## Configure and Enable OpenTelemetry on Devices

Configure your client devices to send OpenTelemetry data to NetQ.

{{<tabs "TabID23" >}}

{{<tab "Cumulus Linux Switches">}}

Enable OpenTelemetry for each metric that you want to monitor, as described in the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Open-Telemetry-Export/" text="Cumulus Linux documentation">}}. Use your NetQ server or cluster’s IP address and port 30008 when configuring the OTLP export destination.

{{<notice info>}}
NVIDIA recommends setting the <code>sample-interval</code> option to 10 seconds for each metric that allows you to set a sample interval.
{{</notice>}}

{{</tab>}}

{{<tab "DPUs and NICs" >}}

1. {{<link title="Install NIC and DPU Agents" text="Install DOCA Telemetry Service (DTS)">}} on your ConnectX hosts or DPUs.

2. Configure OpenTelemetry data export by editing the `/opt/mellanox/doca/services/telemetry/config/dts_config.ini` file. Add the following lines under the `IPC transport` section. Replace `TS-IP` with the IP address of your telemetry receiver. 

For HTTPS transport:

```
open-telemetry-transport=http
open-telemetry-receiver=http://<TS-IP>:30009/v1/metrics
```

For gRPC transport:

```
open-telemetry-transport=grpc
open-telemetry-receiver=<TS-IP>:30008/v1/metrics
```

3. To support telemetry at a scale of up to 4K devices on hosts with ConnectX NICs or DPUs in NIC mode, configure {{<exlink url="https://docs.nvidia.com/doca/sdk/doca-telemetry-service-guide/index.html#src-4464438559_id-.DOCATelemetryServiceGuidev3.2.1Nov_LTS-counterset-and-fieldset-filesCountersetandFieldsetFiles" text="counterset and fieldset">}} files to control the telemetry data exported from DTS.

Download {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-50/DTS/gb200.cset" text="gb200.cset">}} and {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-50/DTS/gb200.fset" text="gb200.fset">}}, then copy the files to `/opt/mellanox/doca/services/telemetry/config/prometheus_configs/cset/` on your host.

Add the following lines to the `/opt/mellanox/doca/services/telemetry/config/dts_config.ini` configuration file:

```
prometheus-fset-indexes=device_name,device_id,pod_name,^id$,@id 
prometheus-cset-dir=/config/prometheus_configs/cset
prometheus-fset-dir=/config/prometheus_configs/cset
open-telemetry-field-set=gb200 
open-telemetry-counter-set=gb200
```

{{%notice note%}}
- It can take up to a minute for the device to restart and apply the changes. If you manually edit the fieldset file, you must restart DTS for the changes to be reflected.
{{%/notice%}}

Read more about OpenTelemetry and DTS configurations in the {{<exlink url="https://docs.nvidia.com/doca/archive/2-9-3/doca+telemetry+service+guide/index.html#src-3382565608_id-.DOCATelemetryServiceGuidev2.9.1-OpenTelemetryExporter" text="DOCA Telemetry Service guide">}}.

{{</tab>}}

{{</tabs>}}


## Configure an External TSDB

OpenTelemetry data is stored in the NetQ TSDB. In addition to NetQ's local storage, you can configure NetQ to also send the collected data to your own external TSDB:

1. If the connection to your external TSDB is secured with TLS, copy the certificate to the NetQ server in the `/mnt/admin/` directory, and reference the full path to the file with the `netq set otlp endpoint-ca-cert tsdb-name <text-tsdb-endpoint> ca-cert <text-path-to-ca-crt>` command.

2. From the NetQ server, add the OTel endpoint of your time-series database (TSDB). Replace `text-tsdb-endpoint` and `text-tsdb-endpoint-url` with the name and IP address of your TSDB, respectively. Include the `export true` option to begin exporting data immediately. Set `security-mode` to `tls` if you configured a certificate to secure the connection, otherwise use `security-mode insecure`.

```
nvidia@netq-server:~$ netq add otlp endpoint tsdb-name <text-tsdb-endpoint> tsdb-url <text-tsdb-endpoint-url> [export true | export false] [security-mode <text-mode>]
```

3. If you set the `export` option to `true` in the previous step, the TSDB will begin receiving the time-series data for the metrics that you configured on the switch. Use the `netq show otlp endpoint` command to view the TSDB endpoint configuration.

## Customize Metric Collection

NetQ restricts the metrics accepted into the local TSDB by default. To view the default whitelist of permitted metrics, run the `netq show otlp whitelist default` command:

{{<expand "Default OTLP Whitelist">}}
```
nvidia@netq-server:~$ netq show otlp whitelist default
- nvswitch_interface_tc_tx_octet
- nvswitch_interface_pg_rx_octet
- nvswitch_interface_oper_state
- nvswitch_interface_dot3_stats_symbol_errors
- nvswitch_interface_carrier_down_changes_total
- nvswitch_interface_dot3_in_pause_frames
- nvswitch_interface_dot3_out_pause_frames
- nvswitch_interface_tc_tx_ecn_marked_tc
- nvswitch_interface_tx_wait
- nvidia_smi_utilization_memory
- nvidia_smi_utilization_gpu
- nvidia_smi_memory_used
- nvidia_smi_temperature_gpu
- hw_np_cnp_sent
- hw_rp_cnp_handled
- hw_rp_cnp_ignored
- np_ecn_marked_roce_packets
- hw_duplicate_request
- hw_implied_nak_seq_err
- hw_local_ack_timeout_err
- hw_out_of_sequence
- hw_packet_seq_err
- hw_req_cqe_error
- hw_req_cqe_flush_error
- hw_req_remote_access_errors
- hw_req_remote_invalid_request
- hw_resp_cqe_error
- hw_resp_cqe_flush_error
- hw_resp_remote_access_errors
- hw_rnr_nak_retry_err
- hw_roce_adp_retrans
- hw_roce_adp_retrans_to
- rx_bytes
- rx_prio0_buf_discard
- rx_prio1_buf_discard
- rx_prio2_buf_discard
- rx_prio3_buf_discard
- rx_prio4_buf_discard
- rx_prio5_buf_discard
- rx_prio6_buf_discard
- rx_prio7_buf_discard
- rx_prio0_cong_discard
- rx_prio1_cong_discard
- rx_prio2_cong_discard
- rx_prio3_cong_discard
- rx_prio4_cong_discard
- rx_prio5_cong_discard
- rx_prio6_cong_discard
- rx_prio7_cong_discard
- rx_prio0_bytes
- rx_prio1_bytes
- rx_prio2_bytes
- rx_prio3_bytes
- rx_prio4_bytes
- rx_prio5_bytes
- rx_prio6_bytes
- rx_prio7_bytes
- rx_prio0_packets
- rx_prio1_packets
- rx_prio2_packets
- rx_prio3_packets
- rx_prio4_packets
- rx_prio5_packets
- rx_prio6_packets
- rx_prio7_packets
- tx_prio0_bytes
- tx_prio1_bytes
- tx_prio2_bytes
- tx_prio3_bytes
- tx_prio4_bytes
- tx_prio5_bytes
- tx_prio6_bytes
- tx_prio7_bytes
- tx_prio0_packets
- tx_prio1_packets
- tx_prio2_packets
- tx_prio3_packets
- tx_prio4_packets
- tx_prio5_packets
- tx_prio6_packets
- tx_prio7_packets
- rx_prio0_pause
- rx_prio1_pause
- rx_prio2_pause
- rx_prio3_pause
- rx_prio4_pause
- rx_prio5_pause
- rx_prio6_pause
- rx_prio7_pause
- rx_prio0_pause_duration
- rx_prio1_pause_duration
- rx_prio2_pause_duration
- rx_prio3_pause_duration
- rx_prio4_pause_duration
- rx_prio5_pause_duration
- rx_prio6_pause_duration
- rx_prio7_pause_duration
- rx_prio0_pause_transition
- rx_prio1_pause_transition
- rx_prio2_pause_transition
- rx_prio3_pause_transition
- rx_prio4_pause_transition
- rx_prio5_pause_transition
- rx_prio6_pause_transition
- rx_prio7_pause_transition
- tx_prio0_pause
- tx_prio1_pause
- tx_prio2_pause
- tx_prio3_pause
- tx_prio4_pause
- tx_prio5_pause
- tx_prio6_pause
- tx_prio7_pause
- tx_prio0_pause_duration
- tx_prio1_pause_duration
- tx_prio2_pause_duration
- tx_prio3_pause_duration
- tx_prio4_pause_duration
- tx_prio5_pause_duration
- tx_prio6_pause_duration
- tx_prio7_pause_duration
- Link_Down
- Time_since_last_clear__Min
- FC_Zero_Hist
- hist0
- hist1
- hist2
- hist3
- hist4
- hist5
- hist6
- hist7
- hist8
- hist9
- hist10
- hist11
- hist12
- hist13
- hist14
- hist15
- Raw_Errors_lane0
- Raw_Errors_lane1
- Raw_Errors_lane2
- Raw_Errors_lane3
- Raw_Errors_lane4
- Raw_Errors_lane5
- Raw_Errors_lane6
- Raw_Errors_lane7
- Effective_Errors
- Symbol_Errors
- rx_power_lane_0
- rx_power_lane_1
- rx_power_lane_2
- rx_power_lane_3
- rx_power_lane_4
- rx_power_lane_5
- rx_power_lane_6
- rx_power_lane_7
- tx_power_lane_0
- tx_power_lane_1
- tx_power_lane_2
- tx_power_lane_3
- tx_power_lane_4
- tx_power_lane_5
- tx_power_lane_6
- tx_power_lane_7
- temperature_high_th
- temperature_low_th
- Module_Temperature
- Module_Voltage
- Chip_Temp
- Advanced_Status_Opcode
- e2e_reason_opcode
- device_name
- Phy_Manager_State
- Ethernet_Protocol_Active
- Active_FEC
- Cable_PN
- Cable_SN
- cable_technology
- cable_type
- cable_vendor
- cable_length
- cable_identifier
- module_fw_version
- Device_FW_Version
- Status_Message
- down_blame
- local_reason_opcode
- remote_reason_opcode
- Port_Number
- MAC_Address
- tx_packets_phy
- tx_bytes_phy
- rx_vport_multicast_packets
- rx_crc_errors_phy
- outbound_pci_stalled_rd
- tx193_packets
- tx_bytes
- tx_packets
- rx_packets
- rx_packets_phy
- DCGM_FI_DEV_APP_MEM_CLOCK
- DCGM_FI_DEV_APP_SM_CLOCK
- DCGM_FI_DEV_AUTOBOOST
- DCGM_FI_DEV_BAR1_FREE
- DCGM_FI_DEV_BAR1_TOTAL
- DCGM_FI_DEV_BAR1_USED
- DCGM_FI_DEV_BOARD_LIMIT_VIOLATION
- DCGM_FI_DEV_CLOCK_THROTTLE_REASONS
- DCGM_FI_DEV_COMPUTE_MODE
- DCGM_FI_DEV_COUNT
- DCGM_FI_DEV_CPU_AFFINITY_0
- DCGM_FI_DEV_CPU_AFFINITY_1
- DCGM_FI_DEV_CPU_AFFINITY_2
- DCGM_FI_DEV_CPU_AFFINITY_3
- DCGM_FI_DEV_CUDA_COMPUTE_CAPABILITY
- DCGM_FI_DEV_DEC_UTIL
- DCGM_FI_DEV_ECC_CURRENT
- DCGM_FI_DEV_ECC_DBE_AGG_DEV
- DCGM_FI_DEV_ECC_DBE_AGG_L1
- DCGM_FI_DEV_ECC_DBE_AGG_L2
- DCGM_FI_DEV_ECC_DBE_AGG_REG
- DCGM_FI_DEV_ECC_DBE_AGG_TEX
- DCGM_FI_DEV_ECC_DBE_AGG_TOTAL
- DCGM_FI_DEV_ECC_DBE_VOL_DEV
- DCGM_FI_DEV_ECC_DBE_VOL_L1
- DCGM_FI_DEV_ECC_DBE_VOL_L2
- DCGM_FI_DEV_ECC_DBE_VOL_REG
- DCGM_FI_DEV_ECC_DBE_VOL_TEX
- DCGM_FI_DEV_ECC_DBE_VOL_TOTAL
- DCGM_FI_DEV_ECC_PENDING
- DCGM_FI_DEV_ECC_SBE_AGG_DEV
- DCGM_FI_DEV_ECC_SBE_AGG_L1
- DCGM_FI_DEV_ECC_SBE_AGG_L2
- DCGM_FI_DEV_ECC_SBE_AGG_REG
- DCGM_FI_DEV_ECC_SBE_AGG_TEX
- DCGM_FI_DEV_ECC_SBE_AGG_TOTAL
- DCGM_FI_DEV_ECC_SBE_VOL_DEV
- DCGM_FI_DEV_ECC_SBE_VOL_L1
- DCGM_FI_DEV_ECC_SBE_VOL_L2
- DCGM_FI_DEV_ECC_SBE_VOL_REG
- DCGM_FI_DEV_ECC_SBE_VOL_TEX
- DCGM_FI_DEV_ECC_SBE_VOL_TOTAL
- DCGM_FI_DEV_ENC_UTIL
- DCGM_FI_DEV_ENFORCED_POWER_LIMIT
- DCGM_FI_DEV_FAN_SPEED
- DCGM_FI_DEV_FB_FREE
- DCGM_FI_DEV_FB_TOTAL
- DCGM_FI_DEV_FB_USED
- DCGM_FI_DEV_GPU_NVLINK_ERRORS
- DCGM_FI_DEV_GPU_TEMP
- DCGM_FI_DEV_GPU_UTIL
- DCGM_FI_DEV_INFOROM_CONFIG_CHECK
- DCGM_FI_DEV_INFOROM_CONFIG_VALID
- DCGM_FI_DEV_LOW_UTIL_VIOLATION
- DCGM_FI_DEV_MAX_MEM_CLOCK
- DCGM_FI_DEV_MAX_SM_CLOCK
- DCGM_FI_DEV_MAX_VIDEO_CLOCK
- DCGM_FI_DEV_MEMORY_TEMP
- DCGM_FI_DEV_MEM_CLOCK
- DCGM_FI_DEV_MEM_COPY_UTIL
- DCGM_FI_DEV_MINOR_NUMBER
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L0
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L1
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L2
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L3
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L4
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L5
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L6
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L7
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L8
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L9
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L10
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L11
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L12
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L13
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L14
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L15
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L16
- DCGM_FI_DEV_NVLINK_BANDWIDTH_L17
- DCGM_FI_DEV_NVLINK_BANDWIDTH_TOTAL
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L0
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L1
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L2
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L3
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L4
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L5
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L6
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L7
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L8
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L9
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L10
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L11
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L12
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L13
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L14
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L15
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L16
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L17
- DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_TOTAL
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L0
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L1
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L2
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L3
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L4
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L5
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L6
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L7
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L8
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L9
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L10
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L11
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L12
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L13
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L14
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L15
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L16
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L17
- DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_TOTAL
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L0
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L1
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L2
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L3
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L4
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L5
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L6
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L7
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L8
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L9
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L10
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L11
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L12
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L13
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L14
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L15
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L16
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L17
- DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_TOTAL
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L0
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L1
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L2
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L3
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L4
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L5
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L6
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L7
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L8
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L9
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L10
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L11
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L12
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L13
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L14
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L15
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L16
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L17
- DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_TOTAL
- DCGM_FI_DEV_NVML_INDEX
- DCGM_FI_DEV_PCIE_LINK_GEN
- DCGM_FI_DEV_PCIE_LINK_WIDTH
- DCGM_FI_DEV_PCIE_MAX_LINK_GEN
- DCGM_FI_DEV_PCIE_MAX_LINK_WIDTH
- DCGM_FI_DEV_PCIE_REPLAY_COUNTER
- DCGM_FI_DEV_PCIE_RX_THROUGHPUT
- DCGM_FI_DEV_PCIE_TX_THROUGHPUT
- DCGM_FI_DEV_PCI_COMBINED_ID
- DCGM_FI_DEV_PCI_SUBSYS_ID
- DCGM_FI_DEV_POWER_MGMT_LIMIT
- DCGM_FI_DEV_POWER_MGMT_LIMIT_DEF
- DCGM_FI_DEV_POWER_MGMT_LIMIT_MAX
- DCGM_FI_DEV_POWER_MGMT_LIMIT_MIN
- DCGM_FI_DEV_POWER_USAGE
- DCGM_FI_DEV_POWER_VIOLATION
- DCGM_FI_DEV_PSTATE
- DCGM_FI_DEV_RELIABILITY_VIOLATION
- DCGM_FI_DEV_RETIRED_DBE
- DCGM_FI_DEV_RETIRED_PENDING
- DCGM_FI_DEV_RETIRED_SBE
- DCGM_FI_DEV_SHUTDOWN_TEMP
- DCGM_FI_DEV_SLOWDOWN_TEMP
- DCGM_FI_DEV_SM_CLOCK
- DCGM_FI_DEV_SYNC_BOOST_VIOLATION
- DCGM_FI_DEV_THERMAL_VIOLATION
- DCGM_FI_DEV_TOTAL_APP_CLOCKS_VIOLATION
- DCGM_FI_DEV_TOTAL_BASE_CLOCKS_VIOLATION
- DCGM_FI_DEV_TOTAL_ENERGY_CONSUMPTION
- DCGM_FI_DEV_VIDEO_CLOCK
- DCGM_FI_DEV_VIRTUAL_MODE
- DCGM_FI_DEV_XID_ERRORS
- DCGM_FI_PROF_DRAM_ACTIVE
- DCGM_FI_PROF_GR_ENGINE_ACTIVE
- DCGM_FI_PROF_NVLINK_RX_BYTES
- DCGM_FI_PROF_NVLINK_TX_BYTES
- DCGM_FI_PROF_PCIE_RX_BYTES
- DCGM_FI_PROF_PCIE_TX_BYTES
- DCGM_FI_PROF_PIPE_FP16_ACTIVE
- DCGM_FI_PROF_PIPE_FP32_ACTIVE
- DCGM_FI_PROF_PIPE_FP64_ACTIVE
- DCGM_FI_PROF_PIPE_TENSOR_ACTIVE
- DCGM_FI_PROF_SM_ACTIVE
- DCGM_FI_PROF_SM_OCCUPANCY
- slurm_nodes
- slurm_job_per_node
- slurm_jobs_node_count
- slurm_jobs
```
{{</expand>}}<p></p>

You cannot modify the default whitelist, but you can configure a custom whitelist to permit additional metrics. To create a custom whitelist, configure a YAML list of metric names on the NetQ filesystem, and run the `netq set otlp whitelist file /path/to/filename.yaml tsdb-name default` command. The following example adds `nvswitch_interface_rx_wait` and `nvswitch_interface_tx_stats_pkts64octets` to the custom whitelist for the internal NetQ TSDB:

1. Create a YAML file with a list of metric names:

```
nvidia@netq-server:~$ vi /home/nvidia/custom.yaml
---
- nvswitch_interface_rx_wait
- nvswitch_interface_tx_stats_pkts64octets
```

2. Apply the custom whitelist:

```
nvidia@netq-server:~$ netq set otlp whitelist file /path/to/custom.yaml tsdb-name default
```

You can view metrics added to the internal TSDB custom whitelist with the `netq show otlp whitelist custom` command:

```
nvidia@netq-server:~$ netq show otlp whitelist custom
- nvswitch_interface_rx_wait
- nvswitch_interface_tx_stats_pkts64octets
```

The OTLP whitelist is disabled on external TSDB endpoints by default. To configure a custom whitelist to limit the metrics sent to an external TSDB, create a YAML file as in step 1 above, but reference the external TSDB endpoint name in the `netq set otlp whitelist file` command and then enable the whitelist for the external TSDB with the `netq modify otlp endpoint tsdb-name` command:

```
nvidia@netq-server:~$ netq set otlp whitelist file /home/nvidia/config.yaml tsdb-name EXTERNAL_DB_NAME
nvidia@netq-server:~$ netq modify otlp endpoint tsdb-name EXTERNAL_DB_NAME whitelist_enabled true
```

Validate the custom whitelist with the `netq show otlp whitelist tsdb-name EXTERNAL_DB_NAME` command.

{{%notice note%}}
When you enable the OTLP whitelist for an external TSDB endpoint, the `default` whitelist applied to the internal NetQ TSDB is not applied to external TSDBs. Configure all desired metrics in the YAML file applied to external TSDBs when you enable the whitelist.
{{%/notice%}}
## Collect Slurm Telemetry

{{<exlink url="https://slurm.schedmd.com/quickstart.html" text="Slurm">}} (Simple Linux Utility for Resource Management) is an open-source job scheduler used in high-performance computing (HPC) environments. It manages and allocates compute resources, schedules jobs, and distributes workloads across a cluster.

To view and filter Slurm jobs in Grafana, you must have an {{<exlink url="https://www.nvidia.com/en-us/data-center/base-command/manager/" text="NVIDIA Base Command Manager">}} deployment running BCM v11 or later. 

1. Authenticate into BCM using either basic authentication (username and password) or certificate-based authentication.

{{<tabs "BCM auth">}}

{{<tab "Basic Authentication">}}

Two versions of this command exist. Specify either the Base Command Manager IP address in `ip-address` or the domain name in `hostname`. Replace `port-text` with the port that BCM uses. You can run this command from any node in your cluster.

```
nvidia@netq-server:~$ netq add bcm auth-type basic user <username> pass <password> ip <ip-address> port <port-text>  
nvidia@netq-server:~$ netq add bcm auth-type basic user <username> pass <password> hostname <hostname> port <port-text> 
```
For example:
```
nvidia@netq-server:~$ netq add bcm auth-type basic user admin pass secretpass123 ip 192.168.1.100 port 8082
```
{{</tab>}}

{{<tab "Certificate-based Authentication" >}}
{{%notice infonopad%}}
You must run this command from the node that hosts the <code>netq-bcm-gateway</code> pod. To identify this node, run the <code>kubectl get pods -o wide | grep netq-bcm-gateway</code> command. The output of this command displays the correct node.
{{%/notice%}}

Two versions of this command exist. Specify either the Base Command Manager IP address in `ip-address` or the domain name in `hostname`. Replace `port-text` with the port that BCM uses. Specify the full path to both the certificate and key files. These are typically located in the `/mnt/bcm/` directory.
```
nvidia@netq-server:~$ netq add bcm auth-type cert cert-file <certificate-path> key-file <key-path> ip <ip-address> port <port-text> 
nvidia@netq-server:~$ netq add bcm auth-type cert cert-file <certificate-path> key-file <key-path> hostname <hostname> port <port-text> 
```
For example:
```
nvidia@netq-server:~$ netq add bcm auth-type cert cert-file /mnt/bcm/bcm.crt key-file /mnt/bcm/bcm.key ip 192.168.1.100 port 8082 
```
{{</tab>}}

{{</tab>}}

2. Verify that your credentials are correct and check for BCM version compatibility:

```
nvidia@netq-server:~$ netq show bcm auth-status
```

You will configure the Slurm data source in the next section using the `slurm-nodes-and-jobs-dashboard` JSON file.

{{< expand "slurm-nodes-and-jobs-dashboard.json" >}}
```
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "grafana",
          "uid": "-- Grafana --"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 14,
  "links": [],
  "panels": [
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 20,
        "w": 4,
        "x": 0,
        "y": 0
      },
      "id": 13,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Slurm_logo.svg/590px-Slurm_logo.svg.png style=\"background-color:white;\" width=\"430\" height=\"320\">",
        "mode": "html"
      },
      "pluginVersion": "12.0.1",
      "title": "Panel Title",
      "type": "text"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisPlacement": "auto",
            "fillOpacity": 70,
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineWidth": 0,
            "spanNulls": 300000
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "bool_on_off"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 10,
        "w": 20,
        "x": 4,
        "y": 0
      },
      "id": 10,
      "options": {
        "alignValue": "left",
        "legend": {
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "mergeValues": true,
        "rowHeight": 0.9,
        "showValue": "never",
        "tooltip": {
          "hideZeros": false,
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "builder",
          "exemplar": false,
          "expr": "min by(pretty_name) (slurm_job_per_node{wlm=~\"$wlm\"})",
          "format": "time_series",
          "fullMetaSearch": false,
          "includeNullMetadata": false,
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "SLURM Timeline",
      "type": "state-timeline"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "fillOpacity": 80,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineWidth": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "decimals": 0,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/Pod 2.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "yellow",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "__systemRef": "hideSeriesFrom",
            "matcher": {
              "id": "byNames",
              "options": {
                "mode": "exclude",
                "names": [
                  "Value (lastNotNull)"
                ],
                "prefix": "All except:",
                "readOnly": true
              }
            },
            "properties": [
              {
                "id": "custom.hideFrom",
                "value": {
                  "legend": false,
                  "tooltip": false,
                  "viz": true
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 10,
        "w": 20,
        "x": 4,
        "y": 10
      },
      "id": 20,
      "options": {
        "barRadius": 0,
        "barWidth": 0.97,
        "fullHighlight": false,
        "groupWidth": 0.7,
        "legend": {
          "calcs": [],
          "displayMode": "table",
          "placement": "right",
          "showLegend": false
        },
        "orientation": "horizontal",
        "showValue": "auto",
        "stacking": "none",
        "tooltip": {
          "hideZeros": false,
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        },
        "xTickLabelRotation": 0,
        "xTickLabelSpacing": 0
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "builder",
          "exemplar": false,
          "expr": "sort_desc(count by(pretty_name) (slurm_job_per_node{wlm=~\"$wlm\"}))",
          "format": "table",
          "fullMetaSearch": false,
          "includeNullMetadata": true,
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "SLURM Node Allocation",
      "transformations": [
        {
          "id": "groupBy",
          "options": {
            "fields": {
              "Value": {
                "aggregations": [
                  "lastNotNull"
                ],
                "operation": "aggregate"
              },
              "pod": {
                "aggregations": []
              },
              "pod_su": {
                "aggregations": [],
                "operation": "groupby"
              },
              "pretty_name": {
                "aggregations": [],
                "operation": "groupby"
              },
              "su": {
                "aggregations": [],
                "operation": "groupby"
              }
            }
          }
        },
        {
          "id": "groupingToMatrix",
          "options": {
            "columnField": "pod_su",
            "rowField": "pretty_name",
            "valueField": "Value (lastNotNull)"
          }
        }
      ],
      "type": "barchart"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            }
          },
          "mappings": []
        },
        "overrides": [
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*mixed.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "light-orange",
                  "mode": "shades"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*down.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*reserved.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "blue",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*idle.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "yellow",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*inval.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*allocate.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "green",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*complet.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "orange",
                  "mode": "fixed"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 0,
        "y": 20
      },
      "id": 18,
      "options": {
        "displayLabels": [
          "value",
          "name"
        ],
        "legend": {
          "displayMode": "table",
          "placement": "right",
          "showLegend": true,
          "sortBy": "Value",
          "sortDesc": true,
          "values": [
            "value"
          ]
        },
        "pieType": "pie",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "count by(state) (count by(state, node) (count_over_time((slurm_nodes{wlm=~\"$wlm\"} != 0)[${__range_s}s]) > 0))",
          "fullMetaSearch": false,
          "hide": false,
          "includeNullMetadata": true,
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "B",
          "useBackend": false
        }
      ],
      "title": "Slurm Node Status - Over Time",
      "type": "piechart"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "fixed"
          },
          "custom": {
            "align": "center",
            "cellOptions": {
              "applyToRow": true,
              "mode": "basic",
              "type": "color-background",
              "wrapText": false
            },
            "filterable": true,
            "inspect": false
          },
          "fieldMinMax": false,
          "mappings": [
            {
              "options": {
                "idle": {
                  "color": "dark-yellow",
                  "index": 8
                }
              },
              "type": "value"
            },
            {
              "options": {
                "pattern": ".*drain.*",
                "result": {
                  "color": "purple",
                  "index": 0
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*down.*",
                "result": {
                  "color": "red",
                  "index": 1
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*reserved.*",
                "result": {
                  "color": "blue",
                  "index": 2
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*idle,.*",
                "result": {
                  "color": "yellow",
                  "index": 3
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*inval.*",
                "result": {
                  "color": "red",
                  "index": 4
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*allocate.*",
                "result": {
                  "color": "green",
                  "index": 5
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*complet.*",
                "result": {
                  "color": "orange",
                  "index": 6
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*mix.*",
                "result": {
                  "color": "semi-dark-orange",
                  "index": 7
                }
              },
              "type": "regex"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "State"
            },
            "properties": [
              {
                "id": "custom.width"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 12,
        "y": 20
      },
      "id": 1,
      "options": {
        "cellHeight": "md",
        "footer": {
          "countRows": false,
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "showHeader": true,
        "sortBy": [
          {
            "desc": false,
            "displayName": "Node"
          }
        ],
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "(count by(state, node) (count_over_time((slurm_nodes{wlm=~\"$wlm\"} != 0)[${__range_s}s]) > 0))",
          "format": "time_series",
          "fullMetaSearch": false,
          "includeNullMetadata": false,
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Slurm Nodes Status",
      "transformations": [
        {
          "id": "seriesToRows",
          "options": {}
        },
        {
          "id": "extractFields",
          "options": {
            "format": "kvp",
            "keepTime": false,
            "replace": true,
            "source": "Metric"
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "cluster": true,
              "opid": true,
              "reason": true,
              "service.name": true,
              "telemetry.sdk.language": true,
              "telemetry.sdk.name": true,
              "telemetry.sdk.version": true,
              "wlm": true
            },
            "includeByName": {},
            "indexByName": {},
            "renameByName": {
              "node": "Node",
              "state": "State"
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            }
          },
          "mappings": []
        },
        "overrides": [
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*Not.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 0,
        "y": 34
      },
      "id": 3,
      "options": {
        "legend": {
          "displayMode": "table",
          "placement": "right",
          "showLegend": true,
          "values": [
            "value"
          ]
        },
        "pieType": "pie",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "count by(reason) (slurm_nodes{wlm=~\"$wlm\"} == 0)",
          "fullMetaSearch": false,
          "includeNullMetadata": true,
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Errors Count",
      "type": "piechart"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "align": "center",
            "cellOptions": {
              "applyToRow": true,
              "mode": "basic",
              "type": "color-background",
              "wrapText": false
            },
            "filterable": true,
            "inspect": false
          },
          "fieldMinMax": false,
          "mappings": [
            {
              "options": {
                "drained": {
                  "color": "red",
                  "index": 1
                }
              },
              "type": "value"
            },
            {
              "options": {
                "pattern": ".*drained.*",
                "result": {
                  "color": "red",
                  "index": 0
                }
              },
              "type": "regex"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "red"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Node"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 234
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "State"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 107
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Reason"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 238
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 12,
        "y": 34
      },
      "id": 2,
      "options": {
        "cellHeight": "md",
        "footer": {
          "countRows": false,
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "showHeader": true,
        "sortBy": [
          {
            "desc": false,
            "displayName": "Node"
          }
        ]
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "min_over_time((slurm_nodes{wlm=~\"$wlm\"} == 0)[${__range_s}s])",
          "format": "time_series",
          "fullMetaSearch": false,
          "includeNullMetadata": false,
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Drained Slurm Nodes  ",
      "transformations": [
        {
          "id": "seriesToRows",
          "options": {}
        },
        {
          "id": "extractFields",
          "options": {
            "format": "kvp",
            "keepTime": false,
            "replace": true,
            "source": "Metric"
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "__name__": true,
              "cluster": true,
              "group": true,
              "hostname": true,
              "instance": true,
              "job": true,
              "service.name": true,
              "state": false,
              "telemetry.sdk.language": true,
              "telemetry.sdk.name": true,
              "telemetry.sdk.version": true,
              "wlm": true
            },
            "includeByName": {},
            "indexByName": {
              "__name__": 0,
              "group": 1,
              "hostname": 2,
              "instance": 3,
              "job": 4,
              "node": 5,
              "reason": 7,
              "state": 6
            },
            "renameByName": {
              "node": "Node",
              "reason": "Reason",
              "state": "State"
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 100,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 0,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "normal"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "allocate"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "green",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "drained"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "idle"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "green",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "inval"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Allocated"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "green",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Drain"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Idle"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "blue",
                  "mode": "fixed"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 0,
        "y": 48
      },
      "id": 19,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "table",
          "placement": "right",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "count(slurm_nodes{state=~\"down|drained|draining|inval\", wlm=~\"$wlm\"})",
          "hide": false,
          "instant": false,
          "legendFormat": "Drain",
          "range": true,
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "count(slurm_nodes{state=~\"allocate|planned|reserved\", wlm=~\"$wlm\"})",
          "fullMetaSearch": false,
          "includeNullMetadata": true,
          "instant": false,
          "legendFormat": "Allocated",
          "range": true,
          "refId": "A",
          "useBackend": false
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "count(slurm_nodes{state=~\"idle\", wlm=~\"$wlm\"})",
          "hide": false,
          "instant": false,
          "legendFormat": "Idle",
          "range": true,
          "refId": "C"
        }
      ],
      "title": "Slurm Node Status - Over Time",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "fieldMinMax": false,
          "mappings": [
            {
              "options": {
                "down": {
                  "color": "red",
                  "index": 0
                }
              },
              "type": "value"
            },
            {
              "options": {
                "pattern": ".*drained.*",
                "result": {
                  "color": "red",
                  "index": 1
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*down.*",
                "result": {
                  "color": "red",
                  "index": 2
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*reserved.*",
                "result": {
                  "color": "green",
                  "index": 3
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*idle.*",
                "result": {
                  "color": "green",
                  "index": 4
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*inval.*",
                "result": {
                  "color": "red",
                  "index": 5
                }
              },
              "type": "regex"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "State"
            },
            "properties": []
          },
          {
            "__systemRef": "hideSeriesFrom",
            "matcher": {
              "id": "byNames",
              "options": {
                "mode": "exclude",
                "names": [
                  "root - avia_test_2"
                ],
                "prefix": "All except:",
                "readOnly": true
              }
            },
            "properties": [
              {
                "id": "custom.hideFrom",
                "value": {
                  "legend": false,
                  "tooltip": false,
                  "viz": true
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 12,
        "y": 48
      },
      "id": 6,
      "options": {
        "legend": {
          "calcs": [
            "last"
          ],
          "displayMode": "table",
          "placement": "right",
          "showLegend": true,
          "sortBy": "Name",
          "sortDesc": false
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "builder",
          "exemplar": false,
          "expr": "slurm_jobs_node_count{wlm=~\"$wlm\"}",
          "format": "time_series",
          "fullMetaSearch": false,
          "includeNullMetadata": false,
          "instant": false,
          "legendFormat": "{{user}} - {{job_name}}",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Nodes Per Job",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "align": "center",
            "cellOptions": {
              "applyToRow": true,
              "mode": "basic",
              "type": "color-background",
              "wrapText": false
            },
            "inspect": false
          },
          "fieldMinMax": false,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "State"
            },
            "properties": [
              {
                "id": "custom.width"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Nodes List"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 300
              },
              {
                "id": "custom.cellOptions",
                "value": {
                  "type": "color-text",
                  "wrapText": false
                }
              },
              {
                "id": "custom.inspect",
                "value": true
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 15,
        "w": 24,
        "x": 0,
        "y": 62
      },
      "id": 5,
      "options": {
        "cellHeight": "md",
        "footer": {
          "countRows": false,
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "showHeader": true,
        "sortBy": [
          {
            "desc": false,
            "displayName": "Job ID"
          }
        ],
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "slurm_jobs{wlm=~\"$wlm\"}",
          "format": "time_series",
          "fullMetaSearch": false,
          "includeNullMetadata": false,
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Slurm Jobs Status",
      "transformations": [
        {
          "id": "seriesToRows",
          "options": {}
        },
        {
          "id": "extractFields",
          "options": {
            "format": "kvp",
            "keepTime": false,
            "replace": true,
            "source": "Metric"
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "__name__": true,
              "group": true,
              "hostname": true,
              "instance": true,
              "job": true,
              "service.name": true,
              "telemetry.sdk.language": true,
              "telemetry.sdk.name": true,
              "telemetry.sdk.version": true,
              "wlm": true
            },
            "includeByName": {},
            "indexByName": {
              "__name__": 0,
              "group": 1,
              "hostname": 2,
              "instance": 3,
              "job": 4,
              "job_id": 6,
              "job_name": 5,
              "nodelist": 7,
              "nodes_count": 8,
              "time_limit": 9,
              "user": 10
            },
            "renameByName": {
              "cluster": "Cluster",
              "job_id": "Job ID",
              "job_name": "Job Name",
              "node": "Node",
              "nodelist": "Nodes List",
              "nodes_count": "Nodes Count",
              "opid": "OPID",
              "run_time": "Run Time",
              "start_time": "Start Time",
              "state": "State",
              "submit_time": "Submit Time",
              "time_limit": "Run Time",
              "user": "User"
            }
          }
        },
        {
          "id": "groupBy",
          "options": {
            "fields": {
              "Cluster": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Job ID": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Job Name": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Nodes Count": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Nodes List": {
                "aggregations": [],
                "operation": "groupby"
              },
              "OPID": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Run Time": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Start Time": {
                "aggregations": [],
                "operation": "groupby"
              },
              "State": {
                "aggregations": [],
                "operation": "groupby"
              },
              "User": {
                "aggregations": [],
                "operation": "groupby"
              }
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Time"
            },
            "properties": []
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 77
      },
      "id": 21,
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 75,
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": false,
        "showThresholdMarkers": true,
        "sizing": "auto"
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "expr": "group by(job_id) (slurm_jobs{wlm=~\"$wlm\"})",
          "fullMetaSearch": false,
          "includeNullMetadata": true,
          "legendFormat": "{{label_name}}",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Active Jobs Count",
      "transformations": [
        {
          "id": "reduce",
          "options": {
            "reducers": [
              "first"
            ]
          }
        },
        {
          "id": "reduce",
          "options": {
            "reducers": [
              "sum"
            ]
          }
        }
      ],
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 77
      },
      "id": 22,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "editorMode": "code",
          "expr": "sum by(state) (slurm_jobs{wlm=~\"$wlm\"})",
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Active Jobs Count Over Time",
      "type": "timeseries"
    }
  ],
  "preload": false,
  "schemaVersion": 41,
  "tags": [],
  "templating": {
    "list": [
      {
        "current": {
          "text": "All",
          "value": "$__all"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_SLURM}"
        },
        "definition": "label_values(slurm_nodes, wlm)",
        "includeAll": true,
        "label": "Workload Manager",
        "name": "wlm",
        "options": [],
        "query": {
          "query": "label_values(slurm_nodes, wlm)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "sort": 1,
        "type": "query"
      },
      {
        "allowCustomValue": false,
        "current": {
          "text": "slurm_dashboard",
          "value": "dewrawgm6mkn4d"
        },
        "hide": 2,
        "label": "Slurm Data Source",
        "name": "DS_SLURM",
        "options": [],
        "query": "prometheus",
        "refresh": 1,
        "regex": "/^slurm/",
        "type": "datasource"
      }
    ]
  },
  "time": {
    "from": "now-5m",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "browser",
  "title": "Slurm Nodes & Jobs",
  "uid": "bdv6i9jduoe80f8",
  "version": 17
}
```
{{< /expand >}}

## Configure Data Sources in Grafana

1. Generate and copy an authentication token using the NetQ CLI. You can adjust time at which the token will expire with the `expiry` option. For example, the following command generates a token that expires after 40 days. If you do not set an `expiry` option, the token expires after 5 days. The maximum number of days allowed is 180.

```
nvidia@netq-server:~$ netq show vm-token expiry 40
```

2. Navigate to your Grafana dashboard. From the menu, select **Connections** and then **Data sources**. Select **Add new data source** and add the Prometheus TSDB:

{{<figure src="/images/netq/grafana-prom-415.png" alt="" width="1200">}}

3. Continue through the steps to configure the data source:

- In the *Name* field, enter the name of the data source. The name **must start with the data source name** and be written in lowercase (for example, `slurm_dashboard` or `kpi-dashboard`).
- In the *Connection* field, enter the IP address of your NetQ server followed by `/api/netq/vm/`, for example `https://10.255.255.255/api/netq/vm/`. In a cluster deployment, enter the virtual IP address in this field (followed by `/api/netq/vm/`). 
- In the *Authentication* section, select **Forward OAuth identity** from the dropdown menu. 
   - In *TLS settings*, select **Skip TLS certificate validation**.
   - In the *HTTP headers* section, select **Add header**. In the *Header* field, enter **Authorization**. In the *Value* field, enter the token that you generated in step one of this section.

{{<figure src="/images/netq/grafana-header-415.png" alt="" width="1000">}}

5. Select **Save & test**. If the operation was successful, you will begin to see metrics in your Grafana dashboard. 

### Import a Dashboard Template

To import a preconfigured dashboard into your Grafana instance:

1. From the side menu, select **Dashboards**.

2. Click **New** and select **Import** from the drop-down menu.

3. Paste the dashboard JSON text into the text area.

4. (Optional) Change the dashboard name, folder, or UID.

5. Click **Import**.
{{<notice tip>}}
If the dashboard does not display data, refresh your browser.
{{</notice>}}
### Grafana Best Practices

If data retrieval with Grafana is slow, you might need to adjust your dashboard settings. Fabric-wide queries on large networks (over 1000 switches) can generate millions of data points, which can significantly degrade performance. You can improve performance by optimizing queries, reducing data volume, and simplifying panel rendering.

Avoid plotting all time-series data at once. To visualize the data in different ways:
   - {{<exlink url="https://grafana.com/docs/grafana/latest/fundamentals/timeseries/#aggregating-time-series" text="Aggregate time-series data">}}
   - {{<exlink url="https://grafana.com/docs/grafana/latest/fundamentals/timeseries/#aggregating-time-series" text="Add labels to your time-series data">}}
   - {{<exlink url="https://grafana.com/docs/grafana/latest/dashboards/variables/add-template-variables/#add-an-interval-variable" text="Add interval variables">}}
   - {{<exlink url="https://grafana.com/docs/grafana/latest/dashboards/variables/add-template-variables/#add-an-interval-variable" text="Use aggregation operators">}} such as `count` and `topk`

{{<notice tip>}}
If Grafana displays "No Data", verify that all VMs in your cluster are operational. You can check the node status using the <code>kubectl get nodes</code> command. A node will show as <code>NotReady</code> if it is down. When the VM is restored, data collection will resume and will be displayed within 20 minutes of restoration.
{{</notice>}}

## Retrieve Metrics with the NetQ API

If you want to view or export the time-series database data without using Grafana, you can use curl commands to directly query the NetQ TSDB. These commands typically complete in fewer than 30 seconds, whereas Grafana can take longer to process and display data.

1. Generate an access token. Replace `<username>` and `<password>` with your NetQ username and password. Copy the access token generated by this command. You will use it in the next step. 
```
curl 'https://10.237.212.61/api/netq/auth/v1/login' -H 'content-type: application/json' --data-raw '{"username":"<username>","password":"<password>"}' --insecure 
```
 2. Generate a JSON Web Token (JWT). Replace `<access_token>` with the token generated from the previous step. Copy the resulting token generated by this command. You will use it in the next step. 
```
curl -k -X GET "https://10.237.212.61/api/netq/auth/v1/vm-access-token?expiryDays=10" -H "Authorization: Bearer <access_token>" 
```
 
3. Fetch a complete list of metrics. Replace `<vm-jwt>` with the token generated from the previous step. You can use this list to create queries based on metrics you're interested in.

```
export token=<vm-jwt> 
curl -k "https://10.237.212.61/api/netq/vm/api/v1/label/__name__/values" -H "Authorization: Bearer $token" 
```
 
{{< expand "Examples queries" >}}

The following example uses the VM query API to retrieve data related to `rx_errors`.

```
export token=<vm-jwt> 
curl -k "https://10.237.212.61/api/netq/vm/api/v1/query" -H "Authorization: Bearer $token" --get --data-urlencode 'query=rx_errors' 
```
 
This example is similar to the one above, but specifies a time range (`rx_errors` from the past 15 minutes):

```
export token=<vm-jwt>  
curl -k "https://10.237.212.61/api/netq/vm/api/v1/query_range" -H "Authorization: Bearer $token" --get --data-urlencode 'query= rx_errors' --data-urlencode "start=$(date -u -d '15 minutes ago' +%Y-%m-%dT%H:%M:%SZ)" --data-urlencode "end=$(date -u +%Y-%m-%dT%H:%M:%SZ)" --data-urlencode 'step=60s' 
```
{{< /expand >}}

## Additional Commands

- {{<link title="modify/#netq modify otlp endpoint" text="netq modify otlp endpoint">}}
- {{<link title="show/#netq show otlp" text="netq show otlp">}} commands



