---
title: gNMI Streaming
author: Cumulus Networks
weight: 811
toc: 4
---
## gNMI Support on Cumulus Linux

You can use *gNMI*, the {{<exlink url="https://github.com/openconfig/gnmi" text="gRPC network management interface">}}, to collect system resource, interface, and counter information from Cumulus Linux and export it to your own gNMI client.

### Configure the gNMI Agent

To configure the gNMI agent, you need to enable it on every switch you want to use with gNMI. Optionally, you can update these default settings:

- **Log level**: The default log level is *info*. You can change the default setting to *debug*, *warning*, or *error*.
- **Default gNMI port**: The gNMI agent listens over port 9339 by default. You can change this setting in case you use that port in another application.

The `/etc/netq/netq.yml` file stores the configuration.

To configure the gNMI agent on a switch:

1. Enable the gNMI agent:

       cumulus@switch:~$ netq config add agent gnmi-enable true
1. If you want to change the default log level to something other than *info* (choose from *debug*, *warning*, or *error*), run:

       cumulus@switch:~$ netq config add agent gnmi-log-level [debug|warning|error]

1. If you want to change the default port over which the gNMI agent listens, run:

       cumulus@switch:~$ netq config add agent gnmi-port <gnmi_port>
1. Restart the NetQ Agent:

       cumulus@switch:~$ netq config restart agent


### Use Only the gNMI Agent

It is possible (although it is not recommended) to collect data using only the gNMI agent, and not the NetQ Agent. However, this sends data only to gNMI and not to NetQ.

To use only gNMI for data collection, disable the NetQ Agent, which is always enabled by default:

    cumulus@switch:~$ netq config add agent opta-enable false

{{%notice info%}}

You cannot disable both the NetQ Agent and the gNMI agent.

{{%/notice%}}

### Supported Models

Cumulus Linux supports the following OpenConfig models:

| Model| Supported Data |
| --------- | ------ |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-interfaces.yang" text="openconfig-interfaces">}} | Name, Operstatus, AdminStatus, IfIndex, MTU, LoopbackMode, Enabled |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-if-ethernet.yang" text="openconfig-if-ethernet">}} | AutoNegotiate, PortSpeed, MacAddress, NegotiatedPortSpeed, Counters|
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-if-ethernet-ext.yang" text="openconfig-if-ethernet-ext">}} | Frame size counters |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/system/openconfig-system.yang" text="openconfig-system">}} | Memory, CPU |



## Collect WJH Data Using gNMI

You can export What Just Happened data from the NetQ Agent to your own gNMI client.

The client should use the following YANG model as a reference:

{{<expand "YANG Model">}}

