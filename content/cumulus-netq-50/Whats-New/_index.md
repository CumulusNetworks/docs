---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. 

- For a list of open and fixed issues, see the {{<link title="NVIDIA NetQ 5.0 Release Notes" text="release notes">}}.

## What's New in NetQ 5.0

- You can now {{<link title="NVLink Management" text="monitor NVLink deployments">}} with NetQ. Use the REST API to manage NVLink network configurations and resources, and allocate GPUs for AI workloads. This release introduces {{<link title="Install the NetQ System" text="new deployment options">}} for Ethernet-only environments or hybrid NVLink-Ethernet networks. Previously called NMX-M, this feature retains all existing functionality and introduces expanded deployment options.
- {{<link title="Switch Inventory/#create-and-assign-switch-labels" text="Create and apply custom labels">}} to organize and filter switches.
- {{<link title="Integrate NetQ with Grafana/#collect-slurm-telemetry" text="View Slurm data in Grafana">}}.
- You can now launch the {{<link title="Cable Validations" text="Cable Validation Tool">}} from NetQ.
- Performance improvements to the duplicate IP address validation (beta)
- Security enhancements and general performance improvements


## Release Considerations

- The API gateway port for on-premises deployments has changed from 32708 to 32710.

### Upgrade Paths

NetQ 5.0 is available exclusively for on-premises deployments. You can upgrade to 5.0 if your deployment is running version 4.15 or 4.14. First {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then concurrently restore your data and upgrade NetQ during a {{<link title="Install the NetQ System" text="new NetQ 5.0 installation">}}


### Compatible Agent Versions

The NetQ 5.0 server is compatible with NetQ agents 5.0 and 4.15. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.15, 5.14, 5.11.3, 5.9.4
- Ubuntu 24.04, 22.04