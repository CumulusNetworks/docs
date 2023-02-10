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

 - Early access support for monitoring {{<link title="PTP" text="Precision Time Protocol">}}
 - {{<link title="Credentials and Profiles" text="Access credentials">}} that can be applied to individual switches for better security and increased flexibility
 - RoCE {{<link title="check/#netq-check-roce" text="check">}} and {{<link title="show/#netq-show-roce-config" text="show">}} commands that display PCP (priority code point) and SP (switch priority) mapping misconfigurations and recommendations
 - Lifecycle management for NVUE-enabled {{<link title="Upgrade Cumulus Linux Using LCM" text="upgrades to Cumulus Linux 5.0.0 and later">}}
 - User guide enhancements, including a {{<link title="Troubleshoot NetQ" text="NetQ troubleshooting guide">}} and updated {{<link title="NetQ CLI Reference" text="command line reference">}}

## Upgrade Paths

NetQ 4.5.0 images have been upgraded to Ubuntu 20.04. To {{<link title="Upgrade NetQ Appliances and Virtual Machines" text="upgrade to NetQ 4.5.0">}}, you must back up your current NetQ data and perform a new installation of NetQ 4.5.0. 
## Compatible Agent Versions

NetQ 4.4.0 is compatible with NetQ Agent versions 4.3.0 and above. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 3.7.12 and later
- SONiC 202012 to 202106
- CentOS 7
- RHEL 7.1
- Ubuntu 18.04


