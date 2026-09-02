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

- NVIDIA SN6600 (128x800G Spectrum-6)
- NVIDIA SN4700 (Spectrum-3)

### New Features and Enhancements

- {{<link url="Inter-subnet-Routing/#prevent-re-export-of-vrf-leaked-evpn-routes" text="Prevent re-export of VRF-leaked EVPN routes">}}
- {{<link url="FRRouting/#class-e-address-space-support" text="Class E (240.0.0.0/4) address space support">}}
- {{<link url="EVPN-Enhancements/#evpn-unreachability-with-8021x-dynamic-vrf-assignment" text="Disjoined multiplane support for EVPN unreachability with 802.1X dynamic VRF assignment">}}
- {{<link url="Upgrading-Cumulus-Linux/#full-resource-mode-issu" text="Full resource mode ISSU on Spectrum-4 and later switches">}} (Beta)
- {{<link url="Bidirectional-Forwarding-Detection-BFD/#offload-to-hardware" text="BFD offload to switch firmware">}}
- {{<link url="Access-Control-List-Configuration/#control-plane-punt-classifier" text="Control plane punt classifier drop counters">}}
- {{<link url="Understanding-the-cl-support-Output-File" text="The cl-support file">}}captures the SSD internal NAND debug log on a switch with a Virtium NVMe SSD
- Layer 3 VXLAN device mode is generally available
- Multi ASIC fast boot support (Beta)
- Packet trimming BTS
- Adaptive Routing Hybrid scheduling mode
- FRR upgrade phase 5
- BMC Host Interface Common Layer
- SN6600 generic part number GA
- VRF per destination support GA
- Support security configurations visibility for manufacturing and field inspection (Phase 1)
- SRv6 Back to sender(BTS) upon link down
- Adaptive Routing - Enable extended grading configuration of AR thresholds through CL profile
- Loopback IP/Interface as Source for NVUE DNS in Cumulus Linux 5.x
- AR-ECMP group segregation for Round Robin per ECMP
- Change the USB0 IP address to 169.254.100.2 / 169.254.100.1
- CPO Debug Params | nv show commands & Telemetry (OTEL and GNMI) GA
- Add step time estimator
- ISSU support for Spectrum-6 - Support More Than 2 RIF MAC Profiles in ISSU Mode
- NVUE
  - {{<link url="System-Power-and-Switch-Reboot" text="Switch power off command">}}
  - {{<link url="Neighbor-Discovery-ND/#clear-a-stale-prefix" text="Clear a stale IPv6 ND prefix on demand">}}
  - {{<link url="BMC/#manage-staged-firmware-files" text="Manage staged platform firmware files, automatic updates, and firmware source per component">}}
  - {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#manage-transceiver-firmware" text="Show and install transceiver firmware">}}
  - {{<link url="Optional-BGP-Configuration/#ipv6-only-unnumbered-peering" text="IPv6-only unnumbered peering command">}}
  - {{<link url="Equal-Cost-Multipath-Load-Sharing/#resilient-hashing" text="Resilient hashing commands">}}
  - {{<link url="NVUE-CLI/#configuration-management-commands" text="nv config apply command improvements">}} to prevent latency and timeout
  - {{<link url="Zero-Touch-Provisioning-ZTP/#suppress-ztp-console-messages" text="Suppress ZTP console messages">}}
  - Map port to connector
  - knob to configure MAX_FDS for FRR
- Telemetry
  - {{<link url="Open-Telemetry-Export/#wjh-metrics" text="WJH metrics for OTEL">}}
  - {{<link url="gNMI-Streaming/#supported-models" text="gNMI component type and name for platform components">}}
  - {{<link url="New-and-Updated-Telemetry-Metrics/#new-gnmi-metrics" text="gNMI and OTEL metrics for unreachability AFI SAFI">}}
  - {{<link url="New-and-Updated-Telemetry-Metrics/#new-gnmi-metrics" text="gNMI metrics for AAA RADIUS">}}
  - uBurst Detection via Per-Port Histograms
  - Support PDB component Telemetry

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.19.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} and {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.19 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- 5.16.1 through 5.16.7
- 5.17.0
- 5.18.0

To upgrade to Cumulus Linux 5.19 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

For a list of the earliest Cumulus Linux releases supported for each switch model, refer to [this knowledge base article]({{<ref "/knowledge-base/Support/Support-Offerings/Minimum-Cumulus-Linux-Release-for-Each-Switch-Model" >}}).

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

### BFD Offload Configuration and Show Output

Cumulus Linux 5.19 replaces the BFD offload boolean with an offload mode that selects where BFD packet processing runs; see {{<link url="Bidirectional-Forwarding-Detection-BFD/#bfd-offload" text="BFD Offload">}}.

- The `nv set router bfd offload <enabled|disabled>` command is replaced by `nv set router bfd offload-mode <control-plane|kernel|hardware>`. When you upgrade, Cumulus Linux translates `offload enabled` to `offload-mode kernel` and removes `offload disabled`, which leaves the `control-plane` default in effect.
- The per-peer offload field now reports the engine carrying the session. In `nv show vrf <vrf-id> router bfd peers` output, the `Offloaded` column shows `kernel`, `hardware`, or `control-plane`; in vtysh and JSON output, `offload-status` shows the same three values. In Cumulus Linux 5.18 and earlier, this field shows only `offloaded` or `control-plane`. Update any automation or monitoring that matches on the string `offloaded`.

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA DSX Air">}}.
