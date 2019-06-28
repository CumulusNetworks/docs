---
title: Layer 1 and Switch Port Attributes
author: Cumulus Networks
weight: 89
aliases:
 - /display/CL330/Layer+1+and+Switch+Port+Attributes
 - /pages/viewpage.action?pageId=5866389
pageID: 5866389
product: Cumulus Linux
version: 3.3.0
imgData: cumulus-linux-330
siteSlug: cumulus-linux-330
---
This chapter discusses the various network interfaces on a switch
running Cumulus Linux, how to configure various interface-level settings
(if needed) and some troubleshooting commands.

## <span>Interface Types</span>

Cumulus Linux exposes network interfaces for several types of physical
and logical devices:

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

  - [Forward error
    correction](https://en.wikipedia.org/wiki/Forward_error_correction)

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

### <span>Differences between Broadcom-based and Mellanox-based Switches</span>

On a Broadcom-based switch, all you need to do is enable
auto-negotiation. Once enabled, Cumulus Linux automatically configures
the link speed, duplex mode and [forward error
correction](https://en.wikipedia.org/wiki/Forward_error_correction)
(FEC, if the cable or optic requires it) for every switch port, based on
the switch model and cable or optic used on the port, as listed in the
[table below](#src-5866389_Layer1andSwitchPortAttributes-settings).

Ports are always automatically configured on a Mellanox-based switch,
with one exception — you only need to configure is
[MTU](#src-5866389_Layer1andSwitchPortAttributes-mtu). You don't even
need to enable auto-negotation, as the Mellanox firmware configures
everything for you.

### <span id="src-5866389_Layer1andSwitchPortAttributes-autoneg_enable" class="confluence-anchor-link"></span><span>Enabling Auto-negotiation</span>

To configure auto-negotiation for a Broadcom-based switch, set
`link-autoneg` to *on* for all the switch ports. For example, to enable
auto-negotiation for swp1 through swp52:

    cumulus@switch:~$ net add interface swp1-52 link autoneg on
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

Any time you enable auto-negotiation, Cumulus Linux restores the default
configuration settings specified in the [table
below](#src-5866389_Layer1andSwitchPortAttributes-sett).

By default on a Broadcom-based switch, auto-negotiation is disabled —
except on 10G and 1G BASE-T switches, where it's required for links to
work at all. And for RJ45-SFP converters, you need to manually configure
the settings as described in the [default settings table
below](#src-5866389_Layer1andSwitchPortAttributes-sett).

If you disable it later or never enable it, then you have to configure
the duplex, FEC and link speed settings manually using
[NCLU](/version/cumulus-linux-330/System_Configuration/Network_Command_Line_Utility)
— see the relevant sections below. The default speed if you disable
auto-negotiation depends on the type of connector used with the port.
For example, a QSFP28 optic defaults to 100G, while a QSFP+ optic
defaults to 40G and SFP+ defaults to 10G.

{{%notice warning%}}

You cannot or should not disable auto-negotiation off for any type of
copper cable, including:

  - 10G BASE-T

  - 10G DAC

  - 40G DAC

  - 100G DAC

However, RJ-45 (10/100/1000 BASE-T) adapters do not work with
auto-negotiation enabled. You must manually configure these ports using
the settings below (link-autoneg=off, link-speed=1000|100|10,
link-duplex=full|half).

{{%/notice%}}

Depending upon the connector used for a port, enabling auto-negotiation
also enables forward error correction (FEC), if the cable requires it
(see the [table
below](#src-5866389_Layer1andSwitchPortAttributes-setting)). FEC always
adjusts for the speed of the cable. However, you **cannot** disable FEC
separately using
[NCLU](/version/cumulus-linux-330/System_Configuration/Network_Command_Line_Utility).

### <span id="src-5866389_Layer1andSwitchPortAttributes-settings" class="confluence-anchor-link"></span><span>Default Interface Configuration Settings</span>

On a Broadcom-based switch, the configuration for each type of interface
is described in the following table. Except as noted below, the settings
for both sides of the link are expected to be the same.

{{%notice note%}}

If the other side of the link is running a version of Cumulus Linux
earlier than 3.2, depending up on the interface type, auto-negotiation
may not work on that switch. Cumulus Networks recommends you use the
default settings on this switch in this case.

{{%/notice%}}

For Mellanox-based switches, the Spectrum firmware decides on the best
settings based on the switch model and connector type.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Speed</p></th>
<th><p>Auto-negotiation</p></th>
<th><p>FEC Setting</p></th>
<th><p>Manual Configuration Steps</p></th>
<th><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>10/100 (RJ45)</p></td>
<td><p>Off</p></td>
<td><p>N/A (does not apply at this speed)</p></td>
<td><pre><code>$ net add interface swp1 link speed 100
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 100</code></pre></td>
<td><ul>
<li><p>The module has two sets of electronics — the port side, which communicates to the switch ASIC, and the RJ45 side.</p></li>
<li><p>Auto-negotiation is always used on the RJ45 side of the link by the PHY built into the module. This is independent of the switch setting. Set <code>link-autoneg</code> to off.</p></li>
<li><p>Auto-negotiation needs to be enabled on the server side in this scenario.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>1000BASE-SX,<br />
1000BASE-LX,<br />
1000BASE-CX<br />
(1G Fiber)</p></td>
<td><p>Recommended On</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 1000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 1000</code></pre></td>
<td><ul>
<li><p>Without auto-negotiation, the link stays up when there is a single fiber break.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>1000BASE-T (RJ45)</p></td>
<td><p>Off</p></td>
<td><p>N/A</p></td>
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
<td><p>10G BASE-T</p></td>
<td><p>On</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 10000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 10000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>10G BASE-CR,<br />
10G BASE-LR,<br />
10G BASE-SR,<br />
10G AOC</p></td>
<td><p>Off</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 10000
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 10000
  link-duplex full</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>40G BASE-CR</p></td>
<td><p>Recommended On</p></td>
<td><p>Disable it</p></td>
<td><pre><code>$ net add interface swp1 link speed 40000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 40000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>40G BASE-SR,<br />
40G BASE-LR,<br />
40G AOC</p></td>
<td><p>Off</p></td>
<td><p>Disable it</p></td>
<td><pre><code>$ net add interface swp1 link speed 40000
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 40000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>100G BASE-CR</p></td>
<td><p>On</p></td>
<td><p>auto-negotiated</p></td>
<td><pre><code>$ net add interface swp1 link speed 100000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 100000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>100G BASE-SR,<br />
100G BASE-LR,<br />
100G AOC</p></td>
<td><p>Off</p></td>
<td><p>RS</p></td>
<td><pre><code>$ net add interface swp1 link speed 100000
$ net add interface swp1 link autoneg off
$ net add interface swp1 link fec rs</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 100000
  link-fec rs</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>25G BASE-CR</p></td>
<td><p>On</p></td>
<td><p>auto-negotiated*</p></td>
<td><pre><code>$ net add interface swp1 link speed 25000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 25000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>25G BASE-SR,<br />
25G BASE-LR</p></td>
<td><p>Off</p></td>
<td><p>Base-R</p></td>
<td><pre><code>$ net add interface swp1 link speed 25000
$ net add interface swp1 link autoneg off
$ net add interface swp1 link fec baser</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 25000
  link-fec baser</code></pre></td>
<td><p> </p></td>
</tr>
</tbody>
</table>

### <span>Port Speed and Duplexing</span>

Cumulus Linux supports both half- and
[full-duplex](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29)
configurations. Supported port speeds include 100M, 1G, 10G, 25G, 40G,
50G and 100G. If you need to manually set the speed on a Broadcom-based
switch, set it in terms of Mbps, where the setting for 1G is 1000, 40G
is 40000 and 100G is 100000, for example.

The duplex mode setting defaults to *full* . You only need to specify
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

| Switch port Type | Lowest Configurable Speed                               |
| ---------------- | ------------------------------------------------------- |
| 1G               | 100 Mb                                                  |
| 10G              | 1 Gigabit (1000 Mb)                                     |
| 40G              | 10G\*                                                   |
| 100G             | 50G & 40G (with or without breakout port), 25G\*, 10G\* |

\*Requires the port to be converted into a breakout port. [See
below](#src-5866389_Layer1andSwitchPortAttributes-breakout).

### <span id="src-5866389_Layer1andSwitchPortAttributes-mtu" class="confluence-anchor-link"></span><span>MTU</span>

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

<span id="src-5866389_Layer1andSwitchPortAttributes-mtu_vxlan"></span>If
you are working with
[VXLANs](/version/cumulus-linux-330/Network_Virtualization/), the MTU
for a virtual network interface (VNI) must be 50 bytes smaller than the
MTU of the physical interfaces on the switch, as those 50 bytes are
required for various headers and other data. You should also consider
setting the MTU much higher than the default 1500.

{{%notice info%}}

**Example MTU Configuration**

In general, the policy file specified above handles default MTU settings
for all interfaces on the switch. If you need to configure a different
MTU setting for a subset of interfaces, use
[NCLU](/version/cumulus-linux-330/System_Configuration/Network_Command_Line_Utility).

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

## <span id="src-5866389_Layer1andSwitchPortAttributes-breakout" class="confluence-anchor-link"></span><span>Configuring Breakout Ports</span>

Cumulus Linux has the ability to:

  - Break out 100G switch ports into the following with breakout cables:
    
      - 2x50G, 4x25G, 4x10G

  - Break out 40G switch ports into four separate 10G ports for use with
    breakout cables.

  - Combine (also called *aggregating* or *ganging*) four 10G switch
    ports into one 40G port for use with a breakout cable ([not to be
    confused with a
    bond](/version/cumulus-linux-330/Layer_One_and_Two/Bonding_-_Link_Aggregation)).

To configure a 4x25G breakout port, run:

    cumulus@switch:~$ net add interface swp1 breakout 4x
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The breakout port configuration is stored in the
`/etc/cumulus/ports.conf` file.

{{%notice info%}}

`/etc/cumulus/ports.conf` varies across different hardware platforms.
Check the current list of supported platforms on [the hardware
compatibility list](http://www.cumulusnetworks.com/hcl).

A snippet from the `/etc/cumulus/ports.conf` looks on a Tomahawk switch
like this:

    # The Dell Z9100 has:
    #
    #     32 QSFP28 ports numbered 1-32
    #     These ports are configurable as 100G, 50G, 40G, 2x50G, 4x25G, 4x10G
    #     or disabled.
    #
    #     Two SFP+ ports. These ports are configurable as 10G or disabled.
    #
    #     The system can only handle 128 logical ports.
    #
    #     This means that if all 32 QSFP28 ports are broken out into
    #     4x25G or 4x10G mode, the two 10G ports (33 and 34) must be
    #     set to "disabled".
    # If you make changes to this file, you must restart switchd for the
    # changes to take effect.
    # QSFP28 ports
    #
    # <port label 1-32> = [4x10G|4x25G|2x50G|40G|50G|100G|disabled]
    1=4x25G
    2=100G
    3=100G
    4=100G
     
    ...
     
    # SFP+ ports
    #
    # <port label 33-34> = [10G|disabled]
    33=disabled
    34=disabled

Notice that you can break out any of the 100G ports into a variety of
options: four 10G ports, four 25G ports or two 50G ports. Keep in mind
that you cannot have more than 128 total logical ports on a Broadcom
switch.

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info%}}

The Mellanox SN-2700 and SN-2700B switches both have a limit of 64
logical ports in total. However, if you want to break out to 4x25G or
4x10G, you must configure the logical ports as follows:

  - You can only break out odd-numbered ports into 4 logical ports.

  - You must disable the next even-numbered port.

These restrictions do not apply to a 2x50G breakout configuration.

For example, if you have a 100G Mellanox SN-2700 switch and configure
port 11 as 4x25G logical ports, you must configure port 12 as disabled
in `/etc/cumulus/ports.conf`:

    ...
     
    11=4x25G
    12=disabled
     
    ...

There is no limitation on any port if interfaces are configured in 2x50G
mode.

{{%/notice%}}

{{%/notice%}}

### <span>Combining Four 10G Ports into One 40G Port</span>

You can *gang* (or aggregate) four 10G ports into one 40G port for use
with a breakout cable, provided you follow these requirements:

  - You must gang four 10G ports in sequential order. For example, you
    cannot gang swp1, swp10, swp20 and swp40 together.

  - The ports must be in increments of four, with the starting port
    being swp1 (or swp5, swp9, or so forth); so you cannot gang swp2,
    swp3, swp4 and swp5 together.

For example, to gangs swp1 through swp4 into a 40G port, run:

    cumulus@switch:~$ net add int swp1-4 breakout /4 
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in the
`/etc/cumulus/ports.conf` file:

    # SFP+ ports#
    # <port label 1-48> = [10G|40G/4]
    1=40G/4
    2=40G/4
    3=40G/4
    4=40G/4
    5=10G

## <span>Logical Switch Port Limitations</span>

100G and 40G switches can support a certain number of logical ports,
depending upon the manufacturer; these include:

  - Mellanox SN-2700 and SN-2700B switches

  - Switches with Broadcom Tomahawk, Trident II and Trident II+ chipsets
    (check the
    [HCL](http://cumulusnetworks.com/support/linux-hardware-compatibility-list/))

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

Mellanox SN-2700 and SN-2700B switches have a limit of 64 logical ports
in total. However, the logical ports must be configured in a specific
way. See [the note](#src-5866389_Layer1andSwitchPortAttributes-breakout)
above.

## <span id="src-5866389_Layer1andSwitchPortAttributes-ethtool" class="confluence-anchor-link"></span><span>Using ethtool to Configure Interfaces</span>

The Cumulus Linux `ethtool` command is an alternative for configuring
interfaces as well as viewing and troubleshooting them.

For example, to manually set link speed, auto-negotiation, duplex mode
and FEC on swp1, run:

    cumulus@switch:~$ sudo ethtool -s swp1 speed 25000 autoneg off duplex full
    cumulus@switch:~$ sudo ethtool --set-fec swp1 encoding off

To view the FEC setting on an interface, run:

    cumulus@switch:~$ sudo ethtool --show-fec swp1FEC parameters for swp1:
    Auto-negotiation: off
    FEC encodings : RS

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

## <span>Caveats and Errata</span>

### <span>Timeout Error on Quanta LY8 and LY9 Switches</span>

On Quanta T5048-LY8 and T3048-LY9 switches, an "Operation timed out"
error occurs while removing and reinserting QSFP module.

The QSPFx2 module cannot be removed while the switch is powered on, as
it is not hot-swappable. However, if this occurs, you can get the link
to come up; however, this involves [restarting
`switchd`](Configuring_switchd.html#src-5866112_Configuringswitchd-restartswitchd)
, which disrupts your network.

On the T3048-LY9, run the following commands:

    cumulus@switch:~$ sudo echo 0 > qsfpd_power_enable/value
    cumulus@switch:~$ sudo rmmod quanta_ly9_rangeley_platform 
    cumulus@switch:~$ sudo modprobe quanta_ly9_rangeley_platform
    cumulus@switch:~$ sudo systemctl restart switchd.service

On the T5048-LY8, run the following commands:

    cumulus@switch:~$ sudo echo 0 > qsfpd_power_enable/value
    cumulus@switch:~$ sudo systemctl restart switchd.service

### <span>swp33 and swp34 Disabled on Some Switches</span>

The front SFP+ ports (swp33 and swp34) are disabled in Cumulus Linux on
the following switches:

  - Dell Z9100-ON

  - Penguin Arctica 3200-series switches (the 3200C, 3200XL and 3200XLP)

  - Supermicro SSE-C3632S

These ports appear as disabled in the `/etc/cumulus/ports.conf` file.

## <span>Related Information</span>

  - [Debian - Network
    Configuration](http://wiki.debian.org/NetworkConfiguration)

  - [Linux Foundation -
    VLANs](http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan)

  - [Linux Foundation -
    Bridges](http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge)

  - [Linux Foundation -
    Bonds](http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding)
