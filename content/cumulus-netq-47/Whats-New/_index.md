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

- {{<link title="Focus Your Monitoring Using Workbenches" text="Create workbenches">}} that can be accessed from an individual premises or that are available globally, across premises
- {{<link title="Configure and Monitor What Just Happened/#suppress-events-with-filters" text="Create WJH suppression rules">}} based on IP addresses
- WIP: {{<link title="Configure and Monitor What Just Happened/#vew-what-just-happenned-metrics" text="">}} aggregate duplicate WJH L1 errors on the same port
- WIP: monitor CPU and memory utilization for services and processes, create TCA rules to limit CPU and memory usage by services/processes
- WIP: Performance improvements to the NetQ Agent (that limit CPU usage to 50%)
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
