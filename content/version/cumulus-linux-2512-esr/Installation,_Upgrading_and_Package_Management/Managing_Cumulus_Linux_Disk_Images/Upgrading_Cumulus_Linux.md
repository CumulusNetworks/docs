---
title: Upgrading Cumulus Linux
author: Cumulus Networks
weight: 203
aliases:
 - /display/CL25ESR/Upgrading+Cumulus+Linux
 - /pages/viewpage.action?pageId=5116002
pageID: 5116002
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
Cumulus Networks software melds the Linux host world with the networking
devices world. Each world comes with its own paradigm on how to upgrade
software. Before we discuss the various ways to upgrade Cumulus Linux
switches, let's review the general considerations and strategies used to
upgrade network devices and Linux hosts.

## <span>Upgrades: Comparing the Network Device Worldview vs. the Linux Host Worldview</span>

### <span>Manual vs. Automated Configuration</span>

Historically, *network devices* were configured in place, and most
network devices required customized configurations, which led
predominantly to configuring the hardware manually. A lack of
standardization between vendors, device types, and device roles hampered
the development of APIs and automation tools. However, in the case of
very large data centers, configurations became uniform and repeatable,
and therefore scriptable. Some larger enterprises had to develop their
own custom scripts to roll out data center network configurations.
Virtually no industry-standard provisioning tools existed.

In contrast to data center network devices, *Linux hosts* in the data
center number in the thousands and tend to have similar configurations.
This increased scale led Linux sysadmins long ago to move to common
tools to automate installation and configuration, since manually
installing and configuring hosts did not work at the scale of a data
center. Nearly all tasks are done via commonly available provisioning
and orchestration tools.

### <span>Locations of Configuration Data vs. Executables</span>

*Network devices* generally separate configuration data from the
executable code. On bootup, the executable code looks into a different
file system and retrieves the configuration file or files, parses the
text and uses that data to configure the software options for each
software subsystem. The model is very centralized, with the executables
generally being packaged together, and the configuration data following
a set of rules that can be read by a centralized parser. Each vendor
controls the configuration format for the entire box, since each vendor
generally supports only their own software. This made sense since the
platform was designed as an application-specific appliance.

Since a *Linux host* is a general purpose platform, with applications
running on top of it, the locations of the files are much more
distributed. Applications install and read their configuration data from
text files usually stored in the /etc directory tree. Executables are
generally stored in one of several *bin* directories, but the bin and
etc directories are often on the same physical device. Since each
*module* (application or executable) was often developed by a different
organization and shared with the world, each module was responsible for
its own configuration data format. Most applications are community
supported, and while there are some generally accepted guiding
principles on how their configuration data is formatted, no central
authority exists to control or ensure compliance.

### <span>Pre-deployment Testing of Production Environments</span>

Historically, the cost of *network device* testing has been hampered by
the cost of a single device. Setting up an appropriately sized lab
topology can be very expensive. As a result, it is difficult to do
comprehensive topology-based testing of a release before deploying it.
Thus, many network admins cannot or will not do comprehensive system
testing of a new release before deploying it.

Alternatively, the cost of a *Linux host* is cheap (or nearly free when
using virtualization), so rigorous testing of a release before deploying
it is not encumbered by budgeting concerns. Most sysadmins extensively
test new releases in the complete application environment.

### <span>Upgrade Procedure</span>

Both network admins and sysadmins generally plan upgrades only to gain
new functionality or to get bug fixes when the workarounds become too
onerous. The goal is to reduce the number of upgrades as much as
possible.

The *network device* upgrade paradigm is to leave the configuration data
in place, and *replace the executable files* either all at once from a
single binary image or in large chunks (subsystems). A full release
upgrade comes with risk due to unexpected behavior changes in subsystems
where the admin did not anticipate or need changes.

The *Linux host* upgrade paradigm is to independently *upgrade a small
list of packages* while leaving most of the OS untouched. Changing a
small list of packages reduces the risk of unintended consequences.
Usually upgrades are a "forward only" paradigm, where the sysadmins
generally plan to move to the latest code within the same major release
when needed. Every few years, when a new kernel train is released, a
major upgrade is planned. A major upgrade involves wiping and replacing
the entire OS and migrating configuration data.

