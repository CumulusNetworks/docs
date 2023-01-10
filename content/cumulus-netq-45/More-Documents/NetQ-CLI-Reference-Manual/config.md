---
title: config
author: NVIDIA
weight: 1102
toc: 3
right_toc_levels: 1
pdfhidden: true
---
<!-- vale NVIDIA.HeadingTitles = NO -->

You must run the `netq config` commands with sudo privileges.

## netq config add agent cluster-servers

Configures the server cluster where the NetQ Agents on monitored switches and hosts should send their collected data. You can also provide a specific port or VRF to use for the communication. Note that you must restart the NetQ Agent to enable the configuration.

### Syntax

```
netq config add agent cluster-servers
    <text-opta-ip-list>
    [port <text-opta-port>]
    [vrf <text-vrf-name>]
    [ssl true | ssl false]
    [ssl-cert <text-ssl-cert-file> | ssl-cert download]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-opta-ip-list\> | Comma-separated list (no spaces) of IP addresses or hostnames of switches to include in server cluster |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| port | \<text-opta-port\> | Use the port with this name on each switch to receive data; default is port 31980 |
| vrf | \<text-vrf-names\> | Use the VRF with this name on each switch to receive data; default VRF is *default* |
| ssl | true, false |  |
| ssl-cert | \<text-ssl-cert-file\> | Use the SSL certificate contained in this file. Value must include entire path to the file. |
| ssl-cert download | NA | |

<!-- Need to add ssl definitions -->

### Sample Usage

Configure cluster with default port and VRF

```
cumulus@switch:~$ netq config add agent cluster-servers leaf01,leaf02,spine01
Updated agent for cluster servers leaf01,leaf02,spine01 port 31980 vrf default. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config del agent cluster-servers
- netq config restart agent

- - -

## netq config add agent command

The NetQ Agent contains a pre-configured set of modular commands that run periodically and send event and resource data to the NetQ appliance or VM. This command lets you fine-tune which events the agent can poll and vary the frequency of polling. Note that you must restart the NetQ Agent to enable the configuration.

Refer to the {{<link title="Manage NetQ Agents/#change-netq-agent-polling-data-and-frequency" text="Manage NetQ Agents">}} for additional details, including service keys and default polling intervals.

### Syntax

```
netq config add agent command
    service-key <text-service-key-anchor>
    [poll-period <text-cmd-periodicity>]
    [command <text-cmd-text>]
    [enable True | enable False]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| service-key | \<text-service-key-anchor\> | Modify the NetQ Agent command with this service key (name) |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| poll-period | \<text-cmd-periodicity\> | Set the polling period (in seconds) for the NetQ Agent command with the designated service key |
| command | \<text-cmd-text\> | Run this executable command for the NetQ Agent command with the designated service key |
| enable | True, False | Enable (True) or disable (False) the NetQ Agent command with the designated service key |

### Sample Usage

Modify the polling frequency for a command:

```
cumulus@switch:~$ netq config add agent command service-key lldp-json poll-period 60
Successfully added/modified Command service lldpd command /usr/sbin/lldpctl -f json
```

Disable a command:

```
cumulus@switch:~$ netq config add agent command service-key ospf-neighbor-json enable False
Command Service ospf-neighbor-json is disabled
```

### Related Commands

- ```netq config show agent```
- ```netq config agent factory-reset```

- - -

## netq config add agent cpu-limit

Configures the NetQ Agent use no more than a specified maximum percentage (between 40 and 60 percent) of the CPU resources of the switch. If you run the command without a value, NetQ assumes a limit of 40%. Cumulus Linux versions 3.6 or later or 4.1.0 or later must be running on the switch for this setting to take effect. Note that you must restart the NetQ Agent to enable the configuration.

For more detail about this feature, refer to this [Knowledge Base]({{<ref "knowledge-base/Configuration-and-Usage/Cumulus-NetQ/NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches">}}) article.

### Syntax

```
netq config add agent cpu-limit
    [<text-limit-number>]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-limit-number\> | Set the threshold for the maximum percentage of CPU resources that the NetQ Agent can use |

### Sample Usage

Limit CPU usage by NetQ Agent to 60%:

