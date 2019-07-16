---
title: Data Center Host to ToR Architecture
author: Cumulus Networks
weight: 253
aliases:
 - /display/CL40/Data-Center-Host-to-ToR-Architecture
 - /pages/viewpage.action?pageId=8366715
pageID: 8366715
product: Cumulus Linux
version: '4.0'
imgData: cumulus-linux-40
siteSlug: cumulus-linux-40
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
<td><details>
<p><a href="/version/cumulus-linux-40/Layer-2/Bonding---Link-Aggregation">Bond</a>/Etherchannel is not configured on host to multiple switches (bonds can still occur but only to one switch at a time), so leaf01 and leaf02 see two different MAC addresses.</p>
<p><strong>Configurations</strong></p>
<summary>leaf01 configuration </summary>
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
<summary>Example Ubuntu host configuration </summary>
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
  bridge-ports eth2.20 vnet1</code></pre>
</details></td>
<td><p><strong>Benefits</strong></p>
<ul>
<li><p>Established technology</p>
<ul>
<li><p>Interoperability with other vendors</p></li>
<li><p>Easy configuration for customer</p></li>
<li><p>Immense documentation from multiple vendors and industry</p></li>
</ul></li>
<li><p>Ability to use <a href="/version/cumulus-linux-40/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree">spanning tree</a> commands</p>
<ul>
<li><p>mstpctl-portadminedge</p></li>
<li><p><a href="Spanning-Tree-and-Rapid-Spanning-Tree.html#src-8366412_SpanningTreeandRapidSpanningTree-bpdu">BPDU guard</a></p></li>
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
<li><p><a href="/version/cumulus-linux-40/Layer-2/Virtual-Router-Redundancy---VRR-and-VRRP">VRR</a></p></li>
</ul>
<p><strong><br />
</strong></p></td>
<td><details>
<ul>
<li><p>ToR layer (recommended)</p></li>
<li><p>Spine layer</p></li>
<li><p>Core/edge/exit</p></li>
</ul>
<summary>More Info... </summary>
<p>VRR can be configured on a pair of switches at any level in the network. However, the higher up the network you configure it, the larger the L2 domain becomes. The benefit here is L2 reachability. The drawback is the L2 domain is more difficult to troubleshoot, does not scale as well, and the pair of switches running VRR needs to carry the entire MAC address table of everything below it in the network. Minimizing the L2 domain as much as possible is recommended by Cumulus Professional Services. <a href="https://docs.google.com/presentation/d/1l1d_6iUF7RTUHTSAmGuLwm3WCUXTNdFjndCLLxzBSOU/edit?usp=sharing" class="external-link">See this presentation for more information</a>.</p>
</details></td>
</tr>
</tbody>
</table>

### <span id="src-8366715_DataCenterHosttoToRArchitecture-mlag" class="confluence-anchor-link"></span><span>MLAG</span>

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
<td><details>
<p><a href="/version/cumulus-linux-40/Layer-2/Multi-Chassis-Link-Aggregation---MLAG">MLAG</a> (multi-chassis link aggregation) is when both uplinks are utilized at the same time. VRR gives the ability for both spines to act as gateways simultaneously for HA (high availability) and <a href="/version/cumulus-linux-40/Network-Virtualization/VXLAN-Active-Active-Mode">active-active mode</a> (both are being used at the same time).</p>
<p><strong>Configurations</strong></p>
<summary>leaf01 configuration </summary>
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
<summary>Example Ubuntu host configuration </summary>
<pre><code>auto bond0
iface bond0 inet manual
  bond-slaves eth0 eth1
  {bond-defaults removed for brevity}
 
auto bond0.10
iface bond0.10 inet manual
 
auto vm-br10
iface vm-br10 inet manual
  bridge-ports bond0.10 vnet0</code></pre>
