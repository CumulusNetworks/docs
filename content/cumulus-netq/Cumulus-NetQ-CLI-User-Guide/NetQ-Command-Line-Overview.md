---
title: NetQ Command Line Overview
author: Cumulus Networks
weight: 31
aliases:
 - /display/NETQ22/NetQ-Command-Line-Overview
 - /pages/viewpage.action?pageId=12321059
pageID: 12321059
product: Cumulus NetQ
version: 2.2.0
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
The NetQ CLI provides access to all of the network state and event
information collected by the NetQ Agents. It behaves the same way most
CLIs behave, with groups of commands used to display related
information, the ability to use TAB completion when entering commands,
and to get help for given commands and options. The commands are grouped
into four categories: check and show, agent and notifier, trace, and
resolve.

{{%notice note%}}

The NetQ command line interface only runs on switches and server hosts
implemented with Intel x86 or ARM-based architectures.
<span style="color: #353744;"> If you are unsure what architecture your
switch or server employs, check the Cumulus [Hardware Compatibility
List](https://cumulusnetworks.com/products/hardware-compatibility-list/)
and verify the value in the **Platforms** tab \> **CPU** column. </span>

{{%/notice%}}

## <span>CLI Access</span>

When NetQ is installed, the CLI is also installed and enabled (refer to
the [Install
NetQ](/version/cumulus-netq-22/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
topic). Simply log in to any network node to access the command line.

<span style="color: #353744;"> To access the CLI from a switch or
server: </span>

1.  <span style="color: #353744;"> Log in to the device. This example
    uses the default username of c*umulus* and a hostname of *switch*.  
    </span>
    
        <computer>:~<username>$ ssh cumulus@switch

2.  <span style="color: #353744;"> <span style="color: #353744;"> Enter
    your password to reach the command prompt. The default password is
    *CumulusLinux\!* For example: </span> </span>
    
        Enter passphrase for key '/Users/<username>/.ssh/id_rsa': <enter CumulusLinux! here>
        Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-112-generic x86_64)
         * Documentation:  https://help.ubuntu.com
         * Management:     https://landscape.canonical.com
         * Support:        https://ubuntu.com/advantage
        Last login: Tue Feb 11 09:28:12 2019 from 10.0.0.14
        cumulus@switch:~$ 

3.  <span style="color: #353744;"> Run commands. For example:  
    </span>
    
        cumulus@switch:~$ netq show agents
        cumulus@switch:~$ netq check bgp

<span style="color: #353744;"> Command Line Basics </span>

<span style="color: #353744;"> This section describes the core structure
and behavior of the NetQ CLI. It includes the following: </span>

  - <span style="color: #353744;"> [Command Line
    Structure](#src-12321059_NetQCommandLineOverview-ComStruct) </span>

  - <span style="color: #353744;"> [Command
    Syntax](#src-12321059_NetQCommandLineOverview-ComSyntax) </span>

  - [Command Output](#src-12321059_NetQCommandLineOverview-ComOut)

  - [Command Prompts](#src-12321059_NetQCommandLineOverview-ComPrompt)
    <span style="color: #353744;"> </span>

  - <span style="color: #353744;"> [Command
    Completion](#src-12321059_NetQCommandLineOverview-ComComp) </span>

  - <span style="color: #353744;"> [Command
    Help](#src-12321059_NetQCommandLineOverview-ComHelp) </span>

  - [Command History](#src-12321059_NetQCommandLineOverview-ComHist)

### <span>Command Line Structure</span>

<span style="color: #353744;"> The Cumulus NetQ command line has a flat
structure as opposed to a modal structure. This means that all commands
can be run from the primary prompt instead of only in a specific mode.
</span> <span style="color: #353744;"> For example, some command lines
require the administrator to switch between a configuration mode and an
operation mode. Configuration commands can only be run in the
configuration mode and operational commands can only be run in operation
mode. This structure requires the administrator to switch between modes
to run commands which can be tedious and time consuming. Cumulus NetQ
command line enables the administrator to run all of its commands at the
same level. </span>

### <span>Command Syntax</span>

<span style="color: #353744;"> NetQ CLI commands all begin with `netq`.
</span> Cumulus NetQ commands fall into one of four syntax categories:
validation (check), monitoring (show), configuration, and trace:

    netq check <network-protocol-or-service> [options]
    netq show <network-protocol-or-service> [options]
    netq config <action> <object> [options]
    netq trace <destination> from <source> [options]

| Symbols               | Meaning                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Parentheses ( )       | Grouping of required parameters. Choose one.                                                                           |
| Square brackets \[ \] | Single or group of optional parameters. If more than one object or keyword is available, choose one.                   |
| Angle brackets \< \>  | Required variable. Value for a keyword or option; enter according to your deployment nomenclature.                     |
| Pipe |                | Separates object and keyword options, also separates value options; enter one object or keyword and zero or one value. |

<span style="color: #353744;"> For example, in the </span> `netq check`
<span style="color: #353744;"> command: </span>

  - <span style="color: #353744;"> \[\<hostname\>\] is an optional
    parameter with a variable value named *hostname* </span>

  - \<network-protocol-or-service\> represents a number of possible key
    words, such as *agents, bgp, evpn,* and so forth

  - \<options\> represents a number of possible conditions for the given
    object, such as *around, vrf,* or *json*

Thus some valid commands are:

  - `netq leaf02 check agents json`

  - `netq show bgp`

  - `netq config restart cli`

  - `netq trace 10.0.0.5 from 10.0.0.35`

### <span>Command Output</span>

<span style="color: #353744;"> The command output presents results in
color for many commands. </span> Results with errors are shown in
<span style="color: #ff0000;"> red </span> , and warnings are shown in
<span style="color: #ffcc00;"> yellow </span> . Results without errors
or warnings are shown in either black or <span style="color: #00ff00;">
green </span> . VTEPs are shown in <span style="color: #0000ff;"> blue
</span> . A node in the *pretty* output is shown in **bold**, and a
router interface is wrapped in angle brackets (\< \>). To view the
output with only black text, run the `netq config del color` command.
You can view output with colors again by running `netq config add
color`.

<span style="color: #353744;"> All check and show commands are run with
a default timeframe of now to one hour ago, unless you specify an
approximate time using the </span> `around`
<span style="color: #353744;"> keyword </span>
<span style="color: #353744;"> . For example, running `netq check bgp`
shows the status of BGP over the last hour. Running `netq show bgp
around 3h` shows the status of BGP three hours ago. </span>

### <span>Command Prompts</span>

<span style="color: #353744;"> NetQ code examples use the following
prompts: </span>

  - ` cumulus@switch:~$  `Indicates the user *cumulus* is logged in to a
    switch to run the example command

  - ` cumulus@host:~$  `Indicates the user *cumulus* is logged in to a
    host to run the example command

The switches must be running the Cumulus Linux operating system (OS),
NetQ Platform software, and the NetQ Agent. The hosts must be running
CentOS, RHEL, or Ubuntu OS and the NetQ Agent. Refer to the [Install
NetQ](/version/cumulus-netq-22/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
topic for details.

### <span>Command Completion</span>

As you enter commands, you can get help with the valid keywords or
options using <span style="color: #353744;"> the **Tab** key. For
example, using Tab completion with `netq check` displays the possible
objects for the command, and returns you to the command prompt to
complete the command. </span>

    cumulus@switch:~$ netq check <<press Tab>>
        agents      :  Netq agent
        bgp         :  BGP info
        clag        :  Cumulus Multi-chassis LAG
        evpn        :  EVPN
        interfaces  :  network interface port
        license     :  License information
        lnv         :  Lightweight Network Virtualization info
        mtu         :  Link MTU
        ntp         :  NTP
        ospf        :  OSPF info
        sensors     :  Temperature/Fan/PSU sensors
        vlan        :  VLAN
        vxlan       :  VXLAN data path
    cumulus@switch:~$ netq check 

### <span>Command Help</span>

<span style="color: #353744;"> As you enter commands, you can get help
with command syntax by entering *help* at various points within a
command entry. For example, to find out what options are available for a
BGP check, enter *h* </span> <span style="color: #353744;"> *elp* after
entering a portion of the `netq check` command. In this example, you can
see that there are no additional required parameters and two optional
parameters, *vrf* and *around*, that can be used with a BGP check.
</span>

    cumulus@switch:~$ netq check bgp help
    Commands:
       netq check bgp [vrf <vrf>] [around <text-time>] [json]
    cumulus@switch:~$

To see an exhaustive list of commands, run:

    cumulus@switch:~$ netq help list verbose

### <span id="src-12321059_NetQCommandLineOverview-ComHist" class="confluence-anchor-link"></span><span>Command History</span>

The CLI stores commands issued within a session, which enables you to
review and rerun commands that have already been run. At the command
prompt, press the **Up Arrow** and **Down Arrow** keys to move back and
forth through the list of commands previously entered. When you have
found a given command, you can run the command by pressing **Enter**,
just as you would if you had entered it manually. Optionally you can
modify the command before you run it.

## <span>Command Categories</span>

<span style="color: #353744;"> While the CLI has a flat structure, the
commands can be conceptually grouped into four functional categories:
</span>

  - <span style="color: #353744;"> [Validation
    Commands](#src-12321059_NetQCommandLineOverview-ChkCmds) </span>

  - <span style="color: #353744;"> [Monitoring
    Commands](#src-12321059_NetQCommandLineOverview-ShowCmds) </span>

  - <span style="color: #353744;"> [Configuration
    Commands](#src-12321059_NetQCommandLineOverview-ConfigCmds)  
    </span>

  - <span style="color: #353744;"> [Trace
    Commands](#src-12321059_NetQCommandLineOverview-TraceCmds) </span>

### <span>Validation Commands</span>

<span style="color: #353744;"> The `netq` `check` commands enable the
network administrator to validate the current or historical state of the
network by looking for errors and misconfigurations in the network. The
commands run fabric-wide validations against various configured
protocols and services to determine how well the network is operating.
</span> <span style="color: #353744;"> Validation checks can be
performed for the following: </span>

  - agents: NetQ Agents operation on all switches and hosts

  - bgp: BGP (Border Gateway Protocol) operation across the network
    fabric

  - clag: Cumulus Multi-chassis LAG (link aggregation) operation

  - evpn: EVPN (Ethernet Virtual Private Network) operation

  - interfaces: network interface port operation

  - license: License status

  - lnv: Lightweight Network Virtualization operation

  - mtu: Link MTU (maximum transmission unit) consistency across paths

  - ntp: NTP (Network Time Protocol) operation

  - ospf: OSPF (Open Shortest Path First) operation

  - sensors: Temperature/Fan/PSU sensor operation

  - vlan: VLAN (Virtual Local Area Network) operation

  - vxlan: VXLAN (Virtual Extensible LAN) data path operation

The commands take the form of `netq check <network-protocol-or-service>
[options]`, where the options vary according to the protocol or service.

This example shows the output for the `netq check bgp` command, followed
by the same command using the *json* option. If there had been any
failures, they would be have been listed below the summary results or in
the *failedNodes* section, respectively.

    cumulus@switch:~$ netq check bgp
    Total Nodes: 8, Failed Nodes: 0, Total Sessions: 30, Failed Sessions: 0
     
    cumulus@switch:~$ netq check bgp json
    {
        "failedNodes":[
        ],
        "summary":{
            "checkedNodeCount":8,
            "failedSessionCount":0,
            "failedNodeCount":0,
            "totalSessionCount":30
        }
    }

### <span>Monitoring Commands</span>

The `netq show` commands enable the network administrator to view
details about the current or historical configuration and status of the
various protocols or services. The configuration and status can be shown
for the following:

  - agents: NetQ Agents status on switches and hosts

  - bgp: BGP status across the network fabric

  - clag: CLAG status

  - events: Display changes over time

  - evpn: EVPN status

  - interfaces: network interface port status

  - inventory: hardware component information

  - ip: IPv4 status

  - ipv6: IPv6 status

  - kubernetes: Kubernetes cluster, daemon, pod, node, service and
    replication status

  - lldp: LLDP status

  - lnv: Lightweight Network Virtualization status

  - macs: MAC table or address information

  - notification: Slack or PagerDuty notification configurations

  - ntp: NTP status

  - ospf: OSPF status

  - sensors: Temperature/Fan/PSU sensor status

  - services: System services status

  - vlan: VLAN status

  - vxlan: VXLAN data path status

The commands take the form of `netq [<hostname>] show
<network-protocol-or-service> [options]`, where the options vary
according to the protocol or service. The commands can be restricted
from showing the information for *all* devices to showing information
for a selected device using the *hostname* variable.

This example shows the standard and restricted output for the `netq show
agents` command.

    cumulus@switch:~$ netq show agents
    Matching agents records:
    Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
    ----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
    edge01            Fresh            yes      2.1.0-ub16.04u15~1555612152.6e34b56  2d:2h:48m:43s             2d:2h:48m:36s             2d:2h:48m:36s              Sun Apr 21 16:00:50 2019
    exit01            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:2h:48m:1s              2d:2h:47m:53s             2d:2h:47m:53s              Sun Apr 21 16:00:52 2019
    exit02            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:2h:48m:7s              2d:2h:47m:58s             2d:2h:47m:58s              Sun Apr 21 16:01:19 2019
    leaf01            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:2h:47m:59s             2d:2h:47m:51s             2d:2h:47m:51s              Sun Apr 21 16:00:59 2019
    leaf02            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:2h:48m:9s              2d:2h:48m:0s              2d:2h:48m:0s               Sun Apr 21 16:01:43 2019
    leaf03            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:2h:48m:8s              2d:2h:47m:59s             2d:2h:47m:59s              Sun Apr 21 16:01:23 2019
    leaf04            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:2h:48m:10s             2d:2h:48m:2s              2d:2h:48m:2s               Sun Apr 21 16:01:27 2019
    server01          Fresh            yes      2.1.0-ub16.04u15~1555612152.6e34b56  2d:2h:46m:6s              2d:2h:45m:58s             2d:2h:45m:58s              Sun Apr 21 16:00:43 2019
    server02          Fresh            yes      2.1.0-ub16.04u15~1555612152.6e34b56  2d:2h:46m:5s              2d:2h:45m:57s             2d:2h:45m:57s              Sun Apr 21 16:00:46 2019
    server03          Fresh            yes      2.1.0-ub16.04u15~1555612152.6e34b56  2d:2h:46m:5s              2d:2h:45m:57s             2d:2h:45m:57s              Sun Apr 21 16:00:52 2019
    server04          Fresh            yes      2.1.0-ub16.04u15~1555612152.6e34b56  2d:2h:46m:5s              2d:2h:45m:57s             2d:2h:45m:57s              Sun Apr 21 16:00:43 2019
    spine01           Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:2h:48m:11s             2d:2h:48m:3s              2d:2h:48m:3s               Sun Apr 21 16:01:33 2019
    spine02           Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:2h:48m:5s              2d:2h:47m:57s             2d:2h:47m:57s              Sun Apr 21 16:01:12 2019
      
    cumulus@switch:~$ netq show agents json
    {
        "agents":[
            {
                "status":"Fresh",
                "lastChanged":1555862450.0,
                "reinitializeTime":1555689453.0,
                "hostname":"edge01",
                "version":"2.1.0-ub16.04u15~1555612152.6e34b56",
                "sysUptime":1555689446.0,
                "ntpSync":"yes",
                "agentUptime":1555689453.0
            },
            {
                "status":"Fresh",
                "lastChanged":1555862452.0,
                "reinitializeTime":1555689496.0,
                "hostname":"exit01",
                "version":"2.1.0-cl3u15~1555612272.6e34b56",
                "sysUptime":1555689488.0,
                "ntpSync":"yes",
                "agentUptime":1555689496.0
            },
            {
                "status":"Fresh",
                "lastChanged":1555862479.0,
                "reinitializeTime":1555689491.0,
                "hostname":"exit02",
                "version":"2.1.0-cl3u15~1555612272.6e34b56",
                "sysUptime":1555689482.0,
                "ntpSync":"yes",
                "agentUptime":1555689491.0
            },
    ...
      
    cumulus@switch:~$ netq leaf01 show agents
    Matching agents records:
    Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
    ----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
    leaf01            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:2h:49m:59s             2d:2h:49m:51s             2d:2h:49m:51s              Sun Apr 21 16:00:59 2019

### <span>Configuration Commands</span>

<span style="color: #353744;"> The `netq config` and `netq notification`
commands enable the network administrator to manage NetQ Agent and CLI
server configuration, set up container monitoring, and event
notification. </span>

#### <span>NetQ Agent Configuration </span>

The agent commands enable the network administrator to configure
individual NetQ Agents. Refer to [Cumulus NetQ
Primer](/version/cumulus-netq-22/Cumulus-NetQ-Deployment-Guide/Cumulus-NetQ-Primer)
for a description of NetQ Agents and to [Manage NetQ
Agents](/version/cumulus-netq-22/Cumulus-NetQ-CLI-User-Guide/Manage-NetQ-Agents)
for more detailed usage examples.

The agent configuration commands enable you to add and remove agents
from switches and hosts, start and stop agent operations, add and remove
Kubernetes container monitoring, add or remove sensors, debug the agent,
and add or remove FRR (FRRouting).

{{%notice info%}}

<span style="color: #353744;"> <span style="color: #353744;"> Commands
apply to one agent at a time, and are run from the switch or host where
the NetQ Agent resides. </span> </span>

{{%/notice%}}

<span style="color: #353744;"> <span style="color: #353744;"> The agent
configuration commands include: </span> </span>

    netq config (add|del|show) agent
    netq config (start|stop|status|restart) agent

This example shows how to configure the agent to send sensor data.

    cumulus@switch~:$ netq config add agent sensors

This example shows how to start monitoring with Kubernetes.

    cumulus@switch:~$ netq config add agent kubernetes-monitor poll-period 15

This example show how to view the NetQ Agent configuration.

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

{{%notice info%}}

After making configuration changes to your agents, you must restart the
agent for the changes to take effect. Use the `netq config restart
agent` command.

{{%/notice%}}

#### <span>CLI Configuration</span>

The CLI commands enable the network administrator to configure and
manage the CLI component. These commands enable you to add or remove CLI
(essentially enabling/disabling the service), start and restart it, and
view the configuration of the service.

{{%notice info%}}

<span style="color: #353744;"> Commands apply to one device at a time,
and are run from the switch or host where the CLI is run. </span>

{{%/notice%}}

<span style="color: #353744;"> The CLI configuration commands include:
</span>

    netq config (add|del|show) cli server
    netq config add cli server api.netq.cumulusnetworks.com access-key <user-access-key> secret-key <user-secret-key> port 443
    netq config (start|restart) cli

This example shows how to start the CLI instance.

    cumulus@switch~:$ netq config start cli

This example shows how to enable the CLI on a NetQ Platform or NetQ
Appliance.

    cumulus@switch~:$ netq config add cli server 10.1.3.101

This example shows how to enable the CLI on a NetQ Cloud Appliance.

    netq config add cli server api.netq.cumulusnetworks.com access-key <user-access-key> secret-key <user-secret-key> port 443

#### <span>Event Notification Commands</span>

<span style="color: #353744;"> The notification configuration commands
enable you to add, remove and show notification application
integrations. These commands create the channels, filters, and rules
needed to control event messaging. </span>
<span style="color: #353744;"> The commands include: </span>

    netq (add|del|show) notification channel
    netq (add|del|show) notification rule
    netq (add|del|show) notification filter

An integration includes at least one channel, PagerDuty or Slack.
Filters are optional and defined by rules you create. If you have a
filter, it must have at least one rule.

This example shows how to configure a PagerDuty channel:

    cumulus@switch:~$ netq add notification channel pagerduty pd-netq-events integration-key c6d666e210a8425298ef7abde0d1998
    Successfully added/updated channel pd-netq-events

<span style="color: #353744;"> Refer to </span>
<span style="color: #353744;"> </span> [Integrate with Third-party
Software and
Hardware](/version/cumulus-netq-22/Cumulus-NetQ-Deployment-Guide/Integrate-with-Third-party-Software-and-Hardware)
<span style="color: #353744;"> for details about using these commands
and additional examples. </span>

### <span>Trace Commands</span>

<span style="color: #353744;"> The `trace` commands enable the network
administrator to view the available paths between two nodes on the
network currently and at a time in the past. You can perform a layer 2
or layer 3 trace, and view the output in one of three formats (*json,
pretty,* and *detail*). JSON output provides the output in a JSON file
format for ease of importing to other applications or software. Pretty
output lines up the paths in a pseudo-graphical manner to help visualize
multiple paths. Detail output is useful for traces with higher hop
counts where the pretty output wraps lines, making it harder to
interpret the results. The detail output displays a table with a row for
each path. </span>

<span style="color: #353744;"> The trace command syntax is: </span>

    netq trace <mac> [vlan <1-4096>] from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug]
    netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug] 

<span style="color: #353744;"> **Example**: Running a trace based on the
destination IP address, in *pretty* output </span> with a small number
of resulting paths:

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

**Example**: Running a trace <span style="color: #353744;"> based on the
destination IP address, in *detail* output </span> with a small number
of resulting paths:

    cumulus@oob-mgmt-server:~$ netq trace 10.0.0.11 from 10.0.0.14 detail
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

<span style="color: #353744;"> **Example**: Running a trace based on the
destination MAC address, in *pretty* output: </span>

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

## <span>Command Changes</span>

A number of commands have changed in this release to accommodate the
addition of new keywords and options or to simplify their syntax.
Additionally, new commands have been added and others have been removed.
A summary of those changes is provided here.

### <span>New Commands</span>

The following table summarizes the new commands available with this
release.

| Command                                                                                                                    | Summary                                                                          |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `netq install opta interface <text-opta-ifname> tarball <text-tarball-name> key <text-opta-key> [file <text-config-file>]` | Installs NetQ software onto NetQ Cloud Appliance.                                |
| `netq upgrade opta interface <text-opta-ifname> key <text-opta-key>`                                                       | Upgrades the NetQ software on the NetQ Cloud Appliance.d                         |
| `netq [<hostname>] show interface-stats [errors \| all] [<physical-port>] [around <text-time>] [json]`                     | This is an early access feature that displays a variety of interface statistics. |

### <span>Modified Commands</span>

The following table summarizes the commands that have been changed with
this release.

| Updated Command                                                                                                                                                                             | Old Command                                                                | What Changed                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `netq check evpn [mac-consistency] [around <text-time>] [json]`                                                                                                                             | `netq [<hostname>] show evpn [vni <text-vni>] [around <text-time>] [json]` | Added *mac-consistency* option that includes a check to verify if the MAC associated with each end of the EVPN connection is the same. Removed *hostname* and *vni* options. |
| `netq config add cli server <text-gateway-dest> [access-key <text-access-key> secret-key <text-secret-key>] [premise <text-premise-name>] [port <text-gateway-port>] [vrf <text-vrf-name>]` | `netq config add cli server`                                               | This adds the CLI daemon to the switch or host where this command is run. When using a NetQ Cloud Appliance, the access-key, secret-key, and port are required.              |
| `netq config show cli premises [json]`                                                                                                                                                      | `netq config show cli [json]`                                              | Displays configuration settings for the CLI for all cloud premises.                                                                                                          |

### <span>Deprecated Commands</span>

The following table summarizes the commands that have been removed and a
recommended alternative, if appropriate.

| Command | Alternative Command |
| ------- | ------------------- |
| N/A     | N/A                 |

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
