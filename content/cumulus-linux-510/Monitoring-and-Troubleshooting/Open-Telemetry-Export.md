---
title: Open Telemetry Export
author: NVIDIA
weight: 1232
toc: 3
---
You use telemetry to collect, send, and analyze large amounts of data, such as traffic statistics, port status, device health and configuration, and events. This data helps you monitor switch performance, health and behavior, traffic patterns, and quality of service (QoS).

Cumulus Linux supports {{<exlink url="https://github.com/open-telemetry/" text="open telemetry (OTEL)">}} export on the SN5600 switch. You can use <span class="a-tooltip">[OTLP](## "open telemetry protocol")</span> to export metrics, such as interface counters and histogram collection data to an external collector for analysis and visualization.

## Enable Open Telemetry Export

To enable open telemetry export:

```
cumulus@switch:~$ nv set system telemetry export otlp state enabled 
cumulus@switch:~$ nv config apply
```

You can enable open telemetry export for interface statistics, histogram collection, or both:

```
cumulus@switch:~$ nv set system telemetry interface-stats export state enabled
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv set system telemetry histogram export state enabled
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- When you enable open telemetry export for interface statistics, the switch exports counters on all interfaces.
- When you enable open telemetry export for histogram data, your [histogram collection configuration](#histogram-collection) defines the data that the switch exports.
{{%/notice%}}

### gRPC OTLP Export

To configure open telemetry export:

1. Configure gRPC to communicate with the collector by providing the collector destination IP address or hostname. Specify the port to use for communication if it is different from the default port 8443.

   ```
   cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.100 port 4317
   cumulus@switch:~$ nv config apply
   ```

2. Configure an X.509 certificate to secure the gRPC connection:

   ```
   cumulus@switch:~$ nv set system telemetry export otlp grpc cert-id <certificate>
   cumulus@switch:~$ nv config apply
   ```

By default, OTLP export is in **secure** mode and requires a certificate. For connections without a configured certificate, you must enable `insecure` mode with the `nv set system telemetry export otlp grpc insecure enabled` command.

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
