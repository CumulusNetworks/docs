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
This release includes several performance and infrastructure improvements that make NetQ faster and more reliable. Additional features and improvements include:


RoCE command line updates. The `netq check roce` {{<link title="check#netq-check-roce" text="command output">}} now includes a column displaying PCP (priority code point) and SP (switch priority) mapping misconfigurations and recommendations. `netq show roce-config` displays all {{<link title="RoCE#view-the-roce-configuration" text="PCP and SP mappings">}}.

Lifecycle management now supports {{<link title="Upgrade Cumulus Linux Using LCM" text="upgrades to Cumulus Linux 5.0.0 and later">}} with and without NVUE enabled.

Precision time protocol (PTP) monitoring

An updated command line reference


## Upgrade Paths

You can upgrade to NetQ 4.4.0 directly from versions 4.1.0 or later. Upgrades from releases earlier than NetQ 4.1.0 require a fresh installation or an incremental upgrade to version 4.1.0 first.

NetQ no longer supports the Admin UI for installation and upgrades. Follow the {{<link title="Installation Management" text="updated instructions">}} according to your deployment model.
## Compatible Agent Versions

NetQ 4.4.0 is compatible with NetQ Agent versions 4.3.0 and above. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 3.7.12 and later
- SONiC 202012 to 202106
- CentOS 7
- RHEL 7.1
- Ubuntu 18.04


