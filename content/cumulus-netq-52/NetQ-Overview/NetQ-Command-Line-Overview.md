---
title: NetQ Command Line Overview
author: NVIDIA
weight: 160
toc: 4
---

The NetQ command line interface (CLI) provides access to all network state and event information collected by NetQ Agents. It behaves similarly to typical CLIs, with groups of commands that display related information, and help commands that provide additional information. See the {{<link title="NetQ CLI Reference" text="command line reference">}} for a comprehensive list of NetQ commands, including examples, options, and definitions.

{{<notice note>}}

The NetQ CLI only runs on switches and server hosts implemented with Intel x86 or ARM-based architectures.

{{</notice>}}

## CLI Access

After you install or upgrade NetQ, you can also {{<link title="Install NetQ CLI" text="install and configure the CLI">}} on your NetQ server and hosts.

To access the CLI from a switch or server:

<!-- vale off -->
1. Log in to the device. The following example uses the default username of *cumulus* and a hostname of *switch*:

    ```
    <computer>:~<username>$ ssh nvidia@switch
    ```

2. Enter your password to reach the command prompt. The default password is *CumulusLinux\!*

3.  You can now run commands:

    ```
    nvidia@switch:~$ netq show agents
    ```
<!-- vale on -->

## Command Line Basics

This section describes the core structure and behavior of the NetQ CLI.

### Command Line Structure

The NetQ command line has a flat structure as opposed to a modal structure: you can run all commands from the standard command prompt instead of only in a specific mode, at the same level.

### Command Syntax

All NetQ CLI commands begin with `netq`. The commands you use to monitor your network fall into one of four main syntax categories: validation (check), monitoring (show), configuration, and trace.

```
netq check <network-protocol-or-service> [options]
netq show <network-protocol-or-service> [options]
netq config <action> <object> [options]
netq trace <destination> from <source> [options]
```

| Symbols  | Meaning  |
| -------- | -------- |
| Parentheses ( ) | Grouping of required parameters. Choose one. |
| Square brackets [ \] | Single or group of optional parameters. If more than one object or keyword is available, choose one. |
| Angle brackets \< \> | Required variable. Value for a keyword or option; enter according to your deployment nomenclature. |
| Pipe \| | Separates object and keyword options, also separates value options; enter one object or keyword and zero or one value. |

### Command Output

The command output presents results in color for many commands. Results with errors appear in red, and warnings appear in yellow. Results without errors or warnings appear in either black or green. VTEPs appear in blue. A node in the *pretty* output appears in **bold**, and angle brackets (\< \>) wrap around a router interface. To view the output with only black text, run the `netq config del color` command. You can view output with colors again by running `netq config add color`.

All check and show commands have a default timeframe of now to one hour ago, unless you specify an approximate time using the `around` keyword or a range using the `between` keyword. For example, running `netq check bgp` shows the status of BGP over the last hour. Running `netq show bgp around 3h` shows the status of BGP three hours ago.

{{%notice note%}}

When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: weeks
- **d**: days
- **h**: hours
- **m**: minutes
- **s**: seconds
- **now**

When using the `between` option, you can enter the start time (`text-time`) and end time (`text-endtime`) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure. Use the <code>around</code> option to view information for a particular time.

{{%/notice%}}

### Command Completion

As you enter commands, you can get help with the valid keywords or options using the **tab** key. For example, using tab completion with `netq check` displays the possible objects for the command, and returns you to the command prompt to complete the command:

```
nvidia@switch:~$ netq check <<press Tab>>
    addresses   :  IPv4/v6 addresses
    agents      :  Netq agent
    bgp         :  BGP info
    cl-version  :  Cumulus Linux version
    evpn        :  EVPN
    interfaces  :  network interface port
    mlag        :  Multi-chassis LAG (alias of clag)
    mtu         :  Link MTU
    ntp         :  NTP
    roce        :  RoCE
    sensors     :  Temperature/Fan/PSU sensors
    topology    :  Topology
    vlan        :  VLAN
    vxlan       :  VxLAN
nvidia@switch:~$ netq check
```

