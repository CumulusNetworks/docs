---
title: Filesystem Timeouts and Read-only Filesystem on Hardware Using 3IE3 3IE4 3ME3 Solid State Disks
author: NVIDIA
weight: 431
toc: 4
---

Some SSD (solid-state disk or flash) drive models commonly used in network switches require the use of the TRIM command to function properly. By default, Cumulus Linux, like most other Linux distributions, does not enable TRIM. This command enables the operating system to keep the firmware up to date on empty areas of the drive to ensure that writes work correctly. Over time, without this notification, when you enable extensive logging or debugging to the SSD, the firmware might take longer to perform write operations, which can in turn cause driver timeouts. These disk errors might eventually lead to the filesystem mounting as read-only.

For customers running versions 3.0.0 through 3.7.3, NVIDIA is distributing a package to address this issue. Because these SSD drives are widespread in networking hardware, all customers using 3IE3, 3IE4 or 3ME3 SSDs should install this package. Customers without the affected SSDs should see no behavioral change. Installing the package should have no adverse effects. Cumulus Linux 3.7.4 and later handles this functionality automatically.

## Issue Description

Recently, two SSD models — 3IE and 3ME — that manufacturers commonly used in embedded devices such as network switches moved to End-of-Life/End-of-Sale status by the SSD manufacturer Innodisk. The 3IE3, 3IE4 and 3ME3 SSDs replaced these models. Although Innodisk considered the 3IE3, 3IE4 and 3ME3 drives to be "drop-in replacements" for the previous 3IE and 3ME drives, these drives require the ATA TRIM command to function properly, while the 3IE and 3ME drives did not.

Cumulus Linux, like most other Linux distributions, does not enable TRIM by default.

Using the TRIM command, the operating system can notify the SSD firmware which logical block addresses (LBAs) are free from the filesystem perspective so that the SSD controller can change the TRIMmed pages that map to these LBAs from VALID to INVALID.

When the SSD firmware detects that there are not enough FREE blocks on the SSD, the garbage collection feature on the SSD firmware converts INVALID pages to FREE blocks. The SSD firmware can convert only the pages that marked as INVALID to FREE blocks.

On the 3IE3, 3IE4 and 3ME3 drives, with some firmware versions, the TRIM option is the only mechanism by which the operating system can notify the SSD firmware which LBAs are free. Without the TRIM command enabled on these drives, over time nearly every FREE block on the SSD gets filled with data and marked as VALID. This exhaustion of FREE blocks can cause the SSD firmware to shuffle data around the SSD to create a new FREE block where it can write new data. This is similar to defragmenting non-SSD drives. This process is time consuming and can result in disk driver timeouts in the operating system during disk writes, which can in turn cause the filesystem to mount as read-only.

## Environment

Cumulus Linux versions 3.0.0 through 3.7.3.

NVIDIA supports a large number of devices with 3IE3, 3IE4 and 3ME3 SSDs. To determine if you have the affected hardware, run:

    cumulus@switch:~$ ls /dev/disk/by-id | egrep '3ME3|3IE3|3IE4'

If the command has no output, then you are not affected.

## Resolution

NVIDIA is distributing a package named `cumulus-trim` that is compatible with Cumulus Linux versions 3.0.0 through 3.7.3 that mitigates the potential for customer devices to encounter this failure. Cumulus Linux 3.7.4 and later releases detect drives that require TRIM and enable the *discard* option when creating the `/etc/fstab` file during the installation of the network operating system. The `/etc/fstab` file also enables the *discard* option when running `apt-get upgrade` to upgrade to Cumulus Linux 3.7.4 or later.

## Installation

To install the `cumulus-trim` package, run the following commands. After the installation finishes, the package automatically executes and performs actions if it detects the affected drives.

    cumulus@switch:~$ sudo -E apt-get update
    cumulus@switch:~$ sudo -E apt-get install cumulus-trim

## Operation

The `cumulus-trim` package does the following if it detects a drive that requires the TRIM command:

- Executes the `/sbin/fstrim` command during the package installation to instruct the SSD firmware to mark pages associated with free LBAs as INVALID, making them eligible for conversion to FREE blocks.
- Creates a `cron` job to execute `/sbin/fstrim` every 6 hours to notify the SSD firmware of free LBAs, allowing the SSD to mark the associated physical block addresses (PBAs) as INVALID and eligible for conversion to FREE blocks.
- Modifies the `/etc/fstab` to enable the *discard* option on the SSD mount points. The *discard* option tells the filesystem layer of the operating system to send TRIM commands to the SSD firmware whenever the filesystem frees a range of filesystem blocks, such as when someone deletes or partially overwrites a file with a smaller file.
- The next time the switch boots after the package installation, the switch detects the *discard* option as enabled, then runs `/sbin/fstrim` one last time. It then removes the `cron` job, as it is no longer necessary.
