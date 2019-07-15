---
title: Data Center Host to ToR Architecture
author: Cumulus Networks
weight: 249
aliases:
 - /display/DOCS/Data+Center+Host+to+ToR+Architecture
 - /pages/viewpage.action?pageId=8362991
pageID: 8362991
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
This chapter discusses the various architectures and strategies
available from the top of rack (ToR) switches all the way down to the
server hosts.

## <span>Layer 2 - Architecture</span>

### <span>Traditional Spanning Tree - Single Attached</span>

****

**{{% imgOld 0 %}}**

****

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Summary</p></th>
<th><p>More Information</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/cumulus-linux/Layer_2/Bonding_-_Link_Aggregation">Bond</a>/Etherchannel is not configured on host to multiple switches (bonds can still occur but only to one switch at a time), so leaf01 and leaf02 see two different MAC addresses.</p>
<p><strong>Configurations</strong></p>
<p><strong>leaf01 Config</strong></p>
<pre><code>auto bridge
iface bridge
  bridge-vlan-aware yes
  bridge-ports swp1 peerlink
  bridge-vids 1-2000
  bridge-stp on
 
auto bridge.10
iface bridge.10
  address 10.1.10.2/24
 
auto peerlink
iface peerlink
    bond-slaves glob swp49-50
 
auto swp1
iface swp1
  mstpctl-portadminedge yes
  mstpctl-bpduguard yes</code></pre>
<p><strong>Example Host Config (Ubuntu)</strong></p>
<pre><code>auto eth1
iface eth1 inet manual
 
auto eth1.10
iface eth1.10 inet manual
 
auto eth2
iface eth1 inet manual
 
auto eth2.20
iface eth2.20 inet manual
 
auto br-10
iface br-10 inet manual
  bridge-ports eth1.10 vnet0
 
auto br-20
iface br-20 inet manual
  bridge-ports eth2.20 vnet1</code></pre></td>
<td><p><strong>Benefits</strong></p>
<ul>
<li><p>Established technology</p>
<ul>
<li><p>Interoperability with other vendors</p></li>
<li><p>Easy configuration for customer</p></li>
<li><p>Immense documentation from multiple vendors and industry</p></li>
</ul></li>
<li><p>Ability to use <a href="/cumulus-linux/Layer_2/Spanning_Tree_and_Rapid_Spanning_Tree">spanning tree</a> commands</p>
<ul>
<li><p>mstpctl-portadminedge</p></li>
<li><p><a href="Spanning_Tree_and_Rapid_Spanning_Tree.html#src-8362689_SpanningTreeandRapidSpanningTree-bpdu">BPDU guard</a></p></li>
</ul></li>
<li><p>Layer 2 reachability to all VMs</p></li>
</ul>
<p><strong>Caveats</strong></p>
<ul>
<li><p>The load balancing mechanism on the host can cause problems. If there is only host pinning to each NIC, there are no problems, but if you are doing a bond, you need to look at an MLAG solution.</p></li>
<li><p>No active-active host links. Some operating systems allow HA (NIC failover), but this still does not utilize all the bandwidth. VMs are using one NIC, not two.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Active-Active Mode</strong></p></th>
<th><p><strong>Active-Passive Mode</strong></p></th>
<th><p><strong>L2 to L3 Demarcation</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>None (not possible with traditional spanning tree)</p></li>
</ul></td>
<td><ul>
<li><p><a href="/cumulus-linux/Layer_2/Virtual_Router_Redundancy_-_VRR_and_VRRP">VRR</a></p></li>
</ul>
<p><strong><br />
</strong></p></td>
<td><ul>
<li><p>ToR layer (recommended)</p></li>
<li><p>Spine layer</p></li>
<li><p>Core/edge/exit</p></li>
</ul>
More Info...
<p>VRR can be configured on a pair of switches at any level in the network. However, the higher up the network you configure it, the larger the L2 domain becomes. The benefit here is L2 reachability. The drawback is the L2 domain is more difficult to troubleshoot, does not scale as well, and the pair of switches running VRR needs to carry the entire MAC address table of everything below it in the network. Minimizing the L2 domain as much as possible is recommended by Cumulus Professional Services. <a href="https://docs.google.com/presentation/d/1l1d_6iUF7RTUHTSAmGuLwm3WCUXTNdFjndCLLxzBSOU/edit?usp=sharing" class="external-link">See this presentation for more information</a>.</p></td>
</tr>
</tbody>
</table>

