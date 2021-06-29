---
title: Manage NetQ Agents
author: NVIDIA
weight: 700
toc: 3
---
At various points in time, you might want to change which network nodes are being monitored by NetQ or look more closely at a network node for troubleshooting purposes. Adding the NetQ Agent to a switch or host is described in {{<link url="Install-NetQ" text="Install NetQ">}}. Viewing the status of an Agent, disabling an Agent, managing NetQ Agent logging, and configuring the events the agent collects are presented here.

## View NetQ Agent Status

To view the health of your NetQ Agents, run:

```
netq [<hostname>] show agents [fresh | dead | rotten | opta] [around <text-time>] [json]
```

You can view the status for a given switch, host or NetQ Appliance or Virtual Machine. You can also filter by the status and view the status at a time in the past.

To view the current status of all NetQ Agents:

```
cumulus@switch~:$ netq show agents
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
border01          Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:54 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:38 2020
border02          Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:57 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:33 2020
fw1               Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:44 2020  Tue Sep 29 21:24:48 2020  Tue Sep 29 21:24:48 2020   Thu Oct  1 16:07:26 2020
fw2               Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:42 2020  Tue Sep 29 21:24:48 2020  Tue Sep 29 21:24:48 2020   Thu Oct  1 16:07:22 2020
leaf01            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 16:49:04 2020  Tue Sep 29 21:24:49 2020  Tue Sep 29 21:24:49 2020   Thu Oct  1 16:07:10 2020
leaf02            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:14 2020  Tue Sep 29 21:24:49 2020  Tue Sep 29 21:24:49 2020   Thu Oct  1 16:07:30 2020
leaf03            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:37 2020  Tue Sep 29 21:24:49 2020  Tue Sep 29 21:24:49 2020   Thu Oct  1 16:07:24 2020
leaf04            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:35 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:13 2020
oob-mgmt-server   Fresh            yes      3.1.1-ub18.04u29~1599111022.78b9e43  Mon Sep 21 16:43:58 2020  Mon Sep 21 17:55:00 2020  Mon Sep 21 17:55:00 2020   Thu Oct  1 16:07:31 2020
server01          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:16 2020
server02          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:24 2020
server03          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:56 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:12 2020
server04          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:17 2020
server05          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:25 2020
server06          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:21 2020
server07          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:06:48 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:28 2020
server08          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:06:45 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:31 2020
spine01           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:34 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:20 2020
spine02           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:33 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:16 2020
spine03           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:34 2020  Tue Sep 29 21:25:07 2020  Tue Sep 29 21:25:07 2020   Thu Oct  1 16:07:20 2020
spine04           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:32 2020  Tue Sep 29 21:25:07 2020  Tue Sep 29 21:25:07 2020   Thu Oct  1 16:07:33 2020

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

You can view the current configuration of a NetQ Agent to determine what data is being collected and where it is being sent. To view this configuration, run:

```
netq config show agent [kubernetes-monitor|loglevel|stats|sensors|frr-monitor|wjh|wjh-threshold|cpu-limit] [json]
```

This example shows a NetQ Agent in an on-premises deployment, talking to an appliance or VM at 127.0.0.1 using the default ports and VRF. No special configuration is included to monitor kubernetes, FRR, interface statistics, sensors, WJH. No limit has been set on the CPU usage or alter the default logging level.

```
cumulus@switch:~$ netq config show agent
netq-agent             value      default
---------------------  ---------  ---------
exhibitport
exhibiturl
server                 127.0.0.1  127.0.0.1
cpu-limit              100        100
agenturl
enable-opta-discovery  True       True
agentport              8981       8981
port                   31980      31980
vrf                    default    default
()
```

To view the configuration of a particular aspect of a NetQ Agent, use the various options.

This example show a NetQ Agent that has been configured with a CPU limit of 60%.

```
cumulus@switch:~$ netq config show agent cpu-limit
CPU Quota
-----------
60%
()
```

## Modify the Configuration of the NetQ Agent on a Node

The agent configuration commands enable you to do the following:

- Add, Disable, and Remove a NetQ Agent
- Start and Stop a NetQ Agent
- Configure a NetQ Agent to Collect Selected Data (CPU usage limit, FRR, Kubernetes, sensors, WJH)
- Configure a NetQ Agent to Send Data to a Server Cluster
- Troubleshoot the NetQ Agent

{{<notice note>}}

Commands apply to one agent at a time, and are run from the switch or host where the NetQ Agent resides.

{{</notice>}}

### Add and Remove a NetQ Agent

Adding or removing a NetQ Agent is to add or remove the IP address (and port and VRF when specified) from NetQ configuration file (at */etc/netq/netq.yml*). This adds or removes the information about the appliance or VM where the agent sends the data it collects.

To use the NetQ CLI to add or remove a NetQ Agent on a switch or host, run:

```
netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>]
netq config del agent server
```

If you want to use a specific port on the appliance or VM, use the `port` option. If you want the data sent over a particular virtual route interface, use the `vrf` option.

This example shows how to add a NetQ Agent and tell it to send the data it collects to the NetQ Appliance or VM at the IPv4 address of 10.0.0.23 using the default port (on-premises = 31980; cloud = 443) and vrf (default).

```
cumulus@switch~:$ netq config add agent server 10.0.0.23
cumulus@switch~:$ netq config restart agent
```

<!-- vale off -->
### Disable and Re-enable a NetQ Agent
<!-- vale on -->

You can temporarily disable NetQ Agent on a node. Disabling the NetQ Agent maintains the data already collected in the NetQ database, but stops the NetQ Agent from collecting new data until it is re-enabled.

To disable a NetQ Agent, run:

```
cumulus@switch:~$ netq config stop agent
```

To re-enable a NetQ Agent, run:

```
cumulus@switch:~$ netq config restart agent
```

### Configure a NetQ Agent to Limit Switch CPU Usage

While not typically an issue, you can restrict the NetQ Agent from using more than a configurable amount of the CPU resources. This setting requires Cumulus Linux versions 3.6.x, 3.7.x or 4.1.0 or later to be running on the switch.

For more detail about this feature, refer to this [Knowledge Base article]({{<ref "knowledge-base/Configuration-and-Usage/Cumulus-NetQ/NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches">}}).

This example limits a NetQ Agent from consuming more than 40% of the CPU resources on a Cumulus Linux switch.

```
cumulus@switch:~$ netq config add agent cpu-limit 40
cumulus@switch:~$ netq config restart agent
```

To remove the limit, run:

```
cumulus@switch:~$ netq config del agent cpu-limit
cumulus@switch:~$ netq config restart agent
```

### Configure a NetQ Agent to Collect Data from Selected Services

You can enable and disable collection of data from the FRR (FR Routing), Kubernetes, sensors, and WJH (What Just Happened) by the NetQ Agent.

To configure the agent to start or stop collecting **FRR** data, run:

```
cumulus@chassis~:$ netq config add agent frr-monitor
cumulus@switch:~$ netq config restart agent

