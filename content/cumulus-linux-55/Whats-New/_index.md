---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.5 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.5, see the {{<link title="Cumulus Linux 5.5 Release Notes" text="Cumulus Linux 5.5 Release Notes">}}.
- To upgrade to Cumulus Linux 5.5, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.5.1
<!-- vale on -->
Cumulus Linux 5.5.1 provides a new SDK and firmware version, and includes a bug fix to resolve a {{<link title="Cumulus Linux 5.5 Release Notes#fixed-issues-in-551" text="link degradation issue">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.5.0
<!-- vale on -->
Cumulus Linux 5.5.0 supports new platforms, contains several new features and improvements, and provides bug fixes.

{{%notice note%}}
Early access features are now called beta features.
{{%/notice%}}

### Platforms

- NVIDIA SN3750-SX (100G Spectrum-2) continues to be in beta

{{%notice warning%}}
The NVIDIA SN3750-SX switch is available for [beta]({{<ref "/knowledge-base/Support/Support-Offerings/Early-Access-Features-Defined" >}}) and open to customer feedback. Do not use this switch in production; it is not supported through NVIDIA networking support.
{{%/notice%}}

### New Features and Enhancements

- {{<link url="Switch-Port-Attributes/#breakout-ports" text="1G support">}} for all NVIDIA Spectrum-2 and Spectrum-3 switches now generally available
- {{<link url="Precision-Time-Protocol-PTP/#ptp-profiles" text="PTP ITU-T G.8275.2 profile">}}
- {{<link url="Precision-Time-Protocol-PTP#ptp-traffic-shaping" text="PTP traffic shaping">}}
- {{<link url="EVPN-Enhancements/#configure-a-site-id-for-mlag" text="Site ID for MLAG">}}
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - {{<link url="TACACS" text="TACACS+">}} commands are now generally available
  - {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="Fast, cold, and warm">}} restart mode
  - {{<link url="VLAN-aware-Bridge-Mode#mac-address-ageing" text="MAC address aging timer">}}
  - {{<link url="Netfilter-ACLs/#control-plane-acls" text="Control plane ACLs">}}
  - New commands to {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE" text="show and clear interface counters">}}
  - New OSPF commands to {{<link url="Open-Shortest-Path-First-v2-OSPFv2/#troubleshooting" text="show interface and neighbor configuration and counters">}}, and {{<link url="Open-Shortest-Path-First-v2-OSPFv2/#clear-ospf-counters" text="clear OSPF interface counters">}}
  - New command to {{<link url="Route-Filtering-and-Redistribution/#clear-matches-against-a-route-map" text="clear matches against a route map">}}
  - New {{<link url="Troubleshooting-BGP/#clear-bgp-routes" text="BGP commands">}} to clear BGP routes
  - New commands to {{<link url="Precision-Time-Protocol-PTP/#show-ptp-counters" text="show PTP counters">}}
  - New EVPN commands to show {{<link url="EVPN-Multihoming/#troubleshooting" text="multihoming information">}}, {{<link url="Troubleshooting-EVPN/#examine-remote-router-mac-addresses" text="remote router MAC addresses">}}, {{<link url="Troubleshooting-EVPN/#examine-gateway-next-hops" text="nexthop VTEPs">}}, and {{<link url="Troubleshooting-EVPN/#show-access-vlans" text="access VLANs and their VNIs">}}
  - Updated {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#next-hop-groups" text="nv show router nexthop rib">}} and {{<link url="FRRouting/#next-hop-tracking" text="nv show vrf <vrf> router nexthop-tracking">}} commands show operational data
  - Updated {{<link url="Troubleshooting-BGP/#show-bgp-route-information" text="nv show vrf <vrf> router bgp neighbor">}} and {{<link url="Troubleshooting-BGP/#show-next-hop-information" text="nv show vrf <vrf> router bgp nexthop">}} commands show operational data
  - Support for {{<link url="Optional-BGP-Configuration/#bgp-community-lists" text="named well known BGP communities">}} `no-export`, `no-advertise`, and `additive` options

{{< expand "Changed Commands" >}}
| Previous Command | New Command |
| ---------------- | ----------- |
| `nv set service dhcp-relay6 <vrf> interface upstream <interface> address <ipv6-address>`| `nv set service dhcp-relay6 <vrf> interface upstream <interface> server-address <ipv6-address>` |
| `nv set service dhcp-relay6 <vrf> interface downstream <interface> address <ipv6-address>` | `nv set service dhcp-relay6 <vrf> interface downstream <interface> link-address <ipv6-address>` |
| `nv set service dhcp-relay <vrf> giaddress-interface`| `nv set service dhcp-relay <vrf> gateway-interface`|
| `nv show interface <interface> ptp counters` | `nv show interface <interface> counters ptp`|
| `nv show interface <interface> qos counters` | `nv show interface <interface> counters qos` |
| `nv show interface <interface> qos counters egress-queue-stats` | `nv show interface <interface> counters qos egress-queue-stats` |
| `nv show interface <interface> qos counters ingress-buffer-stats` |`nv show interface <interface> counters qos ingress-buffer-stats`|
| `nv show interface <interface> qos counters pfc-stats` | `nv show interface <interface> counters qos pfc-stats`|
| `nv show interface <interface> qos counters port-stats` |`nv show interface <interface> counters qos port-stats` |

{{< /expand >}}

{{< expand "New Commands" >}}
   {{< tabs "TabID40 ">}}
{{< tab "nv show commands ">}}

```
nv show evpn vni <vni-id> multihoming
nv show evpn vni <vni-id> multihoming esi
nv show evpn vni <vni-id> multihoming bgp-info
nv show evpn vni <vni-id> multihoming bgp-info esi
nv show evpn vni <vni-id> multihoming bgp-info esi <esi-id>
nv show evpn vni <vni-id> multihoming bgp-info esi <esi-id> remote-vtep
nv show evpn vni <vni-id> multihoming bgp-info esi <esi-id> remote-vtep <ipv4-address-id>
nv show evpn multihoming esi
nv show evpn multihoming esi <esi-id>
nv show evpn multihoming esi <esi-id> remote-vtep
nv show evpn multihoming esi <esi-id> remote-vtep <ipv4-address-id>
nv show evpn multihoming bgp-info
nv show evpn multihoming bgp-info esi
nv show evpn multihoming bgp-info esi <esi-id>
nv show evpn multihoming bgp-info esi <esi-id> remote-vtep
nv show evpn multihoming bgp-info esi <esi-id> remote-vtep <ipv4-address-id>
nv show evpn multihoming bgp-info esi <esi-id> fragments
nv show evpn multihoming bgp-info esi <esi-id> fragments <fragment-id>
nv show evpn access-vlan-info
nv show evpn access-vlan-info vlan
nv show evpn access-vlan-info vlan <vlan-id>
nv show evpn access-vlan-info vlan <vlan-id> member-interface
nv show evpn l2-nhg
nv show evpn l2-nhg vtep-ip
nv show evpn l2-nhg vtep-ip <vtep-ip-id>
nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address-family
nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address-family <afi>
nv show interface <interface-id> counters
nv show interface <interface-id> counters errors
nv show interface <interface-id> counters drops
nv show interface <interface-id> counters pktdist
nv show interface <interface-id> counters qos
nv show interface <interface-id> counters qos port-stats
nv show interface <interface-id> counters qos egress-queue-stats
nv show interface <interface-id> counters qos ingress-buffer-stats
nv show interface <interface-id> counters qos pfc-stats
nv show interface <interface-id> counters ptp
nv show service dhcp-relay <vrf-id> gateway-interface
nv show service dhcp-relay <vrf-id> gateway-interface <interface-id>
nv show service ptp <instance-id> status
nv show system control-plane acl
nv show system control-plane acl <acl-id>
nv show system control-plane acl <acl-id> statistics
nv show system control-plane acl <acl-id> statistics <rule-id>
nv show system aaa tacacs authorization
nv show system aaa tacacs authorization <privilege-level-id>
nv show system aaa tacacs authorization <privilege-level-id>
nv show vrf <vrf-id> router nexthop-tracking <afi> ip-address
nv show vrf <vrf-id> router nexthop-tracking <afi> ip-address <nht-ip-id>
nv show vrf <vrf-id> router nexthop-tracking <afi> ip-address <nht-ip-id> resolved-via
nv show vrf <vrf-id> router nexthop-tracking <afi> ip-address <nht-ip-id> resolved-via <nht-resolved-id>
nv show vrf <vrf-id> router nexthop-tracking <afi> ip-address <nht-ip-id> protocol
nv show vrf <vrf-id> router nexthop-tracking <afi> ip-address <nht-ip-id> protocol <protocol-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-counters
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id> nexthop
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id> nexthop <nexthop-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id> peer
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id> flags
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id> bestpath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id> aspath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id> community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id> ext-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id> nexthop
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id> nexthop <nexthop-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id> peer
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id> flags
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id> bestpath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id> aspath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id> community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id> ext-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id> nexthop
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id> nexthop <nexthop-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id> peer
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id> flags
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id> bestpath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id> aspath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id> community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id> ext-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-counters
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id> nexthop
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id> nexthop <nexthop-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id> peer
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id> flags
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id> bestpath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id> aspath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id> community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id> ext-community
nv show vrf <vrf-id> router ospf interface
nv show vrf <vrf-id> router ospf interface <interface-id>
nv show vrf <vrf-id> router ospf interface <interface-id> local-ip
nv show vrf <vrf-id> router ospf interface <interface-id> local-ip <ipv4-address-id>
nv show vrf <vrf-id> router ospf neighbor
nv show vrf <vrf-id> router ospf neighbor <ipv4-nbr-id>
nv show vrf <vrf-id> router ospf neighbor <ipv4-nbr-id> interface
nv show vrf <vrf-id> router ospf neighbor <ipv4-nbr-id> interface <interface-id>
nv show vrf <vrf-id> router ospf neighbor <ipv4-nbr-id> interface <interface-id> local-ip
nv show vrf <vrf-id> router ospf neighbor <ipv4-nbr-id> interface <interface-id> local-ip <ipv4-address-id>
```

{{< /tab >}}
{{< tab "nv set commands ">}}

```
nv set router policy route-map <route-map-id> rule <rule-id> match ext-community-list
nv set bridge domain <domain-id> ageing
nv set interface <interface-id> ptp local-priority
nv set service dhcp-relay <vrf-id> gateway-interface <interface-id>
nv set service dhcp-relay <vrf-id> gateway-interface <interface-id> address
nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> server-address
nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> link-address
nv set service lldp lldp-med-inventory-tlv
nv set system reboot
nv set system reboot mode
nv set system control-plane acl <acl-id>
nv set system aaa tacacs server <priority-id> prefer-ip-version
nv set system aaa tacacs authorization <privilege-level-id>
nv set system aaa tacacs authorization <privilege-level-id> command
nv set system aaa tacacs authorization <privilege-level-id> role
nv set vrf <vrf-id> router bgp address-family ipv4-unicast in
nv set vrf <vrf-id> router bgp address-family ipv4-unicast out
nv set vrf <vrf-id> router bgp address-family ipv4-unicast soft
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn in
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn out
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn soft
nv set vrf <vrf-id> router bgp address-family ipv6-unicast in
nv set vrf <vrf-id> router bgp address-family ipv6-unicast out
nv set vrf <vrf-id> router bgp address-family ipv6-unicast soft
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast in
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast out
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast soft
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound maximum
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast in
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast out
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast soft
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn in
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn out
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn soft
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> in
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> out
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> soft
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast in
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast out
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast soft
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast in
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast out
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast soft
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn in
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn out
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn soft
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> in
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> out
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> soft
nv set acl <acl-id> rule <rule-id> match ip ttl
```

{{< /tab >}}
{{< tab "nv unset commands ">}}

```
nv unset router policy route-map <route-map-id> rule <rule-id> match ext-community-list
nv unset bridge domain <domain-id> ageing
nv unset interface <interface-id> ptp local-priority
nv unset service dhcp-relay6 <vrf-id> interface upstream <interface-id> server-address
nv unset service dhcp-relay6 <vrf-id> interface downstream <interface-id> link-address
nv unset service lldp lldp-med-inventory-tlv
nv unset system reboot
nv unset system reboot mode
nv unset system control-plane acl
nv unset system control-plane acl <acl-id>
nv unset system aaa tacacs server <priority-id> prefer-ip-version
nv unset system aaa tacacs authorization
nv unset system aaa tacacs authorization <privilege-level-id>
nv unset system aaa tacacs authorization <privilege-level-id> command
nv unset system aaa tacacs authorization <privilege-level-id> role
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast in
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast out
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast soft
nv unset vrf <vrf-id> router bgp address-family l2vpn-evpn in
nv unset vrf <vrf-id> router bgp address-family l2vpn-evpn out
nv unset vrf <vrf-id> router bgp address-family l2vpn-evpn soft
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast in
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast out
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast soft
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast in
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast out
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast soft
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast in
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast out
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast soft
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn in
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn out
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn soft
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> in
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> out
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> soft
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast in
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast out
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast soft
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast in
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast out
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast soft
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn in
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn out
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn soft
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> in
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> out
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> soft
nv unset acl <acl-id> rule <rule-id> match ip ttl
```

{{< /tab >}}
{{< tab "nv action commands ">}}

```
nv action disconnect system aaa user <user-id>
nv action reboot system
nv action clear router policy route-map <route-map-id>
nv action clear interface <interface-id> counters ptp
nv action clear interface <interface-id> synce counters
nv action clear service ptp <instance-id> monitor violations log max-offset
nv action clear service ptp <instance-id> monitor violations log min-offset
nv action clear service ptp <instance-id> monitor violations log path-delay
nv action clear vrf <vrf-id> router bgp address-family ipv4-unicast in
nv action clear vrf <vrf-id> router bgp address-family ipv4-unicast out
nv action clear vrf <vrf-id> router bgp address-family ipv4-unicast soft in
nv action clear vrf <vrf-id> router bgp address-family ipv4-unicast soft out
nv action clear vrf <vrf-id> router bgp address-family l2vpn-evpn in
nv action clear vrf <vrf-id> router bgp address-family l2vpn-evpn out
nv action clear vrf <vrf-id> router bgp address-family l2vpn-evpn soft in
nv action clear vrf <vrf-id> router bgp address-family l2vpn-evpn soft out
nv action clear vrf <vrf-id> router bgp address-family ipv6-unicast in
nv action clear vrf <vrf-id> router bgp address-family ipv6-unicast out
nv action clear vrf <vrf-id> router bgp address-family ipv6-unicast soft in
nv action clear vrf <vrf-id> router bgp address-family ipv6-unicast soft out
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> in
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> out
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> soft in
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> soft out
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast in
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast out
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast soft in
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast soft out
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast in
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast out
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast soft in
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast soft out
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn in
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn out
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn soft in
nv action clear vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn soft out
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> in
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> out
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> soft in
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> soft out
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast in
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast out
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast soft in
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast soft out
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast in
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast out
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast soft in
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast soft out
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn in
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn out
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn soft in
nv action clear vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn soft out
nv action clear vrf <vrf-id> router ospf interface <interface-id>
```

{{< /tab >}}
{{< /tabs >}}

{{< /expand >}}

{{%notice info%}}
Cumulus Linux 5.5 includes the NVUE object model. After you upgrade to Cumulus Linux 5.5, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
