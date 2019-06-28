---
title: Layer 1 and Switch Port Attributes
author: Cumulus Networks
weight: 55
aliases:
 - /display/RMP31/Layer+1+and+Switch+Port+Attributes
 - /pages/viewpage.action?pageId=5122796
pageID: 5122796
product: Cumulus RMP
version: 3.1.2
imgData: cumulus-rmp-312
siteSlug: cumulus-rmp-312
---
This chapter discusses the various network interfaces on a switch
running Cumulus RMP.

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

Cumulus RMP exposes network interfaces for several types of physical and
logical devices:

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

Cumulus RMP supports both half- and
[full-duplex](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29)
configurations. Supported port speeds include 1G and 10G. Set the speeds
in terms of Mbps, where the setting for 1G is 1000 and 10G is 10000.

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

### <span>Auto-negotiation</span>

You can enable or disable
[auto-negotiation](http://en.wikipedia.org/wiki/Autonegotiation) (that
is, set it *on* or *off*) on a switch port.

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
<p>You can use <code>ethtool</code> to configure auto-negotiation for your switch ports. The following example uses swp1.</p>
<p>To enable or disable auto-negotiation, run:</p>
<pre><code>ethtool -s swp1 speed 10000 duplex full autoneg on|off</code></pre></td>
</tr>
</tbody>
</table>

### <span id="src-5122796_Layer1andSwitchPortAttributes-mtu" class="confluence-anchor-link"></span><span>MTU</span>

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

When you are configuring MTU for a bridge, its MTU setting is the lowest
MTU setting of any interface that is a member of that bridge (that is,
every interface specified in `bridge-ports` in the bridge configuration
in the `interfaces` file). Consider this bridge configuration:

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
        bond-mode 802.3ad
        bond-miimon 100
        bond-lacp-rate 1
        bond-min-links 1
        bond-xmit_hash_policy layer3+4
        mtu 9000

To show MTU, use `ip link show`:

    cumulus@switch:~$ ip link show dev swp1
    3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff

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

  - [wiki.debian.org/NetworkConfiguration](http://wiki.debian.org/NetworkConfiguration)

  - [www.linuxfoundation.org/collaborate/workgroups/networking/vlan](http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan)

  - [www.linuxfoundation.org/collaborate/workgroups/networking/bridge](http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge)

  - [www.linuxfoundation.org/collaborate/workgroups/networking/bonding](http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding)
