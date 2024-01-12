---
title: gNMI Streaming
author: NVIDIA
weight: 811
toc: 4
---
You can use {{<exlink url="https://github.com/openconfig/gnmi" text="gRPC Network Management Interface">}} (gNMI) to collect system resource, interface, and counter information from Cumulus Linux and export it to your own gNMI client.

### Configure the gNMI Agent

The `netq-agent` package includes the gNMI agent, which it disables by default. To enable the gNMI agent:

```
 cumulus@switch:~$ sudo systemctl enable netq-agent.service
 cumulus@switch:~$ sudo systemctl start netq-agent.service
 cumulus@switch:~$ netq config add agent gnmi-enable true
 ```

The gNMI agent listens over port 9339. You can change the default port in case you use that port in another application. The `/etc/netq/netq.yml` file stores the configuration.

Use the following commands to adjust the settings:

1. Disable the gNMI agent:

   ```
   cumulus@switch:~$ netq config add agent gnmi-enable false
   ```

2. Change the default port over which the gNMI agent listens:

   ```
   cumulus@switch:~$ netq config add agent gnmi-port <gnmi_port>
   ```

3. Restart the NetQ Agent to incorporate the configuration changes:

   ```
   cumulus@switch:~$ netq config restart agent
   ```

{{%notice note%}}
The gNMI agent relies on the data it collects from the NVUE service. For complete data collection with gNMI, you must enable the NVUE service. To check the status of the `nvued` service, run the `sudo systemctl status nvued.service` command:

```
cumulus@switch:mgmt:~$ sudo systemctl status nvued.service
● nvued.service - NVIDIA User Experience Daemon
   Loaded: loaded (/lib/systemd/system/nvued.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2023-03-09 20:00:17 UTC; 6 days ago
```

If necessary, enable and start the service:

```
cumulus@switch:mgmt:~$ sudo systemctl enable nvued.service
cumulus@switch:mgmt:~$ sudo systemctl start nvued.service
```

{{%/notice%}}

### Use the gNMI Agent Only

NVIDIA recommends that you collect data with both the gNMI and NetQ agents. However, if you do not want to collect data with both agents or you are not streaming data to NetQ, you can disable the NetQ agent. Cumulus Linux then sents data only to the gNMI agent.

To disable the NetQ agent:

```
cumulus@switch:~$ netq config add agent opta-enable false
```

{{%notice note%}}
You cannot disable both the NetQ and gNMI agent. If you enable both agents on Cumulus Linux and a NetQ server is unreachable, the switch does not send the data to gNMI from the following models:
- `openconfig-interfaces`
- `openconfig-if-ethernet`
- `openconfig-if-ethernet-ext`
- `openconfig-system`
- `nvidia-if-ethernet-ext`

WJH, `openconfig-platform`, and `openconfig-lldp` data continue streaming to gNMI in this state. If you are only using gNMI and a NetQ telemetry server does not exist, disable the NetQ agent by setting `opta-enable` to `false`.
{{%/notice%}}

### Supported Subscription Modes

Cumulus Linux supports the following gNMI {{<exlink url="https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#3515-creating-subscriptions" text="subscription modes">}}:

- `POLL` mode
- `ONCE` mode
- `STREAM` mode, supported for `ON_CHANGE` subscriptions only

### Supported Models

Cumulus Linux supports the following OpenConfig models:

| Model| Supported Data |
| --------- | ------ |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-interfaces.yang" text="openconfig-interfaces">}} | Name, Operstatus, AdminStatus, IfIndex, MTU, LoopbackMode, Enabled |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-if-ethernet.yang" text="openconfig-if-ethernet">}} | AutoNegotiate, PortSpeed, MacAddress, NegotiatedPortSpeed, Counters|
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-if-ethernet-ext.yang" text="openconfig-if-ethernet-ext">}} | Frame size counters |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/system/openconfig-system.yang" text="openconfig-system">}} | Memory, CPU |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/platform/openconfig-platform.yang" text="openconfig-platform">}} | Platform data |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/lldp/openconfig-lldp.yang" text="openconfig-lldp">}} | LLDP data |

