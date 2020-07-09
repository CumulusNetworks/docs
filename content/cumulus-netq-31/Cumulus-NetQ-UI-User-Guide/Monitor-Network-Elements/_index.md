---
title: Monitor Network Elements
author: Cumulus Networks
weight: 450
---
In addition to network performance monitoring, the Cumulus NetQ UI provides a view into the current status and configuration of the network elements in a tabular, network-wide view. These are helpful when you want to see all data for all of a particular element in your network for troubleshooting, or you want to export a list view.

Some of these views provide data that is also available through the card workflows, but these views are not treated like cards. They only provide the current status; you cannot change the time period of the views, or graph the data within the UI.

Access these tables through the Main Menu (<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/>), under the **Network** heading.

{{<figure src="/images/netq/main-menu-admin-network-selected-310.png" width="700">}}

{{<notice tip>}}
If you do not have administrative rights, the Admin menu options are not available to you.
{{</notice>}}

Tables can be manipulated using the settings above the tables, shown here and described in {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.

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

{{<figure src="/images/netq/main-menu-ntwk-macs-241.png" width="700">}}

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

## View What Just Happened

The *What Just Happened* (WJH) feature, available on Mellanox switches, streams detailed and contextual telemetry data for analysis. This provides real-time visibility into problems in the network, such as hardware packet drops due to buffer congestion, incorrect routing, and ACL or layer 1 problems. You must have Cumulus Linux 4.0.0 or later and NetQ 2.4.0 or later to take advantage of this feature.

{{<notice tip>}}
If your switches are sourced from a vendor other than Mellanox, this view is blank as no data is collected.
{{</notice>}}

When WJH capabilities are combined with Cumulus NetQ, you have the ability to hone in on losses, anywhere in the fabric, from a single management console. You can:

- View any current or historic drop information, including the reason for the drop
- Identify problematic flows or endpoints, and pin-point exactly where communication is failing in the network

{{%notice info%}}
By default, Cumulus Linux 4.0.0 provides the NetQ 2.3.1 Agent and CLI. If you installed Cumulus Linux 4.0.0 on your Mellanox switch, you need to upgrade the NetQ Agent and optionally the CLI to release 2.4.0 or later (preferably the latest release).

```
cumulus@<hostname>:~$ sudo apt-get update
cumulus@<hostname>:~$ sudo apt-get install -y netq-agent
cumulus@<hostname>:~$ netq config restart agent
cumulus@<hostname>:~$ sudo apt-get install -y netq-apps
cumulus@<hostname>:~$ netq config restart cli
```

{{%/notice%}}

### Configure the WJH Feature

WJH is enabled by default on Mellanox switches and no configuration is required in Cumulus Linux 4.0.0; however, you must enable the NetQ Agent to collect the data in NetQ 2.4.0 or later.

To enable WJH in NetQ:

1. Configure the NetQ Agent on the Mellanox switch.

    ```
    cumulus@switch:~$ netq config add agent wjh
    ```

2. Restart the NetQ Agent to start collecting the WJH data.

    ```
    cumulus@switch:~$ netq config restart agent
    ```

When you are finished viewing the WJH metrics, you might want to disable the NetQ Agent to reduce network traffic. Use `netq config del agent wjh` followed by `netq config restart agent` to disable the WJH feature on the given switch.

{{%notice note%}}
Using *wjh_dump.py* on a Mellanox platform that is running Cumulus Linux 4.0 and the NetQ 2.4.0 agent causes the NetQ WJH client to stop receiving packet drop call backs. To prevent this issue, run *wjh_dump.py* on a different system than the one where the NetQ Agent has WJH enabled, or disable *wjh_dump.py* and restart the NetQ Agent (run `netq config restart agent`).
{{%/notice%}}

### View What Just Happened Metrics

The What Just Happened view displays events based on conditions detected in the data plane. The most recent 1000 events from the last 24 hours are presented for each drop category.

{{<figure src="/images/netq/main-menu-ntwk-wjh-l1-310.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Tab</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="even">
<td>L1 Drops</td>
<td>Displays the reason why a port is in the down state. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:
<ul>
<li><strong>Hostname</strong>: Name of the Mellanox server</li>
<li><strong>Port Down Reason</strong>: Reason why the port is down
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
<li><strong>Corrective Action</strong>: Provides recommend action(s) to take to resolve the port down state</li>
<li><strong>First Timestamp</strong>: Date and time this port was marked as down for the first time</li>
<li><strong>Ingress Port</strong>: Port accepting incoming traffic</li>
<li><strong>CRC Error Count</strong>: Number of CRC errors generated by this port</li>
<li><strong>Symbol Error Count</strong>: Number of Symbol errors generated by this port</li>
<li><strong>State Change Count</strong>: Number of state changes that have  occurred on this port</li>
<li><strong>OPID</strong>: Operation identifier; used for internal purposes</li>
<li><strong>Is Port Up</strong>: Indicates whether the port is in an Up (true) or Down (false) state</li>
</ul></td>
<tr class="even">
<td>L2 Drops</td>
<td>Displays the reason for a link to be down. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:
<ul>
<li><strong>Hostname</strong>: Name of the Mellanox server</li>
<li><strong>Source Port</strong>: Port ID where the link originates</li>
<li><strong>Source IP</strong>: Port IP address where the link originates</li>
<li><strong>Source MAC</strong>: Port MAC address where the link originates</li>
<li><strong>Destination Port</strong>: Port ID where the link terminates</li>
<li><strong>Destination IP</strong>: Port IP address where the link terminates</li>
<li><strong>Destination MAC</strong>: Port MAC address where the link terminates</li>
<li><strong>Reason</strong>: Reason why the link is down
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
<li><strong>First Timestamp</strong>: Date and time this link was marked as down for the first time</li>
<li><strong>Aggregate Count </strong>: Total number of dropped packets</li>
<li><strong>Protocol</strong>: ID of the communication protocol running on this link</li>
<li><strong>Ingress Port</strong>: Port accepting incoming traffic</li>
<li><strong>OPID</strong>: Operation identifier; used for internal purposes</li>
</ul></td>
</tr>
<tr class="even">
<td>Router Drops</td>
<td>Displays the reason why the server is unable to route a packet. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:
<ul>
<li><strong>Hostname</strong>: Name of the Mellanox server</li>
<li><strong>Reason</strong>: Reason why the server is unable to route a packet
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
<td>Tunnel Drops</td>
<td>Displays the reason for a tunnel to be down. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:
<ul>
<li><strong>Hostname</strong>: Name of the Mellanox server</li>
<li><strong>Reason</strong>: Reason why the tunnel is down
<ul><li>Overlay switch - source MAC is multicast:  Overlay packet's source MAC address is multicast</li>
<li>Overlay switch - source MAC equals destination MAC: Overlay packet's source MAC address is the same as the destination MAC address</li>
<li>Decapsulation error: Decapsulation produced incorrect format of packet. For example, encapsulation of packet with many VLANs or IP options on the underlay can cause decapsulation to result in a short packet.</li>
</ul></li>
</ul></td>
<tr class="even">
<td>Buffer Drops</td>
<td>Displays the reason for the server buffer to be drop packets. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:
<ul>
<li><strong>Hostname</strong>: Name of the Mellanox server</li>
<li><strong>Reason</strong>: Reason why the buffer dropped packet
<ul><li>Tail drop: Tail drop is enabled, and buffer queue is filled to maximum capacity</li>
<li>WRED: Weighted Random Early Detection is enabled, and buffer queue is filled to maximum capacity or the RED engine dropped the packet as of random congestion prevention.</li>
</ul></li>
</ul></td>
<tr class="even">
<td>ACL Drops</td>
<td>Displays the reason for an ACL to drop packets. By default, the listing is sorted by <strong>Last Timestamp</strong>. The tab provides the following additional data about each drop event:
<ul>
<li><strong>Hostname</strong>: Name of the Mellanox server</li>
<li><strong>Reason</strong>: Reason why ACL dropped packets
<ul><li>Ingress port ACL:  ACL action set to deny on the ingress port</li>
<li>Ingress router ACL: ACL action set to deny on the ingress router interface</li>
<li>Egress port ACL:  ACL action set to deny on the egress port</li>
<li>Egress router ACL: ACL action set to deny on the egress router interface</li>
</ul></li>
</ul></td>
</tbody>
</table>

## View Sensors

The Sensors view provides all available parameter data provided by the power supply units (PSUs), fans, and temperature sensors in the system. Select the relevant tab to view the data.

{{<figure src="/images/netq/main-menu-ntwk-sensors-psu-310.png" width="700">}}

| PSU Parameter | Description |
| --- | --- |
| Hostname | Name of the switch or host where the power supply is installed |
| Timestamp | Date and time the data was captured |
| Message Type | Type of sensor message; always *PSU* in this table |
| PIn(W) | Input power (Watts) for the PSU on the switch or host |
| POut(W) | Output power (Watts) for the PSU on the switch or host |
| Sensor Name | User-defined name for the PSU |
| Previous State | State of the PSU when data was captured in previous window |
| State | State of the PSU when data was last captured |
| VIn(V) | Input voltage (Volts) for the PSU on the switch or host |
| VOut(V) | Output voltage (Volts) for the PSU on the switch or host |

| Fan Parameter | Description |
| --- | --- |
| Hostname | Name of the switch or host where the fan is installed |
| Timestamp | Date and time the data was captured |
| Message Type | Type of sensor message; always *Fan* in this table |
| Description | User specified description of the fan |
| Speed (RPM) | Revolution rate of the fan (revolutions per minute) |
| Max | Maximum speed (RPM) |
| Min | Minimum speed (RPM) |
| Message | Message |
| Sensor Name | User-defined name for the fan |
| Previous State | State of the fan when data was captured in previous window |
| State | State of the fan when data was last captured |

| Temperature Parameter | Description |
| --- | --- |
| Hostname | Name of the switch or host where the temperature sensor is installed |
| Timestamp | Date and time the data was captured |
| Message Type | Type of sensor message; always *Temp* in this table |
| Critical | Current critical maximum temperature (&deg;C) threshold setting|
| Description | User specified description of the temperature sensor |
| Lower Critical | Current critical minimum temperature (&deg;C) threshold setting |
| Max | Maximum temperature threshold setting |
| Min | Minimum temperature threshold setting |
| Message | Message |
| Sensor Name | User-defined name for the temperature sensor |
| Previous State | State of the fan when data was captured in previous window |
| State | State of the fan when data was last captured |
| Temperature(Celsius) | Current temperature (&deg;C) measured by sensor |

## View Digital Optics

The Digital Optics view provides all available parameter data provided by any digital optics modules in the system. View Laser power and bias current for a given interface and channel on a switch, and temperature and voltage for a given module. Select the relevant tab to view the data.

{{<figure src="/images/netq/main-menu-ntwk-dom-laserrx-power-310.png" width="700">}}

| Laser Parameter | Description |
| --- | --- |
| Hostname | Name of the switch or host where the digital optics module resides |
| Timestamp | Date and time the data was captured |
| If Name | Name of interface where the digital optics module is installed |
| Units | Measurement unit for the power (mW) or current (mA) |
| Channel 1&ndash;8 | Value of the power or current on each channel where the digital optics module is transmitting |

| Module Parameter | Description |
| --- | --- |
| Hostname | Name of the switch or host where the digital optics module resides |
| Timestamp | Date and time the data was captured |
| If Name | Name of interface where the digital optics module is installed |
| Degree C | Current module temperature, measured in degrees Celsius |
| Degree F | Current module temperature, measured in degrees Fahrenheit |
| Units | Measurement unit for module voltage; Volts |
| Value | Current module voltage |