### <span>Rollback Procedure</span>

Even the most well planned and tested upgrades can result in unforeseen
problems, and sometimes the best solution to new problems is to roll
back to the previous state.

Since *network device*s clearly separate data and executables, generally
the process is to *overwrite the new release executable* with the
previously running executable. If the configuration was changed by the
newer release, then you either have to manually back out or repair the
changes, or restore from an already backed up configuration.

The *Linux host* scenario can be more complicated. There are three main
approaches:

  - Back out individual packages: If the problematic package is
    identified, the sysadmin can downgrade the affected package
    directly. In rare cases the configuration files may have to be
    restored from backup, or edited to back out any changes that were
    automatically made by the upgrade package.

  - Flatten and rebuild: If the OS becomes unusable, you can use
    orchestration tools to reinstall the previous OS release from
    scratch and then automatically rebuild the configuration.

  - Backup and restore: Another common strategy is to restore to a
    previous state via a backup captured before the upgrade.

### <span>Third Party Packages</span>

Third party packages are rare in the *network device* world. Because the
network OS is usually proprietary, third party packages are usually
packaged by the network device vendor and upgrades of those packages is
handled by the network device upgrade system.

Third party packages in *Linux host* world often use the same package
system as the distribution into which it is to be installed (for
example, Debian uses `apt-get`). Or the package may be compiled and
installed by the sysadmin. Configuration and executable files generally
follow the same filesystem hierarchy standards as other applications.

## <span>Upgrading Cumulus Linux Devices: Strategies and Processes</span>

Because Cumulus Linux is both Linux *and* a network device, it has
characteristics of both paradigms. The following describes the Cumulus
Linux paradigm with respect to upgrade planning and execution.

### <span>Automated Configuration Is Preferred over Manual Configuration</span>

Because Cumulus Linux *is* Linux, Cumulus Networks recommends that even
with small networks or test labs, network admins should make the jump to
deploy, provision, configure, and upgrade switches using automation from
the very beginning. The small up front investment of time spent learning
an orchestration tool, even to provision a small number of Cumulus Linux
devices, will pay back dividends for a long time. The biggest gain is
realized during the upgrade process, where the network admin can quickly
upgrade dozens of devices in a repeatable manner.

