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
- You can now name a threshold-crossing rule {{<link title="add/#netq-add-tca" text="using the command line">}}.
- Deprecated support for administrative and operational state mismatch checks that are run as part of interface validations. If you are running an older version of NetQ, you may still see errors related to these checks in the interface validation results. They can be safely ignored.
- Security, performance, and usability improvements


## Upgrade Paths

You can upgrade to NetQ 4.13 if your deployment is running version 4.12 or 4.11. For on-premises and cloud deployments, {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then restore your data during a {{<link title="Install the NetQ System" text="new NetQ 4.13 installation">}}.

{{%notice note%}}
When you upgrade from NetQ 4.11 to 4.13, any pre-existing validation data will be lost.
{{%/notice%}}

## Compatible Agent Versions

The NetQ 4.13 server is compatible with NetQ agents 4.12 and 4.13. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.9.2 or later
- Ubuntu 22.04

NVIDIA recommends upgrading to the latest agent version.