---
title: Manage NetQ Agents
author: Cumulus Networks
weight: 590
toc: 3
---
At various points in time, you might want to change which network nodes are being monitored by NetQ or look more closely at a network node for troubleshooting purposes. Adding the NetQ Agent to a switch or host is described in {{<link url="Install-NetQ" text="Install NetQ">}}. Viewing the status of an Agent, disabling an Agent, and managing NetQ Agent logging are presented.

## View NetQ Agent Status

To view the health of your NetQ Agents, use the `netq show agents` command:

```
netq [<hostname>] show agents [fresh | dead | rotten | opta] [around <text-time>] [json]
```
You can view the status for a given switch, host or NetQ server. You can also filter by the status as well as view the status at a time in the past.

To view the current status of all NetQ Agents:

```
cumulus@switch~:$ netq show agents
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
exit-1            Fresh            yes      2.2.1-cl3u19~1564503011.e3b463d      1d:4h:35m:11s             1d:4h:14m:34s             1d:4h:14m:34s              Wed Jul 31 16:50:40 2019
exit-2            Fresh            yes      2.2.1-cl3u19~1564503011.e3b463d      1d:4h:35m:11s             1d:4h:14m:30s             1d:4h:14m:30s              Wed Jul 31 16:51:07 2019
firewall-1        Fresh            yes      2.2.1-ub16.04u19~1564494614.6fed81f  1d:4h:35m:11s             1d:4h:14m:24s             1d:4h:14m:24s              Wed Jul 31 16:51:13 2019
firewall-2        Fresh            yes      2.2.1-rh7u19~1564496494.6fed81f      1d:4h:34m:35s             1d:4h:14m:18s             1d:4h:14m:18s              Wed Jul 31 16:51:06 2019
hostd-11          Fresh            yes      2.2.1-ub16.04u19~1564494614.6fed81f  1d:4h:35m:6s              1d:4h:14m:6s              1d:4h:14m:6s               Wed Jul 31 16:51:16 2019
hostd-12          Fresh            yes      2.2.1-rh7u19~1564496494.6fed81f      1d:4h:34m:40s             1d:4h:14m:2s              1d:4h:14m:2s               Wed Jul 31 16:51:40 2019
...
```

To view NetQ Agents that are not communicating:

```
cumulus@switch~:$ netq show agents rotten
No matching agents records found
```

To view NetQ Agent status on the NetQ Server or Appliance, run the following command from a node:

```
cumulus@leaf01~:$ netq show agents opta
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
10-20-14-157      Fresh            yes      2.2.1-cl3u19~1564299612.73c7ab4      1d:5h:40m:41s             6m:34.417s                6m:34.417s                 Wed Jul 31 22:12:40 2019
```

## Modify the Configuration of the NetQ Agent on a Node

The agent configuration commands enable you to do the following:

- add and remove agents from switches and hosts
- start and stop agent operations
- add and remove Kubernetes container monitoring
- add or remove sensors
- debug the agent
- add or remove FRR (FRRouting)
- set a limit on how many CPU resources the agent can consume on a Cumulus Linux switch
- send data to the cluster nodes
- collect What Just Happened data on a Mellanox switch

{{%notice note%}}

Commands apply to one agent at a time,
and are run from the switch or host where the NetQ Agent resides.

{{%/notice%}}

The agent configuration commands include:

    netq config add agent cluster-servers <text-opta-ip-list> [port <text-opta-port>] [vrf <text-vrf-name>]
    netq config add agent cpu-limit [<text-limit-number>]
    netq config add agent frr-monitor [<text-frr-docker-name>]
    netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
    netq config add agent loglevel [debug|error|info|warning]
    netq config add agent sensors
    netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>]
    netq config (start|stop|status|restart) agent
    netq config del agent (cluster-servers|cpu-limit|frr-monitor|kubernetes-monitor|loglevel|sensors|server|stats|wjh)
    netq config show agent [cpu-limit|frr-monitor|kubernetes-monitor|loglevel|sensors|stats|wjh] [json]

This example shows how to specify the IP address and optionally a
specific port on the NetQ Platform where agents should send their data.

    cumulus@switch~:$ netq config add agent server 10.0.0.23

This example shows how to configure the agent to send sensor data.

    cumulus@switch~:$ netq config add agent sensors

This example shows how to start monitoring with Kubernetes.

    cumulus@switch:~$ netq config add agent kubernetes-monitor

This example shows how to configure the agent to send data to the cluster nodes.
You can optionally specify a port or VRF.

    cumulus@switch:~$ netq config add agent cluster-servers 10.0.0.21,10.0.0.22,10.0.0.23 vrf rocket

This example shows how to prevent the agent from consuming no more than 40% of
CPU resources on a Cumulus Linux switch. This setting requires Cumulus Linux
versions 3.7.12 or later and 4.1.0 or later to be running on the switch.

    netq config add agent cpu-limit 40

