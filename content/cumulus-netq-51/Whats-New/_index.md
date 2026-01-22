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

- The NetQ integration with Grafana is generally available
- You can now deploy NetQ for Ethernet and NVLink with an increased number of nodes to support large networks. To get started, {{<link title="Install NetQ for Ethernet and NVLink" text="perform a fresh installation">}}. This deployment type is currently in beta, and installations with more than five nodes will not support upgrades to future NetQ versions.
- You can now increase the TTL of your time-series database by configuring a list of metrics that NetQ ignores.
- Multiplane support: topology, TCA events, UI filters
- You can now create {{<link title="Configure and Monitor Threshold-Crossing Events" text="threshold-crossing rules">}} with a wider range of measurement units in both the UI and the CLI. Additionally, NetQ no longer broadcasts multiple events for breaches to the same threshold-crossing rule. <!--link to change new default behavior-->
- Performance improvements to the account management page in the UI
- The time required to install NetQ has been reduced.
- NetQ for NVLink API changes:
    - Added the ability to download support packages and upgrade NVOS for all switches within an NVLink domain.
    - Added an endpoint to retrieve NetQ's version
    - Added a fault tolerance mechanism that allows NVLink switches with at least two out-of-band management ports to maintain connectivity to NMX controller and telemetry services in case of port failure.
    - Queries to the `compute-nodes` endpoint now return hostnames within the response
    - Performance improvements to scale deployments
    - Refer to the {{<link title="NetQ NVLink API Changelog">}} for a comprehensive list of changes


## Release Considerations



### Upgrade Paths

NetQ 5.1 is available exclusively for on-premises deployments. You can upgrade to 5.1 if your deployment is running version 5.0 or 4.15. First {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then concurrently restore your data and upgrade NetQ during a {{<link title="Install the NetQ System" text="new NetQ 5.0 installation">}}.


### Compatible Agent Versions

The NetQ 5.1 server is compatible with NetQ agents 5.1 and 5.0. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.16, 5.15, 5.11.3, 5.9.4
- Ubuntu 24.04, 22.04