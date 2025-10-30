---
title: Upgrading Cumulus Linux
author: NVIDIA
weight: 30
toc: 3
---
This guide describes the three methods for upgrading Cumulus Linux. Two of these methods optionally support {{<link url="#issu" text="In-Service-System-Upgrade (ISSU)">}}, enabling you to perform a hitless (sub-second loss of data plane traffic) upgrade.

To upgrade Cumulus Linux, choose one of the three upgrade methods:

- Install a new Cumulus Linux image with {{<link url="#optimized-image-upgrade" text="optimized image upgrade">}}, (ISSU support and maintains the current switch configuration)
- Upgrade only changed packages with {{<link url="#package-upgrade" text="package upgrade">}} (ISSU support and maintains the current switch configuration)
- Install a new Cumulus Linux image with {{<link url="#onie-image-upgrade" text="ONIE">}} (no ISSU support and you will need to manually back up and restore your switch configuration)
## Upgrades with ISSU

<span class="a-tooltip">[ISSU](## "In Service System Upgrade")</span> enables you to perform a hitless upgrade of the switch software while the network continues to forward packets. ISSU hitless upgrade minimizes data plane traffic disruption to sub-second levels and automatically translates the switch NVUE configuration to the new version’s schema. During ISSU, the routing control plane is temporarily unavailable; however, the {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="BGP graceful restart">}} capability maintains traffic flow through the switch.

Cumulus Linux supports two methods that can use ISSU:
- {{<link url="#optimized-image-upgrade" text="Optimized image upgrade">}}
- {{<link url="#package-upgrade" text="Package upgrade">}}

ISSU requires the use of {{<link url="System-Power-and-Switch-Reboot/#switch-reboot" text="warm reboot mode">}}. You must configure the switch in half-resource mode to perform a warm reboot. When the switch operates in half-resource mode, performing a warm reboot (using the `nv action reboot system mode warm` command) results in a hitless upgrade. For more information about reboot modes, refer to {{<link url="System-Power-and-Switch-Reboot/#switch-reboot" text="Switch Reboot Modes">}}.

To configure the switch in half resource mode:

{{< tabs "TabID40 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system forwarding resource-mode half
```

To set the resource-mode back to the default value (full) run the `nv unset system forwarding resource-mode` command.

{{%notice infonopad%}}
Changing the resource mode on the switch requires a `switchd` restart, which impacts traffic forwarding. 
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.d/resource-mode.conf
...
resource_mode = half
```

Restart the switchd service with the `sudo systemctl restart switchd.service` command.

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Cumulus Linux supports ISSU and warm reboot mode with 802.1X, layer 2 forwarding, layer 3 forwarding with BGP, static routing, and VXLAN routing with EVPN. 

The following features are not supported during warm reboot:
- EVPN MLAG or EVPN multihoming.
- LACP bonds. LACP control plane sessions might time out before warm reboot completes. Use static LAG to keep bonds up with sub-second convergence during a warm reboot.
{{%/notice%}}

## Before You Upgrade
### Create a cl-support File

**Before** and **after** you upgrade the switch, run the `cl-support` script to create a `cl-support` archive file. The file is a compressed archive of useful information for troubleshooting. If you experience any issues during upgrade, you can send this archive file to the Cumulus Linux support team to investigate.

1. Create the `cl-support` archive file with either the NVUE `nv action generate system tech-support` command or the Linux `sudo cl-support` command:

```
cumulus@switch:~$ nv action generate system tech-support
```

2. Copy the `cl-support` file off the switch to a different location.

3. After upgrade is complete, create a new archive file:

```
cumulus@switch:~$ nv action generate system tech-support
```

## Optimized Image Upgrade

Optimized image upgrade uses two partitions to upgrade the image with just one reboot cycle. With two partitions on the switch, the current image boots from one partition, from which the image upgrade triggers. After detecting the running partition and checking if the second partition is available for installation, optimized upgrade starts to stage the installation in the second partition (copying the image, preparing the partition, unpacking the new image, and tuning and finalizing the new partition for the new image). The subsequent boot occurs from the second partition.

  - You can only use optimized image upgrade on a switch with a 30GB <span class="a-tooltip">[SSD](## "Solid state drive")</span> or larger to accommodate the second partition required for upgrade. To validate the size of the SSD, run the `sudo blockdev --getsize64 /dev/sda` command. As an alternative, run the `sudo blkid` command and confirm the `CL-SYSTEM-2` partition exists on the switch to support optimized upgrade.
  - You cannot downgrade a Cumulus Linux 5.15 switch to Cumulus Linux 5.11.0 or earlier with optimized image upgrade; use ONIE instead.
<br>
  For a list of the releases from which you can upgrade to Cumulus Linux 5.15 with optimized image upgrade, see {{<link url="Whats-New/#upgrade-requirements" text="Release Considerations">}}.

{{%notice note%}}
Upgrading an MLAG pair requires additional steps. If you are using MLAG to dual connect two Cumulus Linux switches in your environment, follow the steps in [Upgrade Switches in an MLAG Pair](#upgrade-switches-in-an-mlag-pair) below to ensure a smooth upgrade.
{{%/notice%}}

{{< tabs "TabID569 ">}}
{{< tab "NVUE Commands ">}}

1. Download the Cumulus Linux image with the `nv action fetch system image <remote-url>` command:

   ```
   cumulus@switch:~$ nv action fetch system image http://10.0.1.251/cumulus-linux-5.15.0-mlx-amd64.bin
   ```

   The `nv action fetch system image <remote-url>` command copies the image to the `/var/images` directory on the switch. If you copy the image manually to the switch instead of using the `nv action fetch system image <remote-url>` command, make sure to copy the image to the `/var/images` directory.

2. Install the image on the second partition:

   ```
   cumulus@switch:~$ nv action install system image files cumulus-linux-5.15.0-mlx-amd64.bin
   ```

   Use the `force` option to force install the image:

   ```
   cumulus@switch:~$ nv action install system image files cumulus-linux-5.15.0-mlx-amd64.bin force
   ```

3. Set the boot partition:

   ```
   cumulus@switch:~$ nv action boot-next system image other 
   ```

4. Reboot the switch. If you configured the switch resource mode to half for {{<link url="#issu" text="ISSU">}}, reboot with warm mode for a hitless upgrade:

```
    cumulus@switch:~$ nv action reboot system mode warm
```

If you are not using ISSU, reboot with a {{<link url="System-Power-and-Switch-Reboot/#switch-reboot" text="cold reboot">}}:

```
    cumulus@switch:~$ nv action reboot system
```

If the upgrade fails or you want to go back to the Cumulus Linux release from which you upgraded, run the `nv action boot-next system image other rollback` command. The switch boots back to the previous release image and restores the switch configuration.

- To rename a Cumulus Linux image on the switch, run the `nv action rename system image files <image> <new-image-name>` command.
- To delete a Cumulus Linux image from the switch, run the `nv action delete system image files <image>` command.

To show information about a cumulus image:

```
cumulus@switch:~$ nv show system image
               operational              
-------------  -------------------------
current        2                        
next           2                        
partition1                              
  build-id     5.13.0.0026
  description  Cumulus Linux 5.13.0     
  disk         /dev/sda5                
  release      5.13.0                   
partition2                              
  build-id     5.15.0.0018
  description  Cumulus Linux 5.15.0     
  disk         /dev/sda6                
  release      5.15.0 
```

- To list the available Cumulus Linux image files, run the `nv show system image files` command.
- To show information about a specific Cumulus Linux image file, run the `nv show system image files <image-filename>` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Download the Cumulus Linux image to the switch.

2. Install the image on the second partition:

   ```
   cumulus@switch:~$ cl-image-upgrade -u cumulus-linux-5.15.0-mlx-amd64.bin
   ```

To check the current boot partition status, run the `cl-image-upgrade -s` command:

```
cumulus@switch:~$ cl-image-upgrade -s  
Current system partition is 1 on /dev/sda5 
Current system partition has 5.11.0 "Cumulus Linux 5.11.0" 5.11.0.0012
Other system partition is 2 on /dev/sda6 
...
```

To activate the other partition at next boot, run the `cl-image-upgrade -a` command:

```
cumulus@switch:~$ cl-image-upgrade -a 
```

3. Reboot the switch. If you configured the switch resource mode to half for {{<link url="#issu" text="ISSU">}}, reboot with warm mode for a hitless upgrade:

```
    cumulus@switch:~$ sudo csmgrctl -wf
```

If you are not using ISSU, reboot with a {{<link url="System-Power-and-Switch-Reboot/#switch-reboot" text="cold reboot">}}:

```
    cumulus@switch:~$ sudo reboot
```

{{< /tab >}}
{{< /tabs >}}

## Package Upgrade

Cumulus Linux completely embraces the Linux and Debian upgrade workflow, where you use an installer to install a base image, then perform any upgrades within that release train with package upgrade. Any packages that change after the base install get upgraded in place from the repository. All switch configuration files remain untouched, or in rare cases merged during the package upgrade.

When you use package upgrade to upgrade the switch, configuration data stays in place during the upgrade. If the new release updates a previously changed configuration file, the upgrade process prompts you to either specify the version you want to use or evaluate the differences.

Upgrading an MLAG pair requires additional steps. If you are using MLAG to dual connect two Cumulus Linux switches in your environment, follow the steps in [Upgrade Switches in an MLAG Pair](#upgrade-switches-in-an-mlag-pair) below to ensure a smooth upgrade.

{{%notice note%}}
- You cannot upgrade the switch to a new release train. For example, you **cannot** use package upgrade to upgrade the switch from 4.x to 5.x.
- Package upgrade always updates to the latest available release in the Cumulus Linux repository.
- The package upgrade command might restart or stop services as part of the upgrade process.
- The package upgrade command might disrupt core services by changing core service dependency packages.
- After you upgrade, account UIDs and GIDs created by packages might be different on different switches, depending on the configuration and package installation history.
- Cumulus Linux does not support the Linux `sudo -E apt-get dist-upgrade` command. Be sure to use `sudo -E apt-get upgrade` when upgrading packages.
- To package upgrade to Cumulus Linux 5.15, you need 0.8GB of free disk space. Before you upgrade, run the NVUE `nv show system disk usage` command or the Linux `sudo df -h` command to show how much disk space you are currently using on the switch.
{{%/notice%}}

For a list of the releases from which you can upgrade to Cumulus Linux 5.15, see {{<link url="Whats-New/#upgrade-requirements" text="Release Considerations">}}.

To upgrade the switch with package upgrade:

{{< tabs "TabID253 ">}}
{{< tab "NVUE Commands ">}}

1. Fetch the latest update metadata from the repository and review potential upgrade issues (in some cases, upgrading new packages might also upgrade additional existing packages due to dependencies).

   ```
   cumulus@switch:~$ sudo nv action upgrade system packages to latest use-vrf default dry-run
   ```

   By default, the NVUE `sudo nv action upgrade system packages` command runs in the management VRF. To run the command in a non-management VRF such as `default`, you must use the `use-vrf <vrf-id>` option.

2. Upgrade all the packages to the latest distribution.

    ```
    cumulus@switch:~$ sudo nv action upgrade system packages to latest use-vrf default
    ```

    By default, the NVUE `sudo nv action upgrade system packages` command runs in the management VRF. To run the command in a non-management VRF such as `default`, you must use the `use-vrf <vrf-id>` option.

    If you see errors for expired GPG keys that prevent you from upgrading packages, follow the steps in [Upgrading Expired GPG Keys]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Update-Expired-GPG-Keys" >}}).

3. After the upgrade completes, check if you need to reboot the switch, then reboot the switch if required:

```
    cumulus@switch:~$ nv show system reboot required
    yes
```

If you configured the switch resource mode to half for {{<link url="#issu" text="ISSU">}}, reboot with warm mode for a hitless upgrade:

```
    cumulus@switch:~$ nv action reboot system mode warm
```
If you are not using ISSU, reboot with a {{<link url="System-Power-and-Switch-Reboot/#switch-reboot" text="cold reboot">}}:

```
    cumulus@switch:~$ nv action reboot system
```

4. Verify correct operation with the old configurations on the new version.

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Fetch the latest update metadata from the repository.

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
    ```

If you configured the switch resource mode to half for {{<link url="#issu" text="ISSU">}}, reboot with warm mode for a hitless upgrade:

```
cumulus@switch:~$ sudo csmgrctl -wf
```

If you are not using ISSU, reboot with a {{<link url="System-Power-and-Switch-Reboot/#switch-reboot" text="cold reboot">}}:

```
cumulus@switch:~$ sudo reboot
```

6. Verify correct operation with the old configurations on the new version.

{{< /tab >}}
{{< /tabs >}}

## ONIE Image Upgrade

ONIE is an open source project (equivalent to PXE on servers) that enables the installation of network operating systems (NOS) on a switch. ONIE upgrade enables you to choose the exact release to which you want to upgrade and is the *only* method available to upgrade your switch to a new release train (for example, from 4.4 to 5.15).

{{%notice note%}}
- Installing a Cumulus Linux image with ONIE is destructive; any configuration files on the switch are not saved; copy them to a different server before you start the Cumulus Linux image install.
- You must move configuration data to the new network operating system using ZTP or automation while the operating system is first booted, or soon afterwards using out-of-band management.
- Moving a configuration file can cause issues.
- Identifying all the locations that include configuration data is not always an easy task. See [Before You Upgrade Cumulus Linux](#before-you-upgrade) above.
- Merge conflicts with configuration file changes in the new release sometimes go undetected.
- If configuration files do not restore correctly, you cannot `ssh` to the switch from in-band management. Use out-of-band connectivity (eth0 or the console).
- You *must* reinstall and reconfigure third-party applications after upgrade.
{{%/notice%}}

To upgrade the switch with ONIE:

1. Back up the configurations off the switch.

{{< tabs "TabID189">}}
{{< tab "Back up Configuration with NVUE">}}

If you manage your switch configuration with NVUE, use the following procedure to up the configuration.

As Cumulus Linux supports more features and functionality, NVUE syntax might change between releases and the content of snippets and flexible snippets might become invalid. Before you back up and restore configuration across different Cumulus Linux releases, make sure to review the {{<link url="Whats-New" text="What's New">}} for new NVUE syntax and other configuration file changes.

{{%notice note%}}
- Any certificates or CRLs imported to the system with NVUE are not backed up during an ONIE image upgrade. You must reimport the certificates after the new image is installed. 
- If you reinstall Cumulus Linux with an embedded `startup.yaml` file using `onie-install -t`, Cumulus Linux preserves your NVUE startup configuration and translates the contents automatically to NVUE syntax required by the new release. This method still requires reimporting certificates and CRLs after the image install.
- If NVUE introduces new syntax for a feature that a snippet configures, you must remove the snippet before upgrading.
{{%/notice%}}

To back up the configuration file:

1. Save the configuration to the `/etc/nvue.d/startup.yaml` file with the `nv config save` command:

   ```
   cumulus@switch:~$ nv config save
   saved
   ```

2. Copy the `/etc/nvue.d/startup.yaml` file off the switch to a different location.


For information about the NVUE object model and commands, see {{<link url="NVIDIA-User-Experience-NVUE" text="NVIDIA User Experience - NVUE">}}.


{{< /tab >}}

{{< tab "Back up Linux Configuration Files">}}

If you do not use NVUE to manage your switch configuration, reference this section to back up your configuration files. 

As with other Linux distributions, the `/etc` directory is the primary location for all configuration data in Cumulus Linux. The following list contains the files you need to back up and migrate to a new release. Make sure you examine any changed files. Make the following files and directories part of a backup strategy.

**Network Configuration Files:**

| File Name and Location | Description| Cumulus Linux Documentation | Debian Documentation |
| ---------------------- | ---------- | ----------------------------| -------------------- |
| `/etc/frr/` | Routing application (responsible for BGP and OSPF) | {{<link title="FRRouting">}} | N/A |
| `/etc/hostname` | Configuration file for the hostname of the switch | {{<link title="Quick Start Guide">}} | {{<exlink url="https://wiki.debian.org/HowTo/ChangeHostname">}} |
| `/etc/network/` | Network configuration files, most notably `/etc/network/interfaces` and `/etc/network/interfaces.d/` | {{<link title="Switch Port Attributes">}} | N/A |
| `/etc/resolv.conf` | DNS resolution| Not unique to Cumulus Linux: {{<exlink url="https://wiki.debian.org/NetworkConfiguration#The_resolv.conf_configuration_file" text="wiki.debian.org/NetworkConfiguration">}} | {{<exlink url="https://www.debian.org/doc/manuals/debian-reference/ch05.en.html">}} |
| `/etc/hosts`  | Configuration file for the hostname of the switch | {{<link title="Quick Start Guide">}} | {{<exlink url="https://wiki.debian.org/HowTo/ChangeHostname">}} |
| `/etc/cumulus/acl/*` | Netfilter configuration | {{<link title="Access Control List Configuration">}} |N/A |
| `/etc/cumulus/control-plane/policers.conf` | Configuration for control plane policers | {{<link title="Access Control List Configuration#control-plane-policers">}} | N/A |
| `/etc/cumulus/datapath/qos/qos_features.conf` | QoS configuration <br><br><b>Note:</b> In Cumulus Linux 5.0 and later, default ECN configuration parameters start with `default_ecn_red_conf` instead of `default_ecn_conf`. | {{<link title="Quality of Service">}} | N/A |
| `/etc/mlx/datapath/qos/qos_infra.conf` | QoS configuration | {{<link title="Quality of Service">}} | N/A |
| `/etc/mlx/datapath/tcam_profile.conf` | Configuration for the forwarding table profiles| {{<link title="Forwarding Table Size and Profiles">}} | N/A |
| `/etc/cumulus/datapath/traffic.conf` | Configuration for the forwarding table profiles| {{<link title="Forwarding Table Size and Profiles">}} | N/A |
| `/etc/cumulus/ports.conf` | Breakout cable configuration file | {{<link title="Switch Port Attributes">}} | N/A; read the guide on breakout cables |
| `/etc/cumulus/switchd.conf` | `switchd` configuration | {{<link title="Configuring switchd">}} | N/A; read the guide on `switchd` configuration |


**Commonly Used Files:**

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

**Never Migrate Files:**

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

To show a list of files changed from the previous Cumulus Linux install, run the `sudo dpkg --verify` command.
To show a list of generated `/etc/default/isc-*` files changed from the previous Cumulus Linux install, run the `egrep -v '^$|^#|=""$' /etc/default/isc-dhcp-*` command.

{{< /tab >}}

{{< /tabs >}}

2. Download the Cumulus Linux image.
3. Install the Cumulus Linux image with the `onie-install -a -i <image-location>` command, which boots the switch into ONIE. The following example command installs the image from a web server, defines the current NVUE startup configuration to back up and restore in the new image, then reboots the switch. There are additional ways to install the Cumulus Linux image, such as using FTP, a local file, or a USB drive. For more information, see {{<link title="Installing a New Cumulus Linux Image with ONIE">}}.

    ```
    cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/cumulus-linux-5.15.0-mlx-amd64.bin && sudo reboot
    ```

4. Restore certificates and the configuration files to the new release:

   a. {{<link url="NVUE-CLI/#security-with-certificates-and-crls" text="Reimport all certificates">}} and/or CRLs that were configured in the previous release with the `nv action import system security` command, ensuring you use the same `certificate-id` that was originally assigned to each certificate.

   b. Copy the `/etc/nvue.d/startup.yaml` file from the back up process to the switch.

   c. If required, convert the `startup.yaml` file to the format of the currently running release on the switch. Refer to {{<link url="NVUE-CLI/#translate-a-configuration-revision-or-file" text="Commands to translate a revision or yaml configuration file">}}.

   d. Run the `nv config replace` command, then run the `nv config apply` command. In the following example `startup.yaml` is in the `/home/cumulus` directory on the switch:

   ```
   cumulus@switch:~$ nv config replace /home/cumulus/startup.yaml
   cumulus@switch:~$ nv config apply
   ```

{{%notice infonopad%}}
If you pre-stage your NVUE `startup.yaml` during an {{<link url="Installing-a-New-Cumulus-Linux-Image-with-ONIE/#install-using-a-local-file" text="ONIE image installation from Cumulus Linux">}} with the `onie-install -t` option, certificates and CRLs configured on the switch are not backed up or automatically restored. After the switch boots with the new image, features that rely on certificates (such as NVUE API, gNMI, OTEL, etc.) remain unavailable until the certificates are {{<link url="NVUE-CLI/#security-with-certificates-and-crls" text="reimported">}}. When reimporting certificates and CRLs with the `nv action import system security` command, use the same `certificate-id` that was originally assigned to each certificate in the prior release.
{{%/notice%}}

5. Verify correct operation with the old configurations on the new release.
6. Reinstall third party applications and associated configurations.

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

4. Upgrade the switch:

   - To upgrade the switch with optimized image upgrade, see {{<link url="#image-upgrade" text="Optimized Image Upgrade">}}.
   - To boot the switch into ONIE, see {{<link url="#image-upgrade" text="ONIE Image Install">}}.
   - To upgrade the switch with package upgrade instead of booting into ONIE, see {{<link url="#package-upgrade" text="Package Upgrade">}}.

5. If you installed a new image on the switch, restore the configuration files to the new release. If you performed an upgrade with `apt`, bring the uplink and peer link interfaces you shut down in steps 2 and 3 up:

    ```
    cumulus@switch:~$ nv set interface swp1 link state up
    cumulus@switch:~$ nv set interface peerlink link state up
    cumulus@switch:~$ nv config apply
    cumulus@switch:~$ nv config save
    ```

6. Verify STP convergence across both switches with the Linux `mstpctl showall` command. NVUE does not provide an equivalent command.

    ```
    cumulus@switch:~$ mstpctl showall
    ```

7. Verify core uplinks and peer links are UP:

    ```
    cumulus@switch:~$ nv show interface
    ```

8. Verify MLAG convergence:

    ```
    cumulus@switch:~$ nv show mlag
    ```

9. Make this secondary switch the primary:

    ```
    cumulus@switch:~$ nv set mlag priority 2084
    ```

10. Verify the other switch is now in the secondary role.
11. Repeat steps 2-8 on the new secondary switch.
12. Remove the priority 2048 and restore the priority back to 32768 on the current primary switch:

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

4. Upgrade the switch:

   - To upgrade the switch with optimized image upgrade, see {{<link url="#optimized-image-upgrade" text="Optimized Image Upgrade">}}.
   - To boot the switch into ONIE, see {{<link url="#onie-image-upgrade" text="ONIE Image Upgrade">}}.
   - To upgrade the switch with package upgrade instead of booting into ONIE, see {{<link url="#package-upgrade" text="Package Upgrade">}}.

5. If you installed a new image on the switch, restore the configuration files to the new release.

6. Verify STP convergence across both switches:

    ```
    cumulus@switch:~$ mstpctl showall
    ```

7. Verify that core uplinks and peer links are UP:

    ```
    cumulus@switch:~$ ip addr show
    ```

8. Verify MLAG convergence:

    ```
    cumulus@switch:~$ clagctl status
    ```

9. Make this secondary switch the primary:

    ```
    cumulus@switch:~$ clagctl priority 2048
    ```

10. Verify the other switch is now in the secondary role.
11. Repeat steps 2-9 on the new secondary switch.
12. Remove the priority 2048 and restore the priority back to 32768 on the current primary switch:

    ```
    cumulus@switch:~$ clagctl priority 32768
    ```

{{< /tab >}}
{{< /tabs >}}

## Considerations

- The `/etc/os-release` and `/etc/lsb-release` files update to the currently installed Cumulus Linux release when you upgrade the switch using either *package upgrade* or *Cumulus Linux image install*. For example, if you perform a package upgrade and the latest Cumulus Linux release on the repository is 5.15, these two files display the release as 5.15 after the upgrade.
- The `/etc/image-release` file updates **only** when you run a Cumulus Linux image install. Therefore, if you run a Cumulus Linux image install of Cumulus Linux 5.13, followed by a package upgrade to 5.15, the `/etc/image-release` file continues to display Cumulus Linux 5.13, which is the originally installed base image.
- To downgrade a switch with Secure Boot enabled, see {{<link url="Installing-a-New-Cumulus-Linux-Image-with-ONIE/#downgrade-a-secure-boot-switch" text="Downgrade a Secure Boot Switch">}}.
- If you install any third party applications on a Cumulus Linux switch, configuration data is typically installed in the `/etc` directory, but it is not guaranteed. It is your responsibility to understand the behavior and configuration file information of any third party packages installed on the switch. After you upgrade using a full Cumulus Linux image install, you need to reinstall any third party packages. Package upgrade does **not** replace or remove third-party applications.
