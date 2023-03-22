---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.6 Release Notes" text="release notes">}}.

<!-- vale off -->
## What's New in NetQ 4.6.0
<!-- vale on -->
NetQ 4.6.0 includes the following new features and improvements:

- Full support for {{<link title="PTP" text="Precision Time Protocol monitoring">}} via the UI and CLI
- Expanded {{<link title="Access Data with Cards#table-settings" text="table options">}} that allow you to export and download tables that exceed 10,000 rows as a CSV file


## Upgrade Paths

NetQ 4.5.0 images have been upgraded to Ubuntu 20.04. 

To {{<link title="Upgrade NetQ Appliances and Virtual Machines" text="upgrade to NetQ 4.5.0">}}, you must back up your current NetQ data and perform a new installation of NetQ 4.5.0. This process is supported when upgrading from NetQ 4.3.0 or above.

Upgrades from releases earlier than NetQ 4.3.0 require an incremental {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-43/Installation-Management/Upgrade-NetQ/Upgrade-System/" text="upgrade to version 4.3.0">}} before you {{<link title="Upgrade NetQ Appliances and Virtual Machines" text="back up your data">}} and perform a new installation of NetQ 4.5.0.
## Compatible Agent Versions

NetQ 4.5.0 is compatible with NetQ Agent versions 4.4.0 and above. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 3.7.16 and later
- SONiC 202012
- CentOS 7
- RHEL 7.1
- Ubuntu 18.04

You must upgrade to the latest agent version to enable 4.5 features.
