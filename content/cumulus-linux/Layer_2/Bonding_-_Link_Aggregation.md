---
title: Bonding - Link Aggregation
author: Cumulus Networks
weight: 119
aliases:
 - /display/DOCS/Bonding+-+Link+Aggregation
 - /pages/viewpage.action?pageId=8362653
pageID: 8362653
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
Linux bonding provides a method for aggregating multiple network
interfaces (*slaves*) into a single logical bonded interface (*bond*).
Cumulus Linux supports two bonding modes:

  - IEEE 802.3ad link aggregation mode, which allows one or more links
    to be aggregated together to form a *link aggregation group* (LAG),
    so that a media access control (MAC) client can treat the link
    aggregation group as if it were a single link. IEEE 802.3ad link
    aggregation is the default mode.

  - Balance-xor mode, where the bonding of slave interfaces are static
    and all slave interfaces are active for load balancing and fault
    tolerance purposes. This is useful for
    [MLAG](/cumulus-linux/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG)
    deployments.

The benefits of link aggregation include:

  - Linear scaling of bandwidth as links are added to LAG

  - Load balancing

  - Failover protection

Cumulus Linux uses version 1 of the LAG control protocol (LACP).

To temporarily bring up a bond even when there is no LACP partner, use
[LACP Bypass](/cumulus-linux/Layer_2/LACP_Bypass).

## <span>Hash Distribution</span>

Egress traffic through a bond is distributed to a slave based on a
packet hash calculation, providing load balancing over the slaves; many
conversation flows are distributed over all available slaves to load
balance the total traffic. Traffic for a single conversation flow always
hashes to the same slave.

The hash calculation uses packet header data to choose to which slave to
transmit the packet:

  - For IP traffic, IP header source and destination fields are used in
    the calculation.

  - For IP + TCP/UDP traffic, source and destination ports are included
    in the hash calculation.

{{%notice note%}}

In a failover event, the hash calculation is adjusted to steer traffic
over available slaves.

{{%/notice%}}

## <span>Create a Bond</span>

You can create and configure a bond with the Network Command Line
Utility
([NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU)).
Follow the steps below to create a new bond:

1.  SSH into the switch.