gNMI clients can also use the following model for extended Ethernet counters:
<!-- vale off -->
{{<expand "nvidia-if-ethernet-ext">}}
```
module nvidia-if-ethernet-counters-ext {
    // xPath --> /interfaces/interface[name=*]/ethernet/counters/state/

   namespace "http://nvidia.com/yang/nvidia-ethernet-counters";
   prefix "nvidia-if-ethernet-counters-ext";


  // import some basic types
  import openconfig-interfaces { prefix oc-if; }
  import openconfig-if-ethernet { prefix oc-eth; }
  import openconfig-yang-types { prefix oc-yang; }


  revision "2021-10-12" {
    description
      "Initial revision";
    reference "1.0.0.";
  }

  grouping ethernet-counters-ext {

    leaf alignment-error {
      type oc-yang:counter64;
    }

    leaf in-acl-drops {
      type oc-yang:counter64;
    }

    leaf in-buffer-drops {
      type oc-yang:counter64;
    }

    leaf in-dot3-frame-errors {
      type oc-yang:counter64;
    }

    leaf in-dot3-length-errors {
      type oc-yang:counter64;
    }

    leaf in-l3-drops {
      type oc-yang:counter64;
    }

    leaf in-pfc0-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc1-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc2-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc3-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc4-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc5-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc6-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc7-packets {
      type oc-yang:counter64;
    }

    leaf out-non-q-drops {
      type oc-yang:counter64;
    }

    leaf out-pfc0-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc1-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc2-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc3-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc4-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc5-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc6-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc7-packets {
      type oc-yang:counter64;
    }

    leaf out-q0-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q1-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q2-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q3-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q4-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q5-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q6-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q7-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q8-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q9-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q-drops {
      type oc-yang:counter64;
    }

    leaf out-q-length {
      type oc-yang:counter64;
    }

    leaf out-wred-drops {
      type oc-yang:counter64;
    }

    leaf symbol-errors {
      type oc-yang:counter64;
    }

    leaf out-tx-fifo-full {
      type oc-yang:counter64;
    }

  }

  augment "/oc-if:interfaces/oc-if:interface/oc-eth:ethernet/" +
    "oc-eth:state/oc-eth:counters" {
      uses ethernet-counters-ext;
  }

}
```
{{</expand>}}
<!-- vale on -->
## Collect WJH Data with gNMI

You can export WJH data from the NetQ agent to your own gNMI client.

The client must use the following YANG model as a reference:
<!-- vale off -->
{{<expand "nvidia-if-wjh-drop-aggregate">}}

