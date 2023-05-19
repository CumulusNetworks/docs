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

## Introduction

VRF route leaking is commonly used in enterprise and service provider environments ever since IP based VPN services were introduced. This is the same for EVPN-based Ethernet VPNs. We use VRFs to isolate routing tables and create multi-tenancy within wide-area networks (WANs) and data centers. However, routing across VRFs is often required and for the scenarios where external routing in between VRFs is neither possible nor economical, route leaking is the only tool. Regarding with route-leaking in a data center fabric one of the first and most critical questions to be answered is that where in the network route leaking needs to happen.  

If we want a common denominator that will keep a summary of each POD and also face with the external environments, interconnect PODs and DC locations, we could narrow down our selection for such location in the network, border leaf. Usually border leaf nodes are dedicated leaf nodes for firewalls, load balancers, intrusion detection systems (IDS), SSL-offload devices, and WEB application firewalls (WAF), also where datacenter interconnection takes place. If we have any of these services and an interconnect, the border leaf is the point which has visibility to each tenant in the DC. Such network and security services are typically used across VRFs or come in handy when they have a direct connection to each tenant network. That is why VRF is a practical technology. Therefore, performing VRF route-leaking on regular leaf nodes blinds those services because they’re attached to a service leaf or a border leaf separate from a regular leaf. That’s one of the reasons route leaking on a border leaf node tends to be a more desirable choice. Another reason is that one might prefer having a deterministic set of next-hops and number of hops to reach such cross-connection point. Again, in this use case border leaf nodes are good choices for route leaking operations. 

{{<img src="/images/guides/route-leaking-between-vrfs.png">}}

However, each network is unique and has its own business and technical requirements. There might be use cases where route leaking would be the best on each individual leaf. Each leaf can perform the leaking operation, so depending on the complexity and scale of the operation, this might be the desired solution. Moreover, leaking can be partially performed on border leaf nodes and partially on regular leaf equipment.  
## Configurations
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
<br>

The route-import statement is used in both RED and GREEN VRFs to mutually leak (inject) EVPN Type-5 routes into their respective routing tables: 
`nv set vrf <vrf_name> router bgp route-import from-evpn route-target <asn:vni>`

There is direct DCI connectivity between borderleaf01 and borderleaf04. You must enable the l2vpn address family for the DCI underlay session to exchange EVPN routes. 

To avoid any Layer-2 stretch with EVPN Type-2 and Type-3 routes, filter any unwanted EVPN route types with a simple filter applied to the BGP peer-group outbound direction: 

```
nv set router policy route-map control_t5 rule 1 action permit 
nv set router policy route-map control_t5 rule 1 match evpn-route-type ip-prefix 
nv set router policy route-map control_t5 rule 3 action deny 
 
nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn policy outbound route-map control_t5 
```
### Borderleaf01

To verify route-targets leaked into each vrf use the following command on border leaf nodes.

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
</div>

### Borderleaf04

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
</div>

### Borderleaf01

To examine BGP and routing tables for each VRF, run the following commands.

<div class=scroll>

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

### Borderleaf04

<div class=scroll>

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

### Leaf01

<div class=scroll>

```
nv set vrf GREEN evpn enable on 
nv set vrf GREEN evpn vni 4002 
nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
nv set vrf GREEN router bgp autonomous-system 65101 
nv set vrf GREEN router bgp enable on 
nv set vrf GREEN router bgp peer-group underlay address-family l2vpn-evpn enable on 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4001 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4002 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5001 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5002 
nv set vrf GREEN router bgp router-id 10.10.10.1 
nv set vrf RED evpn enable on 
nv set vrf RED evpn vni 4001 
nv set vrf RED router bgp address-family ipv4-unicast enable on 
nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
nv set vrf RED router bgp autonomous-system 65101 
nv set vrf RED router bgp enable on 
nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on 
nv set vrf RED router bgp route-import from-evpn route-target ANY:4001 
nv set vrf RED router bgp route-import from-evpn route-target ANY:4002 
nv set vrf RED router bgp route-import from-evpn route-target ANY:5001 
nv set vrf RED router bgp route-import from-evpn route-target ANY:5002 
nv set vrf RED router bgp router-id 10.10.10.1 
nv set vrf default router bgp address-family ipv4-unicast enable on 
nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32 
nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on 
nv set vrf default router bgp address-family l2vpn-evpn enable on 
nv set vrf default router bgp enable on 
nv set vrf default router bgp neighbor swp1 peer-group underlay 
nv set vrf default router bgp neighbor swp1 type unnumbered 
nv set vrf default router bgp neighbor swp2 peer-group underlay 
nv set vrf default router bgp neighbor swp2 type unnumbered 
nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
nv set vrf default router bgp peer-group underlay remote-as external 
```
</div>

### Leaf03

<div class=scroll>

```
nv set vrf GREEN evpn enable on 
nv set vrf GREEN evpn vni 5002 
nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
nv set vrf GREEN router bgp autonomous-system 65201 
nv set vrf GREEN router bgp enable on 
nv set vrf GREEN router bgp peer-group underlay address-family l2vpn-evpn enable on 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4001 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4002 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5001 
nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5002 
nv set vrf GREEN router bgp router-id 10.10.20.1 
nv set vrf RED evpn enable on 
nv set vrf RED evpn vni 5001 
nv set vrf RED router bgp address-family ipv4-unicast enable on 
nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
nv set vrf RED router bgp autonomous-system 65201 
nv set vrf RED router bgp enable on 
nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on 
nv set vrf RED router bgp route-import from-evpn route-target ANY:4001 
nv set vrf RED router bgp route-import from-evpn route-target ANY:4002 
nv set vrf RED router bgp route-import from-evpn route-target ANY:5001 
nv set vrf RED router bgp route-import from-evpn route-target ANY:5002 
nv set vrf RED router bgp router-id 10.10.20.1 
nv set vrf default router bgp address-family ipv4-unicast enable on 
nv set vrf default router bgp address-family ipv4-unicast network 10.10.20.1/32 
nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on 
nv set vrf default router bgp address-family l2vpn-evpn enable on 
nv set vrf default router bgp enable on 
nv set vrf default router bgp neighbor swp1 peer-group underlay 
nv set vrf default router bgp neighbor swp1 type unnumbered 
nv set vrf default router bgp neighbor swp2 peer-group underlay 
nv set vrf default router bgp neighbor swp2 type unnumbered 
nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
nv set vrf default router bgp peer-group underlay remote-as external 
```

</div>
<br>

As displayed in the leaf configurations, leaf nodes must also import cross-site route-targets advertised by border leafs. This is because interconnected data centers use VNIs that are different from downstream VNIs. The classical auto-route-target import function has no way of detecting these VNIs and cannot import the route targets automatically.