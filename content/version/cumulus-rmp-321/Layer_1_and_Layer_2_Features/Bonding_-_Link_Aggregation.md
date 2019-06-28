---
title: Bonding - Link Aggregation
author: Cumulus Networks
weight: 77
aliases:
 - /display/RMP321/Bonding+-+Link+Aggregation
 - /pages/viewpage.action?pageId=5127595
pageID: 5127595
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
Linux bonding provides a method for aggregating multiple network
interfaces (the *slaves*) into a single logical bonded interface (the
*bond*). Cumulus RMP bonding supports the IEEE 802.3ad link aggregation
mode, which allows one or more links to be aggregated together to form a
*link aggregation group* (LAG), such that a media access control (MAC)
client can treat the link aggregation group as if it were a single link.
The benefits of link aggregation include:

  - Linear scaling of bandwidth as links are added to LAG

  - Load balancing

  - Failover protection

The Cumulus RMP uses version 1 of the LAG protocol.

## <span>Hash Distribution</span>

Egress traffic through a bond is distributed to a slave based on a
packet hash calculation, providing load balancing over the slaves; many
conversation flows are distributed over all available slaves to load
balance the total traffic. Traffic for a single conversation flow always
hashes to the same slave.

The hash calculation uses packet header data to pick which slave to
transmit the packet to:

  - For IP traffic, IP header source and destination fields are used in
    the calculation.

  - For IP + TCP/UDP traffic, source and destination ports are included
    in the hash calculation.

{{%notice note%}}

In a failover event, the hash calculation is adjusted to steer traffic
over available slaves.

{{%/notice%}}

## <span>Creating a Bond</span>

Bonds can be created and configured using the Network Command Line
Utility
([NCLU](/version/cumulus-rmp-321/System_Configuration/Network_Command_Line_Utility)).
Follow the steps below to create a new bond:

1.  SSH into the switch.

2.  Add a bond using the `net add bond` command, replacing `[bond-name]`
    with the name of the bond, and `[slaves]` with the list of slaves:
    
        cumulus@switch:~$ net add bond [bond-name] bond slaves [slaves]
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit

{{%notice note%}}

The name of the bond must be:

  - Compliant with Linux interface naming conventions.

  - Unique within the switch.

{{%/notice%}}

### <span>Configuration Options</span>

The configuration options, and their default values, are listed in the
table below.

{{%notice note%}}

Each bond configuration option, except for `bond slaves,` is set to the
recommended value by default in Cumulus RMP. They should only be
configured if a different setting is needed. For more information on
configuration values, refer to the Related Information section below.

{{%/notice%}}

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Configuration Option</p></th>
<th><p>Description</p></th>
<th><p>Default Value</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>bond mode</code></p></td>
<td><p>The defined bonding mode.</p>
<p>{{%notice warning%}}</p>
<p>Cumulus RMP <em>only</em> supports IEEE 802.3ad link aggregation mode. This setting <strong>must not</strong> be changed.</p>
<p>{{%/notice%}}</p></td>
<td><p><code>802.3ad</code></p></td>
</tr>
<tr class="even">
<td><p><code>bond slaves</code></p></td>
<td><p>The list of slaves in the bond.</p></td>
<td><p>N/A</p></td>
</tr>
<tr class="odd">
<td><p><code>bond miimon</code></p></td>
<td><p>Defines how often the link state of each slave is inspected for failures.</p></td>
<td><p><code>100</code></p></td>
</tr>
<tr class="even">
<td><p><code>bond use-carrier</code></p></td>
<td><p>Determines the link state.</p></td>
<td><p><code>1</code></p></td>
</tr>
<tr class="odd">
<td><p><code>bond xmit-hash-policy</code></p></td>
<td><p>Hash method used to select the slave for a given packet.</p>
<p>{{%notice warning%}}</p>
<p>This setting <strong>must not</strong> be changed.</p>
<p>{{%/notice%}}</p></td>
<td><p><code>layer3+4</code></p></td>
</tr>
<tr class="even">
<td><p><code>bond lacp-rate</code></p></td>
<td><p>Sets the rate to ask the link partner to transmit LACP control packets.</p>
<p>{{%notice note%}}</p>
<p>At this time, you can set the LACP rate to slow (0) only by editing the setting <code>bond-lacp-rate</code> to <em>0</em> in the <code>/etc/network/interfaces</code> file.</p>
<p>{{%/notice%}}</p></td>
<td><p>1</p></td>
</tr>
<tr class="odd">
<td><p><code>bond min-links</code></p></td>
<td><p>Defines the minimum number of links that must be active before the bond is put into service.</p>
<p>{{%notice info%}}</p>
<p>A value greater than <code>1</code> is useful if higher level services need to ensure a minimum aggregate bandwidth level before activating a bond. Keeping <code>bond-min-links</code> set to <code>1</code> indicates the bond must have at least one active member. If the number of active members drops below the <code>bond-min-links</code> setting, the bond will appear to upper-level protocols as <code>link-down</code>. When the number of active links returns to greater than or equal to <code>bond-min-links</code>, the bond will become <code>link-up</code>.</p>
<p>{{%/notice%}}</p></td>
<td><p><code>1</code></p></td>
</tr>
</tbody>
</table>

## <span>Example Configuration: Bonding 4 Slaves</span>

In the following example, the front panel port interfaces swp1-swp4 are
slaves in bond0, while swp5 and swp6 are not part of bond0.

{{% imgOld 0 %}}

{{%notice info%}}

**Example Bond Configuration**

The following commands create a bond with four slaves:

    cumulus@switch:~$ net add bond bond0 address 10.0.0.1/30
    cumulus@switch:~$ net add bond bond0 bond slaves swp1-4
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create this code snippet in the `/etc/network/interfaces`
file:

    auto bond0
    iface bond0
        address 10.0.0.1/30
        bond-slaves swp1 swp2 swp3 swp4

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info%}}

If you are intending that the bond become part of a bridge, you don't
need to specify an IP address.

{{%/notice%}}

{{%/notice%}}

When networking is started on switch, bond0 is created as MASTER and
interfaces swp1-swp4 come up in SLAVE mode, as seen in the `ip link
show` command:

    cumulus@switch:~$ ip link show
    ...
     
    3: swp1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
    4: swp2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
    5: swp3: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
    6: swp4: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
     
    ...
     
    55: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff

{{%notice note%}}

All slave interfaces within a bond have the same MAC address as the
bond. Typically, the first slave added to the bond donates its MAC
address as the bond MAC address, while the other slaves’ MAC addresses
are set to the bond MAC address.

The bond MAC address is used as source MAC address for all traffic
leaving the bond, and provides a single destination MAC address to
address traffic to the bond.

{{%/notice%}}

## <span>Caveats and Errata</span>

  - An interface cannot belong to multiple bonds.

  - A bond can have subinterfaces, but not the other way around.

  - A bond cannot enslave VLAN subinterfaces.

  - Slave ports within a bond should all be set to the same
    speed/duplex, and should match the link partner’s slave ports.

## <span>Related Information</span>

  - [Linux Foundation -
    Bonding](http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding)

  - [802.3ad](http://www.ieee802.org/3/ad/) ([Accessible
    writeup](http://cs.uccs.edu/%7Escold/doc/linkage%20aggregation.pdf))

  - [Wikipedia - Link
    aggregation](http://en.wikipedia.org/wiki/Link_aggregation)
