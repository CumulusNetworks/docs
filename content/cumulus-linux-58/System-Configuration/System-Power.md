---
title: System Power
author: NVIDIA
weight: 278
toc: 3
---
In certain situations, you might need to power off the switch instead of rebooting. To power off the switch, you can run the Linux `poweroff` command.

```
cumulus@switch:~$ sudo poweroff
```

When you run the Linux `poweroff` command on the SN2201, SN2010, SN2100, SN2100B, SN3420, SN3700, SN3700C, SN4410, SN4600C, SN4600, SN4700, or SN5600 switch, the switch reboots instead of powering off. To power off the switch, run the `cl-poweroff` command instead. The `cl-poweroff` command performs a hard *abrupt* power down instead of a graceful power down.

```
cumulus@switch:~$ sudo cl-poweroff
```
