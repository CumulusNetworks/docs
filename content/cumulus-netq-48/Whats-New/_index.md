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

- {{<link title="Adaptive Routing" text="Adaptive routing">}} monitoring for switches (beta)
- Lifecycle management support for {{<link url="Lifecycle-Management/#lcm-support-for-in-band-management" text="in-band deployments">}}
- {{<link title="Data Center Network Deployments#high-availability" text="High-availability">}} improvements for new on-premises cluster installations: you can now access the NetQ UI via a virtual IP address in the event of a node failure 
- Monitoring for NVLink4 devices: view your NVLink4 inventory, monitor events, perform NVOS upgrades, and generate troubleshooting files. Visit the {{<link title="NVLink4" text="NVLink4 section">}} to get started.
- {{<link title="RoCE" text="RoCE monitoring">}} for DPUs (beta)
- {{<link title="Network Topology" text="Network topology">}} redesign that accommodates large networks with many devices (beta)
- Performance improvements to the NetQ Agent
- Security enhancements


## Upgrade Paths

For deployments running:

- 4.7.0 or 4.6.0: {{<link title="Upgrade NetQ Virtual Machines/#upgrading-from-netq-460-or-470" text="upgrade directly">}} to NetQ 4.8.0
- 4.5.0, 4.4.1, 4.4.0, or 4.3.0: {{<link title="Back Up and Restore NetQ/" text="back up your NetQ data">}} and perform a {{<link title="Install NetQ" text="new installation of NetQ 4.8.0">}}
- 4.2.0 or earlier: upgrade incrementally {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-43/Installation-Management/Upgrade-NetQ/Upgrade-System/" text="to version 4.3.0">}}. Then {{<link title="Back Up and Restore NetQ/#back-up-netq-4.4.1-or-earlier" text="back up your NetQ data">}} and perform a {{<link title="Install NetQ" text="new installation of NetQ 4.8.0">}}.

{{%notice note%}}
Enabling {{<link title="Data Center Network Deployments#high-availability" text="high availability">}} of the NetQ control plane and UI requires a new installation of your server cluster deployment. Database migration is not supported for new HA server cluster installations. 
{{%/notice%}}

## Compatible Agent Versions

The NetQ 4.8.0 server is compatible with NetQ Agents 4.7.0 and 4.6.0. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 4.3.0 and 4.3.1 (Broadcom switches)
- Cumulus Linux 5.0.0 and above (Spectrum switches)
- SONiC 202012
- CentOS 7
- RHEL 7.1
- Ubuntu 20.04

You must upgrade to the latest agent version to enable 4.8 features.