```
cumulus@switch:~$ netq config add agent cpu-limit 60
Successfully set agent CPU limit to 60
Please restart agent(netq config restart agent)
'netq-agent'
cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- ```netq config show agent cpu-limit```
- ```netq config del agent cpu-limit```
- ```netq config restart agent```

- - -

## netq config add agent frr-monitor

Configures the NetQ Agent to monitor the Free Range Router (FRR) function when running in a Docker container. Typically, FRR runs as a service. Note that you must restart the NetQ Agent to enable the configuration.

### Syntax

```
netq config add agent frr-monitor
    [<text-frr-docker-name>]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-frr-docker-name\> | Collect statistics about the FRR docker container with this name pattern, used by `grep` |

### Sample Usage

Configure NetQ Agent to collect FRR statistics:

```
cumulus@switch:~$ netq config add agent frr-monitor frr
Successfully added FRR docker monitoring for netq-agent. Please restart service.

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- ```netq config show agent frr-monitor```
- ```netq config del agent frr-monitor```
- ```netq config restart agent```

- - -

## netq config add agent kubernetes-monitor

Configures the NetQ Agent to monitor Kubernetes containers on the switch and to set how often to collect this information (between 10 and 120 seconds). Note that you must restart the NetQ Agent to enable the configuration.

### Syntax

```
netq config add agent kubernetes-monitor
    [poll-period <text-duration-period>]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| poll-period | \<text-duration-period\> | Collect statistics about Kubernetes containers at this frequency, in seconds |

### Sample Usage

Configure NetQ Agent to monitor Kubernetes containers:

```
cumulus@switch:~$ netq config add agent kubernetes-monitor
Successfully added kubernetes monitor. Please restart netq-agent.

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

Configure the polling frequency for Kubernetes container data collection:

```
cumulus@switch:~$ netq config add agent kubernetes-monitor poll-period 120
Successfully added kubernetes monitor. Please restart netq-agent.

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- ```netq config show agent kubernetes-monitor```
- ```netq config del agent kubernetes-monitor```
- ```netq config restart agent```

- - -

## netq config add agent loglevel

Configures the amount of information to log about the NetQ Agent activity, from only critical issues to every available message. Identified issues get logged to */var/log/netq-agent.log* file. The default log level is *info*.

- Error: Logs only events classified as errors
- Warning: Logs events classified as warnings and errors
- Info: Logs events classified as info, warning, and errors
- Debug: Logs all events

After you finish debugging, reset the log level to info or higher. Note that you must restart the NetQ Agent to enable the configuration.

### Syntax

```
netq config add agent loglevel
    [debug|error|info|warning]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | debug, error, info, warning | Log NetQ Agent events with this severity |

### Sample Usage

Configure NetQ Agent to log only errors:

```
cumulus@switch:~$ netq config add agent loglevel error
Successfully added logging for netq-agent. Please restart service.

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- ```netq config show agent loglevel```
- ```netq config del agent loglevel```
- ```netq config restart agent```

- - -

## netq config add agent opta-discovery-servers

Configures the range of IP addresses to search as part of the lifecycle management discovery process (when NetQ is looking for Cumulus Linux switches not running NetQ).

Ranges can be contiguous, for example *192.168.0.24-64*, or non-contiguous, for example *192.168.0.24-64,128-190,235*, but they must be within a single subnet. You can include a maximum of 50 addresses in an address range; if necessary, break the range into smaller ranges.

### Syntax

```
netq config add agent opta-discovery-servers 
    <text-opta-discovery-ips> 
    [vrf <text-vrf-name>]
    [port <text-discovery-server-port>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| opta-discovery-servers | \<text-opta-discovery-ips\> | Look for Cumulus Linux switches not running NetQ within this range of IP addresses |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| vrf | \<text-vrf-name\> | Look for Cumulus Linux switches with the specified IP addresses that use the VRF with this name. When unspecified, the command uses the *default* VRF. |
| port | \<text-discovery-server-port\> | Look for Cumulus Linux switches with the specified IP addresses that use this port. When unspecified, the command uses port 31980. |

### Sample Usage

Configure a range of IP addresses to search for switches that are not running NetQ:

```
cumulus@switch:~$ netq config add agent opta-discovery-servers 192.168.0.24-64,128-190
Updated agent discovery servers 192.168.0.24-64,128-190 port 31980 vrf default. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- ```netq config restart agent```

- - -

## netq config add agent sensors

Configures the NetQ Agent to collect information from the sensors on the switch chassis, including fan, power supply, and temperature data. You must run this command from the chassis.

### Syntax

```
netq config add agent sensors
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| sensors | NA | Collect information from all chassis sensors |

### Options

None

### Sample Usage

Configure sensor monitoring

```
cumulus@chassis:~$ netq config add agent sensors
Successfully added sensors monitor. Please restart netq-agent (netq config restart agent)

