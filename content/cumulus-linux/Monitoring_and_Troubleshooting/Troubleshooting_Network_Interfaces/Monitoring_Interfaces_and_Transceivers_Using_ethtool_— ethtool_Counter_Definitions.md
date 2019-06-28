---
title: "Monitoring Interfaces and Transceivers Using ethtool —\_ethtool Counter Definitions"
author: Cumulus Networks
weight: 459
aliases:
 - "/display/DOCS/Monitoring+Interfaces+and+Transceivers+Using+ethtool+—\_ethtool+Counter+Definitions"
 - /pages/viewpage.action?pageId=9018051
pageID: 9018051
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
The `ethtool` command enables you to query or control the network driver
and hardware settings. It takes the device name (like swp1) as an
argument. When the device name is the only argument to `ethtool`, it
prints the current settings of the network device. See `man ethtool(8)`
for details. Not all options are currently supported on switch port
interfaces.

## <span>Monitor Interface Status Using ethtool</span>

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

## <span>View and Clear Interface Counters</span>

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

## <span>Monitor Switch Port SFP/QSFP Hardware Information Using ethtool</span>

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

## <span>ethtool Counter Definitions</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Counter</p></th>
<th><p>Definition</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>HwIfInOctets</p></td>
<td><p>The total number of octets received on the interface, including framing characters.</p></td>
</tr>
<tr class="even">
<td><p>HwIfInUcastPkts</p></td>
<td><p>The number of packets delivered by this sub-layer to a higher (sub-)layer that were not addressed to a multicast or broadcast address at this sub-layer.</p></td>
</tr>
<tr class="odd">
<td><p>HwIfInBcastPkts</p></td>
<td><p>The number of packets delivered by this sub-layer to a higher (sub-)layer that were addressed to a broadcast address at this sub-layer.</p></td>
</tr>
<tr class="even">
<td><p>HwIfInMcastPkts</p></td>
<td><p>The number of packets delivered by this sub-layer to a higher (sub-)layer that were addressed to a multicast address at this sub-layer. For a MAC layer protocol, this includes both group and functional addresses.</p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutOctets</p></td>
<td><p>The total number of octets transmitted out of the interface, including framing characters.</p></td>
</tr>
<tr class="even">
<td><p>HwIfOutUcastPkts</p></td>
<td><p>The total number of packets that higher-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent.</p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutMcastPkts</p></td>
<td><p>The total number of packets that higher-level protocols requested to be transmitted, and which were addressed to a multicast address at this sub-layer, including those that were discarded or not sent. For a MAC layer protocol, this includes both group and functional addresses.</p></td>
</tr>
<tr class="even">
<td><p>HwIfOutBcastPkts</p></td>
<td><p>The total number of packets that higher-level protocols requested be transmitted, and which were addressed to a broadcast address at this sub-layer, including those that were discarded or not sent.</p></td>
</tr>
<tr class="odd">
<td><p>HwIfInDiscards</p></td>
<td><p>The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol. One possible reason for discarding such a packet could be to free up buffer space.</p>
<p>The sum of all Rx discards on an interface including all of the more specific itemized ethtool counters. It also accounts for all other drops that do not have a more specific ethtool drop reason when a frame arrives that doesn't result in a valid forwarding decision - STP discarding, IGMP snooping drop, VLAN tag not configured</p>
<p><strong>MLAG issue for RX_DRPs</strong></p>
<p><strong>(Also in bcmcmd counter <a href="https://wiki.cumulusnetworks.com/display/SD/Finding+packet+drops+in+a+Broadcom+chip#FindingpacketdropsinaBroadcomchip-DefaultDebugCounterSettings" class="external-link">RDBGC0</a><a href="https://wiki.cumulusnetworks.com/display/SD/Finding+packet+drops+in+a+Broadcom+chip#FindingpacketdropsinaBroadcomchip-DefaultDebugCounterSettings" class="external-link">)</a></strong></p></td>
</tr>
<tr class="even">
<td><p>HwIfInL3Drops</p></td>
<td><p>All layer 3 packets that were discarded.</p></td>
</tr>
<tr class="odd">
<td><p>HwIfInBufferDrops</p></td>
<td><p>All ingress buffer congestion discards.</p>
<p>These are ingress buffer drops that are commonly seen during bursty congestion. Broadcom platforms have a buffer pool that is shared across all interfaces rather than a per-interface queue. When the global buffer pool is congested, InBufferDrops will accrue.</p></td>
</tr>
<tr class="even">
<td><p>HwIfInAclDrops</p></td>
<td><p>All packets that were intentionally dropped.</p>
<p>These are common ACL drops for control plane policing or otherwise. <code>cl-acltool -L all</code> shows the current ACLs installed on the system.</p></td>
</tr>
<tr class="odd">
<td><p>HwIfInBlackholeDrops</p></td>
<td><p>All packets that were unintentionally dropped.</p></td>
</tr>
<tr class="even">
<td><p>HwIfInDot3LengthErrors</p></td>
<td><p>A count of frames received on a particular interface with a length field value that falls between the minimum unpadded LLC data size and the maximum allowed LLC data size inclusive and that does not match the number of LLC data octets received. The count represented by an instance of this object also includes frames for which the length field value is less than the minimum unpadded LLC data size.</p>
<p>This counter accrues when the value of the length field in a frame does not match the number of octets received in the frame or it has incorrect padding - we've also seen incorrect padding or length field concerns in some legacy proprietary protocols used by other vendors such as CGMP. These frames are still forwarded.</p></td>
</tr>
<tr class="odd">
<td><p>HwIfInDot3FrameErrors</p></td>
<td><p>A count of frames received on a particular interface that are an integral number of octets in length but do not pass the FCS check. The count represented by an instance of this object is incremented when the frameCheckError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions obtain are, according to the conventions of [9], counted exclusively according to the error status presented to the LLC.</p></td>
</tr>
<tr class="even">
<td><p>HwIfInErrors</p></td>
<td><p>For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol. For character-oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol.</p>
<p>This is the total of all “in” or Rx errors such as frame/FCS errors as outlined below</p></td>
</tr>
<tr class="odd">
<td><p>SoftInErrors</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>SoftInDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>SoftInFrameErrors</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfOutDiscards</p></td>
<td><p>The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a packet could be to free up buffer space.</p>
<p><strong>(Also in bcmcmd counter <a href="https://wiki.cumulusnetworks.com/display/SD/Finding+packet+drops+in+a+Broadcom+chip#FindingpacketdropsinaBroadcomchip-DefaultDebugCounterSettings" class="external-link">TDBGC3</a>)</strong></p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutErrors</p></td>
<td><p>For packet-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character-oriented or fixed-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.</p>
<p><strong>(Also in bcmcmd counter TERR)</strong></p></td>
</tr>
<tr class="even">
<td><p>HwIfOutQDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutNonQDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>SoftOutErrors</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>SoftOutDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>SoftOutTxFifoFull</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutQLen</p></td>
<td><p>The length of the output packet queue in packets.</p></td>
</tr>
<tr class="even">
<td><p>HwIfInPausePkt</p></td>
<td><p>A count of MAC control frames received on this interface with an opcode indicating the PAUSE operation.</p>
<p>This counter does not increment when the interface is operating in half-duplex mode.</p>
<p>For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate. Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the HwIfInPausePkt object for 10 Gb/s or faster interfaces.</p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutPausePkt</p></td>
<td><p>A count of MAC control frames transmitted on this interface with an opcode indicating the PAUSE operation.</p>
<p>This counter does not increment when the interface is operating in half-duplex mode.</p>
<p>For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate. Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the HwIfOutPausePkt object for 10 Gb/s or faster interfaces.</p></td>
</tr>
<tr class="even">
<td><p>HwIfInPfc0Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutPfc0Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfInPfc1Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutPfc1Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfInPfc2Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutPfc2Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfInPfc3Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutPfc3Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfInPfc4Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutPfc4Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfInPfc5Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutPfc5Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfInPfc6Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutPfc6Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfInPfc7Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutPfc7Pkt</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfOutWredDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutQ0WredDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfOutQ1WredDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutQ2WredDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfOutQ3WredDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutQ4WredDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfOutQ5WredDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutQ6WredDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfOutQ7WredDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>HwIfOutQ8WredDrops</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>HwIfOutQ9WredDrops</p></td>
<td><p> </p></td>
</tr>
</tbody>
</table>