{{%notice note%}}
After making configuration changes to your agents, you must restart the
agent for the changes to take effect. Use the `netq config restart agent`
command.
{{%/notice%}}

## Disable the NetQ Agent on a Node

You can temporarily disable NetQ Agent on a node. Disabling the agent
maintains the activity history in the NetQ database.

To disable NetQ Agent on a node, run the following command from the
node:

    cumulus@switch:~$ netq config stop agent

## Remove the NetQ Agent from a Node

You can decommission a NetQ Agent on a given node. You might need to do
this when you:

  - RMA the switch or host being monitored
  - Change the hostname of the switch or host being monitored
  - Move the switch or host being monitored from one data center to
    another

{{%notice note%}}

Decommissioning the node removes the agent server settings from the
local configuration file.

{{%/notice%}}

To decommission a node from the NetQ database:

1.  On the given node, stop and disable the NetQ Agent service.

        cumulus@switch:~$ sudo systemctl stop netq-agent
        cumulus@switch:~$ sudo systemctl disable netq-agent

2.  On the NetQ Appliance or Platform, decommission the node.

        cumulus@netq-appliance:~$ netq decommission <hostname>

## Configure Logging for a NetQ Agent

The logging level used for a NetQ Agent determines what types of events
are logged about the NetQ Agent on the switch or host.

First, you need to decide what level of
logging you want to configure. You can configure the logging level to be
the same for every NetQ Agent, or selectively increase or decrease the
logging level for a NetQ Agent on a problematic node.

| Logging Level | Description                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| debug         | Sends notifications for all debugging-related, informational, warning, and error messages.                            |
| info          | Sends notifications for informational, warning, and error messages (default). |
| warning       | Sends notifications for warning and error messages.                            |
| error         | Sends notifications for errors messages.                                      |

You can view the NetQ Agent log directly. Messages have the following
structure:

`<timestamp> <node> <service>[PID]: <level>: <message>`

| Element         | Description                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------- |
| timestamp       | Date and time event occurred in UTC format                                                   |
| node            | Hostname of network node where event occurred                                                |
| service \[PID\] | Service and Process IDentifier that generated the event                                      |
| level           | Logging level in which the given event is classified; *debug*, *error*, *info*, or *warning* |
| message         | Text description of event, including the node where the event occurred                       |

For example:

{{<figure src="/images/netq/NetQAgentLogFormat.png" height="69" width="747">}}

This example shows a portion of a NetQ Agent log with debug level
logging.

    ...
    2019-02-16T18:45:53.951124+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery exhibit url hydra-09.cumulusnetworks.com port 4786
    2019-02-16T18:45:53.952035+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery Agent ID spine-1
    2019-02-16T18:45:53.960152+00:00 spine-1 netq-agent[8600]: INFO: Received Discovery Response 0
    2019-02-16T18:46:54.054160+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery exhibit url hydra-09.cumulusnetworks.com port 4786
    2019-02-16T18:46:54.054509+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery Agent ID spine-1
    2019-02-16T18:46:54.057273+00:00 spine-1 netq-agent[8600]: INFO: Received Discovery Response 0
    2019-02-16T18:47:54.157985+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery exhibit url hydra-09.cumulusnetworks.com port 4786
    2019-02-16T18:47:54.158857+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery Agent ID spine-1
    2019-02-16T18:47:54.171170+00:00 spine-1 netq-agent[8600]: INFO: Received Discovery Response 0
    2019-02-16T18:48:54.260903+00:00 spine-1 netq-agent[8600]: INFO: OPTA Discovery exhibit url hydra-09.cumulusnetworks.com port 4786
    ...

**Example: Configure debug-level logging**

1.  Set the logging level to *debug.*

        cumulus@switch:~$ netq config add agent loglevel debug

2.  Restart the NetQ Agent.

        cumulus@switch:~$ netq config restart agent

3.  Optionally, verify connection to the NetQ platform by viewing the
    `netq-agent.log` messages.

**Example: Configure warning-level logging**

    cumulus@switch:~$ netq config add agent loglevel warning
    cumulus@switch:~$ netq config restart agent

**Example: Disable Agent Logging**

If you have set the logging level to
*debug* for troubleshooting, it is recommended that you either change
the logging level to a less heavy mode or completely disable agent
logging altogether when you are finished troubleshooting.

To change the logging level, run the
following command and restart the agent service:

    cumulus@switch:~$ netq config add agent loglevel <LOG_LEVEL> 
    cumulus@switch:~$ netq config restart agent

To disable all logging:

    cumulus@switch:~$ netq config del agent loglevel 
    cumulus@switch:~$ netq config restart agent



