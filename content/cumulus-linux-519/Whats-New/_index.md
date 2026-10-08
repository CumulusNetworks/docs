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

Cumulus Linux 5.19.0 includes new features and improvements, and provides bug fixes.

{{%notice infonopad%}}
Cumulus Linux 5.19.0 is currently only qualified for **non-Spectrum-X**.
{{%/notice%}}

### New Features and Enhancements

- {{<link url="Inter-subnet-Routing/#prevent-re-export-of-vrf-leaked-evpn-routes" text="Prevent re-export of VRF-leaked EVPN routes">}}
- {{<link url="FRRouting/#class-e-address-space-support" text="Class E (240.0.0.0/4) address space support">}}
- {{<link url="EVPN-Enhancements/#evpn-unreachability-with-8021x-dynamic-vrf-assignment" text="Disjoined multiplane support for EVPN unreachability with 802.1X dynamic VRF assignment">}}
- {{<link url="Inter-subnet-Routing/#layer-3-vxlan-device-mode" text="Layer 3 VXLAN device mode">}} is generally available
- {{<link url="System-Power-and-Switch-Reboot" text="Multi ASIC fast boot support">}} (Beta)
- {{<link url="Upgrading-Cumulus-Linux/#full-resource-mode-issu" text="Full resource mode ISSU on Spectrum-4 and later switches">}} (Beta)
- {{<link url="Bidirectional-Forwarding-Detection-BFD/#offload-to-hardware" text="BFD offload to switch firmware">}}
- {{<link url="Access-Control-List-Configuration/#control-plane-punt-classifier" text="Control plane punt classifier drop counters">}}
- {{<link url="Understanding-the-cl-support-Output-File/#collect-the-nvme-nand-debug-log" text="The cl-support file">}} captures the SSD internal NAND debug log on a switch with a Virtium NVMe SSD
- {{<link url="Patches" text="Patch uninstall returns the switch to the patch installed underneath, and a new command reclaims the space held by superseded patches">}}
- {{<link url="Quality-of-Service/#pfc-watchdog" text="PFC watchdog detection parameters that distinguish a real deadlock from steady-state congestion">}}
- {{<link url="Security-Configuration-Visibility" text="Security configuration visibility for manufacturing and field inspection">}}
- {{<link url="Packet-Trimming/#back-to-sender-notification-on-congestion-tail-drop" text="Back-to-sender notification on congestion tail drop">}} on Spectrum-6 switches
- {{<link url="Packet-Trimming/#back-to-sender-notification-on-link-down" text="Back-to-sender notification when an MRC egress link fails">}}
- {{<link url="Equal-Cost-Multipath-Load-Sharing/#extended-grading" text="Adaptive routing extended grading on Spectrum-6 switches">}}
- {{<link url="High-Frequency-Telemetry/#step-time-estimation" text="Step time estimation for AI training workloads">}}
- {{<link url="Equal-Cost-Multipath-Load-Sharing/#ecmp-group-segregation" text="Adaptive routing ECMP group segregation for round-robin port selection on Spectrum-6 switches">}}
- {{<link url="Quality-of-Service/#service-port-buffers" text="Dedicated service port ingress buffers on Spectrum-6 switches">}}
- {{<link url="Equal-Cost-Multipath-Load-Sharing/#resource-mode-and-hybrid-scheduling" text="Adaptive routing hybrid scheduling mode, which moves low weight ECMP groups to random forwarding to reduce adaptive routing group merging">}}
- {{<link url="Domain-Name-System-DNS/#dns-query-source-address" text="Configurable source address for DNS queries, so that queries leave the switch from a stable loopback identity">}}
- {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#show-cpo-module-and-laser-source-information" text="CPO module and laser source visibility on switches with co-packaged optics">}}
- {{<link url="Packet-Trimming/#packet-trimming-counters" text="Trimmed packet sent and dropped counters at the global, port, and traffic class level">}} on Spectrum-6 switches
- NVUE
  - {{<link url="Using-sudo-to-Delegate-Privileges" text="Passwordless sudo access by default">}} for members of the sudo group, and {{<link url="Role-Based-Access-Control/#os-command-classes" text="RBAC os-command allow-lists">}} for granular passwordless access to specific commands (Beta)
  - {{<link url="System-Power-and-Switch-Reboot" text="Switch power off command">}}
  - {{<link url="Neighbor-Discovery-ND/#clear-a-stale-prefix" text="Clear a stale IPv6 ND prefix on demand">}}
  - {{<link url="BMC/#manage-staged-firmware-files" text="Manage staged platform firmware files, automatic updates, and firmware source per component">}}
  - {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#manage-transceiver-firmware" text="Show and install transceiver firmware">}}
  - {{<link url="Optional-BGP-Configuration/#ipv6-only-unnumbered-peering" text="IPv6-only unnumbered peering command">}}
  - {{<link url="Equal-Cost-Multipath-Load-Sharing/#resilient-hashing" text="Resilient hashing commands">}}
  - {{<link url="NVUE-CLI/#nvue-config-apply-and-frr" text="nv config apply command improvements">}} to prevent latency and timeout during FRR configuration changes
  - {{<link url="Zero-Touch-Provisioning-ZTP/#suppress-ztp-console-messages" text="Suppress ZTP console messages">}}
  - {{<link url="FRRouting/#tcp-sockets-and-bgp-peering-sessions" text="Configure the file descriptor limit for the FRR routing daemons">}}
  - {{<link url="Switch-Port-Attributes/#show-the-physical-connector-for-a-port" text="Show the physical connector for a port">}}
- Telemetry
  - {{<link url="Open-Telemetry-Export/#wjh-metrics" text="WJH metrics for OTEL">}}
  - {{<link url="gNMI-Streaming/#supported-models" text="gNMI component type and name for platform components">}}
  - {{<link url="New-and-Updated-Telemetry-Metrics/#new-gnmi-metrics" text="gNMI and OTEL metrics for unreachability AFI SAFI">}}
  - {{<link url="New-and-Updated-Telemetry-Metrics/#new-otel-metrics" text="OTEL metrics for AAA RADIUS login authentication">}}
  - {{<link url="ASIC-Monitoring/#microburst-histogram" text="Microburst histogram with per-port burst scoring">}}
  - {{<link url="gNMI-Streaming/#dial-out-source-address" text="Configurable source address for gNMI dial-out connections">}}
  - {{<link url="New-and-Updated-Telemetry-Metrics/#new-gnmi-metrics" text="gNMI and OTEL metrics for CPO modules and laser sources">}}
  - {{<link url="New-and-Updated-Telemetry-Metrics/#new-otel-metrics" text="OTEL metrics for trimmed packet sent and dropped counters">}} on Spectrum-6 switches
  - {{<link url="New-and-Updated-Telemetry-Metrics/#new-gnmi-metrics" text="gNMI and OTEL metrics for back-to-sender notification on link down">}} on Spectrum-6 switches

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.19.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} and {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.19 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- 5.16.1 through 5.16.8
- 5.17.0
- 5.18.0, 5.18.1, 5.18.2, 5.18.3

{{%notice infonopad%}}
For the SN6600-LD switch, you can upgrade to Cumulus Linux 5.19 only from Cumulus Linux 5.18.3 or later.
{{%/notice%}}

To upgrade to Cumulus Linux 5.19 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

For a list of the earliest Cumulus Linux releases supported for each switch model, refer to [this knowledge base article]({{<ref "/knowledge-base/Support/Support-Offerings/Minimum-Cumulus-Linux-Release-for-Each-Switch-Model" >}}).

### Spectrum-6 BMC Requirements

{{%notice infonopad%}}
For a Spectrum-6 switch, you must upgrade BMC before you upgrade Cumulus Linux. For information about upgrading BMC, refer to {{<link url="BMC" text="BMC">}}.
{{%/notice%}}

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

### RIB-to-FIB Filter Protocol Values

Cumulus Linux 5.19 removes `connected`, `kernel`, and `table` as valid values for `<import-protocol-id>` in the `nv set vrf <vrf-id> router rib <address-family> fib-filter protocol <import-protocol-id> route-map <route-map-id>` command; see {{<link url="Route-Filtering-and-Redistribution/#apply-a-route-map" text="Apply a Route Map">}}.

- If your configuration filters RIB-to-FIB routes from one of these three protocols, `nv config apply` rejects it after you upgrade. Update any such configuration before you upgrade.
- Remaining valid values are `bgp`, `ospf`, `static`, `rip`, `sharp`, `isis`, `ospf6`, and `ripng`.

### PIM and MSDP vtysh Commands

Cumulus Linux 5.19 upgrades FRR, which moves the vtysh commands that configure PIM and MSDP for a routing instance into a `router pim [vrf <vrf-name>]` block and drops the `ip` prefix; see {{<link url="Protocol-Independent-Multicast-PIM/#basic-pim-configuration" text="Protocol Independent Multicast - PIM">}}.

- `ip pim rp`, `ip pim ssm prefix-list`, `ip pim ecmp`, `ip pim spt-switchover`, the `ip pim` timer commands, and the `ip msdp mesh-group` commands move under `router pim` and lose the `ip` prefix. For example, `switch(config)# ip pim rp 10.10.10.101` becomes `switch(config)# router pim` followed by `switch(config-pim)# rp 10.10.10.101`.
- `ip pim spt-switchover infinity` becomes `spt-switchover infinity-and-beyond`.
- Per-VRF PIM settings move out of the `vrf <vrf-name>` block into a separate top-level `router pim vrf <vrf-name>` block.
- Interface-level commands, such as `ip pim`, `ip pim hello`, `ip pim bfd`, `ip pim use-source`, `ip pim allow-rp`, `ip pim active-active`, `ip multicast boundary oil`, and all `ip igmp` commands, are unchanged. All NVUE commands are unchanged.
- Check the `/etc/frr/frr.conf` file and any automation that configures PIM or MSDP through vtysh before you upgrade.

### Class E Address Space Support

FRR now treats the IPv4 240.0.0.0/4 (Class E) range as valid unicast address space on every switch running Cumulus Linux 5.19, whether or not you allow Class E as routable address space. A Class E interface address and its connected route can appear in `nv show interface` output and the routing table even if you never run the `nv set router allow-reserved-range class-e` command.

- The FRR `allow-reserved-ranges` command no longer includes Class E; it now covers only 0.0.0.0/8 and 127.0.0.0/8. If you previously set this command only to use Class E, you no longer need to.
- Until you allow Class E, Cumulus Linux still blocks Class E traffic, but the control-plane packet filter drops it instead of the ASIC. If you monitor hardware drop counters for Class E source addresses, you see this difference after you upgrade.

For more information, see {{<link url="FRRouting/#class-e-address-space-support" text="Class E Address Space Support">}}.

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA DSX Air">}}.
