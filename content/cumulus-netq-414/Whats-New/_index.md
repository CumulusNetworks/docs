---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.14 Release Notes" text="release notes">}}.

## What's New in NetQ 4.14

NetQ 4.14.0 includes the following new features:

- Expanded support for hostname filtering: NetQ now supports partial-word match and will suggest results for all hostnames that match the filter query. This feature is also supported when you filter using regular expressions.
- Security, performance, and usability improvements

<!-- You can now name a threshold-crossing rule {{<link title="add/#netq-add-tca" text="using the command line">}}. Miriam to confirm-->

## Upgrade Paths

For deployments running:

- 4.13.0: {{<link title="Upgrade NetQ Virtual Machines" text="upgrade directly">}} to NetQ 4.14.0
- 4.12.0 or earlier: {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then concurrently restore your data and upgrade NetQ during a {{<link title="Install the NetQ System" text="new NetQ 4.14 installation">}}


{{%notice note%}}
When you upgrade from NetQ v4.14.0, any pre-existing validation data will be lost. Additionally, NetQ will not retain data related to network services (including BGP, LLDP, EVPN, and MLAG) after upgrading.
{{%/notice%}}

## Compatible Agent Versions

The NetQ 4.14 server is compatible with NetQ agents 4.14 and 4.13. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.12.1, 5.11.1, or 5.9.2
- Ubuntu 22.04

NVIDIA recommends upgrading to the latest agent version.