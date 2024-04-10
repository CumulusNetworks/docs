---
title: Manage NetQ Agents
author: NVIDIA
weight: 700
toc: 3
---

Run the following commands to view the status of an agent, disable an agent, manage logging, and configure the events the agent collects.

<!--the following section was in network inventory. It needs to be incorporated here.
To view the NetQ Agents on all switches and hosts:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> Menu.

2. Select **Agents** from the **Network** column.

3. View the **Version** column to determine which release of the NetQ Agent is running on your devices. Ideally, this version should be the same as the NetQ release you are running, and is the same across all your devices.

    {{<figure src="/images/netq/main-menu-ntwk-agents-310.png" width="700">}}

<div style="padding-left: 18px;"><table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td>Name of the switch or host</td>
</tr>
<tr>
<td>Timestamp</td>
<td>Date and time the data was captured</td>
</tr>
<tr>
<td>Last Reinit</td>
<td>Date and time that the switch or host was reinitialized</td>
</tr>
<tr>
<td>Last Update Time</td>
<td>Date and time that the switch or host was updated</td>
</tr>
<tr>
<td>Lastboot</td>
<td>Date and time that the switch or host was last booted up</td>
</tr>
<tr>
<td>NTP State</td>
<td>Status of NTP synchronization on the switch or host; yes = in synchronization, no = out of synchronization</td>
</tr>
<tr>
<td>Sys Uptime</td>
<td>Amount of time the switch or host has been continuously up and running</td>
</tr>
<tr>
<td>Version</td>
<td>NetQ version running on the switch or host</td>
</tr>
</tbody>
</table>
</div>

-->

## View NetQ Agent Status

The syntax for the NetQ Agent status command is:

```
netq [<hostname>] show agents
    [fresh | dead | rotten | opta]
    [around <text-time>]
    [json]
```

You can view the status for a given switch, host or NetQ appliance or virtual machine. You can also filter by the status and view the status at a time in the past.

To view the current status of all NetQ Agents, run:

```
cumulus@switch~:$ netq show agents
```

To view NetQ Agents that are not communicating, run:

```
cumulus@switch~:$ netq show agents rotten
No matching agents records found
```

To view NetQ Agent status on the NetQ appliance or VM, run:

```
cumulus@switch~:$ netq show agents opta
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
netq-ts           Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 16:46:53 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:29:51 2020
```

## View NetQ Agent Configuration

You can view the current configuration of a NetQ Agent to determine what data it collects and where it sends that data. The syntax for this command is:

```
sudo netq config show agent 
    [cpu-limit|frr-monitor|loglevel|ssl|stats|wjh|wjh-threshold] 
    [json]
```

The following example shows a NetQ Agent in an on-premises deployment, talking to an appliance or VM at 127.0.0.1 using the default ports and VRF.

```
cumulus@switch:~$ sudo netq config show agent
netq-agent             value      default
---------------------  ---------  ---------
exhibitport
exhibiturl
server                    127.0.0.1  127.0.0.1
cpu-limit                 100        100
agenturl
wjh                                  Enabled
asic-monitor                         Enabled
enable-opta-discovery     False      False
agentport                 8981       8981
port                      31980      31980
vrf                       default    default
is-gnmi-enabled           False      False
netq_stream_port          7680       7680
netq_stream_address       127.0.0.1  127.0.0.1
is-ssl-enabled            False      False
ssl-cert
generate-unique-hostname  False      False
()
```

To view the configuration of a particular aspect of a NetQ Agent, use the various options.

This example shows a NetQ Agent configured with a CPU limit of 60%.

```
cumulus@switch:~$ sudo netq config show agent cpu-limit
CPU Quota
-----------
60%
()
```

## Modify the Configuration of the NetQ Agent on a Node

The agent configuration commands let you:

- Add, disable, and remove a NetQ Agent
- Start and stop a NetQ Agent
- Configure a NetQ Agent to collect selected data (CPU usage limit, FRR, Kubernetes, WJH)
- Configure a NetQ Agent to send data to a server cluster
- Troubleshoot the NetQ Agent

{{<notice note>}}

Commands apply to one agent at a time, and you run them on the switch or host where the NetQ Agent resides.

{{</notice>}}

### Add or Remove a NetQ Agent

To add or remove a NetQ Agent, you must add or remove the IP address (as well as the port and VRF, if specified) from the NetQ configuration file, `/etc/netq/netq.yml`. This adds or removes the information about the server where the agent sends the data it collects.

