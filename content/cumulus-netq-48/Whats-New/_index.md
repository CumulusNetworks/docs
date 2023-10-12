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

- Lifecycle management support for in-band deployments
- High-availability improvements for on-premises cluster deployments: you can now access the NetQ UI via a virtual IP address in the event of a node failure 
- NVLink support
- RoCE monitoring for DPUs and NICs {{<link title="RoCE">}} and create threshold-crossing rules {{<link title="Threshold-Crossing Events Reference/#dpu-roce">}}
- Topology redesign {{<link title="Network Topology">}} to accommodate more devices
- Performance improvements to the NetQ Agent that limit its CPU usage to 50% on Cumulus switches 
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
