---
title: Upgrading Cumulus Linux
author: NVIDIA
weight: 50
toc: 3
---
{{%notice warning%}}
The default password for the *cumulus* user account is `cumulus`. The first time you log into Cumulus Linux, you **must** change this default password. Be sure to update any automation scripts before you upgrade. You can use ONIE command line options to change the default password automatically during the Cumulus Linux image installation process. Refer to {{<link url="Installing-a-New-Cumulus-Linux-Image#onie-installation-options" text="ONIE Installation Options">}}.
{{%/notice%}}

This topic describes how to upgrade Cumulus Linux on your switch.

Consider deploying, provisioning, configuring, and upgrading switches using automation, even with small networks or test labs. During the upgrade process, you can upgrade dozens of devices in a repeatable manner. Using tools like Ansible, Chef, or Puppet for configuration management greatly increases the speed and accuracy of the next major upgrade; these tools also enable you to quickly swap failed switch hardware.

## Before You Upgrade

{{%notice tip%}}
Be sure to read the knowledge base article
[Upgrades: Network Device and Linux Host Worldview Comparison]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Network-Device-and-Linux-Host-Worldview-Comparison" >}}), which provides a detailed comparison between the network device and Linux host worldview of upgrade and installation.
{{%/notice%}}

### Back up Configuration Files

Understanding the location of configuration data is important for successful upgrades, migrations, and backup. As with other Linux distributions, the `/etc` directory is the primary location for all configuration data in Cumulus Linux. The following list contains the files you need to back up and migrate to a new release. Make sure you examine any changed files. Make the following files and directories part of a backup strategy.

{{< tabs "TabID25 ">}}
{{< tab "Network Configuration Files ">}}

| File Name and Location | Description| Cumulus Linux Documentation | Debian Documentation |
| ---------------------- | ---------- | ----------------------------| -------------------- |
| `/etc/frr/` | Routing application (responsible for BGP and OSPF) | {{<link title="FRRouting">}} | N/A |
| `/etc/hostname` | Configuration file for the hostname of the switch | {{<link title="Quick Start Guide">}} | {{<exlink url="https://wiki.debian.org/HowTo/ChangeHostname">}} |
| `/etc/network/` | Network configuration files, most notably `/etc/network/interfaces` and `/etc/network/interfaces.d/` | {{<link title="Switch Port Attributes">}} | N/A |
| `/etc/resolv.conf` | DNS resolution| Not unique to Cumulus Linux: {{<exlink url="https://wiki.debian.org/NetworkConfiguration#The_resolv.conf_configuration_file" text="wiki.debian.org/NetworkConfiguration">}} | {{<exlink url="https://www.debian.org/doc/manuals/debian-reference/ch05.en.html">}} |
| `/etc/hosts`  | Configuration file for the hostname of the switch | {{<link title="Quick Start Guide">}} | {{<exlink url="https://wiki.debian.org/HowTo/ChangeHostname">}} |
| `/etc/cumulus/acl/*` | Netfilter configuration | {{<link title="Netfilter - ACLs">}} |N/A |
| `/etc/cumulus/control-plane/policers.conf` | Configuration for control plane policers | {{<link title="Netfilter - ACLs#control-plane-policers">}} | N/A |
| `/etc/cumulus/datapath/qos/qos_features.conf` | QoS configuration <br><br><b>Note:</b> In Cumulus Linux 5.0 and later, default ECN configuration parameters start with `default_ecn_red_conf` instead of `default_ecn_conf`. | {{<link title="Quality of Service">}} | N/A |
| `/etc/mlx/datapath/qos/qos_infra.conf` | QoS configuration | {{<link title="Quality of Service">}} | N/A |
| `/etc/mlx/datapath/tcam_profile.conf` | Configuration for the forwarding table profiles| {{<link title="Supported Route Table Entries#tcam-resource-profiles-for-spectrum-switches">}} | N/A |
| `/etc/cumulus/datapath/traffic.conf` | Configuration for the forwarding table profiles| {{<link title="Supported Route Table Entries">}} | N/A |
| `/etc/cumulus/ports.conf` | Breakout cable configuration file | {{<link title="Switch Port Attributes">}} | N/A; read the guide on breakout cables |
| `/etc/cumulus/switchd.conf` | `switchd` configuration | {{<link title="Configuring switchd">}} | N/A; read the guide on `switchd` configuration |
| `/etc/cumulus/switchd.d/qos.conf` | QoS configuration | {{<link title="Quality of Service">}} | N/A |

