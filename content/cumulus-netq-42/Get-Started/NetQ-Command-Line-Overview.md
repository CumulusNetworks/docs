---
title: NetQ Command Line Overview
author: NVIDIA
weight: 160
toc: 4
---

The NetQ CLI provides access to all network state and event information collected by the NetQ Agents. It behaves the same way most CLIs behave, with groups of commands used to display related information, the ability to use TAB completion when entering commands, and to get help for given commands and options. There are four categories of commands: check, show, config, and trace.

{{<notice note>}}

The NetQ command line interface only runs on switches and server hosts implemented with Intel x86 or ARM-based architectures.

{{</notice>}}

## CLI Access

When you install or upgrade NetQ, you can also install and enable the CLI on your NetQ server or appliance and hosts. Refer to the {{<link url="Install-NetQ">}} topic for details.

To access the CLI from a switch or server:

<!-- vale off -->
1. Log in to the device. This example uses the default username of *cumulus* and a hostname of *switch*.

    ```
    <computer>:~<username>$ ssh cumulus@switch
    ```

2. Enter your password to reach the command prompt. The default password is *CumulusLinux\!* For example:

    ```
    Enter passphrase for key '/Users/<username>/.ssh/id_rsa': <enter CumulusLinux! here>
    Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-112-generic x86_64)
        * Documentation:  https://help.ubuntu.com
        * Management:     https://landscape.canonical.com
        * Support:        https://ubuntu.com/advantage
    Last login: Tue Sep 15 09:28:12 2019 from 10.0.0.14
    cumulus@switch:~$
    ```

3.  Run commands. For example:

    ```
    cumulus@switch:~$ netq show agents
    cumulus@switch:~$ netq check bgp
    ```
<!-- vale on -->

## Command Line Basics

This section describes the core structure and behavior of the NetQ CLI. It includes the following:

- {{<link url="#command-line-structure" text="Command Line Structure">}}
- {{<link url="#command-syntax" text="Command Syntax">}}
- {{<link url="#command-output" text="Command Output">}}
- {{<link url="#command-prompts" text="Command Prompts">}}
- {{<link url="#command-completion" text="Command Completion">}}
- {{<link url="#command-help" text="Command Help">}}
- {{<link url="#command-history" text="Command History">}}

### Command Line Structure

The NetQ command line has a flat structure as opposed to a modal structure. Thus, you can run all commands from the standard command prompt instead of only in a specific mode, at the same level.

### Command Syntax

NetQ CLI commands all begin with `netq`. NetQ commands fall into one of four syntax categories: validation (check), monitoring (show), configuration, and trace.

```
netq check <network-protocol-or-service> [options]
netq show <network-protocol-or-service> [options]
netq config <action> <object> [options]
netq trace <destination> from <source> [options]
```

| Symbols  | Meaning  |
| -------- | -------- |
| Parentheses ( ) | Grouping of required parameters. Choose one. |
| Square brackets \[ \] | Single or group of optional parameters. If more than one object or keyword is available, choose one. |
| Angle brackets \< \> | Required variable. Value for a keyword or option; enter according to your deployment nomenclature. |
| Pipe \| | Separates object and keyword options, also separates value options; enter one object or keyword and zero or one value. |

For example, in the `netq check` command:

- \[\<hostname\>\] is an optional parameter with a variable value named *hostname*
<!-- vale off -->
- \<network-protocol-or-service\> represents a number of possible key words, such as *agents*, *bgp*, *evpn,* and so forth

- \<options\> represents a number of possible conditions for the given object, such as *around*, *vrf,* or *json*
<!-- vale on -->
Thus some valid commands are:

- `netq leaf02 check agents json`
- `netq show bgp`
- `netq config restart cli`
- `netq trace 10.0.0.5 from 10.0.0.35`

### Command Output

The command output presents results in color for many commands. Results with errors appear in <span style="color: #ff0000;">red</span>, and warnings appear in <span style="color: #ffcc00;">yellow</span>. Results without errors or warnings appear in either black or <span style="color: #00ff00;">green</span>. VTEPs appear in <span style="color: #0000ff;">blue</span>. A node in the *pretty* output appears in **bold**, and angle brackets (\< \>) wrap around a router interface. To view the output with only black text, run the `netq config del color` command. You can view output with colors again by running `netq config add color`.

