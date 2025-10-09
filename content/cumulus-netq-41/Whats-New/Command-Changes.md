---
title: NetQ CLI Changes
author: NVIDIA
weight: 20
toc: 4
---

Many commands have changed in this release to accommodate the addition of new options or to simplify their syntax. Additionally, NVIDIA added new commands while removing others. This topic provides a summary of those changes.

## New Commands

The following table summarizes the new commands available with this release.

| Command | Summary | Version |
| ------- | ------- | ------- |
| netq add notification channel generic | Configures the generic webhook channel. | 4.1.0 |
| netq install cluster add-worker | Adds a new worker node in an on-premise cluster deployment. | 4.1.0 |
| netq install opta cluster add-worker | Adds a new worker node in a cloud-hosted cluster deployment. | 4.1.0 |
| netq check addresses | Validation for duplicate address detection. | 4.1.0 |

## Modified Commands

The following table summarizes the commands that have changed with this release.
<!-- vale off -->
| Updated Command | What Changed | Version |
| --------------- | ------------ | ------- |
| netq show wjh-drop | added `[between <text-fixed-time> and <text-fixed-endtime>] [around <text-fixed-time>]` This accepts a time string such as 10m, 30s, 1h, 1d. Absolute epoch time in seconds is also accepted e.g. 1638205776 | 4.1.0 |
| netq check evpn<br/>netq check vxlan | Added `[streaming]` option to perform a streaming query check. | 4.1.0 |
| netq check evpn | Removed `mac-consistency` option. Use `include 2` for this data instead. | 4.1.0 |
| netq <hostname> show ip routes <br/> netq show ip routes <br/> netq <hostname> show ipv6 routes <br/> netq show ipv6 routes | Added `[edge]` option to display the edge switch that a route is learned from on hosts and network devices that do not run Cumulus Linux. | 4.1.0 |
<!-- vale on -->
## Removed Commands

<!-- vale off -->
The following table summarizes the commands that have been removed in this release.
<!-- vale on -->

| Updated Command | Version |
| --------------- | ------- |
| netq config add agent gnmi-log-level | 4.1.0 |

