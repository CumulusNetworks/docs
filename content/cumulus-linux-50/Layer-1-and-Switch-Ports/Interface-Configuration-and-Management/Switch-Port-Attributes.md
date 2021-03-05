---
title: Switch Port Attributes
author: NVIDIA
weight: 300
toc: 4
---

Cumulus Linux exposes network interfaces for several types of physical and logical devices:

- `lo` is the network loopback device
- `ethN` are switch management ports (for out of band management only)
- `swpN` are switch front panel ports
- (optional) `brN` are bridges (IEEE 802.1Q VLANs)
- (optional) `bondN` are bonds (IEEE 802.3ad link aggregation trunks, or port channels)

Each physical network interface (port) has a number of settings:

- Auto-negotiation
- Duplex Mode
- Link speed
- MTU (maximum transmission unit)
- FEC (forward error correction)

For **Spectrum ASICs**, MTU is the only port attribute you can directly configure. The Spectrum firmware configures FEC, link speed, duplex mode and auto-negotiation automatically, following a predefined list of parameter settings until the link comes up. However, you can disable FEC if necessary, which forces the firmware to not try any FEC options.

## MTU

Interface MTU applies to traffic traversing the management port, front panel or switch ports, bridge, VLAN subinterfaces, and bonds (both physical and logical interfaces). MTU is the only interface setting that you must set manually.

In Cumulus Linux, `ifupdown2` assigns 9216 as the default MTU setting. The initial MTU value set by the driver is 9238. After you configure the interface, the default MTU setting is 9216.

To change the MTU setting, run the following commands:

{{< tabs "TabID227 ">}}

{{< tab "NCLU Commands ">}}

Run the `net add interface <interface> mtu` command. The following example command sets the MTU to 1500 for the swp1 interface.

```
cumulus@switch:~$ net add interface swp1 mtu 1500
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following code snippet:

```
auto swp1
iface swp1
    mtu 1500
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. The following example sets the MTU to 1500 for the swp1 interface.

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

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

### Set a Global Policy

For a global policy to set MTU, create a policy document (called `mtu.json`). For example:

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

For *bridge* to have an MTU of 9000, set the MTU for each of the member interfaces (bond1 to bond 4, and peer5) to 9000 at minimum.

{{%notice tip%}}

**Use MTU 9216 for a bridge**

Two common MTUs for jumbo frames are 9216 (the default value) and 9000 bytes. The corresponding MTUs for the VNIs are 9166 and 8950.

{{%/notice%}}

When configuring MTU for a bond, configure the MTU value directly under the bond interface; the configured value is inherited by member links/slave interfaces. If you need a different MTU on the bond, set it on the bond interface, as this ensures the slave interfaces pick it up. You are not required to specify an MTU on the slave interfaces.

VLAN interfaces inherit their MTU settings from their physical devices or their lower interface; for example, swp1.100 inherits its MTU setting from swp1. Therefore, specifying an MTU on swp1 ensures that swp1.100 inherits the MTU setting for swp1.

