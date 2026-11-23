---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.20 release, and lists new features and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.20, see the {{<link title="Cumulus Linux 5.20 Release Notes" text="Cumulus Linux 5.20 Release Notes">}}.
- To upgrade to Cumulus Linux 5.20, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.20.0

Cumulus Linux 5.20.0 includes new features and improvements, provides bug fixes, and includes a fix for CVE-2026-98432.

{{%notice infonopad%}}
Cumulus Linux 5.20.0 passes testing and validation as part of the Spectrum-X reference architecture release 2.4.

For a list of approved product releases, refer to the {{<exlink url="https://docs.nvidia.com/networking/software/spectrumx-solution-stack/index.html" text="NVIDIA Spectrum-X Validated Solution Stack">}}.
{{%/notice%}}

### New Features and Enhancements

## Release Considerations

Before you upgrade to Cumulus Linux 5.20, review the following considerations.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} to upgrade the switch to Cumulus Linux 5.20 from the following releases.
- 5.17.0, 5.18.0, 5.18.1, 5.18.2, 5.18.3 (with ISSU warm boot)

{{%notice infonopad%}}
- For the SN6600-LD switch, you can upgrade to Cumulus Linux 5.20 only from Cumulus Linux 5.18.3 or later. 
- ISSU is not supported on the SN6600-LD switch.
{{%/notice%}}

To upgrade to Cumulus Linux 5.20 from a release that does not support optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

For a list of the earliest Cumulus Linux releases supported for each switch model, refer to [this knowledge base article]({{<ref "/knowledge-base/Support/Support-Offerings/Minimum-Cumulus-Linux-Release-for-Each-Switch-Model" >}}).

{{%notice infonopad%}}
NVIDIA is discontinuing package upgrade (apt upgrade) in Cumulus Linux 5.20 due to very low adoption, reliability risks, and misalignment with industry best practices.

If you currently use `apt-get upgrade`, `apt-get dist-upgrade`, or apt-based automation in your upgrade runbooks and CI/CD pipelines, plan to migrate to the following upgrade methods:
- Optimized image upgrade (cl-img-install and ISSU) for production.
- ONIE install for initial deployment.
- Patching for targeted fixes.

NVIDIA recommends completing migration before Cumulus Linux 5.20.0.
{{%/notice%}}

### Spectrum-6 BMC Requirements

{{%notice warning%}}
For a Spectrum-6 switch, you must upgrade BMC before you upgrade Cumulus Linux. Before you upgrade to Cumulus Linux 5.20.0, you must upgrade the BMC firmware to version 88.0070.1910 and the ERoT firmware to version 02.00.0048.0000_n05. The ERoT firmware upgrade requires a power cycle of the switch to activate. For information about upgrading BMC, refer to {{<link url="BMC" text="BMC">}}.
{{%/notice%}}

### Linux Configuration Files Overwritten

If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.20.

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.20 or after a new binary image installation:

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

### Link Tracking Customized Files

During optimized image upgrade to Cumulus Linux 5.20, the upgrade process does not carry forward customized `/etc/ifplugd/action.d/ifupdown` and `/etc/default/ifplugd` files by default. The switch uses the default configurations from the new image instead.

To preserve customizations, add a carry-forward entry for each required file in a configuration file under `/etc/cumulus/upgrade-carry-forward.d/` on the partition from which you are upgrading. For example:

```
cumulus@switch:~$ sudo nano /etc/cumulus/upgrade-carry-forward.d/custom.conf
# Customized Files
carry-forward /etc/ifplugd/ifplugd.action
carry-forward /etc/default/ifplugd
```

Refer to {{<link url="Upgrading-Cumulus-Linux/#carry-forward-additional-files" text="Carry Forward Additional Files">}}.

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA DSX Air">}}.
