---
title: Layer 3 Extensions with VRF Route Leaking
author: Cumulus Networks
weight: 60
product: Cumulus Networks Guides
imgData: guides
---
<style>
  .scroll{
    height: 500px;
    overflow-y: auto;
  }
</style>


## Configurations

VRF route leaking is commonly used in enterprise and service provider environments ever since IP based VPN services were introduced. This is the same for EVPN- based Ethernet VPNs. We use VRFs to isolate routing tables and create multi-tenancy within our WAN and datacenters. However, routing across VRFs is often required and for the scenarios where external routing in between VRF’s is not possible nor economical, route leaking is the only tool. Regarding with route-leaking in a data center fabric one of the first and most critical questions to be answered is that where in the network route leaking needs to happen.  

If we want a common denominator that will  keep a summary of each POD and also face with the external environments, interconnect PODs and DC locations, we could narrow down our selection for such location in the network, border leaf. Usually border leaf nodes are dedicated leaf nodes for firewalls, load balancers, intrusion detection systems (IDS), SSL-offload devices, and WEB application firewalls (WAF), also where datacenter interconnection takes place. If we have any of these services and an interconnect, the border leaf is the point which has visibility to each tenant in the DC. Such network and security services are typically used across VRFs or come in handy when they have a direct connection to each tenant network. That is why VRF is a practical technology. Therefore, performing VRF route-leaking on regular leaf nodes blinds those services because they’re attached to a service leaf or a border leaf separate from a regular leaf. That’s one of the reasons route leaking on a border leaf node tends to be a more desirable choice. Another reason is that one might prefer having a deterministic set of next-hops and number of hops to reach such cross-connection point. Again, in this use case border leaf nodes are good choices for route leaking operations. 

{{<img src= "/images/guides/route-leaking.png">}}

However, each network is unique and has its own business and technical requirements. There might be use cases where route leaking would be the best on each individual leaf. Each leaf can perform the leaking operation, so depending on the complexity and scale of the operation, this might be the desired solution. Moreover, leaking can be partially performed on border leaf nodes and partially on regular leaf equipment.  

### Borderleaf01

<div class=scroll>

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
</div>

### Borderleaf04

<div class=scroll>

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

</div>

`nv set vrf <vrf_name> router bgp route-import from-evpn route-target <asn:vni>`

The route-import statement above is used in both RED and GREEN VRFs to mutually leak (inject) EVPN Type-5 routes into their respective routing tables. There is direct DCI connectivity between borderleaf01 and borderleaf04.You must enable the l2vpn address family for the DCI underlay session to exchange EVPN routes. 

To avoid any Layer-2 stretch with EVPN Type-2 and Type-3 routes, filter any unwanted EVPN route type with a simple filter applied to the BGP peer-group outbound direction: 

```
nv set router policy route-map control_t5 rule 1 action permit 
nv set router policy route-map control_t5 rule 1 match evpn-route-type ip-prefix 
nv set router policy route-map control_t5 rule 3 action deny 
 
nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn policy outbound route-map control_t5 
```