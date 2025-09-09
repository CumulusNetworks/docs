---
title: System Power and Switch Reboot
author: NVIDIA
weight: 295
toc: 3
---
Cumulus Linux provides commands to:
- {{<link url="#switch-reboot" text="Reboot the switch">}}
- {{<link url="#power-off" text="Power off the switch">}}

## Switch Reboot

Cumulus Linux provides these reboot modes:
- **immediate** reboots the switch immediately without notifying any running processes. Use this mode to reboot as quickly as possible, skipping graceful shutdown to avoid delays or to avoid the switch from hanging.
- **halt** shuts down the system. Use this mode to stop the switch completely instead of rebooting.
- **power-cycle** lets you power cycle the switch to recover from certain conditions, such as a thermal ASIC shutdown due to high temperatures.
- **cold** restarts the system and resets all the hardware devices on the switch (including the switching ASIC). This is the default restart mode on the switch.
- **fast** restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The switch restarts the kernel and software stack without touching the forwarding entries or the switching ASIC; therefore, the data plane is not affected as the software stack restarts. Traffic outage is much lower in this mode as there is a momentary interruption after reboot, while the system reinitializes.
- **warm** restarts the switch with no interruption to traffic for existing route entries and without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. Warm reboot mode reduces all the available {{<link title="Forwarding Table Size and Profiles" text="forwarding table entries">}} on the switch by half to accommodate traffic forwarding during a reboot.

  When you restart the switch in warm reboot mode, BGP only performs a graceful restart if the BGP graceful restart option is set to `full`. To set BGP graceful restart to full, run the `nv set router bgp graceful-restart mode full` command, then apply the configuration with `nv config apply`. For more information about BGP graceful restart, refer to {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="Optional BGP Configuration">}}.

  In an eBGP multihop configuration with warm reboot mode, you must set the {{<link url="Optional-BGP-Configuration/#restart-timers" text="BGP graceful restart timer">}} to 180 seconds or more.

{{%notice note%}}
Cumulus Linux supports warm reboot mode with:
- 802.1X, layer 2 forwarding, layer 3 forwarding with BGP, static routing, and VXLAN routing with EVPN. Cumulus Linux does not support warm boot with EVPN MLAG or EVPN multihoming.
{{%/notice%}}

### Resource Allocation

To manage switch resource allocation for fast, cold, and warm reboot mode, you can configure the resource mode to be either `half` or `full`. By default, the resource mode for warm boot and ISSU-based software upgrade is `half`.

The following example sets the switch resource mode to `full`:

```
cumulus@switch:~$ nv set system forwarding resource-mode full
```

To set the resource-mode back to the default value (half) run the `nv unset system forwarding resource-mode` command.

### Reboot

To reboot the switch, run the `nv action reboot system <mode>` command. To force the reboot without prompting for confirmation, add the `force` option (`nv action reboot system <mode> force`).

The following command reboots the switch immediately without notifying any running processes:

```
cumulus@switch:~$ nv action reboot system immediate

Do you want to continue? [y/N]  
Action executing ... 
Action succeeded 
```

The following command shuts down the system:

```
cumulus@switch:~$ nv action reboot system halt

Do you want to continue? [y/N]  
Action executing ... 
Action succeeded 
```

The following command power cycles the switch:

```
cumulus@switch:~$ nv action reboot system power-cycle
The operation will Power Cycle the switch.
Type [y] to power cycle.
Type [N] to abort.

Do you want to continue? [y/N]  
Action executing ... 
Action succeeded 
```

The following command reboots the switch in cold mode without prompting for confirmation:

```
cumulus@switch:~$ nv action reboot system cold force
```

You can also run `nv action reboot system force` because cold reboot is the default mode.

The following command reboots the switch in fast mode:

```
cumulus@switch:~$ nv action reboot system fast

Do you want to continue? [y/N]  
Action executing ... 
Action succeeded 
```

The following command reboots the switch in warm mode without prompting for confirmation.

```
cumulus@switch:~$ nv action reboot system warm force
```

### Show Reboot and Resource Mode

To show reboot information, such as the date and time, and reason, and the reboot mode, run the `nv show system reboot` command:

```
cumulus@switch:~$ nv show system reboot
           operational                       applied
---------  --------------------------------  -------
reason                                              
  reason   Unknown                                  
  gentime  2025-05-16T16:08:27.798068+00:00         
  user     system/root                              
required   no
last-reboot-mode  warm
```

To display the current resource mode, run the `nv show system forwarding resource-mode` command. 

```
cumulus@switch:~$ nv show system forwarding resource-mode
cumulus@switch:~$ nv config apply
```

## Power Off

In certain situations, you might need to power off the switch instead of rebooting. To power off the switch, run the `cl-poweroff` command, which shuts down the switch.

```
cumulus@switch:~$ sudo cl-poweroff
```

You can also run the Linux `poweroff` command, which gracefully shuts down the switch (the switch LEDs stay on). On certain switches, such as the NVIDIA SN2201, SN2010, SN2100, SN2100B, SN3420, SN3700, SN3700C, SN4410, SN4600C, SN4600, SN4700, SN5400, or SN5600, the switch reboots instead of powering off.

```
cumulus@switch:~$ sudo poweroff
```
