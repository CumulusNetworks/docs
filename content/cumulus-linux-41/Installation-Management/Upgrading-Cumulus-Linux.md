---
title: Upgrading Cumulus Linux
author: NVIDIA
weight: 50
toc: 3
---

This topic describes how to upgrade Cumulus Linux on your switch.

Deploying, provisioning, configuring, and upgrading switches using automation is highly recommended, even with small networks or test labs. During the upgrade process, you can quickly upgrade dozens of devices in a repeatable manner. Using tools like Ansible, Chef, or Puppet for configuration management greatly increases the speed and accuracy of the next major upgrade; these tools also enable the quick swap of failed switch hardware.

## Before You Upgrade

{{%notice tip%}}
Be sure to read the knowledge base article
[Upgrades: Network Device and Linux Host Worldview Comparison]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Network-Device-and-Linux-Host-Worldview-Comparison" >}}), which provides a detailed comparison between the network device and Linux host worldview of upgrade and installation.
{{%/notice%}}

### Back up Configuration Files

Understanding the location of configuration data is required for successful upgrades, migrations, and backup. As with other Linux distributions, the `/etc` directory is the primary location for all configuration data in Cumulus Linux. The following list is a likely set of files that you need to back up and migrate to a new release. Make sure you examine any file that has been changed. Consider making the following files and directories part of a backup strategy.

{{< tabs "TabID25 ">}}

{{< tab "Network Configuration Files ">}}

| File Name and Location | Explanation| Cumulus Linux Documentation | Debian Documentation |
| ---------------------- | ---------- | ----------------------------| -------------------- |
| `/etc/network/` | Network configuration files, most notably `/etc/network/interfaces` and `/etc/network/interfaces.d/` | {{<link title="Switch Port Attributes">}} | N/A |
| `/etc/resolv.conf` | DNS resolution| Not unique to Cumulus Linux: {{<exlink url="https://wiki.debian.org/NetworkConfiguration#The_resolv.conf_configuration_file" text="wiki.debian.org/NetworkConfiguration">}} | {{<exlink url="https://www.debian.org/doc/manuals/debian-reference/ch05.en.html">}} |
| `/etc/frr/` | Routing application (responsible for BGP and OSPF) | {{<link title="FRRouting Overview">}} | N/A |
| `/etc/hostname` | Configuration file for the hostname of the switch | {{<link title="Quick Start Guide">}} | {{<exlink url="https://wiki.debian.org/HowTo/ChangeHostname">}} |
| `/etc/hosts`  | Configuration file for the hostname of the switch | {{<link title="Quick Start Guide">}} | {{<exlink url="https://wiki.debian.org/HowTo/ChangeHostname">}} |
| `/etc/cumulus/acl/*` | Netfilter configuration | {{<link title="Netfilter - ACLs">}} |N/A |
| `/etc/cumulus/ports.conf` | Breakout cable configuration file | {{<link title="Switch Port Attributes">}} | N/A; read the guide on breakout cables |
| `/etc/cumulus/switchd.conf` | `switchd` configuration | {{<link title="Configuring switchd">}} | N/A; read the guide on `switchd` configuration |

{{< /tab >}}

{{< tab "Commonly-Used Files ">}}

| File Name and Location | Explanation| Cumulus Linux Documentation | Debian Documentation |
| ---------------------- | ---------- | --------------------------- | -------------------- |
| `/etc/motd` | Message of the day | Not unique to Cumulus Linux | {{<exlink url="https://wiki.debian.org/motd#Wheezy" text="wiki.debian.org/motd" >}} |
| `/etc/passwd` | User account information | Not unique to Cumulus Linux | {{<exlink url="https://www.debian.org/doc/manuals/debian-reference/ch04.en.html">}} |
| `/etc/shadow` | Secure user account information| Not unique to Cumulus Linux | {{<exlink url="https://www.debian.org/doc/manuals/debian-reference/ch04.en.html">}} |
| `/etc/group` | Defines user groups on the switch| Not unique to Cumulus Linux | {{<exlink url="https://www.debian.org/doc/manuals/debian-reference/ch04.en.html">}} |
| `/etc/lldpd.conf` | Link Layer Discover Protocol (LLDP) daemon configuration | {{<link title="Link Layer Discovery Protocol">}} | {{<exlink url="https://packages.debian.org/buster/lldpd">}} |
| `/etc/lldpd.d/` | Configuration directory for lldpd | {{<link title="Link Layer Discovery Protocol">}} | {{<exlink url="https://packages.debian.org/buster/lldpd">}} |
| `/etc/nsswitch.conf` | Name Service Switch (NSS) configuration file | {{<link title="TACACS">}} | N/A |
|`/etc/ssh/` | SSH configuration files | {{<link title="SSH for Remote Access">}} | {{<exlink url="https://wiki.debian.org/SSH">}} |
| `/etc/sudoers`, `/etc/sudoers.d` | Best practice is to place changes in `/etc/sudoers.d/` instead of `/etc/sudoers`; changes in the `/etc/sudoers.d/` directory are not lost during upgrade. | {{<link title="Using sudo to Delegate Privileges">}} |

