---
title: Layer 3 Extensions
author: NVIDIA
weight: 50
product: Technical Guides
imgData: guides
---
<style>
  .scroll{
    height: 500px;
    overflow-y: auto;
  }
</style>
Layer 3 extensions use EVPN as a control plane and are similar to layer 3 VPN with VXLAN tunnels. The leaf switches set up full mesh VXLAN tunnels within and across PODs, and the routing exchange between pods occurs with EVPN type-5 routes. Within the pod, there are type-1 and type-4 routes for EVPN multihoming, type-2 for MAC addresses, IP addresses and MAC routes, and type-3 for BUM HER routes.

## Configuration

{{<img src="/images/guides/dci-reference-topology.png">}}

|DCI 1|DCI 2|
|--|--|
|<table> </tr><tr><td>VRF</td><td>RED</td></tr><td>Layer 2 VNI</td><td>10</tr><td>Layer 3 VNI</td><td>4001</td></tr></table>| <table> </tr><tr><td>VRF</td><td>RED</td></tr><td>Layer 2 VNI</td><td>1010</tr><td>Layer 3 VNI</td><td>5001</td></tr> </table>|
|<table> </tr><tr><td>VRF</td><td>GREEN</td></tr><td>Layer 2 VNI</td><td>20</tr><td>Layer 3 VNI</td><td>4002</td></tr></table>| <table> </tr><tr><td>VRF</td><td>GREEN</td></tr><td>Layer 2 VNI</td><td>2020</tr><td>Layer 3 VNI</td><td>5002</td></tr> </table>|

The following configuration example connects VRF RED in DC1 with VRF RED in DC2, using downstream VNI and symmetrical routing. The `route-target import` statements connect two RED VRFs at layer 3 (for prefix exchange). This configuration provides IP connectivity between server01 and server03 within VRF RED, and server02 and server04 within VRF GREEN, but the RED and GREEN VRFs cannot communicate with each other. All servers are in different IP subnets; there is no layer 2 adjacency between them. A server communicates with its peer in the other DC through its default gateway, which is the local VRR MAC address in the ARP cache.

The example shows a layer 3 interconnect configuration, where the border leafs filter EVPN prefixes (except type-5) to distribute across DCI links. This configuration ensures that DCI only exchanges type-5 prefixes, and that the remote DC does not receive and process unwanted prefix types. The ESI and MAC addresses are visible for each local POD, but not across PODs.

{{< tabs "TabID27 ">}}
{{< tab "server01 ">}}

<div class=scroll>

```
ubuntu@server01:~$ cat /etc/netplan/config.yaml 
################################################################ 
# IMPORTANT: When using NVIDIA Air services,                   # 
#  your Internet-facing interface must include the following:  # 
#   dhcp6: false                                               # 
#   accept-ra: true                                            # 
################################################################ 
network: 
  version: 2 
  renderer: networkd 
  ethernets: 
    eth0: 
      dhcp4: true 
    eth1: 
      dhcp4: false 
    eth2: 
      dhcp4: false 
  bonds: 
      bond0: 
          interfaces: [eth1, eth2] 
          addresses: [192.168.1.10/24] 
          gateway4: 192.168.1.1 
          routes: 
          - to: 192.168.0.0/16 
            via: 192.168.1.1 
          parameters: 
              mode: 802.3ad 
  version: 2 
ubuntu@server01:~$ ip addr 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00 
    inet 127.0.0.1/8 scope host lo 
       valid_lft forever preferred_lft forever 
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever 
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 
    link/ether 44:38:39:22:aa:01 brd ff:ff:ff:ff:ff:ff 
    inet 192.168.200.20/24 brd 192.168.200.255 scope global dynamic eth0 
       valid_lft 163305sec preferred_lft 163305sec 
    inet6 fe80::4638:39ff:fe22:aa01/64 scope link 
       valid_lft forever preferred_lft forever 
3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc fq_codel master bond0 state UP group default qlen 1000 
    link/ether 42:20:47:91:95:a7 brd ff:ff:ff:ff:ff:ff 
4: eth2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc fq_codel master bond0 state UP group default qlen 1000 
    link/ether 42:20:47:91:95:a7 brd ff:ff:ff:ff:ff:ff 
5: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000 
    link/ether 42:20:47:91:95:a7 brd ff:ff:ff:ff:ff:ff 
    inet 192.168.1.10/24 brd 192.168.1.255 scope global bond0 
       valid_lft forever preferred_lft forever 
    inet6 fe80::4020:47ff:fe91:95a7/64 scope link 
       valid_lft forever preferred_lft forever 
```
</div>

{{< /tab >}}
{{< tab "server03 ">}}

<div class=scroll>

```
ubuntu@server03:~$ cat /etc/netplan/config.yaml 
################################################################ 
# IMPORTANT: When using NVIDIA Air services,                   # 
#  your Internet-facing interface must include the following:  # 
#   dhcp6: false                                               # 
#   accept-ra: true                                            # 
################################################################ 
network: 
  version: 2 
  renderer: networkd 
  ethernets: 
    eth0: 
      dhcp4: true 
    eth1: 
      dhcp4: false 
    eth2: 
      dhcp4: false 
  bonds: 
      bond0: 
          interfaces: [eth1, eth2] 
          addresses: [192.168.10.110/24] 
          gateway4: 192.168.10.100 
          routes: 
          - to: 192.168.0.0/16 
            via: 192.168.10.100 
          parameters: 
              mode: 802.3ad 
  version: 2 
ubuntu@server03:~$ ip addr 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00 
    inet 127.0.0.1/8 scope host lo 
       valid_lft forever preferred_lft forever 
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever 
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 
    link/ether 44:38:39:22:aa:03 brd ff:ff:ff:ff:ff:ff 
    inet 192.168.200.22/24 brd 192.168.200.255 scope global dynamic eth0 
       valid_lft 163264sec preferred_lft 163264sec 
    inet6 fe80::4638:39ff:fe22:aa03/64 scope link 
       valid_lft forever preferred_lft forever 
3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc fq_codel master bond0 state UP group default qlen 1000 
    link/ether b6:4b:0f:ea:f2:02 brd ff:ff:ff:ff:ff:ff 
4: eth2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc fq_codel master bond0 state UP group default qlen 1000 
    link/ether b6:4b:0f:ea:f2:02 brd ff:ff:ff:ff:ff:ff 
5: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000 
    link/ether b6:4b:0f:ea:f2:02 brd ff:ff:ff:ff:ff:ff 
    inet 192.168.10.110/24 brd 192.168.10.255 scope global bond0 
       valid_lft forever preferred_lft forever 
    inet6 fe80::b44b:fff:feea:f202/64 scope link 
       valid_lft forever preferred_lft forever 
```
</div>

{{< /tab >}}
{{< tab "leaf01 ">}}

<div class=scroll>

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10 
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 20 vni 20 
cumulus@leaf01:mgmt:~$ nv set evpn enable on 
cumulus@leaf01:mgmt:~$ nv set evpn multihoming enable on 
cumulus@leaf01:mgmt:~$ nv set interface bond1 bond member swp3 
cumulus@leaf01:mgmt:~$ nv set interface bond1 bridge domain br_default access 10 
cumulus@leaf01:mgmt:~$ nv set interface bond1 evpn multihoming segment local-id 1 
cumulus@leaf01:mgmt:~$ nv set interface bond1-2 bond lacp-bypass on 
cumulus@leaf01:mgmt:~$ nv set interface bond1-2 evpn multihoming segment df-preference 50000 
cumulus@leaf01:mgmt:~$ nv set interface bond1-2 evpn multihoming segment enable on 
cumulus@leaf01:mgmt:~$ nv set interface bond1-2 evpn multihoming segment mac-address 00:00:00:00:00:AA 
cumulus@leaf01:mgmt:~$ nv set interface bond1-2 type bond 
cumulus@leaf01:mgmt:~$ nv set interface bond2 bond member swp4 
cumulus@leaf01:mgmt:~$ nv set interface bond2 bridge domain br_default access 20 
cumulus@leaf01:mgmt:~$ nv set interface bond2 evpn multihoming segment local-id 2 
cumulus@leaf01:mgmt:~$ nv set interface eth0 ip vrf mgmt 
cumulus@leaf01:mgmt:~$ nv set interface eth0 type eth 
cumulus@leaf01:mgmt:~$ nv set interface lo ip address 10.10.10.1/32 
cumulus@leaf01:mgmt:~$ nv set interface lo type loopback 
cumulus@leaf01:mgmt:~$ nv set interface swp1-2 evpn multihoming uplink on 
cumulus@leaf01:mgmt:~$ nv set interface swp1-2 type swp 
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip address 192.168.1.2/24 
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrf RED 
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr address 192.168.1.1/24 
cumulus@leaf01:mgmt:~$ nv set interface vlan10 vlan 10 
cumulus@leaf01:mgmt:~$ nv set interface vlan10,20 ip vrr enable on 
cumulus@leaf01:mgmt:~$ nv set interface vlan10,20 ip vrr state up 
cumulus@leaf01:mgmt:~$ nv set interface vlan10,20 type svi 
cumulus@leaf01:mgmt:~$ nv set interface vlan20 ip address 192.168.2.2/24 
cumulus@leaf01:mgmt:~$ nv set interface vlan20 ip vrf GREEN 
cumulus@leaf01:mgmt:~$ nv set interface vlan20 ip vrr address 192.168.2.1/24 
cumulus@leaf01:mgmt:~$ nv set interface vlan20 vlan 20 
cumulus@leaf01:mgmt:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf01:mgmt:~$ nv set nve vxlan enable on 
cumulus@leaf01:mgmt:~$ nv set nve vxlan source address 10.10.10.1 
cumulus@leaf01:mgmt:~$ nv set router bgp autonomous-system 65101 
cumulus@leaf01:mgmt:~$ nv set router bgp enable on 
cumulus@leaf01:mgmt:~$ nv set router bgp router-id 10.10.10.1 
cumulus@leaf01:mgmt:~$ nv set router vrr enable on 
cumulus@leaf01:mgmt:~$ nv set service lldp 
cumulus@leaf01:mgmt:~$ nv set system config auto-save enable on 
cumulus@leaf01:mgmt:~$ nv set system global anycast-id 10 
cumulus@leaf01:mgmt:~$ nv set system global fabric-id 10 
cumulus@leaf01:mgmt:~$ nv set system hostname leaf01 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN evpn vni 4002 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp autonomous-system 65101 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4002 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5002 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp router-id 10.10.10.1 
cumulus@leaf01:mgmt:~$ nv set vrf RED evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED evpn vni 4001 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp autonomous-system 65101 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:4001 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:5001 
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
{{< tab "spine01 ">}}

<div class=scroll>

```
cumulus@spine01:mgmt:~$ nv set interface eth0 ip vrf mgmt 
cumulus@spine01:mgmt:~$ nv set interface eth0 type eth 
cumulus@spine01:mgmt:~$ nv set interface lo ip address 10.10.10.101/32 
cumulus@spine01:mgmt:~$ nv set interface lo type loopback 
cumulus@spine01:mgmt:~$ nv set interface swp1-4 type swp 
cumulus@spine01:mgmt:~$ nv set router bgp autonomous-system 65199 
cumulus@spine01:mgmt:~$ nv set router bgp enable on 
cumulus@spine01:mgmt:~$ nv set router bgp router-id 10.10.10.101 
cumulus@spine01:mgmt:~$ nv set system config auto-save enable on 
cumulus@spine01:mgmt:~$ nv set system hostname spine01 
cumulus@spine01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@spine01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32 
cumulus@spine01:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@spine01:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp1-4 address-family l2vpn-evpn enable on 
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp1-4 remote-as external 
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp1-4 type unnumbered 
```
</div>

