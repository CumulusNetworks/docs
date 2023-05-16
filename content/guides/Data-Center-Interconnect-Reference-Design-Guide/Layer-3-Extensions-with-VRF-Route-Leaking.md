---
title: Layer 3 Extensions with VRF Route Leaking
author: Cumulus Networks
weight: 60
product: Cumulus Networks Guides
imgData: guides
---

## Configurations

### Borderleaf01

```
cumulus@borderleaf01:mgmt:~$ nv config show -o commands 
nv set evpn enable on 
nv set interface eth0 ip vrf mgmt 
nv set interface eth0 type eth 
nv set interface lo ip address 10.10.10.10/32 
nv set interface lo type loopback 
nv set interface swp1-3 type swp 
nv set nve vxlan enable on 
nv set router bgp autonomous-system 65110 
nv set router bgp enable on 
nv set router bgp router-id 10.10.10.10 
nv set router policy route-map control_t5 rule 1 action permit 
nv set router policy route-map control_t5 rule 1 match evpn-route-type ip-prefix 
nv set router policy route-map control_t5 rule 3 action deny 
nv set service lldp 
nv set system config auto-save enable on 
nv set system global anycast-id 10 
nv set system global fabric-id 10 
nv set system hostname borderleaf01 
nv set system message post-login 'DCI ref guide - Layer3 VRF stretch topology with route leaking use case' 
nv set vrf GREEN evpn enable on 
nv set vrf GREEN evpn vni 4002 
nv set vrf GREEN router bgp address-family ipv4-unicast aggregate-route 192.168.1.0/24 
nv set vrf GREEN router bgp address-family ipv4-unicast aggregate-route 192.168.10.0/24 
nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
nv set vrf GREEN router bgp autonomous-system 65110 
nv set vrf GREEN router bgp enable on 
nv set vrf GREEN router bgp route-import from-evpn route-target 65210:5001 
nv set vrf GREEN router bgp route-import from-evpn route-target 65210:5002 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4001 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4002 
nv set vrf GREEN router bgp router-id 10.10.10.10 
nv set vrf RED evpn enable on 
nv set vrf RED evpn vni 4001 
nv set vrf RED router bgp address-family ipv4-unicast aggregate-route 192.168.2.0/24 
nv set vrf RED router bgp address-family ipv4-unicast aggregate-route 192.168.20.0/24 
nv set vrf RED router bgp address-family ipv4-unicast enable on 
nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
nv set vrf RED router bgp address-family ipv4-unicast route-import 
nv set vrf RED router bgp autonomous-system 65110 
nv set vrf RED router bgp enable on 
nv set vrf RED router bgp route-import from-evpn route-target 65210:5001 
nv set vrf RED router bgp route-import from-evpn route-target 65210:5002 
nv set vrf RED router bgp route-import from-evpn route-target ANY:4001 
nv set vrf RED router bgp route-import from-evpn route-target ANY:4002 
nv set vrf RED router bgp router-id 10.10.10.10 
nv set vrf default router bgp address-family ipv4-unicast enable on 
nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.10/32 
nv set vrf default router bgp address-family l2vpn-evpn enable on 
nv set vrf default router bgp enable on 
nv set vrf default router bgp neighbor swp1 peer-group underlay 
nv set vrf default router bgp neighbor swp1 type unnumbered 
nv set vrf default router bgp neighbor swp2 peer-group underlay 
nv set vrf default router bgp neighbor swp2 type unnumbered 
nv set vrf default router bgp neighbor swp3 peer-group dci_group1 
nv set vrf default router bgp neighbor swp3 type unnumbered 
nv set vrf default router bgp peer-group dci_group1 address-family ipv4-unicast enable on 
nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn enable on 
nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn policy outbound route-map control_t5 
nv set vrf default router bgp peer-group dci_group1 remote-as external 
nv set vrf default router bgp peer-group underlay address-family ipv4-unicast 
nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
nv set vrf default router bgp peer-group underlay remote-as external 
```

### Borderleaf04

```
cumulus@borderleaf04:mgmt:~$ nv config show -o commands 
nv set evpn enable on 
nv set interface eth0 ip vrf mgmt 
nv set interface eth0 type eth 
nv set interface lo ip address 10.10.20.11/32 
nv set interface lo type loopback 
nv set interface swp1-3 type swp 
nv set nve vxlan enable on 
nv set router bgp autonomous-system 65210 
nv set router bgp enable on 
nv set router bgp router-id 10.10.20.11 
nv set router policy community-list 
nv set router policy route-map control_t5 rule 1 action permit 
nv set router policy route-map control_t5 rule 1 match evpn-route-type ip-prefix 
nv set router policy route-map control_t5 rule 3 action deny 
nv set service lldp 
nv set system config auto-save enable on 
nv set system global anycast-id 20 
nv set system global fabric-id 20 
nv set system hostname borderleaf04 
nv set system message post-login 'DCI ref guide - Layer3 VRF stretch topology with route leaking use case' 
nv set vrf GREEN evpn enable on 
nv set vrf GREEN evpn vni 5002 
nv set vrf GREEN router bgp address-family ipv4-unicast aggregate-route 192.168.10.0/24 
nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
nv set vrf GREEN router bgp autonomous-system 65210 
nv set vrf GREEN router bgp enable on 
nv set vrf GREEN router bgp route-import from-evpn route-target 65110:4001 
nv set vrf GREEN router bgp route-import from-evpn route-target 65110:4002 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5001 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5002 
nv set vrf GREEN router bgp router-id 10.10.20.11 
nv set vrf RED evpn enable on 
nv set vrf RED evpn vni 5001 
nv set vrf RED router bgp address-family ipv4-unicast aggregate-route 192.168.20.0/24 
nv set vrf RED router bgp address-family ipv4-unicast enable on 
nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
nv set vrf RED router bgp autonomous-system 65210 
nv set vrf RED router bgp enable on 
nv set vrf RED router bgp route-import from-evpn route-target 65110:4001 
nv set vrf RED router bgp route-import from-evpn route-target 65110:4002 
nv set vrf RED router bgp route-import from-evpn route-target ANY:5001 
nv set vrf RED router bgp route-import from-evpn route-target ANY:5002 
nv set vrf RED router bgp router-id 10.10.20.11 
nv set vrf RED router static 
nv set vrf default router bgp address-family ipv4-unicast enable on 
nv set vrf default router bgp address-family ipv4-unicast network 10.10.20.11/32 
nv set vrf default router bgp address-family l2vpn-evpn enable on 
nv set vrf default router bgp enable on 
nv set vrf default router bgp neighbor swp1 peer-group underlay 
nv set vrf default router bgp neighbor swp1 type unnumbered 
nv set vrf default router bgp neighbor swp2 peer-group underlay 
nv set vrf default router bgp neighbor swp2 type unnumbered 
nv set vrf default router bgp neighbor swp3 peer-group dci_group1 
nv set vrf default router bgp neighbor swp3 type unnumbered 
nv set vrf default router bgp peer-group dci_group1 address-family ipv4-unicast enable on 
nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn enable on 
nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn policy outbound route-map control_t5 
nv set vrf default router bgp peer-group dci_group1 remote-as external 
nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
nv set vrf default router bgp peer-group underlay remote-as external 
```