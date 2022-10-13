---
title: Storm Control
author: NVIDIA
weight: 470
toc: 3
---
Storm control provides protection against excessive inbound BUM (broadcast, unknown unicast, multicast) traffic on layer 2 switch port interfaces, which can cause poor network performance.

{{%notice note%}}

- Storm control is *not* supported on a switch with the Tomahawk2 ASIC.
- On Broadcom switches, ARP requests over layer 2 VXLAN bypass broadcast storm control; they are forwarded to the CPU and subjected to embedded control plane QoS instead.

{{%/notice%}}

## Configure Storm Control

To configure storm control for physical ports, edit the `/etc/cumulus/switchd.conf` file. For example, to enable broadcast storm control for swp1 at 400 packets per second (pps), multicast storm control at 3000 pps, and unknown unicast at 500 pps, edit the `/etc/cumulus/switchd.conf` file and uncomment the `storm_control.broadcast`, `storm_control.multicast`, and `storm_control.unknown_unicast` lines:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
# Storm Control setting on a port, in pps, 0 means disable
interface.swp1.storm_control.broadcast = 400
interface.swp1.storm_control.multicast = 3000
interface.swp1.storm_control.unknown_unicast = 500
...
```

When you update the `/etc/cumulus/switchd.conf` file, you must restart `switchd` for the changes to take effect.

{{<cl/restart-switchd>}}

Alternatively, you can run the following commands. The configuration below takes effect immediately, but does not persist if you reboot the switch. For a persistent configuration, edit the `/etc/cumulus/switchd.conf` file, as described above.

```
cumulus@switch:~$ sudo sh -c 'echo 400 > /cumulus/switchd/config/interface/swp1/storm_control/broadcast'
cumulus@switch:~$ sudo sh -c 'echo 3000 > /cumulus/switchd/config/interface/swp1/storm_control/multicast'
cumulus@switch:~$ sudo sh -c 'echo 500 > /cumulus/switchd/config/interface/swp1/storm_control/unknown_unicast'
```

To use the same command above on range of interfaces you can use a for-loop from the switch CLI using the below example.

```
cumulus@switch:mgmt:~$ for i in {1..5}; do
> sudo sh -c "echo 400 > /cumulus/switchd/config/interface/swp$i/storm_control/broadcast"
> sudo sh -c "echo 3000 > /cumulus/switchd/config/interface/swp$i/storm_control/multicast"
> sudo sh -c "echo 500 > /cumulus/switchd/config/interface/swp$i/storm_control/unknown_unicast"
> done
cumulus@switch:mgmt:~$ 
```