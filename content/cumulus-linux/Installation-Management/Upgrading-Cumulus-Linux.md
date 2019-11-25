---
title: Upgrading Cumulus Linux
author: Cumulus Networks
weight: 45
aliases:
 - /display/DOCS/Upgrading+Cumulus+Linux
 - /pages/viewpage.action?pageId=8366370
product: Cumulus Linux
version: '4.0'
---

This topic describes how to upgrade Cumulus Linux on your switch.

Cumulus Networks recommends that you deploy, provision, configure, and upgrade switches using automation, even with small networks or test labs. During the upgrade process, you can quickly upgrade dozens of devices in a repeatable manner. Using tools like Ansible, Chef, or Puppet for configuration management greatly increases the speed and accuracy of the next major upgrade; these tools also enable the quick swap of failed switch hardware.

## Before You Upgrade

{{%notice tip%}}

Be sure to read the knowledge base article [Upgrades: Network Device and Linux Host Worldview Comparison](https://support.cumulusnetworks.com/hc/en-us/articles/360010451353), which provides a detailed comparison between the network device and Linux host worldview of upgrade and installation.

{{%/notice%}}

Understanding the location of configuration data is required for successful upgrades, migrations, and backup. As with other Linux distributions, the `/etc` directory is the primary location for all configuration data in Cumulus Linux. The following list is a likely set of files that you need to back up and migrate to a new release. Make sure you examine any file that has been changed. Cumulus Networks recommends you consider making the following files and directories part
of a backup strategy.

<details>

<summary>Network Configuration Files </summary>

| File Name and Location | Explanation| Cumulus Linux Documentation | Debian Documentation |
| ---------------------- | ---------- | ----------------------------| -------------------- |
| `/etc/network/` | Network configuration files, most notably `/etc/network/interfaces` and `/etc/network/interfaces.d/` | [Switch Port Attributes](../../Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes/) | N/A |
| `/etc/resolv.conf` | DNS resolution|Not unique to Cumulus Linux: [wiki.debian.org/NetworkConfiguration](https://wiki.debian.org/NetworkConfiguration#The_resolv.conf_configuration_file) | [www.debian.org/doc/manuals/debian-reference/ch05.en.html](https://www.debian.org/doc/manuals/debian-reference/ch05.en.html) |
| `/etc/frr/` | Routing application (responsible for BGP and OSPF) | [FRRouting Overview](../../Layer-3/FRRouting-Overview/)| N/A |
| `/etc/hostname` | Configuration file for the hostname of the switch | [Quick Start Guide](../../Quick-Start-Guide/)| [wiki.debian.org/HowTo/ChangeHostname](https://wiki.debian.org/HowTo/ChangeHostname) |
| `/etc/cumulus/acl/*` | Netfilter configuration | [Netfilter - ACLs](../../System-Configuration/Netfilter-ACLs/) |N/A |
| `/etc/cumulus/ports.conf` | Breakout cable configuration file | [Switch Port Attributes](../../Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes/) | N/A; read the guide on breakout cables |
| `/etc/cumulus/switchd.conf` | Switchd configuration | [Configuring switchd](../../System-Configuration/Configuring-switchd/) | N/A; read the guide on switchd configuration |

{{%notice note%}}

If you are using the root user account, consider including `/root/`.

If you have custom user accounts, consider including `/home/<username>/`.

{{%/notice%}}

</details>

<details>

<summary>Additional Commonly Used Files </summary>

| File Name and Location | Explanation| Cumulus Linux Documentation | Debian Documentation |
| ---------------------- | ---------- | --------------------------- | -------------------- |
| `/etc/motd` |Message of the day |Not unique to Cumulus Linux |[wiki.debian.org/motd](https://wiki.debian.org/motd#Wheezy) |
| `/etc/passwd` | User account information |Not unique to Cumulus Linux | [www.debian.org/doc/manuals/debian-reference/ch04.en.html](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html) |
| `/etc/shadow` | Secure user account information|Not unique to Cumulus Linux | [www.debian.org/doc/manuals/debian-reference/ch04.en.html](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html) |
| `/etc/group` | Defines user groups on the switch|Not unique to Cumulus Linux | [www.debian.org/doc/manuals/debian-reference/ch04.en.html](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html) |
| `/etc/lldpd.conf` | Link Layer Discover Protocol (LLDP) daemon configuration |[Link Layer Discovery Protocol](../../Layer-2/Link-Layer-Discovery-Protocol/) | [packages.debian.org/wheezy/lldpd](https://packages.debian.org/wheezy/lldpd) |
| `/etc/lldpd.d/` | Configuration directory for lldpd | [Link Layer Discovery Protocol](../../Layer-2/Link-Layer-Discovery-Protocol/) | [packages.debian.org/wheezy/lldpd](https://packages.debian.org/wheezy/lldpd) |
| `/etc/nsswitch.conf` | Name Service Switch (NSS) configuration file | [TACACS Plus](../../System-Configuration/Authentication-Authorization-and-Accounting/TACACS+/) |N/A |
|`/etc/ssh/` | SSH configuration files |[SSH for Remote Access](../../System-Configuration/Authentication-Authorization-and-Accounting/SSH-for-Remote-Access/) | [wiki.debian.org/SSH](https://wiki.debian.org/SSH) |
| `/etc/sudoers`, `/etc/sudoers.d` | Best practice is to place changes in `/etc/sudoers.d/` instead of `/etc/sudoers`; changes in the `/etc/sudoers.d/` directory are not lost during upgrade. | [Using sudo to Delegate Privileges](../../System-Configuration/Authentication-Authorization-and-Accounting/Using-sudo-to-Delegate-Privileges/) |

{{%notice note%}}

If you are using the root user account, consider including `/root/`. If you have custom user accounts, consider including `/home/<username>/`.

{{%/notice%}}

</details>

<details>

<summary>Never Migrate these Files between Versions or Switches</summary>

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

</details>

If you are using certain forms of network virtualization, including [VMware NSX-V](../../Network-Virtualization/Virtualization-Integrations/Integrating-Hardware-VTEPs-with-VMware-NSX-V/) or [Midokura MidoNet](../../Network-Virtualization/Virtualization-Integrations/Integrating-Hardware-VTEPs-with-Midokura-MidoNet-and-OpenStack/), you might have updated the `/usr/share/openvswitch/scripts/ovs-ctl-vtep` file. This file is not marked as a configuration file; therefore, if the
file contents change in a newer release of Cumulus Linux, they overwrite any changes you made to the file. Be sure to back up this file and the database file `conf.db` before upgrading.

{{%notice note%}}

You can check which files have changed since the last binary install with the following commands. Be sure to back up any changed files:

- Run the `sudo dpkg --verify` command to show a list of changed files.
- Run the `egrep -v '^$|^#|=""$' /etc/default/isc-dhcp-*` command to see if any of the generated `/etc/default/isc-*` files have changed.

{{%/notice%}}

## Upgrade Cumulus Linux

To upgrade to Cumulus Linux 4.0 from Cumulus Linux 3.7, you must install a disk image of the new release using ONIE. You *cannot* upgrade packages with the `apt-get upgrade` command.

ONIE is an open source project (equivalent to PXE on servers) that enables the installation of network operating systems (NOS) on a bare metal switch.

{{%notice note%}}

Upgrading an MLAG pair requires additional steps. If you are using MLAG to dual connect two Cumulus Linux switches in your environment, follow the steps in [Upgrade Switches in an MLAG Pair](#upgrade-switches-in-an-mlag-pair) below to ensure a smooth upgrade.

{{%/notice%}}

{{%notice note%}}

Cumulus Networks deprecated lightweight network virtualization (LNV) in Cumulus Linux 4.0 in favor of Ethernet virtual private networks ([EVPN](../../Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/)).
If your network is configured for LNV, you need to migrate your network configuration to a BGP EVPN configuration that is functionally equivalent ***before*** you upgrade to Cumulus Linux 4.0. Refer
[Migrating from LNV to EVPN](../Migrating-from-LNV-to-EVPN/).

{{%/notice%}}

Be aware of the following when installing the disk image:

- Installing a disk image is destructive; any configuration files on the switch are not saved; copy them to a different server before you start installation.
- You must move configuration data to the new OS using ZTP or automation while the OS is first booted, or soon afterwards using out-of-band management.
- Moving a configuration file might cause issues:
  - Identifying all the locations of configuration data is not always an easy task. See [Before You Upgrade](#before-you-upgrade) above.
  - Merge conflicts with configuration file changes in the new release might go undetected.
- If configuration files are not restored correctly, you might be unable to `ssh` to the switch from in-band management. Out-of-band connectivity (eth0 or console) is recommended.
- You *must* reinstall and reconfigure third-party applications after upgrade.

To upgrade the switch:

1. Back up the configurations off the switch.
2. Download the Cumulus Linux image.
3. Install the disk image with the `onie-install -a -i <image-location>` command, which boots the switch into ONIE. The following example command installs the image from a web server, then reboots the switch. There are additional ways to install the disk image, such as using FTP, a local file, or a USB drive. For more information, see [Installing a New Cumulus Linux Image](../Installing-a-New-Cumulus-Linux-Image/).

```
cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/cumulus-linux-4.0.0-mlx-amd64.bin && sudo reboot
```

4. Restore the configuration files to the new release — ideally with automation.
5. Verify correct operation with the old configurations on the new release.
6. Reinstall third party applications and associated configurations.

## Upgrade Switches in an MLAG Pair

If you are using [MLAG](../../Layer-2/Multi-Chassis-Link-Aggregation-MLAG/)
to dual connect two switches in your environment, follow the steps below to upgrade the switches:

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

4. Run the `onie-install -a -i <image-location>` command to boot the switch into ONIE. The following example command installs the image from a web server. There are additional ways to install the disk image, such as using FTP, a local file, or a USB drive. For more information, see [Installing a New Cumulus Linux Image](../Installing-a-New-Cumulus-Linux-Image/).

```
cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/downloads/cumulus-linux-4.0.0-mlx-amd64.bin
```

5. Reboot the switch:

```
cumulus@switch:~$ sudo reboot
```

6. Verify STP convergence across both switches:

```
cumulus@switch:~$ mstpctl showall
```

7. Verify core uplinks and peer links are UP:

```
cumulus@switch:~$ net show interface
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
11. Repeat steps 2-8 on the new secondary switch.
12. Remove the priority 2048 and restore the priority back to 32768 on the current primary switch:

```
cumulus@switch:~$ clagctl priority 32768
```

## Roll Back a Cumulus Linux Installation

Even the most well planned and tested upgrades can result in unforeseen problems; sometimes the best solution is to roll back to the previous state. There are three main strategies; all require detailed planning and
execution:

- Flatten and rebuild: If the OS becomes unusable, you can use orchestration tools to reinstall the previous OS release from scratch and then rebuild the configuration automatically.
- Backup and restore: Another common strategy is to restore to a previous state using a backup captured before the upgrade. See [Back up and Restore](../Back-up-and-Restore/).

The method you employ is specific to your deployment strategy, so providing detailed steps for each scenario is outside the scope of this document.

## Third Party Packages

Third party packages in the *Linux host* world often use the same package system as the distribution into which it is to be installed (for example, Debian uses `apt-get`). Or, the package might be compiled and
installed by the system administrator. Configuration and executable files generally follow the same filesystem hierarchy standards as other applications.

If you install any third party applications on a Cumulus Linux switch, configuration data is typically installed into the `/etc` directory, but it is not guaranteed. It is your responsibility to understand the
behavior and configuration file information of any third party packages installed on the switch.

After you upgrade using a full disk image install, you need to reinstall any third party packages or any Cumulus Linux add-on packages.

## Related Information

- [Upgrades: Network Device Worldview and Linux Host Worldview Comparison](https://support.cumulusnetworks.com/hc/en-us/articles/360010451353)
- [Automation Solutions](https://cumulusnetworks.com/solutions/automation/)
- [ONIE Design Specification](http://opencomputeproject.github.io/onie/design-spec/)
- [Multi-Chassis Link Aggregation - MLAG](../../Layer-2/Multi-Chassis-Link-Aggregation-MLAG/)
- [Zero Touch Provisioning - ZTP](../Zero-Touch-Provisioning-ZTP/)
