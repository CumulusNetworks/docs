---
title: SysRq and Cumulus Linux
author: NVIDIA
weight: 322
toc: 4
---
When using SysRq with Cumulus Linux, `/var/log/syslog` might show unexpected output similar to the following:

```
[ 8638.455521] SysRq : HELP : loglevel(0-9) reBoot Crash terminate-all-tasks(E) memory-full-oom-kill(F) kill-all-tasks(I) thaw-filesystems(J) show-backtrace-all-active-cpus(L) show-memory-usage(M) nice-all-RT-tasks(N) powerOff show-registers(P) show-all-timers(Q) Sync show-task-states(T) Unmount show-blocked-tasks(W) dump-ftrace-buffer(Z)
```

To work around this issue, you can disable the SysRq facility temporarily with the following command:

```
cumulus@switch:~$ sudo bash
cumulus@switch:~$ echo 0 > /proc/sys/kernel/sysrq
```

The above command does not persist if you reboot the switch. To make this configuration persistent, create a `sysrq.conf` file in the `/etc/sysctl.d` directory and add the following line:

```
kernel.sysrq = 0
```

You use SysRq to interact with the kernel directly, typically when the switch hangs or is not working correctly. Several triggers reach SysRq:

- Pressing the SysRq key while connected to the console.
- Pressing the Break key while connected to the console.
- Issuing a Send Break from a telnet session into the switch.
- Issuing `echo ? > /proc/sysrq-trigger`.

{{%notice note%}}
Different terminal emulators might use different key sequences to generate a Break signal. On a directly attached laptop, a Break might send based on an application-specific hotkey.
{{%/notice%}}

A Break key presents an extended space (low signal without start and stop bits). You can also simulate a Break key by connecting a bad or incorrect cable or malfunctioning device to the console.

{{%notice note%}}
Verify that you have connected your serial console port correctly.
{{%/notice%}}

If the correct key sequence is evaluated after the SysRq trigger, it can also cause the switch to power off or reboot. Use caution when connecting cables and devices to the Cumulus Linux switch console.

For more information, see {{<exlink url="https://www.kernel.org/doc/html/latest/admin-guide/sysrq.html" >}}.
