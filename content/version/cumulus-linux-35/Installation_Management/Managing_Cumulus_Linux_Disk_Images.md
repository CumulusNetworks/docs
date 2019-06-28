---
title: Managing Cumulus Linux Disk Images
author: Cumulus Networks
weight: 41
aliases:
 - /display/CL35/Managing+Cumulus+Linux+Disk+Images
 - /pages/viewpage.action?pageId=8357414
pageID: 8357414
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
The Cumulus Linux operating system resides on a switch as a *disk
image*. This section discusses how to manage the image, including
installation and upgrading.

## <span id="src-8357414_ManagingCumulusLinuxDiskImages-new_image" class="confluence-anchor-link"></span><span>Installing a New Cumulus Linux Image</span>

For details, read the chapter, [Installing a New Cumulus Linux
Image](/version/cumulus-linux-35/Installation_Management/Installing_a_New_Cumulus_Linux_Image).

## <span id="src-8357414_ManagingCumulusLinuxDiskImages-upgrade" class="confluence-anchor-link"></span><span>Upgrading Cumulus Linux</span>

There are two ways you can upgrade Cumulus Linux:

  - Upgrading only the changed packages, using `apt-get update` and
    `apt-get upgrade`. **This is the preferred method.**

  - Perform a binary (full image) install of the new version, using
    [ONIE](http://opencomputeproject.github.io/onie/). This is used when
    moving between major versions or if you want to install a clean
    image.

The entire upgrade process is described in [Upgrading Cumulus
Linux](/version/cumulus-linux-35/Installation_Management/Upgrading_Cumulus_Linux).

## <span>x86 vs ARM Switches</span>

You can easily determine whether your switch is on an x86 or ARM
platform by using the `uname -m` command.

For example, on an x86 platform, `uname -m` outputs *x86\_64*:

    cumulus@x86switch$ uname -m
     x86_64

While on an ARM platform, `uname -m` outputs *armv7l*:

    cumulus@ARMswitch$ uname -m
     armv7l

You can also visit the HCL ([hardware compatibility
list](http://cumulusnetworks.com/support/linux-hardware-compatibility-list/))
to look at your hardware to determine the processor type.

## <span>Reprovisioning the System (Restart Installer)</span>

You can reprovision the system, wiping out the contents of the whole
switch.

To initiate the provisioning and installation process, use `onie-select
-i`:

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

If you change your mind, you can cancel a pending reinstall operation by
using `onie-select -c`:

    cumulus@switch:~$ sudo onie-select -c
    Cancelling pending install at next reboot...done.

{{%/notice%}}

## <span>Uninstalling All Images and Removing the Configuration</span>

To remove all installed images and configurations, returning the switch
to its factory defaults, use `onie-select -k`:

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

If you change your mind you can cancel a pending uninstall operation by
using `onie-select -c`:

    cumulus@switch:~$ sudo onie-select -c
    Cancelling pending uninstall at next reboot...done.

{{%/notice%}}

## <span>Booting into Rescue Mode</span>

If your system becomes broken is some way, you may be able to correct
things by booting into ONIE rescue mode. In rescue mode, the file
systems are unmounted and you can use various Cumulus Linux utilities to
try and fix the problem.

To reboot the system into the ONIE rescue mode, use `onie-select -r`:

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

If you change your mind you can cancel a pending rescue boot operation
by using `onie-select -c`:

    cumulus@switch:~$ sudo onie-select -c
    Cancelling pending rescue at next reboot...done.

{{%/notice%}}

## <span>Inspecting Image File Contents</span>

The Cumulus Linux installation disk image file is executable. From a
running switch, you can display the contents of the Cumulus Linux image
file by passing the `info` option to the image file. For example, if the
image file is called `onie-installer` and is located in
`/var/lib/cumulus/installer`, you can get information about the disk
image by running:

    cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer info
    Verifying image checksum ... OK.
    Preparing image archive ... OK.
    Control File Contents
    =====================
    Description: Cumulus Linux
    OS-Release: 2.1.0-0556262-201406101128-NB
    Architecture: amd64
    Date: Tue, 10 Jun 2014 11:44:28 -0700
    Installer-Version: 1.2
    Platforms: im_n29xx_t40n mlx_sx1400_i73612 dell_s6000_s1220
    Homepage: http://www.cumulusnetworks.com/
     
    Data Archive Contents
    =====================
           128 2014-06-10 18:44:26 file.list
            44 2014-06-10 18:44:27 file.list.sha1
     104276331 2014-06-10 18:44:27 sysroot-internal.tar.gz
            44 2014-06-10 18:44:27 sysroot-internal.tar.gz.sha1
       5391348 2014-06-10 18:44:26 vmlinuz-initrd.tar.xz
            44 2014-06-10 18:44:27 vmlinuz-initrd.tar.xz.sha1
    cumulus@switch:~$

You can also extract the contents of the image file by passing the
`extract` option to the image file:

    cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer extract PATH
    Verifying image checksum ... OK.
    Preparing image archive ... OK.
    file.list
    file.list.sha1
    sysroot-internal.tar.gz
    sysroot-internal.tar.gz.sha1
    vmlinuz-initrd.tar.xz
    vmlinuz-initrd.tar.xz.sha1
    Success: Image files extracted OK.
    cumulus@switch:~$ sudo ls -l
    total 107120
    -rw-r--r-- 1 1063 3000       128 Jun 10 18:44 file.list
    -rw-r--r-- 1 1063 3000        44 Jun 10 18:44 file.list.sha1
    -rw-r--r-- 1 1063 3000 104276331 Jun 10 18:44 sysroot-internal.tar.gz
    -rw-r--r-- 1 1063 3000        44 Jun 10 18:44 sysroot-internal.tar.gz.sha1
    -rw-r--r-- 1 1063 3000   5391348 Jun 10 18:44 vmlinuz-initrd.tar.xz
    -rw-r--r-- 1 1063 3000        44 Jun 10 18:44 vmlinuz-initrd.tar.xz.sha1 

Finally, you can verify the contents of the image file by passing the
`verify` option to the image file:

    cumulus@switch:~$ sudo /var/lib/cumulus/installer/onie-installer verify
    Verifying image checksum ... OK.
    Preparing image archive ... OK.
    file.list
    file.list.sha1
    sysroot-internal.tar.gz
    sysroot-internal.tar.gz.sha1
    vmlinuz-initrd.tar.xz
    vmlinuz-initrd.tar.xz.sha1
    Success: Image files extracted OK.
    cumulus@switch:~$ sudo ls -l
    total 107120
    -rw-r--r-- 1 1063 3000       128 Jun 10 18:44 file.list
    -rw-r--r-- 1 1063 3000        44 Jun 10 18:44 file.list.sha1
    -rw-r--r-- 1 1063 3000 104276331 Jun 10 18:44 sysroot-internal.tar.gz
    -rw-r--r-- 1 1063 3000        44 Jun 10 18:44 sysroot-internal.tar.gz.sha1
    -rw-r--r-- 1 1063 3000   5391348 Jun 10 18:44 vmlinuz-initrd.tar.xz
    -rw-r--r-- 1 1063 3000        44 Jun 10 18:44 vmlinuz-initrd.tar.xz.sha1 

## <span>Related Information</span>

  - [Open Network Install Environment (ONIE) Home
    Page](http://opencomputeproject.github.io/onie/)
