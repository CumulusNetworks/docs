---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. 

- For a list of open and fixed issues, see the {{<link title="NVIDIA NetQ 5.0 Release Notes" text="release notes">}}

## What's New in NetQ 5.0

- You can now monitor NVLink switches with NetQ. 
- {{<link title="Switch Inventory/#create-and-assign-switch-labels" text="Create and apply custom labels">}} to organize and filter switches.
- {{<link title="Integrate NetQ with Grafana/#collect-slurm-telemetry" text="View Slurm data in Grafana">}}
- You can now launch the {{<link title="Cable Validations" text="Cable Validation Tool">}} from NetQ.
- Performance improvements to the duplicate IP address validation (beta)
- Security enhancements and general performance improvements


## Release Considerations

<!-- check on this pre-release -->

- When you upgrade to NetQ v5.0, any pre-existing validation data will be lost. Additionally, NetQ will not retain data related to network services (including BGP, LLDP, EVPN, and MLAG) after upgrading.
- You must upgrade cloud (OPTA) deployments to NetQ 5.0 before initiating a {{<link title="Switch Management/#switch-discovery" text="switch discovery">}}.
- The API gateway port for on-premises deployments has changed from 32708 to 32710.

### Upgrade Paths

You can upgrade to NetQ 5.0 if your deployment is running version 4.15 or 4.14. For on-premises and cloud deployments, {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then concurrently restore your data and upgrade NetQ during a {{<link title="Install the NetQ System" text="new NetQ 5.0 installation">}}

To upgrade your existing NMX-M deployment, perform a system bringup to connect to NMX-C and NMX-T <!--4.15 link to pages when ready-->


### Compatible Agent Versions

The NetQ 5.0 server is compatible with NetQ agents 5.0 and 4.15. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.15, 5.14, 5.11.3, 5.9.4
- Ubuntu 24.04, 22.04