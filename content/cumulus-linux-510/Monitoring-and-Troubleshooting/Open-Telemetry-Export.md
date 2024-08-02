---
title: Open Telemetry Export
author: NVIDIA
weight: 1232
toc: 3
---
Telemetry enables you to collect, send, and analyze large amounts of data, such as traffic statistics, port status, device health and configuration, and events. This data helps you monitor switch performance, health and behavior, traffic patterns, and <span class="a-tooltip">[QoS](## "Quality of Service")</span>.

Cumulus Linux supports {{<exlink url="https://github.com/open-telemetry/" text="open telemetry (OTEL)">}} export. You can use <span class="a-tooltip">[OTLP](## "open telemetry protocol")</span> to export metrics, such as interface counters and histogram collection data to an external collector for analysis and visualization.

{{%notice note%}}
- Cumulus Linux supports {{<exlink url="https://github.com/open-telemetry/" text="open telemetry (OTEL)">}} export for the SN5600 switch only.
- Open Telemetry Export is a Beta feature.
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
- When you enable open telemetry for histogram data, your {{<link url="ASIC-Monitoring#histogram-collection" text="histogram collection configuration">}} defines the data that the switch exports.
{{%/notice%}}

You can enable additional interface statistic collection per interface for specific ingress buffer traffic classes (0 through 7) and egress buffer priority groups (0 through 15). When you enable these settings, the switch exports `interface_pg` and `interface_tc` [counters](#interface-statistics) for the defined priority groups and traffic classes:

```
cumulus@switch:~$ nv set system telemetry interface-stats ingress-buffer priority-group 4
cumulus@switch:~$ nv set system telemetry interface-stats egress-buffer traffic-class 12
cumulus@switch:~$ nv config apply
```

You can adjust the interface statistics sample interval (in seconds). You can specify a value between 1 and 86400. The default value 1.

```
cumulus@switch:~$ nv set system telemetry interface-stats sample-interval 100
cumulus@switch:~$ nv config apply
```

### gRPC OTLP Export

To configure open telemetry export:

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

The histogram data samples that the switch exports to the OTEL collector are {{<exlink url="https://opentelemetry.io/docs/specs/otel/metrics/data-model/#histogram" text="histogram data points">}} that include the {{<link url="ASIC-Monitoring#histogram-collection-example" text="histogram bucket (bin)">}} counts and the respective queue length size boundaries for each bucket.

The switch sends a sample with the following names for each interface enabled for ingress and egress buffer histogram collection:

| Name | Description |
|----- | ----------- |
| `nvswitch_histogram_interface_egress_buffer` | Histogram interface egress buffer queue depth. |
| `nvswitch_histogram_interface_ingress_buffer` | Histogram interface ingress buffer queue depth. |

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

<!-- Commenting out HTTP export for phase 1
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
