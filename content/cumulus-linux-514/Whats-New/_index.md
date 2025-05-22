---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.14 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.14, see the {{<link title="Cumulus Linux 5.14 Release Notes" text="Cumulus Linux 5.14 Release Notes">}}.
- To upgrade to Cumulus Linux 5.14, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.14

Cumulus Linux 5.14.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN5640 (800G Spectrum-5) BETA

### New Features and Enhancements

- {{<link url="Switch-Port-Attributes/#auto-negotiation-and-link-speed" text="Speed setting without auto-negotiation">}}
- {{<link title="Erase all Data from the Switch" text="Erase all data from the switch">}} now generally available
- Map port to connector
- Operational revision
- EVPN info across all VRFs
- Configure different DHCP relay servers per interface
- NVUE login brute force via API
- FRR upgrade to 10.x via API
- Clear layer 1 PCS/phy detail link counters
- gNMI requirements phase 4
- FIPS 140-2 and 3 approved crypto modules
- Crypto mechanisms to prevent unauthorized modification of all information 
- Strong authenticators
- MRC:
  - {{<link url="Quality-of-Service/#configure-mrc-with-default-settings" text="Packet trimming and SRv6">}}
  - {{<link url="RDMA-over-Converged-Ethernet-RoCE/#mrc-qos-profile" text="New QoS profile for MRC">}}
  - {{<link url="Quality-of-Service/#asymmetric-packet-trimming" text="Packet trimming with asymmetric DSCP">}}
- NVUE
  - {{< expand "Changed NVUE Commands" >}}
| Cumulus Linux 5.14 | Cumulus Linux 13 and Earlier |
| --------------- |---------------------------------------|
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |

{{< /expand >}}
  - {{< expand "Removed NVUE Commands" >}}
```

```
{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```

```

{{< /tab >}}
{{< tab "nv set ">}}

```

```

{{< /tab >}}
{{< tab "nv unset ">}}

```

```

{{< /tab >}}
{{< tab "nv action ">}}

```

```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.14.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="optimized image upgrade">}} to upgrade the switch to Cumulus Linux 5.14 from Cumulus Linux 5.12.0 and later.

You can use {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.14 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- Cumulus Linux 5.13.0
- Cumulus Linux 5.13.1
- Cumulus Linux 5.12.0
- Cumulus Linux 5.12.1

To upgrade to Cumulus Linux 5.14 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux 5.13 and later includes a new option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. After upgrading to Cumulus Linux 5.14 from 5.12, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

{{%notice warning%}}
If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.14 or later.
{{%/notice%}}

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.14 or later, or after a new binary image installation:

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

Cumulus Linux 5.14 includes the NVUE object model. After you upgrade to Cumulus Linux 5.14, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA AIR">}}.
