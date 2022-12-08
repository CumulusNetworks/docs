---
title: DPU Inventory
author: NVIDIA
weight: 760
toc: 4
---

{{<notice note>}}

DPU monitoring is an early access feature. 

{{</notice>}}

In the UI, you can view your DPU inventory across the network or individually, including a DPU's operating system, ASIC, CPU model, disk, platform, and memory information. This information can help with upgrades, compliance, and other planning tasks.

## Access and View DPU Inventory Data

The Inventory/DPU card displays the hardware- and software-component inventory on DPUs running NetQ in your network.

{{<figure src="/images/netq/dpu-inventory-platform-l2-42.png" alt="DPU inventory card with chart" width="200">}}

Hover over the chart in the default card view to view component details. To view the distribution of components, hover over the card header and increase the card's size. Select the corresponding icon to view a detailed chart for ASIC, platform, or software components:

{{<figure src="/images/netq/dpu-inventory-l3-42.png" alt="medium DPU inventory card displaying component distribution" width="600">}}

To display detailed information as a table, expand the card to its largest size:

{{<figure src="/images/netq/dpu-inventory-l4-42.png" alt="fully expanded DPU inventory card displaying a table with data" width="1000">}}

## Related Information

To monitor DPU hardware resource utilization, see {{<link title="Monitor DPUs">}}.

To read more about NVIDIA BlueField DPUs and the DOCA Telemetry Service, refer to the {{<exlink url="https://docs.nvidia.com/doca/sdk/doca-telemetry-service/index.html" text="DOCA SDK Documentation">}}.