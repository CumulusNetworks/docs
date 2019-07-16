---
title: Managing Cumulus Linux Disk Images
author: Cumulus Networks
weight: 41
aliases:
 - /display/CL40/Managing-Cumulus-Linux-Disk-Images
 - /pages/viewpage.action?pageId=8366355
pageID: 8366355
product: Cumulus Linux
version: '4.0'
imgData: cumulus-linux-40
siteSlug: cumulus-linux-40
---
The Cumulus Linux operating system resides on a switch as a *disk
image*. This section discusses how to manage the disk image.

For information on installing a new Cumulus Linux disk image, refer to
[Installing a New Cumulus Linux
Image](/version/cumulus-linux-40/Installation-Management/Installing-a-New-Cumulus-Linux-Image).
For information on upgrading Cumulus Linux, refer to [Upgrading Cumulus
Linux](/version/cumulus-linux-40/Installation-Management/Upgrading-Cumulus-Linux).

## <span>Determine the Switch Platform</span>

To determine if your switch is on an x86 or ARM platform, run the `uname
-m` command.

For example, on an x86 platform, `uname -m` outputs *x86\_64*:

    cumulus@switch:~$ uname -m
     x86_64

On an ARM platform, `uname -m` outputs *armv7l*:

    cumulus@switch:~$ uname -m
     armv7l

You can also visit the HCL ([hardware compatibility
list](http://cumulusnetworks.com/support/linux-hardware-compatibility-list/))
to look at your hardware and determine the processor type.

## <span>Reprovision the System (Restart the Installer)</span>

Reprovisioning the system deletes all system data from the switch.

To start the provisioning and installation process, run the `onie-select
-i` command:

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

To remove all installed images and configurations, and return the switch
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

A reboot is required for the uninstallation process to begin.

{{%/notice%}}

{{%notice tip%}}

To cancel a pending uninstall operation, run the `onie-select -c`
command:

    cumulus@switch:~$ sudo onie-select -c
    Cancelling pending uninstall at next reboot...done.

{{%/notice%}}

## <span>Boot into Rescue Mode</span>

If your system becomes unresponsive is some way, you can correct certain
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

<span style="color: #36424a;"> The Cumulus Linux installation disk image
file is executable. From a running </span> switch, you can display,
extract, and verify the contents of the image file.

To display the contents of the Cumulus Linux image file, pass the `info`
option to the image file. For example, to display the contents of an
image file called `onie-installer` located in the
`/var/lib/cumulus/installer` directory:

    cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer info
    Verifying image checksum ...OK.
    Preparing image archive ... OK.
    Control File Contents
    =====================
    Description: Cumulus Linux 4.0.0
    Release: 4.0.0
    Architecture: amd64
    Switch-Architecture: bcm-amd64
    Build-Id: dirtyz224615f
    Build-Date: 2019-05-17T16:34:22+00:00
    Build-User: clbuilder
    Homepage: http://www.cumulusnetworks.com/
    Min-Disk-Size: 1073741824
    Min-Ram-Size: 536870912
    mkimage-version: 0.11.111_gbcf0

To extract the contents of the image file, use with the `extract <path>`
option. For example, to extract an image file called `onie-installer`
located in the `/var/lib/cumulus/installer` directory to the `mypath`
directory:

    cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer extract mypath
    total 181860
    -rw-r--r-- 1 4000 4000       308 May 16 19:04 control
    drwxr-xr-x 5 4000 4000      4096 Apr 26 21:28 embedded-installer
    -rw-r--r-- 1 4000 4000  13273936 May 16 19:04 initrd
    -rw-r--r-- 1 4000 4000   4239088 May 16 19:04 kernel
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

<span style="color: #36424a;"> </span>

## <span>Related Information</span>

[Open Network Install Environment (ONIE) Home
Page](http://opencomputeproject.github.io/onie/)

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
