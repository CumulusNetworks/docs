---
title: RX Error Counters and Slow Throughput Performance
author: NVIDIA
weight: 377
toc: 4
---

## Issue

There might be slow throughput performance in a switch and RX error counters are incrementing, as well as possibly TX error counters. You might see these error counters in the output of different commands:

- `cl-netstat`
- `ip -s link show`
- `ethtool -S`

If you want to monitor the output of these commands to see the statistics live as they change, use the Linux `watch` command. For more information on using this command, refer to the following {{<link url="Using-the-watch-Command" text="article">}}.
<!-- vale off -->
### cl-netstat Shows RX\_ERR
<!-- vale on -->
You can see RX error counters in the output of `cl-netstat` as `RX_ERR`, as shown below.

    cumulus@switch$ cl-netstat
    Kernel Interface table
    Iface   MTU Met         RX_OK RX_ERR RX_DRP RX_OVR        TX_OK TX_ERR TX_DRP TX_OVR    Flg
    ---------------------------------------------------------------------------------------------
    eth0      1500 0      7361728      0      0 0           2030188      0      0      0 BMRU
    lo       16436 0          173      0      0 0               173      0      0      0 LRU
    swp1      9000 0   7669976333 15682741   1439 0      3035723493      0      0      0 BMRU
    swp2      9000 0   3023667770 10728822    978 0      9840616134      0      0      0 BMRU
    swp3      9000 0  24315580462 14877988   1307 0     80763548753      0      0      0 BMRU
    swp4      9000 0  13869960451 8452232    897 0       7477191326      0      0      0 BMRU
<!-- vale off -->
*\<Output is truncated\>*
<!-- vale on -->
For additional information on how to use the `cl-netstat` command, read [the user guide]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Troubleshooting-Network-Interfaces/Monitoring-Interfaces-and-Transceivers-Using-ethtool" >}}).

### ip -s link show Shows RX errors

You can see RX error counters in the output of `ip -s link show`, as shown below.

    cumulus@switch$ ip -s link show swp5
    7: swp5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc pfifo_fast state UP mode DEFAULT qlen 500 
        link/ether 08:9e:01:ce:e0:6c brd ff:ff:ff:ff:ff:ff
        RX: bytes  packets  errors  dropped overrun mcast   
        8552309    71000    1899    1       0       63108  
        TX: bytes  packets  errors  dropped carrier collsns 
        1940799    15779    0       0       0       0 

### ethtool -S Shows HwIfInErrors

You can see RX error counters in the output of `ethtool -S <interface>` as `HwIfInErrors`, as shown below.

    cumulus@switch$ ethtool -S swp1
    NIC statistics:
         HwIfInOctets: 51883086875273
         HwIfInUcastPkts: 7669711571
         HwIfInBcastPkts: 0
         HwIfInMcastPkts: 264791
         HwIfOutOctets: 10590370555531
         HwIfOutUcastPkts: 3035458717
         HwIfOutMcastPkts: 264792
         HwIfOutBcastPkts: 0
         HwIfInDiscards: 1439
         HwIfInL3Drops: 0
         HwIfInBufferDrops: 1439
         HwIfInAclDrops: 115
         HwIfInDot3LengthErrors: 0
         HwIfInErrors: 15682741
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

## Environment

- Cumulus Linux, all versions

## Overview

### Cause of the Errors

These RX\_ERR or HwIfInErrors indicate some Ethernet data frames became corrupted somewhere along the transmission line, typically due to some bad cable or transceiver. The cyclic redundancy check (CRC) algorithm in the Frame Check Sequences (FCS) calculation might detect these errors.

When the switch receives a frame, it runs its own checksum on the frame and compares the resulting CRC value to the value in the Ethernet frame. If they are not equal, it means some bits got corrupted and thus the switch counts these as RX errors. In half-duplex mode, some FCS errors might be normal. In full-duplex mode, FCS errors are not normal.

### Propagation of the Errors