### Command Help

As you enter commands, you can get help with command syntax by entering `help` as part of the command. For example, to find out which options are available for an IP addresses check, enter the `netq check addresses` command followed by `help`:

```
nvidia@switch:~$ netq check addresses help
Commands:
    netq check addresses [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <addr-number-range-list> | exclude <addr-number-range-list>] [around <text-time>] [json | summary]
```

To see an exhaustive list of commands and their definitions, run:

```
nvidia@switch:~$ netq help list
```

To display NetQ command formatting rules, run:

```
nvidia@switch:~$ netq help verbose
```
### Command Abbreviations

NetQ supports command abbreviation, where you can type a certain number of characters instead of a whole command to speed up CLI interaction. For example, instead of typing `netq show status verbose`, you can type `netq sh st v`.

### Command History

The CLI stores commands issued within a session, which lets you review and rerun commands that you already ran. At the command prompt, press the **Up Arrow** and **Down Arrow** keys to move back and forth through the list of commands previously entered. When you have found a given command, you can run the command by pressing **Enter**, just as you would if you had entered it manually. You can also modify the command before you run it.

## Command Categories

While the CLI has a flat structure, NetQ commands are conceptually grouped into the following functional categories:

- {{<link url="#validation-commands" text="Validation Commands">}}
- {{<link url="#monitoring-commands" text="Monitoring Commands">}}
- {{<link url="#configuration-commands" text="Configuration Commands">}}
- {{<link url="#trace-commands" text="Trace Commands">}}

### Validation Commands

The {{<link title="check" text="netq check commands">}} validate the current or historical state of the network by looking for errors and misconfigurations in the network. The commands run fabric-wide validations against various configured protocols and services to determine how well the network is operating. You can perform validation checks for the following:

<!-- vale off -->
- **addresses**: IPv4 and IPv6 addresses duplicates across devices
- **agents**: NetQ Agents operation on all switches and hosts
- **bgp**: BGP (Border Gateway Protocol) operation across the network
  fabric
- **clag**: Cumulus Linux MLAG (multi-chassis LAG/link aggregation) operation
- **cl-version**: Cumulus Linux version
- **evpn**: EVPN (Ethernet Virtual Private Network) operation
- **interfaces**: network interface port operation
- **mlag**: Cumulus MLAG (multi-chassis LAG/link aggregation) operation
- **mtu**: Link MTU (maximum transmission unit) consistency across paths
- **ntp**: NTP (Network Time Protocol) operation
- **roce**: RoCE (RDMA over Converged Ethernet) configurations
- **sensors**: Temperature/Fan/PSU sensor operation
- **topology**: Topology configuration
- **vlan**: VLAN (Virtual Local Area Network) operation
- **vxlan**: VXLAN (Virtual Extensible LAN) data path operation
<!-- vale on -->

The commands take the form of `netq check <network-protocol-or-service> [options]`, where the options vary according to the protocol or service.

{{< expand "Example check command" >}}

The following example shows the output for the `netq check bgp` command. Failed checks appear in the summary results or in the *failedNodes* section.