```
module WjhDropAggregate {
    // Entrypoint container interfaces.
    // Path --> interfaces/interface[name]/wjh/aggregate/[acl, l2, router, tunnel, buffer]/reasons/reason[id, severity]/drop[]
    // Path for L1 --> interfaces/interface[name]/wjh/aggregate/l1/drop[]

    namespace "http://nvidia.com/yang/what-just-happened-config";
    prefix "wjh_drop_aggregate";

    container interfaces {
        config false;
        list interface {
            key "name";
            leaf name {
                type string;
                mandatory "true";
                description "Interface name";
            }
            uses wjh_aggregate;
        }
    }

    grouping wjh_aggregate {
    description "Top-level grouping for What-just happened data.";
        container wjh {
            container aggregate {
                container l1 {
                    uses l1-drops;
                }
                container l2 {
                    list reason {
                        key "id severity";
                        uses reason-key;
                        uses l2-drops;
                    }
                }
                container router {
                    list reason {
                        key "id severity";
                        uses reason-key;
                        uses router-drops;
                    }
                }
                container tunnel {
                    list reason {
                        key "id severity";
                        uses reason-key;
                        uses tunnel-drops;
                    }
                }
                container acl {
                    list reason {
                        key "id severity";
                        uses reason-key;
                        uses acl-drops;
                    }
                }
                container buffer {
                    list reason {
                        key "id severity";
                        uses reason-key;
                        uses buffer-drops;
                    }
                }
            }
        }
    }

    grouping reason-key {
        leaf id {
            type uint32;
            mandatory "true";
            description "reason ID";
        }
        leaf severity {
            type string;
            mandatory "true";
            description "Severity";
        }
    }

    grouping reason_info {
        leaf reason {
                type string;
                mandatory "true";
                description "Reason name";
        }
        leaf drop_type {
            type string;
            mandatory "true";
            description "reason drop type";
        }
        leaf ingress_port {
            type string;
            mandatory "true";
            description "Ingress port name";
        }
        leaf ingress_lag {
            type string;
            description "Ingress LAG name";
        }
        leaf egress_port {
            type string;
            description "Egress port name";
        }
        leaf agg_count {
            type uint64;
            description "Aggregation count";
        }
        leaf severity {
            type string;
            description "Severity";
        }
        leaf first_timestamp {
            type uint64;
            description "First timestamp";
        }
        leaf end_timestamp {
            type uint64;
            description "End timestamp";
        }
    }

    grouping packet_info {
        leaf smac {
            type string;
            description "Source MAC";
        }
        leaf dmac {
            type string;
            description "Destination MAC";
        }
        leaf sip {
            type string;
            description "Source IP";
        }
        leaf dip {
            type string;
            description "Destination IP";
        }
        leaf proto {
            type uint32;
            description "Protocol";
        }
        leaf sport {
            type uint32;
            description "Source port";
        }
        leaf dport {
            type uint32;
            description "Destination port";
        }
    }

    grouping l1-drops {
        description "What-just happened drops.";
        list drop {
            leaf ingress_port {
                type string;
                description "Ingress port";
            }
            leaf is_port_up {
                type boolean;
                description "Is port up";
            }
            leaf port_down_reason {
                type string;
                description "Port down reason";
            }
            leaf description {
                type string;
                description "Description";
            }
            leaf state_change_count {
                type uint64;
                description "State change count";
            }
            leaf symbol_error_count {
                type uint64;
                description "Symbol error count";
            }
            leaf crc_error_count {
                type uint64;
                description "CRC error count";
            }
            leaf first_timestamp {
                type uint64;
                description "First timestamp";
            }
            leaf end_timestamp {
                type uint64;
                description "End timestamp";
            }
            leaf timestamp {
                type uint64;
                description "Timestamp";
            }
        }
    }
    grouping l2-drops {
        description "What-just happened drops.";
        list drop {
            uses reason_info;
            uses packet_info;
        }
    }

    grouping router-drops {
        description "What-just happened drops.";
        list drop {
            uses reason_info;
            uses packet_info;
        }
    }

    grouping tunnel-drops {
        description "What-just happened drops.";
        list drop {
            uses reason_info;
            uses packet_info;
        }
    }

    grouping acl-drops {
        description "What-just happened drops.";
        list drop {
            uses reason_info;
            uses packet_info;
            leaf acl_rule_id {
                type uint64;
                description "ACL rule ID";
            }
            leaf acl_bind_point {
                type uint32;
                description "ACL bind point";
            }
            leaf acl_name {
                type string;
                description "ACL name";
            }
            leaf acl_rule {
                type string;
                description "ACL rule";
            }
        }
    }

    grouping buffer-drops {
        description "What-just happened drops.";
        list drop {
            uses reason_info;
            uses packet_info;
            leaf traffic_class {
                type uint32;
                description "Traffic Class";
            }
            leaf original_occupancy {
                type uint32;
                description "Original occupancy";
            }
            leaf original_latency {
                type uint64;
                description "Original latency";
            }
        }
    }
}
```

{{</expand>}}

### Supported Features

In this release, the gNMI agent supports *capability* and *stream subscribe* requests for WJH events.


### WJH Drop Reasons
<!-- vale off -->
The data NetQ sends to the gNMI agent is in the form of WJH drop reasons. The reasons are generated by the SDK and are stored in the `/usr/etc/wjh_lib_conf.xml` file on the switch and. Use this file as a guide to filter for specific reason types (L1, ACL, and so forth), reason IDs, and/or event severities.

#### L1 Drop Reasons

<!-- L1 aggregate drops do not have severity column as it's missing from the SDK, and hence it's not exported -->

| Reason ID | Reason | Description |
| --------- | ------ | ----------- |
| 10021 | Port admin down | Validate port configuration |
| 10022 | Auto-negotiation failure | Set port speed manually, disable auto-negotiation |
| 10023 | Logical mismatch with peer link | Check cable/transceiver |
| 10024 | Link training failure | Check cable/transceiver |
| 10025 | Peer is sending remote faults | Replace cable/transceiver |
| 10026 | Bad signal integrity | Replace cable/transceiver |
| 10027 | Cable/transceiver is not supported | Use supported cable/transceiver |
| 10028 | Cable/transceiver is unplugged | Plug cable/transceiver |
| 10029 | Calibration failure | Check cable/transceiver |
| 10030 | Cable/transceiver bad status | Check cable/transceiver |
| 10031 | Other reason | Other L1 drop reason|

