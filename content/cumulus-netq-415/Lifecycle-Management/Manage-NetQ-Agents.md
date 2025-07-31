---
title: Manage NetQ Agents
author: NVIDIA
weight: 700
toc: 3
---

Run the following commands to view the status of an agent, disable an agent, manage logging, and configure the events the agent collects.

## View NetQ Agent Status

The syntax for the NetQ Agent status command is:

```
netq [<hostname>] show agents
    [fresh | dead | rotten | opta]
    [around <text-time>]
    [json]
```

You can view the status for a given switch, host or NetQ virtual machine. You can also filter by the status and view the status at a time in the past.

To view the current status of all NetQ Agents, run:

```
nvidia@switch~:$ netq show agents
```

To view NetQ Agents that are not communicating, run:

```
nvidia@switch~:$ netq show agents rotten
No matching agents records found
```

To view NetQ Agent status on the NetQ VM, run:

```
nvidia@switch~:$ netq show agents opta
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
netq-appliance    Fresh            yes      4.15.0-ub24.04u52~1744815786.8dbbbd2 Mon Mar  3 16:30:50 2025  Mon Mar  3 19:52:26 2025  Mon Mar  3 19:52:59 2025   Tue Mar  4 18:57:09 2025 
```

## View NetQ Agent Configuration

You can view the current configuration of a NetQ Agent to determine what data it collects and where it sends that data. The syntax for this command is:

```
sudo netq config show agent 
    [asic-monitor|cpu-limit|frr-monitor|global-timeout|loglevel|ssl|spice|stats|wjh|wjh-threshold] 
    [json]
```

The following example shows a NetQ Agent in an on-premises deployment, connected to and communicating with a VM at 127.0.0.1 using the default ports and VRF.

```
nvidia@switch:~$ sudo netq config show agent
netq-agent                value      default
------------------------  ---------  ---------
exhibitport
exhibiturl
server                    127.0.0.1  127.0.0.1
cpu-limit                 100        100
agenturl
wjh                       Enabled    Enabled
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
agent-hostname            cumulus    cumulus
()
```

To view the configuration of a particular aspect of a NetQ Agent, use the various options.

This example shows a NetQ Agent configured with a CPU limit of 60%.

```
nvidia@switch:~$ sudo netq config show agent cpu-limit
CPU Quota
-----------
60%
()
```

## Modify the Configuration of the NetQ Agent on a Node

The agent configuration commands let you:

- Add, disable, and remove a NetQ Agent
- Start and stop a NetQ Agent
- Configure a NetQ Agent to collect selected data (CPU usage limit, FRR, WJH)
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
nvidia@switch~:$ sudo netq config add agent server 10.0.0.23
nvidia@switch~:$ sudo netq config restart agent
```

This example shows how to add a NetQ Agent and tell it to send the data it collects to the NetQ server at the IPv4 address of 10.0.0.23 using the default port (port 31980 for on-premises and port 443 for cloud deployments) and the `default` VRF for a switch managed through an in-band connection on interface `swp1`:

```
nvidia@switch~:$ sudo netq config add agent server 10.0.0.23 vrf default inband-interface swp1
nvidia@switch~:$ sudo netq config restart agent
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
nvidia@switch:~$ sudo netq config stop agent
```

To reenable a NetQ Agent, run:

```
nvidia@switch:~$ sudo netq config restart agent
```

### Configure a NetQ Agent to Limit Switch CPU Usage

You can limit the NetQ Agent to use only a certain percentage of CPU resources on a switch. This setting requires a switch running Cumulus Linux versions 3.7, 4.1, or later.

For more detail about this feature, refer to this [Knowledge Base article]({{<ref "knowledge-base/Configuration-and-Usage/Cumulus-NetQ/NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches">}}).

This example limits a NetQ Agent from consuming more than 40% of the CPU resources on a Cumulus Linux switch.

```
nvidia@switch:~$ sudo netq config add agent cpu-limit 40
nvidia@switch:~$ sudo netq config restart agent
```

To remove the limit, run:

```
nvidia@switch:~$ sudo netq config del agent cpu-limit
nvidia@switch:~$ sudo netq config restart agent
```

### Configure a NetQ Agent to Collect Data from Selected Services

You can enable and disable data collection about FRRouting (FRR) and What Just Happened (WJH).

To configure the agent to start or stop collecting FRR data, run:

```
nvidia@chassis~:$ sudo netq config add agent frr-monitor
nvidia@switch:~$ sudo netq config restart agent