cumulus@chassis:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config show agent sensors
- netq config del agent sensors
- netq config restart agent

- - -

## netq config add agent server

Configures the destination (NetQ appliance or VM) for the data collected by the NetQ Agent and for API requests.

### Syntax

```
netq config add agent server
    <text-opta-ip>
    [port <text-opta-port>]
    [vrf <text-vrf-name>]
    [ssl true | ssl false ]
    [ssl-cert <text-ssl-cert-file> | ssl-cert download]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| server | \<text-opta-ip\> | Use the appliance or VM with this IP address to receive NetQ Agent data and API requests |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| port | \<text-opta-port\> | Use this port on the appliance or VM to receive NetQ Agent data and API requests |
| vrf | \<text-vrf-name\> | Use this VRF on the appliance or VM to receive NetQ Agent data and API requests |
| ssl | true, false |  |
| ssl-cert | \<text-ssl-cert-file\> | Use the SSL certificate contained in this file. Value must include entire path to the file. |
| ssl-cert download | NA | |

### Sample Usage

Configure destination server with default port and VRF

```
cumulus@switch:~$ netq config add agent server 192.168.200.250
Updated agent server 192.168.200.250 port 31980 vrf default. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config del agent server
- netq config restart agent

- - -

## netq config add agent stats

Configures the NetQ Agent to collect and send interface statistics.

### Syntax

```
netq config add agent stats
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| stats | NA | Collect and send interface statistics |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config add agent stats
stats config added. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config show agent stats
- netq config del agent stats
- netq config restart agent

- - -

## netq config add agent wjh

Configures the NetQ Agent to collect and send What Just Happened events from  NVIDIA Spectrum&trade; switches. Refer to the {{<link title="WJH Event Messages Reference" text="WJH events reference">}} for a list of supported WJH events and to {{<link title="Configure and Monitor What Just Happened" text="WJH configuration">}} for configuration information.

### Syntax

```
netq config add agent wjh
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh | NA | Collect and send What Just Happened events |

### Options

None

### Sample Usage

```
cumulus@chassis:~$ netq config add agent wjh
Successfully added WJH monitor. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- ```netq config show agent wjh```
- ```netq config del agent wjh```
- ```netq config add agent wjh-drop-filter```
- ```netq config add agent wjh-threshold```
- ```netq config restart agent```

- - -

## netq config add agent wjh-drop-filter

Filters the WJH events at the NetQ Agent before the NetQ system processes them. NetQ performs the filtering on a drop-type basis. You can filter the drop type further by specifying one or more drop reasons or severities. This command only applies to NVIDIA Spectrum switches.

### Syntax

```
netq config add agent wjh-drop-filter
    drop-type <text-wjh-drop-type> 
    [drop-reasons <text-wjh-drop-reasons>]
    [severity <text-drop-severity-list>]
```

### Required Arguments

<!-- vale off -->
| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh-drop-filter | NA | Collect and send WJH events filtered by drop type, reason or severity |
| drop-type | \<text-wjh-drop-type\> | Only collect and send WJH events with this drop type. Valid drop types include *acl*, *buffer*, *l1*, *l2*, *router*, and *tunnel*. |
<!-- vale on -->

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| drop-reasons | \<text-wjh-drop-reasons\> | Only collect and send WJH events with these drop reasons. When you desire more than one drop reason, you should format this value as a comma-separated list, without spaces. Valid drop reasons vary according to the drop type. Refer to the {{<link title="WJH Event Messages Reference" text="WJH events reference">}}. |
| severity | \<text-drop-severity-list\> | Only collect and send WJH events with these severities. When you desire more than one severity, you should format this value as a comma-separated list, without spaces. Valid severities include *Notice*, *Warning*, and *Error*. |

### Sample Usage

```
cumulus@switch:~$ netq config add agent wjh-drop-filter drop-type l1 drop-reasons PORT_ADMIN_DOWN,BAD_SIGNAL_INTEGRITY

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config del agent wjh-drop-filter
- netq config add agent wjh
- netq config add agent wjh-threshold
- netq config restart agent

- - -

## netq config add agent wjh-threshold

WJH latency and congestion metrics depend on threshold settings to trigger the events. NetQ measures packet latency as the time spent inside a single system (switch). It measures congestion as a percentage of buffer occupancy on the switch. When configured, the NetQ Agent collects and sends these WJH-triggered events when a metric crosses the high and low thresholds.

This command only applies to NVIDIA Spectrum switches.

