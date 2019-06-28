---
title: Cumulus Linux Quagga Commands
author: Cumulus Networks
weight: 305
aliases:
 - /display/CL31/Cumulus+Linux+Quagga+Commands
 - /pages/viewpage.action?pageId=5122124
pageID: 5122124
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
Using the `vtysh` modal CLI is the primary way to [configure
Quagga](/version/cumulus-linux-312/Layer_3_Features/Configuring_Quagga/)
in Cumulus Linux. However, an alternative exists in the form of a
non-modal CLI containing a suite of Cumulus Linux-specific commands,
structured similar to the Linux `ip` command. The available commands are
as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Command</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>cl-bgp</p></td>
<td><p><a href="/version/cumulus-linux-312/Layer_3_Features/Border_Gateway_Protocol_-_BGP">BGP</a> commands. See <code>man cl-bgp</code> for details.</p></td>
</tr>
<tr class="even">
<td><p>cl-ospf</p></td>
<td><p><a href="/version/cumulus-linux-312/Layer_3_Features/Open_Shortest_Path_First_-_OSPF_-_Protocol">OSPFv2</a> commands. For example:<br />
<code>cumulus@switch:~$ sudo cl-ospf area 0.0.0.1 range 10.10.10.0/24</code></p></td>
</tr>
<tr class="odd">
<td><p>cl-ospf6</p></td>
<td><p><a href="/version/cumulus-linux-312/Layer_3_Features/Open_Shortest_Path_First_v3_-_OSPFv3_-_Protocol">OSPFv3</a> commands.</p></td>
</tr>
<tr class="even">
<td><p>cl-ra</p></td>
<td><p>Route advertisement commands. See <code>man cl-ra</code> for details.</p></td>
</tr>
<tr class="odd">
<td><p>cl-rctl</p></td>
<td><p>Zebra and non-routing protocol-specific commands. See <code>man cl-rctl</code> for details.</p></td>
</tr>
</tbody>
</table>

## <span>Comparing vtysh and Cumulus Linux Commands</span>

The following table compares the various Quagga commands with their
Cumulus Linux CLI counterparts.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Action</p></th>
<th><p>Quagga Commands</p></th>
<th><p>Cumulus Linux Commands</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Display the routing table</p></td>
<td><pre><code>switch# show ip route</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-rctl route</code></pre></td>
</tr>
<tr class="even">
<td><p>Create a new neighbor</p></td>
<td><pre><code>switch(config)# router bgp 65002
switch(config-router)# neighbor 14.0.0.22</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-bgp as 65002 neighbor add 14.0.0.22</code></pre></td>
</tr>
<tr class="odd">
<td><p>Redistribute routing information from static route entries into RIP tables</p></td>
<td><pre><code>switch(config)# router bgp 65002
switch(config-router)# redistribute static</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-bgp as 65002 redistribute add static</code></pre></td>
</tr>
<tr class="even">
<td><p>Define a static route</p>
<p>{{%notice note%}}</p>
<p>If you intend to use static routes, you only need to enable the <code>zebra</code> daemon.</p>
<p>{{%/notice%}}</p></td>
<td><pre><code>switch(config)# ip route 155.1.2.20/24 br2 45</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-rctl ip route add 175.0.0.0/28 interface br1 distance 25</code></pre></td>
</tr>
<tr class="odd">
<td><p>Configure an IPv6 address</p></td>
<td><pre><code>switch(config)# int br3
switch(config-if)# ipv6 address  3002:2123:1234:1abc::21/64</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-rctl interface add swp3 ipv6 address 3002:2123:abcd:2120::41/64</code></pre></td>
</tr>
<tr class="even">
<td><p>Enable topology checking (<a href="/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Prescriptive_Topology_Manager_-_PTM">PTM</a>)</p></td>
<td><pre><code>switch(config)# ptm-enable</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-rctl ptm-enable set</code></pre></td>
</tr>
<tr class="odd">
<td><p>Configure <a href="Layer_1_and_Switch_Port_Attributes.html#src-5122107_Layer1andSwitchPortAttributes-mtu">MTU</a> in IPv6 network discovery for an interface</p></td>
<td><pre><code>switch(config)# int swp3
switch(config-if)# ipv6 nd mtu 9000</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-ra interface swp3 set mtu 9000</code></pre></td>
</tr>
<tr class="even">
<td><p>Set the OSPF interface priority</p></td>
<td><pre><code>switch(config)# int swp3
switch(config-if)# ip ospf priority  120</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-ospf interface set swp3 priority 120</code></pre></td>
</tr>
<tr class="odd">
<td><p>Configure timing for OSPF SPF calculations</p></td>
<td><pre><code>switch(config)# router ospf6
switch(config-ospf6)# timer throttle spf 40 50 60</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-ospf6 timer add throttle spf 40 50 60</code></pre></td>
</tr>
<tr class="even">
<td><p>Configure the OSPF Hello packet interval in number of seconds for an interface</p></td>
<td><pre><code>switch(config)# int swp4
switch(config-if)# ipv6 ospf6 hello-interval  60 </code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-ospf6 interface set swp4 hello-interval 60</code></pre></td>
</tr>
<tr class="odd">
<td><p>Display OSPF debugging status</p></td>
<td><pre><code>switch# show debugging ospf</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-ospf debug show</code></pre></td>
</tr>
<tr class="even">
<td><p>Display <a href="/version/cumulus-linux-312/Layer_3_Features/Border_Gateway_Protocol_-_BGP">BGP</a> information</p></td>
<td><pre><code>switch# show ip bgp summary</code></pre></td>
<td><pre><code>cumulus@switch:~$ sudo cl-bgp summary </code></pre></td>
</tr>
</tbody>
</table>
