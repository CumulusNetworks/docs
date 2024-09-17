---
title: Factory Reset
author: NVIDIA
weight: 92
toc: 3
---
Factory reset puts the switch back to the same or similar state it was in when shipped from the factory. When you perform a factory reset, the currently installed image remains on the switch.

Use factory reset for wide scale data center deployments or if you work with multiple vendors, where each vendor installs their own configuration on the switch. You can also run factory reset when you want to remove a complex or corrupted configuration that is blocking your progress, when you want to move a switch from one network to another, reset the switch to factory defaults and configure it as a new switch, or if you want to selectively remove either configurations or system log files for debugging.
<!--
{{%notice note%}}
You must be root to run factory reset commands.
{{%/notice%}}
-->
## Run Factory Reset

Factory reset provides options to:
- Remove all configuration, system files, and log files.
- Remove certain configuration, system files, and log files but keep password policy rules, management interface configuration (such as eth0), local user accounts and roles, and SSH configuration.
- Remove system files and log files but keep all configuration.
- Remove configuration but keep system files and log files.

When you run the NVUE factory reset commands, the switch prompts you to confirm that you want to continue.

{{< tabs "215 ">}}
{{< tab "NVUE Commands ">}}

The following example resets the switch to the factory defaults and removes configuration, system files, and log files:

```
root@switch:~# nv action reset system factory-reset
The operation will reset the system configuration and initiate a reboot. 
Type [y] to reset the system configuration and reboot. 
Type [n] to abort. 
Do you want to continue? [y/n] y 
Action executing ... 
System will be rebooted,  configurations and system files might be deleted 
Action executing ... 
Broadcast message from root@cumulus (Fri 2024-08-09 17:12:02 UTC): 
The system will reboot now! 
```

The following example resets the switch to the factory defaults but keep password policy rules, management interface configuration (such as eth0), local user accounts and roles, and SSH configuration:

```
root@switch:~# nv action reset system factory-reset keep basic 
```

The following example resets the switch to the factory defaults but keeps all configuration:

```
root@switch:~# nv action reset system factory-reset keep all-config 
```

The following example resets the switch to the factory defaults but keeps all system files and log files:

```
root@switch:~# nv action reset system factory-reset keep all-files
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/tmp/factory-reset.conf` file, then restart the factory reset service with the `systemctl restart factory-reset.service` command.

```
root@switch:~# nano /tmp/factory-reset.conf
```

```
root@switch:~# systemctl restart factory-reset.service
```

{{< /tab >}}
{{< /tabs >}}

## Considerations

- The switch always reboots in cold mode after a factory reset even if the switch is in warm boot mode when you run factory reset commands.
- If ZTP fails (the ZTP configuration file is not present, there is no USB drive, or there are DHCP errors), factory reset continues successfully; ZTP is a separate task and does not affect the factory reset status.
- If there is an issue when running factory reset, the switch reverts to the previous configuration and logs the exceptions and errors.
- The factory reset command is similar to the `onie-select -k` command; however, `onie-select -k` also removes the installed image.  
