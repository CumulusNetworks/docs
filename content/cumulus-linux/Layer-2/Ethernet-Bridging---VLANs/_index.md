---
title: Ethernet Bridging - VLANs
author: Cumulus Networks
weight: 121
aliases:
 - /display/CL3740/Ethernet-Bridging---VLANs
 - /pages/viewpage.action?pageId=83626556378
pageID: 83626556378
product: Cumulus Linux
version: 3.7.7'4.0'
imgData: cumulus-linux-37740
siteSlug: cumulus-linux-37740
---
<details>

Ethernet bridges provide a means forenable hosts to communicate through layer
2, 2 by 
connecting all of the physical and logical interfaces in the
 system into 
a single layer 2 domain. The bridge is a logical interface
 with a MAC 
address and an
[MTU](Switch-Port-Attributes.html#src-83630266750_SwitchPortAttributes-mtu)
(maximum transmission unit). The bridge MTU is the minimum MTU among all
its members. By default, the [bridge's MAC
address](https://support.cumulusnetworks.com/hc/en-us/articles/360005695794)
is the MAC address of the first port in the `bridge-ports` list. The
bridge can also be assigned an IP address, as discussed
[below](#src-83626556378_EthernetBridging-VLANs-svi).

{{%notice note%}}

Bridge members can be individual physical interfaces, bonds, or logical
interfaces that traverse an 802.1Q VLAN trunk.

{{%/notice%}}

{{% imgOld 0 %}}

{{%notice tip%}}

Cumulus Networks recommends using *[VLAN-aware
mode](/version/cumulus-linux-37740/Layer-2/Ethernet-Bridging---VLANs/VLAN-aware-Bridge-Mode)*
bridges, rather than instead of *traditional mode* bridges. The bridge driver in
Cumulus Linux is capable of VLAN filtering, which allows for
configurations that are similar to incumbent network devices. While
Cumulus Linux supports Ethernet bridges in traditional mode, Cumulus
Networks **** recommends using VLAN-aware mode.

{{%/notice%}}

{{%notice info%}}

For a 
comparison of traditional and VLAN-aware modes, read [this
 knowledge 
base
article](https://support.cumulusnetworks.com/hc/en-us/articles/204909397).

{{%/notice%}}

{{%notice note%}}

**Notes**

  - Cumulus Linux does not put all ports into a bridge by default.

{{%/notice%}}

{{%notice tip%}}

  - You can configure both VLAN-aware and traditional mode bridges on
    the
 same network in Cumulus Linux; however you cannot have more than
    one
 VLAN-aware bridge on a given switch.

{{%/notice%}}

## <span>Create a VLAN-aware Bridge</span>

To learn aboutcreate a VLAN-aware bridges and how to configure them, read
, see [VLAN-aware Bridge
Mode](/version/cumulus-linux-37740/Layer-2/Ethernet-Bridging---VLANs/VLAN-aware-Bridge-Mode).

## <span>Create a Traditional Mode Bridge</span>

To create a traditional mode bridge, see [Traditional Bridge
Mode](/version/cumulus-linux-37740/Layer-2/Ethernet-Bridging---VLANs/Traditional-Bridge-Mode).

## <span>Configure Bridge MAC Addresses</span>

The MAC address for a frame is learned when the frame enters the bridge
viathrough an interface. The MAC address is recorded in the bridge table, 
and
 the bridge forwards the frame to its intended destination by looking 
up
 the destination MAC address. The MAC entry is then maintained for a
period of time defined by the `bridge-ageing` configuration option. If
the frame is seen with the same source MAC address before the MAC entry
age is exceeded, the MAC entry age is refreshed; if the MAC entry age is
exceeded, the MAC address is deleted from the bridge table.

The following example output shows a MAC address table for the bridge:

    cumulus@switch:~$ net show bridge macs 
    VLAN      Master    Interface    MAC                  TunnelDest  State      Flags    LastSeen
    --------  --------  -----------  -----------------  ------------  ---------  -------  -----------------
    untagged  bridge    swp1         44:38:39:00:00:03                                    00:00:15
    untagged  bridge    swp1         44:38:39:00:00:04                permanent           20 days, 01:14:03

## <span id="src-83626556378_EthernetBridging-VLANs-mac_ageing" class="confluence-anchor-link"></span><span>MAC Address Ageing</span>

></span>By 
default, Cumulus Linux stores MAC addresses in the Ethernet switching
table for 1800 seconds (30 minutes). You canTo change this setting using
NCLU.e amount of time MAC
addresses are stored in the table, configure *bridge ageing*.

{{%notice note%}}

The `bridge- ageing` option is in the [NCLU
blacklist](Network-Command-Line-Utility---NCLU.html#src-83625806301_NetworkCommandLineUtility-NCLU-conf),
as it's not frequently used. To configur.
If you want to change this setting, you need to
 first remove the 
`bridge-ageing` keyword from the `ifupdown_blacklist` insection of the
`/etc/netd.conf`. file, then [Rrestart the `netd`
service](Network-Command-Line-Utility---NCLU.html#src-83625806301_NetworkCommandLineUtility-NCLU-restart)
after you edit the file.

Now you can change the setting using NCLU. For example, to change the
sett.

{{%/notice%}}

To configure bridge ageing:

<summary>NCLU Commands </summary>

Run the `net add bridge bridge ageing` command. The following example
commands set MAC address ageing to 600 seconds, run:

    cumulus@switch:~$ net add bridge bridge ageing 600
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in<summary>Linux Commands </summary>

Edit the
 `/etc/network/interfaces` file: and add `bridge-ageing` to the
bridge stanza. The following example sets MAC address ageing to 600
seconds.

    cumulus@switch:~$ catsudo nano /etc/network/interfaces
      
    ...
     
    auto bridge
    iface bridge
        bridge-ageing 600
     
    ...

Run the `ifreload -a` command to load the new configuration:

    cumulus@switch:~$ ifreload -a

## <span id="src-83626556378_EthernetBridging-VLANs-svi" class="confluence-anchor-link"></span><span>Configure an SVI (Switch VLAN Interface)</span>

Bridges can be included as part of a routing topology after being
assigned an<span style="color: #333333;">
routing topology after </span> <span style="color: #333333;"> being
assigned an </span> <span style="color: #333333;"> IP address. This 
enables hosts within the bridge to
 communicate with other hosts outside 
of the bridge, via a through a </span> *switch VLAN
 interface*
<span style="color: #333333;"> (SVI), which provides layer 3 routing. 
The IP address of the
 bridge is typically from the same subnet as the bridge's 
member hosts. of the bridge. </span>

{{%notice note%}}

When you add an interface is added to a bridge, it ceases to function as a
 router 
interface, and the IP address on the interface, if any, becomes
 unreachable.

{{%/notice%}}

To configure the SVI, use
[NCLU](/version/cumulus-linux-377/System-Configuration/Network-Command-Line-Utility---NCLU)::

<summary>NCLU Commands </summary>

Run the `net add bridge` and `net add vlan` commands. The following
example commands configure an SVI using swp1 and swp2, and VLAN ID 10.

    cumulus@switch:~$ net add bridge bridge ports swp1-2
    cumulus@switch:~$ net add vlan 10 ip address 10.100.100.1/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following SVI configuration in<summary>Linux Commands </summary>

Edit the
 `/etc/network/interfaces` file:

    auto bridge
    iface bridge
        bridge-ports swp1 swp2
        bridge-vids 10
        bridge-vlan-aware yes
     
    auto vlan10
    iface vlan10
        address 10.100.100.1/24
        vlan-id 10
        vlan-raw-devic to add the interfaces and VLAN
ID you want to use. The following configures an SVI using swp1 and swp2,
and VLAN ID 10. The `bridge

{{%notice tip%}}

Notice the `-vlan-raw-device` keyword, which NCLU includes automatically.
NCLU uses this keyword toare` parameter associates the SVI 
with the VLAN-aware bridge.

{{%/notice%}}

Alternately, you can use the *bridge.VLAN-ID* naming convention for the
SVI. The following example configuration can be manually created in the
`/etc/network/interfaces` file, which functions identically to the above
configuration:
    cumulus@switch:~$ sudo nano /etc/network/interfaces
     
    ...
    auto bridge
    iface bridge
        bridge-ports swp1 swp2
        bridge-vids 10
        bridge-vlan-aware yes
      
    auto bridge.10
    iface bridge.10
        address 10.100.100.1/24

When a switch is initially configured     
    ...

Run the `ifreload -a` command to load the new configuration:

    cumulus@switch:~$ ifreload -a

When you configure a switch initially, all southbound bridge ports mayight
be down, which means that; therefore, by default, the SVI is also down. However,
you may want toYou can force the 
SVI to always be up, to perform connectivity
testing, for example. To do this, you essentially need to disable
 by disabling interface state tracking, leaving which leaves
the SVI in the UP state always, even
 if all member ports are down. Other 
implementations describe this
 feature as *no autostate*.

In Cumulus Linux, you can This is
beneficial if you want to perform connectivity testing.

To keep the SVI perpetually UP by, creatinge a
 dummy interface, andthen makinge the 
dummy interface a member of the bridge.

<summary>Example Configuration </summary>

Consider the following configuration, without a dummy interface in the
bridge:

    cumulus@switch:~$ sudo cat /etc/network/interfaces
    ...
      
    auto bridge
    iface bridge
        bridge-vlan-aware yes
        bridge-ports swp3
        bridge-vids 100
        bridge-pvid 1
      
    ...

With this configuration, when swp3 is down, the SVI is also down:

    cumulus@switch:~$ ip link show swp3
    5: swp3: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master bridge state DOWN mode DEFAULT group default qlen 1000
        link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
    cumulus@switch:~$ ip link show bridge
    35: bridge: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
        link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff

Now add the dummy interface to your network configuration:

1.  Create a dummy interface, and add it to the bridge configuration.
    You do this by editingEdit the `/etc/network/interfaces` file and adding
    the dummy interface
    stanza before the bridge stanza:
    
        cumulus@switch:~$ sudo nano /etc/network/interfaces
        ...
          
        auto dummy
        iface dummy
            link-type dummy
          
        auto bridge
        iface bridge
        ...

2.  Continue editing the `interfaces` file. Add the dummy interface to
    the `bridge-ports` line in the bridge
    configuration:
    
        auto bridge
        iface bridge
            bridge-vlan-aware yes
            bridge-ports swp3 dummy
            bridge-vids 100
            bridge-pvid 1

3.  Save and exit the file, then reload the configuration:
    
        cumulus@switch:~$ sudo ifreload -a

Now, even when swp3 is down, both the dummy interface and the bridge
remain up:

    cumulus@switch:~$ ip link show swp3
    5: swp3: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master bridge state DOWN mode DEFAULT group default qlen 1000
        link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
    cumulus@switch:~$ ip link show dummy
    37: dummy: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue master bridge state UNKNOWN mode DEFAULT group default
        link/ether 66:dc:92:d4:f3:68 brd ff:ff:ff:ff:ff:ff
    cumulus@switch:~$ ip link show bridge
    35: bridge: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default
        link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff

## <span>IPv6 Link-local Address Generation</span>

By default, Cumulus Linux automatically generates IPv6 [link-local
addresses](https://en.wikipedia.org/wiki/Link-local_address) on VLAN
interfaces. If you want to use a different mechanism to assign
link-local addresses, you shouldcan disable this feature. You can disable
link-local automatic address generation for both regular IPv6 addresses
and address-virtual (macvlan) addresses.

To disable automatic address generation for a regular IPv6 address on a
VLAN 100, run:

    cumulus@switch:~$ net add vlan 100 ipv6-addrgen off
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file::

<summary>NCLU Commands </summary>

Run the `net add vlan <vlan> ipv6-addrgen off` command. The following
example command disables automatic address generation for a regular IPv6
address on a VLAN 100.

    cumulus@switch:~$ net add vlan 100 ipv6-addrgen off
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file and add the line `ipv6-addrgen
off` to the VLAN stanza. The following example disables automatic
address generation for a regular IPv6 address on VLAN 100.

    cumulus@switch:~$ catsudo nano /etc/network/interfaces
     
    ...
     
    auto vlan100
    iface vlan 100
        ipv6-addrgen off
        vlan-id 100
        vlan-raw-device bridge
     
    ...

To disRun the `ifreload -a` command to load the new configuration:

    cumulus@switch:~$ ifreload -a

To re-enable automatic link-local address generation for a virtual VLAN:

<summary>NCLU Commands </summary>

Run the `net del vlan <vlan> ipv6-addrgen off` command. The following
example command re-enables automatic address generation for a regular
IPv6 address on
 VLAN 100, run:.

    cumulus@switch:~$ net adddel vlan 100 address-virtual-ipv6-addrgen off
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in<summary>Linux Commands </summary>

1.  Edit the
 `/etc/network/interfaces` file:

    cumulus@switch:~$ cat /etc/network/interfaces
     
    ...
     
    auto vlan100
    iface vlan 100
        address-virtual-ipv6-addrgen off
        vlan-id 100
        vlan-raw-device bridge
     
    ...

To and **remove** the line
    `ipv6-addrgen off` from the VLAN stanza. The following example
    re-enables automatic link-local address generation, run:

    cumulus@switch:~$ net del vlan 100 ip for a regular IPv6- addrgen off
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

or

    cumulus@switch:~$ net del vlan 100 address-virtual-ipv6-addrgen off
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This removes the relevant configuration from the `interfaces` file.

## <span>Understanding \`ess
    on a VLAN 100.

2.  Run the `ifreload -a` command to load the new configuration:
    
        cumulus@switch:~$ ifreload -a

## <span id="src-8366378_EthernetBridging-VLANs-fdb" class="confluence-anchor-link"></span><span>bridge fdb\` Command Output</span>

The `bridge fdb` command in Linux interacts with the forwarding database
table (FDB), which the bridge uses to store the MAC addresses it has learned and
s
and the ports on which ports it learneds those MAC addresses. The `bridge fdb 
show`
 command output contains some specific keywords that require further
explanation:

  - **self**: t:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Keyword</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>self</strong></p></td>
<td><p>The Linux kernel FDB entry flag that indicatinges the FDB entry
    belongs to the FDB on the device referenced by the device.  
    <br />
For example, this FDB entry belongs to the VXLAN device vx-1000:  
    `"<br />
<code>00:02:00:00:00:08 dev vx-1000 dst 27.0.0.10 self"`

  - **master**: t</code></p></td>
</tr>
<tr class="even">
<td><p><strong>master</strong></p></td>
<td><p>The Linux kernel FDB entry flag that indicatinges the FDB entry
    belongs to the FDB on the device's master, and the FDB entry is
    pointing to a master's port.  
    <br />
For example, this FDB entry is from the master device named *<em>bridge*
   </em> and is pointing to the VXLAN bridge port vx-1001:  
    `<br />
<code>02:02:00:00:00:08 dev vx-1001 vlan 1001 master bridge`

  - **offload**: t</code></p></td>
</tr>
<tr class="odd">
<td><p><strong>offload</strong></p></td>
<td><p>The Linux kernel FDB entry flag that indicatinges the FDB
    entry is managed (or offloaded) by an external control plane — for
    example,, such as the BGP control plane for EVPN.

Consider the following output of</p></td>
</tr>
</tbody>
</table>

The following example shows the `bridge fdb show` command output:

    cumulus@switch:~$ bridge fdb show | grep 02:02:00:00:00:08
    02:02:00:00:00:08 dev vx-1001 vlan 1001 offload master bridge 
    02:02:00:00:00:08 dev vx-1001 dst 27.0.0.10 self offload

Some things you should note about the output:{{%notice note%}}

  - *02:02:00:00:00:08* is the MAC address learned viawith BGP EVPN.

  - The first FDB entry points to a Linux bridge entry pointing to the
   that points to
    the VXLAN device *vx-1001*.

  - The second FDB entry points to the same entry on the VXLAN device
    withand includes additional remote destination information.

  - The VXLAN FDB augments the bridge FDB with additional remote
    destination information.

  - All FDB entries that pointing to a VXLAN port appear as two such entries.
    with tThe second entry augmentings the remote destination information.

{{%/notice%}}

## <span>Caveats and Errata</span>

  - A bridge cannot contain multiple subinterfaces of the **same** port.
    Attempting this configuration results in an error.

  - In environments where both VLAN-aware and traditional bridges are in
    used, if a traditional bridge has a subinterface of a bond that is a
    normal interface in a VLAN-aware bridge, the bridge is flapped when
    the traditional bridge's bond subinterface is brought down.

  - You cannot enslave a VLAN raw device to a different master interface
    (that is, you cannot edit the `vlan-raw-device` setting in the
    `/etc/network/interfaces` file). You need to delete the VLAN and
    recreate it again.

  - On a Mellanox platformswitch, Cumulus Linux supports up to 2000 VLANs.
    This
    includes the internal interfaces, bridge interfaces, logical
    interfaces, and so forthon.

  - In Cumulus Linux, MAC learning is enabled by default on traditional
    or VLAN-aware bridge interfaces. Cumulus Networks recommends you do
    not disable MAC learning unless you are using EVPN. See [Ethernet
    Virtual Private Network -
    EVPN](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=8366455Ethernet-Virtual-Private-Network---EVPN.html#src-8366455_EthernetVirtualPrivateNetwork-EVPN-DisableDataPlaneMACLearningoverVXLANTunnels).

## <span>Related Information</span>

  - [Linux Foundation -
    VLANs](http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan)

  - [Linux Journal - Linux as an Ethernet
    Bridge](http://www.linuxjournal.com/article/8172)

  - [Comparing Traditional Bridge Mode to VLAN-aware Bridge
    Mode](https://support.cumulusnetworks.com/hc/en-us/articles/204909397)

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

</details>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMjU0Mjc2ODddfQ==
-->