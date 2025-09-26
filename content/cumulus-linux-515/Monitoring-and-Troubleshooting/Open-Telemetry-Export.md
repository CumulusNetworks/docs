---
title: Open Telemetry Export
author: NVIDIA
weight: 1232
toc: 3
---
Telemetry enables you to collect, send, and analyze large amounts of data, such as traffic statistics, port status, device health and configuration, and events. This data helps you monitor switch performance, health and behavior, traffic patterns, and <span class="a-tooltip">[QoS](## "Quality of Service")</span>.

## Configure Open Telemetry

Cumulus Linux supports {{<exlink url="https://github.com/open-telemetry/" text="open telemetry (OTEL)">}} export. You can use <span class="a-tooltip">[OTLP](## "open telemetry protocol")</span> to export metrics, such as interface counters, buffer statistics, histogram collection, platform statistics, routing metrics, and `systemd` statistics to an external collector for analysis and visualization.

{{%notice note%}}
Cumulus Linux supports open telemetry export on switches with the Spectrum-2 ASIC and later.
{{%/notice%}}

To enable open telemetry:

```
cumulus@switch:~$ nv set system telemetry export otlp state enabled 
cumulus@switch:~$ nv config apply
```

When you enable open telemetry, the switch collects and exports [system information](#system-information-format) metrics to the configured external collector by default. In addition, you can enable open telemetry to collect and export [interface statistics](#interface-statistics), [buffer statistics](#buffer-statistics), [histogram data](#histogram-data), [control plane statistics](#control-plane-statistics), [platform statistics](#platform-statistics), and [routing metrics](#router-statistics).

### ACL Statistics

When you enable open telemetry for ACL statistics, the switch exports [ACL](#acl-statistic-format) interface metrics (such as packet and byte count) for all the interfaces on which ACLs are applied.

```
cumulus@switch:~$ nv set system telemetry acl-stats export state enabled 
cumulus@switch:~$ nv config apply
```

To enable open telemetry for ACL configuration and operational metrics (such as matches and actions for each ACL):

```
cumulus@switch:~$ nv set system telemetry acl-stats class acl-set state enabled 
cumulus@switch:~$ nv config apply
```

You can adjust the ACL statistics sample interval (in seconds). You can specify a value between 1 and 86400. The default value is 5.

```
cumulus@switch:~$ nv set system telemetry acl-stats sample-interval 100
cumulus@switch:~$ nv config apply
```

### AI Ethernet Statistics

When you enable open telemetry for AI Ethernet statistics, the switch exports [adaptive routing, SRv6, and packet trimming statistics](#ai-ethernet-statistic-format):

```
cumulus@switch:~$ nv set system telemetry ai-ethernet-stats export state enabled
cumulus@switch:~$ nv config apply
```

You can adjust the adaptive routing statistics sample interval (in seconds). You can specify a value between 1 and 86400. The default setting is 1 second.

```
cumulus@switch:~$ nv set system telemetry ai-ethernet-stats sample-interval 40
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- To export adaptive routing metrics, you must {{<link url="Equal-Cost-Multipath-Load-Sharing/#enable-adaptive-routing" text="enable adaptive routing">}}.
- To export packet trimming metrics, you must {{<link url="Packet-Trimming" text="enable packet trimming">}}.
- To export SRv6 metrics, you must {{<link url="Segment-Routing" text="enable segment routing">}}.
{{%/notice%}}

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

#### Temporality Mode

Histogram temporality mode lets you choose how to aggregate and report histogram data over time.

Cumulus Linux supports the following temporality modes:
- Delta mode captures only the new data recorded after the last export, reflecting the rate of change instead of cumulative totals. Each export includes only the counts collected within the latest time window; previous values do not carry over to the next reporting cycle. This is the default setting.
- Cumulative mode reports the total count from the beginning of the measurement period. Each export includes all previously reported values along with newly recorded data, ensuring that the metric continues to grow until the measurement cycle resets. This approach prevents the metric from resetting between reports.

{{%notice note%}}
Changing the temporality mode:
- Impacts both snapshot file collection and metric data export.
- Restarts the histogram service, initiating a new measurement cycle.
{{%/notice%}}

To change the temporality mode, run the `nv set system telemetry histogram temporality <mode>` command. The following command sets the temporality mode to cumulative:

```
cumulus@switch:~$ nv set system telemetry histogram temporality cumulative
cumulus@switch:~$ nv config apply
```

To reset the temporality mode to the default value (`delta`), run the `nv unset system telemetry histogram temporality` command or set the mode to delta with the `nv set system telemetry histogram temporality delta` command.

To show histogram data configuration, run the `nv show system telemetry histogram` command.

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

### LLDP Statistics

When you enable LLDP statistic open telemetry, the switch exports neighbor, port, and chassis information. LLDP metrics are useful to get a network topology to optimize and efficiently use network resources. Knowing the network layout makes it easier to configure network devices. To enable the [LLDP statistics](#lldp-statistic-format):

```
cumulus@switch:~$ nv set system telemetry lldp export state enabled
cumulus@switch:~$ nv config apply
```

You can adjust the LLDP statistics sample interval (in seconds). You can specify a value between 1 and 86400. The default value is 5.

```
cumulus@switch:~$ nv set system telemetry lldp sample-interval 10
cumulus@switch:~$ nv config apply
```

### Platform Statistics

When you enable platform statistic open telemetry, the switch exports data about the CPU, disk, filesystem, memory, sensor health, and transceiver information. To enable all [platform statistics](#platform-statistic-format) globally:

```
cumulus@switch:~$ nv set system telemetry platform-stats export state enabled
cumulus@switch:~$ nv config apply
```

If you do not want to enable all platform statistics, you can enable or disable individual platform telemetry components or adjust the sample interval for individual components. The default sample interval is 60 seconds.

{{< tabs "TabID115 ">}}
{{< tab "CPU ">}}

To enable CPU statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class cpu state enabled
cumulus@switch:~$ nv config apply
```

To adjust the sample interval for CPU statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class cpu sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Disk">}}

To enable disk statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class disk state enabled
cumulus@switch:~$ nv config apply
```

To adjust the sample interval for disk statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class disk sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Filesystem">}}

To enable filesystem statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class file-system state enabled
cumulus@switch:~$ nv config apply
```

To adjust the sample interval for filesystem statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class file-system sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Memory">}}

To enable memory statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class memory state enabled
cumulus@switch:~$ nv config apply
```

To adjust the sample interval for memory statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class memory sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Environment sensors">}}

To enable environment sensor statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class environment-sensors state enabled
cumulus@switch:~$ nv config apply
```

To adjust the sample interval for environment sensor statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class environment-sensors sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Transceivers">}}

To enable transceiver statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class transceiver-info state enabled
cumulus@switch:~$ nv config apply
```

To adjust the sample interval for transceiver statistics:

```
cumulus@switch:~$ nv set system telemetry platform-stats class transceiver-info sample-interval 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Platform Information">}}

To enable platform information statistics, such as the time of last reboot, the last reboot reason, or firmware version:

```
cumulus@switch:~$ nv set system telemetry platform-stats class platform-info state enabled
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
- You can disable BGP export across all VRFs with the `nv set telemetry router bgp export state disabled` command and enable it only for specific VRFs with the `nv set telemetry router vrf <vrf-id> bgp export state enabled` command. 
- You can also disable BGP export across all peers in a VRF with the `nv set telemetry router vrf <vrf-id> bgp export state disabled` command, and enable telemetry only for specific peers in the VRF with the `nv set telemetry router vrf <vrf-id> bgp peer <peer> export state enabled` command.
{{%/notice%}}

To show routing metrics configuration settings, run the `nv show system telemetry router` command.

### Software Statistics

[Software statistics](#software-statistics-format) telemetry currently includes `systemd` unit metrics. When you enable `systemd` metrics, the switch exports unit-level metrics, efficiently reporting only relevant data depending on the service state to ensure minimal performance overhead. You can collect additional `systemd` metrics by enabling process-level metrics.

To enable `systemd` unit metrics:

```
cumulus@switch:~$ nv set system telemetry software-stats systemd export state enabled
cumulus@switch:~$ nv config apply
```

To enable `systemd` process-level statistics:

```
cumulus@switch:~$ nv set system telemetry software-stats systemd process-level enabled 
cumulus@switch:~$ nv config apply
```

You can adjust the software routing statistics sample interval (in seconds). You can specify a value between 60 and 86400. The default setting is 60 seconds.

```
cumulus@switch:~$ nv set system telemetry software-stats systemd sample-interval 100
cumulus@switch:~$ nv config apply
```

By default, the switch collects statistics for the following units:

{{< expand "Units collected by default" >}}
- `asic-monitor.service`
- `frr.service`
- `hostapd.service`
- `hw-management-sync.service`
- `netq-agent.service`
- `netqd.service`
- `nginx.service`
- `ntpsec.service`
- `nv-telemetry.service`
- `nvued.service`
- `prometheus-node-exporter.service`
- `prometheus-sdk-stats.service`
- `ptp4l.service`
- `snmpd.service`
- `switchd.service`
- `sx_sdk.service`
- `wd_keepalive.service`
{{< /expand >}}
<br>
If a `systemd` unit is not active, the switch only collects the unit state, reducing unnecessary data processing.

You can configure custom profiles to collect statistics for specific units. To configure a custom profile, run the `nv set system telemetry software-stats systemd unit-profile <profile-name> unit <unit>` command to provide a custom profile name and the unit you want to monitor. You must then set the custom profile you want to use as the active profile. You can configure multiple units in a custom profile. Only one profile can be active at a time.

The following example configures a custom profile called CUSTOM1 that collects statistics about the NGINX unit and the NVUE unit, and a custom profile called CUSTOM2 that collects statistics about the FRR unit. The example then sets CUSTOM2 as the active profile:

```
cumulus@switch:~$ nv set system telemetry software-stats systemd unit-profile CUSTOM1 unit nginx.service
cumulus@switch:~$ nv set system telemetry software-stats systemd unit-profile CUSTOM1 unit nvued.service
cumulus@switch:~$ nv set system telemetry software-stats systemd unit-profile CUSTOM2 unit frr.service
cumulus@switch:~$ nv set system telemetry software-stats systemd active-profile CUSTOM2
cumulus@switch:~$ nv config apply
```

To show `systemd` software statistics configuration, run the `nv show system telemetry software-stats systemd` command:

```
cumulus@switch:~$ nv show system telemetry software-stats systemd 
                 applied 
---------------  --------
sample-interval  100     
process-level    disabled
active-profile   CUSTOM2 
export                   
  state          enabled 
[unit-profile]   CUSTOM1 
[unit-profile]   CUSTOM2 
[unit-profile]   default
```

To show the default profile and all configured custom profiles, run the `nv show system telemetry software-stats systemd unit-profile` command:

```
cumulus@switch:~$ nv show system telemetry software-stats systemd unit-profile 
         Summary                               
-------  --------------------------------------
CUSTOM1  unit:                    nginx.service
         unit:                    nvued.service
CUSTOM2  unit:                    frr.service
default  unit:             asic-monitor.service
         unit:                      frr.service
         unit:                  hostapd.service
         unit:       hw-management-sync.service
         unit:               netq-agent.service
         unit:                    netqd.service
         unit:                    nginx.service
         unit:                   ntpsec.service
         unit:             nv-telemetry.service
         unit:                    nvued.service
         unit: prometheus-node-exporter.service
         unit:     prometheus-sdk-stats.service
         unit:                    ptp4l.service
         unit:                    snmpd.service
         unit:                  switchd.service
         unit:                   sx_sdk.service
         unit:             wd_keepalive.service
```

To show the units configured for a specific profile, run the `nv show system telemetry software-stats systemd unit-profile <profile-id>` command:

```
cumulus@switch:~$ nv show system telemetry software-stats systemd unit-profile CUSTOM1
        operational    applied      
------  -------------  -------------
[unit]  nginx.service  nginx.service
[unit]  nvued.service  nvued.service
```

To show if {{<link url="#customize-export" text="exporting software statistics is enabled">}}, run the `nv show system telemetry software-stats systemd export` command:

```
cumulus@switch:~$ nv show system telemetry software-stats systemd export  
       applied 
-----  --------
state  enabled
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
   cumulus@switch:~$ nv set system telemetry export otlp grpc certificate <ca-certificate>
   cumulus@switch:~$ nv config apply
   ```

By default, OTLP export is in **secure** mode that requires a CA certificate. For connections without a configured certificate, you must enable `insecure` mode with the `nv set system telemetry export otlp grpc insecure enabled` command.
<!-- POC IN CL5.13
{{%notice note%}}
When you make changes to the open telemetry export destination, connections to the destination do not reset.
{{%/notice%}}
-->
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

The following example:
- Configures STAT-GROUP4 to disable histogram (`histogram`) statistics, and enables LLDP statistics (`lldp-stats`) and software statistics (`software-stats`).
- Sets the sample interval of `lldp` statistics to 40.
- Applies the STAT-GROUP4 configuration to the OTLP destination 10.1.1.30.

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP4 histogram export state disabled
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP4 lldp export state enabled
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP4 lldp sample-interval 40
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP4 software-stats systemd export state enabled
cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.30 stats-group STAT-GROUP4
cumulus@switch:~$ nv config apply
```

The following example:
- Configures STAT-GROUP5 to disable buffer statistics (`buffer-stats`) and enable platform information statistics (`platform-info`).
- Applies the STAT-GROUP5 configuration to the OTLP destination 10.1.1.30.

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP5 buffer-stats export state disabled
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP5 platform-stats class platform-info export state enabled
cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.30 stats-group STAT-GROUP5
cumulus@switch:~$ nv config apply
```

The following example:
- Configures STAT-GROUP6 to export ACL interface statistics.
- Applies the STAT-GROUP6 configuration to the OTLP destination 10.1.1.100.
- Sets the sample interval of the ACL set statistics to 3.

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP6 acl-stats export state enabled
cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.30 stats-group STAT-GROUP6
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP7 acl-stats sample-interval 3  
cumulus@switch:~$ nv config apply
```

The following example:
- Configures STAT-GROUP7 to export ACL set statistics.
- Applies the STAT-GROUP7 configuration to the OTLP destination 10.1.1.200.

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP7 acl-stats class acl-set export state enabled
cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.30 stats-group STAT-GROUP7
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
- Label name and description strings can include alphanumeric characters with underscores, periods, or dashes. If you include spaces in the string, wrap the entire string inside double or single quotes.
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

Validate interface label configuration with the `nv show interface <interface-id> telemetry label` command:

```
cumulus@switch:~$ nv show interface swp10 telemetry label
                       description         
---------------------  --------------------
interface_swp10_label  Server 10 connection
```

## Telemetry Data Format

Cumulus Linux exports statistics and histogram data in the formats defined in this section.

{{%notice note%}}
An asterisk (*) in the `Description` column of the tables below indicates that metric is new for Cumulus Linux 5.15.
{{%/notice%}}

### ACL Statistic Format

The switch collects and exports ACL interface statistics for all the interfaces on which ACLs are applied when you configure the `nv set system telemetry acl-stats export state enabled` command.

| Metric | Description |
| ---------- | ------- |
| `nvswitch_acl_interface_matched_pkts` | Matched packets on all interfaces. |
| `nvswitch_acl_interface_matched_ bytes` | Matched bytes on all interfaces. |

The switch collects and exports statistics for IPv4, IPv6, layer 2, and layer 4 ACLs when you configure the `nv set system telemetry acl-stats class acl-set export state enabled` command.

| Metric | Description |
| ---------- | ------- |
| `nvswitch_acl_set_ipv4_info` | IPv4 ACL information. |
| `nvswitch_acl_set_ipv6_info` | IPv6 ACL information. |
| `nvswitch_acl_set_l2_info` | Layer 2 ACL information. |
| `nvswitch_acl_set_l4_info` | Layer 4 ACL information. |

{{< expand "Example JSON data for nvswitch_acl_interface_matched_pkts:" >}}
```
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_acl_set_ipv4_info:" >}}
```
```
{{< /expand >}}

### AI Ethernet Statistic Format

The switch collects and exports the adaptive routing, SRv6, and packet trimming statistics when you configure the `nv set system telemetry ai-ethernet-stats export state enabled` command.

| Metric | Description |
| ---------- | ------- |
| `nvswitch_ar_congestion_changes`  | Number of adaptive routing change events triggered due to congestion or link-down.|
| `nvswitch_srv6_no_sid_drops`| Number of packets dropped due to no matching SID. |
| `nvswitch_srv6_in_pkts` | Number of packets received for this SID. |
| `nvswitch_qos_trimmed_unicast_pkts`| The Number of packets that were trimmed.|

{{< expand "Example JSON data for nvswitch_ar_congestion_changes:" >}}
```
{
      "name": "nvswitch_ar_congestion_changes",
      "description": "NVIDIA Ethernet Switch Adaptive Routing Congestion Changes counter",
      "sum": {
        "dataPoints": [
          {
            "startTimeUnixNano": "1752704043650000000",
            "timeUnixNano": "1752706797650000000",
            "asDouble": 11051568563473
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
<br>
{{< expand "Example JSON data for nvswitch_srv6_in_pkts:" >}}
```
    {
      "name": "nvswitch_srv6_in_pkts",
      "description": "NVIDIA Ethernet Switch SRv6 Processed Packets per SID",
      "sum": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "sid",
                "value": {
                  "stringValue": "1389:1771:0fa1:0000:0000:0000:0000:0000"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1752704951198000000",
            "timeUnixNano": "1752704981198000000",
            "asDouble": 212
          }
        ]
      }
    }
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_qos_trimmed_unicast_pkts:" >}}
```
{
      "name": "nvswitch_qos_trimmed_unicast_pkts",
      "description": "NVIDIA Ethernet Switch QoS Trimmed Packets",
      "sum": {
        "dataPoints": [
          {
            "startTimeUnixNano": "1753852974184000000",
            "timeUnixNano": "1753852974184000000",
            "asDouble": 15322379
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

### Buffer Statistic Format

The switch collects and exports the following interface and switch, buffer occupancy and watermark statistics when you configure the `nv set system telemetry buffer-stats export state enable` command:

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_shared_buffer_port_pg_time_since_clear` | Time in milliseconds after buffer watermarks last cleared. |
| `nvswitch_interface_shared_buffer_port_pg_curr_occupancy` | Current buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_pg_watermark` | Maximum buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_pg_desc_curr_occupancy` | Current buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_pg_desc_watermark` | Maximum buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_pg_watermark_recorded_max` | Highest maximum buffer occupancy recorded after running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_pg_desc_watermark_recorded_max` | Highest maximum buffer occupancy for descriptors recorded after running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_ingress_pool_curr_occupancy` | Current ingress pool buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_ingress_pool_watermark` | Maximum ingress pool buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_ingress_pool_desc_curr_occupancy` | Current ingress pool buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_ingress_pool_desc_watermark` | Maximum ingress pool buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_ingress_pool_watermark_recorded_max` | Highest maximum ingress pool buffer occupancy recorded after running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_ingress_pool_desc_watermark_recorded_max` | Highest maximum ingress pool buffer occupancy for descriptors recorded after running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_tc_curr_occupancy` | Current buffer occupancy for traffic class. |
| `nvswitch_interface_shared_buffer_port_tc_time_since_clear`| Time in milliseconds after buffer watermarks last cleared. |
| `nvswitch_interface_shared_buffer_port_tc_watermark` | Maximum buffer occupancy for traffic class. |
| `nvswitch_interface_shared_buffer_port_tc_desc_curr_occupancy` | Current buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_tc_desc_watermark` | Maximum buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_tc_watermark_recorded_max` | Highest maximum buffer occupancy recorded after running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_tc_desc_watermark_recorded_max` | Highest maximum buffer occupancy for TC descriptors recorded after running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_egress_pool_curr_occupancy` | Current egress pool buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_egress_pool_watermark` | Maximum egress pool buffer occupancy. |
| `nvswitch_interface_shared_buffer_port_egress_pool_desc_curr_occupancy` | Current egress pool buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_egress_pool_desc_watermark` | Maximum egress pool buffer occupancy for descriptors. |
| `nvswitch_interface_shared_buffer_port_egress_pool_watermark_recorded_max` | Highest maximum egress pool buffer occupancy recorded after running sdk_stats. |
| `nvswitch_interface_shared_buffer_port_egress_pool_desc_watermark_recorded_max` | Highest maximum egress pool buffer occupancy for pool desc recorded after running sdk_stats. |
| `nvswitch_interface_shared_buffer_mc_port_curr_occupancy`  | Current buffer occupancy for multicast port. |
| `nvswitch_interface_shared_buffer_mc_port_watermark` | Maximum buffer occupancy for multicast port. |
| `nvswitch_interface_shared_buffer_mc_port_watermark_max` | Highest maximum buffer occupancy for multicast port recorded after running sdk_stats. |
| `nvswitch_shared_buffer_mc_sp_curr_occupancy` | Current buffer occupancy for multicast switch priority. |
| `nvswitch_shared_buffer_mc_sp_watermark` | Maximum buffer occupancy for multicast switch priority. |
| `nvswitch_shared_buffer_mc_sp_watermark_max` | Highest maximum buffer occupancy for multicast switch priority recorded after running sdk_stats. |
| `nvswitch_shared_buffer_pool_curr_occupancy` | Current pool buffer occupancy. |
| `nvswitch_shared_buffer_pool_watermark` | Maximum pool buffer occupancy |
| `nvswitch_shared_buffer_pool_watermark_max` | Highest maximum pool buffer occupancy for multicast switch priority recorded after running sdk_stats. |
| `nvswitch_interface_headroom_buffer_pg_curr_occupancy` | Current headroom buffer occupancy for port buffer. |
| `nvswitch_interface_headroom_buffer_pg_watermark` | Maximum pool headroom buffer occupancy for port buffer. |
| `nvswitch_interface_headroom_buffer_pg_watermark_recorded_max` | Highest maximum headroom buffer occupancy for port buffer recorded after running sdk_stats. |
| `nvswitch_interface_headroom_shared_buffer_curr_occupancy` | Current headroom buffer occupancy for port shared buffer. |
| `nvswitch_interface_headroom_shared_buffer_watermark` | Maximum headroom buffer occupancy for port shared buffer. |
| `nvswitch_interface_headroom_shared_buffer_watermark_recorded_max` | Highest maximum headroom buffer occupancy for port shared buffer recorded after running sdk_stats. |
| `nvswitch_interface_headroom_buffer_pool_curr_occupancy` | Current headroom buffer occupancy for port shared pool buffer |
| `nvswitch_interface_headroom_buffer_pool_watermark` | Maximum headroom buffer occupancy for port shared pool buffer. |
| `nvswitch_interface_headroom_buffer_pool_watermark_recorded_max` | Highest maximum headroom buffer occupancy for port shared pool buffer. |
| `nvswitch_interface_shared_buffer_port_tc_desc_watermark_recorded_max_bytes` | Interface shared buffer traffic class highest recorded watermark counter in bytes.|
| `nvswitch_interface_shared_buffer_port_pg_watermark_recorded_max_timestamp` | Time when highest shared buffer port group watermark is recorded.|
| `nvswitch_interface_shared_buffer_port_tc_watermark_recorded_max_timestamp` | Time when highest shared buffer traffic class watermark is recorded|
| `nvswitch_interface_shared_buffer_port_ingress_pool_watermark_recorded_max_timestamp` | Time when highest shared pool buffer watermark is recorded.|

<!-- vale off -->
<br>
{{< expand "Example JSON data for nvswitch_interface_shared_buffer_port_tc_time_since_clear:" >}}
```
{
  "name": "nvswitch_interface_shared_buffer_port_tc_time_since_clear",
  "description": "Time in milliseconds since buffer watermarks were last cleared",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          },
          {
            "key": "tc",
            "value": {
              "stringValue": "0"
            }
          }
        ],
        "timeUnixNano": "1745875696361000000",
        "asDouble": 710562
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_shared_buffer_port_pg_time_since_clear:" >}}
```
{
  "name": "nvswitch_interface_shared_buffer_port_pg_time_since_clear",
  "description": "Time in milliseconds since buffer watermarks were last cleared",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          },
          {
            "key": "pg",
            "value": {
              "stringValue": "0"
            }
          }
        ],
        "timeUnixNano": "1745875696361000000",
        "asDouble": 710562
      }
    ]
  }
}
```
{{< /expand >}}

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

### Histogram Data Format
<!-- vale on -->
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
| `nvswitch_histogram_interface_counter_bucket` | Histogram interface counter bucket. |
| `nvswitch_histogram_interface_counter_count` | Histogram interface counter count. |
| `nvswitch_histogram_interface_latency` | Histogram interface latency data. |

<!-- vale off -->
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
      }
    ]
  }
}
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
      }  
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
      }
```

{{< /expand >}}
<!-- vale on -->
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
| `nvswitch_interface_802_dot3_a_frames_transmitted_ok` | Number of 802.3a frames transmitted.|
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
| `nvswitch_interface_ether_stats_pkts64octets` | Total packets received, 64 octets in length. |  
| `nvswitch_interface_ether_stats_pkts65to127octets` | Total packets received, 65 to 127 octets in length. |  
| `nvswitch_interface_ether_stats_pkts128to255octets` | Total packets received, 12 to 255 octets in length. |  
| `nvswitch_interface_ether_stats_pkts256to511octets` | Total packets received, 256 to 511 octets in length. |  
| `nvswitch_interface_ether_stats_pkts512to1023octets` | Total packets received, 512 to 1023 octets in length. |  
| `nvswitch_interface_ether_stats_pkts1024to1518octets` | Total packets received, 1024 to 1518 octets in length. |  
| `nvswitch_interface_ether_stats_pkts1519to2047octets` | Total packets received, 1519 to 2047 octets in length. |  
| `nvswitch_interface_ether_stats_pkts2048to4095octets` | Total packets received, 2048 to 4095 octets in length. |  
| `nvswitch_interface_ether_stats_pkts4096to8191octets` | Total packets received, 4096 to 8191 octets in length. |  
| `nvswitch_interface_ether_stats_pkts8192to10239octets` | Total packets received, 8192 to 10239 octets in length. |
| `nvswitch_interface_carrier_up_changes_total` | Total number of carrier up transitions for the interface. |
| `nvswitch_interface_carrier_last_change_time_ms` | Time of last carrier change for the interface as Unix epoch timestamp, with millisecond granularity. |
|`nvswitch_interface_ether_stats_broadcast_pkts` | The total number of good packets received and directed to the broadcast address.|
| `nvswitch_interface_ether_stats_collisions` |The best estimate of the total number of collisions on this Ethernet segment.|
| `nvswitch_interface_ether_stats_crc_align_errors` | The total number of packets received that had a length (excluding framing bits, but including FCS octets) of between 64 and MTU octets, inclusive, but had either a bad frame check sequence (FCS) with an integral number of octets (FCS error) or a bad FCS with a non-integral number of octets (alignment error).|
| `nvswitch_interface_ether_stats_drop_events` | The total number of events in which packets are dropped due to lack of resources. |
| `nvswitch_interface_ether_stats_fragments` | The total number of packets received that were less than 64 octets in length (excluding framing bits but including FCS octets) and had either a bad FCS with an integral number of octets (FCS error) or a bad FCS with a non- integral number of octets (alignment error).|
| `nvswitch_interface_ether_stats_jabbers` | The total number of packets received that were longer than MTU octets (excluding framing bits, but including FCS octets), and had either a bad FCS with an integral number of octets (FCS error) or a bad FCS with a non-integral number of octets (alignment error).|
| `nvswitch_interface_ether_stats_multicast_pkts` | The total number of good packets received and directed to a multicast MAC address. This number does not include packets directed to the broadcast address. |
| `nvswitch_interface_ether_stats_octets` | The total number of octets of data (including those in bad packets) received (excluding framing bits but including FCS octets). |
| `nvswitch_interface_ether_stats_oversize_pkts` | The total number of packets received that were longer than MTU octets (excluding framing bits, but including FCS octets) but were otherwise well formed. |
| `nvswitch_interface_ether_stats_pkts` | The total number of packets (including bad packets, broadcast packets, and multicast packets) received. |
| `nvswitch_interface_ether_stats_undersize_pkts` | The total number of packets received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed. |
| `nvswitch_interface_if_out_ucast_pkts` | The total number of packets that higher-level protocols requested to be transmitted and were not addressed to a multicast or broadcast MAC address, including discarded packets or those not sent. |
| `nvswitch_interface_no_buffer_discard_mc` | The number of multicast packets dropped due to lack of egress buffer resources. Valid only for Spectrum. |
| `nvswitch_interface_rx_buffer_almost_full` | The number of events where the port rx buffer has passed a fullness threshold. |
| `nvswitch_interface_rx_buffer_full` |The number of events where the port rx buffer has reached 100% fullness. |
| `nvswitch_interface_rx_ebp` | The number of received EBP packets. |
| `nvswitch_interface_tx_ebp` | The number of transmitted EBP packets. |
| `nvswitch_interface_tx_int_cksm_err` | Counter increments when there is a packet payload internal checksum error. |
| `nvswitch_interface_tx_stats_pkts64octets` | Total packets transmitted, 64 octets in length. |  
| `nvswitch_interface_tx_stats_pkts65to127octets`| Total packets transmitted, 65 to 127 octets in length. |
| `nvswitch_interface_tx_stats_pkts128to255octets`| Total packets transmitted, 128 to 255 octets in length.|
| `nvswitch_interface_tx_stats_pkts256to511octets` | Total packets transmitted, 256 to 511 octets in length.|
| `nvswitch_interface_tx_stats_pkts512to1023octets` | Total packets transmitted, 512 to 1023 octets in length. |
| `nvswitch_interface_tx_stats_pkts1024to1518octets` | Total packets transmitted, 1024 to 1518 octets in length.|
| `nvswitch_interface_tx_stats_pkts1519to2047octets` | Total packets transmitted, 1519 to 2047 octets in length.|
| `nvswitch_interface_tx_stats_pkts2048to4095octets` | Total packets transmitted, 2048 to 4095 octets in length.|
| `nvswitch_interface_tx_stats_pkts4096to8191octets` | Total packets transmitted, 4096 to 8191 octets in length.|
| `nvswitch_interface_tx_stats_pkts8192to10239octets` | Total packets transmitted, 8192 to 10239 octets in length.|
| `nvswitch_interface_tx_wait` | The time (in ns resolution) during which the port selected has data to transmit but no data was sent.|
| `nvswitch_interface_carrier_down_changes_total` | Total number of carrier down transitions for the interface. |
| `nvswitch_interface_carrier_changes_total` | Total number of carrier changes for the interface. |
| `nvswitch_interface_mtu_bytes` | Operational MTU for the interface in bytes. |
| `nvswitch_interface_info` | Provides information about the interface: MAC address, duplex, ifalias, interface name, operstate. |
| `nvswitch_interface_iface_id` | The ifindex for the interface. |
| `nvswitch_interface_flags` | Kernel device flags set for an interface as an integer representing the {{<exlink url="https://github.com/torvalds/linux/blob/c1e939a21eb111a6d6067b38e8e04b8809b64c4e/include/uapi/linux/if.h#L43" text="kernel `net_device` flags bitmask">}}. |
| `nvswitch_interface_proto_down` | Interface protocol down status. |
| `nvswitch_interface_oper_aggregate_speed` | Speed in bits per second for the connected interface. |
| `nvswitch_interface_number_of_lanes` | Number of lanes used by the interface. |
| `nvswitch_interface_if_in_broadcast_pkts` | Number of interface in broadcast packets. |
| `nvswitch_interface_if_in_discards` | Number of interface in discards.|
| `nvswitch_interface_if_in_errors`| Number of interface in errors.|
| `nvswitch_interface_if_in_multicast_pkts`| Number of interface in multicast packets.|
| `nvswitch_interface_if_in_octets`| Number of interface in octets.|
| `nvswitch_interface_if_in_ucast_pkts`| Number of interface in unicast packets.|
| `nvswitch_interface_if_in_unknown_protos` | Number of interface in unknown protocols.|
| `nvswitch_interface_if_out_broadcast_pkts`| Number of interface out broadcast packets. |
| `nvswitch_interface_if_out_discards` | Number of interface out discards.|
| `nvswitch_interface_if_out_errors` | Number of interface out errors. |
| `nvswitch_interface_if_out_multicast_pkts`|Number of interface out multicast packets. |
| `nvswitch_interface_if_out_octets`| Number of interface out octets.|
| `nvswitch_interface_if_out_octets`| Number of interface out unicast packets.|
| `nvswitch_interface_type`|Link-layer interface type.|
| `nvswitch_interface_ether_stats_jabbers` | Jabber frames receiverd on this interface.|
| `nvswitch_interface_hw_address_info` | System defined default MAC address for the interface.|

{{< /tab >}}
{{< tab "Traffic Class ">}}

The switch collects and exports the following additional interface traffic class statistics when you configure the `nv set system telemetry interface-stats egress-buffer traffic-class <class>` command:

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_tc_tx_bc_frames` | Interface egress traffic class transmit broadcast frames counter. |
| `nvswitch_interface_tc_tx_ecn_marked_tc` | Interface egress traffic class transmit ECN marked counter. |
| `nvswitch_interface_tc_tx_frames` | Interface egress traffic class transmit frames counter. |
| `nvswitch_interface_tc_tx_mc_frames` | Interface egress traffic class transmit multicast frames counter. |
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
| `nvswitch_interface_sp_rx_pause_duration` | Receive pause duration counter for the switch priority. |
| `nvswitch_interface_sp_rx_pause_transition` | Receive pause transition counter for the switch priority. |
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
| `nvswitch_interface_phy_stats_phy_effective_errors` | Number of errors after applying FEC. |
| `nvswitch_interface_phy_stats_phy_raw_errors` | Error bits identified on lane 0 through lane 7. When you enable FEC, this induction corresponds to corrected errors. |
| `nvswitch_interface_phy_stats_raw_ber` | raw_ber_coef_laneX*10^(raw_ber_magnitude) |
| `nvswitch_interface_phy_stats_symbol_ber` | Symbol BER errors. |
| `nvswitch_interface_phy_layer_time_since_last_clear` | Time after counters clear.|
| `nvswitch_interface_phy_layer_fec_per_lane_corrections` | FEC corrections per lane. |
| `nvswitch_interface_phy_layer_fec_block_state_count`| Number of FEC block states.|
| `nvswitch_interface_phy_stats_phy_corrected_bits` | Corrected bits by FEC engine. |
| `nvswitch_interface_phy_stats_time_since_last_clear` | Time after counters clear.|
| `nvswitch_interface_phy_stats_effective_ber` | FEC BER errors. |
| `nvswitch_interface_phy_rs_fec_histogram` | Firmware version information for the transceiver.|

{{< /tab >}}
{{< /tabs >}}

#### Interface Example JSON
<!-- vale off -->
{{< expand "Example JSON data for nvswitch_interface_oper_state:" >}}
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
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_dot3_stats_fcs_errors:" >}}
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
  }
}
```

{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_in_broadcast_pkts:" >}}
```
{
  "name": "nvswitch_interface_if_in_broadcast_pkts",
  "description": "NVIDIA Ethernet Switch Interface if in broadcast pkts counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875601233000000",
        "asDouble": 0
      },
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s1"
            }
          }
        ],
        "timeUnixNano": "1745875601233000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_in_discards:" >}}
