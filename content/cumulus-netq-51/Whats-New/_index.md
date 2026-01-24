---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. 

- For a list of open and fixed issues, see the {{<link title="NVIDIA NetQ 5.1 Release Notes" text="release notes">}}.

## What's New in NetQ 5.1

- The {{<link title="Integrate NetQ with Grafana" text="NetQ integration with Grafana">}} is generally available.
- NetQ now retains OTLP metrics data for 15 days instead of the previous three-day retention period. Additionally, you can now {{<link title="Integrate NetQ with Grafana/#customize-metric-collection" text="create a customizable list of metrics">}} that are forwarded to your time-series database.
- You can now deploy NetQ for Ethernet and NVLink with an increased number of nodes to support large networks. To get started, {{<link title="Install NetQ for Ethernet and NVLink (Beta)" text="perform a fresh installation">}}. This deployment type is currently in beta.
- You can now use NetQ to monitor multiplane networking environments. With this enhancement, you can: 
    - Filter and display telemetry data associated with individual planes. 
    - Perform validations, such as BGP router-ID checks, within the appropriate plane context. 
    - Include plane parameters across telemetry, topology, and validation workflows.
    - To get started, configure {{<link title="Switch Inventory/#create-and-assign-switch-labels" text="device labels">}}.
- You can now create {{<link title="Configure and Monitor Threshold-Crossing Events" text="threshold-crossing rules">}} with a wider range of measurement units in both the UI and the CLI. 
- NetQ no longer broadcasts multiple, successive events for breaches to the same threshold-crossing rule. You can change this new default behavior using the CLI.
- Performance improvements to the account management page in the UI
- The time required to install NetQ has been reduced.
- NetQ for NVLink API changes:
    - Added the ability to download support packages and upgrade NVOS for all switches within an NVLink domain.
    - Added an endpoint to retrieve NetQ's version
    - Added a fault tolerance mechanism that allows NVLink switches with at least two out-of-band management ports to maintain connectivity to NMX controller and telemetry services in case of port failure.
    - Queries to the `compute-nodes` endpoint now return hostnames within the response
    - Performance improvements to scale deployments
    - Refer to the {{<link title="NetQ NVLink API Changelog">}} for a comprehensive list of changes

### Upgrade Paths

NetQ 5.1 is available exclusively for on-premises deployments. You can upgrade to 5.1 if your deployment is running version 5.0 or 4.15. First {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then concurrently restore your data and upgrade NetQ during a {{<link title="Install the NetQ System" text="new NetQ 5.0 installation">}}.


### Compatible Agent Versions

The NetQ 5.1 server is compatible with NetQ agents 5.1 and 5.0. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.16, 5.15, 5.11.3, 5.9.4
- Ubuntu 24.04, 22.04