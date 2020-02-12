---
title: Configure and Monitor Threshold-based Events
author: Cumulus Networks
weight: 326
aliases:
 - /display/NETQ/Monitor+Events
 - /pages/viewpage.action?pageId=12321771
pageID: 12321771
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
toc: 4
---
NetQ supports a set of events that are triggered by crossing a user-defined threshold. These events allow detection and prevention of network failures for selected interface, utilization, and sensor events.

## Supported Events

The following events are supported:

| Category | Event ID | Description |
| ----------- | ---------- | -------------- |
| Interface Statistics | TCA_RXBROADCAST_UPPER  |  rx_broadcast bytes per second on a given switch or host is greater than maximum threshold |
| Interface Statistics | TCA_RXBYTES_UPPER |  rx_bytes per second on a given switch or host is greater than maximum threshold |
| Interface Statistics | TCA_RXMULTICAST_UPPER |  rx_multicast per second on a given switch or host is greater than maximum threshold |
| Resource Utilization | TCA_CPU_UTILIZATION_UPPER | CPU utilization (%) on a given switch or host is greater than maximum threshold |
| Resource Utilization | TCA_DISK_UTILIZATION_UPPER  |  Disk utilization (%) on a given switch or host is greater than maximum threshold |
| Resource Utilization | TCA_MEMORY_UTILIZATION_UPPER  |  Memory utilization (%) on a given switch or host is greater than maximum threshold |
| Interface Statistics | TCA_TXBROADCAST_UPPER |  tx_broadcast bytes per second on a given switch or host is greater than maximum threshold |
| Interface Statistics | TCA_TXBYTES_UPPER     |  tx_bytes per second on a given switch or host is greater than maximum threshold |
| Interface Statistics | TCA_TXMULTICAST_UPPER |  tx_multicast bytes per second on a given switch or host is greater than maximum threshold |
| Sensors | TCA_SENSOR_FAN_UPPER  |  Switch sensor reported fan speed on a given switch or host is greater than maximum threshold |
| Sensors | TCA_SENSOR_POWER_UPPER|  Switch sensor reported power (Watts) on a given switch or host is greater than maximum threshold |
| Sensors | TCA_SENSOR_TEMPERATURE_UPPER  |  Switch sensor reported temperature (&deg;C) on a given switch or host is greater than maximum threshold |
| Sensors | TCA_SENSOR_VOLTAGE_UPPER  |  Switch sensor reported voltage (Volts) on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_TOTAL_ROUTE_ENTRIES_UPPER | Number of routes on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_TOTAL_MCAST_ROUTES_UPPER | Number of multicast routes on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_MAC_ENTRIES_UPPER | Number of MAC addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IPV4_ROUTE_UPPER | Number of IPv4 routes on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IPV4_HOST_UPPER | Number of IPv4 hosts on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IPV6_ROUTE_UPPER | Number of IPv6 hosts on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IPV6_HOST_UPPER | Number of IPv6 hosts on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IN_ACL_V4_FILTER_UPPER | Number of ingress ACL filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_EG_ACL_V4_FILTER_UPPER | Number of egress ACL filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IN_ACL_V4_MANGLE_UPPER | Number of ingress ACL mangles for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_EG_ACL_V4_MANGLE_UPPER | Number of egress ACL mangles for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IN_ACL_V6_FILTER_UPPER | Number of ingress ACL filters for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_EG_ACL_V6_FILTER_UPPER | Number of egress ACL filters for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IN_ACL_V6_MANGLE_UPPER | Number of ingress ACL mangles for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_EG_ACL_V6_MANGLE_UPPER | Number of egress ACL mangles for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IN_ACL_8021x_FILTER_UPPER | Number of ingress ACL 802.1 filters on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_ACL_L4_PORT_CHECKERS_UPPER | Number of ACL port range checkers on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_ACL_REGIONS_UPPER | Number of ACL regions on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IN_ACL_MIRROR_UPPER | Number of ingress ACL mirrors on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_ACL_18B_RULES_UPPER | Number of ACL 18B rules on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_ACL_32B_RULES_UPPER | Number of ACL 32B rules on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_ACL_54B_RULES_UPPER | Number of ACL 54B rules on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IN_PBR_V4_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_IN_PBR_V6_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCAM | TCA_TCAM_ECMP_NEXTHOPS_UPPER | Number of equal cost multi-path (ECMP) next hop entries on a given switch or host is greater than maximum threshold |