### Syntax

```
netq config add agent wjh-threshold
    (latency|congestion)
    (<text-tc-list>|all)
    (<text-port-list>|all)
    <text-th-hi>
    <text-th-lo>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh-threshold | NA | Collect and send WJH latency or congestion events triggered by the specified high and low thresholds |
| latency | NA | Collect and send WJH latency events |
| congestion | NA | Collect and send WJH congestion events |
| NA | \<text-tc-list\> or all | Only send events for these traffic classes, or use *all* for all traffic classes. When you desire more than one traffic class, you should format this value should as a comma-separated list, without spaces. |
| NA | \<text-port-list\> or all | Only send events occurring on these ports, or use *all* for all ports. When you desire more than one port, you should format this value as a comma-separated list, without spaces. For example *swp1,swp2,swp3,swp4*. |
| NA | \<text-th-hi\> | Trigger an event when the latency is greater than this amount of time, or when buffer occupancy is greater than this percentage. |
| NA | \<text-th-lo\> | Trigger an event when the latency is less than this amount of time, or when buffer occupancy is less than this percentage. |

### Options

None
### Sample Usage

Create latency thresholds for Class *3* traffic on port *swp1* where the upper threshold is *10* and the lower threshold is *1*.

```
cumulus@switch:~$ sudo netq config add agent wjh-threshold latency 3 swp1 10 1
```

Create congestion thresholds for Class *4* traffic on port *swp1* where the upper threshold is *200* and the lower threshold is *10*.

```
cumulus@switch:~$ sudo netq config add agent wjh-threshold congestion 4 swp1 200 10
```

### Related Commands

- ```netq config show agent wjh-threshold```
- ```netq config del agent wjh-threshold```
- ```netq config add agent wjh```
- ```netq config add agent wjh-drop-filter```
- ```netq config restart agent```

- - -
## netq config add cli proxy

Adds a new proxy server to the CLI configuration.

### Syntax

```
  netq config add cli proxy 
    <text-proxy-type> 
    <text-proxy-url>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| proxy | \<text-proxy-type\> | |
| proxy | \<text-proxy-url\> |  |

### Options

None

### Sample Usage

### Related Commands

- netq config del cli proxy
- - -
## netq config add cli server

Configures the NetQ CLI on the switch or host where you run this command. Cloud deployments require the `access-key` and `secret-key` options or the `cli-keys-file` option, as well as the `premises` option.

When the NetQ CLI is not configured, you can run only `netq config` and `netq help` commands, and you must use `sudo` to run them.

### Syntax

```
netq config add cli server
    <text-gateway-dest>
    [access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name> | cli-keys-file <text-key-file> premises <text-premises-name>]
    [vrf <text-vrf-name>]
    [port <text-gateway-port>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| server | \<text-gateway-dest\> | Hostname or IP address of the NetQ appliance or VM in on-premises deployments, or gateway IP address or domain name for cloud/remote deployments. |
| access-key | \<text-access-key\> | Access key obtained from NetQ UI for cloud/remote deployments |
| secret-key | \<text-secret-key\> | Secret key obtained from NetQ UI for cloud/remote deployments |
| premises | \<text-premises-name\> | Name of the premises with the data you want to monitor. When you have multiple premises, you must run this command again to view data from another premises. |
| <!-- vale off -->cli-keys-file<!-- vale on --> | \<text-key-file\> | Use the access and secret keys contained in this file for cloud/remote deployments, rather than providing keys individually. Value must include entire path to the file. |

### Options

| Argument | Value | Description |
| ---- | ---- | ---- |
| vrf | \<text-vrf-name\> | Use this VRF for communication with the telemetry server (NetQ appliance, VM, or cloud gateway). This should be the same VRF where you set the routing tables for connectivity to the telemetry server. Typically this is the management VRF. |
| port | \<text-gateway-port\> | Use this port for communication with the telemetry server (NetQ appliance, VM, or cloud gateway). The default port is 32708 for on-premises deployments and 443  for cloud deployments. |

### Sample Usage

On-premises:

```
cumulus@switch:~$ sudo netq config add cli server 10.0.1.1 vrf mgmt port 32000
cumulus@switch:~$ sudo netq config restart cli
```

Cloud/remote:

```
cumulus@switch:~# sudo netq config add cli server api.netq.cumulusnetworks.com access-key 45d11f46bc09986db64612c590204054b1f12bc05219324a7d66084cf741779c secret-key zHoQ9feNlScNuGBVzUNqr0c0kJL+FAZbhEz8YtW2Rc0= premises NewYork 
cumulus@switch:~# sudo netq config restart cli
```

### Related Commands

- ```netq config show cli premises```
- ```netq config del cli server```
- ```netq config restart cli```

- - -
## netq config addons

### Syntax

```
netq config (add|del) addons
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| add | NA |  |
| del | NA | |

