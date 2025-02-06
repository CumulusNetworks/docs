---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.12 Release Notes" text="release notes">}}.

## What's New in NetQ 4.12

NetQ 4.12.0 includes the following new features and improvements:

- {{<link title="Before You Install" text="New installation option">}} that supports up to 1,000 switches
- {{<link title="Focus Your Monitoring Using Workbenches" text="New workbench">}} with {{<link title="Access Data with Cards" text="additional cards">}} that you can add to your existing workbenches
- Compare interfaces and view counter data across links with the {{<link title="Interfaces/#compare-link-interfaces" text="link health view">}} (beta)
- View a switch's BGP and EVPN session information from the full-screen {{<link title="Switches" text="switch dashboard">}}
- New option to send all events to a notification channel as part of {{<link title="Configure System Event Notifications/#create-a-channel" text="the channel setup process">}}
- The {{<link title="Network Topology" text="topology view">}} is now generally available
- The {{<link title="Validate Network Protocol and Service Operations/#topology-validations" text="topology validation">}} is now generally available

## Upgrade Paths

For deployments running:

- 4.11, 4.10.1: {{<link title="Upgrade NetQ Virtual Machines" text="upgrade directly">}} to NetQ 4.12
- 4.10.0 or earlier: {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}} and perform a {{<link title="Install the NetQ System" text="new installation">}}

## Compatible Agent Versions

The NetQ 4.12 server is compatible with the NetQ 4.12 agent. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.0.0 or later (Spectrum switches)
- Ubuntu 22.04, 20.04

## Release Considerations

- NetQ 4.12 is not backward compatible with previous NetQ agent versions. You must install NetQ agent version 4.12 after upgrading your NetQ server to 4.12.
- When you upgrade to NetQ 4.12, any pre-existing event and validation data will be lost.
- If you upgrade a NetQ server with scheduled OSPF validations, they might still appear in the UI but will display results from previous validations.