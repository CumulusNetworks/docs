---
title: Monitor Network Elements
author: Cumulus Networks
weight: 97
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
In addition to network performance monitoring, the Cumulus NetQ UI provides a view into the current status and configuration of the network elements in a tabular, network-wide view. These are helpful when you want to see all data for all of a particular element in your network for troubleshooting, or you want to export a list view.

Some of these views provide data that is also available through the card workflows, but these views are not treated like cards. They only provide the current status; you cannot change the time period of the views, or graph the data within the UI.

Access these tables through the Main Menu (<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg", height="18", width="18"/>), under the **Network** heading.

{{<figure src="/images/netq/main-menu-ntwk-choices-highlighted-240.png" width="400">}}

The tables can be manipulated as described in [Data Grid settings](../NetQ-User-Interface-Overview/Access-Data-with-Cards/#data-grid-settings) and by using the filter function at the top of the table. Expand and collapse the filter by clicking the down and up arrow in the title bar.

{{<figure src="/images/netq/main-menu-ntwk-table-filter-240.png" width="500">}}

You can filter the list of items by selecting a field,  entering a meaningful value, and then clicking **Apply**. Click **Clear** to remove the filter.

## View All NetQ Agents

The Agents view provides all available parameter data about all NetQ Agents in the system. You can filter by hostname and version.

{{<figure src="/images/netq/main-menu-ntwk-agents-240.png" width="700">}}

## View All Events

The Events view provides all available parameter data about all events in the system. You can filter by hostname and message type.

{{<figure src="/images/netq/main-menu-ntwk-events-240.png" width="700">}}

## View All MACs

The MACs (media access control addresses) view provides all available parameter data about all MAC addresses in the system. You can filter by hostname, egress port, MAC address, and VLAN.

{{<figure src="/images/netq/main-menu-ntwk-macs-240.png" width="700">}}

## View All VLANs

The VLANs (virtual local area networks) view provides all available parameter data about all VLANs in the system. You can filter by hostname, ifname, ports, SVI, and VLANs.

{{<figure src="/images/netq/main-menu-ntwk-vlans-240.png" width="700">}}

## View All IP Routes

The IP Routes view provides all available parameter data about all IP routes, all IPv4 routes, and all IPv6 routes in the system. You can filter by hostname, message type, nexthops, prefix, priority, protocol, route type, rt table id, src, and VRF.

{{<figure src="/images/netq/main-menu-ntwk-iproutes-all-240.png" width="700">}}

## View All IP Neighbors

The IP Neighbors view provides all available parameter data about all IP neighbors, all IPv4 neighbors, and all IPv6 neighbors in the system. You can filter by hostname, ifindex, ifname, IP address, MAC address, message type, and VRF.

{{<figure src="/images/netq/main-menu-ntwk-ipnbrs-all-240.png" width="700">}}

## View All IP Addresses

The IP Addresses view provides all available parameter data about all IP addresses, all IPv4 addresses, and all IPv6 addresses in the system. You can filter by hostname, ifname, mask, prefix, and VRF.

{{<figure src="/images/netq/main-menu-ntwk-ipaddrs-all-240.png" width="700">}}

## View What Just Happened

The *What Just Happened* (WJH) feature, available on Mellanox switches, streams detailed and contextual telemetry data for analysis. This provides real-time visibility into problems in the network, such as hardware packet drops due to buffer congestion, incorrect routing, and ACL or layer 1 problems.

{{%notice tip%}}
If your switches are sourced from a vendor other than Mellanox, this view is blank as no data is collected.
{{%/notice%}}

When WJH capabilities are combined with Cumulus NetQ, you have the ability to hone in on losses, anywhere in the fabric, from a single management console. You can:

- View any current or historic drop information, including the reason for the drop
- Identify problematic flows or endpoints, and pin-point exactly where communication is failing in the network

WJH is enabled by default on Mellanox switches and no configuration is required in Cumulus Linux 4.0.0 or NetQ 2.4.0.

### Viewing What Just Happened Metrics

The What Just Happened view displays events based on conditions detected in the data plane. The most recent 1000 events from the last 24 hours are presented for each drop category.

{{<figure src="/images/netq/main-menu-ntwk-wjh-l1-240.png" width="700">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Title</p></td>
<td><p>What Just Happened</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/></p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="even">
<td><p>L1 Drops tab</p></td>
<td><p>Displays the reason why a port is in the down state. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:</p>
<ul>
<li><p><strong>Hostname</strong>: Name of the Mellanox server</p></li>
<li><p><strong>Port Down Reason</strong>: Reason why the port is down</p>
<ul><li>Port admin down: Port has been purposely set down by user</li>
<li>Auto-negotiation failure: Negotiation of port speed with peer has failed</li>
<li>Logical mismatch with peer link: Logical mismatch with peer link</li>
<li>Link training failure: Link is not able to go operational up due to link training failure</li>
<li>Peer is sending remote faults: Peer node is not operating correctly</li>
<li>Bad signal integrity: Integrity of the signal on port is not sufficient for good communication</li>
<li>Cable/transceiver is not supported: The attached cable or transceiver is not supported by this port</li>
<li>Cable/transceiver is unplugged: A cable or transceiver is missing or not fully plugged into the port</li>
<li>Calibration failure: Calibration failure</li>
<li>Port state changes counter: Cumulative number of state changes</li>
<li>Symbol error counter: Cumulative number of symbol errors</li>
<li>CRC error counter: Cumulative number of CRC errors</li>
</ul></li>
<li><p><strong>Corrective Action</strong>: Provides recommend action(s) to take to resolve the port down state</p></li>
<li><p><strong>First Timestamp</strong>: Date and time this port was marked as down for the first time</p></li>
<li><p><strong>Ingress Port</strong>: Port accepting incoming traffic</p></li>
<li><p><strong>CRC Error Count</strong>: Number of CRC errors generated by this port</p></li>
<li><p><strong>Symbol Error Count</strong>: Number of Symbol errors generated by this port</p></li>
<li><p><strong>State Change Count</strong>: Number of state changes that have  occurred on this port</p></li>
<li><p><strong>OPID</strong>: Operation identifier; used for internal purposes</p></li>
<li><p><strong>Is Port Up</strong>: Indicates whether the port is in an Up (true) or Down (false) state</p></li>
</ul></td>
<tr class="even">
<td><p>L2 Drops tab</p></td>
<td><p>Displays the reason for a link to be down. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:</p>
<ul>
<li><p><strong>Hostname</strong>: Name of the Mellanox server</p></li>
<li><p><strong>Source Port</strong>: Port ID where the link originates</p></li>
<li><p><strong>Source IP</strong>: Port IP address where the link originates</p></li>
<li><p><strong>Source MAC</strong>: Port MAC address where the link originates</p></li><li><p><strong>Destination Port</strong>: Port ID where the link terminates</p></li>
<li><p><strong>Destination IP</strong>: Port IP address where the link terminates</p></li>
<li><p><strong>Destination MAC</strong>: Port MAC address where the link terminates</p></li>
<li><p><strong>Reason</strong>: Reason why the link is down</p>
<ul><li>MLAG port isolation: Not supported for port isolation implemented with system ACL</li>
<li>Destination MAC is reserved (DMAC=01-80-C2-00-00-0x): The address cannot be used by this link</li>
<li>VLAN tagging mismatch: VLAN tags on the source and destination do not match</li>
<li>Ingress VLAN filtering: Frames whose port is not a member of the VLAN are discarded</li>
<li>Ingress spanning tree filter: Port is in Spanning Tree blocking state</li>
<li>Unicast MAC table action discard: Currently not supported</li>
<li>Multicast egress port list is empty: No ports are defined for multicast egress</li>
<li>Port loopback filter: Port is operating in loopback mode; packets are being sent to itself (source MAC address is the same as the destination MAC address</li>
<li>Source MAC is multicast: Packets have multicast source MAC address</li>
<li>Source MAC equals destination MAC: Source MAC address is the same as the destination MAC address</li>
</ul></li>
<li><p><strong>First Timestamp</strong>: Date and time this link was marked as down for the first time</p></li>
<li><p><strong>Aggregate Count </strong>: Total number of dropped packets</p></li>
<li><p><strong>Protocol</strong>: ID of the communication protocol running on this link</p></li>
<li><p><strong>Ingress Port</strong>: Port accepting incoming traffic</p></li>
<li><p><strong>OPID</strong>: Operation identifier; used for internal purposes</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Router Drops tab</p></td>
<td><p>Displays the reason why the server is unable to route a packet. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:</p>
<ul>
<li><p><strong>Hostname</strong>: Name of the Mellanox server</p></li>
<li><p><strong>Reason</strong>: Reason why the server is unable to route a packet</p>
<ul><li>Non-routable packet: Packet has no route in routing table</li>
<li>Blackhole route: Packet received with action equal to discard</li>
<li>Unresolved next-hop: The next hop in the route is unknown</li>
<li>Blackhole ARP/neighbor: Packet received with blackhole adjacency</li>
<li>IPv6 destination in multicast scope FFx0:/16: Packet received with multicast destination address in FFx0:/16 address range</li>
<li>IPv6 destination in multicast scope FFx1:/16: Packet received with multicast destination address in FFx1:/16 address range</li>
<li>Non-IP packet: Cannot read packet header because it is not an IP packet</li>
<li>Unicast destination IP but non-unicast destination MAC: Cannot read packet with IP unicast address when destination MAC address is not unicast (FF:FF:FF:FF:FF:FF)</li>
<li>Destination IP is loopback address: Cannot read packet as destination IP address is a loopback address (dip=>127.0.0.0/8)</li>
<li>Source IP is multicast: Cannot read packet as source IP address is a multicast address (ipv4 SIP => 224.0.0.0/4)</li>
<li>Source IP is in class E: Cannot read packet as source IP address is a Class E address</li>
<li>Source IP is loopback address: Cannot read packet as source IP address is a loopback address ( ipv4 => 127.0.0.0/8 for ipv6 => ::1/128)</li>
<li>Source IP is unspecified: Cannot read packet as source IP address is unspecified (ipv4 = 0.0.0.0/32; for ipv6 = ::0)</li>
<li>Checksum or IP ver or IPv4 IHL too short: Cannot read packet due to header checksum error, IP version mismatch, or IPv4 header length is too short</li>
<li>Multicast MAC mismatch:  For IPv4, destination MAC address is not equal to {0x01-00-5E-0 (25 bits), DIP[22:0]} and DIP is multicast. For IPv6, destination MAC address is not equal to {0x3333, DIP[31:0]} and DIP is multicast.</li>
<li>Source IP equals destination IP: Packet has a source IP address equal to the destination IP address</li>
<li>IPv4 source IP is limited broadcast: Packet has broadcast source IP address</li>
<li>IPv4 destination IP is local network (destination = 0.0.0.0/8): Packet has IPv4 destination address that is a local network (destination=0.0.0.0/8)</li>
<li>IPv4 destination IP is link local: Packet has IPv4 destination address that is a local link</li>
<li>Ingress router interface is disabled: Packet destined to a different subnet cannot be routed because ingress router interface is disabled</li>
<li>Egress router interface is disabled: Packet destined to a different subnet cannot be routed because egress router interface is disabled</li>
<li>IPv4 routing table (LPM) unicast miss: No route available in routing table for packet</li>
<li>IPv6 routing table (LPM) unicast miss: No route available in routing table for packet</li>
<li>Router interface loopback: Packet has destination IP address that is local. For example, SIP = 1.1.1.1, DIP = 1.1.1.128.</li>
<li>Packet size is larger than MTU: Packet has larger MTU configured than the VLAN</li>
<li>TTL value is too small: Packet has TTL value of 1</li>
</ul></li>
</ul></td>
<tr class="even">
<td><p>Tunnel Drops tab</p></td>
<td><p>Displays the reason for a tunnel to be down. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:</p>
<ul>
<li><p><strong>Hostname</strong>: Name of the Mellanox server</p></li>
<li><p><strong>Reason</strong>: Reason why the tunnel is down</p>
<ul><li>Overlay switch – source MAC is multicast:  Overlay packet's source MAC address is multicast</li>
<li>Overlay switch – source MAC equals destination MAC: Overlay packet's source MAC address is the same as the destination MAC address</li>
<li>Decapsulation error: Decapsulation produced incorrect format of packet. For example, encapsulation of packet with many VLANs or IP options on the underlay can cause decapsulation to result in a short packet.</li>
</ul></li>
</ul></td>
<tr class="even">
<td><p>Buffer Drops tab</p></td>
<td><p>Displays the reason for the server buffer to be drop packets. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:</p>
<ul>
<li><p><strong>Hostname</strong>: Name of the Mellanox server</p></li>
<li><p><strong>Reason</strong>: Reason why the buffer dropped packet</p>
<ul><li>Tail drop: Tail drop is enabled, and buffer queue is filled to maximum capacity</li>
<li>WRED: Weighted Random Early Detection is enabled, and buffer queue is filled to maximum</li>
</ul></li>
</ul></td>
<tr class="even">
<td><p>ACL Drops tab</p></td>
<td><p>Displays the reason for an ACL to be (something?). By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:</p>
<ul>
<li><p><strong>Hostname</strong>: Name of the Mellanox server</p></li>
<li><p><strong>Reason</strong>: Reason why (ACL xxx)</p>
<ul><li>Ingress port ACL:  ACL action set to deny on the ingress port</li>
<li>Ingress router ACL: ACL action set to deny on the ingress router interface</li>
<li>Egress port ACL:  ACL action set to deny on the egress port</li>
<li>Egress router ACL: ACL action set to deny on the egress router interface</li>
</ul></li>
</ul></td>
<tr class="even">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg", height="18", width="18"/></p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>
