---
title: Managing Cumulus Linux Disk Images with ONIE
author: NVIDIA
weight: 50
toc: 3
---
The Cumulus Linux operating system resides on a switch as a *disk image*. This section discusses how to manage the image.

To install a new Cumulus Linux image, refer to {{<link title="Installing a New Cumulus Linux Image with ONIE">}}. To upgrade Cumulus Linux, refer to {{<link title="Upgrading Cumulus Linux">}}.

## Reprovision the System (Restart the Installer)

{{< tabs "TabID13">}}
{{< tab "NVUE Commands">}}

Reprovisioning the system deletes all system data from the switch.

To stage an <span class="a-tooltip">[ONIE](## "Open Network Install Environment")</span> installer from the network (where ONIE automatically locates the installer), run the `nv action boot-next system image onie install` command. You must reboot the switch to start the install process.

```
cumulus@switch:~$ nv action boot-next system image onie install 
WARNING:
WARNING: Operating System install requested.
WARNING: This will wipe out all system data.
WARNING:
Are you sure (y/N)? y
Enabling install at next reboot...done.
Reboot required to take effect.
```

To cancel a pending reinstall operation, run the `nv action cancel system image onie` command:

```
cumulus@switch:~$ nv action cancel system image onie
Cancelling pending install at next reboot...done.
```

To stage an installer located in a specific location, run the `nv action install system image onie <image>` command. You can specify a local, absolute or relative path, an HTTP or HTTPS server, SCP or FTP server. You can also stage a Zero Touch Provisioning (ZTP) script along with the installer.
Use the `activate reboot` option to activate installation and reboot the switch (`nv action install system image onie <image> activate`).

The following example stages the installer located at `http://203.0.113.10/image-installer` together with the ZTP script located at `http://203.0.113.10/ztp-script`, activates installation and ZTP, and reboots the switch. The `force` option suppresses the prompt and the action proceeds non-interactively. NVIDIA recommends using the `force` option for scripted, automated, or REST API invocations.

```
cumulus@switch:~$ nv action install system image onie http://203.0.113.10/image-installer ztp http://203.0.113.10/ztp-script force activate reboot
```

{{< /tab >}}
{{< tab "ONIE Commands">}}

Reprovisioning the system deletes all system data from the switch.

To stage an <span class="a-tooltip">[ONIE](## "Open Network Install Environment")</span> installer from the network (where ONIE automatically locates the installer), run the `onie-select -i` command. You must reboot the switch to start the install process.

```
cumulus@switch:~$ sudo onie-select -i
WARNING:
WARNING: Operating System install requested.
WARNING: This will wipe out all system data.
WARNING:
Are you sure (y/N)? y
Enabling install at next reboot...done.
Reboot required to take effect.
```

To cancel a pending reinstall operation, run the `onie-select -c` command:

```
cumulus@switch:~$ sudo onie-select -c
Cancelling pending install at next reboot...done.
```

To stage an installer located in a specific location, run the `onie-install -i <location>` command. You can specify a local, absolute or relative path, an HTTP or HTTPS server, SCP or FTP server. You can also stage a Zero Touch Provisioning (ZTP) script along with the installer.
You typically use the `onie-install` command with the `-a` option to activate installation. If you do not specify the `-a` option, you must reboot the switch to start the installation process.

The following example stages the installer located at `http://203.0.113.10/image-installer` together with the ZTP script located at `http://203.0.113.10/ztp-script` and activates installation and ZTP:

```
cumulus@switch:~$ sudo onie-install -i http://203.0.113.10/image-installer
cumulus@switch:~$ sudo onie-install -z http://203.0.113.10/ztp-script
cumulus@switch:~$ sudo onie-install -a
```

You can also specify these options together in the same command. For example:

```
cumulus@switch:~$ sudo onie-install -i http://203.0.113.10/image-installer -z http://203.0.113.10/ztp-script -a
```

To see more `onie-install` options, run `man onie-install.`

{{< /tab >}}
{{< /tabs >}}

## Migrate from Cumulus Linux to ONIE (Uninstall All Images and Remove the Configuration)

To remove all installed images and configurations, and return the switch to its factory defaults:

{{< tabs "TabID96">}}
{{< tab "NVUE Commands">}}

Run the `nv action boot-next system image onie uninstall` command.

{{%notice warning%}}
- The `nv action boot-next system image onie uninstall` command takes a long time to run as it overwrites the entire NOS section of the flash. Only use this command if you want to erase all NOS data and take the switch out of service.
- ONIE does not support front panel ports. After you run `nv action boot-next system image onie uninstall` to return the switch to its factory defaults, you must use the eth0 interface to provision the switch.
{{%/notice%}}

```
cumulus@switch:~$ nv action boot-next system image onie uninstall
WARNING:
WARNING: Operating System uninstall requested.
WARNING: This will wipe out all system data.
WARNING:
Are you sure (y/N)? y
Enabling uninstall at next reboot...done.
Reboot required to take effect.
```

You must reboot the switch to start the uninstallation process.

{{%notice tip%}}
To cancel a pending uninstall operation, run the `nv action cancel system image onie` command:

```
cumulus@switch:~$ nv action cancel system image onie
Cancelling pending uninstall at next reboot...done.
```
{{%/notice%}}

{{< /tab >}}
{{< tab "ONIE Commands">}}

To remove all installed images and configurations, and return the switch to its factory defaults, run the `onie-select -k` command.

{{%notice warning%}}
- The `onie-select -k` command takes a long time to run as it overwrites the entire NOS section of the flash. Only use this command if you want to erase all NOS data and take the switch out of service.
- ONIE does not support front panel ports. After you run `sudo onie-select -k` to return the switch to its factory defaults, you must use the eth0 interface to provision the switch.
{{%/notice%}}

```
cumulus@switch:~$ sudo onie-select -k
WARNING:
WARNING: Operating System uninstall requested.
WARNING: This will wipe out all system data.
WARNING:
Are you sure (y/N)? y
Enabling uninstall at next reboot...done.
Reboot required to take effect.
```

You must reboot the switch to start the uninstallation process.

{{%notice tip%}}
To cancel a pending uninstall operation, run the `onie-select -c` command:

```
cumulus@switch:~$ sudo onie-select -c
Cancelling pending uninstall at next reboot...done.
```
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

## Boot Into Rescue Mode

If your system becomes unresponsive, you can correct certain issues by booting into <span class="a-tooltip">[ONIE](## "Open Network Install Environment")</span> rescue mode, which uses unmounted file systems. You can use various Cumulus Linux utilities to try and resolve a problem.

{{< tabs "TabID170">}}
{{< tab "NVUE Commands">}}

To reboot the system into ONIE rescue mode, run the `nv action boot-next system image onie rescue` command:

```
cumulus@switch:~$ nv action boot-next system image onie rescue
WARNING:
WARNING: Rescue boot requested.
WARNING:
Are you sure (y/N)? y
Enabling rescue at next reboot...done.
Reboot required to take effect.
```

{{%notice note%}}
You must reboot the system to boot into rescue mode.
{{%/notice%}}

{{%notice tip%}}
To cancel a pending rescue boot operation, run the `nv action cancel system image onie` command:

```
cumulus@switch:~$ nv action cancel system image onie
Cancelling pending rescue at next reboot...done.
```
{{%/notice%}}

{{< /tab >}}
{{< tab "ONIE Commands">}}

To reboot the system into ONIE rescue mode, run the `onie-select -r` command:

```
cumulus@switch:~$ sudo onie-select -r
WARNING:
WARNING: Rescue boot requested.
WARNING:
Are you sure (y/N)? y
Enabling rescue at next reboot...done.
Reboot required to take effect.
```

{{%notice note%}}
You must reboot the system to boot into rescue mode.
{{%/notice%}}

{{%notice tip%}}
To cancel a pending rescue boot operation, run the `onie-select -c` command:

```
cumulus@switch:~$ sudo onie-select -c
Cancelling pending rescue at next reboot...done.
```
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

## Show ONIE Installer Information

To show the ONIE installer staged information and the installed images on both partitions, run the`nv show system image` command:

```
cumulus@switch:~$ nv show system image 
                             operational 
-------------------          ------------------------------- 
current                      1 
next                         ONIE install 
partition1 
  build-id                   5.18.0 
  description                Cumulus Linux 5.18.0 
  disk                       /dev/sda5 
  release                    5.18.0 
partition2 
  build-id                   5.18.0
  description                Cumulus Linux 5.18.0 
  disk                       /dev/sda6 
  release                    5.18.0 
onie 
  mode                       install 
  description                Cumulus Linux 5.18.0 
  release                    5.18.0 
  build-id                   5.18.0 
  build-date                 2026-06-06T02:02:43+00:00 
 installer-url               http://203.0.113.10/image-installer            
startup-url                  /etc/nvue.d/startup.yaml 
```

{{%notice note%}}
When the ONIE installer is not staged, onie information does not show.
{{%/notice%}}

To show the onie installer staged information only:

```
cumulus@switch:~$ nv show system image onie
                             operational 
-------------------          ------------------------------- 
  mode                       install 
  description                Cumulus Linux 5.18.0 
  release                    5.18.0 
  build-id                   5.18.0 
  build-date                 2026-06-06T02:02:43+00:00 
installer-url                http://203.0.113.10/image-installer 
 ztp-url                     http://203.0.113.10/users/user1.sh                            
startup-url                  /etc/nvue.d/startup.yaml
```

## Inspect the Image File

The Cumulus Linux image file is executable. From a running switch, you can display, extract, and verify the contents of the image file.

To display the contents of the Cumulus Linux image file, pass the `info` option to the image file. For example, to display the contents of an image file called `onie-installer` located in the `/var/lib/cumulus/installer` directory:

```
cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer info
Verifying image checksum ...OK.
Preparing image archive ... OK.
Control File Contents
=====================
Description: Cumulus Linux 4.1.0
Release: 4.1.0
Architecture: amd64
Switch-Architecture: bcm-amd64
Build-Id: dirtyz224615f
Build-Date: 2019-05-17T16:34:22+00:00
Build-User: clbuilder
Homepage: http://www.cumulusnetworks.com/
Min-Disk-Size: 1073741824
Min-Ram-Size: 536870912
mkimage-version: 0.11.111_gbcf0
```

To extract the contents of the image file, use with the `extract <path>` option. For example, to extract an image file called `onie-installer` located in the `/var/lib/cumulus/installer` directory to the `mypath` directory:

```
cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer extract mypath
total 181860
-rw-r--r-- 1 4000 4000       308 May 16 19:04 control
drwxr-xr-x 5 4000 4000      4096 Apr 26 21:28 embedded-installer
-rw-r--r-- 1 4000 4000  13273936 May 16 19:04 initrd
-rw-r--r-- 1 4000 4000   4239088 May 16 19:04 kernel
-rw-r--r-- 1 4000 4000 168701528 May 16 19:04 sysroot.tar
```

To verify the contents of the image file, use with the `verify` option. For example, to verify the contents of an image file called `onie-installer` located in the `/var/lib/cumulus/installer` directory:

```
cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer verify
Verifying image checksum ...OK.
Preparing image archive ... OK.
./cumulus-linux-bcm-amd64.bin.1: 161: ./cumulus-linux-bcm-amd64.bin.1: onie-sysinfo: not found
Verifying image compatibility ...OK.
Verifying system ram ...OK.
```

## Related Information

{{<exlink url="http://opencomputeproject.github.io/onie/" text="Open Network Install Environment (ONIE) Home Page">}}
