---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 4.3 release, and lists new platforms and features.
- For a list of open and fixed issues in Cumulus Linux 4.3, see the {{<link title="Cumulus Linux 4.3 Release Notes" text="Cumulus Linux 4.3 Release Notes">}}.
- To upgrade to Cumulus Linux 4.3, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 4.3.2

Cumulus Linux 4.3.2 provides bug fixes.

{{%notice note%}}
Cumulus Linux 4.3.2 is supported on Broadcom switches only. You cannot upgrade to Cumulus Linux 4.3.2 on a Mellanox switch.
- NVIDIA does not provide a Cumulus Linux 4.3.2 image for Mellanox switches.
- To upgrade a Broadcom switch to Cumulus Linux 4.3.2 with `apt upgrade`, see {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text=" Upgrade to Cumulus Linux 4.3.1 and later">}}.
{{%/notice%}}

## What's New in Cumulus Linux 4.3.1

Cumulus Linux 4.3.1 provides bug fixes.

{{%notice note%}}
Cumulus Linux 4.3.1 is supported on Broadcom switches only. You cannot upgrade to Cumulus Linux 4.3.1 on a Mellanox switch.
- NVIDIA does not provide a Cumulus Linux 4.3.1 image for Mellanox switches.
- To upgrade a Broadcom switch to Cumulus Linux 4.3.1 with `apt upgrade`, see {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text=" Upgrade to Cumulus Linux 4.3.1 and later">}}.
{{%/notice%}}

## What's New in Cumulus Linux 4.3.0

Cumulus Linux 4.3.0 provides bug fixes, and contains several new features and enhancements.
<!-- vale on -->

### New Features and Enhancements

- {{<link url="Smart-System-Manager" text="Smart System Manager">}}, also known as [ISSU](## "In Service System Upgrade"), enables you to upgrade and troubleshoot an active switch with minimal disruption to the network
- BGP enhancements:
  - {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="BGP graceful restart">}}
  - {{<link url="Optional-BGP-Configuration/#multiple-bgp-asns" text="Multiple ASNs for different VRF instances">}}
- {{<link url="DHCP-Snooping" text="DHCP snooping">}}
- QoS enhancements:
  - {{<link url="Buffer-and-Queue-Management#traffic-shaping" text="Traffic shaping">}}
  - {{<link url="Buffer-and-Queue-Management#scheduling-weights-per-egress-queue" text="Scheduling weights per egress queue">}}
- {{<link title="Mellanox What Just Happened (WJH)" text="Mellanox WJH commands">}} enable you to troubleshoot and diagnose network issues
- {{<link url="Cumulus-User-Experience-CUE" text="Cumulus User Experience (CUE)">}} is an early access feature currently in ALPHA and open to customer feedback
- {{<link url="Docker-on-Cumulus-Linux" text="Docker runtime ">}} is packaged by default with Cumulus Linux
- {{<link url="Troubleshoot-Layer-1" text="Troubleshooting guide for layer 1 issues">}} affecting the port modules connecting switches to networks.
- {{<link url="SPAN-and-ERSPAN" text="NCLU commands for SPAN and ERSPAN">}}
- {{<link url="RDMA-over-Converged-Ethernet-RoCE" text="DoRoCE command">}} enables you to configure RoCE with PFC and ECN on all interfaces
- {{<link url="Netfilter-ACLs/#nonatomic-update-mode-and-atomic-update-mode" text="Incremental nonatomic updates">}} are now supported on NVIDIA Mellanox switches
- New {{<link url="Supported-MIBs" text="SNMP MIB for BGP unnumbered peers">}}
- Multicast routing over VXLAN is now supported on NVIDIA Mellanox switches

### Unsupported Platforms

These platforms are not supported in Cumulus Linux 4.3. They are supported in Cumulus Linux 3.7, until that release reaches its end of life.

- Cumulus Express CX-10256-S/Edgecore OMP-800 (100G Tomahawk)
- Dell S6000-ON (40G Trident2)
- EdgeCore Wedge-100 (100G Tomahawk)
- Facebook Backpack (100G Tomahawk)
- Facebook Voyager (100G Tomahawk)
- Delta AG7648
- QCT QuantaMesh BMS T3048-LY8
- QCT QuantaMesh BMS T3048-LY9