{{< /tab >}}
{{< tab "Commonly Used Files ">}}

| File Name and Location | Description| Cumulus Linux Documentation | Debian Documentation |
| ---------------------- | ---------- | --------------------------- | -------------------- |
| `/etc/motd` | Message of the day | Not unique to Cumulus Linux | {{<exlink url="https://wiki.debian.org/motd#Wheezy" text="wiki.debian.org/motd" >}} |
| `/etc/passwd` | User account information | Not unique to Cumulus Linux | {{<exlink url="https://www.debian.org/doc/manuals/debian-reference/ch04.en.html">}} |
| `/etc/shadow` | Secure user account information| Not unique to Cumulus Linux | {{<exlink url="https://www.debian.org/doc/manuals/debian-reference/ch04.en.html">}} |
| `/etc/group` | Defines user groups on the switch| Not unique to Cumulus Linux | {{<exlink url="https://www.debian.org/doc/manuals/debian-reference/ch04.en.html">}} |
| `/etc/init/lldpd.conf` | Link Layer Discover Protocol (LLDP) daemon configuration | {{<link title="Link Layer Discovery Protocol">}} | {{<exlink url="https://packages.debian.org/buster/lldpd">}} |
| `/etc/lldpd.d/` | Configuration directory for lldpd | {{<link title="Link Layer Discovery Protocol">}} | {{<exlink url="https://packages.debian.org/buster/lldpd">}} |
| `/etc/nsswitch.conf` | Name Service Switch (NSS) configuration file | {{<link title="TACACS">}} | N/A |
|`/etc/ssh/` | SSH configuration files | {{<link title="SSH for Remote Access">}} | {{<exlink url="https://wiki.debian.org/SSH">}} |
| `/etc/sudoers`, `/etc/sudoers.d` | Best practice is to place changes in `/etc/sudoers.d/` instead of `/etc/sudoers`; changes in the `/etc/sudoers.d/` directory are not lost during upgrade | {{<link title="Using sudo to Delegate Privileges">}} |

{{%notice note%}}
- If you are using the root user account, consider including `/root/`.
- If you have custom user accounts, consider including `/home/<username>/`.
{{%/notice%}}

{{< /tab >}}
{{< tab "Never Migrate Files ">}}

| File Name and Location  | Description |
| ----------------------- | ----------- |
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

The following commands verify which files have changed compared to the previous Cumulus Linux install. Be sure to back up any changed files.
- Run the `sudo dpkg --verify` command to show a list of changed files.
- Run the `egrep -v '^$|^#|=""$' /etc/default/isc-dhcp-*` command to see if any of the generated `/etc/default/isc-*` files have changed.

### Back Up and Restore Configuration with NVUE

You can backup and restore the configuration file with NVUE only if you used NVUE commands to configure the switch you want to upgrade.

To back up and restore the configuration file:

1. Save the configuration to the `/etc/nvue.d/startup.yaml` file with the `nv config save` command:

   ```
   cumulus@switch:~$ nv config save
   saved
   ```

2. Copy the `/etc/nvue.d/startup.yaml` file off the switch to a different location.

3. After upgrade is complete, restore the configuration. Copy the `/etc/nvue.d/startup.yaml` file to the switch, then run the `nv config apply startup` command:

   ```
   cumulus@switch:~$ nv config apply startup
   applied
   ```

