---
title: Getting to Know NetQ
author: Cumulus Networks
weight: 13
aliases:
 - /display/NETQ110/Getting+to+Know+NetQ
 - /pages/viewpage.action?pageId=7111332
pageID: 7111332
product: Cumulus NetQ
version: "1.1"
imgData: cumulus-netq-110
siteSlug: cumulus-netq-110
---
After you've installed NetQ, running `netq example` gives you some
pointers as to how it helps you solve issues across your network.

    cumulus@oob-mgmt-server:~$ netq example 
        check            :  Perform fabric-wide checks
        find-duplicates  :  Find Duplicate IP or MAC
        find-origin      :  Find Origin of Route/MAC
        regexp           :  Using Regular Expressions
        resolve          :  Annotate input with names and interesting info
        startup          :  NetQ Quickstart
        trace            :  Control Path Trace
     
    cumulus@switch:~$ netq example trace 
     
    Control Path Trace
    ==================
     
     
    Commands
    ========
       netq trace <mac> [vlan <1-4096>] from <hostname> [vrf <vrf>] [around <text-time>] [json]
       netq trace <ip> from (<hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json]
     
     
    Usage
    =====
    netq trace provides control path tracing (no real packets are sent) from
    a specified source to a specified destination. The trace covers complete
    end-to-end path tracing including bridged, routed and Vxlan overlay paths.
    ECMP is supported as well as checking for forwarding loops, MTU consistency
    across all paths, and VLAN consistency across all paths. The trace also
    covers that the path from dest to src also exists on each hop.
     
     
    cumulus@torc-12:~$ netq trace 27.0.0.22 from 27.0.0.21
    torc-12 -- torc-12:swp3 -- spine-1:swp5 -- torc-21:lo
            -- torc-12:swp4 -- spine-2:swp5 -- torc-21:lo
     
     
    When tracing data, only the egress information is shown as this information
    is gathered by looking at the routing table. In this case, there are two paths
    (one through spine01 and one through spine02) because the environment is
    leveraging equal cost routing.
     
     
    You can trace by MAC as well:
    cumulus@leaf1:~$ netq trace 00:02:00:00:00:02 vlan 1009 from leaf1
    leaf1 -- leaf1:sw_clag200 -- spine1:sw_clag300 -- edge2
                              -- spine1:sw_clag300 -- edge1:VlA-1
          -- leaf1:sw_clag200 -- spine2:sw_clag300 -- edge1:VlA-1
                              -- spine2:sw_clag300 -- edge2
    cumulus@leaf1:~$
     
     
    Legend
    ======
    Any errors are shown in red. Bridged paths are always in WHITE, routed paths
    in GREEN, the VTEPs are shown in BLUE. A node in error is shown in RED.

And `netq help` shows you information about specific commands.

    cumulus@switch:~$ netq help show interfaces
    Commands:
       netq <hostname> show docker container adjacent [interfaces <remote-physical-interface>] [around <text-time>] [json]
       netq [<hostname>] show docker container name <container-name> adjacent [interfaces <remote-physical-interface>] [around <text-time>] [json]
       netq [<hostname>] show interfaces [around <text-time>] [count] [json]
       netq <hostname> show interfaces <remote-interface> [around <text-time>] [count] [json]
       netq [<hostname>] show interfaces type (bond|bridge|eth|loopback|macvlan|swp|vlan|vrf|vxlan) [around <text-time>] [count] [json]
       netq [<hostname>] show interfaces changes [between <text-time> and <text-endtime>] [json]
       netq <hostname> show interfaces <remote-interface> changes [between <text-time> and <text-endtime>] [json]
       netq [<hostname>] show interfaces type (bond|bridge|eth|loopback|macvlan|swp|vlan|vrf|vxlan) changes [between <text-time> and <text-endtime>] [json]

## Getting Information about Network Hardware</span>

You can get information about the hardware on the nodes in the network
with `netq show inventory` command. You can get details about the ASIC,
motherboard, CPU, license, memory, storage, operating system. To see a
shorter summary, use the `brief` option:

    netq@446c0319c06a:/$ netq show inventory brief 
    Node      Switch    OS             CPU     ASIC    Ports
    --------  --------  -------------  ------  ------  -------
    exit01    VX        Cumulus Linux  x86_64  N/A     N/A
    exit02    VX        Cumulus Linux  x86_64  N/A     N/A
    leaf01    VX        Cumulus Linux  x86_64  N/A     N/A
    leaf02    VX        Cumulus Linux  x86_64  N/A     N/A
    leaf03    VX        Cumulus Linux  x86_64  N/A     N/A
    leaf04    VX        Cumulus Linux  x86_64  N/A     N/A
    server01  N/A       Ubuntu         x86_64  N/A     N/A
    server02  N/A       Ubuntu         x86_64  N/A     N/A
    server03  N/A       Ubuntu         x86_64  N/A     N/A
    server04  N/A       Ubuntu         x86_64  N/A     N/A
    spine01   VX        Cumulus Linux  x86_64  N/A     N/A
    spine02   VX        Cumulus Linux  x86_64  N/A     N/A

