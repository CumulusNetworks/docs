---
title: Fault Tolerance
author: NVIDIA
weight: 330
toc: 3
---


NetQ provides fault tolerance for NVLink domain management services (NMX-T and NMX-C) on GB200 and GB300 switches. When a management service becomes unavailable, NetQ automatically detects the failure and attempts recovery in the following order:

1. Failover to an alternate management IP address: NetQ switches connectivity to the next available management IP address on the same switch.
2. Service restart: If no alternate IP address restores connectivity, NetQ stops and restarts the affected service, then verifies that the service is healthy before resuming.

Fault tolerance is enabled by default for GB200 and GB300 switches. To disable the feature for VR switches, add the following to your configuration:

```
feature-flags:
  service-failover-enabled: false
```