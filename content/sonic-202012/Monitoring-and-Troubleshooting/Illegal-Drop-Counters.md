---
title: Illegal Drop Counters
author: Cumulus Networks
weight: 670
product: SONiC
version: 201911_MUR5
siteSlug: sonic
---

Illegal Drop Counters provide better packet drop visibility in SONiC by providing a mechanism which allows the user to count packet drops that occur due to different reasons. The feature is a part of base system, thus, no standalone installation is required.
Counters might drop based on one of the following scenarios:
- drop reason – a condition which led to switch pipeline “drop” decision
- drop reason family – group of drop reasons belonging to a pipeline stage (L2, L3, TUNNEL, ACL)
- drop counter – a user-created counter which can be associated with one or several drop reason
- drop counter type – ingress/egress direction for switch/port level drops

## Supported Drop Reasons

- L2 drop family includes the following drop reasons:

| Drop Reason | Description |
| ----------- | ----------- |
| SMAC_MULTICAST | Source MAC is multicast |
| SMAC_EQUALS_DMAC | Source MAC equals destination MAC |
| DMAC_RESERVED | Destination MAC is Reserved (Destination MAC=01-80-C2-00-00-0x) |
| VLAN_TAG_NOT_ALLOWED | VLAN tag not allowed (Frame tagged when port is dropping tagged, or untagged when dropping untagged) |
| INGRESS_VLAN_FILTER | Ingress VLAN filter (incoming are tagged with a VLAN that is not configured on the ingress bridge port) |
| INGRESS_STP_FILTER | Ingress STP filter |
| FDB_UC_DISCARD | Unicast FDB table action discard |
| FDB_MC_DISCARD | Multicast FDB table empty tx list |
| L2_LOOPBACK_FILTER | Port L2 loopback filter (packet egressing on the same port+VLAN as ingressing) |
| L2_ANY | Any L2 pipeline drop (all L2 drop reasons together) |

- L3 family includes the following drop reasons:

