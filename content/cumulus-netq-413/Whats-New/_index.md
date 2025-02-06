---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.13 Release Notes" text="release notes">}}.

## What's New in NetQ 4.13

NetQ 4.13.0 includes the following new features:

- New option to add additional nodes to your {{<link title="Before You Install" text="HA scale cluster deployment">}}, supporting up to 2,000 switches
- Performance and usability improvements to {{<link title="Switches/#view-queue-lengths-as-histograms" text="queue length histograms">}}
- New functionality that allows you to {{<link title="Monitor Events/#create-event-filters" text="create and save filters">}} for system and What Just Happened events
- {{<link title="Interfaces/#compare-link-interfaces" text="Link health view">}} is now generally available
- Added ability to filter hostnames using regular expressions
- Improved table layout and column order
- Added support for Ubuntu 22.04 and deprecated support for Ubuntu 20.04
- Security and performance improvements


## Upgrade Paths

You can upgrade directly to NetQ 4.13 if your deployment is running version 4.12 or 4.11.

- For on-premises deployments: {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}} and use the new data restoration workflow to install NetQ 4.13
- For cloud deployments: perform a {{<link title="Install the NetQ System" text="fresh 4.13 installation">}}

## Compatible Agent Versions

The NetQ 4.13 server is compatible with NetQ agent 4.12 or later. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.0.0 or later (Spectrum switches)
- Ubuntu 22.04