```
{
  "name": "nvswitch_interface_if_in_discards",
  "description": "NVIDIA Ethernet Switch Interface if in discards counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875691233000000",
        "asDouble": 0
      },
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s1"
            }
          }
        ],
        "timeUnixNano": "1745875691233000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_in_errors:" >}}
```
{
  "name": "nvswitch_interface_if_in_errors",
  "description": "NVIDIA Ethernet Switch Interface if in errors counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875520233000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_in_multicast_pkts:" >}}
```
{
  "name": "nvswitch_interface_if_in_multicast_pkts",
  "description": "NVIDIA Ethernet Switch Interface if in multicast pkts counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875325232000000",
        "asDouble": 11
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_in_octets:" >}}
```
{
  "name": "nvswitch_interface_if_in_octets",
  "description": "NVIDIA Ethernet Switch Interface if in octets counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875331232000000",
        "asDouble": 3758
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_in_ucast_pkts:" >}}
```
{
  "name": "nvswitch_interface_if_in_ucast_pkts",
  "description": "NVIDIA Ethernet Switch Interface if in ucast pkts counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875646233000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_in_unknown_protos:" >}}
```
{
  "name": "nvswitch_interface_if_in_unknown_protos",
  "description": "NVIDIA Ethernet Switch Interface if in unknown protos counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_out_broadcast_pkts:" >}}
