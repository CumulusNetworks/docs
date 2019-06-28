---
title: Managing Cumulus RMP Disk Images
author: Cumulus Networks
weight: 131
aliases:
 - /display/RMP25ESR/Managing+Cumulus+RMP+Disk+Images
 - /pages/viewpage.action?pageId=5116319
pageID: 5116319
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
The Cumulus RMP operating system resides on a switch as a *disk image*.
Switches running Cumulus RMP can be configured with multiple disk
images. This section discusses how to manage them.

## <span>Commands</span>

  - cl-img-install

  - cl-img-select

  - cl-img-pkg

## <span id="src-5116319_ManagingCumulusRMPDiskImages-upgrade" class="confluence-anchor-link"></span><span>Upgrading Cumulus RMP</span>

If you already have Cumulus RMP installed on your switch and you are
upgrading to an X.Y.Z release, like 2.5.7 from an earlier release in the
same major and minor release family **only** (like 2.5.4 to 2.5.7), you
can use `apt-get` to upgrade to the new version. (If are upgrading to a
major (X.0) or minor (X.Y) release, you must do a full image install, as
described in [Installing a New Cumulus RMP
Image](#src-5116319_ManagingCumulusRMPDiskImages-new_image) below.)

To upgrade to a maintenance (X.Y.Z) release using `apt-get`:

1.  Run `apt-get update`.

2.  Run `apt-get dist-upgrade`.

3.  Reboot the switch.

{{%notice warning%}}

While this method doesn't overwrite the target image slot, the disk
image does occupy a lot of disk space used by both Cumulus RMP image
slots.

{{%/notice%}}

## <span id="src-5116319_ManagingCumulusRMPDiskImages-new_image" class="confluence-anchor-link"></span><span>Installing a New Cumulus RMP Image</span>

Cumulus RMP comes preinstalled on your switch. However there may be
instances where you need to perform a full image installation. Before
you install Cumulus RMP, the switch can be in two different states:

  - The switch [already has Cumulus RMP
    installed](#src-5116319_ManagingCumulusRMPDiskImages-alreadyinstalled)
    on it (see
    [below](#src-5116319_ManagingCumulusRMPDiskImages-alreadyinstalled)).

  - The switch has no image on it (so the switch is only running
    [ONIE](http://www.onie.org/)) or a clean installation is desired. In
    which case, you would install Cumulus RMP in one of the following
    ways:
    
      - Using [USB](#src-5116319_ManagingCumulusRMPDiskImages-usb) (see
        [below](#src-5116319_ManagingCumulusRMPDiskImages-usb)).
    
      - For all other ONIE installation methods, refer to [this
        knowledge base
        article](https://support.cumulusnetworks.com/hc/en-us/articles/203771426-Using-ONIE-to-Install-Cumulus-Linux).

{{%notice tip%}}

[ONIE](http://www.onie.org/) is an open source project, equivalent to
PXE on servers, that allows installation of network operating systems
(NOS) on bare metal switches.

{{%/notice%}}

Unlike Cumulus Linux, there is no license to install on a Cumulus RMP
switch.

### <span id="src-5116319_ManagingCumulusRMPDiskImages-alreadyinstalled" class="confluence-anchor-link"></span><span>Installing a New Image when Cumulus RMP Is already Installed</span>

Follow these upgrade steps for both major and minor releases, where:

  - A major release upgrade is 2.X.X to 3.X.X (like 2.5.7 to 3.0.0)

  - A minor release upgrade is X.2.X to X.3.X (like 2.5.4 to 2.5.7)

Installing a new image is a six step process:

1.  Installing the new image into the alternate image slot (see
    [below](#src-5116319_ManagingCumulusRMPDiskImages-slots)).

2.  Backing up your configuration files into `/mnt/persist`.

3.  Selecting the alternate slot for next boot (that is, the slot you
    just installed into).

4.  Rebooting the switch.

5.  Copying the files from `/mnt/persist` to the new slot; this happens
    automatically if you follow the instructions below.

6.  Clearing `/mnt/persist` out so subsequent reboots don't load
    `/mnt/persist`.

{{% imgOld 0 %}}

{{%notice warning%}}

Installing a new image overwrites **all files** — including
configuration files — on the target slot. Cumulus Networks strongly
recommends you create a [persistent
configuration](#src-5116319_ManagingCumulusRMPDiskImages-persistent_config)
to back up your important files, like your configurations; see Step 2
below.

{{%/notice%}}

### <span>Step 1: Installing the New Image</span>

Use the `cl-img-install` command to ****install a new image into the
**alternate** image slot.

{{%notice note%}}

You can only install into the alternate slot, as it is not possible to
install into the actively running slot. The system automatically
determines which slot is the alternate slot (slot 2 in this case).

{{%/notice%}}

This example assumes the new image is located in the current directory
(where the user is running the command from):

    cumulus@switch:~$ sudo cl-img-install CumulusRMP-2.5.7-amd64.bin

Click to expand full output

    cumulus@switch$ sudo cl-img-install CumulusRMP-2.5.7-amd64.bin
    Defaulting to image slot 2 for install.
    Dumping image info from CumulusRMP-2.5.7-amd64.bin ...
    Verifying image checksum ... OK.
    Preparing image archive ... OK.
    Control File Contents
    =====================
    Description: Cumulus RMP
    OS-Release: 2.5.7-3b46bef-201509041633-build
    Architecture: amd64
    Date: Fri, 04 Sep 2015 17:10:30 -0700
    Installer-Version: 1.2
    Platforms: accton_as5712_54x accton_as6712_32x mlx_sx1400_i73612 dell_s6000_s1220 dell_s4000_c2338 dell_s3000_c2338 cel_redstone_xp cel_smallstone_xp cel_pebble quanta_panther quanta_ly8_rangeley quanta_ly6_rangeley quanta_ly9_rangeley
    Homepage: http://www.cumulusnetworks.com/
    Data Archive Contents
    =====================
    -rw-r--r-- build/Development       131 2015-09-05 00:10:29 file.list
    -rw-r--r-- build/Development        44 2015-09-05 00:10:29 file.list.sha1
    -rw-r--r-- build/Development 140238619 2015-09-05 00:10:29 sysroot-release.tar.gz
    -rw-r--r-- build/Development        44 2015-09-05 00:10:30 sysroot-release.tar.gz.sha1
    -rw-r--r-- build/Development   8094220 2015-09-05 00:10:29 vmlinuz-initrd.tar.xz
    -rw-r--r-- build/Development        44 2015-09-05 00:10:30 vmlinuz-initrd.tar.xz.sha1
    Current image slot setup:
    active => slot 1 (primary): 2.5.7-c4e83ad-201506011818-build
              slot 2 (alt    ): 2.5.4-727a0c6-201504132125-build
    About to update image slot 2 using:
    /home/cumulus/CumulusRMP-2.5.7-amd64.bin
    Are you sure (y/N)? y
    Verifying image checksum ... OK.
    Preparing image archive ... OK.
    Validating sha1 for vmlinuz-initrd.tar.xz... done.
    Validating sha1 for sysroot-release.tar.gz... done.
    Installing OS-Release 2.5.7-3b46bef-201509041633-build into image slot 2 ...
    Info: Copying sysroot into slot 2
    Creating logical volume SYSROOT2 on volume group CUMULUS... done.
    Verifying sysroot copy... OK.
    Copying kernel into CLBOOT partition... done.
    Verifying kernel copy... OK.
    Generating grub.cfg ...
    Found Cumulus RMP image: /boot/cl-vmlinuz-3.2.65-1+deb7u2+cl2.5+5-slot-1
    Found Cumulus RMP image: /boot/cl-vmlinuz-3.2.65-1+deb7u2+cl2.5+5-slot-2
    done
    Success: /home/cumulus/CumulusRMP-2.5.7-amd64.bin loaded into image slot 2.

### <span id="src-5116319_ManagingCumulusRMPDiskImages-persistent_config" class="confluence-anchor-link"></span><span>Step 2: Backing up Your Configuration Files into /mnt/persist </span>

Any files that have been modified from the factory default should be
backed up to `/mnt/persist`.

#### <span>Recommended Files to Make Persistent</span>

Cumulus Networks recommends you consider making the following files and
directories part of a persistent configuration.

**Network Configuration Files**

| File Name and Location  | Explanation                                                         | Cumulus RMP Documentation                                                                                                                                                                 | Debian Documentation                                                                                                         |
| ----------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| /etc/network/           | Network configuration files, most notably `/etc/network/interfaces` | [Configuring and Managing Network Interfaces](/version/cumulus-rmp-2512-esr/Configuring_and_Managing_Network_Interfaces/)                                                                 | [wiki.debian.org/NetworkConfiguration](https://wiki.debian.org/NetworkConfiguration)                                         |
| /etc/resolv.conf        | DNS resolution                                                      | Not unique to Cumulus RMP: [wiki.debian.org/NetworkConfiguration\#The\_resolv.conf\_configuration\_file](https://wiki.debian.org/NetworkConfiguration#The_resolv.conf_configuration_file) | [www.debian.org/doc/manuals/debian-reference/ch05.en.html](https://www.debian.org/doc/manuals/debian-reference/ch05.en.html) |
| /etc/hostname           | Configuration file for the hostname of the switch                   | [Quick Start Guide\#ConfiguringtheHostnameandTimeZone](Quick_Start_Guide.html#src-5116307_QuickStartGuide-ConfiguringtheHostnameandTimeZone)                                              | [wiki.debian.org/HowTo/ChangeHostname](https://wiki.debian.org/HowTo/ChangeHostname)                                         |
| /etc/cumulus/ports.conf | Breakout cable configuration file                                   | [Configuring Switch Port Attributes\#ConfiguringBreakoutPorts](Configuring_Switch_Port_Attributes.html#src-5116358_ConfiguringSwitchPortAttributes-ConfiguringBreakoutPorts)              | N/A; please read the guide on breakout cables                                                                                |

**Additional Commonly Used Files**

| File Name and Location | Explanation                                              | Cumulus RMP Documentation                                                                                                                                                  | Debian Documentation                                                                                                         |
| ---------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| /etc/motd              | Message of the day                                       | Not unique to Cumulus RMP                                                                                                                                                  | [wiki.debian.org/motd\#Wheezy](https://wiki.debian.org/motd#Wheezy)                                                          |
| /etc/passwd            | User account information                                 | Not unique to Cumulus RMP                                                                                                                                                  | [www.debian.org/doc/manuals/debian-reference/ch04.en.html](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html) |
| /etc/shadow            | Secure user account information                          | Not unique to Cumulus RMP                                                                                                                                                  | [www.debian.org/doc/manuals/debian-reference/ch04.en.html](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html) |
| /etc/lldpd.conf        | Link Layer Discover Protocol (LLDP) daemon configuration | [Link Layer Discovery Protocol](/version/cumulus-rmp-2512-esr/Layer_1_and_Layer_2_Features/Link_Layer_Discovery_Protocol)                                                  | [packages.debian.org/wheezy/lldpd](https://packages.debian.org/wheezy/lldpd)                                                 |
| /etc/lldpd.d/          | Configuration directory for `lldpd`                      | [Link Layer Discovery Protocol](/version/cumulus-rmp-2512-esr/Layer_1_and_Layer_2_Features/Link_Layer_Discovery_Protocol)                                                  | [packages.debian.org/wheezy/lldpd](https://packages.debian.org/wheezy/lldpd)                                                 |
| /etc/nsswitch.conf     | Name Service Switch (NSS) configuration file             | [LDAP Authentication and Authorization](/version/cumulus-rmp-2512-esr/System_Management/Authentication_Authorization_and_Accounting/LDAP_Authentication_and_Authorization) | [wiki.debian.org/LDAP/NSS](https://wiki.debian.org/LDAP/NSS)                                                                 |
| /etc/ssh/              | SSH configuration files                                  | [SSH for Remote Access](/version/cumulus-rmp-2512-esr/System_Management/Authentication_Authorization_and_Accounting/SSH_for_Remote_Access)                                 | [wiki.debian.org/SSH](https://wiki.debian.org/SSH)                                                                           |
| /etc/ldap/ldap.conf    | Lightweight Directory Access Protocol configuration file | [LDAP Authentication and Authorization](/version/cumulus-rmp-2512-esr/System_Management/Authentication_Authorization_and_Accounting/LDAP_Authentication_and_Authorization) | [www.debian.org/doc/manuals/debian-reference/ch04.en.html](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html) |

  - If you are using the root user account, consider including `/root/`.

  - If you have custom user accounts, consider including
    `/home/<username>/`.

#### <span>Simple Bash Script Example</span>

Example Bash script to automate /mnt/persist backup; click to expand...

The following script is a Bash script that can help grab all the above
files and push them to `/mnt/persist` automatically.

    #!/bin/bash
    #network configuration files
    cp -r --parents /etc/network/ /mnt/persist/
    cp --parents /etc/resolv.conf /mnt/persist/
    if [ -f /etc/quagga/Quagga.conf ]; then cp --parents /etc/quagga/Quagga.conf /mnt/persist; fi
    cp --parents /etc/quagga/daemons /mnt/persist
    cp --parents /etc/hostname /mnt/persist
    cp --parents /etc/cumulus/ports.conf /mnt/persist
     
    #commonly used filed
    cp --parents /etc/motd /mnt/persist/
    cp --parents /etc/passwd /mnt/persist/
    cp --parents /etc/shadow /mnt/persist/
    if [ -f /etc/lldpd.conf ]; then cp --parents /etc/lldpd.conf /mnt/persist/; fi
    cp -r --parents /etc/lldpd.d/* /mnt/persist/
    cp --parents /etc/nsswitch.conf /mnt/persist
    cp -a --parents /etc/ssh/ /mnt/persist/
    if [ -f /etc/ldap.conf ]; then cp --parents /etc/ldap.conf /mnt/persist; fi

To run the script copy the above into a `.sh` file (for example, `sudo
nano backup.sh`).

    cumulus@switch$ bash backup.sh

To check if the script worked use the Linux `tree` command:

    cumulus@switch$ tree /mnt/persist
    /mnt/persist
    `-- etc
        |-- cumulus
        |   `-- ports.conf
        |-- hostname
        |-- lldpd.d
        |   `-- README.conf
        |-- motd
        |-- network
        |   |-- if-down.d
        |   |-- if-post-down.d
        |   |-- if-post-up.d
        |   |-- if-pre-down.d
        |   |-- if-pre-up.d
        |   |   `-- ethtool
        |   |-- if-up.d
        |   |   |-- ethtool
        |   |   |-- mountnfs
        |   |   `-- openssh-server
        |   |-- ifupdown2
        |   |   `-- ifupdown2.conf
        |   |-- interfaces
        |   |-- interfaces.d
        |   `-- run -> /run/network
        |-- nsswitch.conf
        |-- passwd
        |-- quagga
        |   |-- Quagga.conf
        |   `-- daemons
        |-- resolv.conf
        |-- shadow
        `-- ssh
            |-- moduli
            |-- ssh_config
            |-- ssh_host_dsa_key
            |-- ssh_host_dsa_key.pub
            |-- ssh_host_ecdsa_key
            |-- ssh_host_ecdsa_key.pub
            |-- ssh_host_rsa_key
            |-- ssh_host_rsa_key.pub
            `-- sshd_config

### <span>Step 3: Selecting the Alternate Slot for Next Boot</span>

To select the slot you just installed into, either use `cl-img-select
-s` to switch the primary slot to the alternate slot, or use
`cl-img-select` with the number of the slot you want directly (for
example, `cl-img-select 2`).

    cumulus@switch$ sudo cl-img-select -s
    Success: Primary image slot set to 2.
    active => slot 1 (alt    ): 2.5.7-c4e83ad-201506011818-build
              slot 2 (primary): 2.5.6-3b46bef-201509041633-build
    Reboot required to take effect.

### <span>Step 4: Rebooting the Switch</span>

Reboot the switch to boot into the new primary slot.

    cumulus@switch$ reboot

### <span>Step 5: Copying the Files from /mnt/persist to the New Slot </span>

Files in `/mnt/persist` automatically are rolled into the primary image
slot when the switch boots. For example, in this scenario everything in
`/mnt/persist` gets automatically copied into slot 2 when the reboot is
performed in step 4 above. The files in `/mnt/persist` keep their
relative path after the reboot. For example, if there was a
`/mnt/persist/etc/network/interfaces`, it would be copied into
`/etc/network/interfaces`.

Use the tree command to look at the folder structure of `/mnt/`.

    cumulus@switch$ tree /mnt/
    /mnt
    `-- persist
        `-- etc
            `-- network
                `-- interfaces

So in this case `/mnt/persist/etc/network/interfaces` overrides the
primary slot's `/etc/network/interfaces` on boot.

### <span>Step 6: Clearing /mnt/persist </span>

If `/mnt/persist` is not cleared out, everything in `/mnt/persist` will
overwrite any relative files in the primary slot whenever the switch
boots. This can be a problem is a user modifies some files but forgets
to also make the changes to `/mnt/persist`. It is best practice to clear
out `/mnt/persist` so that any subsequent users can make changes and not
have them overwritten the next time the switch boots.

    cumulus@switch$ sudo rm -r /mnt/persist/*
    cumulus@switch$ ls /mnt/persist/
    cumulus@switch$

{{%notice warning%}}

This is an extra reminder to clear out `/mnt/persist`. A future reboot
will cause **everything** in `/mnt/persist` to overwrite the current
primary slot.

{{%/notice%}}

### <span id="src-5116319_ManagingCumulusRMPDiskImages-usb" class="confluence-anchor-link"></span><span>Full Installation of Cumulus RMP Using ONIE over USB</span>

Follow the steps below to conduct a full installation of Cumulus RMP.
This wipes out all pre-existing configuration files that may be present
on the switch.

{{%notice note%}}

Make sure to back up any important configuration files that you may need
to restore the configuration of your switch after the installation
finishes.

{{%/notice%}}

#### <span>Preparing for USB Installation</span>

1.  Download the appropriate Cumulus RMP image for your x86 platform
    from the [Cumulus Downloads
    page](http://cumulusnetworks.com/downloads/).

2.  Prepare your flash drive by formatting in one of the supported
    formats: FAT32, vFAT or EXT2.
    
    Optional: Preparing a USB Drive inside Cumulus Linux
    
    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td><p>{{%notice warning%}}</p>
    <p>It is possible that you could severely damage your system with the following utilities, so please use caution when performing the actions below!</p>
    <p>{{%/notice%}}</p>
    <ol>
    <li><p>Insert your flash drive into the USB port on the switch running Cumulus RMP and log in to the switch.</p></li>
    <li><p>Determine and note which device your flash drive can be found at using output from <code>cat /proc/partitions</code> and <code>sudo fdisk -l [device]</code>. For example, <code>sudo fdisk -l /dev/sdb</code>. These instructions assume your USB drive is the <code>/dev/sdb</code> device, which is typical. Make sure to modify the commands below to use the proper device for your USB drive.</p></li>
    <li><p>Create a new partition table on the device:</p>
    <pre><code>sudo parted /dev/sdb mklabel msdos</code></pre></li>
    <li><p>Create a new partition on the device:</p>
    <pre><code>sudo parted /dev/sdb -a optimal mkpart primary 0% 100%</code></pre></li>
    <li><p>Format the partition to your filesystem of choice using ONE of the examples below:</p>
    <pre><code>sudo mkfs.ext2 /dev/sdb1
    sudo mkfs.msdos -F 32 /dev/sdb1
    sudo mkfs.vfat /dev/sdb1</code></pre>
    <p>{{%notice note%}}</p>
    <p>To use <code>mkfs.msdos</code> or <code>mkfs.vfat</code>, you need to install the <code>dosfstools</code> package from the <a href="http://docs.cumulusnetworks.com/display/DOCS/Adding+and+Updating+Packages#AddingandUpdatingPackages-AddingPackagesfromAnotherRepository" class="external-link">Debian software repositories</a> (step 3 here shows you how to add repositories from Debian), as they are not included by default.</p>
    <p>{{%/notice%}}</p></li>
    <li><p>To continue installing Cumulus RMP, mount the USB drive in order to move files to it.</p>
    <pre><code>sudo mkdir /mnt/usb
    sudo mount /dev/sdb1 /mnt/usb</code></pre></li>
    </ol></td>
    </tr>
    </tbody>
    </table>

3.  Copy the image file over to the flash drive and rename the image
    file to `onie-installer_x86-64`.

4.  Insert the USB stick into the switch, then continue with the
    appropriate instructions below for your x86 platform.

5.  Prepare the switch for installation:
    
      - If the switch is offline, connect to the console and power on
        the switch.
    
      - If the switch is already online in Cumulus RMP, connect to the
        console and reboot the switch into the ONIE environment with the
        `sudo cl-img-select -i` command, followed by `sudo reboot`. Then
        skip to step 4 below.
    
      - If the switch is already online in ONIE, use the `reboot`
        command.
    
    {{%notice note%}}
    
    SSH sessions to the switch get dropped after this step. To complete
    the remaining instructions, connect to the console of the switch.
    Cumulus RMP switches display their boot process to the console, so
    you need to monitor the console specifically to complete the next
    step.
    
    {{%/notice%}}

6.  Monitor the console and select the ONIE option from the first GRUB
    screen shown below.
    
    {{% imgOld 1 %}}

7.  Cumulus RMP uses GRUB chainloading to present a second GRUB menu
    specific to the ONIE partition. No action is necessary in this menu
    to select the default option *ONIE: Install OS*.
    
    {{% imgOld 2 %}}

8.  At this point, the USB drive should be automatically recognized and
    mounted. The image file should be located and automatic installation
    of Cumulus RMP should begin. Here is some sample output:
    
        ONIE: OS Install Mode  ...
         
        Version : quanta_common_rangeley-2014.05.05-6919d98-201410171013
        Build  Date: 2014-10-17T10:13+0800
        Info: Mounting kernel filesystems...  done.
        Info: Mounting LABEL=ONIE-BOOT on /mnt/onie-boot  ...
        initializing eth0...
        scsi 6:0:0:0: Direct-Access  SanDisk Cruzer Facet 1.26 PQ: 0 ANSI: 6
        sd 6:0:0:0: [sdb] 31266816 512-byte logical blocks: (16.0 GB/14.9 GiB)
        sd 6:0:0:0: [sdb] Write Protect is off
        sd 6:0:0:0: [sdb] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
        sd 6:0:0:0: [sdb] Attached SCSI disk
         
        <...snip...>
         
        ONIE:  Executing installer: file://dev/sdb1/onie-installer-x86_64
        Verifying image checksum ... OK.
        Preparing image archive ... OK.
        Dumping image info...
        Control File Contents
        =====================
        Description: Cumulus  Linux
        OS-Release:  2.5.7-3b46bef-201509041633-build
        Architecture: amd64
        Date:  Fri, 04 Sep 2015 17:10:30 -0700
        Installer-Version:  1.2
        Platforms: accton_as5712_54x accton_as6712_32x  mlx_sx1400_i73612 dell_s6000_s1220 dell_s4000_c2338 dell_s3000_c2338  cel_redstone_xp cel_smallstone_xp cel_pebble quanta_panther  quanta_ly8_rangeley quanta_ly6_rangeley quanta_ly9_rangeley  
        Homepage: http://www.cumulusnetworks.com/

9.  After installation completes, the switch automatically reboots into
    the newly installed instance of Cumulus RMP.

<span id="src-5116319_ManagingCumulusRMPDiskImages-slots"></span>

## <span>Understanding Image Slots</span>

Cumulus RMP uses the concept of *image slots* to manage two separate
Cumulus RMP images. The slots are described as follows:

  - **Active image slot**: The currently running image slot.

  - ******Primary image slot**: The image slot that is selected for the
    next boot. Often this is the same as the active image slot.

  - **Alternate image slot**: The inactive image slot, **not** selected
    for the next boot.

{{% imgOld 3 %}}

To identify which slot is active, which slot is the primary, and which
slot is alternate use the `cl-img-select` command:

    cumulus@switch$ sudo cl-img-select
    active => slot 1 (primary): 2.5.7-c4e83ad-201506011818-build
              slot 2 (alt    ): 2.5.4-727a0c6-201504132125-build

The above switch is currently running 2.5.7 as indicated by the
**active**. When the switch is rebooted, it will boot into slot 1, as
indicated by **primary**. The **alternate** slot is running Cumulus RMP
2.5.4 and won't be booted into unless the user selects it.

Each slot is a logical volume in the physical partition, which you can
manage with [LVM](https://wiki.debian.org/LVM). When Cumulus RMP is
installed on an x86 switch, the following entities are created on the
disk:

  - A disk partition using an ext4 file system that contains three
    logical volumes: two logical volumes named *sysroot1* and
    *sysroot2*, and the `/mnt/persist` logical volume. The logical
    volumes represent the Cumulus RMP image slots, so sysroot1 is slot 1
    and sysroot2 is slot 2. `/mnt/persist` is where you store your
    [persistent
    configuration](#src-5116319_ManagingCumulusRMPDiskImages-persistent_config).

  - A boot partition, shared by the logical volumes. Each volume mounts
    this partition as `/boot`.

### <span>Managing Slot Sizes</span>

As space in a slot is used, you may need to increase the size of the
root filesystem by increasing the size of the corresponding logical
volume. This section shows you how to check current utilization and
expand the filesystem as needed.

1.  Check utilization on the root filesystem with the `df` command. In
    the following example, filesystem utilization is 16%:
    
        cumulus@switch$ df -h /
        Filesystem                                              Size  Used Avail Use% Mounted on
        /dev/disk/by-uuid/64650289-cebf-4849-91ae-a34693fce2f1  4.0G  579M  3.2G  16% /
    
    ``` 
     
    ```

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
        active => slot 1 (primary): 2.5.7-199c587-201501081931-build
    
    `cl-img-select` indicates slot number 1 is active.

4.  Resize the slot with the `lvresize` command. The following example
    increases slot size by 20 percent of total available space. Replace
    the "\#" character in the example with the active slot number from
    the last step.
    
        cumulus@switch$ sudo lvresize -l +20%FREE CUMULUS/SYSROOT#
        Extending logical volume SYSROOT# to 5.27 GiB
        Logical volume SYSROOT# successfully resized
    
    {{%notice note%}}
    
    The use of `+` is very important with the `lvresize` command.
    Issuing `lvresize` without the `+` results in the logical volume
    size being set directly to the specified size, rather than extended.
    
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

<span id="src-5116319_ManagingCumulusRMPDiskImages-alt_slot"></span>

## <span>Accessing the Alternate Image Slot</span>

It may be useful to ****access the content of the alternate slot to
retrieve configuration or logs.

{{%notice note%}}

`cl-img-install` fails while the alternate slot is mounted. It is
important to unmount the alternate slot as shown in step 4 below when
done.

{{%/notice%}}

1.  Determine which slot is the alternate with `cl-img-select`.
    
        cumulus@switch$ sudo cl-img-select | grep alt
                slot 2 (alt    ): 2.5.0-199c587-201501081931-build
    
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
systems are unmounted and you can use various Cumulus RMP utilities to
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

From a running system you can display the contents of a Cumulus RMP
image file using `cl-img-pkg -d`:

    cumulus@switch:~$ sudo cl-img-pkg -d /var/lib/cumulus/installer/onie-installer
    Verifying image checksum ... OK.
    Preparing image archive ... OK.
    Control File Contents
    =====================
    Description: Cumulus RMP
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
