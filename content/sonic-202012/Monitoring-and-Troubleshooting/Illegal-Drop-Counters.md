---
title: Illegal Drop Counters
author: NVIDIA
weight: 670
product: SONiC
version: 202012
siteSlug: sonic
---

Illegal drop counters provide better packet drop visibility in SONiC. They are a mechanism for counting packet drops that occur due to different reasons. Counters might drop based on one of the following scenarios:

- drop reason – a condition which led to switch pipeline “drop” decision
- drop reason family – group of drop reasons belonging to a pipeline stage (L2, L3, TUNNEL, ACL)
- drop counter – a user-created counter which can be associated with one or several drop reason
- drop counter type – ingress/egress direction for switch/port level drops

Illegal drop counters are included in the base SONiC image, so there is nothing to install.

## Supported Drop Reasons

THe layer 2 drop family includes the following drop reasons:

| Drop Reason | Description |
| ----------- | ----------- |
| SMAC_MULTICAST | Source MAC is multicast |
| SMAC_EQUALS_DMAC | Source MAC equals destination MAC |
| DMAC_RESERVED | Destination MAC is reserved (destination MAC=01-80-C2-00-00-0x) |
| VLAN_TAG_NOT_ALLOWED | VLAN tag not allowed (frame is tagged when port is dropping tagged, or is untagged when dropping untagged) |
| INGRESS_VLAN_FILTER | Ingress VLAN filter (incoming frames are tagged with a VLAN that is not configured on the ingress bridge port) |
| INGRESS_STP_FILTER | Ingress STP filter |
| FDB_UC_DISCARD | Unicast FDB table action discard |
| FDB_MC_DISCARD | Multicast FDB table empty TX list |
| L2_LOOPBACK_FILTER | Port L2 loopback filter (packet egressing and ingressing on the same port and VLAN) |
| L2_ANY | Any L2 pipeline drop (all L2 drop reasons together) |

The layer 3 family includes the following drop reasons:

