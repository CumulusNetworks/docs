---
title: Adaptive Routing
author: NVIDIA
weight: 790
toc: 3
---

Adaptive routing is a load balancing feature that improves network utilization for eligible IP packets by selecting forwarding paths dynamically based on the state of the switch, such as queue occupancy and port utilization. You can use the adaptive routing dashboard to view switches with adaptive routing capabilities, events related to adaptive routing, RoCE settings, and egress queue lengths in the form of histograms.

{{<notice note>}}

Adaptive routing monitoring is supported on Spectrum-2 switches and above. It requires a switch fabric running Cumulus Linux 5.5.0 or above. This feature is in beta.

{{</notice>}}

## Requirements

To display adaptive routing data, you must have adaptive routing configured on the switch; it can be either enabled or disabled. Switches without an adaptive routing configuration will not appear in the UI or CLI. Additionally, {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/" text="RoCE lossless mode">}} must be enabled to display adaptive routing data. Switches with RoCE lossy mode enabled will appear in the UI and CLI, but will not display adaptive routing data.

## Adaptive Routing Commands

Monitor adaptive routing with the following commands. See the {{<link title="show/#netq-show-adaptive-routing-config" text="command line reference">}} for additional options, definitions, and examples.

```
netq show adaptive routing config global
netq show adaptive routing config interface
```

## Access the Adaptive Routing Dashboard

1. Select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**.

2. Under the Network section, select **Adaptive routing**.

The adaptive routing dashboard displays:

- devices with adaptive routing (enabled or disabled) and their RoCE modes (lossy or lossless).
- a summary of adaptive routing events, including ECMP traffic imbalances that can be investigated further by viewing their histograms.
- a list of up to 10 switches, which can be sorted by highest P95 value, highest standard deviation, or widest deviation from the P95 value (aggregated over the past 3 minutes). From this panel, you can select **View more** in the **View histogram** column to display {{<link title="Switches/#view-queue-lengths-in-histograms" text="queue lengths in the form of histograms">}} for any listed switch.

{{<figure src="/images/netq/ar-dashboard-480.png" alt="adaptive routing dashboard displaying two devices with AR enabled" width="1100">}}

## Related Information

- {{<kb_link latest="cl" url="Layer-3/Routing/Equal-Cost-Multipath-Load-Sharing.md" text="Cumulus Linux and ECMP">}}