---
title: Switch Port Attributes
author: Cumulus Networks
weight: 307
aliases:
 - /display/DOCS/Switch+Port+Attributes
 - /pages/viewpage.action?pageId=8366750
product: Cumulus Linux
version: '4.0'
---
Cumulus Linux exposes network interfaces for several types of physical and logical devices:

- `lo` is the network loopback device
- `ethN` are switch management ports (for out of band management only)
- `swpN` are switch front panel ports
- (optional) `brN` are bridges (IEEE 802.1Q VLANs)
- (optional) `bondN` are bonds (IEEE 802.3ad link aggregation trunks, or port channels)

Each physical network interface (port) has a number of configurable settings:

- [Auto-negotiation](http://en.wikipedia.org/wiki/Autonegotiation)
- [Duplex Mode](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29)
- Link speed
- [MTU](https://en.wikipedia.org/wiki/Maximum_transmission_unit), (maximum transmission unit)
- [FEC](https://en.wikipedia.org/wiki/Forward_error_correction) (forward error correction)

Most of these settings are configured automatically for you, depending upon your switch ASIC; however, you must always set MTU manually.

For **Spectrum ASICs**, MTU is the only port attribute you can directly configure. The Spectrum firmware configures FEC, link speed, duplex mode and auto-negotiation automatically, following a predefined list of parameter settings until the link comes up. However, you can disable FEC if necessary, which forces the firmware to not try any FEC options.

For **Broadcom-based switches,** Cumulus Networks recommends that you enable auto-negotiation on each port. When enabled, Cumulus Linux automatically configures the best link parameter settings based on the module type (speed, duplex, auto-negotiation, and FEC, where supported).

This topic describes the auto-negotiation, link speed, duplex mode, MTU, and FEC settings and provides a
[table](#interface-configuration-recommendations-for-broadcom-platforms) showing the default configuration for various port and cable types. Breakout port configuration, logical switch port limitations, and troubleshooting is also provided.

## Auto-negotiation

By default on a Broadcom-based switch, auto-negotiation is disabled — except on 10G and 1000BASE-T fixed copper switch ports, where it is required for links to work. For RJ-45 SFP adapters, you need to manually configure the desired link speed and auto-negotiation as described in the [default settings table](#interface-configuration-recommendations-for-broadcom-platforms) below.

If you disable auto-negotiation later or never enable it, then you have to configure any settings that deviate from the port default — such as duplex mode, FEC, and link speed settings.

{{%notice warning%}}

Some module types support auto-negotiation while others do not. To enable a simpler configuration, Cumulus Linux allows you to configure auto-negotiation on all port types on Broadcom switches; the port configuration software then configures the underlying hardware according to its capabilities.

If you do decide to disable auto-negotiation, be aware of the following:

- You must manually set any non-default link speed, duplex, pause, and FEC.
- Disabling auto-negotiation on a 1G optical cable prevents detection of single fiber breaks.
- You cannot disable auto-negotiation on 1GT or 10GT fixed copper switch ports.

For 1000BASE-T RJ-45 SFP adapters, auto-negotiation is automatically done on the SFP PHY, so enabling auto-negotiation on the port settings is not required. You must manually configure these ports using the [settings below](#interface-configuration-recommendations-for-broadcom-platforms).

{{%/notice%}}

Depending upon the connector used for a port, enabling auto-negotiation also enables forward error correction (FEC), if the cable requires it (see the [table below](#interface-configuration-recommendations-for-broadcom-platforms)). The correct FEC mode is set based on the speed of the cable when auto-negotiation is enabled.

To configure auto-negotiation for a switch:

<details>

<summary>NCLU Commands </summary>

Run the `net add interface <interface> link autoneg` command. The following example commands enable auto-negotiation for the swp1 interface:

```
cumulus@switch:~$ net add interface swp1 link autoneg on
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

1. Edit the `/etc/network/interfaces` file. The following example disables auto-negotiation for the swp1 interface.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
    link-autoneg off
```

2. Run the `ifreload -a` command to load the updated configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

You can use `ethtool` to configure auto-negotiation. The following example command enables auto-negotiation for the swp1 interface:

```
ethtool -s swp1 speed 10000 duplex full autoneg on|off
```

{{%notice warning%}}

A runtime configuration is non-persistent; the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

</details>

{{%notice note%}}

Any time you enable auto-negotiation, Cumulus Linux restores the default configuration settings specified in the [table below](#interface-configuration-recommendations-for-broadcom-platforms).

{{%/notice%}}

## Port Speed and Duplex Mode

Cumulus Linux supports both half- and [full-duplex](http://en.wikipedia.org/wiki/Duplex_%28telecommunications%29) configurations. Half-duplex is supported only with speeds of less than 1G.

Supported port speeds include 100M, 1G, 10G, 25G, 40G, 50G and 100G. In Cumulus Linux, you set the speed on Broadcom-based switch in Mbps, where the setting for 1G is *1000*, 40G is *40000*, and 100G is *100000*.

You can configure ports to one speed less than their maximum speed.

| Switch Port Type | Lowest Configurable Speed                                 |
| ---------------- | --------------------------------------------------------- |
| 1G               | 100 Mb                                                    |
| 10G              | 1 Gigabit (1000 Mb)                                       |
| 40G              | 10G\*                                                     |
| 100G             | 50G\* & 40G (with or without breakout port), 25G\*, 10G\* |

\*Requires the port to be converted into a breakout port. See [Configure Breakout Ports](#breakout-ports), below.

{{%notice note%}}

**Platform Limitations**

- On Lenovo NE2572O switches, swp1 through swp8 only support 25G speed.
- For 10G and 1G SFPs inserted in a 25G port on a Broadcom platform, you must edit the `/etc/cumulus/ports.conf` file and configure the four ports in the same core to be 10G. See [Caveats and Errata](#caveats-and-errata).

{{%/notice%}}

To configure the port speed and duplex mode:

<details>

<summary>NCLU Commands </summary>

Run the `net add interface <interface> link speed` command. The following commands configure the port speed for the swp1 interface. The duplex mode setting defaults to *full*. You only need to specify `link duplex` if you want to set half-duplex mode.

```
cumulus@switch:~$ net add interface swp1 link speed 10000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The above commands create the following `/etc/network/interfaces` file code snippet:

```
auto swp1
iface swp1
    link-speed 10000
```

The following commands configure the port speed and set half-duplex mode for the swp31 interface.

```
cumulus@switch:~$ net add interface swp31 link speed 100 
cumulus@switch:~$ net add interface swp31 link duplex half
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The above commands create the following `/etc/network/interfaces` file code snippet:

```
auto swp31
iface swp31
    link-speed 100
    link-duplex half
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file to create a persistent configuration for the port speeds:

1. Add the appropriate lines for each switch port stanza. The following example shows that the port speed for the swp1 interface is set to 10G and the duplex mode is set to *full*.

    {{%notice note%}}

If you specify the port speed in the `/etc/network/interfaces` file, you must also specify the duplex mode setting; otherwise, the interface defaults to half duplex.

{{%/notice%}}

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
    address 10.1.1.1/24
    link-speed 10000
    link-duplex full
```

2. Run the `ifreload -a` command to load the updated configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

You can use `ethtool` to configure the port speed and duplex mode for your switch ports. You must specify both the port speed and the duplex mode in the `ethtool` command; auto-negotiation is optional.

The following example command sets the port speed to 10G and duplex mode to full on the swp1 interface:

```
cumulus@switch:~$  ethtool -s swp1 speed 10000 duplex full
```

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

</details>

## MTU

Interface MTU applies to traffic traversing the management port, front panel/switch ports, bridge, VLAN subinterfaces, and bonds (both physical and logical interfaces). MTU is the only interface setting that you must set manually.

On Mellanox switches, the default MTU setting is 9248 in Cumulus Linux. On Broadcom switches, the default MTU setting is 1500. To change the setting, run the following commands:

<details>

<summary>NCLU Commands </summary>

Run the `net add interface <interface> mtu` command. The following example command sets MTU to 9000 for the swp1 interface.

```
cumulus@switch:~$ net add interface swp1 mtu 9000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following code snippet:

```
auto swp1
iface swp1
    mtu 9000
```

</details>

<details>

<summary>Linux Commands </summary>

1. Edit the `/etc/network/interfaces` file. The following example sets MTU to 9000 for the swp1 interface.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
    mtu 9000
```

2. Run the `ifreload -a` command to load the updated configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

Run the `ip link set` command. The following example command sets the swp1 interface to Jumbo Frame MTU=9000.

```
cumulus@switch:~$ sudo ip link set dev swp1 mtu 9000
```

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

</details>

{{%notice note%}}

Some switches might not support the same maximum MTU setting in hardware for both the management interface (eth0) and the data plane ports.

{{%/notice%}}

### Set a Policy for Global System MTU

For a global policy to set MTU, create a policy document (called `mtu.json`). For example:

```
cumulus@switch:~$ sudo cat /etc/network/ifupdown2/policy.d/mtu.json
{
  "address": {"defaults": { "mtu": "9216" }
            }
}
```

{{%notice note%}}

If your platform does not support a high MTU on eth0, you can set a lower MTU with the following command:

```
cumulus@switch:~$ net add interface eth0 mtu 1500
cumulus@switch:~$ net commit
```

{{%/notice%}}

{{%notice warning%}}

The policies and attributes in any file in `/etc/network/ifupdown2/policy.d/` override the default policies and attributes in `/var/lib/ifupdown2/policy.d/`.

{{%/notice%}}

### MTU for a Bridge

The MTU setting is the lowest MTU of any interface that is a member of the bridge (every interface specified in `bridge-ports` in the bridge configuration of the `/etc/network/interfaces` file). There is **no** need to specify an MTU on the bridge. Consider this bridge configuration:

```
auto bridge
iface bridge
    bridge-ports bond1 bond2 bond3 bond4 peer5
    bridge-vids 100-110
    bridge-vlan-aware yes
```

For *bridge* to have an MTU of 9000, set the MTU for each of the member interfaces (bond1 to bond 4, and peer5), to 9000 at minimum.

{{%notice tip%}}

**Use MTU 9216 for a bridge**

Two common MTUs for jumbo frames are 9216 and 9000 bytes. The corresponding MTUs for the VNIs would be 9166 and 8950.

{{%/notice%}}

When configuring MTU for a bond, configure the MTU value directly under the bond interface; the configured value is inherited by member links/slave interfaces. If you need a different MTU on the bond, set it on the bond interface, as this ensures the slave interfaces pick it up. There is no need to specify MTU on the slave interfaces.

VLAN interfaces inherit their MTU settings from their physical devices or their lower interface; for example, swp1.100 inherits its MTU setting from swp1. Therefore, specifying an MTU on swp1 ensures that swp1.100 inherits the MTU setting for swp1.

If you are working with [VXLANs](../../../Network-Virtualization/), the MTU for a virtual network interface (VNI must be 50 bytes smaller than the MTU of the physical interfaces on the switch, as those 50 bytes are required for various headers and other data. Also, consider setting the MTU much higher than 1500.

{{%notice note%}}

The MTU for an SVI interface, such as vlan100, is derived from the bridge. When you use NCLU to change the MTU for an SVI and the MTU setting is higher than it is for the other bridge member interfaces, the MTU for all bridge member interfaces changes to the new setting. If you need to use a mixed MTU configuration for SVIs, (if some SVIs have a higher MTU and some lower), set the MTU for all member interfaces to the maximum value, then set the MTU on the specific SVIs that need to run at a lower MTU.

{{%/notice%}}

To show the MTU setting for an interface:

<details>

<summary>NCLU Commands </summary>

Run the `net show interface <interface>` command:

```
cumulus@switch:~$ net show interface swp1
    Name    MAC                Speed      MTU  Mode
--  ------  -----------------  -------  -----  ---------
UP  swp1    44:38:39:00:00:04  1G        1500  Access/L2
```

</details>

<details>

<summary>Linux Commands </summary>

Run the `ip link show <interface>` command:

```
cumulus@switch:~$ ip link show dev swp1
3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500
   link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
```

</details>

### Bring Down an Interface for a Bridge Member

When you bring down an interface for a bridge member, the MTU for the interface and the MTU for the bridge are both set to the default value of 1500 for Broadcom switches and 9248 for Mellanox switches. To work around this, run `ifdown` on the interface, then run the `sudo ip link set dev <interface> mtu` command.

For example:

```
sudo ifdown swp3
sudo ip link set dev swp3 mtu 9192
```

As an alternative, add a `post-down` command in the `/etc/network/interfaces` file to reset the MTU of the interface. For example:

```
auto swp3
iface swp3
    bridge-vids 106 109 119 141 150-151
    mtu 9192
    post-down /sbin/ip link set dev swp3 mtu 9192
```

## FEC

[Forward Error Correction (FEC)](https://en.wikipedia.org/wiki/Forward_error_correction) is an encoding and decoding layer that enables the switch to detect and correct bit errors introduced over the cable between two interfaces. Because 25G transmission speeds can introduce a higher than acceptable bit error rate (BER) on a link, FEC is required or recommended for 25G, 4x25G, and 100G link speeds.

For the link to come up, the two interfaces on each end must use the same FEC setting.

{{%notice note%}}

There is a very small latency overhead required for FEC. For most applications, this small amount of latency is preferable to error packet retransmission latency.

{{%/notice%}}

There are two FEC types:

- Reed Solomon (**RS**), IEEE 802.3 Clause 108 (CL108) on individual 25G channels and Clause 91 on 100G (4channels). This is the highest FEC algorithm, providing the best bit-error correction.
- Base-R (**BaseR**), Fire Code (FC), IEEE 802.3 Clause 74 (CL74). Base-R provides less protection from bit errors than RS FEC but adds less latency.

Cumulus Linux includes additional FEC options:

- *Auto* FEC instructs the hardware to select the best FEC. For copper DAC, FEC can be negotiated with the remote end. However, optical modules do not have auto-negotiation capability; if the device chooses a preferred mode, it might not match the remote end. This is the current default on a Spectrum switch.
- *No* FEC (no error correction is done). This is the current default on a Broadcom switch.

{{%notice note%}}

The Trident II switch does not support FEC.

The Tomahawk switch does not support RS FEC or auto-negotiation of FEC on 25G lanes that are broken out (Tomahawk pre-dates 802.3by). If you are using a 4x25G breakout DAC or AOC on a Tomahawk switch, you can configure either Base-R FEC or no FEC, and choose cables appropriate for that limitation (CA-25G-S, CA-25G-N or fiber). Tomahawk+, Tomahawk2, Trident3 and Maverick switches do not have this limitation.

{{%/notice%}}

For **25G DAC, 4x25G Breakouts DAC and 100G DAC cables**, the IEEE 802.3by specification creates 3 classes:

- CA-25G-L (long cables - achievable cable length of at least 5m) dB loss less or equal to 22.48. Requires RS FEC and expects BER of 10-5 or better with RS FEC enabled.
- CA-25G-S (short cables - achievable cable length of at least 3m) dB loss less or equal to 16.48. Requires Base-R FEC and expects BER of 10-8 or better with Base-R FEC enabled.
- CA-25G-N (no FEC - achievable cable length of at least 3m) dB loss less or equal to 12.98. Does not require FEC. Expects BER 10-12 or better with no FEC.

The IEEE classification is based on various dB loss measurements and minimum achievable cable length. You can build longer and shorter cables if they comply to the dB loss and BER requirements.

If a cable is manufactured to CA-25G-S classification and FEC is not enabled, the BER might be unacceptable in a production network. It is important to set the FEC according to the cable class (or better) to have acceptable bit error rates. See [Determining Cable Class](#determine-cable-class-of-100g-and-25g-dacs) below.

You can check bit errors using `cl-netstat` (`RX_ERR` column) or `ethtool -S` (`HwIfInErrors` counter) after a large amount of traffic has passed through the link. A non-zero value indicates bit errors.
Expect error packets to be zero or extremely low compared to good packets. If a cable has an unacceptable rate of errors with FEC enabled, replace the cable.

For **25G, 4x25G Breakout, and 100G Fiber modules and AOCs**, there is no classification of 25G cable types for dB loss, BER or length. FEC is recommended but might not be required if the BER is low enough.

### Determine Cable Class of 100G and 25G DACs

You can determine the cable class for 100G and 25G DACs from the Extended Specification Compliance Code field (SFP28: 0Ah, byte 35, QSFP28: Page 0, byte 192) in the cable EEPROM programming.

For 100G DACs, most manufacturers use the 0x0Bh *100GBASE-CR4 or 25GBASE-CR CA-L* value (the 100G DAC specification predates the IEEE 802.3by 25G DAC specification). RS FEC is the expected setting for 100G DAC but might not be required with shorter or better cables.

{{%notice note%}}

A manufacturer's EEPROM setting might not match the dB loss on a cable or the actual bit error rates that a particular cable introduces. Use the designation as a guide, but set FEC according to the bit error rate tolerance in the design criteria for the network. For most applications, the highest mutual FEC ability of both end devices is the best choice.

{{%/notice%}}

You can determine for which grade the manufacturer has designated the cable as follows.

For the **SFP28 DAC**, run the following command:

```
cumulus@switch:~$ sudo ethtool -m swp35 hex on | grep 0020 | awk '{ print $6}'
0c
```

The values at location 0x0024 are:

- 0x0b : CA-L (long cable - RS FEC required)
- 0x0c : CA-S (short cable - Base-R or better FEC required)
- 0x0d : CA-N (no FEC required)

For the **QSFP28 DAC**, run the following command:

```
cumulus@switch:~$ sudo ethtool -m swp51s0 hex on | grep 00c0 | awk '{print $2}'
0b
```

The values at 0x00c0 are:

- 0x0b : CA-L (long cable - RS FEC required) or 100G CR4
- 0x0c : CA-S (short cable - Base-R or better FEC required)
- 0x0d : CA-N (no FEC required)

In each example below, the *Compliance* field is derived using the method described above and is not visible in the `ethool -m` output.

```
3meter cable that does not require FEC 
(CA-N)  
Cost: More expensive  
Cable size: 26AWG (Note that AWG does not necessarily correspond to overall dB loss or BER performance)  
Compliance Code: 25GBASE-CR CA-N

3meter cable that requires Base-R FEC 
(CA-S)  
Cost: Less expensive  
Cable size: 26AWG  
Compliance Code: 25GBASE-CR CA-S
```

When in doubt, consult the manufacturer directly to determine the cable classification.

### Spectrum ASIC FEC Behavior

The firmware in a Spectrum ASIC applies an FEC configuration to 25G and 100G cables based on the cable type and whether the peer switch also has a Spectrum ASIC.

When the link is between two switches with Spectrum ASICs:

- For 25G optical modules, the Spectrum ASIC firmware chooses Base-R/FC-FEC.
- For 25G DAC cables with attenuation less or equal to 16db, the firmware chooses Base-R/FC-FEC.
- For 25G DAC cables with attenuation higher than 16db, the firmware chooses RS-FEC.
- For 100G cables/modules, the firmware chooses RS-FEC.

| Cable Type | <div style="width:300px">FEC Mode |
|------------|----------|
| 25G optical cables | Base-R/FC-FEC |
| 25G 1,2 meters: CA-N, loss <13db | Base-R/FC-FEC|
| 25G 2.5,3 meters: CA-S, loss <16db | Base-R/FC-FEC|
| 25G 2.5,3,4,5 meters: CA-L, loss > 16db | RS-FEC|
| 100G DAC or optical | RS-FEC|

When linking to a non-Spectrum peer, the firmware lets the peer decide. The Spectrum ASIC supports RS-FEC (for both 100G and 25G), Base-R/FC-FEC (25G only), or no-FEC (for both 100G and 25G).

| Cable Type | <div style="width:300px">FEC Mode |
|------------|----------|
| 25G pptical cables | Let peer decide|
| 25G 1,2 meters: CA-N, loss <13db | Let peer decide|
| 25G 2.5,3 meters: CA-S, loss <16db | Let peer decide|
| 25G 2.5,3,4,5 meters: CA-L, loss > 16db | Let peer decide|
| 100G | Let peer decide: RS-FEC or No FEC|

### How Does Cumulus Linux use FEC?

This depends upon the make of the switch you are using.

A Spectrum switch enables FEC automatically when it powers up; that is, the setting is `fec auto`. The port firmware tests and determines the correct FEC mode to bring the link up with the neighbor. It is possible to get a link up to a Spectrum switch without enabling FEC on the remote device as the switch eventually finds a working combination to the neighbor without FEC.

On a Broadcom switch, Cumulus Linux does not enable FEC by default; that is, the setting is `fec off`. Cumulus Networks recommends you configure FEC explicitly to match the configured FEC on the link neighbor. On 100G DACs, you can configure `link-autoneg` so that the port attempts to negotiate FEC settings with the remote peer.

The following sections describe how to show the current FEC mode, and to enable and disable FEC.

### Show the Current FEC Mode

Cumulus Linux returns different output for the `ethtool --show-fec` command, depending upon whether you are using a Broadcom or Mellanox Spectrum switch.

On a Broadcom switch, the `--show-fec` output tells you exactly what you configured, even if the link is down due to a FEC mismatch with the neighbor.

On a Spectrum switch, the `--show-fec` output tells you the current active state of FEC **only if the link is up**; that is, if the FEC modes matches that of the neighbor. If the link is not up, the value displays *None*, which is not valid.

To show the FEC mode currently enabled on a given switch port, run the `ethtool --show-fec <interface>` command.

```
cumulus@switch:~$ sudo ethtool --show-fec swp23
FEC parameters for swp23:
Configured FEC encodings: Auto
Active FEC encoding: Off
```

### Enable or Disable FEC

To enable **Reed Solomon (RS) FEC** on a link:

<details>

<summary>NCLU Commands </summary>

Run the `net add interface <interface> link fec rs` command. For example:

```
cumulus@switch:~$ sudo net add interface swp23 link fec rs
cumulus@switch:~$ sudo net pending
cumulus@switch:~$ sudo net commit
```

</details>

<details>

<summary>Linux Commands </summary>

1. Edit the `/etc/network/interfaces` file. The following example enables RS FEC for the swp1 interface (`link-fec rs`):

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
     link-autoneg off
     link-speed 100000
     link-fec rs
```

2. Run the `ifreload -a` command to load the updated configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

Run the `ethtool --set-fec <interface> encoding RS` command. For example:

```
cumulus@switch:~$ sudo ethtool --set-fec swp1 encoding RS
```

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

</details>

To enable **Base-R/FireCode FEC** on a link:

<details>

<summary>NCLU Commands </summary>

Run the `net add interface <interface> link fec baser` command. For example:

```
cumulus@switch:~$ sudo net add interface swp23 link fec baser
cumulus@switch:~$ sudo net pending
cumulus@switch:~$ sudo net commit
```

</details>

<details>

<summary>Linux Commands </summary>

1. Edit the `/etc/network/interfaces` file. The following example enables Base-R FEC for the swp1 interface (`link-fec baser`):

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
     link-autoneg off
     link-speed 100000
     link-fec baser
```

2. Run the `ifreload -a` command to load the updated configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

Run the `ethtool --set-fec <interface> encoding baser` command. For example:

```
cumulus@switch:~$ sudo ethtool --set-fec swp1 encoding BaseR
```

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

</details>

To enable FEC with Auto-negotiation:

{{%notice note%}}

FEC with auto-negotiation is supported on DACs only.

{{%/notice%}}

<details>

<summary>NCLU Commands </summary>

Run the `net add interface <interface> link autoneg` `on` command. The following example command enables FEC with auto-negotiation on the swp12 interface:

```
cumulus@switch:~$ sudo net add interface swp12 link autoneg on
cumulus@switch:~$ sudo net pending
cumulus@switch:~$ sudo net commit
```

</details>

<details>

<summary>Linux Commands </summary>

1. Edit the `/etc/network/interfaces` file and set auto-negotiation to *on*. For example:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
    link-autoneg on
```

2. Run the `ifreload -a` command to load the updated configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

You can use `ethtool` to enable FEC with auto-negotiation. For example:

```
ethtool -s swp1 speed 10000 duplex full autoneg on
```

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

</details>

To show the FEC and auto-negotiation settings for an interface, run the
following command:

```
cumulus@switch:~$ sudo ethtool swp12 | egrep 'FEC|auto'
Supports auto-negotiation: Yes
Supported FEC modes: RS
Advertised auto-negotiation: Yes
Advertised FEC modes: RS
Link partner advertised auto-negotiation: Yes
Link partner advertised FEC modes: Not reported
```

To disable FEC on a link:

<details>

<summary>NCLU Commands </summary>

Run the `net add interface <interface> link fec off` command. For example:

```
cumulus@switch:~$ sudo net add interface swp23 link fec off
cumulus@switch:~$ sudo net pending
cumulus@switch:~$ sudo net commit
```

</details>

<details>

<summary>Linux Commands </summary>

1. Edit the `/etc/network/interfaces` file. The following example disables Base-R FEC for the swp1 interface (`link-fec baser`):

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp23
iface swp23
link-fec off
```

2. Run the `ifreload -a` command to load the updated configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

Run the `ethtool --set-fec <interface> encoding off` command. For example:

```
cumulus@switch:~$ sudo ethtool --set-fec swp23 encoding off
```

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

</details>

## Interface Configuration Recommendations for Broadcom Platforms

The recommended configuration for each type of interface is described in the following table. These are the link settings that are applied to the port hardware when auto-negotiation is enabled on a Broadcom-based switch. If further troubleshooting is required to bring a link up, use the table below as a guide to set the link parameters.

Except as noted below, the settings for both sides of the link are expected to be the same.

{{%notice note%}}

Spectrum switches automatically configure these settings following a predefined list of parameter settings until the link comes up.

{{%/notice%}}

| Speed<img width=100/>| Auto-negotiation|FEC Setting|Manual Configuration Examples<img width=300/>| Notes|
|--- |--- |--- |--- |--- |
| 100BASE-T (RJ-45 SFP adapter)| Off|N/A |**NCLU commands**<pre>$ net add interface swp1 link speed 100<br>$ net add interface swp1 link autoneg off</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg off<br>&nbsp; &nbsp;link-speed 100</pre> | The module has two sets of electronics: the port side, which communicates with the switch ASIC and the RJ-45 adapter side.<br><br>Auto-negotiation is always used on the RJ-45 adapter side of the link by the PHY built into the module. This is independent of the switch setting. Set auto-negotiation to off.<br><br>Auto-negotiation must be enabled on the server side in this scenario. |
| 100BASE-T on a 1G fixed copper port | On | N/A | **NCLU commands**<pre>$ net add interface swp1 link speed 100<br>$net add interface swp1 link autoneg on</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;ink-autoneg on<br>&nbsp; &nbsp;link-speed 100</pre> | 10M or 100M speeds are possible with auto-negotiation off on both sides.<br><br>Testing on an Edgecore AS4610-54P showed the ASIC reporting auto-negotiation as on.<br><br>Power over Ethernet might require auto-negotiation to be on. |
| 1000BASE-T (RJ-45 SFP adapter) | Off | N/A | **NCLU commands**<pre>$ net add interface swp1 link speed 1000<br>$ net add interface swp1 link autoneg off</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg off<br>&nbsp; &nbsp;link-speed 1000</pre> | The module has two sets of electronics: the port side, which communicates with the switch ASIC and the RJ-45 side.<br><br>Auto-negotiation is always used on the RJ-45 side of the link by the PHY built into the module. This is independent of the switch setting. Set auto-negotiation to off.<br><br>Auto-negotiation must be enabled on the server side. |
| 1000BASE-T on a 1G fixed copper port | On | N/A | **NCLU commands**<pre>$ net add interface swp1 link speed 1000<br>$ net add interface swp1 link autoneg on</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg on<br>&nbsp; &nbsp;link-speed 1000</pre> | |
| 1000BASE-T on a 10G fixed copper port | On | N/A |**NCLU commands**<pre>$ net add interface swp1 link speed 1000<br>$ net add interface swp1 link autoneg on</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg on<br>&nbsp; &nbsp;link-speed 1000</pre>| |
| 1000BASE-SX 1000BASE-LX (1G Fiber) | Recommended On | N/A |**NCLU commands**<pre>$ net add interface swp1 link speed 1000<br>$ net add interface swp1 link autoneg on</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg on<br>&nbsp; &nbsp;link-speed 1000</pre> |Without auto-negotiation, the link stays up when there is a single fiber break.<br><br>See the limitation discussed in [10G and 1G SFPs Inserted in a 25G Port](#10g-and-1g-sfps-inserted-in-a-25g-port), below. |
| 10GBASE-T (RJ-45 SFP Module) | Off | N/A | **NCLU commands**<pre>$ net add interface swp1 link speed 10000<br>$ net add interface swp1 link autoneg off</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg off<br>&nbsp; &nbsp;link-speed 10000</pre> |The module has two sets of electronics — the port side, which communicates to the switch ASIC and the RJ-45 side.<br><br>Auto-negotiation is always used on the RJ-45 side of the link by the PHY built into the module. This is independent of the switch setting. Set link-autoneg to off.<br><br>Auto-negotiation needs to be enabled on the server side. |
| 10GBASE-T fixed copper port | On | N/A |**NCLU commands**<pre>$ net add interface swp1 link speed 10000<br>$ net add interface swp1 link autoneg on</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg on<br>&nbsp; &nbsp;link-speed 10000</pre> | |
| 10GBASE-CR<br>10GBASE-LR<br>10GBASE-SR<br>10G AOC | Off | N/A | **NCLU commands**<pre>$ net add interface swp1 link speed 10000<br>$ net add interface swp1 link autoneg off</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg off<br>&nbsp; &nbsp;link-speed 10000</pre> ||
| 40GBASE-CR4 | Recommended On | Disable | **NCLU commands**<pre>$ net add interface swp1 link speed 40000<br>$ net add interface swp1 link autoneg on</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg on<br>&nbsp; &nbsp;link-speed 40000</pre>|40G standards mandate auto-negotiation be enabled for DAC connections. |
| 40GBASE-SR4<br>40GBASE-LR4<br>40G AOC | Off | Disable | **NCLU commands**<pre>$ net add interface swp1 link speed 40000<br>$ net add interface swp1 link autoneg off</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg off<br>&nbsp; &nbsp;link-speed 40000</pre> ||
| 100GBASE-CR4 | On | auto-negotiated | **NCLU commands**<pre>$ net add interface swp1 link speed 100000<br>$ net add interface swp1 link autoneg on</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg on<br>&nbsp; &nbsp;link-speed 100000</pre> ||
| 100GBASE-SR4<br>100G AOC | Off | RS | **NCLU commands**<pre>$ net add interface swp1 link speed 100000<br>$ net add interface swp1 link autoneg off<br>$ net add interface swp1 link fec rs</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg off<br>&nbsp; &nbsp;link-speed 100000<br>&nbsp; &nbsp;link-fec rs</pre> | |
| 100GBASE-LR4 | Off | None | **NCLU commands**<pre>$ net add interface swp1 link speed 100000<br>$ net add interface swp1 link autoneg off<br>$ net add interface swp1 link fec off</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg off<br>&nbsp; &nbsp;link-speed 100000<br>&nbsp; &nbsp;link-fec off</pre> | |
| 25GBASE-CR | On | auto-negotiated | **NCLU commands**<pre>$ net add interface swp1 link speed 25000<br>$ net add interface swp1 link autoneg on</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg on<br>&nbsp; &nbsp;link-speed 25000</pre> | Tomahawk predates 802.3by. It does not support RS FEC or auto-negotiation of RS FEC on a 25G port or subport. It does support Base-R FEC.|
| 25GBASE-SR | Off | RS | **NCLU commands**<pre>$ net add interface swp1 link speed 25000<br>$ net add interface swp1 link autoneg off<br>$ net add interface swp1 link fec baser</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg off<br>&nbsp; &nbsp;link-speed 25000<br>&nbsp; &nbsp;link-fec baser</pre> | Tomahawk predates 802.3by. It does not support RS FEC on a 25G port or subport. It does support Base-R FEC. |
| 25GBASE-LR | Off | None | **NCLU commands**<pre>$ net add interface swp1 link speed 25000<br>$ net add interface swp1 link autoneg off<br>$ net add interface swp1 link fec off</pre>**Configuration in /etc/network/interfaces**<pre>auto swp1<br>iface swp1<br>&nbsp; &nbsp;link-autoneg off<br>&nbsp; &nbsp; link-speed 25000<br>&nbsp; &nbsp;link-fec off</pre> | |

## Default Policies for Interface Settings

Instead of configuring settings for each individual interface, you can specify a policy for all interfaces on a switch or tailor custom settings for each interface. Create a file in `/etc/network/ifupdown2/policy.d/` and populate the settings accordingly. The following example shows a file called `address.json.`

```
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
        "defaults": { "mtu": "9000" },
        "iface_defaults": {
            "eth0": {"mtu": "1500"}
        }
    }
}
```

{{%notice note%}}

Setting the default MTU also applies to the management interface. Be sure to add the *iface\_defaults* to override the MTU for eth0, to remain at 1500 for Broadcom switches or 9248 for Mellanox switches.

{{%/notice%}}

## Breakout Ports

Cumulus Linux provides the ability to:

- Break out 100G switch ports into 2x50G, 2x40G, 4x25G, or 4x10G with breakout cables:
- Break out 40G switch ports into four separate 10G ports for use with breakout cables.
- Combine (*aggregate* or *gang*) four 10G switch ports into one 40G port for use with a breakout cable ([not to be confused with a bond](../../../Layer-2/Bonding-Link-Aggregation/)).

{{%notice note%}}

- For switches with ports that support 100G speeds, you can break out any 100G port into a variety of options: four 10G ports, four 25G ports, two 40G ports or two 50G ports. You *cannot* have more than 128 total logical ports on a Broadcom switch.
- You can only use NCLU to configure a 4x25G breakout port. To configure other breakout ports, use Linux commands.
- You cannot use NCLU to break out the uplink ports.

{{%/notice%}}

{{%notice note%}}

The Mellanox SN2700, SN2700B, SN2410, and SN2410B switches all have a limit of 64 logical ports in total. However, if you want to break out to 4x25G or 4x10G, you must configure the logical ports as follows:

- You can only break out odd-numbered ports into 4 logical ports.
- You must disable the next even-numbered port. For example, if you break out port 11 into 4 logical ports, you must disable port 12.

These restrictions do *not* apply to a 2x50G breakout configuration.

{{%/notice%}}

To configure a breakout port:

<details>

<summary>NCLU Commands - 4x25G breakout ports only </summary>

Run the following commands to configure the port to break out and set the link speed. The following example command breaks out swp3 into four 25G ports:

```
cumulus@switch:~$ net add interface swp3 breakout 4x25G
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%notice note%}}

On Spectrum switches, you need to disable the next port. The following example command disables swp4.

```
cumulus@switch:~$ net add interface swp4 breakout disabled
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%/notice%}}

These commands break out the 100G interfaces to 4x25G interfaces in thev`/etc/cumulus/ports.conf` file,vrestart the `switchd` process tovreconfigure the ports and create four interfaces in thev`/etc/network/interfaces` file named as follows:

```
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
```

The breakout port configuration is stored in the `/etc/cumulus/ports.conf` file.

{{%notice note%}}

When you commit your change, `switchd` restarts to apply the changes. The restart [interrupts network services](../../../System-Configuration/Configuring-switchd/).

{{%/notice%}}

</details>

<details>

<summary>Linux Commands </summary>

1. Edit the `/etc/cumulus/ports.conf` file to configure the port breakout. See the examples below.
2. Configure the breakout ports in the `/etc/network/interfaces` file. See the example below.
3. [Restart `switchd`](../../../System-Configuration/Configuring-switchd/#restart-switchd).

The `/etc/cumulus/ports.conf` file varies across different hardware platforms. Check the current list of supported platforms on [the hardware compatibility list](http://www.cumulusnetworks.com/hcl).

The following example shows a snippet from the `/etc/cumulus/ports.conf` file on a Dell S6000 switch (with a Trident II+ ASIC) where swp6 is broken out into four 10G ports:

```
cumulus@switch:~$ sudo cat /etc/cumulus/ports.conf
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
```

The following example shows the swp26 breakout ports (swp26s0, swp26s1, swp26s2, and swp26s3) in the `/etc/network/interfaces` file.

```
cumulus@switch:~$ sudo cat /etc/network/interfaces
...
auto swp26s0
iface swp26s0

auto swp26s1
iface swp26s1

auto swp26s2
iface swp26s2

auto swp26s3
iface swp26s3
...
```

</details>

{{%notice tip%}}

Refer to [this article](https://community.mellanox.com/docs/DOC-2685) article for an example of how to configure breakout cables for the Mellanox Spectrum SN2700 switch.

{{%/notice%}}

### Break out a 100G Port to Four 10G Ports

If you want to support 10G speed modules or cables on 100G ports you must set up the port in 10G mode first by configuring breakout ports on the 100G ports using the following commands:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add interface swp25 breakout 4x10G
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

1. Edit the `/etc/cumulus/ports.conf` file to configure the port breakout.

```
cumulus@switch:~$ sudo nano /etc/cumulus/ports.conf
...

25s0=10G
25s1=10G
25s2=10G
25s3=10G
...
```

2. Configure the breakout ports in the `/etc/network/interfaces` file.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...

auto swp25s0
iface swp25s0

auto swp25s1
iface swp25s1

auto swp25s2
iface swp25s2

auto swp25s3
iface swp25s3
...
```

3. [Restart `switchd`](../../../System-Configuration/Configuring-switchd/#restart-switchd).

</details>

### Remove a Breakout Port

To remove a breakout port:

<details>

<summary>NCLU Commands </summary>

1. Run the `net del interface <interface>` command. For example:

```
cumulus@switch:~$ net del interface swp3s0
cumulus@switch:~$ net del interface swp3s1
cumulus@switch:~$ net del interface swp3s2
cumulus@switch:~$ net del interface swp3s3
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

2. Manually edit the `/etc/cumulus/ports.conf` file to configure the interface for the original speed. For example:

```
cumulus@switch:~$ sudo nano /etc/cumulus/ports.conf
...

2=100G
3=100G
4=100G
...
```

3. [Restart `switchd`](../../../System-Configuration/Configuring-switchd/#restart-switchd).

</details>

<details>

<summary>Linux Commands </summary>

1. Edit the `/etc/cumulus/ports.conf` file to configure the interface for the original speed.

```
cumulus@switch:~$ sudo nano /etc/cumulus/ports.conf
...

2=100G
3=100G
4=100G
...
```

2. [Restart `switchd`](../../../System-Configuration/Configuring-switchd/#restart-switchd).

</details>

### Combine Four 10G Ports into One 40G Port

You can *gang* (combine) four 10G ports into one 40G port for use with a breakout cable, provided you follow these requirements:

- You must gang four 10G ports in sequential order. For example, you cannot gang swp1, swp10, swp20 and swp40 together.
- The ports must be in increments of four, with the starting port being swp1 (or swp5, swp9, or so forth); so you cannot gang swp2, swp3, swp4 and swp5 together.

{{%notice note%}}

The `/etc/cumulus/ports.conf` file varies across different hardware platforms. Check the current list of supported platforms on [the hardware compatibility list](http://www.cumulusnetworks.com/hcl).

{{%/notice%}}

<details>

<summary>NCLU Commands </summary>

To gang swp1 through swp4 into a 40G port, run the following commands:

```
cumulus@switch:~$ net add int swp1-4 breakout /4
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following configuration snippet in the `/etc/cumulus/ports.conf` file:

```
# SFP+ ports#
# <port label 1-48> = [10G|40G/4]
1=40G/4
2=40G/4
3=40G/4
4=40G/4
5=10G
```

</details>

<details>

<summary>Linux Commands </summary>

To gang swp1 through swp4 into a 40G port, edit the `/etc/cumulus/ports.conf` file as shown below, then  [restart `switchd`](../../../System-Configuration/Configuring-switchd/#restart-switchd).

```
# SFP+ ports#
# <port label 1-48> = [10G|40G/4]
1=40G/4
2=40G/4
3=40G/4
4=40G/4
5=10G
```

</details>

## Logical Switch Port Limitations

100G and 40G switches can support a certain number of logical ports, depending on the manufacturer; these include:

- Mellanox SN2700, SN2700B, SN2410, and SN2410B switches
- Switches with Broadcom Tomahawk, Trident II, Trident II+, and Trident3 chipsets (check the [HCL](http://cumulusnetworks.com/support/linux-hardware-compatibility-list/))

Before you configure any logical/unganged ports on a switch, check the limitations listed in `/etc/cumulus/ports.conf`; this file is specific to each manufacturer.

The following example shows the logical port limitation provided in the Dell S6000 `ports.conf` file. The maximum number of ports for this switch is 104.

```
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
```

Mellanox SN2700 and SN2700B switches have a limit of 64 logical ports in total. However, the logical ports must be configured in a specific way. See the note above.

## Verification and Troubleshooting Commands

### Statistics

To show high-level interface statistics, run the `net show interface` command:

```
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
```

To show low-level interface statistics, run the following `ethtool` command:

```
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
      HwIfOutErrors: 0
      HwIfOutQDrops: 0
      HwIfOutNonQDrops: 0
      SoftOutErrors: 0
      SoftOutDrops: 0
      SoftOutTxFifoFull: 0
      HwIfOutQLen: 0
```

### Query SFP Port Information

To verify SFP settings, run the `ethtool -m` command. The following example shows the vendor, type and power output for the swp4 interface.

```
cumulus@switch:~$ sudo ethtool -m swp4 | egrep 'Vendor|type|power\s+:'
        Transceiver type                          : 10G Ethernet: 10G Base-LR
        Vendor name                               : FINISAR CORP.
        Vendor OUI                                : 00:90:65
        Vendor PN                                 : FTLX2071D327
        Vendor rev                                : A
        Vendor SN                                 : UY30DTX
        Laser output power                        : 0.5230 mW / -2.81 dBm
        Receiver signal average optical power     : 0.7285 mW / -1.38 dBm
```

## Caveats and Errata

### Port Speed and the ifreload -a Command

When configuring port speed or break outs in the `/etc/cumulus/ports.conf` file, you need to run the `ifreload -a` command to reload the configuration after restarting `switchd` in the following cases:

- If you configure, or configure then remove, the port speed in the `/etc/cumulus/ports.conf` file and you also set or remove the speed on the same physical port or breakouts of that port in the `/etc/network/interfaces` file since the last time you restarted `switchd`.
- If you break out a switch port or remove a break out port and the port speed is set in both the `/etc/cumulus/ports.conf` file and the `/etc/network/interfaces` file.

### Port Speed Configuration

If you change the port speed in the `/etc/cumulus/ports.conf` file but the speed is also configured for that port in the `/etc/network/interfaces` file, after you edit the `/etc/cumulus/ports.conf` file and restart `switchd`, you must also run the `ifreload -a` command so that the `/etc/network/interfaces` file is also updated with your change.

### 10G and 1G SFPs Inserted in a 25G Port

For 10G and 1G SFPs inserted in a 25G port on a Broadcom platform, you must configure the four ports in the same core to be 10G. Each set of four 25G ports are controlled by a single core; therefore, each core must run at the same clock speed. The four ports must be in sequential order; for example, swp1, swp2, swp3, and swp4.

1. Edit the `/etc/cumulus/ports.conf` file and configure the four ports to be 10G. 1G SFPs are clocked at 10G speeds; therefore, for 1G SFPs, the `/etc/cumulus/ports.conf` file entry must also specify 10G. Currently you cannot use NCLU commands for this step.

```
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
```

2. [Restart `switchd`](../../../System-Configuration/Configuring-switchd/#restart-switchd).
3. If you want to set the speed of any SFPs to 1G, set the port speed to 1000 Mbps using NCLU commands; this is *not* necessary for 10G SFPs. You don't need to set the port speed to 1G for all four ports. For example, if you intend only for swp5 and swp6 to use 1G SFPs, do the following:

```
cumulus@switch:~$ net add interface swp5-swp6 link speed 1000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%notice note%}}

100G switch ASICs do not support 1000Base-X auto-negotiation (Clause 37), which is recommended for 1G fiber optical modules. As a result, single fiber breaks cannot be detected when using 1G optical modules on these switches.

The auto-negotiation setting must be the same on both sides of the connection. If using 1G fiber modules in 25G SFP28 ports, ensure auto-negotiation is disabled on the link partner interface as well.

{{%/notice%}}

### Timeout Error on Quanta LY8 and LY9 Switches

On Quanta T5048-LY8 and T3048-LY9 switches, an *Operation timed out* error occurs when you remove and reinsert a QSFP module.

You cannot remove the QSFPx2 module while the switch is powered on; it is *not* hot-swappable. However, if an *Operation timed out* error occurs, [restart `switchd`](../../../System-Configuration/Configuring-switchd/#restart-switchd) to bring the link up. Be aware that this disrupts your network.

On the T3048-LY9, run the following commands:

```
cumulus@switch:~$ sudo echo 0 > qsfpd_power_enable/value
cumulus@switch:~$ sudo rmmod quanta_ly9_rangeley_platform
cumulus@switch:~$ sudo modprobe quanta_ly9_rangeley_platform
cumulus@switch:~$ sudo systemctl restart switchd.service
```

On the T5048-LY8, run the following commands:

```
cumulus@switch:~$ sudo echo 0 > qsfpd_power_enable/value
cumulus@switch:~$ sudo systemctl restart switchd.service
```

### swp33 and swp34 Disabled on Some Switches

The front SFP+ ports (swp33 and swp34) are disabled in Cumulus Linux on the following switches:

- Dell Z9100-ON
- Penguin Arctica 3200-series switches (the 3200C, 3200XL and 3200XLP)
- Supermicro SSE-C3632S

These ports appear as disabled in the `/etc/cumulus/ports.conf` file.

### 200G Interfaces on the Dell S5248F Switch

On the Dell S5248F switch, the 2x200G QSFP-DD interfaces labeled 49/50 and 51/52 are not supported natively at 200G speeds. The interfaces are supported with 100G cables; however, you can only use one 100G from each QSFP-DD port. The upper QSFP-DD port is named swp49 and the lower QSFP-DD port is named swp52.

### QSFP+ Ports on the Dell S5232F Switch

Cumulus Linux does not support the 2x10G QSFP+ ports on the Dell S5232F switch.

### QSFP+ Ports on the Dell S4148T Switch

On the Dell S4148T switch, the two QSFP+ ports are set to `disabled` by default and the four QSFP28 ports are configured for 100G. The following example shows the default settings in the `/etc/cumulus/ports.conf` file for this switch:

```
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
```

To enable the two QSFP+ ports, you *must* configure all four QSFP28 ports for either 40G or 4x10G. You cannot use either of the QSFP+ ports if any of the QSFP28 ports are configured for 100G.

The following example shows the `/etc/cumulus/ports.conf` file with all four QSFP28 ports configured for 40G and both QSFP+ ports enabled:

```
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
```

{{%notice note%}}

To disable the QSFP+ ports, you must set the ports to `disabled`. Do not comment out the lines as this prevents `switchd` from restarting.

{{%/notice%}}

### Mellanox SN2100 Switch and eth0 Link Speed

After rebooting the Melllanox SN2100 switch, eth0 always has a speed of 100Mb/s. If you bring the interface down and then back up again, the interface negotiates 1000Mb. This only occurs the first time the interface comes up.
To work around this issue, either flap the interface or add commands to the `/etc/rc.local` file so that this occurs on boot automatically.

### Link Speed on the EdgeCore AS7326-56X Switch

On the EdgeCore AS7326-56X switch, all four switch ports in each port group must be set to the same link speed; otherwise, the links do not come up. These ports are set to 25G by default, but can also be set to 10G. The port groups on this switch are as follows, where each row is a port group:

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

For example, if you configure port 19 for 10G, you must also configure ports 16, 17 and 21 for 10G.

Additionally, you can gang each port group together as a 100G or 40G port. When ganged together, one port (based on the arrangement of the ports) is designated as the gang leader. This port's number is used to configure the ganged ports and is marked with an asterisk (\*) above.

{{%notice note%}}

The EdgeCore AS7326-56X is a 48x25G + 8x100G + 2x10G switch. The dedicated 10G ports are not currently supported in Cumulus Linux. However, you can configure all other ports to run at 10G speeds.

{{%/notice%}}

### Link Speed on the Lenovo NE2572O Switch

The Lenovo NE2572O switch has external retimers on swp1 through swp8. Currently, these ports only support a speed of 25G.

### ethtool Shows Incorrect Port Speed on 100G Spectrum Switches

On a Spectrum switch, after you set the interface speed to 40G in the `ports.conf` file, `ethtool` still shows the speed as 100G. This is a known issue where `ethtool` does not update after restarting `switchd` and continues to display the outdated port speed.

To correctly set the port speed, run the following commands.

<details>

<summary>NCLU Commands </summary>

Run the `net add interface <interface> link speed` command. The
following example command sets the port speed to 40G:

```
cumulus@switch:~$ net add interface swp1 link speed 40000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Run the `ethtool -s <interface> speed` command. The following example command sets the port speed to 40G:

```
cumulus@switch:~$ sudo ethtool -s swp1 speed 40000
```

</details>

### Delay in Reporting Interface as Operational Down

When you remove two transceivers simultaneously from a switch, both interfaces show the `carrier down` status immediately. However, it takes one second for the second interface to show the `operational down` status. In addition, the services on this interface also take an extra second to come down.

### Mellanox Spectrum-2 and Tomahawk-based Switches Support Different FEC Modes

The Mellanox Spectrum-2 (25G) switch only supports RS FEC. The Tomahawk-based switch only supports BASE-R FEC. These two switches do not share compatible FEC modes and do not interoperate reliably.

### Maverick Switches with Modules that Don't Support Auto-negotiation

On a Maverick switch, if auto-negotiation is configured on a 10G interface and the installed module does not support auto-negotiation (for example, 10G DAC, 10G Optical, 1G RJ45 SFP), the link breaks.
To work around this issue, disable auto-negotiation on interfaces where it is not supported.

## Related Information

- [Debian - Network Configuration](http://wiki.debian.org/NetworkConfiguration)
- [Linux Foundation - VLANs](http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan)
- [Linux Foundation - Bonds](http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding)