All check and show commands have a default timeframe of now to one hour ago, unless you specify an approximate time using the `around` keyword or a range using the `between` keyword. For example, running `netq check bgp` shows the status of BGP over the last hour. Running `netq show bgp around 3h` shows the status of BGP three hours ago.

### Command Prompts

NetQ code examples use the following prompts:

<!-- vale off -->
- `cumulus@switch:~$` Indicates the user *cumulus* is logged in to a switch to run the example command
- `cumulus@host:~$` Indicates the user *cumulus* is logged in to a host to run the example command
- `cumulus@netq-appliance:~$` Indicates the user *cumulus* is logged in to either the NetQ Appliance or NetQ Cloud Appliance to run the command
- `cumulus@hostname:~$` Indicates the user *cumulus* is logged in to a switch, host or appliance to run the example command
<!-- vale on -->

To use the NetQ CLI, the switches must be running the Cumulus Linux or SONiC operating system (OS), NetQ Platform or NetQ Collector software, the NetQ Agent, and the NetQ CLI. The hosts must be running CentOS, RHEL, or Ubuntu OS, the NetQ Agent, and the NetQ CLI. Refer to the {{<link url="Install-NetQ">}} topic for details.

### Command Completion

As you enter commands, you can get help with the valid keywords or options using the **Tab** key. For example, using Tab completion with `netq check` displays the possible objects for the command, and returns you to the command prompt to complete the command.

```
cumulus@switch:~$ netq check <<press Tab>>
    agents      :  Netq agent
    bgp         :  BGP info
    cl-version  :  Cumulus Linux version
    clag        :  Cumulus Multi-chassis LAG
    evpn        :  EVPN
    interfaces  :  network interface port
    mlag        :  Multi-chassis LAG (alias of clag)
    mtu         :  Link MTU
    ntp         :  NTP
    ospf        :  OSPF info
    sensors     :  Temperature/Fan/PSU sensors
    vlan        :  VLAN
    vxlan       :  VXLAN data path
cumulus@switch:~$ netq check
```

### Command Help

As you enter commands, you can get help with command syntax by entering `help` at various points within a command entry. For example, to find out what options are available for a BGP check, enter `help` after entering some of the `netq check` command. In this example, you can see that there are no additional required parameters and you can use three optional parameters &mdash; `hostnames`, `vrf` and `around` &mdash; with a BGP check.

```
cumulus@switch:~$ netq check bgp help
Commands:
    netq check bgp [label <text-label-name> | hostnames <text-list-hostnames>] [vrf <vrf>] [check_filter_id <text-check-filter-id>] [include <bgp-number-range-list> | exclude <bgp-number-range-list>] [around <text-time>] [streaming] [json | summary]
   netq show unit-tests bgp [check_filter_id <text-check-filter-id>] [json]
```

To see an exhaustive list of commands, run:

```
cumulus@switch:~$ netq help list
```

To get usage information for NetQ, run:

```
cumulus@switch:~$ netq help verbose
```

### Command History

The CLI stores commands issued within a session, which enables you to review and rerun commands that you already ran. At the command prompt, press the **Up Arrow** and **Down Arrow** keys to move back and forth through the list of commands previously entered. When you have found a given command, you can run the command by pressing **Enter**, just as you would if you had entered it manually. Optionally you can modify the command before you run it.

## Command Categories

While the CLI has a flat structure, the commands can be conceptually grouped into these functional categories:

- {{<link url="#validation-commands" text="Validation Commands">}}
- {{<link url="#monitoring-commands" text="Monitoring Commands">}}
- {{<link url="#configuration-commands" text="Configuration Commands">}}
- {{<link url="#trace-commands" text="Trace Commands">}}

### Validation Commands

The `netq` `check` commands enable the network administrator to validate the current or historical state of the network by looking for errors and misconfigurations in the network. The commands run fabric-wide validations against various configured protocols and services to determine how well the network is operating. You can perform validation checks for the following:

<!-- vale off -->
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
- **ospf**: OSPF (Open Shortest Path First) operation
- **sensors**: Temperature/Fan/PSU sensor operation
- **vlan**: VLAN (Virtual Local Area Network) operation
- **vxlan**: VXLAN (Virtual Extensible LAN) data path operation
<!-- vale on -->

