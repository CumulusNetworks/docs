---
title: ECMP
author: NVIDIA
weight: 815
toc: 3
---

Equal-cost multi-path (ECMP) is a routing strategy whereby packets are forwarded along multiple paths of equal cost. Load sharing occurs automatically for IPv4 and IPv6 routes with multiple installed next hops. The hardware or the routing protocol configuration determines the maximum number of routes for which load sharing occurs.

{{<notice note>}}

ECMP monitoring is supported on NVIDIA Spectrum switches running Cumulus Linux.

{{</notice>}}

## ECMP Commands

- {{<link title="show/#netq-show-ecmp" text="netq show ecmp">}}
- {{<link title="show/#netq-show-ecmp-hash-config" text="netq show ecmp-hash-config">}}

## View ECMP Resource Utilization in the UI

You can view resource utilization for ECMP next hops in the full-screen switch card. Search for the device’s hostname in the global search field or from the header select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card&nbsp;<span aria-label="and then">></span> Device card**. Select a switch from the list. When the card opens on the dashboard, expand it to the largest size.

Select **Forwarding resources** from the side menu. The ECMP next hops column displays the maximum number of hops seen in the forwarding table, the number used, and the percentage of this usage compared to the maximum number.

{{<figure src="/images/netq/ecmp-hops-413.png" alt="" width="1100" height="430">}}

## Adaptive Routing

Adaptive routing is a load balancing feature that improves network utilization for eligible IP packets by selecting forwarding paths dynamically based on the state of the switch, such as queue occupancy and port utilization. You can use the adaptive routing dashboard to view switches with adaptive routing capabilities, events related to adaptive routing, RoCE settings, and egress queue lengths in the form of histograms.

### Requirements

- Adaptive routing monitoring is supported on Spectrum-4 switches. It requires a switch fabric running Cumulus Linux 5.5.0 or later.
- To display adaptive routing data, you must {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Routing/Equal-Cost-Multipath-Load-Sharing/#adaptive-routing" text="configure adaptive routing">}} on the switch; it can be either enabled or disabled. Switches without an adaptive routing configuration will not appear in the UI or CLI. 
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/" text="RoCE lossless mode">}} must be enabled to display adaptive routing data. Switches with RoCE *lossy* mode enabled will appear in the UI and CLI, but will not display adaptive routing data.
- To view a switch's {{<link title="Switches#view-queue-lengths-as-histograms" text="histogram data">}} and adaptive routing imbalance events, you must enable {{<kb_link latest="cl" url="Monitoring-and-Troubleshooting/ASIC-Monitoring.md" text="ASIC monitoring">}} on the switch. If you stop the `asic-monitor` service, NetQ will report values of 0 for all histogram metrics (P95, standard deviation, mean, and maximum queue lengths).

### Adaptive Routing Commands

- {{<link title="show/#netq-show-adaptive-routing-config" text="netq show adaptive-routing config">}}

### Access the Adaptive Routing Dashboard

From the header or {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu, select **Spectrum-X**, then **Adaptive routing**. The adaptive routing dashboard displays:

- Devices with adaptive routing configured (enabled or disabled) and their RoCE modes (lossy or lossless).
- A list of interfaces on the switch and their configurations. 

{{<figure src="/images/netq/ar-isr1-413.png" alt="adaptive routing dashboard displaying 10 devices with AR enabled" width="1200">}}

In the Interfaces column, select **View details** to view interfaces with adaptive routing configured:

{{<figure src="/images/netq/int-details-490.png" alt="list of interfaces adaptive routing configured" width="600">}}

The Events tab displays a summary of adaptive routing events, including ECMP traffic imbalances. The table displays up to 10 switches, which can be sorted by highest P95 value, highest standard deviation, or ports with the widest deviation from the P95 value (aggregated over the past five minutes). From this panel, you can select **View more** in the View histogram column to display {{<link title="Switches/#view-queue-lengths-in-histograms" text="queue lengths in the form of histograms">}} for any listed switch.

{{<figure src="/images/netq/ecmp-imbalance-490.png" alt="dashboard displaying ECMP imbalances" width="1000">}}

## Related Information

- {{<kb_link latest="cl" url="Layer-3/Routing/Equal-Cost-Multipath-Load-Sharing.md" text="Cumulus Linux and ECMP">}} 