{{< /tab >}}
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
cumulus@borderleaf01:mgmt:~$ nv set router policy route-map control_t5 rule 2 action deny 
cumulus@borderleaf01:mgmt:~$ nv set service lldp 
cumulus@borderleaf01:mgmt:~$ nv set system config auto-save enable on 
cumulus@borderleaf01:mgmt:~$ nv set system global anycast-id 10 
cumulus@borderleaf01:mgmt:~$ nv set system global fabric-id 10 
cumulus@borderleaf01:mgmt:~$ nv set system hostname borderleaf01 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN evpn vni 4002 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp autonomous-system 65110 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4002 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5002 
cumulus@borderleaf01:mgmt:~$ nv set vrf GREEN router bgp router-id 10.10.10.10 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED evpn vni 4001 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp autonomous-system 65110 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:4001 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:5001 
cumulus@borderleaf01:mgmt:~$ nv set vrf RED router bgp router-id 10.10.10.10 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.10/32 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 peer-group underlay 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 type unnumbered 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 peer-group underlay 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 type unnumbered 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp3 peer-group dci_group1 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp3 type unnumbered 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn policy outbound route-map control_t5 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 remote-as external 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group underlay remote-as external 
```
</div>

{{< /tab >}}
{{< tab "leaf03 ">}}

<div class=scroll>

```
cumulus@leaf03:mgmt:~$ nv set bridge domain br_default vlan 1010 vni 1010 
cumulus@leaf03:mgmt:~$ nv set bridge domain br_default vlan 2020 vni 2020 
cumulus@leaf03:mgmt:~$ nv set evpn enable on 
cumulus@leaf03:mgmt:~$ nv set evpn multihoming enable on 
cumulus@leaf03:mgmt:~$ nv set interface bond1 bond member swp3 
cumulus@leaf03:mgmt:~$ nv set interface bond1 bridge domain br_default access 1010 
cumulus@leaf03:mgmt:~$ nv set interface bond1 evpn multihoming segment local-id 1 
cumulus@leaf03:mgmt:~$ nv set interface bond1-2 bond lacp-bypass on 
cumulus@leaf03:mgmt:~$ nv set interface bond1-2 evpn multihoming segment df-preference 50000 
cumulus@leaf03:mgmt:~$ nv set interface bond1-2 evpn multihoming segment enable on 
cumulus@leaf03:mgmt:~$ nv set interface bond1-2 evpn multihoming segment mac-address 00:00:00:00:00:BB 
cumulus@leaf03:mgmt:~$ nv set interface bond1-2 type bond 
cumulus@leaf03:mgmt:~$ nv set interface bond2 bond member swp4 
cumulus@leaf03:mgmt:~$ nv set interface bond2 bridge domain br_default access 2020 
cumulus@leaf03:mgmt:~$ nv set interface bond2 evpn multihoming segment local-id 2 
cumulus@leaf03:mgmt:~$ nv set interface eth0 ip vrf mgmt 
cumulus@leaf03:mgmt:~$ nv set interface eth0 type eth 
cumulus@leaf03:mgmt:~$ nv set interface lo ip address 10.10.20.1/32 
cumulus@leaf03:mgmt:~$ nv set interface lo type loopback 
cumulus@leaf03:mgmt:~$ nv set interface swp1-2 evpn multihoming uplink on 
cumulus@leaf03:mgmt:~$ nv set interface swp1-2 type swp 
cumulus@leaf03:mgmt:~$ nv set interface vlan1010 ip address 192.168.10.101/24 
cumulus@leaf03:mgmt:~$ nv set interface vlan1010 ip vrf RED 
cumulus@leaf03:mgmt:~$ nv set interface vlan1010 ip vrr address 192.168.10.100/24 
cumulus@leaf03:mgmt:~$ nv set interface vlan1010 vlan 1010 
cumulus@leaf03:mgmt:~$ nv set interface vlan1010,2020 ip vrr enable on 
cumulus@leaf03:mgmt:~$ nv set interface vlan1010,2020 ip vrr state up 
cumulus@leaf03:mgmt:~$ nv set interface vlan1010,2020 type svi 
cumulus@leaf03:mgmt:~$ nv set interface vlan2020 ip address 192.168.20.101/24 
cumulus@leaf03:mgmt:~$ nv set interface vlan2020 ip vrf GREEN 
cumulus@leaf03:mgmt:~$ nv set interface vlan2020 ip vrr address 192.168.20.100/24 
cumulus@leaf03:mgmt:~$ nv set interface vlan2020 vlan 2020 
cumulus@leaf03:mgmt:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf03:mgmt:~$ nv set nve vxlan enable on 
cumulus@leaf03:mgmt:~$ nv set nve vxlan source address 10.10.20.1 
cumulus@leaf03:mgmt:~$ nv set router bgp autonomous-system 65201 
cumulus@leaf03:mgmt:~$ nv set router bgp enable on 
cumulus@leaf03:mgmt:~$ nv set router bgp router-id 10.10.20.1 
cumulus@leaf03:mgmt:~$ nv set router vrr enable on 
cumulus@leaf03:mgmt:~$ nv set service lldp 
cumulus@leaf03:mgmt:~$ nv set system config auto-save enable on 
cumulus@leaf03:mgmt:~$ nv set system global anycast-id 20 
cumulus@leaf03:mgmt:~$ nv set system global fabric-id 20 
cumulus@leaf03:mgmt:~$ nv set system hostname leaf03 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN evpn vni 5002 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp autonomous-system 65201 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4002 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5002 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp router-id 10.10.20.1 
cumulus@leaf03:mgmt:~$ nv set vrf RED evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED evpn vni 5001 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp autonomous-system 65201 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:4001 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:5001 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp router-id 10.10.20.1 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.20.1/32 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp1 address-family l2vpn-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp1 remote-as external 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp1 type unnumbered 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp2 address-family l2vpn-evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp2 remote-as external 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp2 type unnumbered 
```
</div>

{{< /tab >}}
{{< tab "spine03 ">}}

<div class=scroll>

```
cumulus@spine03:mgmt:~$ nv set interface eth0 ip vrf mgmt 
cumulus@spine03:mgmt:~$ nv set interface eth0 type eth 
cumulus@spine03:mgmt:~$ nv set interface lo ip address 10.10.20.103/32 
cumulus@spine03:mgmt:~$ nv set interface lo type loopback 
cumulus@spine03:mgmt:~$ nv set interface swp1-4 type swp 
cumulus@spine03:mgmt:~$ nv set router bgp autonomous-system 65299 
cumulus@spine03:mgmt:~$ nv set router bgp enable on 
cumulus@spine03:mgmt:~$ nv set router bgp router-id 10.10.20.103 
cumulus@spine03:mgmt:~$ nv set system config auto-save enable on 
cumulus@spine03:mgmt:~$ nv set system global anycast-id 20 
cumulus@spine03:mgmt:~$ nv set system global fabric-id 20 
cumulus@spine03:mgmt:~$ nv set system hostname spine03 
cumulus@spine03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@spine03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.20.103/32 
cumulus@spine03:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@spine03:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@spine03:mgmt:~$ nv set vrf default router bgp neighbor swp1-4 address-family l2vpn-evpn enable on 
cumulus@spine03:mgmt:~$ nv set vrf default router bgp neighbor swp1-4 remote-as external 
cumulus@spine03:mgmt:~$ nv set vrf default router bgp neighbor swp1-4 type unnumbered 
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
cumulus@borderleaf04:mgmt:~$ nv set router policy route-map control_t5 rule 1 action permit 
cumulus@borderleaf04:mgmt:~$ nv set router policy route-map control_t5 rule 1 match evpn-route-type ip-prefix 
cumulus@borderleaf04:mgmt:~$ nv set router policy route-map control_t5 rule 2 action deny 
cumulus@borderleaf04:mgmt:~$ nv set service lldp 
cumulus@borderleaf04:mgmt:~$ nv set system config auto-save enable on 
cumulus@borderleaf04:mgmt:~$ nv set system global anycast-id 20 
cumulus@borderleaf04:mgmt:~$ nv set system global fabric-id 20 
cumulus@borderleaf04:mgmt:~$ nv set system hostname borderleaf04 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN evpn vni 5002 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp autonomous-system 65210 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:4002 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target ANY:5002 
cumulus@borderleaf04:mgmt:~$ nv set vrf GREEN router bgp router-id 10.10.20.11 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED evpn vni 5001 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp autonomous-system 65210 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:4001 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target ANY:5001 
cumulus@borderleaf04:mgmt:~$ nv set vrf RED router bgp router-id 10.10.20.11 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.20.11/32 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp1 peer-group underlay 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp1 type unnumbered 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp2 peer-group underlay 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp2 type unnumbered 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp3 peer-group dci_group1 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp neighbor swp3 type unnumbered 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn policy outbound route-map control_t5 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 remote-as external 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group underlay remote-as external 
```
</div>

{{< /tab >}}
{{< /tabs >}}

## Diagnostic Commands

The following examples show troubleshooting commands.

{{< tabs "TabID512 ">}}
{{< tab "DC1 ">}}

<div class=scroll>

```
cumulus@leaf01:mgmt:~$ net show bgp sum 
show bgp ipv4 unicast summary 
============================= 
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0 
BGP table version 216 
RIB entries 23, using 4600 bytes of memory 
Peers 2, using 46 KiB of memory 
Peer groups 1, using 64 bytes of memory 
 
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
spine01(swp1)   4      65199      2924      2922        0    0    0 02:18:51           10       12 
spine02(swp2)   4      65199      2924      2922        0    0    0 02:18:51           10       12 
 
Total number of neighbors 2 
 
show bgp ipv6 unicast summary 
============================= 
% No BGP neighbors found 
 
show bgp l2vpn evpn summary 
=========================== 
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0 
BGP table version 0 
RIB entries 75, using 15 KiB of memory 
Peers 2, using 46 KiB of memory 
Peer groups 1, using 64 bytes of memory 
 
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
spine01(swp1)   4      65199      2924      2922        0    0    0 02:18:52           26       46 
spine02(swp2)   4      65199      2924      2922        0    0    0 02:18:52           26       46 
 
Total number of neighbors 2
```

``` 
cumulus@leaf01:mgmt:~$ net show evpn es 
Type: B bypass, L local, R remote, N non-DF 
ESI                            Type ES-IF                 VTEPs 
03:00:00:00:00:00:aa:00:00:01  LR   bond1                 10.10.10.2 
03:00:00:00:00:00:aa:00:00:02  LR   bond2                 10.10.10.2 
```

```
cumulus@leaf01:mgmt:~$ net show bgp l2vpn evpn es 
ES Flags: B - bypass, L local, R remote, I inconsistent 
VTEP Flags: E ESR/Type-4, A active nexthop 
ESI                            Flags RD                    #VNIs    VTEPs 
03:00:00:00:00:00:aa:00:00:01  LR    10.10.10.1:3          1        10.10.10.2(EA) 
03:00:00:00:00:00:aa:00:00:02  LR    10.10.10.1:4          1        10.10.10.2(EA) 
```

```
cumulus@leaf01:mgmt:~$ net show bgp l2vpn evpn es-evi 
Flags: L local, R remote, I inconsistent 
VTEP-Flags: E EAD-per-ES, V EAD-per-EVI 
VNI      ESI                            Flags VTEPs 
20       03:00:00:00:00:00:aa:00:00:02  LR    10.10.10.2(EV) 
10       03:00:00:00:00:00:aa:00:00:01  LR    10.10.10.2(EV) 
```

```
cumulus@leaf01:mgmt:~$ net show bgp l2vpn evpn es-vrf 
ES-VRF Flags: A Active 
ESI                            VRF             Flags IPv4-NHG IPv6-NHG Ref 
03:00:00:00:00:00:aa:00:00:01  VRF RED         A     72580645 72580646 1 
03:00:00:00:00:00:aa:00:00:02  VRF GREEN       A     72580647 72580648 1 
```

```
cumulus@leaf01:mgmt:~$ net show int bond1 
    Name   MAC                Speed  MTU   Mode 
--  -----  -----------------  -----  ----  ------- 
UP  bond1  48:b0:2d:3d:e9:84  1G     9216  802.3ad 
 