```
module nvidia-wjh {
    // Entrypoint /oc-if:interfaces/oc-if:interface
    //
    // xPath L1     --> interfaces/interface[name=*]/wjh/aggregate/l1
    // xPath L2     --> /interfaces/interface[name=*]/wjh/aggregate/l2/reasons/reason[id=*][severity=*]
    // xPath Router --> /interfaces/interface[name=*]/wjh/aggregate/router/reasons/reason[id=*][severity=*]
    // xPath Tunnel --> /interfaces/interface[name=*]/wjh/aggregate/tunnel/reasons/reason[id=*][severity=*]
    // xPath Buffer --> /interfaces/interface[name=*]/wjh/aggregate/buffer/reasons/reason[id=*][severity=*]
    // xPath ACL    --> /interfaces/interface[name=*]/wjh/aggregate/acl/reasons/reason[id=*][severity=*]

    import openconfig-interfaces { prefix oc-if; }

    namespace "http://nvidia.com/yang/what-just-happened-config";
    prefix "nvidia-wjh";

    revision "2021-10-12" {
        description
            "Initial revision";
        reference "1.0.0.";
    }

    augment "/oc-if:interfaces/oc-if:interface" {
        uses interfaces-wjh;
    }

    grouping interfaces-wjh {
        description "Top-level grouping for What-just happened data.";
        container wjh {
            container aggregate {
                container l1 {
                    container state {
                        leaf drop {
                            type string;
                            description "Drop list based on wjh-drop-types module encoded in JSON";
                        }
                    }
                }
                container l2 {
                    uses reason-drops;
                }
                container router {
                    uses reason-drops;
                }
                container tunnel {
                    uses reason-drops;
                }
                container acl {
                    uses reason-drops;
                }
                container buffer {
                    uses reason-drops;
                }
            }
        }
    }

    grouping reason-drops {
        container reasons {
            list reason {
                key "id severity";
                leaf id {
                    type leafref {
                        path "../state/id";
                    }
                    description "reason ID";
                }
                leaf severity {
                    type leafref {
                        path "../state/severity";
                    }
                    description "Reason severity";
                }
                container state {
                    leaf id {
                        type uint32;
                        description "Reason ID";
                    }
                    leaf name {
                        type string;
                        description "Reason name";
                    }
                    leaf severity {
                        type string;
                        mandatory "true";
                        description "Reason severity";
                    }
                    leaf drop {
                        type string;
                        description "Drop list based on wjh-drop-types module encoded in JSON";
                    }
                }
            }
        }
    }
}

module wjh-drop-types {
    namespace "http://nvidia.com/yang/what-just-happened-config-types";
    prefix "wjh-drop-types";

    container l1-aggregated {
        uses l1-drops;
    }
    container l2-aggregated {
        uses l2-drops;
    }
    container router-aggregated {
        uses router-drops;
    }
    container tunnel-aggregated {
        uses tunnel-drops;
    }
    container acl-aggregated {
        uses acl-drops;
    }
    container buffer-aggregated {
        uses buffer-drops;
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
    grouping l2-drops {
        description "What-just happened drops.";
        uses reason_info;
        uses packet_info;
    }

    grouping router-drops {
        description "What-just happened drops.";
        uses reason_info;
        uses packet_info;
    }

    grouping tunnel-drops {
        description "What-just happened drops.";
        uses reason_info;
        uses packet_info;
    }

    grouping acl-drops {
        description "What-just happened drops.";
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

    grouping buffer-drops {
        description "What-just happened drops.";
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
```

{{</expand>}}
<!-- vale on -->
### Supported Features

The gNMI Agent supports `Capabilities` and `STREAM` subscribe requests for WJH events.

### WJH Drop Reasons
<!-- vale off -->
The data that NetQ sends to the gNMI agent is in the form of WJH drop reasons. The SDK generates the drop reasons and Cumulus Linux stores them in the `/usr/etc/wjh_lib_conf.xml` file. Use this file as a guide to filter for specific reason types (L1, ACL, and so on), reason IDs, or event severities.

#### L1 Drop Reasons

<!-- L1 aggregate drops do not have severity column as it's missing from the SDK, and hence it's not exported -->

| Reason ID | Reason | Description |
| --------- | ------ | ----------- |
| 10021 | Port admin down | Validate port configuration |
| 10022 | Auto-negotiation failure | Set port speed manually, disable auto-negotiation |
| 10023 | Logical mismatch with peer link | Check cable or transceiver |
| 10024 | Link training failure | Check cable or transceiver |
| 10025 | Peer is sending remote faults | Replace cable or transceiver |
| 10026 | Bad signal integrity | Replace cable or transceiver |
| 10027 | Cable or transceiver is not supported | Use supported cable or transceiver |
| 10028 | Cable or transceiver is unplugged | Plug cable or transceiver |
| 10029 | Calibration failure | Check cable or transceiver |
| 10030 | Cable or transceiver bad status | Check cable or transceiver |
| 10031 | Other reason | Other L1 drop reason|

