---
title: Monitoring Interfaces and Transceivers with ethtool
author: NVIDIA
weight: 1105
toc: 4
---

The `ethtool` command enables you to query or control the network driver and hardware settings and takes the device name, such as swp1, as an argument. When the device name is the only argument, `ethtool` prints the network device settings. See `man ethtool(8)` for details.

{{%notice tip%}}
NVIDIA recommends using the `l1-show` command to monitor Ethernet data; refer to {{<link url="Troubleshoot-Layer-1">}}.
{{%/notice%}}

## Monitor Interface Status

To check the status of an interface, run the `ethtool <interface>` command:

```
cumulus@switch:~$ ethtool swp1
Settings for swp1:
        Supported ports: [ FIBRE ]
        Supported link modes:   1000baseT/Full
                                10000baseT/Full
        Supported pause frame use: No
        Supports auto-negotiation: No
        Advertised link modes:  1000baseT/Full
        Advertised pause frame use: No
        Advertised auto-negotiation: No
        Speed: 10000Mb/s
        Duplex: Full
        Port: FIBRE
        PHYAD: 0
        Transceiver: external
        Auto-negotiation: off
        Current message level: 0x00000000 (0)

Link detected: yes
```

{{%notice note%}}
The switch hardware includes the {{<link url="Switch-Port-Attributes" text="active port settings">}}. The output of `ethtool <interface>` shows the port settings in the kernel. The `switchd` process keeps the hardware and kernel in sync for the important port settings (speed, auto-negotiation, and link detected). However, some fields in `ethtool`, such as Supported Link Modes and Advertised Link Modes, do not update based on the actual module in the port and might show incorrect or misleading results.
{{%/notice%}}

To query interface statistics, run the `ethtool -S <interface>` command:

```
cumulus@switch:~$ ethtool -S swp1
NIC statistics:
     rx_queue_0_packets: 5
     rx_queue_0_bytes: 300
     rx_queue_0_drops: 0
     rx_queue_0_xdp_packets: 0
     rx_queue_0_xdp_tx: 0
     rx_queue_0_xdp_redirects: 0
     rx_queue_0_xdp_drops: 0
     rx_queue_0_kicks: 1
     tx_queue_0_packets: 144957
     tx_queue_0_bytes: 10546468
     tx_queue_0_xdp_tx: 0
     tx_queue_0_xdp_tx_drops: 0
     tx_queue_0_kicks: 144950
```

## View and Clear Interface Counters

Interface counters provide information about an interface. You can view this information when you run `cl-netstat`, `ifconfig`, or `cat /proc/net/dev`. You can also run `sudo cl-netstat -c` to save or clear the interface counters.

```
cumulus@switch:~$ sudo cl-netstat
Kernel Interface table
Iface            MTU    RX_OK    RX_ERR    RX_DRP    RX_OVR    TX_OK    TX_ERR    TX_DRP    TX_OVR  Flg
-------------  -----  -------  --------  --------  --------  -------  --------  --------  --------  -----
lo             65536   185932         0         0         0   185932         0         0         0  LRU
eth0            1500   151883         0         0         0    13504         0         0         0  BMRU
swp1            9216        5         0         5         0   144986         0         0         0  BMsRU
swp2            9216        5         0         5         0   144988         0         0         0  BMsRU
swp3            9216        5         0         5         0   144944         0         0         0  BMsRU
swp49           9216   502662         0         5         0   502629         0         0         0  BMsRU
swp50           9216   507636         0         5         0   507666         0         0         0  BMsRU
swp51           9216   749122         0         5         0   794080         0         0         0  BMRU
swp52           9216   216057         0         5         0   212567         0         0         0  BMRU
bond1           9216        0         0         0         0   144942         0         0         0  BMmRU
bond2           9216        0         0         0         0   144944         0         0         0  BMmRU
bond3           9216        0         0         0         0   144944         0         0         0  BMmRU
br_default      9216     5072         0         0         0     5074         0         0         0  BMRU
mgmt           65575     3365         0         0         0        0         0       936         0  OmRU
peerlink        9216  1010288         0         0         0  1010295         0         0         0  BMmRU
peerlink.4094   9216   506672         0         0         0   506668         0         0         0  BMRU
vlan10          9216     1687         0         0         0     1687         0         0         0  BMRU
vlan10-v0       9216     1678         0         0         0     1677         0         0         0  BMRU
vlan20          9216     1688         0         0         0     1688         0         0         0  BMRU
vlan20-v0       9216     1678         0         0         0     1677         0         0         0  BMRU
vlan30          9216     1687         0         0         0     1689         0         0         0  BMRU
vlan30-v0       9216     1678         0         0         0     1678         0         0         0  BMRU
```

```
cumulus@switch:~$ sudo cl-netstat -c
Cleared counters
```

To see the `cl-netstat` command options, run the `cl-netstat -h` command.