nvidia@chassis~:$ sudo netq config del agent frr-monitor
nvidia@switch:~$ sudo netq config restart agent
```

To configure the agent to start or stop collecting WJH data, run:

```
nvidia@chassis~:$ sudo netq config add agent wjh
nvidia@switch:~$ sudo netq config restart agent

nvidia@chassis~:$ sudo netq config del agent wjh
nvidia@switch:~$ sudo netq config restart agent
```

### Configure a NetQ Agent to Send Data to a Server Cluster

If you have a high-availability server cluster arrangement, you should configure the NetQ Agent to distribute data across all servers in the cluster. For {{<link title="Set Up Your Virtual Machine for an On-premises HA Scale Cluster" text="scale cluster deployments">}}, configure the agent with the IP address of the `master-ip` and each `ha-node`. For 5-node deployments, you do not need to specify the `worker-nodes`. Refer to {{<link title="Install NetQ Agents/#configure-netq-agents" text="Configure NetQ Agents">}} for step-by-step instructions.

To configure the agent to send data to the servers in your cluster, run:

```
sudo netq config add agent cluster-servers <text-opta-ip-list> [port <text-opta-port>] [vrf <text-vrf-name>]
```

You must separate the list of IP addresses by commas (not spaces). You can optionally specify a port or VRF.

This example configures the NetQ Agent on a switch to send the data to three servers located at *10.0.0.21*, *10.0.0.22*, and *10.0.0.23* using the *mgmt* VRF.

```
nvidia@switch:~$ sudo netq config add agent cluster-servers 10.0.0.21,10.0.0.22,10.0.0.23 vrf mgmt
```

To stop a NetQ Agent from sending data to a server cluster, run:

```
nvidia@switch:~$ sudo netq config del agent cluster-servers
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
    nvidia@switch:~$ sudo netq config add agent loglevel debug
    ```

2. Restart the NetQ Agent:

    ```
    nvidia@switch:~$ sudo netq config restart agent
    ```

3. (Optional) Verify the connection to the NetQ VM by viewing the `netq-agent.log` messages.

#### Disable Agent Logging

If you set the logging level to *debug* for troubleshooting, NVIDIA recommends that you either change the logging level to a less verbose mode or disable agent logging when you finish troubleshooting.

To change the logging level from debug to another level, run:

```
nvidia@switch:~$ sudo netq config add agent loglevel [info|warning|error]
nvidia@switch:~$ sudo netq config restart agent
```

To disable all logging:

```
nvidia@switch:~$ sudo netq config del agent loglevel
nvidia@switch:~$ sudo netq config restart agent
```

## Change NetQ Agent Polling Data and Frequency

The NetQ Agent contains a pre-configured set of modular commands that run periodically and send event and resource data to the NetQ VM. You can fine tune which events the agent can poll and vary frequency of polling using the NetQ CLI.

For example, if your network is not running EVPN, you can disable the command that polls for EVPN events. Or you can decrease the polling interval for LLDP from the default of 60 seconds to 120 seconds. By not polling for selected data or polling less frequently, you can reduce switch CPU usage by the NetQ Agent.

Depending on the switch platform, the NetQ Agent might not execute some supported protocol commands. For example, if a switch has no VXLAN capability, then the agent skips all VXLAN-related commands.

### Supported Commands

To see the list of supported modular commands, run:

```
nvidia@switch:~$ sudo netq config show agent commands
Service Key               Period  Active       Command                                                        Timeout
-----------------------  --------  --------  --------------------------------------------------------------  ---------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']         30
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']               30
lldp-json                     120  yes       /usr/sbin/lldpctl -f json                                              30
clagctl-json                   60  yes       /usr/bin/clagctl -j                                                    30
mstpctl-bridge-json            60  yes       /sbin/mstpctl showall json                                             30
ports                        3600  yes       Netq Predefined Command                                                30
proc-net-dev                   30  yes       Netq Predefined Command                                                30
dom                          1800  yes       Netq Predefined Command                                                30
roce                           60  yes       Netq Predefined Command                                                30
roce-config                   300  yes       Netq Predefined Command                                                30
nvue-roce-config              300  yes       Netq Predefined Command                                                30
ntp                            30  yes       Netq Predefined Command                                                45
agent_stats                   300  yes       Netq Predefined Command                                                30
agent_util_stats              300  yes       Netq Predefined Command                                                30
tcam-resource-json            300  yes       /usr/cumulus/bin/cl-resource-query -j                                  30
nvue-mon-json                 300  yes       Netq Predefined Command                                                30
cl-support-json              3600  yes       Netq Predefined Command                                                30
resource-util-json            300  yes       findmnt / -n -o FS-OPTIONS                                             30
smonctl-json                  120  yes       /usr/sbin/smonctl -j                                                   30
sensors-json                 1800  yes       sensors -u                                                             30
ssd-util-json               86400  yes       /usr/sbin/smartctl -a /dev/sda                                         30
ssd-util-nvme-json          86400  yes       /usr/sbin/smartctl -a /dev/nvme0                                       30
ecmp-hash-info                300  yes       cat /etc/cumulus/datapath/traffic.conf                                 30
ecmp-info                      60  yes       Netq Predefined Command                                                30
ptp-config-info                60  yes       cat /etc/ptp4l.conf                                                    30
ptp-clock-info                 60  yes       Netq Predefined Command                                                30
ptp-clock-status               60  yes       Netq Predefined Command                                                30
ptp-statistics                 60  yes       Netq Predefined Command                                                30
ptp-correction                 30  yes       Netq Predefined Command                                                30
log-exporter                   60  yes       Netq Predefined Command                                                30
adaptive-routing-config       300  yes       Netq Predefined Command                                                30
ber-info                       30  yes       Netq Predefined Command                                                30
```
### Modify the Polling Frequency

You can change the polling frequency (in seconds) of a modular command. For example, to change the polling frequency of the `ntp` command to 60 seconds from its default of 30 seconds, run:

```
nvidia@switch:~$ sudo netq config add agent command service-key ntp poll-period 30
Successfully added/modified Command service misc command None

