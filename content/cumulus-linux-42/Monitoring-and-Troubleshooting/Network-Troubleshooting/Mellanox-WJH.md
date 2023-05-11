---
title: Mellanox What Just Happened (WJH)
author: NVIDIA
weight: 1130
toc: 4
---
Cumulus Linux supports the *What Just Happened* (WJH) feature for Mellanox switches to stream detailed and contextual telemetry for off-box analysis with tools, such as {{<kb_link latest="netq" text="NVIDIA NetQ">}}. This advanced streaming telemetry technology provides real time visibility into problems in the network, such as hardware packet drops due to buffer congestion, incorrect routing, ACL or layer 1 problems.

When WJH capabilities are combined with the analytics engine of NVIDIA NetQ, you have the ability to home in on any loss, anywhere in the fabric, from a single management console. You can view any current or historic drops and specific drop reasons, and also identify any flow or endpoints and pin-point exactly where communication is failing in the network.

WJH is enabled by default on a Mellanox switch; no configuration is required in Cumulus Linux.
