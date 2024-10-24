---
title: Open Telemetry Export
author: NVIDIA
weight: 1232
toc: 3
---
Telemetry enables you to collect, send, and analyze large amounts of data, such as traffic statistics, port status, device health and configuration, and events. This data helps you monitor switch performance, health and behavior, traffic patterns, and <span class="a-tooltip">[QoS](## "Quality of Service")</span>.

Cumulus Linux supports {{<exlink url="https://github.com/open-telemetry/" text="open telemetry (OTEL)">}} export. You can use <span class="a-tooltip">[OTLP](## "open telemetry protocol")</span> to export metrics, such as interface counters, histogram collection, and platform statistic data to an external collector for analysis and visualization.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with Spectrum-4 ASIC only.
{{%/notice%}}

## Configure Open Telemetry

To enable open telemetry:

```
cumulus@switch:~$ nv set system telemetry export otlp state enabled 
cumulus@switch:~$ nv config apply
```

You can enable open telemetry for interface statistics, histogram collection, or both:

```
cumulus@switch:~$ nv set system telemetry interface-stats export state enabled
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv set system telemetry histogram export state enabled
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- When you enable open telemetry for interface statistics, the switch exports counters on all configured interfaces.
- When you enable open telemetry for histogram data, your buffer, counter, and latency {{<link url="ASIC-Monitoring#histogram-collection" text="histogram collection configuration">}} defines the data that the switch exports. 
{{%/notice%}}

You can enable additional interface statistic collection per interface for specific ingress buffer traffic classes (0 through 15) and egress buffer priority groups (0 through 7). When you enable these settings, the switch exports `interface_pg` and `interface_tc` [counters](#interface-statistics) for the defined priority groups and traffic classes:

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

### gRPC OTLP Export

To configure the open telemetry export destination:

1. Configure gRPC to communicate with the collector by providing the collector destination IP address or hostname. Specify the port to use for communication if it is different from the default port 8443:

   ```
   cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.100 port 4317
   cumulus@switch:~$ nv config apply
   ```

2. Configure an X.509 certificate to secure the gRPC connection:

   ```
   cumulus@switch:~$ nv set system telemetry export otlp grpc cert-id <certificate>
   cumulus@switch:~$ nv config apply
   ```

By default, OTLP export is in **secure** mode that requires a certificate. For connections without a configured certificate, you must enable `insecure` mode with the `nv set system telemetry export otlp grpc insecure enabled` command.

### Show Telemetry Export Configuration

To show the telemetry export configuration, run the `nv show telemetry export` command:

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

Cumulus Linux exports interface statistic and histogram data in the following format.

### Interface Statistics

The interface statistic data samples that the switch exports to the OTEL collector are {{<exlink url="https://opentelemetry.io/docs/specs/otel/metrics/data-model/#gauge" text="gauge streams">}} that include the interface name as an attribute and the statistics value reported in the asDouble {{<exlink url="https://opentelemetry.io/docs/specs/otel/metrics/data-model/#exemplars" text="exemplar">}}.

The following table describes the interface statistics:

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
| `nvswitch_interface_pg_rx_buffer_discard` | Interace ingress priority group receive buffer discard counter. |
| `nvswitch_interface_pg_rx_frames` | Interface ingress priority group receive frames counter.|
| `nvswitch_interface_pg_rx_octet` | Interface ingress priority group receive bytes counter. |
| `nvswitch_interface_pg_rx_shared_buffer_discard` | Interface ingress priority group receive shared buffer discard counter. |
| `nvswitch_interface_tc_tx_bc_frames` | Interface egress traffic class transmit broadcast frames counter. |
| `nvswitch_interface_tc_tx_ecn_marked_tc` | Interface egress traffic class transmit ECN marked counter. |
| `nvswitch_interface_tc_tx_frames` | Interface egress traffic class trasmit frames counter. |
| `nvswitch_interface_tc_tx_mc_frames` | Interface egress traffic class trasmit multicast frames counter. |
| `nvswitch_interface_tc_tx_no_buffer_discard_uc` | Interface egress traffic class transmit unicast no buffer discard counter. |
| `nvswitch_interface_tc_tx_octet` | Interface egress traffic class transmit bytes counter.|
| `nvswitch_interface_tc_tx_queue` | Interface egress traffic class transmit queue counter. |
| `nvswitch_interface_tc_tx_uc_frames` | Interface egress traffic class transmit unicast frames counter. |
| `nvswitch_interface_tc_tx_wred_discard` | Interface egress traffic class transmit WRED discard counter. |
| `nvswitch_interface_performance_marked_packets` | Interface performance marked packets, with marking as `ece` or `ecn`. |

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

### Histogram Data

The histogram data samples that the switch exports to the OTEL collector are {{<exlink url="https://opentelemetry.io/docs/specs/otel/metrics/data-model/#histogram" text="histogram data points">}} that include the {{<link url="ASIC-Monitoring#histogram-collection-example" text="histogram bucket (bin)">}} counts and the respective queue length size boundaries for each bucket. Latency and counter histogram data are also exported, if configured. 

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
                          "stringValue": "swp1"
                        }
                      },
                      {
                        "key": "pg",
                        "value": {
                          "stringValue": "0"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1722458110024982775",
                    "timeUnixNano": "1722458189324842275",
                    "count": "79",
                    "sum": 77705974,
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
                      "0",
                      "0",
                      "0",
                      "79"
                    ],
                    "explicitBounds": [
                      0,
                      1024,
                      2048,
                      3072,
                      4096,
                      5120,
                      6144,
                      7168,
                      8192,
                      9216,
                      10240,
                      11264
                    ],
                    "min": 980353,
                    "max": 1028062
                  },
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for interface_egress_buffer:" >}}
```
            {
              "name": "nvswitch_histogram_interface_egress_buffer",
              "description": "NVIDIA Ethernet Switch Histogram Interface Engress Buffer Queue Depth",
              "unit": "bytes",
              "histogram": {
                "dataPoints": [
                  {
                    "attributes": [
                      {
                        "key": "interface",
                        "value": {
                          "stringValue": "swp1"
                        }
                      },
                      {
                        "key": "tc",
                        "value": {
                          "stringValue": "0"
                        }
                      }
                    ],
                    "startTimeUnixNano": "1722460215693291034",
                    "timeUnixNano": "1722460275853160707",
                    "count": "60",
                    "sum": 58945566,
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
                      "0",
                      "0",
                      "0",
                      "60"
                    ],
                    "explicitBounds": [
                      0,
                      1024,
                      2048,
                      3072,
                      4096,
                      5120,
                      6144,
                      7168,
                      8192,
                      9216,
                      10240,
                      11264
                    ],
                    "min": 980181,
                    "max": 1006965
                  },
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
                          "stringValue": "swp20" 
                        } 
                      }, 
                      { 
                        "key": "type", 
                        "value": { 
                          "stringValue": "rx-byte" 
                        } 
                      } 
                    ], 
                    "startTimeUnixNano": "1725403612794459038", 
                    "timeUnixNano": "1725403612795123308", 
                    "count": "1018476", 
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for interface_latency:" >}}
```
            { 
              "name": "nvswitch_histogram_interface_latency", 
              "description": "NVIDIA Ethernet Switch Histogram Interface Latency", 
              "unit": "time", 
              "histogram": { 
                "dataPoints": [ 
                  { 
                    "attributes": [ 
                      { 
                        "key": "interface", 
                        "value": { 
                          "stringValue": "swp20" 
                        } 
                      }, 
                      { 
                        "key": "tc", 
                        "value": { 
                          "intValue": "2" 
                        } 
                      }
                    ],
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