```
nvidia@switch:~$ netq check bgp
bgp check result summary:

Total nodes         : 7
Checked nodes       : 7
Failed nodes        : 7
Rotten nodes        : 0
Warning nodes       : 0
Skipped nodes       : 0

Additional summary:
Failed Sessions     : 13
Total Sessions      : 37
warn_sessions       : 0


Session Establishment Test   :  0 warnings, 13 errors
Address Families Test        :  Passed.
Router ID Test               :  Passed.
Hold Time Test               :  Passed.
Keep Alive Interval Test     :  Passed.
Ipv4 Stale Path Time Test    :  Passed.
Ipv6 Stale Path Time Test    :  Passed.
Interface MTU Test           :  Passed.


Session Establishment Test details:
Hostname          VRF             Peer Name         Peer Hostname     Reason                                        Last Changed
----------------- --------------- ----------------- ----------------- --------------------------------------------- -------------------------
border01          default         swp53             Unknown           BGP session with peer Unknown (swp53 vrf defa Tue Mar  4 15:48:45 2025
                                                                      ult) failed, reason: RA not configured(?)
border01          default         swp54             Unknown           BGP session with peer Unknown (swp54 vrf defa Tue Mar  4 15:48:45 2025
                                                                      ult) failed, reason: RA not configured(?)
border02          default         swp53             Unknown           BGP session with peer Unknown (swp53 vrf defa Tue Mar  4 15:48:56 2025
                                                                      ult) failed, reason: RA not configured(?)
border02          default         swp54             Unknown           BGP session with peer Unknown (swp54 vrf defa Tue Mar  4 15:48:56 2025
                                                                      ult) failed, reason: RA not configured(?)
leaf01            default         swp53             Unknown           BGP session with peer Unknown (swp53 vrf defa Mon Mar  3 19:44:28 2025
                                                                      ult) failed, reason: RA not configured(?)
leaf01            default         swp54             Unknown           BGP session with peer Unknown (swp54 vrf defa Mon Mar  3 19:44:29 2025
                                                                      ult) failed, reason: RA not configured(?)
leaf02            default         swp53             Unknown           BGP session with peer Unknown (swp53 vrf defa Tue Mar  4 15:48:45 2025
                                                                      ult) failed, reason: RA not configured(?)
leaf02            default         swp54             Unknown           BGP session with peer Unknown (swp54 vrf defa Tue Mar  4 15:48:45 2025
                                                                      ult) failed, reason: RA not configured(?)
leaf04            default         peerlink.4094     leaf03            BGP session with peer leaf03 (peerlink.4094 v Tue Mar  4 16:36:07 2025
                                                                      rf default) failed,
                                                                      reason: Peer not configured
leaf04            default         swp53             Unknown           BGP session with peer Unknown (swp53 vrf defa Tue Mar  4 15:48:45 2025
                                                                      ult) failed, reason: RA not configured(?)
leaf04            default         swp54             Unknown           BGP session with peer Unknown (swp54 vrf defa Tue Mar  4 15:48:45 2025
                                                                      ult) failed, reason: RA not configured(?)
spine01           default         swp3              leaf03            BGP session with peer leaf03 (swp3 vrf defaul Tue Mar  4 16:40:11 2025
                                                                      t) failed, reason: Peer not configured
spine02           default         swp3              leaf03            BGP session with peer leaf03 (swp3 vrf defaul Tue Mar  4 16:40:14 2025
                                                                      t) failed, reason: Peer not configured
```
{{< /expand >}}

{{< expand "Example check command in JSON format" >}}