</details></td>
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
<li><p>Can be done with either the <a href="/version/cumulus-linux-40/Layer-2/Ethernet-Bridging---VLANs/">traditional</a> or <a href="/version/cumulus-linux-40/Layer-2/Ethernet-Bridging---VLANs/VLAN-aware-Bridge-Mode">VLAN-aware</a> bridge driver depending on overall STP needs</p></li>
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
<li><p><a href="/version/cumulus-linux-40/Layer-2/Virtual-Router-Redundancy---VRR-and-VRRP">VRR</a></p></li>
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
<td><p>Routing on the host means there is a routing application (such as <a href="/version/cumulus-linux-40/Layer-3/FRRouting-Overview/">FRRouting</a>) either on the bare metal host (no VMs/containers) or the hypervisor (for example, Ubuntu with KVM). This is highly recommended by the Cumulus Networks Professional Services team.</p></td>
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
<li><p><a href="/version/cumulus-linux-40/Layer-3/Configuring-FRRouting/">Configuring FRRouting</a></p></li>
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
<li><p><a href="/version/cumulus-linux-40/Layer-3/Configuring-FRRouting/">Configuring FRRouting</a></p></li>
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
<td><p>Virtual router (vRouter) runs as a VM on the hypervisor/host, sends routes to the ToR using <a href="/version/cumulus-linux-40/Layer-3/Border-Gateway-Protocol---BGP">BGP</a> or <a href="/version/cumulus-linux-40/Layer-3/Open-Shortest-Path-First---OSPF">OSPF</a>.</p></td>
<td><p><strong><strong>Benefits</strong></strong></p>
<p>In addition to routing on a host:</p>
<ul>
<li><p>Multi-tenancy can work (multiple customers sharing same racks)</p></li>
<li><p>Base OS does not need to be routing capable</p></li>
</ul>
<p><strong><strong>Caveats</strong></strong></p>
<ul>
<li><p><a href="/version/cumulus-linux-40/Layer-3/Equal-Cost-Multipath-Load-Sharing---Hardware-ECMP">ECMP</a> might not work correctly (load balancing to multiple ToRs); Linux kernel in older versions is not capable of ECMP per flow (does it per packet)</p></li>
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
<li><p><a href="/version/cumulus-linux-40/Layer-3/Configuring-FRRouting/">Configuring FRRouting</a></p></li>
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
<td><details>
<p>In contrast to routing on the host (preferred), this method allows a user to route <strong>to</strong> the host. The ToRs are the gateway, as with redistribute neighbor, except because there is no daemon running, the networks must be manually configured under the routing process. There is a potential to black hole unless a script is run to remove the routes when the host no longer responds.</p>
<p><strong>Configurations</strong></p>
<summary>leaf01 configurations </summary>
<p>/etc/network/interfaces</p>
<pre><code>auto swp1
iface swp1
  address 172.16.1.1/30</code></pre>
<p><code>/etc/frr/frr.conf</code></p>
<pre><code>router ospf
  router-id 10.0.0.11
interface swp1
  ip ospf area 0</code></pre>
<summary>leaf02 configurations </summary>
<p><code>/etc/network/interfaces</code></p>
<pre><code>auto swp2
iface swp2
  address 172.16.1.1/30</code></pre>
<p><code>/etc/frr/frr.conf</code></p>
<pre><code>router ospf
  router-id 10.0.0.12
interface swp1
  ip ospf area 0</code></pre>
<summary>Example Ubuntu host configuration </summary>
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
  address 172.16.1.2/32</code></pre>
</details></td>
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

## <span>Network Virtualization: EVPN with Symmetric VXLAN Routing</span>

****

**{{% imgOld 8 %}}**

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
<td><details>
<p><a href="/version/cumulus-linux-40/Network-Virtualization/VXLAN-Routing">Symmetric VXLAN routing</a> is configured directly on the ToR, using <a href="/version/cumulus-linux-40/Network-Virtualization/Ethernet-Virtual-Private-Network---EVPN">EVPN</a> for both VLAN and VXLAN bridging as well as VXLAN and external routing.</p>
<p>Each server is configured on a VLAN, with a total of two VLANs for the setup. MLAG is also set up between servers and the leafs. Each leaf is configured with an anycast gateway, and the servers default gateways are pointing towards the corresponding leaf switch IP gateway address. Two tenant VNIs (corresponding to two VLANs/VXLANs) are bridged to corresponding VLANs.</p>
<p><strong>Configurations</strong></p>
<summary>Leaf01 /etc/network/interfaces </summary>
<pre><code># Loopback interface
auto lo
iface lo inet loopback
  address 10.0.0.11/32
  clagd-vxlan-anycast-ip 10.0.0.112
  alias loopback interface
 
# Management interface
 auto eth0
 iface eth0 inet dhcp
    vrf mgmt
 
auto mgmt
iface mgmt
    address 127.0.0.1/8
    vrf-table auto
 
# Port to Server01
auto swp1
iface swp1
  alias to Server01
  # This is required for Vagrant only
  post-up ip link set swp1 promisc on
 
# Port to Server02
auto swp2
iface swp2
  alias to Server02
  # This is required for Vagrant only
  post-up ip link set swp2 promisc on
 
# Port to Leaf02
auto swp49
iface swp49
  alias to Leaf02
  # This is required for Vagrant only
  post-up ip link set swp49 promisc on
 
# Port to Leaf02
auto swp50
iface swp50
  alias to Leaf02
  # This is required for Vagrant only
  post-up ip link set swp50 promisc on
 
# Port to Spine01
auto swp51
iface swp51
  mtu 9216
  alias to Spine01
 
# Port to Spine02
auto swp52
iface swp52
  mtu 9216
  alias to Spine02
 
# MLAG Peerlink bond
auto peerlink
iface peerlink
  mtu 9000
  bond-slaves swp49 swp50
 
