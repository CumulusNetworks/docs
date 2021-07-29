---
title: Monitor Using Topology View
author: NVIDIA
weight: 1040
toc: 3
---
The core capabilities of NetQ enable you to monitor your network by viewing performance and configuration data about your individual network devices and the entire fabric networkwide. The topics contained in this section describe monitoring tasks that can be performed from a topology view rather than through the NetQ UI card workflows or the NetQ CLI.

## Access the Topology View

To open the topology view, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/41-Hierachy-Organization/hierarchy.svg" height="18" width="18"/> in any workbench header.

{{<figure src="/images/netq/topo-access-from-wb-hdr-231.png" width="700">}}

This opens the full screen view of your network topology.

{{<figure src="/images/netq/topo-main-page-ref-topo-240.png" width="700">}}

This document uses the Cumulus Networks {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Solutions/Cumulus-Networks-Services-Demos#reference-topology" text="reference topology">}} for all examples.

To close the view, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

## Topology Overview

The topology view provides a visual representation of your Linux network, showing the connections and device information for all monitored nodes, for an alternate monitoring and troubleshooting perspective. The topology view uses a number of icons and elements to represent the nodes and their connections as follows:

| Symbol | Usage |
| :----: | ----- |
| {{<img src="/images/netq/rocket-turtle-limed-spruce.svg" width="28" height="28">}} | Switch running Cumulus Linux OS |
| <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> | Switch running RedHat, Ubuntu, or CentOS |
| <img src="https://icons.cumulusnetworks.com/12-Design/08-Grids-Rulers/grid-monitor.svg" height="18" width="18"/> | Host with unknown operating system |
| {{<img src="/images/netq/cof_white-black_hex.png" width="18" height="18">}} | Host running Ubuntu |
| Red <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell-ring.svg" height="18" width="18"/> | Alarm (critical) event is present on the node|
| Yellow <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/> | Info event is present |
| Lines | Physical links or connections |

## Interact with the Topology

There are a number of ways in which you can interact with the topology.

### Move the Topology Focus

You can move the focus on the topology closer to view a smaller number of nodes, or further out to view a larger number of nodes. As with mapping applications, the node labels appear and disappear as you move in and out on the diagram for better readability. To zoom, you can use:

- The zoom controls, {{<img src="/images/netq/topo-zoom-widget-230.png" width="18">}}, in the bottom right corner of the screen; the '+' zooms you in closer, the '-' moves you further out, and the 'o' resets to the default size.
- A scrolling motion on your mouse.
- Your trackpad.

You can also click anywhere on the topology, and drag it left, right, up, or down to view a different portion of the network diagram. This is especially helpful with larger topologies.

### View Data About the Network

You can hover over the various elements to view data about them.  Hovering over a node highlights its connections to other nodes, temporarily de-emphasizing all other connections.

{{<figure src="/images/netq/topo-hover-node-231.png" width="500">}}

Hovering over a line highlights the connection and displays the interface ports used on each end of the connection. All other connections are temporarily de-emphasized.

{{<figure src="/images/netq/topo-hover-link-230.png" width="300">}}

You can also click on the nodes and links to open the Configuration Panel with additional data about them.

{{<figure src="/images/netq/topo-node-detail-231.png" width="700">}}
{{<figure src="/images/netq/topo-link-detail-230.png" width="500">}}

From the Configuration Panel, you can view the following data about nodes and links:

| Node Data | Description |
| --------- | ----------- |
| ASIC | Name of the ASIC used in the switch. A value of Cumulus Networks VX indicates a virtual machine. |
| NetQ Agent Status | Operational status of the NetQ Agent on the switch; Fresh, Rotten. |
| NetQ Agent Version | Version ID of the NetQ Agent on the switch. |
| OS Name | Operating system running on the switch. |
| Platform | Vendor and name of the switch hardware. |
| Open Card/s | Opens the Event|Alarms and/or the Events|Info cards when there are events present. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell-ring.svg" height="18" width="18"/> | Number of alarm events present on the switch. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/> | Number of info events present on the switch. |

<p> </p>

| Link Data | Description |
| --------- | ----------- |
| Source | Switch where the connection originates |
| Source Interface | Port on the source switch used by the connection |
| Target | Switch where the connection ends |
| Target Interface | Port on the destination switch used by the connection |

After reviewing the provided information, click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-left-2.svg" height="18" width="18"/> to close the panel, or to view data for another node or link without closing the panel, simply click on that element. The panel is hidden by default.

When no devices or links are selected, you can view the unique count of items in the network by clicking on the <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-right-2.svg" height="18" width="18"/> on the upper left to open the count summary. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-left-2.svg" height="18" width="18"/> to close the panel.

{{<figure src="/images/netq/topo-open-item-count-summary-230.png" width="400">}}

You can change the time period for the data as well. This enables you to view the state of the network in the past and compare it with the current state. Click in the timestamp box in the topology header to select an alternate time period.

{{<figure src="/images/netq/topo-time-picker-230.png" width="150">}}
    
### Hide Events on Topology Diagram

You can hide the event symbols on the topology diagram. Simple move the Events toggle in the header to the left. Move the toggle to the right to show them again.

{{<figure src="/images/netq/topo-hide-show-events-toggle-240.png" width="200">}}

### Export Your NetQ Topology Data

The topology view  provides the option to export your topology information as a JSON file. Click **Export** in the header.

{{<figure src="/images/netq/topo-export-button-240.png" width="700">}}

The JSON file will be similar to this example:

```
{"inventory":{"unique_counts":{"asic":3,"netq_agent_version":3,"os":4,"platform":3}},"name":"topology","tiers":{"0":"Tier 0","1":"Tier 1","2":"Tier 2","3":"Tier 3"},"links":[{"id":35,"interfaces":[{"interface":"swp1","node":"leaf04"},{"interface":"eth2","node":"server03"}]},{"id":10,"interfaces":[{"interface":"swp51","node":"exit02"},{"interface":"swp29","node":"spine01"}]},{"id":32,"interfaces":[{"interface":"swp2","node":"leaf03"},{"interface":"eth1","node":"server04"}]},{"id":13,"interfaces":[{"interface":"swp51","node":"leaf02"},{"interface":"swp2","node":"spine01"}]},{"id":26,"interfaces":[{"interface":"swp44","node":"exit01"},{"interface":"swp1","node":"internet"}]},{"id":30,"interfaces":[{"interface":"swp31","node":"spine01"},{"interface":"swp31","node":"spine02"}]},{"id":23,"interfaces":[{"interface":"swp1","node":"leaf01"},{"interface":"eth1","node":"server01"}]},{"id":42,"interfaces":[{"interface":"swp51","node":"exit01"},{"interface":"swp30","node":"spine01"}]},{"id":17,"interfaces":[{"interface":"swp52","node":"exit02"},{"interface":"swp29","node":"spine02"}]},{"id":24,"interfaces":[{"interface":"swp50","node":"leaf03"},{"interface":"swp50","node":"leaf04"}]},{"id":9,"interfaces":[{"interface":"eth0","node":"server04"},{"interface":"swp5","node":"oob-mgmt-switch"}]},{"id":28,"interfaces":[{"interface":"swp50","node":"leaf01"},{"interface":"swp50","node":"leaf02"}]},{"id":40,"interfaces":[{"interface":"swp51","node":"leaf04"},{"interface":"swp4","node":"spine01"}]},{"id":12,"interfaces":[{"interface":"swp32","node":"spine01"},{"interface":"swp32","node":"spine02"}]},{"id":29,"interfaces":[{"interface":"eth0","node":"leaf01"},{"interface":"swp6","node":"oob-mgmt-switch"}]},{"id":25,"interfaces":[{"interface":"swp51","node":"leaf03"},{"interface":"swp3","node":"spine01"}]},{"id":22,"interfaces":[{"interface":"swp1","node":"leaf03"},{"interface":"eth1","node":"server03"}]},
...
{"inventory":{"asic":"Cumulus Networks VX","netq_agent_status":"Fresh","netq_agent_version":"2.2.1-cl3u19~1564507571.4cb6474","os":"CL 3.7.6","platform":"Cumulus Networks VX"},"name":"leaf04","tier":1,"interfaces":[{"name":"swp50","connected_to":{"interface":"swp50","link":24,"node":"leaf03"}},{"name":"swp51","connected_to":{"interface":"swp4","link":40,"node":"spine01"}},{"name":"swp2","connected_to":{"interface":"eth2","link":5,"node":"server04"}},{"name":"swp1","connected_to":{"interface":"eth2","link":35,"node":"server03"}},{"name":"swp49","connected_to":{"interface":"swp49","link":2,"node":"leaf03"}},{"name":"swp52","connected_to":{"interface":"swp4","link":11,"node":"spine02"}}],"protocol":{"bgp":false,"clag":false,"evpn":false,"lldp":true,"vni":[]},"events":{"count_alarm":0,"count_info":0}}],"events":{"count_alarm":0,"count_info":0}}
```

### Rearrange the Topology Layout

The network topology is generated automatically by NetQ and the nodes are positioned automatically. In large topologies, the position of the nodes may not be suitable for easy viewing. You can move the components of the topology around on screen to suit your needs. You can save the new layout so other users can see it.

1. Consider the following topology:

   {{<figure src="/images/netq/topo-move-before.png" width="700">}}

1. Click {{<img src="/images/netq/topo-move-icon.png" width="25">}} the **Move** icon.

1. In the example below, we switch the positions of the two border switches (border01 and border02):

   {{<figure src="/images/netq/topo-move-after.png" width="700">}}

1. Click {{<img src="/images/netq/topo-save-icon.png" width="25">}} the **Save** icon.


