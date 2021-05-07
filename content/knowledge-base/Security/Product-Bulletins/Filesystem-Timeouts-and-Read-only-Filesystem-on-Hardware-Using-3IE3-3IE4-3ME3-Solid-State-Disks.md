---
title: Filesystem Timeouts and Read-only Filesystem on Hardware Using 3IE3 3IE4 3ME3 Solid State Disks
author: NVIDIA
weight: 431
toc: 4
---

Some SSD (solid-state disk or flash) drive models commonly used in network switches require the use of the TRIM command to function properly. By default, Cumulus Linux, like most other Linux distributions, does not enable TRIM. This command enables the operating system to keep the firmware up to date on empty areas of the drive to ensure that writes work correctly. Over time, without this notification, when extensive logging or debugging to the SSD is enabled, the firmware may take longer to perform write operations, which can in turn cause driver timeouts. These disk errors may eventually lead to the filesystem being mounted as read-only.

For customers running versions 3.0.0 through 3.7.3, Cumulus Networks is distributing a package to address this issue. Since these SSD drives are widespread in networking hardware, all customers using 3IE3, 3IE4 or 3ME3 SSDs should install this package. Customers without the affected SSDs will see no behavioral change. Installing the package should have no adverse effects. This functionality will be handled automatically by Cumulus Linux 3.7.4 and later.

## Issue Description

Recently, two SSD models — 3IE and 3ME — that were commonly used by manufacturers in embedded devices such as network switches were moved to End-of-Life/End-of-Sale status by the SSD manufacturer Innodisk. These models were replaced by the 3IE3, 3IE4 and 3ME3 SSDs. Although the 3IE3, 3IE4 and 3ME3 drives were thought by Innodisk to be "drop-in replacements" for the previous 3IE and 3ME drives, these drives require the ATA TRIM command to function properly, while the 3IE and 3ME drives did not.

Cumulus Linux, like most other Linux distributions, does not enable TRIM by default.

Using the TRIM command, the operating system can notify the SSD firmware which logical block addresses (LBAs) are free from the filesystem perspective so that the SSD controller can change the TRIMmed pages that map to these LBAs from VALID to INVALID.

When the SSD firmware detects that there are not enough FREE blocks on the SSD, the garbage collection feature on the SSD firmware converts INVALID pages to FREE blocks. Only pages that are marked as INVALID can be converted to FREE blocks.

On the 3IE3, 3IE4 and 3ME3 drives, with some firmware versions, the TRIM option is the only mechanism by which the operating system can notify the SSD firmware which LBAs are free. Without the TRIM command enabled on these drives, over time nearly every FREE block on the SSD will be filled with data and marked as VALID. This exhaustion of FREE blocks can cause the SSD firmware to shuffle data around the SSD to create a new FREE block for new data to be written. This is similar to defragmenting non-SSD drives. This process is time consuming and can result in disk driver timeouts in the operating system during disk writes, which can in turn cause the filesystem to be mounted as read-only.

## Environment

Cumulus Linux versions 3.0.0 through 3.7.3.

Cumulus Networks supports a large number of devices with 3IE3, 3IE4 and 3ME3 SSDs. To determine if you have the affected hardware, run:

    cumulus@switch:~$ ls /dev/disk/by-id | egrep '3ME3|3IE3|3IE4'

If the command has no output, then you aren't affected.

## Resolution

Cumulus Networks is distributing a package named `cumulus-trim` that is compatible with Cumulus Linux versions 3.0.0 through 3.7.3 that mitigates the potential for customer devices to encounter this failure. Cumulus Linux 3.7.4 and later releases will detect drives that require TRIM and enable the *discard* option when creating the `/etc/fstab` file during the installation of the network operating system. The `/etc/fstab` file will also be updated to enable the *discard* option when running `apt-get upgrade` to upgrade to Cumulus Linux 3.7.4 or later.

## Installation

To install the `cumulus-trim` package, run the following commands. Once installed, the package automatically executes and performs actions if it detects the affected drives.

    cumulus@switch:~$ sudo -E apt-get update
    cumulus@switch:~$ sudo -E apt-get install cumulus-trim

## Operation

The `cumulus-trim` package does the following if it detects a drive that requires the TRIM command:

- Executes the `/sbin/fstrim` command during the package installation to instruct the SSD firmware to mark pages associated with free LBAs as INVALID, making them eligible to be converted to FREE blocks.
- Creates a `cron` job to execute `/sbin/fstrim` every 6 hours to notify the SSD firmware of free LBAs, allowing the SSD to mark the associated physical block addresses (PBAs) as INVALID and eligible to be converted to FREE blocks.
- Modifies the `/etc/fstab` to enable the *discard* option on the SSD mount points. The *discard* option tells the filesystem layer of the operating system to send TRIM commands to the SSD firmware whenever a range of filesystem blocks is freed by the filesystem, such as when a file is deleted or partially overwritten with a smaller file.
- The next time the switch is booted after the package is installed, the *discard* option is detected as enabled, `/sbin/fstrim` is run one last time, and the `cron` job is then removed, as it is no longer necessary.