The commands take the form of `netq check <network-protocol-or-service> [options]`, where the options vary according to the protocol or service.

This example shows the output for the `netq check bgp` command, followed by the same command using the `json` option. If there were any failures, they would appear below the summary results or in the *failedNodes* section, respectively.

```
cumulus@switch:~$ netq check bgp
bgp check result summary:

Checked nodes       : 8
Total nodes         : 8
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Total Sessions      : 30
Failed Sessions     : 0

Session Establishment Test   : passed
Address Families Test        : passed
Router ID Test               : passed

```

```
cumulus@switch:~$ netq check bgp json
{
    "tests":{
        "Session Establishment":{
            "suppressed_warnings":0,
            "errors":[

            ],
            "suppressed_errors":0,
            "passed":true,
            "warnings":[

            ],
            "duration":0.0000853539,
            "enabled":true,
            "suppressed_unverified":0,
            "unverified":[

            ]
        },
        "Address Families":{
            "suppressed_warnings":0,
            "errors":[

            ],
            "suppressed_errors":0,
            "passed":true,
            "warnings":[

            ],
            "duration":0.0002634525,
            "enabled":true,
            "suppressed_unverified":0,
            "unverified":[

            ]
        },
        "Router ID":{
            "suppressed_warnings":0,
            "errors":[

            ],
            "suppressed_errors":0,
            "passed":true,
            "warnings":[

            ],
            "duration":0.0001821518,
            "enabled":true,
            "suppressed_unverified":0,
            "unverified":[

            ]
        }
    },
    "failed_node_set":[

    ],
    "summary":{
        "checked_cnt":8,
        "total_cnt":8,
        "rotten_node_cnt":0,
        "failed_node_cnt":0,
        "warn_node_cnt":0
    },
    "rotten_node_set":[

    ],
    "warn_node_set":[

    ],
    "additional_summary":{
        "total_sessions":30,
        "failed_sessions":0
    },
    "validation":"bgp"
}
```

### Monitoring Commands

The `netq show` commands enable the network administrator to view details about the current or historical configuration and status of the various protocols or services. You can view the configuration and status for the following:

<!-- vale off -->
- **address-history**: Address history info for a IP address / prefix
- **agents**: NetQ Agents status on switches and hosts
- **bgp**: BGP status across the network fabric
- **cl-btrfs-info**: BTRFS file system data for monitored Cumulus Linux switches
- **cl-manifest**: Information about the versions of Cumulus Linux available on monitored switches
- **cl-pkg-info**: Information about software packages installed on monitored switches
- **cl-resource**: ACL and forwarding information
- **cl-ssd-util**: SSD utilization information
- **clag**: CLAG/MLAG status
- **dom**: Digital Optical Monitoring
- **ethtool-stats**: Interface statistics
- **events**: Display changes over time
- **events-config**: Events configured for suppression
- **evpn**: EVPN status
- **interface-stats**: Interface statistics
- **interface-utilization**: Interface statistics plus utilization
- **interfaces**: network interface port status
- **inventory**: hardware component information
- **ip**: IPv4 status
- **ipv6**: IPv6 status
- **job-status**: status of upgrade jobs running on the appliance or VM
- **kubernetes**: Kubernetes cluster, daemon, pod, node, service and replication status
- **lldp**: LLDP status
- **mac-commentary**: MAC commentary info for a MAC address
- **mac-history**: Historical information for a MAC address
- **macs**: MAC table or address information
- **mlag**: MLAG status (an alias for CLAG)
- **neighbor-history**:  Neighbor history info for an IP address
- **notification**: Send notifications to Slack or PagerDuty
- **ntp**: NTP status
- **opta-health**: Display health of apps on the OPTA
- **opta-platform**: NetQ Appliance version information and uptime
- **ospf**: OSPF status
- **recommended-pkg-version**: Current host information to be considered
- **resource-util**: Display usage of memory, CPU and disk resources
- **roce-config**: Display RoCE configuration
- **roce-counters**: Displays RDMA over Converged Ethernet counters for a given switch
- **sensors**: Temperature/Fan/PSU sensor status
- **services**: System services status
- **tca**: Threshold crossing alerts
- **trace**: Control plane trace path across fabric
- **unit-tests**: Show list of unit tests for `netq check`
- **validation**: Schedule a validation check
- **vlan**: VLAN status
- **vxlan**: VXLAN data path status
- **wjh-drop**: dropped packet data from NVIDIA&reg; Mellanox&reg; What Just Happened&reg;
<!-- vale on -->

