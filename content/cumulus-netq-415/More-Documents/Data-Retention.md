---
title: Data Retention
author: NVIDIA
weight: 1130
toc: 3
---

NetQ deletes some types of data periodically to minimize database usage and increase performance. The following table outlines the amount of time (in days) that NetQ retains data. When data reaches the end of the retention period, it is deleted automatically. There is no way to reduce or increase the retention period. 

| Feature | Retention Period (Days) |
| -------------| :---: |
|Queue histograms | 3 |
|Link health | 3 |
|OTLP metrics | 7 |
|Validation results | 30*, 40<sup>†</sup>|
|Flow analysis | 40 |
|RoCE data | 40 |
|Device inventory  | 40 |
|Network snapshots | 40 |
|Topology data | 40 |
|What Just Happened data | 40 |

*30-day: BGP, EVPN, interfaces, MLAG, MTU, RoCE, VLAN, VXLAN<br>
<sup>†</sup>40-day: addresses, agent, NTP, sensors, topology, validation filters

