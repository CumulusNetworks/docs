---
title: Factory Reset
author: NVIDIA
weight: 80
toc: 3
---
Factory reset puts the switch back to the same or similar state it was in when shipped from the factory. When you perform a factory reset, the currently installed image remains on the switch.

You can also run factory reset when you want to remove a complex or corrupted configuration that is blocking your progress, when you want to move a switch from one network to another, reset the switch to factory defaults and configure it as a new switch, or if you want to selectively remove either configurations or system log files to identify issues.

{{%notice note%}}
- To run factory reset commands, you must have system admin, root, or sudo privileges.
- The switch does not support factory reset if you upgrade to Cumulus Linux 5.12 from Cumulus Linux 5.9.x or 5.10.x with package upgrade.
- To run factory reset with NVUE commands, the `nvued` service must be running.
- After a successful reset, Cumulus Linux runs `ztp-X` to restart the ZTP process. The ZTP `-X` option resets ZTP and clears the URL cache.
{{%/notice%}}

## Run Factory Reset

Factory reset provides options to:
- Remove all configuration, system files, and log files.
- Remove system files and log files but keep certain configuration, such as password policy rules, management interface configuration (such as eth0), local user accounts and roles, and SSH configuration.
- Remove system files and log files but keep all configuration.
- Remove configuration but keep system files and log files.

{{< tabs "215 ">}}
{{< tab "NVUE Commands ">}}

To reset the switch to the factory defaults and remove **all** configuration, system files, and log files, run the `nv action reset system factory-default` command.

Use the following options to keep configuration or system and log files:

| Option | Description|
| ------ | ---------- |
| `keep basic` | Retains password policy rules, management interface configuration, local user accounts and roles, and SSH configuration.|
| `keep all-config` | Retains all configuration. |
| `keep only-files` | Retains all system files and log files. |

When you run the NVUE factory reset commands, the switch prompts you to confirm that you want to continue. To run the commands without the prompts to continue, add the `force` option at the end of the command.

The following example resets the switch to the factory defaults and removes **all** configuration, system files, and log files:

```
cumulus@switch:~$ nv action reset system factory-default
This operation will reset the system configuration, delete the log files and reboot the switch.
Type [y] continue. 
Type [n] to abort. 
Do you want to continue? [y/n] y
...
```

The following example resets the switch to the factory defaults but keeps password policy rules, management interface configuration (such as eth0), local user accounts and roles, and SSH configuration:

```
cumulus@switch:~$ nv action reset system factory-default keep basic
This operation will keep only the basic system configuration, delete the log files and reboot the switch.
Type [y] to continue. 
Type [n] to abort. 
Do you want to continue? [y/n] y
... 
```

The following example resets the switch to the factory defaults but keeps all configuration:

```
cumulus@switch:~$ nv action reset system factory-default keep all-config
This operation will not reset the system configuration, only delete the log files and reboot the switch.
Type [y] to continue.
Type [n] to abort.
Do you want to continue? [y/n] y 
...
```

The following example resets the switch to the factory defaults but keeps all system files and log files:

```
cumulus@switch:~$ nv action reset system factory-default keep only-files
This operation will reset the system configuration, not delete the log files and reboot the switch.
Type [y] to continue. 
Type [n] to abort. 
Do you want to continue? [y/n] y 
...
```

The following example resets the switch to the factory defaults but keeps all system files and log files. The force option runs factory reset without the prompts to continue:

```
cumulus@switch:~$ nv action reset system factory-default keep only-files force 
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To reset the switch to the factory defaults and remove all configuration, system files, and log files (the default option), run the `systemctl restart factory-reset.service` command.

```
cumulus@switch:~$ sudo systemctl restart factory-reset.service
```

To keep certain configuration, keep all configuration but not system and log files, or keep system and log files but no configuration, create the `/tmp/factory-reset.conf` file, add one of the reset options to the file, then run the `systemctl restart factory-reset.service` command.
- `TYPE=keep-basic` resets the switch to the factory defaults but keeps password policy rules, management interface configuration (such as eth0), local user accounts and roles, and SSH configuration.
- `TYPE=keep-all-config` resets the switch to the factory defaults but keeps all configuration.
- `TYPE=keep-all-files` resets the switch to the factory defaults but keep all system files and log files.

The following example resets the switch to the factory defaults but keeps password policy rules, management interface configuration (such as eth0), local user accounts and roles, and SSH configuration.

```
cumulus@switch:~$ sudo nano /tmp/factory-reset.conf
TYPE=keep-basic
```

{{%notice note%}}
When you use the `keep-basic` option, you must create a `/tmp/startup-new.yaml` file with the configuration you want after factory reset, then start `factory-reset.service`. This is not necessary for the other options.
{{%/notice%}}

```
cumulus@switch:~$ sudo systemctl restart factory-reset.service
```

{{< /tab >}}
{{< /tabs >}}

## Considerations

- The switch always reboots in cold mode after a factory reset even if the switch is in warm boot mode when you run factory reset commands.
- If ZTP fails (the ZTP configuration file is not present, there is no USB drive, or there are DHCP errors), factory reset continues successfully; ZTP is a separate task and does not affect the factory reset status.
- If there is an issue when running factory reset, the switch reverts to the previous configuration and logs the exceptions and errors.
- The factory reset command is similar to the `onie-select -k` command; however, `onie-select -k` also removes the installed image.  
