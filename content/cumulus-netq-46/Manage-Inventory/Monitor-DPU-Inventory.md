---
title: DPU Inventory
author: NVIDIA
weight: 760
toc: 4
---

Use the UI or CLI to view your data processing unit (DPU) inventory. 

For DPU performance information, refer to {{<link title="DPUs" text="DPU Monitoring">}}.

## DPU Inventory Commands

Several forms of this command are available based on the inventory component you'd like to view. See the {{<link title="show/#netq-show-inventory" text="command line reference">}} for additional options, definitions, and examples.

```
netq show inventory (brief | asic | board | cpu | disk | memory | license | os)
```

## View DPU Inventory in the UI

The Inventory/DPU card displays the hardware- and software-component inventory on DPUs running NetQ in your network, including operating system, ASIC, CPU model, disk, platform, and memory information. 

To add this card to your workbench, select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card** > **Inventory** > **Inventory/DPU card** > **Open cards**.

{{<figure src="/images/netq/dpu-inventory-updated.png" alt="DPU inventory card with chart" width="200">}}

Hover over the chart to view component details. To view the distribution of components, hover over the card header and increase the card's size. Select the corresponding icon to view a detailed chart for ASIC, platform, or software components:

{{<figure src="/images/netq/dpu-inventory-l3-42.png" alt="medium DPU inventory card displaying component distribution" width="650">}}

Expand the card to its largest size to view, filter, and export detailed information: 

{{<figure src="/images/netq/dpu-inventory-l4-42.png" alt="fully expanded DPU inventory card displaying a table with data" width="1100">}}

## Related Information

To read more about NVIDIA BlueField DPUs and the DOCA Telemetry Service, refer to the {{<exlink url="https://docs.nvidia.com/doca/sdk/doca-telemetry-service/index.html" text="DOCA SDK Documentation">}}.