The commands take the form of `netq [<hostname>] show <network-protocol-or-service> [options]`, where the options vary according to the protocol or service. You can restrict the commands from showing the information for *all* devices to showing information only for a selected device using the `hostname` option.

The following examples show the standard and filtered output for the  `netq show agents` command.

```
cumulus@switch:~$ netq show agents
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

```
cumulus@switch:~$ netq leaf01 show agents
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
leaf01            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 16:49:04 2020  Tue Sep 29 21:24:49 2020  Tue Sep 29 21:24:49 2020   Thu Oct  1 16:26:33 2020
```

### Configuration Commands

Various commands, including `netq config`, `netq notification`, and `netq install` enable the network administrator to manage NetQ Agent and CLI server configuration, configure lifecycle management, set up container monitoring, and manage notifications.

#### NetQ Agent Configuration

The agent commands enable the network administrator to configure individual NetQ Agents. Refer to {{<link url="NetQ-Components/#netq-agents">}} for a description of NetQ Agents, to {{<link url="Manage-NetQ-Agents">}}, or to {{<link url="Install-NetQ-Agents">}} for more detailed usage examples.

The agent configuration commands enable you to add and remove agents from switches and hosts, start and stop agent operations, debug the agent, specify default commands, and enable or disable a variety of monitoring features (including Kubernetes, sensors, FRR (FRRouting), CPU usage limit, and What Just Happened).

{{<notice note>}}
Commands apply to one agent at a time; you run them from the switch or host where the NetQ Agent resides.
{{</notice>}}

The agent configuration commands include:

```
netq config (add|del|show) agent
netq config (start|stop|status|restart) agent
```

This example shows how to configure the agent to send sensor data:

```
cumulus@switch~:$ netq config add agent sensors
```

This example shows how to start monitoring with Kubernetes:

```
cumulus@switch:~$ netq config add agent kubernetes-monitor poll-period 15
```

This example shows how to view the NetQ Agent configuration:

```
cumulus@switch:~$ netq config show agent
netq-agent             value      default
---------------------  ---------  ---------
enable-opta-discovery  True       True
exhibitport
agenturl
server                 127.0.0.1  127.0.0.1
exhibiturl
vrf                    default    default
agentport              8981       8981
port                   31980      31980
```

{{<notice note>}}
After making configuration changes to your agents, you must restart the agent for the changes to take effect. Use the <code>netq config restart agent</code> command.
{{</notice>}}

#### CLI Configuration

The `netq config cli` commands enable the network administrator to configure and manage the CLI component. These commands enable you to add or remove CLI (essentially enabling/disabling the service), start and restart it, and view the configuration of the service.

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

This example shows how to restart the CLI instance:

```
cumulus@switch~:$ netq config restart cli
```

This example shows how to enable the CLI on a NetQ On-premises appliance or virtual machine (VM):

```
cumulus@switch~:$ netq config add cli server 10.1.3.101
```

This example shows how to enable the CLI on a NetQ Cloud Appliance or VM for the Chicago premises and the default port:

```
netq config add cli server api.netq.cumulusnetworks.com access-key <user-access-key> secret-key <user-secret-key> premises chicago port 443
```

#### NetQ System Configuration Commands

You use the following commands to manage the NetQ system itself:

- **bootstrap**: Loads the installation program onto the network switches and hosts in either a single server or server cluster arrangement.
- **decommission**: Decommissions a switch or host.
- **install**: Installs NetQ in standalone or cluster deployments; also used to install patch software.
- **upgrade bundle**: Upgrades NetQ on NetQ On-premises Appliances or VMs.

This example shows how to bootstrap a single server or master server in a server cluster:

```
cumulus@switch:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-4.1.0.tgz
```

This example shows how to decommission a switch named leaf01:

    cumulus@netq-appliance:~$ netq decommission leaf01

For information and examples on installing and upgrading the NetQ system, see {{<link url="Install-NetQ">}} and {{<link url="Upgrade-NetQ">}}.

#### Event Notification Commands

The notification configuration commands enable you to add, remove and show notification application integrations. These commands create the channels, filters, and rules needed to control event messaging. The commands include:

    netq (add|del|show) notification channel
    netq (add|del|show) notification rule
    netq (add|del|show) notification filter
    netq (add|del|show) notification proxy

An integration includes at least one channel (PagerDuty, Slack, or syslog), at least one filter (defined by rules you create), and at least one rule.

This example shows how to configure a PagerDuty channel:

```
cumulus@switch:~$ netq add notification channel pagerduty pd-netq-events integration-key c6d666e210a8425298ef7abde0d1998
Successfully added/updated channel pd-netq-events
```

Refer to {{<link title="Configure System Event Notifications">}} for details about using these commands and additional examples.

<!-- vale off -->
#### Threshold-based Event Notification Commands
<!-- vale on -->

NetQ supports {{<link title="Configure Threshold-Based Event Notifications" text="TCA events">}}, a set of events that <!--vale off -->are triggered<!-- vale on --> by crossing a user-defined threshold. You configure and manage TCA events using the following commands:

```
netq add tca [event_id <text-event-id-anchor>] [tca_id <text-tca-id-anchor>] [scope <text-scope-anchor>] [severity info | severity error] [is_active true | is_active false] [suppress_until <text-suppress-ts>] [threshold_type user_set | threshold_type vendor_set] [ threshold <text-threshold-value> ] [channel <text-channel-name-anchor> | channel drop <text-drop-channel-name>]
netq del tca tca_id <text-tca-id-anchor>
netq show tca [tca_id <text-tca-id-anchor>] [json]
```

#### Lifecycle Management Commands

The `netq lcm` ({{<link title="Manage Switches through Their Lifecycle" text="lifecycle management">}}) commands enable you to manage the deployment of NVIDIA product software onto your network devices (servers, appliances, and switches) in the most efficient way and with the most information about the process as possible. The LCM commands provide for:

- Managing network OS and NetQ images in a local repository
- Configuring switch access credentials for installations and upgrades
- Managing switch inventory and roles
- Upgrade NetQ (Agents and CLI) on switches with NetQ Agents
- Install or upgrade NetQ Agents and CLI on switches with or without NetQ Agents all in a single job
- Upgrade the network OS on switches with NetQ Agents
- View a result history of upgrade attempts

This example shows the NetQ configuration profiles:

```
cumulus@switch:~$ netq lcm show netq-config
ID                        Name            Default Profile                VRF             WJH       CPU Limit Log Level Last Changed
------------------------- --------------- ------------------------------ --------------- --------- --------- --------- -------------------------
config_profile_3289efda36 NetQ default co Yes                            mgmt            Disable   Disable   info      Tue Apr 27 22:42:05 2021
db4065d56f91ebbd34a523b45 nfig
944fbfd10c5d75f9134d42023
eb2b
```

This example shows how to add a Cumulus Linux installation image to the NetQ repository on the switch:

    netq lcm add cl-image /path/to/download/cumulus-linux-4.3.0-mlnx-amd64.bin

### Trace Commands

The `trace` commands enable the network administrator to view the available paths between two nodes on the network currently and at a time in the past. You can perform a layer 2 or layer 3 trace, and view the output in one of three formats (*json*, *pretty*, and *detail*). JSON output provides the output in a JSON file format for ease of importing to other applications or software. Pretty output lines up the paths in a pseudo-graphical manner to help visualize multiple paths. Detail output is useful for traces with higher hop counts where the pretty output wraps lines, making it harder to interpret the results. The detail output displays a table with a row for each path.

The trace command syntax is:

```
netq trace <mac> [vlan <1-4096>] from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug]
netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug]
```

This example shows how to run a trace based on the destination IP address, in *pretty* output with a small number of resulting paths:

```
cumulus@switch:~$ netq trace 10.0.0.11 from 10.0.0.14 pretty
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

This example shows how to run a trace based on the destination IP address, in *detail* output with a small number of resulting paths:

```
cumulus@switch:~$ netq trace 10.0.0.11 from 10.0.0.14 detail
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

This example shows how to run a trace based on the destination MAC address, in *pretty* output:

```
cumulus@switch:~$ netq trace A0:00:00:00:00:11 vlan 1001 from Server03 pretty
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