#### L2 Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 201 | MLAG port isolation | Notice | Expected behavior |
| 202 | Destination MAC is reserved (DMAC=01-80-C2-00-00-0x) | Error | Bad packet received from the peer |
| 203 | VLAN tagging mismatch | Error | Validate the VLAN tag configuration on both ends of the link |
| 204 | Ingress VLAN filtering | Error | Validate the VLAN membership configuration on both ends of the link |
| 205 | Ingress spanning tree filter | Notice | Expected behavior |
| 206 | Unicast MAC table action discard | Error | Validate MAC table for this destination MAC |
| 207 | Multicast egress port list is empty | Warning | Validate why IGMP join or multicast router port does not exist |
| 208 | Port loopback filter | Error | Validate MAC table for this destination MAC |
| 209 | Source MAC is multicast | Error | Bad packet received from peer |
| 210 | Source MAC equals destination MAC | Error | Bad packet received from peer |

#### Router Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 301 | Non-routable packet | Notice | Expected behavior |
| 302 | Blackhole route | Warning | Validate routing table for this destination IP |
| 303 | Unresolved neighbor or next hop | Warning | Validate ARP table for the neighbor or next hop |
| 304 | Blackhole ARP or neighbor | Warning | Validate ARP table for the next hop |
| 305 | IPv6 destination in multicast scope FFx0:/16 | Notice | Expected behavior - packet is not routable |
| 306 | IPv6 destination in multicast scope FFx1:/16 | Notice | Expected behavior - packet is not routable |
| 307 | Non-IP packet | Notice | Destination MAC is the router, packet is not routable |
| 308 | Unicast destination IP but multicast destination MAC | Error | Bad packet received from the peer |
| 309 | Destination IP is loopback address | Error | Bad packet received from the peer |
| 310 | Source IP is multicast | Error | Bad packet received from the peer |
| 311 | Source IP is in class E | Error | Bad packet received from the peer |
| 312 | Source IP is loopback address | Error | Bad packet received from the peer |
| 313 | Source IP is unspecified | Error | Bad packet received from the peer |
| 314 | Checksum or IPver or IPv4 IHL too short | Error | Bad cable or bad packet received from the peer |
| 315 | Multicast MAC mismatch | Error | Bad packet received from the peer |
| 316 | Source IP equals destination IP | Error | Bad packet received from the peer |
| 317 | IPv4 source IP is limited broadcast | Error | Bad packet received from the peer |
| 318 | IPv4 destination IP is local network (destination=0.0.0.0/8) | Error | Bad packet received from the peer || 319 | IPv4 destination IP is link local (destination in 169.254.0.0/16) | Error | Bad packet received from the peer |
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
| 505 | Port TC congestion threshold crossed | Notice | Monitor network congestion |
| 506 | Packet latency threshold crossed | Notice | Monitor network congestion |

### gNMI Client Requests

<!-- vale off -->
You can use your gNMI client on a host to request capabilities and data to which the Agent subscribes. The examples below use the {{<exlink url="https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#3515-creating-subscriptions" text="gNMIc client.">}}.
<!-- vale on -->

The following example shows a gNMIc `STREAM` request for WJH data:

