---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.12 Release Notes" text="release notes">}}.

## What's New in NetQ 4.12

NetQ 4.12.0 includes the following new features and improvements:

- View and BGP and EVPN session information in the full-screen {{<link title="Switches" text="switch dashboard">}}

## Upgrade Paths

For deployments running:

- 4.10, 4.9: {{<link title="Upgrade NetQ Virtual Machines" text="upgrade directly">}} to NetQ 4.11
- 4.8 or earlier: {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}} and perform a {{<link title="Install the NetQ System" text="new installation">}}

## Compatible Agent Versions

The NetQ 4.11 server is compatible with NetQ Agent 4.9 or later. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 5.0.0 or later (Spectrum switches)
- Cumulus Linux 4.3.1 and 4.3.2 (Broadcom switches)
- Ubuntu 20.04

You must upgrade to the latest agent version to enable 4.11 features.

{{%notice info%}}
Switches running Cumulus Linux 5.9 or later require the NetQ 4.10 or later agent package. See {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/Installation-Management/Install-NetQ/Install-NetQ-Agents/" text="Install NetQ Agents">}}.
{{%/notice%}}