---
title: System Power
author: NVIDIA
weight: 278
toc: 3
---
In certain situations, you might need to power off the switch instead of rebooting. To power off the switch, you can run the Linux `poweroff` command, which gracefully shuts down the switch (the switch LEDs stay on).

```
cumulus@switch:~$ sudo poweroff
```

When you run the Linux `poweroff` command on certain switches, such as the NVIDIA SN2201, SN2010, SN2100, SN2100B, SN3420, SN3700, SN3700C, SN4410, SN4600C, SN4600, SN4700, or SN5600, the switch reboots instead of powering off. To power off the switch, run the `cl-poweroff` command instead.

```
cumulus@switch:~$ sudo cl-poweroff
```
