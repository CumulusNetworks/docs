---
title: Data Retention Policies
author: NVIDIA
weight: 1140
toc: 3
---

NetQ deletes some types of data periodically to minimize database usage and potentially increase performance. The following table outlines NetQ’s time to live (TTL) policies.

| Entry Name | Feature | TTL (days) |
| ------------- | :---: | :---: |
|netq.acl_resource |  | 40 |
|netq.address | IP addresses | 40 |
|netq.agentstats | NetQ Agent data | 40 |
|netq.appinfo | 
|netq.arconfigglobal |
|netq.arconfigglobalv2 |
|netq.arconfigintf |
|netq.arconfigprofile |
|netq.arecmpinfo |
|netq.asic_queue_histogram |
|netq.asic_queue_histogram_aggregate |
|netq.asic_queue_histogram_device_summary |
|netq.asic_queue_histogram_device_summary_aggregate |
|netq.ber_info | Bit error rates | 40 |