{{< /tab >}}

{{%notice note%}}

- If you are using the root user account, consider including `/root/`.
- If you have custom user accounts, consider including `/home/<username>/`.
- Run the `net show configuration files | grep -B 1 "==="` command and back up the files listed in the command output.

{{%/notice%}}

{{< tab "Never Migrate Files ">}}

| File Name and Location  | Explanation |
| ----------------------- | ----------- |
| `/etc/bcm.d/` | Per-platform hardware configuration directory, created on first boot. Do not copy. |
| `/etc/mlx/` | Per-platform hardware configuration directory, created on first boot. Do not copy. |
| `/etc/default/clagd` | Created and managed by `ifupdown2`. Do not copy.|
| `/etc/default/grub` | Grub `init` table. Do not modify manually. |
| `/etc/default/hwclock` | Platform hardware-specific file. Created during first boot. Do not copy. |
| `/etc/init` | Platform initialization files. Do not copy. |
| `/etc/init.d/` | Platform initialization files. Do not copy. |
| `/etc/fstab` | Static information on filesystem. Do not copy. |
| `/etc/image-release` | System version data. Do not copy. |
| `/etc/os-release` | System version data. Do not copy. |
| `/etc/lsb-release` | System version data. Do not copy. |
| `/etc/lvm/archive` | Filesystem files. Do not copy. |
| `/etc/lvm/backup` | Filesystem files. Do not copy. |
| `/etc/modules` | Created during first boot. Do not copy. |
| `/etc/modules-load.d/` | Created during first boot. Do not copy. |
| `/etc/sensors.d` | Platform-specific sensor data. Created during first boot. Do not copy. |
| `/root/.ansible` | Ansible `tmp` files. Do not copy. |
| `/home/cumulus/.ansible` | Ansible `tmp` files. Do not copy.|

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

You can check which files have changed since the last binary install with the following commands. Be sure to back up any changed files:

- Run the `sudo dpkg --verify` command to show a list of changed files.
- Run the `egrep -v '^$|^#|=""$' /etc/default/isc-dhcp-*` command to see if any of the generated `/etc/default/isc-*` files have changed.

{{%/notice%}}

### Create a cl-support File

**Before** and **after** you upgrade the switch, run the `cl-support` script to create a `cl-support` archive file. The file is a compressed archive of useful information for troubleshooting. If you experience any issues during upgrade, you can send this archive file to the Cumulus Linux support team to investigate.

1. Create the `cl-support` archive file with the `cl-support` command:

   ```
   cumulus@switch:~$ sudo cl-support
   ```

2. Copy the `cl-support` file off the switch to a different location.

3. After upgrade is complete, run the `cl-support` command again to create a new archive file:

   ```
   cumulus@switch:~$ sudo cl-support
   ```

## Upgrade Cumulus Linux

You can upgrade Cumulus Linux in one of two ways:

- Install a disk image of the new release, using ONIE.
- Upgrade only the changed packages using the `sudo -E apt-get update` and `sudo -E apt-get upgrade` command.

{{%notice note%}}