Bond Details 
------------------  -------- 
Bond Mode:          802.3ad 
Load Balancing:     layer3+4 
Minimum Links:      1 
LACP Sys Priority: 
LACP Rate:          1 
LACP Bypass:        Active 
 
All VLANs on L2 Port 
-------------------- 
10 
 
Untagged 
-------- 
10 
 
cl-netstat counters 
------------------- 
 RX_OK  RX_ERR  RX_DRP  RX_OVR   TX_OK  TX_ERR  TX_DRP  TX_OVR 
------  ------  ------  ------  ------  ------  ------  ------ 
257688       0       1       0  163218       0       0       0 
 
LLDP Details 
------------ 
LocalPort  RemotePort(RemoteHost) 
---------  --------------------------- 
swp3       48:b0:2d:33:24:a3(server01) 
 
Routing 
------- 
  Interface bond1 is up, line protocol is up 
  Link ups:       4    last: 2023/04/14 15:51:23.59 
  Link downs:     0    last: (never) 
  PTM status: disabled 
  vrf: default 
  index 10 metric 0 mtu 9216 speed 4294967295 
  flags: <UP,BROADCAST,RUNNING,MULTICAST> 
  Type: Ethernet 
  HWaddr: 48:b0:2d:3d:e9:84 
  Interface Type bond 
  Master interface: br_default PVID: 10 
  EVPN-MH: ES id 1 ES sysmac 00:00:00:00:00:aa 
  protodown: off (n/a) 
  ARP-ND redirect enabled: ARP 1713 ND 2791 
```

``` 
cumulus@leaf01:mgmt:~$ net show bgp vrf RED 
show bgp vrf RED ipv4 unicast 
============================= 
BGP table version is 57, local router ID is 10.10.10.1, vrf id 19 
Default local pref 100, local AS 65101 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*  192.168.1.0/24   10.10.10.2<                            0 65199 65102 ? 
*                   10.10.10.2<                            0 65199 65102 ? 
*>                  0.0.0.0                  0         32768 ? 
*  192.168.10.0/24  10.10.20.2<                            0 65199 65110 65210 65299 65202 ? 
*=                  10.10.20.2<                            0 65199 65110 65210 65299 65202 ? 
*>                  10.10.20.1<                            0 65199 65110 65210 65299 65201 ? 
*                   10.10.20.1<                            0 65199 65110 65210 65299 65201 ? 
 
Displayed  2 routes and 7 total paths 

show bgp vrf RED ipv6 unicast 
============================= 
No BGP prefixes displayed, 0 exist
```

```
cumulus@leaf01:mgmt:~$ net show route vrf RED 
show ip route vrf RED 
====================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 2d22h09m 
C * 192.168.1.0/24 [0/1024] is directly connected, vlan10-v0, 2d19h15m 
C>* 192.168.1.0/24 is directly connected, vlan10, 2d22h09m 
B>* 192.168.10.0/24 [20/0] via 10.10.20.1, vxlan99 (vrf default) onlink, label 5001, weight 1, 00:02:56 
  *                        via 10.10.20.2, vxlan99 (vrf default) onlink, label 5001, weight 1, 00:02:56 
  
show ipv6 route vrf RED 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 2d22h09m 
C * fe80::/64 is directly connected, vlan10-v0, 2d19h15m 
C * fe80::/64 is directly connected, vlan220_l3, 2d22h08m 
C>* fe80::/64 is directly connected, vlan10, 2d22h09m 
```

```
cumulus@leaf01:mgmt:~$ net show bgp vrf GREEN 
show bgp vrf GREEN ipv4 unicast 
=============================== 
BGP table version is 67, local router ID is 10.10.10.1, vrf id 13 
Default local pref 100, local AS 65101 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*  192.168.2.0/24   10.10.10.2<                            0 65199 65102 ? 
*                   10.10.10.2<                            0 65199 65102 ? 
*>                  0.0.0.0                  0         32768 ? 
*  192.168.20.0/24  10.10.20.2<                            0 65199 65110 65210 65299 65202 ? 
*=                  10.10.20.2<                            0 65199 65110 65210 65299 65202 ? 
*>                  10.10.20.1<                            0 65199 65110 65210 65299 65201 ? 
*                   10.10.20.1<                            0 65199 65110 65210 65299 65201 ? 
 
Displayed  2 routes and 7 total paths 
 
show bgp vrf GREEN ipv6 unicast 
=============================== 
No BGP prefixes displayed, 0 exist 
```

```
cumulus@leaf01:mgmt:~$ net show route vrf GREEN 
show ip route vrf GREEN 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 2d22h09m 
C * 192.168.2.0/24 [0/1024] is directly connected, vlan20-v0, 2d19h16m 
C>* 192.168.2.0/24 is directly connected, vlan20, 2d22h09m 
B>* 192.168.20.0/24 [20/0] via 10.10.20.1, vxlan99 (vrf default) onlink, label 5002, weight 1, 00:03:43 
  *                        via 10.10.20.2, vxlan99 (vrf default) onlink, label 5002, weight 1, 00:03:43 
  