## Using the NetQ Shell on the NetQ Telemetry Server</span>

If you need to run `netq` commands from the telemetry server, use the
NetQ shell. While most other Linux commands can work from this shell,
Cumulus Networks recommends you only run `netq` commands here.

    cumulus@netq-appliance:~$ netq-shell
    [<Container: a017716433>]
    Welcome to Cumulus (R) Linux (R)
     
    For support and online technical documentation, visit
    http://www.cumulusnetworks.com/support
     
    The registered trademark Linux (R) is used pursuant to a sublicense from LMI, the exclusive licensee of Linux Torvalds, owner of the mark on a worldwide basis. 
     
    TIP: Type `netq` to access NetQ CLI.
    netq@017716433d5:/$ netq show agents
    Node        Status    Sys Uptime    Agent Uptime
    ----------  --------  ------------  --------------
    exit01      Fresh     3h ago        3h ago
    exit02      Fresh     3h ago        3h ago
    leaf01      Fresh     3h ago        3h ago
    leaf02      Fresh     3h ago        3h ago
    server01    Fresh     3h ago        3h ago
    server02    Fresh     3h ago        3h ago
    server03    Fresh     3h ago        3h ago
    server04    Fresh     3h ago        3h ago
     
    ...

## Using the netq resolve Command</span>

Linux commands can be piped through NetQ with the `netq resolve`
command, in order to provide more contextual information and colored
highlights. For example, to show routes installed by the kernel, you
would run the `ip route show proto kernel` command:

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
    10.0.0.0/22 (    
    multiple:    
    ) dev eth0  scope link  src 10.0.0.165 (    
    cel-smallxp-13    
    :    
    eth0    
    ) 
    3.0.2.128/26 (     
    server02    
     :     
    torbond1.103    
     ) dev VlanA-1.103  scope link  src 3.0.2.131 (     
    leaf02    
     :     
    VlanA-1.103    
     )  
    3.0.2.128/26 (     
    server02    
     :     
    torbond1.103    
     ) dev VlanA-1-103-v0  scope link  src 3.0.2.129 (     
    leaf02    
     :     
    VlanA-1-103-v0    
     )  
    3.0.2.192/26 (     
    leaf02    
     :     
    VlanA-1-104-v0    
     ) dev VlanA-1.104  scope link  src 3.0.2.195 (     
    leaf02    
     :     
    VlanA-1.104    
     )  
    3.0.2.192/26 (     
    leaf02    
     :     
    VlanA-1-104-v0    
     ) dev VlanA-1-104-v0  scope link  src 3.0.2.193 (     
    leaf02    
     :     
    VlanA-1-104-v0    
     )  
    3.0.3.0/26 (     
    server01    
     :     
    torbond1.105    
     ) dev VlanA-1.105  scope link  src 3.0.3.3 (     
    leaf02    
     :     
    VlanA-1.105    
     )  
    3.0.3.0/26 (     
    server01    
     :     
    torbond1.105    
     ) dev VlanA-1-105-v0  scope link  src 3.0.3.1 (     
    leaf02    
     :     
    VlanA-1-105-v0    
     )  
    3.0.3.64/26 (     
    server02    
     :     
    torbond1.106    
     ) dev VlanA-1.106  scope link  src 3.0.3.67 (     
    leaf02    
     :     
    VlanA-1.106    
     )  
    3.0.3.64/26 (     
    server02    
     :     
    torbond1.106    
     ) dev VlanA-1-106-v0  scope link  src 3.0.3.65 (     
    leaf01    
     :     
    VlanA-1-106-v0    
     )  
    169.254.0.8/30 (     
    leaf02    
     :     
    peerlink-1.4094    
     ) dev peerlink-1.4094  scope link  src 169.254.0.10 (     
    leaf02    
     :     
    peerlink-1.4094    
     )  
    192.168.0.0/24 (     
    server02    
     :     
    eth0    
     ) dev eth0  scope link  src 192.168.0.15 (     
    leaf01    
     :     
    eth0    
     )

## Sample Commands for Various Components </span>