```
{
  "name": "nvswitch_interface_if_out_broadcast_pkts",
  "description": "NVIDIA Ethernet Switch Interface if out broadcast pkts counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_out_discards:" >}}
```
{
  "name": "nvswitch_interface_if_out_discards",
  "description": "NVIDIA Ethernet Switch Interface if out discards counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875256232000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_out_errors:" >}}
```
{
  "name": "nvswitch_interface_if_out_errors",
  "description": "NVIDIA Ethernet Switch Interface if out errors counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_out_multicast_pkts:" >}}
```
{
  "name": "nvswitch_interface_if_out_multicast_pkts",
  "description": "NVIDIA Ethernet Switch Interface if out multicast pkts counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 22
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_out_octets:" >}}
```
{
  "name": "nvswitch_interface_if_out_octets",
  "description": "NVIDIA Ethernet Switch Interface if out octets counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 4928
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_if_out_ucast_pkts:" >}}
```
{
  "name": "nvswitch_interface_if_out_ucast_pkts",
  "description": "NVIDIA Ethernet Switch Interface if out ucast pkts counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_802_dot3_a_frames_transmitted_ok:" >}}
```
{
  "name": "nvswitch_interface_802_dot3_a_frames_transmitted_ok",
  "description": "NVIDIA Ethernet Switch Interface 802.3a frames transmitted ok counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 22
      },
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s1"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 22
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_ether_stats_jabbers:" >}}
```
 {
      "name": "nvswitch_interface_ether_stats_jabbers",
      "description": "NVIDIA Ethernet Switch Interface ether stats jabbers counter",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp1s0"
                }
              }
            ],
            "timeUnixNano": "1753901194269000000",
            "asDouble": 0
          },
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp1s1"
                }
              }
            ],
            "timeUnixNano": "1753901194269000000",
            "asDouble": 0
          },
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp1s2"
                }
              }
            ],
            "timeUnixNano": "1753901194269000000",
            "asDouble": 0
          },
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp1s3"
                }
              }
            ],
            "timeUnixNano": "1753901194269000000",
            "asDouble": 0
          },
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp61s0"
                }
              }
            ],
            "timeUnixNano": "1753901194269000000",
            "asDouble": 0
          },
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp61s1"
                }
              }
            ],
            "timeUnixNano": "1753901194269000000",
            "asDouble": 0
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
    }
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_hw_address_info:" >}}
```
{
      "name": "nvswitch_interface_hw_address_info",
      "description": "Hardware (MAC) address information for network interface.",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "address",
                "value": {
                  "stringValue": "1c:34:da:28:01:00"
                }
              },
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp35"
                }
              }
            ],
            "timeUnixNano": "1753901194568000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "address",
                "value": {
                  "stringValue": "1c:34:da:28:01:02"
                }
              },
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp36"
                }
              }
            ],
            "timeUnixNano": "1753901194568000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "address",
                "value": {
                  "stringValue": "1c:34:da:28:01:04"
                }
              },
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp33"
                }
              }
            ],
            "timeUnixNano": "1753901194568000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "address",
                "value": {
                  "stringValue": "1c:34:da:28:01:06"
                }
              },
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp34"
                }
              }
            ],
            "timeUnixNano": "1753901194568000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "address",
                "value": {
                  "stringValue": "1c:34:da:28:01:08"
                }
              },
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp39"
                }
              }
            ],
            "timeUnixNano": "1753901194568000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "address",
                "value": {
                  "stringValue": "1c:34:da:28:01:0a"
                }
              },
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp40"
                }
              }
...
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_type:" >}}
```
{
      "name": "nvswitch_interface_type",
      "description": "Network device property: type",
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
            "timeUnixNano": "1753901194568000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp11"
                }
              }
            ],
            "timeUnixNano": "1753901194568000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp12"
                }
              }
            ],
            "timeUnixNano": "1753901194568000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp13"
                }
              }
            ],
            "timeUnixNano": "1753901194568000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp14"
                }
              }
            ],
            "timeUnixNano": "1753901194568000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "interface",
                "value": {
                  "stringValue": "swp15"
                }
              }