2.  Add a bond using the `net add bond` command, replacing `[bond-name]`
    with the name of the bond, and `[slaves]` with the list of slaves:
    
        cumulus@switch:~$ net add bond [bond-name] bond slaves [slaves]
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit
    
    The bond is configured by default in IEEE 802.3ad link aggregation
    mode. To configure the bond in balance-xor mode, see [bond
    mode](#src-8362653_Bonding-LinkAggregation-bond_mode) below.

{{%notice note%}}

The name of the bond must be:

  - Compliant with Linux interface naming conventions.

  - Unique within the switch.

{{%/notice%}}

### <span>Configuration Options</span>

The configuration options and their default values are listed in the
table below.

{{%notice note%}}

Each bond configuration option, except for `bond slaves,` is set to the
recommended value by default in Cumulus Linux. Only configure an option
if a different setting is needed. For more information on configuration
values, refer to the [Related
Information](#src-8362653_Bonding-LinkAggregation-related-information)
section below.

{{%/notice%}}

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>NCLU Configuration Option</p></th>
<th><p>Description</p></th>
<th><p>Default Value</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>bond mode</code></p></td>
<td><p>The bonding mode. Cumulus Linux supports IEEE 802.3ad link aggregation mode and balance-xor mode. IEEE 802.3ad link aggregation is the default mode.</p>
<p>You can change the bond mode using NCLU. The following example changes bond1 to balance-xor mode.</p>
<p><strong>Note</strong>: Use balance-xor mode only if you cannot use LACP. <a href="#src-8362653_Bonding-LinkAggregation-balance_xor">See below</a> for more information.</p>
<pre><code>cumulus@switch:~$ net add bond bond1 bond mode balance-xor
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit</code></pre>
<p>The following example changes bond1 to IEEE 802.3ad link aggregation mode:</p>
<pre><code>cumulus@switch:~$ net add bond bond1 bond mode 802.3ad
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit</code></pre></td>
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
<td><p><code>bond downdelay</code></p></td>
<td><p>Specifies the time, in milliseconds, to wait before disabling a slave after a link failure has been detected. This option is only valid for the miimon link monitor. The downdelay value must be a multiple of the miimon value; if not, it is rounded down to the nearest multiple.</p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><code>bond updelay</code></p></td>
<td><p>Specifies the time, in milliseconds, to wait before enabling a slave after a link recovery has been detected. This option is only valid for the miimon link monitor. The updelay value must be a multiple of the miimon value; if not, it is rounded down to the nearest multiple.</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><code>bond use-carrier</code></p></td>
<td><p>Determines the link state.</p></td>
<td><p><code>1</code></p></td>
</tr>
<tr class="odd">
<td><p><code>bond xmit-hash-policy</code></p></td>
<td><p>The hash method used to select the slave for a given packet.</p>
<p>{{%notice warning%}}</p>
<p>Do not change this setting.</p>
<p>{{%/notice%}}</p></td>
<td><p><code>layer3+4</code></p></td>
</tr>
<tr class="even">
<td><p><code>bond lacp-bypass-allow</code></p></td>
<td><p>Enables <a href="/cumulus-linux/Layer_2/LACP_Bypass">LACP bypass</a>.</p></td>
<td><p>N/A</p></td>
</tr>
<tr class="odd">
<td><p><code>bond lacp-rate</code></p></td>
<td><p>Sets the rate to ask the link partner to transmit LACP control packets.</p>
<p>You can set the LACP rate to slow using <a href="/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU">NCLU</a>:</p>
<pre><code>cumulus@switch:~$ net add bond bond01 bond lacp-rate slow</code></pre></td>
<td><p>1</p></td>
</tr>
<tr class="even">
<td><p><code>bond min-links</code></p></td>
<td><p>Defines the minimum number of links that must be active before the bond is put into service.</p>
<p>{{%notice info%}}</p>
<p>A value greater than <code>1</code> is useful if higher level services need to ensure a minimum aggregate bandwidth level before activating a bond. Keeping <code>bond-min-links</code> set to <code>1</code> indicates the bond must have at least one active member. If the number of active members drops below the <code>bond-min-links</code> setting, the bond will appear to upper-level protocols as <code>link-down</code>. When the number of active links returns to greater than or equal to <code>bond-min-links</code>, the bond becomes <code>link-up</code>.</p>
<p>{{%/notice%}}</p></td>
<td><p>1</p></td>
</tr>
</tbody>
</table>

### <span id="src-8362653_Bonding-LinkAggregation-balance_xor" class="confluence-anchor-link"></span><span>Enable balance-xor Mode</span>

When you enable *balance-xor mode*, the bonding of slave interfaces are
static and all slave interfaces are active for load balancing and fault
tolerance purposes. Packet transmission on the bond is based on the hash
policy specified by `xmit-hash-policy`.

When using balance-xor mode to dual-connect host-facing bonds in an
[MLAG](/cumulus-linux/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG)
environment, you **must** configure the `clag_id` parameter on the MLAG
bonds and it must be the same on both MLAG switches. Otherwise, the
bonds are treated by the MLAG switch pair as single-connected.

{{%notice note%}}

Use balance-xor mode **only** if you cannot use LACP; LACP can detect
mismatched link attributes between bond members and can even detect
misconnections.

{{%/notice%}}

To change the mode of an existing bond to balance-xor, run the `net add
bond <bond-name> bond mode balance-xor` command. The following example
commands change bond1 to balance-xor mode:

    cumulus@switch:~$ net add bond bond1 bond mode balance-xor
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

To create a new bond and configure the bond to use balance-xor mode,
create the bond, then configure the bond mode. The following example
commands create a bond called bond1 and configure bond mode to be
balance-xor:

    cumulus@switch:~$ net add bond bond1 bond slaves swp3,4
    cumulus@switch:~$ net add bond bond1 bond mode balance-xor
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto bond1
    iface bond1
        bond-mode balance-xor
        bond-slaves swp3 swp4

To view the bond, use
[NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU):

    cumulus@switch:~$ net show interface bond1 
        Name    MAC                Speed    MTU    Mode
    --  ------  -----------------  -------  -----  ------
    UP  bond1   00:02:00:00:00:12  20G      1500   Bond
     
     
    Bond Details
    ---------------  -------------
    Bond Mode:       Balance-XOR
    Load Balancing:  Layer3+4
    Minimum Links:   1
    In CLAG:         CLAG Inactive
     
     
        Port     Speed      TX    RX    Err    Link Failures
    --  -------  -------  ----  ----  -----  ---------------
    UP  swp3(P)  10G         0     0      0                0
    UP  swp4(P)  10G         0     0      0                0
     
     
    LLDP
    -------  ----  ------------
    swp3(P)  ====  swp1(p1c1h1)
    swp4(P)  ====  swp2(p1c1h1)Routing
    -------
      Interface bond1 is up, line protocol is up
      Link ups:       3    last: 2017/04/26 21:00:38.26
      Link downs:     2    last: 2017/04/26 20:59:56.78
      PTM status: disabled
      vrf: Default-IP-Routing-Table
      index 31 metric 0 mtu 1500
      flags: <UP,BROADCAST,RUNNING,MULTICAST>
      Type: Ethernet
      HWaddr: 00:02:00:00:00:12
      inet6 fe80::202:ff:fe00:12/64
      Interface Type Other

## <span>Example Configuration: Bonding 4 Slaves</span>

In the following example, the front panel port interfaces swp1 thru swp4
are slaves in bond0, while swp5 and swp6 are not part of bond0.

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

If the bond is going to become part of a bridge, you do not need to
specify an IP address.

{{%/notice%}}

{{%/notice%}}

When networking is started on the switch, bond0 is created as MASTER and
interfaces swp1 thru swp4 come up in SLAVE mode, as seen in the `ip link
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
address as the bond MAC address, whereas the MAC addresses of the other
slaves are set to the bond MAC address.

The bond MAC address is used as the source MAC address for all traffic
leaving the bond and provides a single destination MAC address to
address traffic to the bond.

{{%/notice%}}

## <span>Caveats and Errata</span>

  - An interface cannot belong to multiple bonds.

  - A bond can have subinterfaces, but subinterfaces cannot have a bond.

  - A bond cannot enslave VLAN subinterfaces.

  - Set all slave ports within a bond to the same speed/duplex and make
    sure they match the link partner’s slave ports.

  - On a [Cumulus
    RMP](https://docs.cumulusnetworks.com/display/RMP/Cumulus+RMP)
    switch, if you create a bond with multiple 10G member ports, traffic
    gets dropped when the bond uses members of the same *unit* listed in
    the `/var/lib/cumulus/porttab` file. For example, traffic gets
    dropped if both swp49 and swp52 are in the bond because they both
    are in the xe0 unit (or if both swp50 and swp51 are in the same bond
    because they are both in xe1):  
    swp49 xe0 0 0 -1 0  
    swp50 xe1 0 0 -1 0  
    swp51 xe1 1 0 -1 0  
    swp52 xe0 1 0 -1 0  
    Single port member bonds, bonds with different units (xe0 or xe1, as
    above), or layer 3 bonds do not have this issue.
    
    {{%notice note%}}
    
    On Cumulus RMP switches, which are built with two Hurricane2 ASICs,
    you cannot form an LACP bond on links that terminate on different
    Hurricane2 ASICs.
    
    {{%/notice%}}

## <span id="src-8362653_Bonding-LinkAggregation-related-information" class="confluence-anchor-link"></span><span>Related Information</span>

  - [Linux Foundation -
    Bonding](http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding)

  - [802.3ad](http://www.ieee802.org/3/ad/) ([Accessible
    writeup](http://cs.uccs.edu/%7Escold/doc/linkage%20aggregation.pdf))

  - [Wikipedia - Link
    aggregation](http://en.wikipedia.org/wiki/Link_aggregation)
