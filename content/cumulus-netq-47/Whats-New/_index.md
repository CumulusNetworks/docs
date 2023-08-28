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

- {{<link title="Switches/#view-cpu-and-memory-utilization-for-processes-and-services" text="Monitor CPU and memory utilization">}} for services and processes; create threshold-crossing rules that generate events when a process or service exceeds the limit you defined
- {{<link title="Switches/#view-queue-lengths-in-histograms" text="View queue lengths in the form of histograms">}}
- {{<link title="Focus Your Monitoring Using Workbenches" text="Create workbenches">}} that can be accessed from an individual premises or that are available globally, across multiple premises
- View ConnectX network interface controller (NIC) {{<link title="NICs" text="telemetry">}} and {{<link title="NIC Inventory" text="inventory">}} data in the UI 
- Decommission {{<link title="Host Inventory/#decommission-a-host" text="hosts">}}, {{<link title="NIC Inventory/#decommission-a-nic" text="NICs">}}, and {{<link title="DPU Inventory/#decommission-a-dpu" text="DPUs">}} from the UI or CLI
- Create What Just Happened filters that suppress events {{<link title="config/#netq-config-add-agent-wjh-drop-filter" text="based on IP addresses">}}; {{<link title="Configure and Monitor What Just Happened/#view-what-just-happened-metrics" text="aggregate WJH L1 errors">}} that occur on the same port
- New instructions for installing the {{<link title="Install NIC and DPU Agents" text="DOCA Telemetry Service on hosts and DPUs">}}
- Performance improvements to the NetQ Agent that limit its CPU usage

## Upgrade Paths

For deployments running:

- 4.6.0 or 4.5.0: {{<link title="Upgrade NetQ/#upgrading-from-netq-4.5.0-or-later" text="upgrade directly">}} to NetQ 4.7.0
- 4.4.1, 4.4.0, or 4.3.0: {{<link title="Back Up and Restore NetQ/#back-up-netq-4.4.1-or-earlier" text="back up your NetQ data">}} and perform a {{<link title="Install NetQ" text="new installation of NetQ 4.7.0">}}. 
- 4.2.0 or earlier: upgrade incrementally {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-43/Installation-Management/Upgrade-NetQ/Upgrade-System/" text="to version 4.3.0">}}. Then {{<link title="Back Up and Restore NetQ/#back-up-netq-4.4.1-or-earlier" text="back up your NetQ data">}} and perform a {{<link title="Install NetQ" text="new installation of NetQ 4.7.0">}}.

## Compatible Agent Versions

The NetQ 4.7.0 server is compatible with NetQ Agents 4.6.0 and 4.7.0. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 4.3.0 and above (Broadcom switches)
- Cumulus Linux 5.0.0 and above (Spectrum switches)
- SONiC 202012
- CentOS 7
- RHEL 7.1
- Ubuntu 20.04

You must upgrade to the latest agent version to enable 4.7 features.
