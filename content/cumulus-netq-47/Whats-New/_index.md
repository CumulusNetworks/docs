---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.7 Release Notes" text="release notes">}}.

<!-- vale off -->
## What's New in NetQ 4.7.0
<!-- vale on -->
NetQ 4.7.0 includes the following new features and improvements:

- View network interface controller (NIC) {{<link title="NICs" text="telemetry">}} and {{<link title="NIC Inventory" text="inventory">}} data in the UI 
- Decommission {{<link title="Host Inventory/#decommission-a-host" text="hosts">}}, {{<link title="NIC Inventory/#decommission-a-nic" text="NICs">}}, and {{<link title="DPU Inventory/#decommission-a-dpu" text="DPUs">}} from the UI or CLI
- {{<link title="Focus Your Monitoring Using Workbenches" text="Create workbenches">}} that can be accessed from an individual premises or that are available globally, across multiple premises
- {{<link title="Configure and Monitor What Just Happened/#suppress-events-with-filters" text="Create WJH suppression rules">}} based on IP addresses
- WIP: Visualize egress queue lengths in histograms in the UI 
- WIP: {{<link title="Configure and Monitor What Just Happened/#view-what-just-happened-metrics" text="">}} aggregate WJH L1 errors that occur on the same port
- WIP: {{<link title="Switches/#monitor-resource-utilization-for-processes-and-services" text="">}} monitor CPU and memory utilization for services and processes, create TCA rules to limit CPU and memory usage by services/processes
- Performance improvements to the NetQ Agent that limit it from consuming more than 50% of CPU resources

## Upgrade Paths

You can {{<link title="Upgrade NetQ" text="upgrade directly to NetQ 4.7.0">}} if your deployment is currently running version 4.5.0 or later.

To {{<link title="Upgrade NetQ" text="upgrade to NetQ 4.7.0">}} from versions earlier than 4.5.0, you must back up your current NetQ data and perform a new installation of NetQ 4.7.0. This process is supported when upgrading from NetQ 4.3.0 or above.

Upgrades from releases earlier than NetQ 4.3.0 require an incremental {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-43/Installation-Management/Upgrade-NetQ/Upgrade-System/" text="upgrade to version 4.3.0">}} before you {{<link title="Upgrade NetQ" text="back up your data">}} and perform a new installation of NetQ 4.5.0.
## Compatible Agent Versions

NetQ 4.6.0 is compatible with NetQ Agent versions 4.5.0 and later. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 4.3.0 and later (Broadcom switches)
- Cumulus Linux 4.4.0 and later (Spectrum switches)
- SONiC 202012
- CentOS 7
- RHEL 7.1
- Ubuntu 18.04

You must upgrade to the latest agent version to enable 4.7 features.
