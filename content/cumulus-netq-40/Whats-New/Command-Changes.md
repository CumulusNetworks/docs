---
title: NetQ CLI Changes
author: NVIDIA
weight: 20
toc: 4
---

Many commands have changed in this release to accommodate the addition of new options or to simplify their syntax. Additionally, new commands have been added and others have been removed. A summary of those changes is provided here.

## New Commands

The following table summarizes the new commands available with this release.

| Command | Summary | Version |
| ------- | ------- | ------- |
| netq config add agent opta-enable | Enables or disables the NetQ Platform (also known as OPTA). | 4.0.0 |
| netq config add agent gnmi-enable | Enables or disables the gNMI agent. | 4.0.0 |
| netq config add agent gnmi-log-level | Sets the log level verbosity for the gNMI agent. | 4.0.0 |
| netq config add agent gnmi-port | Changes the gNMI port. | 4.0.0 |
| netq add check-filter | Creates a filter for validations. | 4.0.0 |
| netq del check-filter | Deletes the specified check filter. | 4.0.0 |
| netq show check-filter | Shows all check filters. | 4.0.0 |
| netq [&lt;hostname>] show roce-counters | Displays the RoCE counters. | 4.0.0 |                             
| netq [&lt;hostname>] show roce-config | Displays the RoCE configuration. | 4.0.0 |
| netq [&lt;hostname>] show roce-counters pool | Displays the RoCE counter pools. | 4.0.0 |

## Modified Commands

The following table summarizes the commands that have been changed with this release.

| Updated Command | What Changed | Version |
| --------------- | ------------ | ------- |
| netq check agents<br/>netq check bgp<br/>netq check cl-version<br/>netq check clag<br/>netq check evpn<br/>netq check interfaces<br/>netq check mlag<br/>netq check mtu<br/>netq check ntp<br/>netq check ospf<br/>netq check sensors<br/>netq check vlan<br/>netq check vxlan<br/>netq show unit-tests agent<br/>netq show unit-tests bgp<br/>netq show unit-tests cl-version<br/>netq show unit-tests evpn<br/>netq show unit-tests interfaces<br/>netq show unit-tests ntp<br/>netq show unit-tests ospf<br/>netq show unit-tests sensors<br/>netq show unit-tests vlan<br/>netq show unit-tests vxlan | Added `[check_filter_id &lt;text-check-filter-id>]` as an option, so you can specify a unique ID for a check filter. | 4.0.0 |
| netq check agents<br/>netq check bgp<br/>netq check clag<br/>netq check interfaces<br/>netq check mlag<br/>netq check mtu<br/>netq check ntp | Added `[streaming]` option to perform a streaming query check. | 4.0.0 |
| netq [&lt;hostname>] show bgp | Added `[established|failed]` options to show only established or failed BGP sessions. | 4.0.0 |
| netq config add agent wjh-threshold | You can specify *all* instead of a list of traffic classes (`&lt;text-tc-list>`) or a list of ports `(&lt;text-port-list>)`. | 4.0.0 |
| netq config del agent wjh-threshold | You can specify *all* instead of a list of traffic classes (`&lt;text-tc-list>`). | 4.0.0 |
| netq [&lt;hostname>] show events | Added `tca_roce` and `roceconfig` event types. | 4.0.0 |
| netq lcm upgrade | Changed the `run-before-after` option to `run-snapshot-before-after`. | 4.0.0 |

## Removed Commands

The following table summarizes the commands that have been removed in this release.

| Updated Command | Version |
| --------------- | ------- |
| netq check license | 4.0.0 |
| netq show license | 4.0.0 |
| netq show unit-tests license | 4.0.0 |