### <span id="src-8362991_DataCenterHosttoToRArchitecture-mlag" class="confluence-anchor-link"></span><span>MLAG</span>

****

**{{% imgOld 1 %}}**

****

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Summary</p></th>
<th><p>More Information</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/cumulus-linux/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG">MLAG</a> (multi-chassis link aggregation) is when both uplinks are utilized at the same time. VRR gives the ability for both spines to act as gateways simultaneously for HA (high availability) and <a href="/cumulus-linux/Network_Virtualization/VXLAN_Active-Active_Mode">active-active mode</a> (both are being used at the same time).</p>
<p><strong>Configurations</strong></p>
<p><strong>leaf01 Config</strong></p>
<pre><code>auto bridge
iface bridge
  bridge-vlan-aware yes
  bridge-ports host-01 peerlink
  bridge-vids 1-2000
  bridge-stp on
 
auto bridge.10
iface bridge.10
  address 172.16.1.2/24
  address-virtual 44:38:39:00:00:10 172.16.1.1/24
 
auto peerlink
iface peerlink
    bond-slaves glob swp49-50
 
auto peerlink.4094
iface peerlink.4094
    address 169.254.1.2
    clagd-enable yes
    clagd-peer-ip 169.254.1.2
    clagd-system-mac 44:38:39:FF:40:94
 
auto host-01
iface host-01
  bond-slaves swp1
  clag-id 1
  {bond-defaults removed for brevity}</code></pre>
<p><strong>Example Host Config (Ubuntu)</strong></p>
<pre><code>auto bond0
iface bond0 inet manual
  bond-slaves eth0 eth1
  {bond-defaults removed for brevity}
 
auto bond0.10
iface bond0.10 inet manual
 
auto vm-br10
iface vm-br10 inet manual
  bridge-ports bond0.10 vnet0</code></pre></td>
<td><p><strong>Benefits</strong></p>
<ul>
<li><p>100% of links utilized</p></li>
</ul>
<p><strong>Caveats</strong></p>
<ul>
<li><p>More complicated (more moving parts)</p></li>
<li><p>More configuration</p></li>
<li><p>No interoperability between vendors</p></li>
<li><p>ISL (inter-switch link) required</p></li>
</ul>
<p><strong>Additional Comments</strong></p>
<ul>
<li><p>Can be done with either the <a href="/cumulus-linux/Layer_2/Ethernet_Bridging_-_VLANs/">traditional</a> or <a href="/cumulus-linux/Layer_2/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode">VLAN-aware</a> bridge driver depending on overall STP needs</p></li>
<li><p>There are a few different solutions including Cisco VPC and Arista MLAG, but none of them interoperate and are very vendor specific</p></li>
<li><p><a href="https://cumulusnetworks.com/media/resources/validated-design-guides/Cumulus-Linux-Layer-2-HA-Validated-Design-Guide_v1.0.0.pdf" class="external-link">Cumulus Networks Layer 2 HA validated design guide</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Active-Active Mode</strong></p></th>
<th><p><strong>Active-Passive Mode</strong></p></th>
<th><p><strong>L2-&gt;L3 Demarcation</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p><a href="/cumulus-linux/Layer_2/Virtual_Router_Redundancy_-_VRR_and_VRRP">VRR</a></p></li>
</ul></td>
<td><p>None</p></td>
<td><ul>
<li><p>ToR layer (recommended)</p></li>
<li><p>Spine layer</p></li>
<li><p>Core/edge/exit</p></li>
</ul></td>
</tr>
</tbody>
</table>

