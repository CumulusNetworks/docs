---
title: Threshold-Crossing Events Reference
author: NVIDIA
weight: 812
toc: 4
---

This reference lists the threshold-based events that NetQ supports. You can view these messages through third-party notification applications. For details about configuring notifications for these events, refer to {{<link title="Configure and Monitor Threshold-Crossing Events">}}.

## ACL Resources

<!-- vale off -->
| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Ingress ACL IPv4 % | TCA_TCAM_IN_ACL_V4_FILTER_UPPER | Number of ingress ACL filters for IPv4 addresses on a given switch or host exceeded user-defined threshold |
| Egress ACL IPv4 % | TCA_TCAM_EG_ACL_V4_FILTER_UPPER | Number of egress ACL filters for IPv4 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL IPv4 mangle % | TCA_TCAM_IN_ACL_V4_MANGLE_UPPER | Number of ingress ACL mangles for IPv4 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL IPv4 mangle % | TCA_TCAM_EG_ACL_V4_MANGLE_UPPER | Number of egress ACL mangles for IPv4 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL IPv6 % | TCA_TCAM_IN_ACL_V6_FILTER_UPPER | Number of ingress ACL filters for IPv6 addresses on a given switch or host exceeded user-defined maximum threshold |
| Egress ACL IPv6 % | TCA_TCAM_EG_ACL_V6_FILTER_UPPER | Number of egress ACL filters for IPv6 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL IPv6 mangle % | TCA_TCAM_IN_ACL_V6_MANGLE_UPPER | Number of ingress ACL mangles for IPv6 addresses on a given switch or host exceeded user-defined maximum threshold |
| Egress ACL IPv6 mangle % | TCA_TCAM_EG_ACL_V6_MANGLE_UPPER | Number of egress ACL mangles for IPv6 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL 8021x % | TCA_TCAM_IN_ACL_8021x_FILTER_UPPER | Number of ingress ACL 802.1 filters on a given switch or host exceeded user-defined maximum threshold |
| ACL L4 port % | TCA_TCAM_ACL_L4_PORT_CHECKERS_UPPER | Number of ACL port range checkers on a given switch or host exceeded user-defined maximum threshold |
| ACL regions % | TCA_TCAM_ACL_REGIONS_UPPER | Number of ACL regions on a given switch or host exceeded user-defined maximum threshold |
| Ingress ACL mirror % | TCA_TCAM_IN_ACL_MIRROR_UPPER | Number of ingress ACL mirrors on a given switch or host exceeded user-defined maximum threshold |
| ACL 18B rules % | TCA_TCAM_ACL_18B_RULES_UPPER | Number of ACL 18B rules on a given switch or host exceeded user-defined maximum threshold |
| ACL 32B % | TCA_TCAM_ACL_32B_RULES_UPPER | Number of ACL 32B rules on a given switch or host exceeded user-defined maximum threshold |
| ACL 54B % | TCA_TCAM_ACL_54B_RULES_UPPER | Number of ACL 54B rules on a given switch or host exceeded user-defined maximum threshold |
| Ingress PBR IPv4 % | TCA_TCAM_IN_PBR_V4_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv4 addresses on a given switch or host exceeded user-defined maximum threshold |
| Ingress PBR IPv6 % | TCA_TCAM_IN_PBR_V6_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv6 addresses on a given switch or host exceeded user-defined maximum threshold |
<!-- vale on -->

## BGP

<!-- vale off -->
| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| BGP connection drop | TCA_BGP_CONN_DROP | Increase in drop count for a BGP session exceeding user-defined threshold |
| BGP packet queue length | TCA_BGP_PACKET_QUEUE_LENGTH | Packet queue length persistently non-zero for more than the threshold duration (in seconds) |

## Digital Optics


| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Laser Rx power alarm upper | TCA_DOM_RX_POWER_ALARM_UPPER | Transceiver Input power (mW) for the digital optical module on a given switch or host interface exceeded user-defined the maximum alarm threshold |
| Laser Rx power alarm lower | TCA_DOM_RX_POWER_ALARM_LOWER | Transceiver Input power (mW) for the digital optical module on a given switch or host exceeded user-defined minimum alarm threshold |
| Laser Rx power warning upper | TCA_DOM_RX_POWER_WARNING_UPPER | Transceiver Input power (mW) for the digital optical module on a given switch or host exceeded user-defined specified warning threshold |
| Laser Rx power warning lower | TCA_DOM_RX_POWER_WARNING_LOWER | Transceiver Input power (mW) for the digital optical module on a given switch or host exceeded user-defined minimum warning threshold |
| Laser bias current alarm upper | TCA_DOM_BIAS_CURRENT_ALARM_UPPER | Laser bias current (mA) for the digital optical module on a given switch or host exceeded user-defined maximum alarm threshold |
| Laser bias current alarm lower | TCA_DOM_BIAS_CURRENT_ALARM_LOWER | Laser bias current (mA) for the digital optical module on a given switch or host exceeded user-defined minimum alarm threshold |
| Laser bias current warning upper | TCA_DOM_BIAS_CURRENT_WARNING_UPPER | Laser bias current (mA) for the digital optical module on a given switch or host exceeded user-defined maximum warning threshold |
| Laser bias current warning lower | TCA_DOM_BIAS_CURRENT_WARNING_LOWER | Laser bias current (mA) for the digital optical module on a given switch or host exceeded user-defined minimum warning threshold |
| Laser output power alarm upper | TCA_DOM_OUTPUT_POWER_ALARM_UPPER | Laser output power (mW) for the digital optical module on a given switch or host exceeded user-defined maximum alarm threshold |
| Laser output power alarm lower | TCA_DOM_OUTPUT_POWER_ALARM_LOWER | Laser output power (mW) for the digital optical module on a given switch or host exceeded user-defined minimum alarm threshold |
| Laser output power alarm upper | TCA_DOM_OUTPUT_POWER_WARNING_UPPER | Laser output power (mW) for the digital optical module on a given switch or host exceeded user-defined maximum warning threshold |
| Laser output power warning lower | TCA_DOM_OUTPUT_POWER_WARNING_LOWER | Laser output power (mW) for the digital optical module on a given switch or host exceeded user-defined minimum warning threshold |
| Laser module temperature alarm upper | TCA_DOM_MODULE_TEMPERATURE_ALARM_UPPER | Digital optical module temperature (&deg;C) on a given switch or host exceeded user-defined maximum alarm threshold |
| Laser module temperature alarm lower | TCA_DOM_MODULE_TEMPERATURE_ALARM_LOWER | Digital optical module temperature (&deg;C) on a given switch or host exceeded user-defined minimum alarm threshold |
| Laser module temperature warning upper | TCA_DOM_MODULE_TEMPERATURE_WARNING_UPPER | Digital optical module temperature (&deg;C) on a given switch or host exceeded user-defined maximum warning threshold |
| Laser module temperature warning lower | TCA_DOM_MODULE_TEMPERATURE_WARNING_LOWER | Digital optical module temperature (&deg;C) on a given switch or host exceeded user-defined minimum warning threshold |
| Laser module voltage alarm upper | TCA_DOM_MODULE_VOLTAGE_ALARM_UPPER | Transceiver voltage (V) on a given switch or host exceeded user-defined maximum alarm threshold |
| Laser module voltage alarm lower | TCA_DOM_MODULE_VOLTAGE_ALARM_LOWER | Transceiver voltage (V) on a given switch or host exceeded user-defined minimum alarm threshold |
| Laser module voltage warning upper | TCA_DOM_MODULE_VOLTAGE_WARNING_UPPER | Transceiver voltage (V) on a given switch or host exceeded user-defined maximum warning threshold |
| Laser module voltage warning lower | TCA_DOM_MODULE_VOLTAGE_WARNING_LOWER | Transceiver voltage (V) on a given switch or host exceeded user-defined minimum warning threshold |

## DPU RoCE


| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Implied nak seq error | TCA_HOSTD_IMPLIED_NAK_SEQ_ERR | Count of implied sequence errors exceeded user-defined maximum threshold |
| Out of buffer | TCA_HOSTD_OUT_OF_BUFFER | Count of out-of-buffer errors exceeded user-defined maximum threshold |
| Outbound PCI stalled read | TCA_HOSTD_OUTBOUND_PCI_STALLED_RD | Percentage of outbound stalled read requests exceeded user-defined maximum threshold |
| Outbound PCI stalled write | TCA_HOSTD_OUTBOUND_PCI_STALLED_WR | Percentage of outbound stalled write requests exceeded user-defined maximum threshold |
| Packet seq err | TCA_HOSTD_PACKET_SEQ_ERR | Count of packet sequence errors exceeded user-defined maximum threshold |
| Req CQE error | TCA_HOSTD_REQ_CQE_ERROR | Count of req <!--check this-->completion queue events (CQE) errors exceeded user-defined maximum threshold |
| Req remote access errors | TCA_HOSTD_REQ_REMOTE_ACCESS_ERRORS| Count of remote access errors exceeded user-defined maximum threshold |
| Resp CQE error | TCA_HOSTD_RESP_CQE_ERROR| Count of response completion queue events (CQE) errors exceeded user-defined maximum threshold |
| Resp remote access errors | TCA_HOSTD_RESP_REMOTE_ACCESS_ERRORS | Count of response remote access errors exceeded user-defined maximum threshold |
| RNR nak retry error |	TCA_HOSTD_RNR_NAK_RETRY_ERR	| Count of RNR retry errors exceeded user-defined maximum threshold |
| Rx CRC errors phy | TCA_HOSTD_RX_CRC_ERRORS_PHY | Count of Rx CRC errors exceeded user-defined maximum threshold |
| Rx discards phy |	TCA_HOSTD_RX_DISCARDS_PHY | Rate of Rx discards exceeded user-defined maximum threshold |
| Rx PCI signal integrity |	TCA_HOSTD_RX_PCI_SIGNAL_INTEGRITY | Count of Rx PCIe signal integrity errors exceeded user-defined maximum threshold |
| Rx pcs symbol err phy	| TCA_HOSTD_RX_PCS_SYMBOL_ERR_PHY | Count of Rx symbol errors exceeded user-defined maximum threshold |
| Rx prio0 buf discard | TCA_HOSTD_RX_PRIO0_BUF_DISCARD | Rate of p0 buffer discards exceeded user-defined maximum threshold |
| Rx prio0 cong discard | TCA_HOSTD_RX_PRIO0_CONG_DISCARD |	Rate of p0 congestion discards exceeded user-defined maximum threshold |
| Rx prio1 buf discard | TCA_HOSTD_RX_PRIO1_BUF_DISCARD | Rate of p1 buffer discards exceeded user-defined maximum threshold |
| Rx prio1 cong discard | TCA_HOSTD_RX_PRIO1_CONG_DISCARD |	Rate of p1 congestion discards exceeded user-defined maximum threshold |
| Rx prio2 buf discard | TCA_HOSTD_RX_PRIO2_BUF_DISCARD | Rate of p2 buffer discards exceeded user-defined maximum threshold |
| Rx prio2 cong discard | TCA_HOSTD_RX_PRIO2_CONG_DISCARD | Rate of p2 congestion discards exceeded user-defined maximum threshold |
| Rx prio3 buf discard | TCA_HOSTD_RX_PRIO3_BUF_DISCARD | Rate of p3 buffer discards exceeded user-defined maximum threshold |
| Rx prio3 cong discard | TCA_HOSTD_RX_PRIO3_CONG_DISCARD | Rate of p3 congestion discards exceeded user-defined maximum threshold |
| Rx prio4 buf discard | TCA_HOSTD_RX_PRIO4_BUF_DISCARD | Rate of p4 buffer discards exceeded user-defined maximum threshold |
| Rx prio4 cong discard | TCA_HOSTD_RX_PRIO4_CONG_DISCARD | Rate of p4 congestion discards exceeded user-defined maximum threshold |
| Rx prio5 buf discard | TCA_HOSTD_RX_PRIO5_BUF_DISCARD | Rate of p5 buffer discards exceeded user-defined maximum threshold |
| Rx prio5 cong discard | TCA_HOSTD_RX_PRIO5_CONG_DISCARD | Rate of p5 congestion discards exceeded user-defined maximum threshold |
| Rx prio6 buf discard | TCA_HOSTD_RX_PRIO6_BUF_DISCARD | Rate of p6 buffer discards exceeded user-defined maximum threshold |
| Rx prio6 cong discard | TCA_HOSTD_RX_PRIO6_CONG_DISCARD | Rate of p6 congestion discards exceeded user-defined maximum threshold |
| Rx prio7 buf discard | TCA_HOSTD_RX_PRIO7_BUF_DISCARD | Rate of p7 buffer discards exceeded user-defined maximum threshold |
| Rx prio7 cong discard | TCA_HOSTD_RX_PRIO7_CONG_DISCARD | Rate of p7 congestion discards exceeded user-defined maximum threshold |
| Rx symbol err phy | TCA_HOSTD_RX_SYMBOL_ERR_PHY| Count of Rx symbol errors (physical coding errors) exceeded user-defined maximum threshold |
| Tx discards phy | TCA_HOSTD_TX_DISCARDS_PHY | Rate of Tx discards exceeded user-defined maximum threshold |
| Tx errors phy | TCA_HOSTD_TX_ERRORS_PHY | Count of Tx errors exceeded user-defined maximum threshold |
| Tx pause storm error events |	TCA_HOSTD_TX_PAUSE_STORM_ERROR_EVENTS |	Count of pause error events exceeded user-defined maximum threshold |
| Tx pause storm warning events | TCA_HOSTD_TX_PAUSE_STORM_WARNING_EVENTS | Count of pause warning events exceeded user-defined maximum threshold |
| Tx PCI signal integrity |	TCA_HOSTD_TX_PCI_SIGNAL_INTEGRITY |	Count of Tx PCIe signal integrity errors exceeded user-defined maximum threshold |