```
nvidia@switch:~$ netq check bgp json
{
    "additional_summary":{
        "failed_sessions":13,
        "total_sessions":37,
        "warn_sessions":0
    },
    "failed_node_set":[
        "leaf04",
        "leaf01",
        "spine02",
        "leaf02",
        "border01",
        "spine01",
        "border02"
    ],
    "rotten_node_set":[

    ],
    "skipped_node_set":[

    ],
    "summary":{
        "checked_cnt":7,
        "checked_hostnames":"leaf02, spine01, border02, spine02, leaf01, border01, leaf04",
        "failed_node_cnt":7,
        "rotten_node_cnt":0,
        "skipped_node_cnt":0,
        "total_cnt":7,
        "warn_node_cnt":0
    },
    "tests":{
        "Address Families":{
            "enabled":true,
            "errors":[

            ],
            "passed":true,
            "suppressed_errors":0,
            "suppressed_unverified":0,
            "suppressed_warnings":0,
            "unverified":[

            ],
            "warnings":[

            ]
        },
        "Hold Time":{
            "enabled":true,
            "errors":[

            ],
            "passed":true,
            "suppressed_errors":0,
            "suppressed_unverified":0,
            "suppressed_warnings":0,
            "unverified":[

            ],
            "warnings":[

            ]
        },
        "Interface MTU":{
            "enabled":true,
            "errors":[

            ],
            "passed":true,
            "suppressed_errors":0,
            "suppressed_unverified":0,
            "suppressed_warnings":0,
            "unverified":[

            ],
            "warnings":[

            ]
        },
        "Ipv4 Stale Path Time":{
            "enabled":true,
            "errors":[

            ],
            "passed":true,
            "suppressed_errors":0,
            "suppressed_unverified":0,
            "suppressed_warnings":0,
            "unverified":[

            ],
            "warnings":[

            ]
        },
        "Ipv6 Stale Path Time":{
            "enabled":true,
            "errors":[

            ],
            "passed":true,
            "suppressed_errors":0,
            "suppressed_unverified":0,
            "suppressed_warnings":0,
            "unverified":[

            ],
            "warnings":[

            ]
        },
        "Keep Alive Interval":{
            "enabled":true,
            "errors":[

            ],
            "passed":true,
            "suppressed_errors":0,
            "suppressed_unverified":0,
            "suppressed_warnings":0,
            "unverified":[

            ],
            "warnings":[

            ]
        },
        "Router ID":{
            "enabled":true,
            "errors":[

            ],
            "passed":true,
            "suppressed_errors":0,
            "suppressed_unverified":0,
            "suppressed_warnings":0,
            "unverified":[

            ],
            "warnings":[

            ]
        },
        "Session Establishment":{
            "enabled":true,
            "errors":[
                {
                    "hostname":"border01",
                    "lastChanged":1741103325674,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"Unknown",
                    "peerName":"swp53",
                    "reason":"BGP session with peer Unknown (swp53 vrf default) failed, reason: RA not configured(?)",
                    "vrf":"default"
                },
                {
                    "hostname":"border01",
                    "lastChanged":1741103325657,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"Unknown",
                    "peerName":"swp54",
                    "reason":"BGP session with peer Unknown (swp54 vrf default) failed, reason: RA not configured(?)",
                    "vrf":"default"
                },
                {
                    "hostname":"border02",
                    "lastChanged":1741103336772,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"Unknown",
                    "peerName":"swp53",
                    "reason":"BGP session with peer Unknown (swp53 vrf default) failed, reason: RA not configured(?)",
                    "vrf":"default"
                },
                {
                    "hostname":"border02",
                    "lastChanged":1741103336451,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"Unknown",
                    "peerName":"swp54",
                    "reason":"BGP session with peer Unknown (swp54 vrf default) failed, reason: RA not configured(?)",
                    "vrf":"default"
                },
                {
                    "hostname":"leaf01",
                    "lastChanged":1741031068713,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"Unknown",
                    "peerName":"swp53",
                    "reason":"BGP session with peer Unknown (swp53 vrf default) failed, reason: RA not configured(?)",
                    "vrf":"default"
                },
                {
                    "hostname":"leaf01",
                    "lastChanged":1741031069219,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"Unknown",
                    "peerName":"swp54",
                    "reason":"BGP session with peer Unknown (swp54 vrf default) failed, reason: RA not configured(?)",
                    "vrf":"default"
                },
                {
                    "hostname":"leaf02",
                    "lastChanged":1741103325133,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"Unknown",
                    "peerName":"swp53",
                    "reason":"BGP session with peer Unknown (swp53 vrf default) failed, reason: RA not configured(?)",
                    "vrf":"default"
                },
                {
                    "hostname":"leaf02",
                    "lastChanged":1741103325225,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"Unknown",
                    "peerName":"swp54",
                    "reason":"BGP session with peer Unknown (swp54 vrf default) failed, reason: RA not configured(?)",
                    "vrf":"default"
                },
                {
                    "hostname":"leaf04",
                    "lastChanged":1741106167198,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"leaf03",
                    "peerName":"peerlink.4094",
                    "reason":"BGP session with peer leaf03 (peerlink.4094 vrf default) failed, reason: Peer not configured",
                    "vrf":"default"
                },
                {
                    "hostname":"leaf04",
                    "lastChanged":1741103325035,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"Unknown",
                    "peerName":"swp53",
                    "reason":"BGP session with peer Unknown (swp53 vrf default) failed, reason: RA not configured(?)",
                    "vrf":"default"
                },
                {
                    "hostname":"leaf04",
                    "lastChanged":1741103325076,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"Unknown",
                    "peerName":"swp54",
                    "reason":"BGP session with peer Unknown (swp54 vrf default) failed, reason: RA not configured(?)",
                    "vrf":"default"
                },
                {
                    "hostname":"spine01",
                    "lastChanged":1741106411628,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"leaf03",
                    "peerName":"swp3",
                    "reason":"BGP session with peer leaf03 (swp3 vrf default) failed, reason: Peer not configured",
                    "vrf":"default"
                },
                {
                    "hostname":"spine02",
                    "lastChanged":1741106414396,
                    "msg_id":"BGP_EVT_SESS_ERROR",
                    "peerHostname":"leaf03",
                    "peerName":"swp3",
                    "reason":"BGP session with peer leaf03 (swp3 vrf default) failed, reason: Peer not configured",
                    "vrf":"default"
                }
            ],
            "passed":false,
            "suppressed_errors":0,
            "suppressed_unverified":0,
            "suppressed_warnings":0,
            "unverified":[

            ],
            "warnings":[

            ]
        }
    },
    "validation":"bgp",
    "warn_node_set":[

    ]
}
```
{{< /expand >}}

