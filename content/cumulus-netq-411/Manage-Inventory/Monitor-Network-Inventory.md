---
title: Networkwide Inventory
author: NVIDIA
weight: 730
toc: 4
---

Use the UI or CLI to monitor your network's inventory of switches, hosts, NICs, and DPUs. The inventory includes a count for each device and information about the hardware and software components on individual switches, such as the operating system, motherboard, ASIC, microprocessor, disk, memory, fan, and power supply information.

## Networkwide Inventory Commands

Several forms of this command are available based on the inventory component you'd like to view. See the {{<link title="show/#netq-show-inventory" text="command line reference">}} for additional options, definitions, and examples.

```
netq show inventory (brief | asic | board | cpu | disk | memory | os)
```
## View Networkwide Inventory in the UI

{{<tabs "TabID 34">}}

{{<tab "NetQ UI">}}

To view the quantity of devices in your network, open the Inventory/Devices card. The medium-sized card displays the total number of devices in the network. Hover your cursor over the chart to view the number and percentage of switches, hosts, NICS, and DPUs that comprise your network.

{{<figure src="/images/netq/inventory-devices-490.png" alt="medium inventory card displaying 8 total devices" width="200">}}

Expand to the large card to view the distribution of ASIC vendors, OS versions, NetQ Agent versions, and platforms deployed across all switches in your network. You can hover over and select any of the segments in the distribution chart to highlight and filter data, including:

   - Name or value of the component type, such as the version number or status
   - Total number of switches with a particular type of component deployed compared to the total number of switches
   - Percentage of the selected type compared to all component types

   {{<figure src="/images/netq/inventory-large-490.png" width="650">}}

Expand the Inventory/Devices card to full-screen to view comprehensive inventory information for all switches, hosts, DPUs, and NICs in your network in a table where you can filter and export data by selecting the icons above the table:

{{<figure src="/images/netq/full-inventory-490.png" alt="full-screen inventory/devices card displaying a list of switches" width="1200">}}

{{</tab>}}

{{</tabs>}}

