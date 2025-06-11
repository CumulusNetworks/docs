---
title: Open Telemetry Export
author: NVIDIA
weight: 1232
toc: 3
---
Telemetry enables you to collect, send, and analyze large amounts of data, such as traffic statistics, port status, device health and configuration, and events. This data helps you monitor switch performance, health and behavior, traffic patterns, and <span class="a-tooltip">[QoS](## "Quality of Service")</span>.

## Configure Open Telemetry

Cumulus Linux supports {{<exlink url="https://github.com/open-telemetry/" text="open telemetry (OTEL)">}} export. You can use <span class="a-tooltip">[OTLP](## "open telemetry protocol")</span> to export metrics, such as interface counters, buffer statistics, histogram collection, platform statistics, and routing metrics to an external collector for analysis and visualization.

{{%notice note%}}
Cumulus Linux supports open telemetry export on switches with the Spectrum-2 ASIC and later.
{{%/notice%}}

To enable open telemetry:

```
cumulus@switch:~$ nv set system telemetry export otlp state enabled 
cumulus@switch:~$ nv config apply
```

When you enable open telemetry, the switch collects and exports [system information](#system-information-format) metrics to the configured external collector by default. In addition, you can enable open telemetry to collect and export [interface statistics](#interface-statistics), [buffer statistics](#buffer-statistics), [histogram data](#histogram-data), [control plane statistics](#control-plane-statistics), [platform statistics](#platform-statistics), and [routing metrics](#router-statistics).

### Interface Statistics

When you enable open telemetry for interface statistics, the switch exports [interface statistics](#interface-statistic-format) on all configured interfaces:

```
cumulus@switch:~$ nv set system telemetry interface-stats export state enabled
cumulus@switch:~$ nv config apply
```

You can adjust the interface statistics sample interval (in seconds). You can specify a value between 1 and 86400. The default value is 1.

```
cumulus@switch:~$ nv set system telemetry interface-stats sample-interval 100
cumulus@switch:~$ nv config apply
```

You can enable these additional interface statistics:
- Traffic Class and Switch Priority metrics for ingress buffer traffic classes (0 through 15) and egress buffer priority groups (0 through 7)
- PHY for interface PHY metrics

{{< tabs "TabID35 ">}}
{{< tab "Traffic Class and Switch Priority ">}}

When you enable these settings, the switch exports `interface_pg` and `interface_tc` counters for the defined priority groups and traffic classes:

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

{{< /tab >}}
{{< tab "PHY">}}

When you enable this setting, the switch exports `nvswitch_interface_phy` and `nvswitch_interface_raw` interface PHY counters:

```
cumulus@switch:~$ nv set system telemetry interface-stats class phy state enabled
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

To show interface statistics configuration, run the `nv show system telemetry interface-stats` command.

### Buffer Statistics

When you enable open telemetry for buffer statistics, the switch exports interface and switch [buffer occupancy and watermark](#buffer-statistic-format) metrics.

```
cumulus@switch:~$ nv set system telemetry buffer-stats export state enabled 
cumulus@switch:~$ nv config apply
```

To show buffer statistics configuration, run the `nv show system telemetry buffer-stats` command.

### Control Plane Statistics

When you enable open telemetry for control plane statistics, the switch exports additional counters for [control plane packets](#control-plane-statistic-format):

```
cumulus@switch:~$ nv set system telemetry control-plane-stats export state enabled
cumulus@switch:~$ nv config apply
```

You can adjust the control plane statistics sample interval (in seconds). You can specify a value between 1 and 86400. The default value is 1.

```
cumulus@switch:~$ nv set system telemetry control-plane-stats sample-interval 100
cumulus@switch:~$ nv config apply
```

To show control plane statistics configuration, run the `nv show system telemetry control-plane-stats` command.

### Histogram Data

When you enable open telemetry for histogram data, your buffer, counter, and latency {{<link url="ASIC-Monitoring#histogram-collection" text="histogram collection configuration">}} defines the data that the switch exports:

```
cumulus@switch:~$ nv set system telemetry histogram export state enabled
cumulus@switch:~$ nv config apply
```

To show histogram data configuration, run the `nv show system telemetry histogram` command.

### Platform Statistics

When you enable platform statistic open telemetry, the switch exports data about the CPU, disk, filesystem, memory, and sensor health. To enable all [platform statistics](#platform-statistic-format) globally:

```
cumulus@switch:~$ nv set system telemetry platform-stats export state enabled
cumulus@switch:~$ nv config apply
```

If you do not want to enable all platform statistics, you can enable or disable individual platform telemetry components or adjust the sample interval for individual components. The default sample interval is 60 seconds.

{{< tabs "TabID115 ">}}
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

To show platform statistics configuration, run the `nv show system telemetry platform-stats` command.

### Routing Metrics

To enable open telemetry for layer 3 [routing metrics](#routing-metrics-format), enable the OTEL routing service:

```
cumulus@switch:~$ nv set system telemetry router export state enabled
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
To export any of the routing metrics, you must first enable the OTEL routing service.
{{%/notice%}}

To enable collection and export of BGP peer state statistics across all VRFs:

```
cumulus@switch:~$ nv set system telemetry router bgp export state enabled
cumulus@switch:~$ nv config apply
```

To enable collection and export of statistics for all BGP peers under a specific VRF, run the `nv set system telemetry router vrf <vrf-id> bgp export state enabled` command; for example:

```
cumulus@switch:~$ nv set system telemetry router vrf RED bgp export state enabled
cumulus@switch:~$ nv config apply
```

To enable collection and export of statistics for a specific BGP peer under a specific VRF, run the `nv set system telemetry router vrf <vrf-id> bgp peer <peer-id> export state enabled` command; for example:

```
cumulus@switch:~$ nv set system telemetry router vrf RED bgp peer swp1 export state enabled
cumulus@switch:~$ nv config apply
```

To enable collection and export of statistics for the IP routing table across all VRFs:

```
cumulus@switch:~$ nv set system telemetry router rib export state enabled
cumulus@switch:~$ nv config apply 
```

To enable collection and export of statistics for the IP routing table for a specific VRF, run the `nv set system telemetry router vrf <vrf-id> rib export state enabled` command; for example::

```
cumulus@switch:~$ nv set system telemetry router vrf RED rib export state enabled
cumulus@switch:~$ nv config apply
```

You can adjust the sample interval (in seconds) for routing metrics. You can specify a value in multiples of 10 up to 60. The default value is 30.

```
cumulus@switch:~$ nv set system telemetry router sample-interval 40
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- You can disable BGP export across all VRFs with the `nv set telemetry router bgp export state disabled` command and enable it only for specific VRFs with the `nv set telemetry router vrf <vrf-name> bgp export state enabled` command. 
- You can also disable BGP export across all peers in a VRF with the `nv set telemetry router vrf <vrf-name> bgp export state disabled` command, and enable telemetry only for specific peers in the VRF with the `nv set telemetry router vrf <vrf-name> bgp peer <peer> export state enabled` command.
{{%/notice%}}

To show routing metrics configuration settings, run the `nv show system telemetry router` command.

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

### Customize Export

By default, the switch exports all statistics enabled {{<link url="#configure-open-telemetry" text="globally">}} (with the `nv set system telemetry <statistics>` command) to all configured OTLP destinations. If you want to export different metrics to different OTLP destinations, you can customize the export by specifying a statistics group to control which statistics you export and the sample interval for a destination.

{{%notice note%}}
Statistics groups inherit global OTLP export configurations by default. More specific configuration under a statistics group, such as enabling or disabling a statistic type or changing the sample interval overrides any global OTLP configuration.
{{%/notice%}}

The following example:
- Configures STAT-GROUP1 to export all platform statistics (`platform-stats`) but not interface statistics (`interface-stats`).
- Applies the STAT-GROUP1 configuration to the OTLP destination 10.1.1.100.

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 platform-stats export state enabled
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 interface-stats export state disabled
cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.100 stats-group STAT-GROUP1
cumulus@switch:~$ nv config apply
```

The following example:
- Configures STAT-GROUP2 to inherit all statistic configuration from the global telemetry configuration, but changes the sample interval of `router` statistics to 100:
- Applies the STAT-GROUP2 configuration to the OTLP destination 10.1.1.200.

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP2 router sample-interval 100
cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.200 stats-group STAT-GROUP2
cumulus@switch:~$ nv config apply
```

The following example:
- Configures STAT-GROUP3 to disable histogram (`histogram`) and buffer (`buffer-stats`) statistics, and enables all platform statistics(`platform-stats`) except for disk state:
- Applies the STAT-GROUP3 configuration to the OTLP destination 10.1.1.30.

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP3 buffer-stats export state disabled
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP3 histogram export state disabled
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP3 platform-stats export state enabled
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP3 platform-stats class disk state disabled
cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.30 stats-group STAT-GROUP3
cumulus@switch:~$ nv config apply
```

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

### System Information Format

When you enable open telemetry with the `nv set system telemetry export otlp state enabled` command, the switch exports the following system information metrics to the configured OTEL collector by default:

|  Name | Description |
|------ | ----------- |
| `node_boot_time_seconds` | Node boot time, in unixtime. |
| `node_time_seconds` | System time in seconds since epoch (1970). |
| `node_os_info` |  Operating system and image information, such as name and version. |

### Interface Statistic Format

The interface statistic data samples that the switch exports to the OTEL collector are {{<exlink url="https://opentelemetry.io/docs/specs/otel/metrics/data-model/#gauge" text="gauge streams">}} that include the interface name as an attribute and the statistics value reported in the asDouble {{<exlink url="https://opentelemetry.io/docs/specs/otel/metrics/data-model/#exemplars" text="exemplar">}}.

{{< tabs "TabID319 ">}}
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
| `nvswitch_interface_ether_stats_pkts` | Total number of received packets (including bad, broadcast, and multicast packets). |
| `nvswitch_interface_ether_stats_broadcast_pkts` | Total number of good packets received that were directed to the broadcast address. This does not include multicast packets.|
| `nvswitch_interface_ether_stats_collisions` | Best estimate of the total number of collisions on this Ethernet segment. |
| `nvswitch_interface_ether_stats_crc_align_errors` | Total number of received packets (excluding framing bits, but including FCS octets) between 64 and MTU octets, inclusive, but had either a bad frame check sequence (FCS) with an integral number of octets (FCS error) or a bad FCS with a non-integral number of octets (alignment error). |
| `nvswitch_interface_ether_stats_drop_events` | Total number of events in which packets were dropped by the probe due to lack of resources.|
| `nvswitch_interface_ether_stats_fragments` | Total number of received packets with less than 64 octets (excluding framing bits but including FCS octets) and that have either a bad FCS with an integral number of octets (FCS error) or a bad FCS with a non-integral number of octets (alignment error). |
| `nvswitch_interface_ether_stats_jabbers` | Total number of received packets longer than MTU octets (excluding framing bits, but including FCS octets), and that have either a bad FCS with an integral number of octets (FCS error) or a bad FCS with a non-integral number of octets (alignment error). |
| `nvswitch_interface_ether_stats_multicast_pkts` | Total number of good packets received that were directed to a multicast MAC address. This number does not include packets directed to the broadcast address. |
| `nvswitch_interface_ether_stats_octets` | Total number of octets of data (including those in bad packets) received (excluding framing bits but including FCS octets). |
| `nvswitch_interface_ether_stats_oversize_pkts` | Total number of received packets longer than MTU octets (excluding framing bits, but including FCS octets) but were otherwise well formed. |
| `nvswitch_interface_ether_stats_undersize_pkts` | Total number of received packets with less than 64 octets (excluding framing bits, but including FCS octets) and were otherwise well formed.|
| `nvswitch_interface_no_buffer_discard_mc` | Number of multicast packets dropped due to lack of egress buffer resources. |
| `nvswitch_interface_rx_buffer_almost_full` | Number of events where the port rx buffer has passed a fullness threshold. |
| `nvswitch_interface_rx_buffer_full` | Number of events where the port rx buffer has reached 100% fullness. |
| `nvswitch_interface_rx_ebp` | Number of received EBP packets. |
| `nvswitch_interface_tx_ebp` | Number of transmitted EBP packets. |
| `nvswitch_interface_tx_int_cksm_err` | Counter is incremented upon packet payload internal checksum error. |
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
| `nvswitch_interface_tx_stats_pkts65to127octets` | Total packets transmitted, 65-255 octets in length. |	 
| `nvswitch_interface_tx_stats_pkts256to511octets` | Total packets transmitted, 256-511 octets in length. |  
| `nvswitch_interface_tx_stats_pkts512to1023octets` | Total packets transmitted, 512-1023 octets in length. |  
| `nvswitch_interface_tx_stats_pkts1024to1518octets` | Total packets transmitted, 1024-1518 octets in length. |  
| `nvswitch_interface_tx_stats_pkts1519to2047octets` | Total packets transmitted, 1519-2047 octets in length. |  
| `nvswitch_interface_tx_stats_pkts2048to4095octets` | Total packets transmitted, 2048-4095 octets in length. |  
| `nvswitch_interface_tx_stats_pkts4096to8191octets` | Total packets transmitted, 4096-8191 octets in length. |  
| `nvswitch_interface_tx_stats_pkts8192to10239octets` | Total packets transmitted, 8192-10239 octets in length. |  
| `nvswitch_interface_ether_stats_pkts64octets` | Total packets received, 64 octets in length. |  
| `nvswitch_interface_ether_stats_pkts65to127octets` | Total packets received, 65-127 octets in length. |  
| `nvswitch_interface_tx_stats_pkts256to511octets` | Total packets received, 128-255 octets in length. |  
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
| `nvswitch_interface_oper_aggregate_speed` | Speed in bits per second for the connected interface. |
| `nvswitch_interface_number_of_lanes` | Number of lanes used by the interface. |

{{< /tab >}}
{{< tab "Traffic Class ">}}

The switch collects and exports the following additional interface traffic class statistics when you configure the `nv set system telemetry interface-stats egress-buffer traffic-class <class>` command:

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

The switch collects and exports the following additional interface priority group statistics when you configure the `nv set system telemetry interface-stats ingress-buffer priority-group <priority>` command:

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_pg_rx_buffer_discard` | Interface ingress priority group receive buffer discard counter. |
| `nvswitch_interface_pg_rx_frames` | Interface ingress priority group receive frames counter.|
| `nvswitch_interface_pg_rx_octets` | Interface ingress priority group receive bytes counter. |
| `nvswitch_interface_pg_rx_shared_buffer_discard` | Interface ingress priority group receive shared buffer discard counter. |

{{< /tab >}}
{{< tab "Switch Priority ">}}

The switch collects and exports the following additional interface switch priority statistics when you configure the `nv set system telemetry interfaces-stats switch-priority <priority>` command:

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
{{< tab "PHY">}}

The switch collects and exports the following additional interface statistics when you configure the `nv set system telemetry interface-stats class phy state enabled` command:

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_phy_stats_phy_received_bits` | Total amount of traffic (bits) received. |
| `nvswitch_interface_phy_stats_phy_symbol_errors` | Error bits not corrected by the FEC correction algorithm or when FEC is not active. |
| `nvswitch_interface_phy_stats_phy_effective_errors` | Number of errors after FEC is applied. |
| `nvswitch_interface_phy_stats_phy_raw_errors` | Error bits identified on lane 0 through lane 7. When FEC is enabled, this induction corresponds to corrected errors. |
| `nvswitch_interface_phy_stats_raw_ber` | raw_ber_coef_laneX*10^(raw_ber_magnitude) |
| `nvswitch_interface_phy_stats_phy_corrected_bits` | Corrected bits by FEC engine. |
| `nvswitch_interface_phy_stats_time_since_last_clear` | Time passed since the last counters clear event in msec.|

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

### Buffer Statistic Format

The switch collects and exports the following interface and switch, buffer occupancy and watermark statistics when you configure the `nv set system telemetry buffer-stats export state enable` command:

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_shared_buffer_port_pg_curr_occupancy` | Current buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_pg_watermark` | Maximum buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_pg_desc_curr_occupancy` | Current buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_pg_desc_watermark` | Maximum buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_pg_watermark_recorded_max` | Highest maximum buffer occupancy recorded since running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_pg_desc_watermark_recorded_max` | Highest maximum buffer occupancy for descriptors recorded since running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_igress_pool_curr_occupancy` | Current ingress pool buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_igress_pool_desc_curr_occupancy` | Current ingress pool buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_ingress_pool_watermark` | Maximum ingress pool buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_ingress_pool_desc_watermark` | Maximum ingress pool buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_ingress_pool_watermark_recorded_max` | Highest maximum ingress pool buffer occupancy recorded since running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_ingress_pool_desc_watermark_recorded_max` | Highest maximum ingress pool buffer occupancy for descriptors recorded since running sdk_stats. |
| `nvswitch_interface_shared_buffer_tc_time_since_clear` | Time in milliseconds since the buffer watermarks were last cleared.|
| `nvswitch_interface_shared_buffer_port_tc_curr_occupancy` | Current buffer occupancy for traffic class. |
| `nvswitch_interface_shared_buffer_port_tc_watermark` | Maximum buffer occupancy for traffic class. |
| `nvswitch_interface_shared_buffer_port_tc_desc_curr_occupancy` | Current buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_tc_desc_watermark` | Maximum buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_tc_watermark_recorded_max` | Highest maximum buffer occupancy recorded since running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_tc_desc_watermark_recorded_max` | Highest maximum buffer occupancy for TC descriptors recorded since running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_egress_pool_curr_occupancy` | Current egress pool buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_egress_pool_watermark` | Maximum egress pool buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_egress_pool_desc_curr_occupancy` | Current egress pool buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_egress_pool_desc_watermark` | Maximum egress pool buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_egress_pool_watermark_recorded_max` | Highest maximum egress pool buffer occupancy recorded since running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_egress_pool_desc_watermark_recorded_max` | Highest maximum egress pool buffer occupancy for pool desc recorded since running sdk_stats. |
| `nvswitch_interface_shared_buffer_mc_port_curr_occupancy`  | Current buffer occupancy for multicast port. |
| `nvswitch_interface_shared_buffer_mc_port_watermark` | Maximum buffer occupancy for multicast port. |
| `nvswitch_interface_shared_buffer_mc_port_watermark_recorded_max` | Highest maximum buffer occupancy for multicast port recorded since running sdk_stats. |
| `nvswitch_shared_buffer_mc_sp_curr_occupancy` | Current buffer occupancy for multicast switch priority. |
| `nvswitch_shared_buffer_mc_sp_watermark` | Maximum buffer occupancy for multicast switch priority. |
| `nvswitch_shared_buffer_mc_sp_watermark_recorded_max` | Highest maximum buffer occupancy for multicast switch priority recorded since running sdk_stats. |
| `nvswitch_shared_buffer_pool_curr_occupancy` | Current pool buffer occupancy. |
| `nvswitch_shared_buffer_pool_watermark` | Maximum pool buffer occupancy |
| `nvswitch_shared_buffer_pool_watermark_recorded_max` | Highest maximum pool buffer occupancy for multicast switch priority recorded since running sdk_stats. |
| `nvswitch_interface_headroom_buffer_pg_curr_occupancy` | Current headroom buffer occupancy for port buffer. |
| `nvswitch_interface_headroom_buffer_pg_watermark` | Maximum pool headroom buffer occupancy for port buffer. |
| `nvswitch_interface_headroom_buffer_pg_watermark_recorded_max` | Highest maximum headroom buffer occupancy for port buffer recorded since running sdk_stats. |
| `nvswitch_interface_headroom_shared_buffer_curr_occupancy` | Current headroom buffer occupancy for port shared buffer. |
| `nvswitch_interface_headroom_shared_buffer_watermark` | Maximum headroom buffer occupancy for port shared buffer. |
| `nvswitch_interface_headroom_shared_buffer_watermark_recorded_max` | Highest maximum headroom buffer occupancy for port shared buffer recorded since running sdk_stats. |
| `nvswitch_interface_headroom_pool_curr_occupancy` | Current headroom buffer occupancy for port shared pool buffer |
| `nvswitch_interface_headroom_pool_watermark` | Maximum headroom buffer occupancy for port shared pool buffer. |
| `nvswitch_interface_headroom_pool_watermark_recorded_max` | Highest maximum headroom buffer occupancy for port shared pool buffer. |

### Control Plane Statistic Format

When you enable control plane statistic telemetry, the switch exports the following statistics:

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

When you enable platform statistic telemetry globally, or when you enable telemetry for the individual components, the switch exports the following statistics:

{{< tabs "TabID723 ">}}
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

### Routing Metrics Format

When you enable layer 3 routing metrics telemetry, the switch exports the following statistics:

| Name | Description |
|----- | ----------- |
| `nvrouting_bgp_peer_state` |  BGP peer state: `Established`, `Idle`, `Connect`, `Active`, `OpenSent`.  |
| `nvrouting_bgp_peer_fsm_established_transitions` | Number of BGP peer state transitions to the `Established` state for the peer session.|
| `nvrouting_bgp_peer_rib_adj_in_ipv4_unicast` | Number of IPv4 unicast routes received from the BGP neighbor after applying any policies. This count is the number of routes present in the post-policy Adj-RIB-In for the neighbor. |
| `nvrouting_bgp_peer_rib_adj_in_ipv6_unicast` | Number of IPv6 unicast routes received from the BGP neighbor after applying any policies. This count is the number of routes present in the post-policy Adj-RIB-In for the neighbor. |
| `nvrouting_bgp_peer_rib_adj_in_l2vpn_evpn` | Number of EVPN routes received from the BGP neighbor after applying any policies. This count is the number of routes present in the post-policy Adj-RIB-In for the neighbor. |
| `nvrouting_bgp_peer_socket_in_queue` | Number of messages queued to be received from the BGP neighbor.|
| `nvrouting_bgp_peer_socket_out_queue` | Number of messages queued to be sent to the BGP neighbor.|
| `nvrouting_bgp_peer_rx_updates` | Number of BGP messages received from the neighbor.|
| `nvrouting_bgp_peer_tx_updates` | Number of BGP messages sent to the neighbor. |
| `nvrouting_rib_count` | Number of routes in the IP routing table for each route source. |
| `nvrouting_rib_count_ipv6` | Tracks the IPv6 RIB route count for each route source. |
| `nvrouting_rib_count_connected` | Tracks the total IPv4 RIB connected route count. |
| `nvrouting_rib_count_bgp` | Tracks the total IPv4 RIB BGP route count. |
| `nvrouting_rib_count_kernel` | Tracks the total IPv4 RIB kernel route count.|
| `nvrouting_rib_count_static` | Tracks the total IPv4 RIB static route count. |
| `nvrouting_rib_count_pbr` | Tracks the total IPv4 RIB PBR route count. |
| `nvrouting_rib_count_ospf` | Tracks the total IPv4 RIB OSPF route count. |
| `nvrouting_rib_count_connected_ipv6` | Tracks the total IPv6 RIB connected route count. |
| `nvrouting_rib_count_bgp_ipv6` | Tracks the total IPv6 RIB BGP route count. |
| `nvrouting_rib_count_kernel_ipv6` | Tracks the total IPv6 RIB kernel route count. |
| `nvrouting_rib_count_static_ipv6` | Tracks the total IPv6 RIB static route count. |
| `nvrouting_rib_count_pbr_ipv6` | Tracks the total IPv6 RIB PBR route count. |
| `nvrouting_rib_count_ospf_ipv6` | Tracks the total IPv6 RIB OSPF route count. |

{{< expand "Example JSON data for BGP peer metrics:" >}}
```
INFO:root:Received metrics export request
INFO:root:Metric name: nvrouting_bgp_peer_state
INFO:root:Metric:
name: "nvrouting_bgp_peer_state"
description: "Tracks BGP peer state information (Established:1,Idle:2,Connect:3, Active:4, Opensent:5 )"
gauge {
  data_points {
    start_time_unix_nano: 1738017981273381011
    time_unix_nano: 1738017981275774678
    as_int: 1
    attributes {
      key: "peer-id"
      value {
        string_value: "swp17.100"
      }
    }
    attributes {
      key: "state"
      value {
        string_value: "Established"
      }
    }
    attributes {
      key: "vrf"
      value {
        string_value: "default"
      }
    }
  }
  data_points {
    start_time_unix_nano: 1738017981273381011
    time_unix_nano: 1738017981275774678
    as_int: 1
    attributes {
      key: "peer-id"
      value {
        string_value: "swp17.101"
      }
    }
    attributes {
      key: "state"
      value {
        string_value: "Established"
      }
    }
    attributes {
      key: "vrf"
      value {
        string_value: "default"
      }
    }
  }
 
INFO:root:Metric name: nvrouting_bgp_peer_fsm_established_transitions
INFO:root:Metric:
name: "nvrouting_bgp_peer_fsm_established_transitions"
description: "Tracks BGP peer state transitions to the Established state"
gauge {
  data_points {
    start_time_unix_nano: 1738017981273393225
    time_unix_nano: 1738017981275785883
    as_int: 1
    attributes {
      key: "peer-id"
      value {
        string_value: "swp16.100"
      }
    }
    attributes {
      key: "state"
      value {
        string_value: "Established"
      }
    }
    attributes {
      key: "vrf"
      value {
        string_value: "default"
      }
    }
  }
  data_points {
    start_time_unix_nano: 1738017981273393225
    time_unix_nano: 1738017981275785883
    as_int: 1
    attributes {
      key: "peer-id"
      value {
        string_value: "swp18.101"
      }
    }
    attributes {
      key: "state"
      value {
        string_value: "Established"
      }
    }
    attributes {
      key: "vrf"
      value {
        string_value: "default"
      }
    }
  }
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for RIB count metrics:" >}}
```
name: "nvrouting_rib_count_bgp_ipv6"
description: "Total Number of ipv6 BGP routes in Zebra"
gauge {
  data_points {
    start_time_unix_nano: 1738016804524747485
    time_unix_nano: 1738016804529163046
    as_int: 2062
    attributes {
      key: "vrf"
      value {
        string_value: "vrf2"
      }
    }
  }
  data_points {
    start_time_unix_nano: 1738016804524747485
    time_unix_nano: 1738016804529163046
    as_int: 2062
    attributes {
      key: "vrf"
      value {
        string_value: "vrf6"
      }
    }
  }
```
{{< /expand >}}

### Histogram Data Format

The histogram data samples that the switch exports to the OTEL collector are {{<exlink url="https://opentelemetry.io/docs/specs/otel/metrics/data-model/#histogram" text="histogram data points">}} that include the {{<link url="ASIC-Monitoring#histogram-collection-example" text="histogram bucket (bin)">}} counts and the respective queue length size boundaries for each bucket. Latency and counter histogram data are also exported, if configured.

{{% notice note %}}
Latency histogram bucket counts do not increment in exported telemetry data if there are no packets transmitted in the traffic class during the sample interval.
{{% /notice %}}

The switch sends a sample with the following names for each interface enabled for ingress and egress buffer, latency, and counter histogram collection:

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

## Show Telemetry Health Metrics

To show telemetry health information, run the `nv show system telemetry health` command:

```
cumulus@switch:~$ nv show system telemetry health
                                     operational
---------------------------          -----------
service-status    
  nv-telemtry-service                active                      
  platform-stats-service             active
  histogram-export-service           active
  sdk-stats-service                  active
  routing-telemtry-service           inactive
internal-metrics 
  process 
    cpu-seconds                      3020
    memory-rss-kilobytes             182812672
    runtime-heap-alloc-bytes         28617960
    runtime-total-alloc-bytes        915541979208
    runtime-total-sys-memory-bytes   151368752
    uptime-seconds                   65313
[receivers]                          otlp/global
[receivers]                          prometheus/global
processors
  [memory-limiter]                   memory_limiter/1
  [batch]                            batch/1
[exporters]                          otlp/global

Export Destination Status
=======================
    Destination         Connectivity          Export Counter       Drop Counter
    -----------         ------------          --------------       ------------
    11.0.10.2:4317      Pass                  51534586             7087
```

Cumulus Linux Open telemetry also provides a set of internal metrics exposed by the collector to monitor its performance and behavior. These metrics are essential to understand the health and efficiency of the collector.

To show information about the telemetry health internal metrics, run the `nv show system telemetry health internal-metrics` command:

```
cumulus@switch:~$ nv show system telemetry health internal-metrics
                                     operational
------------------------             -----------
process        
  cpu-seconds                        029
  memory-rss-kilobytes               182812672
  runtime-heap-alloc-bytes           28617960
  runtime-total-alloc-bytes          915541979208
  runtime-total-sys-memory-bytes     151368752
  uptime-seconds                     65313
[receivers]                          otlp/global
[receivers]                          prometheus/global
processors
  [memory-limiter]                   memory_limiter/1
  [batch]                            batch/1
[exporters]                          otlp/global
```

To show information about the telemetry health internal metrics process, run the `nv show system telemetry health internal-metrics process` command:

```
cumulus@switch:~$ nv show system telemetry health internal-metrics process
                                   operational
------------------------           -----------
cpu-seconds                        029
memory-rss-kilobytes               182812672
runtime-heap-alloc-bytes           28617960
runtime-total-alloc-bytes          915541979208
runtime-total-sys-memory-bytes     151368752
uptime-seconds                     65313
```

To show information about the telemetry health internal metrics receivers, run the `nv show system telemetry health internal-metrics receivers` command:

```
cumulus@switch:~$ nv show system telemetry health internal-metrics receivers
Receivers            Accepted Metric Points      Refused Metric Points
---------            ----------------------      ---------------------
otlp/global          4967144                     0
prometheus/global    46989135                    0
```

To show information about the telemetry health internal metrics processors, run the `nv show system telemetry health internal-metrics processors` command:

```
cumulus@switch:~$ nv show system telemetry health internal-metrics processors
  Memory-limiter
  ==============
    memory_limiter/1
     Accepted Metric Points: 25002370
     Dropped Metric Points: 0
     Inserted Metric Points: 0
     Refused Metric Points: 0

  Batch Processor
  ===============
    batch/1
     Batch Send Size Bucket 10: 828620
     Batch Send Size Bucket 25: 828620
     Batch Send Size Bucket 50: 828620
     Batch Send Size Bucket 75: 828620
     Batch Send Size Bucket 100: 828620
...
```

To show information about the telemetry health internal metrics exporters, run the `nv show system telemetry health internal-metrics exporters` command:

```
cumulus@switch:~$ nv show system telemetry health internal-metrics exporters
Exporters       Enqueue Failed Metric Points   Queue Capacity   Queue Size   Send Failed Metric Points   Sent Metric Points
---------       ----------------------------   --------------   ----------   -------------------------   ------------------
otlp/global     0                              1000             0            7087                        52000844
```