cumulus@chassis~:$ netq config del agent frr-monitor
cumulus@switch:~$ netq config restart agent
```

To configure the agent to start or stop collecting **Kubernetes** data, run:

```
cumulus@switch:~$ netq config add agent kubernetes-monitor
cumulus@switch:~$ netq config restart agent

cumulus@switch:~$ netq config del agent kubernetes-monitor
cumulus@switch:~$ netq config restart agent
```

To configure the agent to start or stop collecting chassis **sensor** data, run:

```
cumulus@chassis~:$ netq config add agent sensors
cumulus@switch:~$ netq config restart agent

cumulus@chassis~:$ netq config del agent sensors
cumulus@switch:~$ netq config restart agent
```

{{<notice note>}}
This command is only valid when run on a chassis, not a switch.
{{</notice>}}

To configure the agent to start or stop collecting **WJH** data, run:

```
cumulus@chassis~:$ netq config add agent wjh
cumulus@switch:~$ netq config restart agent

cumulus@chassis~:$ netq config del agent wjh
cumulus@switch:~$ netq config restart agent
```

### Configure a NetQ Agent to Send Data to a Server Cluster

If you have a server cluster arrangement for NetQ, you should configure the NetQ Agent to send the data it collects to every server in the cluster.

To configure the agent to send data to the servers in your cluster, run:

```
netq config add agent cluster-servers <text-opta-ip-list> [port <text-opta-port>] [vrf <text-vrf-name>]
```

The list of IP addresses  must be separated by commas, but no spaces. You can optionally specify a port or VRF.

This example configures the NetQ Agent on a switch to send the data to three servers located at *10.0.0.21*, *10.0.0.22*, and *10.0.0.23* using the *rocket* VRF.

```
cumulus@switch:~$ netq config add agent cluster-servers 10.0.0.21,10.0.0.22,10.0.0.23 vrf rocket
```

To stop a NetQ Agent from sending data to a server cluster, run:

```
cumulus@switch:~$ netq config del agent cluster-servers
```

### Configure Logging to Troubleshoot a NetQ Agent

The logging level used for a NetQ Agent determines what types of events
are logged about the NetQ Agent on the switch or host.

First, you need to decide what level of logging you want to configure. You can configure the logging level to be the same for every NetQ Agent, or selectively increase or decrease the logging level for a NetQ Agent on a problematic node.

| Logging Level | Description |
| ------------- | ------------------ |
| debug | Sends notifications for all debugging-related, informational, warning, and error messages. |
| info | Sends notifications for informational, warning, and error messages (default). |
| warning | Sends notifications for warning and error messages. |
| error | Sends notifications for errors messages. |

You can view the NetQ Agent log directly. Messages have the following structure:

`<timestamp> <node> <service>[PID]: <level>: <message>`

| Element | Description |
| ---------- | -------------- |
| timestamp | Date and time event occurred in UTC format|
| node | Hostname of network node where event occurred |
| service \[PID\] | Service and Process IDentifier that generated the event |
| level | Logging level in which the given event is classified; *debug*, *error*, *info*, or *warning* |
| message | Text description of event, including the node where the event occurred |

For example:

{{<figure src="/images/netq/NetQAgentLogFormat.png" height="69" width="747">}}

This example shows a portion of a NetQ Agent log with debug level logging.

    ...
    2020-02-16T18:45:53.951124+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery exhibit url switch.domain.com port 4786
    2020-02-16T18:45:53.952035+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery Agent ID spine-1
    2020-02-16T18:45:53.960152+00:00 spine-1 netq-agent[8600]: INFO: Received Discovery Response 0
    2020-02-16T18:46:54.054160+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery exhibit url switch.domain.com port 4786
    2020-02-16T18:46:54.054509+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery Agent ID spine-1
    2020-02-16T18:46:54.057273+00:00 spine-1 netq-agent[8600]: INFO: Received Discovery Response 0
    2020-02-16T18:47:54.157985+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery exhibit url switch.domain.com port 4786
    2020-02-16T18:47:54.158857+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery Agent ID spine-1
    2020-02-16T18:47:54.171170+00:00 spine-1 netq-agent[8600]: INFO: Received Discovery Response 0
    2020-02-16T18:48:54.260903+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery exhibit url switch.domain.com port 4786
    ...

To configure **debug**-level logging:

1. Set the logging level to *debug.*

    ```
    cumulus@switch:~$ netq config add agent loglevel debug
    ```

2. Restart the NetQ Agent.

    ```
    cumulus@switch:~$ netq config restart agent
    ```

3. Optionally, verify connection to the NetQ appliance or VM by viewing the `netq-agent.log` messages.

To configure **warning**-level logging:

```
cumulus@switch:~$ netq config add agent loglevel warning
cumulus@switch:~$ netq config restart agent
```

#### Disable Agent Logging

If you have set the logging level to *debug* for troubleshooting, it is recommended that you either change the logging level to a less heavy mode or completely disable agent logging altogether when you are finished troubleshooting.

To change the logging level from debug to another level, run:

```
cumulus@switch:~$ netq config add agent loglevel [info|warning|error]
cumulus@switch:~$ netq config restart agent
```

To disable all logging:

```
cumulus@switch:~$ netq config del agent loglevel
cumulus@switch:~$ netq config restart agent
```

## Change NetQ Agent Polling Data and Frequency

The NetQ Agent contains a pre-configured set of modular commands that run periodically and send event and resource data to the NetQ appliance or VM. You can fine tune which events the agent can poll and vary frequency of polling using the NetQ CLI.

For example, if your network is not running OSPF, you can disable the command that polls for OSPF events. Or you can decrease the polling interval for LLDP from the default of 60 seconds to 120 seconds. By not polling for selected data or polling less frequently, you can reduce switch CPU usage by the NetQ Agent.

Depending on the switch platform, some supported protocol commands may not be executed by the NetQ Agent. For example, if a switch has no VXLAN capability, then all VXLAN-related commands get skipped by agent.

You cannot create new commands in this release.

### Supported Commands

To see the list of supported modular commands, run:

```
cumulus@switch:~$ netq config show agent commands
 Service Key               Period  Active       Command
