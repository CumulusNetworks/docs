---
title: NetQ Command Line Overview
author: Cumulus Networks
weight: 51
aliases:
 - /display/NETQ141/NetQ+Command+Line+Overview
 - /pages/viewpage.action?pageId=10453454
pageID: 10453454
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
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
If you are unsure what architecture your
switch or server employs, check the Cumulus [Hardware Compatibility
List](https://cumulusnetworks.com/products/hardware-compatibility-list/)
and verify the value in the **Platforms** tab \> **CPU** column.

{{%/notice%}}

## CLI Access

When NetQ is installed, the CLI is also installed and enabled (refer to
the [Install
NetQ](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
topic). Simply log in to any network node to access the command line. If
you want to run the CLI on the Telemetry Server (TS), Cumulus Networks
recommends using netq-shell. While most other Linux commands can work
from this shell, Cumulus Networks recommends you only run `netq`
commands here.  

To access the CLI from a switch or server:

1.  Log in to device. This example uses a
    username of *Cumulus* and a hostname of *switch*.  


        <computer>:~Cumulus$ ssh switch

2.  Enter your password, if required, to reach the command prompt. For
    example:  

        Enter passphrase for key '/Users/<username>/.ssh/id_rsa': 
        Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-112-generic x86_64)
         * Documentation:  https://help.ubuntu.com
         * Management:     https://landscape.canonical.com
         * Support:        https://ubuntu.com/advantage
        Last login: Thu Aug 16 06:28:12 2018 from 10.50.11.103
        <username>@<hostname>:~$ 

3.  Run commands. For example:  

        <username>@<hostname>:~$netq show agents
        <username>@<hostname>:~$netq check bgp

To access the CLI from a Telemetry Server:   

1.  Log in to TS. This example uses a username of *Cumulus* and a TS with a
    hostname of *ts*.

        <computer>:~Cumulus$ ssh ts

2.  Run netq-shell.  

        cumulus@ts:~$ netq-shell
        Welcome to Cumulus (R) Linux (R)
         
        For support and online technical documentation, visit
        http://www.cumulusnetworks.com/support
         
        The registered trademark Linux (R) is used pursuant to a sublicense from LMI, the exclusive licensee of Linux Torvalds, owner of the mark on a worldwide basis.
         
        TIP: Type `netq` to access NetQ CLI.
        cumulus@ts:~$

3.  Run commands. For example:

        Cumulus@ts:~$ netq show agent
        Matching agents records:
        Hostname    Status    Ntp Sync    Version                             Sys Uptime    Agent Uptime    Reinitialize Time    Last Changed
        ----------  --------  ----------  ----------------------------------  ------------  --------------  -------------------  --------------
        leaf01      Fresh     yes         1.3.0-cl3u9~1522713084.b08ca60      2h:42m:27s    2h:15m:36s      2h:15m:36s           23.663727s
        leaf02      Fresh     yes         1.3.0-cl3u9~1522713084.b08ca60      2h:42m:2s     2h:15m:37s      2h:15m:37s           35.518794s
        leaf03      Fresh     yes         1.3.0-cl3u9~1522713084.b08ca60      2h:42m:13s    2h:15m:36s      2h:15m:36s           9.191086s
        leaf04      Fresh     yes         1.3.0-cl3u9~1522713084.b08ca60      2h:42m:28s    2h:15m:37s      2h:15m:37s           9.809986s
        server01    Fresh     yes         1.3.0-ub16.04u9~1522713679.b08ca60  2h:29m:14s    2h:13m:41s      2h:13m:41s           12.207030s
        server02    Fresh     yes         1.3.0-ub16.04u9~1522713679.b08ca60  2h:29m:14s    2h:1m:8s        2h:1m:8s             31.850285s
        server03    Fresh     yes         1.3.0-ub16.04u9~1522713679.b08ca60  2h:29m:14s    2h:0m:21s       2h:0m:21s            15.317886s
        server04    Fresh     yes         1.3.0-ub16.04u9~1522713679.b08ca60  2h:29m:14s    2h:16m:33s      2h:16m:33s           22.853980s
        spine01     Fresh     yes         1.3.0-cl3u9~1522713084.b08ca60      2h:42m:42s    2h:15m:36s      2h:15m:36s           21.486093s
        spine02     Fresh     yes         1.3.0-cl3u9~1522713084.b08ca60      2h:42m:55s    2h:15m:37s      2h:15m:37s           6.269588s
        Cumulus@ts:~$ netq check agents
        Checked nodes: 12, Rotten nodes: 0

## Command Line Basics

This section describes the core structure
and behavior of the NetQ CLI. It includes the following:

  - [Command Line Structure](#src-10453454_NetQCommandLineOverview-ComStruct)
  - [Command Syntax](#src-10453454_NetQCommandLineOverview-ComSyntax)
  - [Command Output](#src-10453454_NetQCommandLineOverview-ComOut)
  - [Command Prompts](#src-10453454_NetQCommandLineOverview-ComPrompt)
  - [Command Completion](#src-10453454_NetQCommandLineOverview-ComComp)
  - [Command Help](#src-10453454_NetQCommandLineOverview-ComHelp)
  - [Command History](#src-10453454_NetQCommandLineOverview-ComHist)

### Command Line Structure

The Cumulus NetQ command line has a flat
structure as opposed to a modal structure. This means that all commands
can be run from the primary prompt instead of only in a specific mode.
 For example, some command lines
require the administrator to switch between a configuration mode and an
operation mode. Configuration commands can only be run in the
configuration mode and operational commands can only be run in operation
mode. This structure requires the administrator to switch between modes
to run commands which can be tedious and time consuming. Cumulus NetQ
command line enables the administrator to run all of its commands at the
same level.

### Command Syntax

NetQ CLI commands all begin with `netq`.
 Their basic syntax is as follows:

    netq [<hostname>] (check|show) <object> <options>
    netq trace <options>
    netq resolve
    netq config (agent|notifier) <action> [<options>] [vrf <vrf>]

| Symbols               | Meaning                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| Parentheses ( )       | Enter one of the objects or keywords                                                              |
| Square brackets \[ \] | Optional parameter; enter keyword or keyword-value pair as needed                                 |
| Angle brackets \< \>  | Variable value for a keyword or option; required, enter according to your deployment nomenclature |
| Pipe |                | Separates keyword options, also separates value options; enter one keyword and zero or one value  |

For example, in the `netq check` command:

  - \[\<hostname\>\] is an optional
    parameter with a variable value named *hostname*

  - \<object\> represents a number of possible key words, such as
    *agents, bgp, clag,* and so forth

  - \<options\> represents a number of possible conditions for the given
    object, such as *around, vrf,* or *json*

Thus some valid commands are:

  - `netq check agents json`
  - `netq show bgp`
  - `netq agent restart`

### Command Output

The command output presents results in
color for many commands.  Results with errors are shown in
<span style="color: #ff0000;"> red </span> , and warnings are shown in
<span style="color: #ffcc00;"> yellow </span> . Results without errors
or warnings are shown in either black or <span style="color: #00ff00;">
green </span> . VTEPs are shown in <span style="color: #0000ff;"> blue
</span> . A node in the *pretty* output is shown in **bold**, and a
router interface is wrapped in angle brackets (\< \>). To view the
output with only black text, run the `netq config del color` command.
You can view output with colors again by running `netq config add
color`.

All check and show commands are run with
a default timeframe of now to one hour ago, unless you specify an
approximate time (`around` keyword) or a range (`between` keyword). For example, running `netq check bgp` shows the status of BGP
over the last hour. Running `netq show bgp around 3h` shows the status
of BGP three hours ago. Running `netq show bgp changes between now
and 3h` shows changes that have been made to BGP configuration in the
past three hours.

### Command Prompts

NetQ code examples use the following
prompts:

| Prompt              | Description                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| `cumulus@switch:~$` | Indicates the user *cumulus* is logged in to a switch to run the example command                  |
| `cumulus@ts:~$`     | Indicates the user *cumulus* is logged in to the Telemetry Server (TS) to run the example command |
| `cumulus@host:~$`   | Indicates the user *cumulus* is logged in to a host to run the example command                    |

The switches and TS must be running the Cumulus Linux operating system
(OS) and NetQ. The hosts must be running CentOS, RHEL, or Ubuntu OS and
NetQ. Refer to the [Install
NetQ](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
topic for details.

### Command Completion

As you
enter commands, you can get help with the valid keywords or options
using the Tab key. For example, using Tab completion with `netq
check` displays the possible objects for the command, and returns you to
the command prompt to complete the command.

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
    cumulus@oob-mgmt-server:~$ netq check 

### Command Help

As you enter commands, you can get help
with command syntax by entering *help* at various points within a
command entry. For example, to find out what options are available for a
BGP check, enter *help* after
entering a portion of the `netq check` command. In this example, you can
see that there are two possible commands related to BGP checks and the
display shows the options available for each.

    cumulus@ts:~$ netq check bgp help
    Commands:
       netq example check bgp
       netq check bgp [vrf <vrf>] [around <text-time>] [json]
    Keywords:
       check bgp                    : Check BGP Status Across the Fabric
    cumulus@ts:~$

To see an exhaustive list of commands, run:

    cumulus@switch:~$ netq help list verbose

### Command History

The CLI stores commands issued within a session, which enables you to
review and rerun commands that have already been run. At the command
prompt, press the **Up Arrow** and **Down Arrow** keys to move back and
forth through the list of commands previously entered. When you have
found a given command, you can run the command by pressing **Enter**,
just as you would if you had entered it manually. Optionally you can
modify the command before you run it.

## Command Categories

While the CLI has a flat structure, the
commands can be conceptually grouped into four functional categories:


  - [Check and Show Commands](#src-10453454_NetQCommandLineOverview-ChkShCmds)
  - [Agent and Notifier Commands](#src-10453454_NetQCommandLineOverview-AgentNotifCmds)
  - [Trace Command](#src-10453454_NetQCommandLineOverview-TraceCmd)
  - [Resolve Command](#src-10453454_NetQCommandLineOverview-ResolveCmd)

### Check and Show Commands

The `check` and `show` commands enable
the network administrator to view the current and historical state of
the network by manually monitoring for errors and misconfigurations in
the network. Check commands run validation checks against various
components and configured protocols and services to determine the
network is operating as expected. Show commands present details about
the current or historical configuration and status of the various
component, protocol or service.

Validation checks can be performed for
the following:

  - agents: NetQ Agents operation on all switches and hosts
  - bgp: BGP (Border Gateway Protocol) operation across the network
    fabric
  - clag: Cumulus Multi-chassis LAG (link aggregation) operation
  - evpn: EVPN (Ethernet Virtual Private Network) operation
  - interfaces: network interface port operation
  - license: License status
  - lnv: Lightweight Network Virtualization operation
  - mtu: Link MTU (maximun transmission unit) consistency across fabric
  - ntp: NTP (Network Time Protocol) operation
  - ospf: OSPF (Open Shortest Path First) operation
  - sensors: Temperature/Fan/PSU sensor operation
  - vlan: VLAN (Virtual Local Area Network) operation
  - vxlan: VXLAN (Virtual Extensible LAN) data path operation

The configuration and status can be shown
for the following:

  - agents: NetQ Agents status on switches and hosts
  - bgp: BGP status across the network fabric
  - change: For a given component, protocol or service, lists changes
    over time frame
  - clag: CLAG status
  - docker: Docker Swarm, container and network status
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
  - ntp: NTP status
  - ospf: OSPF status
  - sensors: Temperature/Fan/PSU sensor status
  - services: System services status
  - vlan: VLAN status
  - vxlan: VXLAN data path status

The commands take the form of `netq [<hostname>] (check|show) <object>
<options>`, where the object is one of the components, protocols, or
services listed here and the options vary according to the object. The
commands can be restricted from checking or showing the information for
*all* devices to checking or showing information for a *group* of
devices or a *selected* device using the *hostname* keyword.

This example shows all three cases for the `netq show agents` command.

    cumulus@switch:~$ netq show agents
    Matching agents records:
    Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
    ----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
    edge01            Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   9d:22h:2m:52s             9d:22h:2m:42s             13h:57m:25s                21.85752s
    exit01            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:48m:26s            7d:17h:46m:50s            13h:58m:38s                16.678010s
    exit02            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:48m:24s            7d:17h:46m:26s            13h:58m:46s                6.584077s
    internet          Fresh            no       1.3.0-cl3u9~1522970647.b08ca60       7d:22h:48m:29s            7d:22h:48m:8s             13h:58m:42s                29.653689s
    leaf01            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:48m:27s            7d:18h:39m:50s            13h:58m:46s                32.407732s
    leaf02            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:48m:28s            7d:17h:53m:11s            13h:58m:41s                15.177563s
    leaf03            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:48m:25s            7d:17h:52m:22s            13h:58m:42s                27.262121s
    leaf04            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:48m:19s            7d:17h:49m:1s             13h:58m:48s                13.540505s
    oob-mgmt-server   Fresh            yes      1.4.0-cl3u10~1537731912.eae9c33      9d:22h:4m:24s             9d:22h:3m:59s             13h:58m:38s                23.999988s
    server01          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   7d:22h:46m:36s            7d:22h:46m:26s            13h:58m:45s                5.142742s
    server02          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   7d:22h:46m:36s            7d:22h:46m:26s            13h:58m:44s                4.564975s
    server03          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   7d:22h:46m:36s            7d:22h:46m:26s            13h:58m:45s                7.762726s
    server04          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   7d:22h:46m:36s            7d:22h:46m:26s            13h:58m:47s                9.125672s
    spine01           Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:48m:26s            7d:17h:48m:18s            13h:58m:49s                13.474365s
    spine02           Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:48m:19s            7d:17h:47m:50s            13h:58m:40s                33.837156s
     
    cumulus@switch:~$ netq 'leaf*' show agents
    Matching agents records:
    Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
    ----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
    leaf01            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:45m:25s            7d:18h:36m:48s            13h:55m:44s                6.249341s
    leaf02            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:45m:26s            7d:17h:50m:9s             13h:55m:39s                20.84034s
    leaf03            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:45m:23s            7d:17h:49m:20s            13h:55m:40s                32.264194s
    leaf04            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:45m:17s            7d:17h:45m:59s            13h:55m:46s                18.449755s
     
    cumulus@switch:~$ netq spine01 show agents
    Matching agents records:
    Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
    ----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
    spine01           Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       7d:22h:48m:47s            7d:17h:48m:39s            13h:59m:10s                34.242092s

### Agent and Notifier Commands

The agent and notifier commands enable the network administrator to
configure individual NetQ Agents and the NetQ Notifier on the TS. Refer
to the [Cumulus NetQ Primer](/version/cumulus-netq-141/) and [Configure
Optional NetQ
Capabilities](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Configure-Optional-NetQ-Capabilities)
topics for details about these NetQ components.

The agent
configuration commands enable you to add and remove agents from switches
and hosts, start and stop agent operations, add and remove docker and
kubernetes container monitoring, add or remove sensors, debug the agent,
and add or remove FRR (Free Range Routing). Commands apply to one agent
at a time, and are run from the switch or host where the NetQ Agent
resides.

The agent configuration commands include:

    netq config (start|stop|status|restart) agent
    netq config add agent docker-monitor [poll-period <text-duration-period>]
    netq config del agent docker-monitor
    netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
    netq config del agent kubernetes-monitor
    netq config (add|del) agent (stats|sensors)
    netq config add agent loglevel [debug|info|warning|error]
    netq config add agent frr-monitor [<text-frr-docker-name>]
    netq config del agent (loglevel|frr-monitor)
    netq config show agent [kubernetes-monitor|docker-monitor|loglevel|stats|sensors|frr-monitor] [json]

The notifier configuration commands
enable you to start and stop the NetQ
Notifier, add and remove notification application integrations,
debug the notifier operation, and view its configuration. The commands
must be run on the Telemetry Server where the NetQ Notifier resides.

The notifier configuration commands include:

    netq config ts add notifier integration slack <text-integration-name> webhook <text-webhook-url>
        [severity info | severity warning | severity error | severity debug | severity info] [tag <text-slack-tag>]
    netq config ts add notifier integration pagerduty <text-integration-name> api-access-key <text-api-access-key> api-integration-key
        <text-api-integration-key> [severity info | severity warning | severity error | severity debug | severity info]
    netq config ts add notifier integration pagerduty <text-integration-name> api-integration-key <text-api-integration-key>
        api-access-key <text-api-access-key> [severity info | severity warning | severity error | severity debug | severity info]
    netq config ts add notifier filter <text-filter-name> [before <text-filter-name-anchor> | after <text-filter-name-anchor>]
        [rule <text-rule-key> <text-rule-value>] [output <text-integration-name-anchor>]
    netq config ts add notifier loglevel [debug|info|warning|error]
    netq config ts del notifier loglevel
    netq config ts del notifier integration (slack|pagerduty) <text-integration-name-anchor>
    netq config ts del notifier filter <text-filter-name-anchor>
    netq config ts (start|stop|status|restart) notifier
    netq config ts show notifier [json]

Notice that the `netq config ts add notifier integration pagerduty` is
presented twice here because the `api-access-key` and the
`api-integration-key` are not order dependent. Either can be entered
first. The rest of the syntax is the same.

### Trace Command

The `trace` command enables the network
administrator to view the available paths between two nodes on the
network currently and at a time in the past. You can base the trace on
MAC or IP addresses, perform the trace in only one direction or both,
and view the output in one of three formats (*json, pretty,* and
*detail*). JSON output provides the output in a JSON file format for
ease of importing to other applications or software. Pretty output lines
up the paths in a pseudo-graphical manner to help visualize multiple
paths. Detail output is useful for traces with higher hop counts where
the pretty output wraps lines, making it harder to interpret the
results. The detail output displays a table with a row for each path.
The trace command also has a detailed usage example for reference.

The trace command syntax is:

    netq trace <mac> [vlan <1-4096>] from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [bidir] [json|detail|pretty] [debug]
    netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [bidir] [json|detail|pretty] [debug] 

**Example**: Running a trace based on the
destination IP address, in *pretty* output with a small number
of resulting paths

    cumulus@switch:~# netq trace 192.168.0.11 from Leaf04 pretty
    Number of Paths: 2
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9202
     
     Leaf04 uplink-2 -- downlink-5 Spine02 downlink-1 -- uplink-2 Leaf01 <uplink-2>
            uplink-1 -- downlink-5 Spine01 downlink-1 -- uplink-1 Leaf01 <uplink-2>

**Example**: Running a trace based on the
destination MAC address, in *pretty* output with a larger number of
resulting paths

    cumulus@switch:mgmt-vrf:~# netq trace A0:00:00:00:00:11 vlan 1001 from Server03 detail
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

**Example**: View the detailed usage example for the trace command

    cumulus@switch:~$ netq example trace
     
    Control Path Trace
    ==================
     
    Commands
    ========
       netq trace <mac> [vlan <1-4096>] from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [bidir] [json|detail|pretty] [debug]
       netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [bidir] [json|detail|pretty] [debug]
     
    Usage
    =====
    netq trace provides control path tracing (no real packets are sent) from a specified source to a specified destination. The trace covers complete
    end-to-end path tracing including bridged, routed and VXLAN overlay paths. ECMP is supported as well as checking for forwarding loops, MTU consistency
    across all paths, and VLAN consistency across all paths.  Reverse path trace is also available as an option.
     
    ...

### Resolve Command

The
`resolve` command enables the network administrator to view Cumulus
Linux command results with more contextual information
and colored highlights. By piping the commands through netq resolve, the
output shows hostnames and interfaces in <span style="color: #00ff00;">
green </span>, for example.

To show routes installed by the kernel, you would run the `ip route show
proto kernel` command:

    cumulus@leaf01:~$ ip route show proto kernel
    3.0.2.128/26 dev VlanA-1.103  scope link  src 3.0.2.131
    3.0.2.128/26 dev VlanA-1-103-v0  scope link  src 3.0.2.129
    3.0.2.192/26 dev VlanA-1.104  scope link  src 3.0.2.195
    3.0.2.192/26 dev VlanA-1-104-v0  scope link  src 3.0.2.193
    3.0.3.0/26 dev VlanA-1.105  scope link  src 3.0.3.3
    3.0.3.0/26 dev VlanA-1-105-v0  scope link  src 3.0.3.1
    3.0.3.64/26 dev VlanA-1.106  scope link  src 3.0.3.67
    3.0.3.64/26 dev VlanA-1-106-v0  scope link  src 3.0.3.65
    169.254.0.8/30 dev peerlink-1.4094  scope link  src 169.254.0.10
    192.168.0.0/24 dev eth0  scope link  src 192.168.0.15

You can enhance the output to display the node names and interfaces by
piping the output through `netq resolve` so the output looks like this:

    cumulus@leaf01:~$ ip route show proto kernel | netq resolve
    10.0.0.0/22 (multiple:) dev eth0  scope link  src 10.0.0.165 (cel-smallxp-13:eth0)
    3.0.2.128/26 (server02:torbond1.103) dev VlanA-1.103  scope link  src 3.0.2.131 (leaf02:VlanA-1.103)  
    3.0.2.128/26 (server02:torbond1.103) dev VlanA-1-103-v0  scope link  src 3.0.2.129 (leaf02:VlanA-1-103-v0)  
    3.0.2.192/26 (leaf02:VlanA-1-104-v0) dev VlanA-1.104  scope link  src 3.0.2.195 (leaf02:VlanA-1.104)  
    3.0.2.192/26 (leaf02:VlanA-1-104-v0) dev VlanA-1-104-v0  scope link  src 3.0.2.193 (leaf02:VlanA-1-104-v0)  
    3.0.3.0/26 (server01:torbond1.105) dev VlanA-1.105  scope link  src 3.0.3.3 (leaf02:VlanA-1.105)  
    3.0.3.0/26 (server01:torbond1.105) dev VlanA-1-105-v0  scope link  src 3.0.3.1 (leaf02:VlanA-1-105-v0)  
    3.0.3.64/26 (server02:torbond1.106) dev VlanA-1.106  scope link  src 3.0.3.67 (leaf02:VlanA-1.106)  
    3.0.3.64/26 (server02:torbond1.106) dev VlanA-1-106-v0  scope link  src 3.0.3.65 (leaf01:VlanA-1-106-v0)  
    169.254.0.8/30 (leaf02:peerlink-1.4094) dev peerlink-1.4094  scope link  src 169.254.0.10 (leaf02:peerlink-1.4094)  
    192.168.0.0/24 (server02:eth0) dev eth0  scope link  src 192.168.0.15 (leaf01:eth0)

## Detailed Usage Examples

Additional help is available to understand key commands using the
examples provided with NetQ. Each example includes details about a
command's usage and operation, as well as specific examples to help you
monitor and manage your network, and solve issues you may find.

Run any of the example commands to view its detailed information:

    netq example check bgp
    netq example check clag
    netq example check mtu
    netq example find-duplicates
    netq example find-origin
    netq example ha-setup
    netq example query
    netq example regexp
    netq example resolve macs
    netq example resolve routes
    netq example startup
    netq example stats
    netq example trace

**Example**: View Example for Duplicate IP or MAC Address

    cumulus@switch:~$ netq example find-duplicates
    Find Duplicate IP or MAC
    ========================
    Commands
    ========
        - netq show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] origin [around <text-time>] [json]
        - netq show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] origin count [around <text-time>] [json]
        - netq show macs [<mac>] [vlan <0-4096>] origin [around <text-time>] [json]
     
    Usage
    =====
    Using the 'origin' option coupled with the 'count' option, its easy to find duplicate route announcements.
     
        cumulus@switch:mgmt-vrf:~$ netq show ip routes 3.0.0.0/26 origin count
        Count of matching routes: 3
     
    The example above shows that the ip route 3.0.0.0/26 has been announced from three nodes in the network. You can look at which nodes by issuing the same
    command without the count option. JSON output is of course available for both commands.
     
    ...

## Command Changes

A number of commands have changed in this release to accommodate the
addition of new keywords and options or to simplify their syntax.
Additionally, new commands have been added and others have been removed.
A summary of those changes is provided here.

### New Commands

The following table summarizes the new commands available with this release.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 47%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><p> </p></th>
<th><p>Command</p></th>
<th><p>Summary</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1</p></td>
<td><p>netq config (add|del) color</p></td>
<td><p>Add or remove color from CLI output. Default displays colored output.</p></td>
</tr>
<tr class="even">
<td><p>2</p></td>
<td><p>netq config (status|restart) cli</p></td>
<td><p>Show whether the CLI daemon is running, or restart the CLI daemon if it is not running</p></td>
</tr>
<tr class="odd">
<td><p>3</p></td>
<td><p>netq [&lt;hostname&gt;] show agents changes [between &lt;text-time&gt; and &lt;text-endtime&gt;] [json]</p></td>
<td><p>Show NetQ Agent configuration or status changes within the specified timeframe. When the timeframe is not specified, the default is 1 hour.</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>netq [&lt;hostname&gt;] show docker swarm cluster [node-name &lt;cluster-node&gt;] [around &lt;text-time&gt;] [json]</p></td>
<td><p>Show Docker Swarm container clusters at an earlier point in time</p></td>
</tr>
<tr class="odd">
<td><p>5</p></td>
<td><p>netq [&lt;hostname&gt;] show docker swarm cluster changes [between &lt;text-time&gt; and &lt;text-endtime&gt;] [json]</p></td>
<td><p>Show Docker Swarm container cluster configuration or status changes within the specified timeframe. When the timeframe is not specified, the default is 1 hour. </p></td>
</tr>
<tr class="even">
<td><p>6</p></td>
<td><p>netq config add agent frr-monitor [&lt;text-frr-docker-name&gt;]</p></td>
<td><p>Add Free Range Routing (FRR) monitoring to the switch or host server</p></td>
</tr>
<tr class="odd">
<td><p>7</p></td>
<td><p>netq config ts del notifier integration (slack|pagerduty) &lt;text-integration-name-anchor&gt;</p></td>
<td><p>Remove an event notification integration using its anchor name</p></td>
</tr>
<tr class="even">
<td><p>6</p></td>
<td><p>netq config ts del notifier filter &lt;text-filter-name-anchor&gt;</p></td>
<td><p>Remove an event filter using its anchor name</p></td>
</tr>
</tbody>
</table>

### Modified Commands

The following table summarizes the commands that have been changed with
this release.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 47%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><p> </p></th>
<th><p>Command</p></th>
<th><p>What Changed</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1</p></td>
<td><p>netq check agents [around &lt;text-time&gt;] [json]</p></td>
<td><p>Added around keyword-value pair</p></td>
</tr>
<tr class="even">
<td><p>2</p></td>
<td><p>netq [&lt;hostname&gt;] show agents [around &lt;text-time&gt;] [json]</p></td>
<td><p>Added around keyword-value pair</p></td>
</tr>
<tr class="odd">
<td><p>3</p></td>
<td><p>netq config (add|del) agent (stats|sensors)</p></td>
<td><p>Added sensors keyword</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>netq config del agent (loglevel|frr-monitor)</p></td>
<td><p>Added frr-monitor keyword</p></td>
</tr>
<tr class="odd">
<td><p>5</p></td>
<td><p>netq config show agent [kubernetes-monitor|docker-monitor|loglevel|stats|sensors|frr-monitor] [json]</p></td>
<td><p>Added sensors and frr-monitor keywords</p></td>
</tr>
<tr class="even">
<td><p>6</p></td>
<td><p>netq config ts add notifier integration slack &lt;text-integration-name&gt; webhook &lt;text-webhook-url&gt; [severity info | severity warning | severity error | severity debug | severity info] [tag &lt;text-slack-tag&gt;]</p></td>
<td><p>Added integration keyword</p></td>
</tr>
<tr class="odd">
<td><p>7</p></td>
<td><p>netq config ts add notifier integration pagerduty &lt;text-integration-name&gt; api-integration-key &lt;text-api-integration-key&gt; api-access-key &lt;text-api-access-key&gt; [severity info | severity warning | severity error | severity debug | severity info]</p>
<p>netq config ts add notifier integration pagerduty &lt;text-integration-name&gt; api-access-key &lt;text-api-access-key&gt; api-integration-key &lt;text-api-integration-key&gt; [severity info | severity warning | severity error | severity debug | severity info]</p></td>
<td><p>Added integration keyword and allowed user-preferred order of api-integration-key and api-access-key keywords</p></td>
</tr>
<tr class="even">
<td><p>8</p></td>
<td><p>netq config ts add notifier filter &lt;text-filter-name&gt; [before &lt;text-filter-name-anchor&gt; | after &lt;text-filter-name-anchor&gt;] [rule &lt;text-rule-key&gt; &lt;text-rule-value&gt;] [output &lt;text-integration-name-anchor&gt;]</p></td>
<td><p>Combined separate NetQ Notifier commands into single command</p></td>
</tr>
<tr class="odd">
<td><p>9</p></td>
<td><p>netq trace &lt;mac&gt; [vlan &lt;1-4096&gt;] from (&lt;src-hostname&gt;|&lt;ip-src&gt;) [vrf &lt;vrf&gt;] [around &lt;text-time&gt;] [bidir] [json|detail|pretty] [debug]</p></td>
<td><p>Added ip-source as alternate for src-hostname. Added bidir as option to perform the trace in both directions. Added detail (tabular) and pretty (tree-like) output options. Added debug keyword.</p></td>
</tr>
<tr class="even">
<td><p>10</p></td>
<td><p>netq trace &lt;ip&gt; from (&lt;src-hostname&gt;|&lt;ip-src&gt;) [vrf &lt;vrf&gt;] [around &lt;text-time&gt;] [bidir] [json|detail|pretty] [debug]</p></td>
<td><p>Added bidir as option to perform the trace in both directions. Added detail (tabular) and pretty (tree-like) doutput options. Added debug keyword.</p></td>
</tr>
</tbody>
</table>

### Deprecated commands

The following table summarizes the commands that have been removed and a
recommended alternative, if appropriate.

|     | Command                                        | Alternative Command                   |
| --- | ---------------------------------------------- | ------------------------------------- |
| 1 | netq config ts show notifier loglevel \[json\] | netq config ts show notifier \[json\] |
