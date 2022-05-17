---
title: NVUE Command Reference
author: Cumulus Networks
weight: -34
subsection: true
cascade:
  product: Cumulus Linux
toc: 1
---
NVUE is an object-oriented, schema driven model of a complete Cumulus Linux system (hardware and software) providing a robust API that allows for multiple interfaces to both view (show) and configure (set and unset) any element within a system running the NVUE software.

## Command Syntax

This command reference uses the following syntax:

| Syntax | Description | Example |
| ------ | ----------- | ------- |
| [ ] |  Brackets identify options you can use with a command.| `nv show interface <interface-id> lldp neighbor`<br>`nv show interface swp1 lldp neighbor` |
|  \| |A vertical bar  separates mutually exclusive options for a command. | |
| < >| Angle brackets (`< >`) identify variables that you must replace.| |

The NVUE CLI provides the following commands:
- {{<link url="Show-Commands" text="show">}} commands show various parts of the network configuration.
- {{<link url="Set-Commands" text="set">}} commands set configuration options on the switch.
- {{<link url="Set-Commands" text="unset">}} commands unset configuration options on the switch.
- {{<link url="Config-Commands" text="config">}} commands manage and apply configurations.
