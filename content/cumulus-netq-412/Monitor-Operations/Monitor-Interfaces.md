---
title: Interfaces
author: NVIDIA
weight: 840
toc: 3
---

## View Link Interfaces

To view a table of interfaces along with types, states, and basic details, select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then enter **Interfaces** in the search field.

## Compare Link Interfaces

{{%notice note%}}
Link health view is a beta feature. It is not available in large-scale environments.
{{%/notice%}}

To troubleshoot link issues, expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then select **Link health view**. From this dashboard you can compare links according to different parameters, such as link utilization, link flaps, transmit and receive counters, drops and errors, and other counter data. NetQ displays the links in the table ordered from highest to lowest egress queue length.

To compare links, select up to 20 links from the dashboard, then click **Compare selected** above the table. The comparison charts update to reflect the data from the links you selected. Toggle the **Show top 5** switch on or off to view the top five and bottom five devices and their respective links according to the parameters you selected. In each of the charts, the x-axis represents time in hours, according to a 24-hour clock and the y-axis represents a count of the parameter you selected. The yellow line displays the average values for the selected links.

You can click each of the comparison charts to open a tabular view of the data that is displayed in the chart.

{{<figure src="/images/netq/link-health-comp-412.png" alt="" width="1100">}}

{{%notice tip%}}
You can bookmark the link health view in your browser. When you navigate back to the bookmarked page or share the link, your settings will be preserved.
{{%/notice%}}
## Interface Commands

NetQ uses {{<kb_link latest="cl" url="Layer-2/Link-Layer-Discovery-Protocol.md" text="LLDP">}} (Link Layer Discovery Protocol) to collect port information. NetQ can also identify peer ports connected to DACs (Direct Attached Cables) and AOCs (Active Optical Cables) without using LLDP, even if the link is not UP. To monitor OSI Layer 1 physical components on network devices, use the {{<link title="show/#netq-show-interfaces" text="netq show interfaces physical">}} command.

View interface (link) state, type, count, aliases, and additional information with the {{<link title="show/#netq-show-interfaces" text="netq show interfaces">}} and {{<link title="show/#netq-show-events" text="netq show events">}} commands.

The {{<link title="check/#netq check interfaces" text="netq check interfaces">}} command verifies interface communication status for all nodes (leafs, spines, and hosts) or an interface between specific nodes in your network fabric. This command only checks the physical interfaces; it does not check bridges, bonds, or other software constructs.

```
netq check interfaces
```
You can view link and interface statistics with the following commands:

- View statistics about a given node and interface, including frame errors, ACL drops, and buffer drops with {{<link title="show/#netq-show-ethtool-stats" text="netq show ethtool-stats">}}
- View interface statistics and utilization with the {{<link title="show/#netq-show-interface-stats" text="netq show interface-stats">}} or {{<link title="show/#netq-show-interface-utilization" text="netq show interface-utilization">}} commands.
- View incoming and outgoing access control lists (ACLs) configured on all switches and host with {{<link title="show/#netq-show-cl-resource" text="netq show cl-resource acl">}}
- View forwarding resources on all devices with {{<link title="show/#netq-show-cl-resource" text="netq show cl-resource forwarding">}}
- View SDD utilization with {{<link title="show/#netq-show-cl-ssd-util" text="netq show cl-ssd-util">}}
- View how many compute resources&mdash;CPU, disk, and memory&mdash;the switches on your network consume with {{<link title="show/#netq-show-resource-util" text="netq show resource-util">}}

## Check for MTU Inconsistencies

The maximum transmission unit (MTU) determines the largest size packet or frame that can be transmitted across a given communication link. When the MTU is not configured to the same value on both ends of the link, communication problems can occur. Use the {{<link title="check/#netq-check-mtu" text="netq check mtu">}} command to verify that the MTU is correctly specified for each link.



