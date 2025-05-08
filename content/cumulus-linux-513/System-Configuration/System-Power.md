---
title: System Power
author: NVIDIA
weight: 295
toc: 3
---

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
