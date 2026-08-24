---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.18 release, and lists new features and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.18, see the {{<link title="Cumulus Linux 5.18 Release Notes" text="Cumulus Linux 5.18 Release Notes">}}.
- To upgrade to Cumulus Linux 5.18, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.18.1

Cumulus Linux 5.18.1 provides bug fixes.

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} and {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.18.1 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- 5.16.0, 5.16.1, 5.16.5, 5.16.6, 5.16.7
- 5.17.0
- 5.18.0

## What's New in Cumulus Linux 5.18.0

Cumulus Linux 5.18.0 supports new platforms, contains new features and improvements, and provides bug fixes.

{{%notice infonopad%}}
Cumulus Linux 5.18.0 is currently only qualified for **non-Spectrum-X**.
{{%/notice%}}

## Platforms
- {{<exlink url="https://docs.nvidia.com/nvidia-spectrum-6-sn6000-ethernet-switch-systems-hardware-user-manual.pdf" text="NVIDIA SN6600_LD">}} (128x800G Spectrum-6)

{{%notice note%}}
The NVIDIA SN6600_LD switch does not support:
- Port speed 800Gx8
- Warmboot
- PTP
{{%/notice%}}

Cumulus Linux 5.18.0 is the earliest release in which the NVIDIA SN6600_LD switch is generally available. You must upgrade any engineering sample to Cumulus Linux 5.18 with ONIE.

### New Features and Enhancements
- Kernel update to Debian 6.1.174
- {{<link url="Quality-of-Service/#lossless-headroom-based-on-small-packet-probability" text="Lossless headroom size based on small packet probability">}} is generally available
- {{<link url="Quality-of-Service/#dynamic-ecn" text="Dynamic ECN">}} is generally available
- {{<link url="EVPN-Enhancements/#evpn-unreachability-in-disjoined-planes" text="EVPN Unreachability in Disjoined Planes">}} is generally available
- {{<link url="Link-Layer-Discovery-Protocol/#bgp-unreachable-prefix-tlv" text="BGP unreachable prefix TLV">}} is generally available
- {{<link url="Interface-Configuration-and-Management/#link-tracking" text="Link tracking ">}}
- {{<link url="EVPN-Multihoming/#svi-ip-address-configuration" text="EVPN Multihoming without a unique SVI IP address">}}
- {{<link url="RADIUS-AAA/#nas-ip-address-and-identifier" text="RADIUS NAS IP address and identifier configuration">}}
- {{<link url="Inter-subnet-Routing/#layer-3-vxlan-device-mode" text="Layer 3 VXLAN device mode">}} (Beta)
- {{<link url="Profile-Based-Configuration" text="Profile-based switch configuration">}} (Beta)
- {{<link url="Patches" text="Patch infrastructure">}}
- {{<link url="RDMA-over-Converged-Ethernet-RoCE/#dci-1-profile" text="Data Center Interconnect (DCI-1) QoS profile">}} (Beta)
- {{<link url="Optional-BGP-Configuration/#bgp-unreachability-safi" text="BGP Unreachability SAFI uses the IANA assigned value of 81 instead of a private value">}} (Beta)
- {{<link url="Optional-BGP-Configuration/#graceful-fabric-maintenance" text="BGP graceful fabric maintenance">}} (Beta)
- {{<link url="Optional-BGP-Configuration/#inter-dc-routing" text="Inter-DC Routing">}} (Beta)
- {{<link url="Forwarding-Table-Size-and-Profiles/#spectrum-6" text="Spectrum-6 forwarding resource profiles">}} 
- NVUE
  - {{<link url="NVUE-CLI/#automatic-configuration-backup-and-restore" text="Automatic configuration backup and restore">}}
  - {{<link title="What Just Happened (WJH)" text="WJH commands to filter packets, set latency and congestion thresholds, control aggregation interval and cache size, and export to a PCAP file ">}}
  - {{<link url="Managing-Cumulus-Linux-Disk-Images-with-ONIE" text="NVUE commands for binary image installation (onie-install)">}}
  - {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#amber-phy-health-management" text="nv show interface --ber command to show PHY health statistics for all interfaces ">}}
  - {{<link url="Switch-Port-Attributes/#show-module-information" text="nv show interface --dom command to show transceiver information for all interfaces">}} (Beta)
  - {{<link url="NVUE-CLI/#show-specific-configuration" text="NVUE command to show specific configuration on the switch">}} and {{<link url="NVUE-API/#view-specific-configuration" text="NVUE API query parameter to show specific configuration on the switch">}}
  - {{<link url="BMC" text="BMC commands for Spectrum-6 switches">}}
  - {{<link url="RADIUS-AAA/#show-and-clear-radius-counters" text="NVUE commands to show and clear RADIUS counters">}}
  - {{<link url="Resource-Diagnostics/#clear-resource-metrics" text="NVUE action command to clear resource metrics for a specific ASIC">}}
  - {{<link url="Resource-Diagnostics/#monitor-routes-in-cumulus-linux-hardware" text="Updated nv show platform asic <asic-id> resource command output">}}
  - Applying FRR configuration changes to the `/etc/frr/daemons` file with NVUE now results in an FRR reload instead of an FRR restart, minimizing service disruption.
  - {{<link url="New-and-Removed-NVUE-Commands/" text="New NVUE command list">}}
- Security
  - {{<link url="User-Accounts/#password-security" text="Password policy setting for minimum password character difference">}}
  - {{<link url="User-Accounts/#password-security" text="Password hardening is now disabled by default">}}
  - {{<link url="VLAN-aware-Bridge-Mode/#configure-the-default-vlan-identifier" text="Configure the default VLAN identifier">}}
  - {{<link url="VLAN-aware-Bridge-Mode/#dynamic-arp-inspection" text="Dynamic ARP inspection">}}
  - {{<link url="IP-Source-Guard" text="IP Source Guard">}}
- Telemetry
  - New OTEL metrics: {{<link url="New-and-Updated-Telemetry-Metrics/#new-otel-metrics" text="802.1X RADIUS, ASIC resource, platform leakage sensor, platform power supply (to support Spectrum-6), and patch updates">}}
  - New gNMI metrics: {{<link url="New-and-Updated-Telemetry-Metrics/#new-gnmi-metrics" text="802.1X RADIUS, ASIC resource, WJH, Platform leakage sensor, platform power supply (to support Spectrum-6), and patch updates">}}
  - {{<link url="Open-Telemetry-Export/#granular-metric-selection" text="OTEL granular metric selection">}} is generally available
  - You can now run both {{<link title="What Just Happened (WJH)" text="NVUE WJH commands">}} and {{<link url="gNMI-Streaming" text="subscribe to gNMI YANG paths">}} at the same time.

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.18.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} and {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.18.0 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- 5.16.0
- 5.16.1
- 5.16.5
- 5.16.6
- 5.17.0

{{%notice note%}}
The Spectrum-6 switch does not support ISSU.
{{%/notice%}}

To upgrade to Cumulus Linux 5.18.0 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

For a list of the earliest Cumulus Linux releases supported for each switch model, refer to [this knowledge base article]({{<ref "/knowledge-base/Support/Support-Offerings/Minimum-Cumulus-Linux-Release-for-Each-Switch-Model" >}}).
<!--
### TACACS and RADIUS Upgrade

When you upgrade the switch to Cumulus Linux 5.18 from Cumulus Linux 5.16.7, package upgrade does not upgrade the TACACS and RADIUS packages. You must run package upgrade a second time with the `apt-get update && apt-get upgrade` command or run the NVUE `nv action upgrade system packages` command.
-->
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

### nv show vrf \<vrf-id\> router bgp address-family \<address-family\>-unreachability route -o json Command

In Cumulus Linux 5.18, running the `nv show vrf <vrf-id> router bgp address-family <address-family>-unreachability route -o json` command is now equivalent to running the vtysh `show bgp vrf <vrf-id> ipv6 unreachability json brief` command. Therefore, certain fields, such as path details and reporter AS, no longer show. To show a more detailed view, run the `nv show vrf <vrf-id> router bgp address-family <address-family>-unreachability route <prefix> -o json` command.

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA DSX Air">}}.
