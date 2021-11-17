---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.0 release, and lists new platforms and features.

- For a list of all the platforms supported in Cumulus Linux 5.0, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.0, see the {{<link title="Cumulus Linux 5.0 Release Notes" text="Cumulus Linux 5.0 Release Notes">}}.
- To upgrade to Cumulus Linux 5.0, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.0
<!-- vale on -->
Cumulus Linux 5.0 provides bug fixes, and contains several new features and improvements.

### New Features and Enhancements

- New NVUE commands to:
  - Configure {{<link url="Protocol-Independent-Multicast-PIM" text="PIM">}}, {{<link url="IGMP-and-MLD-Snooping" text="IGMP">}} and {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP/#vrrp" text="VRRP">}}
  - Set the {{<link title="Setting the Date and Time" text="time zone">}}
  - Include interface descriptions (alias)
  - Clear counters, such as {{<link url="RDMA-over-Converged-Ethernet-RoCE" text="RoCE counters">}}
- Modified NVUE commands:
  - BGP `static-network` is now `network`
  - `nv set platform config` command options are now `nv set system config` options
  - `nv set platform hostname value <hostname>` command is now `nv set system hostname <hostname>`
- DHCPv6 supports SVI interfaces
- New forwarding resource profiles: `v6-lpm-heavy-1` and `l2-heavy-3`
- SNMP enhancements
