---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.19 release, and lists new features and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.19, see the {{<link title="Cumulus Linux 5.19 Release Notes" text="Cumulus Linux 5.19 Release Notes">}}.
- To upgrade to Cumulus Linux 5.19, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.19.0

Cumulus Linux 5.19.0 supports new platforms, contains new features and improvements, and provides bug fixes.

{{%notice infonopad%}}
Cumulus Linux 5.19.0 is currently only qualified for **non-Spectrum-X**.
{{%/notice%}}

## Platforms

### New Features and Enhancements

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.19.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} and {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.19 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- 5.16.1 through 5.16.7
- 5.17.0
- 5.18.0

To upgrade to Cumulus Linux 5.19 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

For a list of the earliest Cumulus Linux releases supported for each switch model, refer to [this knowledge base article]({{<ref "/knowledge-base/Support/Support-Offerings/Minimum-Cumulus-Linux-Release-for-Each-Switch-Model" >}}).

### Maximum Number of NVUE Revisions

Cumulus Linux includes an option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. If you upgrade to Cumulus Linux 5.19 from 5.12 or earlier, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.19.

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.19 or after a new binary image installation:

1.  Disable NVUE auto save:

   ```
   cumulus@switch:~$ nv set system config auto-save state disabled
   cumulus@switch:~$ nv config apply
   cumulus@switch:~$ nv config save
   ```

2. Delete the `/etc/nvue.d/startup.yaml` file:

   ```
   cumulus@switch:~$ sudo rm -rf /etc/nvue.d/startup.yaml
   ```

3. Add the `PASSWORD_NVUE_SYNC=no` line to the `/etc/default/nvued` file:
   ```
   cumulus@switch:~$ sudo nano /etc/default/nvued
   PASSWORD_NVUE_SYNC=no
   ```

### DHCP Lease with the host-name Option

When a Cumulus Linux switch with NVUE enabled receives a DHCP lease containing the host-name option, it ignores the received hostname and does not apply it. For details, see this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Hostname-Option-Received-From-DHCP-Ignored" >}}).

### NVUE Commands After Upgrade

After you upgrade to Cumulus Linux, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

### nv show vrf \<vrf-id\> router bgp address-family \<address-family\>-unreachability route -o json Command

In Cumulus Linux 5.18 and later, running the `nv show vrf <vrf-id> router bgp address-family <address-family>-unreachability route -o json` command is now equivalent to running the vtysh `show bgp vrf <vrf-id> ipv6 unreachability json brief` command. Therefore, certain fields, such as path details and reporter AS, no longer show. To show a more detailed view, run the `nv show vrf <vrf-id> router bgp address-family <address-family>-unreachability route <prefix> -o json` command.

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA DSX Air">}}.
