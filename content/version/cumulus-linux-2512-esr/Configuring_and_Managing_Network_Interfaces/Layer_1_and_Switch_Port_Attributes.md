---
title: Layer 1 and Switch Port Attributes
author: Cumulus Networks
weight: 77
aliases:
 - /display/CL25ESR/Layer+1+and+Switch+Port+Attributes
 - /pages/viewpage.action?pageId=5116098
pageID: 5116098
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
This chapter discusses the various network interfaces on a switch
running Cumulus Linux.

## <span>Commands</span>

  - ethtool

  - ip

## <span>Man Pages</span>

  - man ethtool

  - man interfaces

  - man ip

  - man ip addr

  - man ip link

## <span>Configuration Files</span>

  - /etc/network/interfaces

## <span>Interface Types</span>

Cumulus Linux exposes network interfaces for several types of physical
and logical devices:

  - lo, network loopback device

  - ethN, switch management port(s), for out of band management only

  - swpN, switch front panel ports

  - (optional) brN, bridges (IEEE 802.1Q VLANs)

  - (optional) bondN, bonds (IEEE 802.3ad link aggregation trunks, or
    port channels)

## <span>Settings</span>

You can set the MTU, speed, duplex and auto-negotiation settings under a
physical or logical interface stanza:

    auto swp1
    iface swp1
       address 10.1.1.1/24
       mtu 9000
       link-speed 10000
       link-duplex full
       link-autoneg off

To load the updated configuration, run the `ifreload -a` command:

    cumulus@switch:~$ sudo ifreload -a

### <span>Port Speed and Duplexing</span>

Cumulus Linux supports both half- and
[full-duplex](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29)
configurations. Supported port speeds include 1G, 10G and 40G. Set the
speeds in terms of Mbps, where the setting for 1G is 1000, 10G is 10000
and 40G is 40000.

You can create a persistent configuration for port speeds in
`/etc/network/interfaces`. Add the appropriate lines for each switch
port stanza. For example:

    auto swp1
    iface swp1
       address 10.1.1.1/24
       link-speed 10000
       link-duplex full

{{%notice note%}}

If you specify the port speed in `/etc/network/interfaces`, you must
also specify the duplex mode setting along with it; otherwise, `ethtool`
defaults to half duplex.

{{%/notice%}}

You can also configure these settings at run time, using `ethtool`.

Runtime Configuration (Advanced)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>{{%notice warning%}}</p>
<p>A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.</p>
<p>{{%/notice%}}</p>
<p>You can use <code>ethtool</code> to configure duplexing and the speed for your switch ports. You must specify both port speed and duplexing in the <code>ethtool</code> command; auto-negotiation is optional. The following examples use swp1.</p>
<ul>
<li><p>To set the port speed to 1G, run:</p>
<pre><code>ethtool -s swp1 speed 1000 duplex full</code></pre></li>
<li><p>To set the port speed to 10G, run:</p>
<pre><code>ethtool -s swp1 speed 10000 duplex full</code></pre></li>
<li><p>To enable duplexing, run:</p>
<pre><code>ethtool -s swp1 speed 10000 duplex full|half</code></pre></li>
</ul></td>
</tr>
</tbody>
</table>

#### <span>Port Speed Limitations</span>

Ports can be configured to one speed less than their maximum speed.

| Switch port Type | Lowest Configurable Speed |
| ---------------- | ------------------------- |
| 1G               | 100 Mb                    |
| 10G              | 1 Gigabit (1000 Mb)       |
| 40G              | 10G\*                     |

\*Requires the port to be converted into a breakout port.

### <span>Auto-negotiation</span>

You can enable or disable
[auto-negotiation](http://en.wikipedia.org/wiki/Autonegotiation) (that
is, set it *on* or *off*) on a switch port.

{{%notice note%}}

Cumulus Linux does not support auto-negotiation for 10G or 40G
interfaces.

{{%/notice%}}

    auto swp1
    iface swp1
       link-autoneg off

Runtime Configuration (Advanced)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>{{%notice warning%}}</p>
<p>A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.</p>
<p>{{%/notice%}}</p>
<p>You can use <code>ethtool</code> to configure auto-negotiation for your switch ports. The following example use swp1:</p>
<ul>
<li><p>To enable or disable auto-negotiation, run:</p>
<pre><code>ethtool -s swp1 speed 10000 duplex full autoneg on|off</code></pre></li>
</ul></td>
</tr>
</tbody>
</table>

### <span id="src-5116098_Layer1andSwitchPortAttributes-mtu" class="confluence-anchor-link"></span><span>MTU</span>

Interface MTU applies to the management port, front panel port, bridge,
VLAN subinterfaces and bonds.

    auto swp1
    iface swp1
       mtu 9000

