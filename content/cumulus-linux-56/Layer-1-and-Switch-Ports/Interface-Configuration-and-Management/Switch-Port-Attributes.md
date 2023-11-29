---
title: Switch Port Attributes
author: NVIDIA
weight: 300
toc: 4
---

Cumulus Linux exposes network interfaces for several types of physical and logical devices:

- `lo` is the network loopback device
- `eth` is a switch management port (for out of band management only)
- `swp` is a switch front panel port
- (optional) `br` is a bridge (IEEE 802.1Q VLAN)
- (optional) `bond` is a bond (IEEE 802.3ad link aggregation trunk, or port channel)

Each physical network interface (port) has several settings:

- Auto-negotiation
- Duplex Mode
- Link speed
- <span style="background-color:#F5F5DC">[MTU](## "Maximum Transmission Unit")</span>
- <span style="background-color:#F5F5DC">[FEC](## "Forward Error Correction")</span>

For NVIDIA Spectrum ASICs, the firmware configures FEC, link speed, duplex mode and auto-negotiation automatically, following a predefined list of parameter settings until the link comes up. You can disable FEC if necessary, which forces the firmware to not try any FEC options.

## MTU

Interface <span style="background-color:#F5F5DC">[MTU](## "Maximum Transmission Unit")</span> applies to traffic traversing the management port, front panel or switch ports, bridge, VLAN subinterfaces, and bonds (both physical and logical interfaces). MTU is the only interface setting that you must set manually.

In Cumulus Linux, `ifupdown2` assigns 9216 as the default MTU setting. The initial MTU value set by the driver is 9238. After you configure the interface, the default MTU setting is 9216.

To change the MTU setting, run the following commands. The example command sets the MTU to 1500 for the swp1 interface.

{{< tabs "TabID227 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 link mtu 1500
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
    mtu 1500
```

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

Run the `ip link set` command. The following example command sets the swp1 interface MTU to 1500.

```
cumulus@switch:~$ sudo ip link set dev swp1 mtu 1500
```

{{%notice warning%}}
A runtime configuration is non-persistent; the configuration you create does not persist after you reboot the switch.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

### Set a Global Policy

To set a global MTU policy, create a policy document (called `mtu.json`). For example:

```
cumulus@switch:~$ sudo cat /etc/network/ifupdown2/policy.d/mtu.json
{
  "address": {"defaults": { "mtu": "9216" }
            }
}
```

{{%notice warning%}}
The policies and attributes in any file in `/etc/network/ifupdown2/policy.d/` override the default policies and attributes in `/var/lib/ifupdown2/policy.d/`.
{{%/notice%}}

### Bridge MTU

The MTU setting is the lowest MTU of any interface that is a member of the bridge (every interface specified in `bridge-ports` in the bridge configuration of the `/etc/network/interfaces` file). You are not required to specify an MTU on the bridge. Consider this bridge configuration:

```
auto bridge
iface bridge
    bridge-ports bond1 bond2 bond3 bond4 peer5
    bridge-vids 100-110
    bridge-vlan-aware yes
```

For a *bridge* to have an MTU of 9000, set the MTU for each of the member interfaces (bond1 to bond 4, and peer5) to 9000 at minimum.

When configuring MTU for a bond, configure the MTU value directly under the bond interface; the member links or slave interfaces inherit the configured value. If you need a different MTU on the bond, set it on the bond interface, as this ensures the slave interfaces pick it up. You do not have to specify an MTU on the slave interfaces.

VLAN interfaces inherit their MTU settings from their physical devices or their lower interface; for example, swp1.100 inherits its MTU setting from swp1. Therefore, specifying an MTU on swp1 ensures that swp1.100 inherits the MTU setting for swp1.

If you are working with {{<link url="Network-Virtualization" text="VXLANs">}}, the MTU for a virtual network interface (VNI must be 50 bytes smaller than the MTU of the physical interfaces on the switch, as various headers and other data require those 50 bytes. Also, consider setting the MTU much higher than 1500.

To show the MTU setting for an interface:

{{< tabs "TabID354 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv show interface swp1
...
link                                                   
  auto-negotiate           off                on       
  duplex                   full               full     
  speed                    1G                 auto     
  fec                                         auto     
  mtu                      9216               9216
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ ip link show dev swp1
3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9216 qdisc pfifo_fast state UP mode DEFAULT qlen 500
   link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
```

{{< /tab >}}
{{< /tabs >}}

### Drop Packets that Exceed the Egress Layer 3 MTU

The switch forwards all packets that are within the MTU value set for the egress layer 3 interface. However, when packets are larger in size than the MTU value, the switch fragments the packets that do *not* have the <span style="background-color:#F5F5DC">[DF](## "Don’t Fragment")</span> bit set and drops the packets that *do* have the <span style="background-color:#F5F5DC">[DF](## "Don’t Fragment")</span> bit set.

Run the following command to drop **all** IP packets that are larger in size than the MTU value for the egress layer 3 interface instead of fragmenting packets:

{{< tabs "TabID166 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system control-plane trap l3-mtu-err state off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ echo "0 >" /cumulus/switchd/config/trap/l3-mtu-err/enable
```

{{< /tab >}}
{{< /tabs >}}

## FEC

<span style="background-color:#F5F5DC">[FEC](## "Forward Error Correction")</span> is an encoding and decoding layer that enables the switch to detect and correct bit errors introduced over the cable between two interfaces. The target IEEE <span style="background-color:#F5F5DC">[BER](## "Bit Error Rate")</span> on high speed Ethernet links is 10<sup>-12</sup>. Because 25G transmission speeds can introduce a higher than acceptable BER on a link, FEC is often required to correct errors to achieve the target BER at 25G, 4x25G, 100G, and higher link speeds. The type and grade of a cable or module and the medium of transmission determine which FEC setting is necessary.

For the link to come up, the two interfaces on each end must use the same FEC setting.

{{%notice note%}}
FEC requires small latency overhead. For most applications, this small amount of latency is preferable to error packet retransmission latency.
{{%/notice%}}

The two FEC types are:
- Reed Solomon (**RS**), IEEE 802.3 Clause 108 (CL108) on individual 25G channels and Clause 91 on 100G (4channels). This is the highest FEC algorithm, providing the best bit-error correction.
- Base-R (**BaseR**), Fire Code (FC), IEEE 802.3 Clause 74 (CL74). Base-R provides less protection from bit errors than RS FEC but adds less latency.

Cumulus Linux includes additional FEC options:
- *Auto* FEC instructs the hardware to select the best FEC. For copper DAC, the remote end can negotiate FEC. However, optical modules do not have auto-negotiation capability; if the device chooses a preferred mode, it might not match the remote end. This is the current default on the NVIDIA Spectrum switch.
- *No* FEC (no error correction).

{{%notice info%}}
While *Auto* FEC is the default setting on the NVIDIA Spectrum switch, do *not* explicitly configure the `fec auto` option on the switch as this leads to a link flap whenever you run `net commit` or `ifreload -a`.
{{%/notice%}}

For **25G DAC, 4x25G Breakouts DAC and 100G DAC cables**, the IEEE 802.3by specification creates 3 classes:

- CA-25G-L (Long cable) - Requires RS FEC - Achievable cable length of at least 5m. dB loss less or equal to 22.48.  Expected BER of 10<sup>-5</sup> or better without RS FEC enabled.
- CA-25G-S (Short cable) - Requires Base-R FEC - Achievable cable length of at least 3m.  dB loss less or equal to 16.48.  Expected BER of 10<sup>-8</sup> or better without Base-R FEC enabled.
- CA-25G-N (No FEC) - Does not require FEC - Achievable cable length of at least 3m.  dB loss less or equal to 12.98. Expected BER 10<sup>-12</sup> or better with no FEC enabled.

The IEEE classification specifies various dB loss measurements and minimum achievable cable length. You can build longer and shorter cables if they comply to the dB loss and BER requirements.

If a cable has a CA-25G-S classification and FEC is not on, the BER might be unacceptable in a production network. It is important to set the FEC according to the cable class (or better) to have acceptable bit error rates. See
{{<link url="#cable-class-of-100g-and-25g-dacs" text="Determining Cable Class">}} below.

You can check bit errors using `cl-netstat` (`RX_ERR` column) or `ethtool -S` (`HwIfInErrors` counter) after a large amount of traffic passes through the link. A non-zero value indicates bit errors.
Expect error packets to be zero or extremely low compared to good packets. If a cable has an unacceptable rate of errors with FEC enabled, replace the cable.

For **25G, 4x25G Breakout, and 100G Fiber modules and AOCs**, there is no classification of 25G cable types for dB loss, BER or length. Use FEC if the BER is low enough.

### Cable Class of 100G and 25G DACs

You can determine the cable class for 100G and 25G DACs from the Extended Specification Compliance Code field (SFP28: 0Ah, byte 35, QSFP28: Page 0, byte 192) in the cable EEPROM programming.

For 100G DACs, most manufacturers use the 0x0Bh *100GBASE-CR4 or 25GBASE-CR CA-L* value (the 100G DAC specification predates the IEEE 802.3by 25G DAC specification). Use RS FEC for 100G DAC; shorter or better cables might not need this setting.

{{%notice note%}}
A manufacturer's EEPROM setting might not match the dB loss on a cable or the actual bit error rates that a particular cable introduces. Use the designation as a guide, but set FEC according to the bit error rate tolerance in the design criteria for the network. For most applications, the highest mutual FEC ability of both end devices is the best choice.
{{%/notice%}}

You can determine for which grade the manufacturer has designated the cable as follows.

For the **SFP28 DAC**, run the following command:

```
cumulus@switch:~$ sudo ethtool -m swp1 hex on | grep 0020 | awk '{ print $6}'
0c
```

The values at location 0x0024 are:

- 0x0b : CA-L (long cable - RS FEC required)
- 0x0c : CA-S (short cable - Base-R or better FEC required)
- 0x0d : CA-N (no FEC required)

For the **QSFP28 DAC**, run the following command:

```
cumulus@switch:~$ sudo ethtool -m swp1s0 hex on | grep 00c0 | awk '{print $2}'
0b
```

The values at 0x00c0 are:

- 0x0b : CA-L (long cable - RS FEC required) or 100G CR4
- 0x0c : CA-S (short cable - Base-R or better FEC required)
- 0x0d : CA-N (no FEC required)

In each example below, the *Compliance* field comes from the method described above; the `ethool -m` output does not show it.

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

The firmware in a Spectrum ASIC applies FEC configuration to 25G and 100G cables based on the cable type and whether the peer switch also has a Spectrum ASIC.

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
| 25G optical cables | Let peer decide|
| 25G 1,2 meters: CA-N, loss <13db | Let peer decide|
| 25G 2.5,3 meters: CA-S, loss <16db | Let peer decide|
| 25G 2.5,3,4,5 meters: CA-L, loss > 16db | Let peer decide|
| 100G | Let peer decide: RS-FEC or No FEC|

### How Does Cumulus Linux use FEC?

A Spectrum switch enables FEC automatically when it powers up. The port firmware tests and determines the correct FEC mode to bring the link up with the neighbor. It is possible to get a link up to a switch without enabling FEC on the remote device as the switch eventually finds a working combination to the neighbor without FEC.

The following sections describe how to show the current FEC mode, and how to enable and disable FEC.

### Show the Current FEC Mode

To show the FEC mode on a switch port, run the NVUE `nv show interface <interface> link` command.

```
cumulus@switch:~$ nv show interface swp1 link
                  operational   applied  pending  description
----------------  ------------  -------  -------  ----------------------------------------------------------------------
auto-negotiate    off           on       on       Link speed and characteristic auto negotiation
breakout                        1x       1x       sub-divide or disable ports (only valid on plug interfaces)
duplex            full          full     full     Link duplex
fec                             auto     auto     Link forward error correction mechanism
...
```

### Enable or Disable FEC

To enable **Reed Solomon (RS) FEC** on a link:

{{< tabs "TabID313 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 link fec rs
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. The following example enables RS FEC for the swp1 interface (`link-fec rs`):

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
    link-autoneg off
    link-speed 100000
    link-fec rs
```

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

Run the `ethtool --set-fec <interface> encoding RS` command. For example:

```
cumulus@switch:~$ sudo ethtool --set-fec swp1 encoding RS
```

{{%notice warning%}}
A runtime configuration is non-persistent. The configuration you create does not persist after you reboot the switch.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

To enable **Base-R/FireCode FEC** on a link:

{{< tabs "TabID366 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 link fec baser
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. The following example enables Base-R FEC for the swp1 interface (`link-fec baser`):

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
    link-autoneg off
    link-speed 100000
    link-fec baser
```

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

Run the `ethtool --set-fec <interface> encoding baser` command. For example:

```
cumulus@switch:~$ sudo ethtool --set-fec swp1 encoding BaseR
```

{{%notice warning%}}
A runtime configuration is non-persistent. The configuration you create does not persist after you reboot the switch.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

To enable FEC with Auto-negotiation:

{{%notice note%}}
You can use FEC with auto-negotiation on DACs only.
{{%/notice%}}

{{< tabs "TabID423 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 link auto-negotiate on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to set auto-negotiation to *on*, then run the `ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
link-autoneg on
```

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

You can use `ethtool` to enable FEC with auto-negotiation. For example:

```
ethtool -s swp1 speed 10000 duplex full autoneg on
```

{{%notice warning%}}
A runtime configuration is non-persistent. The configuration you create does not persist after you reboot the switch.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

To show the FEC and auto-negotiation settings for an interface, either run the NVUE `nv show interface <interface> link` command or the Linux `sudo ethtool swp1 | egrep 'FEC|auto'` command:

```
cumulus@switch:~$ sudo ethtool swp1 | egrep 'FEC|auto'
Supports auto-negotiation: Yes
Supported FEC modes: RS
Advertised auto-negotiation: Yes
Advertised FEC modes: RS
Link partner advertised auto-negotiation: Yes
Link partner advertised FEC modes: Not reported
```

To disable FEC on a link:

{{< tabs "TabID487 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 link fec off
cumulus@switch:~$ nv config apply
```

To configure FEC to the default value, run the `nv unset interface swp1 link fec` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. The following example disables Base-R FEC for the swp1 interface (`link-fec baser`):

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
link-fec off
```

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

Run the `ethtool --set-fec <interface> encoding off` command. For example:

```
cumulus@switch:~$ sudo ethtool --set-fec swp1 encoding off
```

{{%notice warning%}}
A runtime configuration is non-persistent. The configuration you create does not persist after you reboot the switch.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

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
Setting the default MTU also applies to the management interface. Be sure to add the *iface_defaults* to override the MTU for eth0, to remain at 9216.
{{%/notice%}}

## Breakout Ports

Cumulus Linux supports the following ports breakout options:
<!-- vale off -->
{{< tabs "Platforms ">}}
{{< tab "SN2010">}}

18x SFP28 25G and 4x QSFP28 100G interfaces only support NRZ encoding. You can set all speeds down to 1G.

All 4x QSFP28 ports can break out into 4x SFP28 or 2x QSFP28.

{{< tabs "SN2010 ">}}
{{< tab "1G ">}}

- 18x 1G - 18x SFP28 set to 1G
- 16x 1G - 4x QSFP28 configured as 4x breakouts and set to 1G

Max 1G ports: 34

{{< /tab >}}
{{< tab "10G ">}}

- 18x 10G - 18x SFP28 set to 10G
- 16x 10G - 4x QSFP28 configured as 4x breakouts and set to 10G

Maximum 10G ports: 34

{{< /tab >}}
{{< tab "25G ">}}

- 18x 25G - 18x SFP28 (native speed)
- 16x 25G - 4x QSFP28 breakouts to 4x and set to 25G

Maximum 25G ports: 34

{{< /tab >}}
{{< tab "40G ">}}

4x 40G - 4x QSFP28 set to 40G

Maximum 40G ports: 4

{{< /tab >}}
{{< tab "50G ">}}

8x 50G - 4x QSFP28 break out into 2x and set to 50G

Maximum 50G ports: 8

{{< /tab >}}
{{< tab "100G ">}}

4x 100G - 4x QSFP28 (native speed)

Maximum 100G ports: 4

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN2100">}}

16x QSFP28 100G interfaces only support NRZ encoding. You can set all speeds down to 1G.

All QSFP28 ports can break out into 4x SFP28 or 2x QSFP28.

{{< tabs "SN2100 ">}}
{{< tab "1G ">}}

64x 1G - 16x QSFP28 break out into 4x and set to 1G

Max 1G ports: 64

{{< /tab >}}
{{< tab "10G ">}}

64x 10G - 16x QSFP28 break out into 4x and set to 10G

Maximum 10G ports: 64

{{< /tab >}}
{{< tab "25G ">}}

64x 25G - 16x QSFP28 break out into 4x and set to 25G

Maximum 25G ports: 64

{{< /tab >}}
{{< tab "40G ">}}

16x 40G - 4x QSFP28 set to 40G

Maximum 40G ports: 16

{{< /tab >}}
{{< tab "50G ">}}

32x 50G - 16x QSFP28 break out into 2x and set to 50G

Maximum 50G ports: 32

{{< /tab >}}
{{< tab "100G ">}}

16x 100G - 16x QSFP28 (native speed)

Maximum 100G ports: 16

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN2201">}}

48x 1GBase-T ports (RJ45 up to 100m CAT5E/6) and 4x QSFP28 100G interfaces (only support NRZ encoding). You can set all speeds down to 1G.

All 4x QSFP28 ports can break out into 4x SFP28 or 2x QSFP28.

{{< tabs "SN2201 ">}}
{{< tab "1G ">}}

- 48x 1GBase-T - 48x Base-T set to 1G. You can set them to also to 10/100Mb.
- 16x 1G - 4x QSFP28 configured as 4x breakouts and set to 1G

Maximum 10/100MBase-T ports: 48
Maximum 1GBase-T ports: 48
Maximum 1G ports: 16

{{< /tab >}}
{{< tab "10G ">}}

- 16x 10G - 4x QSFP28 configured as 4x breakouts and set to 10G

Maximum 10G ports: 16

{{< /tab >}}
{{< tab "25G ">}}

- 16x 25G - 4x QSFP28 breakouts to 4x and set to 25G

Maximum 25G ports: 16

{{< /tab >}}
{{< tab "40G ">}}

4x 40G - 4x QSFP28 set to 40G

Maximum 40G ports: 4

{{< /tab >}}
{{< tab "50G ">}}

8x 50G - 4x QSFP28 break out into 2x

Maximum 50G ports: 8

{{< /tab >}}
{{< tab "100G ">}}

4x 100G - 4x QSFP28 (native speed)

Maximum 100G ports: 4

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN2410">}}

48x SFP28 25G and 8x QSFP28 100G interfaces only support NRZ encoding. You can set all speeds down to 1G.

The top 4x QSFP28 ports can break out into 4x SFP28. You cannot use the lower 4x QSFP28 disabled ports.

All 8x QSFP28 ports can break out into 2x QSFP28 without disabling ports.

{{< tabs "2410_ports ">}}
{{< tab "1G ">}}

- 48x 1G - 48x SFP28 set to 10G
- 16x 1G - 4x QSFP28 break out into 4x and set to 1G

Max 1G ports: 64

{{< /tab >}}
{{< tab "10G ">}}

- 48x 10G - 48x SFP28 set to 10G
- 16x 10G - 4x QSFP28 break out into 4x and set to 10G

Maximum 10G ports: 64

{{< /tab >}}
{{< tab "25G ">}}

- 48x 25G - 48x SFP28 (native speed)
- 16x 25G - Top 4x QSFP28 break out into 4x (bottom 4x QSFP28 disabled)

Maximum 25G ports: 64

{{< /tab >}}
{{< tab "40G ">}}

8x 40G - 8x QSFP28 set to 40G

Maximum 40G ports: 8

{{< /tab >}}
{{< tab "50G ">}}

16x 50G - 8x QSFP28 break out into 2x

Maximum 50G ports: 16

{{< /tab >}}
{{< tab "100G ">}}

8x 100G - 8x QSFP28 (native speed)

Maximum 100G ports: 8

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN2700">}}

32x QSFP28 100G interfaces only support NRZ encoding. You can set all speeds down to 1G.

The top 16x QSFP28 ports can break out into 4x SFP28. You cannot use the lower 4x QSFP28 disabled ports.

All 32x QSFP28 ports can break out into 2x QSFP28 without disabling ports.

{{< tabs "2700_ports ">}}
{{< tab "1G ">}}

64x 1G - Top 16x QSFP28 break out into 4x and set to 1G (bottom 16XQSFP28 disabled)

Max 1G ports: 64

{{< /tab >}}
{{< tab "10G ">}}

64x 10G - Top 16x QSFP28 break out into 4x and set to 10G (bottom 16x QSFP28 disabled)

Maximum 10G ports: 64

{{< /tab >}}
{{< tab "25G ">}}

64x 25G - Top 16x QSFP28 break out into 4x (bottom 16x QSFP28 disabled)

Maximum 25G ports: 64

{{< /tab >}}
{{< tab "40G ">}}

32x 40G - 32x QSFP28 set to 40G

Maximum 40G ports: 32

{{< /tab >}}
{{< tab "50G ">}}

64x 50G - 64x QSFP28 break out into 2x

Maximum 50G ports: 64

{{< /tab >}}
{{< tab "100G ">}}

32x 100G - 32x QSFP28 (native speed)

Maximum 100G ports: 32

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN3420">}}

48x SFP28 25G and 12x QSFP28 100G interfaces only support NRZ encoding. You can set all speeds down to 1G.

All 12x QSFP28 ports can break out into 4x SFP28 or 2x QSFP28.

{{< tabs "3420_ports ">}}
{{< tab "1G ">}}

- 48x 1G - 48XSFP28 set to 1G
- 48x 1G - 12XQSFP28 break out into 4x and set to 1G

Max 1G ports: 96

{{< /tab >}}
{{< tab "10G ">}}

- 48x 10G - 48x SFP28 set to 10G
- 48x 10G - 12x QSFP28 break out into 4x and set to 10G

Maximum 10G ports: 96

{{< /tab >}}
{{< tab "25G ">}}

- 48x 25G - 48x SFP28 (native speed)
- 48x 25G - 12x QSFP28 break out into 4x

Maximum 25G ports: 96

{{< /tab >}}
{{< tab "40G ">}}

12x 40G - 12x QSFP28 set to 40G

Maximum 40G ports: 12

{{< /tab >}}
{{< tab "50G ">}}

24x 50G - 12x QSFP28 break out into 2x

Maximum 50G ports: 24

{{< /tab >}}
{{< tab "100G ">}}

12x 100G - 12x QSFP28 (native speed)

Maximum 100G ports: 12

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}

<!-- SN3510 PLATFORM DELAYED UNTILL FURTHER NOTICE
{< tab "SN3510">}}

SN3510 48xSFP56 (50GbE) and 6xQSFP-DD (400GbE) interfaces support both PAM4 and NRZ encodings with all speeds down to 1G.

For lower speeds, PAM4 is automatically converted to NRZ encoding.

All 6xQSFP-DD ports can break out into 8xSFP56 (8x50GbE), 4xQSFP56 (4x100GbE), or 2xQSFP56 (2x200GbE).

{< tabs "3510_ports ">}}
{< tab "10G ">}}

- 48x10G - 48xSFP56 set to 10G
- 48x10G - 6xQSFP-DD break out into 8x50G and set to 10G

Maximum 10G ports: 96

{< /tab >}}
{< tab "25G ">}}

- 48x25G - 48xSFP56 set to 25G
- 48x25G - 6xQSFP-DD break out into 8x50G and set to 25G

Maximum 25G ports: 96

{< /tab >}}
{< tab "40G ">}}

12x40G - 12xQSFP-DD set to 40G

Maximum 40G ports: 12

{< /tab >}}
{< tab "50G ">}}

- 48x50G - 48xSFP56 (native speed)
- 48x50G - 6xQSFP-DD break out into 8x50G

Maximum 50G ports: 96

{< /tab >}}
{< tab "100G ">}}

24x100G - 6xQSFP-DD break out into 4x100G

Maximum 100G ports: 24

{< /tab >}}
{< tab "200G ">}}

12x200G - 6xQSFP-DD break out into 4x200G

Maximum 200G ports: 12

{< /tab >}}
{< tab "400G ">}}

6x400G - 6xQSFP-DD (native speed)

Maximum 400G ports: 6

{< /tab >}}
{< /tab >}}

{< /tabs >}}

-->

{{< tab "SN3700C">}}

32x QSFP28 100G interfaces only support NRZ encoding. You can set all speeds down to 1G.

All 32x QSFP28 ports can break out into 4x SFP28 or 2x QSFP28.

{{< tabs "SN3700C_ports ">}}
{{< tab "1G ">}}

128x1G - 32XQSFP28 break out into 4x and set to 1G

Max 1G ports: 128

{{< /tab >}}
{{< tab "10G ">}}

128x 10G - 32x QSFP28 break out into 4x and set to 10G

Maximum 10G ports: 128

{{< /tab >}}
{{< tab "25G ">}}

128x25G - 32x QSFP28 break out into 4x

Maximum 25G ports: 128

{{< /tab >}}
{{< tab "40G ">}}

32x 40G - 32x QSFP28 set to 40G

Maximum 40G ports: 32

{{< /tab >}}
{{< tab "50G ">}}

64x 50G - 32x QSFP28 break out into 2x

Maximum 50G ports: 64

{{< /tab >}}
{{< tab "100G ">}}

32x 100G - 32x QSFP28 (native speed)

Maximum 100G ports: 32

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN3700 and SN3750SX">}}

32x QSFP56 200G interfaces support both PAM4 and NRZ encodings. You can set all speeds down to 1G.

For lower speed interface configurations, PAM4 is automatically converted to NRZ encoding.

All 32x QSFP56 ports can break out into 4xSFP56 or 2x QSFP56.

{{< tabs "3700_ports ">}}
{{< tab "1G ">}}

128x 1G - 32XQSFP56 break out into 4x and set to 1G

Max 1G ports: 128

{{< /tab >}}
{{< tab "10G ">}}

128x 10G - 32x QSFP56 break out into 4x and set to 10G

Maximum 10G ports: 128

{{< /tab >}}
{{< tab "25G ">}}

128x 25G - 32x QSFP56 break out into 4x and set to 25G

Maximum 25G ports: 128

{{< /tab >}}
{{< tab "40G ">}}

32x 40G - 32x QSFP56 set to 40G

Maximum 40G ports: 32

{{< /tab >}}
{{< tab "50G ">}}

128x 50G - 32x QSFP56 break out into 4x

Maximum 50G ports: 128

{{< /tab >}}
{{< tab "100G ">}}

64x100G - 32x QSFP56 break out into 2x

Maximum 100G ports: 64

{{< /tab >}}
{{< tab "200G ">}}

32x 200G - 32x QSFP56 (native speed)

Maximum 200G ports: 32

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN4410">}}

SN4410 24xQSFP28-DD interfaces [ports 1-24] support both PAM4 and NRZ encoding with all speeds from 200G down to 1G.

The 8xQSFP-DD (400GbE) interfaces [ports 25-32] support both PAM4 and NRZ encodings with all speeds from 400G down to 1G.

For lower speeds, PAM4 is automatically converted to NRZ encoding.

You can split ports #1 to #32 into:
- 2x ports with PAM 4 and NRZ encoding with no limitations.
- 4x ports with PAM 4 and NRZ encoding with no limitations.
- 8x ports with PAM 4 and NRZ encoding but this forces blocking of an adjacent port (the total available number of MAC addresses is 128)

{{< tabs "4410_ports ">}}
{{< tab "1G ">}}

- 96x 1G - 24XQSFP28-DD break out into 4x and set to 1G
- 32x 1G - Top 4XQSFP-DD break out into 8x and set to 1G (bottom 4XQSFP-DD blocked*)

Max 1G ports: 128

{{< /tab >}}
{{< tab "10G ">}}

- 96x 10G - 24xQSFP28-DD break out into 4x and set to 10G
- 32x 10G - 4 top QSFP-DD break out into 8x and set to 10G (bottom 4xQSFP-DD blocked*)

Maximum 10G ports: 128

*Other QSFP-DD breakout combinations are available up to maximum of 128x ports.

{{< /tab >}}
{{< tab "25G ">}}

- 96x 25G - 24xQSFP28-DD break out into 4x
- 32x 25G - 4 top QSFP-DD break out into 8x and set to 25G (bottom 4xQSFP-DD blocked*)

Maximum 25G ports: 128

*Other QSFP-DD breakout combinations are available up to maximum of 128x ports.

{{< /tab >}}
{{< tab "40G ">}}

- 48x 40G - 24xQSFP28-DD breakout into 2x and set to 40G
- 16x 40G – 8xQSFP-DD breakout into 2x and set to 40G

Maximum 40G ports: 64

{{< /tab >}}
{{< tab "50G ">}}

- 96x 50G - 24xQSFP28-DD/QSFP56 break out into 4x
- 32x 50G - 8xQSFP-DD break out into 4x

Maximum 50G ports: 128

{{< /tab >}}
{{< tab "100G ">}}

- 96x 100G - 24xQSFP28-DD/QSFP56 break out into 4x
- 32x 100G - 8xQSFP-DD break out into 4x

Maximum 100G ports: 128

{{< /tab >}}
{{< tab "200G ">}}

- 48x 200G - 24xQSFP28-DD/QSFP56 break out into 2x
- 16x 200G - 8xQSFP-DD break out into 2x

Maximum 200G ports: 64

{{< /tab >}}
{{< tab "400G ">}}

8x400G - 8xQSFP-DD (native speed)

Maximum 400G ports: 8

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN4600C">}}

64x QSFP28 100G interfaces only support NRZ encoding. You can set all speeds down to 1G.

Only 32x QSFP28 ports can break out into 4x SFP28. You must disable the adjacent QSFP28 port. Only the first and third or second and forth rows can break out into 4xSFP28.

All 64x QSFP28 ports can break out into 2x QSFP28 without disabling ports.

{{< tabs "4600C_ports ">}}
{{< tab "1G ">}}

128x 1G - 32XQSFP28 break out into 4x and set to 1G

Max 1G ports: 128

{{< /tab >}}
{{< tab "10G ">}}

128x 10G - 32x QSFP28 break out into 4x and set to 10G

Maximum 10G ports: 128

{{< /tab >}}
{{< tab "25G ">}}

128x 25G - 32x QSFP28 break out into 4x

Maximum 25G ports: 128

{{< /tab >}}
{{< tab "40G ">}}

64x 40G - 64x QSFP28 set to 40G

Maximum 40G ports: 64

{{< /tab >}}
{{< tab "50G ">}}

128x 50G - 64x QSFP28 break out into 2x

Maximum 50G ports: 128

{{< /tab >}}
{{< tab "100G ">}}

64x 100G - 64x QSFP28 (native speed)

Maximum 100G ports: 64

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN4600">}}

SN4600 64xQSFP56 (200GbE) interfaces support both PAM4 and NRZ encodings with all speeds down to 1G.

For lower speeds, PAM4 is automatically converted to NRZ encoding.

Only 32xQSFP56 ports can break out into 4xSFP56 (4x50GbE). But, in this case, the adjacent QSFP56 port are blocked (only the first and third or second and fourth rows can break out into 4xSFP56).

All 64xQSFP56 ports can break out into 2xQSFP56 (2x100GbE) without blocking ports.

{{< tabs "4600_ports ">}}
{{< tab "1G ">}}

128x 1G - 32XQSFP56 break out into 4x and set to 1G

Max 1G ports: 128

{{< /tab >}}
{{< tab "10G ">}}

128x10G - 64xQSFP56 break out into 4x and set to 10G

Maximum 10G ports: 128

{{< /tab >}}
{{< tab "25G ">}}

128x25G - 64xQSFP56 break out into 4x and set to 25G

Maximum 25G ports: 128

{{< /tab >}}
{{< tab "40G ">}}

64x40G - 64xQSFP56 set to 40G

Maximum 40G ports: 64

{{< /tab >}}
{{< tab "50G ">}}

128x50G - 32xQSFP56 break out into 4x

Maximum 50G ports: 128

{{< /tab >}}
{{< tab "100G ">}}

- 128x 100G - 64xQSFP56 break out into 2x
- 64x 100G - 64xQSFP28 set to 100G

Maximum 100G ports: 128

{{< /tab >}}
{{< tab "200G ">}}

64x200G - 64xQSFP56 (native speed)

Maximum 200G ports: 64

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN4700">}}

SN4700 32x QSFP-DD 400GbE interfaces support both PAM4 and NRZ encodings. You can set all speeds down to 1G.

For lower speed interface configurations, PAM4 is automatically converted to NRZ encoding.

Only the top 16x QSFP-DD ports can break out into 8x SFP56. You must disable the adjacent QSFP-DD port.

All 32x QSFP-DD ports can break out into 2x QSFP56 at 2x200G or 4x QSFP56 at 4x 100G without disabling ports.

{{< tabs "4700_ports ">}}
{{< tab "1G ">}}

128x 1G - Top 16XQSFP-DD break out into 8x and set to 1G

Maximum 1G ports: 128

{{< /tab >}}
{{< tab "10G ">}}

128x 10G - 16x QSFP-DD break out into 8x and set to 10G

Maximum 10G ports: 128

*Cumulus Linux supports other QSFP-DD breakout combinations up to maximum of 128x ports.

{{< /tab >}}
{{< tab "25G ">}}

128x 25G - 16x QSFP-DD break out into 8x and set to 25G

Maximum 25G ports: 128

*Cumulus Linux supports other QSFP-DD breakout combinations up to maximum of 128x ports.

{{< /tab >}}
{{< tab "40G ">}}

32x 40G - 32x QSFP-DD set to 40G

Maximum 40G ports: 32

{{< /tab >}}
{{< tab "50G ">}}

128x 50G - 16x QSFP-DD break out into 8x

Maximum 50G ports: 128

*Cumulus Linux supports other QSFP-DD breakout combinations up to maximum of 128x ports.

{{< /tab >}}
{{< tab "100G ">}}

128x 100G - 32x QSFP-DD break out into 4x

Maximum 100G ports: 128

{{< /tab >}}
{{< tab "200G ">}}

64x 200G - 64x QSFP-DD break out into 2x

Maximum 200G ports: 64

{{< /tab >}}
{{< tab "400G ">}}

32x 400G - 32x QSFP-DD (native speed)

Maximum 400G ports: 32

{{< /tab >}}
{{< /tab >}}

{{< /tabs >}}
{{< tab "SN5600">}}

SN5600 64xOSFP (800GbE) interfaces support both PAM4 and NRZ encodings with all speeds down to 10G.

For lower speeds, PAM4 is automatically converted to NRZ encoding.

Bonus port #65 supports 1G, 10G, and 25G but does not support breakouts.

{{< tabs "5600_ports ">}}
{{< tab "1G ">}}

Maximum 1G ports: 1 (bonus port)

{{< /tab >}}
{{< tab "10G ">}}

256x 10G

Maximum 10G ports: 257 (256 + 1 bonus port)

{{< /tab >}}
{{< tab "25G ">}}

256x 25G

Maximum 25G ports: 257 (256 + 1 bonus port)

{{< /tab >}}
{{< tab "40G ">}}

128x 40G

Maximum 40G ports: 128

{{< /tab >}}
{{< tab "50G ">}}

256x 50G - 32x OSFP break out into 8x - You must disable the adjacent OSFP port.

Maximum 50G ports: 256

{{< /tab >}}
{{< tab "100G ">}}

256x 100G - 32x OSFP break out into 8x - You must disable the adjacent OSFP port.

Maximum 100G ports: 256

{{< /tab >}}
{{< tab "200G ">}}

256x 200G - 64x OSFP break out into 4x

Maximum 200G ports: 256

{{< /tab >}}
{{< tab "400G ">}}

128x 400G - 64x OSFP break out into 2x

Maximum 400G ports: 128

{{< /tab >}}
{{< tab "800G ">}}

64x 800G

Maximum 800G ports: 64

{{< /tab >}}
{{< /tab >}}

{{< /tab >}}
{{< /tabs >}}
<!-- vale on -->
{{%notice note%}}
- You can use a single SFP (10/25/50G) transceiver in a QSFP (100/200/400G) port with *QSFP-to-SFP Adapter* (QSA). Set the port speed to the SFP speed with the `nv set interface <interface> link speed <speed>` command. Do not configure this port as a breakout port.
- If you break out a port, then reload the `switchd` service on a switch running in *nonatomic* ACL mode, temporary disruption to traffic occurs while the ACLs reinstall.
- Cumulus Linux does not support port ganging.
{{%/notice%}}

### Configure a Breakout Port

You can break out (split) a port using the following options:

- `1x` does not split the port. This is the default port setting.
- `2x` splits the port into two interfaces.
- `4x` splits the port into four interfaces.
- `8x` splits the port into eight interfaces.

If you split a 100G port into four interfaces and auto-negotiation is on (the default setting), Cumulus Linux advertises the speed for each interface up to the maximum speed possible for a 100G port (100/4=25G). You can overide this configuration and set specific speeds for the split ports if necessary.

{{%notice warning%}}
- Cumulus Linux 5.4 and later uses a new format for port splitting; instead of 1=100G or 1=4x10G, you specify 1=1x or 1=4x. The new format does not support specifying a speed for breakout ports in the `/etc/cumulus/ports.conf` file. To set a speed, either set the `link-speed` parameter for each split port in the `/etc/network/interfaces` file or run the NVUE `nv set interface <interface> link speed <speed>` command.
{{%/notice%}}

{{< tabs "TabID1281 ">}}
{{< tab "NVUE Commands ">}}

The following example breaks out a 100G port on swp1 into four interfaces. Cumulus Linux advertises the speed for each interface up to a maximum of 25G:

```
cumulus@switch:~$ nv set interface swp1 link breakout 4x
cumulus@switch:~$ nv set interface swp1s0-3 link state up
cumulus@switch:~$ nv config apply
```

The following example splits the port into four interfaces and forces the link speed to be 10G. Cumulus disables auto-negotiation when you force set the speed.

```
cumulus@switch:~$ nv set interface swp1 link breakout 4x
cumulus@switch:~$ nv set interface swp1s0-3 link state up
cumulus@switch:~$ nv set interface swp1s0-3 link speed 10G
```

{{%notice note%}}

Certain switches, such as the SN2700, SN4600, and SN4600c, require that you disable the subsequent even-numbered port when you configure a breakout port for 4x or 8x. NVUE automatically disables the subsequent even-numbered port on any switch with this requirement.
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. To split a port into multiple interfaces, edit the `/etc/cumulus/ports.conf` file. The following example command breaks out swp1 into four interfaces.

   ```
   cumulus@switch:~$ sudo cat /etc/cumulus/ports.conf
   ...
   1=4x 
   2=disabled 
   3=1x 
   4=1x 
   ...
   ```

   {{%notice note%}}
When you configure a breakout port to 4x or 8x on certain switches such as the SN2700, SN4600, and SN4600c, you must set the subsequent even-numbered port to `disabled` in the `/etc/cumulus/ports.conf` file. The SN3700, SN3700c, SN2201, SN2010, and SN2100 switch does not have this requirement.
{{%/notice%}}

2. Reload `switchd` with the `sudo systemctl reload switchd.service` command. The reload does **not** interrupt network services.

   ```
   cumulus@switch:~$ sudo systemctl reload switchd.service
   ```

3. To configure specific speeds for the split ports, edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. The following example configures the speed for each swp1 breakout port (swp1s0, swp1s1, swp1s2, and swp1s3) to 10G with auto-negotiation off.

```
cumulus@switch:~$ sudo cat /etc/network/interfaces
...
auto swp1s0
iface swp1s0
    link-speed 10000 
    link-duplex full 
    link-autoneg off
auto swp1s1
iface swp1s1
    link-speed 10000 
    link-duplex full 
    link-autoneg off
auto swp1s2
iface swp1s2
    link-speed 10000 
    link-duplex full 
    link-autoneg off
auto swp1s3
iface swp1s3
    link-speed 10000 
    link-duplex full 
    link-autoneg off
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

The SN4700 and SN4410 switch does not support auto-negotiation on QSFP-DD 400G transceiver modules. You need to force set the speed.

### Set the Number of Lanes per Split Port

By default, to calculate the split port width, Cumulus Linux uses the formula `split port width = full port width / breakout`. For example, a port split into two interfaces (2x breakout) => 8 lanes width / 2x breakout = 4 lanes per split port.

If you need to use a different port width than the default, you can set the number of lanes per port.

{{%notice note%}}
QSFP56-DD transceiver ports split into four interfaces (4x) default to one lane per interface for backwards compatibility. You can change the lane setting to two lanes per interface.
{{%/notice%}}

The following example command splits swp1 into two interfaces (2x) and sets the number of lanes per split port to 2.

{{< tabs "TabID1383 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 link breakout 2x lanes-per-port 2
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
You must configure the lanes-per-port at the same time as you configure the breakout. If you want to change the number of lanes per port after you configure a breakout, you must first unset the breakout with the `nv unset interface <port> breakout` and `nv config apply` commands, then reconfigure the breakout and the lanes with the `nv set interface <interface> link breakout <breakout> lanes-per-port <lanes>` command. For example:

```
cumulus@switch:~$ nv unset interface swp1 breakout
cumulus@switch:~$ nv config apply
cumulus@switch:~$ nv set interface swp1 link breakout 2x lanes-per-port 2
cumulus@switch:~$ nv config apply
```
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/ports_width.conf` file and add the numer of lanes per split port you want to use, then reload `switchd`:

{{%notice note%}}
You must configure the lanes per port in the `/etc/cumulus/ports_width.conf` before you configure the breakout in the `/etc/cumulus/ports.conf` file. If the `ports.conf` file already contains breakout configuration for a port, you must set the breakout back to `1x`, then reload `switchd`. You can then set the desired lanes per port, then reconfigure the breakout.
{{%/notice%}}

```
cumulus@switch:~$ sudo nano /etc/cumulus/ports_width.conf
...
1=2
2=default
3=default
4=default
5=default
6=default
7=default
8=default
...
```

```
cumulus@switch:~$ sudo systemctl reload switchd.service
```

{{< /tab >}}
{{< /tabs >}}

### Remove a Breakout Port

To remove a breakout port:

{{< tabs "TabID1361 ">}}
{{< tab "NVUE Commands ">}}

1. Run the `nv unset interface <interface>` command. For example:

   ```
   cumulus@switch:~$ nv unset interface swp1s0
   cumulus@switch:~$ nv unset interface swp1s1
   cumulus@switch:~$ nv unset interface swp1s2
   cumulus@switch:~$ nv unset interface swp1s3
   cumulus@switch:~$ nv config apply
   ```

2. Run the `nv unset interface <interface> link breakout` command to configure the interface for the original speed. For example:

   ```
   cumulus@switch:~$ nv unset interface swp1 link breakout
   cumulus@switch:~$ nv config apply
   ```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/cumulus/ports.conf` file to configure the interface for the original speed.

    ```
    cumulus@switch:~$ sudo nano /etc/cumulus/ports.conf
    ...
    1=1x 
    2=1x 
    3=1x 
    4=1x 
    ...
    ```

2. Reload `switchd`. The reload does **not** interrupt network services.

   ```
   cumulus@switch:~$ sudo systemctl reload switchd.service
   ```

3. Remove the breakout interface configuration from the `/etc/network/interfaces` file, then run the `ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

## Configure Port Lanes

You can override the default behavior for supported speeds and platforms and specify the number of lanes for a port. For example, for the NVIDIA SN4700 switch, the default port speed is 50G (2 lanes, <span style="background-color:#F5F5DC">[NRZ](## "Non-Return-to-Zero")</span> signaling mode) and 100G (4 lanes, NRZ signaling mode). You can override this setting to 50G (1 lane, <span style="background-color:#F5F5DC">[PAM4](## "Pulse Amplitude Modulation 4-level")</span> signaling mode) and 100G (2 lanes, PAM4 signaling mode).

{{%notice note%}}
This setting does not apply when auto-negotiation is on because Cumulus Linux advertises all supported speed options, including PAM4 and NRZ during auto-negotiation.
{{%/notice%}}

{{< tabs "TabID1415 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 link speed 50G
cumulus@switch:~$ nv set interface swp1 link lanes 1
cumulus@switch:~$ nv config apply 
```

```
cumulus@switch:~$ nv set interface swp2 link speed 100G
cumulus@switch:~$ nv set interface swp2 link lanes 2
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

   ```
   cumulus@switch:~$ sudo nano /etc/network/interfaces
   ...
   auto swp1
   iface swp1
       link-lanes 1
       link-speed 50000
   auto swp2
   iface swp2
       link-lanes 2
       link-speed 100000
   ```

2. Run the `ifreload -a` command:

   ```
   cumulus@switch:~$ sudo ifreload -a
   ```

{{< /tab >}}
{{< /tabs >}}

<!-- vale off -->
## ports.conf File Validator
<!-- vale on -->
Cumulus Linux includes a `ports.conf` validator that `switchd` runs automatically before the switch starts up to confirm that the file syntax is correct. You can run the validator manually to verify the syntax of the file whenever you make changes. The validator is useful if you want to copy a new `ports.conf` file to the switch with automation tools, then validate that it has the correct syntax.

To run the validator manually, run the `/usr/cumulus/bin/validate-ports -f <file>` command. For example:

```
cumulus@switch:~$ /usr/cumulus/bin/validate-ports -f /etc/cumulus/ports.conf
```

## Troubleshooting

This section shows basic commands for troubleshooting switch ports. For a more comprehensive troubleshooting guide, see {{<link url="Troubleshoot-Layer-1">}}.

### Interface Settings

To see all settings for an interface, run the `nv show interface <interface>` command:

```
cumulus@switch:~$ nv show interface swp1                          operational        applied
------------------------  -----------------  -------
type                      swp                swp    
[acl]                                               
evpn                                                
  multihoming                                       
    uplink                                   off    
ptp                                                 
  enable                                     off    
router                                              
  adaptive-routing                                  
    enable                                   off    
  ospf                                              
    enable                                   off    
  ospf6                                             
    enable                                   off    
  pbr                                               
    [map]                                           
  pim                                               
    enable                                   off    
synce                                               
  enable                                     off    
ip                                                  
  igmp                                              
    enable                                   off    
  ipv4                                              
    forward                                  on     
  ipv6                                              
    enable                                   on     
    forward                                  on     
  neighbor-discovery                                
    enable                                   on     
    [dnssl]                                         
    home-agent                                      
      enable                                 off    
    [prefix]                                        
    [rdnss]                                         
    router-advertisement                            
      enable                                 off    
  vrrp                                              
    enable                                   off    
  vrf                                        default
  [gateway]                                         
link                                                
  auto-negotiate          off                on     
  duplex                  full               full   
  speed                   1G                 auto   
  fec                                        auto   
  mtu                     9000               9216   
  fast-linkup             off                       
  [breakout]                                        
  state                   up                 up     
  stats                                             
    carrier-transitions   4                         
    in-bytes              600 Bytes                 
    in-drops              5                         
    in-errors             0                         
    in-pkts               10                        
    out-bytes             2.11 MB                   
    out-drops             0                         
    out-errors            0                         
    out-pkts              33143                     
  mac                     48:b0:2d:39:3f:83         
ifindex                   3
```

You can add the `--view` option to show different views: `acl-statistics`, `brief`, `detail`, `lldp`, `mac`, `mlag-cc`, `pluggables`, `qos-profile`, and `small`. For example, the `nv show interface --view=small` command lists the interfaces on the switch. The `nv show interface --view=brief` command shows information about each interface on the switch, such as the interface type, speed, remote host and port. The `nv show interface --view=mac` command shows the MAC address of each interface.

The description column only shows in the output when you use the `--view=detail` option.

The following example shows the MAC address of each interface on the switch:

```
cumulus@switch:~$ nv show interface --view=mac
Interface   State  Speed  MTU    MAC                Type    
----------  -----  -----  -----  -----------------  --------
BLUE        up            65575  2a:f9:b5:3c:74:b8  vrf     
RED         up            65575  8e:91:ed:ed:d5:76  vrf     
bond1       up     1G     9000   48:b0:2d:39:3f:83  bond    
bond2       up     1G     9000   48:b0:2d:b3:5e:18  bond    
bond3       up     1G     9000   48:b0:2d:c2:9d:47  bond    
br_default  up            9216   44:38:39:22:01:7a  bridge  
br_l3vni    up            9216   44:38:39:22:01:7a  bridge  
eth0        up     1G     1500   44:38:39:22:01:7a  eth     
lo          up            65536  00:00:00:00:00:00  loopback
mgmt        up            65575  8a:58:d0:25:47:7d  vrf     
swp1        up     1G     9000   48:b0:2d:39:3f:83  swp     
swp2        up     1G     9000   48:b0:2d:b3:5e:18  swp     
swp3        up     1G     9000   48:b0:2d:c2:9d:47  swp     
swp4        down          1500   48:b0:2d:c2:7e:cd  swp     
swp5        down          1500   48:b0:2d:6e:bc:c1  swp     
swp6        down          1500   48:b0:2d:2d:89:16  swp 
...
```

You can filter the `nv show interface` command output on specific columns. For example, the `nv show interface --filter mtu=1500` shows only the interfaces with MTU set to 1500.

To filter on multiple column outputs, enclose the filter types in parentheses; for example, `nv show interface --filter "type=bridge&mtu=9216"` shows data for bridges with MTU 9216.

You can filter on all revisions (operational, applied, and pending); for example, `nv show interface --filter mtu=1500 --rev=applied` shows only the interfaces with MTU set to 1500 in the applied revision.

The following example shows information for all bridges configured on the switch with MTU 9216:

```
cumulus@switch:~$ nv show interface --filter "type=bridge&mtu=9216"
Interface   State  Speed  MTU   Type    Remote Host  Remote Port  Summary                                
----------  -----  -----  ----  ------  -----------  -----------  ---------------------------------------
br_default  up            9216  bridge                            IP Address: fe80::4638:39ff:fe22:17a/64
br_l3vni    up            9216  bridge                            IP Address: fe80::4638:39ff:fe22:17a/64
```

### Statistics

To show interface statistics, run the NVUE `nv show interface <interface> counters` command or the Linux `sudo ethtool -S <interface>` command.

```
cumulus@switch:~$ nv show interface swp1 counters
                    operational  applied
-------------------  -----------  -------
carrier-transitions  4                   
in-bytes             3.37 MB             
in-drops             0                   
in-errors            0                   
in-pkts              29025               
out-bytes            4.28 MB             
out-drops            0                   
out-errors           0                   
out-pkts             43945  
...
```

For more information about showing and clearing interface counters, refer to {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE" text="Monitoring Interfaces and Transceivers with NVUE">}}.

### SFP Port Information

To verify SFP settings, run the NVUE `nv show interface <interface> pluggable` command or the `ethtool -m` command. The following example shows the vendor, type and power output for swp1.

```
cumulus@switch:~$ sudo ethtool -m swp1 | egrep 'Vendor|type|power\s+:'
        Transceiver type                          : 10G Ethernet: 10G Base-LR
        Vendor name                               : FINISAR CORP.
        Vendor OUI                                : 00:90:65
        Vendor PN                                 : FTLX2071D327
        Vendor rev                                : A
        Vendor SN                                 : UY30DTX
        Laser output power                        : 0.5230 mW / -2.81 dBm
        Receiver signal average optical power     : 0.7285 mW / -1.38 dBm
```

## Considerations
<!-- vale off -->
<!-- Vale issue #253 -->
### Auto-negotiation and FEC
<!-- vale on -->
If auto-negotiation is off on 100G and 25G interfaces, you must set FEC to *OFF*, RS, or BaseR to match the neighbor. The FEC default setting of *auto* does not link up when auto-negotiation is off.
<!-- vale off -->
<!-- Vale issue #253 -->
### Auto-negotiation and Link Speed
<!-- vale on -->
If auto-negotiation is on and you set the link speed for a port, Cumulus Linux disables auto-negotiation and uses the port speed setting you configure.
<!-- vale off -->
<!-- Vale issue #253 -->

### Auto-negotiation with the Spectrum-4 Switch

When you connect an NVIDIA Spectrum-4 switch to another NVIDIA Spectrum-4 switch with PAM4 modulation, you must enable auto-negotiation.

<!--
When you use copper cables to connect an NVIDIA Spectrum-4 switch to another NVIDIA Spectrum-4 switch with PAM4 modulation, you must enable auto-negotiation.
-->

### 1000BASE-T SFP Modules Supported Only on Certain 25G Platforms
<!-- vale on -->
The following  25G switches support 1000BASE-T SFP modules:

- NVIDIA SN2410
- NVIDIA SN2010
<!-- - NVIDIA SN3420-->

100G or faster switches do not support 1000BASE-T SFP modules.

### NVIDIA SN2100 Switch and eth0 Link Speed

After rebooting the NVIDIA SN2100 switch, eth0 always has a speed of 100MB per second. If you bring the interface down and then back up again, the interface negotiates 1000MB. This only occurs the first time the interface comes up.

To work around this issue, add the following commands to the `/etc/rc.local` file to flap the interface automatically when the switch boots:

```
modprobe -r igb
sleep 20
modprobe igb
```

### NVIDIA SN5600 Switch and Force Mode

When you configure force mode on NVIDIA SN5600 switch ports 10 through 50, the Rx precoding setting must be the same between local and peer ports to get the optimal Signal-Integrity of the link.

### Delay in Reporting Interface as Operational Down

When you remove two transceivers simultaneously from a switch, both interfaces show the `carrier down` status immediately. However, it takes one second for the second interface to show the `operational down` status. In addition, the services on this interface also take an extra second to come down.

<!-- vale off -->
<!-- Vale issue #253 -->
### NVIDIA Spectrum-2 Switches and FEC Mode
<!-- vale on -->

The NVIDIA Spectrum-2 (25G) switch only supports RS FEC.

## Related Information

- {{<exlink url="http://wiki.debian.org/NetworkConfiguration" text="Debian - Network Configuration">}}
