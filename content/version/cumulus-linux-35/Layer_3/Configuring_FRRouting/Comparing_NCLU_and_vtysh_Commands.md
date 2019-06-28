---
title: Comparing NCLU and vtysh Commands
author: Cumulus Networks
weight: 411
aliases:
 - /display/CL35/Comparing+NCLU+and+vtysh+Commands
 - /pages/viewpage.action?pageId=8357716
pageID: 8357716
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
Using
[NCLU](/version/cumulus-linux-35/System_Configuration/Network_Command_Line_Utility_-_NCLU/)
is the primary way to [configure
routing](/version/cumulus-linux-35/Layer_3/Configuring_FRRouting/) in
Cumulus Linux. However, an alternative exists in the the `vtysh` modal
CLI. The available commands are as follows:

## <span>Comparing vtysh and NCLU Commands</span>

The following table compares the various FRRouting commands with their
Cumulus Linux NCLU counterparts.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Action</p></th>
<th><p>NCLU Commands</p></th>
<th><p>FRRouting Commands</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Display the routing table</p></td>
<td><pre><code>cumulus@switch:~$ net show route</code></pre></td>
<td><pre><code>switch# show ip route</code></pre></td>
</tr>
<tr class="even">
<td><p>Create a new neighbor</p></td>
<td><pre><code>cumulus@switch:~$ net add bgp autonomous-system 65002
cumulus@switch:~$ net add bgp neighbor 14.0.0.22</code></pre></td>
<td><pre><code>switch(config)# router bgp 65002
switch(config-router)# neighbor 14.0.0.22</code></pre></td>
</tr>
<tr class="odd">
<td><p>Redistribute routing information from static route entries into RIP tables</p></td>
<td><pre><code>cumulus@switch:~$ net add bgp redistribute static</code></pre></td>
<td><pre><code>switch(config)# router bgp 65002
switch(config-router)# redistribute static</code></pre></td>
</tr>
<tr class="even">
<td><p>Define a <a href="/version/cumulus-linux-35/Layer_3/Routing">static route</a></p></td>
<td><pre><code>cumulus@switch:~$ net add routing route 155.1.2.20/24 bridge 45
 </code></pre></td>
<td><pre><code>switch(config)# ip route 155.1.2.20/24 bridge 45</code></pre></td>
</tr>
<tr class="odd">
<td><p>Configure an IPv6 address</p></td>
<td><pre><code>cumulus@switch:~$ net add interface swp3 ipv6 address 3002:2123:1234:1abc::21/64</code></pre></td>
<td><pre><code>switch(config)# int swp3
switch(config-if)# ipv6 address 3002:2123:1234:1abc::21/64</code></pre></td>
</tr>
<tr class="even">
<td><p>Enable topology checking (<a href="/version/cumulus-linux-35/Layer_1_and_2/Prescriptive_Topology_Manager_-_PTM">PTM</a>)</p></td>
<td><pre><code>cumulus@switch:~$ net add routing ptm-enable</code></pre></td>
<td><pre><code>switch(config)# ptm-enable</code></pre></td>
</tr>
<tr class="odd">
<td><p>Configure <a href="Layer_1_and_Switch_Port_Attributes.html#src-8357670_Layer1andSwitchPortAttributes-mtu">MTU</a> in IPv6 network discovery for an interface</p></td>
<td><pre><code>cumulus@switch:~$ sudo cl-ra interface swp3 set mtu 9000</code></pre></td>
<td><pre><code>switch(config)# int swp3
switch(config-if)# ipv6 nd mtu 9000</code></pre></td>
</tr>
<tr class="even">
<td><p>Set the OSPF interface priority</p></td>
<td><pre><code>cumulus@switch:~$ net add interface swp3 ospf6 priority 120</code></pre></td>
<td><pre><code>switch(config)# int swp3
switch(config-if)# ip ospf6 priority  120</code></pre></td>
</tr>
<tr class="odd">
<td><p>Configure timing for OSPF SPF calculations</p></td>
<td><pre><code>cumulus@switch:~$ net add ospf6 timers throttle spf 40 50 60</code></pre></td>
<td><pre><code>switch(config)# router ospf6
switch(config-ospf6)# timer throttle spf 40 50 60</code></pre></td>
</tr>
<tr class="even">
<td><p>Configure the OSPF Hello packet interval in number of seconds for an interface</p></td>
<td><pre><code>cumulus@switch:~$ net add interface swp4 ospf6 hello-interval 60</code></pre></td>
<td><pre><code>switch(config)# int swp4
switch(config-if)# ipv6 ospf6 hello-interval  60 </code></pre></td>
</tr>
<tr class="odd">
<td><p>Display <a href="/version/cumulus-linux-35/Layer_3/Border_Gateway_Protocol_-_BGP">BGP</a> information</p></td>
<td><pre><code>cumulus@switch:~$ net show bgp summary</code></pre></td>
<td><pre><code>switch# show ip bgp summary</code></pre></td>
</tr>
<tr class="even">
<td><p>Display OSPF debugging status</p></td>
<td><pre><code>cumulus@switch:~$ net show debugs</code></pre></td>
<td><pre><code>switch# show debugging ospf</code></pre></td>
</tr>
</tbody>
</table>
