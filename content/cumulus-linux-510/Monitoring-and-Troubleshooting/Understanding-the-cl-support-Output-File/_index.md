---
title: Understanding the cl-support Output File
author: NVIDIA
weight: 1050
toc: 3
---
The `cl-support` script generates a compressed archive file of useful information for troubleshooting. The system either creates the file automatically or you can create the file manually.
<!-- vale off -->
## Automatic cl-support File
<!-- vale on -->
The system creates the `cl-support` file automatically:
- When there is a {{<exlink url="http://linux.die.net/man/5/core" text="core dump file">}} for any application (not specific to Cumulus Linux, but something all Linux distributions support), located in `/var/support/core`.
- When one of the monitored services fails for the first time after you reboot or power cycle the switch.
<!-- vale off -->
## Manual cl-support File
<!-- vale on -->

{{< tabs "TabID19 ">}}
{{< tab "NVUE Commands ">}}

To create the `cl-support` file manually, run the `nv action generate system tech-support` command:

```
cumulus@switch:~$ nv action generate system tech-support
Action executing ...
Generating system tech-support file, it might take a few minutes...
Action executing ...
Generated tech-support
Action succeeded
```

Cumulus Linux saves the `cl-support` file in the `/var/support` directory. The file name starts with `cl_support` and ends with the date and time of creation.

{{%notice note%}}
The Linux command to generate the `cl-support` file includes more options; for example, you can include security sensitive information, include debugging information, only run certain modules, and provide a reason for running the script in the file.
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

To create the `cl-support` file manually, run the `cl-support` command:

```
cumulus@switch:~$ sudo cl-support
```

If the Cumulus Linux support team requests that you submit the output from `cl-support` to investigate issues you experience, and you need to include security-sensitive information, such as the `sudoers` file, use the `-s` option:

```
cumulus@switch:~$ sudo cl-support -s
```
<!-- vale off -->
### cl-support Script Options

| Option | Description |
| ------- | ------------ |
| `-h`: | Displays the available `cl-support` script options with a description. |
| `-c`: | Runs only modules matching core files (if no `-e` modules). |
| `-D`: | Displays debugging information. |
| `-d`: | Does not run modules in the provided comma separated list. |
| `-e`: | Only runs modules in the provided comma separated list. `-e all` runs all modules and submodules, including all optional modules. |
| `-j`: | Creates `json` output files for modules, where supported. |
| `-l`: | Lists the available modules, then exits. |
| `-M`: | Does not set a timeout for modules. Use this option with `-T`. |
| `-m`: | Runs modules serially and sets the module memory limit in MB; `-m 0` runs serially without limits. |
| `-p`: | Adds a prefix to the `cl-support` archive file name. |
| `-r`: | Provides the reason for running the `cl-support` script. You must enclose the reason in quotes. |
| `-S`: | Uses a different output directory than the default `/var/support`. |
| `-s`: | Includes security sensitive information, such as the `sudoers` file. |
| `-T`: | Sets the timeout in seconds for creating the `cl-support` file.  0 disables the timeout. |
| `-t`: | Provides a tag string as part of the `cl-support` file name. |
| `-v`: | Runs in verbose mode to display status messages. |

### cl-support Examples
<!-- vale on -->
The following example does not run the `cl-support` script on the `ptp4l.ptp4l` and `what-just-happened.wjh` modules.

```
cumulus@switch:~$ sudo cl-support -d ptp4l.ptp4l,what-just-happened.wjh
cl-support: cl-support is running without memory limits
Please send /var/support/cl_support_leaf01_20240214_183635.txz to Cumulus support.
```

The following example runs the `cl-support` script and displays debugging information:

```
cumulus@switch:~$ sudo cl-support -D
DEBUG: Memory headroom set as 256MB
DEBUG: Available memory 576MB
DEBUG: Allowed memory consumption calculated at 320MB
DEBUG: Using calculated memory limit
DEBUG: Last parallel mode archive creation used 4MB
DEBUG: /usr/bin/systemd-run -q -P -G -p MemoryMax=320M /usr/bin/time -v -o /tmp/tmp.f8L5l6odWn /usr/lib/cumulus/cl-support -D
DEBUG: run_timeout 90 synced
...
```

The following example runs the `cl-support` script, lists available modules, then exits.

```
cumulus@switch:~$ sudo cl-support -l
Default modules: synced.synced ptp4l.ptp4l what-just-happened.wjh
   gdb.coreinfo openvswitch.dump ptmd.ptm switchd.mlx switchd.stack
   switchd.fuse clag.clag network.kernel network.ifquery network.sfp
   network.sfphex network.net_use network.ifupdown2_policy dot1x.config
   system.versions system.logs system.systemd system.dmesg system.hwinfo
   system.memory_use system.configs system.pkg system.misc system.uefi
   system.time frr.frr neighmgr.neighmgr nvue.config lldp.lldp
Optional modules: switchd.verbose clag.clagkerneldB system.pkgverify
   frr.ospftable frr.ospf6table frr.evpntable frr.bgptable nclu.config
```

The following example adds a prefix to the generated `cl-support` file name:

```
cumulus@switch:~$ sudo cl-support -p myprefix
Please send /var/support/myprefix_support_leaf01_20240214_184135.txz to Cumulus support.
```

The following example provides the reason for running the `cl-support` script:

```
cumulus@switch:~$ sudo cl-support -r "switchd crash"
Please send /var/support/cl_support_leaf01_20240214_184806.txz to Cumulus support.
```

{{< /tab >}}
{{< /tabs >}}
<!-- vale off -->
## Delete cl-support Files
<!-- vale on -->
To delete a `cl-support` file from the switch, run the NVUE `nv action delete system tech-support files <file-name>` command. You can also use the Linux `sudo rm /var/support/<file-name>` command.

```
cumulus@switch:~$ nv action delete system tech-support files /var/support/cl_support_leaf01_20240725_221237.txz
Action executing ...
File Delete Succeeded
Action succeeded
```

## Show cl-support Files

To show the `cl-support` files on the switch, run the `nv show system tech-support files` command. You can also run the Linux `ls` command on the `/var/support` directory (`ls /var/support`).

```
cumulus@switch:~$ nv show system tech-support files
File name                              File path                                         
-------------------------------------  --------------------------------------------------
cl_support_leaf01_20240725_225811.txz  /var/support/cl_support_leaf01_20240725_225811.txz
```
<!-- vale off -->
## Upload cl-support Files
<!-- vale on -->
To upload a `cl-support` file off the switch to an external location, run the `nv action upload system tech-support files <file-name> <remote-url>` command.

## Related Information

For information on the directories included in the `cl-support` archive, see:
- {{<link url="Troubleshooting-the-etc-Directory">}}. The `/etc` directory contains the largest number of files.
- {{<link url="Troubleshooting-Log-Files">}}. This guide highlights the most important log files to inspect. Keep in mind, `cl-support` includes all log files.
