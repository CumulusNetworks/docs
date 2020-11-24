---
title: TCA Event Messages Reference
author: NVIDIA
weight: 812
toc: 4
---
Threshold-based events are supported for ACL resources, digital optics, forwarding resources, interface errors and statistics, link flaps, resource utilization, and sensors. These messages can be viewed through third-party notification applications. For details about configuring notifications for these events, refer to {{<link title="Configure Threshold-based Event Notifications">}}.

{{< tabs "TabID2035" >}}

{{< tab "ACL Resources" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_TCAM_IN_ACL_V4_FILTER_UPPER | Number of ingress ACL filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_EG_ACL_V4_FILTER_UPPER | Number of egress ACL filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_ACL_V4_MANGLE_UPPER | Number of ingress ACL mangles for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_EG_ACL_V4_MANGLE_UPPER | Number of egress ACL mangles for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_ACL_V6_FILTER_UPPER | Number of ingress ACL filters for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_EG_ACL_V6_FILTER_UPPER | Number of egress ACL filters for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_ACL_V6_MANGLE_UPPER | Number of ingress ACL mangles for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_EG_ACL_V6_MANGLE_UPPER | Number of egress ACL mangles for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_ACL_8021x_FILTER_UPPER | Number of ingress ACL 802.1 filters on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ACL_L4_PORT_CHECKERS_UPPER | Number of ACL port range checkers on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ACL_REGIONS_UPPER | Number of ACL regions on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_ACL_MIRROR_UPPER | Number of ingress ACL mirrors on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ACL_18B_RULES_UPPER | Number of ACL 18B rules on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ACL_32B_RULES_UPPER | Number of ACL 32B rules on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ACL_54B_RULES_UPPER | Number of ACL 54B rules on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_PBR_V4_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_PBR_V6_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv6 addresses on a given switch or host is greater than maximum threshold |

{{< /tab >}}

{{< tab "Digital Optics" >}}

{{<notice info>}}
Some of the event IDs have changed. If you have TCA rules configured for digital optics for a previous release, verify that they are using the correct event IDs. You might need to remove and recreate some of the events.
{{</notice>}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_DOM_RX_POWER_ALARM_UPPER | Transceiver Input power (mW) for the digital optical module on a given switch or host interface is greater than the maximum alarm threshold |
| TCA_DOM_RX_POWER_ALARM_LOWER | Transceiver Input power (mW) for the digital optical module on a given switch or host is less than minimum alarm threshold |
| TCA_DOM_RX_POWER_WARNING_UPPER | Transceiver Input power (mW) for the digital optical module on a given switch or host is greater than specified warning threshold |
| TCA_DOM_RX_POWER_WARNING_LOWER | Transceiver Input power (mW) for the digital optical module on a given switch or host is less than minimum warning threshold |
| TCA_DOM_BIAS_CURRENT_ALARM_UPPER | Laser bias current (mA) for the digital optical module on a given switch or host is greater than maximum alarm threshold |
| TCA_DOM_BIAS__CURRENT_ALARM_LOWER | Laser bias current (mA) for the digital optical module on a given switch or host is less than minimum alarm threshold |
| TCA_DOM_BIAS_CURRENT_WARNING_UPPER | Laser bias current (mA) for the digital optical module on a given switch or host is greater than maximum warning threshold |
| TCA_DOM_BIAS__CURRENT_WARNING_LOWER | Laser bias current (mA) for the digital optical module on a given switch or host is less than minimum warning threshold |
| TCA_DOM_OUTPUT_POWER_ALARM_UPPER | Laser output power (mW) for the digital optical module on a given switch or host is greater than maximum alarm threshold |
| TCA_DOM_OUTPUT_POWER_ALARM_LOWER | Laser output power (mW) for the digital optical module on a given switch or host is less than minimum alarm threshold |
| TCA_DOM_OUTPUT_POWER_WARNING_UPPER | Laser output power (mW) for the digital optical module on a given switch or host is greater than maximum warning threshold |
| TCA_DOM_OUTPUT_POWER_WARNING_LOWER | Laser output power (mW) for the digital optical module on a given switch or host is less than minimum warning threshold |
| TCA_DOM_MODULE_TEMPERATURE_ALARM_UPPER | Digital optical module temperature (&deg;C) on a given switch or host is greater than maximum alarm threshold |
| TCA_DOM_MODULE_TEMPERATURE_ALARM_LOWER | Digital optical module temperature (&deg;C) on a given switch or host is less than minimum alarm threshold |
| TCA_DOM_MODULE_TEMPERATURE_WARNING_UPPER | Digital optical module temperature (&deg;C) on a given switch or host is greater than maximum warning threshold |
| TCA_DOM_MODULE_TEMPERATURE_WARNING_LOWER | Digital optical module temperature (&deg;C) on a given switch or host is less than minimum warning threshold |
| TCA_DOM_MODULE_VOLTAGE_ALARM_UPPER | Transceiver voltage (V) on a given switch or host is greater than maximum alarm threshold |
| TCA_DOM_MODULE_VOLTAGE_ALARM_LOWER | Transceiver voltage (V) on a given switch or host is less than minimum alarm threshold |
| TCA_DOM_MODULE_VOLTAGE_WARNING_UPPER | Transceiver voltage (V) on a given switch or host is greater than maximum warning threshold |
| TCA_DOM_MODULE_VOLTAGE_WARNING_LOWER | Transceiver voltage (V) on a given switch or host is less than minimum warning threshold |

{{< /tab >}}

{{< tab "Forwarding Resources" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_TCAM_TOTAL_ROUTE_ENTRIES_UPPER | Number of routes on a given switch or host is greater than maximum threshold |
| TCA_TCAM_TOTAL_MCAST_ROUTES_UPPER | Number of multicast routes on a given switch or host is greater than maximum threshold |
| TCA_TCAM_MAC_ENTRIES_UPPER | Number of MAC addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IPV4_ROUTE_UPPER | Number of IPv4 routes on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IPV4_HOST_UPPER | Number of IPv4 hosts on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IPV6_ROUTE_UPPER | Number of IPv6 hosts on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IPV6_HOST_UPPER | Number of IPv6 hosts on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ECMP_NEXTHOPS_UPPER | Number of equal cost multi-path (ECMP) next hop entries on a given switch or host is greater than maximum threshold |

{{< /tab >}}

{{< tab "Interface Errors" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_HW_IF_OVERSIZE_ERRORS | Number of times a frame is longer than maximum size (1518 Bytes) |
| TCA_HW_IF_UNDERSIZE_ERRORS | Number of times a frame is shorter than minimum size (64 Bytes) |
| TCA_HW_IF_ALIGNMENT_ERRORS | Number of times a frame has an uneven byte count and a CRC error |
| TCA_HW_IF_JABBER_ERRORS | Number of times a frame is longer than maximum size (1518 bytes) and has a CRC error |
| TCA_HW_IF_SYMBOL_ERRORS | Number of times undefined or invalid symbols have been detected |

{{< /tab >}}

{{< tab "Interface Statistics" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_RXBROADCAST_UPPER  |  rx_broadcast bytes per second on a given switch or host is greater than maximum threshold |
| TCA_RXBYTES_UPPER |  rx_bytes per second on a given switch or host is greater than maximum threshold |
| TCA_RXMULTICAST_UPPER |  rx_multicast per second on a given switch or host is greater than maximum threshold |
| TCA_TXBROADCAST_UPPER |  tx_broadcast bytes per second on a given switch or host is greater than maximum threshold |
| TCA_TXBYTES_UPPER     |  tx_bytes per second on a given switch or host is greater than maximum threshold |
| TCA_TXMULTICAST_UPPER |  tx_multicast bytes per second on a given switch or host is greater than maximum threshold |

{{< /tab >}}

{{< tab "Link Flaps" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_LINK | Number of link flaps is greater than the maximum threshold |

{{< /tab >}}

{{< tab "Resource Utilization" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_CPU_UTILIZATION_UPPER | CPU utilization (%) on a given switch or host is greater than maximum threshold |
| TCA_DISK_UTILIZATION_UPPER  |  Disk utilization (%) on a given switch or host is greater than maximum threshold |
| TCA_MEMORY_UTILIZATION_UPPER  |  Memory utilization (%) on a given switch or host is greater than maximum threshold |

{{< /tab >}}

{{< tab "Sensors" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_SENSOR_FAN_UPPER  |  Switch sensor reported fan speed on a given switch or host is greater than maximum threshold |
| TCA_SENSOR_POWER_UPPER|  Switch sensor reported power (Watts) on a given switch or host is greater than maximum threshold |
| TCA_SENSOR_TEMPERATURE_UPPER  |  Switch sensor reported temperature (&deg;C) on a given switch or host is greater than maximum threshold |
| TCA_SENSOR_VOLTAGE_UPPER  |  Switch sensor reported voltage (Volts) on a given switch or host is greater than maximum threshold |

{{< /tab >}}

{{< /tabs >}}