...
```
{{< /expand >}}

#### PHY Example JSON

{{< expand "Example JSON data for nvswitch_interface_phy_layer_fec_block_state_count:" >}}
```
{
  "name": "nvswitch_interface_phy_layer_fec_block_state_count",
  "description": "NVIDIA Ethernet Switch Interface phy layer FEC block state counter",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          },
          {
            "key": "mechanism",
            "value": {
              "stringValue": "rs"
            }
          },
          {
            "key": "state",
            "value": {
              "stringValue": "clean"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_phy_layer_fec_per_lane_corrections:" >}}
```
{
  "name": "nvswitch_interface_phy_layer_fec_per_lane_corrections",
  "description": "NVIDIA Ethernet Switch Interface phy layer FEC corrections for lane",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          },
          {
            "key": "lane",
            "value": {
              "stringValue": "0"
            }
          },
          {
            "key": "mechanism",
            "value": {
              "stringValue": "fc"
            }
          },
          {
            "key": "state",
            "value": {
              "stringValue": "corrected"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 0
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_phy_layer_time_since_last_clear:" >}}
```
{
  "name": "nvswitch_interface_phy_layer_time_since_last_clear",
  "description": "NVIDIA Ethernet Switch Interface phy layer time since counters were cleared",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 494848
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_phy_stats_effective_ber:" >}}
```
{
  "name": "nvswitch_interface_phy_stats_effective_ber",
  "description": "NVIDIA Ethernet Switch Interface phy effective BER errors",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 1.4999999999999995e-254
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_interface_phy_stats_symbol_ber:" >}}
```
{
  "name": "nvswitch_interface_phy_stats_symbol_ber",
  "description": "NVIDIA Ethernet Switch Interface phy symber BER errors",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "interface",
            "value": {
              "stringValue": "swp1s0"
            }
          }
        ],
        "timeUnixNano": "1745875697233000000",
        "asDouble": 1.4999999999999995e-254
      }
    ]
  }
}
```
{{< /expand >}}
<!-- vale on -->
### LLDP Statistic Format

When you enable LLDP statistic telemetry, the switch exports the following statistics:

| Name | Description |
|----- | ----------- |
| `nvswitch_lldp_chassis_info` | LLDP chassis information. |
| `nvswitch_lldp_chassis_capabilities` | LLDP chassis capabilities as a bitmap. IEEE 802.1AB defines the capabilities.|
| `nvswitch_lldp_neighbor_age` | LLDP neighbor age information in seconds.|
| `nvswitch_lldp_neighbor_capabilities` | LLDP neighbor capabilities as a bitmap. IEEE 802.1AB defines the capabilities. |
| `nvswitch_lldp_neighbor_info` | LLDP neighbor information.|
| `nvswitch_lldp_neighbor_ttl` | LLDP neighbor port TTL in seconds.|
| `nvswitch_lldp_neighbor_management_address-info` | LLDP neighbor management address information.|
| `nvswitch_lldp_interface_enabled` | Per-directional status on whether LLDP is enabled per interface.|

{{< expand "Example JSON data for nvswitch_lldp_chassis_info:" >}}

```
{
  "name": "nvswitch_lldp_chassis_info",
  "description": "NVIDIA Ethernet Switch LLDP Chassis information",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "chassis_id",
            "value": {
              "stringValue": "94:6d:ae:ab:00:ea"
            }
          },
          {
            "key": "chassis_id_type",
            "value": {
              "stringValue": "mac"
            }
          },
          {
            "key": "system_description",
            "value": {
              "stringValue": "Cumulus Linux version 5.13.0 running on Nvidia SN5600"
            }
          },
          {
            "key": "system_name",
            "value": {
              "stringValue": "mlx-5600-12"
            }
          }
        ],
        "timeUnixNano": "1745868046553000000",
        "asDouble": 1
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_lldp_chassis_capabilities:" >}}
```
{
    "name": "nvswitch_lldp_chassis_capabilities",
    "description": "NVIDIA Ethernet Switch LLDP Chassis Capabilities as a bitmap. The capabilities are defined in IEEE 802.1AB",
    "gauge": {
      "dataPoints": [
        {
          "attributes": [
            {
              "key": "chassis_id",
              "value": {
                "stringValue": "94:6d:ae:ab:00:ea"
              }
            },
            {
              "key": "system_name",
              "value": {
                "stringValue": "mlx-5600-12"
              }
            }
          ],
          "timeUnixNano": "1745868428817000000",
          "asDouble": 16
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
  }
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_lldp_neighbor_age:" >}}
```
  {
    "name": "nvswitch_lldp_neighbor_age",
    "description": "NVIDIA Ethernet Switch LLDP Neighbor Age in seconds",
    "sum": {
      "dataPoints": [
        {
          "attributes": [
            {
              "key": "interface",
              "value": {
                "stringValue": "swp10s0"
              }
            },
            {
              "key": "port_id",
              "value": {
                "stringValue": "swp10s0"
              }
            },
            {
              "key": "system_name",
              "value": {
                "stringValue": "mlx-5600-13"
              }
            },
            {
              "key": "mgmtVrfNoTls-l1",
              "value": {
                "stringValue": "Management VRF Insecure Label-1"
              }
            }
          ],
          "startTimeUnixNano": "1745866926553000000",
          "timeUnixNano": "1745868457768000000",
          "asDouble": 2608
        }
      ]
    }
  }
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_lldp_neighbor_capabilities:" >}}