### Options

None

### Sample Usage

### Related Commands

None

- - -
## netq config color

<!-- vale off -->
Configures command output to presents results in color for many commands. Results with errors are shown in <span style="color: #ff0000;">red</span>, and warnings are shown in <span style="color: #ffcc00;">yellow</span>. Results without errors or warnings are shown in either black or <span style="color: #00ff00;">green</span>. VTEPs are shown in <span style="color: #0000ff;">blue</span>. A node in the *pretty* output of a trace command is shown in **bold**, and a router interface is wrapped in angle brackets (\< \>). Outputs are shown with color cues as soon as you run the command.
<!-- vale on -->

### Syntax

```
netq config (add|del) color
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| add | NA | Display color-coded command output |
| del | NA | Remove color-coded command output |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config add color
Color coded output config added
```

### Related Commands

None

- - -

## netq config agent factory-reset commands

Resets the factory default settings for NetQ Agent modular commands, removing any manual adjustments made to data to collect and polling frequency.

### Syntax

```
netq config agent factory-reset commands 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| factory-reset commands | NA | Reset NetQ Agent polling data and frequency to factory settings |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config agent factory-reset commands
Netq Command factory reset successful
```

### Related Commands

- ```netq config add agent```
- ```netq config show agent```

- - -

## netq config del agent cluster-servers

For deployments using a cluster server configuration, this command removes the IP addresses of all cluster servers configured to receive NetQ Agent data.

### Syntax

```
netq config del agent cluster-servers
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cluster-servers | NA | Remove all cluster servers configured to receive NetQ Agent data |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config del agent cluster-servers
Deleted agent cluster servers 10.10.0.101,10.20.0.101 port 31980 vrf default. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config add agent cluster-servers
- netq config restart agent

- - -

## netq config del agent cpu-limit

Removes the CPU usage limit for the NetQ Agent on this device.

### Syntax

```
netq config del agent cpu-limit
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cpu-limit | NA | Remove CPU usage limit for the NetQ Agent on this device |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config del agent cpu-limit
Successfully deleted agent CPU limit
Please restart agent(netq config restart agent)

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- ```netq config show agent cpu-limit```
- ```netq config add agent cpu-limit```
- ```netq config restart agent```

- - -

## netq config del agent frr-monitor

Disables NetQ Agent from monitoring FRR running in a Docker container. This *does not* disable NetQ Agent from monitoring FRR running as a service.

### Syntax

```
netq config del agent frr-monitor
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| frr-monitor | NA | Stop the NetQ Agent from monitoring FRR when running in a container |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config del agent frr-monitor
Successfully deleted FRR docker monitoring for netq-agent. Please restart service.

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config show agent frr-monitor
- netq config add agent frr-monitor
- netq config restart agent

- - -

## netq config del agent kubernetes-monitor

Disables NetQ Agent from monitoring Kubernetes container activity on a switch.

### Syntax

```
netq config del agent kubernetes-monitor
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| kubernetes-monitor | NA | Stop the NetQ Agent from monitoring Kubernetes containers |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config del agent kubernetes-monitor
Successfully deleted kubernetes monitoring for netq-agent. Please restart service.

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config show agent kubernetes-monitor
- netq config add agent kubernetes-monitor
- netq config restart agent

- - -

## netq config del agent loglevel

Disables NetQ Agent logging on a switch.

### Syntax

```
netq config del agent loglevel
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| loglevel | NA | Stops the NetQ Agent from logging events about the agent |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config del agent loglevel
Successfully deleted logger for netq-agent. Please restart service.

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config show agent loglevel
- netq config add agent loglevel
- netq config restart agent

- - -

## netq config del agent sensors

Disables NetQ Agent from collecting fan, power supply unit, and temperature sensors for a switch chassis.

### Syntax

```
netq config del agent sensors
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| sensors | NA | Stops the NetQ Agent from monitoring chassis sensors |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config del agent sensors
cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config show agent sensors
- netq config add agent sensors
- netq config restart agent

- - -

## netq config del agent server

Removes the destination (NetQ appliance or VM) for the data collected by the NetQ Agent and for API requests.

### Syntax

