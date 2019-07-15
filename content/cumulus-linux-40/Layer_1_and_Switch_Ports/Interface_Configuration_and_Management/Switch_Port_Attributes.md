---
title: Switch Port Attributes
author: Cumulus Networks
weight: 309
aliases:
 - /display/DOCS/Switch+Port+Attributes
 - /pages/viewpage.action?pageId=8363026
pageID: 8363026
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
Cumulus Linux exposes network interfaces for several types of physical
and logical devices:

  - lo, network loopback device

  - ethN, switch management port(s), for out of band management only

  - swpN, switch front panel ports

  - (optional) brN, bridges (IEEE 802.1Q VLANs)

  - (optional) bondN, bonds (IEEE 802.3ad link aggregation trunks, or
    port channels)

Each physical network interface has a number of configurable settings:

  - [Auto-negotiation](http://en.wikipedia.org/wiki/Autonegotiation)

  - [Duplex](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29)

  - [FEC](https://en.wikipedia.org/wiki/Forward_error_correction)
    (Forward error correction)

  - Link speed

  - MTU, or [maximum transmission
    unit](https://en.wikipedia.org/wiki/Maximum_transmission_unit)

Most of these settings are configured automatically for you, depending
upon your switch ASIC, although you must always set MTU manually.

{{%notice note%}}

You can only set MTU for logical interfaces. If you try to set
auto-negotiation, duplex mode, or link speed for a logical interface, an
unsupported error is shown.

{{%/notice%}}

<span style="color: #333333;"> For </span> **Mellanox switches**, MTU is
the only port attribute you can directly configure. The Mellanox
firmware configures FEC, link speed, duplex mode and auto-negotiation
automatically, following a predefined list of parameter settings until
the link comes up. However, you can disable FEC if necessary, which
forces the firmware to not try any FEC options.

For **Broadcom-based switches,** Cumulus Networks recommends that you
enable auto-negotiation on each port. When enabled, Cumulus Linux
automatically configures the best link parameter settings based on the
module type (speed, duplex, auto-negotiation, and FEC where supported).
To understand the default configuration for the various port and cable
types, see the [table
below](#src-8363026_SwitchPortAttributes-settings). If you need to
troubleshoot further to bring the link up, follow the sections below to
set the specific link parameters.

## <span id="src-8363026_SwitchPortAttributes-autoneg_enable" class="confluence-anchor-link"></span><span>Auto-negotiation</span>

To configure auto-negotiation for a Broadcom-based switch, set
`link-autoneg` to *on* for all the switch ports. For example, to enable
auto-negotiation for swp1 through swp52:

    cumulus@switch:~$ net add interface swp1-52 link autoneg on
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

Any time you enable auto-negotiation, Cumulus Linux restores the default
configuration settings specified in the [table
below](#src-8363026_SwitchPortAttributes-sett).

By default on a Broadcom-based switch, auto-negotiation is disabled —
except on 10G and 1000BASE-T fixed copper switch ports, where it is
required for links to work. For RJ-45 SFP adapters, you need to manually
configure the desired link speed and auto-negotiation as described in
the [default settings table
below](#src-8363026_SwitchPortAttributes-settings).

If you disable auto-negotiation later or never enable it, then you have
to configure any settings that deviate from the port default — such as
duplex mode, FEC, and link speed settings.

{{%notice warning%}}

Some module types support auto-negotiation while others do not. To
enable a simpler configuration, Cumulus Linux allows you to configure
auto-negotiation on all port types on Broadcom switches; the port
configuration software then configures the underlying hardware according
to its capabilities.

If you do decide to disable auto-negotiation, be aware of the following:

  - You must manually set any non-default link speed, duplex, pause, and
    FEC.

  - Disabling auto-negotiation on a 1G optical cable prevents detection
    of single fiber breaks.

  - You cannot disable auto-negotiation on 1GT or 10GT fixed copper
    switch ports.

For 1000BASE-T RJ-45 SFP adapters, auto-negotiation is automatically
done on the SFP PHY, so enabling auto-negotiation on the port settings
is not required. You must manually configure these ports using the
[settings below](#src-8363026_SwitchPortAttributes-settings).

{{%/notice%}}

Depending upon the connector used for a port, enabling auto-negotiation
also enables forward error correction (FEC), if the cable requires it
(see the [table below](#src-8363026_SwitchPortAttributes-settings)). The
correct FEC mode is set based on the speed of the cable when
auto-negotiation is enabled.

## <span>Port Speed and Duplex Mode</span>

Cumulus Linux supports both half- and
[full-duplex](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29)
configurations. The duplex mode setting defaults to *full*. You only
need to specify `link duplex` if you want half-duplex mode.

Supported port speeds include 100M, 1G, 10G, 25G, 40G, 50G and 100G. If
you need to manually set the speed on a Broadcom-based switch, set it in
terms of Mbps, where the setting for 1G is *1000*, 40G is *40000* and
100G is *100000*, for example.

You can configure ports to one speed less than their maximum speed.

| Switch Port Type | Lowest Configurable Speed                                 |
| ---------------- | --------------------------------------------------------- |
| 1G               | 100 Mb                                                    |
| 10G              | 1 Gigabit (1000 Mb)                                       |
| 40G              | 10G\*                                                     |
| 100G             | 50G\* & 40G (with or without breakout port), 25G\*, 10G\* |

\*Requires the port to be converted into a breakout port. See
[Configuring Breakout Ports](#src-8363026_SwitchPortAttributes-breakout)
below.

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

{{%notice note%}}

**Platform Limitations**

  - On Lenovo NE2572O switches, swp1 thru swp8 only support 25G speed.

  - For 10G and 1G SFPs inserted in a 25G port on a Broadcom platform,
    you must edit the `/etc/cumulus/ports.conf` file and configure the
    four ports in the same core to be 10G. See [Caveats and
    Errata](#src-8363026_SwitchPortAttributes-caveats) below.

{{%/notice%}}

## <span id="src-8363026_SwitchPortAttributes-mtu" class="confluence-anchor-link"></span><span>MTU</span>

Interface MTU ([maximum transmission
unit](https://en.wikipedia.org/wiki/Maximum_transmission_unit)) applies
to traffic traversing the management port, front panel/switch ports,
bridge, VLAN subinterfaces and bonds — in other words, both physical and
logical interfaces.

MTU is the only interface setting that you must set manually.

In Cumulus Linux, `ifupdown2` assigns 1500 as the default MTU setting.
To change the setting, run:

    cumulus@switch:~$ net add interface swp1 mtu 9000
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

Some switches might not support the same maximum MTU setting in hardware
for both the management interface (eth0) and the data plane ports.

{{%/notice%}}

### <span id="src-8363026_SwitchPortAttributes-global_mtu" class="confluence-anchor-link"></span><span>Set a Policy for Global System MTU</span>

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

### <span>MTU for a Bridge</span>

The MTU setting is the lowest MTU setting of any interface that is a
member of that bridge (every interface specified in `bridge-ports` in
the bridge configuration in the `interfaces` file), even if another
bridge member has a higher MTU value. There is **no** need to specify an
MTU on the bridge. Consider this bridge configuration:

    auto bridge
    iface bridge
        bridge-ports bond1 bond2 bond3 bond4 peer5
        bridge-vids 100-110
        bridge-vlan-aware yes

For *bridge* to have an MTU of 9000, set the MTU for each of the member
interfaces (bond1 to bond 4, and peer5), to 9000 at minimum.

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
from swp1. Therefore, specifying an MTU on swp1 ensures that swp1.100
inherits the MTU setting for swp1.

<span id="src-8363026_SwitchPortAttributes-mtu_vxlan"></span>If you are
working with [VXLANs](/cumulus-linux/Network_Virtualization/), the MTU
for a virtual network interface (VNI) must be 50 bytes smaller than the
MTU of the physical interfaces on the switch, as those 50 bytes are
required for various headers and other data. Also, consider setting the
MTU much higher than the default 1500.

{{%notice info%}}

**Example MTU Configuration**

In general, the policy file specified above handles default MTU settings
for all interfaces on the switch. If you need to configure a different
MTU setting for a subset of interfaces, use
[NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU).

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
conversation path. MTU mismatches result in dropped or truncated
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

To view the MTU setting, run the ` net show interface <interface>
 `command:

    cumulus@switch:~$ net show interface swp1
        Name    MAC                Speed      MTU  Mode
    --  ------  -----------------  -------  -----  ---------
    UP  swp1    44:38:39:00:00:04  1G        1500  Access/L2

### <span>Bring Down an Interface for a Bridge Member</span>

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

## <span>FEC</span>

[Forward Error Correction
(FEC)](https://en.wikipedia.org/wiki/Forward_error_correction) is an
encoding and decoding layer that enables the switch to detect and
correct bit errors introduced over the cable between two interfaces.
Because 25G transmission speeds can introduce a higher than acceptable
bit error rate (BER) on a link, FEC is required or recommended for 25G,
4x25G, and 100G link speeds. In order for the link to come up, the two
interfaces on each end must use the same FEC setting.

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

  - Auto FEC instructs the hardware to select the best FEC. For copper
    DAC, FEC can be negotiated with the remote end. However, optical
    modules do not have auto-negotiation capability; if the device
    chooses a preferred mode, it might not match the remote end. This is
    the current default on a Mellanox switch.

  - No FEC (no error correction is done). This is the current default on
    a Broadcom switch.

{{%notice note%}}

**Important**

The Tomahawk switch does not support RS FEC or auto-negotiation of FEC
on 25G lanes that are broken out (Tomahawk pre-dates 802.3by). If you
are using a 4x25G breakout DAC or AOC on a Tomahawk switch, you can
configure either Base-R FEC or no FEC, and choose cables appropriate for
that limitation (CA-25G-S, CA-25G-N or fiber).

Tomahawk+, Tomahawk2, Trident3, and Maverick switches do not have this
limitation.

{{%/notice%}}

{{%notice note%}}

You cannot set RS FEC on any Trident II switch with either NCLU or by
directly editing the `/etc/network/interfaces` file.

{{%/notice%}}

For **25G DAC, 4x25G Breakouts DAC and 100G DAC cables**, the IEEE
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
have acceptable bit error rates. See [Determining Cable
Class](#src-8363026_SwitchPortAttributes-cable_class) below.

You can check bit errors using `cl-netstat` (`RX_ERR` column) or
`ethtool -S` (`HwIfInErrors` counter) after a large amount of traffic
has passed through the link. A non-zero value indicates bit errors.
Expect error packets to be zero or extremely low compared to good
packets. If a cable has an unacceptable rate of errors with FEC enabled,
replace the cable.

For **25G, 4x25G Breakout, and 100G Fiber modules and AOCs**, there is
no classification of 25G cable types for dB loss, BER or length. FEC is
recommended but might not be required if the BER is low enough.

### <span id="src-8363026_SwitchPortAttributes-cable_class" class="confluence-anchor-link"></span><span>Determine Cable Class of 100G and 25G DACs</span>

You can determine the cable class for 100G and 25G DACs from the
Extended Specification Compliance Code field (SFP28: 0Ah, byte 35,
QSFP28: Page 0, byte 192) in the cable EEPROM programming.

For 100G DACs, most manufacturers use the 0x0Bh *100GBASE-CR4 or
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

    cumulus@switch:~$ sudo ethtool -m swp35 hex on | grep 0020 | awk '{ print $6}'
    0c

The values at location 0x0024 are:

  - 0x0b : CA-L (long cable - RS FEC required)

  - 0x0c : CA-S (short cable - BaseR or better FEC required)

  - 0x0d : CA-N (no FEC required)

For the **QSFP28 DAC**, run the following command:

    cumulus@switch:~$ sudo ethtool -m swp51s0 hex on | grep 00c0 | awk '{print $2}'
    0b

The values at 0x00c0 are:

  - 0x0b : CA-L (long cable - RS FEC required) or 100G CR4

  - 0x0c : CA-S (short cable - BaseR or better FEC required)

  - 0x0d : CA-N (no FEC required)

In each example below, the *Compliance* field is derived using the
method described above and is not visible in the `ethool -m` output.

{{%notice info%}}

****Cable Class** Example 1**: 3meter cable that does not require FEC
(CA-N)  
Cost : More expensive  
Cable size : 26AWG (Note that AWG does not necessarily correspond to
overall dB loss or BER performance)  
Compliance Code : 25GBASE-CR CA-N

{{%/notice%}}

{{%notice info%}}

****Cable Class** Example 2**: 3meter cable that requires Base-R FEC
(CA-S)  
Cost: Less expensive  
Cable size : 26AWG  
Compliance Code : 25GBASE-CR CA-S

{{%/notice%}}

When in doubt, consult the manufacturer directly to determine the cable
classification.

### <span>How Does Cumulus Linux use FEC?</span>

This depends upon the make of the switch you are using.

A Mellanox switch enables FEC automatically when it powers up; that is,
the setting is `fec auto`. The port firmware tests and determines the
correct FEC mode to bring the link up with the neighbor. It is possible
to get a link up to a Mellanox switch without enabling FEC on the remote
device as the switch eventually finds a working combination to the
neighbor without FEC.

On a Broadcom switch, Cumulus Linux does not enable FEC by default; that
is, the setting is `fec off`. Cumulus Networks recommends you configure
FEC explicitly to match the configured FEC on the link neighbor. On 100G
DACs, you can configure `link-autoneg` so that the port attempts to
negotiate FEC settings with the remote peer.

The following sections describe how to show the current FEC mode, and to
enable and disable FEC.

### <span>Show the Current FEC Mode</span>

Cumulus Linux returns different output for the `ethtool --show-fec`
command, depending upon whether you are using a Broadcom or Mellanox
switch.

On a Broadcom switch, the `--show-fec` output tells you exactly what you
configured, even if the link is down due to a FEC mismatch with the
neighbor.

On a Mellanox switch, the `--show-fec` output tells you the current
active state of FEC **only if the link is up**; that is, if the FEC
modes matches that of the neighbor. If the link is not up, the value
displays *None*, which is not valid.

To display the FEC mode currently enabled on a given switch port, run
the following command:

    cumulus@switch:~$ sudo ethtool --show-fec swp23
    FEC parameters for swp23:
    FEC encodings : None

### <span>Enable or Disable FEC</span>

To enable **Reed Solomon (RS) FEC** on a link, run the following NCLU
commands:

    cumulus@switch:~$ sudo net add interface swp23 link fec rs
    cumulus@switch:~$ sudo net commit

To review the FEC setting on the link, run the following command:

    cumulus@switch:~$ sudo ethtool --show-fec swp23
    FEC parameters for swp23:
    FEC encodings : RS

To enable **Base-R/FireCode FEC** on a link, run the following NCLU
commands:

    cumulus@switch:~$ sudo net add interface swp23 link fec baser
    cumulus@switch:~$ sudo net commit

To review the FEC setting on the link, run the following command:

    cumulus@switch:~$ sudo ethtool --show-fec swp23
    FEC parameters for swp23:
    FEC encodings : BaseR

{{%notice note%}}

FEC with auto-negotiation is supported on DACs only.

{{%/notice%}}

To enable FEC with auto-negotiation, run the following NCLU commands:

    cumulus@switch:~$ sudo net add interface swp12 link autoneg on
    cumulus@switch:~$ sudo net commit

To view the FEC and auto-negotiation settings, run the following
command:

    cumulus@switch:~$ sudo ethtool swp12 | egrep 'FEC|auto'
    Supports auto-negotiation: Yes
    Supported FEC modes: RS
    Advertised auto-negotiation: Yes
    Advertised FEC modes: RS
    Link partner advertised auto-negotiation: Yes
    Link partner advertised FEC modes: Not reported

    cumulus@switch:~$ sudo ethtool --show-fec swp12
    FEC parameters for swp12:
    FEC encodings : RS

<span style="color: #333333;"> To disable FEC on a link, run the
following NCLU commands: </span>

    cumulus@switch:~$ sudo net add interface swp23 link fec off
    cumulus@switch:~$ sudo net commit

To review the FEC setting on the link, run the following command:

    cumulus@switch:~$ sudo ethtool --show-fec swp23
    FEC parameters for swp23:
    FEC encodings : None

## <span id="src-8363026_SwitchPortAttributes-settings" class="confluence-anchor-link"></span><span>Interface Configuration Recommendations for Broadcom Platforms</span>

The recommended configuration for each type of interface is described in
the following table. These are the link settings that are applied to the
port hardware when auto-negotiation is enabled on a Broadcom-based
switches. If further troubleshooting is required to bring a link up, use
the table below as a guide to set the link parameters.

Except as noted below, the settings for both sides of the link are
expected to be the same.

{{%notice note%}}

Mellanox switches automatically configure these settings following a
predefined list of parameter settings until the link comes up.

{{%/notice%}}

{{%notice note%}}

If the other side of the link is running a version of Cumulus Linux
earlier than 3.2, depending upon the interface type, auto-negotiation
may not work on that switch. Cumulus Networks recommends you use the
recommended settings as show below on this switch in this case.

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
<th><p>Speed/Type</p></th>
<th><p>Auto-negotiation</p></th>
<th><p>FEC Setting</p></th>
<th><p>Manual Configuration Steps</p></th>
<th><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>100BASE-T<br />
(RJ-45 SFP Module)</p></td>
<td><p>Off</p></td>
<td><p>N/A (does not apply at this speed)</p></td>
<td><pre><code>$ net add interface swp1 link speed 100
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 100</code></pre></td>
<td><ul>
<li><p>The module has two sets of electronics — the port side, which communicates to the switch ASIC, and the RJ-45 adapter side.</p></li>
<li><p>Auto-negotiation is always used on the RJ-45 adapter side of the link by the PHY built into the module. This is independent of the switch setting. Set <code>link-autoneg</code> to off.</p></li>
<li><p>Auto-negotiation needs to be enabled on the server side in this scenario.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>100BASE-T on a 1G fixed copper port</p></td>
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
<li><p><a href="/cumulus-linux/System_Configuration/Power_over_Ethernet_-_PoE">Power over Ethernet</a> may require auto-negotiation to be ON.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>1000BASE-T<br />
(RJ-45 SFP Module)</p></td>
<td><p>Off</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 1000
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 1000</code></pre></td>
<td><ul>
<li><p>The module has two sets of electronics — the port side, which communicates to the switch ASIC, and the RJ-45 side.</p></li>
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
<td><p> </p></td>
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
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>1000BASE-SX,<br />
1000BASE-LX,<br />
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
</ul>
<p>See the limitation discussed in <a href="#src-8363026_SwitchPortAttributes-10Gand1GSFPsInsertedina25GPort">10G and 1G SFPs Inserted in a 25G Port</a>, below</p></td>
</tr>
<tr class="odd">
<td><p>10GBASE-T<br />
(RJ-45 SFP Module)</p></td>
<td><p>Off</p></td>
<td><p>N/A</p></td>
<td><pre><code>$ net add interface swp1 link speed 10000
$ net add interface swp1 link autoneg off</code></pre>
<pre><code>auto swp1
iface swp1
  link-autoneg off
  link-speed 10000</code></pre></td>
<td><ul>
<li><p>The module has two sets of electronics — the port side, which communicates to the switch ASIC and the RJ-45 side.</p></li>
<li><p>Auto-negotiation is always used on the RJ-45 side of the link by the PHY built into the module. This is independent of the switch setting. Set link-autoneg to off.</p></li>
<li><p>Auto-negotiation needs to be enabled on the server side.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>10GBASE-T fixed copper port</p></td>
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
<td><p> </p></td>
</tr>
<tr class="even">
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
<tr class="odd">
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
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>100GBASE-CR4</p></td>
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
<td><p> </p></td>
</tr>
<tr class="even">
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
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>25GBASE-CR</p></td>
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
<tr class="even">
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
<tr class="odd">
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
<td><p> </p></td>
</tr>
</tbody>
</table>

## <span>Default Policies for Interface Settings</span>

Instead of configuring these settings for each individual interface, you
can specify a policy for all interfaces on a switch, or tailor custom
settings for each interface. Create a file in
`/etc/network/ifupdown2/policy.d/` and populate the settings
accordingly. The following example shows a file called `address.json.`

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
            "iface_defaults": {
                "eth0": {"mtu": "1500"}
            }
        }
    }

{{%notice note%}}

Setting the default MTU also applies to the management interface. Be
sure to add the *iface\_defaults* to override the MTU for eth0, to
remain at 1500.

{{%/notice%}}

## <span id="src-8363026_SwitchPortAttributes-breakout" class="confluence-anchor-link"></span><span>Breakout Ports</span>

Cumulus Linux has the ability to:

  - Break out 100G switch ports into the following with breakout cables:
    
      - 2x50G, 2x40G, 4x25G, 4x10G

  - Break out 40G switch ports into four separate 10G ports for use with
    breakout cables.

  - Combine (also called *aggregating* or *ganging*) four 10G switch
    ports into one 40G port for use with a breakout cable ([not to be
    confused with a
    bond](/cumulus-linux/Layer_2/Bonding_-_Link_Aggregation)).

To configure a 4x25G breakout port, first configure the port to break
out then set the link speed:

    cumulus@switch:~$ net add interface swp3 breakout 4x25G
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

On Mellanox switches, you need to disable the next port (see below). In
this example, you must run the following before committing the update
with `net commit`:

    cumulus@switch:~$ net add interface swp4 breakout disabled

Also, [see below](#src-8363026_SwitchPortAttributes-mlnx_breakout) for
how to configure breakout ports on Mellanox switches.

{{%/notice%}}

These commands break out the 100G interfaces to 4x25G interfaces in the
`/etc/cumulus/ports.conf` file, restart the `switchd` process to
reconfigure the ports and create four interfaces in the
`/etc/network/interfaces` file named as follows:

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

When you commit your change configuring the breakout ports, `switchd`
restarts to apply the changes. The restart [interrupts network
services](Configuring_switchd.html#src-8362561_Configuringswitchd-restartswitchd).

{{%/notice%}}

The breakout port configuration is stored in the
`/etc/cumulus/ports.conf` file.

{{%notice info%}}

The`  /etc/cumulus/ports.conf ` file varies across different hardware
platforms. Check the current list of supported platforms on [the
hardware compatibility list](http://www.cumulusnetworks.com/hcl).

A snippet from the `/etc/cumulus/ports.conf` file on a Dell S6000 switch
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

{{%/notice%}}

### <span>Break out a 100G Port to Four 10G Ports</span>

If you want to support 10G speed modules or cables on 100G ports you
must set up the port in 10G mode first by configuring breakout ports on
the 100G ports using the following NCLU commands:

    cumulus@switch:~$ net add interface swp25 breakout 4x10G
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

### <span>Remove a Breakout Port</span>

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
         

3.  [Restart
    `switchd`](Configuring_switchd.html#src-8362561_Configuringswitchd-restartswitchd).

### <span>Combine Four 10G Ports into One 40G Port</span>

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

## <span>Logical Switch Port Limitations</span>

100G and 40G switches can support a certain number of logical ports,
depending upon the manufacturer; these include:

  - Mellanox SN2700, SN2700B, SN2410 and SN2410B switches

  - Switches with Broadcom Tomahawk, Trident II, Trident II+ and
    Trident3 chipsets (check the
    [HCL](http://cumulusnetworks.com/support/linux-hardware-compatibility-list/))

You *cannot* have more than 128 total logical ports on a Broadcom
switch.

The Mellanox SN2700, SN2700B, SN2410 and SN2410B switches all have a
limit of 64 logical ports in total.

<span style="color: #333333;"> Before you configure any logical/unganged
ports on a switch, check the limitations listed in </span>
`/etc/cumulus/ports.conf` <span style="color: #333333;"> ; this file is
specific to each manufacturer. </span>

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

### <span id="src-8363026_SwitchPortAttributes-mlnx_breakout" class="confluence-anchor-link"></span><span>Mellanox Logical Port Limits and Breakout Configurations</span>

The Mellanox SN2700, SN2700B, SN2410 and SN2410B switches all have a
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

{{%notice tip%}}

Here is an example showing how to configure breakout cables for the
[Mellanox Spectrum
SN2700](https://community.mellanox.com/docs/DOC-2685).

{{%/notice%}}

## <span id="src-8363026_SwitchPortAttributes-ethtool" class="confluence-anchor-link"></span><span>Configure Interfaces with ethtool </span>

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

### <span>Query SFP Port Information</span>

You can verify SFP settings using [`ethtool
-m`](/cumulus-linux/Monitoring_and_Troubleshooting/Troubleshooting_Network_Interfaces/Monitoring_Interfaces_and_Transceivers_Using_ethtool).
The following example shows the vendor, type and power output for the
swp4 interface.

    cumulus@switch:~$ sudo ethtool -m swp4 | egrep 'Vendor|type|power\s+:'
            Transceiver type                          : 10G Ethernet: 10G Base-LR
            Vendor name                               : FINISAR CORP.
            Vendor OUI                                : 00:90:65
            Vendor PN                                 : FTLX2071D327
            Vendor rev                                : A
            Vendor SN                                 : UY30DTX
            Laser output power                        : 0.5230 mW / -2.81 dBm
            Receiver signal average optical power     : 0.7285 mW / -1.38 dBm

## <span id="src-8363026_SwitchPortAttributes-caveats" class="confluence-anchor-link"></span><span>Caveats and Errata</span>

### <span>Port Speed and the ifreload -a Command</span>

When configuring port speed or break outs in the
`/etc/cumulus/ports.conf` file, you need to run the `ifreload -a`
command to reload the configuration after restarting `switchd` in the
following cases:

  - If you configure, or configure then remove, the port speed in the
    `/etc/cumulus/ports.conf` file and you also set or remove the speed
    on the same physical port or breakouts of that port in the
    `/etc/network/interfaces` file since the last time you restarted
    `switchd`.

<!-- end list -->

  - If you break out a switch port or remove a break out port and the
    port speed is set in both the `/etc/cumulus/ports.conf` file and the
    `/etc/network/interfaces` file.

### <span>10G and 1G SFPs Inserted in a 25G Port</span>

For 10G and 1G SFPs inserted in a 25G port on a Broadcom platform, you
must configure the four ports in the same core to be 10G. Each set of
four 25G ports are controlled by a single core; therefore, each core
must run at the same clock speed. The four ports must be in sequential
order; for example, swp1, swp2, swp3, and swp4.

1.  Edit the `/etc/cumulus/ports.conf` file and configure the four ports
    to be 10G. 1G SFPs are clocked at 10G speeds; therefore, for 1G
    SFPs, the `/etc/cumulus/ports.conf` file entry must also specify
    10G. Currently, you cannot use NCLU commands for this step.
    
        ...
        # SFP28 ports
        #
        # <port label 1-48> = [25G|10G|100G/4|40G/4]
        1=25G
        2=25G
        3=25G
        4=25G
        5=10G
        6=10G
        7=10G
        8=10G
        9=25G
        ...

2.  [Restart
    `switchd`](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=8366282).

3.  If you want to set the speed of any SFPs to 1G, set the port speed
    to 1000 Mbps using NCLU commands; this is *not* necessary for 10G
    SFPs. You don't need to set the port speed to 1G for all four ports.
    For example, if you intend only for swp5 and swp6 to use 1G SFPs, do
    the following:
    
        cumulus@switch:~$ net add interface swp5-swp6 link speed 1000 
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit

{{%notice note%}}

100G switch ASICs do not support 1000Base-X auto-negotiation (Clause
37), which is recommended for 1G fiber optical modules. As a result,
single fiber breaks cannot be detected when using 1G optical modules on
these switches.

The auto-negotiation setting must be the same on both sides of the
connection. If using 1G fiber modules in 25G SFP28 ports, ensure
auto-negotiation is disabled on the link partner interface as well.

{{%/notice%}}

### <span>Timeout Error on Quanta LY8 and LY9 Switches</span>

On Quanta T5048-LY8 and T3048-LY9 switches, an *Operation timed out*
error occurs while removing and reinserting QSFP module.

You cannot remove the QSFPx2 module while the switch is powered on, as
it is not hot-swappable. However, if an *Operation timed out* error
occurs, you can get the link to come up by [restarting
`switchd`](Configuring_switchd.html#src-8362561_Configuringswitchd-restartswitchd);
however, this disrupts your network.

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

### <span>200G Interfaces on the Dell S5248F Switch</span>

On the Dell S5248F switch, the 2x200G QSFP-DD interfaces labeled 49/50
and 51/52 are not supported natively at 200G speeds. The interfaces are
supported with 100G cables; however, you can only use one 100G cable
from each QSFP-DD port. The upper QSFP-DD port is named swp49 and the
lower QSFP-DD port is named swp52.

### <span>QSFP+ Ports on the Dell S5232F Switch</span>

Cumulus Linux does not support the 2x10G QSFP+ ports on the Dell S5232F
switch.

### <span>QSFP+ Ports on the Dell S4148T Switch</span>

On the Dell S4148T switch, the two QSFP+ ports are set to `disabled` by
default and the four QSFP28 ports are configured for 100G. The following
example shows the default settings in the `/etc/cumulus/ports.conf` file
for this switch:

    cumulus@switch:~$ sudo cat /etc/cumulus/ports.conf
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
    26=100G
    29=100G
    30=100G

To enable the two QSFP+ ports, you *must* configure all four QSFP28
ports for either 40G or 4x10G. You cannot use either of the QSFP+ ports
if any of the QSFP28 ports are configured for 100G.

The following example shows the `/etc/cumulus/ports.conf` file with all
four QSFP28 ports configured for 40G and both QSFP+ ports enabled:

    cumulus@switch:~$ sudo cat /etc/cumulus/ports.conf
    ...
    # QSFP+ ports
    #
    # <port label 27-28> = [4x10G|40G]
    27=40G
    28=40G
    # QSFP28 ports
    #
    # <port label 25-26, 29-30> = [4x10G|4x25G|2x50G|40G|50G|100G]
    25=40G
    26=40G
    29=40G
    30=40G

{{%notice note%}}

To disable the QSFP+ ports, you must set the ports to `disabled`. Do not
comment out the lines as this prevents `switchd` from restarting.

{{%/notice%}}

### <span>Link Speed on the EdgeCore AS7326-56X Switch</span>

On the EdgeCore AS7326-56X switch, all four switch ports in each port
group must be set to the same link speed; otherwise, the links do not
come up. These ports are set to 25G by default, but can also be set to
10G. The port groups on this switch are as follows, where each row is a
port group:

  - 1 2 3 6\*

  - 4 5 7\* 9

  - 8 10 11\* 12

  - 13 14 15 18\*

  - 16 17 19\* 21

  - 20 22 23\* 24

  - 25 26 27 30\*

  - 28 29 31\* 33

  - 32 34 35\* 36

  - 37 38 39 42\*

  - 40\* 41 43 45

  - 44\* 46 47 48

For example, if you configure port 19 for 10G, you must also configure
ports 16, 17 and 21 for 10G.

Additionally, you can gang each port group together as a 100G or 40G
port. When ganged together, one port (based on the arrangement of the
ports) is designated as the gang leader. This port's number is used to
configure the ganged ports and is marked with an asterisk ( \* ) above.

{{%notice note%}}

The EdgeCore AS7326-56X is a 48x25G + 8x100G + 2x10G switch. The
dedicated 10G ports are not currently supported in Cumulus Linux.
However, you can configure all other ports to run at 10G speeds.

{{%/notice%}}

### <span>ethtool Shows Incorrect Port Speed on 100G Mellanox Switches</span>

After setting the interface speed to 40G by editing the `ports.conf`
file on a Mellanox switch, `ethtool` still shows the speed as 100G.

This is a known issue where `ethtool` does not update after restarting
`switchd`, so it continues to display the outdated port speed.

To correctly set the port speed, use
[NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU)
or `ethtool` to set the speed instead of manually editing the
`ports.conf` file.

For example, to set the speed to 40G using NCLU:

    cumulus@switch:~$ net add interface swp1 link speed 40000 

Or using `ethtool`:

    cumulus@switch:~$ sudo ethtool -s swp1 speed 40000 

### <span>Delay in Reporting Interface as Operational Down</span>

When you remove two transceivers simultaneously from a switch, both
interfaces show the `carrier down` status immediately. However, it takes
one second for the second interface to show the `operational down`
status. In addition, the services on this interface also take an extra
second to come down.

## <span>Related Information</span>

  - [Debian - Network
    Configuration](http://wiki.debian.org/NetworkConfiguration)

  - [Linux Foundation -
    VLANs](http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan)

  - [Linux Foundation -
    Bonds](http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding)