For information about the NVUE object model and commands, see {{<link url="NVIDIA-User-Experience-NVUE" text="NVIDIA User Experience - NVUE">}}.

{{%notice note%}}
As NVUE supports more features and introduces new syntax, {{<link url="NVUE-Snippets" text="snippets and flexible snippets">}} become invalid.

Before you upgrade Cumulus Linux to a new release, make sure to:
- Review the {{<link url="Whats-New" text="What's New">}} for new NVUE syntax.
- If NVUE introduces new syntax for the feature that a snippet configures, you must remove the snippet before upgrading.
{{%/notice%}}
<!-- vale off -->
### Create a cl-support File
<!-- vale on -->
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

<span class="a-tooltip">[ONIE](## "Open Network Install Environment")</span> is an open source project (equivalent to PXE on servers) that enables the installation of network operating systems (NOS) on a bare metal switch.

You can upgrade Cumulus Linux in one of two ways:

- Install a Cumulus Linux image of the new release, using ONIE.
- Upgrade only the changed packages using the `sudo -E apt-get update` and `sudo -E apt-get upgrade` command.

Cumulus Linux also provides ISSU to upgrade an active switch with minimal disruption to the network. See {{<link url="In-Service-System-Upgrade-ISSU" text="In-Service-System-Upgrade-ISSU">}}.

{{%notice note%}}
- To upgrade to Cumulus Linux 5.8.0 from Cumulus Linux 4.x or 3.x, you must install a disk image of the new release using ONIE. You *cannot* upgrade packages with the `apt-get upgrade` command.
- Upgrading an MLAG pair requires additional steps. If you are using MLAG to dual connect two Cumulus Linux switches in your environment, follow the steps in [Upgrade Switches in an MLAG Pair](#upgrade-switches-in-an-mlag-pair) below to ensure a smooth upgrade.
{{%/notice%}}

### Install a Cumulus Linux Image or Upgrade Packages?

The decision to upgrade Cumulus Linux by either installing a Cumulus Linux image or upgrading packages depends on your environment and your preferences. Here are some recommendations for each upgrade method.

**Install a Cumulus Linux image** if you are performing a rolling upgrade in a production environment and if are using up-to-date and comprehensive automation scripts. This upgrade method enables you to choose the exact release to which you want to upgrade and is the *only* method available to upgrade your switch to a new release train (for example, from 4.4.3 to 5.8.0).

Be aware of the following when installing the Cumulus Linux image:

- Installing a Cumulus Linux image is destructive; any configuration files on the switch are not saved; copy them to a different server before you start the Cumulus Linux image install.
- You must move configuration data to the new OS using ZTP or automation while the OS is first booted, or soon afterwards using out-of-band management.
- Moving a configuration file can cause issues.
- Identifying all the locations of configuration data is not always an easy task. See [Before You Upgrade Cumulus Linux](#before-you-upgrade) above.
- Merge conflicts with configuration file changes in the new release sometimes go undetected.
- If configuration files do not restore correctly, you cannot ssh to the switch from in-band management. Use out-of-band connectivity (eth0 or console).
- You *must* reinstall and reconfigure third-party applications after upgrade.

Run **package upgrade** if you are upgrading from Cumulus Linux 5.0.0 to a later 5.x release, or if you use third-party applications (package upgrade does not replace or remove third-party applications, unlike the Cumulus Linux image install).

Be aware of the following when upgrading packages:

- You cannot upgrade the switch to a new release train. For example, you **cannot** upgrade the switch from 4.x to 5.x.
- The `sudo -E  apt-get upgrade` command might restart or stop services as part of the upgrade process.
- The `sudo -E apt-get upgrade` command might disrupt core services by changing core service dependency packages.
- After you upgrade, account UIDs and GIDs created by packages might be different on different switches, depending on the configuration and package installation history.
- Cumulus Linux does not support the `sudo -E apt-get dist-upgrade` command. Be sure to use `sudo -E apt-get upgrade` when upgrading packages.

### Cumulus Linux Image Install (ONIE)

ONIE is an open source project (equivalent to PXE on servers) that enables the installation of network operating systems (NOS) on a bare metal switch.

To upgrade the switch:

1. Back up the configurations off the switch.
2. Download the Cumulus Linux image.
3. Install the Cumulus Linux image with the `onie-install -a -i <image-location>` command, which boots the switch into ONIE. The following example command installs the image from a web server, then reboots the switch. There are additional ways to install the Cumulus Linux image, such as using FTP, a local file, or a USB drive. For more information, see {{<link title="Installing a New Cumulus Linux Image">}}.

    ```
    cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/cumulus-linux-4.1.0-mlx-amd64.bin && sudo reboot
    ```

4. Restore the configuration files to the new release (restoring files with automation is not recommended).
5. Verify correct operation with the old configurations on the new release.
6. Reinstall third party applications and associated configurations.

### Package Upgrade

{{%notice note%}}
- NVUE deprecated the port split command options (2x10G, 2x25G, 2x40G, 2x50G, 2x100G, 2x200G, 4x10G, 4x25G, 4x50G, 4x100G, 8x50G) available in Cumulus Linux 5.3 and earlier. If you use NVUE to configure port breakout speeds in Cumulus 5.3 or earlier, NVUE automatically updates the configuration during upgrade to Cumulus Linux 5.5 and later to use the new format (2x, 4x, 8x).
- Cumulus Linux continues to support the old port split format in the `/etc/cumulus/ports.conf` file; however NVIDIA recommends that you use the new format.
{{%/notice%}}

Cumulus Linux completely embraces the Linux and Debian upgrade workflow, where you use an installer to install a base image, then perform any upgrades within that release train with `sudo -E apt-get update` and `sudo -E apt-get upgrade` commands. Any packages that have changed after the base install get upgraded in place from the repository. All switch configuration files remain untouched, or in rare cases merged (using the Debian merge function) during the package upgrade.

When you use package upgrade to upgrade your switch, configuration data stays in place during the upgrade. If the new release updates a previously changed configuration file, the upgrade process prompts you to either specify the version you want to use or evaluate the differences.

#### Disk Space Requirements

Make sure you have enough disk space to perform a package upgrade. Cumulus Linux 5.8.0 requires:
- 1.5GB GB of free disk space to upgrade from 5.7
- 1.8GB of free disk space to upgrade from 5.6

Before you upgrade, run the `sudo df -h` command to show how much disk space you are currently using on the switch.

```
cumulus@switch:~$ sudo df -h
Filesystem      Size   Used   Avail   Use%    Mounted on
udev            7.7G      0    7.7G     0%    /dev
tmpfs           1.6G    18M    1.6G     2%    /run
/dev/sda4        28G   7.9G     18G    31%    /
tmpfs           7.7G   277M    7.4G     4%    /dev/shm
tmpfs           5.0M      0    5.0M     0%    /run/lock
tmpfs           7.7G      0    7.7G     0%    /sys/fs/cgroup
tmpfs           7.7G    16K    7.7G     1%    /tmp
overlay          28G   7.9G     18G    31%   
```

#### Upgrade the Switch

To upgrade the switch using package upgrade:

1. Back up the configurations from the switch.

2. Fetch the latest update metadata from the repository.

    ```
    cumulus@switch:~$ sudo -E apt-get update
    ```

3. Review potential upgrade issues (in some cases, upgrading new packages might also upgrade additional existing packages due to dependencies).

    ```
    cumulus@switch:~$ sudo -E apt-get upgrade --dry-run
    ```

4. Upgrade all the packages to the latest distribution.

    ```
    cumulus@switch:~$ sudo -E apt-get upgrade
    ```

    If you do not need to reboot the switch after the upgrade completes, the upgrade ends, restarts all upgraded services, and logs messages in the `/var/log/syslog` file similar to the ones shown below. In the examples below, the process only upgrades the `frr` package.

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
    ```

    - To see the differences between the currently installed version and the new version, type `D`.
    - To keep the currently installed version, type `N`. The new package version installs with the suffix `.dpkg-dist` (for example, `/etc/frr/daemons.dpkg-dist`). When the upgrade completes and **before** you reboot, merge your changes with the changes from the newly installed file.
    - To install the new version, type `I`. Your currently installed version has the suffix `.dpkg-old`.
    - Cumulus Linux includes `/etc/apt/sources.list` in the `cumulus-archive-keyring` package. During upgrade, you must select if you want the new version from the package or the existing file.

    When the upgrade is complete, you can search for the files with the `sudo find / -mount -type f -name '*.dpkg-*'` command.

    If you see errors for expired GPG keys that prevent you from upgrading packages, follow the steps in [Upgrading Expired GPG Keys]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Update-Expired-GPG-Keys" >}}).

5. Reboot the switch if the upgrade messages indicate that you need to perform a system restart.

    ```
    cumulus@switch:~$ sudo -E apt-get upgrade
    ... upgrade messages here ...

    *** Caution: Service restart prior to reboot could cause unpredictable behavior
    *** System reboot required ***
    cumulus@switch:~$ sudo reboot
    ```

6. Verify correct operation with the old configurations on the new version.

{{%notice info%}}
The first time you run the NVUE `nv config apply` command after upgrading to Cumulus Linux 5.4, NVUE might override certain existing configuration for features that are now configurable with NVUE. Immediately after you reboot the switch to complete the upgrade, NVIDIA recommends you either:
- Run NVUE commands to configure these features.
- Configure NVUE to ignore changes to the relevant configuration files for these features; refer to {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to Ignore Linux Files">}}.
{{%/notice%}}

### Upgrade Notes

*Package upgrade* always updates to the latest available release in the Cumulus Linux repository. For example, if you are currently running Cumulus Linux 5.0.0 and run the `sudo -E apt-get upgrade` command on that switch, the packages upgrade to the latest releases in the latest 5.x release.

Because Cumulus Linux is a collection of different Debian Linux packages, be aware of the following:

- The `/etc/os-release` and `/etc/lsb-release` files update to the currently installed Cumulus Linux release when you upgrade the switch using either *package upgrade* or *Cumulus Linux image install*. For example, if you run `sudo -E apt-get upgrade` and the latest Cumulus Linux release on the repository is 5.8.0, these two files display the release as 5.8.0 after the upgrade.
- The `/etc/image-release` file updates **only** when you run a Cumulus Linux image install. Therefore, if you run a Cumulus Linux image install of Cumulus Linux 5.6.0, followed by a package upgrade to 5.8.0 using `sudo -E apt-get upgrade`, the `/etc/image-release` file continues to display Cumulus Linux 5.6.0, which is the originally installed base image.

## Upgrade Switches in an MLAG Pair

If you are using {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} to dual connect two switches in your environment, follow the steps below to upgrade the switches.

{{%notice info%}}
You must upgrade both switches in the MLAG pair to the same release of Cumulus Linux.

Only during the upgrade process does Cumulus Linux supports different software versions between MLAG peer switches. After you upgrade the first MLAG switch in the pair, run the `clagctl showtimers` command to monitor the `init-delay` timer. When the timer expires, make the upgraded MLAG switch the primary, then upgrade the peer to the same version of Cumulus Linux.

NVIDIA has not tested running different versions of Cumulus Linux on MLAG peer switches outside of the upgrade time period; you might see unexpected results.
{{%/notice%}}

{{< tabs "TabID311 ">}}
{{< tab "NVUE Commands ">}}

1. Verify the switch is in the secondary role:

    ```
    cumulus@switch:~$ nv show mlag
    ```

2. Shut down the core uplink layer 3 interfaces. The following example shuts down swp1:

    ```
    cumulus@switch:~$ nv set interface swp1 link state down
    cumulus@switch:~$ nv config apply
    ```

3. Shut down the peer link:

    ```
    cumulus@switch:~$ nv set interface peerlink link state down
    cumulus@switch:~$ nv config apply
    ```

4. To boot the switch into ONIE, run the `onie-install -a -i <image-location>` command. The following example command installs the image from a web server. There are additional ways to install the Cumulus Linux image, such as using FTP, a local file, or a USB drive. For more information, see {{<link title="Installing a New Cumulus Linux Image">}}.

    ```
    cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/downloads/cumulus-linux-4.1.0-mlx-amd64.bin
    ```

   To upgrade the switch with package upgrade instead of booting into ONIE, run the `sudo -E apt-get update` and `sudo -E apt-get upgrade` commands; see {{<link url="#package-upgrade" text="Package Upgrade">}}.

5. Save the changes to the NVUE configuration from steps 2-3 and reboot the switch:

    ```
    cumulus@switch:~$ nv config save
    cumulus@switch:~$ nv action reboot system
    ```

6. If you installed a new image on the switch, restore the configuration files to the new release. If you performed an upgrade with `apt`, bring the uplink and peer link interfaces you shut down in steps 2-3 up:

    ```
    cumulus@switch:~$ nv set interface swp1 link state up
    cumulus@switch:~$ nv set interface peerlink link state down
    cumulus@switch:~$ nv config apply
    cumulus@switch:~$ nv config save
    ```

7. Verify STP convergence across both switches with the Linux `mstpctl showall` command. NVUE does not provide an equivalent command.

    ```
    cumulus@switch:~$ mstpctl showall
    ```

8. Verify core uplinks and peer links are UP:

    ```
    cumulus@switch:~$ nv show interface
    ```

9. Verify MLAG convergence:

    ```
    cumulus@switch:~$ nv show mlag
    ```

10. Make this secondary switch the primary:

    ```
    cumulus@switch:~$ nv set mlag priority 2084
    ```

11. Verify the other switch is now in the secondary role.
12. Repeat steps 2-9 on the new secondary switch.
13. Remove the priority 2048 and restore the priority back to 32768 on the current primary switch:

    ```
    cumulus@switch:~$ nv set mlag priority 32768
    ```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Verify the switch is in the secondary role:

    ```
    cumulus@switch:~$ clagctl status
    ```

2. Shut down the core uplink layer 3 interfaces:

    ```
    cumulus@switch:~$ sudo ip link set <switch-port> down
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

8. Verify that core uplinks and peer links are UP:

    ```
    cumulus@switch:~$ ip addr show
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

{{< /tab >}}
{{< /tabs >}}

## Roll Back a Cumulus Linux Installation

Even the most well planned and tested upgrades can result in unforeseen problems and sometimes the best solution is to roll back to the previous state. These main strategies require detailed planning and execution:

- Flatten and rebuild. If the OS becomes unusable, you can use orchestration tools to reinstall the previous OS release from scratch and then rebuild the configuration automatically.
- Restore to a previous state using a backup configuration captured before the upgrade.

The method you employ is specific to your deployment strategy. Providing detailed steps for each scenario is outside the scope of this document.

## Third Party Packages

If you install any third party applications on a Cumulus Linux switch, configuration data is typically installed in the `/etc` directory, but it is not guaranteed. It is your responsibility to understand the behavior and configuration file information of any third party packages installed on the switch.

After you upgrade using a full Cumulus Linux image install, you need to reinstall any third party packages or any Cumulus Linux add-on packages.

## Related Information

- [Upgrades: Network Device Worldview and Linux Host Worldview Comparison]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Network-Device-and-Linux-Host-Worldview-Comparison" >}})
- {{<exlink url="https://www.nvidia.com/en-us/networking/network-automation/" text="Automation Solutions">}}
- {{<exlink url="http://opencomputeproject.github.io/onie/design-spec/" text="ONIE Design Specification">}}
- {{<link title="Multi-Chassis Link Aggregation - MLAG">}}
- {{<link title="Zero Touch Provisioning - ZTP">}}
