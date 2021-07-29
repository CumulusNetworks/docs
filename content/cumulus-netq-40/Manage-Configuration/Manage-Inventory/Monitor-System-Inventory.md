---
title: Monitor System Inventory
author: NVIDIA
weight: 750
---
In addition to network and switch inventory, the NetQ UI provides a view into the current status and configuration of the software network constructs in a tabular, networkwide view. These are helpful when you want to see all the data for <!-- vale off -->all of<!-- vale on --> a particular element in your network for troubleshooting, or you want to export a list view.

Some of these views provide data that is also available through the card workflows, but these views are not treated like cards. They only provide the current status; you cannot change the time period of the views, or graph the data within the UI.

Access these tables through the Main Menu (<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/>), under the **Network** heading.

{{<figure src="/images/netq/main-menu-admin-network-selected-310.png" width="700">}}

Tables can be manipulated using the settings above the tables, shown here and described in {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.

{{<figure src="/images/netq/main-menu-ntwk-table-settings-241.png" width="100">}}

Pagination options are shown when there are more than 25 results.

## View All NetQ Agents

The Agents view provides all available parameter data about all NetQ Agents in the system.

{{<figure src="/images/netq/main-menu-ntwk-agents-241.png" width="700">}}

| Parameter | Description |
| --- | --- |
| Hostname | Name of the switch or host |
| Timestamp | Date and time the data was captured |
| Last Reinit | Date and time that the switch or host was reinitialized |
| Last Update Time | Date and time that the switch or host was updated |
| Lastboot | Date and time that the switch or host was last booted up |
| NTP State | Status of NTP synchronization on the switch or host; yes = in synchronization, no = out of synchronization |
| Sys Uptime | Amount of time the switch or host has been continuously up and running |
| Version | NetQ version running on the switch or host |

## View All Events

The Events view provides all available parameter data about all events in the system.

{{<figure src="/images/netq/main-menu-ntwk-events-241.png" width="700">}}

| Parameter | Description |
| --- | --- |
| Hostname | Name of the switch or host that experienced the event |
| Timestamp | Date and time the event was captured |
| Message | Description of the event |
| Message Type | Network service or protocol that generated the event |
| Severity | Importance of the event. Values include critical, warning, info, and debug. |

## View All MACs

The MACs (media access control addresses) view provides all available parameter data about all MAC addresses in the system.

{{<figure src="/images/netq/main-menu-ntwk-macs-320.png" width="700">}}

| Parameter | Description |
| --- | --- |
| Hostname | Name of the switch or host where the MAC address resides |
| Timestamp | Date and time the data was captured |
| Egress Port | Port where traffic exits the switch or host |
| Is Remote | Indicates if the address is |
| Is Static | Indicates if the address is a static (*true*) or dynamic assignment (*false*) |
| MAC Address | MAC address |
| Nexthop | Next hop for traffic hitting this MAC address on this switch or host |
| Origin | Indicates if address is owned by this switch or host (*true*) or by a peer (*false*) |
| VLAN | VLAN associated with the MAC address, if any |

## View All VLANs

The VLANs (virtual local area networks) view provides all available parameter data about all VLANs in the system.

{{<figure src="/images/netq/main-menu-ntwk-vlans-310.png" width="700">}}

| Parameter | Description |
| --- | --- |
| Hostname | Name of the switch or host where the VLAN(s) reside(s) |
| Timestamp | Date and time the data was captured |
| If Name | Name of interface used by the VLAN(s) |
| Last Changed | Date and time when this information was last updated |
| Ports | Ports on the switch or host associated with the VLAN(s) |
| SVI | Switch virtual interface associated with a bridge interface |
| VLANs | VLANs associated with the switch or host |

## View IP Routes

The IP Routes view provides all available parameter data about all IP routes. The list of routes can be filtered to view only the IPv4 or IPv6 routes by selecting the relevant tab.

{{<figure src="/images/netq/main-menu-ntwk-iproutes-all-310.png" width="700">}}

| Parameter | Description |
| --- | --- |
| Hostname | Name of the switch or host where the VLAN(s) reside(s) |
| Timestamp | Date and time the data was captured |
| Is IPv6 | Indicates if the address is an IPv6 (*true*) or IPv4 (*false*) address |
| Message Type | Network service or protocol; always *Route* in this table |
| Nexthops | Possible ports/interfaces where traffic can be routed to next |
| Origin | Indicates if this switch or host is the source of this route  (*true*) or not (*false*) |
| Prefix | IPv4 or IPv6 address prefix |
| Priority | Rank of this route to be used before another, where the lower the number, less likely is to be used; value determined by routing protocol |
| Protocol | Protocol responsible for this route |
| Route Type | Type of route |
| Rt Table ID | The routing table identifier where the route resides |
| Src | Prefix of the address where the route is coming from (the previous hop) |
| VRF | Associated virtual route interface associated with this route |

## View IP Neighbors

The IP Neighbors view provides all available parameter data about all IP neighbors. The list of neighbors can be filtered to view only the IPv4 or IPv6 neighbors by selecting the relevant tab.

{{<figure src="/images/netq/main-menu-ntwk-ipnbrs-all-310.png" width="700">}}

| Parameter | Description |
| --- | --- |
| Hostname | Name of the neighboring switch or host |
| Timestamp | Date and time the data was captured |
| IF Index | Index of interface used to communicate with this neighbor |
| If Name | Name of interface used to communicate with this neighbor |
| IP Address | IPv4 or IPv6 address of the neighbor switch or host |
| Is IPv6 | Indicates if the address is an IPv6 (*true*) or IPv4 (*false*) address |
| Is Remote | Indicates if the address is |
| MAC Address | MAC address of the neighbor switch or host |
| Message Type | Network service or protocol; always *Neighbor* in this table |
| VRF | Associated virtual route interface associated with this neighbor |

## View IP Addresses

The IP Addresses view provides all available parameter data about all IP addresses. The list of addresses can be filtered to view only the IPv4 or IPv6 addresses by selecting the relevant tab.

{{<figure src="/images/netq/main-menu-ntwk-ipaddrs-all-310.png" width="700">}}

| Parameter | Description |
| --- | --- |
| Hostname | Name of the neighboring switch or host |
| Timestamp | Date and time the data was captured |
| If Name | Name of interface used to communicate with this neighbor |
| Is IPv6 | Indicates if the address is an IPv6 (*true*) or IPv4 (*false*) address |
| Mask | Host portion of the address  |
| Prefix | Network portion of the address |
| VRF | Virtual route interface associated with this address prefix and interface on this switch or host |

{{<notice note>}}

Refer to the following for information about:
<ul>
<li>What Just Happened: {{<link title="Configure and Monitor What Just Happened" text="Configure and Monitor What Just Happened">}}</li>
<li>Sensors: {{<link title="Monitor Networkwide Inventory/#view-sensor-information" text="View Sensor Information">}} or {{<link title="Monitor Switch Inventory/#view-sensor-information-for-a-switch" text="View Sensor Information for a Switch">}}</li>
<li>Digital Optics: {{<link title="Monitor Switch Inventory/#view-digital-optics-information-for-a-switch" text="View Digital Optics Information for a Switch">}}</li>
</ul>

{{</notice>}}
