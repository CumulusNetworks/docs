---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.18 release, and lists new features and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.18, see the {{<link title="Cumulus Linux 5.18 Release Notes" text="Cumulus Linux 5.18 Release Notes">}}.
- To upgrade to Cumulus Linux 5.18, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.18

Cumulus Linux 5.18 supports new platforms, contains new features and improvements, and provides bug fixes.

## Platforms

- NVIDIA SN5800-LD (400G Spectrum-5 Multi-ASIC)
- NVIDIA SN5810-LD (400G Spectrum-5 Single ASIC)
- NVIDIA SN6600_LD (800G Spectrum-6) Beta
- NVIDIA SN5800-LD (800G Spectrum-6 Multi-ASIC)
- NVIDIA SN5810-LD (800G Spectrum-6 Single ASIC)

### New Features and Enhancements

- Kernel update to Debian 6.1.174-1
- {{<link url="Quality-of-Service/#lossless-headroom-based-on-small-packet-probability" text="Lossless headroom size based on small packet probability">}} is generally available
- {{<link url="Quality-of-Service/#dynamic-ecn" text="Dynamic ECN">}} is generally available
- {{<link url="EVPN-Enhancements/#evpn-unreachability-in-disjoined-planes" text="EVPN Unreachability in Disjoined Planes">}} are generally available
- {{<link url="Link-Layer-Discovery-Protocol/#bgp-unreachable-prefix-tlv" text="BGP unreachable prefix TLV">}} is generally available
- {{<link url="Profile-Based-Configuration" text="Profile-based switch configuration">}}
- {{<link url="RDMA-over-Converged-Ethernet-RoCE/#data-center-interconnect-(dci-1)-profile" text="Data Center Interconnect (DCI-1) QoS profile">}}
- {{<link url="Interface-Configuration-and-Management/#apsu-and-link-precoding-control" text="APSU and link precoding control">}}
- {{<link url="Bidirectional-Forwarding-Detection-BFD/#bfd-offload-to-firmware" text="BFD offload to firmware">}}
- Changes to the `/etc/frr/daemons` file no longer require an FRR service restart; you can use FRR reload
- Layer 3 VXLAN interface
- EVPN Multihoming and MLAG without a unique SVI IP address
- Xplane extensions
- Advertise BOTH SAFI 254 AND SAFI 81 in capability negotiation
- NVUE
  - {{<link url="VLAN-aware-Bridge-Mode/#configure-the-default-vlan-identifier" text="Configure the default VLAN Identifier">}}
  - {{<link url="Interface-Configuration-and-Management/#uplink-tracking" text="Uplink tracking ">}}
  - {{<link title="What Just Happened (WJH)" text="WJH commands to filter packets, set latency and congestion thresholds, control aggregation interval and cache size, and export to a PCAP file ">}}
  - {{<link url="Managing-Cumulus-Linux-Disk-Images-with-ONIE" text="NVUE commands for binary image installation (onie-install)">}}
  - {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#amber-phy-health-management" text="nv show interface --ber command to show PHY health statistics for all interfaces ">}}
  - {{<link url="Switch-Port-Attributes/#show-module-information" text="nv show interface --dom command to show transceiver information for all interfaces">}}
  - {{<link url="NVUE-CLI/#show-specific-configuration" text="Show specific configuration on the switch">}}
  - {{<link url="BMC" text="BMC commands">}}
  - {{<link url="New-and-Removed-NVUE-Commands/" text="New NVUE command list">}}
- Security
  - {{<link url="User-Accounts/#password-security" text="Password policy setting for minimum password character difference between the current and new password">}}
  - {{<link url="VLAN-aware-Bridge-Mode/#configure-the-default-vlan-identifier" text="Configure the default VLAN identifier">}}
  - {{<link url="VLAN-aware-Bridge-Mode/#dynamic-arp-inspection" text="Dynamic ARP inspection">}}
  - {{<link title="Automatic Configuration Backup" text="Automatic Snapshots">}}
  - {{<link url="VLAN-aware-Bridge-Mode/#ip-source-guard" text="IP Source Guard">}}
- Telemetry
  - New OTEL metrics: {{<link url="Open-Telemetry-Export/#platform-statistic-format" text="ASIC">}}
  - New gNMI metrics: {{<link url="gNMI-Streaming/#metrics" text="ASIC">}}
  - {{<link url="Open-Telemetry-Export/#granular-metric-selection" text="OTEL granular metric selection">}} is generally available
  - What Just Happened gNMI metrics
  - Support 802.1x RADIUS GNMI metrics

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.18.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} and {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.18 from Cumulus Linux 5.16 and later. Package upgrade supports ISSU (warm boot) for these upgrade paths.

{{%notice note%}}
The Spectrum-6 switch does not support ISSU.
{{%/notice%}}

To upgrade to Cumulus Linux 5.18 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux includes an option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. If you upgrade to Cumulus Linux 5.18 from 5.12 or earlier, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.18.

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.18 or after a new binary image installation:

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

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA DSX Air">}}.