To use the NetQ CLI to add or remove a NetQ Agent on a switch or host, run:

```
sudo netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>] [inband-interface <interface-name>]
```

If you want to use a specific port on the server, use the `port` option. If you want the data sent over a particular virtual route interface, use the `vrf` option.

This example shows how to add a NetQ Agent and tell it to send the data it collects to the NetQ server at the IPv4 address of 10.0.0.23 using the default port (port 31980 for on-premises and port 443 for cloud deployments) and the default VRF (mgmt). The port and VRF are not specified, so NetQ assumes default settings.

```
cumulus@switch~:$ sudo netq config add agent server 10.0.0.23
cumulus@switch~:$ sudo netq config restart agent
```

This example shows how to add a NetQ Agent and tell it to send the data it collects to the NetQ server at the IPv4 address of 10.0.0.23 using the default port (port 31980 for on-premises and port 443 for cloud deployments) and the `default` VRF for a switch managed through an in-band connection on interface `swp1`:

```
cumulus@switch~:$ sudo netq config add agent server 10.0.0.23 vrf default inband-interface swp1
cumulus@switch~:$ sudo netq config restart agent
```
To remove a NetQ Agent on a switch or host, run:

```
sudo netq config del agent server
```
<!-- vale off -->
### Disable and Reenable a NetQ Agent
<!-- vale on -->

You can temporarily disable the NetQ Agent on a node. Disabling the NetQ Agent maintains the data already collected in the NetQ database, but stops the NetQ Agent from collecting new data until you reenable it.

To disable a NetQ Agent, run:

```
cumulus@switch:~$ sudo netq config stop agent
```

To reenable a NetQ Agent, run:

```
cumulus@switch:~$ sudo netq config restart agent
```

### Configure a NetQ Agent to Limit Switch CPU Usage

You can limit the NetQ Agent to use only a certain percentage of CPU resources on a switch. This setting requires a switch running Cumulus Linux versions 3.7, 4.1, or later.

For more detail about this feature, refer to this [Knowledge Base article]({{<ref "knowledge-base/Configuration-and-Usage/Cumulus-NetQ/NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches">}}).

This example limits a NetQ Agent from consuming more than 40% of the CPU resources on a Cumulus Linux switch.

```
cumulus@switch:~$ sudo netq config add agent cpu-limit 40
cumulus@switch:~$ sudo netq config restart agent
```

To remove the limit, run:

```
cumulus@switch:~$ sudo netq config del agent cpu-limit
cumulus@switch:~$ sudo netq config restart agent
```

### Configure a NetQ Agent to Collect Data from Selected Services

You can enable and disable data collection about FRRouting (FRR) and What Just Happened (WJH).

To configure the agent to start or stop collecting FRR data, run:

```
cumulus@chassis~:$ sudo netq config add agent frr-monitor
cumulus@switch:~$ sudo netq config restart agent

cumulus@chassis~:$ sudo netq config del agent frr-monitor
cumulus@switch:~$ sudo netq config restart agent
```

To configure the agent to start or stop collecting WJH data, run:

```
cumulus@chassis~:$ sudo netq config add agent wjh
cumulus@switch:~$ sudo netq config restart agent

cumulus@chassis~:$ sudo netq config del agent wjh
cumulus@switch:~$ sudo netq config restart agent
```

### Configure a NetQ Agent to Send Data to a Server Cluster

If you have a server cluster arrangement for NetQ, you should configure the NetQ Agent to send the data it collects to every server in the cluster.

To configure the agent to send data to the servers in your cluster, run:

```
sudo netq config add agent cluster-servers <text-opta-ip-list> [port <text-opta-port>] [vrf <text-vrf-name>]
```

You must separate the list of IP addresses by commas (not spaces). You can optionally specify a port or VRF.

This example configures the NetQ Agent on a switch to send the data to three servers located at *10.0.0.21*, *10.0.0.22*, and *10.0.0.23* using the *rocket* VRF.

```
cumulus@switch:~$ sudo netq config add agent cluster-servers 10.0.0.21,10.0.0.22,10.0.0.23 vrf rocket
```

To stop a NetQ Agent from sending data to a server cluster, run:

```
cumulus@switch:~$ sudo netq config del agent cluster-servers
```

### Configure Logging to Troubleshoot a NetQ Agent

The logging level used for a NetQ Agent determines what types of events get logged about the NetQ Agent on the switch or host.

