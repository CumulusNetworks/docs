---
title: TCA Event Messages Reference
author: NVIDIA
weight: 812
toc: 4
---
This reference lists the threshold-based events that NetQ supports for ACL resources, digital optics, forwarding resources, interface errors and statistics, link flaps, resource utilization, and sensors. These messages can be viewed through third-party notification applications. For details about configuring notifications for these events, refer to {{<link title="Configure Threshold-Based Event Notifications">}}.

## ACL Resources

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
| Symbol Errors | TCA_HW_IF_SYMBOL_ERRORS | Number of times undefined or invalid symbols have been detected exceeded user-defined threshold |

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

## Sensors

| NetQ UI Name | NetQ CLI Event ID | Description | Example Message |
| --- | --- | --- | --- |
| Fan Speed | TCA_SENSOR_FAN_UPPER  |  Fan speed exceeded user-defined maximum threshold on a switch | Sensor for spine03 exceeded threshold fan speed 700 for sensor fan2 |
| Power Supply Watts | TCA_SENSOR_POWER_UPPER| Power supply output exceeded user-defined maximum threshold on a switch | Sensor for leaf14 exceeded threshold power 120 watts for sensor psu1 |
| Power Supply Volts | TCA_SENSOR_VOLTAGE_UPPER  | Power supply voltage exceeded user-defined maximum threshold on a switch | Sensor for leaf14 exceeded threshold voltage 12 volts for sensor psu2 |
| Switch Temperature | TCA_SENSOR_TEMPERATURE_UPPER  | Temperature (&deg; C) exceeded user-defined maximum threshold on a switch | Sensor for leaf14 exceeded threshold temperature 90 for sensor temp1 |