## ECMP

<!-- vale off -->
| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| ECMP imbalance | TCA_ECMP_IMBALANCE | ECMP path utilization imbalance greater than the threshold |


## Forwarding Resources

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Total route entries % | TCA_TCAM_TOTAL_ROUTE_ENTRIES_UPPER | Number of routes on a given switch or host exceeded user-defined maximum threshold |
| Mcast routes % | TCA_TCAM_TOTAL_MCAST_ROUTES_UPPER | Number of multicast routes on a given switch or host exceeded user-defined maximum threshold |
| MAC entries % | TCA_TCAM_MAC_ENTRIES_UPPER | Number of MAC addresses on a given switch or host exceeded user-defined maximum threshold |
| IPv4 routes % | TCA_TCAM_IPV4_ROUTE_UPPER | Number of IPv4 routes on a given switch or host exceeded user-defined maximum threshold |
| IPv4 hosts % | TCA_TCAM_IPV4_HOST_UPPER | Number of IPv4 hosts on a given switch or host exceeded user-defined maximum threshold |
| Exceeding IPv6 routes % | TCA_TCAM_IPV6_ROUTE_UPPER | Number of IPv6 routes on a given switch or host exceeded user-defined maximum threshold |
| IPv6 hosts % | TCA_TCAM_IPV6_HOST_UPPER | Number of IPv6 hosts on a given switch or host exceeded user-defined maximum threshold |
| ECMP next hop % | TCA_TCAM_ECMP_NEXTHOPS_UPPER | Number of equal cost multi-path (ECMP) next hop entries on a given switch or host exceeded user-defined maximum threshold |

## Interface Errors

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Oversize errors | TCA_HW_IF_OVERSIZE_ERRORS | Number of times a frame longer than maximum size (1518 Bytes) exceeded user-defined threshold |
| Undersize errors | TCA_HW_IF_UNDERSIZE_ERRORS | Number of times a frame shorter than minimum size (64 Bytes) exceeded user-defined threshold |
| Alignment errors | TCA_HW_IF_ALIGNMENT_ERRORS | Number of times a frame with an uneven byte count and a CRC error exceeded user-defined threshold |
| Jabber errors | TCA_HW_IF_JABBER_ERRORS | Number of times a frame longer than maximum size (1518 bytes) and with a CRC error exceeded user-defined threshold |
| Symbol errors | TCA_HW_IF_SYMBOL_ERRORS | Number of times that detected undefined or invalid symbols exceeded user-defined threshold |

## Interface Statistics

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Broadcast received bytes | TCA_RXBROADCAST_UPPER  |  Number of broadcast receive bytes per second exceeded user-defined maximum threshold on a switch interface |
| Received bytes | TCA_RXBYTES_UPPER |  Number of receive bytes exceeded user-defined maximum threshold on a switch interface |
| Multicast received bytes | TCA_RXMULTICAST_UPPER |  rx_multicast per second on a given switch or host exceeded user-defined maximum threshold |
| Broadcast transmitted bytes | TCA_TXBROADCAST_UPPER |  Number of broadcast transmit bytes per second exceeded user-defined maximum threshold on a switch interface |
| Transmitted bytes | TCA_TXBYTES_UPPER | Number of transmit bytes exceeded user-defined maximum threshold on a switch interface |
| Multicast transmitted bytes | TCA_TXMULTICAST_UPPER | Number of multicast transmit bytes per second exceeded user-defined maximum threshold on a switch interface |