Switches, like servers, should be treated like *[cattle, not
pets](https://www.google.com/search?q=cattle+not+pets).*

### <span>Out-of-Band Management Is Worth the Investment</span>

Because network devices are reachable via the IP addresses on the front
panel ports, many network admins of small-to-medium sized networks use
*in-band* networks to manage their switches. In this design, management
traffic like SSH, SNMP, and console server connections use the same
networks that regular network traffic traverses — there is no separation
between the *management plane* and the *data plane*. Larger data centers
create a separate *out-of-band* network with a completely separate
subnet and reachability path to attach to the management ports — that is
accessible via eth0 and the serial console.

This is a situation where smaller companies should learn from the big
companies. A separate management network isn't free, but it is
relatively cheap. With an inexpensive [Cumulus
RMP](https://cumulusnetworks.com/rmp) management switch, an inexpensive
console server, and a separate cable path, up to 48 devices can be
completely controlled via the out-of-band network in the case of a
network emergency.

There are many scenarios where in-band networking can fail and leave the
network admin waiting for someone to drive to the data center or remote
site to connect directly to the console of a misconfigured or failing
device. The cost of one outage would usually more than pay for the
investment in a separate network. For even more security, attach
remote-controllable power distribution units (PDUs) in each rack to the
management network, so you can have complete control to remote power
cycle every device in that rack.

### <span>Pre-Deployment Testing of New Releases Is Advised and Enabled </span>

White box switches and virtualization (Cumulus VX) brings the cost of
networking devices down, so network admins' testing of their own
procedures, configurations, applications, and network topology in an
appropriately-sized lab topology becomes extremely affordable.

### <span>Understanding the Locations of Configuration Data for Management, Migration, and Backup</span>

As with other Linux distributions, the `/etc` directory is the primary
location for all configuration data in Cumulus Linux. You can use the
[Config File Migration
script](https://github.com/CumulusNetworks/config-backup-upgrade-helper)
to identify, archive and migrate configuration files that have changed
since the image was installed.

The table below lists the most likely and recommended files to back up
and migrate to a new release, but any file that has been changed would
need to be examined:

#### <span>Network Configuration Files</span>

| File Name and Location    | Explanation                                                                                          | Cumulus Linux Documentation                                                                                                                                                                 | Debian Documentation                                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| /etc/network/             | Network configuration files, most notably `/etc/network/interfaces` and `/etc/network/interfaces.d/` | [Configuring and Managing Network Interfaces](/version/cumulus-linux-2512-esr/Configuring_and_Managing_Network_Interfaces/)                                                                 | [wiki.debian.org/NetworkConfiguration](https://wiki.debian.org/NetworkConfiguration)                                         |
| /etc/resolv.conf          | DNS resolution                                                                                       | Not unique to Cumulus Linux: [wiki.debian.org/NetworkConfiguration\#The\_resolv.conf\_configuration\_file](https://wiki.debian.org/NetworkConfiguration#The_resolv.conf_configuration_file) | [www.debian.org/doc/manuals/debian-reference/ch05.en.html](https://www.debian.org/doc/manuals/debian-reference/ch05.en.html) |
| /etc/quagga/              | Routing application (responsible for BGP and OSPF)                                                   | [Quagga Overview](/version/cumulus-linux-2512-esr/Layer_3_Features/Quagga_Overview)                                                                                                         | [packages.debian.org/wheezy/quagga](https://packages.debian.org/wheezy/quagga)                                               |
| /etc/hostname             | Configuration file for the hostname of the switch                                                    | [Quick Start Guide\#ConfiguringtheHostnameandTimeZone](Quick_Start_Guide.html#src-5115897_QuickStartGuide-ConfiguringtheHostnameandTimeZone)                                                | [wiki.debian.org/HowTo/ChangeHostname](https://wiki.debian.org/HowTo/ChangeHostname)                                         |
| /etc/cumulus/ports.conf   | Breakout cable configuration file                                                                    | [Layer 1 and Switch Port Attributes\#ConfiguringBreakoutPorts](Layer_1_and_Switch_Port_Attributes.html#src-5116098_Layer1andSwitchPortAttributes-ConfiguringBreakoutPorts)                  | N/A; please read the guide on breakout cables                                                                                |
| /etc/cumulus/switchd.conf | Switchd configuration                                                                                | [Configuring switchd](/version/cumulus-linux-2512-esr/System_Management/Configuring_switchd)                                                                                                | N/A; please read the guide on switchd configuration                                                                          |

#### <span>Additional Commonly Used Files</span>

| File Name and Location | Explanation                                              | Cumulus Linux Documentation                                                                                                                                                  | Debian Documentation                                                                                                         |
| ---------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| /etc/motd              | Message of the day                                       | Not unique to Cumulus Linux                                                                                                                                                  | [wiki.debian.org/motd\#Wheezy](https://wiki.debian.org/motd#Wheezy)                                                          |
| /etc/passwd            | User account information                                 | Not unique to Cumulus Linux                                                                                                                                                  | [www.debian.org/doc/manuals/debian-reference/ch04.en.html](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html) |
| /etc/shadow            | Secure user account information                          | Not unique to Cumulus Linux                                                                                                                                                  | [www.debian.org/doc/manuals/debian-reference/ch04.en.html](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html) |
| /etc/group             | Defines user groups on the switch                        | Not unique to Cumulus Linux                                                                                                                                                  | [www.debian.org/doc/manuals/debian-reference/ch04.en.html](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html) |
| /etc/lldpd.conf        | Link Layer Discover Protocol (LLDP) daemon configuration | [Link Layer Discovery Protocol](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Link_Layer_Discovery_Protocol)                                                  | [packages.debian.org/wheezy/lldpd](https://packages.debian.org/wheezy/lldpd)                                                 |
| /etc/lldpd.d/          | Configuration directory for `lldpd`                      | [Link Layer Discovery Protocol](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Link_Layer_Discovery_Protocol)                                                  | [packages.debian.org/wheezy/lldpd](https://packages.debian.org/wheezy/lldpd)                                                 |
| /etc/nsswitch.conf     | Name Service Switch (NSS) configuration file             | [LDAP Authentication and Authorization](/version/cumulus-linux-2512-esr/System_Management/Authentication_Authorization_and_Accounting/LDAP_Authentication_and_Authorization) | [wiki.debian.org/LDAP/NSS](https://wiki.debian.org/LDAP/NSS)                                                                 |
| /etc/ssh/              | SSH configuration files                                  | [SSH for Remote Access](/version/cumulus-linux-2512-esr/System_Management/Authentication_Authorization_and_Accounting/SSH_for_Remote_Access)                                 | [wiki.debian.org/SSH](https://wiki.debian.org/SSH)                                                                           |
| /etc/ldap/ldap.conf    | Lightweight Directory Access Protocol configuration file | [LDAP Authentication and Authorization](/version/cumulus-linux-2512-esr/System_Management/Authentication_Authorization_and_Accounting/LDAP_Authentication_and_Authorization) | [www.debian.org/doc/manuals/debian-reference/ch04.en.html](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html) |

  - If you are using the root user account, consider including `/root/`.

  - If you have custom user accounts, consider including
    `/home/<username>/`.

#### <span id="src-5116002_UpgradingCumulusLinux-FilesToNeverMigrate" class="confluence-anchor-link"></span><span>Files That Should Never Be Migrated Between Versions or Boxes</span>

| File Name and Location | Explanation                                                                                                                      |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| /etc/adjtime           | System clock adjustment data. NTP manages this automatically. It is incorrect when the switch hardware is replaced. Do not copy. |
| /etc/bcm.d/            | Per-platform hardware configuration directory, created on first boot. Do not copy.                                               |
| /etc/blkid.tab         | Partition table. It should not be modified manually. Do not copy.                                                                |
| /etc/blkid.tab.old     | A previous partition table; it should not be modified manually. Do not copy.                                                     |
| /etc/cumulus/init      | Platform hardware-specific files. Do not copy.                                                                                   |
| /etc/default/clagd     | Created and managed by `ifupdown2`. Do not copy.                                                                                 |
| /etc/default/grub      | Grub `init` table; it should not be modified manually.                                                                           |
| /etc/default/hwclock   | Platform hardware-specific file. Created during first boot. Do not copy.                                                         |
| /etc/init              | Platform initialization files. Do not copy.                                                                                      |
| /etc/init.d/           | Platform initialization files. Do not copy.                                                                                      |
| /etc/fstab             | Static info on filesystem. Do not copy.                                                                                          |
| /etc/image-release     | System version data. Do not copy.                                                                                                |
| /etc/os-release        | System version data. Do not copy.                                                                                                |
| /etc/lsb-release       | System version data. Do not copy.                                                                                                |
| /etc/lvm/archive       | Filesystem files. Do not copy.                                                                                                   |
| /etc/lvm/backup        | Filesystem files. Do not copy.                                                                                                   |
| /etc/modules           | Created during first boot. Do not copy.                                                                                          |
| /etc/modules-load.d/   | Created during first boot. Do not copy.                                                                                          |
| /etc/sensors.d         | Platform-specific sensor data. Created during first boot. Do not copy.                                                           |
| /root/.ansible         | Ansible tmp files. Do not copy.                                                                                                  |
| /home/cumulus/.ansible | Ansible tmp files. Do not copy.                                                                                                  |

### <span>Upgrading Switches in an MLAG Pair</span>

If you have a pair of Cumulus Linux switches as part of an [MLAG
(multi-chassis link aggregation)
pair](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Multi-Chassis_Link_Aggregation_-_MLAG),
you should only upgrade each switch when it is in the *secondary role*.
The upgrade path is as follows:

1.  Upgrade Cumulus Linux on the switch already in the secondary role.
    This is the switch with the higher `clagd-priority` value.

2.  Set the switch in the secondary role into the primary role by
    setting its `clagd-priority` to a value lower than the
    `clagd-priority` setting on the switch in the primary role.
    
        cumulus@switch:~$ sudo clagctl priority VALUE 

3.  Upgrade the switch that just took on the secondary role.

4.  Put that switch into the primary role again, if you so choose.
    
        cumulus@switch:~$ sudo clagctl priority VALUE

For more information about setting the priority, see [Understanding
Switch
Roles](Multi-Chassis_Link_Aggregation_-_MLAG.html#src-5116071_Multi-ChassisLinkAggregation-MLAG-roles).

## <span>Upgrading Cumulus Linux: Choosing between a Binary Install vs. Package Upgrade</span>

Network admins have two ways to upgrade Cumulus Linux:

  - Performing a binary (full image) install of the new version, running
    `cl-img-install` on the switch

  - Upgrading only the changed packages, using `apt-get update` and
    `apt-get dist-upgrade`

There are advantages and disadvantages to using these methods, which are
outlined below.

<span id="src-5116002_UpgradingCumulusLinux-binary_upgrade"></span>

### <span>Upgrading via Binary Install (cl-img-install)</span>

Pros:

  - Image is installed to the [alternate disk image
    slot](Managing_Cumulus_Linux_Disk_Images.html#src-5115988_ManagingCumulusLinuxDiskImages-slots)
    while the switch remains operational.

  - The only downtime is the reboot/init process.

  - You choose the exact version that you want to upgrade to.

  - Rolling back to the previous version and config is easy and quick;
    it requires only running `cl-img-select -s` and reboot.

  - This is the only method for upgrading to a new major (X.0) or minor
    version (X.Y). For example, when you are upgrading from 2.5.5 to 3.0
    or from 2.2.2 to 2.5.5.

Cons:

  - Configuration data must be moved to the new OS via some mechanism
    before the new OS is booted, or soon afterwards via out-of-band
    management.

  - Moving the configuration file can go wrong in various ways:
    
      - Identifying all the locations of config data is not always an
        easy task.
    
      - Config file changes in the new version may cause merge conflicts
        that go undetected.

To upgrade the switch by running a binary install:

1.  Back up the configurations off the switch using the [Config File
    Migration
    script](https://github.com/CumulusNetworks/config-backup-upgrade-helper)
    with the `--backup` option and then copy the archive off the
    switch.  
    **Optional:** Use the Ansible playbook included with the [Config
    File Migration
    script](https://github.com/CumulusNetworks/config-backup-upgrade-helper)
    to automate the backup of all your Cumulus Linux 2.5 switches. See
    the section below on [Using Automation Tools to Backup
    Configurations](#src-5116002_UpgradingCumulusLinux-Using_Automation_Tools)
    for more details.

2.  Install the binary image to the [alternate
    slot](Managing_Cumulus_Linux_Disk_Images.html#src-5115988_ManagingCumulusLinuxDiskImages-slots)
    and select it as the new primary slot.
    
        cumulus@switch$ sudo cl-img-install -s <image_url>
    
    {{%notice note%}}
    
    If you don't use the `-s` flag here, you will have to run
    `cl-img-select -s` after the installation to manually select the
    alternate slot.
    
    {{%/notice%}}
    
    Click to expand full output
    
        cumulus@switch$ sudo cl-img-install -s CumulusLinux-2.5.3a-amd64.bin
        Defaulting to image slot 2 for install.
        Dumping image info from CumulusLinux-2.5.3a-amd64.bin ...
        Verifying image checksum ... OK.
        Preparing image archive ... OK.
        Control File Contents
        =====================
        Description: Cumulus Linux
        OS-Release: 2.5.3a-3b46bef-201509041633-build
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
        active => slot 1 (primary): 2.5.3-c4e83ad-201506011818-build
                  slot 2 (alt    ): 2.5.2-727a0c6-201504132125-build
        About to update image slot 2 using:
        /home/cumulus/CumulusLinux-2.5.3a-amd64.bin
        Are you sure (y/N)? y
        Verifying image checksum ... OK.
        Preparing image archive ... OK.
        Validating sha1 for vmlinuz-initrd.tar.xz... done.
        Validating sha1 for sysroot-release.tar.gz... done.
        Installing OS-Release 2.5.3a-3b46bef-201509041633-build into image slot 2 ...
        Info: Copying sysroot into slot 2
        Creating logical volume SYSROOT2 on volume group CUMULUS... done.
        Verifying sysroot copy... OK.
        Copying kernel into CLBOOT partition... done.
        Verifying kernel copy... OK.
        Generating grub.cfg ...
        Found Cumulus Linux image: /boot/cl-vmlinuz-3.2.65-1+deb7u2+cl2.5+5-slot-1
        Found Cumulus Linux image: /boot/cl-vmlinuz-3.2.65-1+deb7u2+cl2.5+5-slot-2
        done
        Success: /home/cumulus/CumulusLinux-2.5.3a-amd64.bin loaded into image slot 2.

3.  **Optional:** Migrate the configuration files to the alternate slot
    using the [Config File Migration
    script](https://github.com/CumulusNetworks/config-backup-upgrade-helper)
    with the `--sync` option.

4.  Reboot the switch.
    
        cumulus@switch$ sudo reboot

5.  Restore the configuration files to the new version — ideally via
    automation — if the files were not migrated in step 3. To manually
    restore an archive created by the [Config File Migration
    script](https://github.com/CumulusNetworks/config-backup-upgrade-helper):
    
        # On the switch, copy the config file archive back from the server:
        cumulus@switch$ scp user@my_external_server:PATH/SWITCHNAME-config-archive-DATE_TIME.tar.gz .
         
        # Untar the archive to the root of the box
        cumulus@switch$ sudo tar -C / -xvf SWITCHNAME-config-archive-DATE_TIME.tar.gz

6.  Verify correct operation with the old configurations on the new
    version.

7.  Reinstall third party apps and associated configurations.

<span id="src-5116002_UpgradingCumulusLinux-apt_upgrade"></span>

### <span>Upgrading Using Package Installs (apt-get update && apt-get dist-upgrade)</span>

Pros:

  - Configuration data stays in place while the binaries are upgraded.

  - Third-party apps stay in place.

Cons:

  - This method works only if you are upgrading to a later maintenance
    release (X.Y.Z, like 2.5.5) from an earlier release in the same
    major and minor release family **only** (like 2.5.0 to 2.5.4, or
    2.5.2 to 2.5.5).

  - Rollback is quite difficult and tedious.

  - You can't choose the exact release version that you want to run.

  - When you upgrade, you upgrade all packages to the latest available
    version.

  - The upgrade process takes a while to complete, and various switch
    functions are intermittently available during the upgrade.

  - Some upgrade operations will terminate SSH sessions on the in-band
    (front panel) ports, leaving the user unable to monitor the upgrade
    process. As a workaround, use the [dtach
    tool](https://support.cumulusnetworks.com/hc/en-us/articles/215453578).

  - Just like the binary install method, you still must reboot after the
    upgrade, lengthening the downtime.

{{%notice note%}}

Before you upgrade a PowerPC switch, run `df -m` and make sure the
overlay filesystem `/mnt/root-rw` has at least 200MB of free disk space.
See [this release
note](https://support.cumulusnetworks.com/hc/en-us/articles/211153707-Cumulus-Linux-2-5-4-Release-Notes#rn334)
for more details.

{{%/notice%}}

To upgrade the switch by updating the packages:

1.  Back up the configurations off the switch.

2.  Fetch the latest update meta-data from the repository.
    
        cumulus@switch$ sudo apt-get update

3.  Upgrade all the packages to the latest distribution.
    
        cumulus@switch$ sudo apt-get dist-upgrade

4.  Reboot the switch.
    
        cumulus@switch$ sudo reboot

5.  Verify correct operation with the old configurations on new version.

{{%notice warning%}}

While this method doesn't overwrite the [target image
slot](Managing_Cumulus_Linux_Disk_Images.html#src-5115988_ManagingCumulusLinuxDiskImages-slots),
the disk image does occupy a lot of disk space used by both Cumulus
Linux image slots.

{{%/notice%}}

{{%notice note%}}

After you successfully upgrade Cumulus Linux, you may notice some some
results that you may or may not have expected:

  - `apt-get dist-upgrade` always updates the operating system to the
    most current version, so if you are currently running Cumulus Linux
    2.5.2 and run `apt-get dist-upgrade` on that switch, the packages
    will get upgraded to the latest version.

  - When you run `cl-img-select`, the output still shows the version of
    Cumulus Linux from the last binary install. So if you installed
    Cumulus Linux 2.5.3 as a full image install and then upgraded to
    2.5.8 using `apt-get dist-upgrade`, the output from `cl-img-select`
    still shows version 2.5.3. To see the current version of Cumulus
    Linux running on the switch, use `cat /etc/lsb-release`.

{{%/notice%}}

Why you should use apt-get dist-upgrade instead of apt-get upgrade
(Click here to expand...)

{{%notice warning%}}

Cumulus Networks recommends you upgrade Cumulus Linux using `apt-get
dist-upgrade` instead of `apt-get upgrade`.

This ensures all the packages in the distribution get updated to the
current version. `apt-get upgrade` **may** work correctly if no packages
are held back by `apt`. A package can be held back if one or more of its
dependencies has changed, or it can occur for other reasons. For
example, if you see this message when running `apt-get upgrade`:

    "The following packages have been kept back:
    linux-image-powerpc"

It means `apt-get upgrade` did not install the kernel package. However,
`apt-get dist-upgrade` would have picked it up. Most applications in
Cumulus Linux rely on the correct kernel version. If an application
doesn't get the kernel version it expects, It may result in a
non-functional system.

You can manually install a held back package by running `apt-get
install` on it:

    apt-get install linux-image-powerpc

If you must use `apt-get upgrade`, run it twice. For the second time,
include the `-s` or `--dry-run` option to verify that all packages were
picked up when you upgraded. Otherwise, you must manually install any
held back packages to complete the upgrade.

    apt-get upgrade --dry-run

{{%/notice%}}

## <span id="src-5116002_UpgradingCumulusLinux-Using_Automation_Tools" class="confluence-anchor-link"></span><span>Using Automation Tools to Back Up Configurations</span>

Adopting the use of automation tools like Ansible, Chef or Puppet for
configuration management greatly increases the speed and accuracy of the
next major upgrade; they also enable the quick swap of failed switch
hardware. Included with the [Config Migration
Script](https://github.com/CumulusNetworks/config-backup-upgrade-helper)
is an Ansible playbook that can be used to create a backup archive of
all deployed Cumulus Linux 2.5.z switch configuration files and to
retrieve them to a central server. This is a quick start on the road to
setting up automated configuration and control for your deployment. For
more details on integrating automation into your Cumulus Linux
deployment, see the [Automation Solutions section on
cumulusnetworks.com](https://cumulusnetworks.com/solutions/automation/).

## <span>Rolling Back a Cumulus Linux Installation</span>

### <span>Rolling Back after Using Binary Install</span>

1.  Select the alternate slot as the new primary slot. (The primary slot
    will be booted at the next reboot)
    
        cumulus@switch$ sudo cl-img-select -s

2.  Reboot the switch.
    
        cumulus@switch$ sudo reboot

### <span>Rolling Back after Using Package Install</span>

Rolling back to an earlier release after upgrading the packages on the
switch follows the same procedure as described for the Linux host OS
rollback above. There are three main strategies, and all require
detailed planning and execution:

  - Back out individual packages: If the problematic package is
    identified, the network admin can downgrade the affected package
    directly. In rare cases the configuration files may have to be
    restored from backup, or edited to back out any changes that were
    automatically made by the upgrade package.

  - Flatten and rebuild: If the OS becomes unusable, you can use
    orchestration tools to reinstall the previous OS release from
    scratch and then automatically rebuild the configuration.

  - Backup and restore: Another common strategy is to restore to a
    previous state via a backup captured before the upgrade.

Which method you employ is specific to your deployment strategy, so
providing detailed steps for each scenario is outside the scope of this
document.

## <span>Third Party Package Considerations</span>

Note that if you install any third party apps on a Cumulus Linux switch,
any configuration data will likely be installed into the /etc directory,
but it is not guaranteed. It is the responsibility of the network admin
to understand the behavior and config file information of any third
party packages installed on a Cumulus Linux switch.

After you upgrade the OS in the alternate image slot, you will need to
reinstall any third party packages or any Cumulus Linux add-on packages,
such as `cl-mgmtvrf`, or `vxsnd` and `vxrd`.

## <span>Caveats while Upgrading Cumulus Linux 2.5.x</span>

  - [RN-287](https://support.cumulusnetworks.com/hc/en-us/articles/214459418#rn287):
    Copying the `/etc/passwd` file to the other slot when one version is
    earlier than Cumulus Linux 2.5.3 and the other version is later than
    Cumulus Linux 2.5.3 causes issues with LLDP not starting and Quagga
    logs not being created.