| Drop Reason | Description |
| ----------- | ----------- |
| EXCEEDS_L3_MTU | Packet size is larger than the L3 (router interface) MTU |
| TTL | TTL expired |
| L3_LOOPBACK_FILTER | RIF L3 loopback filter (packet ingressing and egressing on the same RIF) |
| NON_ROUTABLE | Non-routable packet (IGMP v1 v2 v3 membership query, IGMP v1 membership report, IGMP v2 membership report, IGMP v2 leave group, IGMP v3 membership report) |
| NO_L3_HEADER | Destination MAC is the router MAC; however, packet is not routable (isn't IP or MPLS) |
| IP_HEADER_ERROR | IP header error (due to header checksum, bad IP version or IPv4 IHL too short) |
| UC_DIP_MC_DMAC | Unicast destination IP with non-unicast (multicast or broadcast) destination MAC |
| DIP_LOOPBACK | Destination IP is loopback address (for IPv4: destination IP=127.0.0.0/8, for IPv6: destination IP=::1/128 **or** destination IP=0:0:0:0:0:ffff:7f00:0/104) |
| SIP_LOOPBACK | Source IP is loopback address (for IPv4: source IP=127.0.0.0/8, for IPv6: source IP=::1/128) |
| SIP_MC | Source IP is multicast address (for IPv4: source IP=224.0.0.0/4, for IPv6: source IP=FF00::/8) |
| SIP_CLASS_E | Source IP is in class E (IPv4 AND Source IP=240.0.0.0/4 AND Source IP!=255.255.255.255) |
| SIP_UNSPECIFIED | Source IP unspecified (for IPv4: source IP=0.0.0.0/32, for IPv6: source IP=::0) |
| MC_DMAC_MISMATCH | Destination IP is multicast but destination MAC isn't (destination IP is multicast **and** for IPv4: destination MAC!={01-00-5E-0 (25 bits), dip[22:0]}, for IPv6: destination MAC!={33-33, DIP[31:0]}) |
| SIP_EQUALS_DIP | Source IP equals destination IP |
| SIP_BC | IPv4 source IP is limited broadcast (source IP=255.255.255.255) |
| DIP_LOCAL | IPv4 destination IP is local network (destination IP=0.0.0.0/8) |
| DIP_LINK_LOCAL | IPv4 unicast destination IP is link local (destination IP=169.254.0.0/16) |
| SIP_LINK_LOCAL | IPv4 source IP is link local (source IP=169.254.0.0/16) |
| IPV6_MC_SCOPE0 | IPv6 destination in multicast scope 0 reserved (destination IP=ff:x0:/16) |
| IPV6_MC_SCOPE1 | IPv6 destination in multicast scope 1 interface-local (destination IP=ff:x1:/16) |
| IRIF_DISABLED | Ingress RIF is disabled |
| ERIF_DISABLED | Egress RIF is disabled |
| LPM4_MISS | IPv4 routing table (LPM) unicast miss |
| LPM6_MISS | IPv6 routing table (LPM) unicast miss |
| BLACKHOLE_ROUTE | Black hole route (discard by route entry) |
| BLACKHOLE_ARP | Black hole ARP/neighbor (discard by ARP or neighbor entries) |
| UNRESOLVED_NEXT_HOP | Unresolved next hop (missing ARP entry) |
| L3_ANY | Any L3 pipeline drop (all L3 drop reasons together) |

The tunnel drop family includes:

| Drop Reason | Description |
| ----------- | ----------- |
| DECAP_ERROR | Packet decapsulation failed (need to decapsulate too many bytes, remaining headers are too short) |

The ACL drop family includes:

| Drop Reason | Description |
| ----------- | ----------- |
| ACL_ANY | Packet is dropped due to configured ACL rules, all stages/bind points combinations |

## Configuration Commands

| config dropcounters install | Description |
| --------------------------- | ----------- |
| config dropcounters install [OPTIONS] COUNTER_NAME COUNTER_TYPE REASONS | Installs a new drop counter. |
| Example | <pre>admin@switch:~$ sudo config dropcounters install COUNTER_1 SWITCH_INGRESS_DROPS L2_ANY</pre> |

| config dropcounters add-reasons | Description |
| --------------------------- | ----------- |
| config dropcounters add-reasons [OPTIONS] COUNTER_NAME REASONS | Adds reasons to an existing drop counter. |
| Example | <pre>admin@switch:~$ sudo config dropcounters add-reasons COUNTER_1 L3_ANY</pre> |

| config dropcounters remove-reasons | Description |
| --------------------------- | ----------- |
| config dropcounters remove-reasons [OPTIONS] COUNTER_NAME REASONS | Remove reasons from an existing drop counter |
| Example | <pre>admin@switch:~$ sudo config dropcounters remove-reasons COUNTER_1 L2_ANY</pre> |

| config dropcounters delete | Description |
| --------------------------- | ----------- |
| config dropcounters delete [OPTIONS] COUNTER_NAME | Deletes an existing drop counter |
| Example | <pre>admin@switch:~$ sudo config dropcounters delete COUNTER_1</pre> |

| show dropcounters capabilities | Description |
| --------------------------- | ----------- |
| show dropcounters capabilities | Displays a total allowed number of drop counters and a list of the supported drop reasons for a particular counter type. |
| Example | <pre>admin@switch:~$ show dropcounters capabilities<br />Counter Type            Total<br />--------------------  -------<br />SWITCH_EGRESS_DROPS        31<br />SWITCH_INGRESS_DROPS       31<br /><br />SWITCH_INGRESS_DROPS<br />        ACL_ANY<br />        DECAP_ERROR<br />        BLACKHOLE_ARP<br />        LPM6_MISS<br />        ERIF_DISABLED<br />        IPV6_MC_SCOPE1<br />        IPV6_MC_SCOPE0<br />        SIP_LINK_LOCAL<br />        DIP_LINK_LOCAL<br />        DIP_LOCAL<br />        MC_DMAC_MISMATCH<br />        FDB_MC_DISCARD<br />        L3_ANY<br />        INGRESS_VLAN_FILTER<br />        LPM4_MISS<br />        L2_ANY<br />        IRIF_DISABLED<br />        SMAC_MULTICAST<br />        FDB_UC_DISCARD<br />        DMAC_RESERVED<br />        INGRESS_STP_FILTER<br />        DIP_LOOPBACK<br />        L2_LOOPBACK_FILTER<br />        VLAN_TAG_NOT_ALLOWED<br />        SIP_LOOPBACK<br />        UNRESOLVED_NEXT_HOP<br />        TTL<br />        SIP_BC<br />        SMAC_EQUALS_DMAC<br />        UC_DIP_MC_DMAC<br />        EXCEEDS_L3_MTU<br />        L3_LOOPBACK_FILTER<br />        SIP_UNSPECIFIED<br />        NON_ROUTABLE<br />        BLACKHOLE_ROUTE<br />        NO_L3_HEADER<br />        IP_HEADER_ERROR<br />        SIP_MC<br />        SIP_CLASS_E</pre> |

| show dropcounters configuration | Description |
| --------------------------- | ----------- |
| show dropcounters configuration | Shows the current drop counter configuration. |
| Example | <pre>admin@switch:~$ show dropcounters configuration<br />Counter    Alias      Group    Type                  Reasons    Description<br />---------  ---------  -------  --------------------  ---------  -------------<br />COUNTER_1  COUNTER_1  N/A      SWITCH_INGRESS_DROPS  L2_ANY     N/A<br />                                                     L3_ANY</pre> |

| show dropcounters counts | Description |
| --------------------------- | ----------- |
| show dropcounters counts | Shows drop counts. |
| Example | <pre>admin@switch:~$ show dropcounters counts<br />      IFACE    STATE    RX_ERR    RX_DROPS    TX_ERR    TX_DROPS<br />-----------  -------  --------  ----------  --------  ----------<br />  Ethernet0        U     80004           0         0           0<br />  Ethernet1        D         0           0         0           0<br />  Ethernet2        D         0           0         0           0<br />  Ethernet3        D         0           0         0           0<br />……………………<br /><br />           DEVICE    COUNTER_1<br />-----------------  -----------<br />r-qa-sw-eth-20123            0</pre> |

## Limitations

- Illegal drop counters and {{<link url="What-Just-Happened">}} counters are mutually exclusive; they cannot be used simultaneously.
- The total available amount of drop counters is actually lower than what is output from `show dropcounters capabilities` due to a complex internal logic.
- An individual drop reason can be used only once in a configuration; multiple counters cannot share the same drop reason.
- Individual L2_ANY (including all L2 drop reasons) and L3_ANY (including all L3 drop reasons) reasons can be used only once in a configuration.
- All NVIDIA Spectrum-based switches support the same set of drop reasons, but later Spectrum models support more drop counters (Spectrum 1-based systems support fewer drop reasons than NVIDIA Spectrum 2-based systems, for example).
- All Spectrum-based switches support only one counter type: SWITCH_INGRESS_DROPS (switch level, ingress direction).
- The following drop reasons are disabled. Packets matching the following drop reasons are forwarded, not dropped:
  - SIP_EQUAL_DIP (source ip = destination ip)
  - L3_LOOPBACK_FILTER (packet egressing on same RIF as ingressing)
- The following drop reasons require specific system configuration via developers debug utilities:
  - IRIF_DISABLED (ingress RIF is disabled)
  - ERIF_DISABLED (egress RIF is disabled)
  - BLACKHOLE_ARP (discard by ARP)
- The following drop reasons are never matched because of internal default blackhole routes for 0.0.0.0/0 and ::/0:
  - LPM4_MISS (IPv4 routing table unicast miss)
  - LPM6_MISS (IPv6 routing table unicast miss)
- The following drop reason is never matched because such traffic is trapped at the CPU:
  - UNRESOLVED_NEXT_HOP (missing ARP entries)
