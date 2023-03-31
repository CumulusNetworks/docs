---
title: NVUE Command Reference
author: Cumulus Networks
weight: -34
subsection: true
cascade:
  product: Cumulus Linux
toc: 1
---
{{%notice note%}}
This document is in Beta.
{{%/notice%}}

NVUE is an object-oriented, schema driven model of a complete Cumulus Linux system (hardware and software) providing a robust API that allows for multiple interfaces to both view (show) and configure (set and unset) any element within a system running the NVUE software.

This document is a reference for the Cumulus Linux NVUE CLI commands.

## Command Types

The NVUE CLI provides the following commands:
- {{<link url="Show-Commands" text="nv show">}} commands show various parts of the network configuration.
- {{<link url="Set-and-Unset-Commands" text="nv set">}} commands set configuration options on the switch.
- {{<link url="Set-and-Unset-Commands" text="nv unset">}} commands unset configuration options on the switch.
- {{<link url="Config-Commands" text="nv config">}} commands manage and apply configurations.
- {{<link url="Action-Commands" text="nv action">}} commands reset counters, remove MLAG LACP conflicts, and disconnect authorized and authenticated users.