Runtime Configuration (Advanced)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>{{%notice warning%}}</p>
<p>A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.</p>
<p>{{%/notice%}}</p>
<p>To set swp1 to Jumbo Frame MTU=9000, use <code>ip link set</code>:</p>
<pre><code>cumulus@switch:~$ sudo ip link set dev swp1 mtu 9000
cumulus@switch:~$ ip link show dev swp1
3: swp1: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 9000 qdisc pfifo_fast state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff</code></pre></td>
</tr>
</tbody>
</table>

{{%notice warning%}}

You must take care to ensure there are no MTU mismatches in the
conversation path. MTU mismatches will result in dropped or truncated
packets, degrading or blocking network performance.

{{%/notice%}}

When you are configuring MTU for a bridge, don't set MTU on the bridge
itself; set it on the individual members of the bridge. The MTU setting
is the lowest MTU setting of any interface that is a member of that
bridge (that is, every interface specified in `bridge-ports` in the
bridge configuration in the `interfaces` file), even if another bridge
member has a higher MTU value. Consider this bridge configuration:

    auto br0
    iface br0
        bridge-ports bond1 bond2 bond3 bond4 peer5
        bridge-vlan-aware yes
        bridge-vids 100-110
        bridge-stp on

In order for br0 to have an MTU of 9000, set the MTU for each of the
member interfaces (bond1 to bond 4, and peer5), to 9000 at minimum.

    auto peer5
    iface peer5
        bond-slaves swp3 swp4
        mtu 9000

When configuring MTU for a bond, configure the MTU value direcly under
the bond interface; the configured value is inherited by member links.

To show MTU, use `ip link show`:

    cumulus@switch:~$ ip link show dev swp1
    3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff

#### <span id="src-5116098_Layer1andSwitchPortAttributes-mtu_vxlan" class="confluence-anchor-link"></span><span>Configuring MTU for a VXLAN Virtual Network Interface</span>

If you are working with
[VXLANs](/display/CL25ESR/Network+Virtualization), the MTU for a virtual
network interface (VNI) must be 50 bytes smaller than the MTU of the
physical interfaces on the switch, as those 50 bytes are required for
various headers and other data. You should also consider setting the MTU
much higher than the default 1500.

Two common MTUs for physical interfaces are 9216 and 9000 bytes. The
corresponding MTUs for the VNIs would be 9166 and 8950.

## <span>Configuring Breakout Ports</span>

Cumulus Linux has the ability to:

  - Break out 40G switch ports into four separate 10G ports for use with
    a breakout cable.

  - Combine (also called *aggregating* or *ganging*) four 10G switch
    ports into one 40G port for use with a breakout cable ([not to be
    confused with a
    bond](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Bonding_-_Link_Aggregation)).

A typical DAC (directly-attached copper) 40G 1xQSFP to 10G 4xSFP+ looks
like this:

{{% imgOld 0 %}}

