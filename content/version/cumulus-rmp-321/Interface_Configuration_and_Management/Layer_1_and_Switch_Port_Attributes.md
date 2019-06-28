---
title: Layer 1 and Switch Port Attributes
author: Cumulus Networks
weight: 57
aliases:
 - /display/RMP321/Layer+1+and+Switch+Port+Attributes
 - /pages/viewpage.action?pageId=5127618
pageID: 5127618
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
This chapter discusses the various network interfaces on a switch
running Cumulus RMP, how to configure various interface-level settings
(if needed) and some troubleshooting commands.

## <span>Interface Types</span>

Cumulus RMP exposes network interfaces for several types of physical and
logical devices:

  - lo, network loopback device

  - ethN, switch management port(s), for out of band management only

  - swpN, switch front panel ports

  - (optional) brN, bridges (IEEE 802.1Q VLANs)

  - (optional) bondN, bonds (IEEE 802.3ad link aggregation trunks, or
    port channels)

## <span>Interface Settings</span>

Each physical network interface has a number of configurable settings:

  - [Auto-negotiation](http://en.wikipedia.org/wiki/Autonegotiation)

  - [Duplex](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29)

  - Link speed

  - MTU, or [maximum transmission
    unit](https://en.wikipedia.org/wiki/Maximum_transmission_unit)

Almost all of these settings are configured automatically for you,
depending upon your switch ASIC, although you must always set MTU
manually.

{{%notice note%}}

You can only set MTU for logical interfaces. If you try to set
auto-negotiation, duplex mode or link speed for a logical interface, an
unsupported error gets returned.

{{%/notice%}}

### <span id="src-5127618_Layer1andSwitchPortAttributes-autoneg_enable" class="confluence-anchor-link"></span><span>Enabling Auto-negotiation</span>

To configure auto-negotiation, set `link-autoneg` to *on* for all the
switch ports. For example, to enable auto-negotiation for swp1 through
swp52:

    cumulus@switch:~$ net add interface swp1-52 link autoneg on
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

Any time you enable auto-negotiation, Cumulus RMP restores the default
configuration settings specified in the [table
below](#src-5127618_Layer1andSwitchPortAttributes-sett).

By default, auto-negotiation is disabled — except on 10G and 1G BASE-T
switches, where it's required for links to work at all. And for RJ45-SFP
converters, you need to manually configure the settings as described in
the [default settings table
below](#src-5127618_Layer1andSwitchPortAttributes-sett).

If you disable it later or never enable it, then you have to configure
the duplex and link speed settings manually using
[NCLU](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=5120643)
— see the relevant sections below. The default speed if you disable
auto-negotiation depends on the type of connector used with the port.
For example, SFP+ optics default to 10G.

{{%notice warning%}}

You cannot or should not disable auto-negotiation off for any type of
copper cable, including:

  - 10G BASE-T

  - 10G DAC

However, RJ-45 (10/100/1000 BASE-T) adapters do not work with
auto-negotiation enabled. You must manually configure these ports using
the settings below (link-autoneg=off, link-speed=1000|100|10,
link-duplex=full|half).

{{%/notice%}}

### <span id="src-5127618_Layer1andSwitchPortAttributes-settings" class="confluence-anchor-link"></span><span>Default Interface Configuration Settings</span>

The configuration for each type of interface is described in the
following table. Except as noted below, the settings for both sides of
the link are expected to be the same.

{{%notice note%}}

If the other side of the link is running a version of Cumulus RMP or
Cumulus Linux earlier than 3.2, depending up on the interface type,
auto-negotiation may not work on that switch. Cumulus Networks
recommends you use the default settings on this switch in this case.

{{%/notice%}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Speed</p></th>
<th><p>Auto-negotiation</p></th>
<th><p>Manual Configuration Steps</p></th>
<th><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1000BASE-T (RJ45)</p></td>
<td><p>Off</p></td>
<td><pre><code>$ net add interface swp1 link speed 1000
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 1000</code></pre></td>
<td><ul>
<li><p>The module has two sets of electronics — the port side, which communicates to the switch ASIC, and the RJ45 side.</p></li>
<li><p>Auto-negotiation is always used on the RJ45 side of the link by the PHY built into the module. This is independent of the switch setting. Set <code>link-autoneg</code> to off.</p></li>
<li><p>Auto-negotiation needs to be enabled on the server side in this scenario.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>10G BASE-CR,<br />
10G BASE-LR,<br />
10G BASE-SR,<br />
10G AOC</p></td>
<td><p>Off</p></td>
<td><pre><code>$ net add interface swp1 link speed 10000
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 10000</code></pre></td>
<td><p> </p></td>
</tr>
</tbody>
</table>

### <span>Port Speed and Duplexing</span>

Cumulus RMP supports both half- and
[full-duplex](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29)
configurations. Supported port speeds include 100M, 1G and 10G. Set the
speeds in terms of Mbps, where the setting for 1G is 1000 and 10G is
10000.

The duplex mode setting defaults to *full*. You only need to specify
`link duplex` if you want half-duplex mode.

{{%notice info%}}

**Example Port Speed and Duplexing Configuration**

The following NCLU commands configure the port speed for the swp1
interface:

    cumulus@switch:~$ net add interface swp1 link speed 10000
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The above commands create the following ` /etc/network/interfaces  `code
snippet:

    auto swp1
    iface swp1
       link-speed 10000

{{%/notice%}}

#### <span>Port Speed Limitations</span>

Ports can be configured to one speed less than their maximum speed.

| Switch port Type | Lowest Configurable Speed |
| ---------------- | ------------------------- |
| 1G               | 100 Mb                    |
| 10G              | 1 Gigabit (1000 Mb)       |

### <span id="src-5127618_Layer1andSwitchPortAttributes-mtu" class="confluence-anchor-link"></span><span>MTU</span>

Interface MTU ([maximum transmission
unit](https://en.wikipedia.org/wiki/Maximum_transmission_unit)) applies
to traffic traversing the management port, front panel/switch ports,
bridge, VLAN subinterfaces and bonds — in other words, both physical and
logical interfaces.

MTU is the only interface setting that must be set manually.

In Cumulus Linux, `ifupdown2` assigns 1500 as the default MTU setting.
You can override this default value by specifying a policy file in
`/etc/network/ifupdown2/policy.d/`, like in the following example:

    cumulus@switch:~$ cat /etc/network/ifupdown2/policy.d/address.json
    {
        "address": {
            "defaults": { "mtu": "9000" }
        }
    }

#### <span>MTU for a Bridge</span>

The MTU setting is the lowest MTU setting of any interface that is a
member of that bridge (that is, every interface specified in
`bridge-ports` in the bridge configuration in the `interfaces` file),
even if another bridge member has a higher MTU value. There is **no**
need to specify an MTU on the bridge. Consider this bridge
configuration:

    auto bridge
    iface bridge
        bridge-ports bond1 bond2 bond3 bond4 peer5
        bridge-vids 100-110
        bridge-vlan-aware yes

In order for *bridge* to have an MTU of 9000, set the MTU for each of
the member interfaces (bond1 to bond 4, and peer5), to 9000 at minimum.

{{%notice tip%}}

**Use MTU 9216 for a bridge**

Two common MTUs for jumbo frames are 9216 and 9000 bytes. The
corresponding MTUs for the VNIs would be 9166 and 8950.

{{%/notice%}}

When configuring MTU for a bond, configure the MTU value directly under
the bond interface; the configured value is inherited by member
links/slave interfaces. If you need a different MTU on the bond, set it
on the bond interface, as this ensures the slave interfaces pick it up.
There is no need to specify MTU on the slave interfaces.

VLAN interfaces inherit their MTU settings from their physical devices
or their lower interface; for example, swp1.100 inherits its MTU setting
from swp1. Hence, specifying an MTU on swp1 ensures that swp1.100
inherits swp1's MTU setting.

{{%notice info%}}

**Example MTU Configuration**

In general, the policy file specified above handles default MTU settings
for all interfaces on the switch. If you need to configure a different
MTU setting for a subset of interfaces, use
[NCLU](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=5120643).

The following commands configure an MTU minimum value of 9000 on swp1:

    cumulus@switch:~$ net add interface swp1 mtu 9000
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following code snippet:

    auto swp1
    iface swp1
       mtu 9000

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info%}}

You must take care to ensure there are no MTU mismatches in the
conversation path. MTU mismatches will result in dropped or truncated
packets, degrading or blocking network performance.

{{%/notice%}}

{{%/notice%}}

To view the MTU setting, use `net show interface <interface>`:

    cumulus@switch:~$ net show interface swp1
        Name    MAC                Speed      MTU  Mode
    --  ------  -----------------  -------  -----  ---------
    UP  swp1    44:38:39:00:00:04  1G        1500  Access/L2

## <span>Verification and Troubleshooting Commands</span>

### <span>Statistics</span>

High-level interface statistics are available with the `net show
interface` command:

    cumulus@switch:~$ net show interface swp1
     
        Name    MAC                Speed      MTU  Mode
    --  ------  -----------------  -------  -----  ---------
    UP  swp1    44:38:39:00:00:04  1G        1500  Access/L2
     
     
    Vlans in disabled State
    -------------------------
    br0
     
     
    Counters      TX    RX
    ----------  ----  ----
    errors         0     0
    unicast        0     0
    broadcast      0     0
    multicast      0     0
     
     
    LLDP
    ------  ----  ---------------------------
    swp1    ====  44:38:39:00:00:03(server01)

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

You can verify SFP settings using ` ethtool -m  `. The following example
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

## <span>Related Information</span>

  - [Debian - Network
    Configuration](http://wiki.debian.org/NetworkConfiguration)

  - [Linux Foundation -
    VLANs](http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan)

  - [Linux Foundation -
    Bridges](http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge)

  - [Linux Foundation -
    Bonds](http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding)
