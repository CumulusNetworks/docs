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

- New option to add additional nodes to your HA scale cluster deployment, supporting up to 2,000 switches
- Performance and usability improvements to {{<link title="Switches/#view-queue-lengths-as-histograms" text="queue length histograms">}}
- New functionality that allows you to {{<link title="Monitor Events/#create-event-filters" text="create and save filters">}} for system and What Just Happened events
- {{<link title="Interfaces/#compare-link-interfaces" text="Link health view">}} is now generally available
- Added ability to filter hostnames using regular expressions
- Improved table layout and column order
- Security and performance improvements
- Added support for Ubuntu 22.04 and deprecated support for Ubuntu 20.04


## Upgrade Paths

To upgrade to NetQ 4.13.0, {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}} and perform a new installation of NetQ 4.13.0. This process is supported when upgrading from NetQ 4.11 or 4.12.

## Compatible Agent Versions

The NetQ 4.12 server is compatible with the NetQ 4.12 agent. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.0.0 or later (Spectrum switches)
- Ubuntu 22.04

## Release Considerations

- When you upgrade to NetQ 4.13, any pre-existing PTP data will be lost.