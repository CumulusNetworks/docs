---
title: Storm Control
author: Cumulus Networks
weight: 385
toc: 3
---
Storm control provides protection against excessive inbound BUM (broadcast, unknown unicast, multicast) traffic on layer 2 switch port interfaces, which can cause poor network performance.

## Configure Storm Control

You configure storm control for each physical port by editing the `/etc/cumulus/switchd.conf` file.

For example, to enable broadcast storm control at 400 packets per second (pps) and multicast storm control at 3000 pps for swp1, edit the `/etc/cumulus/switchd.conf` file and uncomment the `storm_control.broadcast` and `storm_control.multicast` lines:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
# Storm Control setting on a port, in pps, 0 means disable
interface.swp1.storm_control.broadcast = 400
interface.swp1.storm_control.multicast = 3000
...
```

Alternatively, you can run the following commands. This configuration below takes effect immediately, but does not persist if you reboot the switch. For a persistent configuration, edit the `/etc/cumulus/switchd.conf` file, as described above.

```
cumulus@switch:~$ sudo sh -c 'echo 400 > /cumulus/switchd/config/interface/swp1/storm_control/unknown_unicast'
cumulus@switch:~$ sudo sh -c 'echo 3000 > /cumulus/switchd/config/interface/swp1/storm_control/multicast'
cumulus@switch:~$ sudo systemctl restart switchd.service
```
