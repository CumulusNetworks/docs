---
title: Monitoring Interfaces and Transceivers Using ethtool
author: NVIDIA
weight: 457
pageID: 8362604
---
The `ethtool` command enables you to query or control the network driver
and hardware settings. It takes the device name (like swp1) as an
argument. When the device name is the only argument to `ethtool`, it
prints the current settings of the network device. See `man ethtool(8)`
for details. Not all options are currently supported on switch port
interfaces.

## Monitor Interface Status Using ethtool

To check the status of an interface using `ethtool`:

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

{{%notice note%}}

The switch hardware contains the {{<link url="Switch-Port-Attributes" text="active port settings">}}.
The output of `ethtool swpXX` shows the port settings stored in the
kernel. The `switchd` process keeps the hardware and kernel in sync for
the important port settings (speed, auto-negotiation, and link detected)
when they change. However, many of the fields in `ethtool`, like
Supported Link Modes and Advertised Link Modes are not updated based on
the actual module inserted in the port and therefore are incorrect or
misleading.

{{%/notice%}}

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

## View and Clear Interface Counters

Interface counters contain information about an interface. You can view
this information when you run `cl-netstat`, `ifconfig`, or `cat
/proc/net/dev`. You can also use `cl-netstat` to save or clear this
information:

    cumulus@switch:~$ sudo cl-netstat
    Kernel Interface table
    Iface   MTU Met        RX_OK RX_ERR RX_DRP RX_OVR        TX_OK TX_ERR TX_DRP TX_OVR    Flg
    ---------------------------------------------------------------------------------------------
    eth0   1500   0          611      0      0      0          487      0      0      0   BMRU
    lo    16436   0            0      0      0      0            0      0      0      0    LRU
    swp1   1500   0            0      0      0      0            0      0      0      0    BMU
     
    cumulus@switch:~$ sudo cl-netstat -c
    Cleared counters

<table>
<thead>
<tr class="header">
<th><p>Option</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>-c</p></td>
<td><p>Copies and clears statistics. It does not clear counters in the kernel or hardware.</p>
<p>{{%notice note%}}</p>
<p>The <code>-c</code> argument is applied per user ID by default. You can override it by using the <code>-t</code> argument to save statistics to a different directory.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="even">
<td><p>-d</p></td>
<td><p>Deletes saved statistics, either the <code>uid</code> or the specified tag.</p>
<p>{{%notice note%}}</p>
<p>The <code>-d</code> argument is applied per user ID by default. You can override it by using the <code>-t</code> argument to save statistics to a different directory.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="odd">
<td><p>-D</p></td>
<td><p>Deletes all saved statistics.</p></td>
</tr>
<tr class="even">
<td><p>-l</p></td>
<td><p>Lists saved tags.</p></td>
</tr>
<tr class="odd">
<td><p>-r</p></td>
<td><p>Displays raw statistics (unmodified output of <code>cl-netstat</code>).</p></td>
</tr>
<tr class="even">
<td><p>-t &lt;tag name&gt;</p></td>
<td><p>Saves statistics with <code>&lt;tag name&gt;</code>.</p></td>
</tr>
<tr class="odd">
<td><p>-v</p></td>
<td><p>Prints <code>cl-netstat</code> version and exits.</p></td>
</tr>
</tbody>
</table>

{{%notice note%}}
On Mellanox switches, Cumulus Linux updates physical counters to the kernel every two seconds and virtual interfaces (such as VLAN interfaces) every ten seconds. You cannot change these values. Because the update process takes a lower priority than other `switchd` processes, the interval might be longer when the system is under a heavy load.
{{%/notice%}}

## Monitor Switch Port SFP/QSFP Hardware Information Using ethtool

To see hardware capabilities and measurement information on the SFP or
QSFP module installed in a particular port, use the `ethtool -m`
command. If the SFP/QSFP supports Digital Optical Monitoring (that is,
the `Optical diagnostics support` field in the output below is set to
*Yes*), the optical power levels and thresholds are also printed below
the standard hardware details.

In the sample output below, you can see that this module is a
1000BASE-SX short-range optical module, manufactured by JDSU, part
number PLRXPL-VI-S24-22. The second half of the output displays the
current readings of the Tx power levels (`Laser output power`) and Rx
power (`Receiver signal average optical power`), temperature, voltage
and alarm threshold settings.

    cumulus@switch$ sudo ethtool -m swp3
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