NetQ provides network validation for the entire stack, providing
algorithmic answers to many questions, both simple and intractable, that
pertain to your network fabric.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Component</p></th>
<th><p>Problem</p></th>
<th><p>Solution</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Host</p></td>
<td><p>Where is this container located?</p>
<p>Open ports? What image is being used?</p>
<p>Which containers are part of this service? How are they connected?</p></td>
<td><p>netq show docker container</p>
<p>netq show docker container service</p></td>
</tr>
<tr class="even">
<td><p>Overlay</p></td>
<td><p>Is my overlay configured correctly?</p>
<p>Can A reach B?</p>
<p>Is my control plane configured correctly?</p></td>
<td><p>netq check|show vxlan</p>
<p>netq check evpn|lnv</p>
<p>netq trace overlay</p></td>
</tr>
<tr class="odd">
<td><p>L3</p></td>
<td><p>Is OSPF working as expected?</p>
<p>Is BGP working as expected?</p>
<p>Can IP A reach IP B?</p></td>
<td><p>netq check|show ospf</p>
<p>netq check|show bgp</p>
<p>netq trace l3</p></td>
</tr>
<tr class="even">
<td><p>L2</p></td>
<td><p>Is MLAG configured correctly?</p>
<p>Is there an STP loop?</p>
<p>Is VLAN or MTU misconfigured?</p>
<p>How does MAC A reach B?</p></td>
<td><p>netq check|show clag</p>
<p>netq show stp</p>
<p>netq check|show vlan</p>
<p>netq check mtu</p>
<p>netq trace L2</p></td>
</tr>
<tr class="odd">
<td><p>OS</p></td>
<td><p>Are all switches licensed correctly?</p>
<p>Do all switches have NetQ agents running?</p></td>
<td><p>netq check license</p>
<p>netq check|show agents</p></td>
</tr>
<tr class="even">
<td><p>Interfaces</p></td>
<td><p>Is my link down? Are all bond links up?</p>
<p>What optics am I using? What's the peer for this port?</p>
<p>Which ports are empty? Is there a link mismatch? Are links flapping?</p></td>
<td><p>netq show|check interfaces</p></td>
</tr>
<tr class="odd">
<td><p>Hardware</p></td>
<td><p>Have any components crashed?</p>
<p>What switches do I have in the network?</p></td>
<td><p>netq check sensors</p>
<p>netq show sensors all</p>
<p>netq show inventory brief</p></td>
</tr>
</tbody>
</table>

## Understanding Timestamps in NetQ</span>

Every event or entry in the NetQ database is stored with a timestamp of
when the event was captured by the NetQ agent on the node. This
timestamp is based on time on the node where the agent is running, and
is pushed in UTC format. Thus, it is important to ensure that all nodes
are [NTP synchronized](/version/cumulus-netq-110/Proactively-Monitoring-the-Network-Fabric/).
Without this NTP sync, events may be displayed out of order or, worse,
not displayed when looking for events that occurred at a particular time
or within a time window.

Interface state, IP addresses, routes, ARP/ND table (IP neighbor)
entries and MAC table entries carry a timestamp that represents the time
the event happened (such as when a route is deleted or an interface
comes up) - *except* the first time the NetQ agent is run. If the
network has been running and stable when a NetQ agent is brought up for
the first time, then this time reflects when the agent was started.
Subsequent changes to these objects are captured with an accurate time
of when the event happened.

Data that is captured and saved based on polling, and just about all
other data in the NetQ database as of NetQ 1.1, including control plane
state (such as BGP or MLAG), has a timestamp of when the information was
*captured* rather than when the event *actually happened*, though NetQ
does try to compensate for it if the data extracted provides additional
information to compute a more precise time of the event; for example,
BGP uptime can be used to determine when the event actually happened in
conjunction with the timestamp.

When retrieving the timestamp, JSON output always returns the time in
microseconds since the epoch. Non-JSON output displays how long ago in
the past the event occurred. The closer the event is to the present, the
more granular is the time shown. For example, if an event happened less
than an hour ago, NetQ displays the information with a timestamp with
microseconds of granularity. However, the farther you are from the
event, this granularity is coarser. This is shown in the two outputs
below:

    cumulus@leaf01:mgmt-vrf:~$ netq leaf01 show interfaces swp51
    Matching link records are:
    Node             Interface        Type     State Details                     Last Changed
    ---------------- ---------------- -------- ----- --------------------------- --------------
    leaf01           swp51            swp      up    LLDP: spine01:swp1,         2h ago
                                                     MTU: 1500
     
    cumulus@leaf01:mgmt-vrf:~$ netq leaf01 show interfaces swp52
    Matching link records are:
    Node             Interface        Type     State Details                     Last Changed
    ---------------- ---------------- -------- ----- --------------------------- --------------
    leaf01           swp52            swp      up    LLDP: spine02:swp1,         2h ago
                                                     MTU: 1500

{{%notice note%}}

Remember that the time stored in the database is the one with
microseconds since the epoch and is what is returned (as a float) in the
JSON output.

{{%/notice%}}

One more important point to note. If a NetQ agent is restarted on a
node, it doesn't update all the timestamps for existing objects to this
new restart time. Those times are preserved to those at the agent's
original start time, unless the node is rebooted between the agent
stopping and restarting; in which case, the time is once again the time
of agent restart.

