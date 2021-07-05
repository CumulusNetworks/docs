---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 4.4 release, and lists new platforms and features.

- For a list of all the platforms supported in Cumulus Linux 4.4, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 4.4, see the {{<link title="Cumulus Linux 4.4 Release Notes" text="Cumulus Linux 4.4 Release Notes">}}.
- To upgrade to Cumulus Linux 4.4, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 4.4

Cumulus Linux 4.4 supports supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- NVIDIA SN3700C-S (100G Spectrum-2) with Secure Boot

### New Features and Enhancements

- {{<link url="NVIDIA-User-Experience-NVUE" text="NVIDIA User Experience (NVUE)">}} is a new object-oriented, schema driven model of a complete Cumulus Linux system (hardware and software) with a robust API that allows multiple interfaces to both view and configure any element within the system. NVUE provides both a CLI and an API.
{{%notice note%}}
The NVUE commands and outputs are subject to change.
{{%/notice%}}
- {{<link url="VLAN-aware-Bridge-Mode/" text="Multiple VLAN-aware bridges">}}
- {{<link url="VXLAN-Devices/#single-vxlan-device" text="Single VXLAN Devices">}}
- {{<link url="Inter-subnet-Routing/#downstream-vni" text="Downstream VNI (symmetric EVPN route leaking)">}}
- {{<link url="EVPN-Multihoming" text="EVPN multihoming Head End Replication">}}
- {{<link url="Precision-Time-Protocol-PTP" text="PTP Boundary Clock">}} enhancements
- {{<link url="Protocol-Independent-Multicast-PIM/#allow-rp" text="PIM Allow RP">}}
- {{<link url="Optional-BGP-Configuration/#conditional-advertisement" text="BGP conditional route advertisement">}}
- {{<link url="IGMP-and-MLD-Snooping/#optimized-multicast-flooding-omf" text="Optimized Multicast Flooding (OMF)">}}
- Smart System Manager {{<link url="Smart-System-Manager" text="warm boot">}}
- {{<link url="Installing-a-New-Cumulus-Linux-Image/#secure-boot" text="Secure Boot">}}
- {{<link url="Quality-of-Service" text="QoS enhancements ">}} (`traffic.conf` and `datapath.conf` files removed and replaced)
- {{<link url="Hybrid-Cloud-Connectivity-with-QinQ-and-VXLANs" text="QinQ Double-tagged translation ">}} is now supported on switches with the Spectrum-2 and Spectrum-3 ASIC
- {{<link url="Network-Address-Translation-NAT" text="Double (twice) NAT ">}}
- ZTP enhancements include {{<link url="Zero-Touch-Provisioning-ZTP/#dhcp-on-front-panel-ports" text="DHCP on front panel ports">}}, the ability to {{<link url="Zero-Touch-Provisioning-ZTP/#continue-provisioning" text="continue provisioning after executing the script locally">}}, and improved logging
- A specific software license key is no longer required to enable the `switchd` service. For more information, refer to [Licensing in Cumulus Linux 44 and Later]({{<ref "/knowledge-base/Installing-and-Upgrading/Installation/Licensing-in-Cumulus-Linux-44-and-Later" >}}).

### Unsupported Platforms

Cumulus Linux 4.4 supports NVIDIA Spectrum-based ASIC platforms only. This release removes support for Broadcom-based networking ASICs. Broadcom-based ASICs will continue to be supported throughout the life of the Cumulus Linux 3.7 and 4.3 releases.
