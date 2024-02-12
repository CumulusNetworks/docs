---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.9 Release Notes" text="release notes">}}.

<!-- vale off -->
## What's New in NetQ 4.9.0
<!-- vale on -->
NetQ 4.9.0 includes the following new features and improvements:

- {{<link title="Adaptive Routing" text="Adaptive routing monitoring">}} for switches is generally available
- {{<link title="RoCE" text="RoCE monitoring">}} for DPUs is generally available
- Prometheus endpoints for ConnectX adapters update dynamically and no longer require manual configuration. {{<link title="Install NIC and DPU Agents" text="Upgrade the DOCA Telemetry Service">}} on your NICs and DPUs to enable this feature.
- You can now {{<link title="Switch Management#host-a-ztp-script-with-netq" text="host a ZTP script with NetQ">}}
- Performance and security enhancements


## Upgrade Paths

For deployments running:

- 4.8.0, 4.7.0, 4.6.0, or 4.5.0: {{<link title="Upgrade NetQ Virtual Machines" text="upgrade directly">}} to NetQ 4.9.0
- 4.4.1, 4.4.0, or 4.3.0: {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}} and perform a {{<link title="Install the NetQ System" text="new installation of NetQ 4.9.0">}}
- 4.2.0 or earlier: upgrade incrementally {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-43/Installation-Management/Upgrade-NetQ/Upgrade-System/" text="to version 4.3.0">}}. Then {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}} and perform a {{<link title="Install the NetQ System" text="new installation of NetQ 4.9.0">}}

{{%notice note%}}
Cluster deployments running NetQ 4.9.0 require a virtual IP address. Refer to the upgrade or installation documentation for your deployment type for instructions on adding the virtual IP address to your deployment.
{{%/notice%}}

## Compatible Agent Versions

The NetQ 4.9.0 server is compatible with NetQ Agents 4.8.0 and 4.7.0. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 5.0.0 and later (Spectrum switches)
- Cumulus Linux 4.3.0, 4.3.1, and 4.3.2 (Broadcom switches)
- SONiC 202012
- CentOS 7
- RHEL 7.1
- Ubuntu 20.04

You must upgrade to the latest agent version to enable 4.9 features.