nvidia@switch:~$ sudo netq config show agent commands
Service Key               Period  Active       Command                                                        Timeout
-----------------------  --------  --------  --------------------------------------------------------------  ---------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']         30
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']               30
lldp-json                     120  yes       /usr/sbin/lldpctl -f json                                              30
clagctl-json                   60  yes       /usr/bin/clagctl -j                                                    30
mstpctl-bridge-json            60  yes       /sbin/mstpctl showall json                                             30
ports                        3600  yes       Netq Predefined Command                                                30
proc-net-dev                   30  yes       Netq Predefined Command                                                30
dom                          1800  yes       Netq Predefined Command                                                30
roce                           60  yes       Netq Predefined Command                                                30
roce-config                   300  yes       Netq Predefined Command                                                30
nvue-roce-config              300  yes       Netq Predefined Command                                                30
ntp                            60  yes       Netq Predefined Command                                                45
agent_stats                   300  yes       Netq Predefined Command                                                30
agent_util_stats              300  yes       Netq Predefined Command                                                30
tcam-resource-json            300  yes       /usr/cumulus/bin/cl-resource-query -j                                  30
nvue-mon-json                 300  yes       Netq Predefined Command                                                30
cl-support-json              3600  yes       Netq Predefined Command                                                30
resource-util-json            300  yes       findmnt / -n -o FS-OPTIONS                                             30
smonctl-json                  120  yes       /usr/sbin/smonctl -j                                                   30
sensors-json                 1800  yes       sensors -u                                                             30
ssd-util-json               86400  yes       /usr/sbin/smartctl -a /dev/sda                                         30
ssd-util-nvme-json          86400  yes       /usr/sbin/smartctl -a /dev/nvme0                                       30
ecmp-hash-info                300  yes       cat /etc/cumulus/datapath/traffic.conf                                 30
ecmp-info                      60  yes       Netq Predefined Command                                                30
ptp-config-info                60  yes       cat /etc/ptp4l.conf                                                    30
ptp-clock-info                 60  yes       Netq Predefined Command                                                30
ptp-clock-status               60  yes       Netq Predefined Command                                                30
ptp-statistics                 60  yes       Netq Predefined Command                                                30
ptp-correction                 30  yes       Netq Predefined Command                                                30
log-exporter                   60  yes       Netq Predefined Command                                                30
adaptive-routing-config       300  yes       Netq Predefined Command                                                30
ber-info                       30  yes       Netq Predefined Command                                                30
```

### Disable a Command

You can disable unnecessary commands. This can help reduce the compute resources the NetQ Agent consumes on the switch. For example, if your network does not run EVPN, you can disable the EVPN command:

```
nvidia@switch:~$ sudo netq config add agent command service-key evpn-vni enable False
Command Service evpn-vni is disabled
```

### Reset to Default

To revert to the original command settings, run:

```
nvidia@switch:~$ sudo netq config agent factory-reset commands
Netq Command factory reset successful
```