```
netq config del agent server
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| server | NA | Delete the current destination of NetQ Agent data and API requests |

### Options

None
### Sample Usage

```
cumulus@switch:~$ netq config del agent server
Deleted agent server 127.0.0.1 port 31980 vrf default. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config add agent server
- netq config restart agent

- - -

## netq config del agent stats

Disables the NetQ Agent from collecting interface statistics on a switch.

### Syntax

```
netq config del agent stats
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| stats | NA | Stop NetQ Agent from collecting interface statistics |

### Options

None
### Sample Usage

```
cumulus@switch:~$ netq config del agent stats
stats config deleted
```

### Related Commands

- netq config show agent stats
- netq config add agent stats
- netq config restart agent

- - -

## netq config del agent wjh

Disables the NetQ Agent from collecting What Just Happened events on a switch.

### Syntax

```
netq config del agent wjh
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh | NA | Stop NetQ Agent from collecting WJH information |

### Options

None
### Sample Usage

```
cumulus@switch:~$ netq config del agent wjh
cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config del agent wjh
- netq config del agent wjh-threshold
- netq config show agent wjh
- netq config add agent wjh
- netq config restart agent

- - -

## netq config del agent wjh-drop-filter

Delete a What Just Happened event filter on a switch.

### Syntax

```
netq config del agent wjh-drop-filter
    drop-type <text-wjh-drop-type> 
    [drop-reasons <text-wjh-drop-reasons>]
    [severity <text-drop-severity-list>]
```

### Required Arguments

<!-- vale off -->
| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh-drop-filter | NA | Delete existing WJH event filter |
| drop-type | \<text-wjh-drop-type\> | Delete WJH event filter with this drop type. Valid drop types include *acl*, *buffer*, *l1*, *l2*, *router*, and *tunnel*. |
<!-- vale on -->

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| drop-reasons | \<text-wjh-drop-reasons\> | Delete WJH event filter with these drop reasons. When you desire more than one drop reason, you should format this value as a comma-separated list, without spaces. Valid drop reasons vary according to the drop type. Refer to the {{<link title="WJH Event Messages Reference" text="WJH events reference">}}. |
| severity | \<text-drop-severity-list\> | Delete WJH event filter with these severities. When you desire more than one severity, you should format this value as a comma-separated list, without spaces. Valid severities include *Notice*, *Warning*, and *Error*. |

### Sample Usage

```
cumulus@switch:~$ netq config del agent wjh-drop-filter drop-type l1 drop-reasons PORT_ADMIN_DOWN,BAD_SIGNAL_INTEGRITY

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config add agent wjh-drop-filter
- netq config add/del agent wjh
- netq config del agent wjh-threshold
- netq config restart agent

- - -

## netq config del agent wjh-threshold

Remove latency or congestion thresholds for WJH events.

### Syntax

```
netq config del agent wjh-threshold
    (latency|congestion)
    (<text-tc-list>|all)
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh-threshold | NA | Remove latency or congestion events triggered by thresholds |
| latency | NA | Remove latency event thresholds |
| congestion | NA | Remove congestion event thresholds |
| NA | \<text-tc-list\> or all | Remove latency or congestion events for these traffic classes, or use *all* for all traffic classes. When you want more than one traffic class, format this value as a comma-separated list, without spaces. |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config del agent wjh-threshold latency 3

cumulus@switch:~$ netq config del agent wjh-threshold congestion 4
```

### Related Commands

- ```netq config show agent wjh-threshold```
- ```netq config add agent wjh-threshold```
- ```netq config del agent wjh```
- ```netq config del agent wjh-drop-filter```
- ```netq config restart agent```

- - -
<!-- vale off -->
## netq config del cli
<!-- vale on -->
Removes the NetQ CLI configuration or proxy server from a switch.

### Syntax

```
netq config del cli (server | proxy)
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| <!-- vale off -->cli<!-- vale on --> | server, proxy | Delete the current NetQ CLI configuration or proxy server |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config del cli server
```

### Related Commands

- ```netq config add cli server```
- ```netq config show cli premises```
- ```netq config restart agent```

- - -

## netq config experimental

### Syntax

```
netq config (add|del) experimental
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| add | NA | Enables experimental features |
| del | NA | Disables experimental features |

### Options

None
### Sample Usage

### Related Commands

None

- - -

## netq config reload parser

Loads the NetQ configuration file.

### Syntax

```
netq config reload parser
```

### Required Arguments

None

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config reload parser
Parser reloaded
```

