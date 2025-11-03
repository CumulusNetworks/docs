---
title: Data Retention
author: NVIDIA
weight: 1130
toc: 3
---

NetQ deletes some types of data periodically to minimize database usage and increase performance. The following table outlines the amount of time (in days) that NetQ retains data. When data reaches the end of the retention period, it is deleted automatically. There is no way to reduce or increase the retention period. 

| Feature | Retention Period (Days) |
| -------------| :---: |
|Agent validations | 40 |
|BGP validations | 30 |
|Device inventory  | 40 |
|Duplicate IP address validations | 40 |
|EVPN validations | 30 |
|Flow analysis | 40 |
|Interface validations | 30 |
|Link health | 3 |
|MLAG validations | 30 |
|MTU validations | 30 |
|Network snapshots | 40 |
|NTP validations | 40 |
|Queue histograms | 3 |
|RoCE data | 40 |
|RoCE validations | 30 |
|Sensor validations | 40 |
|Topology data | 40 |
|Topology validations | 40 |
|Validation filters | 40 |
|VLAN validations | 30 |
|VXLAN validations | 30 |
|What Just Happened data | 40 |