show ipv6 route vrf GREEN 
========================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 2d22h09m 
C * fe80::/64 is directly connected, vlan20-v0, 2d19h16m 
C * fe80::/64 is directly connected, vlan20, 2d22h09m 
C>* fe80::/64 is directly connected, vlan370_l3, 2d22h09m 
```

```
cumulus@leaf01:mgmt:~$ net show bgp vrf RED 192.168.1.0/24 
BGP routing table entry for 192.168.1.0/24 
Paths: (3 available, best #3, vrf RED) 
  Not advertised to any peer 
  Imported from 10.10.10.2:4:[5]:[0]:[24]:[192.168.1.0], VNI 4001 
  65199 65102 
    10.10.10.2 from spine01(swp1) (10.10.10.101) announce-nh-self 
      Origin incomplete, valid, external, bestpath-from-AS 65199 
      Extended Community: RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
      Last update: Mon Apr 17 08:46:49 2023 
  Imported from 10.10.10.2:4:[5]:[0]:[24]:[192.168.1.0], VNI 4001 
  65199 65102 
    10.10.10.2 from spine02(swp2) (10.10.10.102) announce-nh-self 
      Origin incomplete, valid, external 
      Extended Community: RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
      Last update: Mon Apr 17 08:46:49 2023 
  Local 
    0.0.0.0 from 0.0.0.0 (10.10.10.1) 
      Origin incomplete, metric 0, weight 32768, valid, sourced, bestpath-from-AS Local, best (Weight) 
      Last update: Mon Apr 17 08:46:47 2023 
```

```
cumulus@leaf01:mgmt:~$ net show bgp vrf RED 192.168.10.0/24 
BGP routing table entry for 192.168.10.0/24 
Paths: (4 available, best #3, vrf RED) 
  Not advertised to any peer 
  Imported from 10.10.20.2:6:[5]:[0]:[24]:[192.168.10.0], VNI 5001 
  65199 65110 65210 65299 65202 
    10.10.20.2 from spine01(swp1) (10.10.10.101) announce-nh-self 
      Origin incomplete, valid, external 
      Extended Community: RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
      Last update: Mon Apr 17 11:04:25 2023 
  Imported from 10.10.20.2:6:[5]:[0]:[24]:[192.168.10.0], VNI 5001 
  65199 65110 65210 65299 65202 
    10.10.20.2 from spine02(swp2) (10.10.10.102) announce-nh-self 
      Origin incomplete, valid, external, multipath 
      Extended Community: RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
      Last update: Mon Apr 17 11:04:25 2023 
  Imported from 10.10.20.1:8:[5]:[0]:[24]:[192.168.10.0], VNI 5001 
  65199 65110 65210 65299 65201 
    10.10.20.1 from spine01(swp1) (10.10.10.101) announce-nh-self 
      Origin incomplete, valid, external, multipath, bestpath-from-AS 65199, best (Router ID) 
      Extended Community: RT:65201:5001 ET:8 Rmac:44:38:39:22:bb:08 
      Last update: Mon Apr 17 11:04:25 2023 
  Imported from 10.10.20.1:8:[5]:[0]:[24]:[192.168.10.0], VNI 5001 
  65199 65110 65210 65299 65201 
    10.10.20.1 from spine02(swp2) (10.10.10.102) announce-nh-self 
      Origin incomplete, valid, external 
      Extended Community: RT:65201:5001 ET:8 Rmac:44:38:39:22:bb:08 
      Last update: Mon Apr 17 11:04:25 2023 
```

```
cumulus@leaf01:mgmt:~$  net show bgp evpn vni 
Advertise Gateway Macip: Disabled 
Advertise SVI Macip: Disabled 
Advertise All VNI flag: Enabled 
BUM flooding: Head-end replication 
VXLAN flooding: Enabled 
Number of L2 VNIs: 2 
Number of L3 VNIs: 2 
Flags: * - Kernel 
  VNI        Type RD                    Import RT                 Export RT                 Tenant VRF 
* 20         L2   10.10.10.1:2          65101:20                  65101:20                 GREEN 
* 10         L2   10.10.10.1:7          65101:10                  65101:10                 RED 
* 4002       L3   10.10.10.1:5          0:4002, ...               65101:4002               GREEN 
* 4001       L3   10.10.10.1:6          0:4001, ...               65101:4001               RED 
```

```
cumulus@leaf01:mgmt:~$ net show bgp evpn vni 4001 
VNI: 4001 (known to the kernel) 
  Type: L3 
  Tenant VRF: RED 
  RD: 10.10.10.1:6 
  Originator IP: 10.10.10.1 
  Advertise-gw-macip : n/a 
  Advertise-svi-macip : n/a 
  Advertise-pip: Yes 
  System-IP: 10.10.10.1 
  System-MAC: 44:38:39:22:bb:06 
  Router-MAC: 44:38:39:22:bb:06 
  Import Route Target: 
    0:4001 
    0:5001 
  Export Route Target: 
    65101:4001 
```

```
cumulus@leaf01:mgmt:~$ net show bgp evpn vni 4002 
VNI: 4002 (known to the kernel) 
  Type: L3 
  Tenant VRF: GREEN 
  RD: 10.10.10.1:5 
  Originator IP: 10.10.10.1 
  Advertise-gw-macip : n/a 
  Advertise-svi-macip : n/a 
  Advertise-pip: Yes 
  System-IP: 10.10.10.1 
  System-MAC: 44:38:39:22:bb:06 
  Router-MAC: 44:38:39:22:bb:06 
  Import Route Target: 
    0:4002 
    0:5002 
  Export Route Target: 
    65101:4002
```

``` 
cumulus@leaf01:mgmt:~$ net show evpn mac vni all 
VNI 10 #MACs (local and remote) 5 
 
Flags: B=bypass N=sync-neighs, I=local-inactive, P=peer-active, X=peer-proxy 
MAC               Type   Flags Intf/Remote ES/VTEP            VLAN  Seq #'s 
44:38:39:22:bb:06 local        vlan10                               0/0 
48:b0:2d:33:24:a3 local  X     bond1                          10    0/0 
44:38:39:22:bb:07 remote       10.10.10.2                           0/0 
42:20:47:91:95:a7 local  NP    bond1                          10    1/0 
48:b0:2d:bc:7e:83 remote       10.10.10.2                           0/0 
 
VNI 20 #MACs (local and remote) 5 
 
Flags: B=bypass N=sync-neighs, I=local-inactive, P=peer-active, X=peer-proxy 
MAC               Type   Flags Intf/Remote ES/VTEP            VLAN  Seq #'s 
48:b0:2d:9d:31:ae local  X     bond2                          20    0/0 
44:38:39:22:bb:06 local        vlan20                               0/0 
48:b0:2d:7f:a9:bd remote       10.10.10.2                           0/0 
44:38:39:22:bb:07 remote       10.10.10.2                           0/0 
a6:e0:55:25:f3:b2 local  NP    bond2                          20    1/0 
```

```
cumulus@leaf02:mgmt:~$ net show bgp sum 
show bgp ipv4 unicast summary 
============================= 
BGP router identifier 10.10.10.2, local AS number 65102 vrf-id 0 
BGP table version 205 
RIB entries 23, using 4600 bytes of memory 
Peers 2, using 46 KiB of memory 
Peer groups 1, using 64 bytes of memory 
 
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
spine01(swp1)   4      65199      3015      3013        0    0    0 02:23:25           10       12 
spine02(swp2)   4      65199      3015      3013        0    0    0 02:23:25           10       12 
 
Total number of neighbors 2 
 
show bgp ipv6 unicast summary 
============================= 
% No BGP neighbors found 
 
show bgp l2vpn evpn summary 
=========================== 
BGP router identifier 10.10.10.2, local AS number 65102 vrf-id 0 
BGP table version 0 
RIB entries 75, using 15 KiB of memory 
Peers 2, using 46 KiB of memory 
Peer groups 1, using 64 bytes of memory 
 
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
spine01(swp1)   4      65199      3015      3013        0    0    0 02:23:26           24       46 
spine02(swp2)   4      65199      3015      3013        0    0    0 02:23:26           24       46 
 
Total number of neighbors 2 
```

```
cumulus@leaf02:mgmt:~$ net show bgp vrf RED 
show bgp vrf RED ipv4 unicast 
============================= 
BGP table version is 53, local router ID is 10.10.10.2, vrf id 19 
Default local pref 100, local AS 65102 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*  192.168.1.0/24   10.10.10.1<                            0 65199 65101 ? 
*                   10.10.10.1<                            0 65199 65101 ? 
*>                  0.0.0.0                  0         32768 ? 
*  192.168.10.0/24  10.10.20.2<                            0 65199 65110 65210 65299 65202 ? 
*=                  10.10.20.2<                            0 65199 65110 65210 65299 65202 ? 
*                   10.10.20.1<                            0 65199 65110 65210 65299 65201 ? 
*>                  10.10.20.1<                            0 65199 65110 65210 65299 65201 ? 
 
Displayed  2 routes and 7 total paths 
 
show bgp vrf RED ipv6 unicast 
============================= 
No BGP prefixes displayed, 0 exist
```

``` 
cumulus@leaf02:mgmt:~$ net show bgp vrf GREEN 
show bgp vrf GREEN ipv4 unicast 
=============================== 
BGP table version is 66, local router ID is 10.10.10.2, vrf id 13 
Default local pref 100, local AS 65102 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*  192.168.2.0/24   10.10.10.1<                            0 65199 65101 ? 
*                   10.10.10.1<                            0 65199 65101 ? 
*>                  0.0.0.0                  0         32768 ? 
*  192.168.20.0/24  10.10.20.2<                            0 65199 65110 65210 65299 65202 ? 
*=                  10.10.20.2<                            0 65199 65110 65210 65299 65202 ? 
*                   10.10.20.1<                            0 65199 65110 65210 65299 65201 ? 
*>                  10.10.20.1<                            0 65199 65110 65210 65299 65201 ? 
 
Displayed  2 routes and 7 total paths 
 
show bgp vrf GREEN ipv6 unicast 
=============================== 
No BGP prefixes displayed, 0 exist
```

``` 
cumulus@leaf02:mgmt:~$ net show route vrf RED 
show ip route vrf RED 
====================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 2d22h13m 
C * 192.168.1.0/24 [0/1024] is directly connected, vlan10-v0, 2d19h20m 
C>* 192.168.1.0/24 is directly connected, vlan10, 2d22h13m 
B>* 192.168.10.0/24 [20/0] via 10.10.20.1, vxlan99 (vrf default) onlink, label 5001, weight 1, 00:07:19 
  *                        via 10.10.20.2, vxlan99 (vrf default) onlink, label 5001, weight 1, 00:07:19 
  
show ipv6 route vrf RED 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 2d22h13m 
C * fe80::/64 is directly connected, vlan10-v0, 2d19h20m 
C * fe80::/64 is directly connected, vlan10, 2d22h13m 
C>* fe80::/64 is directly connected, vlan220_l3, 2d22h13m 
```

```
cumulus@leaf02:mgmt:~$ net show route vrf GREEN 
show ip route vrf GREEN 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 2d22h13m 
C * 192.168.2.0/24 [0/1024] is directly connected, vlan20-v0, 2d19h20m 
C>* 192.168.2.0/24 is directly connected, vlan20, 2d22h13m 
B>* 192.168.20.0/24 [20/0] via 10.10.20.1, vxlan99 (vrf default) onlink, label 5002, weight 1, 00:07:23 
  *                        via 10.10.20.2, vxlan99 (vrf default) onlink, label 5002, weight 1, 00:07:23 
  
show ipv6 route vrf GREEN 
========================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 2d22h13m 
C * fe80::/64 is directly connected, vlan20-v0, 2d19h20m 
C * fe80::/64 is directly connected, vlan20, 2d22h13m 
C>* fe80::/64 is directly connected, vlan370_l3, 2d22h13m 
```

```
cumulus@leaf02:mgmt:~$ net show evpn es 
Type: B bypass, L local, R remote, N non-DF 
ESI                            Type ES-IF                 VTEPs 
03:00:00:00:00:00:aa:00:00:01  LRN  bond1                 10.10.10.1 
03:00:00:00:00:00:aa:00:00:02  LRN  bond2                 10.10.10.1 
```

```
cumulus@leaf02:mgmt:~$ net show bgp l2vpn evpn es 
ES Flags: B - bypass, L local, R remote, I inconsistent 
VTEP Flags: E ESR/Type-4, A active nexthop 
ESI                            Flags RD                    #VNIs    VTEPs 
03:00:00:00:00:00:aa:00:00:01  LR    10.10.10.2:6          1        10.10.10.1(EA) 
03:00:00:00:00:00:aa:00:00:02  LR    10.10.10.2:7          1        10.10.10.1(EA) 
```

```
cumulus@leaf02:mgmt:~$ net show bgp l2vpn evpn es-evi 
Flags: L local, R remote, I inconsistent 
VTEP-Flags: E EAD-per-ES, V EAD-per-EVI 
VNI      ESI                            Flags VTEPs 
20       03:00:00:00:00:00:aa:00:00:02  LR    10.10.10.1(EV) 
10       03:00:00:00:00:00:aa:00:00:01  LR    10.10.10.1(EV) 
```

```
cumulus@leaf02:mgmt:~$ net show bgp l2vpn evpn es-vrf 
ES-VRF Flags: A Active 
ESI                            VRF             Flags IPv4-NHG IPv6-NHG Ref 
03:00:00:00:00:00:aa:00:00:01  VRF RED         A     72580647 72580648 1 
03:00:00:00:00:00:aa:00:00:02  VRF GREEN       A     72580645 72580646 1 
```

```
cumulus@leaf02:mgmt:~$  net show bgp evpn vni 
Advertise Gateway Macip: Disabled 
Advertise SVI Macip: Disabled 
Advertise All VNI flag: Enabled 
BUM flooding: Head-end replication 
VXLAN flooding: Enabled 
Number of L2 VNIs: 2 
Number of L3 VNIs: 2 
Flags: * - Kernel 
  VNI        Type RD                    Import RT                 Export RT                 Tenant VRF 
* 20         L2   10.10.10.2:2          65102:20                  65102:20                 GREEN 
* 10         L2   10.10.10.2:3          65102:10                  65102:10                 RED 
* 4001       L3   10.10.10.2:4          0:4001, ...               65102:4001               RED 
* 4002       L3   10.10.10.2:5          0:4002, ...               65102:4002               GREEN 
```

```
cumulus@leaf02:mgmt:~$ net show int bond1 
    Name   MAC                Speed  MTU   Mode 
--  -----  -----------------  -----  ----  ------- 
UP  bond1  48:b0:2d:f0:64:6e  1G     9216  802.3ad 
 
Bond Details 
------------------  -------- 
Bond Mode:          802.3ad 
Load Balancing:     layer3+4 
Minimum Links:      1 
LACP Sys Priority: 
LACP Rate:          1 
LACP Bypass:        Active 
 
All VLANs on L2 Port 
-------------------- 
10 
 
Untagged 
-------- 
10 
 
cl-netstat counters 
------------------- 
 RX_OK  RX_ERR  RX_DRP  RX_OVR   TX_OK  TX_ERR  TX_DRP  TX_OVR 
------  ------  ------  ------  ------  ------  ------  ------ 
255593       0       0       0  165821       0       0       0 
 
LLDP Details 
------------ 
LocalPort  RemotePort(RemoteHost) 
---------  --------------------------- 
swp3       48:b0:2d:bc:7e:83(server01) 
 
Routing 
------- 
  Interface bond1 is up, line protocol is up 
  Link ups:       6    last: 2023/04/14 15:51:19.73 
  Link downs:     0    last: (never) 
  PTM status: disabled 
  vrf: default 
  index 9 metric 0 mtu 9216 speed 1000 
  flags: <UP,BROADCAST,RUNNING,MULTICAST> 
  Type: Ethernet 
  HWaddr: 48:b0:2d:f0:64:6e 
  Interface Type bond 
  Master interface: br_default PVID: 10 
  EVPN-MH: ES id 1 ES sysmac 00:00:00:00:00:aa 
  protodown: off (n/a) 
  ARP-ND redirect enabled: ARP 906 ND 3030 
```

```
cumulus@leaf02:mgmt:~$ net show bgp evpn vni 4001 
VNI: 4001 (known to the kernel) 
  Type: L3 
  Tenant VRF: RED 
  RD: 10.10.10.2:4 
  Originator IP: 10.10.10.2 
  Advertise-gw-macip : n/a 
  Advertise-svi-macip : n/a 
  Advertise-pip: Yes 
  System-IP: 10.10.10.2 
  System-MAC: 44:38:39:22:bb:07 
  Router-MAC: 44:38:39:22:bb:07 
  Import Route Target: 
    0:4001 
    0:5001 
  Export Route Target: 
    65102:4001 
```

```
cumulus@leaf02:mgmt:~$ net show bgp evpn vni 4002 
VNI: 4002 (known to the kernel) 
  Type: L3 
  Tenant VRF: GREEN 
  RD: 10.10.10.2:5 
  Originator IP: 10.10.10.2 
  Advertise-gw-macip : n/a 
  Advertise-svi-macip : n/a 
  Advertise-pip: Yes 
  System-IP: 10.10.10.2 
  System-MAC: 44:38:39:22:bb:07 
  Router-MAC: 44:38:39:22:bb:07 
  Import Route Target: 
    0:4002 
    0:5002 
  Export Route Target: 
    65102:4002
```

```
cumulus@leaf02:mgmt:~$ net show evpn mac vni all 
VNI 10 #MACs (local and remote) 5 
 
Flags: B=bypass N=sync-neighs, I=local-inactive, P=peer-active, X=peer-proxy 
MAC               Type   Flags Intf/Remote ES/VTEP            VLAN  Seq #'s 
44:38:39:22:bb:06 remote       10.10.10.1                           0/0 
48:b0:2d:33:24:a3 local  PI    bond1                          10    0/0 
44:38:39:22:bb:07 local        vlan10                               0/0 
42:20:47:91:95:a7 local  NP    bond1                          10    1/0 
48:b0:2d:bc:7e:83 local        bond1                          10    0/0 
 
VNI 20 #MACs (local and remote) 5 
 
Flags: B=bypass N=sync-neighs, I=local-inactive, P=peer-active, X=peer-proxy 
MAC               Type   Flags Intf/Remote ES/VTEP            VLAN  Seq #'s 
48:b0:2d:9d:31:ae local  PI    bond2                          20    0/0 
44:38:39:22:bb:06 remote       10.10.10.1                           0/0 
48:b0:2d:7f:a9:bd local        bond2                          20    0/0 
44:38:39:22:bb:07 local        vlan20                               0/0 
a6:e0:55:25:f3:b2 local  NP    bond2                          20    1/0 
```
</div>

Verify that the bridge `br_default` is learning MAC entries:

<div class=scroll>

```
cumulus@leaf01:mgmt:~$ nv show bridge domain br_default mac-table 
    age     bridge-domain  entry-type  interface   last-update  MAC address        src-vni  vlan  vni   Summary 
--  ------  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  ---------------------- 
0   3       br_default     static      bond2       9770         48:b0:2d:9d:31:ae           20 
1   58      br_default     static      bond2       237427       a6:e0:55:25:f3:b2           20 
2   253880  br_default     permanent   bond2       253880       48:b0:2d:ce:f9:6f 
3   9770    br_default                 vxlan48     9770         48:b0:2d:bc:7e:83           10    None  remote-dst: 10.10.10.2 
4   9770    br_default                 vxlan48     9770         44:38:39:22:bb:07           10    None  remote-dst: 10.10.10.2 
5   9770    br_default                 vxlan48     9770         48:b0:2d:7f:a9:bd           20    None  remote-dst: 10.10.10.2 
6   253880  br_default     permanent   vxlan48     253880       96:8b:4a:de:a2:71                 None 
7   9770                   permanent   vxlan48     4            00:00:00:00:00:00  10             None  remote-dst: 10.10.10.2 
8   26      br_default     static      bond1       9770         48:b0:2d:33:24:a3           10 
9   53      br_default     static      bond1       235497       42:20:47:91:95:a7           10 
10  253880  br_default     permanent   bond1       253880       48:b0:2d:3d:e9:84 
11                         permanent   br_default               00:00:5e:00:01:0a 
12  243496  br_default     permanent   br_default  243496       44:38:39:22:bb:06           10 
```

```
cumulus@leaf02:mgmt:~$ nv show bridge domain br_default mac-table 
    age     bridge-domain  entry-type  interface   last-update  MAC address        src-vni  vlan  vni   Summary 
--  ------  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  ---------------------- 
0   250398  br_default     static      bond2       250398       48:b0:2d:9d:31:ae           20 
1   65      br_default     static      bond2       250384       a6:e0:55:25:f3:b2           20 
2   2       br_default                 bond2       253825       48:b0:2d:7f:a9:bd           20 
3   253891  br_default     permanent   bond2       253891       48:b0:2d:aa:08:bd 
4   250398  br_default     static      bond1       250398       48:b0:2d:33:24:a3           10 
5   105     br_default     static      bond1       235506       42:20:47:91:95:a7           10 
6   2       br_default                 bond1       253825       48:b0:2d:bc:7e:83           10 
7   253891  br_default     permanent   bond1       253891       48:b0:2d:f0:64:6e 
8   9775    br_default                 vxlan48     65           44:38:39:22:bb:06           20    None  remote-dst: 10.10.10.1 
9   253891  br_default     permanent   vxlan48     253891       1a:64:66:e8:14:39           1     None 
10  9775                   permanent   vxlan48     50           00:00:00:00:00:00  10             None  remote-dst: 10.10.10.1 
11                         permanent   br_default               00:00:5e:00:01:0a 
12  243505  br_default     permanent   br_default  243505       44:38:39:22:bb:07           10 
```
</div>

From the table above, locate the layer 3 VLAN interface MAC address and the VRR MAC address:

<div class=scroll>

```
cumulus@leaf01:mgmt:~$  nv show int vlan10 ip vrr 
             operational        applied 
-----------  -----------------  -------------- 
enable                          on 
mac-address  00:00:5e:00:01:0a  auto 
mac-id                          none 
[address]    192.168.1.1/24     192.168.1.1/24 
state        up                 up 
```

```
cumulus@leaf01:mgmt:~$ nv show int vlan10 | grep mac 
    mac-address                              auto 
    mac-id                                   none 
  mac                     44:38:39:22:bb:06 
```

```
cumulus@leaf02:mgmt:~$ nv show int vlan10 | grep mac 
    mac-address                              auto 
    mac-id                                   none 
  mac                     44:38:39:22:bb:07 
```
</div>

Verify EVPN type-5 routes at the ingress PE (leaf01) for the end host *192.168.10.110*, which connects to leaf03 and leaf04:

<div class=scroll>

```
cumulus@leaf01:mgmt:~$ net show bgp evpn route type 5 | grep 192.168.10 -A 4 -B 1 
Route Distinguisher: 10.10.20.1:8 
*  [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.1:8 
                    10.10.20.1 (spine02) 
                                                           0 65199 65110 65210 65299 65201 ? 
                    RT:65201:5001 ET:8 Rmac:44:38:39:22:bb:08 
*> [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.1:8 
                    10.10.20.1 (spine01) 
                                                           0 65199 65110 65210 65299 65201 ? 
                    RT:65201:5001 ET:8 Rmac:44:38:39:22:bb:08 
Route Distinguisher: 10.10.20.2:6 
*  [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.2:6 
                    10.10.20.2 (spine02) 
                                                           0 65199 65110 65210 65299 65202 ? 
                    RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
*> [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.2:6 
                    10.10.20.2 (spine01) 
                                                           0 65199 65110 65210 65299 65202 ? 
                    RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
Route Distinguisher: 10.10.20.2:7 
```
</div>

Verify EVPN type-5 routes at the egress PE (leaf03) for the end host 192.168.10.110, which connects to leaf03 and leaf04:

<div class=scroll>

```
cumulus@leaf03:mgmt:~$ net show bgp evpn route type 5 | grep 192.168.10 -A 4 -B 1 
Route Distinguisher: 10.10.20.1:8 
*> [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.1:8 
                    10.10.20.1 (leaf03) 
                                             0         32768 ? 
                    ET:8 RT:65201:5001 Rmac:44:38:39:22:bb:08 
Route Distinguisher: 10.10.20.2:6 
*  [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.2:6 
                    10.10.20.2 (spine03) 
                                                           0 65299 65202 ? 
                    RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
*> [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.2:6 
                    10.10.20.2 (spine04) 
                                                           0 65299 65202 ? 
                    RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
Route Distinguisher: 10.10.20.2:7 
```
</div>

To verify routing on the border leaf:

<div class=scroll>

```
cumulus@borderleaf01:mgmt:~$ net show bgp sum 
show bgp ipv4 unicast summary 
============================= 
BGP router identifier 10.10.10.10, local AS number 65110 vrf-id 0 
BGP table version 12 
RIB entries 19, using 3800 bytes of memory 
Peers 3, using 68 KiB of memory 
Peer groups 2, using 128 bytes of memory 
 
Neighbor           V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
borderleaf04(swp3) 4      65210       735       734        0    0    0 00:35:39            5       10 
spine01(swp1)      4      65199       778       776        0    0    0 00:36:20            3       10 
spine02(swp2)      4      65199       777       775        0    0    0 00:36:16            3       10 
 
Total number of neighbors 3 
 
show bgp ipv6 unicast summary 
============================= 
% No BGP neighbors found 
 
show bgp l2vpn evpn summary 
=========================== 
BGP router identifier 10.10.10.10, local AS number 65110 vrf-id 0 
BGP table version 0 
RIB entries 31, using 6200 bytes of memory 
Peers 3, using 68 KiB of memory 
Peer groups 2, using 128 bytes of memory 
 
Neighbor           V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
borderleaf04(swp3) 4      65210       735       734        0    0    0 00:35:39            4        8 
spine01(swp1)      4      65199       778       776        0    0    0 00:36:20           42       46 
spine02(swp2)      4      65199       777       775        0    0    0 00:36:16           42       46 
 
Total number of neighbors 3 
```

```
cumulus@borderleaf01:mgmt:~$ net show bgp vrf RED 
show bgp vrf RED ipv4 unicast 
============================= 
BGP table version is 3, local router ID is 10.10.10.10, vrf id 13 
Default local pref 100, local AS 65110 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*  192.168.1.0/24   10.10.10.2<                            0 65199 65102 ? 
*                   10.10.10.1<                            0 65199 65101 ? 
*=                  10.10.10.2<                            0 65199 65102 ? 
*>                  10.10.10.1<                            0 65199 65101 ? 
*  192.168.1.10/32  10.10.10.2<                            0 65199 65102 i 
*                   10.10.10.1<                            0 65199 65101 i 
*=                  10.10.10.2<                            0 65199 65102 i 
*>                  10.10.10.1<                            0 65199 65101 i 
*= 192.168.10.0/24  10.10.20.2<                            0 65210 65299 65202 ? 
*>                  10.10.20.1<                            0 65210 65299 65201 ? 
 
Displayed  3 routes and 10 total paths 

show bgp vrf RED ipv6 unicast 
============================= 
No BGP prefixes displayed, 0 exist
```

```
cumulus@borderleaf01:mgmt:~$ net show bgp evpn route type 5 | grep 192.168.1 -A 3 -B 1 
Route Distinguisher: 10.10.10.1:6 
*  [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.1:6 
                    10.10.10.1 (spine02) 
                                                           0 65199 65101 ? 
                    RT:65101:4001 ET:8 Rmac:44:38:39:22:bb:06 
*> [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.1:6 
                    10.10.10.1 (spine01) 
                                                           0 65199 65101 ? 
                    RT:65101:4001 ET:8 Rmac:44:38:39:22:bb:06 
Route Distinguisher: 10.10.10.2:4 
*  [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.2:4 
                    10.10.10.2 (spine02) 
                                                           0 65199 65102 ? 
                    RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
*> [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.2:4 
                    10.10.10.2 (spine01) 
                                                           0 65199 65102 ? 
                    RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
-- 
Route Distinguisher: 10.10.20.1:8 
*> [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.1:8 
                    10.10.20.1 (borderleaf04) 
                                                           0 65210 65299 65201 ? 
                    RT:65201:5001 ET:8 Rmac:44:38:39:22:bb:08 
Route Distinguisher: 10.10.20.2:6 
*> [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.2:6 
                    10.10.20.2 (borderleaf04) 
                                                           0 65210 65299 65202 ? 
                    RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
```
</div>

{{< /tab >}}
{{< tab "DC2 ">}}

<div class=scroll>

```
cumulus@leaf03:mgmt:~$ net show bgp sum 
show bgp ipv4 unicast summary 
============================= 
BGP router identifier 10.10.20.1, local AS number 65201 vrf-id 0 
BGP table version 57 
RIB entries 23, using 4600 bytes of memory 
Peers 2, using 46 KiB of memory 
 
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
spine03(swp1)   4      65299     79699     79701        0    0    0 2d18h00m           10       12 
spine04(swp2)   4      65299     79714     79714        0    0    0 2d18h00m           10       12 
 
Total number of neighbors 2 
 
show bgp ipv6 unicast summary 
============================= 
% No BGP neighbors found 
 
show bgp l2vpn evpn summary 
=========================== 
BGP router identifier 10.10.20.1, local AS number 65201 vrf-id 0 
BGP table version 0 
RIB entries 71, using 14 KiB of memory 
Peers 2, using 46 KiB of memory 
 
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
spine03(swp1)   4      65299     79699     79702        0    0    0 2d18h00m           25       46 
spine04(swp2)   4      65299     79714     79715        0    0    0 2d18h00m           25       46 
 
Total number of neighbors 2
```

```
cumulus@leaf03:mgmt:~$ net show evpn es 
Type: B bypass, L local, R remote, N non-DF 
ESI                            Type ES-IF                 VTEPs 
03:00:00:00:00:00:bb:00:00:01  LR   bond1                 10.10.20.2 
03:00:00:00:00:00:bb:00:00:02  LR   bond2                 10.10.20.2 
```

```
cumulus@leaf03:mgmt:~$ net show bgp l2vpn evpn es 
ES Flags: B - bypass, L local, R remote, I inconsistent 
VTEP Flags: E ESR/Type-4, A active nexthop 
ESI                            Flags RD                    #VNIs    VTEPs 
03:00:00:00:00:00:bb:00:00:01  LR    10.10.20.1:3          1        10.10.20.2(EA) 
03:00:00:00:00:00:bb:00:00:02  LR    10.10.20.1:4          1        10.10.20.2(EA) 
```

```
cumulus@leaf03:mgmt:~$ net show bgp l2vpn evpn es-evi 
Flags: L local, R remote, I inconsistent 
VTEP-Flags: E EAD-per-ES, V EAD-per-EVI 
VNI      ESI                            Flags VTEPs 
2020     03:00:00:00:00:00:bb:00:00:02  LR    10.10.20.2(EV) 
1010     03:00:00:00:00:00:bb:00:00:01  LR    10.10.20.2(EV) 
```

```
cumulus@leaf03:mgmt:~$ net show bgp l2vpn evpn es-vrf 
ES-VRF Flags: A Active 
ESI                            VRF             Flags IPv4-NHG IPv6-NHG Ref 
03:00:00:00:00:00:bb:00:00:01  VRF RED         A     72580647 72580648 1 
03:00:00:00:00:00:bb:00:00:02  VRF GREEN       A     72580645 72580646 1
```

```
cumulus@leaf03:mgmt:~$ net show int bond1 
    Name   MAC                Speed  MTU   Mode 
--  -----  -----------------  -----  ----  ------- 
UP  bond1  48:b0:2d:7d:9c:74  1G     9216  802.3ad 
 
Bond Details 
------------------  -------- 
Bond Mode:          802.3ad 
Load Balancing:     layer3+4 
Minimum Links:      1 
LACP Sys Priority: 
LACP Rate:          1 
LACP Bypass:        Active 
 
All VLANs on L2 Port 
-------------------- 
1010 
 
Untagged 
-------- 
1010 
 
cl-netstat counters 
------------------- 
 RX_OK  RX_ERR  RX_DRP  RX_OVR   TX_OK  TX_ERR  TX_DRP  TX_OVR 
------  ------  ------  ------  ------  ------  ------  ------ 
241819       0       0       0  157114       0       0       0 
 
LLDP Details 
------------ 
LocalPort  RemotePort(RemoteHost) 
---------  --------------------------- 
swp3       48:b0:2d:72:28:ff(server03) 
 
Routing 
------- 
  Interface bond1 is up, line protocol is up 
  Link ups:       2    last: 2023/04/17 08:44:08.84 
  Link downs:     0    last: (never) 
  PTM status: disabled 
  vrf: default 
  index 9 metric 0 mtu 9216 speed 1000 
  flags: <UP,BROADCAST,RUNNING,MULTICAST> 
  Type: Ethernet 
  HWaddr: 48:b0:2d:7d:9c:74 
  Interface Type bond 
  Master interface: br_default PVID: 1010 
  EVPN-MH: ES id 1 ES sysmac 00:00:00:00:00:bb 
  protodown: off (n/a) 
  ARP-ND redirect enabled: ARP 1653 ND 2667 
```

```
cumulus@leaf03:mgmt:~$ net show bgp vrf RED 
show bgp vrf RED ipv4 unicast 
============================= 
BGP table version is 11, local router ID is 10.10.20.1, vrf id 19 
Default local pref 100, local AS 65201 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*  192.168.1.0/24   10.10.10.2<                            0 65299 65210 65110 65199 65102 ? 
*                   10.10.10.1<                            0 65299 65210 65110 65199 65101 ? 
*=                  10.10.10.2<                            0 65299 65210 65110 65199 65102 ? 
*>                  10.10.10.1<                            0 65299 65210 65110 65199 65101 ? 
*  192.168.10.0/24  10.10.20.2<                            0 65299 65202 ? 
*                   10.10.20.2<                            0 65299 65202 ? 
*>                  0.0.0.0                  0         32768 ? 
 
Displayed  2 routes and 7 total paths 
 
show bgp vrf RED ipv6 unicast 
============================= 
No BGP prefixes displayed, 0 exist
```

``` 
cumulus@leaf03:mgmt:~$ net show bgp vrf GREEN 
show bgp vrf GREEN ipv4 unicast 
=============================== 
BGP table version is 10, local router ID is 10.10.20.1, vrf id 13 
Default local pref 100, local AS 65201 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*  192.168.2.0/24   10.10.10.2<                            0 65299 65210 65110 65199 65102 ? 
*                   10.10.10.1<                            0 65299 65210 65110 65199 65101 ? 
*=                  10.10.10.2<                            0 65299 65210 65110 65199 65102 ? 
*>                  10.10.10.1<                            0 65299 65210 65110 65199 65101 ? 
*  192.168.20.0/24  10.10.20.2<                            0 65299 65202 ? 
*                   10.10.20.2<                            0 65299 65202 ? 
*>                  0.0.0.0                  0         32768 ? 
 
Displayed  2 routes and 7 total paths 
 
show bgp vrf GREEN ipv6 unicast 
=============================== 
No BGP prefixes displayed, 0 exist 
```

```
cumulus@leaf03:mgmt:~$ net show route vrf RED 
show ip route vrf RED 
====================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 2d18h01m 
B>* 192.168.1.0/24 [20/0] via 10.10.10.1, vxlan99 (vrf default) onlink, label 4001, weight 1, 00:38:33 
  *                       via 10.10.10.2, vxlan99 (vrf default) onlink, label 4001, weight 1, 00:38:33 
C * 192.168.10.0/24 [0/1024] is directly connected, vlan1010-v0, 02:56:10 
C>* 192.168.10.0/24 is directly connected, vlan1010, 02:56:10 
  
show ipv6 route vrf RED 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 2d18h01m 
C * fe80::/64 is directly connected, vlan1010, 02:56:08 
C * fe80::/64 is directly connected, vlan1010-v0, 02:56:10 
C>* fe80::/64 is directly connected, vlan220_l3, 2d18h01m 
```

```
cumulus@leaf03:mgmt:~$ net show route vrf GREEN 
show ip route vrf GREEN 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 2d18h01m 
B>* 192.168.2.0/24 [20/0] via 10.10.10.1, vxlan99 (vrf default) onlink, label 4002, weight 1, 00:38:36 
  *                       via 10.10.10.2, vxlan99 (vrf default) onlink, label 4002, weight 1, 00:38:36 
C * 192.168.20.0/24 [0/1024] is directly connected, vlan2020-v0, 02:56:13 
C>* 192.168.20.0/24 is directly connected, vlan2020, 02:56:13 
  
show ipv6 route vrf GREEN 
========================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 2d18h01m 
C * fe80::/64 is directly connected, vlan2020, 02:56:12 
C * fe80::/64 is directly connected, vlan2020-v0, 02:56:14 
C>* fe80::/64 is directly connected, vlan370_l3, 2d18h01m 
```

```
cumulus@leaf03:mgmt:~$ net show bgp vrf RED 192.168.10.0/24 
BGP routing table entry for 192.168.10.0/24 
Paths: (3 available, best #3, vrf RED) 
  Not advertised to any peer 
  Imported from 10.10.20.2:6:[5]:[0]:[24]:[192.168.10.0], VNI 5001 
  65299 65202 
    10.10.20.2 from spine03(swp1) (10.10.20.103) announce-nh-self 
      Origin incomplete, valid, external, bestpath-from-AS 65299 
      Extended Community: RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
      Last update: Mon Apr 17 08:46:49 2023 
  Imported from 10.10.20.2:6:[5]:[0]:[24]:[192.168.10.0], VNI 5001 
  65299 65202 
    10.10.20.2 from spine04(swp2) (10.10.20.104) announce-nh-self 
      Origin incomplete, valid, external 
      Extended Community: RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
      Last update: Mon Apr 17 08:46:49 2023 
  Local 
    0.0.0.0 from 0.0.0.0 (10.10.20.1) 
      Origin incomplete, metric 0, weight 32768, valid, sourced, bestpath-from-AS Local, best (Weight) 
      Last update: Mon Apr 17 08:46:48 2023 
```

```
cumulus@leaf03:mgmt:~$ net show bgp vrf RED 192.168.1.0/24 
BGP routing table entry for 192.168.1.0/24 
Paths: (4 available, best #4, vrf RED) 
  Not advertised to any peer 
  Imported from 10.10.10.2:4:[5]:[0]:[24]:[192.168.1.0], VNI 4001 
  65299 65210 65110 65199 65102 
    10.10.10.2 from spine03(swp1) (10.10.20.103) announce-nh-self 
      Origin incomplete, valid, external 
      Extended Community: RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
      Last update: Mon Apr 17 11:04:26 2023 
  Imported from 10.10.10.1:6:[5]:[0]:[24]:[192.168.1.0], VNI 4001 
  65299 65210 65110 65199 65101 
    10.10.10.1 from spine03(swp1) (10.10.20.103) announce-nh-self 
      Origin incomplete, valid, external 
      Extended Community: RT:65101:4001 ET:8 Rmac:44:38:39:22:bb:06 
      Last update: Mon Apr 17 11:04:26 2023 
  Imported from 10.10.10.2:4:[5]:[0]:[24]:[192.168.1.0], VNI 4001 
  65299 65210 65110 65199 65102 
    10.10.10.2 from spine04(swp2) (10.10.20.104) announce-nh-self 
      Origin incomplete, valid, external, multipath 
      Extended Community: RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
      Last update: Mon Apr 17 11:04:24 2023 
  Imported from 10.10.10.1:6:[5]:[0]:[24]:[192.168.1.0], VNI 4001 
  65299 65210 65110 65199 65101 
    10.10.10.1 from spine04(swp2) (10.10.20.104) announce-nh-self 
      Origin incomplete, valid, external, multipath, bestpath-from-AS 65299, best (Older Path) 
      Extended Community: RT:65101:4001 ET:8 Rmac:44:38:39:22:bb:06 
      Last update: Mon Apr 17 11:04:24 2023 
```

```
cumulus@leaf03:mgmt:~$ net show bgp evpn vni 
Advertise Gateway Macip: Disabled 
Advertise SVI Macip: Disabled 
Advertise All VNI flag: Enabled 
BUM flooding: Head-end replication 
VXLAN flooding: Enabled 
Number of L2 VNIs: 2 
Number of L3 VNIs: 2 
Flags: * - Kernel 
  VNI        Type RD                    Import RT                 Export RT                 Tenant VRF 
* 2020       L2   10.10.20.1:2          65201:2020                65201:2020               GREEN 
* 1010       L2   10.10.20.1:9          65201:1010                65201:1010               RED 
* 5002       L3   10.10.20.1:7          0:4002, ...               65201:5002               GREEN 
* 5001       L3   10.10.20.1:8          0:4001, ...               65201:5001               RED 
```

```
cumulus@leaf03:mgmt:~$ net show bgp evpn vni 5001 
VNI: 5001 (known to the kernel) 
  Type: L3 
  Tenant VRF: RED 
  RD: 10.10.20.1:8 
  Originator IP: 10.10.20.1 
  Advertise-gw-macip : n/a 
  Advertise-svi-macip : n/a 
  Advertise-pip: Yes 
  System-IP: 10.10.20.1 
  System-MAC: 44:38:39:22:bb:08 
  Router-MAC: 44:38:39:22:bb:08 
  Import Route Target: 
    0:4001 
    0:5001 
  Export Route Target: 
    65201:5001 
```

```
cumulus@leaf03:mgmt:~$ net show bgp evpn vni 5002 
VNI: 5002 (known to the kernel) 
  Type: L3 
  Tenant VRF: GREEN 
  RD: 10.10.20.1:7 
  Originator IP: 10.10.20.1 
  Advertise-gw-macip : n/a 
  Advertise-svi-macip : n/a 
  Advertise-pip: Yes 
  System-IP: 10.10.20.1 
  System-MAC: 44:38:39:22:bb:08 
  Router-MAC: 44:38:39:22:bb:08 
  Import Route Target: 
    0:4002 
    0:5002 
  Export Route Target: 
    65201:5002 
```

```
cumulus@leaf03:mgmt:~$ net show evpn mac vni all 
VNI 1010 #MACs (local and remote) 5 
 
Flags: B=bypass N=sync-neighs, I=local-inactive, P=peer-active, X=peer-proxy 
MAC               Type   Flags Intf/Remote ES/VTEP            VLAN  Seq #'s 
48:b0:2d:72:28:ff local  P     bond1                          1010  0/0 
48:b0:2d:82:05:04 local  P     bond1                          1010  0/0 
b6:4b:0f:ea:f2:02 local  NP    bond1                          1010  0/0 
44:38:39:22:bb:09 remote       10.10.20.2                           0/0 
44:38:39:22:bb:08 local        vlan1010                             0/0 
 
VNI 2020 #MACs (local and remote) 5 
 
Flags: B=bypass N=sync-neighs, I=local-inactive, P=peer-active, X=peer-proxy 
MAC               Type   Flags Intf/Remote ES/VTEP            VLAN  Seq #'s 
ee:54:69:be:3a:3f local  NP    bond2                          2020  0/0 
48:b0:2d:75:8e:7a local  P     bond2                          2020  0/0 
44:38:39:22:bb:09 remote       10.10.20.2                           0/0 
48:b0:2d:a7:e2:6e local  P     bond2                          2020  0/0 
44:38:39:22:bb:08 local        vlan2020                             0/0 
```

```
cumulus@leaf04:mgmt:~$ net show bgp sum 
show bgp ipv4 unicast summary 
============================= 
BGP router identifier 10.10.20.2, local AS number 65202 vrf-id 0 
BGP table version 21 
RIB entries 23, using 4600 bytes of memory 
Peers 2, using 46 KiB of memory 
 
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
spine03(swp1)   4      65299       229       236        0    0    0 00:08:42           10       12 
spine04(swp2)   4      65299       224       231        0    0    0 00:08:34           10       12 
 
Total number of neighbors 2 
 
show bgp ipv6 unicast summary 
============================= 
% No BGP neighbors found 
 
show bgp l2vpn evpn summary 
=========================== 
BGP router identifier 10.10.20.2, local AS number 65202 vrf-id 0 
BGP table version 0 
RIB entries 31, using 6200 bytes of memory 
Peers 2, using 46 KiB of memory 
 
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
spine03(swp1)   4      65299       229       236        0    0    0 00:08:42           25       46 
spine04(swp2)   4      65299       224       231        0    0    0 00:08:34           25       46 
 
Total number of neighbors 2
```

```
cumulus@leaf04:mgmt:~$ net show bgp vrf RED 
show bgp vrf RED ipv4 unicast 
============================= 
BGP table version is 2, local router ID is 10.10.20.2, vrf id 19 
Default local pref 100, local AS 65202 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*  192.168.1.0/24   10.10.10.2<                            0 65299 65210 65110 65199 65102 ? 
*                   10.10.10.1<                            0 65299 65210 65110 65199 65101 ? 
*=                  10.10.10.2<                            0 65299 65210 65110 65199 65102 ? 
*>                  10.10.10.1<                            0 65299 65210 65110 65199 65101 ? 
*  192.168.10.0/24  10.10.20.1<                            0 65299 65201 ? 
*                   10.10.20.1<                            0 65299 65201 ? 
*>                  0.0.0.0                  0         32768 ? 
 
Displayed  2 routes and 7 total paths 
 
show bgp vrf RED ipv6 unicast 
============================= 
No BGP prefixes displayed, 0 exist 
```

```
cumulus@leaf04:mgmt:~$ net show bgp vrf GREEN 
show bgp vrf GREEN ipv4 unicast 
=============================== 
BGP table version is 2, local router ID is 10.10.20.2, vrf id 13 
Default local pref 100, local AS 65202 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*  192.168.2.0/24   10.10.10.2<                            0 65299 65210 65110 65199 65102 ? 
*                   10.10.10.1<                            0 65299 65210 65110 65199 65101 ? 
*=                  10.10.10.2<                            0 65299 65210 65110 65199 65102 ? 
*>                  10.10.10.1<                            0 65299 65210 65110 65199 65101 ? 
*  192.168.20.0/24  10.10.20.1<                            0 65299 65201 ? 
*                   10.10.20.1<                            0 65299 65201 ? 
*>                  0.0.0.0                  0         32768 ? 
 
Displayed  2 routes and 7 total paths 
 
show bgp vrf GREEN ipv6 unicast 
=============================== 
No BGP prefixes displayed, 0 exist 
```

```
cumulus@leaf04:mgmt:~$ net show route vrf RED 
show ip route vrf RED 
====================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 00:09:06 
B>* 192.168.1.0/24 [20/0] via 10.10.10.1, vxlan99 (vrf default) onlink, label 4001, weight 1, 00:09:03 
  *                       via 10.10.10.2, vxlan99 (vrf default) onlink, label 4001, weight 1, 00:09:03 
C * 192.168.10.0/24 [0/1024] is directly connected, vlan1010-v0, 00:09:06 
C>* 192.168.10.0/24 is directly connected, vlan1010, 00:09:06 
  
show ipv6 route vrf RED 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 00:09:06 
C * fe80::/64 is directly connected, vlan220_l3, 00:09:05 
C * fe80::/64 is directly connected, vlan1010, 00:09:06 
C>* fe80::/64 is directly connected, vlan1010-v0, 00:09:06 
```

```
cumulus@leaf04:mgmt:~$ net show route vrf GREEN 
show ip route vrf GREEN 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIP, 
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP, 
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP, 
       F - PBR, f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 00:09:13 
B>* 192.168.2.0/24 [20/0] via 10.10.10.1, vxlan99 (vrf default) onlink, label 4002, weight 1, 00:09:10 
  *                       via 10.10.10.2, vxlan99 (vrf default) onlink, label 4002, weight 1, 00:09:10 
C * 192.168.20.0/24 [0/1024] is directly connected, vlan2020-v0, 00:09:13 
C>* 192.168.20.0/24 is directly connected, vlan2020, 00:09:13 
  
show ipv6 route vrf GREEN 
========================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF GREEN: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 00:09:13 
C * fe80::/64 is directly connected, vlan370_l3, 00:09:13 
C * fe80::/64 is directly connected, vlan2020-v0, 00:09:13 
C>* fe80::/64 is directly connected, vlan2020, 00:09:13 
```

```
cumulus@leaf04:mgmt:~$ net show evpn es 
Type: B bypass, L local, R remote, N non-DF 
ESI                            Type ES-IF                 VTEPs 
03:00:00:00:00:00:bb:00:00:01  LRN  bond1                 10.10.20.1 
03:00:00:00:00:00:bb:00:00:02  LRN  bond2                 10.10.20.1 
```

```
cumulus@leaf04:mgmt:~$ net show bgp l2vpn evpn es 
ES Flags: B - bypass, L local, R remote, I inconsistent 
VTEP Flags: E ESR/Type-4, A active nexthop 
ESI                            Flags RD                    #VNIs    VTEPs 
03:00:00:00:00:00:bb:00:00:01  LR    10.10.20.2:3          1        10.10.20.1(EA) 
03:00:00:00:00:00:bb:00:00:02  LR    10.10.20.2:4          1        10.10.20.1(EA) 
```

```
cumulus@leaf04:mgmt:~$ net show bgp l2vpn evpn es-evi 
Flags: L local, R remote, I inconsistent 
VTEP-Flags: E EAD-per-ES, V EAD-per-EVI 
VNI      ESI                            Flags VTEPs 
2020     03:00:00:00:00:00:bb:00:00:02  LR    10.10.20.1(EV) 
1010     03:00:00:00:00:00:bb:00:00:01  LR    10.10.20.1(EV) 
```

```
cumulus@leaf04:mgmt:~$ net show bgp l2vpn evpn es-vrf 
ES-VRF Flags: A Active 
ESI                            VRF             Flags IPv4-NHG IPv6-NHG Ref 
03:00:00:00:00:00:bb:00:00:01  VRF RED         A     72580645 72580646 1 
03:00:00:00:00:00:bb:00:00:02  VRF GREEN       A     72580647 72580648 1 
```

```
cumulus@leaf04:mgmt:~$ net show bgp evpn vni 
Advertise Gateway Macip: Disabled 
Advertise SVI Macip: Disabled 
Advertise All VNI flag: Enabled 
BUM flooding: Head-end replication 
VXLAN flooding: Enabled 
Number of L2 VNIs: 2 
Number of L3 VNIs: 2 
Flags: * - Kernel 
  VNI        Type RD                    Import RT                 Export RT                 Tenant VRF 
* 2020       L2   10.10.20.2:2          65202:2020                65202:2020               GREEN 
* 1010       L2   10.10.20.2:9          65202:1010                65202:1010               RED 
* 5002       L3   10.10.20.2:7          0:4002, ...               65202:5002               GREEN 
* 5001       L3   10.10.20.2:8          0:4001, ...               65202:5001               RED 
```

```
cumulus@leaf04:mgmt:~$ net show int bond1 
    Name   MAC                Speed  MTU   Mode 
--  -----  -----------------  -----  ----  ------- 
UP  bond1  48:b0:2d:84:e8:0f  1G     9216  802.3ad 
 
Bond Details 
------------------  -------- 
Bond Mode:          802.3ad 
Load Balancing:     layer3+4 
Minimum Links:      1 
LACP Sys Priority: 
LACP Rate:          1 
LACP Bypass:        Active 
 
All VLANs on L2 Port 
-------------------- 
1010 
 
Untagged 
-------- 
1010 
 
cl-netstat counters 
------------------- 
RX_OK  RX_ERR  RX_DRP  RX_OVR  TX_OK  TX_ERR  TX_DRP  TX_OVR 
-----  ------  ------  ------  -----  ------  ------  ------ 
  481       0       0       0    257       0       0       0 
 
LLDP Details 
------------ 
LocalPort  RemotePort(RemoteHost) 
---------  --------------------------- 
swp3       48:b0:2d:82:05:04(server03) 
 
Routing 
------- 
  Interface bond1 is up, line protocol is up 
  Link ups:       1    last: 2023/04/17 11:51:10.75 
  Link downs:     0    last: (never) 
  PTM status: disabled 
  vrf: default 
  index 10 metric 0 mtu 9216 speed 1000 
  flags: <UP,BROADCAST,RUNNING,MULTICAST> 
  Type: Ethernet 
  HWaddr: 48:b0:2d:84:e8:0f 
  Interface Type bond 
  Master interface: br_default PVID: 1010 
  EVPN-MH: ES id 1 ES sysmac 00:00:00:00:00:bb 
  protodown: off (n/a) 
  ARP-ND redirect enabled: ARP 1 ND 8 
```

```
cumulus@leaf04:mgmt:~$ net show bgp evpn vni 5001 
VNI: 5001 (known to the kernel) 
  Type: L3 
  Tenant VRF: RED 
  RD: 10.10.20.2:8 
  Originator IP: 10.10.20.2 
  Advertise-gw-macip : n/a 
  Advertise-svi-macip : n/a 
  Advertise-pip: Yes 
  System-IP: 10.10.20.2 
  System-MAC: 44:38:39:22:bb:09 
  Router-MAC: 44:38:39:22:bb:09 
  Import Route Target: 
    0:4001 
    0:5001 
  Export Route Target: 
    65202:5001 
```

```
cumulus@leaf04:mgmt:~$ net show bgp evpn vni 5002 
VNI: 5002 (known to the kernel) 
  Type: L3 
  Tenant VRF: GREEN 
  RD: 10.10.20.2:7 
  Originator IP: 10.10.20.2 
  Advertise-gw-macip : n/a 
  Advertise-svi-macip : n/a 
  Advertise-pip: Yes 
  System-IP: 10.10.20.2 
  System-MAC: 44:38:39:22:bb:09 
  Router-MAC: 44:38:39:22:bb:09 
  Import Route Target: 
    0:4002 
    0:5002 
  Export Route Target: 
    65202:5002 
```

```
cumulus@leaf04:mgmt:~$ net show evpn mac vni all 
VNI 1010 #MACs (local and remote) 5 
 
Flags: B=bypass N=sync-neighs, I=local-inactive, P=peer-active, X=peer-proxy 
MAC               Type   Flags Intf/Remote ES/VTEP            VLAN  Seq #'s 
48:b0:2d:72:28:ff local  P     bond1                          1010  0/0 
48:b0:2d:82:05:04 local  P     bond1                          1010  0/0 
b6:4b:0f:ea:f2:02 local  NP    bond1                          1010  0/0 
44:38:39:22:bb:09 local        vlan1010                             0/0 
44:38:39:22:bb:08 remote       10.10.20.1                           0/0 
 
VNI 2020 #MACs (local and remote) 5 
 
Flags: B=bypass N=sync-neighs, I=local-inactive, P=peer-active, X=peer-proxy 
MAC               Type   Flags Intf/Remote ES/VTEP            VLAN  Seq #'s 
ee:54:69:be:3a:3f local  NP    bond2                          2020  0/0 
48:b0:2d:75:8e:7a local  P     bond2                          2020  0/0 
44:38:39:22:bb:09 local        vlan2020                             0/0 
48:b0:2d:a7:e2:6e local  P     bond2                          2020  0/0 
44:38:39:22:bb:08 remote       10.10.20.1                           0/0 
```
</div>

To verify that the bridge `br_default` is learning MAC address entries:

<div class=scroll>

```
cumulus@leaf03:mgmt:~$ nv show bridge domain br_default mac-table 
    age  bridge-domain  entry-type  interface   last-update  MAC address        src-vni  vlan  vni   Summary 
--  ---  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  ---------------------- 
0   27   br_default     static      bond2       725          48:b0:2d:75:8e:7a           2020 
1   867  br_default     static      bond2       867          48:b0:2d:a7:e2:6e           2020 
2   63   br_default     static      bond2       867          ee:54:69:be:3a:3f           2020 
3   874  br_default     permanent   bond2       874          48:b0:2d:d5:d5:91 
4   27   br_default     static      bond1       725          48:b0:2d:72:28:ff           1010 
5   867  br_default     static      bond1       867          48:b0:2d:82:05:04           1010 
6   189  br_default     static      bond1       867          b6:4b:0f:ea:f2:02           1010 
7   874  br_default     permanent   bond1       874          48:b0:2d:7d:9c:74 
8   725  br_default                 vxlan48     189          44:38:39:22:bb:09           1010  None  remote-dst: 10.10.20.2 
9   874  br_default     permanent   vxlan48     874          ca:e9:d5:f3:4b:b9                 None 
10  725                 permanent   vxlan48     2            00:00:00:00:00:00  2020           None  remote-dst: 10.10.20.2 
11                      permanent   br_default               00:00:5e:00:01:14 
12  874  br_default     permanent   br_default  874          44:38:39:22:bb:08           1010 
```

```  
cumulus@leaf04:mgmt:~$ nv show bridge domain br_default mac-table 
    age  bridge-domain  entry-type  interface   last-update  MAC address        src-vni  vlan  vni   Summary 
--  ---  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  ---------------------- 
0   725  br_default     static      bond2       725          48:b0:2d:75:8e:7a           2020 
1   2    br_default     static      bond2       725          48:b0:2d:a7:e2:6e           2020 
2   180  br_default     static      bond2       725          ee:54:69:be:3a:3f           2020 
3   729  br_default     permanent   bond2       729          48:b0:2d:95:3f:b0 
4   725  br_default                 vxlan48     725          44:38:39:22:bb:08           2020  None  remote-dst: 10.10.20.1 
5   729  br_default     permanent   vxlan48     729          52:d0:7e:cf:6e:ac                 None 
6   725                 permanent   vxlan48     43           00:00:00:00:00:00  1010           None  remote-dst: 10.10.20.1 
7   725  br_default     static      bond1       725          48:b0:2d:72:28:ff           1010 
8   59   br_default     static      bond1       725          b6:4b:0f:ea:f2:02           1010 
9   2    br_default     static      bond1       725          48:b0:2d:82:05:04           1010 
10  729  br_default     permanent   bond1       729          48:b0:2d:84:e8:0f 
11                      permanent   br_default               00:00:5e:00:01:14 
12  729  br_default     permanent   br_default  729          44:38:39:22:bb:09           1010 
```
</div>

From the table above, locate the layer 3 VLAN interface MAC address and the VRR MAC address:

<div class=scroll>

```
cumulus@leaf03:mgmt:~$ nv show int vlan1010 | grep mac 
    mac-address                              auto 
    mac-id                                   none 
  mac                     44:38:39:22:bb:08 
```

```
cumulus@leaf03:mgmt:~$ nv show int vlan1010 ip vrr 
             operational        applied 
-----------  -----------------  ----------------- 
enable                          on 
mac-address  00:00:5e:00:01:14  auto 
mac-id                          none 
[address]    192.168.10.100/24  192.168.10.100/24 
state        up                 up 
```

```
cumulus@leaf04:mgmt:~$ nv show int vlan1010 | grep mac 
    mac-address                              auto 
    mac-id                                   none 
  mac                     44:38:39:22:bb:09 
```

```
cumulus@leaf04:mgmt:~$ nv show int vlan1010 ip vrr 
             operational        applied 
-----------  -----------------  ----------------- 
enable                          on 
mac-address  00:00:5e:00:01:14  auto 
mac-id                          none 
[address]    192.168.10.100/24  192.168.10.100/24 
state        up                 up 
```
</div>

To verify EVPN type-5 routes at the ingress PE (leaf03) for the end host *192.168.1.10* connected to leaf01 and leaf02:

<div class=scroll>

```
cumulus@leaf03:mgmt:~$ net show bgp evpn route type 5 | grep 192.168.1\. -A 4 -B 1 
Route Distinguisher: 10.10.10.1:6 
*  [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.1:6 
                    10.10.10.1 (spine03) 
                                                           0 65299 65210 65110 65199 65101 ? 
                    RT:65101:4001 ET:8 Rmac:44:38:39:22:bb:06 
*> [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.1:6 
                    10.10.10.1 (spine04) 
                                                           0 65299 65210 65110 65199 65101 ? 
                    RT:65101:4001 ET:8 Rmac:44:38:39:22:bb:06 
Route Distinguisher: 10.10.10.2:4 
*  [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.2:4 
                    10.10.10.2 (spine03) 
                                                           0 65299 65210 65110 65199 65102 ? 
                    RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
*> [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.2:4 
                    10.10.10.2 (spine04) 
                                                           0 65299 65210 65110 65199 65102 ? 
                    RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
Route Distinguisher: 10.10.10.2:5 
```
</div>

Verify EVPN type-5 routes at the egress PE (leaf01) for the end host *192.168.1.10* connected to leaf01 and leaf02:

<div class=scroll>

```
cumulus@leaf01:mgmt:~$ net show bgp evpn route type 5 | grep 192.168.1\. -A 4 -B 1 
Route Distinguisher: 10.10.10.1:6 
*> [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.1:6 
                    10.10.10.1 (leaf01) 
                                             0         32768 ? 
                    ET:8 RT:65101:4001 Rmac:44:38:39:22:bb:06 
Route Distinguisher: 10.10.10.2:4 
*  [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.2:4 
                    10.10.10.2 (spine02) 
                                                           0 65199 65102 ? 
                    RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
*> [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.2:4 
                    10.10.10.2 (spine01) 
                                                           0 65199 65102 ? 
                    RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
Route Distinguisher: 10.10.10.2:5 
-- 
```
</div>

To view routing from the border leaf:

<div class=scroll>

```
cumulus@borderleaf04:mgmt:~$ net show bgp sum 
show bgp ipv4 unicast summary 
============================= 
BGP router identifier 10.10.20.11, local AS number 65210 vrf-id 0 
BGP table version 18 
RIB entries 19, using 3800 bytes of memory 
Peers 3, using 68 KiB of memory 
Peer groups 2, using 128 bytes of memory 
 
Neighbor           V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
borderleaf01(swp3) 4      65110      1260      1263        0    0    0 01:01:26            5       10 
spine03(swp1)      4      65299      1341      1345        0    0    0 01:01:24            4       10 
spine04(swp2)      4      65299      1340      1343        0    0    0 01:01:16            4       10 
 
Total number of neighbors 3 
 
show bgp ipv6 unicast summary 
============================= 
% No BGP neighbors found 
 
show bgp l2vpn evpn summary 
=========================== 
BGP router identifier 10.10.20.11, local AS number 65210 vrf-id 0 
BGP table version 0 
RIB entries 35, using 7000 bytes of memory 
Peers 3, using 68 KiB of memory 
Peer groups 2, using 128 bytes of memory 
 
Neighbor           V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt 
borderleaf01(swp3) 4      65110      1260      1263        0    0    0 01:01:26            4        8 
spine03(swp1)      4      65299      1342      1346        0    0    0 01:01:24           42       46 
spine04(swp2)      4      65299      1340      1343        0    0    0 01:01:16           42       46 
 
Total number of neighbors 3
```

``` 
cumulus@borderleaf04:mgmt:~$ net show bgp vrf RED 
show bgp vrf RED ipv4 unicast 
============================= 
BGP table version is 11, local router ID is 10.10.20.11, vrf id 13 
Default local pref 100, local AS 65210 
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath, 
               i internal, r RIB-failure, S Stale, R Removed 
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self 
Origin codes:  i - IGP, e - EGP, ? - incomplete 
 
   Network          Next Hop            Metric LocPrf Weight Path 
*= 192.168.1.0/24   10.10.10.2<                            0 65110 65199 65102 ? 
*>                  10.10.10.1<                            0 65110 65199 65101 ? 
*= 192.168.10.0/24  10.10.20.2<                            0 65299 65202 ? 
*                   10.10.20.2<                            0 65299 65202 ? 
*>                  10.10.20.1<                            0 65299 65201 ? 
*                   10.10.20.1<                            0 65299 65201 ? 
*= 192.168.10.110/32 
                    10.10.20.2<                            0 65299 65202 i 
*                   10.10.20.2<                            0 65299 65202 i 
*>                  10.10.20.1<                            0 65299 65201 i 
*                   10.10.20.1<                            0 65299 65201 i 
 
Displayed  3 routes and 10 total paths 

show bgp vrf RED ipv6 unicast 
============================= 
No BGP prefixes displayed, 0 exist
```

```
cumulus@borderleaf04:mgmt:~$ net show bgp evpn route type 5 | grep 192.168.1\. -A 3 -B 1 
Route Distinguisher: 10.10.10.1:6 
*> [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.1:6 
                    10.10.10.1 (borderleaf01) 
                                                           0 65110 65199 65101 ? 
                    RT:65101:4001 ET:8 Rmac:44:38:39:22:bb:06 
Route Distinguisher: 10.10.10.2:4 
*> [5]:[0]:[24]:[192.168.1.0] RD 10.10.10.2:4 
                    10.10.10.2 (borderleaf01) 
                                                           0 65110 65199 65102 ? 
                    RT:65102:4001 ET:8 Rmac:44:38:39:22:bb:07 
-- 
Route Distinguisher: 10.10.20.1:8 
*  [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.1:8 
                    10.10.20.1 (spine03) 
                                                           0 65299 65201 ? 
                    RT:65201:5001 ET:8 Rmac:44:38:39:22:bb:08 
*> [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.1:8 
                    10.10.20.1 (spine04) 
                                                           0 65299 65201 ? 
                    RT:65201:5001 ET:8 Rmac:44:38:39:22:bb:08 
-- 
Route Distinguisher: 10.10.20.2:8 
*  [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.2:8 
                    10.10.20.2 (spine04) 
                                                           0 65299 65202 ? 
                    RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
*> [5]:[0]:[24]:[192.168.10.0] RD 10.10.20.2:8 
                    10.10.20.2 (spine03) 
                                                           0 65299 65202 ? 
                    RT:65202:5001 ET:8 Rmac:44:38:39:22:bb:09 
```
</div>

{{< /tab >}}
{{< /tabs >}}