{{%notice note%}}
Some services, such as {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#large-packet-drops-on-the-peer-link-interface" text="MLAG">}} and {{<link url="DHCP-Relays/#considerations" text="DHCP">}} can cause drop counters to increment as expected and do not cause a problem on the switch.
{{%/notice%}}

## Monitor Switch Port SFP and QSFP Hardware Information

To see hardware capabilities and measurement information on the SFP or QSFP module in a particular port, use the `ethtool -m` command. If the SFP or QSFP supports Digital Optical Monitoring (the `Optical diagnostics support` field is *Yes* in the output below), the optical power levels and thresholds also show below the standard hardware details.

In the sample output below, you can see that this module is a 1000BASE-SX short-range optical module, manufactured by JDSU, part number PLRXPL-VI-S24-22. The second half of the output displays the current readings of the `Tx` power levels (`Laser output power`) and Rx power (`Receiver signal average optical power`), temperature, voltage and alarm threshold settings.

```
cumulus@switch$ ethtool -m swp3
        Identifier                                : 0x03 (SFP)
        Extended identifier                       : 0x04 (GBIC/SFP defined by 2-wire interface ID)
        Connector                                 : 0x07 (LC)
        Transceiver codes                         : 0x00 0x00 0x00 0x01 0x20 0x40 0x0c 0x05
        Transceiver type                          : Ethernet: 1000BASE-SX
        Transceiver type                          : FC: intermediate distance (I)
        Transceiver type                          : FC: Shortwave laser w/o OFC (SN)
        Transceiver type                          : FC: Multimode, 62.5um (M6)
        Transceiver type                          : FC: Multimode, 50um (M5)
        Transceiver type                          : FC: 200 MBytes/sec
        Transceiver type                          : FC: 100 MBytes/sec
        Encoding                                  : 0x01 (8B/10B)
        BR, Nominal                               : 2100MBd
        Rate identifier                           : 0x00 (unspecified)
        Length (SMF,km)                           : 0km
        Length (SMF)                              : 0m
        Length (50um)                             : 300m
        Length (62.5um)                           : 150m
        Length (Copper)                           : 0m
        Length (OM3)                              : 0m
        Laser wavelength                          : 850nm
        Vendor name                               : JDSU
        Vendor OUI                                : 00:01:9c
        Vendor PN                                 : PLRXPL-VI-S24-22
        Vendor rev                                : 1
        Optical diagnostics support               : Yes
        Laser bias current                        : 21.348 mA
        Laser output power                        : 0.3186 mW / -4.97 dBm
        Receiver signal average optical power     : 0.3195 mW / -4.96 dBm
        Module temperature                        : 41.70 degrees C / 107.05 degrees F
        Module voltage                            : 3.2947 V
        Alarm/warning flags implemented           : Yes
        Laser bias current high alarm             : Off
        Laser bias current low alarm              : Off
        Laser bias current high warning           : Off
        Laser bias current low warning            : Off
        Laser output power high alarm             : Off
        Laser output power low alarm              : Off
        Laser output power high warning           : Off
        Laser output power low warning            : Off
        Module temperature high alarm             : Off
        Module temperature low alarm              : Off
        Module temperature high warning           : Off
        Module temperature low warning            : Off
        Module voltage high alarm                 : Off
        Module voltage low alarm                  : Off
        Module voltage high warning               : Off
        Module voltage low warning                : Off
        Laser rx power high alarm                 : Off
        Laser rx power low alarm                  : Off
        Laser rx power high warning               : Off
        Laser rx power low warning                : Off
        Laser bias current high alarm threshold   : 10.000 mA
        Laser bias current low alarm threshold    : 1.000 mA
        Laser bias current high warning threshold : 9.000 mA
         Laser bias current low warning threshold  : 2.000 mA
        Laser output power high alarm threshold   : 0.8000 mW / -0.97 dBm
        Laser output power low alarm threshold    : 0.1000 mW / -10.00 dBm
        Laser output power high warning threshold : 0.6000 mW / -2.22 dBm
        Laser output power low warning threshold  : 0.2000 mW / -6.99 dBm
        Module temperature high alarm threshold   : 90.00 degrees C / 194.00 degrees F
        Module temperature low alarm threshold    : -40.00 degrees C / -40.00 degrees F
        Module temperature high warning threshold : 85.00 degrees C / 185.00 degrees F
        Module temperature low warning threshold  : -40.00 degrees C / -40.00 degrees F
        Module voltage high alarm threshold       : 4.0000 V
        Module voltage low alarm threshold        : 0.0000 V
        Module voltage high warning threshold     : 3.6450 V
        Module voltage low warning threshold      : 2.9550 V
        Laser rx power high alarm threshold       : 1.6000 mW / 2.04 dBm
        Laser rx power low alarm threshold        : 0.0100 mW / -20.00 dBm
        Laser rx power high warning threshold     : 1.0000 mW / 0.00 dBm
        Laser rx power low warning threshold      : 0.0200 mW / -16.99 dBm
```
