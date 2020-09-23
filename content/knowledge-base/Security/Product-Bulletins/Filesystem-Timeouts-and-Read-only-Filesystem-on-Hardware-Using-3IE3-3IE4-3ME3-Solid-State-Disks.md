---
title: Filesystem Timeouts and Read-only Filesystem on Hardware Using 3IE3 3IE4 3ME3 Solid State Disks
author: Cumulus Networks
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

<!--
## Comments

- 
    
    <div id="comment_360002355193">
    
    <div class="comment-avatar">
    
    ![Avatar](https://secure.gravatar.com/avatar/29b1e874251ae5ea84c6666e000925a1?default=https%3A%2F%2Fassets.zendesk.com%2Fhc%2Fassets%2Fdefault_avatar.png&r=g)
    
    </div>
    
    <div class="comment-container">
    
    **drew mouw** <span class="comment-published">July 11, 2019
    15:43</span>
    
    <div class="comment-body markdown">
    
    certain ACCTON / Edgecore switches contain USB storage which is not
    able to perform the TRIM function and will eventually put the files
    system in read-only.
    
    the above command does not account for the USB drive, must run the
    following command to verify USB storage:
    
    smartctl -i /dev/sda
    
    output of affected systems:
    
    /dev/sda: Unknown USB bridge \[0x13fe:0x5200 (0x100)\]
    
    </div>
    
    <span class="comment-actions"> <span class="dropdown">
    <span class="dropdown-toggle" data-aria-label="Comment actions" data-aria-haspopup="true">Comment
    actions</span> <span class="dropdown-menu" data-role="menu">
    </span> </span>
    </span>
    
    </div>
    
    </div>

- 
    
    <div id="comment_360002400654">
    
    <div class="comment-container">
    
    **Peter Bratach** <span class="comment-published">July 15, 2019
    20:31</span>
    
    <div class="comment-body markdown">
    
    Thanks for letting us know, Drew. We didn't find this to be the case
    in our testing, where the Accton switches completely ignore both the
    fstrim command and discard in the mount options. This was our
    experience with the cumulus-trim package and btrfs.
    
    Can you let us know which model or models you've had to do this
    with? Thanks\!
    
    </div>
    
    <span class="comment-actions"> <span class="dropdown">
    <span class="dropdown-toggle" data-aria-label="Comment actions" data-aria-haspopup="true">Comment
    actions</span> <span class="dropdown-menu" data-role="menu">
    </span> </span>
    </span>
    
    </div>
    
    </div>

- 
    
    <div id="comment_360003342194">
    
    <div class="comment-avatar">
    
    ![Avatar](https://secure.gravatar.com/avatar/4a6e34d98a87309dfb33a2857cc6ca08?default=https%3A%2F%2Fassets.zendesk.com%2Fhc%2Fassets%2Fdefault_avatar.png&r=g)
    
    </div>
    
    <div class="comment-container">
    
    **Rob Stevens** <span class="comment-published">October 30, 2019
    21:47</span>
    
    <div class="comment-body markdown">
    
    How do you recover if your filesystem has already been marked
    read-only?
    
    </div>
    
    <span class="comment-actions"> <span class="dropdown">
    <span class="dropdown-toggle" data-aria-label="Comment actions" data-aria-haspopup="true">Comment
    actions</span> <span class="dropdown-menu" data-role="menu">
    </span> </span>
    </span>
    
    </div>
    
    </div>

- 
    
    <div id="comment_360003337953">
    
    <div class="comment-avatar comment-avatar-agent">
    
    ![Avatar](https://support.cumulusnetworks.com/system/photos/0001/1366/9073/profilepic.jpg)
    
    </div>
    
    <div class="comment-container">
    
    **Peter Bratach** <span class="comment-published">October 31, 2019
    16:26</span>
    
    <div class="comment-body markdown">
    
    Hi Rob, the first thing to do is to try rebooting (at a time when
    it's OK if the switch doesn't come up to a usable state) into single
    user mode\[1\], and then, if it's a drive that supports and requires
    TRIM, running \`fstrim -v /\`. If you can't even boot to single user
    mode (rescue mode), then the drive is probably shot, and it's not
    TRIM related.
    
    1\.
    <https://docs.cumulusnetworks.com/cumulus-linux/Monitoring-and-Troubleshooting/Single-User-Mode-Password-Recovery/>
    
    </div>
    
    <span class="comment-actions"> <span class="dropdown">
    <span class="dropdown-toggle" data-aria-label="Comment actions" data-aria-haspopup="true">Comment
    actions</span> <span class="dropdown-menu" data-role="menu">
    </span> </span>
    </span>
    
    </div>
    
    </div>

- 
    
    <div id="comment_360003337993">
    
    <div class="comment-avatar comment-avatar-agent">
    
    ![Avatar](https://support.cumulusnetworks.com/system/photos/0001/1366/9073/profilepic.jpg)
    
    </div>
    
    <div class="comment-container">
    
    **Peter Bratach** <span class="comment-published">October 31, 2019
    16:29</span>
    
    <div class="comment-body markdown">
    
    Moreover, you can't assume that a read-only state is due to the TRIM
    behavior. Cumulus support often sees read-only states happen when
    the drive is hosed for other reasons — the drive is worn or faulty
    and so forth.
    
    In theory you can try to remount the filesystem as read-write using
    ​\`sudo mount -o remount,rw \`, but if the drive is hosed then all
    you can really do is power cycle and hope it comes back. Ideally
    you'll be able to get things like syslog and kernel logs before
    power cycling, so you can check if there's anything logged that
    might give an indication as to what caused the read-only remount.
    
    </div>
    
    <span class="comment-actions"> <span class="dropdown">
    <span class="dropdown-toggle" data-aria-label="Comment actions" data-aria-haspopup="true">Comment
    actions</span> <span class="dropdown-menu" data-role="menu">
    </span> </span>
</span>
    
    </div>
    
    </div> -->
