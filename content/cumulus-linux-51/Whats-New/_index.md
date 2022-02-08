---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.1 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.1, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.1, see the {{<link title="Cumulus Linux 5.1 Release Notes" text="Cumulus Linux 5.1 Release Notes">}}.
- To upgrade to Cumulus Linux 5.1, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.1.0
<!-- vale on -->
Cumulus Linux 5.1.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN3800(100G Spectrum-3) available for early access
- 1G supported for all Spectrum-2 and Spectrum-3 switches

### New Features and Enhancements

- {{<link url="GRE-Tunneling" text="GRE tunneling">}}
- Refactor port configuration
- {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#adaptive-routing" text="Adaptive routing with RoCE">}}
- LLDP enhancements include support for custom TLV LLDP messages and dynamic LLDP TLV advertisements
- GTP hashing support
- VXLAN port isolation on Spectrum-3 switches
- Simplified EVPN configuration
- {{<link url="Smart-System-Manager" text="Bonds support warmboot">}}
- NVUE enhancements include:
  - Support control of IPv6 ND processes
  - Flexible snippet architecture
  - EVPN, PBR show commands
  - Logging improvements