```
{
    "name": "nvswitch_lldp_neighbor_capabilities",
    "description": "NVIDIA Ethernet Switch LLDP Neighbor Capabilities as a bitmap. The capabilities are defined in IEEE 802.1AB",
    "gauge": {
      "dataPoints": [
        {
          "attributes": [
            {
              "key": "interface",
              "value": {
                "stringValue": "swp10s0"
              }
            },
            {
              "key": "port_id",
              "value": {
                "stringValue": "swp10s0"
              }
            },
            {
              "key": "system_name",
              "value": {
                "stringValue": "mlx-5600-13"
              }
            },
            {
              "key": "mgmtVrfNoTls-l1",
              "value": {
                "stringValue": "Management VRF Insecure Label-1"
              }
            }
          ],
          "timeUnixNano": "1745868465982000000",
          "asDouble": 20
        }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_lldp_neighbor_info:" >}}
```
{
    "name": "nvswitch_lldp_neighbor_info",
    "description": "NVIDIA Ethernet Switch LLDP Neighbor information",
    "gauge": {
      "dataPoints": [
        {
          "attributes": [
            {
              "key": "chassis_id",
              "value": {
                "stringValue": "94:6d:ae:ab:00:42"
              }
            },
            {
              "key": "chassis_id_type",
              "value": {
                "stringValue": "mac"
              }
            },
            {
              "key": "interface",
              "value": {
                "stringValue": "swp10s0"
              }
            },
            {
              "key": "port_description",
              "value": {
                "stringValue": "swp10s0"
              }
            },
            {
              "key": "port_id",
              "value": {
                "stringValue": "swp10s0"
              }
            },
            {
              "key": "port_id_type",
              "value": {
                "stringValue": "ifname"
              }
            },
            {
              "key": "system_description",
              "value": {
                "stringValue": "Cumulus Linux version 5.13.0 running on Nvidia SN5600"
              }
            },
            {
              "key": "system_name",
              "value": {
                "stringValue": "mlx-5600-13"
              }
            },
            {
              "key": "mgmtVrfNoTls-l1",
              "value": {
                "stringValue": "Management VRF Insecure Label-1"
              }
            }
          ],
          "timeUnixNano": "1745868465982000000",
          "asDouble": 1
        }
    }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_lldp_neighbor_ttl:" >}}
```
{
    "name": "nvswitch_lldp_neighbor_ttl",
    "description": "NVIDIA Ethernet Switch LLDP Neighbor Port TTL in seconds",
    "gauge": {
      "dataPoints": [
        {
          "attributes": [
            {
              "key": "interface",
              "value": {
                "stringValue": "eth0"
              }
            },
            {
              "key": "port_id",
              "value": {
                "stringValue": "swp26"
              }
            },
            {
              "key": "system_name",
              "value": {
                "stringValue": "removed_for_privacy"
              }
            }
          ],
          "timeUnixNano": "1745868465982000000",
          "asDouble": 120
        }
      ]
    }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_lldp_neighbor_management_address_info:" >}}
```
{
    "name": "nvswitch_lldp_neighbor_management_address_info",
    "description": "NVIDIA Ethernet Switch LLDP Neighbor Management Address Information",
    "gauge": {
      "dataPoints": [
        {
          "attributes": [
            {
              "key": "interface",
              "value": {
                "stringValue": "eth0"
              }
            },
            {
              "key": "management_address",
              "value": {
                "stringValue": "10.112.129.193"
              }
            },
            {
              "key": "management_address_type",
              "value": {
                "stringValue": "IPv4"
              }
            },
            {
              "key": "port_id",
              "value": {
                "stringValue": "swp26"
              }
            },
            {
              "key": "system_name",
              "value": {
                "stringValue": "removed_for_privacy"
              }
            }
          ],
          "timeUnixNano": "1745868478250000000",
          "asDouble": 1
        }
      ]
    }
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
| `node_disk_discards_completed_total` | Total number of discards completed. |  
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
| `node_memory_Buffers_bytes` | `/proc/meminfo` Buffers bytes. |
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
| `nvswitch_platform_environment_fan_cur_speed` | Current fan speed in RPM. |  
| `nvswitch_platform_environment_fan_dir` | Fan direction (0: Front2Back, 1: Back2Front). | 
| `nvswitch_platform_environment_fan_max_speed` | Fan maximum speed in RPM. | 
| `nvswitch_platform_environment_fan_min_speed` | Fan minimum speed in RPM. |  
| `nvswitch_platform_environment_fan_state` | Fan status (0: ABSENT, 1: OK, 2: FAILED, 3: BAD). | 
| `nvswitch_platform_environment_psu_capacity` | PSU capacity in watts. | 
| `nvswitch_platform_environment_psu_current` | PSU current in amperes. | 
| `nvswitch_platform_environment_psu_power` | PSU power in watts. | 
| `nvswitch_platform_environment_psu_state` | PSU state (0: ABSENT, 1: OK, 2: FAILED, 3: BAD). | 
| `nvswitch_platform_environment_psu_voltage` | PSU voltage in volts. | 
| `nvswitch_platform_environment_temp_crit` | Critical temperature threshold in centigrade. | 
| `nvswitch_platform_environment_temp_current` | Current temperature in centigrade. | 
| `nvswitch_platform_environment_temp_max` | Maximum temperature threshold in centigrade. | 
| `nvswitch_platform_environment_temp_min` | Minimum temperature threshold in centigrade. | 
| `nvswitch_platform_environment_temp_state` | Temperature sensor status (0: ABSENT, 1: OK, 2: FAILED, 3: BAD). |
| `nvswitch_platform_evironment_input_voltage` | Input voltage to the PSU.|
| `nvswitch_platform_environment_input_current` | Input current to the PSU.|

{{< /tab >}}
{{< tab "Transceivers ">}}

| Metric | Description |
| ---------- | ------- |
| `nvswitch_platform_transceiver_vendor_info` | The transceiver vendor information, such as which port the transceiver plugs into, the date of manufacture, the revision, the name of the manufacturer, the manufacturer part number, the serial number, and the IEEE company ID of the vendor.  |
| `nvswitch_platform_transceiver_info` | General information for the transceiver, such as which port the transceiver plugs into, the cable type, the cable length in meters, the status (plugged-enabled, plugged-disabled, plugged-error, or unplugged), the error status, the identifier, and the Ethernet compliance revision. |
| `nvswitch_platform_transceiver_temperature` |The temperature of the module in Celsius as a 64bit decimal value. |
| `nvswitch_platform_transceiver_temperature_alarm`| The alarm status due to temperature crossing thresholds defined for the module. The value sent for the temperature alarm is a bit mask:<br> Bit 0: high_temp_alarm<br>Bit 1: low_temp_alarm<br>Bit 2: high_temp_warning<br>Bit 3: low_temp_warning  |
| `nvswitch_platform_transceiver_temperature_threshold_info`| Temperature thresholds defined for the module (low or high). |
| `nvswitch_platform_transceiver_voltage` | The internally measured supply voltage for the module in volts (a 64bit decimal value). |
| `nvswitch_platform_transceiver_voltage_alarm` | The alarm status due to Voltage crossing thresholds defined for the module:<br>Bit 0: high_vcc_alarm<br>Bit 1: low_vcc_alarm<br>Bit 2: high_vcc_warning<br>Bit 3: low_vcc_warning |
| `nvswitch_platform_transceiver_voltage_threshold_info` | Voltage thresholds defined for the module. The level is alarm or warning. The threshold is low or high.|
| `nvswitch_platform_transceiver_channel_power` | The transceiver channel power value in dBm units (logarithmic scale) for each channel in both rx and tx directions.|
| `nvswitch_platform_transceiver_channel_power_alarm` | The alarm state for power value compared with the defined thresholds for the module as a bit mask value for each channel and for both rx and tx directions:<br>Bit 0: tx_power_hi_al<br>Bit 1: l tx_power_lo_al<br>Bit 2: tx_power_hi_war<br>Bit 3: l tx_power_lo_war. |
| `nvswitch_platform_transceiver_power_threshold_info` | Threshold information for the power for both rx and tx directions. These threshold values are applicable for all channels. The units are in dBm and represented by a 32bit decimal value. |
| `nvswitch_platform_transceiver_channel_tx_bias_current` | tx bias current measured for the channel in Amps units and represented by a 32bit decimal value. |
| `nvswitch_platform_transceiver_channel_tx_bias_current_alarm` | tx bias current alarm state of tx bias current measure for the channel when compared to the threshold values for the channel defined for the module. This is a bit mask value:<br>Bit 0: tx_bias_hi_al<br>Bit 1: l tx_bias_lo_al<br>Bit 2: tx_bia_hi_war<br>Bit 3: l tx_bias_lo_war |
| `nvswitch_platform_transceiver_channel_tx_bias_current_threshold_info` | tx bias current thresholds defined for the channel in Amps units and represented by a 32bit decimal value. |
| `nvswitch_platform_transceiver_firmware_version`| Firmware version information for the transceiver.|
| `nvswitch_platform_transceiver_info` | General information for the transceiver.|
| `nvswitch_platform_transceiver_ethernet_pmd` | Ethernet PMD information for the transceiver.|
| `nvswitch_platform_transceiver_physical_channel_state` | Per physical channel LOS and CDR LOL state.|
| `nvswitch_platform_transceiver_host_lane_state` | Per host lane LOS and CDR LOL state.|
| `nvswitch_platform_transceiver_voltage` | Input voltage as measured by the transceiver |

{{< /tab >}}
{{< tab "Platform Information ">}}

| Metric | Description |
| ---------- | ------- |
| `nvswitch_platform_info_last_reboot_time` | Time of last reboot in ns since epoch.|
| `nvswitch_platform_info_last_reboot_reason` | Information about the last reboot reason of a component.|
| `nvswitch_platform_info_firmware_version` | Information about the firmware version of a component.|

{{< /tab >}}
{{< /tabs >}}

#### Environment Sensor Example JSON
<!-- vale off -->
{{< expand "Example JSON data for nvswitch_platform_environment_psu_state:" >}}

```
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
}
```

{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_environment_temp_crit:" >}}

```
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
}
```

{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_environment_temp_current:" >}}

```
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
}
```

{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_environment_temp_current:" >}}

```
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
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_environment_psu_input_voltage:" >}}
```
{
      "name": "nvswitch_platform_environment_psu_input_voltage",
      "description": "PSU input voltage in Volts.",
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
            "timeUnixNano": "1753901249206000000",
            "asDouble": 239.5
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
            "timeUnixNano": "1753901249206000000",
            "asDouble": 240
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
...
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_environment_psu_input_current:" >}}
```
{
      "name": "nvswitch_platform_environment_psu_input_current",
      "description": "PSU input current in Amperes.",
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
            "timeUnixNano": "1753901249206000000",
            "asDouble": 10
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
            "timeUnixNano": "1753901249206000000",
            "asDouble": 11.75
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
```
{{< /expand >}}

#### Transceiver Example JSON

{{< expand "Example JSON data for nvswitch_platform_transceiver_info:" >}}
```
{
      "name": "nvswitch_platform_transceiver_info",
      "description": "NVIDIA Ethernet Switch Transceiver Information",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "cable_length",
                "value": {
                  "stringValue": "2.0m"
                }
              },
              {
                "key": "cable_type",
                "value": {
                  "stringValue": "Passive copper cable"
                }
              },
              {
                "key": "error_status",
                "value": {
                  "stringValue": "N/A"
                }
              },
              {
                "key": "identifier",
                "value": {
                  "stringValue": "OSFP"
                }
              },
              {
                "key": "name",
                "value": {
                  "stringValue": "transceiver36"
                }
              },
              {
                "key": "port",
                "value": {
                  "stringValue": "36"
                }
              },
              {
                "key": "revision_compliance",
                "value": {
                  "stringValue": "Rev 5.0"
                }
              },
              {
                "key": "status",
                "value": {
                  "stringValue": "plugged, enabled"
                }
              }
            ],
            "timeUnixNano": "1753399762615000000",
            "asDouble": 1
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
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_transceiver_voltage:" >}}
```
    {
      "name": "nvswitch_platform_transceiver_voltage",
      "description": "NVIDIA Ethernet Switch Transceiver Voltage in V",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "name",
                "value": {
                  "stringValue": "transceiver33"
                }
              },
              {
                "key": "port",
                "value": {
                  "stringValue": "33"
                }
              }
            ],
            "timeUnixNano": "1753399700615000000",
            "asDouble": 3.2324
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
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_transceiver_firmware_version:" >}}
```
    {
      "name": "nvswitch_platform_transceiver_firmware_version",
      "description": "NVIDIA Ethernet Switch Transceiver Firmware Version",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "fw_version",
                "value": {
                  "stringValue": "47.171.10"
                }
              },
              {
                "key": "name",
                "value": {
                  "stringValue": "transceiver33"
                }
              },
              {
                "key": "port",
                "value": {
                  "stringValue": "33"
                }
              }
            ],
            "timeUnixNano": "1753399700615000000",
            "asDouble": 1
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
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_transceiver_ethernet_pmd:" >}}
```
    {
      "name": "nvswitch_platform_transceiver_ethernet_pmd",
      "description": "NVIDIA Ethernet Switch Transceiver Ethernet PMD Type",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "name",
                "value": {
                  "stringValue": "transceiver9"
                }
              },
              {
                "key": "pmd_type",
                "value": {
                  "stringValue": "400G_AUI4_CR4"
                }
              },
              {
                "key": "port",
                "value": {
                  "stringValue": "9"
                }
              }
            ],
            "timeUnixNano": "1753399700615000000",
            "asDouble": 1
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
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_transceiver_physical_channel_state:" >}}
```
    {
      "name": "nvswitch_platform_transceiver_physical_channel_state",
      "description": "NVIDIA Ethernet Switch Transceiver Physical Channel State (rx-los, rx-cdr-lol)",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "channel",
                "value": {
                  "stringValue": "1"
                }
              },
              {
                "key": "name",
                "value": {
                  "stringValue": "transceiver33"
                }
              },
              {
                "key": "port",
                "value": {
                  "stringValue": "33"
                }
              },
              {
                "key": "state",
                "value": {
                  "stringValue": "rx-cdr-lol"
                }
              }
            ],
            "timeUnixNano": "1753399700615000000",
            "asDouble": 0
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
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_transceiver_host_lane_state:" >}}
```
    {
      "name": "nvswitch_platform_transceiver_host_lane_state",
      "description": "NVIDIA Ethernet Switch Transceiver Host Lane State (tx-los, tx-cdr-lol)",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "lane",
                "value": {
                  "stringValue": "1"
                }
              },
              {
                "key": "name",
                "value": {
                  "stringValue": "transceiver33"
                }
              },
              {
                "key": "port",
                "value": {
                  "stringValue": "33"
                }
              },
              {
                "key": "state",
                "value": {
                  "stringValue": "tx-cdr-lol"
                }
              }
            ],
            "timeUnixNano": "1753399700615000000",
            "asDouble": 0
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
    }
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_platform_transceiver_vendor_info:" >}}
```
{
    "name": "nvswitch_platform_transceiver_vendor_info",
    "description": "NVIDIA Ethernet Switch Transceiver Vendor Information",
    "gauge": {
      "dataPoints": [
        {
          "attributes": [
            {
              "key": "date_code",
              "value": {
                "stringValue": "220705"
              }
            },
            {
              "key": "name",
              "value": {
                "stringValue": "transceiver1"
              }
            },
            {
              "key": "name_name",
              "value": {
                "stringValue": "NVIDIA"
              }
            },
            {
              "key": "oui",
              "value": {
                "stringValue": "48:B0:2D"
              }
            },
            {
              "key": "part_no",
              "value": {
                "stringValue": "MCP4Y10-N001"
              }
            },
            {
              "key": "port",
              "value": {
                "stringValue": "1"
              }
            },
            {
              "key": "rev",
              "value": {
                "stringValue": "A3"
              }
            },
            {
              "key": "serial_no",
              "value": {
                "stringValue": "MT2230VS00663"
              }
            }
          ],
          "timeUnixNano": "1745875376987000000",
          "asDouble": 1
        }
      ]
    }
  }
```
{{< /expand >}}

### Routing Metrics Format

When you enable layer 3 routing metrics telemetry, the switch exports the following statistics:

| Name | Description |
|----- | ----------- |
| `nvrouting_bgp_peer_state` |  BGP peer state: `Established`, `Idle`, `Connect`, `Active`, `OpenSent`.  |
| `nvrouting_bgp_peer_fsm_established_transitions` | Number of BGP peer state transitions to the `Established` state for the peer session.|
| `nvrouting_bgp_peer_rib_adj_in_installed` | Tracks the number of prefixes received from the neighbor, installed in the RIB and actively used for forwarding.  |
| `nvrouting_bgp_peer_rib_adj_out_advertised` | Tracks the number of prefixes advertised to the neighbor after applying any policies. |
| `nvrouting_bgp_peer_total_msgs_sent` | Number of BGP messages sent to the neighbor. |
| `nvrouting_bgp_peer_total_msgs_recvd` | Number of BGP messages received from the neighbor.|
| `nvrouting_bgp_peer_rib_adj_in` | Number of IPv4, IPv6, and EVPN prefixes received from the peer after applying any policies. This count is the number of prefixes present in the post-policy Adj-RIB-In for the peer. |
| `nvrouting_bgp_peer_socket_in_queue` | Number of messages queued to be received from the BGP neighbor.|
| `nvrouting_bgp_peer_socket_out_queue` | Number of messages queued to be sent to the BGP neighbor.|
| `nvrouting_bgp_peer_rx_updates` | Number of BGP messages received from the neighbor.|
| `nvrouting_bgp_peer_tx_updates` | Number of BGP messages sent to the neighbor. |
| `nvrouting_bgp_peer_info` | BGP peer information.|
| `nvrouting_bgp_peer_last_established` | Last established time of the BGP peer.|
| `nvrouting_bgp_peer_as` | Autonomous system number of the BGP peer.|
| `nvrouting_bgp_peer_local_as` | Local autonomous system number.|
 |`nvrouting_bgp_peer_graceful_shutdown` | * Graceful shutdown information for a peer. |
| `nvrouting_rib_count` | Number of IPv4 and IPv6 routes in the IP routing table for each route source. |
| `nvrouting_rib_count_connected` | Number of IPv4 connected routes in the IP routing table. |
| `nvrouting_rib_count_bgp` | Number of IPv4 BGP routes in the IP routing table. |
| `nvrouting_rib_count_kernel` | Number of IPv4 kernel routes in the IP routing table.|
| `nvrouting_rib_count_static` | Number of IPv4 static routes in the IP routing table. |
| `nvrouting_rib_count_pbr` | Number of IPv4 PBR routes in the IP routing table. |
| `nvrouting_rib_count_ospf` | Number of IPv4 OSPF routes in the IP routing table. |
| `nvrouting_rib_count_connected_ipv6` | Number of IPv6 connected routes in the IP routing table. |
| `nvrouting_rib_count_bgp_ipv6` | Number of IPv6 BGP routes in the IP routing table. |
| `nvrouting_rib_count_kernel_ipv6` | Number of IPv6 kernel routes in the IP routing table. |
| `nvrouting_rib_count_static_ipv6` | Number of IPv6 static routes in the IP routing table. |
| `nvrouting_rib_count_pbr_ipv6` | Number of IPv6 PBR routes in the IP routing table. |
| `nvrouting_rib_count_ospf_ipv6` | Number of IPv6 OSPF routes in the IP routing table. |
| `nvrouting_rib_nhg_count` | Number of next hop groups in the routing table. |

<!-- vale off -->
{{< expand "Example JSON data for nvrouting_bgp_peer_state:" >}}
```
{
  "name": "nvrouting_bgp_peer_state",
  "description": "Tracks BGP peer state information (Established:1,Idle:2,Connect:3, Active:4, Opensent:5 )",
  "gauge" {
  "data_points" [
    "start_time_unix_nano": "1738017981273381011",
    "time_unix_nano": "1738017981275774678",
    "as_int": "1"
    "attributes" [
      "key": "peer-id",
      "value" {
        "string_value": "swp17.100"
      }
    ]
    "attributes" [
      "key": "state",
      "value" {
        "string_value": "Established"
      }
    ]
    "attributes" [
      "key": "vrf",
      "value" {
        "string_value": "default"
      }
    ]
  }
  "data_points" {
    "start_time_unix_nano": "1738017981273381011",
    "time_unix_nano": "1738017981275774678",
    "as_int": "1"
    "attributes" [
      "key": "peer-id",
      "value" {
        "string_value": "swp17.101"
      }
    ]
    "attributes" [
      "key": "state",
      "value" {
        "string_value": "Established"
      }
    ]
    "attributes" [
      "key": "vrf",
      "value" {
        "string_value": "default"
      }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_rib_count_bgp_ipv6:" >}}

```
{
  "name": "nvrouting_rib_count_bgp_ipv6",
  "description": "Total Number of ipv6 BGP routes in Zebra",
  "gauge" {
    "data_points" {
      "start_time_unix_nano": "1738016804524747485",
      "time_unix_nano": "1738016804529163046",
      "as_int": "2062"
      "attributes" {
        "key": "vrf",
        "value" {
          "string_value": "vrf2"
        }
      }
    }
    "data_points" {
      "start_time_unix_nano": "1738016804524747485",
      "time_unix_nano": "1738016804529163046",
      "as_int": "2062"
      "attributes" {
        "key": "vrf",
        "value" {
          "string_value": "vrf6"
        }
      }
    }
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_fsm_established_transitions:" >}}

```
{
    "name": "nvrouting_bgp_peer_fsm_established_transitions",
    "description": "Tracks BGP peer state transitions to the Established state",
    "gauge": {
      "dataPoints": [
        {
          "attributes": [
            {
              "key": "peer-id",
              "value": {
                "stringValue": "2.1.1.1"
              }
            },
            {
              "key": "state",
              "value": {
                "stringValue": "Established"
              }
            },
            {
              "key": "vrf",
              "value": {
                "stringValue": "default"
              }
            }
          ],
          "startTimeUnixNano": "1745875680082453094",
          "timeUnixNano": "1745875680086100106",
          "asInt": "1"
        }
      ]
    }
  }
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_rib_adj_in_installed:" >}}
```
{
"name": "nvrouting_bgp_peer_rib_adj_in_installed",
"description": "Tracks received prefixes installed post policy",
"gauge": {
    "dataPoints": [
    {
        "attributes": [
            {
            "key": "afi",
            "value": {
                "stringValue": "IPv6"
            }
            },
            {
            "key": "afi-safi-name",
            "value": {
                "stringValue": "IPV6_UNICAST"
            }
            },
            {
            "key": "peer-id",
            "value": {
                "stringValue": "20.2.0.1"
            }
            },
            {
            "key": "safi",
            "value": {
                "stringValue": "unicast"
            }
            },
            {
            "key": "vrf",
            "value": {
                "stringValue": "default"
            }
            }
        ],
        "startTimeUnixNano": "1745875260035122804",
        "timeUnixNano": "1745875260038241158",
        "asInt": "6"
        },
        {
        "attributes": [
            {
            "key": "afi",
            "value": {
                "stringValue": "l2vpn"
            }
            },
            {
            "key": "afi-safi-name",
            "value": {
                "stringValue": "L2VPN_EVPN"
            }
            },
            {
            "key": "peer-id",
            "value": {
                "stringValue": "20.2.0.1"
            }
            },
            {
            "key": "safi",
            "value": {
                "stringValue": "evpn"
            }
            },
            {
            "key": "vrf",
            "value": {
                "stringValue": "default"
            }
            }
        ],
        "startTimeUnixNano": "1745875260035122804",
        "timeUnixNano": "1745875260038241158",
        "asInt": "0"
        }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_rib_adj_in:" >}}
```
{
"name": "nvrouting_bgp_peer_rib_adj_in",
"description": "Tracks received prefixes post policy",
"gauge": {
    "dataPoints": [
    {
        "attributes": [
        {
            "key": "afi",
            "value": {
            "stringValue": "IPv4"
            }
        },
        {
            "key": "afi-safi-name",
            "value": {
            "stringValue": "IPV4_UNICAST"
            }
        },
        {
            "key": "peer-id",
            "value": {
            "stringValue": "20.1.0.1"
            }
        },
        {
            "key": "safi",
            "value": {
            "stringValue": "unicast"
            }
        },
        {
            "key": "vrf",
            "value": {
            "stringValue": "default"
            }
        }
        ],
        "startTimeUnixNano": "1745875680082504240",
        "timeUnixNano": "1745875680086131030",
        "asInt": "9"
    },
    {
        "attributes": [
        {
            "key": "afi",
            "value": {
            "stringValue": "IPv6"
            }
        },
        {
            "key": "afi-safi-name",
            "value": {
            "stringValue": "IPV6_UNICAST"
            }
        },
        {
            "key": "peer-id",
            "value": {
            "stringValue": "20.1.0.1"
            }
        },
        {
            "key": "safi",
            "value": {
            "stringValue": "unicast"
            }
        },
        {
            "key": "vrf",
            "value": {
            "stringValue": "default"
            }
        }
        ],
        "startTimeUnixNano": "1745875680082504240",
        "timeUnixNano": "1745875680086131030",
        "asInt": "9"
    }
    ]
}
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_rib_adj_out_advertised:" >}}
```
{
"name": "nvrouting_bgp_peer_rib_adj_out_advertised",
"description": "Tracks route count advertised per BGP peer with afi and safi as attributes",
"gauge": {
    "dataPoints": [
    {
        "attributes": [
        {
            "key": "afi",
            "value": {
            "stringValue": "IPv4"
            }
        },
        {
            "key": "afi-safi-name",
            "value": {
            "stringValue": "IPV4_UNICAST"
            }
        },
        {
            "key": "peer-id",
            "value": {
            "stringValue": "20.2.0.1"
            }
        },
        {
            "key": "safi",
            "value": {
            "stringValue": "unicast"
            }
        },
        {
            "key": "vrf",
            "value": {
            "stringValue": "default"
            }
        }
        ],
        "startTimeUnixNano": "1745875680082526528",
        "timeUnixNano": "1745875680086148380",
        "asInt": "9"
    },
    {
        "attributes": [
        {
            "key": "afi",
            "value": {
            "stringValue": "l2vpn"
            }
        },
        {
            "key": "afi-safi-name",
            "value": {
            "stringValue": "L2VPN_EVPN"
            }
        },
        {
            "key": "peer-id",
            "value": {
            "stringValue": "2.1.1.2"
            }
        },
        {
            "key": "safi",
            "value": {
            "stringValue": "evpn"
            }
        },
        {
            "key": "vrf",
            "value": {
            "stringValue": "default"
            }
        }
        ],
        "startTimeUnixNano": "1745875680082526528",
        "timeUnixNano": "1745875680086148380",
        "asInt": "21610"
    }
    ]
}
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_rx_updates:" >}}
```
{
"name": "nvrouting_bgp_peer_rx_updates",
"description": "Tracks total number of BGP received packets",
"gauge": {
    "dataPoints": [
    {
        "attributes": [
        {
            "key": "peer-id",
            "value": {
            "stringValue": "2.1.1.1"
            }
        },
        {
            "key": "state",
            "value": {
            "stringValue": "Established"
            }
        },
        {
            "key": "vrf",
            "value": {
            "stringValue": "default"
            }
        }
        ],
        "startTimeUnixNano": "1745875680082484874",
        "timeUnixNano": "1745875680086118678",
        "asInt": "16702"
     }
    ]
  }
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_socket_in_queue:" >}}
```
{
"name": "nvrouting_bgp_peer_socket_in_queue",
"description": "Tracks total number of BGP messages enqueued into InQ buffer",
"gauge": {
    "dataPoints": [
        {
            "attributes": [
            {
                "key": "peer-id",
                "value": {
                "stringValue": "20.0.0.1"
                }
            },
            {
                "key": "state",
                "value": {
                "stringValue": "Established"
                }
            },
            {
                "key": "vrf",
                "value": {
                "stringValue": "default"
                }
            }
            ],
            "startTimeUnixNano": "1745875680082467806",
            "timeUnixNano": "1745875680086105359",
            "asInt": "0"
        }
        ]
    }
    }
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_socket_out_queue:" >}}
```
{
"name": "nvrouting_bgp_peer_socket_out_queue",
"description": "Tracks total number of BGP messages enqueued into OutQ buffer",
"gauge": {
    "dataPoints": [
    {
        "attributes": [
        {
            "key": "peer-id",
            "value": {
            "stringValue": "2.1.1.1"
            }
        },
        {
            "key": "state",
            "value": {
            "stringValue": "Established"
            }
        },
        {
            "key": "vrf",
            "value": {
            "stringValue": "default"
            }
        }
        ],
        "startTimeUnixNano": "1745875680082473745",
        "timeUnixNano": "1745875680086109500",
        "asInt": "0"
    }
    ]
}
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_state:" >}}
```
{
"name": "nvrouting_bgp_peer_state",
"description": "Tracks BGP peer state information (Established:1,Idle:2,Connect:3, Active:4, Opensent:5 )",
"gauge": {
    "dataPoints": [
    {
        "attributes": [
        {
            "key": "peer-id",
            "value": {
            "stringValue": "20.0.0.1"
            }
        },
        {
            "key": "state",
            "value": {
            "stringValue": "Established"
            }
        },
        {
            "key": "vrf",
            "value": {
            "stringValue": "default"
            }
        }
        ],
        "startTimeUnixNano": "1745875680082426701",
        "timeUnixNano": "1745875680086082560",
        "asInt": "1"
    }
    ]
}
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_total_msgs_recvd:" >}}
```
{
"name": "nvrouting_bgp_peer_total_msgs_recvd",
"description": "Tracks the total number of BGP messages received per BGP peer",
"gauge": {
    "dataPoints": [
    {
        "attributes": [
        {
            "key": "peer-id",
            "value": {
            "stringValue": "2.1.1.2"
            }
        },
        {
            "key": "vrf",
            "value": {
            "stringValue": "default"
            }
        }
        ],
        "startTimeUnixNano": "1745875680082495292",
        "timeUnixNano": "1745875680086126857",
        "asInt": "17160"
    }
    ]
}
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_total_msgs_sent:" >}}
```
{
"name": "nvrouting_bgp_peer_total_msgs_sent",
"description": "Tracks the total number of BGP messages sent per BGP peer",
"gauge": {
    "dataPoints": [
    {
        "attributes": [
        {
            "key": "peer-id",
            "value": {
            "stringValue": "20.1.0.1"
            }
        },
        {
            "key": "vrf",
            "value": {
            "stringValue": "default"
            }
        }
        ],
        "startTimeUnixNano": "1745875680082489967",
        "timeUnixNano": "1745875680086122997",
        "asInt": "26388"
    }
    ]
}
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_tx_updates:" >}}
```
{
"name": "nvrouting_bgp_peer_tx_updates",
"description": "Tracks total number of BGP sent packets",
"gauge": {
    "dataPoints": [
    {
        "attributes": [
        {
            "key": "peer-id",
            "value": {
            "stringValue": "2.1.1.1"
            }
        },
        {
            "key": "state",
            "value": {
            "stringValue": "Established"
            }
        },
        {
            "key": "vrf",
            "value": {
            "stringValue": "default"
            }
        }
        ],
        "startTimeUnixNano": "1745875680082478563",
        "timeUnixNano": "1745875680086114010",
        "asInt": "26220"
    }
    ]
}
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_rib_count:" >}}
```
{
"name": "nvrouting_rib_count",
"description": "Tracks RIB counts with attributes for BGP, connected, PBR, and AF",
"gauge": {
    "dataPoints": [
    {
        "attributes": [
            {
            "key": "AF",
            "value": {
                "stringValue": "ipv6"
            }
            },
            {
            "key": "type",
            "value": {
                "stringValue": "total"
            }
            },
            {
            "key": "vrf",
            "value": {
                "stringValue": "vrf5"
            }
            }
        ],
        "startTimeUnixNano": "1745875680327436353",
        "timeUnixNano": "1745875680344618037",
        "asInt": "806"
        },
        {
        "attributes": [
            {
            "key": "AF",
            "value": {
                "stringValue": "ipv4"
            }
            },
            {
            "key": "type",
            "value": {
                "stringValue": "kernel"
            }
            },
            {
            "key": "vrf",
            "value": {
                "stringValue": "vrf7"
            }
            }
        ],
        "startTimeUnixNano": "1745875680327436353",
        "timeUnixNano": "1745875680344618037",
        "asInt": "1"
        },
        {
        "attributes": [
            {
            "key": "AF",
            "value": {
                "stringValue": "ipv6"
            }
            },
            {
            "key": "type",
            "value": {
                "stringValue": "bgp"
            }
            },
            {
            "key": "vrf",
            "value": {
                "stringValue": "vrf3"
            }
            }
        ],
        "startTimeUnixNano": "1745875680327436353",
        "timeUnixNano": "1745875680344618037",
        "asInt": "603"
        },
        {
        "attributes": [
            {
            "key": "AF",
            "value": {
                "stringValue": "ipv4"
            }
            },
            {
            "key": "type",
            "value": {
                "stringValue": "connected"
            }
            },
            {
            "key": "vrf",
            "value": {
                "stringValue": "vrf33"
            }
            }
        ],
        "startTimeUnixNano": "1745875680327436353",
        "timeUnixNano": "1745875680344618037",
        "asInt": "1"
        }
    ]
}
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_rib_nhg_count:" >}}
```
{
"name": "nvrouting_rib_nhg_count",
"description": "Tracks next-hop group counts globally",
"gauge": {
    "dataPoints": [
    {
        "startTimeUnixNano": "1745875680327449169",
        "timeUnixNano": "1745875680345545247",
        "asInt": "1725"
    }
    ]
}
}
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_last_established:" >}}
```
{
      "name": "nvrouting_bgp_peer_last_established",
      "description": "Tracks the last established time of the bgp peer",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "2.1.1.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066649250",
            "timeUnixNano": "1753901204069100927",
            "asInt": "1753901145"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "2.1.1.2"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066649250",
            "timeUnixNano": "1753901204069100927",
            "asInt": "1753901145"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.0.0.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066649250",
            "timeUnixNano": "1753901204069100927",
            "asInt": "1753901144"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.1.0.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066649250",
            "timeUnixNano": "1753901204069100927",
            "asInt": "1753901144"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.2.0.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066649250",
            "timeUnixNano": "1753901204069100927",
            "asInt": "1753901144"
          }
        ]
      }
    },
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_info:" >}}
```
    {
      "name": "nvrouting_bgp_peer_info",
      "description": "Tracks the peer information of the bgp peer",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "description",
                "value": {
                  "stringValue": "ebgp_mulithop_neighbor_2.1.1.1"
                }
              },
              {
                "key": "last-notification-error-code-received",
                "value": {
                  "stringValue": ""
                }
              },
              {
                "key": "last-notification-error-code-sent",
                "value": {
                  "stringValue": ""
                }
              },
              {
                "key": "peer-address",
                "value": {
                  "stringValue": "2.1.1.1"
                }
              },
              {
                "key": "peer-group",
                "value": {
                  "stringValue": "ebgp_mulithop"
                }
              },
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "2.1.1.1"
                }
              },
              {
                "key": "peer-type",
                "value": {
                  "stringValue": "EXTERNAL"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066661716",
            "timeUnixNano": "1753901204069104448",
            "asInt": "1"
          },
          {
            "attributes": [
              {
                "key": "description",
                "value": {
                  "stringValue": "ebgp_mulithop_neighbor_2.1.1.2"
                }
              },
              {
                "key": "last-notification-error-code-received",
                "value": {
                  "stringValue": ""
                }
              },
              {
                "key": "last-notification-error-code-sent",
                "value": {
                  "stringValue": ""
                }
              },
              {
                "key": "peer-address",
                "value": {
                  "stringValue": "2.1.1.2"
                }
              },
              {
                "key": "peer-group",
                "value": {
                  "stringValue": "ebgp_mulithop"
                }
              },
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "2.1.1.2"
                }
              },
              {
                "key": "peer-type",
                "value": {
                  "stringValue": "EXTERNAL"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066661716",
            "timeUnixNano": "1753901204069104448",
            "asInt": "1"
          },
          {
            "attributes": [
              {
                "key": "description",
                "value": {
                  "stringValue": "fabric_neighbor_20.0.0.1"
                }
              },
              {
                "key": "last-notification-error-code-received",
                "value": {
                  "stringValue": ""
                }
              },
              {
                "key": "last-notification-error-code-sent",
                "value": {
                  "stringValue": ""
                }
              },
              {
                "key": "peer-address",
                "value": {
                  "stringValue": "20.0.0.1"
                }
              },
              {
                "key": "peer-group",
                "value": {
                  "stringValue": "fabric"
                }
              },
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.0.0.1"
                }
              },
              {
                "key": "peer-type",
                "value": {
                  "stringValue": "EXTERNAL"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066661716",
            "timeUnixNano": "1753901204069104448",
            "asInt": "1"
          },
          {
            "attributes": [
              {
                "key": "description",
                "value": {
                  "stringValue": "fabric_neighbor_20.1.0.1"
                }
              },
              {
                "key": "last-notification-error-code-received",
                "value": {
                  "stringValue": ""
                }
              },
              {
                "key": "last-notification-error-code-sent",
                "value": {
                  "stringValue": ""
                }
              },
              {
                "key": "peer-address",
                "value": {
                  "stringValue": "20.1.0.1"
                }
              },
              {
                "key": "peer-group",
                "value": {
                  "stringValue": "fabric"
                }
              },
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.1.0.1"
                }
              },
              {
                "key": "peer-type",
                "value": {
                  "stringValue": "EXTERNAL"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066661716",
            "timeUnixNano": "1753901204069104448",
            "asInt": "1"
          },
          {
            "attributes": [
              {
                "key": "description",
                "value": {
                  "stringValue": "fabric_neighbor_20.2.0.1"
                }
              },
              {
                "key": "last-notification-error-code-received",
                "value": {
                  "stringValue": ""
                }
              },
              {
                "key": "last-notification-error-code-sent",
                "value": {
                  "stringValue": ""
                }
              },
              {
                "key": "peer-address",
                "value": {
                  "stringValue": "20.2.0.1"
                }
              },
              {
                "key": "peer-group",
                "value": {
                  "stringValue": "fabric"
                }
              },
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.2.0.1"
                }
              },
              {
                "key": "peer-type",
                "value": {
                  "stringValue": "EXTERNAL"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066661716",
            "timeUnixNano": "1753901204069104448",
            "asInt": "1"
          }
        ]
      }
    },
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_as:" >}}
```
    {
      "name": "nvrouting_bgp_peer_as",
      "description": "Tracks the autonomous system number of the bgp peer",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "2.1.1.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066643656",
            "timeUnixNano": "1753901204069096194",
            "asInt": "744603565"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "2.1.1.2"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066643656",
            "timeUnixNano": "1753901204069096194",
            "asInt": "744603565"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.0.0.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066643656",
            "timeUnixNano": "1753901204069096194",
            "asInt": "744603564"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.1.0.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066643656",
            "timeUnixNano": "1753901204069096194",
            "asInt": "744603564"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.2.0.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066643656",
            "timeUnixNano": "1753901204069096194",
            "asInt": "744603564"
          }
        ]
      }
    },
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvrouting_bgp_peer_local_as:" >}}
```
    {
      "name": "nvrouting_bgp_peer_local_as",
      "description": "Tracks the local autonomous system number",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "2.1.1.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066640069",
            "timeUnixNano": "1753901204069092308",
            "asInt": "744603563"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "2.1.1.2"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066640069",
            "timeUnixNano": "1753901204069092308",
            "asInt": "744603563"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.0.0.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066640069",
            "timeUnixNano": "1753901204069092308",
            "asInt": "744603563"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.1.0.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066640069",
            "timeUnixNano": "1753901204069092308",
            "asInt": "744603563"
          },
          {
            "attributes": [
              {
                "key": "peer-id",
                "value": {
                  "stringValue": "20.2.0.1"
                }
              },
              {
                "key": "vrf",
                "value": {
                  "stringValue": "default"
                }
              }
            ],
            "startTimeUnixNano": "1753901204066640069",
            "timeUnixNano": "1753901204069092308",
            "asInt": "744603563"
          }
        ]
      }
    }
```
{{< /expand >}}

### Software Statistics Format

When you enable `systemd` software statistic telemetry, the switch collects the following `systemd` unit statistics:

|  Name | Description |
|------ | ----------- |
| `nvswitch_systemd_unit_main_pid ` | The main process ID of the unit. |
| `nvswitch_systemd_unit_state`| The active status of the unit. |
| `nvswitch_systemd_unit_running` | The running status of the unit.|
| `nvswitch_systemd_unit_exe_path` | The executable path of the unit. |
| `nvswitch_systemd_unit_restart`| The `systemd` managed restart count of the unit. |
| `nvswitch_systemd_unit_cpu_usage_seconds` | The CPU usage of the unit (in seconds).|
| `nvswitch_systemd_unit_memory_usage_bytes` |  The memory usage of the unit (in bytes). |
| `nvswitch_systemd_unit_start_time_seconds` | The start time of the unit in seconds since epoch.|
| `nvswitch_systemd_unit_uptime_seconds` | The uptime of the unit (in seconds). |
| `nvswitch_systemd_unit_threads` | The number of threads in the unit. |
| `nvswitch_systemd_unit_processes`| The number of processes in the unit. |

If you enable `systemd` process-level statistics, the switch collects the following metrics:

|  Name | Description |
|------ | ----------- |
| `nvswitch_systemd_unit_process_parent_pid` | The parent process ID. |
| `nvswitch_systemd_unit_process_start_time_seconds` | The start time of the process in seconds since epoch.|
| `nvswitch_systemd_unit_process_state` | The process running status.|
| `nvswitch_systemd_unit_process_threads` | The number of threads in the process.|
| `nvswitch_systemd_unit_process_subprocesses` | The number of child processes.|
| `nvswitch_systemd_unit_process_context_switches` | The number of context switches based on context type after the main process was created.|
| `nvswitch_systemd_unit_process_cpu_usage_seconds` | The CPU usage of the process (user and kernel mode, including children).|
| `nvswitch_systemd_unit_process_cpu_usage_user_seconds` | CPU usage of the process (User mode) in seconds.|
| `nvswitch_systemd_unit_process_cpu_usage_system_seconds`| CPU usage of the process (System mode) in seconds.|
| `nvswitch_systemd_unit_process_info` | Process information includes pid, name and args. |
| `nvswitch_systemd_unit_process_virtual_memory_usage_bytes` | The virtual memory usage of the process (in bytes).|
| `nvswitch_systemd_unit_process_resident_memory_usage_bytes` | The resident memory usage of the process (in bytes).|
| `nvswitch_systemd_unit_process_shared_memory_usage_bytes` | The shared memory usage of the process (in bytes).|

{{< expand "Example JSON data for nvswitch_systemd_unit_cpu_usage_seconds:" >}}

```
{
  "name": "nvswitch_systemd_unit_cpu_usage_seconds",
  "description": "CPU usage of the unit (in seconds)",
  "sum": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "unit_name",
            "value": {
              "stringValue": "frr.service"
            }
          }
        ],
        "startTimeUnixNano": "1745866936115000000",
        "timeUnixNano": "1745869936115000000",
        "asDouble": 6.903563
      },
      {
        "attributes": [
          {
            "key": "unit_name",
            "value": {
              "stringValue": "hw-management-sync.service"
            }
          }
        ],
        "startTimeUnixNano": "1745866936115000000",
        "timeUnixNano": "1745869936115000000",
        "asDouble": 4.948827
      },
      {
        "attributes": [
          {
            "key": "unit_name",
            "value": {
              "stringValue": "nginx.service"
            }
          }
        ],
        "startTimeUnixNano": "1745866936115000000",
        "timeUnixNano": "1745869936115000000",
        "asDouble": 0.114203
      }
    ]
  }
}
```

{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_systemd_unit_exe_path:" >}}

```
{
  "name": "nvswitch_systemd_unit_exe_path",
  "description": "Executable path of the unit",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "exe_path",
            "value": {
              "stringValue": "/bin/sh"
            }
          },
          {
            "key": "unit_name",
            "value": {
              "stringValue": "hw-management-sync.service"
            }
          }
        ],
        "timeUnixNano": "1745869876115000000",
        "asDouble": 1
      },
      {
        "attributes": [
          {
            "key": "exe_path",
            "value": {
              "stringValue": "/usr/bin/prometheus-node-exporter"
            }
          },
          {
            "key": "unit_name",
            "value": {
              "stringValue": "prometheus-node-exporter.service"
            }
          }
        ],
        "timeUnixNano": "1745869876115000000",
        "asDouble": 1
      }
    ]
  }
}

```

{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_systemd_unit_main_pid:" >}}

```
{
  "name": "nvswitch_systemd_unit_main_pid",
  "description": "Main Process ID of the unit",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "unit_name",
            "value": {
              "stringValue": "hw-management-sync.service"
            }
          }
        ],
        "timeUnixNano": "1745869216115000000",
        "asDouble": 20845
      },
      {
        "attributes": [
          {
            "key": "unit_name",
            "value": {
              "stringValue": "nginx.service"
            }
          }
        ],
        "timeUnixNano": "1745869216115000000",
        "asDouble": 23135
      }
    ]
  }
}

```

{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_systemd_unit_memory_usage_bytes:" >}}

```
{
  "name": "nvswitch_systemd_unit_memory_usage_bytes",
  "description": "Memory usage of the unit (in bytes)",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "unit_name",
            "value": {
              "stringValue": "frr.service"
            }
          }
        ],
        "timeUnixNano": "1745869936115000000",
        "asDouble": 48377856
      },
      {
        "attributes": [
          {
            "key": "unit_name",
            "value": {
              "stringValue": "hw-management-sync.service"
            }
          }
        ],
        "timeUnixNano": "1745869936115000000",
        "asDouble": 13131776
      }
    ]
  }
}

```

{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_systemd_unit_start_time_seconds:" >}}

```
{
  "name": "nvswitch_systemd_unit_start_time_seconds",
  "description": "Start time of the unit in seconds since epoch",
  "gauge": {
    "dataPoints": [
      {
        "attributes": [
          {
            "key": "unit_name",
            "value": {
              "stringValue": "frr.service"
            }
          }
        ],
        "timeUnixNano": "1745869876115000000",
        "asDouble": 1745864324.62
      },
      {
        "attributes": [
          {
            "key": "unit_name",
            "value": {
              "stringValue": "hw-management-sync.service"
            }
          }
        ],
        "timeUnixNano": "1745869876115000000",
        "asDouble": 1745864182
      }
    ]
  }
}

```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_systemd_unit_process_cpu_usage_system_seconds:" >}}
```
{
      "name": "nvswitch_systemd_unit_process_cpu_usage_system_seconds",
      "description": "CPU usage of the process (kernel mode) in seconds",
      "sum": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "pid",
                "value": {
                  "stringValue": "17976"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "hw-management-sync.service"
                }
              }
            ],
            "startTimeUnixNano": "1753901249206000000",
            "timeUnixNano": "1753901249206000000",
            "asDouble": 0
          },
          {
            "attributes": [
              {
                "key": "pid",
                "value": {
                  "stringValue": "17977"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "hw-management-sync.service"
                }
              }
            ],
            "startTimeUnixNano": "1753901249206000000",
            "timeUnixNano": "1753901249206000000",
            "asDouble": 93.07
          },
          {
            "attributes": [
              {
                "key": "pid",
                "value": {
                  "stringValue": "19594"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "nginx.service"
                }
              }
            ],
            "startTimeUnixNano": "1753901249206000000",
            "timeUnixNano": "1753901249206000000",
            "asDouble": 0.01
          },
          {
            "attributes": [
              {
                "key": "pid",
                "value": {
                  "stringValue": "19595"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "nginx.service"
                }
              }
            ],
            "startTimeUnixNano": "1753901249206000000",
            "timeUnixNano": "1753901249206000000",
            "asDouble": 0.04
          },
          {
            "attributes": [
              {
                "key": "pid",
                "value": {
                  "stringValue": "19596"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "nginx.service"
                }
              }
            ],
            "startTimeUnixNano": "1753901249206000000",
            "timeUnixNano": "1753901249206000000",
            "asDouble": 0.07
          },
          {
            "attributes": [
              {
                "key": "pid",
                "value": {
                  "stringValue": "19597"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "nginx.service"
                }
              }
            ],
            "startTimeUnixNano": "1753901249206000000",
            "timeUnixNano": "1753901249206000000",
            "asDouble": 0.04
          },
          {
            "attributes": [
              {
                "key": "pid",
                "value": {
                  "stringValue": "19598"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "nginx.service"
                }
              }
            ],
            "startTimeUnixNano": "1753901249206000000",
            "timeUnixNano": "1753901249206000000",
            "asDouble": 0.09
          },
...
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_systemd_unit_process_info:" >}}
```
{
      "name": "nvswitch_systemd_unit_process_info",
      "description": "Process information includes PID, name and args ",
      "gauge": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "args",
                "value": {
                  "stringValue": "/bin/sh -c /usr/bin/hw_management_sync.py"
                }
              },
              {
                "key": "name",
                "value": {
                  "stringValue": "sh"
                }
              },
              {
                "key": "pid",
                "value": {
                  "stringValue": "17976"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "hw-management-sync.service"
                }
              }
            ],
            "timeUnixNano": "1753901249206000000",
            "asDouble": 1
          },
          {
            "attributes": [
              {
                "key": "args",
                "value": {
                  "stringValue": "/usr/bin/prometheus-node-exporter --web.disable-exporter-metrics --collector.nvsystemd_unit --collector.nvsystemd_unit.process_level"
                }
              },
              {
                "key": "name",
                "value": {
                  "stringValue": "prometheus-node"
                }
              },
              {
                "key": "pid",
                "value": {
                  "stringValue": "680926"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "prometheus-node-exporter.service"
                }
              }
            ],
            "timeUnixNano": "1753901249206000000",
            "asDouble": 1
          },
...
```
{{< /expand >}}
<br>
{{< expand "Example JSON data for nvswitch_systemd_unit_process_cpu_usage_user_seconds:" >}}
```
{
      "name": "nvswitch_systemd_unit_process_cpu_usage_user_seconds",
      "description": "CPU usage of the process (user mode) in seconds",
      "sum": {
        "dataPoints": [
          {
            "attributes": [
              {
                "key": "pid",
                "value": {
                  "stringValue": "17976"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "hw-management-sync.service"
                }
              }
            ],
            "startTimeUnixNano": "1753901249206000000",
            "timeUnixNano": "1753901249206000000",
            "asDouble": 0
          },
          {
            "attributes": [
              {
                "key": "pid",
                "value": {
                  "stringValue": "17977"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "hw-management-sync.service"
                }
              }
            ],
            "startTimeUnixNano": "1753901249206000000",
            "timeUnixNano": "1753901249206000000",
            "asDouble": 118.2
          },
          {
            "attributes": [
              {
                "key": "pid",
                "value": {
                  "stringValue": "19594"
                }
              },
              {
                "key": "unit_name",
                "value": {
                  "stringValue": "nginx.service"
                }
              }
            ],
            "startTimeUnixNano": "1753901249206000000",
            "timeUnixNano": "1753901249206000000",
            "asDouble": 0
          },
...
```
{{< /expand >}}

### System Information Format

When you enable open telemetry with the `nv set system telemetry export otlp state enabled` command, the switch exports the following system information metrics to the configured OTEL collector by default:

|  Name | Description |
|------ | ----------- |
| `node_boot_time_seconds` | Node boot time, in unixtime. |
| `node_time_seconds` | System time in seconds since epoch (1970). |
| `node_os_info` |  Operating system and image information, such as name and version. |

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
<!-- vale on -->