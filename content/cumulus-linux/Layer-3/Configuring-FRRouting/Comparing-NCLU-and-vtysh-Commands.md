---
title: Comparing NCLU and vtysh Commands
author: Cumulus Networks
weight: 419397
aliases:
 - /display/CL3740/Comparing-NCLU-and-vtysh-Commands
 - /pages/viewpage.action?pageId=83629206644
pageID: 83629206644
product: Cumulus Linux
version: 3.7.7'4.0'
imgData: cumulus-linux-37740
siteSlug: cumulus-linux-37740
---
Using
[NCLU](/version/cumulus-linux-37740/System-Configuration/Network-Command-Line-Utility---NCLU)
is the primaryrecommended way to [configure
routing](/version/cumulus-linux-37740/Layer-3/Configuring-FRRouting/) in
Cumulus Linux. H; however, an alternative exists in thyou can use the `vtysh` modal
 CLI. The available commands are as follows:

The following table compares the variousshows the FRRouting commands with theirand the equivalent
Cumulus Linux NCLU counterpartmmands.

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
<td><p>Define a <a href="/version/cumulus-linux-37740/Layer-3/Routing">static route</a></p></td>
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
<td><p>Enable topology checking (<a href="/version/cumulus-linux-37740/Layer-1-and-Switch-Ports/Prescriptive-Topology-Manager---PTM">PTM</a>)</p></td>
<td><pre><code>cumulus@switch:~$ net add routing ptm-enable</code></pre></td>
<td><pre><code>switch(config)# ptm-enable</code></pre></td>
</tr>
<tr class="odd">
<td><p>Configure <a href="Switch-Port-Attributes.html#src-83630266750_SwitchPortAttributes-mtu">MTU</a> in IPv6 network discovery for an interface</p></td>
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
<td><p>Display <a href="/version/cumulus-linux-37740/Layer-3/Border-Gateway-Protocol---BGP">BGP</a> information</p></td>
<td><pre><code>cumulus@switch:~$ net show bgp summary</code></pre></td>
<td><pre><code>switch# show ip bgp summary</code></pre></td>
</tr>
<tr class="even">
<td><p>Display OSPF debugging status</p></td>
<td><pre><code>cumulus@switch:~$ net show debugs</code></pre></td>
<td><pre><code>switch# show debugging ospf</code></pre></td>
</tr>
<tr class="odd">
<td><p>Show information about the interfaces on the switch</p></td>
<td><pre><code>cumulus@switch:~$ net show interface</code></pre></td>
<td><pre><code>switch# show interface</code></pre>
<p>To quickly check important information, such as IP address, VRF, and operational status, in easy to read tabular format:</p>
<pre><code>switch# show interface brief</code></pre></td>
</tr>
</tbody>
</table>

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg5NDQzNDQwNV19
-->