---
title: Open Telemetry Export
author: NVIDIA
weight: 1232
toc: 3
---
Telemetry enables you to collect, send, and analyze large amounts of data, such as traffic statistics, port status, device health and configuration, and events. This data helps you monitor switch performance, health and behavior, traffic patterns, and <span class="a-tooltip">[QoS](## "Quality of Service")</span>.

## Configure Open Telemetry

Cumulus Linux supports {{<exlink url="https://github.com/open-telemetry/" text="open telemetry (OTEL)">}} export. You can use <span class="a-tooltip">[OTLP](## "open telemetry protocol")</span> to export metrics, such as interface counters, histogram collection, and platform statistic data to an external collector for analysis and visualization.

{{%notice note%}}
Cumulus Linux supports open telemetry export on switches with the Spectrum-2 ASIC and later.
{{%/notice%}}

To enable open telemetry:

```
cumulus@switch:~$ nv set system telemetry export otlp state enabled 
cumulus@switch:~$ nv config apply
```

You can enable open telemetry for [interface statistics](#interface-statistics), [histogram data](#histogram-data), [control plane statistics](#control-plane-statistics), and [platform statistics](#platform-statistics).

### Interface Statistics

When you enable open telemetry for interface statistics, the switch exports [counters](#interface-statistic-format) on all configured interfaces:

```
cumulus@switch:~$ nv set system telemetry interface-stats export state enabled
cumulus@switch:~$ nv config apply
```

You can enable additional interface statistic collection per interface for specific ingress buffer traffic classes (0 through 15) and egress buffer priority groups (0 through 7). When you enable these settings, the switch exports `interface_pg` and `interface_tc` counters for the defined priority groups and traffic classes:

```
cumulus@switch:~$ nv set system telemetry interface-stats ingress-buffer priority-group 4
cumulus@switch:~$ nv set system telemetry interface-stats egress-buffer traffic-class 12
cumulus@switch:~$ nv config apply
```

You can enable additional switch priority interface statistic collection on all configured interfaces for specific switch priority values:

```
cumulus@switch:~$ nv set system telemetry interface-stats switch-priority 4
cumulus@switch:~$ nv config apply
```

You can adjust the interface statistics sample interval (in seconds). You can specify a value between 1 and 86400. The default value is 1.

```
cumulus@switch:~$ nv set system telemetry interface-stats sample-interval 100
cumulus@switch:~$ nv config apply
```

### Control Plane Statistics

When you enable open telemetry for control plane statistics, additional counters for [control plane packets](#control-plane-statistic-format) are exported:

```
cumulus@switch:~$ nv set system telemetry control-plane-stats export state enabled
cumulus@switch:~$ nv config apply
```
You can adjust the control plane statistics sample interval (in seconds). You can specify a value between 1 and 86400. The default value is 1.

```
cumulus@switch:~$ nv set system telemetry control-plane-stats sample-interval 100
cumulus@switch:~$ nv config apply
```

### Histogram Data

When you enable open telemetry for histogram data, your buffer, counter, and latency {{<link url="ASIC-Monitoring#histogram-collection" text="histogram collection configuration">}} defines the data that the switch exports:

```
cumulus@switch:~$ nv set system telemetry histogram export state enabled
cumulus@switch:~$ nv config apply
```

### Platform Statistics

When you enable platform statistic open telemetry, data related to CPU, disk, filesystem, memory, and sensor health is exported. To enable all [platform statistics](#platform-statistic-format) globally:

```
cumulus@switch:~$ nv set system telemetry platform-stats export state enabled
cumulus@switch:~$ nv config apply
```

If you do not want to enable all platform statistics, you can enable or disable individual platform telemetry components or adjust the sample interval for individual components. The default sample interval is 60 seconds.

{{< tabs "TabID92 ">}}
{{< tab "CPU ">}}

```
cumulus@switch:~$ nv set system telemetry platform-stats class cpu state enabled
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv set system telemetry platform-stats class cpu sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Disk">}}

```
cumulus@switch:~$ nv set system telemetry platform-stats class disk state enabled
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv set system telemetry platform-stats class disk sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Filesystem">}}

```
cumulus@switch:~$ nv set system telemetry platform-stats class file-system state enabled
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv set system telemetry platform-stats class file-system sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Memory">}}

```
cumulus@switch:~$ nv set system telemetry platform-stats class memory state enabled
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv set system telemetry platform-stats class memory sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Environment sensors">}}

```
cumulus@switch:~$ nv set system telemetry platform-stats class environment-sensors state enabled
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv set system telemetry platform-stats class environment-sensors sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

### gRPC OTLP Export

To configure the open telemetry export destination:

1. Configure gRPC to communicate with the collector by providing the collector destination IP address or hostname. Specify the port to use for communication if it is different from the default port 8443:

   ```
   cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.100 port 4317
   cumulus@switch:~$ nv config apply
   ```

2. Configure an X.509 certificate to secure the gRPC connection:

   ```
   cumulus@switch:~$ nv set system telemetry export otlp grpc cert-id <ca-certificate>
   cumulus@switch:~$ nv config apply
   ```

By default, OTLP export is in **secure** mode that requires a CA certificate. For connections without a configured certificate, you must enable `insecure` mode with the `nv set system telemetry export otlp grpc insecure enabled` command.

### Show Telemetry Export Configuration

To show the telemetry export configuration, run the `nv show system telemetry export` command:

```
cumulus@switch:~$ nv show system telemetry export
                    applied   pending 
------------------  --------  --------
vrf                 default   default 
otlp                                  
  state             disabled  disabled
  grpc                                
    insecure  disabled  disabled
    port            8443      8443    
    [destination]             
```

To show the OTLP gRPC destination configuration, run the `nv show system telemetry export otlp grpc destination` command.

### Static Labels

You can apply static labels to switches and individual interfaces to configure descriptions for devices and interface roles. Exported OTLP data includes these label names and descriptions.

{{%notice note%}}
- Cumulus Linux supports up to 10 device labels and up to 10 interface labels.
- Label name and description strings can include alphanumeric characters with underscores, periods, or dashes. If spaces are included in the string, wrap the entire string inside double or single quotes.
{{%/notice%}}

To configure a switch device label `Data_Center_Location` and a string identifying it as part of `Data_Center_B`:

```
cumulus@switch:~$ nv set system telemetry label "Data Center Location" description "Data Center B"
cumulus@switch:~$ nv config apply
```

Validate device label configuration with the `nv show system telemetry label` command:

```
cumulus@switch:~$ nv show system telemetry label
                      description  
--------------------  -------------
Data Center Location  Data Center B
```

To configure a switch interface label `interface_swp10_label` with the description `Server 10 connection`:

```
cumulus@switch:~$ nv set interface swp10 telemetry label "interface_swp10_label" description "Server 10 connection"
cumulus@switch:~$ nv config apply
```

Validate the configuration with the `nv show system telemetry label` command:

```
cumulus@switch:~$ nv show system telemetry label
                      description  
--------------------  -------------
Data Center Location  Data Center B
```

Validate interface label configuration with the `nv show interface <interface> telemetry label` command:

```
cumulus@switch:~$ nv show interface swp10 telemetry label
                       description         
---------------------  --------------------
interface_swp10_label  Server 10 connection
```

## Telemetry Data Format

Cumulus Linux exports statistics and histogram data in the formats defined in this section.

### Interface Statistic Format

The interface statistic data samples that the switch exports to the OTEL collector are {{<exlink url="https://opentelemetry.io/docs/specs/otel/metrics/data-model/#gauge" text="gauge streams">}} that include the interface name as an attribute and the statistics value reported in the asDouble {{<exlink url="https://opentelemetry.io/docs/specs/otel/metrics/data-model/#exemplars" text="exemplar">}}.

{{< tabs "TabID249 ">}}
{{< tab "Interface Statistics ">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_oper_state` | Interface operational state as a bitmap: (None[0], Up[1], Down[2], Invalid[4], Error[8]) |
| `nvswitch_interface_dot3_control_in_unknown_opcodes` | Input 802.3 unknown opcode counter. |
| `nvswitch_interface_dot3_in_pause_frames` | Input 802.3 pause frame counter. |
| `nvswitch_interface_dot3_out_pause_frames` | Output 802.3 pause frame counter. |
| `nvswitch_interface_dot3_stats_alignment_errors` | 802.3 alignment error counter. |
| `nvswitch_interface_dot3_stats_carrier_sense_errors` | 802.3 interface carrier sense error counter. |
| `nvswitch_interface_dot3_stats_deferred_transmissions` | 802.3 deferred transmission counter. |
| `nvswitch_interface_dot3_stats_excessive_collisions` | 802.3 excessive collisions counter. |
| `nvswitch_interface_dot3_stats_fcs_errors` | 802.3 FCS error counter. |
| `nvswitch_interface_dot3_stats_frame_too_longs` | 802.3 excessive frame size counter. |
| `nvswitch_interface_dot3_stats_internal_mac_receive_errors` | 802.3 internal MAC receive error counter. |
| `nvswitch_interface_dot3_stats_internal_mac_transmit_errors` | 802.3 internal MAC transmit error counter. |
| `nvswitch_interface_dot3_stats_late_collisions` | 802.3 late collisions counter. |
| `nvswitch_interface_dot3_stats_multiple_collision_frames` | 802.3 multiple collision frames counter. |
| `nvswitch_interface_dot3_stats_single_collision_frames` | 802.3 single collision frames counter. |
| `nvswitch_interface_dot3_stats_sqe_test_errors` | 802.3 SQE test error counter. |
| `nvswitch_interface_dot3_stats_symbol_errors` | 802.3 symbol error counter. |
| `nvswitch_interface_performance_marked_packets` | Interface performance marked packets, with marking as `ece` or `ecn`. |
| `nvswitch_interface_discards_ingress_general` | Interface ingress general discards counter. |
| `nvswitch_interface_discards_ingress_policy_engine` | Interface ingress policy engine discards counter. |
| `nvswitch_interface_discards_ingress_vlan_membership` | Interface ingress VLAN membership filter discards counter. |
| `nvswitch_interface_discards_ingress_tag_frame_type` | Interface ingress VLAN tag filter discards counter. |
| `nvswitch_interface_discards_egress_vlan_membership` | Interface egress VLAN emmbership filter discards counter. |
| `nvswitch_interface_discards_loopback_filter` | Interface loopback filter discards counter. |
| `nvswitch_interface_discards_egress_general` | Interface egress general discards counter. |
| `nvswitch_interface_discards_egress_link_down` | Interface egress link down discards counter. |
| `nvswitch_interface_discards_egress_hoq` | Interface egress head-of-queue timeout discards. |
| `nvswitch_interface_discards_port_isolation` | Interface port isolation filter discards. |
| `nvswitch_interface_discards_egress_policy_engine` | Interface egress policy engine discards. |
| `nvswitch_interface_discards_ingress_tx_link_down` | Interface ingress transmit link down discards. |
| `nvswitch_interface_discards_egress_stp_filter` | Interface egress spanning tree filter discards. | 
| `nvswitch_interface_discards_egress_hoq_stall` | Interface egress head-of-queue stall discards.|
| `nvswitch_interface_discards_egress_sll` | Interface egress switch lifetime limit discards. |
| `nvswitch_interface_discards_ingress_discard_all` | Interface total ingress discards.| 
| `nvswitch_interface_tx_stats_pkts64octets` | Total packets transmitted, 64 octets in length. |  
| `nvswitch_interface_tx_stats_pkts65-to127octets` | Total packets transmitted, 64 octets in length. |	 
| `nvswitch_interface_tx_stats_pkts256-to511octets` | Total packets transmitted, 256-511 octets in length. |  
| `nvswitch_interface_tx_stats_pkts512-to1023octets` | Total packets transmitted, 512-1023 octets in length. |  
| `nvswitch_interface_tx_stats_pkts1024-to1518octets` | Total packets transmitted, 1024-1518 octets in length. |  
| `nvswitch_interface_tx_stats_pkts1519-to2047octets` | Total packets transmitted, 1519-2047 octets in length. |  
| `nvswitch_interface_tx_stats_pkts2048-to4095octets` | Total packets transmitted, 2048-4095 octets in length. |  
| `nvswitch_interface_tx_stats_pkts4096-to8191octets` | Total packets transmitted, 4096-8191 octets in length. |  
| `nvswitch_interface_tx_stats_pkts8192-to10239octets` | Total packets transmitted, 8192-10239 octets in length. |  
| `nvswitch_interface_ether_stats_pkts64octets` | Total packets received, 64 octets in length. |  
| `nvswitch_interface_ether_stats_pkts65to127octets` | Total packets received, 65-127 octets in length. |  
| `nvswitch_interface_ether_stats_pkts128to255octets` | Total packets received, 128-255 octets in length. |  
| `nvswitch_interface_ether_stats_pkts256to511octets` | Total packets received, 256-511 octets in length. |  
| `nvswitch_interface_ether_stats_pkts512to1023octets` | Total packets received, 512-1023 octets in length. |  
| `nvswitch_interface_ether_stats_pkts1024to1518octets` | Total packets received, 1024-1518 octets in length. |  
| `nvswitch_interface_ether_stats_pkts1519to2047octets` | Total packets received, 1519-2047 octets in length. |  
| `nvswitch_interface_ether_stats_pkts2048to4095octets` | Total packets received, 2048-4095 octets in length. |  
| `nvswitch_interface_ether_stats_pkts4096to8191octets` | Total packets received, 4096-8191 octets in length. |  
| `nvswitch_interface_ether_stats_pkts8192to10239octets` | Total packets received, 8192-10239 octets in length. |
| `nvswitch_interface_carrier_up_changes_total` | Total number of carrier up transitions for the interface. |
| `nvswitch_interface_carrier_last_change_time_ms` | Time of last carrier change for the interface as Unix epoch timestamp, with millisecond granularity. |
| `nvswitch_interface_carrier_down_changes_total` | Total number of carrier down transitions for the interface. |
| `nvswitch_interface_carrier_changes_total` | Total number of carrier changes for the interface. |
| `nvswitch_interface_mtu_bytes` | Operational MTU for the interface in bytes. |
| `nvswitch_interface_info` | Provides information about the interface: MAC address, duplex, ifalias, interface name, operstate. |
| `nvswitch_interface_iface_id` | The ifindex for the interface. |
| `nvswitch_interface_flags` | Kernel device flags set for an interface as an integer representing the {{<exlink url="https://github.com/torvalds/linux/blob/c1e939a21eb111a6d6067b38e8e04b8809b64c4e/include/uapi/linux/if.h#L43" text="kernel `net_device` flags bitmask">}}. |
| `nvswitch_interface_proto_down` | Interface protocol down status. |

{{< /tab >}}
{{< tab "Traffic Class ">}}

The following additional interface traffic class statistics are collected and exported when you configure the `nv set system telemetry interface-stats egress-buffer traffic-class <class>` command:

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_tc_tx_bc_frames` | Interface egress traffic class transmit broadcast frames counter. |
| `nvswitch_interface_tc_tx_ecn_marked_tc` | Interface egress traffic class transmit ECN marked counter. |
| `nvswitch_interface_tc_tx_frames` | Interface egress traffic class trasmit frames counter. |
| `nvswitch_interface_tc_tx_mc_frames` | Interface egress traffic class trasmit multicast frames counter. |
| `nvswitch_interface_tc_tx_no_buffer_discard_uc` | Interface egress traffic class transmit unicast no buffer discard counter. |
| `nvswitch_interface_tc_tx_octet` | Interface egress traffic class transmit bytes counter.|
| `nvswitch_interface_tc_tx_queue` | Interface egress traffic class transmit queue counter. |
| `nvswitch_interface_tc_tx_uc_frames` | Interface egress traffic class transmit unicast frames counter. |
| `nvswitch_interface_tc_tx_wred_discard` | Interface egress traffic class transmit WRED discard counter. |

{{< /tab >}}
{{< tab "Priority Group ">}}

The following additional interface priority group statistics are collected and exported when you configure the `nv set system telemetry interface-stats ingress-buffer priority-group <priority>` command:

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_pg_rx_buffer_discard` | Interace ingress priority group receive buffer discard counter. |
| `nvswitch_interface_pg_rx_frames` | Interface ingress priority group receive frames counter.|
| `nvswitch_interface_pg_rx_octet` | Interface ingress priority group receive bytes counter. |
| `nvswitch_interface_pg_rx_shared_buffer_discard` | Interface ingress priority group receive shared buffer discard counter. |
| `nvswitch_interface_pg_rx_uc_frames` | Interface receive priority group unicast frames counter. |
| `nvswitch_interface_pg_rx_mc_frames` | Interface receive priority group multicast frames counter. |
| `nvswitch_interface_pg_rx_bc_frames` | Interface receive priority group broadcast frames counter. |	 	 
| `nvswitch_interface_pg_tx_octets` | Interface receive priority group transmit bytes counter. |
| `nvswitch_interface_pg_tx_uc_frames` | Interface receive priority group transmit unicast frames counter. |	 
| `nvswitch_interface_pg_tx_mc_frames` | Interface receive priority group transmit multicast frames counter. |	 
| `nvswitch_interface_pg_tx_bc_frames` | Interface receive priority group transmit broadcast frames counter. |	 
| `nvswitch_interface_pg_tx_frames` | Interface receive priority group transmit frames counter. | 
| `nvswitch_interface_pg_rx_pause` | Interface receive priority group receive pause counter. | 
| `nvswitch_interface_pg_rx_pause_duration` | Interface receive priority group receive pause duration counter. |	 
| `nvswitch_interface_pg_tx_pause` | Interface receive priority group transmit pause counter. |
| `nvswitch_interface_pg_tx_pause_duration` | Interface receive priority group transmit pause duration counter. |	
| `nvswitch_interface_pg_rx_pause_transition` | Interface receive priority group receive pause transition counter. |	 
| `nvswitch_interface_pg_rx_discard` | Interface receive priority group receive discard counter. |

{{< /tab >}}
{{< tab "Switch Priority ">}}

The following additional interface switch priority statistics are collected and exported when you configure the `nv set system telemetry interfaces-stats switch-priority <priority>` command:

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_sp_rx_bc_frames` | Received broadcast counter for the switch priority |
| `nvswitch_interface_sp_rx_discard` | Receive discard counter for the switch priority |
| `nvswitch_interface_sp_rx_frames` | Receive frame counter for the switch priority. |
| `nvswitch_interface_sp_rx_mc_frames` | Receive multicast frame counter for the switch priority. |
| `nvswitch_interface_sp_rx_octets` | Receive octets counter for the switch priority. |
| `nvswitch_interface_sp_rx_pause` | Receive pause counter for the switch priority. |
| `nvswitch_interface_sp_rx_pause_duration` | Recieve pause duration counter for the switch priority. |
| `nvswitch_interface_sp_rx_pause_transition` | Recieve pause transition counter for the switch priority. |
| `nvswitch_interface_sp_rx_uc_frames` | Receive unicast frame counter for the switch priority. |
| `nvswitch_interface_sp_tx_bc_frames` | Transmit broadcast frame counter for the switch priority. |
| `nvswitch_interface_sp_tx_frames` | Transmit frame counter for the switch priority. |
| `nvswitch_interface_sp_tx_mc_frames` | Transmit multicast frame counter for the switch priority. |
| `nvswitch_interface_sp_tx_octets` | Transmit octets counter for the switch priority. |
| `nvswitch_interface_sp_tx_pause` | Transmit pause counter for the switch priority. |
| `nvswitch_interface_sp_tx_pause_duration` | Transmit pause duration for the switch priority. |
| `nvswitch_interface_sp_tx_uc_frames` | Transmit unicast frame counter for the switch priority. |

{{< /tab >}}
{{< /tabs >}}

{{< expand "Example JSON data for interface_oper_state:" >}}
```
            {
              "name": "nvswitch_interface_oper_state",
              "description": "NVIDIA Ethernet Switch Interface operational state",
              "gauge": {
                "dataPoints": [
                  {
                     "attributes": [
                      {
                        "key": "interface",
                        "value": {
                          "stringValue": "swp61s0"
                        }
                      }
                    ],
                    "timeUnixNano": "1722458198491000000",
                    "asDouble": 1
                  },
                  {
                    "attributes": [
                      {
                        "key": "interface",
                        "value": {
                          "stringValue": "swp1"
                        }
                      }
                    ],
                    "timeUnixNano": "1722458198491000000",
                    "asDouble": 2
                  }
                ]
              },
```

{{< /expand >}}
<br>
{{< expand "Example JSON data for interface_dot3_stats_fcs_errors:" >}}
```
            {
              "name": "nvswitch_interface_dot3_stats_fcs_errors",
              "description": "NVIDIA Ethernet Switch Interface dot3 stats fcs errors counter",
              "gauge": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "interface",
                        "value": {
                          "stringValue": "swp1"
                        }
                      }
                    ],
                    "timeUnixNano": "1722458205491000000",
                    "asDouble": 0
                  }
                ]
              },
```

{{< /expand >}}

### Control Plane Statistic Format

When you enable control plane statistic telemetry, the following statistics are exported:

| Name | Description |
|----- | ----------- |
| `nvswitch_control_plane_tx_packets` | Control plane transmit packets. |
| `nvswitch_control_plane_tx_bytes` | Control plane transmit bytes. |
| `nvswitch_control_plane_rx_packets` | Control plane receive packets. |
| `nvswitch_control_plane_rx_bytes` | Control plane receive bytes. |
| `nvswitch_control_plane_rx_buffer_drops` | Control plane receive buffer drops. |
| `nvswitch_control_plane_trap_rx_packets` | Control plane trap group receive packets. |
| `nvswitch_control_plane_trap_rx_event_count`| Control plane trap group receive events. |
| `nvswitch_control_plane_trap_rx_drop` | Control plane trap group receive drops. |
| `nvswitch_control_plane_trap_rx_bytes` | Control plane trap group receive bytes. |
| `nvswitch_control_plane_trap_group_rx_packets` | Control plane trap group receive packets. |
| `nvswitch_control_plane_trap_group_rx_bytes` | Control plane trap group receive bytes. |
| `nvswitch_control_plane_trap_group_pkt_violations` | Control plane trap group packet violations. |

{{< expand "Example JSON data for nvswitch_control_plane_trap_rx_drop:" >}}
```
            {
              "name": "nvswitch_control_plane_trap_rx_drop",
              "description": "NVIDIA Ethernet Switch trap t_drops counter",
              "sum": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "group",
                        "value": {
                          "stringValue": "25"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1729836350747000000",
                    "timeUnixNano": "1729839232747000000",
                    "asDouble": 0
                  },
                  {
                    "attributes": [
                      {
                        "key": "group",
                        "value": {
                          "stringValue": "3"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1729836350747000000",
                    "timeUnixNano": "1729839232747000000",
                    "asDouble": 0
                  },
                  {
                    "attributes": [
                      {
                        "key": "group",
                        "value": {
                          "stringValue": "5"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1729836350747000000",
                    "timeUnixNano": "1729839232747000000",
                    "asDouble": 0
                  },
                  {
                    "attributes": [
                      {
                        "key": "group",
                        "value": {
                          "stringValue": "53"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1729836350747000000",
                    "timeUnixNano": "1729839232747000000",
                    "asDouble": 0
                  },
                  {
                    "attributes": [
                      {
                        "key": "group",
                        "value": {
                          "stringValue": "78"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1729836350747000000",
                    "timeUnixNano": "1729839232747000000",
                    "asDouble": 1
                  },
                  {
                    "attributes": [
                      {
                        "key": "group",
                        "value": {
                          "stringValue": "80"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1729836350747000000",
                    "timeUnixNano": "1729839232747000000",
                    "asDouble": 1
                  }
                ],
                "aggregationTemporality": 2,
                "isMonotonic": true
              },
              "metadata": [
                {
                  "key": "prometheus.type",
                  "value": {
                    "stringValue": "counter"
                  }
                }
              ]
            }
```

{{< /expand >}}

### Platform Statistic Format

When you enable platform statistic telemetry globally, or when you enable telemetry for the individual components, the following statistics are exported:

{{< tabs "TabID201 ">}}
{{< tab "CPU ">}}

CPU statistics include the CPU core number and operation mode (user, system, idle, iowait, irq, softirq, steal, guest, guest_nice).

| Name | Description |
|----- | ----------- |
| `node_cpu_core_throttles_total` | Number of times a CPU core has been throttled. |
| `node_cpu_frequency_max_hertz` | Maxiumum CPU thread frequency in hertz. |
| `node_cpu_frequency_min_hertz` | Minimum CPU thread frequency in hertz. |
| `node_cpu_guest_seconds_total` | Seconds the CPUs spent in guests for each mode. |
| `node_cpu_package_throttles_total` | Number of times the CPU package has been throttled. |
| `node_cpu_scaling_frequency_hertz` | Current scaled CPU thread frequency in hertz. |  
| `node_cpu_scaling_frequency_max_hertz` | Maximum scaled CPU thread frequency in hertz. |  
| `node_cpu_scaling_frequency_min_hertz` | Minimum scaled CPU thread frequency in hertz. | 
| `node_cpu_seconds_total` | Seconds the CPU spent in each mode. | 

{{< /tab >}}
{{< tab "Disk ">}}

| Name | Description |
|----- | ----------- |
| `node_disk_ata_rotation_rate_rpm` | ATA disk rotate rate in RPMs. (0 for SSDs). |
| `node_disk_ata_write_cache` | ATA disk write cache presence. |
| `node_disk_ata_write_cache_enabled` | ATA disk write cache status (enabled or disabled). | 
| `node_disk_discard_time_seconds_total` | Total number of seconds spent by all discards. |  
| `node_disk_discarded_sectors_total` | Total number of sectors discarded successfully. |  
| `node_disk_discards_completed_total` | Total number of discards discards completed. |  
| `node_disk_discards_merged_total` |  Total number of discards merged. |  
| `node_disk_flush_requests_time_seconds_total` | Total number of seconds spent by all flush requests. |  
| `node_disk_flush_requests_total` | The total number of flush requests completed successfully. |  
| `node_disk_info` | Disk information from `/sys/block/<block_device>`. |  
| `node_disk_io_now` | Number of I/Os in progress. |  
| `node_disk_io_time_seconds_total` | Total seconds spent during I/O. |  
| `node_disk_io_time_weighted_seconds_total` | Weighted number of seconds spent during I/O. |  
| `node_disk_read_bytes_total` | Total number of bytes read successfully. |  
| `node_disk_read_time_seconds_total` | Total number of seconds spent by all reads. |  
| `node_disk_reads_completed_total` | Total number of reads completed successfully. |  
| `node_disk_reads_merged_total` | Total number of reads merged. |  
| `node_disk_write_time_seconds_total` | Total number of seconds spent by all writes. |  
| `node_disk_writes_completed_total` | Total number of writes completed successfully. |  
| `node_disk_writes_merged_total` | Number of writes merged. |  
| `node_disk_written_bytes_total` | Total number of bytes written successfully. |  

{{< /tab >}}
{{< tab "Filesystem ">}}

| Name | Description |
|----- | ----------- |
| `node_filesystem_avail_bytes` | Filesystem space available to non-root users in bytes.|
| `node_filesystem_device_error` | Whether an error occurred while getting statistics for the given device. |
| `node_filesystem_files` | Filesystem total file nodes.| 
| `node_filesystem_files_free` | Filesystem total free file nodes. |  
| `node_filesystem_free_bytes` | Filesystem free space in bytes. |  
| `node_filesystem_readonly` | Filesystem read-only status. |  
| `node_filesystem_size_bytes` |  Filesystem size in bytes. |  

{{< /tab >}}
{{< tab "Memory ">}}

| Name | Description |
|----- | ----------- |
| `node_memory_Active_anon_bytes` | `/proc/meminfo` Active_anon bytes. |
| `node_memory_Active_bytes` | `/proc/meminfo` Active bytes. |  
| `node_memory_Active_file_bytes` | `/proc/meminfo` Active_file bytes. |  
| `node_memory_AnonHugePages_bytes` | `/proc/meminfo` AnonHugePages bytes. |
| `node_memory_AnonPages_bytes` | `/proc/meminfo` AnonPages bytes. |  
| `node_memory_Bounce_bytes` | `/proc/meminfo` Bounce bytes. |  
| `node_memory_Buffers_bytes`  `/proc/meminfo` Buffers bytes. | |  
| `node_memory_Cached_bytes` | `/proc/meminfo` Cached bytes. |  
| `node_memory_CommitLimit_bytes` | `/proc/meminfo` CommitLimit bytes. |  
| `node_memory_Committed_AS_bytes` | `/proc/meminfo` Committed_AS bytes. |  
| `node_memory_DirectMap1G_bytes` | `/proc/meminfo` DirectMap1G bytes. |  
| `node_memory_DirectMap2M_bytes` | `/proc/meminfo` DirectMap2M bytes. |  
| `node_memory_DirectMap4k_bytes` | `/proc/meminfo` DirectMap4k bytes. |  
| `node_memory_Dirty_bytes` | `/proc/meminfo` Dirty bytes. |  
| `node_memory_FileHugePages_bytes` | `/proc/meminfo` FileHugePages bytes. |  
| `node_memory_FilePmdMapped_bytes` | `/proc/meminfo` FilePmdMapped bytes. |  
| `node_memory_HardwareCorrupted_bytes` | `/proc/meminfo` HardwareCorrupted bytes. |  
| `node_memory_HugePages_Free` | `/proc/meminfo` HugePages_Free. |  
| `node_memory_HugePages_Rsvd` | `/proc/meminfo` HugePages_Rsvd. |  
| `node_memory_HugePages_Surp` | `/proc/meminfo` HugePages_Surp. |  
| `node_memory_HugePages_Total` | `/proc/meminfo` HugePages_Total.|  
| `node_memory_Hugepagesize_bytes` | `/proc/meminfo` Hugepagesize bytes. |  
| `node_memory_Hugetlb_bytes` | `/proc/meminfo` Hugetlb bytes. |  
| `node_memory_Inactive_anon_bytes` | `/proc/meminfo` Inactive_anon bytes. |  
| `node_memory_Inactive_bytes` | `/proc/meminfo` Inactive bytes. |  
| `node_memory_Inactive_file_bytes` | `/proc/meminfo` Inactive_file bytes. |  
| `node_memory_KReclaimable_bytes` | `/proc/meminfo` KReclaimable bytes. |  
| `node_memory_KernelStack_bytes` | `/proc/meminfo` KernelStack bytes. |  
| `node_memory_Mapped_bytes` | `/proc/meminfo` Mapped bytes. |  
| `node_memory_MemAvailable_bytes` | `/proc/meminfo` MemAvailable bytes. |  
| `node_memory_MemFree_bytes` | `/proc/meminfo` MemFree bytes. |  
| `node_memory_MemTotal_bytes` | `/proc/meminfo` MemTotal bytes. |  
| `node_memory_Mlocked_bytes` | `/proc/meminfo` Mlocked bytes. |  
| `node_memory_NFS_Unstable_bytes` | `/proc/meminfo` NFS_Unstable bytes. |  
| `node_memory_PageTables_bytes` | `/proc/meminfo` PageTables bytes. |  
| `node_memory_Percpu_bytes` | `/proc/meminfo` Percpu bytes. |  
| `node_memory_SReclaimable_bytes` | `/proc/meminfo` SReclaimable bytes. |  
| `node_memory_SUnreclaim_bytes` | `/proc/meminfo` SUnreclaim bytes. |  
| `node_memory_SecPageTables_bytes` | `/proc/meminfo` SecPageTables bytes. |  
| `node_memory_ShmemHugePages_bytes` | `/proc/meminfo` ShmemHugePages bytes. |  
| `node_memory_ShmemPmdMapped_bytes` | `/proc/meminfo` ShmemPmdMapped bytes. |  
| `node_memory_Shmem_bytes` | `/proc/meminfo` Shmem bytes. |  
| `node_memory_Slab_bytes` | `/proc/meminfo` Slab bytes. |  
| `node_memory_SwapCached_bytes` | `/proc/meminfo` SwapCached bytes. |  
| `node_memory_SwapFree_bytes` | `/proc/meminfo` SwapFree bytes. |  
| `node_memory_SwapTotal_bytes` | `/proc/meminfo` SwapTotal bytes. |  
| `node_memory_Unevictable_bytes` | `/proc/meminfo` Unevictable bytes. |  
| `node_memory_VmallocChunk_bytes` | `/proc/meminfo` VmallocChunk bytes. |  
| `node_memory_VmallocTotal_bytes` | `/proc/meminfo` VmallocTotal bytes. |  
| `node_memory_VmallocUsed_bytes` | `/proc/meminfo` VmallocUsed bytes. |  
| `node_memory_WritebackTmp_bytes` | `/proc/meminfo` WritebackTmp bytes. |  
| `node_memory_Writeback_bytes` | `/proc/meminfo` Writeback bytes. |  
| `node_memory_Zswap_bytes` | `/proc/meminfo` Zswap bytes. |  
| `node_memory_Zswapped_bytes` | `/proc/meminfo` Zswapped bytes. |

{{< /tab >}}
{{< tab "Environment Sensors ">}}

| Name | Description |
|----- | ----------- |
| `nvswitch_env_fan_cur_speed` | Current fan speed in RPM. |  
| `nvswitch_env_fan_dir` | Fan direction (0: Front2Back, 1: Back2Front). | 
| `nvswitch_env_fan_max_speed` | Fan maximum speed in RPM. | 
| `nvswitch_env_fan_min_speed` | Fan minimum speed in RPM. |  
| `nvswitch_env_fan_state` | Fan status (0: ABSENT, 1: OK, 2: FAILED, 3: BAD). | 
| `nvswitch_env_psu_capacity` | PSU capacity in watts. | 
| `nvswitch_env_psu_current` | PSU current in amperes. | 
| `nvswitch_env_psu_power` | PSU power in watts. | 
| `nvswitch_env_psu_state` | PSU state (0: ABSENT, 1: OK, 2: FAILED, 3: BAD). | 
| `nvswitch_env_psu_voltage` | PSU voltage in volts. | 
| `nvswitch_env_temp_crit` | Critical temperature threshold in centigrade. | 
| `nvswitch_env_temp_current` | Current temperature in centigrade. | 
| `nvswitch_env_temp_max` | Maximum temperature threshold in centigrade. | 
| `nvswitch_env_temp_min` | Minimum temperature threshold in centigrade. | 
| `nvswitch_env_temp_state` | Temperature sensor status (0: ABSENT, 1: OK, 2: FAILED, 3: BAD). | 

{{< /tab >}}
{{< /tabs >}}

{{< expand "Example JSON data for PSU and temperature sensor telemetry:" >}}

            {
              "name": "nvswitch_platform_environment_psu_state",
              "description": "PSU state. 0:ABSENT 1:OK 2:FAILED 3:BAD",
              "gauge": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "Power Supply Unit 1"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "PSU1"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 1
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "Power Supply Unit 2"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "PSU2"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 3
                  }
                        "value": {
                          "stringValue": "Power Supply Unit 1"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "PSU1"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 1
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "Power Supply Unit 2"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "PSU2"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 3
                  }
                ]
              },
              "metadata": [
                {
                  "key": "prometheus.type",
                  "value": {
                    "stringValue": "gauge"
                  }
                }
              ]
            },
            {
              "name": "nvswitch_platform_environment_temp_crit",
              "description": "Critical temperature in Centigrade.",
              "gauge": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "Asic Temp Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp4"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 120
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 0"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp5"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 100
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 1"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp6"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 100
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 2"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp7"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 100
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 3"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp8"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 100
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 4"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp9"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 100
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 5"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp10"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 100
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Package Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp1"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 100
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "Main Board Ambient Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp3"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 85
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "PSU1 Temp Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "PSU1Temp1"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 85
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "PSU2 Temp Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "PSU2Temp1"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 0
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "Port Ambient Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp2"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 85
                  }
                ]
              },
              "metadata": [
                {
                  "key": "prometheus.type",
                  "value": {
                    "stringValue": "gauge"
                  }
                }
              ]
            },
            {
              "name": "nvswitch_platform_environment_temp_current",
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "Port Ambient Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp2"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 85
                  }
                ]
              },
              "metadata": [
                {
                  "key": "prometheus.type",
                  "value": {
                    "stringValue": "gauge"
                  }
                }
              ]
            },
            {
              "name": "nvswitch_platform_environment_temp_current",
              "description": "Current temperature in Centigrade.",
              "gauge": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "Asic Temp Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp4"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 50
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 0"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp5"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 52
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 1"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp6"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 69
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 2"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp7"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 55
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 3"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp8"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 54
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 4"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp9"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 52
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Core Sensor 5"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp10"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 52
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "CPU Package Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp1"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 69
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "Main Board Ambient Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp3"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 24.687
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "PSU1 Temp Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "PSU1Temp1"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 24.531
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "PSU2 Temp Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "PSU2Temp1"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 0
                  },
                  {
                    "attributes": [
                      {
                        "key": "description",
                        "value": {
                          "stringValue": "Port Ambient Sensor"
                        }
                      },
                      {
                        "key": "name",
                        "value": {
                          "stringValue": "Temp2"
                        }
                      }
                    ],
                    "timeUnixNano": "1729113543218000000",
                    "asDouble": 22.312
                  }
                ]
              },
              "metadata": [
                {
                  "key": "prometheus.type",
                  "value": {
                    "stringValue": "gauge"
                  }
                }
              ]
            },

{{< /expand >}}

### Histogram Data Format

The histogram data samples that the switch exports to the OTEL collector are {{<exlink url="https://opentelemetry.io/docs/specs/otel/metrics/data-model/#histogram" text="histogram data points">}} that include the {{<link url="ASIC-Monitoring#histogram-collection-example" text="histogram bucket (bin)">}} counts and the respective queue length size boundaries for each bucket. Latency and counter histogram data are also exported, if configured. 

{{% notice note %}}
Latency histogram bucket counts do not increment in exported telemetry data if there are no packets transmitted in the traffic class during the sample interval.
{{% /notice %}} 

The switch sends a sample with the following names for each interface enabled for ingress and egress buffer, latency, and/or counter histogram collection:

| Name | Description |
|----- | ----------- |
| `nvswitch_histogram_interface_egress_buffer` | Histogram interface egress buffer queue depth. |
| `nvswitch_histogram_interface_ingress_buffer` | Histogram interface ingress buffer queue depth. |
| `nvswitch_histogram_interface_counter` | Histogram interface counter data. |
| `nvswitch_histogram_interface_latency` | Histogram interface latency data. |

{{< expand "Example JSON data for interface_ingress_buffer:" >}}
```
            {
              "name": "nvswitch_histogram_interface_ingress_buffer",
              "description": "NVIDIA Ethernet Switch Histogram Interface Ingress Buffer Queue Depth",
              "unit": "bytes",
              "histogram": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "interface",
                        "value": {
                          "stringValue": "swp1s1"
                        }
                      },
                      {
                        "key": "pg",
                        "value": {
                          "intValue": "0"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1729839231624809212",
                    "timeUnixNano": "1729839231628434909",
                    "count": "1019165",
                    "bucketCounts": [
                      "1019165",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0"
                    ],
                    "explicitBounds": [
                      863,
                      295775,
                      590687,
                      885599,
                      1180511,
                      1475423,
                      1770335,
                      2065247,
                      2360159
                    ]
                  },
```

{{< /expand >}}
<br>
{{< expand "Example JSON data for interface_egress_buffer:" >}}
```
{
              "name": "nvswitch_histogram_interface_egress_buffer",
              "description": "NVIDIA Ethernet Switch Histogram Interface Egress Buffer Queue Depth",
              "unit": "bytes",
              "histogram": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "interface",
                        "value": {
                          "stringValue": "swp1s1"
                        }
                      },
                      {
                        "key": "tc",
                        "value": {
                          "intValue": "0"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1729839232707032279",
                    "timeUnixNano": "1729839232709312158",
                    "count": "1077334",
                    "bucketCounts": [
                      "1077334",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0"
                    ],
                    "explicitBounds": [
                      863,
                      1180511,
                      2360159,
                      3539807,
                      4719455,
                      5899103,
                      7078751,
                      8258399,
                      9438047
                    ]
                  }
```

{{< /expand >}}
<br>
{{< expand "Example JSON data for interface_counter:" >}}
```
            {
              "name": "nvswitch_histogram_interface_counter",
              "description": "NVIDIA Ethernet Switch Histogram Interface Counter",
              "unit": "counter",
              "histogram": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "interface",
                        "value": {
                          "stringValue": "swp1s1"
                        }
                      },
                      {
                        "key": "type",
                        "value": {
                          "stringValue": "crc"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1729839235935525147",
                    "timeUnixNano": "1729839235937099838",
                    "count": "1033926",
                    "bucketCounts": [
                      "1033926",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0"
                    ],
                    "explicitBounds": [
                      99999,
                      1337499,
                      2574999,
                      3812499,
                      5049999,
                      6287499,
                      7524999,
                      8762499,
                      9999999
                    ]
                  },  
```

{{< /expand >}}
<br>
{{< expand "Example JSON data for interface_latency:" >}}
```
            {
              "name": "nvswitch_histogram_interface_latency",
              "description": "NVIDIA Ethernet Switch Histogram Interface Latency",
              "unit": "packets",
              "histogram": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "interface",
                        "value": {
                          "stringValue": "swp1s1"
                        }
                      },
                      {
                        "key": "tc",
                        "value": {
                          "intValue": "0"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1729839233815168456",
                    "timeUnixNano": "1729839233818493910",
                    "bucketCounts": [
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0",
                      "0"
                    ],
                    "explicitBounds": [
                      319,
                      831,
                      1343,
                      1855,
                      2367,
                      2879,
                      3391,
                      3903,
                      4415
                    ]
                  },
```

{{< /expand >}}
<br>

### Static Label Format

Device static labels are exported in the {{<exlink url="https://opentelemetry.io/docs/specs/otel/resource/sdk/" text="resource">}} metric section of OTLP data:

{{< expand "Example JSON data for static device label:" >}}

{ 
  "resourceMetrics": [ 
    { 
      "resource": { 
        "attributes": [ 
          { 
            "key": "net.host.name", 
            "value": { 
              "stringValue": "switch-hostname" 
            } 
          }, 
          { 
            "key": "static_label_1", 
            "value": { 
              "stringValue": "label_1_string" 
            } 
          } 
        ] 
      }
    }
  ]
}

{{< /expand >}}
<br>
Interface static labels are exported as attributes in the gauge metrics for each interface.

{{< expand "Example JSON data for static interface label:" >}}

          "metrics": [ 
              "name": "nvswitch_interface_iface_id", 
              "description": "Network device property: iface_id", 
              "gauge": { 
                "dataPoints": [ 
                  { 
                    "attributes": [ 
                      { 
                        "key": "interface", 
                        "value": { 
                          "stringValue": "swp10" 
                        } 
                      } 
                    ], 
                    "timeUnixNano": "1727942163835000000", 
                    "asDouble": 13 
                  }, 
                  { 
                    "attributes": [ 
                      { 
                        "key": "interface_swp10_label", 
                        "value": { 
                          "stringValue": "swp10_label_string" 
                        } 
                      }

{{< /expand >}}

<!-- Commenting out HTTP export for phase 1 and 2
### HTTP OTLP Export

You can configure open telemetry export to use HTTP to communicate with the collector and define the port to use for communication:

```
cumulus@switch:~$ nv set system telemetry export otlp http port 9443
cumulus@switch:~$ nv config apply
```

Optionally, you can configure an X.509 certificate to secure the HTTP connection:

```
cumulus@switch:~$ nv set system telemetry export otlp http cert-id <certificate>
cumulus@switch:~$ nv config apply
```

For connections without a configured certificate, enable `insecure` mode:

```
cumulus@switch:~$ nv set system telemetry export otlp http insecure enabled
cumulus@switch:~$ nv config apply
```

The default encoding format for HTTP export is binary protocol buffer (`proto`); You can configure the encoding format to JSON:

```
cumulus@switch:~$ nv set system telemetry export otlp http encoding json
cumulus@switch:~$ nv config apply
```
-->