### Related Commands

None

- - -

## netq config restart

Restarts the NetQ Agent or CLI daemons on a switch. Use this command after making changes to the NetQ Agent or CLI configurations.

### Syntax

```
netq config restart agent

netq config restart cli
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| agent | NA | Restart the NetQ Agent daemon (`netq-agent`) |
| <!-- vale off -->cli <!-- vale on -->| NA | Restart the NetQ CLI daemon (`netq-cli`) |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!

cumulus@switch:~$ netq config restart cli 
Restarting NetQ CLI... Success!
```

### Related Commands

- `netq config (start|stop) agent`

- - -
<!-- vale off -->
## netq config select cli premise
<!-- vale on -->
In a multi-premises deployment, this command configures the NetQ CLI to view data from the given premises.

### Syntax

```
netq config select cli
    premise <text-premise>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| premise | \<text-premise\> | Show data from this premises in the NetQ CLI command outputs |

### Options

None
### Sample Usage

```
cumulus@switch:~$ netq config select cli premise Boston
```

### Related Commands

None

- - -

## netq config show agent

Displays the configuration of the NetQ Agent on a switch. Several forms of this command are available.



<!-- CPU Limit: Displays the maximum percentage of CPU resources of the switch that a NetQ Agent might use. When restricted by the `netq config add agent cpu-limit` command, the value is between 40 and 60 percent. For more detail about this feature, refer to this [Knowledge Base]({{<ref "knowledge-base/Configuration-and-Usage/Cumulus-NetQ/NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches">}}) article.

FRR Monitor: Displays the NetQ Agent Free Range Router (FRR) function monitoring configuration on a switch. If configured, FRR monitoring occurs on FRR running in a Docker container. If not configured, FRR is likely running as a service.

Kubernetes Monitor: Displays the NetQ Agent Kubernetes monitoring configuration on a switch, included whether it is enabled and the polling period.

Log Level: Displays the amount of information logged about the NetQ Agent activity, from only critical issues to every available message. Identified issues get logged to the `/var/log/netq-agent.log` file. The default log level is *info*.

- Error: Logs only events classified as errors
- Warning: Logs events classified as warnings and errors
- Info: Logs events classified as info, warning, and errors
- Debug: Logs all events

Sensors: Displays the NetQ Agent sensors configuration on a chassis.

SSL: 

Stats: Displays whether you configured the NetQ Agent for interface statistics monitoring on a switch (true) or not (false).

WJH: Displays whether you configured the NetQ Agent for What Just Happened event monitoring on an NVIDIA Spectrum switch. Refer to {{<link title="Configure and Monitor What Just Happened" text="WJH configuration">}} for setting up WJH monitoring.

WJH Threshold: Displays whether you configured the NetQ Agent with WJH latency and congestion thresholds on an NVIDIA Spectrum switch. -->

### Syntax

```
netq config show agent 
    [cpu-limit|frr-monitor|kubernetes-monitor|loglevel|sensors|ssl|stats||wjh|wjh-threshold] 
    [json]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| cpu-limit | NA | View the maximum percentage of CPU resource that the NetQ Agent can use |
| frr-monitor | NA | Display FRR monitoring configuration |
| kubernetes-monitor | NA | Display the Kubernetes monitoring configuration |
| loglevel | NA | Display the NetQ Agent logging level configuration |
| sensors | NA | Display NetQ Agent sensors configuration |
| ssl | NA | Display SSL configuration |
| stats | NA | Display status of interface statistics |
| wjh | NA | Display NetQ Agent What Just Happened monitoring configuration |
| wjh-threshold | NA | Display NetQ Agent WJH latency and congestion thresholds configuration |
| json | NA | Display the output in JSON file format |
### Sample Usage

```
cumulus@switch:~$ netq config show agent 
netq-agent             value      default
---------------------  ---------  ---------
exhibitport
exhibiturl
server                 127.0.0.1  127.0.0.1
cpu-limit              100        100
agenturl
enable-opta-discovery  False      False
agentport              8981       8981
port                   31980      31980
vrf                    default    default
()
```
### Related Commands

- `netq config show all`
- `netq config show cli premises`
- `netq config add agent`
- `netq config del agent`

- - -
## netq config show agent commands

The NetQ Agent contains a pre-configured set of modular commands that run periodically and send event and resource data to the NetQ appliance or VM. This command displays the configuration of these commands, including the definition of the commands, which are active, and how often they run. You can also filter by the service key to view a given command.

### Syntax