You configure breakout ports with the `/etc/cumulus/ports.conf` file.
After you modify the configuration, restart `switchd` to push the new
configuration (run `sudo service switchd restart`; [this interrupts
network
services](Configuring_switchd.html#src-5115907_Configuringswitchd-restartswitchd)).

### <span>Breaking out a 40G port into 4x10G Ports</span>

{{%notice info%}}

`/etc/cumulus/ports.conf` varies across different hardware platforms.
Check the current list of supported platforms on [the hardware
compatibility list](http://www.cumulusnetworks.com/hcl).

{{%/notice%}}

A snippet from the `/etc/cumulus/ports.conf` looks like this:

    # QSFP+ ports
    #
    # <port label 49-52> = [4x10G|40G]
    49=40G
    50=40G
    51=40G
    52=40G

To change a 40G port to 4x10G ports, edit the `/etc/cumulus/ports.conf`
file with a text editor (nano, vi, zile). Change *40G* to *4x10G*.

In the following example, switch port 49 is changed to a breakout port:

    # QSFP+ ports
    #
    # <port label 49-52> = [4x10G|40G]
    49=4x10G
    50=40G
    51=40G
    52=40G

To load the change restart `switchd`:

    cumulus@switch:~$ sudo service switchd restart

Many services depend on `switchd`. It is highly recommended to restart
Cumulus Linux if possible in this situation.

### <span>Combining Four 10G Ports into One 40G Port</span>

To gang (aggregate) four 10G ports into one 40G port for use with a
breakout cable, you must edit `/etc/cumulus/ports.conf`.

{{%notice info%}}

`/etc/cumulus/ports.conf` varies across different hardware platforms.
Check the current list of supported platforms on [the hardware
compatibility list](http://www.cumulusnetworks.com/hcl).

{{%/notice%}}

A snippet from the `/etc/cumulus/ports.conf` looks like this:

    # SFP+ ports#
    # <port label 1-48> = [10G|40G/4]
    1=10G
    2=10G
    3=10G
    4=10G
    5=10G

To change four 10G ports into one 40G port, edit the
`/etc/cumulus/ports.conf` file with a text editor (nano, vi, zile).
Change *10G* to *40G/4* for every port being ganged.

In the following example, switch ports swp1-4 are changed to a ganged
port:

    # SFP+ ports#
    # <port label 1-48> = [10G|40G/4]
    1=40G/4
    2=40G/4
    3=40G/4
    4=40G/4
    5=10G

To load the change, restart `switchd`.

    cumulus@switch:~$ sudo service switchd restart

Many services depend on `switchd`. It is highly recommended to restart
Cumulus Linux if possible in this situation.

{{%notice warning%}}

  - You must gang four 10G ports in sequential order. For example, you
    cannot gang swp1, swp10, swp20 and swp40 together.

  - The ports must be in increments of four, with the starting port
    being swp1 (or swp5, swp9, or so forth); so you cannot gang swp2,
    swp3, swp4 and swp5 together.

{{%/notice%}}

## <span>Logical Switch Port Limitations</span>

40G switches with Trident II chipsets (check the *40G Portfolio* section
of the
[HCL](http://cumulusnetworks.com/support/linux-hardware-compatibility-list/))
can support a certain number of logical ports, depending upon the
manufacturer.

Before you configure any logical/unganged ports on a switch, check the
limitations listed in `/etc/cumulus/ports.conf`; this file is specific
to each manufacturer.

For example, the Dell S6000 `ports.conf` file indicates the logical port
limitation like this:

    # ports.conf --
    #
    # This file controls port aggregation and subdivision.  For example, QSFP+
    # ports are typically configurable as either one 40G interface or four
    # 10G/1000/100 interfaces.  This file sets the number of interfaces per port
    # while /etc/network/interfaces and ethtool configure the link speed for each
    # interface.
    #
    # You must restart switchd for changes to take effect.
    #
    # The DELL S6000 has:
    #     32 QSFP ports numbered 1-32
    #     These ports are configurable as 40G, split into 4x10G ports or
    #     disabled.
    #
    #     The X pipeline covers QSFP ports 1 through 16 and the Y pipeline
    #     covers QSFP ports 17 through 32.
    #
    #     The Trident2 chip can only handle 52 logical ports per pipeline.
    #
    #     This means 13 is the maximum number of 40G ports you can ungang
    #     per pipeline, with the remaining three 40G ports set to
    #     "disabled". The 13 40G ports become 52 unganged 10G ports, which
    #     totals 52 logical ports for that pipeline.
    # 

The means the maximum number of ports for this Dell S6000 is 104.

## <span>Verification and Troubleshooting Commands</span>

### <span>Statistics</span>

High-level interface statistics are available with the `ip -s link`
command:

    cumulus@switch:~$ ip -s link show dev swp1
    3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
        RX: bytes  packets  errors  dropped overrun mcast
        21780      242      0       0       0       242
        TX: bytes  packets  errors  dropped carrier collsns
        1145554    11325    0       0       0       0

Low-level interface statistics are available with `ethtool`:

    cumulus@switch:~$ sudo ethtool -S swp1
    NIC statistics:
         HwIfInOctets: 21870
         HwIfInUcastPkts: 0
         HwIfInBcastPkts: 0
         HwIfInMcastPkts: 243
         HwIfOutOctets: 1148217
         HwIfOutUcastPkts: 0
         HwIfOutMcastPkts: 11353
         HwIfOutBcastPkts: 0
         HwIfInDiscards: 0
         HwIfInL3Drops: 0
         HwIfInBufferDrops: 0
         HwIfInAclDrops: 0
         HwIfInBlackholeDrops: 0
         HwIfInDot3LengthErrors: 0
         HwIfInErrors: 0
         SoftInErrors: 0
         SoftInDrops: 0
         SoftInFrameErrors: 0
         HwIfOutDiscards: 0
         HwIfOutErrors: 0
         HwIfOutQDrops: 0
         HwIfOutNonQDrops: 0
         SoftOutErrors: 0
         SoftOutDrops: 0
         SoftOutTxFifoFull: 0
         HwIfOutQLen: 0

### <span>Querying SFP Port Information</span>

You can verify SFP settings using `ethtool -m`. The following example
shows the output for 1G and 10G modules:

    cumulus@switch:~# sudo ethtool -m | egrep '(swp|RXPower :|TXPower :|EthernetComplianceCode)'
     
    swp1: SFP detected
                  EthernetComplianceCodes : 1000BASE-LX
                  RXPower : -10.4479dBm
                  TXPower : 18.0409dBm
    swp3: SFP detected
                  10GEthernetComplianceCode : 10G Base-LR
                  RXPower : -3.2532dBm
                  TXPower : -2.0817dBm

## <span>Useful Links</span>

  - <http://wiki.debian.org/NetworkConfiguration>

  - <http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan>

  - <http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge>

  - <http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding>
