---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.1 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.1, see the {{<link title="Cumulus Linux 5.1 Release Notes" text="Cumulus Linux 5.1 Release Notes">}}.
- To upgrade to Cumulus Linux 5.1, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.1.0
<!-- vale on -->
Cumulus Linux 5.1.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN4410 (100G and 400G Spectrum-3) now generally available
- NVIDIA SN4700 (Spectrum-3-A1) now generally available
- NVIDIA SN4600C (100G Spectrum-3-A1) now generally available

### New Features and Enhancements

- {{<link url="GRE-Tunneling" text="GRE tunneling">}}
- {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#adaptive-routing" text="Adaptive routing with RoCEv2">}}
- {{<link url="Link-Layer-Discovery-Protocol/#lldp-dcbx-tlvs" text="LLDP DCBX TLVs">}}
- {{<link url="In-Service-System-Upgrade-ISSU" text="Warmboot on bonds">}}
- {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#peer-link-consistency-check" text="MLAG peer link consistency check">}}
- {{<link url="Precision-Time-Protocol-PTP" text="PTP on bonds">}}
- {{<link title="Spanning Tree and Rapid Spanning Tree - STP/#bpdu-guard" text="BPDU guard protodown state and reason">}}
- {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#gtp-hashing" text="TEID-based ECMP hashing">}} and {{<link url="Bonding-Link-Aggregation/#gtp-hashing" text="TEID-based bond hashing">}} available for early access (Linux commands only).
- The {{<link title="What Just Happened (WJH)" text="WJH service">}} is now enabled by default.
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - {{<link url="Neighbor-Discovery-ND" text="IPv6 ND configuration options">}}
  - {{<link url="NVUE-Snippets/#flexible-snippets" text="Flexible snippets">}}
  - {{<link url="VXLAN-Devices/#automatic-vlan-to-vni-mapping" text="Automatic VLAN to VNI mapping">}}
  - {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP/#change-the-vrr-mac-address" text="Fabric-wide MAC address configuration">}}
  - {{<link url="Route-Filtering-and-Redistribution/#apply-a-route-map" text="FIB filter configuration">}}
  - {{< expand "New NVUE commands" >}}
  
```
nv show router pbr map <pbr-map-id> rule <rule-id> action nexthop-group
nv show router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id>
nv show router adaptive-routing
nv show mlag lacp-conflict
nv show mlag consistency-checker
nv show mlag consistency-checker global
nv show mlag backup <backup-ip>
nv show interface <interface-id> router pbr map
nv show interface <interface-id> router pbr map <pbr-map-id>
nv show interface <interface-id> router adaptive-routing
nv show interface <interface-id> bond mlag lacp-conflict
nv show interface <interface-id> bond mlag consistency-checker
nv show interface <interface-id> ip neighbor-discovery
nv show interface <interface-id> ip neighbor-discovery rdnss
nv show interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>
nv show interface <interface-id> ip neighbor-discovery prefix
nv show interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>
nv show interface <interface-id> ip neighbor-discovery dnssl
nv show interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>
nv show interface <interface-id> ip neighbor-discovery router-advertisement
nv show interface <interface-id> ip neighbor-discovery home-agent
nv show interface <interface-id> lldp neighbor
nv show interface <interface-id> lldp neighbor <neighbor-id>
nv show interface <interface-id> lldp neighbor <neighbor-id> bridge
nv show interface <interface-id> lldp neighbor <neighbor-id> bridge vlan
nv show interface <interface-id> lldp neighbor <neighbor-id> bridge vlan <vid>
nv show interface <interface-id> tunnel
nv show vrf <vrf-id> router rib <afi> protocol
nv show vrf <vrf-id> router rib <afi> protocol <import-protocol-id>
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> entry-index <entry-index> via <via-id> label
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart
nv set router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id>
nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-prefer-global (on|off)
nv set router adaptive-routing
nv set router adaptive-routing enable (on|off)
nv set bridge domain <domain-id> vlan-vni-offset 0-16773120
nv set mlag lacp-conflict
nv set mlag backup <backup-ip>
nv set mlag backup <backup-ip> vrf <vrf-name>
nv set qos roce cable-length 1-100000
nv set interface <interface-id> router pbr map <pbr-map-id>
nv set interface <interface-id> router adaptive-routing
nv set interface <interface-id> router adaptive-routing enable (on|off)
nv set interface <interface-id> router adaptive-routing link-utilization-threshold 1-100
nv set interface <interface-id> bond mlag lacp-conflict
nv set interface <interface-id> ip neighbor-discovery
nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>
nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> lifetime (0-4294967295|infinite)
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime 0-4294967295
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime 0-4294967295
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> off-link (on|off)
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> autoconfig (on|off)
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> router-address (on|off)
nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>
nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> lifetime (0-4294967295|infinite)
nv set interface <interface-id> ip neighbor-discovery router-advertisement
nv set interface <interface-id> ip neighbor-discovery router-advertisement enable (on|off)
nv set interface <interface-id> ip neighbor-discovery router-advertisement interval 70-1800000
nv set interface <interface-id> ip neighbor-discovery router-advertisement interval-option (on|off)
nv set interface <interface-id> ip neighbor-discovery router-advertisement fast-retransmit (on|off)
nv set interface <interface-id> ip neighbor-discovery router-advertisement lifetime 0-9000
nv set interface <interface-id> ip neighbor-discovery router-advertisement reachable-time 0-3600000
nv set interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time 0-4294967295
nv set interface <interface-id> ip neighbor-discovery router-advertisement managed-config (on|off)
nv set interface <interface-id> ip neighbor-discovery router-advertisement other-config (on|off)
nv set interface <interface-id> ip neighbor-discovery router-advertisement hop-limit 0-255
nv set interface <interface-id> ip neighbor-discovery router-advertisement router-preference (high|medium|low)
nv set interface <interface-id> ip neighbor-discovery home-agent
nv set interface <interface-id> ip neighbor-discovery home-agent lifetime 0-65520
nv set interface <interface-id> ip neighbor-discovery home-agent preference 0-65535
nv set interface <interface-id> ip neighbor-discovery enable (on|off)
nv set interface <interface-id> ip neighbor-discovery mtu 1-65535
nv set interface <interface-id> lldp
nv set interface <interface-id> lldp dcbx-pfc-tlv (on|off)
nv set interface <interface-id> lldp dcbx-ets-config-tlv (on|off)
nv set interface <interface-id> lldp dcbx-ets-recomm-tlv (on|off)
nv set interface <interface-id> tunnel
nv set interface <interface-id> tunnel source-ip <ipv4>
nv set interface <interface-id> tunnel dest-ip <ipv4>
nv set interface <interface-id> tunnel ttl 1-255
nv set interface <interface-id> tunnel mode gre
nv set interface <interface-id> tunnel interface <interface-name>
nv set interface <interface-id> type (swp|eth|bond|loopback|svi|sub|peerlink|tunnel)
nv set system global fabric-mac (none|<mac>)
nv set system global fabric-id 1-255
nv set vrf <vrf-id> router rib <afi>
nv set vrf <vrf-id> router rib <afi> protocol <import-protocol-id>
nv set vrf <vrf-id> router rib <afi> protocol <import-protocol-id> fib-filter (none|<instance-name>)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities source-address (<interface-name>|<ipv4>|<ipv6>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart mode (auto|off|helper-only|full)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait 1-4294967295
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait 1-4294967295
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> description none
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities source-address (<interface-name>|<ipv4>|<ipv6>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart mode (auto|off|helper-only|full)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait 1-4294967295
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait 1-4294967295
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> description none
nv set vrf <vrf-id> router bgp dynamic-peer-limit 1-5000
nv unset router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id>
nv unset router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-prefer-global
nv unset router adaptive-routing
nv unset router adaptive-routing enable
nv unset bridge domain <domain-id> vlan-vni-offset
nv unset mlag lacp-conflict
nv unset mlag backup <backup-ip>
nv unset mlag backup <backup-ip> vrf
nv unset interface <interface-id> router pbr map <pbr-map-id>
nv unset interface <interface-id> router adaptive-routing
nv unset interface <interface-id> router adaptive-routing enable
nv unset interface <interface-id> router adaptive-routing link-utilization-threshold
nv unset interface <interface-id> bond mlag lacp-conflict
nv unset interface <interface-id> ip neighbor-discovery
nv unset interface <interface-id> ip neighbor-discovery rdnss
nv unset interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>
nv unset interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> lifetime
nv unset interface <interface-id> ip neighbor-discovery prefix
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> off-link
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> autoconfig
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> router-address
nv unset interface <interface-id> ip neighbor-discovery dnssl
nv unset interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>
nv unset interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> lifetime
nv unset interface <interface-id> ip neighbor-discovery router-advertisement
nv unset interface <interface-id> ip neighbor-discovery router-advertisement enable
nv unset interface <interface-id> ip neighbor-discovery router-advertisement interval
nv unset interface <interface-id> ip neighbor-discovery router-advertisement interval-option
nv unset interface <interface-id> ip neighbor-discovery router-advertisement fast-retransmit
nv unset interface <interface-id> ip neighbor-discovery router-advertisement lifetime
nv unset interface <interface-id> ip neighbor-discovery router-advertisement reachable-time
nv unset interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time
nv unset interface <interface-id> ip neighbor-discovery router-advertisement managed-config
nv unset interface <interface-id> ip neighbor-discovery router-advertisement other-config
nv unset interface <interface-id> ip neighbor-discovery router-advertisement hop-limit
nv unset interface <interface-id> ip neighbor-discovery router-advertisement router-preference
nv unset interface <interface-id> ip neighbor-discovery home-agent
nv unset interface <interface-id> ip neighbor-discovery home-agent lifetime
nv unset interface <interface-id> ip neighbor-discovery home-agent preference
nv unset interface <interface-id> ip neighbor-discovery enable
nv unset interface <interface-id> ip neighbor-discovery mtu
nv unset interface <interface-id> lldp
nv unset interface <interface-id> lldp dcbx-pfc-tlv
nv unset interface <interface-id> lldp dcbx-ets-config-tlv
nv unset interface <interface-id> lldp dcbx-ets-recomm-tlv
nv unset interface <interface-id> tunnel
nv unset interface <interface-id> tunnel source-ip
nv unset interface <interface-id> tunnel dest-ip
nv unset interface <interface-id> tunnel ttl
nv unset interface <interface-id> tunnel mode
nv unset interface <interface-id> tunnel interface
nv unset system global fabric-mac
nv unset system global fabric-id
nv unset vrf <vrf-id> router rib
nv unset vrf <vrf-id> router rib <afi>
nv unset vrf <vrf-id> router rib <afi> protocol
nv unset vrf <vrf-id> router rib <afi> protocol <import-protocol-id>
nv unset vrf <vrf-id> router rib <afi> protocol <import-protocol-id> fib-filter
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities source-address
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart mode
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> description
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities source-address
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart mode
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> description
nv unset vrf <vrf-id> router bgp dynamic-peer-limit
```
{{< /expand >}}

{{%notice info%}}
Cumulus Linux 5.1 includes the NVUE object model. After you upgrade to Cumulus Linux 5.1, running NVUE configuration commands replaces the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf` and removes any configuration you add manually or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVIDIA-User-Experience-NVUE/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
