---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.5 Release Notes" text="release notes">}}.

<!-- vale off -->
## What's New in NetQ 4.5.0
<!-- vale on -->
NetQ 4.5.0 includes the following new features and improvements:

 - {{<link title="Credentials and Profiles" text="Access credentials">}} that can be applied to individual switches for better security and increased flexibility
 - RoCE {{<link title="check/#netq-check-roce" text="check">}} and {{<link title="show/#netq-show-roce-config" text="show">}} commands that display priority code point (PCP) and switch priority (SP) mapping misconfigurations and recommendations
 - Lifecycle management for NVUE-enabled {{<link title="Upgrade Cumulus Linux Using LCM" text="upgrades to Cumulus Linux 5.0.0 and later">}}
 - Initial support for Precision Time Protocol monitoring via the UI and CLI (not intended for use in production)
 - User guide enhancements, including a {{<link title="Troubleshoot NetQ" text="NetQ troubleshooting guide">}} and updated {{<link title="NetQ CLI Reference" text="command line reference">}}

## Upgrade Paths

NetQ 4.5.0 images have been upgraded to Ubuntu 20.04. 

To {{<link title="Upgrade NetQ Appliances and Virtual Machines" text="upgrade to NetQ 4.5.0">}}, you must back up your current NetQ data and perform a new installation of NetQ 4.5.0. This process is supported when upgrading from NetQ 4.3.0 or above.

Upgrades from releases earlier than NetQ 4.3.0 require an incremental {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-43/Installation-Management/Upgrade-NetQ/Upgrade-System/" text="upgrade to version 4.3.0">}} before you {{<link title="Upgrade NetQ Appliances and Virtual Machines" text="back up your data">}} and perform a new installation of NetQ 4.5.0.

The NetQ Hardware Appliance is no longer available for purchase. For existing customers, contact NVIDIA support for assistance upgrading to 4.5.
## Compatible Agent Versions

NetQ 4.5.0 is compatible with NetQ Agent versions 4.4.0 and above. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 3.7.16 and later
- SONiC 202012
- CentOS 7
- RHEL 7.1
- Ubuntu 18.04

You must upgrade to the latest agent version to enable 4.5 features.
