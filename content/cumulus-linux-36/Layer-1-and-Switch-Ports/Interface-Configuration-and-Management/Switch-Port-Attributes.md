---
title: Switch Port Attributes
author: Cumulus Networks
weight: 315
pageID: 8362492
---
This chapter discusses the various network interfaces on a switch
running Cumulus Linux, how to configure various interface-level settings
(if needed) and some troubleshooting commands.

## Interface Types

Cumulus Linux exposes network interfaces for several types of physical
and logical devices:

  - lo, network loopback device

  - ethN, switch management port(s), for out of band management only

  - swpN, switch front panel ports

  - (optional) brN, bridges (IEEE 802.1Q VLANs)

  - (optional) bondN, bonds (IEEE 802.3ad link aggregation trunks, or
    port channels)

## Interface Settings

Each physical network interface has a number of configurable settings:

  - [Auto-negotiation](http://en.wikipedia.org/wiki/Autonegotiation)

  - [Duplex](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29)

  - [Forward error
    correction](https://en.wikipedia.org/wiki/Forward_error_correction)

  - Link speed

  - MTU, or [maximum transmission
    unit](https://en.wikipedia.org/wiki/Maximum_transmission_unit)

  - [FEC](https://en.wikipedia.org/wiki/Forward_error_correction)

Almost all of these settings are configured automatically for you,
depending upon your switch ASIC, although you must always set MTU
manually.

{{%notice note%}}

You can only set MTU for logical interfaces. If you try to set
auto-negotiation, duplex mode or link speed for a logical interface, an
unsupported error gets returned.

{{%/notice%}}

### Differences between Broadcom-based and Mellanox-based Switches

On a Broadcom-based switch, all you need to do is enable
auto-negotiation. Once enabled, Cumulus Linux automatically configures
the link speed, duplex mode and [forward error
correction](https://en.wikipedia.org/wiki/Forward_error_correction)
(FEC, if the cable or optic requires it) for every switch port, based on
the port type and cable or optic used on the port, as listed in the
[table below](#interface-configuration-recommendations).

Ports are always automatically configured on a Mellanox-based switch,
with one exception - you only need to configure is [MTU](#mtu). You 
don't even need to enable auto-negotation, as the Mellanox firmware 
configures everything for you.

### Enabling Auto-negotiation

To configure auto-negotiation for a Broadcom-based switch, set
`link-autoneg` to *on* for all the switch ports. For example, to enable
auto-negotiation for swp1 through swp52:

    cumulus@switch:~$ net add interface swp1-52 link autoneg on
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

Any time you enable auto-negotiation, Cumulus Linux restores the default
configuration settings specified in the 
[table below](#interface-configuration-recommendations).

By default on a Broadcom-based switch, auto-negotiation is disabled -
except on 10G and 1000BASE-T switch ports, where it's required for links
to work at all. And for RJ-45 SFP adapters, you need to manually
configure the settings as described in the 
[default settings table below](#interface-configuration-recommendations).

If you disable it later or never enable it, then you have to configure
the duplex, FEC and link speed settings manually using
[NCLU](/cumulus-linux-36/System-Configuration/Network-Command-Line-Utility-NCLU/)
- see the relevant sections below. The default speed if you disable
auto-negotiation depends on the type of connector used with the port.
For example, a QSFP28 optic defaults to 100G, while a QSFP+ optic
defaults to 40G and SFP+ defaults to 10G.

{{%notice warning%}}

You should keep auto-negotiation enabled at all times. If you do decide
to disable it, keep in mind the following:

  - You must manually set link speed, duplex, pause and FEC.
  - Disabling auto-negotiation on a copper cable of any kind prevents
    the port from optimizing the link through link training.
  - Disabling auto-negotiation on a 1G optical cable prevents detection
    of single fiber breaks.
  - You cannot disable auto-negotiation for 1GT or 10GT cables.

However, 10/100/1000BASE-T RJ-45 SFP adapters do not work with
auto-negotiation enabled. You must manually configure these ports using
the settings below (link-autoneg=off, link-speed=1000|100|10,
link-duplex=full|half).

{{%/notice%}}

Depending upon the connector used for a port, enabling auto-negotiation
also enables forward error correction (FEC), if the cable requires it
(see the [table below](#interface-configuration-recommendations)). FEC
always adjusts for the speed of the cable. However, you **cannot**
disable FEC separately using
[NCLU](/cumulus-linux-36/System-Configuration/Network-Command-Line-Utility-NCLU/).

### Port Speed and Duplexing

Cumulus Linux supports both half- and
[full-duplex](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29)
configurations. Supported port speeds include 100M, 1G, 10G, 25G, 40G,
50G and 100G. If you need to manually set the speed on a Broadcom-based
switch, set it in terms of Mbps, where the setting for 1G is *1000*, 40G
is *40000* and 100G is *100000*, for example.

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

#### Port Speed Limitations

Ports can be configured to one speed less than their maximum speed.

| Switch Port Type | Lowest Configurable Speed                               |
| ---------------- | ------------------------------------------------------- |
| 1G               | 100 Mb                                                  |
| 10G              | 1 Gigabit (1000 Mb)                                     |
| 40G              | 10G\*                                                   |
| 100G             | 50G & 40G (with or without breakout port), 25G\*, 10G\* |

\*Requires the port to be converted into a breakout port. 
[See below](#configuring-breakout-ports).

{{%notice note%}}

On Dell S4148F-ON and S4128F-ON switches, you must configure ports
within the same port group with the same link speed.

{{%/notice%}}

### MTU

Interface MTU ([maximum transmission
unit](https://en.wikipedia.org/wiki/Maximum_transmission_unit)) applies
to traffic traversing the management port, front panel/switch ports,
bridge, VLAN subinterfaces and bonds - in other words, both physical and
logical interfaces.

MTU is the only interface setting that must be set manually.

In Cumulus Linux, `ifupdown2` assigns 1500 as the default MTU setting.
To change the setting, run:

    cumulus@switch:~$ net add interface swp1 mtu 9000
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

Some switches may not support the same maximum MTU setting in hardware
for both the management interface (eth0) and the data plane ports.

{{%/notice%}}

#### MTU for a Bridge

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

For a *bridge* to have an MTU of 9000, set the MTU for each of
the member interfaces (bond1 to bond 4, and peer5), to 9000 at minimum.

When configuring MTU for a bond, configure the MTU value directly under
the bond interface; the configured value is inherited by member
links/slave interfaces. If you need a different MTU on the bond, set it
on the bond interface, as this ensures the slave interfaces pick it up.
There is no need to specify MTU on the slave interfaces.

VLAN interfaces inherit their MTU settings from their physical devices
or their lower interface; for example, swp1.100 inherits its MTU setting
from swp1. Hence, specifying an MTU on swp1 ensures that swp1.100
inherits swp1's MTU setting.

If you are working with [VXLANs](/cumulus-linux-36/Network-Virtualization/), 
the MTU for a virtual network interface (VNI) must be 50 bytes smaller than the MTU
of the physical interfaces on the switch, as those 50 bytes are required
for various headers and other data. You should also consider setting the
MTU much higher than the default 1500.

{{%notice info%}}

**Example MTU Configuration**

In general, the policy file specified above handles default MTU settings
for all interfaces on the switch. If you need to configure a different
MTU setting for a subset of interfaces, use
[NCLU](/cumulus-linux-36/System-Configuration/Network-Command-Line-Utility-NCLU/).

The following commands configure an MTU minimum value of 9000 on swp1:

    cumulus@switch:~$ net add interface swp1 mtu 9000
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following code snippet:

    auto swp1
    iface swp1
       mtu 9000

{{%notice warning%}}

You must take care to ensure there are no MTU mismatches in the
conversation path. MTU mismatches will result in dropped or truncated
packets, degrading or blocking network performance.

{{%/notice%}}

{{%/notice%}}

{{%notice note%}}

The MTU for an SVI interface, such as vlan100, is derived from the
bridge. When you use NCLU to change the MTU for an SVI and the MTU
setting is higher than it is for the other bridge member interfaces, the
MTU for all bridge member interfaces changes to the new setting. If you
need to use a mixed MTU configuration for SVIs, for example, if some
SVIs have a higher MTU and some lower, then set the MTU for all member
interfaces to the maximum value, then set the MTU on the specific SVIs
that need to run at a lower MTU.

{{%/notice%}}

To view the MTU setting, use `net show interface <interface>`:

    cumulus@switch:~$ net show interface swp1
        Name    MAC                Speed      MTU  Mode
    --  ------  -----------------  -------  -----  ---------
    UP  swp1    44:38:39:00:00:04  1G        1500  Access/L2

#### Bringing Down an Interface for a Bridge Member

When you bring down an interface for a bridge member, the MTU for the
interface and the MTU for the bridge are both set to the default value
of 1500. To work around this, run `ifdown` on the interface, then run
the `sudo ip link set dev <interface> mtu <mtu>` command.

For example:

    sudo ifdown swp3
    sudo ip link set dev swp3 mtu 9192

As an alternative, add a `post-down` command in the
`/etc/network/interfaces` file to reset the MTU of the interface. For
example:

    auto swp3
    iface swp3
        alias BNBYLAB-PD01HV-01_Port3
        bridge-vids 106 109 119 141 150-151
        mtu 9192
        post-down /sbin/ip link set dev swp3 mtu 9192

#### Setting a Policy for Global System MTU

For a global policy to set MTU, create a policy document (called
`mtu.json` here) like the following:

    cat /etc/network/ifupdown2/policy.d/mtu.json
    {
     "address": {"defaults": { "mtu": "9216" }
                }
    }

{{%notice note%}}

If your platform does not support a high MTU on eth0, you can set a
lower MTU with the following command:

    cumulus@switch:~$ net add interface eth0 mtu 1500
    cumulus@switch:~$ net commit

{{%/notice%}}

{{%notice warning%}}

The policies and attributes in any file in
`/etc/network/ifupdown2/policy.d/` override the default policies and
attributes in `/var/lib/ifupdown2/policy.d/`.

{{%/notice%}}

### FEC

Forward Error Correction (FEC) is an encoding and decoding layer that
enables the switch to detect and correct bit errors introduced over the
cable between two interfaces. Because 25G transmission speeds can
introduce a higher than acceptable bit error rate (BER) on a link, FEC
is required or recommended for 25G, 4x25G, and 100G link speeds.  
The two interfaces on each end must use the same FEC setting for the
link to come up.

{{%notice note%}}

There is a very small latency overhead required for FEC. For most
applications, this small amount of latency is preferable to error packet
retransmission latency.

{{%/notice%}}

There are two FEC types:

  - Reed Solomon (**RS**), IEEE 802.3 Clause 108 (CL108) on individual
    25G channels and Clause 91 on 100G (4channels). This is the highest
    FEC algorithm, providing the best bit-error correction.
  - Base-R (**BaseR**), Fire Code (FC), IEEE 802.3 Clause 74 (CL74).
    Base-R provides less protection from bit errors than RS FEC but adds
    less latency.

There are additional FEC options for Cumulus Linux configuration:

  - Auto FEC instructs the hardware to select the best FEC. For Copper
    DAC, FEC can be negotiated with the remote end. However, optical
    modules do not have auto-negotiation capability; if the device
    chooses a preferred mode, it might not match the remote end.
  - No FEC (no error correction is done). This is the current default on
    a Broadcom switch.

{{%notice note%}}

**Important**

The Tomahawk switch does not support RS FEC or auto-negotiation of FEC
on 25G lanes that are broken out (Tomahawk pre-dates 802.3by). If you
are using a 4x25G breakout DAC or AOC on a Tomahawk switch, you can
configure either Base-R FEC or no FEC, and choose cables appropriate for
that limitation (CA-25G-S, CA-25G-N or fiber).

Tomahawk+ and Maverick switches do not have this limitation.

{{%/notice%}}

**For 25G DAC, 4x25G Breakouts DAC and 100G DAC cables**, the IEEE
802.3by specification creates 3 classes:

  - CA-25G-L (long cables - achievable cable length of at least 5m) dB
    loss less or equal to 22.48. Requires RS FEC and expects BER of 10-5
    or better with RS FEC enabled.
  - CA-25G-S (short cables - achievable cable length of at least 3m) dB
    loss less or equal to 16.48. Requires Base-R FEC and expects BER of
    10-8 or better with Base-R FEC enabled.
  - CA-25G-N (no FEC - achievable cable length of at least 3m) dB loss
    less or equal to 12.98. Does not require FEC. Expects BER 10-12 or
    better with no FEC.

The IEEE classification is based on various dB loss measurements and
minimum achievable cable length. You can build longer and shorter cables
if they comply to the dB loss and BER requirements.

If a cable is manufactured to CA-25G-S classification and FEC is not
enabled, the BER might be unacceptable in a production network. It is
important to set the FEC according to the cable class (or better) to
have acceptable bit error rates. See 
[Determining Cable Class](#determining-cable-class) below.

You can check bit errors using `cl-netstat` (`RX_ERR` column) or
`ethtool -S` (`HwIfInErrors` counter) after a large amount of traffic
has passed through the link. A non zero value indicates bit errors.
Expect error packets to be zero or extremely low compared to good
packets. If a cable has an unacceptable rate of errors with FEC enabled,
replace the cable.

For **25G, 4x25G Breakout, and 100G Fiber modules and AOCs**, there is
no classification of 25G cable types for dB loss, BER, or Length. FEC is
recommended but might not be required if the BER is low enough.

#### Determining Cable Class

You can determine the cable class from the Extended Specification
Compliance Code field (SFP28: 0Ah, byte 35, QSFP28: Page 0, byte 192) in
the cable EEPROM programming.

For 100G DAC, most manufacturers use the 0x0Bh *100GBASE-CR4 or
25GBASE-CR CA-L* value (the 100G DAC specification predates the IEEE
802.3by 25G DAC specification). RS FEC is the expected setting for 100G
DAC but might not be required with shorter or better cables.

{{%notice note%}}

A manufacturer's EEPROM setting might not match the dB loss on a cable
or the actual bit error rates that a particular cable introduces. Use
the designation as a guide, but set FEC according to the bit error rate
tolerance in the design criteria for the network. For most applications,
the highest mutual FEC ability of both end devices is the best choice.

{{%/notice%}}

You can determine for which grade the manufacturer has designated the
cable as follows.

For the **SFP28 DAC**, run the following command:

    root@mlx-2410-02:~# ethtool -m swp35 hex on | grep 0020 | awk '{ print $6}'
    0c

The values at location 0x0024 are:

  - 0x0b : CA-L (long cable - RS FEC required)
  - 0x0c : CA-S (short cable - BaseR or better FEC required)
  - 0x0d : CA-N (no FEC required)

For the **QSFP28 DAC**, run the following command:

    root@mlx-2410-02:~# ethtool -m swp51s0 hex on | grep 00c0 | awk '{print $2}'
    0b

The values at 0x00c0 are:

  - 0x0b : CA-L (long cable - RS FEC required) or 100G CR4
  - 0x0c : CA-S (short cable - BaseR or better FEC required)
  - 0x0d : CA-N (no FEC required)

**Cable Class Examples**

In each example below, the *Compliance* field is derived using the
method described above and is not visible in the `ethool -m` output.

**Example 1**: 3meter cable that does not require FEC (CA-N)  
Cost : More expensive  
Cable size : 26AWG (Note that AWG does not necessarily correspond to
overall dB loss or BER performance)  
Compliance Code : 25GBASE-CR CA-N

**Example 2**: 3meter cable that requires Base-R FEC (CA-S)  
Cost: Less expensive  
Cable size : 26AWG  
Compliance Code : 25GBASE-CR CA-S

When in doubt, consult the manufacturer directly to determine the cable
classification.

#### How Does Cumulus Linux use FEC?

The Mellanox switch enables FEC automatically first. The port firmware
tries a pre-set list of link configuration combinations to attempt to
bring up the link. It is possible to get a link up to a Mellanox switch
without enabling FEC on the remote device as the switch eventually finds
a working combination to the neighbor without FEC.

On a Broadcom switch, Cumulus Linux does not enable FEC by default.
Cumulus Networks recommends you configure FEC explicitly. On 100G DACs,
you can configure `link-autoneg` so that the port attempts to negotiate
FEC settings with the remote peer.

The following sections describe how to display the current FEC
configuration, and enable and disable FEC on a Broadcom switch.

#### Displaying the Current FEC Mode

To display the FEC mode currently enabled on a Broadcom switch, run the
following command:

    cumulus@switch:~# sudo ethtool --show-fec swp23
    FEC parameters for swp23:
    FEC encodings : None

{{%notice note%}}

On a Mellanox switch, the currently-enabled FEC mode is not accessible
with user commands at this time; however, you can deduce the mode from
the remote FEC setting when the link is up.

{{%/notice%}}

#### Enabling FEC

To enable **Reed Solomon (RS) FEC** on a link, run the following NCLU
commands:

    cumulus@switch:~# sudo net add interface swp23 link fec rs
    cumulus@switch:~# sudo net commit

To review the FEC setting on the link, run the following command:

    cumulus@switch:~# sudo ethtool --show-fec swp23
    FEC parameters for swp23:
    FEC encodings : RS

To enable **Base-R/FireCode FEC** on a link, run the following NCLU
commands:

    cumulus@switch:~# sudo net add interface swp23 link fec baser
    cumulus@switch:~# sudo net commit

To review the FEC setting on the link, run the following command:

    cumulus@switch:~# sudo ethtool --show-fec swp23
    FEC parameters for swp23:
    FEC encodings : BaseR

#### Enabling FEC with Auto-negotiation

FEC with auto-negotiation is supported on DACs only.

To enable FEC with auto-negotiation, run the following NCLU commands:

    cumulus@switch:~# sudo net add interface swp12 link autoneg on
    cumulus@switch:~# sudo net commit

To view the FEC and auto-negotiation settings, run the following
command:

    cumulus@switch:~# sudo ethtool swp12 | egrep 'FEC|auto'
    Supports auto-negotiation: Yes
    Supported FEC modes: RS
    Advertised auto-negotiation: Yes
    Advertised FEC modes: RS
    Link partner advertised auto-negotiation: Yes
    Link partner advertised FEC modes: Not reported

    cumulus@switch:~# sudo ethtool --show-fec swp12
    FEC parameters for swp12:
    FEC encodings : RS

#### Disabling FEC

To disable FEC on a link, run the following NCLU commands:

    cumulus@switch:~# sudo net add interface swp23 link fec off
    cumulus@switch:~# sudo net commit

To review the FEC setting on the link, run the following command:

    cumulus@switch:~# sudo ethtool --show-fec swp23
    FEC parameters for swp23:
    FEC encodings : None

### Interface Configuration Recommendations

The default configuration for each type of interface is described in the
following table. Except as noted below, the settings for both sides of
the link are expected to be the same.

{{%notice note%}}

If the other side of the link is running a version of Cumulus Linux
earlier than 3.2, depending up on the interface type, auto-negotiation
may not work on that switch. Cumulus Networks recommends you use the
default settings on this switch in this case.

{{%/notice%}}

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
<td><p>10/100BASE-T<br />
(RJ-45 SFP adapter)</p></td>
<td><p>On</p></td>
<td><p>N/A (does not apply at this speed)</p></td>
<td><pre><code>$ net add interface swp1 link speed 100
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 100</code></pre></td>
<td><ul>
<li><p>The module has two sets of electronics - the port side, which communicates to the switch ASIC, and the RJ-45 adapter side.</p></li>
<li><p>Auto-negotiation is always used on the RJ-45 adapter side of the link by the PHY built into the module. This is independent of the switch setting. Set <code>link-autoneg</code> to off.</p></li>
<li><p>Auto-negotiation needs to be enabled on the server side in this scenario.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>10/100BASE-T on a 1G fixed copper port</p></td>
<td><p>On</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 100
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 100</code></pre></td>
<td><ul>
<li><p>10M or 100M speeds are possible with auto-negotiation OFF on both sides. Testing on an Edgecore AS4610-54P revealed the ASIC reporting auto-negotiation as ON.</p></li>
<li><p><a href="/cumulus-linux-36/System-Configuration/Power-over-Ethernet-PoE">Power over Ethernet</a> may require auto-negotiation to be ON.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>1000BASE-T<br />
(RJ-45 SFP adapter)</p></td>
<td><p>On</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 1000
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 1000</code></pre></td>
<td><ul>
<li><p>The module has two sets of electronics - the port side, which communicates to the switch ASIC, and the RJ-45 side.</p></li>
<li><p>Auto-negotiation is always used on the RJ-45 side of the link by the PHY built into the module. This is independent of the switch setting. Set <code>link-autoneg</code> to off.</p></li>
<li><p>Auto-negotiation needs to be enabled on the server side.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>1000BASE-T on a 1G fixed copper port</p></td>
<td><p>On</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 1000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 1000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>1000BASE-T on a 10G fixed copper port</p></td>
<td><p>On</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 1000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 1000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>1000BASE-SX,<br />
1000BASE-LX,<br />
1000BASE-CX<br />
(1G Fiber)</p></td>
<td><p>Recommended On</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on</code></pre></td>
<td><ul>
<li><p>Without auto-negotiation, the link stays up when there is a single fiber break.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>10GBASE-T fixed copper port</p></td>
<td><p>On</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 10000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 10000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>10GBASE-CR,<br />
10GBASE-LR,<br />
10GBASE-SR,<br />
10G AOC</p></td>
<td><p>Off</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 10000
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 10000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>40GBASE-CR4</p></td>
<td><p>Recommended On</p></td>
<td><p>Disable it</p></td>
<td><pre><code>$ net add interface swp1 link speed 40000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 40000</code></pre></td>
<td><ul>
<li><p>40G standards mandate auto-negotiation should be enabled for DAC connections.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>40GBASE-SR4,<br />
40GBASE-LR4,<br />
40G AOC</p></td>
<td><p>Off</p></td>
<td><p>Disable it</p></td>
<td><pre><code>$ net add interface swp1 link speed 40000
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 40000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>100GBASE-CR4</p></td>
<td><p>On</p></td>
<td><p>auto-negotiated</p></td>
<td><pre><code>$ net add interface swp1 link speed 100000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 100000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>100GBASE-SR4,<br />
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
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>100GBASE-LR4</p></td>
<td><p>Off</p></td>
<td><p>None stated</p></td>
<td><pre><code>$ net add interface swp1 link speed 100000
$ net add interface swp1 link autoneg off
$ net add interface swp1 link fec off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 100000
  link-fec off</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>25GBASE-CR</p></td>
<td><p>On</p></td>
<td><p>auto-negotiated*</p></td>
<td><pre><code>$ net add interface swp1 link speed 25000
$ net add interface swp1 link autoneg on</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg on
  link-speed 25000</code></pre></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>25GBASE-SR</p></td>
<td><p>Off</p></td>
<td><p>RS*</p></td>
<td><pre><code>$ net add interface swp1 link speed 25000
$ net add interface swp1 link autoneg off
$ net add interface swp1 link fec baser</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 25000
  link-fec baser</code></pre></td>
<td><ul>
<li><p>Tomahawk cannot do RS on a single channel, only BASE-R/FC/FireCode/Type74, which violates the 802.3by specification for 25G.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>25GBASE-LR</p></td>
<td><p>Off</p></td>
<td><p>None stated</p></td>
<td><pre><code>$ net add interface swp1 link speed 25000
$ net add interface swp1 link autoneg off
$ net add interface swp1 link fec off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 25000
  link-fec off</code></pre></td>
<td><p> </p></td>
</tr>
</tbody>
</table>

### Creating a Default Policy for Various Interface Settings

Instead of configuring these settings for each individual interface, you
can specify a policy for all interfaces on a switch, or tailor custom
settings for each interface. Create a file in
`/etc/network/ifupdown2/policy.d/`, like in the following example
(called `address.json`), and populate the settings accordingly:

    cumulus@switch:~$ cat /etc/network/ifupdown2/policy.d/address.json
    { 
        "ethtool": {
            "defaults": {
                "link-duplex": "full"
            },
            "iface_defaults": {
                "swp1": {
                    "link-autoneg": "on", 
                    "link-speed": "1000"
                },
                "swp16": {
                    "link-autoneg": "off",
                    "link-speed": "10000"
                },
                "swp50": {
                    "link-autoneg": "off",
                    "link-speed": "100000",
                    "link-fec": "rs"
                }
            }
        },
        "address": {
            "defaults": { "mtu": "9000" }
        }
    }

## Configuring Breakout Ports

Cumulus Linux has the ability to:

  - Break out 100G switch ports into the following with breakout cables:
      - 2x50G, 4x25G, 4x10G
  - Break out 40G switch ports into four separate 10G ports for use with
    breakout cables.
  - Combine (also called *aggregating* or *ganging*) four 10G switch
    ports into one 40G port for use with a breakout cable ([not to be
    confused with a
    bond](/cumulus-linux-36/Layer-2/Bonding-Link-Aggregation)).

To configure a 4x25G breakout port, first configure the port to break
out then set the link speed:

    cumulus@switch:~$ net add interface swp3 breakout 4x
    cumulus@switch:~$ net add interface swp3s0-3 link speed 25000
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create 4 interfaces in the `/etc/network/interfaces` file
named as follows:

    cumulus@switch:~$ cat /etc/network/interfaces
     
    ...
     
    auto swp3s0
    iface swp3s0
     
    auto swp3s1
    iface swp3s1
     
    auto swp3s2
    iface swp3s2
     
    auto swp3s3
    iface swp3s3
     
    ...

{{%notice note%}}

On [Dell switches with Maverick ASICs](https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/),
you configure breakout ports on the 100G uplink ports by manually
editing the `/etc/cumulus/ports.conf` file. You need to specify either
*4x10* or *4x25* for the port speed. For example, on a Dell S4148F-ON
switch, to break out swp26 into 4 25G ports, you would modify the line
starting with "26=" in `ports.conf` as follows:

    cumulus@switch:~$ sudo nano /etc/cumulus/ports.conf
     
    ...
     
    # QSFP+ ports
    #
    # <port label 27-28> = [4x10G|40G]
     
    27=disabled
    28=disabled
     
    # QSFP28 ports
    #
    # <port label 25-26, 29-30> = [4x10G|4x25G|2x50G|40G|50G|100G]
     
    25=100G
    26=4x25G
    29=100G
    30=100G
     
    ...

Then you need to configure the breakout ports in the
`/etc/network/interfaces` file:

    cumulus@switch:~$ sudo nano /etc/network/interfaces
     
    ...
     
    auto swp26s0
    iface swp26s0
     
    auto swp26s1
    iface swp3s1
     
    auto swp26s2
    iface swp26s2
     
    auto swp26s3
    iface swp26s3
     
    ...

You cannot use NCLU to break out the uplink ports.

{{%/notice%}}

{{%notice note%}}

On Mellanox switches, you need to disable the next port (see below). In
this example, you would also run the following before committing the
update:

    cumulus@switch:~$ net add interface swp4 breakout disabled

{{%/notice%}}

{{%notice note%}}

When you commit your change configuring the breakout ports, `switchd`
restarts to apply the changes. The restart 
[interrupts network services](/cumulus-linux-36/System-Configuration/Configuring-switchd/#configuring-switchd-parameters).

{{%/notice%}}

The breakout port configuration is stored in the
`/etc/cumulus/ports.conf` file.

{{%notice info%}}

`/etc/cumulus/ports.conf` varies across different hardware platforms.
Check the current list of supported platforms on [the hardware
compatibility list](http://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list).

A snippet from the `/etc/cumulus/ports.conf` on a Dell S6000 switch
(with a Trident II+ ASIC) where swp6 is broken out looks like this:

    cumulus@switch:~$ cat /etc/cumulus/ports.conf 
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
    # QSFP+ ports
    #
    # <port label 1-32> = [4x10G|40G|disabled]
    1=40G
    2=40G
    3=40G
    4=40G
    5=40G
    6=4x
    7=40G
    8=40G
    9=40G
    10=40G
    11=40G
    12=40G
    13=40G
    14=40G
    15=40G
    16=40G
    17=40G
    18=40G
    19=40G
    20=40G
    21=40G
    22=40G
    23=40G
    24=40G
    25=40G
    26=40G
    27=40G
    28=40G
    29=40G
    30=40G
    31=40G
    32=40G

For switches with ports that support 100G speeds, you can break out any
100G port into a variety of options: four 10G ports, four 25G ports, two
40G ports or two 50G ports. Keep in mind that you cannot have more than
128 total logical ports on a Broadcom switch.

{{%notice info%}}

The Mellanox SN2700, SN2700B, SN2410, and SN2410B switches both have a
limit of 64 logical ports in total. However, if you want to break out to
4x25G or 4x10G, you must configure the logical ports as follows:

  - You can only break out odd-numbered ports into 4 logical ports.
  - You must disable the next even-numbered port.

These restrictions do not apply to a 2x50G breakout configuration.

For example, if you have a 100G Mellanox SN2700 switch and break out
port 11 into 4 logical ports, you must disable port 12 by running `net
add interface swp12 breakout disabled`, which results in this
configuration in `/etc/cumulus/ports.conf`:

    ...
     
    11=4x
    12=disabled
     
    ...

There is no limitation on any port if interfaces are configured in 2x50G
mode.

{{%/notice%}}

{{%/notice%}}

{{%notice tip%}}

Here is an example showing how to configure breakout cables for the
[Mellanox Spectrum SN2700](https://community.mellanox.com/s/article/howto-configure-breakout-cables-40g---gt--4x10g-using-cumulus-linux).

{{%/notice%}}

### Removing a Breakout Port

To remove a breakout port, you need to do the following:

1.  Remove the breakout port interfaces using NCLU, then commit the
    change. Continuing with the original example:
    
        cumulus@switch:~$ net del interface swp3s0
        cumulus@switch:~$ net del interface swp3s1
        cumulus@switch:~$ net del interface swp3s2
        cumulus@switch:~$ net del interface swp3s3
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit

2.  Manually edit the `/etc/cumulus/ports.conf` file to configure the
    interface for the original speed, then save your changes:
    
        cumulus@switch:~$ sudo nano /etc/cumulus/ports.conf 
         
        ...
         
        2=100G
        3=100G
        4=100G
         
        ...
         

3.  [Restart `switchd`](/cumulus-linux-36/System-Configuration/Configuring-switchd/#configuring-switchd-parameters).

### Combining Four 10G Ports into One 40G Port

You can *gang* (aggregate) four 10G ports into one 40G port for use with
a breakout cable, provided you follow these requirements:

  - You must gang four 10G ports in sequential order. For example, you
    cannot gang swp1, swp10, swp20 and swp40 together.
  - The ports must be in increments of four, with the starting port
    being swp1 (or swp5, swp9, or so forth); so you cannot gang swp2,
    swp3, swp4 and swp5 together.

For example, to gang swp1 through swp4 into a 40G port, run:

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

## Logical Switch Port Limitations

100G and 40G switches can support a certain number of logical ports,
depending upon the manufacturer; these include:

  - Mellanox SN2700 and SN2700B switches
  - Switches with Broadcom Tomahawk, Trident II and Trident II+ chipsets
    (check the [HCL](https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/))

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

The means the maximum number of ports for this Dell S6000 is 104.

Mellanox SN2700 and SN2700B switches have a limit of 64 logical ports in
total. However, the logical ports must be configured in a specific way.
See [the note](#configuring-breakout-ports) above.

## Using ethtool to Configure Interfaces

The Cumulus Linux `ethtool` command is an alternative for configuring
interfaces as well as viewing and troubleshooting them.

For example, to manually set link speed, auto-negotiation, duplex mode
and FEC on swp1, run:

    cumulus@switch:~$ sudo ethtool -s swp1 speed 25000 autoneg off duplex full
    cumulus@switch:~$ sudo ethtool --set-fec swp1 encoding off

To view the FEC setting on an interface, run:

    cumulus@switch:~$ sudo ethtool --show-fec swp1FEC parameters for swp1:
    Auto-negotiation: off
    FEC encodings : RS

## Verification and Troubleshooting Commands

### Statistics

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

### Querying SFP Port Information

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

## Caveats and Errata

### Timeout Error on Quanta LY8 and LY9 Switches

On Quanta T5048-LY8 and T3048-LY9 switches, an "Operation timed out"
error occurs while removing and reinserting QSFP module.

The QSFPx2 module cannot be removed while the switch is powered on, as
it is not hot-swappable. However, if this occurs, you can get the link
to come up; however, this involves 
[restarting `switchd`](/cumulus-linux-36/System-Configuration/Configuring-switchd/#configuring-switchd-parameters), 
which disrupts your network.

On the T3048-LY9, run the following commands:

    cumulus@switch:~$ sudo echo 0 > qsfpd_power_enable/value
    cumulus@switch:~$ sudo rmmod quanta_ly9_rangeley_platform 
    cumulus@switch:~$ sudo modprobe quanta_ly9_rangeley_platform
    cumulus@switch:~$ sudo systemctl restart switchd.service

On the T5048-LY8, run the following commands:

    cumulus@switch:~$ sudo echo 0 > qsfpd_power_enable/value
    cumulus@switch:~$ sudo systemctl restart switchd.service

### swp33 and swp34 Disabled on Some Switches

The front SFP+ ports (swp33 and swp34) are disabled in Cumulus Linux on
the following switches:

  - Dell Z9100-ON
  - Penguin Arctica 3200-series switches (the 3200C, 3200XL and 3200XLP)
  - Supermicro SSE-C3632S

These ports appear as disabled in the `/etc/cumulus/ports.conf` file.

### ethtool Shows Incorrect Port Speed on 100G Mellanox Switches

After setting interface speed to 40G by editing the `ports.conf` file on
a Mellanox switch, `ethtool` still shows the speed as 100G.

This is a known issue whereby `ethtool` does not update after restarting
`switchd`, so it continues to display the outdated port speed.

To correctly set the port speed, use
[NCLU](/cumulus-linux-36/System-Configuration/Network-Command-Line-Utility-NCLU/)
or `ethtool` to set the speed instead of hand editing the `ports.conf`
file.

For example, to set the speed to 40G using NCLU:

    cumulus@switch:~$ net add interface swp1 link speed 40000 

Or using `ethtool`:

    cumulus@switch:~$ sudo ethtool -s swp1 speed 40000 

## Related Information

  - [Debian - Network Configuration](http://wiki.debian.org/NetworkConfiguration)
  - [Linux Foundation - VLANs](http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan)
  - [Linux Foundation - Bridges](http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge)
  - [Linux Foundation - Bonds](http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding)