#### L2 Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 201 | MLAG port isolation | Notice | Expected behavior |
| 202 | Destination MAC is reserved (DMAC=01-80-C2-00-00-0x) | Error | Bad packet was received from the peer |
| 203 | VLAN tagging mismatch | Error | Validate the VLAN tag configuration on both ends of the link |
| 204 | Ingress VLAN filtering | Error | Validate the VLAN membership configuration on both ends of the link |
| 205 | Ingress spanning tree filter | Notice | Expected behavior |
| 206 | Unicast MAC table action discard | Error | Validate MAC table for this destination MAC |
| 207 | Multicast egress port list is empty | Warning | Validate why IGMP join or multicast router port does not exist |
| 208 | Port loopback filter | Error | Validate MAC table for this destination MAC |
| 209 | Source MAC is multicast | Error | Bad packet was received from peer |
| 210 | Source MAC equals destination MAC | Error | Bad packet was received from peer |

#### Router Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 301 | Non-routable packet | Notice | Expected behavior |
| 302 | Blackhole route | Warning | Validate routing table for this destination IP |
| 303 | Unresolved neighbor/next hop | Warning | Validate ARP table for the neighbor/next hop |
| 304 | Blackhole ARP/neighbor | Warning | Validate ARP table for the next hop |
| 305 | IPv6 destination in multicast scope FFx0:/16 | Notice | Expected behavior - packet is not routable |
| 306 | IPv6 destination in multicast scope FFx1:/16 | Notice | Expected behavior - packet is not routable |
| 307 | Non IP packet | Notice | Destination MAC is the router, packet is not routable |
| 308 | Unicast destination IP but multicast destination MAC | Error | Bad packet was received from the peer |
| 309 | Destination IP is loopback address | Error | Bad packet was received from the peer |
| 310 | Source IP is multicast | Error | Bad packet was received from the peer |
| 311 | Source IP is in class E | Error | Bad packet was received from the peer |
| 312 | Source IP is loopback address | Error | Bad packet was received from the peer |
| 313 | Source IP is unspecified | Error | Bad packet was received from the peer |
| 314 | Checksum or IPver or IPv4 IHL too short | Error | Bad cable or bad packet was received from the peer |
| 315 | Multicast MAC mismatch | Error | Bad packet was received from the peer |
| 316 | Source IP equals destination IP | Error | Bad packet was received from the peer |
| 317 | IPv4 source IP is limited broadcast | Error | Bad packet was received from the peer |
| 318 | IPv4 destination IP is local network (destination=0.0.0.0/8) | Error | Bad packet was received from the peer || 319 | IPv4 destination IP is link local (destination in 169.254.0.0/16) | Error | Bad packet was received from the peer |
| 320 | Ingress router interface is disabled | Warning | Validate your configuration |
| 321 | Egress router interface is disabled | Warning | Validate your configuration |
| 323 | IPv4 routing table (LPM) unicast miss | Warning | Validate routing table for this destination IP |
| 324 | IPv6 routing table (LPM) unicast miss | Warning | Validate routing table for this destination IP |
| 325 | Router interface loopback | Warning | Validate the interface configuration |
| 326 | Packet size is larger than router interface MTU | Warning | Validate the router interface MTU configuration |
| 327 | TTL value is too small | Warning | Actual path is longer than the TTL |
<!-- vale on -->

#### Tunnel Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 402 | Overlay switch - Source MAC is multicast | Error | The peer sent a bad packet |
| 403 | Overlay switch - Source MAC equals destination MAC | Error | The peer sent a bad packet |
| 404 | Decapsulation error | Error | The peer sent a bad packet |

#### ACL Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 601 | Ingress port ACL | Notice | Validate ACL configuration |
| 602 | Ingress router ACL | Notice | Validate ACL configuration |
| 603 | Egress router ACL | Notice | Validate ACL configuration |
| 604 | Egress port ACL | Notice | Validate ACL configuration |