# MLAG Peerlink L2 interface.
# This creates VLAN 4094 that only lives on the peerlink bond
# No other interface will be aware of VLAN 4094
auto peerlink.4094
iface peerlink.4094
  address 169.254.1.1/30
  clagd-peer-ip 169.254.1.2
  clagd-backup-ip 10.0.0.12
  clagd-sys-mac 44:39:39:ff:40:94
  clagd-priority 100
 
# Bond to Server01
auto bond01
iface bond01
  mtu 9000
  bond-slaves swp1
  bridge-access 13
  clag-id 1
 
# Bond to Server02
auto bond02
iface bond02
  mtu 9000
  bond-slaves swp2
  bridge-access 24
  clag-id 2
 
# Define the bridge for STP
auto bridge
iface bridge
  bridge-vlan-aware yes
  # bridge-ports includes all ports related to VxLAN and CLAG.
  # does not include the Peerlink.4094 subinterface
  bridge-ports bond01 bond02 peerlink vni13 vni24 vxlan4001
  bridge-vids 13 24
  bridge-pvid 1
 
# VXLAN Tunnel for Server1-Server3 (Vlan 13)
auto vni13
iface vni13
  mtu 9000
  vxlan-id 13
  vxlan-local-tunnelip 10.0.0.11
  bridge-access 13
  bridge-learning off
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
 
#VXLAN Tunnel for Server2-Server4 (Vlan 24)
auto vni24
iface vni24
  mtu 9000
  vxlan-id 24
  vxlan-local-tunnelip 10.0.0.11
  bridge-access 24
  bridge-learning off
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
  bridge-arp-nd-suppress on
 
auto vxlan4001
iface vxlan4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.11
    bridge-learning off
    bridge-access 4001
 
auto vrf1
iface vrf1
   vrf-table auto
 
#Tenant SVIs - anycast GW
auto vlan13
iface vlan13
    address 10.1.3.11/24
    address-virtual 44:39:39:ff:00:13 10.1.3.1/24
    vlan-id 13
    vlan-raw-device bridge
    vrf vrf1
 
auto vlan24
iface vlan24
    address 10.2.4.11/24
    address-virtual 44:39:39:ff:00:24 10.2.4.1/24
    vlan-id 24
    vlan-raw-device bridge
    vrf vrf1
 
#L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    hwaddress 44:39:39:FF:40:94
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1</code></pre>
<summary>Server01 /etc/network/interfaces </summary>
<pre><code>auto lo
iface lo inet loopback
 
auto eth0
iface eth0 inet dhcp
 
auto eth1
iface eth1 inet manual
  bond-master uplink
  # Required for Vagrant
  post-up ip link set promisc on dev eth1
 
auto eth2
iface eth2 inet manual
  bond-master uplink
  # Required for Vagrant
  post-up ip link set promisc on dev eth2
 
auto uplink
iface uplink inet static
  mtu 9000
  bond-slaves none
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  address 10.1.3.101
  netmask 255.255.255.0
  post-up ip route add default via 10.1.3.1</code></pre>
<summary>Leaf02 /etc/network/interfaces </summary>
<pre><code># Loopback interface
auto lo
iface lo inet loopback
  address 10.0.0.12/32
  clagd-vxlan-anycast-ip 10.0.0.112
  alias loopback interface
 
# Management interface
auto eth0
iface eth0 inet dhcp
    vrf mgmt
 
auto mgmt
iface mgmt
    address 127.0.0.1/8
    vrf-table auto
 
# Port to Server01
auto swp1
iface swp1
  alias to Server01
  # This is required for Vagrant only
  post-up ip link set swp1 promisc on
 
# Port to Server02
auto swp2
iface swp2
  alias to Server02
  # This is required for Vagrant only
  post-up ip link set swp2 promisc on
 
# Port to Leaf01
auto swp49
iface swp49
  alias to Leaf01
  # This is required for Vagrant only
  post-up ip link set swp49 promisc on
 
# Port to Leaf01
auto swp50
iface swp50
  alias to Leaf01
  # This is required for Vagrant only
  post-up ip link set swp50 promisc on
 
# Port to Spine01
auto swp51
iface swp51
  mtu 9216
  alias to Spine01
 
# Port to Spine02
auto swp52
iface swp52
  mtu 9216
  alias to Spine02
 
# MLAG Peerlink bond
auto peerlink
iface peerlink
  mtu 9000
  bond-slaves swp49 swp50
 
# MLAG Peerlink L2 interface.
# This creates VLAN 4094 that only lives on the peerlink bond
# No other interface will be aware of VLAN 4094
auto peerlink.4094
iface peerlink.4094
  address 169.254.1.2/30
  clagd-peer-ip 169.254.1.1
  clagd-backup-ip 10.0.0.11
  clagd-sys-mac 44:39:39:ff:40:94
  clagd-priority 200
 