-----------------------  --------  --------  ---------------------------------------------------------------------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']
lldp-json                     120  yes       /usr/sbin/lldpctl -f json
clagctl-json                   60  yes       /usr/bin/clagctl -j
dpkg-query                  21600  yes       dpkg-query --show -f ${Package},${Version},${Status}\n
ptmctl-json                   120  yes       ptmctl
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
sensors-json                   30  yes       sensors -u
ssd-util-json               86400  yes       sudo /usr/sbin/smartctl -a /dev/sda
ospf-neighbor-json             60  yes       ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  yes       ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
```

The NetQ predefined commands are described as follows:

- **agent_stats**: Collects statistics about the NetQ Agent every five (5) minutes.
- **agent_util_stats**: Collects switch CPU and memory utilization by the NetQ Agent every 30 seconds.
- **cl-support-json**: Polls the switch every three (3) minutes to determine if a `cl-support` file was generated.
- **config-mon-json**: Polls the */etc/network/interfaces*, */etc/frr/frr.conf*, */etc/lldpd.d/README.conf* and */etc/ptm.d/topology.dot* files every two (2) minutes to determine if the contents of any of these files has changed. If a change has occurred, the contents of the file and its modification time are transmitted to the NetQ appliance or VM.
- **ports**: Polls for optics plugged into the switch every hour.
- **proc-net-dev**: Polls for network statistics on the switch every 30 seconds.
- **running-config-mon-json**: Polls the `clagctl` parameters every 30 seconds and sends a diff of any changes to the NetQ appliance or VM.

### Modify the Polling Frequency

You can change the polling frequency of a modular command. The frequency is specified in seconds. For example, to change the polling frequency of the `lldp-json` command to 60 seconds from its default of 120 seconds, run:

```
cumulus@switch:~$ netq config add agent command service-key lldp-json poll-period 60
Successfully added/modified Command service lldpd command /usr/sbin/lldpctl -f json