First, you need to decide what level of logging you want to configure. You can configure the logging level to be the same for every NetQ Agent, or selectively increase or decrease the logging level for a NetQ Agent on a problematic node.

| Logging Level | Description |
| ------------- | ------------------ |
| debug | Sends notifications for all debug, info, warning, and error messages. |
| info | Sends notifications for info, warning, and error messages (default). |
| warning | Sends notifications for warning and error messages. |
| error | Sends notifications for errors messages. |

You can view the NetQ Agent log directly. Messages have the following structure:

`<timestamp> <node> <service>[PID]: <level>: <message>`

| Element | Description |
| ---------- | -------------- |
| timestamp | Date and time event occurred in UTC format|
| node | Hostname of network node where event occurred |
| service \[PID\] | Service and Process IDentifier that generated the event |
| level | Logging level assigned for the given event: *debug*, *error*, *info*, or *warning* |
| message | Text description of event, including the node where the event occurred |

For example:

{{<figure src="/images/netq/NetQAgentLogFormat.png" alt="logging message anatomy, including timestamp, node, service, level, and message" height="69" width="747">}}

To configure a logging level, follow these steps. This example sets the logging level to **debug**:

1. Set the logging level:

    ```
    cumulus@switch:~$ sudo netq config add agent loglevel debug
    ```

2. Restart the NetQ Agent:

    ```
    cumulus@switch:~$ sudo netq config restart agent
    ```

3. (Optional) Verify the connection to the NetQ appliance or VM by viewing the `netq-agent.log` messages.

#### Disable Agent Logging

If you set the logging level to *debug* for troubleshooting, NVIDIA recommends that you either change the logging level to a less verbose mode or disable agent logging when you finish troubleshooting.

To change the logging level from debug to another level, run:

```
cumulus@switch:~$ sudo netq config add agent loglevel [info|warning|error]
cumulus@switch:~$ sudo netq config restart agent
```

To disable all logging:

```
cumulus@switch:~$ sudo netq config del agent loglevel
cumulus@switch:~$ sudo netq config restart agent
```

## Change NetQ Agent Polling Data and Frequency

The NetQ Agent contains a pre-configured set of modular commands that run periodically and send event and resource data to the NetQ appliance or VM. You can fine tune which events the agent can poll and vary frequency of polling using the NetQ CLI.

For example, if your network is not running OSPF, you can disable the command that polls for OSPF events. Or you can decrease the polling interval for LLDP from the default of 60 seconds to 120 seconds. By not polling for selected data or polling less frequently, you can reduce switch CPU usage by the NetQ Agent.

Depending on the switch platform, the NetQ Agent might not execute some supported protocol commands. For example, if a switch has no VXLAN capability, then the agent skips all VXLAN-related commands.

### Supported Commands

To see the list of supported modular commands, run:

```
cumulus@switch:~$ sudo netq config show agent commands
 Service Key               Period  Active       Command
-----------------------  --------  --------  ---------------------------------------------------------------------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']
lldp-json                     120  yes       /usr/sbin/lldpctl -f json
clagctl-json                   60  yes       /usr/bin/clagctl -j
dpkg-query                  21600  yes       dpkg-query --show -f ${Package},${Version},${Status}\n
ptmctl-json                   600  yes       /usr/bin/ptmctl -d -j
mstpctl-bridge-json            60  yes       /sbin/mstpctl showall json
ports                        3600  yes       Netq Predefined Command
proc-net-dev                   30  yes       Netq Predefined Command
dom                          1800  yes       Netq Predefined Command
roce                           60  yes       Netq Predefined Command
roce-config                    60  yes       Netq Predefined Command
nvue-roce-config               60  yes       Netq Predefined Command
agent_stats                   300  yes       Netq Predefined Command
agent_util_stats               30  yes       Netq Predefined Command
tcam-resource-json            300  yes       /usr/cumulus/bin/cl-resource-query -j
config-mon-json               120  yes       Netq Predefined Command
nvue-mon-json                  60  yes       Netq Predefined Command
running-config-mon-json        30  yes       Netq Predefined Command
cl-support-json               180  yes       Netq Predefined Command
resource-util-json            120  yes       findmnt / -n -o FS-OPTIONS
smonctl-json                  120  yes       /usr/sbin/smonctl -j
sensors-json                 1800  yes       sensors -u
ssd-util-json               86400  yes       /usr/sbin/smartctl -a /dev/sda
ssd-util-nvme-json          86400  yes       /usr/sbin/smartctl -a /dev/nvme0
ospf-neighbor-json             60  yes       ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  yes       ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
ecmp-hash-info                 60  yes       cat /etc/cumulus/datapath/traffic.conf
ecmp-info                      60  yes       Netq Predefined Command
ptp-config-info                60  yes       cat /etc/ptp4l.conf
ptp-clock-info                 60  yes       Netq Predefined Command
ptp-clock-status               60  yes       Netq Predefined Command
ptp-statistics                 60  yes       Netq Predefined Command
ptp-correction                 30  yes       Netq Predefined Command
log-exporter                   60  yes       Netq Predefined Command
adaptive-routing-config       120  yes       Netq Predefined Command
```
### Modify the Polling Frequency

