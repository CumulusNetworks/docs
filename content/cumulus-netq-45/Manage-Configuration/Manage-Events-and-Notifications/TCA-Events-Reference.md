---
title: TCA Event Messages Reference
author: NVIDIA
weight: 812
toc: 4
---

This reference lists the threshold-based events that NetQ supports. You can view these messages through third-party notification applications. For details about configuring notifications for these events, refer to {{<link title="Configure Threshold-Crossing Event Notifications">}}.

## ACL Resources

<!-- vale off -->
| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Ingress ACL IPv4 % | TCA_TCAM_IN_ACL_V4_FILTER_UPPER | Number of ingress ACL filters for IPv4 addresses on a given switch or host exceeded user-defined threshold |
| Egress ACL IPv4 % | TCA_TCAM_EG_ACL_V4_FILTER_UPPER | Number of egress ACL filters for IPv4 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL IPv4 Mangle % | TCA_TCAM_IN_ACL_V4_MANGLE_UPPER | Number of ingress ACL mangles for IPv4 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL IPv4 Mangle % | TCA_TCAM_EG_ACL_V4_MANGLE_UPPER | Number of egress ACL mangles for IPv4 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL IPv6 % | TCA_TCAM_IN_ACL_V6_FILTER_UPPER | Number of ingress ACL filters for IPv6 addresses on a given switch or host exceeded user-defined maximum threshold |
| Egress ACL IPv6 % | TCA_TCAM_EG_ACL_V6_FILTER_UPPER | Number of egress ACL filters for IPv6 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL IPv6 Mangle % | TCA_TCAM_IN_ACL_V6_MANGLE_UPPER | Number of ingress ACL mangles for IPv6 addresses on a given switch or host exceeded user-defined maximum threshold |
| Egress ACL IPv6 Mangle % | TCA_TCAM_EG_ACL_V6_MANGLE_UPPER | Number of egress ACL mangles for IPv6 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL 8021x % | TCA_TCAM_IN_ACL_8021x_FILTER_UPPER | Number of ingress ACL 802.1 filters on a given switch or host exceeded user-defined maximum threshold |
| ACL L4 port % | TCA_TCAM_ACL_L4_PORT_CHECKERS_UPPER | Number of ACL port range checkers on a given switch or host exceeded user-defined maximum threshold |
| ACL Regions % | TCA_TCAM_ACL_REGIONS_UPPER | Number of ACL regions on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL Mirror % | TCA_TCAM_IN_ACL_MIRROR_UPPER | Number of ingress ACL mirrors on a given switch or host exceeded user-defined maximum threshold |
| ACL 18B Rules % | TCA_TCAM_ACL_18B_RULES_UPPER | Number of ACL 18B rules on a given switch or host exceeded user-defined maximum threshold |
| ACL 32B % | TCA_TCAM_ACL_32B_RULES_UPPER | Number of ACL 32B rules on a given switch or host exceeded user-defined maximum threshold |
| ACL 54B % | TCA_TCAM_ACL_54B_RULES_UPPER | Number of ACL 54B rules on a given switch or host exceeded user-defined maximum threshold |
| Ingress PBR IPv4 % | TCA_TCAM_IN_PBR_V4_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv4 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress PBR IPv6 % | TCA_TCAM_IN_PBR_V6_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv6 addresses on a given switch or host exceeded user-defined maximum threshold |
<!-- vale on -->

## Digital Optics

