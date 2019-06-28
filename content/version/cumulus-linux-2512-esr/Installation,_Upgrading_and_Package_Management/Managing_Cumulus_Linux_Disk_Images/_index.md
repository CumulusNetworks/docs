---
title: Managing Cumulus Linux Disk Images
author: Cumulus Networks
weight: 39
aliases:
 - /display/CL25ESR/Managing+Cumulus+Linux+Disk+Images
 - /pages/viewpage.action?pageId=5115988
pageID: 5115988
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
The Cumulus Linux operating system resides on a switch as a *disk
image*. Switches running Cumulus Linux can be configured with 2 separate
disk images. This section discusses how to manage them including
installation and upgrading.

## <span>Commands</span>

  - apt-get

  - cl-img-install

  - cl-img-select

  - cl-img-clear-overlay

  - cl-img-pkg

## <span id="src-5115988_ManagingCumulusLinuxDiskImages-new_image" class="confluence-anchor-link"></span><span>Installing a New Cumulus Linux Image</span>

For details, read the chapter, [Installing a New Cumulus Linux
Image](/version/cumulus-linux-2512-esr/Installation_Upgrading_and_Package_Management/Managing_Cumulus_Linux_Disk_Images/Installing_a_New_Cumulus_Linux_Image).

<span id="src-5115988_ManagingCumulusLinuxDiskImages-upgrade"></span>

## <span>Upgrading Cumulus Linux</span>

There are two ways you can upgrade Cumulus Linux:

  - Perform a binary (full image) install of the new version, running
    `cl-img-install` on the switch

  - Upgrade only the changed packages, using `apt-get update` and
    `apt-get dist-upgrade`

The entire upgrade process is described in [Upgrading Cumulus
Linux](/version/cumulus-linux-2512-esr/Installation_Upgrading_and_Package_Management/Managing_Cumulus_Linux_Disk_Images/Upgrading_Cumulus_Linux).

## <span id="src-5115988_ManagingCumulusLinuxDiskImages-slots" class="confluence-anchor-link"></span><span>Understanding Image Slots</span>

Cumulus Linux uses the concept of *image slots* to manage two separate
Cumulus Linux images. The important terminology for the slots is as
follows:

  - **Active image slot**: The currently running image slot.

  - **Primary image slot**: The image slot that is selected for the next
    boot. Often this is the same as the active image slot.

  - **Alternate image slot**: The inactive image slot, **not** selected
    for the next boot.

{{% imgOld 0 %}}

To identify which slot is active, which slot is the primary, and which
slot is alternate use the `cl-img-select` command:

    cumulus@switch$ sudo cl-img-select
    active => slot 1 (primary): 2.5.3-c4e83ad-201506011818-build
              slot 2 (alt    ): 2.5.2-727a0c6-201504132125-build

Slot 1 is the active slot, as indicated by the **active**. When the
switch is rebooted, it will boot into slot 1, as indicated by
**primary**. The **alternate** slot won't be booted into unless the user
selects it.

{{%notice note%}}

`cl-img-select` displays the version of the software that was
*initially* installed on the switch; if you've upgraded your switch,
`cl-img-select` won't display the most current version of Cumulus Linux
installed. The above switch had Cumulus Linux 2.5.3 installed initially
in slot 1, and Cumulus Linux 2.5.2 initially installed in slot 2.

To see the current version of Cumulus Linux running on the switch, use
cat /etc/lsb-release.

{{%/notice%}}

### <span>PowerPC vs x86 vs ARM Switches</span>

The characteristics of the image slots vary, based on whether your
switch is on a PowerPC, ARM or x86 platform. You can easily determine
which platform the switch is on by using the `uname -m` command.

For example, on a PowerPC platform, `uname -m` outputs *ppc*:

    cumulus@PPCswitch$ uname -m
     ppc

While on an x86 platform, `uname -m` outputs *x86\_64*:

    cumulus@x86switch$ uname -m
     x86_64

While on an ARM platform, `uname -m` outputs *armv7l*:

    cumulus@ARMswitch$ uname -m
     armv7l