A notification configuration must contain one rule. Each rule must contain a scope and a threshold. Optionally, you can specify an associated channel.  **Note**: If a rule is not associated with a channel, the event information is only reachable from the database. If you want to deliver events to one or more notification channels (syslog, Slack, or PagerDuty), create them by following the instructions in [Create Your Channel](#create-your-channel), and then return here to define your rule.

### Define a Scope

A scope is used to filter the events generated by a given rule. Scope values are set on a per TCA rule basis. Scope parameters must be entered in the order defined.

| Event ID | Scope Parameters |
| ---------- | -------------- |
| TCA_CPU_UTILIZATION_UPPER | Hostname |
| TCA_DISK_UTILIZATION_UPPER  |  Hostname |
| TCA_MEMORY_UTILIZATION_UPPER  |  Hostname |
| TCA_RXBROADCAST_UPPER  |  Hostname, Interface |
| TCA_RXBYTES_UPPER |  Hostname, Interface |
| TCA_RXMULTICAST_UPPER |  Hostname, Interface |
| TCA_SENSOR_FAN_UPPER  |  Hostname, Sensor Name |
| TCA_SENSOR_POWER_UPPER|  Hostname, Sensor Name |
| TCA_SENSOR_TEMPERATURE_UPPER  |  Hostname, Sensor Name |
| TCA_SENSOR_VOLTAGE_UPPER  |  Hostname, Sensor Name |
| TCA_TXBROADCAST_UPPER |  Hostname, Interface |
| TCA_TXBYTES_UPPER  |  Hostname, Interface |
| TCA_TXMULTICAST_UPPER |  Hostname, Interface |

Scopes are defined with regular expressions, as follows. When two paramaters are used,they are separated by a comma, but no space. 

| Parameters | Scope Value | Example | Result |
| -------------- | --------------- | ---------- | -------- |
| Hostname | \<hostname> | leaf01 | Deliver events for the specified device |
| Hostname | \<partial-hostname>\* | leaf\* | Deliver events for devices with hostnames starting with specified text (*leaf*) |
| Hostname | \* | \* | Deliver events for all devices |
| Hostname, Interface | \<hostname>,\<interface> | leaf01,swp9 | Deliver events for the specified interface (*swp9*) on the specified device (*leaf01*) |
| Hostname, Interface | \<hostname>,\* | leaf01,\* | Deliver events for all interfaces on the specified device (*leaf01*) |
| Hostname, Interface | \*,\<interface> | \*,swp9 | Deliver events for the specified interface (*swp9*) on all devices |
| Hostname, Interface | \*,\* | \*,\* | Deliver events for all devices and all interfaces |
| Hostname, Interface | \<partial-hostname>\*,\<interface> | leaf*,swp9 | Deliver events for the specified interface (*swp9*) on all devices with hostnames starting with the specified text (*leaf*) |
| Hostname, Interface | \<hostname>,\<partial-interface>\* | leaf01,swp* | Deliver events for all interface with names starting with the specified text (*swp*) on the specified device (*leaf01*) |
| Hostname, Sensor Name | \<hostname>,\<sensorname> | leaf01,fan1 | Deliver events for the specified sensor (*fan1*) on the specified device (*leaf01*) |
| Hostname, Sensor Name | \*,\<sensorname> | \*,fan1 | Deliver events for the specified sensor (*fan1*) for all devices |
| Hostname, Sensor Name |  \<hostname>,\* | leaf01,* | Deliver events for all sensors on the specified device (*leaf01*) |
| Hostname, Sensor Name | \<partial-hostname>\*,\<interface> | leaf*,fan1 | Deliver events for the specified sensor (*fan1*) on all devices with hostnames starting with the specified text (*leaf*) |
| Hostname, Sensor Name | \<hostname>,\<partial-sensorname>\* | leaf01,fan* | Deliver events for all sensors with names starting with the specified text (*fan*) on the specified device (*leaf01*) |
| Hostname, Sensor Name | \*,\* | \*,\* | Deliver events for all sensors on all devices |

### Create a TCA Rule