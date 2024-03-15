---
title: Adaptive Routing
author: NVIDIA
weight: 790
toc: 3
---

Adaptive routing is a load balancing feature that improves network utilization for eligible IP packets by selecting forwarding paths dynamically based on the state of the switch, such as queue occupancy and port utilization. You can use the adaptive routing dashboard to view switches with adaptive routing capabilities, events related to adaptive routing, RoCE settings, and egress queue lengths in the form of histograms.

{{<notice note>}}

Adaptive routing monitoring is supported on Spectrum-4 switches. It requires a switch fabric running Cumulus Linux 5.5.0 and later.

{{</notice>}}

## Requirements

To display adaptive routing data, you must have adaptive routing configured on the switch; it can be either enabled or disabled. Switches without an adaptive routing configuration will not appear in the UI or CLI. Additionally, {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/" text="RoCE lossless mode">}} must be enabled to display adaptive routing data. Switches with RoCE lossy mode enabled will appear in the UI and CLI, but will not display adaptive routing data.

## Adaptive Routing Commands

Monitor adaptive routing with the {{<link title="show/#netq-show-adaptive-routing-config" text="netq show adaptive-routing config">}} commands. The output of these commands display adaptive routing information either globally on the switch or at the interface level.

```
netq show adaptive-routing config global
netq show adaptive-routing config interface
```

## Access the Adaptive Routing Dashboard

1. Select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**.

2. Under the Network section, select **Adaptive routing**.

{{<figure src="/images/netq/ar-dashboard-480.png" alt="adaptive routing dashboard displaying two devices with AR enabled" width="1100">}}

The adaptive routing dashboard displays:

- Devices with adaptive routing configured (enabled or disabled) and their RoCE modes (lossy or lossless).
- A list of interfaces on the switch and their configurations. In the Interfaces column, select **View details** to view interfaces with adaptive routing configured:

{{<figure src="/images/netq/int-details-490.png" alt="list of interfaces adaptive routing configured" width="600">}}

- A summary of adaptive routing events, including ECMP traffic imbalances.
- A list of up to 10 switches, which can be sorted by highest P95 value, highest standard deviation, or ports with the widest deviation from the P95 value (aggregated over the past 3 minutes). From this panel, you can select **View more** in the View histogram column to display {{<link title="Switches/#view-queue-lengths-in-histograms" text="queue lengths in the form of histograms">}} for any listed switch.



## Related Information

- {{<kb_link latest="cl" url="Layer-3/Routing/Equal-Cost-Multipath-Load-Sharing.md" text="Cumulus Linux and ECMP">}}