### Monitoring Commands

The {{<link title="show" text="netq show commands">}} let you view details about the current or historical configuration and status of various protocols and services. 

The commands take the form of `netq [<hostname>] show <network-protocol-or-service> [options]`, where the options vary according to the protocol or service. You can restrict the commands from showing the information for *all* devices to showing information only for a selected device using the `hostname` option.

{{< expand "Example show command" >}}

The following example shows the standard output for the `netq show agents` command:

```
nvidia@switch:~$ netq show agents
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
border01          Fresh            yes      4.15.0-cld12u52~1744815975.8dbbbd20c Mon Mar  3 17:23:32 2025  Tue Mar  4 15:46:39 2025  Tue Mar  4 15:46:39 2025   Tue Mar  4 17:11:35 2025
border02          Fresh            yes      4.15.0-cld12u52~1744815975.8dbbbd20c Thu Jan 23 14:59:39 2025  Tue Mar  4 15:46:50 2025  Tue Mar  4 15:46:50 2025   Tue Mar  4 17:11:32 2025
fw1               Fresh            yes      4.15.0-cld12u52~1744815975.8dbbbd20c Thu Jan 23 14:59:40 2025  Tue Mar  4 15:46:44 2025  Tue Mar  4 15:46:44 2025   Tue Mar  4 17:11:31 2025
fw2               Fresh            yes      4.15.0-cld12u52~1744815975.8dbbbd20c Thu Jan 23 14:39:07 2025  Tue Mar  4 15:46:39 2025  Tue Mar  4 15:46:39 2025   Tue Mar  4 17:11:27 2025
leaf01            Fresh            yes      4.15.0-cld12u52~1744815975.8dbbbd20c Mon Mar  3 17:31:09 2025  Mon Mar  3 17:58:56 2025  Mon Mar  3 19:53:12 2025   Tue Mar  4 17:11:38 2025
leaf02            Fresh            yes      4.15.0-cld12u52~1744815975.8dbbbd20c Mon Mar  3 17:31:10 2025  Tue Mar  4 15:46:38 2025  Tue Mar  4 15:46:38 2025   Tue Mar  4 17:11:48 2025
leaf04            Fresh            yes      4.15.0-cld12u52~1744815975.8dbbbd20c Mon Mar  3 17:31:16 2025  Tue Mar  4 15:46:38 2025  Tue Mar  4 15:46:38 2025   Tue Mar  4 17:11:44 2025
spine01           Fresh            yes      4.15.0-cld12u52~1744815975.8dbbbd20c Mon Mar  3 17:31:21 2025  Tue Mar  4 15:46:38 2025  Tue Mar  4 15:46:38 2025   Tue Mar  4 17:11:45 2025
spine02           Fresh            yes      4.15.0-cld12u52~1744815975.8dbbbd20c Mon Mar  3 17:31:22 2025  Tue Mar  4 15:46:38 2025  Tue Mar  4 15:46:38 2025   Tue Mar  4 17:11:41 2025
```
{{< /expand >}}