## Link Flaps

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Link flap errors | TCA_LINK_FLAP_UPPER | Number of link flaps exceeded user-defined maximum threshold |

## Resource Utilization

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Service memory utilization | TCA_SERVICE_MEMORY_UTILIZATION_UPPER | Percentage of service memory utilization exceeded user-defined maximum threshold on a switch |
| Disk utilization | TCA_DISK_UTILIZATION_UPPER  |  Percentage of disk utilization exceeded user-defined maximum threshold on a switch or host |
| CPU utilization | TCA_CPU_UTILIZATION_UPPER | Percentage of CPU utilization exceeded user-defined maximum threshold on a switch or host |
| Service CPU utilization | TCA_SERVICE_CPU_UTILIZATION_UPPER | Percentage of service CPU utilization exceeded user-defined maximum threshold on a switch |
| Memory utilization | TCA_MEMORY_UTILIZATION_UPPER  |  Percentage of memory utilization exceeded user-defined maximum threshold on a switch or host |

## RoCE 

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Rx CNP buffer usage | TCA_RX_CNP_BUFFER_USAGE_CELLS | Percentage of Rx General+CNP buffer usage exceeded user-defined maximum threshold on a switch interface |
| Rx CNP no buffer discard | TCA_RX_CNP_NO_BUFFER_DISCARD | Rate of Rx General+CNP no buffer discard exceeded user-defined maximum threshold on a switch interface |
| Rx CNP PG usage | TCA_RX_CNP_PG_USAGE_CELLS | Percentage of Rx General+CNP PG usage exceeded user-defined maximum threshold on a switch interface |
| Rx RoCE buffer usage | TCA_RX_ROCE_BUFFER_USAGE_CELLS | Percentage of Rx RoCE buffer usage exceeded user-defined maximum threshold on a switch interface |
| Rx RoCE no buffer discard | TCA_RX_ROCE_NO_BUFFER_DISCARD | Rate of Rx RoCE no buffer discard exceeded user-defined maximum threshold on a switch interface |
| Rx RoCE PG usage | TCA_RX_ROCE_PG_USAGE_CELLS | Percentage of Rx RoCE PG usage exceeded user-defined maximum threshold on a switch interface |
| Rx RoCE PFC pause duration | TCA_RX_ROCE_PFC_PAUSE_DURATION | Number of Rx RoCE PFC pause duration exceeded user-defined maximum threshold on a switch interface |
| Rx RoCE PFC pause packets | TCA_RX_ROCE_PFC_PAUSE_PACKETS | Rate of Rx RoCE PFC pause packets exceeded user-defined maximum threshold on a switch interface |
| Tx CNP buffer usage | TCA_TX_CNP_BUFFER_USAGE_CELLS | Percentage of Tx General+CNP buffer usage exceeded user-defined maximum threshold on a switch interface |
| Tx CNP TC usage | TCA_TX_CNP_TC_USAGE_CELLS | Percentage of Tx CNP TC usage exceeded user-defined maximum threshold on a switch interface |
| Tx CNP unicast no buffer discard | TCA_TX_CNP_UNICAST_NO_BUFFER_DISCARD | Rate of Tx CNP unicast no buffer discard exceeded user-defined maximum threshold on a switch interface |
| Tx ECN marked packets | TCA_TX_ECN_MARKED_PACKETS | Rate of Tx Port ECN marked packets exceeded user-defined maximum threshold on a switch interface |
| Tx RoCE buffer usage | TCA_TX_ROCE_BUFFER_USAGE_CELLS | Percentage of Tx RoCE buffer usage exceeded user-defined maximum threshold on a switch interface | 
| Tx RoCE PFC pause duration | TCA_TX_ROCE_PFC_PAUSE_DURATION | Number of Tx RoCE PFC pause duration exceeded user-defined maximum threshold on a switch interface |
| Tx RoCE PFC pause packets | TCA_TX_ROCE_PFC_PAUSE_PACKETS | Rate of Tx RoCE PFC pause packets exceeded user-defined maximum threshold on a switch interface |
| Tx RoCE TC usage | TCA_TX_ROCE_TC_USAGE_CELLS | Percentage of Tx RoCE TC usage exceeded user-defined maximum threshold on a switch interface |
| Tx RoCE unicast no buffer discard | TCA_TX_ROCE_UNICAST_NO_BUFFER_DISCARD | Rate of Tx RoCE unicast no buffer discard exceeded user-defined maximum threshold on a switch interface |