Upgrading an MLAG pair requires additional steps. If you are using MLAG to dual connect two Cumulus Linux switches in your environment, follow the steps in [Upgrade Switches in an MLAG Pair](#upgrade-switches-in-an-mlag-pair) below to ensure a smooth upgrade.

{{%/notice%}}

### Should I Install a Disk Image or Upgrade Packages?

The decision to upgrade Cumulus Linux by either installing a disk image or upgrading packages depends on your environment and your preferences. Here are some recommendations for each upgrade method.

**Installing a disk image** is recommended if you are performing a rolling upgrade in a production environment and if are using up-to-date and comprehensive automation scripts. This upgrade method enables you to choose the exact release to which you want to upgrade and is the *only* method available to upgrade your switch to a new release train (for example, from 3.7.12 to 4.1.0).

Be aware of the following when installing the disk image:

- Installing a disk image is destructive; any configuration files on the switch are not saved; copy them to a different server before you start the disk image install.
- You must move configuration data to the new OS using ZTP or automation while the OS is first booted, or soon afterwards using out-of-band management.
- Moving a configuration file might cause issues;
- Identifying all the locations of configuration data is not always an easy task. See [Before You Upgrade](#before-you-upgrade) above.
- Merge conflicts with configuration file changes in the new release might go undetected.
- If configuration files are not restored correctly, you might be unable to ssh to the switch from in-band management. Out-of-band connectivity (eth0 or console) is recommended.
- You *must* reinstall and reconfigure third-party applications after upgrade.

**Package upgrade** is recommended if you are upgrading from Cumulus Linux 4.0, or if you use third-party applications (package upgrade does not replace or remove third-party applications, unlike disk image install).

Be aware of the following when upgrading packages:

- You cannot upgrade the switch to a new release train. For example, you **cannot** upgrade the switch from **3**.7.x to **4**.1.0.
- The `sudo -E  apt-get upgrade` command might result in services being restarted or stopped as part of the upgrade process.
- The `sudo -E apt-get upgrade` command might disrupt core services by changing core service dependency packages.
- After you upgrade, account UIDs and GIDs created by packages might be different on different switches, depending on the configuration and package installation history.

### Disk Image Install (ONIE)

ONIE is an open source project (equivalent to PXE on servers) that enables the installation of network operating systems (NOS) on a bare metal switch.

{{%notice note%}}

Lightweight network virtualization (LNV) is deprecated in Cumulus Linux 4.0 in favor of Ethernet virtual private networks ({{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}. If your network is configured for LNV, you need to migrate your network configuration to a BGP EVPN configuration that is functionally equivalent ***before*** you upgrade. Refer to {{<link title="Migrating from LNV to EVPN">}}.

{{%/notice%}}

To upgrade the switch:

1. Back up the configurations off the switch.
2. Download the Cumulus Linux image.
3. Install the disk image with the `onie-install -a -i <image-location>` command, which boots the switch into ONIE. The following example command installs the image from a web server, then reboots the switch. There are additional ways to install the disk image, such as using FTP, TFTP, a local file, or a USB drive. For more information, see {{<link title="Installing a New Cumulus Linux Image">}}.

    ```
    cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/cumulus-linux-4.1.0-mlx-amd64.bin &&   sudo reboot
    ```

4. Restore the configuration files to the new release - ideally with automation.
5. Verify correct operation with the old configurations on the new release.
6. Reinstall third party applications and associated configurations.

### Package Upgrade

Cumulus Linux completely embraces the Linux and Debian upgrade workflow, where you use an installer to install a base image, then perform any upgrades within that release train with `sudo -E apt-get update` and `sudo -E apt-get upgrade` commands. Any packages that have been changed since the base install get upgraded in place from the repository. All switch configuration files remain untouched, or in rare cases merged (using the Debian merge function) during the package upgrade.

When you use package upgrade to upgrade your switch, configuration data stays in place while the packages are upgraded. If the new release updates a configuration file that you changed previously, you are prompted for the version you want to use or if you want to evaluate the differences.

To upgrade the switch using package upgrade:

1. Back up the configurations from the switch.

2. Fetch the latest update metadata from the repository.

    ```
    cumulus@switch:~$ sudo -E apt-get update
    ```

3. Review potential upgrade issues (in some cases, upgrading new packages might also upgrade additional existing packages due to dependencies). Run the following command to see the additional packages that will be installed or upgraded.

    ```
    cumulus@switch:~$ sudo -E apt-get upgrade --dry-run
    ```

4. Upgrade all the packages to the latest distribution.

    ```
    cumulus@switch:~$ sudo -E apt-get upgrade
    ```

    If no reboot is required after the upgrade completes, the upgrade ends, restarts all upgraded services, and log messages in the `/var/log/syslog` file similar to the ones shown below. In the examples below, only the `frr` package is upgraded.

    ```
    Policy: Service frr.service action stop postponed
    Policy: Service frr.service action start postponed
    Policy: Restarting services: frr.service
    Policy: Finished restarting services
    Policy: Removed /usr/sbin/policy-rc.d
    Policy: Upgrade is finished
    ```
    If the upgrade process encounters changed configuration files that have new versions in the release to which you are upgrading, you see a message similar to this:

    ```
    Configuration file '/etc/frr/daemons'
    ==> Modified (by you or by a script) since installation.
    ==> Package distributor has shipped an updated version.
    What would you like to do about it ? Your options are:
    Y or I : install the package maintainer's version
    N or O : keep your currently-installed version
    D : show the differences between the versions
    Z : start a shell to examine the situation
    The default action is to keep your current version.
    *** daemons (Y/I/N/O/D/Z) [default=N] ?

    - To see the differences between the currently installed version and the
    new version, type `D`- To keep the currently installed version, type `N`.
    The new package version is installed with the suffix `_.dpkg-dist`
    (for example, `/etc/frr/daemons.dpkg-dist`). When upgrade is complete and
    **before** you reboot, merge your changes with the changes from the newly
    installed file.
    - To install the new version, type `I`. Your currently installed version is
    saved with the suffix `.dpkg-old`.
    When the upgrade is complete, you can search for the files with the
    `sudo find / -mount -type f -name '*.dpkg-*'` command.
    ```

    If you see errors for expired GPG keys that prevent you from upgrading packages, follow the steps in [Upgrading Expired GPG Keys]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Update-Expired-GPG-Keys" >}}).

5. Reboot the switch if the upgrade messages indicate that a system restart is required.

    ```
    cumulus@switch:~$ sudo -E apt-get upgrade
    ... upgrade messages here ...

    *** Caution: Service restart prior to reboot could cause unpredictable behavior
    *** System reboot required ***
    cumulus@switch:~$ sudo reboot
    ```

6. Verify correct operation with the old configurations on the new version.

### Upgrade Notes

*Package upgrade* always updates to the latest available release in the Cumulus Linux repository. For example, if you are currently running Cumulus Linux 4.0.0 and run the `sudo -E apt-get upgrade` command on that switch, the packages are upgraded to the latest releases contained in the latest 4.y.z release.

Because Cumulus Linux is a collection of different Debian Linux packages, be aware of the following:

- The `/etc/os-release` and `/etc/lsb-release` files are updated to the currently installed Cumulus Linux release when you upgrade the switch using either *package upgrade* or *disk image install*. For example, if you run `sudo -E apt-get upgrade` and the latest Cumulus Linux release on the repository is 4.1.0, these two files display the release as 4.1.0 after the upgrade.
- The `/etc/image-release` file is updated **only** when you run a disk image install. Therefore, if you run a disk image install of Cumulus Linux 4.0.0, followed by a package upgrade to 4.1.0 using `sudo -E apt-get upgrade`, the `/etc/image-release` file continues to display Cumulus Linux 4.0.0, which is the originally installed base image.

## Upgrade Switches in an MLAG Pair

If you are using {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} to dual connect two switches in your environment, follow the steps below to upgrade the switches.

{{%notice info%}}
You must upgrade both switches in the MLAG pair to the same release of Cumulus Linux.

Only during the upgrade process does Cumulus Linux supports different software versions between MLAG peer switches. After you upgrade the first MLAG switch in the pair, run the `clagctl showtimers` command to monitor the `init-delay` timer. When the timer expires, make the upgraded MLAG switch the primary, then upgrade the peer to the same version of Cumulus Linux.

Running different versions of Cumulus Linux on MLAG peer switches outside of the upgrade time period is untested and might have unexpected results.
{{%/notice%}}

{{%notice warning%}}

For networks with MLAG deployments, you can only upgrade to Cumulus Linux 4.1 from version 3.7.10 or later. If you are using a version of Cumulus Linux earlier than 3.7.10, you must upgrade to version 3.7.10 first, then upgrade to version 4.1. Version 3.7.10 is available on the
{{<exlink url="https://enterprise-support.nvidia.com/s/downloader" text="NVIDIA Enterprise support portal">}} on our website.

{{%/notice%}}

{{%notice info%}}
During upgrade, MLAG bonds stay single-connected while the switches are running different major releases; for example, while leaf01 is running 3.7.12 and leaf02 is running 4.1.1.

This is due to a change in the bonding driver regarding how the *actor port key* is derived, which causes the port key to have a different value for links with the same speed/duplex settings across different major releases. The port key received from the LACP partner must remain consistent between all bond members in order for all bonds to be synchronized. When each MLAG switch sends LACPDUs with different port keys, only links to one MLAG switch are in sync.
{{%/notice%}}

1. Verify the switch is in the secondary role:

    ```
    cumulus@switch:~$ clagctl status
    ```

2. Shut down the core uplink layer 3 interfaces:

    ```
    cumulus@switch:~$ sudo ip link set swpX down
    ```

3. Shut down the peer link:

    ```
    cumulus@switch:~$ sudo ip link set peerlink down
    ```

4. To boot the switch into ONIE, run the `onie-install -a -i <image-location>` command. The following example command installs the image from a web server. There are additional ways to install the Cumulus Linux image, such as using FTP, a local file, or a USB drive. For more information, see {{<link title="Installing a New Cumulus Linux Image">}}.

    ```
    cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/downloads/cumulus-linux-4.1.0-mlx-amd64.bin
    ```

   To upgrade the switch with package upgrade instead of booting into ONIE, run the `sudo -E apt-get update` and `sudo -E apt-get upgrade` commands; see {{<link url="#package-upgrade" text="Package Upgrade">}}.

5. Reboot the switch:

    ```
    cumulus@switch:~$ sudo reboot
    ```

6. If you installed a new image on the switch, restore the configuration files to the new release.

7. Verify STP convergence across both switches:

    ```
    cumulus@switch:~$ mstpctl showall
    ```

8. Verify core uplinks and peer links are UP:

    ```
    cumulus@switch:~$ net show interface
    ```

9. Verify MLAG convergence:

    ```
    cumulus@switch:~$ clagctl status
    ```

10. Make this secondary switch the primary:

    ```
    cumulus@switch:~$ clagctl priority 2048
    ```

11. Verify the other switch is now in the secondary role.
12. Repeat steps 2-9 on the new secondary switch.
13. Remove the priority 2048 and restore the priority back to 32768 on the current primary switch:

    ```
    cumulus@switch:~$ clagctl priority 32768
    ```

## Roll Back a Cumulus Linux Installation

Even the most well planned and tested upgrades can result in unforeseen problems; sometimes the best solution is to roll back to the previous state. There are three main strategies; all require detailed planning and execution:

- Flatten and rebuild: If the OS becomes unusable, you can use orchestration tools to reinstall the previous OS release from scratch and then rebuild the configuration automatically.
- Backup and restore: Another common strategy is to restore to a previous state using a backup captured before the upgrade. See {{<link title="Back up and Restore">}}.

The method you employ is specific to your deployment strategy, so providing detailed steps for each scenario is outside the scope of this document.

## Third Party Packages

Third party packages in the *Linux host* world often use the same package system as the distribution into which it is to be installed (for example, Debian uses `apt-get`). Or, the package might be compiled and installed by the system administrator. Configuration and executable files generally follow the same filesystem hierarchy standards as other applications.

If you install any third party applications on a Cumulus Linux switch, configuration data is typically installed into the `/etc` directory, but it is not guaranteed. It is your responsibility to understand the behavior and configuration file information of any third party packages installed on the switch.

After you upgrade using a full disk image install, you need to reinstall any third party packages or any Cumulus Linux add-on packages.

## Related Information

- [Upgrades: Network Device Worldview and Linux Host Worldview Comparison]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Network-Device-and-Linux-Host-Worldview-Comparison" >}})
- {{<exlink url="https://www.nvidia.com/en-us/networking/network-automation/" text="Automation Solutions">}}
- {{<exlink url="http://opencomputeproject.github.io/onie/design-spec/" text="ONIE Design Specification">}}
- {{<link title="Multi-Chassis Link Aggregation - MLAG">}}
- {{<link title="Zero Touch Provisioning - ZTP">}}
