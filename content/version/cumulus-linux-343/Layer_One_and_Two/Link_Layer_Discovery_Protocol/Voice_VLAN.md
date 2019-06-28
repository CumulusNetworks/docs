---
title: Voice VLAN
author: Cumulus Networks
weight: 311
aliases:
 - /display/CL34/Voice+VLAN
 - /pages/viewpage.action?pageId=7112405
pageID: 7112405
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
In Cumulus Linux, a *voice VLAN* is a VLAN dedicated to voice traffic on
a switch. However, the term can mean different things to different
vendors.

## <span>Cumulus Linux Voice VLAN Example</span>

{{% imgOld 0 %}}

You can configure the topology above using the following
[NCLU](/version/cumulus-linux-343/System_Configuration/Network_Command_Line_Utility_-_NCLU)
commands:

    cumulus@switch:~$ net add bridge bridge ports swp1-3
    cumulus@switch:~$ net add bridge bridge vids 1-1000
    cumulus@switch:~$ net add bridge bridge pvid 1
    cumulus@switch:~$ net add interface swp1-2 bridge vids 200
    cumulus@switch:~$ net add interface swp1-2 bridge pvid 100
    cumulus@switch:~$ net add interface swp1-2 stp bpduguard
    cumulus@switch:~$ net add interface swp1-2 stp portadminedge
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in the
`/etc/network/interfaces` file:

    auto bridge
    iface bridge
      bridge-ports swp1 swp2 swp3
      bridge-pvid 1
      bridge-vids 1-1000
      bridge-vlan-aware yes
     
    auto swp1
    iface swp1
       bridge-pvid 100
       bridge-vids 200
       mstpctl-bpduguard yes
       mstpctl-portadminedge yes
     
    auto swp2
    iface swp2
       bridge-pvid 100
       bridge-vids 200
       mstpctl-bpduguard yes
       mstpctl-portadminedge yes

The `bridge-vids` can be reviewed with the `net show bridge vlan`
command:

    cumulus@ig-spine-01:~$ net show bridge vlan
     
    Interface    VLAN      Flags
    -----------  --------  ---------------------
    swp1         100       PVID, Egress Untagged
                 200
     
    swp2         100       PVID, Egress Untagged
                 200
     
    swp3         1         PVID, Egress Untagged
                 2-1000

## <span>Cumulus Linux vs Cisco IOS Configuration</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Cumulus Linux <code>/etc/network/interfaces</code></p></th>
<th><p>Cisco IOS</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>auto swp1
iface swp1
   bridge-vids 200
   bridge-pvid 100
   mstpctl-bpduguard yes
   mstpctl-portadminedge yes</code></pre></td>
<td><pre><code>interface FastEthernet0/1
  switchport access vlan 100
  switchport voice vlan 200
  spanning-tree portfast
  spanning-tree bpduguard enable</code></pre></td>
</tr>
</tbody>
</table>

## <span>Cisco Voice VLAN and 802.1q Trunk Differences</span>

On Cisco Systems' Catalyst software, when a switch port is configured as
an access port (switchport mode access), and has a voice VLAN configured
on that switch port, the switch port behaves identically to a 802.1q
trunk. This means that the untagged VLAN is configured for the personal
computer (PC), and the tagged VLAN is configured for the voice over IP
(VoIP) handset, effectively configuring the switch port as a trunk with
2 VLANs (one tagged and one untagged).

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Behavior</p></th>
<th><p>Cumulus Linux Trunk</p></th>
<th><p>Cisco Voice VLAN</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CoS &amp; 802.1p</p></td>
<td><ul>
<li><p>CoS value is trusted on tagged and untagged packets.</p></li>
<li><p>As IP Phone overrides the priority, according to Cisco documentation, the behavior should be identical.</p></li>
</ul></td>
<td><ul>
<li><p>All untagged traffic is sent according to the default CoS priority of the port.</p></li>
<li><p>The default CoS value is 0 for incoming traffic.</p></li>
<li><p>The CoS value is not trusted for 802.1P or 802.1Q tagged traffic.</p></li>
<li><p>The IP Phone overrides the priority of all incoming traffic (tagged and untagged) and sets the CoS value to 0.</p></li>
</ul>
<p><a href="http://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2940/software/release/12-1_19_ea1/configuration/guide/2940scg_1/swvoip.html#wp1030860" class="external-link">Source</a></p></td>
</tr>
<tr class="even">
<td><p>Portfast</p></td>
<td><ul>
<li><p>If portfast behavior is desired, <code>mstpctl-portadminedge</code> must be enabled.</p></li>
</ul></td>
<td><ul>
<li><p>The Port Fast feature is automatically enabled when voice VLAN is configured. When you disable voice VLAN, the Port Fast feature is not automatically disabled.</p></li>
</ul>
<p><a href="http://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2940/software/release/12-1_19_ea1/configuration/guide/2940scg_1/swvoip.html#wp1030860" class="external-link">Source</a></p></td>
</tr>
<tr class="odd">
<td><p>Trust CoS on Phone</p></td>
<td><ul>
<li><p>Must be configured on Phone or Call Manager (or Call Manager equivalent).</p></li>
<li><p>Cumulus Linux trusts COS values by default (unless configured not to).</p></li>
</ul></td>
<td><ul>
<li><p>Use the command <code>switchport priority extend trust</code>.</p></li>
</ul>
<p><a href="http://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2940/software/release/12-1_19_ea1/configuration/guide/2940scg_1/swvoip.html#wp1030860" class="external-link">Source</a></p></td>
</tr>
<tr class="even">
<td><p>Automatic Detection</p></td>
<td><ul>
<li><p>Not available as of 11/22/2016 as this is proprietary to Cisco Systems. Please <a href="mailto:support@cumulusnetworks.com" class="external-link">contact support</a> if this is a required feature.</p></li>
</ul></td>
<td><ul>
<li><p>Use the command <code>switchport voice detect cisco-phone full-duplex</code>.</p></li>
</ul>
<p><a href="http://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/12-2_55_se/configuration/guide/3750xscg/swvoip.html" class="external-link">Source</a></p></td>
</tr>
</tbody>
</table>