{{< expand "Example show command with filtered output" >}}

The following example shows the filtered output for the `netq show agents` command:
```
nvidia@switch:~$ netq leaf01 show agents

Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
leaf01            Fresh            yes      4.15.0-cld12u52~1744815975.8dbbbd20c Mon Mar  3 17:31:09 2025  Mon Mar  3 17:58:56 2025  Mon Mar  3 19:53:12 2025   Tue Mar  4 17:12:33 2025
```
{{< /expand >}}
### Configuration Commands

Various commands---{{<link title="config" text="netq config">}}, {{<link title="lcm" text="netq lcm">}}, {{<link title="add" text="netq add">}}, and {{<link title="del" text="netq del">}}---allow you to manage NetQ Agent and CLI server configurations, configure lifecycle management, set up container monitoring, and manage notifications.

#### NetQ Agent Configuration

The agent commands configure individual NetQ Agents. 

The agent configuration commands can add and remove agents from switches and hosts, start and stop agent operations, debug the agent, specify default commands, and enable or disable a variety of monitoring features (including sensors, FRR (FRRouting), CPU usage limit, and What Just Happened).

{{<notice note>}}
Commands apply to one agent at a time. Run them from the switch or host where the NetQ Agent resides. You must run the <code>netq config</code> commands with sudo privileges.
{{</notice>}}

The agent configuration commands include:

```
netq config (add|del|show) agent
netq config (start|stop|status|restart) agent
```

