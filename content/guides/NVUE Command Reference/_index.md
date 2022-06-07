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

This document is a reference for the Cumulus Linux NVUE CLI commands, and provides a description and usage for each command.

## Command Types

The NVUE CLI provides the following commands:
- {{<link url="Show-Commands" text="nv show">}} commands show various parts of the network configuration.
- {{<link url="Set-Commands" text="nv set">}} commands set configuration options on the switch.
- {{<link url="Unset-Commands" text="nv unset">}} commands unset configuration options on the switch.
- {{<link url="Config-and-Action-Commands" text="nv config">}} commands manage and apply configurations.

## Command Syntax

Cumulus Linux NVUE CLI commands uses the following syntax:

| Syntax | Description |
| ------ | ----------- |
| [ ] |  Brackets identify options you can use with a command.|
|  \| |A vertical bar separates mutually exclusive options for a command. |
| < >| Angle brackets identify variables that you must replace.|
| ... | Elipses indicate that you can repeat the previous option multiple times with different values. |
