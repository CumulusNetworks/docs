---
title: Getting to Know NetQ
author: Cumulus Networks
weight: 13
aliases:
 - /display/NETQ10/Getting+to+Know+NetQ
 - /pages/viewpage.action?pageId=6488226
pageID: 6488226
product: Cumulus NetQ
version: 1.0.0
imgData: cumulus-netq-10
siteSlug: cumulus-netq-10
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

## <span>Getting Information about Network Hardware</span>

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

## <span>Using the NetQ Shell on the NetQ Telemetry Server</span>

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

## <span>Using the netq resolve Command</span>

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

<div class="confbox panel">

<div class="panel-content">

    cumulus@leaf01:~$ ip route show proto kernel | netq resolve
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

</div>

</div>

## <span>Sample Commands for Various Components </span>

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
<p>Open ports? What image is being used?</p></td>
<td><p>netq show docker container</p></td>
</tr>
<tr class="even">
<td><p>Overlay</p></td>
<td><p>Is my overlay configured correctly?</p>
<p>Can A reach B?</p></td>
<td><p>netq check vxlan</p>
<p>netq check lnv</p>
<p>netq trace</p></td>
</tr>
<tr class="odd">
<td><p>L3</p></td>
<td><p>Is OSPF working as expected?</p>
<p>Is BGP working as expected?</p>
<p>Can IP A reach IP B?</p></td>
<td><p>netq check ospf</p>
<p>netq check/show bgp</p>
<p>netq trace l3</p></td>
</tr>
<tr class="even">
<td><p>L2</p></td>
<td><p>Is MLAG configured correctly?</p>
<p>Is there a STP loop?</p>
<p>Is VLAN or MTU misconfigured?</p>
<p>How does MAC A reach B?</p></td>
<td><p>netq check clag</p>
<p>netq show clag</p>
<p>netq show stp topology</p>
<p>netq check vlan</p>
<p>netq check mtu</p>
<p>netq trace L2</p></td>
</tr>
<tr class="odd">
<td><p>OS</p></td>
<td><p>Are all switches licensed correctly?</p>
<p>Do all switches have NetQ agents running?</p></td>
<td><p>netq check license</p>
<p>netq check agents</p>
<p>netq show agents</p></td>
</tr>
<tr class="even">
<td><p>Interfaces</p></td>
<td><p>Is my link down? Are all bond links up?</p></td>
<td><p>netq show interfaces</p>
<p>netq show interfaces type bond</p></td>
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

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

<script src="js/lunr.js"></script>

<script src="js/lunr-extras.js"></script>

<script src="assets/js/scroll-search.js"></script>