The following example shows how to view the NetQ Agent configuration:

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
```

{{<notice note>}}
After making configuration changes to your agents, you must restart the agent for the changes to take effect. Use the <code>netq config restart agent</code> command.
{{</notice>}}

Refer to {{<link url="Manage-NetQ-Agents">}} and {{<link url="Install-NetQ-Agents">}} for additional examples.

#### CLI Configuration

The `netq config cli` configures and manages the CLI component. You can add or remove the CLI (essentially enabling/disabling the service), start and restart it, and view the configuration of the service.

{{<notice note>}}
Commands apply to one device at a time, and you run them from the switch or host where you run the CLI.
{{</notice>}}

The CLI configuration commands include:

```
netq config add cli server
netq config del cli server
netq config show cli premises [json]
netq config show (cli|all) [json]
netq config (status|restart) cli
netq config select cli premise
```

The following example shows how to restart the CLI instance:

```
nvidia@switch~:$ netq config restart cli
```

The following example shows how to enable the CLI on a NetQ on-premises server or virtual machine:

```
nvidia@switch~:$ netq config add cli server 10.1.3.101
```
#### NetQ System Configuration Commands

Use the following commands to manage the NetQ system itself:

- **bootstrap**: Loads the installation program onto the network switches and hosts in either a single server or server cluster arrangement.
- **decommission**: Decommissions a switch or host.
- **install**: Installs NetQ in standalone or cluster deployments; also used to install patch software.
- **upgrade bundle**: Upgrades NetQ on NetQ on-premises VMs.

The following example shows how to decommission a switch named leaf01:

    nvidia@netq-server:~$ netq decommission leaf01

For information and examples on installing and upgrading the NetQ system, see {{<link url="Install-NetQ">}} and {{<link url="Upgrade-NetQ">}}.

#### Event Notification Commands

The notification configuration commands can add, remove, and show notification via third-party integrations. These commands create the channels, filters, and rules that display event messages. Refer to {{<link title="Configure System Event Notifications">}} for step-by-step instructions and examples.

<!-- vale off -->
#### Threshold-based Event Notification Commands
<!-- vale on -->

NetQ supports {{<link title="Configure and Monitor Threshold-Crossing Events" text="TCA events">}}, a set of events that <!--vale off -->are triggered<!-- vale on --> by crossing a user-defined threshold. Configure and manage TCA events using the following commands:

```
netq add tca
netq del tca tca_id <text-tca-id-anchor>
netq show tca
```

#### Lifecycle Management Commands

The {{<link title="Lifecycle Management" text="lifecycle management">}} commands help you efficiently manage the deployment of NVIDIA product software onto your network devices.

LCM commands allow you to:

- Manage network OS and NetQ images in a local repository
- Configure switch access credentials for installations and upgrades
- Manage switch inventory and roles
- Install or upgrade NetQ Agents and CLI on switches
- Upgrade the network OS on switches with NetQ Agents
- View a result history of upgrade attempts
- Add or delete NetQ configuration profiles

The following example shows the NetQ configuration profiles:

```
nvidia@switch:~$ netq lcm show netq-config
ID                        Name            Default Profile                VRF             WJH       CPU Limit Log Level Last Changed              In-Band Interface
------------------------- --------------- ------------------------------ --------------- --------- --------- --------- ------------------------- ----------------------------------
config_profile_3289efda36 NetQ default co Yes                            mgmt            Disable   Disable   info      Mon Mar  3 19:22:35 2025  N/A
db4065d56f91ebbd34a523b45 nfig
944fbfd10c5d75f9134d42023
eb2b
```

The following example shows how to add a Cumulus Linux installation image to the NetQ repository on the switch:

    netq lcm add cl-image /path/to/download/cumulus-linux-5.12.0-mlnx-amd64.bin

### Trace Commands

The {{<link title="trace" text="netq trace commands">}} let you view the available paths between two nodes on the network. You can perform a layer 2 or layer 3 trace, and view the output in one of three formats: JSON, pretty, and detail. JSON output provides the output in a JSON file format for ease of importing to other applications or software. Pretty output lines up the paths in a pseudo-graphical manner to help visualize multiple paths. Detail output is useful for traces with higher hop counts where the pretty output wraps lines, making it harder to interpret the results. The detail output displays a table with a row for each path.

The trace command syntax is:

```
netq trace (<mac> vlan <1-4096>) from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug]
netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug]
netq trace (<mac> vlan <1-4096>) from <mac-src> [around <text-time>] [json|detail|pretty] [debug]
```

{{< expand "Example trace command with pretty output" >}}

The following example shows how to run a trace based on the destination IP address, in *pretty* output with a small number of resulting paths:

```
nvidia@switch:~$ netq trace 10.0.0.11 from 10.0.0.14 pretty
Number of Paths: 6
    Inconsistent PMTU among paths
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9000
    leaf04 swp52 -- swp4 spine02 swp2 -- swp52 leaf02 peerlink.4094 -- peerlink.4094 leaf01 lo
                                                    peerlink.4094 -- peerlink.4094 leaf01 lo
    leaf04 swp51 -- swp4 spine01 swp2 -- swp51 leaf02 peerlink.4094 -- peerlink.4094 leaf01 lo
                                                    peerlink.4094 -- peerlink.4094 leaf01 lo
    leaf04 swp52 -- swp4 spine02 swp1 -- swp52 leaf01 lo
    leaf04 swp51 -- swp4 spine01 swp1 -- swp51 leaf01 lo