#### Buffer Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 503 | Tail drop | Warning | Monitor network congestion |
| 504 | WRED | Warning | Monitor network congestion |
| 505 | Port TC Congestion Threshold Crossed | Notice | Monitor network congestion |
| 506 | Packet Latency Threshold Crossed | Notice | Monitor network congestion |

### Related Information

{{<exlink url="https://datatracker.ietf.org/meeting/101/materials/slides-101-netconf-grpc-network-management-interface-gnmi-00" text="gNMI presentation to IETF">}}

### gNMI Client Requests

<!-- vale off -->
You use your gNMI client on a host server to request capabilities and data the agent is subscribed to.
<!-- vale on -->

To make a subscribe request, run:

```
[root@host ~]# /path/to/your/gnmi_client/gnmi_client -gnmi_address 10.209.37.84 -request subscribe
2021/05/06 18:33:10.142160 host gnmi_client[24847]: INFO: 10.209.37.84:9339: ready for streaming
2021/05/06 18:33:10.220814 host gnmi_client[24847]: INFO: sync response received: sync_response:true
2021/05/06 18:33:16.813000 host gnmi_client[24847]: INFO: update received [interfaces interface swp8 wjh aggregate l2 reason 209 error]: {"Drop":[{"AggCount":1,"Dip":"1.2.0.0","Dmac":"00:bb:cc:11:22:32","Dport":0,"DropType":"L2","EgressPort":"","EndTimestamp":1620326044,"FirstTimestamp":1620326044,"IngressLag":"","IngressPort":"swp8","Proto":0,"Reason":"Source MAC is multicast","Severity":"Error","Sip":"10.213.1.242","Smac":"ff:ff:ff:ff:ff:ff","Sport":0}],"Id":209,"Severity":"Error"}
2021/05/06 18:33:16.815068 host gnmi_client[24847]: INFO: update received [interfaces interface swp8 wjh aggregate l2 reason 209 error]: {"Drop":[{"AggCount":1,"Dip":"1.2.0.0","Dmac":"00:bb:cc:11:22:32","Dport":0,"DropType":"L2","EgressPort":"","EndTimestamp":1620326044,"FirstTimestamp":1620326044,"IngressLag":"","IngressPort":"swp8","Proto":0,"Reason":"Source MAC is multicast","Severity":"Error","Sip":"10.213.2.242","Smac":"ff:ff:ff:ff:ff:ff","Sport":0}],"Id":209,"Severity":"Error"}
2021/05/06 18:33:16.818896 host gnmi_client[24847]: INFO: update received [interfaces interface swp8 wjh aggregate l2 reason 209 error]: {"Drop":[{"AggCount":1,"Dip":"1.2.0.0","Dmac":"00:bb:cc:11:22:32","Dport":0,"DropType":"L2","EgressPort":"","EndTimestamp":1620326044,"FirstTimestamp":1620326044,"IngressLag":"","IngressPort":"swp8","Proto":0,"Reason":"Source MAC is multicast","Severity":"Error","Sip":"10.213.3.242","Smac":"ff:ff:ff:ff:ff:ff","Sport":0}],"Id":209,"Severity":"Error"}
2021/05/06 18:33:16.823091 host gnmi_client[24847]: INFO: update received [interfaces interface swp8 wjh aggregate l2 reason 209 error]: {"Drop":[{"AggCount":1,"Dip":"1.2.0.0","Dmac":"00:bb:cc:11:22:32","Dport":0,"DropType":"L2","EgressPort":"","EndTimestamp":1620326044,"FirstTimestamp":1620326044,"IngressLag":"","IngressPort":"swp8","Proto":0,"Reason":"Source MAC is multicast","Severity":"Error","Sip":"10.213.4.242","Smac":"ff:ff:ff:ff:ff:ff","Sport":0}],"Id":209,"Severity":"Error"}
...
```

To request the capabilities, run:

```
[root@host ~]# /path/to/your/gnmi_client/gnmi_client/gnmi_client -gnmi_address 10.209.37.84 -request capabilities
2021/05/06 18:36:31.285648 host gnmi_client[25023]: INFO: 10.209.37.84:9339: ready for streaming
2021/05/06 18:36:31.355944 host gnmi_client[25023]: INFO: capability response: supported_models:{name:"WjhDropAggregate"  organization:"NVIDIA"  version:"0.1"}  supported_encodings:JSON  supported_encodings:JSON_IETF
```