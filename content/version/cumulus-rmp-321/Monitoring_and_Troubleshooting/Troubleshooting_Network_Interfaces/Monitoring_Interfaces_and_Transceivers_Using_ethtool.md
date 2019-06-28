---
title: Monitoring Interfaces and Transceivers Using ethtool
author: Cumulus Networks
weight: 197
aliases:
 - /display/RMP321/Monitoring+Interfaces+and+Transceivers+Using+ethtool
 - /pages/viewpage.action?pageId=5127571
pageID: 5127571
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
The `ethtool` command enables you to query or control the network driver
and hardware settings. It takes the device name (like swp1) as an
argument. When the device name is the only argument to `ethtool`, it
prints the current settings of the network device. See `man ethtool(8)`
for details. Not all options are currently supported on switch port
interfaces.

## <span>Monitoring Interfaces Using ethtool</span>

To check the status of an interface using `ethtool`:

    cumulus@switch:~$ ethtool swp1
    Settings for swp1:
        Supported ports: [ TP ]
        Supported link modes:   10baseT/Half 10baseT/Full 
                                100baseT/Half 100baseT/Full 
                                1000baseT/Full 
        Supported pause frame use: Symmetric Receive-only
        Supports auto-negotiation: Yes
        Advertised link modes:  10baseT/Half 10baseT/Full 
                                100baseT/Half 100baseT/Full 
                                1000baseT/Half 1000baseT/Full 
        Advertised pause frame use: Symmetric
        Advertised auto-negotiation: No
        Speed: 1000Mb/s
        Duplex: Full
        Port: FIBRE
        PHYAD: 0
        Transceiver: external
        Auto-negotiation: on
        Current message level: 0x00000000 (0)
                       
        Link detected: yes

To query interface statistics:

    cumulus@switch:~$ sudo ethtool -S swp1
    NIC statistics:
            HwIfInOctets: 1435339
            HwIfInUcastPkts: 11795
            HwIfInBcastPkts: 3
            HwIfInMcastPkts: 4578
            HwIfOutOctets: 14866246
            HwIfOutUcastPkts: 11791
            HwIfOutMcastPkts: 136493
            HwIfOutBcastPkts: 0
            HwIfInDiscards: 0
            HwIfInL3Drops: 0
            HwIfInBufferDrops: 0
            HwIfInAclDrops: 28
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

### <span>Viewing and Clearing Interface Counters</span>

Interface counters contain information about an interface. You can view
this information when you run `cl-netstat`, `ifconfig`, or `cat
/proc/net/dev`. You can also use `cl-netstat` to save or clear this
information:

    cumulus@switch:~$ sudo cl-netstat
    Kernel Interface table
    Iface      MTU    Met    RX_OK    RX_ERR    RX_DRP    RX_OVR    TX_OK    TX_ERR    TX_DRP    TX_OVR  Flg
    -------  -----  -----  -------  --------  --------  --------  -------  --------  --------  --------  -----
    eth0      1500      0     8391         0         0         0     9694         0         0         0  BMRU
    lo       16436      0     1693         0         0         0     1693         0         0         0  LRU
    swp1      1500      0    11914         0      8948         0    20854         0      9338         0  BMRU
    swp2      1500      0    20734         0     17969         0    12033         0     13142         0  BMRU
     
    cumulus@switch:~$ sudo cl-netstat -c
    Cleared counters

| Option           | Description                                                                         |
| ---------------- | ----------------------------------------------------------------------------------- |
| \-c              | Copies and clears statistics. It does not clear counters in the kernel or hardware. |
| \-d              | Deletes saved statistics, either the `uid` or the specified tag.                    |
| \-D              | Deletes all saved statistics.                                                       |
| \-j              | Display in JSON format.                                                             |
| \-l              | Lists saved tags.                                                                   |
| \-r              | Displays raw statistics (unmodified output of `cl-netstat`).                        |
| \-t \<tag name\> | Saves statistics with `<tag name>`.                                                 |
| \-v              | Prints `cl-netstat` version and exits.                                              |

## <span>Monitoring Switch Port SFP/QSFP Using ethtool</span>

To see hardware capabilities and measurement information on SFP or the
QSFP module installed in a particular port, use the ` ethtool -m
 `command. If the SFP/QSFP supports Digital Optical Monitoring (that is,
the `Optical diagnostics support` field in the output below is set to
*Yes*), the optical power levels and thresholds are also printed below
the standard hardware details.

In the sample output below, you can see that this module is a
1000BASE-SX short-range optical module, manufactured by JDSU, part
number PLRXPL-VI-S24-22. The second half of the output displays the
current readings of the Tx power levels (`Laser output power`) and Rx
power (`Receiver signal average optical power`), temperature, voltage
and alarm threshold settings.

    cumulus@switch:~$ sudo ethtool -m swp49
        Identifier                                : 0xff (reserved or unknown)
        Optical diagnostics support               : Yes
        Laser bias current                        : 130.046 mA
        Laser output power                        : 6.5025 mW / 8.13 dBm
        Receiver signal average optical power     : 6.5535 mW / 8.16 dBm
        Module temperature                        : 0.00 degrees C / 32.00 degrees F
        Module voltage                            : 6.5282 V
        Alarm/warning flags implemented           : Yes
        Laser bias current high alarm             : On
        Laser bias current low alarm              : On
        Laser bias current high warning           : On
        Laser bias current low warning            : On
        Laser output power high alarm             : On
        Laser output power low alarm              : On
        Laser output power high warning           : On
        Laser output power low warning            : On
        Module temperature high alarm             : On
        Module temperature low alarm              : On
        Module temperature high warning           : On
        Module temperature low warning            : On
        Module voltage high alarm                 : On
        Module voltage low alarm                  : On
        Module voltage high warning               : On
        Module voltage low warning                : On
        Laser rx power high alarm                 : On
        Laser rx power low alarm                  : On
        Laser rx power high warning               : On
        Laser rx power low warning                : On
        Laser bias current high alarm threshold   : 130.046 mA
        Laser bias current low alarm threshold    : 130.046 mA
        Laser bias current high warning threshold : 130.046 mA
        Laser bias current low warning threshold  : 130.046 mA
        Laser output power high alarm threshold   : 6.5025 mW / 8.13 dBm
        Laser output power low alarm threshold    : 6.5025 mW / 8.13 dBm
        Laser output power high warning threshold : 6.5025 mW / 8.13 dBm
        Laser output power low warning threshold  : 6.5025 mW / 8.13 dBm
        Module temperature high alarm threshold   : -1.00 degrees C / 30.20 degrees F
        Module temperature low alarm threshold    : 0.00 degrees C / 32.00 degrees F
        Module temperature high warning threshold : 0.00 degrees C / 32.00 degrees F
        Module temperature low warning threshold  : 0.00 degrees C / 32.00 degrees F
        Module voltage high alarm threshold       : 6.5282 V
        Module voltage low alarm threshold        : 6.5282 V
        Module voltage high warning threshold     : 6.5282 V
        Module voltage low warning threshold      : 6.5282 V
        Laser rx power high alarm threshold       : 6.5535 mW / 8.16 dBm
        Laser rx power low alarm threshold        : 6.5535 mW / 8.16 dBm
        Laser rx power high warning threshold     : 6.5535 mW / 8.16 dBm
        Laser rx power low warning threshold      : 6.5535 mW / 8.16 dBm