# Bond to Server01
auto bond01
iface bond01
  mtu 9000
  bond-slaves swp1
  bridge-access 13
  clag-id 1
 
# Bond to Server02
auto bond02
iface bond02
  mtu 9000
  bond-slaves swp2
  bridge-access 24
  clag-id 2
 
# Define the bridge for STP
auto bridge
iface bridge
  bridge-vlan-aware yes
  # bridge-ports includes all ports related to VxLAN and CLAG.
  # does not include the Peerlink.4094 subinterface
  bridge-ports bond01 bond02 peerlink vni13 vni24 vxlan4001
  bridge-vids 13 24
  bridge-pvid 1
 
auto vxlan4001
iface vxlan4001
     vxlan-id 104001
     vxlan-local-tunnelip 10.0.0.12
     bridge-learning off
     bridge-access 4001
 
# VXLAN Tunnel for Server1-Server3 (Vlan 13)
auto vni13
iface vni13
  mtu 9000
  vxlan-id 13
  vxlan-local-tunnelip 10.0.0.12
  bridge-access 13
  bridge-learning off
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
 
#VXLAN Tunnel for Server2-Server4 (Vlan 24)
auto vni24
iface vni24
  mtu 9000
  vxlan-id 24
  vxlan-local-tunnelip 10.0.0.12
  bridge-access 24
  bridge-learning off
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
  bridge-arp-nd-suppress on
 
auto vrf1
iface vrf1
   vrf-table auto
 
auto vlan13
iface vlan13
    address 10.1.3.12/24
    address-virtual 44:39:39:ff:00:13 10.1.3.1/24
    vlan-id 13
    vlan-raw-device bridge
    vrf vrf1
 
auto vlan24
iface vlan24
    address 10.2.4.12/24
    address-virtual 44:39:39:ff:00:24 10.2.4.1/24
    vlan-id 24
    vlan-raw-device bridge
    vrf vrf1
 
#L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    hwaddress 44:39:39:FF:40:94
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1</code></pre>
<summary>Server01 /etc/network/interfaces </summary>
<pre><code>auto lo
iface lo inet loopback
 
auto eth0
iface eth0 inet dhcp
 
auto eth1
iface eth1 inet manual
  bond-master uplink
  # Required for Vagrant
  post-up ip link set promisc on dev eth1
 
auto eth2
iface eth2 inet manual
  bond-master uplink
  # Required for Vagrant
  post-up ip link set promisc on dev eth2
 
auto uplink
iface uplink inet static
  mtu 9000
  bond-slaves none
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  address 10.1.3.101
  netmask 255.255.255.0
  post-up ip route add default via 10.1.3.1</code></pre>
<summary>Server02 /etc/network/interfaces </summary>
<pre><code>auto lo
iface lo inet loopback
 
auto eth0
iface eth0 inet dhcp
 
auto eth1
iface eth1 inet manual
  bond-master uplink
  # Required for Vagrant
  post-up ip link set promisc on dev eth1
 
auto eth2
iface eth2 inet manual
  bond-master uplink
  # Required for Vagrant
  post-up ip link set promisc on dev eth2
 
auto uplink
iface uplink inet static
  mtu 9000
  bond-slaves none
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  address 10.2.4.102
  netmask 255.255.255.0
  post-up ip route add default via 10.2.4.1 </code></pre>
</details></td>
<td><p><strong><strong>Benefits</strong></strong></p>
<ul>
<li><p>Layer 2 domain is reduced to the pair of ToRs</p></li>
<li><p>Aggregation layer is all L3 (VLANs do not have to exist on spine switches)</p></li>
<li><p>Greater route scaling and flexibility</p></li>
<li><p>High availability</p></li>
</ul>
<p><strong><strong>Caveats</strong></strong></p>
<ul>
<li><p>Needs MLAG (with the same caveats from the <a href="#src-8366715_DataCenterHosttoToRArchitecture-mlag">MLAG section</a> above)</p></li>
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
<li><p><a href="/version/cumulus-linux-40/Layer-2/Virtual-Router-Redundancy---VRR-and-VRRP">VRR</a></p></li>
</ul></td>
<td><p>None</p></td>
<td><ul>
<li><p>ToR layer</p></li>
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
<li><p><a href="https://github.com/CumulusNetworks/cldemo-evpn-symmetric" class="external-link">Cumulus Networks EVPN with symmetric routing demo on GitHub</a></p></li>
<li><p><a href="/version/cumulus-linux-40/Network-Virtualization/Ethernet-Virtual-Private-Network---EVPN">Ethernet Virtual Private Network - EVPN</a></p></li>
<li><p><a href="/version/cumulus-linux-40/Network-Virtualization/VXLAN-Routing">VXLAN Routing</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
