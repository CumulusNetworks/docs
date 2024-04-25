---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 4.4 release, and lists new platforms and features.
- For a list of open and fixed issues in Cumulus Linux 4.4, see the {{<link title="Cumulus Linux 4.4 Release Notes" text="Cumulus Linux 4.4 Release Notes">}}.
- To upgrade to Cumulus Linux 4.4, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 4.4.5
<!-- vale on -->
Cumulus Linux 4.4.5 provides bug fixes.
<!-- vale off -->
## What's New in Cumulus Linux 4.4.4
<!-- vale on -->
Cumulus Linux 4.4.4 provides bug fixes.
<!-- vale off -->
## What's New in Cumulus Linux 4.4.3
<!-- vale on -->
Cumulus Linux 4.4.3 provides bug fixes.
<!-- vale off -->
## What's New in Cumulus Linux 4.4.2
<!-- vale on -->
Cumulus Linux 4.4.2 provides bug fixes and contains several enhancements.

### Enhancements

- {{<link url="Supported-MIBs" text="Entity-Sensor-MIB extensions">}}
- {{<link url="Switch-Port-Attributes/#drop-packets-that-exceed-the-egress-layer-3-mtu" text="Drop packets that exceed the egress layer 3 MTU">}}
- Netfilter-ACL rules:
  - {{<link url="Netfilter-ACLs#install-and-manage-acl-rules-with-nclu" text="NCLU commands">}} support both a MAC address and IP address in the same rule, and support the MAC address mask
  - {{<link url="Netfilter-ACLs/#match-on-ecn-bits-in-the-tcp-ip-header" text="Match on ECN bits in the TCP IP Header">}}

<!-- vale off -->
## What's New in Cumulus Linux 4.4.0
<!-- vale on -->
Cumulus Linux 4.4.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- NVIDIA SN3700C-S (100G Spectrum-2) with Secure Boot (early access)

### New Features and Enhancements

- {{<link url="NVIDIA-User-Experience-NVUE" text="NVIDIA User Experience (NVUE)">}} is a new object-oriented, schema driven model of a complete Cumulus Linux system (hardware and software) with a robust API that allows multiple interfaces to both view and configure any element within the system. NVUE provides both a CLI and an API.
{{%notice note%}}
The NVUE commands and outputs are subject to change.
{{%/notice%}}
- {{<link url="VLAN-aware-Bridge-Mode/" text="Multiple VLAN-aware bridges">}}
- {{<link url="VXLAN-Devices/#single-vxlan-device" text="Single VXLAN devices">}}
- {{<link url="Inter-subnet-Routing/#downstream-vni" text="Downstream VNI (symmetric EVPN route leaking)">}}
- {{<link url="EVPN-Multihoming" text="EVPN multihoming Head End Replication">}}
- {{<link url="Precision-Time-Protocol-PTP" text="PTP Boundary Clock">}} enhancements
- {{<link url="Protocol-Independent-Multicast-PIM/#allow-rp" text="PIM Allow RP">}}
- {{<link url="Optional-BGP-Configuration/#conditional-advertisement" text="BGP conditional route advertisement">}}
- {{<link url="IGMP-and-MLD-Snooping/#optimized-multicast-flooding-omf" text="Optimized Multicast Flooding (OMF)">}}
- Smart System Manager {{<link url="Smart-System-Manager/#restart-mode" text="warm boot">}}
- {{<link url="Installing-a-New-Cumulus-Linux-Image/#secure-boot" text="Secure Boot">}}
- {{<link url="Quality-of-Service" text="QoS enhancements ">}} (`traffic.conf` and `datapath.conf` files removed and replaced)
- {{<link url="Hybrid-Cloud-Connectivity-with-QinQ-and-VXLANs/#double-tag-translation" text="QinQ double-tagged translation ">}} is now supported on switches with the Spectrum-2 and Spectrum-3 ASIC
- {{<link url="Network-Address-Translation-NAT" text="Double (twice) NAT ">}}
- ZTP enhancements include the ability to {{<link url="Zero-Touch-Provisioning-ZTP/#continue-provisioning" text="continue provisioning after executing the script locally">}}, and improved logging
- A specific software license key is no longer required to enable the `switchd` service. For more information, refer to [Licensing in Cumulus Linux 44 and Later]({{<ref "/knowledge-base/Installing-and-Upgrading/Installation/Licensing-in-Cumulus-Linux-44-and-Later" >}}).

### Unsupported Platforms

Cumulus Linux 4.4 supports NVIDIA Spectrum-based switches only. Cumulus Linux 3.7 and 4.3 continue to support Broadcom-based networking ASICs.

### Deprecated Features
Cumulus Linux 4.4. no longer supports GRE and OVSDB High Availability.

<!-- vale off -->
## What's New in the Documentation
<!-- vale on -->

The Cumulus Linux 4.4 user guide (this guide) provides pre-built Try It demos for certain Cumulus Linux features. The Try It demos run a simulation in NVIDIA Air; a cloud hosted platform that works exactly like a real world production deployment. Use the Try It demos to examine switch configuration for a feature.

The following Try It demos are currently available:
- {{<link url="Configuration-Example/#nvue-commands" text="BGP">}}
- {{<link url="Inter-subnet-Routing/#configure-route-targets" text="EVPN downstream VNI">}}
- {{<link url="EVPN-Multihoming/#evpn-mh-with-head-end-replication" text="EVPN multihoming">}}
- {{<link url="Configuration-Examples/#nvue-commands-2" text="EVPN symmetric routing">}}
- {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#nvue-commands" text="MLAG">}}
- {{<link url="Protocol-Independent-Multicast-PIM/#example-pim-configuration" text="PIM">}}
- {{<link url="Static-VXLAN-Tunnels/#single-vxlan-device" text="Single VXLAN device">}}

For more information, see {{<link url="Try-It-Pre-built-Demos" text="Try It Pre-built Demos">}}.