When a platform detects an FCS error, what the platform does with the Ethernet frame depends on which switching mode you configured, one of either cut-through or store and forward. In cut-through mode, the frame with the FCS error might propagate to the next switch. In store and forward mode, the frame with the FCS error gets discarded.
<!-- vale off -->
#### Cut-through Switching Mode
<!-- vale on -->
You use the cut-through mode of forwarding to minimize the latency (delay) through the switch by beginning the forwarding process before receiving the entire packet from the upstream sender. The data might begin transmitting while the inbound interface is still receiving it, which minimizes the time the switch holds the packet, and thus minimizes delays in propagation. The disadvantage is that data frames with FCS errors might propagate to the next hop because transmission out of the switch begins before detecting the FCS error. Becaus the next hop switch would have begun receiving this packet with no indication of a problem with the packet, it might also begin transmitting to its outbound interface before detecting the FCS error, thereby propagating the error even further.

#### Store and Forward Switching Mode

As the name implies, store and forward waits until the switch receives and validates the entire packet before starting the transmit process on the outbound interface. This allows the switch to verify that the received packet is valid before sending it onward, but it increases latency by holding each packet longer in buffers in the switch. It might also increase buffer utilization by having each packet utilize the resources for a longer period of time.  If you configure store and forward, the platform is able to detect FCS errors before beginning transmission, and thus can discard the frame and not propagate the errors to the next hop.

## Resolution

### Replace the Bad Components

The frame corruption occurs because of some bad component somewhere in the data path, such as cables or transceivers. Trace the RX errors upstream across all the hops in the end-to-end data path

You can use `lldpctl` to trace the ports upstream, hop-by-hop. Here is an example output:

    cumulus@switch$ lldpctl 
    -------------------------------------------------------------------------------
    LLDP neighbors:
    -------------------------------------------------------------------------------
    Interface:    eth0, via: LLDP, RID: 1, Time: 0 day, 23:36:08
      Chassis:     
        ChassisID:    mac 6c:64:1a:00:2f:54
        SysName:      backbone
        SysDescr:     Cumulus Linux version 2.5.2 running on cel kennisis
        MgmtIP:       192.168.1.5
        Capability:   Bridge, on
        Capability:   Router, on
      Port:        
        PortID:       ifname swp21
        PortDescr:    swp21
    -------------------------------------------------------------------------------
    Interface:    swp1, via: LLDP, RID: 5, Time: 0 day, 05:51:40
      Chassis:     
        ChassisID:    mac 08:9e:01:ce:e4:0c
        SysName:      sw23
        SysDescr:     Cumulus Linux version 2.5.2 running on quanta ly2
        MgmtIP:       192.168.2.30
        Capability:   Bridge, off
        Capability:   Router, on
      Port:        
        PortID:       ifname swp7
        PortDescr:    swp7
    -------------------------------------------------------------------------------

After you identify the source point, try replacing the cable or transceiver to resolve the component introducing the data corruption.

### Change the Switching Mode

While cut-through forwarding decreases latency and buffer consumption, one of its disadvantages is that packets are not verified as valid before they begin transmission on the outbound interface. Thus forwarding might begin out of the output interface before detecting the FCS error.

By changing from cut-through to store and forward mode of forwarding operation, Cumulus Linux verifies each packet as correct before the forwarding process begins, limiting the reach of any corrupt packets.  This verification comes at the cost of potential increased latency and buffer consumption.

You need to configure these switches in the data path:

- The switches upstream from the switch with the RX errors (that is, the *previous* switches in the data path) to eliminate the RX errors on the switch in question
- The switch showing the RX errors to prevent it from propagating the errors to the downstream switch (that is, the *next* switch in the data path)

To change the forwarding behavior from cut-through to store and forward on switches with Broadcom ASICs:

1.  Run the following command:

        cumulus@switch$ sudo vi /etc/cumulus/datapath/traffic.conf

2.  Search for the following line in the `traffic.conf` file:

        # To enable cut-through forwarding
        cut_through_enable = true

3.  Modify the value of `cut_through_enable` to *false*:

        # To enable cut-through forwarding
        cut_through_enable = false

4.  To let the change in forwarding mode take effect, restart `switchd`.
    Note that restarting the `switchd` daemon is minimally disruptive.

        cumulus@switch$ sudo service switchd restart

## Considerations

While these instructions discuss how to change the mode of operation for forwarding on a Cumulus Linux switch, the default setting of cut-though is the recommended value in almost every circumstance.  If you make this change on a switch for testing purposes, you should continue to monitor its performance.
