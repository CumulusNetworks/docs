---
title: Monitor Host Inventory
author: NVIDIA
weight: 757
toc: 4
---

With the NetQ UI, you can monitor your inventory of hosts across the network or individually. A user can monitor a host's operating system, ASIC, CPU model, disk, and memory information to help manage upgrades, compliance, and other planning tasks.


To monitor networkwide inventory, refer to {{<link title="Monitor Networkwide Inventory">}}.

## Access Host Inventory Data

The Inventory | Hosts card monitors the hardware- and software-component inventory on hosts running NetQ in your network. Access this card from the NetQ Workbench, or add it to your own workbench by clicking <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Add card) > **Inventory**  > Inventory | Hosts card > **Open Cards**.

### View Host Components

NetQ displays host status and components on the Inventory | Hosts card as a donut chart. The number fresh and rotten hosts will be displayed in the card. Additionally, you can view data for the following host components:

- Disk
- Operating system
- ASIC
- CPU
- Platform
- Memory

{{<img src="/images/netq/inventory-hosts-l2-42.png" width="200">}}

Hover over the chart in the default card view to view component details. To view the distribution of components, hover over the card header and increase the card's size. You can hover over the card header and select the desired icon to view a detailed chart for ASIC, platform, or software components:

{{<figure src="/images/netq/inventory-hosts-l3-42.png" width="600">}}

To display the advanced view, use the size picker to expand the card to its largest size, then select the desired component:

{{<figure src="/images/netq/inventory-hosts-l4-42.png" width="1000">}}

## Monitor Hardware Utilization

To monitor host hardware resource utilization, see {{<link title="Monitor Linux Hosts">}}.