| Drop Reason | Description |
| ----------- | ----------- |
| EXCEEDS_L3_MTU | Packet size is larger than the L3 (Router Interface) MTU |
| TTL | TTL expired |
| L3_LOOPBACK_FILTER | RIF L3 loopback filter (packet egressing on the same RIF as ingressing) |
| NON_ROUTABLE | Non routable packet (IGMP v1 v2 v3 membership query, IGMP v1 membership report, IGMP v2 membership report, IGMP v2 leave group, IGMP v3 membership report) |
| NO_L3_HEADER | Destination MAC is the router MAC; however, packet is not routable (isn't IP or MPLS) |
| IP_HEADER_ERROR | IP Header error (Due to header checksum or bad IP version or IPv4 IHL too short) |
| UC_DIP_MC_DMAC | Unicast destination IP with non-unicast (multicast or broadcast) destination MAC |
| DIP_LOOPBACK | Destination IP is loopback address (for IPv4: Destination IP=127.0.0.0/8, for IPv6: Destination IP=::1/128 OR Destination IP=0:0:0:0:0:ffff:7f00:0/104) |
| SIP_LOOPBACK | Source IP is loopback address (for IPv4: Source IP=127.0.0.0/8, for IPv6: Source IP=::1/128) |
| SIP_MC | Source IP is multicast address (for IPv4: Source IP=224.0.0.0/4, for IPv6: Source IP=FF00::/8) |
| SIP_CLASS_E | Source IP is in class E (IPv4 AND Source IP=240.0.0.0/4 AND Source IP!=255.255.255.255) |
| SIP_UNSPECIFIED | Source IP unspecified (for IPv4: Source IP=0.0.0.0/32, for IPv6: Source IP=::0) |
| MC_DMAC_MISMATCH | Destination IP is multicast but destination MAC isn't (Destination IP is multicast AND for IPv4: Destination MAC!={01-00-5E-0 (25 bits), dip[22:0]}, for IPv6: Destination MAC!={33-33, DIP[31:0]}) |
| SIP_EQUALS_DIP | Source IP equals destination IP |
| SIP_BC | IPv4 source IP is limited broadcast (Source IP=255.255.255.255) |
| DIP_LOCAL | IPv4 destination IP is local network (Destination IP=0.0.0.0/8) |
| DIP_LINK_LOCAL | IPv4 unicast destination IP is link local (Destination IP=169.254.0.0/16) |
| SIP_LINK_LOCAL | IPv4 Source IP is link local (Source IP=169.254.0.0/16) |
| IPV6_MC_SCOPE0 | IPv6 destination in multicast scope 0 reserved (Destination IP=ff:x0:/16) |
| IPV6_MC_SCOPE1 | IPv6 destination in multicast scope 1 interface-local (Destination IP=ff:x1:/16) |
| IRIF_DISABLED | Ingress RIF is disabled |
| ERIF_DISABLED | Egress RIF is disabled |
| LPM4_MISS | IPv4 Routing table (LPM) unicast miss |
| LPM6_MISS | IPv6 Routing table (LPM) unicast miss |
| BLACKHOLE_ROUTE | Black hole route (discard by route entry) |
| BLACKHOLE_ARP | Black hole ARP/Neighbor (discard by ARP or neighbor entries) |
| UNRESOLVED_NEXT_HOP | Unresolved next hop (missing ARP entry) |
| L3_ANY | Any L3 pipeline drop (all L3 drop reasons together) |

- TUNNEL drop family includes:

| Drop Reason | Description |
| ----------- | ----------- |
| DECAP_ERROR | Packet decapsulation failed (need to decap too many bytes, remaining header are to short) |

- ACL drop family includes:

| Drop Reason | Description |
| ----------- | ----------- |
| ACL_ANY | Packet is dropped due to configured ACL rules, all stages/bind points combinations |

## Configuration Commands

| config dropcounters install | Description |
| --------------------------- | ----------- |
| config dropcounters install [OPTIONS] COUNTER_NAME COUNTER_TYPE REASONS | Installs a new drop counter. |
| Example | <pre># config dropcounters install COUNTER_1 SWITCH_INGRESS_DROPS L2_ANY</pre> |

| config dropcounters add-reasons | Description |
| --------------------------- | ----------- |
| config dropcounters add-reasons [OPTIONS] COUNTER_NAME REASONS | Adds reasons to an existing drop counter. |
| Example | <pre># config dropcounters add-reasons COUNTER_1 L3_ANY</pre> |

| config dropcounters remove-reasons | Description |
| --------------------------- | ----------- |
| config dropcounters remove-reasons [OPTIONS] COUNTER_NAME REASONS | Remove reasons from an existing drop counter |
| Example | <pre>#  config dropcounters remove-reasons COUNTER_1 L2_ANY</pre> |

| config dropcounters delete | Description |
| --------------------------- | ----------- |
| config dropcounters delete [OPTIONS] COUNTER_NAME | Deletes an existing drop counter |
| Example | <pre>#  config dropcounters delete COUNTER_1</pre> |

| show dropcounters capabilities | Description |
| --------------------------- | ----------- |
| show dropcounters capabilities | Displays a total allowed number of drop counters and a list of the supported drop reasons for a particular counter type. |
| Example | <pre>#  show dropcounters capabilities<br />Counter Type            Total<br />--------------------  -------<br />SWITCH_EGRESS_DROPS        31<br />SWITCH_INGRESS_DROPS       31<br /><br />SWITCH_INGRESS_DROPS<br />        ACL_ANY<br />        DECAP_ERROR<br />        BLACKHOLE_ARP<br />        LPM6_MISS<br />        ERIF_DISABLED<br />        IPV6_MC_SCOPE1<br />        IPV6_MC_SCOPE0<br />        SIP_LINK_LOCAL<br />        DIP_LINK_LOCAL<br />        DIP_LOCAL<br />        MC_DMAC_MISMATCH<br />        FDB_MC_DISCARD<br />        L3_ANY<br />        INGRESS_VLAN_FILTER<br />        LPM4_MISS<br />        L2_ANY<br />        IRIF_DISABLED<br />        SMAC_MULTICAST<br />        FDB_UC_DISCARD<br />        DMAC_RESERVED<br />        INGRESS_STP_FILTER<br />        DIP_LOOPBACK<br />        L2_LOOPBACK_FILTER<br />        VLAN_TAG_NOT_ALLOWED<br />        SIP_LOOPBACK<br />        UNRESOLVED_NEXT_HOP<br />        TTL<br />        SIP_BC<br />        SMAC_EQUALS_DMAC<br />        UC_DIP_MC_DMAC<br />        EXCEEDS_L3_MTU<br />        L3_LOOPBACK_FILTER<br />        SIP_UNSPECIFIED<br />        NON_ROUTABLE<br />        BLACKHOLE_ROUTE<br />        NO_L3_HEADER<br />        IP_HEADER_ERROR<br />        SIP_MC<br />        SIP_CLASS_E</pre> |

| show dropcounters configuration | Description |
| --------------------------- | ----------- |
| show dropcounters configuration | Shows the current drop counter configuration. |
| Example | <pre># show dropcounters configuration<br />Counter    Alias      Group    Type                  Reasons    Description<br />---------  ---------  -------  --------------------  ---------  -------------<br />COUNTER_1  COUNTER_1  N/A      SWITCH_INGRESS_DROPS  L2_ANY     N/A<br />                                                     L3_ANY</pre> |

| show dropcounters counts | Description |
| --------------------------- | ----------- |
| show dropcounters counts | Shows drop counts. |
| Example | <pre># show dropcounters counts<br />      IFACE    STATE    RX_ERR    RX_DROPS    TX_ERR    TX_DROPS<br />-----------  -------  --------  ----------  --------  ----------<br />  Ethernet0        U     80004           0         0           0<br />  Ethernet1        D         0           0         0           0<br />  Ethernet2        D         0           0         0           0<br />  Ethernet3        D         0           0         0           0<br />……………………<br /><br />           DEVICE    COUNTER_1<br />-----------------  -----------<br />r-qa-sw-eth-20123            0</pre> |

## Limitations

- Illegal drop counters and What Just Happened counters are mutually exclusive, thus they cannot be used simultaneously
- The total available amount of drop counters is lower than the provided by the “show dropcounters capabilities” command due to a complex internal logic
- Particular drop reason can be used only once in configuration (multiple counters cannot share the same drop reason)
- On the L2_ANY (include all L2 drop reasons) and L3_ANY (include all L3 drop reasons) reasons apply the same restriction as described above (“particular drop reason can be used only once in configuration”)
- All Mellanox Spectrum-based switches support the same set of drop reasons, but different number of total amount of drop counters (Mellanox Spectrum based systems support less then Mellanox Spectrum-2 bases systems)
- All Mellanox Spectrum-based switches support only one counter type: SWITCH_INGRESS_DROPS (switch level, ingress direction)
- The following drop reasons are disabled. Packets matching the following drop reasons will be forwarded, not dropped.
  - SIP_EQUAL_DIP (source ip = destination ip)
  - L3_LOOPBACK_FILTER (packet egressing on same RIF as ingressing)
- The following drop reasons require specific system configuration via developers debug utilities:
  - IRIF_DISABLED (ingress RIF is disabled)
  - ERIF_DISABLED (egress RIF is disabled)
  - BLACKHOLE_ARP (discard by ARP)
- The following drop reasons are never matched because of internal default blackhole routes for 0.0.0.0/0 and ::/0:
  - LPM4_MISS (IPv4 routing table unicast miss)
  - LPM6_MISS (IPv6 routing table unicast miss)
- The following drop reason are never matched because such traffic is trapped at the CPU:
  - UNRESOLVED_NEXT_HOP (missing ARP entries)