If you are working with {{<link url="Network-Virtualization" text="VXLANs">}}, the MTU for a virtual network interface (VNI must be 50 bytes smaller than the MTU of the physical interfaces on the switch, as those 50 bytes are required for various headers and other data. Also, consider setting the MTU much higher than 1500.

{{%notice note%}}

The MTU for an SVI interface, such as vlan100, is derived from the bridge. When you use NCLU to change the MTU for an SVI and the MTU setting is higher than it is for the other bridge member interfaces, the MTU for all bridge member interfaces changes to the new setting. If you need to use a mixed MTU configuration for SVIs, (if some SVIs have a higher MTU and some lower), set the MTU for all member interfaces to the maximum value, then set the MTU on the specific SVIs that need to run at a lower MTU.

{{%/notice%}}

To show the MTU setting for an interface:

{{< tabs "TabID354 ">}}

{{< tab "NCLU Commands ">}}

Run the `net show interface <interface>` command:

```
cumulus@switch:~$ net show interface swp1
    Name    MAC                Speed      MTU  Mode
--  ------  -----------------  -------  -----  ---------
UP  swp1    44:38:39:00:00:04  1G        9216  Access/L2
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Run the `ip link show <interface>` command:

```
cumulus@switch:~$ ip link show dev swp1
3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9216 qdisc pfifo_fast state UP mode DEFAULT qlen 500
   link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
```

{{< /tab >}}

{{< /tabs >}}

## FEC

{{<exlink url="https://en.wikipedia.org/wiki/Forward_error_correction" text="Forward Error Correction (FEC)">}} is an encoding and decoding layer that enables the switch to detect and correct bit errors introduced over the cable between two interfaces. The target IEEE bit error rate (BER) on high speed ethernet link is 10<sup>-12</sup>. Because 25G transmission speeds can introduce a higher than acceptable BER on a link, FEC is often required to correct errors to achieve the target BER at 25G, 4x25G, 100G, and higher link speeds.  The type and grade of a cable or module and the medium of transmission will determine which FEC setting is needed.

For the link to come up, the two interfaces on each end must use the same FEC setting.

{{%notice note%}}

There is a very small latency overhead required for FEC. For most applications, this small amount of latency is preferable to error packet retransmission latency.

{{%/notice%}}

There are two FEC types:

- Reed Solomon (**RS**), IEEE 802.3 Clause 108 (CL108) on individual 25G channels and Clause 91 on 100G (4channels). This is the highest FEC algorithm, providing the best bit-error correction.
- Base-R (**BaseR**), Fire Code (FC), IEEE 802.3 Clause 74 (CL74). Base-R provides less protection from bit errors than RS FEC but adds less latency.

Cumulus Linux includes additional FEC options:

- *Auto* FEC instructs the hardware to select the best FEC. For copper DAC, FEC can be negotiated with the remote end. However, optical modules do not have auto-negotiation capability; if the device chooses a preferred mode, it might not match the remote end. This is the current default on a Spectrum switch.
- *No* FEC (no error correction is done).

For **25G DAC, 4x25G Breakouts DAC and 100G DAC cables**, the IEEE 802.3by specification creates 3 classes:

- CA-25G-L (Long cable) - Requires RS FEC - Achievable cable length of at least 5m. dB loss less or equal to 22.48.  Expected BER of 10<sup>-5</sup> or better without RS FEC enabled.
- CA-25G-S (Short cable) - Requires Base-R FEC - Achievable cable length of at least 3m.  dB loss less or equal to 16.48.  Expected BER of 10<sup>-8</sup> or better without Base-R FEC enabled.
- CA-25G-N (No FEC) - Does not require FEC - Achievable cable length of at least 3m.  dB loss less or equal to 12.98. Expected BER 10<sup>-12</sup> or better with no FEC enabled.

The IEEE classification is based on various dB loss measurements and minimum achievable cable length. You can build longer and shorter cables if they comply to the dB loss and BER requirements.

If a cable is manufactured to CA-25G-S classification and FEC is not enabled, the BER might be unacceptable in a production network. It is important to set the FEC according to the cable class (or better) to have acceptable bit error rates. See
{{<link url="#determine-cable-class-of-100g-and-25g-dacs" text="Determining Cable Class">}} below.

You can check bit errors using `cl-netstat` (`RX_ERR` column) or `ethtool -S` (`HwIfInErrors` counter) after a large amount of traffic has passed through the link. A non-zero value indicates bit errors.
Expect error packets to be zero or extremely low compared to good packets. If a cable has an unacceptable rate of errors with FEC enabled, replace the cable.

For **25G, 4x25G Breakout, and 100G Fiber modules and AOCs**, there is no classification of 25G cable types for dB loss, BER or length. FEC is recommended but might not be required if the BER is low enough.

### Cable Class of 100G and 25G DACs

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

A Spectrum switch enables FEC automatically when it powers up. The port firmware tests and determines the correct FEC mode to bring the link up with the neighbor. It is possible to get a link up to a Spectrum switch without enabling FEC on the remote device as the switch eventually finds a working combination to the neighbor without FEC.

The following sections describe how to show the current FEC mode, and to enable and disable FEC.

### Show the Current FEC Mode

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

{{< tabs "TabID568 ">}}

{{< tab "NCLU Commands ">}}

Run the `net add interface <interface> link fec rs` command. For example:

```
cumulus@switch:~$ sudo net add interface swp23 link fec rs
cumulus@switch:~$ sudo net pending
cumulus@switch:~$ sudo net commit
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

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

To enable **Base-R/FireCode FEC** on a link:

{{< tabs "TabID620 ">}}

{{< tab "NCLU Commands ">}}

Run the `net add interface <interface> link fec baser` command. For example:

```
cumulus@switch:~$ sudo net add interface swp23 link fec baser
cumulus@switch:~$ sudo net pending
cumulus@switch:~$ sudo net commit
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

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

To enable FEC with Auto-negotiation:

{{%notice note%}}

FEC with auto-negotiation is supported on DACs only.

{{%/notice%}}

{{< tabs "TabID678 ">}}

{{< tab "NCLU Commands ">}}

Run the `net add interface <interface> link autoneg` `on` command. The following example command enables FEC with auto-negotiation on the swp12 interface:

```
cumulus@switch:~$ sudo net add interface swp12 link autoneg on
cumulus@switch:~$ sudo net pending
cumulus@switch:~$ sudo net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to set auto-negotiation to *on*, then run the `ifreload -a` command. For example:

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

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

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

{{< tabs "TabID741 ">}}

{{< tab "NCLU Commands ">}}

Run the `net add interface <interface> link fec off` command. For example:

```
cumulus@switch:~$ sudo net add interface swp23 link fec off
cumulus@switch:~$ sudo net pending
cumulus@switch:~$ sudo net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. The following example disables Base-R FEC for the swp1 interface (`link-fec baser`):

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp23
iface swp23
link-fec off
```

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

Cumulus Linux lets you:
- Break out 100G switch ports into 2x50G, 4x25G, or 4x10G with breakout cables.
- Break out 40G switch ports into four separate 10G ports (4x10G) for use with breakout cables.

{{%notice note%}}

- If you break out a port, then reload the `switchd` service on a switch running in *nonatomic* ACL mode, temporary disruption to traffic occurs while the ACLs are reinstalled.
- Port ganging is not supported.
- Mellanox switches with the Spectrum 1 ASIC have a limit of 64 logical ports. If you want to break ports out to 4x25G or 4x10G, you must configure the logical ports as follows:
  - You can only break out odd-numbered ports into four logical ports.
  - You must disable the next even-numbered port. For example, if you break out port 11 into four logical ports, you must disable port 12.
  These restrictions do *not* apply to a 2x50G breakout configuration or to the Mellanox SN2100 and SN2010 switches.
- Mellanox switches with the Spectrum 2 and Spectrum 3 ASIC have a limit of 128 logical ports. To ensure that the number of total logical interfaces does not exceed the limit, if you split ports into four interfaces on Spectrum 2 and Spectrum 3 switches with 64 interfaces, you must disable the adjacent port. For example, when splitting port 1 into four 25G interfaces, you must disable port 2 in the `/etc/cumulus/ports.conf` file:

    ```
    1=4x25G
    2=disabled
    ```

   When you split a port into two interfaces, such as 2x50G, you do **not** have to disable the adjacent port.

Valid port configuration and breakout guidance is provided in the `/etc/cumulus/ports.conf` file.

{{%/notice%}}

### Configure a Breakout Port

To configure a breakout port:

{{< tabs "TabID883 ">}}

{{< tab "NCLU Commands ">}}

This example command breaks out the 100G port on swp3 into four 25G ports:

```
cumulus@switch:~$ net add interface swp3 breakout 4x
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To break out swp3 into four 10G ports, run the `net add interface swp3 breakout 4x10G` command.

On Mellanox switches with the Spectrum ASIC, you need to disable the next port. The following example command disables swp4.

```
cumulus@switch:~$ net add interface swp4 breakout disabled
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands break out swp3 into four 25G interfaces in the `/etc/cumulus/ports.conf` file and create four interfaces in the `/etc/network/interfaces` file:

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

When you commit your change, `switchd` reloads and there is no interruption to network services.

{{< /tab >}}

{{< tab "Linux Commands ">}}

1. Edit the `/etc/cumulus/ports.conf` file to configure the port breakout. The following example breaks out the 100G port on swp3 into four 25G ports. To break out swp3 into four 10G ports, use 3=4x10G. You also need to disable the next port. The example also disables swp4.

   ```
   cumulus@switch:~$ sudo cat /etc/cumulus/ports.conf
   ...
   1=100G
   2=100G
   3=4x25G
   4=disabled
   ...
   ```

2. Configure the breakout ports in the `/etc/network/interfaces` file. The following example shows the swp3 breakout ports (swp1s0, swp1s1, swp1s2, and swp1s3).

```
cumulus@switch:~$ sudo cat /etc/network/interfaces
...
auto swp3s0
iface swp1s0

auto swp3s1
iface swp3s1

auto swp3s2
iface swp3s2

auto swp3s3
iface swp310s3
...
```

Reload `switchd` with the `sudo systemctl reload switchd.service` command. The reload does **not** interrupt network services.

```
cumulus@switch:~$ sudo systemctl reload switchd.service
```

{{< /tab >}}

{{< /tabs >}}

### Remove a Breakout Port

To remove a breakout port:

{{< tabs "TabID987 ">}}

{{< tab "NCLU Commands ">}}

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

    1=100G
    2=100G
    3=100G
    4=100G
    ...
    ```

Reload `switchd` with the `sudo systemctl reload switchd.service` command. The reload does **not** interrupt network services.

```
cumulus@switch:~$ sudo systemctl reload switchd.service
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

1. Edit the `/etc/cumulus/ports.conf` file to configure the interface for the original speed.

    ```
    cumulus@switch:~$ sudo nano /etc/cumulus/ports.conf
    ...

    1=100G
    2=100G
    3=100G
    4=100G
    ...
    ```

2. Reload `switchd` with the `sudo systemctl reload switchd.service` command. The reload does **not** interrupt network services.

   ```
   cumulus@switch:~$ sudo systemctl reload switchd.service
   ```

{{< /tab >}}

{{< /tabs >}}

## Logical Switch Port Limitations

100G and 40G switches can support a certain number of logical ports depending on the switch. Before you configure any logical ports on a switch, check the limitations listed in `/etc/cumulus/ports.conf`.

The following example shows the logical port limitation provided in a `ports.conf` file. The maximum number of ports for this switch is 128.

```
# ports.conf --
#
#        This file controls port speed, aggregation and subdivision.
#
# For example, the zQSFP ports can be split into multiple interfaces. This
# file sets the number of interfaces per port and the speed of those interfaces.
#
# You must reload switchd for changes to take effect.
#
# mlnx,x86_MSN3700c has:
#     32 QSFP28 ports numbered 1-32
#         These ports are configurable as 40G, 50G, 2x50G, or 100G; or can be
#         split into 4x25G or 4x10G.
#

# QSFP28 ports
#
# <port label>    = [40G|50G|100G]
#   or when split = [2x50G|4x10G|4x25G|disabled]
...
```

Mellanox SN2700 and SN2700B switches have a limit of 64 logical ports in total. However, the logical ports must be configured in a specific way. See the note above.

## Verification and Troubleshooting Commands

Following are two basic commands for troubleshooting switch ports. For a more comprehensive troubleshooting guide, read {{<link url="Troubleshoot-Layer-1">}}.

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

## Considerations

### Auto-negotiation and FEC

If auto-negotiation is disabled on 100G and 25G interfaces, you must set FEC to *OFF*, RS, or BaseR to match the neighbor. The FEC default setting of *auto* does not link up when auto-negotiation is disabled.

### Port Speed and the ifreload -a Command

When configuring port speed or break outs in the `/etc/cumulus/ports.conf` file, you need to run the `ifreload -a` command to reload the configuration after restarting `switchd` in the following cases:

- If you configure, or configure then remove, the port speed in the `/etc/cumulus/ports.conf` file and you also set or remove the speed on the same physical port or breakouts of that port in the `/etc/network/interfaces` file since the last time you restarted `switchd`.
- If you break out a switch port or remove a break out port and the port speed is set in both the `/etc/cumulus/ports.conf` file and the `/etc/network/interfaces` file.

### Port Speed Configuration

If you change the port speed in the `/etc/cumulus/ports.conf` file but the speed is also configured for that port in the `/etc/network/interfaces` file, after you edit the `/etc/cumulus/ports.conf` file and restart `switchd`, you must also run the `ifreload -a` command so that the `/etc/network/interfaces` file is also updated with your change.

### 1000BASE-T SFP Modules Supported Only on Certain 25G Platforms

1000BASE-T SFP modules are supported on the following 25G platforms:

- Mellanox SN2410
- Mellanox SN2010

1000BASE-T SFP modules are not supported on any 100G or faster platforms.

### Mellanox SN2100 Switch and eth0 Link Speed

After rebooting the Melllanox SN2100 switch, eth0 always has a speed of 100Mb/s. If you bring the interface down and then back up again, the interface negotiates 1000Mb. This only occurs the first time the interface comes up.

To work around this issue, add the following commands to the `/etc/rc.local` file to flap the interface automatically when the switch boots:

```
modprobe -r igb
sleep 20
modprobe igb
```

### Delay in Reporting Interface as Operational Down

When you remove two transceivers simultaneously from a switch, both interfaces show the `carrier down` status immediately. However, it takes one second for the second interface to show the `operational down` status. In addition, the services on this interface also take an extra second to come down.

### Mellanox Spectrum-2 Switches and FEC Mode

The Mellanox Spectrum-2 (25G) switch only supports RS FEC.

## Related Information

- {{<exlink url="http://wiki.debian.org/NetworkConfiguration" text="Debian - Network Configuration">}}
- {{<exlink url="http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan" text="Linux Foundation - VLANs">}}
- {{<exlink url="http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding" text="Linux Foundation - Bonds">}}
