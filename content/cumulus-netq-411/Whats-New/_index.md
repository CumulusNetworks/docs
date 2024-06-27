---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.11 Release Notes" text="release notes">}}.

## What's New in NetQ 4.11

NetQ 4.11.0 includes the following new features and improvements:

- Validate your network's topology. NetQ compares the actual network topology derived from LLDP telemetry data against a topology blueprint that you upload to the UI.
- {{<link title="Focus Your Monitoring Using Workbenches#manage-auto-refresh" text="Adjust the frequency">}} that NetQ reloads dashboard data to every minute, 2 minutes, or 5 minutes
- Create threshold crossing rules that alert you when a {{<link title="Threshold-Crossing Events Reference#sensors" text="sensor's state changes">}}
- Performance and security enhancements


## Upgrade Paths

For deployments running:

- 4.9.0, 4.8.0: {{<link title="Upgrade NetQ Virtual Machines" text="upgrade directly">}} to NetQ 4.10.
- 4.7.0 or earlier: {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}} and perform a {{<link title="Install the NetQ System" text="new installation">}}.

## Compatible Agent Versions

The NetQ 4.11 server is compatible with NetQ Agent 4.9 or later. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 5.0.0 or later (Spectrum switches)
- Cumulus Linux 4.3.1 and 4.3.2 (Broadcom switches)
- SONiC 202012
- CentOS 7
- RHEL 7.1
- Ubuntu 20.04

You must upgrade to the latest agent version to enable 4.11 features.

{{%notice info%}}
Switches running Cumulus Linux 5.9 require the NetQ 4.10 or later agent package. See {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/Installation-Management/Install-NetQ/Install-NetQ-Agents/" text="Install NetQ Agents">}}.
{{%/notice%}}