{{<notice info>}}
Some of the event IDs have changed. If you have TCA rules configured for digital optics for a NetQ 3.1.0 deployment or earlier, verify that they are using the correct event IDs. You might need to remove and recreate some of the events.
{{</notice>}}

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Laser RX Power Alarm Upper | TCA_DOM_RX_POWER_ALARM_UPPER | Transceiver Input power (mW) for the digital optical module on a given switch or host interface exceeded user-defined the maximum alarm threshold |
| Laser RX Power Alarm Lower | TCA_DOM_RX_POWER_ALARM_LOWER | Transceiver Input power (mW) for the digital optical module on a given switch or host exceeded user-defined minimum alarm threshold |
| Laser RX Power Warning Upper | TCA_DOM_RX_POWER_WARNING_UPPER | Transceiver Input power (mW) for the digital optical module on a given switch or host exceeded user-defined specified warning threshold |
| Laser RX Power Warning Lower | TCA_DOM_RX_POWER_WARNING_LOWER | Transceiver Input power (mW) for the digital optical module on a given switch or host exceeded user-defined minimum warning threshold |
| Laser Bias Current Alarm Upper | TCA_DOM_BIAS_CURRENT_ALARM_UPPER | Laser bias current (mA) for the digital optical module on a given switch or host exceeded user-defined maximum alarm threshold |
| Laser Bias Current Alarm Lower | TCA_DOM_BIAS__CURRENT_ALARM_LOWER | Laser bias current (mA) for the digital optical module on a given switch or host exceeded user-defined minimum alarm threshold |
| Laser Bias Current Warning Upper | TCA_DOM_BIAS_CURRENT_WARNING_UPPER | Laser bias current (mA) for the digital optical module on a given switch or host exceeded user-defined maximum warning threshold |
| Laser Bias Current Warning Lower | TCA_DOM_BIAS__CURRENT_WARNING_LOWER | Laser bias current (mA) for the digital optical module on a given switch or host exceeded user-defined minimum warning threshold |
| Laser Output Power Alarm Upper | TCA_DOM_OUTPUT_POWER_ALARM_UPPER | Laser output power (mW) for the digital optical module on a given switch or host exceeded user-defined maximum alarm threshold |
| Laser Output Power Alarm Lower | TCA_DOM_OUTPUT_POWER_ALARM_LOWER | Laser output power (mW) for the digital optical module on a given switch or host exceeded user-defined minimum alarm threshold |
| Laser Output Power Alarm Upper | TCA_DOM_OUTPUT_POWER_WARNING_UPPER | Laser output power (mW) for the digital optical module on a given switch or host exceeded user-defined maximum warning threshold |
| Laser Output Power Warning Lower | TCA_DOM_OUTPUT_POWER_WARNING_LOWER | Laser output power (mW) for the digital optical module on a given switch or host exceeded user-defined minimum warning threshold |
| Laser Module Temperature Alarm Upper | TCA_DOM_MODULE_TEMPERATURE_ALARM_UPPER | Digital optical module temperature (&deg;C) on a given switch or host exceeded user-defined maximum alarm threshold |
| Laser Module Temperature Alarm Lower | TCA_DOM_MODULE_TEMPERATURE_ALARM_LOWER | Digital optical module temperature (&deg;C) on a given switch or host exceeded user-defined minimum alarm threshold |
| Laser Module Temperature Warning Upper | TCA_DOM_MODULE_TEMPERATURE_WARNING_UPPER | Digital optical module temperature (&deg;C) on a given switch or host exceeded user-defined maximum warning threshold |
| Laser Module Temperature Warning Lower | TCA_DOM_MODULE_TEMPERATURE_WARNING_LOWER | Digital optical module temperature (&deg;C) on a given switch or host exceeded user-defined minimum warning threshold |
| Laser Module Voltage Alarm Upper | TCA_DOM_MODULE_VOLTAGE_ALARM_UPPER | Transceiver voltage (V) on a given switch or host exceeded user-defined maximum alarm threshold |
| Laser Module Voltage Alarm Lower | TCA_DOM_MODULE_VOLTAGE_ALARM_LOWER | Transceiver voltage (V) on a given switch or host exceeded user-defined minimum alarm threshold |
| Laser Module Voltage Warning Upper | TCA_DOM_MODULE_VOLTAGE_WARNING_UPPER | Transceiver voltage (V) on a given switch or host exceeded user-defined maximum warning threshold |
| Laser Module Voltage Warning Lower | TCA_DOM_MODULE_VOLTAGE_WARNING_LOWER | Transceiver voltage (V) on a given switch or host exceeded user-defined minimum warning threshold |

