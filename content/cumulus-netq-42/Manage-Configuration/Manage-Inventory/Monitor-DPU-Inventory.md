---
title: Monitor DPU Inventory
author: NVIDIA
weight: 755
toc: 4
---

{{<notice note>}}

DPU monitoring is an Early Access feature. 

{{</notice>}}

With the NetQ UI, you can monitor your inventory of DPUs across the network or individually. A user can monitor such items as operating system, ASIC, CPU model, disk, and memory information. Being able to monitor this inventory aides in upgrades, compliance and other planning tasks.

To monitor networkwide inventory, refer to {{<link title="Monitor Networkwide Inventory">}}.

## Access DPU Inventory Data

The NetQ UI provides the Inventory | DPU card for monitoring the hardware and software component inventory on switches running NetQ in your network. Access this card from the NetQ Workbench, or add it to your own workbench by clicking <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Add card) > **Inventory**  > Inventory|DPU card > **Open Cards**.

### View DPU Components

NetQ displays DPU components on the Inventory | DPU card as a donut chart. You can view data for the following DPU components:

- Disk
- Operating System
- ASIC
- Agent Version
- CPU
- Platform
- Memory

{{<figure src="/images/netq/dpu-inventory-platform-l2-42.png" width="200">}}

Hover the cursor over the chart in the default card view to view component details. Hover the cursor over the card header and increase the card size to view the distribution of components:

{{<figure src="/images/netq/dpu-inventory-l3-42.png" width="600">}}

You can hover the cursor over the card header and select the desired icon to view a detailed chart for ASIC, Platform, or Software components:

{{<figure src="/images/netq/dpu-inventory-l3-icons-42.png" width="600">}}

Change to the largest size card using the size picker to display the advanced component view and select the desired component:

{{<figure src="/images/netq/dpu-inventory-l4-42.png" width="1000">}}

## Monitor Hardware Utilization

To monitor DPU hardware resource utilization, see {{<link title="Monitor DPUs">}}.