## Sensors

| NetQ UI Name | NetQ CLI Event ID | Description |
| --- | --- | --- |
| Fan speed | TCA_SENSOR_FAN_UPPER  |  Fan speed exceeded user-defined maximum threshold on a switch |
| Power supply watts | TCA_SENSOR_POWER_UPPER| Power supply output exceeded user-defined maximum threshold on a switch |
| Power supply volts | TCA_SENSOR_VOLTAGE_UPPER  | Power supply voltage exceeded user-defined maximum threshold on a switch |
| Switch temperature | TCA_SENSOR_TEMPERATURE_UPPER  | Temperature (&deg; C) exceeded user-defined maximum threshold on a switch |

## What Just Happened

<!-- vale off -->
| NetQ UI Name | NetQ CLI Event ID | Drop Type | Reason/Port Down Reason | Description |
| --- | --- | :---: | --- | --- |
| ACL drop aggregate upper | TCA_WJH_ACL_DROP_AGG_UPPER | ACL | Egress port ACL | ACL action set to deny on the physical egress port or bond |
| ACL drop aggregate upper | TCA_WJH_ACL_DROP_AGG_UPPER | ACL | Egress router ACL | ACL action set to deny on the egress switch virtual interfaces (SVIs) |
| ACL drop aggregate upper | TCA_WJH_ACL_DROP_AGG_UPPER | ACL | Ingress port ACL | ACL action set to deny on the physical ingress port or bond |
| ACL drop aggregate upper | TCA_WJH_ACL_DROP_AGG_UPPER | ACL | Ingress router ACL | ACL action set to deny on the ingress switch virtual interfaces (SVIs) |
| Buffer drop aggregate upper | TCA_WJH_BUFFER_DROP_AGG_UPPER | Buffer | Packet Latency Threshold Crossed | Time a packet spent within the switch exceeded or dropped below the specified high or low threshold |
| Buffer drop aggregate upper | TCA_WJH_BUFFER_DROP_AGG_UPPER | Buffer | Port TC Congestion Threshold Crossed | Percentage of the occupancy buffer exceeded or dropped below the specified high or low threshold |
| Buffer drop aggregate upper | TCA_WJH_BUFFER_DROP_AGG_UPPER | Buffer | Tail drop | Tail drop is enabled, and buffer queue is filled to maximum capacity |
| Buffer drop aggregate upper | TCA_WJH_BUFFER_DROP_AGG_UPPER | Buffer | WRED | Weighted Random Early Detection is enabled, and buffer queue is filled to maximum capacity or the RED engine dropped the packet as of random congestion prevention |
| CRC error upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Auto-negotiation failure | Negotiation of port speed with peer has failed |
| CRC error upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Bad signal integrity | Integrity of the signal on port is not sufficient for good communication |
| CRC error upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Cable/transceiver is not supported | The attached cable or transceiver is not supported by this port |
| CRC error upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Cable/transceiver is unplugged | A cable or transceiver is missing or not fully inserted into the port |
| CRC error upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Calibration failure | Calibration failure |
| CRC error upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Link training failure | Link is not able to go operational up due to link training failure |
| CRC error upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Peer is sending remote faults | Peer node is not operating correctly |
| CRC error upper | TCA_WJH_CRC_ERROR_UPPER | L1 | Port admin down | Port has been purposely set down by user |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | L2 | Destination MAC is reserved (DMAC=01-80-C2-00-00-0x) | The address cannot be used by this link |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | L2 | Ingress spanning tree filter | Port is in Spanning Tree blocking state |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | L2 | Ingress VLAN filtering | Frames whose port is not a member of the VLAN are discarded |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | L2 | MLAG port isolation | Not supported for port isolation implemented with system ACL |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | L2 | Multicast egress port list is empty | No ports are defined for multicast egress |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | L2 | Port loopback filter | Port is operating in loopback mode; packets are being sent to itself (source MAC address is the same as the destination MAC address |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | L2 | Unicast MAC table action discard | Currently not supported |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | L2 | VLAN tagging mismatch | VLAN tags on the source and destination do not match |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Blackhole ARP/neighbor | Packet received with blackhole adjacency |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Blackhole route | Packet received with action equal to discard |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Checksum or IPver or IPv4 IHL too short | Cannot read packet due to header checksum error, IP version mismatch, or IPv4 header length is too short |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Destination IP is loopback address | Cannot read packet as destination IP address is a loopback address (dip=>127.0.0.0/8) |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Egress router interface is disabled | Packet destined to a different subnet cannot be routed because egress router interface is disabled |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Ingress router interface is disabled | Packet destined to a different subnet cannot be routed because ingress router interface is disabled |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv4 destination IP is link local | Packet has IPv4 destination address that is a local link (destination in 169.254.0.0/16) |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv4 destination IP is local network (destination=0.0.0.0/8) | Packet has IPv4 destination address that is a local network (destination=0.0.0.0/8) |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv4 routing table (LPM) unicast miss | No route available in routing table for packet |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv4 source IP is limited broadcast | Packet has broadcast source IP address |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv6 destination in multicast scope FFx0:/16 | Packet received with multicast destination address in FFx0:/16 address range |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv6 destination in multicast scope FFx1:/16 | Packet received with multicast destination address in FFx1:/16 address range |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | IPv6 routing table (LPM) unicast miss | No route available in routing table for packet |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Multicast MAC mismatch | For IPv4, destination MAC address is not equal to {0x01-00-5E-0 (25 bits), DIP\[22:0\]} and DIP is multicast. For IPv6, destination MAC address is not equal to {0x3333, DIP\[31:0\]} and DIP is multicast |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Non IP packet | Cannot read packet header because it is not an IP packet |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Non-routable packet | Packet has no route in routing table |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Packet size is larger than router interface MTU | Packet has larger MTU configured than the VLAN |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Router interface loopback | Packet has destination IP address that is local. For example, SIP = 1.1.1.1, DIP = 1.1.1.128. |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Source IP equals destination IP | Packet has a source IP address equal to the destination IP address |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Source IP is in class E | Cannot read packet as source IP address is a Class E address |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Source IP is loopback address | Cannot read packet as source IP address is a loopback address ( ipv4 => 127.0.0.0/8 for ipv6 => ::1/128) |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Source IP is multicast | Cannot read packet as source IP address is a multicast address (ipv4 SIP => 224.0.0.0/4) |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Source IP is unspecified | Cannot read packet as source IP address is unspecified (ipv4 = 0.0.0.0/32; for ipv6 = ::0) |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | TTL value is too small | Packet has TTL value of 1 |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Unicast destination IP but multicast destination MAC | Cannot read packet with IP unicast address when destination MAC address is not unicast (FF:FF:FF:FF:FF:FF) |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Router | Unresolved neighbor/next-hop  | The next hop in the route is unknown |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Tunnel | Decapsulation error | Decapsulation produced incorrect format of packet. For example, encapsulation of packet with many VLANs or IP options on the underlay can cause de-capsulation to result in a short packet. |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Tunnel | Overlay switch - Source MAC equals destination MAC | Overlay packet's source MAC address is the same as the destination MAC address |
| Drop aggregate upper | TCA_WJH_DROP_AGG_UPPER | Tunnel | Overlay switch - Source MAC is multicast | Overlay packet's source MAC address is multicast |
| Symbol error upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Auto-negotiation failure | Negotiation of port speed with peer has failed |
| Symbol error upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Bad signal integrity |Integrity of the signal on port is not sufficient for good communication |
| Symbol error upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Cable/transceiver is not supported | The attached cable or transceiver is not supported by this port |
| Symbol error upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Cable/transceiver is unplugged | A cable or transceiver is missing or not fully inserted into the port |
| Symbol error upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Calibration failure | Calibration failure |
| Symbol error upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Link training failure | Link is not able to go operational up due to link training failure |
| Symbol error upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Peer is sending remote faults | Peer node is not operating correctly |
| Symbol error upper | TCA_WJH_SYMBOL_ERROR_UPPER | L1 | Port admin down | Port has been purposely set down by user |
<!-- vale on -->
