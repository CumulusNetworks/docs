---
title: Adaptive Routing
author: NVIDIA
weight: 790
toc: 3
---

{{<notice note>}}

Adaptive routing monitoring is supported on Spectrum-2 switches and above. It requires a switch fabric running Cumulus Linux 5.5.0 or above. This feature is in beta.

{{</notice>}}

- Must enable RoCE lossless mode on the switch
- To display queue histograms, you must enable and configure ASIC monitoring.  
- Queue histogram collection for NetQ agent should be enabled. Note that it is by default enabled – if no explicit configuration is specified. 

## Adaptive Routing Commands

Monitor adaptive routing with the following commands. See the {{<link title="show/#netq-show-adaptive-routing-config" text="command line reference">}} for additional options, definitions, and examples.

```
netq show adaptive routing config
netq show events message_type adaptive-routing
```

## View Adaptive Routing in the UI

{{<figure src="/images/netq/ar-dashboard-480.png" alt="" width="1100">}}

The following details will be shown in AR summary page: 

Switch AR enabled status 

Switch AR profile distribution 

Switch RoCE mode config and distribution 

AR profile configuration 

AR interface configuration 

Top 10 switches with queue length in last 3 minutes 

Top 10 switches exceeding deviation thresholds 

Events for traffic imbalance across ECMP group based on P95. 

Provide link to setup switch role definition 


## Related Information

- {{<kb_link latest="cl" url="Layer-3/Routing/Equal-Cost-Multipath-Load-Sharing.md" text="Cumulus Linux and ECMP">}}