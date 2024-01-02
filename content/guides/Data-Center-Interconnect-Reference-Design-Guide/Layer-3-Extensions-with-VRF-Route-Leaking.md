---
title: Layer 3 Extensions with VRF Route Leaking
author: NVIDIA
weight: 60
product: Technical Guides
imgData: guides
---
<style>
  .scroll{
    height: 500px;
    overflow-y: auto;
  }
</style>
After the introduction of IP based VPN services, VRF route leaking has become more common in enterprise and service provider environments, and also in EVPN-based Ethernet VPNs. VRFs isolate routing tables, and create multi tenancy within a wide area network (WAN) and data center. However, routing across VRFs is often necessary, especially where external routing between VRFs is not possible or economical. When implementing route leaking in a data center fabric, you need to know where in the network route leaking needs to happen.  

If you want to use a common denominator that keeps a summary of each POD, and interconnects PODs and DC locations, a border leaf is a good choice. Typically, you use border leafs where the data center interconnects, such as with a firewall, load balancer, <span class="a-tooltip">[IDS](## "intrusion detection system ")</span>, SSL-offload device, or <span class="a-tooltip">[WAF](## "WEB application firewall ")</span>. If you have any of these interconnected services, the border leaf is the point that has visibility into each tenant in the DC. You typically use these network and security services across VRFs that have a direct connection to each tenant network. Therefore, performing VRF route leaking on regular leaf switches prevents those services from seeing the big picture because they attach to a service leaf or a border leaf. Using a border leaf is also also a good idea if you prefer to have a deterministic set of next hops or a number of hops that reach the cross-connection point.

{{<img src="/images/guides/route-leaking-between-vrfs.png">}}

Each network is unique and has its own business and technical requirements. You might find that route leaking is best for you on each individual leaf. Each leaf can perform the leaking operation; therefore, depending on the complexity and scale of the operation, this might be the desired solution. You can also perform route leaking partially on a border leaf and partially on a regular leaf.

## Configuration

{{<img src="/images/guides/dci-reference-topology.png">}}

The following examples show a route leaking configuration.

{{< tabs "TabID27 ">}}
{{< tab "borderleaf01 ">}}

<div class=scroll>

```
cumulus@borderleaf01:mgmt:~$ nv set evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set interface eth0 ip vrf mgmt 
cumulus@borderleaf01:mgmt:~$ nv set interface eth0 type eth 
cumulus@borderleaf01:mgmt:~$ nv set interface lo ip address 10.10.10.10/32 
cumulus@borderleaf01:mgmt:~$ nv set interface lo type loopback 
cumulus@borderleaf01:mgmt:~$ nv set interface swp1-3 type swp 
cumulus@borderleaf01:mgmt:~$ nv set nve vxlan enable on 
cumulus@borderleaf01:mgmt:~$ nv set router bgp autonomous-system 65110 
cumulus@borderleaf01:mgmt:~$ nv set router bgp enable on 
cumulus@borderleaf01:mgmt:~$ nv set router bgp router-id 10.10.10.10 
cumulus@borderleaf01:mgmt:~$ nv set router policy route-map control_t5 rule 1 action permit 
cumulus@borderleaf01:mgmt:~$ nv set router policy route-map control_t5 rule 1 match evpn-route-type ip-prefix 
cumulus@borderleaf01:mgmt:~$ nv set router policy route-map control_t5 rule 3 action deny 
cumulus@borderleaf01:mgmt:~$ nv set service lldp 
cumulus@borderleaf01:mgmt:~$ nv set system config auto-save enable on 
cumulus@borderleaf01:mgmt:~$ nv set system global anycast-id 10 
cumulus@borderleaf01:mgmt:~$ nv set system global fabric-id 10 
cumulus@borderleaf01:mgmt:~$ nv set system hostname borderleaf01 
cumulus@borderleaf01:mgmt:~$ nv set system message post-login 'DCI ref guide - Layer3 VRF stretch topology with route leaking use case' 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN evpn vni 4002 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast aggregate-route 192.168.1.0/24 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast aggregate-route 192.168.10.0/24 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp autonomous-system 65110 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target 65210:5001 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target 65210:5002 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4001 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4002 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp router-id 10.10.10.10 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED evpn vni 4001 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast aggregate-route 192.168.2.0/24 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast aggregate-route 192.168.20.0/24 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp autonomous-system 65110 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target 65210:5001 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target 65210:5002 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:4001 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:4002 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp router-id 10.10.10.10 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.10/32 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 peer-group underlay 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 type unnumbered 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 peer-group underlay 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 type unnumbered 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp3 peer-group dci_group1 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp3 type unnumbered 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family ipv4-unicast enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn policy outbound route-map control_t5 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 remote-as external 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group underlay address-family ipv4-unicast 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group underlay remote-as external 
```
</div>

{{< /tab >}}
{{< tab "borderleaf04 ">}}

<div class=scroll>

```
cumulus@borderleaf04:mgmt:~$ nv set evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set interface eth0 ip vrf mgmt 
cumulus@borderleaf04:mgmt:~$ nv set interface eth0 type eth 
cumulus@borderleaf04:mgmt:~$ nv set interface lo ip address 10.10.20.11/32 
cumulus@borderleaf04:mgmt:~$ nv set interface lo type loopback 
cumulus@borderleaf04:mgmt:~$ nv set interface swp1-3 type swp 
cumulus@borderleaf04:mgmt:~$ nv set nve vxlan enable on 
cumulus@borderleaf04:mgmt:~$ nv set router bgp autonomous-system 65210 
cumulus@borderleaf04:mgmt:~$ nv set router bgp enable on 
cumulus@borderleaf04:mgmt:~$ nv set router bgp router-id 10.10.20.11 
cumulus@borderleaf04:mgmt:~$ nv set router policy community-list 
cumulus@borderleaf04:mgmt:~$ nv set router policy route-map control_t5 rule 1 action permit 
cumulus@borderleaf04:mgmt:~$ nv set router policy route-map control_t5 rule 1 match evpn-route-type ip-prefix 
cumulus@borderleaf04:mgmt:~$ nv set router policy route-map control_t5 rule 3 action deny 
cumulus@borderleaf04:mgmt:~$ nv set service lldp 
cumulus@borderleaf04:mgmt:~$ nv set system config auto-save enable on 
cumulus@borderleaf04:mgmt:~$ nv set system global anycast-id 20 
cumulus@borderleaf04:mgmt:~$ nv set system global fabric-id 20 
cumulus@borderleaf04:mgmt:~$ nv set system hostname borderleaf04 
cumulus@borderleaf04:mgmt:~$ nv set system message post-login 'DCI ref guide - Layer3 VRF stretch topology with route leaking use case' 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN evpn vni 5002 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast aggregate-route 192.168.10.0/24 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp autonomous-system 65210 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target 65110:4001 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target 65110:4002 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5001 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5002 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp router-id 10.10.20.11 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED evpn vni 5001 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast aggregate-route 192.168.20.0/24 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp autonomous-system 65210 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target 65110:4001 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target 65110:4002 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:5001 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:5002 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp router-id 10.10.20.11 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router static 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.20.11/32 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp1 peer-group underlay 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp1 type unnumbered 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp2 peer-group underlay 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp2 type unnumbered 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp3 peer-group dci_group1 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp3 type unnumbered 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family ipv4-unicast enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn policy outbound route-map control_t5 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 remote-as external 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group underlay remote-as external 
```
</div>

{{< /tab >}}
{{< tab "leaf01 ">}}

<div class=scroll>

```
cumulus@leaf01:mgmt:~$ nv set vrf GREEN evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN evpn vni 4002 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp autonomous-system 65101 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4001 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4002 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5001 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5002 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp router-id 10.10.10.1 
cumulus@leaf01:mgmt:~$ nv set vrf RED evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED evpn vni 4001 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp autonomous-system 65101 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:4001 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:4002 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:5001 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:5002 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp router-id 10.10.10.1 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 peer-group underlay 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 type unnumbered 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 peer-group underlay 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 type unnumbered 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group underlay remote-as external 
```
</div>

{{< /tab >}}
{{< tab "leaf03 ">}}

<div class=scroll>

```
cumulus@leaf03:mgmt:~$ nv set vrf GREEN evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN evpn vni 5002 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp autonomous-system 65201 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4001 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4002 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5001 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5002 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp router-id 10.10.20.1 
cumulus@leaf03:mgmt:~$ nv set vrf RED evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED evpn vni 5001 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp autonomous-system 65201 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:4001 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:4002 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:5001 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:5002 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp router-id 10.10.20.1 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.20.1/32 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp1 peer-group underlay 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp1 type unnumbered 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp2 peer-group underlay 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp2 type unnumbered 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp peer-group underlay remote-as external 
```
</div>

{{< /tab >}}
{{< /tabs >}}

The leaf switch must also import cross site route targets that the border leafs advertise; interconnected data centers use VNIs that are different from downstream VNIs. The classical `auto-route-target` import function cannot detect these VNIs and cannot import the route targets automatically.

Both RED and GREEN VRFs include the `route-import` statement to mutually leak (inject) EVPN type-5 routes into their respective routing tables:
`nv set vrf <vrf_name> router bgp route-import from-evpn route-target <asn:vni>`

There is direct DCI connectivity between borderleaf01 and borderleaf04. You must enable the `l2vpn` address family for the DCI underlay session to exchange EVPN routes.

To avoid any layer 2 stretch with EVPN type-2 and type-3 routes, filter any unwanted EVPN route types with a simple filter applied to the BGP peer group in the outbound direction:

```
cumulus@borderleaf04:mgmt:~$ nv set router policy route-map control_t5 rule 1 action permit 
cumulus@borderleaf04:mgmt:~$ nv set router policy route-map control_t5 rule 1 match evpn-route-type ip-prefix 
cumulus@borderleaf04:mgmt:~$ nv set router policy route-map control_t5 rule 3 action deny 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn policy outbound route-map control_t5 
```

## Verify and Examine Route Leaking

To verify route targets leaked into each VRF, and to examine BGP and routing tables for each VRF, run the following commands on the border leaf switches.

{{< tabs "TabID290 ">}}
{{< tab "borderleaf01 ">}}

<div class=scroll>

```
cumulus@borderleaf01:mgmt:~$ nv show vrf RED evpn bgp-info 
                       operational        applied 
---------------------  -----------------  ------- 
local-vtep             10.10.10.10 
router-mac             44:38:39:22:dd:06 
system-ip              10.10.10.10 
system-mac             44:38:39:22:dd:06 
[export-route-target]  65110:4001 
[import-route-target]  0:4001 
[import-route-target]  0:4002 
[import-route-target]  65210:5001 
[import-route-target]  65210:5002 
```

```
cumulus@borderleaf01:mgmt:~$ nv show vrf GREEN evpn bgp-info 
                       operational        applied 
---------------------  -----------------  ------- 
local-vtep             10.10.10.10 
router-mac             44:38:39:22:dd:06 
system-ip              10.10.10.10 
system-mac             44:38:39:22:dd:06 
[export-route-target]  65110:4002 
[import-route-target]  0:4001 
[import-route-target]  0:4002 
[import-route-target]  65210:5001 
[import-route-target]  65210:5002 
```

```
cumulus@borderleaf01:mgmt:~$ net show route vrf RED 
show ip route vrf RED 
====================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 00:45:07 
B>* 192.168.1.0/24 [20/0] via 10.10.10.1, vlan220_l3 onlink, weight 1, 00:45:04 
  *                       via 10.10.10.2, vlan220_l3 onlink, weight 1, 00:45:04 
B>* 192.168.1.10/32 [20/0] via 10.10.10.1, vlan220_l3 onlink, weight 1, 00:45:04 
  *                        via 10.10.10.2, vlan220_l3 onlink, weight 1, 00:45:04 
B>* 192.168.2.0/24 [200/0] unreachable (blackhole), weight 1, 00:45:04 
B>* 192.168.2.10/32 [20/0] via 10.10.10.1, vxlan99 (vrf default) onlink, label 4002, weight 1, 00:45:04 
  *                        via 10.10.10.2, vxlan99 (vrf default) onlink, label 4002, weight 1, 00:45:04 
B>* 192.168.10.0/24 [20/0] via 10.10.20.11, vxlan99 (vrf default) onlink, label 5002, weight 1, 00:45:04 
B>* 192.168.20.0/24 [20/0] via 10.10.20.11, vxlan99 (vrf default) onlink, label 5001, weight 1, 00:45:04 

show ipv6 route vrf RED 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 00:45:07 
C>* fe80::/64 is directly connected, vlan220_l3, 00:45:07
```

```
cumulus@borderleaf01:mgmt:~$ net show route vrf GREEN 
show ip route vrf GREEN 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 00:45:12 
B>* 192.168.1.0/24 [200/0] unreachable (blackhole), weight 1, 00:45:09 
B>* 192.168.1.10/32 [20/0] via 10.10.10.1, vxlan99 (vrf default) onlink, label 4001, weight 1, 00:45:09 
  *                        via 10.10.10.2, vxlan99 (vrf default) onlink, label 4001, weight 1, 00:45:09 
B>* 192.168.2.0/24 [20/0] via 10.10.10.1, vlan370_l3 onlink, weight 1, 00:45:09 
  *                       via 10.10.10.2, vlan370_l3 onlink, weight 1, 00:45:09 
B>* 192.168.2.10/32 [20/0] via 10.10.10.1, vlan370_l3 onlink, weight 1, 00:45:09 
  *                        via 10.10.10.2, vlan370_l3 onlink, weight 1, 00:45:09 
B>* 192.168.10.0/24 [20/0] via 10.10.20.11, vxlan99 (vrf default) onlink, label 5002, weight 1, 00:45:09 
B>* 192.168.20.0/24 [20/0] via 10.10.20.11, vxlan99 (vrf default) onlink, label 5001, weight 1, 00:45:09 

show ipv6 route vrf GREEN 
========================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 00:45:12 
C>* fe80::/64 is directly connected, vlan370_l3, 00:45:12
```

```
cumulus@borderleaf01:mgmt:~$ net show bgp vrf RED 
show bgp vrf RED ipv4 unicast 
============================= 
BGP table version is 6, local router ID is 10.10.10.10, vrf id 13 
Default local pref 100, local AS 65110 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*= 192.168.1.0/24   10.10.10.2<                            0 65199 65102 ? 
*                   10.10.10.2<                            0 65199 65102 ? 
*>                  10.10.10.1<                            0 65199 65101 ? 
*                   10.10.10.1<                            0 65199 65101 ? 
*= 192.168.1.10/32  10.10.10.2<                            0 65199 65102 i 
*                   10.10.10.2<                            0 65199 65102 i 
*>                  10.10.10.1<                            0 65199 65101 i 
*                   10.10.10.1<                            0 65199 65101 i 
*> 192.168.2.0/24   0.0.0.0                            32768 i 
*                   10.10.10.2<                            0 65199 65102 ? 
*                   10.10.10.2<                            0 65199 65102 ? 
*                   10.10.10.1<                            0 65199 65101 ? 
*                   10.10.10.1<                            0 65199 65101 ? 
*= 192.168.2.10/32  10.10.10.2<                            0 65199 65102 i 
*                   10.10.10.2<                            0 65199 65102 i 
*>                  10.10.10.1<                            0 65199 65101 i 
*                   10.10.10.1<                            0 65199 65101 i 
*> 192.168.10.0/24  10.10.20.11<                           0 65210 i 
*> 192.168.20.0/24  10.10.20.11<                           0 65210 i 
 
Displayed  6 routes and 19 total paths 
 
show bgp vrf RED ipv6 unicast 
============================= 
No BGP prefixes displayed, 0 exist 
```

```
cumulus@borderleaf01:mgmt:~$ net show bgp vrf GREEN 
show bgp vrf GREEN ipv4 unicast 
=============================== 
BGP table version is 6, local router ID is 10.10.10.10, vrf id 11 
Default local pref 100, local AS 65110 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*  192.168.1.0/24   10.10.10.2<                            0 65199 65102 ? 
*>                  0.0.0.0                            32768 i 
*                   10.10.10.2<                            0 65199 65102 ? 
*                   10.10.10.1<                            0 65199 65101 ? 
*                   10.10.10.1<                            0 65199 65101 ? 
*= 192.168.1.10/32  10.10.10.2<                            0 65199 65102 i 
*                   10.10.10.2<                            0 65199 65102 i 
*>                  10.10.10.1<                            0 65199 65101 i 
*                   10.10.10.1<                            0 65199 65101 i 
*= 192.168.2.0/24   10.10.10.2<                            0 65199 65102 ? 
*                   10.10.10.2<                            0 65199 65102 ? 
*>                  10.10.10.1<                            0 65199 65101 ? 
*                   10.10.10.1<                            0 65199 65101 ? 
*= 192.168.2.10/32  10.10.10.2<                            0 65199 65102 i 
*                   10.10.10.2<                            0 65199 65102 i 
*>                  10.10.10.1<                            0 65199 65101 i 
*                   10.10.10.1<                            0 65199 65101 i 
*> 192.168.10.0/24  10.10.20.11<                           0 65210 i 
*> 192.168.20.0/24  10.10.20.11<                           0 65210 i 
 
Displayed  6 routes and 19 total paths 

show bgp vrf GREEN ipv6 unicast 
=============================== 
No BGP prefixes displayed, 0 exist 
```
</div>

{{< /tab >}}
{{< tab "borderleaf04 ">}}

<div class=scroll>

```
cumulus@borderleaf04:mgmt:~$ nv show vrf RED evpn bgp-info 
                       operational        applied 
---------------------  -----------------  ------- 
local-vtep             10.10.20.11 
router-mac             44:38:39:22:dd:09 
system-ip              10.10.20.11 
system-mac             44:38:39:22:dd:09 
[export-route-target]  65210:5001 
[import-route-target]  0:5001 
[import-route-target]  0:5002 
[import-route-target]  65110:4001 
[import-route-target]  65110:4002 
```

```
cumulus@borderleaf04:mgmt:~$ nv show vrf GREEN evpn bgp-info 
                       operational        applied 
---------------------  -----------------  ------- 
local-vtep             10.10.20.11 
router-mac             44:38:39:22:dd:09 
system-ip              10.10.20.11 
system-mac             44:38:39:22:dd:09 
[export-route-target]  65210:5002 
[import-route-target]  0:5001 
[import-route-target]  0:5002 
[import-route-target]  65110:4001 
[import-route-target]  65110:4002 
```

```
cumulus@borderleaf04:mgmt:~$ net show route vrf RED 
show ip route vrf RED 
====================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 1d03h32m 
B>* 192.168.1.0/24 [20/0] via 10.10.10.10, vxlan99 (vrf default) onlink, label 4002, weight 1, 00:41:52 
B>* 192.168.2.0/24 [20/0] via 10.10.10.10, vxlan99 (vrf default) onlink, label 4001, weight 1, 00:41:52 
B>* 192.168.10.0/24 [20/0] via 10.10.20.1, vlan220_l3 onlink, weight 1, 00:41:52 
  *                        via 10.10.20.2, vlan220_l3 onlink, weight 1, 00:41:52 
B>* 192.168.10.110/32 [20/0] via 10.10.20.1, vlan220_l3 onlink, weight 1, 00:41:52 
  *                          via 10.10.20.2, vlan220_l3 onlink, weight 1, 00:41:52 
B>* 192.168.20.0/24 [200/0] unreachable (blackhole), weight 1, 00:41:52 
B>* 192.168.20.110/32 [20/0] via 10.10.20.1, vxlan99 (vrf default) onlink, label 5002, weight 1, 00:41:52 
  *                          via 10.10.20.2, vxlan99 (vrf default) onlink, label 5002, weight 1, 00:41:52 

show ipv6 route vrf RED 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 1d03h32m 
C>* fe80::/64 is directly connected, vlan220_l3, 1d03h32m 
```

```
cumulus@borderleaf04:mgmt:~$ net show route vrf GREEN 
show ip route vrf GREEN 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 1d03h32m 
B>* 192.168.1.0/24 [20/0] via 10.10.10.10, vxlan99 (vrf default) onlink, label 4002, weight 1, 00:41:57 
B>* 192.168.2.0/24 [20/0] via 10.10.10.10, vxlan99 (vrf default) onlink, label 4001, weight 1, 00:41:57 
B>* 192.168.10.0/24 [200/0] unreachable (blackhole), weight 1, 00:41:57 
B>* 192.168.10.110/32 [20/0] via 10.10.20.1, vxlan99 (vrf default) onlink, label 5001, weight 1, 00:41:57 
  *                          via 10.10.20.2, vxlan99 (vrf default) onlink, label 5001, weight 1, 00:41:57 
B>* 192.168.20.0/24 [20/0] via 10.10.20.1, vlan370_l3 onlink, weight 1, 00:41:57 
  *                        via 10.10.20.2, vlan370_l3 onlink, weight 1, 00:41:57 
B>* 192.168.20.110/32 [20/0] via 10.10.20.1, vlan370_l3 onlink, weight 1, 00:41:57 
  *                          via 10.10.20.2, vlan370_l3 onlink, weight 1, 00:41:57 

show ipv6 route vrf GREEN 
========================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 1d03h32m 
C>* fe80::/64 is directly connected, vlan370_l3, 1d03h32m
```

``` 
cumulus@borderleaf04:mgmt:~$ net show bgp vrf RED 
show bgp vrf RED ipv4 unicast 
============================= 
BGP table version is 40, local router ID is 10.10.20.11, vrf id 13 
Default local pref 100, local AS 65210 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*> 192.168.1.0/24   10.10.10.10<                           0 65110 i 
*> 192.168.2.0/24   10.10.10.10<                           0 65110 i 
*= 192.168.10.0/24  10.10.20.2<                            0 65299 65202 ? 
*                   10.10.20.2<                            0 65299 65202 ? 
*>                  10.10.20.1<                            0 65299 65201 ? 
*                   10.10.20.1<                            0 65299 65201 ? 
*= 192.168.10.110/32 
                    10.10.20.2<                            0 65299 65202 i 
*                   10.10.20.2<                            0 65299 65202 i 
*>                  10.10.20.1<                            0 65299 65201 i 
*                   10.10.20.1<                            0 65299 65201 i 
*> 192.168.20.0/24  0.0.0.0                            32768 i 
*                   10.10.20.2<                            0 65299 65202 ? 
*                   10.10.20.2<                            0 65299 65202 ? 
*                   10.10.20.1<                            0 65299 65201 ? 
*                   10.10.20.1<                            0 65299 65201 ? 
*= 192.168.20.110/32 
                    10.10.20.2<                            0 65299 65202 i 
*                   10.10.20.2<                            0 65299 65202 i 
*>                  10.10.20.1<                            0 65299 65201 i 
*                   10.10.20.1<                            0 65299 65201 i 
 
Displayed  6 routes and 19 total paths 
 
show bgp vrf RED ipv6 unicast 
============================= 
No BGP prefixes displayed, 0 exist
```

``` 
cumulus@borderleaf04:mgmt:~$ net show bgp vrf GREEN 
show bgp vrf GREEN ipv4 unicast 
=============================== 
BGP table version is 40, local router ID is 10.10.20.11, vrf id 11 
Default local pref 100, local AS 65210 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*> 192.168.1.0/24   10.10.10.10<                           0 65110 i 
*> 192.168.2.0/24   10.10.10.10<                           0 65110 i 
*> 192.168.10.0/24  0.0.0.0                            32768 i 
*                   10.10.20.2<                            0 65299 65202 ? 
*                   10.10.20.2<                            0 65299 65202 ? 
*                   10.10.20.1<                            0 65299 65201 ? 
*                   10.10.20.1<                            0 65299 65201 ? 
*= 192.168.10.110/32 
                    10.10.20.2<                            0 65299 65202 i 
*                   10.10.20.2<                            0 65299 65202 i 
*>                  10.10.20.1<                            0 65299 65201 i 
*                   10.10.20.1<                            0 65299 65201 i 
*= 192.168.20.0/24  10.10.20.2<                            0 65299 65202 ? 
*                   10.10.20.2<                            0 65299 65202 ? 
*>                  10.10.20.1<                            0 65299 65201 ? 
*                   10.10.20.1<                            0 65299 65201 ? 
*= 192.168.20.110/32 
                    10.10.20.2<                            0 65299 65202 i 
*                   10.10.20.2<                            0 65299 65202 i 
*>                  10.10.20.1<                            0 65299 65201 i 
*                   10.10.20.1<                            0 65299 65201 i 
 
Displayed  6 routes and 19 total paths 

show bgp vrf GREEN ipv6 unicast 
=============================== 
No BGP prefixes displayed, 0 exist 
```
</div>

{{< /tab >}}
{{< /tabs >}}
