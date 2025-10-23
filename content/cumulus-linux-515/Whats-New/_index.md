---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.15 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.15, see the {{<link title="Cumulus Linux 5.15 Release Notes" text="Cumulus Linux 5.15 Release Notes">}}.
- To upgrade to Cumulus Linux 5.15, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.15

Cumulus Linux 5.15.0 contains new features and improvements, and provides bug fixes.
### New Features and Enhancements

- {{<link url="Packet-Trimming/#packet-trimming-counters" text="Packet Trimming counters">}}
- {{<link url="Bidirectional-Forwarding-Detection-BFD" text="FRR-based BFD support">}}. Legacy BFD configuration and routing link state verification with PTMd is now deprecated.
- {{<link url="Optional-BGP-Configuration/#ecmp" text="Support 256 BGP sessions and 256-way ECMP on Spectrum-4">}}
- {{<link url="Latency-Monitoring" text="Switch latency monitoring">}}
- {{<link url="Docker-with-Cumulus-Linux" text="Support for docker-container">}}
- {{<link url="802.1X-Interfaces/#dynamic-ipv6-multi-tenancy" text="802.1x Dynamic IPv6 Multi-tenancy">}}
- {{<link url="SSH-for-Remote-Access/#ssh-ciphers" text="SSH cipher configuration">}}
- Offline package upgrade
- RoCE `lossy-multi-tc` {{<link url="RDMA-over-Converged-Ethernet-RoCE/#lossy-multi-tc-profile" text="profile">}} updated to map DSCP values 41-50 to traffic class 5.
- {{<link url="User-Accounts/#aaa-authentication-restrictions" text="AAA Authentication Restrictions">}}
- Telemetry
  - You can now run {{<link url="Open-Telemetry-Export" text="OTLP">}} and {{<link url="gNMI-Streaming" text="gNMI streaming">}} at the same time
  - {{<link url="gNMI-Streaming/#gNOI-operational-commands" text="gNOI operational commands">}}
  - {{<link url="Open-Telemetry-Export/#routing-metrics-format" text="BGP graceful shutdown metric for OLTP">}}
  - {{<link url="Open-Telemetry-Export/#acl-statistics" text="ACL metrics for OTLP">}}
  - {{<link url="gNMI-Streaming/#metrics" text="ACL metrics for gNMI streaming">}}
  - {{<link url="gNMI-Streaming/#metrics" text="PHY metrics for gNMI streaming">}} (Number of bit errors corrected and upper boundary of the bin)
  - High frequency telemetry Nsight Integration
  - Telemetry Parity between OpenTelemetry and gNMI (Phase 1)
  - {{< expand "Updated gNMI PHY metric names" >}}
Old Name | New Name|
| -------- | --------- |
| `/interfaces/interface[name]/ethernet/phy/state/effective-errors` | `/interfaces/interface[name]/phy/state/effective-errors` |
| `/interfaces/interface[name]/ethernet/phy/state/received-bits` | `/interfaces/interface[name]/phy/state/received-bits` |
| `/interfaces/interface[name]/ethernet/phy/state/symbol-errors` | `/interfaces/interface[name]/phy/state/symbol-errors` |
| `/interfaces/interface[name]/ethernet/phy/state/fec-time-since-last-clear` | `/interfaces/interface[name]/phy/fec/state/fec-time-since-last-clear` |
| `/interfaces/interface[name]/ethernet/phy/state/corrected-bits` | `/interfaces/interface[name]/phy/fec/state/corrected-bits` |
| `/interfaces/interface[name]/ethernet/phy/state/rs-fec-no-error-blocks` | `/interfaces/interface[name]/phy/fec/state/rs-fec-no-error-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/rs-fec-single-error-blocks` | `/interfaces/interface[name]/phy/fec/state/rs-fec-single-error-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/rs-fec-uncorrectable-blocks` | `/interfaces/interface[name]/phy/fec/state/rs-fec-uncorrectable-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/ber-time-since-last-clear` | `/interfaces/interface[name]/phy/ber/state/ber-time-since-last-clear` |
| `/interfaces/interface[name]/ethernet/phy/state/effective-ber` | `/interfaces/interface[name]/phy/ber/state/effective-ber` |
| `/interfaces/interface[name]/ethernet/phy/state/symbol-ber` | `/interfaces/interface[name]/phy/ber/state/symbol-ber` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/fc-fec-corrected-blocks` | `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/fc-fec-corrected-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/fc-fec-uncorrected-blocks` | `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/fc-fec-uncorrected-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/rs-fec-corrected-symbols` | `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/rs-fec-corrected-symbols` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/raw-ber` | `/interfaces/interface[name]/phy/channels/channel[id]/ber/state/raw-ber` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/raw-errors` | `/interfaces/interface[name]/phy//channels/channel[id]/state/raw-errors` |
{{< /expand >}}
- NVUE
  - {{<link url="Secure-Mount-Directory-Encryption" text="Secure Mount Directory Encryption">}}
  - {{<link url="New-and-Changed-NVUE-Commands" text="Changed command syntax and output">}}
  - `--expand` option for {{<link url="NVUE-CLI/#view-differences-between-configurations" text="nv config diff command">}}, {{<link url="NVUE-CLI/#show-switch-configuration" text="nv config show command">}}, and {{<link url="NVUE-CLI/#search-for-a-specific-configuration" text="nv config find command">}}
  - `expand=true` parameter for API calls to {{<link url="NVUE-API/#view-differences-between-configurations" text="View differences between configurations">}}, {{<link url="NVUE-API/#view-a-configuration" text="view a configuration">}}, and {{<link url="NVUE-API/#use-filters-in-a-query" text="search for a specific configuration">}}
  - Aging time added to neighbor information
  - Timestamp format in `nv show` command output changed from UTC to duration (days, hour:minutes:seconds)
  - {{<link url="NVUE-API/#patch-a-batch-of-configuration-commands" text="Batch execution support for patching in CLI commands through the API">}}. This feature also improves performance when patching in text commands {{<link url="NVUE-CLI/#replace-and-patch-a-pending-configuration" text="through the CLI">}}.
  - Improved command completion when using tab to view CLI command options

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.15.

### New, Changed, and Deprecated NVUE Commands

{{%notice warning%}}
To align with a long-term vision of a common interface between Cumulus Linux, Nvidia OS (NVOS), and Host-Based Networking, many NVUE commands in Cumulus Linux 5.15 have changed. Before you upgrade to 5.15, review the list of {{<link url="New-and-Changed-NVUE-Commands" text="New, Changed, and Deprecated NVUE Commands">}} and be sure to make any necessary changes to your automation.
{{%/notice%}}

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="optimized image upgrade">}} to upgrade the switch to Cumulus Linux 5.15 from Cumulus Linux 5.12 and later.

You can use {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.15 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- Cumulus Linux 5.14.0
- Cumulus Linux 5.13.1
- Cumulus Linux 5.13.0

To upgrade to Cumulus Linux 5.15 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux includes an option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. If you upgrade to Cumulus Linux 5.15 from 5.12, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.15.

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.15 or after a new binary image installation:

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

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA AIR">}}.
