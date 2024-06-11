---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.10 Release Notes" text="release notes">}}.

## What's New in NetQ 4.10.1

NetQ 4.10.1 provides all the same new features and enhancements as NetQ 4.10.0, and in addition, supports {{<link title="Upgrade Cumulus Linux" text="NetQ Lifecycle Management">}} switch upgrades to Cumulus Linux 5.9 for switches configured with NVUE. 

## What's New in NetQ 4.10.0

NetQ 4.10 integrates with Base Command Manager (BCM), a toolkit to streamline cluster provisioning, workload management, and infrastructure monitoring. With Base Command Manager and NetQ, administrators can monitor telemetry data and perform health checks on a network’s fabric.

Base Command Manager 10 also provides a Kubernetes wizard to manage NetQ provisioning for high availability, on-prem single or multi-node clusters. Using the wizard, administrators can:

- Avoid port conflicts between BCM and NetQ
- Verify that all the installation prerequisites are met
- Choose between single-node or high-availability deployments
- Configure files and directories in exclude lists
- Synchronize clocks
- Deploy the NetQ server
- Connect the cluster management daemon, CMDaemon, to the NetQ server to pull telemetry data

To get started, refer to the {{<exlink url="https://docs.nvidia.com/base-command-manager/#product-manuals" text="Base Command Manager administrator and containerization manuals">}}.

{{%notice info%}}
NetQ 4.10.0 does not support upgrading switches to Cumulus Linux version 5.9 with {{<link title="Upgrade Cumulus Linux" text="NetQ Lifecycle Management">}}. To upgrade switches manually, see {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Installation-Management/Upgrading-Cumulus-Linux/" text="Upgrading Cumulus Linux">}}.
{{%/notice%}}
## Upgrade Paths

For deployments running:

- 4.9.0, 4.8.0: {{<link title="Upgrade NetQ Virtual Machines" text="upgrade directly">}} to NetQ 4.10.
- 4.7.0 or earlier: {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}} and perform a {{<link title="Install the NetQ System" text="new installation">}}.

## Compatible Agent Versions

The NetQ 4.10.1 server is compatible with NetQ Agent 4.9 and above. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 5.0.0 and later (Spectrum switches)
- Cumulus Linux 4.3.1 and 4.3.2 (Broadcom switches)
- SONiC 202012
- CentOS 7
- RHEL 7.1
- Ubuntu 20.04

You must upgrade to the latest agent version to enable 4.10 features.

{{%notice info%}}
Switches running Cumulus Linux 5.9 require the NetQ 4.10 or later agent package. See {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/Installation-Management/Install-NetQ/Install-NetQ-Agents/" text="Install NetQ Agents">}}.
{{%/notice%}}
