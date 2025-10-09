---
title: Networkwide Inventory
author: NVIDIA
weight: 730
toc: 4
---

Use the UI or CLI to monitor your inventory of switches, hosts, and DPUs at the networkwide level. The inventory includes a count for each device and its operating system and information about the hardware and software components on individual switches, such as the motherboard, ASIC, microprocessor, disk, memory, fan, and power supply information.

To monitor the inventory of a given switch, host, or DPU, refer to {{<link title="Switch Inventory">}}, {{<link title="Host Inventory">}}, or {{<link title="DPU Inventory">}}.

## Networkwide Inventory Commands

Several forms of this command are available based on the inventory component you'd like to view. See the {{<link title="show/#netq-show-inventory" text="command line reference">}} for additional options, definitions, and examples.

```
netq show inventory (brief | asic | board | cpu | disk | memory | os)
```
## View Networkwide Inventory in the UI

{{<tabs "TabID 34">}}

{{<tab "NetQ UI">}}

To view the quantity of devices in your network, open the Inventory/Devices card. The medium-sized card displays operating system distribution across the network and the total number of devices in the network. Hover over the chart’s outer circle to view operating system distribution; hover over the chart’s inner circle to view device counts.

{{<figure src="/images/netq/inventory-devices-l2-42.png" alt="medium inventory card displaying 15 switches and 10 hosts as a chart" width="200">}}

Expand to the large card for additional distribution info. By default, the Switches tab shows the total number of switches, ASIC vendors, OS versions, NetQ Agent versions, and specific platforms deployed across all your switches. You can hover over and select any of the segments in a component distribution chart to highlight and filter data, including:

   - Name or value of the component type, such as the version number or status
   - Total number of switches with a particular type of component deployed compared to the total number of switches
   - Percentage of this type as compared to all component types

   {{<figure src="/images/netq/large-switches-inventory-devices.png" width="650">}}

Expand the Inventory/Devices card to full-screen to view information for all switches, hosts, and DPUs in your network in a table where you can filter and export data:

{{<figure src="/images/netq/inventory-devices-switches.png" alt="full-screen inventory/devices card displaying a list of switches" width="1100">}}

{{</tab>}}

{{</tabs>}}