## <span>Layer 3 Architecture</span>

### <span>Single-attached Hosts</span>

{{% imgOld 2 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Summary</p></th>
<th><p>More Information</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The server (physical host) has only has one link to one ToR switch.</p>
<p><strong>Configurations</strong></p>
<p><strong>leaf01 Config</strong></p>
<p><code>/etc/network/interfaces</code></p>
<pre><code>auto swp1
iface swp1
  address 172.16.1.1/30</code></pre>
<p><code>/etc/frr/frr.conf</code></p>
<pre><code>router ospf
  router-id 10.0.0.11
interface swp1
  ip ospf area 0</code></pre>
<p><strong>leaf02 Config</strong></p>
<p><code>/etc/network/interfaces</code></p>
<pre><code>auto swp1
iface swp1
  address 172.16.2.1/30</code></pre>
<p><code>/etc/frr/frr.conf</code></p>
<pre><code>router ospf
  router-id 10.0.0.12
interface swp1
  ip ospf area 0</code></pre>
<p><strong>host1 Example Config (Ubuntu)</strong></p>
<pre><code>auto eth1
iface eth1 inet static
  address 172.16.1.2/30
  up ip route add 0.0.0.0/0 nexthop via 172.16.1.1</code></pre>
<p><strong>host2 Example Config (Ubuntu)</strong></p>
<pre><code>auto eth1
iface eth1 inet static
  address 172.16.2.2/30
  up ip route add 0.0.0.0/0 nexthop via 172.16.2.1</code></pre></td>
<td><p><strong><strong>Benefits</strong></strong></p>
<ul>
<li><p>Relatively simple network configuration</p></li>
<li><p>No STP</p></li>
<li><p>No MLAG</p></li>
<li><p>No L2 loops</p></li>
<li><p>No crosslink between leafs</p></li>
<li><p>Greater route scaling and flexibility</p></li>
</ul>
<p><strong><strong>Caveats</strong></strong></p>
<ul>
<li><p>No redundancy for ToR, upgrades would cause downtime</p></li>
<li><p>Many customers do not have software to support application layer redundancy</p></li>
</ul>
<p><strong>Additional Comments</strong></p>
<ul>
<li><p>For additional bandwidth links between host and leaf may be bonded</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>FHR (First Hop Redundancy)</strong></p></td>
<td><p><strong>More Information</strong></p></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>No redundancy, uses single ToR as gateway.</p></li>
</ul></td>
<td><ul>
<li><p><a href="https://cumulusnetworks.com/media/cumulus/pdf/technical/validated-design-guides/Big-Data-Cumulus-Linux-Validated-Design-Guide.pdf" class="external-link">Big Data validated design guide</a> uses single attached ToR</p></li>
</ul></td>
</tr>
</tbody>
</table>

### <span>Redistribute Neighbor</span>

{{% imgOld 3 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Summary</p></th>
<th><p>More Information</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://support.cumulusnetworks.com/hc/en-us/articles/204339077" class="external-link">Redistribute neighbor</a> daemon grabs ARP entries dynamically, utilizes redistribute table for FRRouting to grab these dynamic entries and redistribute them into the fabric.</p></td>
<td><p><strong>Benefits</strong></p>
<ul>
<li><p>Configuration in FRRouting is simple (route-map + redist table)</p></li>
<li><p>Supported by Cumulus Networks</p></li>
</ul>
<p><strong>Caveats</strong></p>
<ul>
<li><p>Silent hosts don't receive traffic (depending on ARP).</p></li>
<li><p>IPv4 only.</p></li>
<li><p>If two VMs are on same L2 domain, they could learn about each other directly rather than utilizing gateway, which causes problems (VM migration for example, or getting their network routed). Put hosts on /32 (no other L2 adjacency).</p></li>
<li><p>VM move does not trigger route withdrawal from original leaf (4 hour timeout).</p></li>
<li><p>Clearing ARP impacts routing. May not be obvious.</p></li>
<li><p>No L2 adjacency between servers without VXLAN.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>FHR (First Hop Redundancy)</strong></p></td>
<td><p><strong>More Information</strong></p></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Equal cost route installed on server/host/hypervisor to both ToRs to load balance evenly.</p></li>
<li><p>For host/VM/container mobility, use the same default route on all hosts (such as x.x.x.1) but don't distribute or advertise the .1 on the ToR into the fabric. This allows the VM to use the same gateway no matter which pair of leafs it is cabled to.</p></li>
</ul></td>
<td><ul>
<li><p><a href="https://cumulusnetworks.com/blog/introducing-rdnbr/" class="external-link">Cumulus Networks blog post introducing redistribute neighbor</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

### <span>Routing on the Host</span>

****

**{{% imgOld 4 %}}**

****

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Summary</p></th>
<th><p>More Information</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Routing on the host means there is a routing application (such as <a href="/cumulus-linux/Layer_3/FRRouting_Overview/">FRRouting</a>) either on the bare metal host (no VMs/containers) or the hypervisor (for example, Ubuntu with KVM). This is highly recommended by the Cumulus Networks Professional Services team.</p></td>
<td><p><strong>Benefits</strong></p>
<ul>
<li><p>No requirement for MLAG</p></li>
<li><p>No spanning-tree or layer 2 domain</p></li>
<li><p>No loops</p></li>
<li><p>3 or more ToRs can be used instead of usual 2</p></li>
<li><p>Host and VM mobility</p></li>
<li><p>Traffic engineering can be used to migrate traffic from one ToR to another for upgrading both hardware and software</p></li>
</ul>
<p><strong>Caveats</strong></p>
<ul>
<li><p>Certain hypervisors or host OSes might not support a routing application like FRRouting and will require a virtual router on the hypervisor</p></li>
<li><p>No L2 adjacnecy between servers without VXLAN</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>FHR (First Hop Redundancy)</strong></p></td>
<td><p><strong>More Information</strong></p></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>The first hop is still the ToR, just like redistribute neighbor</p></li>
<li><p>A default route can be advertised by all leaf/ToRs for dynamic ECMP paths</p></li>
</ul></td>
<td><ul>
<li><p><a href="https://support.cumulusnetworks.com/hc/en-us/articles/213177027-Installing-the-Cumulus-Linux-Quagga-Package-on-an-Ubuntu-Server" class="external-link">Installing the Cumulus Linux FRRouting Package on an Ubuntu Server</a></p></li>
<li><p><a href="/cumulus-linux/Layer_3/Configuring_FRRouting/">Configuring FRRouting</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

### <span>Routing on the VM</span>

{{% imgOld 5 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Summary</p></th>
<th><p>More Information</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Instead of routing on the hypervisor, each virtual machine utilizes its own routing stack.</p></td>
<td><p><strong>Benefits</strong></p>
<ul>
<li><p>In addition to routing on host:</p>
<ul>
<li><p>Hypervisor/base OS does not need to be able to do routing</p></li>
<li><p>VMs can be authenticated into routing fabric</p></li>
</ul></li>
</ul>
<p><strong><strong>Caveats</strong></strong></p>
<ul>
<li><p>All VMs must be capable of routing</p></li>
<li><p>Scale considerations might need to be taken into an account —<br />
instead of one routing process, there are as many as there are VMs</p></li>
<li><p>No L2 adjacency between servers without VXLAN</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>FHR (First Hop Redundancy)</strong></p></td>
<td><p><strong>More Information</strong></p></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>The first hop is still the ToR, just like redistribute neighbor</p></li>
<li><p>Multiple ToRs (2+) can be used</p></li>
</ul></td>
<td><ul>
<li><p><a href="https://support.cumulusnetworks.com/hc/en-us/articles/213177027-Installing-the-Cumulus-Linux-Quagga-Package-on-an-Ubuntu-Server" class="external-link">Installing the Cumulus Linux FRRouting Package on an Ubuntu Server</a></p></li>
<li><p><a href="/cumulus-linux/Layer_3/Configuring_FRRouting/">Configuring FRRouting</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

### <span>Virtual Router</span>

{{% imgOld 6 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Summary</p></th>
<th><p>More Information</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Virtual router (vRouter) runs as a VM on the hypervisor/host, sends routes to the ToR using <a href="#src-8362991" class="unresolved">BGP</a> or <a href="/cumulus-linux/Layer_3/Open_Shortest_Path_First_-_OSPF">OSPF</a>.</p></td>
<td><p><strong><strong>Benefits</strong></strong></p>
<p>In addition to routing on a host:</p>
<ul>
<li><p>Multi-tenancy can work (multiple customers sharing same racks)</p></li>
<li><p>Base OS does not need to be routing capable</p></li>
</ul>
<p><strong><strong>Caveats</strong></strong></p>
<ul>
<li><p><a href="/cumulus-linux/Layer_3/Equal_Cost_Multipath_Load_Sharing_-_Hardware_ECMP">ECMP</a> might not work correctly (load balancing to multiple ToRs); Linux kernel in older versions is not capable of ECMP per flow (does it per packet)</p></li>
<li><p>No L2 adjacency between servers without VXLAN</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>FHR (First Hop Redundancy)</strong></p></td>
<td><p><strong>More Information</strong></p></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>The gateway would be the vRouter, which has two routes out (two ToRs)</p></li>
<li><p>Multiple vRouters could be used</p></li>
</ul></td>
<td><ul>
<li><p><a href="https://support.cumulusnetworks.com/hc/en-us/articles/213177027-Installing-the-Cumulus-Linux-Quagga-Package-on-an-Ubuntu-Server" class="external-link">Installing the Cumulus Linux FRRouting Package on an Ubuntu Server</a></p></li>
<li><p><a href="/cumulus-linux/Layer_3/Configuring_FRRouting/">Configuring FRRouting</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

### <span>Anycast with Manual Redistribution</span>

{{% imgOld 7 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Summary</p></th>
<th><p>More Information</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>In contrast to routing on the host (preferred), this method allows a user to route <strong>to</strong> the host. The ToRs are the gateway, as with redistribute neighbor, except because there is no daemon running, the networks must be manually configured under the routing process. There is a potential to black hole unless a script is run to remove the routes when the host no longer responds.</p>
<p><strong>Configurations</strong></p>
<p><strong>leaf01 Config</strong></p>
<p><code>/etc/network/interfaces</code></p>
<pre><code>auto swp1
iface swp1
  address 172.16.1.1/30</code></pre>
<p><code>/etc/frr/frr.conf</code></p>
<pre><code>router ospf
  router-id 10.0.0.11
interface swp1
  ip ospf area 0</code></pre>
<p><strong>leaf02 Config</strong></p>
<p><code>/etc/network/interfaces</code></p>
<pre><code>auto swp2
iface swp2
  address 172.16.1.1/30</code></pre>
<p><code>/etc/frr/frr.conf</code></p>
<pre><code>router ospf
  router-id 10.0.0.12
interface swp1
  ip ospf area 0</code></pre>
<p><strong>Example Host Config (Ubuntu)</strong></p>
<pre><code>auto lo
iface lo inet loopback
 
auto lo:1
iface lo:1 inet static
  address 172.16.1.2/32
  up ip route add 0.0.0.0/0 nexthop via 172.16.1.1 dev eth0 onlink nexthop via 172.16.1.1 dev eth1 onlink
 
auto eth1
iface eth2 inet static
  address 172.16.1.2/32
 
auto eth2
iface eth2 inet static
  address 172.16.1.2/32</code></pre></td>
<td><p><strong><strong>Benefits</strong></strong></p>
<ul>
<li><p>Most benefits of routing <strong>on</strong> the host</p></li>
<li><p>No requirement for host to run routing</p></li>
<li><p>No requirement for redistribute neighbor</p></li>
</ul>
<p><strong><strong>Caveats</strong></strong></p>
<ul>
<li><p>Removing a subnet from one ToR and re-adding it to another (hence, network statements from your router process) is a manual process</p></li>
<li><p>Network team and server team would have to be in sync, or server team controls the ToR, or automation is being used whenever VM migration happens</p></li>
<li><p>When using VMs/containers it is very easy to black hole traffic, as the leafs continue to advertise prefixes even when VM is down</p></li>
<li><p>No L2 adjacency between servers without VXLAN</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>FHR (First Hop Redundancy)</strong></p></td>
<td><p><strong>More Information</strong></p></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>The gateways would be the ToRs, exactly like redistribute neighbor with an equal cost route installed</p></li>
</ul></td>
<td><p> </p></td>
</tr>
</tbody>
</table>

## <span>Network Virtualization</span>

**LNV with MLAG**

{{% imgOld 8 %}}

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p> </p></th>
<th><p>Summary</p></th>
<th><p>More Information</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p> </p></td>
<td><p>The host runs LACP (Etherchannel/bond) to the pair of ToRs. <a href="/cumulus-linux/Network_Virtualization/Lightweight_Network_Virtualization_Overview/">LNV</a> (Lightweight Network Virtualization) then transports the L2 bridges across an L3 fabric.</p>
<p><strong>Configurations</strong></p>
<p><strong>leaf01 Config</strong></p>
<p><code>/etc/network/interfaces</code></p>
<pre><code>auto lo
iface lo inet loopback 
  address 10.0.0.11/32
  vxrd-src-ip 10.0.0.11
  vxrd-svcnode-ip 10.10.10.10
  clagd-vxlan-anycast-ip 36.0.0.11
 
auto vni-10
iface vni-10 
  vxlan-id 10 
  vxlan-local-tunnelip 10.0.0.11
 
auto br-10 
iface br-10
  bridge-ports swp1 vni-10</code></pre>
<p><strong>leaf02 Config</strong></p>
<p><code>/etc/network/interfaces</code></p>
<pre><code>auto lo
iface lo inet loopback 
  address 10.0.0.12/32
  Vxrd-src-ip 10.0.0.12
  vxrd-svcnode-ip 10.10.10.10
  clagd-vxlan-anycast-ip 36.0.0.11
 
auto vni-10
iface vni-10 
  vxlan-id 10 
  vxlan-local-tunnelip 10.0.0.12
 
auto br-10 
iface br-10
  bridge-ports swp1 vni-10</code></pre></td>
<td><p><strong><strong>Benefits</strong></strong></p>
<ul>
<li><p>Layer 2 domain is reduced to the pair of ToRs</p></li>
<li><p>Aggregation layer is all L3 (VLANs do not have to exist on spine switches)</p></li>
<li><p>Greater route scaling and flexibility</p></li>
<li><p>High availability</p></li>
</ul>
<p><strong><strong>Caveats</strong></strong></p>
<ul>
<li><p>Needs MLAG (with the same caveats from the <a href="#src-8362991_DataCenterHosttoToRArchitecture-mlag">MLAG section</a> above) and <a href="/cumulus-linux/Layer_2/Spanning_Tree_and_Rapid_Spanning_Tree">spanning tree</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Active-Active Mode</strong></p></th>
<th><p><strong>Active-Passive Mode</strong></p></th>
<th><p><strong>Demarcation</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p><a href="/cumulus-linux/Layer_2/Virtual_Router_Redundancy_-_VRR_and_VRRP">VRR</a></p></li>
</ul></td>
<td><p>None</p></td>
<td><ul>
<li><p>ToR layer or exit leafs</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><p> </p></td>
<td><p><strong>More Information</strong></p></td>
</tr>
<tr class="odd">
<td><p> </p></td>
<td><p> </p></td>
<td><ul>
<li><p><a href="/cumulus-linux/Network_Virtualization/Lightweight_Network_Virtualization_Overview/">Cumulus Linux Lightweight Network Virtualization (LNV) documentation</a></p></li>
</ul></td>
</tr>
</tbody>
</table>
