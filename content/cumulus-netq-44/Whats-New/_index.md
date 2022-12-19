---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.4 Release Notes" text="release notes">}}.

<!-- vale off -->

## What's New in NetQ 4.4.1

This release includes important security updates. NVIDIA recommends upgrading to this release to improve software security and reliability.
## What's New in NetQ 4.4.0
<!-- vale on -->
This release includes several performance and infrastructure improvements that make NetQ faster and more reliable. It also includes extensive security enhancements and bug fixes. NVIDIA recommends upgrading to this release to improve software security and reliability. Additional updates include:

Command line updates: 

- `netq check` validation commands are now streaming checks by default.
- `netq show events` commands have an updated syntax: `type` is now `message_type` and `level` is now `severity`. These commands are updated in their respective categories in this user guide.

User guide updates:

- New section defining {{<link title="Accounts and Roles" text="NetQ admin and user roles">}}

## Upgrade Paths

You can upgrade to NetQ 4.4 directly from versions 4.1.0 or later. Upgrades from releases earlier than NetQ 4.1.0 require a fresh installation or an incremental upgrade to version 4.1.0 first.

NetQ no longer supports the Admin UI for installation and upgrades. Follow the {{<link title="Installation Management" text="updated instructions">}} according to your deployment model.
## Compatible Agent Versions

NetQ 4.4 is compatible with NetQ Agent versions 4.3.0 and above. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 3.7.12 and later
- SONiC 202012 to 202106
- CentOS 7
- RHEL 7.1
- Ubuntu 18.04


