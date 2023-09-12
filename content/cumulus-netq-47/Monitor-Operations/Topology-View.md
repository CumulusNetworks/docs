---
title: Network Topology
author: NVIDIA
weight: 890
toc: 3
---

NetQ lets you monitor your network by viewing performance and configuration data for individual network devices and the entire fabric networkwide. This section describes monitoring tasks you can perform from a topology view in the NetQ UI.

## Access the Topology View

To open the topology view, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/41-Hierachy-Organization/hierarchy.svg" height="18" width="18"/> **Topology** in any workbench header. This opens the full-screen view of your network topology.

{{<figure src="/images/netq/full-screen-topology-updated.png" alt="view of a networkwide topology displaying connections between devices" width="900">}}

## Topology Overview

The topology view provides a visual representation of your Linux network, showing the connections and device information for all monitored nodes. The topology view uses a number of icons and elements to represent the nodes and their connections:

| Symbol | Usage |
| :----: | ----- |
| {{<img src="/images/netq/rocket-turtle-limed-spruce.svg" width="28" height="28">}} | Switch running Cumulus Linux OS |
| <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> | Switch running RedHat, Ubuntu, or CentOS |
| <img src="https://icons.cumulusnetworks.com/12-Design/08-Grids-Rulers/grid-monitor.svg" height="18" width="18"/> | Host with unknown operating system |
| {{<img src="/images/netq/cof_white-black_hex.png" width="18" height="18">}} | Host running Ubuntu |
| Lines | Physical links or connections |

## Interact with the Topology

There are a number of ways in which you can interact with the topology.

### Move the Topology Focus

You can zoom in on a topology to view fewer nodes, or zoom out to view more nodes. As with mapping applications, the node labels appear and disappear as you move in and out on the diagram for better readability. To zoom, you can use:

- The zoom controls {{<img src="/images/netq/topo-zoom-widget-230.png" width="18">}} at the bottom-right corner of the screen
- A scrolling motion on your mouse
- Your trackpad

You can also click anywhere on the topology, and drag it left, right, up, or down to view a different portion of the network diagram.

### View Data About the Network

You can hover over the various elements to view data about them. Select an element to open a side panel with additional statistics.

{{<figure src="/images/netq/topology-hover-spine-1.png" alt="overview of events, protocols, and utilization data for spine 1" width="500">}}

Hovering over a line highlights each end of the connection. Select the line to open a side panel with additional configuration data.

{{<figure src="/images/netq/topology-configuration-panel.png" alt="side panel displaying configuration data between two nodes" width="600">}}

From the side panel, you can view the following data about nodes and links:

| Node Data | Description |
| --------- | ----------- |
| ASIC | Name of the ASIC used in the switch. A value of Cumulus Networks VX indicates a virtual machine. |
| NetQ Agent Status | Operational status of the NetQ Agent on the switch (fresh or rotten). |
| NetQ Agent Version | Version ID of the NetQ Agent on the switch. |
| OS Name | Operating system running on the switch. |
| Platform | Vendor and name of the switch hardware. |
| Interface Statistics | Transmit and receive data. |
| Resource Utilization| CPU, memory, and disk utilization. |
| Events| Warning and info events. |


<p> </p>

| Link Data | Description |
| --------- | ----------- |
| Source | Switch where the connection originates |
| Source Interface | Port on the source switch used by the connection |
| Target | Switch where the connection ends |
| Target Interface | Port on the destination switch used by the connection |

Change the time period by selecting the timestamp box in the topology header. Adjust the time to view historic network configurations.

Click **Export** in the header to export your topology information as a JSON file. 
### Rearrange the Topology Layout

NetQ generates the network topology and positions the nodes automatically. In large topologies, the position of the nodes might not be suitable for easy viewing. You can move the components of the topology by dragging and dropping them with your mouse. You can save the new layout so other users can see it by selecting the **Save** icon in the header.


