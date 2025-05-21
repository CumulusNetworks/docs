---
title: Maintenance Mode
author: NVIDIA
weight: 290
toc: 3
---

Maintenance mode enables you to take a switch out of production to perform updates or troubleshoot issues. You can put all protocols or all interfaces in maintenance mode.

{{%notice note%}}
Cumulus Linux 5.13 and later provides new NVUE `nv set maintenance unit` commands and deprecates the `nv action enable system maintenance` commands provided in Cumulus Linux 5.12 and earlier:
{{%/notice%}}

## Protocols

When you put all protocols in maintenance mode:
- All the protocols that support graceful shutdown perform graceful shutdown with all their neighbors.
- The switch goes through a warmboot when rebooted if the switch is in `warm` mode or when you do a warmboot to upgrade software to the next release.

If the protocols perform a graceful shutdown while going into maintenance mode, but some neighbors do not have alternate paths, those neighbors continue to send traffic through the switch. That traffic continues to flow through this switch during warmboot and all protocols remain in maintenance mode throughout the warmboot process.

Protocols that support graceful restart continue to do a graceful restart during warmboot to relearn routes from neighbors in the usual way, even though the all-protocols maintenance unit is in maintenance mode.

{{< tabs "213 ">}}
{{< tab "NVUE Commands ">}}

To put all protocols in maintenance mode, run the `nv set maintenance unit all-protocols mode enabled` command. All the protocols that support graceful shutdown re-advertise the routes with a lower weight or preference.

```
cumulus@switch:~$ nv set maintenance unit all-protocols mode enabled
cumulus@switch:~$ nv config apply
```

To take all protocols out of maintenance and put them back into production, run the `nv set maintenance unit all-protocols mode disabled` command. All the protocols that support graceful shutdown re-advertise the routes with the original weight or preference.

```
cumulus@switch:~$ nv set maintenance unit all-protocols mode disabled
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To put all protocols in maintenance mode, edit the `/etc/cumulus/maintenance.conf` file as shown below, then run the `csmgrctl -m` command. All the protocols that support graceful shutdown re-advertise the routes with a lower weight or preference.

```
cumulus@switch:~$ sudo nano /etc/cumulus/maintenance.conf
{
    "maintenance_units": [
        {
            "interfaces": "all",
            "mode": "enabled",
            "name": "all-protocols",
            "protocols": "all"
        }
    ]
}
```

```
cumulus@switch:~$ sudo csmgrctl -m
```

To take all protocols out of maintenance and put them back into production, edit the `/etc/cumulus/maintenance.conf` and change `mode` to disabled, then run the `csmgrctl -m` command. All the protocols that support graceful shutdown re-advertise the routes with the original weight or preference.

```
cumulus@switch:~$ sudo nano /etc/cumulus/maintenance.conf
{
    "maintenance_units": [
        {
            "interfaces": "all",
            "mode": "disabled",
            "name": "all-protocols",
            "protocols": "all"
        }
    ]
}
```

```
cumulus@switch:~$ sudo csmgrctl -m
```

{{< /tab >}}
{{< /tabs >}}

## Ports

When you put all ports in maintenance mode, all the ports go into the link down state. When you take all ports out of maintenance and put them in production, all the ports move out of the link down state.

{{< tabs "248 ">}}
{{< tab "NVUE Commands ">}}

To put all the ports in maintenance mode, run the `nv set maintenance unit all-interfaces mode enabled` command:

```
cumulus@cumulus:mgmt$ nv set maintenance unit all-interfaces mode enabled
cumulus@switch:~$ nv config apply
```

To take all ports out of maintenance and put them in production, run the `nv set maintenance unit all-interfaces mode disabled` command:

```
cumulus@switch:~$ nv set maintenance unit all-interfaces mode disabled
cumulus@switch:~$ nv config apply 
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To put all the ports in maintenance mode, edit the `/etc/cumulus/maintenance.conf` file as shown below, then run the `csmgrctl -p` command. You must populate the `interfaces` field with either a comma-separated list of individual interfaces or interface ranges (using a hyphen). You must explicitly list any breakout interfaces.

```
cumulus@switch:~$ sudo nano /etc/cumulus/maintenance.conf
{
    "maintenance_units": [
        {
            "interfaces": "swp1s0-1,swp2-swp56",
            "mode": "enabled",
            "name": "all-interfaces",
            "protocols": "none"
        }
    ]
}
```

```
cumulus@switch:~$ sudo csmgrctl -p
```

To take all ports out of maintenance and put them in production, edit the `/etc/cumulus/maintenance.conf` and change `mode` to disabled, then run the `csmgrctl -p` command:

```
cumulus@switch:~$ sudo nano /etc/cumulus/maintenance.conf
{
    "maintenance_units": [
        {
            "interfaces": "swp1s0-1,swp2-swp56",
            "mode": "disabled",
            "name": "all-interfaces",
            "protocols": "none"
        }
    ]
}
```

```
cumulus@switch:~$ sudo csmgrctl -p
```

{{< /tab >}}
{{< /tabs >}}

## Check Maintenance Mode

To check the current maintenance mode on the switch, run the NVUE `nv show maintenance` command or the Linux `sudo csmgrctl -s` command:

```
cumulus@switch:~$ nv show maintenance
Maintenance Info 
==============
Unit                                 State
-----------------------              ---------------
all-protocols                        enabled
all-interfaces                       enabled 
```

To show the current maintenance mode of the protocols, run the `nv show maintenance unit all-protocols` command:

```
cumulus@switch:~$ nv show maintenance unit all-protocols
             operational      applied 
----------    -----------      ----------- 
state         enabled          enabled 
interfaces    all              all
protocols     all              all
```
