---
title: In Service System Upgrade - ISSU
author: NVIDIA
weight: 275
toc: 3
---
Use <span class="a-tooltip">[ISSU](## "In Service System Upgrade")</span> to upgrade and troubleshoot an active switch with minimal disruption to the network.

ISSU includes the following modes:
- Restart
- Upgrade
- Maintenance mode
- Maintenance ports

{{%notice note%}}
In earlier Cumulus Linux releases, ISSU was Smart System Manager.
{{%/notice%}}

## Restart Mode

You can configure the switch to restart in one of the following modes.

- **cold** restarts the system and resets all the hardware devices on the switch (including the switching ASIC).
- **fast** restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The restart process maintains the forwarding entries of the switching ASIC and the data plane is not affected. Traffic outage is much lower in this mode as there is a momentary interruption after reboot, while the system reinitializes.
- **warm** restarts the system with no interruption to traffic for existing route entries. Warm mode restarts the system without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. However, if no alternate paths exist, the switch continues forwarding with the existing entries with no interruptions. Warm mode reduces all of the available {{<link title="Forwarding Table Size and Profiles" text="forwarding table entries">}}  on the switch by half to accommodate traffic forwarding during a reboot.

   When you restart the switch in warm mode, BGP only performs a graceful restart if the BGP graceful restart option is set to `full`. To set BGP graceful restart to full, run the `nv set router bgp graceful-restart mode full` command, then apply the configuration with `nv config apply`. For more information about BGP graceful restart, refer to {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="Optional BGP Configuration">}}.

   In an eBGP multihop configuration with warm restart mode, you must set the {{<link url="Optional-BGP-Configuration/#restart-timers" text="BGP graceful restart timer">}} to 180 seconds or more.

{{%notice note%}}
Cumulus Linux supports:
- Fast mode for all protocols.
- Warm mode for 802.1X, layer 2 forwarding, layer 3 forwarding with BGP, static routing, and VXLAN routing with EVPN. Cumulus Linux does not support warm boot with EVPN MLAG or EVPN multihoming.
- Warm mode with optimized image (two partition) upgrade and package upgrade (the switch must be in warm mode before you start the upgrade).
{{%/notice%}}
<!--
{{%notice note%}}
Cumulus Linux does not support LACP bonds during warm boot; the LACP control plane sessions might time out before warm boot completes. Use a static Link Aggregation Group to keep bonds up during warm boot.
{{%/notice%}}
-->
NVIDIA recommends you use NVUE commands to configure restart mode and reboot the system. If you prefer to use `csmgrctl` commands, you must stop NVUE from managing the `/etc/cumulus/csmgrd.conf` file before you set restart mode:

1. Run the following NVUE commands:

   ```
   cumulus@switch:~$ nv set system config apply ignore /etc/cumulus/csmgrd.conf
   cumulus@switch:~$ nv config apply
   ```

2. Edit the `/etc/cumulus/csmgrd.conf` file and set the `csmgrctl_override` option to `true`:

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/csmgrd.conf
   csmgrctl_override=true
   ...
   ```

3. Save the configuration:

   ```
   cumulus@switch:~$ nv config save
   ```


{{%notice warning%}}
After you change the reboot mode on the switch using NVUE or `csmgrctl` commands, you must reboot the switch to activate the mode change. You can confirm the current operational reboot mode active on the switch using the `nv show system reboot` command.  
{{%/notice%}}

The following command configures the switch to restart in cold mode:

{{< tabs "28 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system reboot mode cold
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -c
```

{{< /tab >}}
{{< /tabs >}}

The following command configures the switch to restart in fast mode:

{{< tabs "52 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system reboot mode fast
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -f
```

{{< /tab >}}
{{< /tabs >}}

The following command configures the switch to restart in warm mode.

{{< tabs "76 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system reboot mode warm
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -w
```

{{< /tab >}}
{{< /tabs >}}

To reboot the switch in the restart mode you configure above with NVUE:

```
cumulus@switch:~$ nv action reboot system no-confirm
```

{{%notice note%}}
You must specify `no-confirm` at the end of the command.
{{%/notice%}}

To show system reboot information, such as the reboot date and time, reason, and reset mode (fast, cold, warm), run the NVUE `nv show system reboot` command:

```
cumulus@switch:~$ nv show system reboot
           operational                       applied  pending
---------  --------------------------------  -------  -------
reason                                                       
  gentime  2023-04-26T15:11:23.140569+00:00                  
  reason   Unknown                                           
  user     system/root
  mode     cold                              cold
  required no
```

## Upgrade Mode

Upgrade mode updates all the components and services on the switch to the latest Cumulus Linux minor release without impacting traffic. After upgrade is complete, you must restart the switch with either a {{<link url="#restart-mode" text="warm, cold, or fast restart">}}.

If the switch is in warm restart mode, restarting the switch after an upgrade does not result in traffic loss (this is a hitless upgrade).

Upgrade mode includes the following options:
- You can upgrade all the system components to the **latest** release without affecting traffic flow. You must restart the system after the upgrade completes with one of the {{<link url="#restart-mode" text="restart modes">}}.
- You can perform an upgrade dry run, which provides information on the components you want to upgrade so that you can review potential upgrade issues (in some cases, upgrading new packages might also upgrade additional existing packages due to dependencies).

The following command upgrades all the system components to the latest release:

{{< tabs "88 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ sudo nv action upgrade system packages to latest use-vrf default
```

By default, the NVUE `sudo nv action upgrade system packages` command runs in the management VRF. To run the command in a non-management VRF such as `default`, you must use the `use-vrf <vrf>` option.

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -u
```

{{< /tab >}}
{{< /tabs >}}

The following command provides information on the components you want to upgrade:

{{< tabs "114 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ sudo nv action upgrade system packages to latest use-vrf default dry-run
```

By default, the NVUE `sudo nv action upgrade system packages` command runs in the management VRF. To run the command in a non-management VRF such as `default`, you must use the `use-vrf <vrf>` option.

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -d
```

{{< /tab >}}
{{< /tabs >}}

## Maintenance Mode

Maintenance mode enables you to take a switch out of production to perform updates or troubleshoot issues. You can put all protocols or all interfaces in maintenance mode.

{{%notice note%}}
Cumulus Linux 5.13 and later provides new NVUE `nv set maintenance unit` commands and deprecates the `nv action enable system maintenance` commands provided in Cumulus Linux 5.12 and earlier:
{{%/notice%}}

### Protocols

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

### Ports

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

### Check Maintenance Mode

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
