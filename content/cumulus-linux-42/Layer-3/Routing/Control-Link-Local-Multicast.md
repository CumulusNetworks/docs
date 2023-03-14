---
title: Control Link Local Multicast
author: NVIDIA
weight: 785
toc: 3
---
Cumulus Linux provides a configuration option on Broadcom switches to disable forwarding of link-local multicast packets to the CPU so that such packets only flood the ASIC, which reduces CPU usage.

To disable forwarding of link local multicast packets to the CPU on a Broadcom switch, run the following command:

```
cumulus@switch:~$ echo TRUE > /cumulus/switchd/config/hal/bcm/ll_mcast_punt_disable
```

The configuration above takes effect immediately, but does not persist if you reboot the switch.

To apply the configuration so that it is persistent, edit the `/etc/cumulus/switchd.conf` file and uncomment the `hal.bcm.ll_mcast_punt_disable = TRUE` option. For example:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
#
# /etc/cumulus/switchd.conf - switchd configuration file
#
...
# Bridge L2MC Link-Local multicast punt disable
hal.bcm.ll_mcast_punt_disable = TRUE
...
```

A `switchd` restart is **not** required.
