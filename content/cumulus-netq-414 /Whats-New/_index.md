---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.14 Release Notes" text="release notes">}}.

## What's New in NetQ 4.13

NetQ 4.13.0 includes the following new features:

- New option to {{<link title="Set Up Your Virtual Machine for an On-premises HA Scale Cluster/#add-additional-worker-nodes" text="add additional nodes">}} to your scale-cluster deployment, supporting networks with up to 2,000 switches. {{<link title="Before You Install" text="Read more about NetQ deployment options">}}.
- Performance and usability improvements to {{<link title="Switches/#view-queue-lengths-as-histograms" text="queue length histograms">}}
- New functionality that allows you to {{<link title="Monitor Events/#create-event-filters" text="create and save filters">}} for system and What Just Happened events
- Added ability to filter hostnames using regular expressions
- Improved table layout and column order
- Added support for Ubuntu 22.04 and deprecated support for Ubuntu 20.04
- Security and performance improvements


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