## Forwarding Resources

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Total Route Entries % | TCA_TCAM_TOTAL_ROUTE_ENTRIES_UPPER | Number of routes on a given switch or host exceeded user-defined maximum threshold |
| Mcast Routes % | TCA_TCAM_TOTAL_MCAST_ROUTES_UPPER | Number of multicast routes on a given switch or host exceeded user-defined maximum threshold |
| MAC entries % | TCA_TCAM_MAC_ENTRIES_UPPER | Number of MAC addresses on a given switch or host exceeded user-defined maximum threshold |
| IPv4 Routes % | TCA_TCAM_IPV4_ROUTE_UPPER | Number of IPv4 routes on a given switch or host exceeded user-defined maximum threshold |
| IPv4 Hosts % | TCA_TCAM_IPV4_HOST_UPPER | Number of IPv4 hosts on a given switch or host exceeded user-defined maximum threshold |
| Exceeding IPV6 Routes % | TCA_TCAM_IPV6_ROUTE_UPPER | Number of IPv6 routes on a given switch or host exceeded user-defined maximum threshold |
| IPv6 Hosts % | TCA_TCAM_IPV6_HOST_UPPER | Number of IPv6 hosts on a given switch or host exceeded user-defined maximum threshold |
| ECMP Next Hop % | TCA_TCAM_ECMP_NEXTHOPS_UPPER | Number of equal cost multi-path (ECMP) next hop entries on a given switch or host exceeded user-defined maximum threshold |

## Interface Errors

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Oversize Errors | TCA_HW_IF_OVERSIZE_ERRORS | Number of times a frame longer than maximum size (1518 Bytes) exceeded user-defined threshold |
| Undersize Errors | TCA_HW_IF_UNDERSIZE_ERRORS | Number of times a frame shorter than minimum size (64 Bytes) exceeded user-defined threshold |
| Alignment Errors | TCA_HW_IF_ALIGNMENT_ERRORS | Number of times a frame with an uneven byte count and a CRC error exceeded user-defined threshold |
| Jabber Errors | TCA_HW_IF_JABBER_ERRORS | Number of times a frame longer than maximum size (1518 bytes) and with a CRC error exceeded user-defined threshold |
| Symbol Errors | TCA_HW_IF_SYMBOL_ERRORS | Number of times that detected undefined or invalid symbols exceeded user-defined threshold |

## Interface Statistics

| NetQ UI Name | NetQ CLI Event ID | Description | Example Message |
| --- | --- | --- | --- |
| Broadcast Received Bytes | TCA_RXBROADCAST_UPPER  |  Number of broadcast receive bytes per second exceeded user-defined maximum threshold on a switch interface | RX broadcast upper threshold breached for host leaf04 ifname:swp45 value: 40200 |
| Received Bytes | TCA_RXBYTES_UPPER |  Number of receive bytes exceeded user-defined maximum threshold on a switch interface | RX bytes upper threshold breached for host spine02 ifname:swp4 value: 20000 |
| Multicast Received Bytes | TCA_RXMULTICAST_UPPER |  rx_multicast per second on a given switch or host exceeded user-defined maximum threshold |
| Broadcast Transmitted Bytes | TCA_TXBROADCAST_UPPER |  Number of broadcast transmit bytes per second exceeded user-defined maximum threshold on a switch interface | TX broadcast upper threshold breached for host leaf04 ifname:swp45 value: 40200 |
| Transmitted Bytes | TCA_TXBYTES_UPPER | Number of transmit bytes exceeded user-defined maximum threshold on a switch interface | TX bytes upper threshold breached for host spine02 ifname:swp4 value: 20000 |
| Multicast Transmitted Bytes | TCA_TXMULTICAST_UPPER | Number of multicast transmit bytes per second exceeded user-defined maximum threshold on a switch interface | TX multicast upper threshold breached for host leaf04 ifname:swp45 value: 30000 |

## Link Flaps

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Link flap errors | TCA_LINK | Number of link flaps user-defined maximum threshold |

## Resource Utilization

| NetQ UI Name | NetQ CLI Event ID | Description | Example Message |
| --- | --- | --- | --- |
| CPU Utilization | TCA_CPU_UTILIZATION_UPPER | Percentage of CPU utilization exceeded user-defined maximum threshold on a switch or host | CPU Utilization for host leaf11 exceed configured mark 85 |
| Disk Utilization | TCA_DISK_UTILIZATION_UPPER  |  Percentage of disk utilization exceeded user-defined maximum threshold on a switch or host | Disk Utilization for host leaf11 exceed configured mark 90 |
| Memory Utilization | TCA_MEMORY_UTILIZATION_UPPER  |  Percentage of memory utilization exceeded user-defined maximum threshold on a switch or host | Memory Utilization for host leaf11 exceed configured mark 95 |

