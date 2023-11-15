---
title: No Connectivity with Intel x710 NICs on Firmware 6.0.x
author: NVIDIA
weight: 334
toc: 4
---

## Issue

10G-SR interfaces flap when connected to Intel x710 NICs using firmware 6.0.x.

Multiple customers have encountered link connectivity issues when connecting to a server containing an Intel x710 NIC with firmware 6.0.0 or 6.0.1. Intel x710 NICs are common on Dell servers. You can see this issue on breakout ports as well.

In some cases, the affected interfaces display as "ge" interfaces in the hardware. For example, the Broadcom ASIC shows the link as 10G/GMII:

```
           ena/ speed/   link auto STP                 lrn inter max loop
port      link duplex    scan neg? state  pause discard ops face  frame back

 ge0(  1) down   10G FD SW   No Disable      None FA GMII 1518
 ge1(  2) down   10G FD SW   No Disable      None FA GMII 1518
```

In other cases, the link remains as no carrier and you can see it flapping. You can see this during a visual inspection of the Intel x710 NIC; the corresponding link status light flashes green.

## Environment

Firmware:

- Intel NIC x710 FW: 6.0.0 & 6.0.1

Hardware (ASIC):

- Broadcom Trident II
- Broadcom Trident II+
- Broadcom Tomahawk
- NVIDIA Spectrum

Hardware (server side transceiver):

- Intel AFBR.709DMZ-IN2

## Workaround

You can choose from two workarounds to avoid this issue:

- Downgrade the firmware on the Intel x710 NIC to 5.x.x.
- Using the Intel x710 6.0.x firmware, force the link speed and auto-negotiation settings on the server and on the switch.  
      
Apply following configuration to the 10G port on the switch:

    auto swpX
    iface swpX
       link-speed 10000

You can do this by executing the following NCLU commands:

    cumulus@switch:~$ net add interface swpX link speed 10000
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

You should apply the following command to the 10G ports on the server to force it to advertise 10000Mb/s:

    ethtool -s ethX advertise 0x80000000000

{{%notice note%}}

If neither workaround is effective, contact Cumulus Support or Dell Support.

{{%/notice%}}

## Resolution

Dell has released an updated firmware version (18.5.17) that fixes this issue. For more information, read Dell's [release notes](https://www.dell.com/support/home/us/en/04/drivers/driversdetails?driverid=t6vn9) for this version.