<!-- vale off -->
```
netq config show agent commands
    [service-key <text-service-key-anchor>]
    [json]
```
<!-- vale on -->

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| commands | NA | View the configuration of all NetQ Agent modular commands |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| service-key | \<text-service-key-anchor\> | View the configuration of the NetQ Agent command with this service key (name) |
| json | NA | Display the output in JSON format|

### Sample Usage

Show the configuration for all commands:

```
cumulus@switch:~$ netq config show agent commands
 Service Key        Period    Active       Command
------------------  --------  --------  ---------------------------------------------------
ports               3600      yes       Netq Predefined Command
proc-net-dev        30        yes       Netq Predefined Command
agent_stats         300       yes       Netq Predefined Command
agent_util_stats    30        yes       Netq Predefined Command
ssd-util-json       86400     yes       /usr/sbin/smartctl -a /dev/sda
lldp-json           30        yes       /usr/sbin/lldpctl -f json
resource-util-json  30        yes       findmnt / -n -o FS-OPTIONS
os-release          N/A       yes       cat /etc/os-release
eprom               N/A       yes       /usr/cumulus/bin/decode-syseeprom -j
lscpu               N/A       yes       /usr/bin/lscpu
meminfo             N/A       yes       cat /proc/meminfo
lsblk               N/A       yes       lsblk -d -n -o name,size,type,vendor,tran,rev,model
dmicode             N/A       yes       dmidecode -t 17
is-opta             N/A       yes       cat /etc/app-release
```

Show the configuration for a specified command:

```
cumulus@switch:~$ netq config show agent commands service-key agent_stats
 Service Key       Period  Active       Command
---------------  --------  --------  -----------------------
agent_stats           300  yes       Netq Predefined Command
```

### Related Commands

- ```netq config add agent commands```
- ```netq config agent factory-reset commands```

- - -
## netq config show all

Displays the configuration of the NetQ Agent and NetQ CLI on a switch.

### Syntax

```
netq config show all
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq config show all 
netq-agent             value      default
---------------------  ---------  ---------
exhibitport
exhibiturl
server                 127.0.0.1  127.0.0.1
cpu-limit              100        100
agenturl
enable-opta-discovery  False      False
agentport              8981       8981
port                   31980      31980
vrf                    default    default
()
netq-cli     value            default
-----------  ---------------  ---------
server       192.168.200.250  127.0.0.1
netq-user
premises     0
port         32708            32708
count        2000             2000
vrf          default          default
api-logging  False            False
()
```

### Related Commands

- `netq config show agent`
- `netq config show cli premises`

- - -

## netq config show cli premises

Displays the configuration of the NetQ CLI on a switch.

### Syntax

```
netq config show cli premises
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq config show cli premises
netq-cli     value            default
-----------  ---------------  ---------
server       192.168.200.250  127.0.0.1
netq-user
premises     0
port         32708            32708
count        2000             2000
vrf          default          default
api-logging  False            False
()
```

### Related Commands

- `netq config show agent`
- `netq config show all`

- - -

## netq config start agent

Starts the NetQ Agent on a switch.

### Syntax

```
netq config start agent
```

### Required Arguments

None

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config start agent 
Starting netq-agent... Success!
```

### Related Commands

- netq config show agent
- netq config stop agent
- netq config restart agent

- - -

## netq config status agent

Displays the operational status of the NetQ Agent on a switch.

### Syntax

```
netq config status agent
```

### Required Arguments

None

### Options

None
### Sample Usage

```
cumulus@switch:~$ netq config status agent 
netq-agent... Running

cumulus@switch:~$ netq config status agent 
netq-agent...stopped

```

### Related Commands

- netq config show agent
- netq config stop agent
- netq config restart agent

- - -
<!-- vale off -->
## netq config status cli
<!-- vale on -->
Displays the operational status of the NetQ CLI on a switch.

### Syntax

```
netq config status cli
```

### Required Arguments

None

### Options

None
### Sample Usage

```
cumulus@switch:~$ netq config status cli
NetQ CLI... Running

```

### Related Commands
<!-- vale off -->
- `netq config show cli premises`
- `netq config restart cli`
<!-- vale on -->
- - -

## netq config stop agent

Stops the NetQ Agent on a switch.

### Syntax

```
netq config stop agent
```

### Required Arguments

None

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq config stop agent
Stopping netq-agent... Success!
```

### Related Commands

- netq config show agent
- netq config start agent
- netq config restart agent
<!-- vale NVIDIA.HeadingTitles = YES -->