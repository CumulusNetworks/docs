---
title: Power over Ethernet - PoE
author: Cumulus Networks
weight: 77
aliases:
 - /display/DOCS/Power+over+Ethernet+++PoE
 - /display/DOCS/Power+over+Ethernet+-+PoE
 - /display/DOCS/Power+over+Ethernet+PoE
 - /pages/viewpage.action?pageId=8366297
product: Cumulus Linux
version: '4.0'
---
Cumulus Linux supports Power over Ethernet (PoE) and PoE+, so certain
Cumulus Linux switches can supply power from Ethernet switch ports to
enabled devices over the Ethernet cables that connect them. PoE is
capable of powering devices up to 15W, while PoE+ can power devices up to 30W.
Configuration for power negotiation is done over
[LLDP](../../Layer-2/Link-Layer-Discovery-Protocol/).

The [currently supported platforms](https://cumulusnetworks.com/products/hardware-compatibility-list/?platform_type%5B0%5D=POE) include:

- Cumulus Express CX-1048-P
- Dell N3048EP-ON
- Delta AG6248C PoE
- EdgeCore AS4610-54P

## PoE Basics

PoE functionality is provided by the `cumulus-poe` package. When a powered device is connected to the switch via an Ethernet cable:

- If the available power is greater than the power required by the connected device, power is supplied to the switch port, and the device powers on
- If available power is less than the power required by the connected device and the switch port's priority is less than the port priority set on all powered ports, power is **not** supplied to the port
- If available power is less than the power required by the connected device and the switch port's priority is greater than the priority of a currently powered port, power is removed from lower priority port(s) and power is supplied to the port
- If the total consumed power exceeds the configured power limit of the power source, low priority ports are turned off. In the case of a tie, the port with the lower port number gets priority

Power is available as follows:

| PSU 1 | PSU 2 | PoE Power Budget |
| ----- | ----- | ---------------- |
| 920W  | x     | 750W             |
| x     | 920W  | 750W             |
| 920W  | 920W  | 1650W            |

The AS4610-54P has an LED on the front panel to indicate PoE status:

- Green: The `poed` daemon is running and no errors are detected
- Yellow: One or more errors are detected or the `poed` daemon is not running

{{%notice note%}}

Link state and PoE state are completely independent of each other. When a link is brought down on a particular port using `ip link <port> down`, power on that port is not turned off; however, LLDP negotiation is not possible.

{{%/notice%}}

## Configure PoE

You use the `poectl` command utility to configure PoE on a [switch that supports](https://cumulusnetworks.com/products/hardware-compatibility-list/?platform_type%5B0%5D=POE) the feature. You can:

- Enable or disable PoE for a given switch port
- Set a switch port's PoE priority to one of three values: *low*, *high* or *critical*

The PoE configuration resides in `/etc/cumulus/poe.conf`. The file lists all the switch ports, whether PoE is enabled for those ports and the priority for each port.

<details>
<summary>Sample poe.conf file ... </summary>

```
[enable]
swp1 = enable
swp2 = enable
swp3 = enable
swp4 = enable
swp5 = enable
swp6 = enable
swp7 = enable
swp8 = enable
swp9 = enable
swp10 = enable
swp11 = enable
swp12 = enable
swp13 = enable
swp14 = enable
swp15 = enable
swp16 = enable
swp17 = enable
swp18 = enable
swp19 = enable
swp20 = enable
swp21 = enable
swp22 = enable
swp23 = enable
swp24 = enable
swp25 = enable
swp26 = enable
swp27 = enable
swp28 = enable
swp29 = enable
swp30 = enable
swp31 = enable
swp32 = enable
swp33 = enable
swp34 = enable
swp35 = enable
swp36 = enable
swp37 = enable
swp38 = enable
swp39 = enable
swp40 = enable
swp41 = enable
swp42 = enable
swp43 = enable
swp44 = enable
swp45 = enable
swp46 = enable
swp47 = enable
swp48 = enable

[priority]
swp1 = low
swp2 = low
swp3 = low
swp4 = low
swp5 = low
swp6 = low
swp7 = low
swp8 = low
swp9 = low
swp10 = low
swp11 = low
swp12 = low
swp13 = low
swp14 = low
swp15 = low
swp16 = low
swp17 = low
swp18 = low
swp19 = low
swp20 = low
swp21 = low
swp22 = low
swp23 = low
swp24 = low
swp25 = low
swp26 = low
swp27 = low
swp28 = low
swp29 = low
swp30 = low
swp31 = low
swp32 = low
swp33 = low
swp34 = low
swp35 = low
swp36 = low
swp37 = low
swp38 = low
swp39 = low
swp40 = low
swp41 = low
swp42 = low
swp43 = low
swp44 = low
swp45 = low
swp46 = low
swp47 = low
swp48 = low
```

</details>

By default, PoE and PoE+ are enabled on all Ethernet/1G switch ports, and these ports are set with a low priority. Switch ports can have low, high or critical priority.

There is no additional configuration for PoE+.

To change the priority for one or more switch ports, run `poectl -p swp# [low|high|critical]`. For example:

```
cumulus@switch:~$ sudo poectl -p swp1-swp5,swp7 high
```

To disable PoE for one or more ports, run `poectl -d [port_numbers]`:

```
cumulus@switch:~$ sudo poectl -d swp1-swp5,swp7
```

To display PoE information for a set of switch ports, run `poectl -i [port_numbers]`:

```
cumulus@switch:~$ sudo poectl -i swp10-swp13
Port          Status            Allocated    Priority  PD type      PD class   Voltage   Current    Power
-----   --------------------   -----------   -------- -----------   --------   -------   -------   ---------
swp10   connected              negotiating   low      IEEE802.3at   4          53.5 V     25 mA    3.9 W
swp11   searching              n/a           low      IEEE802.3at   none        0.0 V      0 mA    0.0 W
swp12   connected              n/a           low      IEEE802.3at   2          53.5 V     25 mA    1.4 W
swp13   connected              51.0 W        low      IEEE802.3at   4          53.6 V     72 mA    3.8 W
```

The **Status** can be one of the following:

- **searching:** PoE is enabled but no device has been detected.
- **disabled:** The PoE port has been configured as disabled.
- **connected:** A powered device is connected and receiving power.
- **power-denied:** There is insufficient PoE power available to enable the connected device.

The **Allocated** column displays how much PoE power has been allocated to the port, which can be one of the following:

- **n/a:** No device is connected or the connected device does not support LLDP negotiation.
- **negotiating:** An LLDP-capable device is connected and is negotiating for PoE power.
- **XX.X W:** An LLDP-capable device has negotiated for XX.X watts of power (for example, 51.0 watts for swp13 above).

To see all the PoE information for a switch, run `poectl -s`:

```
cumulus@switch:~$ poectl -s
System power:
  Total:      730.0 W
  Used:        11.0 W
  Available:  719.0 W
Connected ports:
  swp11, swp24, swp27, swp48
```

The set commands (priority, enable, disable) either succeed silently or display an error message if the command fails.

The `poectl` command takes the following arguments:

|Argument <img width=200/>|Description<img width=500/>|
|-----------------|--------|
|`-h`, `--help`|Show this help message and exit|
|`-i`, `--port-info`<br>`<port-list>`|Returns detailed information for the specified ports. You can specify a range of ports. For example: `-i swp1-swp5,swp10`.<br>**Note**: On an Edge-Core AS4610-54P switch, the voltage reported by the poectl -i command and measured through a power meter connected to the device varies by 5V. The current and power readings are correct and no difference is seen for them.|
|`-a`, `--all`|Returns PoE status and detailed information for all ports.|
|`-p`, `--priority`<br>`<port-list> <priority>`|Sets priority for the specified ports: low, high, critical.|
|`-d`, `--disable-ports <port-list>`|Disables PoE operation on the specified ports.|
|`-e`, `--enable-ports <port-list>`|Enables PoE operation on the specified ports.|
|`-s`, `--system`|Returns PoE status for the entire switch.|
|`-r`, `--reset <port-list>`|Performs a hardware reset on the specified ports. Use this if one or more ports are stuck in an error state. This does not reset any configuration settings for the specified ports.|
|`-v`, `--version`|Displays version information.|
|`-j`, `--json`|Displays output in JSON format.|
|`--save`|Saves the current configuration. The saved configuration is automatically loaded on system boot.|
|`--load`|Loads and applies the saved configuration.|

## Troubleshooting

You can troubleshoot PoE and PoE+ using the following utilities and files:

- `poectl -s`, as described above.
- The Cumulus Linux `cl-support` script, which includes PoE-related output from `poed.conf`, `syslog`, `poectl --diag-info` and `lldpctl`.
- `lldpcli show neighbors ports <swp> protocol lldp hidden details`
- `tcpdump -v -v -i <swp> ether proto 0x88cc`
- The contents of the PoE/PoE+ `/etc/lldpd.d/poed.conf` configuration file, as described above.

### Verify the Link Is Up

LLDP requires network connectivity, so verify that the link is up.

```
cumulus@switch:~$ net show interface swp20
    Name    MAC                Speed      MTU  Mode
--  ------  -----------------  -------  -----  ---------
UP  swp20   44:38:39:00:00:04  1G        1500  Access/L2
```

### View LLDP Information Using lldpcli

You can run `lldpcli` to view the LLDP information that has been received on a switch port. For example:

```
cumulus@switch:~$ sudo lldpcli show neighbors ports swp20 protocol lldp hidden details
-------------------------------------------------------------------------------
LLDP neighbors:
-------------------------------------------------------------------------------
Interface:    swp20, via: LLDP, RID: 2, Time: 0 day, 00:03:34
  Chassis:
    ChassisID:    mac 68:c9:0b:25:54:7c
    SysName:      ihm-ubuntu
    SysDescr:     Ubuntu 14.04.2 LTS Linux 3.14.4+ #1 SMP Thu Jun 26 00:54:44 UTC 2014 armv7l
    MgmtIP:       fe80::6ac9:bff:fe25:547c
    Capability:   Bridge, off
    Capability:   Router, off
    Capability:   Wlan, off
    Capability:   Station, on
  Port:
    PortID:       mac 68:c9:0b:25:54:7c
    PortDescr:    eth0
    PMD autoneg:  supported: yes, enabled: yes
      Adv:          10Base-T, HD: yes, FD: yes
      Adv:          100Base-TX, HD: yes, FD: yes
      MAU oper type: 100BaseTXFD - 2 pair category 5 UTP, full duplex mode
    MDI Power:    supported: yes, enabled: yes, pair control: no
      Device type:  PD
      Power pairs:  spare
      Class:        class 4
      Power type:   2
      Power Source: Primary power source
      Power Priority: low
      PD requested power Value: 51000
      PSE allocated power Value: 51000
  UnknownTLVs: 
    TLV:          OUI: 00,01,42, SubType: 1, Len: 1 05
    TLV:          OUI: 00,01,42, SubType: 1, Len: 1 0D
-------------------------------------------------------------------------------
```

### View LLDP Information Using tcpdump

You can use `tcpdump` to view the LLDP frames being transmitted and received. For example:

```
cumulus@switch:~$ sudo tcpdump -v -v -i swp20 ether proto 0x88cc
tcpdump: listening on swp20, link-type EN10MB (Ethernet), capture size 262144 bytes
18:41:47.559022 LLDP, length 211
    Chassis ID TLV (1), length 7
      Subtype MAC address (4): 00:30:ab:f2:d7:a5 (oui Unknown)
      0x0000:  0400 30ab f2d7 a5
    Port ID TLV (2), length 6
      Subtype Interface Name (5): swp20
      0x0000:  0573 7770 3230
    Time to Live TLV (3), length 2: TTL 120s
      0x0000:  0078
    System Name TLV (5), length 13: dni-3048up-09
      0x0000:  646e 692d 3330 3438 7570 2d30 39
    System Description TLV (6), length 68
      Cumulus Linux version 3.0.1~1466303042.2265c10 running on dni 3048up
      0x0000:  4375 6d75 6c75 7320 4c69 6e75 7820 7665
      0x0010:  7273 696f 6e20 332e 302e 317e 3134 3636
      0x0020:  3330 3330 3432 2e32 3236 3563 3130 2072
      0x0030:  756e 6e69 6e67 206f 6e20 646e 6920 3330
      0x0040:  3438 7570
    System Capabilities TLV (7), length 4
      System  Capabilities [Bridge, Router] (0x0014)
      Enabled Capabilities [Router] (0x0010)
      0x0000:  0014 0010
    Management Address TLV (8), length 12
      Management Address length 5, AFI IPv4 (1): 10.0.3.190
      Interface Index Interface Numbering (2): 2
      0x0000:  0501 0a00 03be 0200 0000 0200
    Management Address TLV (8), length 24
      Management Address length 17, AFI IPv6 (2): fe80::230:abff:fef2:d7a5
      Interface Index Interface Numbering (2): 2
      0x0000:  1102 fe80 0000 0000 0000 0230 abff fef2
      0x0010:  d7a5 0200 0000 0200
    Port Description TLV (4), length 5: swp20
      0x0000:  7377 7032 30
    Organization specific TLV (127), length 9: OUI IEEE 802.3 Private (0x00120f)
      Link aggregation Subtype (3)
        aggregation status [supported], aggregation port ID 0
      0x0000:  0012 0f03 0100 0000 00
    Organization specific TLV (127), length 9: OUI IEEE 802.3 Private (0x00120f)
      MAC/PHY configuration/status Subtype (1)
        autonegotiation [supported, enabled] (0x03)
        PMD autoneg capability [10BASE-T fdx, 100BASE-TX fdx, 1000BASE-T fdx] (0x2401)
        MAU type 100BASEFX fdx (0x0012)
      0x0000:  0012 0f01 0324 0100 12
    Organization specific TLV (127), length 12: OUI IEEE 802.3 Private (0x00120f)
      Power via MDI Subtype (2)
        MDI power support [PSE, supported, enabled], power pair spare, power class class4
      0x0000:  0012 0f02 0702 0513 01fe 01fe
    Organization specific TLV (127), length 5: OUI Unknown (0x000142)
      0x0000:  0001 4201 0d
    Organization specific TLV (127), length 5: OUI Unknown (0x000142)
      0x0000:  0001 4201 01
    End TLV (0), length 0
```

### Log poed Events in syslog

The `poed` service logs the following events to `syslog` when:

- A switch provides power to a powered device.
- A device that was receiving power is removed.
- The power available to the switch changes.
- Errors are detected.
