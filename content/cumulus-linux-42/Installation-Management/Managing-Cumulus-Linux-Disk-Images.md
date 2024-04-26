---
title: Managing Cumulus Linux Disk Images
author: NVIDIA
weight: 30
toc: 3
---
The Cumulus Linux operating system resides on a switch as a *disk image*. This section discusses how to manage the image.

To install a new Cumulus Linux image, refer to {{<link title="Installing a New Cumulus Linux Image">}}. To upgrade Cumulus Linux, refer to {{<link title="Upgrading Cumulus Linux">}}.

## Determine the Switch Platform

To determine if your switch is on an x86 or ARM platform, run the `uname -m` command.

For example, on an x86 platform, `uname -m` outputs *x86\_64*:

```
cumulus@switch:~$ uname -m
 x86_64
```

On an ARM platform, `uname -m` outputs *armv7l*:

```
cumulus@switch:~$ uname -m
 armv7l
```

## Reprovision the System (Restart the Installer)

Reprovisioning the system deletes all system data from the switch.

To stage an ONIE installer from the network (where ONIE automatically locates the installer), run the `onie-select -i` command. A reboot is required for the reinstall to begin.

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

To stage an installer located in a specific location, run the `onie-install` `-i` command. You can specify a local, absolute or relative path, an HTTP or HTTPS server, SCP TFTP, or FTP server. You can also stage a Zero Touch Provisioning (ZTP) script along with the installer.
The `onie-install` command is typically used with the `-a` option to activate installation. If you do not specify the `-a` option, a reboot is required for the reinstall to begin.

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

## Migrate from Cumulus Linux to ONIE (Uninstall All Images and Remove the Configuration)

To remove all installed images and configurations, and return the switch to its factory defaults, run the `onie-select -k` command.

{{%notice warning%}}

The `onie-select -k` command takes a long time to run as it overwrites the entire NOS section of the flash. Only use this command if you want to erase all NOS data and take the switch out of service.

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

A reboot is required for the uninstallation process to begin.

{{%notice tip%}}

To cancel a pending uninstall operation, run the `onie-select -c` command:

```
cumulus@switch:~$ sudo onie-select -c
Cancelling pending uninstall at next reboot...done.
```

{{%/notice%}}

## Boot into Rescue Mode

If your system becomes unresponsive is some way, you can correct certain issues by booting into ONIE rescue mode. In rescue mode, the file systems are unmounted and you can use various Cumulus Linux utilities to try and resolve a problem.

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

A reboot is required to boot into rescue mode.

{{%/notice%}}

{{%notice tip%}}

To cancel a pending rescue boot operation, run the `onie-select -c` command:

```
cumulus@switch:~$ sudo onie-select -c
Cancelling pending rescue at next reboot...done.
```

{{%/notice%}}

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