## RoCE 

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Rx CNP Buffer Usage Cells | TCA_RX_CNP_BUFFER_USAGE_CELLS | Percentage of Rx General+CNP buffer usage exceeded user-defined maximum threshold on a switch interface |
| Rx CNP No Buffer Discard | TCA_RX_CNP_NO_BUFFER_DISCARD | Rate of Rx General+CNP no buffer discard exceeded user-defined maximum threshold on a switch interface |
| Rx CNP PG Usage Cells | TCA_RX_CNP_PG_USAGE_CELLS | Percentage of Rx General+CNP PG usage exceeded user-defined maximum threshold on a switch interface |
| Rx RoCE Buffer Usage Cells | TCA_RX_ROCE_BUFFER_USAGE_CELLS | Percentage of Rx RoCE buffer usage exceeded user-defined maximum threshold on a switch interface |
| Rx RoCE No Buffer Discard | TCA_RX_ROCE_NO_BUFFER_DISCARD | Rate of Rx RoCE no buffer discard exceeded user-defined maximum threshold on a switch interface |
| Rx RoCE PG Usage Cells | TCA_RX_ROCE_PG_USAGE_CELLS | Percentage of Rx RoCE PG usage exceeded user-defined maximum threshold on a switch interface |
| Rx RoCE PFC Pause Duration | TCA_RX_ROCE_PFC_PAUSE_DURATION | Number of Rx RoCE PFC pause duration exceeded user-defined maximum threshold on a switch interface |
| Rx RoCE PFC Pause Packets | TCA_RX_ROCE_PFC_PAUSE_PACKETS | Rate of Rx RoCE PFC pause packets exceeded user-defined maximum threshold on a switch interface |
| Tx CNP Buffer Usage Cells | TCA_TX_CNP_BUFFER_USAGE_CELLS | Percentage of Tx General+CNP buffer usage exceeded user-defined maximum threshold on a switch interface |
| Tx CNP TC Usage Cells | TCA_TX_CNP_TC_USAGE_CELLS | Percentage of Tx CNP TC usage exceeded user-defined maximum threshold on a switch interface |
| Tx CNP Unicast No Buffer Discard | TCA_TX_CNP_UNICAST_NO_BUFFER_DISCARD | Rate of Tx CNP unicast no buffer discard exceeded user-defined maximum threshold on a switch interface |
| Tx ECN Marked Packets | TCA_TX_ECN_MARKED_PACKETS | Rate of Tx Port ECN marked packets exceeded user-defined maximum threshold on a switch interface |
| Tx RoCE Buffer Usage Cells | TCA_TX_ROCE_BUFFER_USAGE_CELLS | Percentage of Tx RoCE buffer usage exceeded user-defined maximum threshold on a switch interface | 
| Tx RoCE PFC Pause Duration | TCA_TX_ROCE_PFC_PAUSE_DURATION | Number of Tx RoCE PFC pause duration exceeded user-defined maximum threshold on a switch interface |
| Tx RoCE PFC Pause Packets | TCA_TX_ROCE_PFC_PAUSE_PACKETS | Rate of Tx RoCE PFC pause packets exceeded user-defined maximum threshold on a switch interface |
| Tx RoCE TC Usage Cells | TCA_TX_ROCE_TC_USAGE_CELLS | Percentage of Tx RoCE TC usage exceeded user-defined maximum threshold on a switch interface |
| Tx RoCE Unicast No Buffer Discard | TCA_TX_ROCE_UNICAST_NO_BUFFER_DISCARD | Rate of Tx RoCE unicast no buffer discard exceeded user-defined maximum threshold on a switch interface |

## Sensors

