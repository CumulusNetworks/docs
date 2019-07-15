---
title: Managing Cumulus Linux Disk Images
author: Cumulus Networks
weight: 41
aliases:
 - /display/DOCS/Managing+Cumulus+Linux+Disk+Images
 - /pages/viewpage.action?pageId=8362634
pageID: 8362634
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
The Cumulus Linux operating system resides on a switch as a *disk
image*. This section discusses how to manage the disk image.

For information on installing a new Cumulus Linux disk image, refer to
[Installing a New Cumulus Linux
Image](/cumulus-linux/Installation_Management/Installing_a_New_Cumulus_Linux_Image).
For information on upgrading Cumulus Linux, refer to [Upgrading Cumulus
Linux](/cumulus-linux/Installation_Management/Upgrading_Cumulus_Linux).

## <span>Determine the Switch Platform</span>

To determine if your switch is on an x86 or ARM platform, run the `uname
-m` command.

For example, on an x86 platform, `uname -m` outputs *x86\_64*:

    cumulus@x86switch$ uname -m
     x86_64

On an ARM platform, `uname -m` outputs *armv7l*:

    cumulus@ARMswitch$ uname -m
     armv7l

You can also visit the HCL ([hardware compatibility
list](http://cumulusnetworks.com/support/linux-hardware-compatibility-list/))
to look at your hardware and determine the processor type.

## <span>Reprovision the System (Restart the Installer)</span>

Reprovisioning the system deletes all system data from the switch.

To initiate the provisioning and installation process, run the
`onie-select -i` command:

    cumulus@switch:~$ sudo onie-select -i
    WARNING:
    WARNING: Operating System install requested.
    WARNING: This will wipe out all system data.
    WARNING:
    Are you sure (y/N)? y
    Enabling install at next reboot...done.
    Reboot required to take effect.

{{%notice note%}}

A reboot is required for the reinstall to begin.

{{%/notice%}}

{{%notice tip%}}

To cancel a pending reinstall operation, run the `onie-select -c`
command:

    cumulus@switch:~$ sudo onie-select -c
    Cancelling pending install at next reboot...done.

{{%/notice%}}

## <span>Uninstall All Images and Remove the Configuration</span>

To remove all installed images and configurations and return the switch
to its factory defaults, run the `onie-select -k` command:

    cumulus@switch:~$ sudo onie-select -k
    WARNING:
    WARNING: Operating System uninstall requested.
    WARNING: This will wipe out all system data.
    WARNING:
    Are you sure (y/N)? y
    Enabling uninstall at next reboot...done.
    Reboot required to take effect.

{{%notice note%}}

A reboot is required for the uninstall to begin.

{{%/notice%}}

{{%notice tip%}}

To cancel a pending uninstall operation, run the `onie-select -c`
command:

    cumulus@switch:~$ sudo onie-select -c
    Cancelling pending uninstall at next reboot...done.

{{%/notice%}}

## <span>Boot into Rescue Mode</span>

If your system becomes broken is some way, you can correct certain
issues by booting into ONIE rescue mode. In rescue mode, the file
systems are unmounted and you can use various Cumulus Linux utilities to
try and resolve a problem.

To reboot the system into ONIE rescue mode, run the `onie-select -r`
command:

    cumulus@switch:~$ sudo onie-select -r
    WARNING:
    WARNING: Rescue boot requested.
    WARNING:
    Are you sure (y/N)? y
    Enabling rescue at next reboot...done.
    Reboot required to take effect.

{{%notice note%}}

A reboot is required to boot into rescue mode.

{{%/notice%}}

{{%notice tip%}}

To cancel a pending rescue boot operation, run the `onie-select -c`
command:

    cumulus@switch:~$ sudo onie-select -c
    Cancelling pending rescue at next reboot...done.

{{%/notice%}}

## <span>Inspect the Image File</span>

The Cumulus Linux installation disk image file is executable. From a
running <span style="color: #333333;"> switch, you can display, extract,
and verify the contents of the image file. </span>

<span style="color: #333333;"> To display the contents of the Cumulus
Linux image file, pass the `info` option to the image file. For example,
to display the contents of an image file called `onie-installer` located
in the `/var/lib/cumulus/installer` directory: </span>

    cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer info 
    Verifying image checksum ...OK. 
    Preparing image archive ... OK. 
    Control File Contents 
    ===================== 
    Description: Cumulus Linux 3.7.6 
    Release: 3.7.6 
    Architecture: amd64 
    Switch-Architecture: bcm-amd64 
    Build-Id: 03bbebdzc4d0ff5 
    Build-Date: 2019-05-01T19:04:25+0000 
    Build-User: clbuilder 
    Homepage: http://www.cumulusnetworks.com/ 
    Min-Disk-Size: 1073741824 
    Min-Ram-Size: 536870912 
    mkimage-version: 0.11.118_gf541

To extract the contents of the image file, use with the `extract <path>`
option. For example, to extract an image file called `onie-installer`
located in the `/var/lib/cumulus/installer` directory to the `mypath`
directory:

    cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer extract mypath 
    total 181860 
    -rw-r--r-- 1 4000 4000 308 May 16 19:04 control 
    drwxr-xr-x 5 4000 4000 4096 Apr 26 21:28 embedded-installer 
    -rw-r--r-- 1 4000 4000 13273936 May 16 19:04 initrd 
    -rw-r--r-- 1 4000 4000 4239088 May 16 19:04 kernel 
    -rw-r--r-- 1 4000 4000 168701528 May 16 19:04 sysroot.tar

To verify the contents of the image file, use with the `verify` option.
For example, to verify the contents of an image file called
`onie-installer` located in the `/var/lib/cumulus/installer` directory:

    cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer verify 
    Verifying image checksum ...OK. 
    Preparing image archive ... OK. 
    ./cumulus-linux-bcm-amd64.bin.1: 161: ./cumulus-linux-bcm-amd64.bin.1: onie-sysinfo: not found 
    Verifying image compatibility ...OK. 
    Verifying system ram ...OK.

## <span>Related Information</span>

[Open Network Install Environment (ONIE) Home
Page](http://opencomputeproject.github.io/onie/)