```
{{< /expand >}}

{{< expand "Example trace command with detail output" >}}

This example shows how to run a trace based on the destination IP address, in *detail* output with a small number of resulting paths:

```
nvidia@switch:~$ netq trace 10.0.0.11 from 10.0.0.14 detail
Number of Paths: 6
    Inconsistent PMTU among paths
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9000
Id  Hop Hostname        InPort          InVlan InTunnel              InRtrIf         InVRF           OutRtrIf        OutVRF          OutTunnel             OutPort         OutVlan
--- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
1   1   leaf04                                                                                       swp52           default                               swp52
    2   spine02         swp4                                         swp4            default         swp2            default                               swp2
    3   leaf02          swp52                                        swp52           default         peerlink.4094   default                               peerlink.4094
    4   leaf01          peerlink.4094                                peerlink.4094   default                                                               lo
--- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
2   1   leaf04                                                                                       swp52           default                               swp52
    2   spine02         swp4                                         swp4            default         swp2            default                               swp2
    3   leaf02          swp52                                        swp52           default         peerlink.4094   default                               peerlink.4094
    4   leaf01          peerlink.4094                                peerlink.4094   default                                                               lo
--- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
3   1   leaf04                                                                                       swp51           default                               swp51
    2   spine01         swp4                                         swp4            default         swp2            default                               swp2
    3   leaf02          swp51                                        swp51           default         peerlink.4094   default                               peerlink.4094
    4   leaf01          peerlink.4094                                peerlink.4094   default                                                               lo
--- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
4   1   leaf04                                                                                       swp51           default                               swp51
    2   spine01         swp4                                         swp4            default         swp2            default                               swp2
    3   leaf02          swp51                                        swp51           default         peerlink.4094   default                               peerlink.4094
    4   leaf01          peerlink.4094                                peerlink.4094   default                                                               lo
--- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
5   1   leaf04                                                                                       swp52           default                               swp52
    2   spine02         swp4                                         swp4            default         swp1            default                               swp1
    3   leaf01          swp52                                        swp52           default                                                               lo
--- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
6   1   leaf04                                                                                       swp51           default                               swp51
    2   spine01         swp4                                         swp4            default         swp1            default                               swp1
    3   leaf01          swp51                                        swp51           default                                                               lo
--- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
```
{{< /expand >}}

{{< expand "Example trace command on destination MAC address" >}}

This example shows how to run a trace based on the destination MAC address, in *pretty* output:

```
nvidia@switch:~$ netq trace A0:00:00:00:00:11 vlan 1001 from Server03 pretty
Number of Paths: 6
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9152
    
    Server03 bond1.1001 -- swp7 <vlan1001> Leaf02 vni: 34 swp5 -- swp4 Spine03 swp7 -- swp5 vni: 34 Leaf04 swp6 -- swp1.1001 Server03 <swp1.1001>
                                                        swp4 -- swp4 Spine02 swp7 -- swp4 vni: 34 Leaf04 swp6 -- swp1.1001 Server03 <swp1.1001>
                                                        swp3 -- swp4 Spine01 swp7 -- swp3 vni: 34 Leaf04 swp6 -- swp1.1001 Server03 <swp1.1001>
            bond1.1001 -- swp7 <vlan1001> Leaf01 vni: 34 swp5 -- swp3 Spine03 swp7 -- swp5 vni: 34 Leaf04 swp6 -- swp1.1001 Server03 <swp1.1001>
                                                        swp4 -- swp3 Spine02 swp7 -- swp4 vni: 34 Leaf04 swp6 -- swp1.1001 Server03 <swp1.1001>
                                                        swp3 -- swp3 Spine01 swp7 -- swp3 vni: 34 Leaf04 swp6 -- swp1.1001 Server03 <swp1.1001>
```
{{< /expand >}}

## Related Information

- {{<link title="NetQ CLI Reference">}}