cumulus@switch:~$ netq config show agent commands
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
sensors-json                   30  yes       sensors -u
ssd-util-json               86400  yes       sudo /usr/sbin/smartctl -a /dev/sda
ospf-neighbor-json             60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
```

### Disable a Command

You can disable any of these commands if they are not needed on your network. This can help reduce the compute resources the NetQ Agent consumes on the switch. For example, if your network does not run OSPF, you can disable the two OSPF commands:

```
cumulus@switch:~$ netq config add agent command service-key ospf-neighbor-json enable False
Command Service ospf-neighbor-json is disabled

cumulus@switch:~$ netq config show agent commands
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
sensors-json                   30  yes       sensors -u
ssd-util-json               86400  yes       sudo /usr/sbin/smartctl -a /dev/sda
ospf-neighbor-json             60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
```

### Reset to Default

To quickly revert to the original command settings, run:

```
cumulus@switch:~$ netq config agent factory-reset commands
Netq Command factory reset successful

cumulus@switch:~$ netq config show agent commands
 Service Key               Period  Active       Command
-----------------------  --------  --------  ---------------------------------------------------------------------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']
lldp-json                     120  yes       /usr/sbin/lldpctl -f json
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
sensors-json                   30  yes       sensors -u
ssd-util-json               86400  yes       sudo /usr/sbin/smartctl -a /dev/sda
ospf-neighbor-json             60  yes       ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  yes       ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
```
