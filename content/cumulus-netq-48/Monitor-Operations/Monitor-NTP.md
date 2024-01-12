---
title: NTP
author: NVIDIA
weight: 900
toc: 3
---
Use the CLI to view Network Time Protocol (NTP). The command output displays the time synchronization status for all devices. You can filter for devices that are either in synchronization or out of synchronization, currently or at a time in the past.

Monitor NTP with the following commands. See the {{<link title="show/#netq-show-ntp" text="command line reference">}} for additional options, definitions, and examples.

```
netq show ntp
netq show events message_type ntp
netq show events-config message_type ntp
```
The {{<link title="check/#netq check ntp" text="netq check ntp">}} command verifies network time synchronization for all nodes (leafs, spines, and hosts) in your network fabric.

```
netq check ntp
```