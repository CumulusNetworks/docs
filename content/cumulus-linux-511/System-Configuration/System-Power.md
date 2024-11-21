---
title: System Power
author: NVIDIA
weight: 295
toc: 3
---
In certain situations, you might need to power off the switch instead of rebooting. To power off the switch, run the `cl-poweroff` command, which shuts down the switch.

```
cumulus@switch:~$ sudo cl-poweroff
```

Alternatively, you can run the Linux `poweroff` command, which will gracefully shut down the switch (the switch LEDs stay on). On certain switches, such as the NVIDIA SN2201, SN2010, SN2100, SN2100B, SN3420, SN3700, SN3700C, SN4410, SN4600C, SN4600, SN4700, SN5400, or SN5600, the switch reboots instead of powering off

```
cumulus@switch:~$ sudo poweroff
```
