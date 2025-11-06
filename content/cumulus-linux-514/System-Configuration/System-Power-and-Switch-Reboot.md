---
title: System Power and Switch Reboot
author: NVIDIA
weight: 295
toc: 3
---
Cumulus Linux provides commands to:
- {{<link url="#switch-reboot" text="Reboot the switch">}}
- {{<link url="#power-off" text="Power off the switch">}}
- {{<link url="#power-cycle" text="Power cycle the switch">}}

## Switch Reboot

Cumulus Linux provides these reboot modes:
- **cold** restarts the system and resets all the hardware devices on the switch (including the switching ASIC). This is the default restart mode on the switch.
- **fast** restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The switch restarts the kernel and software stack without touching the forwarding entries or the switching ASIC; therefore, the data plane is not affected as the software stack restarts. Traffic outage is much lower in this mode as there is a momentary interruption after reboot, while the system reinitializes.
- **warm** restarts the switch with no interruption to traffic for existing route entries and without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. Warm reboot mode reduces all the available {{<link title="Forwarding Table Size and Profiles" text="forwarding table entries">}} on the switch by half to accommodate traffic forwarding during a reboot.

  When you restart the switch in warm reboot mode, BGP only performs a graceful restart if the BGP graceful restart option is set to `full`. To set BGP graceful restart to full, run the `nv set router bgp graceful-restart mode full` command, then apply the configuration with `nv config apply`. For more information about BGP graceful restart, refer to {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="Optional BGP Configuration">}}.

  In an eBGP multihop configuration with warm reboot mode, you must set the {{<link url="Optional-BGP-Configuration/#restart-timers" text="BGP graceful restart timer">}} to 180 seconds or more.

{{%notice note%}}
Cumulus Linux supports warm reboot mode with:
- 802.1X, layer 2 forwarding, layer 3 forwarding with BGP, static routing, and VXLAN routing with EVPN.
- Optimized image (two partition) upgrade and package upgrade (the switch must be in warm reboot mode before you start the upgrade).

The following features are not supported during warm boot:
- EVPN MLAG or EVPN multihoming.
- LACP bonds. LACP control plane sessions might time out before warm boot completes. Use static LAG to keep bonds up with sub-second convergence during warm boot.
{{%/notice%}}
<!--
{{%notice note%}}
Cumulus Linux does not support LACP bonds during warm boot; the LACP control plane sessions might time out before warm boot completes. Use a static Link Aggregation Group to keep bonds up during warm boot.
{{%/notice%}}
-->
NVIDIA recommends you use NVUE commands to configure reboot mode and reboot the system. If you prefer to use `csmgrctl` commands, you must stop NVUE from managing the `/etc/cumulus/csmgrd.conf` file before you set reboot mode.

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

The following commands configure the switch to restart in cold mode:

{{< tabs "108 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system reboot mode cold
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv action reboot system no-confirm
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -c
```

```
cumulus@switch:~$ sudo reboot
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

```
cumulus@switch:~$ nv action reboot system no-confirm
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -f
```

```
cumulus@switch:~$ sudo reboot
```

{{< /tab >}}
{{< /tabs >}}

The following command configures the switch to restart in warm mode.

{{< tabs "85 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system reboot mode warm
cumulus@switch:~$ nv config apply
```

Reboot the switch:

```
cumulus@switch:~$ nv action reboot system no-confirm
```

{{%notice note%}}
You must specify `no-confirm` at the end of the command.
{{%/notice%}}

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -w
```

```
cumulus@switch:~$ sudo reboot
```

{{< /tab >}}
{{< /tabs >}}

{{%notice warning%}}
After you change the reboot mode on the switch with NVUE or `csmgrctl` commands, you must reboot the switch to activate the mode change.
{{%/notice%}}

### Show Reboot Mode

You can confirm the current operational reboot mode active on the switch with the `nv show system reboot` command. The command also shows reboot information, such as the reboot date and time, and reason:

```
cumulus@switch:~$ nv show system reboot
           operational                       applied
---------  --------------------------------  -------
reason                                              
  reason   Unknown                                  
  gentime  2025-05-16T16:08:27.798068+00:00         
  user     system/root                              
mode       warm                               warm   
required   no
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

## Power Cycle

NVUE provides the `nv action power-cycle system` command so that you can power cycle the switch remotely to recover from certain conditions, such as a thermal ASIC shutdown due to high temperatures.

When you run the `nv action power-cycle system` command, the switch prompts you for confirmation before power cycling.

```
cumulus@switch:~$ nv action power-cycle system
The operation will Power Cycle the switch.
Type [y] to power cycle.
Type [N] to abort.

Do you want to continue? [y/N]  
Action executing ... 
Action succeeded 
```

To power cycle the switch without prompts for confirmation, run the `nv action power-cycle system force` command:

```
cumulus@switch:~$ nv action power-cycle system force 
Action executing ... 
Action succeeded
```
