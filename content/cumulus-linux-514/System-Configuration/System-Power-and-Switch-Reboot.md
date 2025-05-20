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
- **warm** restarts the switch with no interruption to traffic for existing route entries and without a hardware reset of the switch ASIC. See {{<link url="In-Service-System-Upgrade-ISSU" text="In-Service-System-Upgrade-ISSU">}}.
- **cold** restarts the system and resets all the hardware devices on the switch (including the switching ASIC). This is the default restart mode on the switch.
- **fast** restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The restart process maintains the forwarding entries of the switching ASIC and the data plane is not affected. Traffic outage is much lower in this mode as there is a momentary interruption after reboot, while the system reinitializes.

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

{{%notice warning%}}
After you change the restart mode on the switch with NVUE or `csmgrctl` commands, you must reboot the switch to activate the mode change.
{{%/notice%}}

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
