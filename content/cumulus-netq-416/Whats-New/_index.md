---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. 

- For a list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.16 Release Notes" text="release notes">}}

## What's New in NetQ 4.16

NetQ 4.16.0 includes the following new features:

- NetQ for NVLink
- Create and apply custom tags to organize and filter devices
- Duplicate IP validation (beta)
- NVOS upgrades for NVLink switches
- View Slurm data in Grafana
- Cable Validation Tool



## Release Considerations

<!-- check on this pre-release -->

- When you upgrade to NetQ v4.15.0, any pre-existing validation data will be lost. Additionally, NetQ will not retain data related to network services (including BGP, LLDP, EVPN, and MLAG) after upgrading.
- You must upgrade cloud (OPTA) deployments to NetQ 4.15 before initiating a {{<link title="Switch Management/#switch-discovery" text="switch discovery">}}.

### Upgrade Paths

You can upgrade to NetQ 4.16 if your deployment is running version 4.15 or 4.14. For on-premises and cloud deployments, {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then concurrently restore your data and upgrade NetQ during a {{<link title="Install the NetQ System" text="new NetQ 4.16 installation">}}

To install NetQ for NVLink, perform a new virtual machine installation.


### Compatible Agent Versions

The NetQ 4.16 server is compatible with NetQ agents 4.16 and 4.15. You can install NetQ agents on switches and servers running:

- Cumulus Linux 
- Ubuntu 24.04, 22.04

NVIDIA recommends upgrading to the latest agent version. The NetQ agent is not compatible with Broadcom switches. Reach out to your NVIDIA support representative if your networking environment requires Broadcom support.