You can also visit the HCL ([hardware compatibility
list](http://cumulusnetworks.com/support/linux-hardware-compatibility-list/))
to look at your hardware to determine the processor type.

### <span>PowerPC Image Slots</span>

Read more about PowerPC image slots

On the PowerPC platform, each image slot consists of a read-only Cumulus
Linux base image overlaid with a read-write user area, as shown in the
following diagram:

{{% imgOld 1 %}}

Files you edit and create reside in the read-write user overlay. This
also includes any additional software you install on top of Cumulus
Linux. After an install, the user overlay is empty.

#### <span>PowerPC Image Slot Overlay Detailed Information</span>

The root directory of an image slot on a PowerPC system is created using
an [overlayfs](https://lwn.net/Articles/447650/) file system. The lower
part of the overlay is a *read-only*
[squashfs](http://squashfs.sourceforge.net/) file system containing the
base Cumulus Linux image. The upper part of the overlay is a
*read-write* directory containing all the user modifications.

The following table describes the mount points and directories used to
create the overlay for image slots 1 and 2.

| Slot Number | R/O squashfs device | R/O mount point | R/W block device | R/W directory        |
| ----------- | ------------------- | --------------- | ---------------- | -------------------- |
| 1           | /dev/sysroot1       | /mnt/root-ro    | /dev/overlay\_rw | /mnt/root-rw/config1 |
| 2           | /dev/sysroot2       | /mnt/root-ro    | /dev/overlay\_rw | /mnt/root-rw/config2 |

{{%notice note%}}

A single read-write partition provides separate read-write directories
for the upper part of the overlay. The lower part of the overlay is a
**partition**, while the upper part is a **directory**.

{{%/notice%}}

The following table describes all the interesting mount points.

| Mount Point    | File System | Purpose                                                                |
| -------------- | ----------- | ---------------------------------------------------------------------- |
| /mnt/root-ro   | squashfs    | Contains the read-only base Cumulus Linux image.                       |
| /mnt/root-rw   | ext2        | Contains the read-write user directories for the overlay.              |
| /              | overlayfs   | The union of `/mnt/root-ro` and `/mnt/root-rw/config1` (or `config2`). |
| /mnt/persist   | ext2        | Contains the persistent user configuration applied to each image slot. |
| /mnt/initramfs | tmpfs       | Contains the `initramfs` used at boot. Needed during shutdown.         |

### <span>x86 and ARM Image Slots</span>

Read more about x86 image slots

Unlike PowerPC-based switches, there is no overlay for an x86-based or
ARM-based switch; instead each slot is a logical volume in the physical
partition, which you can manage with [LVM](https://wiki.debian.org/LVM).

When you install Cumulus Linux on an x86 or ARM switch, the following
entities are created on the disk:

  - A disk partition using an ext4 file system that contains three
    logical volumes: two logical volumes named *sysroot1* and
    *sysroot2*, and the `/mnt/persist` logical volume. The logical
    volumes represent the Cumulus Linux image slots, so sysroot1 is slot
    1 and sysroot2 is slot 2. `/mnt/persist` is where you store your
    [persistent
    configuration](Installing_a_New_Cumulus_Linux_Image.html#src-5115997_InstallingaNewCumulusLinuxImage-persistent_config).

  - A boot partition, shared by the logical volumes. Each volume mounts
    this partition as `/boot`.

#### <span>Managing Slot Sizes</span>

As space in a slot is used, you may need to increase the size of the
root filesystem by increasing the size of the corresponding logical
volume. This section shows you how to check current utilization and
expand the filesystem as needed.

1.  Check utilization on the root filesystem with the `df` command. In
    the following example, filesystem utilization is 16%:
    
        cumulus@switch$ df -h /
        Filesystem                                              Size  Used Avail Use% Mounted on
        /dev/disk/by-uuid/64650289-cebf-4849-91ae-a34693fce2f1  4.0G  579M  3.2G  16% /

2.  To increase available space in the root filesystem, first use the
    `vgs` command to check the available space in the volume group. In
    this example, there is 6.34 Gigabytes of free space available in the
    volume group CUMULUS:
    
        cumulus@switch$ sudo vgs
         VG      #PV #LV #SN Attr   VSize  VFree
         CUMULUS   1   3   0 wz--n- 14.36g 6.34g

3.  Once you confirm the available space, determine the number of the
    currently active slot using `cl-img-select`.
    
        cumulus@switch$ sudo cl-img-select | grep active
        active => slot 1 (primary): 2.5.0-199c587-201501081931-build
    
    `cl-img-select` indicates slot number 1 is active.

4.  Resize the slot with the `lvresize` command. The following example
    increases slot size by 20 percent of total available space. Replace
    the "\#" character in the example with the active slot number from
    the last step.
    
        cumulus@switch$ sudo lvresize -l +20%FREE CUMULUS/SYSROOT#
        Extending logical volume SYSROOT# to 5.27 GiB
        Logical volume SYSROOT# successfully resized
    
    {{%notice note%}}
    
    The use of + is very important with the `lvresize` command. Issuing
    `lvresize` without the + results in the logical volume size being
    set directly to the specified size, rather than extended.
    
    {{%/notice%}}

5.  Once the slot has been extended, use the `resize2fs` command to
    expand the filesystem to fit the new space in the slot. Again,
    replace the "\#" character in the example with the active slot
    number.
    
        cumulus@switch$ sudo resize2fs /dev/CUMULUS/SYSROOT#
        resize2fs 1.42.5 (29-Jul-2012)
        Filesystem at /dev/CUMULUS/SYSROOT# is mounted on /; on-line resizing required
        old_desc_blocks = 1, new_desc_blocks = 1
        Performing an on-line resize of /dev/CUMULUS/SYSROOT# to 1381376 (4k) blocks.
        The filesystem on /dev/CUMULUS/SYSROOT# is now 1381376 blocks long. 

#### <span>Accessing the Alternate Image Slot on x86 and ARM Platforms</span>

It may be useful to ****access the content of the alternate slot to
retrieve the configuration or logs.

{{%notice note%}}

`cl-img-install` fails while the alternate slot is mounted. It is
important to unmount the alternate slot as shown in step 4 below when
done.

{{%/notice%}}

1.  Determine which slot is the alternate with `cl-img-select`:
    
        cumulus@switch$ sudo cl-img-select
        active => slot 1 (primary): 2.5.3-c4e83ad-201506011818-build
                  slot 2 (alt    ): 2.5.2-727a0c6-201504132125-build
    
    This output indicates slot 2 is the alternate slot.

2.  Create a mount point for the alternate slot:
    
        cumulus@switch$ sudo mkdir /mnt/alt

3.  Mount the alternate slot to the mount point:
    
        cumulus@switch$ sudo mount /dev/mapper/CUMULUS-SYSROOT# /mnt/alt
    
    Where **\#** is the number of the alternate slot.
    
    The alternate slot is now accessible under `/mnt/alt`.

4.  Unmount the mount point `/mnt/alt` when done.
    
        cumulus@switch$ cd /
        cumulus@switch$ sudo umount /mnt/alt/

<span id="src-5115988_ManagingCumulusLinuxDiskImages-alt_slot"></span>

## <span>Reverting an Image to its Original Configuration (PowerPC Only)</span>

On PowerPC-based systems, you may want to clear out the read-write user
overlay area. Perhaps something was misconfigured, or was deleted by
mistake, or some unneeded software was installed.

You can purge the read-write overlay using the `cl-img-clear-overlay`
command, passing the slot number as an argument. For example, to purge
the read-write overlay for image slot 2, run:

    cumulus@switch:~$ sudo cl-img-clear-overlay 2
    Success: Overlay configuration 2 will be re-initialized during the next reboot.

{{%notice note%}}

You must reboot the switch to complete the purge.

{{%/notice%}}

## <span>Reprovisioning the System (Restart Installer)</span>

You can reprovision the system, wiping out the contents of both image
slots and `/mnt/persist`.

To initiate the provisioning and installation process, use
`cl-img-select -i`:

    cumulus@switch:~$ sudo cl-img-select -i
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
using `cl-img-select -c`:

    cumulus@switch:~$ sudo cl-img-select -c
    Cancelling pending install at next reboot...done.

{{%/notice%}}

## <span>Uninstalling All Images and Removing the Configuration</span>

To remove all installed images and configurations, returning the switch
to its factory defaults, use `cl-img-select -k`:

    cumulus@switch:~$ sudo cl-img-select -k
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
using `cl-img-select -c`:

    cumulus@switch:~$ sudo cl-img-select -c
    Cancelling pending uninstall at next reboot...done.

{{%/notice%}}

## <span>Booting into Rescue Mode</span>

If your system becomes broken is some way, you may be able to correct
things by booting into ONIE rescue mode. In rescue mode, the file
systems are unmounted and you can use various Cumulus Linux utilities to
try and fix the problem.

To reboot the system into the ONIE rescue mode, use `cl-img-select -r`:

    cumulus@switch:~$ sudo cl-img-select -r
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
by using `cl-img-select -c`:

``` 
cumulus@switch:~$ sudo cl-img-select -c
Cancelling pending rescue at next reboot...done.          
```

{{%/notice%}}

## <span>Inspecting Image File Contents</span>

From a running system you can display the contents of a Cumulus Linux
image file using `cl-img-pkg -d`:

    cumulus@switch:~$ sudo cl-img-pkg -d /var/lib/cumulus/installer/onie-installer
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

You can also extract the image files to the current directory with the
`-e` option:

    cumulus@switch:~$ sudo cl-img-pkg -e /var/lib/cumulus/installer/onie-installer
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

## <span>Useful Links</span>

  - [Open Network Install Environment (ONIE) Home
    Page](http://opencomputeproject.github.io/onie/)
