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

- Keep track of your network's devices at a glance and access actions in fewer clicks using the {{<link title="Application Layout" text="redesigned dashboard navigation">}}. 
- {{<link title="Application Layout/#search" text="Search for a switch">}} and right-click the device to open a dashboard in a new tab that displays an {{<link title="Switches" text="overview of the switch's attributes">}}, events, resource utilization, and interface details.
- {{<link title="Validate Network Protocol and Service Operations/#topology-validations" text="Validate your network's topology">}}. NetQ compares the actual network topology derived from LLDP telemetry data against a topology blueprint that you upload to the UI (beta).
- Monitor a device's link bit error rates (BER) with the {{<link title="show/#netq show dom" text="netq show dom ber">}} command. Or view BER in the UI by searching for the device in the global search field and filtering for diagnostic info from the digital optics tab.
- Create threshold crossing rules that alert you when a {{<link title="Threshold-Crossing Events Reference#sensors" text="sensor's state changes">}}.
- {{<link title="Focus Your Monitoring Using Workbenches#manage-auto-refresh" text="Adjust the frequency">}} that NetQ reloads dashboard data to every minute, 2 minutes, or 5 minutes.

## Upgrade Paths

For deployments running:

- 4.10, 4.9: {{<link title="Upgrade NetQ Virtual Machines" text="upgrade directly">}} to NetQ 4.11
- 4.8 or earlier: {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}} and perform a {{<link title="Install the NetQ System" text="new installation">}}

## Compatible Agent Versions

The NetQ 4.11 server is compatible with NetQ Agent 4.9 or later. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 5.0.0 or later (Spectrum switches)
- Cumulus Linux 4.3.1 and 4.3.2 (Broadcom switches)
- SONiC 202012
- Ubuntu 20.04

You must upgrade to the latest agent version to enable 4.11 features.

{{%notice info%}}
Switches running Cumulus Linux 5.9 or later require the NetQ 4.10 or later agent package. See {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/Installation-Management/Install-NetQ/Install-NetQ-Agents/" text="Install NetQ Agents">}}.
{{%/notice%}}