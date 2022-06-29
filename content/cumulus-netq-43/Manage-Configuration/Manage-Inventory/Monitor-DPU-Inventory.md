---
title: Monitor DPU Inventory
author: NVIDIA
weight: 755
toc: 4
---

{{<notice note>}}

DPU monitoring is an Early Access feature. 

{{</notice>}}

With the NetQ UI, you can monitor your inventory of DPUs across the network or individually. A user can monitor a network’s operating system, ASIC, CPU model, disk, and memory information to help manage upgrades, compliance, and other planning tasks.


To monitor networkwide inventory, refer to {{<link title="Monitor Networkwide Inventory">}}.

## Access DPU Inventory Data

The Inventory | DPU card monitors the hardware- and software-component inventory on DPUs in your network. Access this card from the NetQ Workbench, or add it to your own workbench by clicking <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Add card) > **Inventory**  > Inventory | DPU card > **Open Cards**.

### View DPU Components

NetQ displays DPU status and components on the Inventory | DPU card as a donut chart. The number fresh and rotten DPUs will be displayed in the card. Additionally, you can view data for the following DPU components:

- Disk
- Operating system
- ASIC
- Agent version
- CPU
- Platform
- Memory

{{<figure src="/images/netq/dpu-inventory-platform-l2-42.png" width="200">}}

Hover over the chart in the default card view to view component details. To view the distribution of components, hover over the card header and increase the card's size:

{{<figure src="/images/netq/dpu-inventory-l3-42.png" width="600">}}

You can hover over the card header and select the desired icon to view a detailed chart for ASIC, platform, or software components:

{{<figure src="/images/netq/dpu-inventory-l3-icons-42.png" width="600">}}

To display the advanced view, use the size picker to expand the card to its largest size, then select the desired component:

{{<figure src="/images/netq/dpu-inventory-l4-42.png" width="1000">}}

## Monitor Hardware Utilization

To monitor DPU hardware resource utilization, see {{<link title="Monitor DPUs">}}.

## Related Information

- {{<exlink url="https://docs.nvidia.com/doca/sdk/doca-telemetry-service/index.html" text="DOCA Telemetry Service on NVIDIA BlueField DPUs">}}