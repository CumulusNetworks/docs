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
Cumulus Linux 5.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- NVIDIA SN2201 (100G Spectrum-1)
- NVIDIA SN4800 (100G Spectrum-3)
- NVIDIA SN4600C (100G Spectrum-3)
- NVIDIA SN3700C-S (100G Spectrum-2) with Secure Boot

### New Features and Enhancements

- New NVUE commands to:
  - Configure PIM, IGMP and VRRP
  - Set the time zone
  - Include interface descriptions (alias)
  - Reboot the switch
  - Clear counters, such as RoCE counters
- Modified NVUE commands:
  - BGP `static-network` is now `network`
  - `nv set platform config` command is now `nv set system config`
  - `nv set platform hostname value <hostname>` command is now `nv set system hostname <hostname>`
- cl-support now includes CPLD register information
- DHCPv6 supports SVI interfaces
- MPLS LSR support with BGP labeled-unicast signaling
- New forwarding resource profiles: `v6-lpm-heavy-1` and `l2-heavy-3`
- SNMP enhancements:
  - Support for buffer queue utilisation
  - link up and link down count
  - VRF aware routing MIB