| NetQ UI Name | NetQ CLI Event ID | Description | Example Message |
| --- | --- | --- | --- |
| Fan Speed | TCA_SENSOR_FAN_UPPER  |  Fan speed exceeded user-defined maximum threshold on a switch | Sensor for spine03 exceeded threshold fan speed 700 for sensor fan2 |
| Power Supply Watts | TCA_SENSOR_POWER_UPPER| Power supply output exceeded user-defined maximum threshold on a switch | Sensor for leaf14 exceeded threshold power 120 watts for sensor psu1 |
| Power Supply Volts | TCA_SENSOR_VOLTAGE_UPPER  | Power supply voltage exceeded user-defined maximum threshold on a switch | Sensor for leaf14 exceeded threshold voltage 12 volts for sensor psu2 |
| Switch Temperature | TCA_SENSOR_TEMPERATURE_UPPER  | Temperature (&deg; C) exceeded user-defined maximum threshold on a switch | Sensor for leaf14 exceeded threshold temperature 90 for sensor temp1 |

## What Just Happened

<!-- vale off -->
| NetQ UI Name | NetQ CLI Event ID | Drop Type | Reason/Port Down Reason | Description |
| --- | --- | :---: | --- | --- |
| ACL Drop Aggregate Upper | TCA_WJH_ACL_DROP_AGG_UPPER | ACL | Egress port ACL | ACL action set to deny on the physical egress port or bond |
| ACL Drop Aggregate Upper | TCA_WJH_ACL_DROP_AGG_UPPER | ACL | Egress router ACL | ACL action set to deny on the egress switch virtual interfaces (SVIs) |
| ACL Drop Aggregate Upper | TCA_WJH_ACL_DROP_AGG_UPPER | ACL | Ingress port ACL | ACL action set to deny on the physical ingress port or bond |
| ACL Drop Aggregate Upper | TCA_WJH_ACL_DROP_AGG_UPPER | ACL | Ingress router ACL | ACL action set to deny on the ingress switch virtual interfaces (SVIs) |
| Buffer Drop Aggregate Upper | TCA_WJH_BUFFER_DROP_AGG_UPPER | Buffer | Packet Latency Threshold Crossed | Time a packet spent within the switch exceeded or dropped below the specified high or low threshold |
| Buffer Drop Aggregate Upper | TCA_WJH_BUFFER_DROP_AGG_UPPER | Buffer | Port TC Congestion Threshold Crossed | Percentage of the occupancy buffer exceeded or dropped below the specified high or low threshold |
| Buffer Drop Aggregate Upper | TCA_WJH_BUFFER_DROP_AGG_UPPER | Buffer | Tail drop | Tail drop is enabled, and buffer queue is filled to maximum capacity |
| Buffer Drop Aggregate Upper | TCA_WJH_BUFFER_DROP_AGG_UPPER | Buffer | WRED | Weighted Random Early Detection is enabled, and buffer queue is filled to maximum capacity or the RED engine dropped the packet as of random congestion prevention |
| CRC Error Upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Auto-negotiation failure | Negotiation of port speed with peer has failed |
| CRC Error Upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Bad signal integrity | Integrity of the signal on port is not sufficient for good communication |
| CRC Error Upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Cable/transceiver is not supported | The attached cable or transceiver is not supported by this port |
| CRC Error Upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Cable/transceiver is unplugged | A cable or transceiver is missing or not fully inserted into the port |
| CRC Error Upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Calibration failure | Calibration failure |
| CRC Error Upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Link training failure | Link is not able to go operational up due to link training failure |
| CRC Error Upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Peer is sending remote faults | Peer node is not operating correctly |
| CRC Error Upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Port admin down | Port has been purposely set down by user |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | L2 | Destination MAC is reserved (DMAC=01-80-C2-00-00-0x) | The address cannot be used by this link |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | L2 | Ingress spanning tree filter | Port is in Spanning Tree blocking state |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | L2 | Ingress VLAN filtering | Frames whose port is not a member of the VLAN are discarded |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | L2 | MLAG port isolation | Not supported for port isolation implemented with system ACL |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | L2 | Multicast egress port list is empty | No ports are defined for multicast egress |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | L2 | Port loopback filter | Port is operating in loopback mode; packets are being sent to itself (source MAC address is the same as the destination MAC address |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | L2 | Unicast MAC table action discard | Currently not supported |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | L2 | VLAN tagging mismatch | VLAN tags on the source and destination do not match |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Blackhole ARP/neighbor | Packet received with blackhole adjacency |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Blackhole route | Packet received with action equal to discard |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Checksum or IPver or IPv4 IHL too short | Cannot read packet due to header checksum error, IP version mismatch, or IPv4 header length is too short |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Destination IP is loopback address | Cannot read packet as destination IP address is a loopback address (dip=>127.0.0.0/8) |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Egress router interface is disabled | Packet destined to a different subnet cannot be routed because egress router interface is disabled |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Ingress router interface is disabled | Packet destined to a different subnet cannot be routed because ingress router interface is disabled |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv4 destination IP is link local | Packet has IPv4 destination address that is a local link (destination in 169.254.0.0/16) |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv4 destination IP is local network (destination=0.0.0.0/8) | Packet has IPv4 destination address that is a local network (destination=0.0.0.0/8) |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv4 routing table (LPM) unicast miss | No route available in routing table for packet |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv4 source IP is limited broadcast | Packet has broadcast source IP address |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv6 destination in multicast scope FFx0:/16 | Packet received with multicast destination address in FFx0:/16 address range |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv6 destination in multicast scope FFx1:/16 | Packet received with multicast destination address in FFx1:/16 address range |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv6 routing table (LPM) unicast miss | No route available in routing table for packet |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Multicast MAC mismatch | For IPv4, destination MAC address is not equal to {0x01-00-5E-0 (25 bits), DIP\[22:0\]} and DIP is multicast. For IPv6, destination MAC address is not equal to {0x3333, DIP\[31:0\]} and DIP is multicast |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Non IP packet | Cannot read packet header because it is not an IP packet |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Non-routable packet | Packet has no route in routing table |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Packet size is larger than router interface MTU | Packet has larger MTU configured than the VLAN |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Router interface loopback | Packet has destination IP address that is local. For example, SIP = 1.1.1.1, DIP = 1.1.1.128. |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Source IP equals destination IP | Packet has a source IP address equal to the destination IP address |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Source IP is in class E | Cannot read packet as source IP address is a Class E address |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Source IP is loopback address | Cannot read packet as source IP address is a loopback address ( ipv4 => 127.0.0.0/8 for ipv6 => ::1/128) |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Source IP is multicast | Cannot read packet as source IP address is a multicast address (ipv4 SIP => 224.0.0.0/4) |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Source IP is unspecified | Cannot read packet as source IP address is unspecified (ipv4 = 0.0.0.0/32; for ipv6 = ::0) |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | TTL value is too small | Packet has TTL value of 1 |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Unicast destination IP but multicast destination MAC | Cannot read packet with IP unicast address when destination MAC address is not unicast (FF:FF:FF:FF:FF:FF) |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Router | Unresolved neighbor/next-hop  | The next hop in the route is unknown |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Tunnel | Decapsulation error | De-capsulation produced incorrect format of packet. For example, encapsulation of packet with many VLANs or IP options on the underlay can cause de-capsulation to result in a short packet. |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Tunnel | Overlay switch - Source MAC equals destination MAC | Overlay packet's source MAC address is the same as the destination MAC address |
| Drop Aggregate Upper | TCA_WJH_DROP_AGG_UPPER | Tunnel | Overlay switch - Source MAC is multicast | Overlay packet's source MAC address is multicast |
| Symbol Error Upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Auto-negotiation failure | Negotiation of port speed with peer has failed |
| Symbol Error Upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Bad signal integrity |Integrity of the signal on port is not sufficient for good communication |
| Symbol Error Upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Cable/transceiver is not supported | The attached cable or transceiver is not supported by this port |
| Symbol Error Upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Cable/transceiver is unplugged | A cable or transceiver is missing or not fully inserted into the port |
| Symbol Error Upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Calibration failure | Calibration failure |
| Symbol Error Upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Link training failure | Link is not able to go operational up due to link training failure |
| Symbol Error Upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Peer is sending remote faults | Peer node is not operating correctly |
| Symbol Error Upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Port admin down | Port has been purposely set down by user |
<!-- vale on -->