You can change the polling frequency (in seconds) of a modular command. For example, to change the polling frequency of the `lldp-json` command to 60 seconds from its default of 120 seconds, run:

```
cumulus@switch:~$ sudo netq config add agent command service-key lldp-json poll-period 60
Successfully added/modified Command service lldpd command /usr/sbin/lldpctl -f json

cumulus@switch:~$ sudo netq config show agent commands
 Service Key               Period  Active       Command
-----------------------  --------  --------  ---------------------------------------------------------------------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']
lldp-json                      60  yes       /usr/sbin/lldpctl -f json
clagctl-json                   60  yes       /usr/bin/clagctl -j
dpkg-query                  21600  yes       dpkg-query --show -f ${Package},${Version},${Status}\n
ptmctl-json                   120  yes       /usr/bin/ptmctl -d -j
mstpctl-bridge-json            60  yes       /sbin/mstpctl showall json
ports                        3600  yes       Netq Predefined Command
proc-net-dev                   30  yes       Netq Predefined Command
agent_stats                   300  yes       Netq Predefined Command
agent_util_stats               30  yes       Netq Predefined Command
tcam-resource-json            120  yes       /usr/cumulus/bin/cl-resource-query -j
btrfs-json                   1800  yes       /sbin/btrfs fi usage -b /
config-mon-json               120  yes       Netq Predefined Command
running-config-mon-json        30  yes       Netq Predefined Command
cl-support-json               180  yes       Netq Predefined Command
resource-util-json            120  yes       findmnt / -n -o FS-OPTIONS
smonctl-json                   30  yes       /usr/sbin/smonctl -j
ssd-util-json               86400  yes       sudo /usr/sbin/smartctl -a /dev/sda
ospf-neighbor-json             60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
```

### Disable a Command

You can disable unnecessary commands. This can help reduce the compute resources the NetQ Agent consumes on the switch. For example, if your network does not run OSPF, you can disable the two OSPF commands:

```
cumulus@switch:~$ sudo netq config add agent command service-key ospf-neighbor-json enable False
Command Service ospf-neighbor-json is disabled

cumulus@switch:~$ sudo netq config show agent commands
 Service Key               Period  Active       Command
-----------------------  --------  --------  ---------------------------------------------------------------------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']
lldp-json                      60  yes       /usr/sbin/lldpctl -f json
clagctl-json                   60  yes       /usr/bin/clagctl -j
dpkg-query                  21600  yes       dpkg-query --show -f ${Package},${Version},${Status}\n
ptmctl-json                   120  yes       /usr/bin/ptmctl -d -j
mstpctl-bridge-json            60  yes       /sbin/mstpctl showall json
ports                        3600  yes       Netq Predefined Command
proc-net-dev                   30  yes       Netq Predefined Command
agent_stats                   300  yes       Netq Predefined Command
agent_util_stats               30  yes       Netq Predefined Command
tcam-resource-json            120  yes       /usr/cumulus/bin/cl-resource-query -j
btrfs-json                   1800  yes       /sbin/btrfs fi usage -b /
config-mon-json               120  yes       Netq Predefined Command
running-config-mon-json        30  yes       Netq Predefined Command
cl-support-json               180  yes       Netq Predefined Command
resource-util-json            120  yes       findmnt / -n -o FS-OPTIONS
smonctl-json                   30  yes       /usr/sbin/smonctl -j
ssd-util-json               86400  yes       sudo /usr/sbin/smartctl -a /dev/sda
ospf-neighbor-json             60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
```

### Reset to Default

To revert to the original command settings, run:

```
cumulus@switch:~$ sudo netq config agent factory-reset commands
Netq Command factory reset successful
```
