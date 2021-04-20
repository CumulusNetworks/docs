---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.0 release, and lists new platforms and features.

- For a list of all the platforms supported in Cumulus Linux 5.0, see the {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.0, see the {{<link title="Cumulus Linux 5.0 Release Notes" text="Cumulus Linux 5.0 Release Notes">}}.
- To upgrade to Cumulus Linux 5.0, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.0

Cumulus Linux 5.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- 
- 

### New Features and Enhancements

- {{<link url="Cumulus-User-Experience-CUE" text="Cumulus User Experience (CUE)">}} is a new object-oriented, schema driven model of a complete Cumulus Linux system (hardware and software) with a robust API that allows multiple interfaces to both view and configure any element within the system.
  {{%notice note%}}
  CUE replaces the NCLU command line interface, which is no longer supported. In Cumulus Linux 5.0, not all NCLU commands have a CUE equivalent. You can configure features without CUE commands using Linux commands and FRR. 
  {{%/notice%}}
- Support for {{<link url="VLAN-aware-Bridge-Mode/" text="multiple VLAN aware bridges">}}
- EVPN multihoming HREP support
- {{<link url="Precision-Time-Protocol-PTP" text="PTP Boundary Clock">}} enhancements
- {{<link url="Protocol-Independent-Multicast-PIM/#allow-rp" text="PIM Allow RP">}}
- {{<link url="Optional-BGP-Configuration/#conditional-advertisement" text="BGP conditional route advertisement">}}
- Smart System Manager supports {{<link url="Smart-System-Manager" text="warm boot">}}
- QoS: Dynamic buffer configuration as default
- Enhanced Transmission Selection (ETS): 802.1Qaz
- Optimized Multicast Flooding (OMF)
- IPv6 Traffic class-based PBR matching
- Support for QinQ/QinVNI access and trunk ports on the same system
- Removed licensing from Cumulus Linux
- On NVIDIA Spectrum switches, you now have the ability to {{<link url="Hybrid-Cloud-Connectivity-with-QinQ-and-VXLANs" text="modify the inner tag in double-tagged packets ">}}

### Unsupported Platforms

These platforms are not supported in Cumulus Linux 5.0:
