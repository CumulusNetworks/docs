---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 4.3 release, and lists new platforms and features.

- For a list of all the platforms supported in Cumulus Linux 4.3, see the {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 4.3, see the {{<link title="Cumulus Linux 4.3 Release Notes" text="Cumulus Linux 4.3 Release Notes">}}.
- To upgrade to Cumulus Linux 4.3, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 4.3.0

Cumulus Linux 4.3.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- Mellanox SN4800 (100G Spectrum-3)

### New Features and Enhancements

- {{<link url="Smart-System-Manager" text="Smart System Manager">}}, which enables you to upgrade and troubleshoot an active switch with minimal disruption to the network
- BGP enhancements:
  - {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="BGP graceful restart">}}
  - {{<link url="Optional-BGP-Configuration/#use-distinct-asns-for-different-vrf-instances" text="Distinct AS numbers for different BGP VRF instances">}} are supported in VRF route leaking and EVPN configurations
- {{<link url="SPAN-and-ERSPAN" text="NCLU commands for SPAN and ERSPAN">}}
- {{<link url="DHCP-Snooping" text="DHCP snooping">}}
- QoS enhancements:
  - {{<link url="Buffer-and-Queue-Management#traffic-shaping" text="Traffic shaping">}}
  - {{<link url="Buffer-and-Queue-Management#scheduling-weights-per-egress-queue" text="Scheduling weights per egress queue">}}
- {{<link url="Netfilter-ACLs/#nonatomic-update-mode-and-atomic-update-mode" text="Incremental nonatomic updates">}} now supported on Mellanox switches
- {{<link title="Mellanox What Just Happened (WJH)" text="Mellanox WJH commands">}} to troubleshoot and diagnose network issues
- {{<link url="EVPN-Multihoming" text="EVPN multihoming">}} now supports LACP bypass
- {{<link url="Docker-on-Cumulus-Linux" text="Docker runtime ">}} included by default on Cumulus Linux
- {{<link url="RDMA-over-Converged-Ethernet-RoCE" text="DoRoCE command">}} to configure RoCE with PFC and ECN on all interfaces
- {{<link url="Supported-MIBs" text="SNMP MIB for BGP unnumbered peers">}}
- Multicast routing over VXLAN is now supported on Mellanox switches

### Unsupported Platforms

These platforms are not supported in Cumulus Linux 4.3. They are supported in Cumulus Linux 3.7, until that release reaches its end of life.

- Cumulus Express CX-10256-S/Edgecore OMP-800 (100G Tomahawk)
- Dell S6000-ON (40G Trident2)
- EdgeCore Wedge-100 (100G Tomahawk)
- Facebook Backpack (100G Tomahawk)
- Facebook Voyager (100G Tomahawk)
- Delta AG7648
- Edgecore AS4610-54T-B
- QCT QuantaMesh BMS T3048-LY8
- QCT QuantaMesh BMS T3048-LY9
