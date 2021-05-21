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

## What's New in Cumulus Linux 5.0

Cumulus Linux 5.0 supports provides bug fixes, and contains several new features and improvements.

### New Features and Enhancements

- {{<link url="Cumulus-User-Experience-CUE" text="Cumulus User Experience (CUE)">}} is a new object-oriented, schema driven model of a complete Cumulus Linux system (hardware and software) with a robust API that allows multiple interfaces to both view and configure any element within the system. CUE replaces the NCLU command line interface.

{{<notice info>}}
CUE is created from the ground up and does not inherit any previous functionality from NCLU. Certain features are not yet supported by CUE. If you are an NCLU user, confirm that your features are fully supported in CUE before upgrading to Cumulus Linux 5.0. If you use a feature that is not yet supported, you can either remain on your current 4.x release or perform all your switch configuration using Linux and vtysh commands.
{{</notice>}}

- {{<link url="VLAN-aware-Bridge-Mode/" text="Multiple VLAN-aware bridges">}}
- {{<link url="EVPN-Multihoming" text="EVPN multihoming Head End Replication">}}
- {{<link url="Precision-Time-Protocol-PTP" text="PTP Boundary Clock">}} enhancements
- {{<link url="Protocol-Independent-Multicast-PIM/#allow-rp" text="PIM Allow RP">}}
- {{<link url="Optional-BGP-Configuration/#conditional-advertisement" text="BGP conditional route advertisement">}}
- Smart System Manager supports {{<link url="Smart-System-Manager" text="warm boot">}}
- QoS: Dynamic buffer configuration as default
- {{<link url="IGMP-and-MLD-Snooping/#optimized-multicast-flooding-omf" text="Optimized Multicast Flooding (OMF)">}}
- Support for QinQ/QinVNI access and trunk ports on the same system
- On NVIDIA Spectrum switches, you now have the ability to {{<link url="Hybrid-Cloud-Connectivity-with-QinQ-and-VXLANs" text="modify the inner tag in double-tagged packets ">}}
- A specific software license key is no longer required to enable the `switchd` service.

### Unsupported Platforms

Cumulus Linux 5.0 supports NVIDIA Spectrum-based ASIC platforms only. This release removes support for Broadcom-based networking ASICs. Broadcom-based ASICs will continue to be supported throughout the life of the Cumulus Linux 3.7 and 4.3 releases.