```
gnmic -a 10.209.37.121:9339 -u cumulus -p ****** --skip-verify subscribe --path "wjh/aggregate/l2/reasons/reason[id=209][severity=error]/state/drop" --mode stream --prefix "/interfaces/interface[name=swp8]/" --target netq

{
  "source": "10.209.37.121:9339",
  "subscription-name": "default-1677695197",
  "timestamp": 1677695102858146800,
  "time": "2023-03-01T18:25:02.8581468Z",
  "prefix": "interfaces/interface[name=swp8]/wjh/aggregate/l2/reasons/reason[severity=error][id=209]",
  "target": "netq",
  "updates": [
    {
      "Path": "state/drop",
      "values": {
        "state/drop": "[{\"AggCount\":283,\"Dip\":\"0.0.0.0\",\"Dmac\":\"1c:34:da:17:93:7c\",\"Dport\":0,\"DropType\":\"L2\",\"EgressPort\":\"\",\"EndTimestamp\":1677695102,\"FirstTimestamp\":1677695072,\"Hostname\":\"neo-switch01\",\"IngressLag\":\"\",\"IngressPort\":\"swp8\",\"Proto\":0,\"Reason\":\"Source MAC is multicast\",\"ReasonId\":209,\"Severity\":\"Error\",\"Sip\":\"0.0.0.0\",\"Smac\":\"01:00:5e:00:00:01\",\"Sport\":0}]"
      }
    }
  ]
}
{
  "source": "10.209.37.121:9339",
  "subscription-name": "default-1677695197",
  "timestamp": 1677695132988218890,
  "time": "2023-03-01T18:25:32.98821889Z",
  "prefix": "interfaces/interface[name=swp8]/wjh/aggregate/l2/reasons/reason[severity=error][id=209]",
  "target": "netq",
  "updates": [
    {
      "Path": "state/drop",
      "values": {
        "state/drop": "[{\"AggCount\":287,\"Dip\":\"0.0.0.0\",\"Dmac\":\"1c:34:da:17:93:7c\",\"Dport\":0,\"DropType\":\"L2\",\"EgressPort\":\"\",\"EndTimestamp\":1677695132,\"FirstTimestamp\":1677695102,\"Hostname\":\"neo-switch01\",\"IngressLag\":\"\",\"IngressPort\":\"swp8\",\"Proto\":0,\"Reason\":\"Source MAC is multicast\",\"ReasonId\":209,\"Severity\":\"Error\",\"Sip\":\"0.0.0.0\",\"Smac\":\"01:00:5e:00:00:01\",\"Sport\":0}]"
      }
    }
  ]
}
```

The following example shows a gNMIc `ONCE` mode request for interface port speed:

```
gnmic -a 10.209.37.121:9339 -u cumulus -p ****** --skip-verify subscribe --path "ethernet/state/port-speed" --mode once --prefix "/interfaces/interface[name=swp1]/" --target netq
{
  "source": "10.209.37.123:9339",
  "subscription-name": "default-1677695151",
  "timestamp": 1677256036962254134,
  "time": "2023-02-24T16:27:16.962254134Z",
  "target": "netq",
  "updates": [
    {
      "Path": "interfaces/interface[name=swp1]/ethernet/state/port-speed",
      "values": {
        "interfaces/interface/ethernet/state/port-speed": "SPEED_1GB"
      }
    }
  ]
}
```

The following example shows a gNMIc `POLL` mode request for interface status:

```
gnmic -a 10.209.37.121:9339 -u cumulus -p ****** --skip-verify subscribe --path "state/oper-status" --mode poll --prefix "/interfaces/interface[name=swp1]/" --target netq
{
  "timestamp": 1677644403153198642,
  "time": "2023-03-01T04:20:03.153198642Z",
  "prefix": "interfaces/interface[name=swp1]",
  "target": "netq",
  "updates": [
    {
      "Path": "state/oper-status",
      "values": {
        "state/oper-status": "UP"
      }
    }
  ]
}
received sync response 'true' from '10.209.37.123:9339'
{
  "timestamp": 1677644403153198642,
  "time": "2023-03-01T04:20:03.153198642Z",
  "prefix": "interfaces/interface[name=swp1]",
  "target": "netq",
  "updates": [
    {
      "Path": "state/oper-status",
      "values": {
        "state/oper-status": "UP"
      }
    }
  ]
}
```

## Related Information

- {{<exlink url="https://datatracker.ietf.org/meeting/101/materials/slides-101-netconf-grpc-network-management-interface-gnmi-00" text="gNMI presentation to IETF">}}
- {{<exlink url="https://gnmic.openconfig.net/" text="gNMIc client">}}
- {{<exlink url="https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#3515-creating-subscriptions" text="gNMI subscription mode documentation">}}
