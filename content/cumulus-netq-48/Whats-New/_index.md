---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.8 Release Notes" text="release notes">}}.

<!-- vale off -->
## What's New in NetQ 4.8.0
<!-- vale on -->
NetQ 4.8.0 includes the following new features and improvements:

- Lifecycle management support for {{<link url="Lifecycle-Management/#lcm-support-for-in-band-management" text="in-band deployments">}}
- {{<link title="Adaptive Routing" text="Adaptive routing">}} monitoring for switches (beta)
- High-availability improvements for on-premises cluster deployments: you can now access the NetQ UI via a virtual IP address in the event of a node failure 
- Monitoring for NVLink4 devices: view your NVLink4 inventory, monitor events, perform NVOS upgrades, and generate troubleshooting files. Visit the {{<link title="NVLink4" text="NVLink4 section">}} to get started.
- RoCE monitoring for DPUs {{<link title="RoCE">}} and create threshold-crossing rules {{<link title="Threshold-Crossing Events Reference/#dpu-roce">}}
- {{<link title="Network Topology" text="Network topology">}} redesign that accommodates large networks with many devices (beta)
- Performance improvements to the NetQ Agent
- Security enhancements


## Upgrade Paths

For deployments running:


## Compatible Agent Versions

The NetQ 4.8.0 server is compatible with NetQ Agents 4.7.0 and 4.6.0. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 4.3.0 and 4.3.1 (Broadcom switches)
- Cumulus Linux 5.0.0 and above (Spectrum switches)
- SONiC 202012
- CentOS 7
- RHEL 7.1
- Ubuntu 20.04

You must upgrade to the latest agent version to enable 4.8 features.
