---
title: Layer 2 Extensions
author: NVIDIA
weight: 40
product: Technical Guides
imgData: guides
---
<style>
  .scroll{
    height: 500px;
    overflow-y: auto;
  }
</style>
Layer 2 extension from one data center to another typically supports an application or a system that requires layer 2 adjacency. Some legacy applications require layer 2 adjacency for their operations and those systems, although fewer and fewer, continue to exist in enterprise environments.

With the modern era of cloud computing, extending layer 2 domains across long distances is no longer a typical use case; consider this option as a last resort when you have no other way of solving organizational and technical problems other than extending layer 2 across geographically separated data centers.

Layer 2 extensions are undesirable for the following reasons:
- They can increase the chances of creating topological asymmetries.
- Broadcast and multicast storms risk extending from one data center to others.
- They can increase <span style="background-color:#F5F5DC">[MTTR](## "Mean Time to Recovery")</span>.
- They are difficult to troubleshoot compared to a layer 3 extension because there is no clear demarcation between layer 2 and layer 3.
- They require a layer 2 loop detection system on all ToR and leaf switches.  

By limiting the scope of the layer 2 network, you reduce the potential impact when problems occur. If it is not possible to avoid a layer 2 extension, it is crucial to keep the extended layer 2 broadcast domains to a minimum to limit MAC address advertisements and withdrawals. Extending layer 2 domains is the same as merging multiple broadcast domains; it creates a geographically separated large broadcast domain that is interconnected through a complex network over a distance.

Extending a layer 2 segment from one data center to another involves extending EVPN type-2 (MAC and IP address) routes for individual MAC addresses and type-3 (Inclusive Multicast) routes for <span style="background-color:#F5F5DC">[BUM](## "Broadcast, Unknown-Unicast, and Multicast")</span>  traffic. In modern EVPN and VXLAN environments with multihoming, extending type-1 (Ethernet Auto Discovery) routes and type-4 (Ethernet Segment) routes is equally essential.

## Configuration

{{<img src="/images/guides/dci-reference-topology.png">}}

DCI 1|DCI 2|
|--|--|
|<table> </tr><tr><td>VRF</td><td>RED</td></tr><td>Layer 2 VNI</td><td>10</tr><td>Layer 3 VNI</td><td>4001</td></tr></table>| <table> </tr><tr><td>VRF</td><td>RED</td></tr><td>Layer 2 VNI</td><td>10</tr><td>Layer 3 VNI</td><td>4001</td></tr> </table>|
|<table> </tr><tr><td>VRF</td><td>GREEN</td></tr><td>Layer 2 VNI</td><td>20</tr><td>Layer 3 VNI</td><td>4002</td></tr></table>| <table> </tr><tr><td>VRF</td><td>GREEN</td></tr><td>Layer 2 VNI</td><td>20</tr><td>Layer 3 VNI</td><td>4002</td></tr> </table>|

This example configuration interconnects VLAN ID 10 in DC1 with VLAN ID 10 in DC2 using EVPN and VXLAN layer 2 stretch. The route target import statements connect two RED VRFs to each other and provide connectivity between server01 and server03 within the RED VRF, and server02 and server04 within the GREEN VRF. The RED and GREEN VRFs cannot communicate with each other. server01 and server03 are in the same broadcast domain as server02 and server04. From a layer 2 perspective, they are adjacent hosts. The servers include each other’s MAC addresses in their ARP cache.

The example also configures multiple ESIs across the fabric, which must be unique.

{{< tabs "TabID40 ">}}
{{< tab "server01 ">}}

<div class=scroll>

```
ubuntu@server01:~$ cat /etc/netplan/config.yaml 
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

ubuntu@server01:~$ ip address 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00 
    inet 127.0.0.1/8 scope host lo 
       valid_lft forever preferred_lft forever 
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever 
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 
    link/ether 44:38:39:22:aa:01 brd ff:ff:ff:ff:ff:ff 
    inet 192.168.200.20/24 brd 192.168.200.255 scope global dynamic eth0 
       valid_lft 172619sec preferred_lft 172619sec 
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
          addresses: [192.168.1.110/24] 
          gateway4: 192.168.1.100 
          routes: 
          - to: 192.168.0.0/16 
            via: 192.168.1.100 
          parameters: 
              mode: 802.3ad 
 
ubuntu@server03:~$ ip address 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00 
    inet 127.0.0.1/8 scope host lo 
       valid_lft forever preferred_lft forever 
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever 
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 
    link/ether 44:38:39:22:aa:03 brd ff:ff:ff:ff:ff:ff 
    inet 192.168.200.22/24 brd 192.168.200.255 scope global dynamic eth0 
       valid_lft 172451sec preferred_lft 172451sec 
    inet6 fe80::4638:39ff:fe22:aa03/64 scope link 
       valid_lft forever preferred_lft forever 
3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc fq_codel master bond0 state UP group default qlen 1000 
    link/ether b6:4b:0f:ea:f2:02 brd ff:ff:ff:ff:ff:ff 
4: eth2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc fq_codel master bond0 state UP group default qlen 1000 
    link/ether b6:4b:0f:ea:f2:02 brd ff:ff:ff:ff:ff:ff 
5: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000 
    link/ether b6:4b:0f:ea:f2:02 brd ff:ff:ff:ff:ff:ff 
    inet 192.168.1.110/24 brd 192.168.1.255 scope global bond0 
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
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp enable on 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp route-export to-evpn route-target auto 
cumulus@leaf01:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target 65101:4002 
cumulus@leaf01:mgmt:~$ nv set vrf RED evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED evpn vni 4001 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp enable on 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp route-export to-evpn route-target auto 
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target 65101:4001 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 address-family l2vpn-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 remote-as external 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 type unnumbered 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 address-family l2vpn-evpn enable on 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 remote-as external 
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 type unnumbered  
```
</div>

{{< /tab >}}
{{< tab "spine01 ">}}

<div class=scroll>

```
cumulus@spine01:mgmt:~$ nv set interface eth0 ip vrf mgmt 
cumulus@spine01:mgmt:~$ nv set interface lo ip address 10.10.10.101/32 
cumulus@spine01:mgmt:~$ nv set router bgp autonomous-system 65199 
cumulus@spine01:mgmt:~$ nv set router bgp enable on 
cumulus@spine01:mgmt:~$ nv set router bgp router-id 10.10.10.101 
cumulus@spine01:mgmt:~$ nv set system config auto-save enable on 
cumulus@spine01:mgmt:~$ nv set system hostname spine01 
cumulus@spine01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@spine01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32 
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
cumulus@borderleaf01:mgmt:~$ nv set service lldp 
cumulus@borderleaf01:mgmt:~$ nv set system config auto-save enable on 
cumulus@borderleaf01:mgmt:~$ nv set system global anycast-id 10 
cumulus@borderleaf01:mgmt:~$ nv set system global fabric-id 10 
cumulus@borderleaf01:mgmt:~$ nv set system hostname borderleaf01 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.10/32 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 remote-as external 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp1 type unnumbered 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 remote-as external 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp2 type unnumbered 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp3 peer-group dci_group1 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp neighbor swp3 type unnumbered 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 remote-as external 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@borderleaf01:mgmt:~$ nv set vrf default router bgp peer-group underlay remote-as external 
```
</div>

{{< /tab >}}
{{< tab "leaf03 ">}}

<div class=scroll>

```
cumulus@leaf03:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10 
cumulus@leaf03:mgmt:~$ nv set bridge domain br_default vlan 20 vni 20 
cumulus@leaf03:mgmt:~$ nv set evpn enable on 
cumulus@leaf03:mgmt:~$ nv set evpn multihoming enable on 
cumulus@leaf03:mgmt:~$ nv set interface bond1 bond member swp3 
cumulus@leaf03:mgmt:~$ nv set interface bond1 bridge domain br_default access 10 
cumulus@leaf03:mgmt:~$ nv set interface bond1 evpn multihoming segment local-id 1 
cumulus@leaf03:mgmt:~$ nv set interface bond1-2 bond lacp-bypass on 
cumulus@leaf03:mgmt:~$ nv set interface bond1-2 evpn multihoming segment df-preference 50000 
cumulus@leaf03:mgmt:~$ nv set interface bond1-2 evpn multihoming segment enable on 
cumulus@leaf03:mgmt:~$ nv set interface bond1-2 evpn multihoming segment mac-address 00:00:00:00:00:BB 
cumulus@leaf03:mgmt:~$ nv set interface bond1-2 type bond 
cumulus@leaf03:mgmt:~$ nv set interface bond2 bond member swp4 
cumulus@leaf03:mgmt:~$ nv set interface bond2 bridge domain br_default access 20 
cumulus@leaf03:mgmt:~$ nv set interface bond2 evpn multihoming segment local-id 2 
cumulus@leaf03:mgmt:~$ nv set interface eth0 ip vrf mgmt 
cumulus@leaf03:mgmt:~$ nv set interface eth0 type eth 
cumulus@leaf03:mgmt:~$ nv set interface lo ip address 10.10.20.1/32 
cumulus@leaf03:mgmt:~$ nv set interface lo type loopback 
cumulus@leaf03:mgmt:~$ nv set interface swp1-2 evpn multihoming uplink on 
cumulus@leaf03:mgmt:~$ nv set interface swp1-2 type swp 
cumulus@leaf03:mgmt:~$ nv set interface vlan10 ip address 192.168.1.101/24 
cumulus@leaf03:mgmt:~$ nv set interface vlan10 ip vrf RED 
cumulus@leaf03:mgmt:~$ nv set interface vlan10 ip vrr address 192.168.1.100/24 
cumulus@leaf03:mgmt:~$ nv set interface vlan10 vlan 10 
cumulus@leaf03:mgmt:~$ nv set interface vlan10,20 ip vrr enable on 
cumulus@leaf03:mgmt:~$ nv set interface vlan10,20 ip vrr state up 
cumulus@leaf03:mgmt:~$ nv set interface vlan10,20 type svi 
cumulus@leaf03:mgmt:~$ nv set interface vlan20 ip address 192.168.2.101/24 
cumulus@leaf03:mgmt:~$ nv set interface vlan20 ip vrf GREEN 
cumulus@leaf03:mgmt:~$ nv set interface vlan20 ip vrr address 192.168.2.100/24 
cumulus@leaf03:mgmt:~$ nv set interface vlan20 vlan 20 
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
cumulus@leaf03:mgmt:~$ nv set vrf GREEN evpn vni 4002 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp enable on 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp route-export to-evpn route-target auto 
cumulus@leaf03:mgmt:~$ nv set vrf GREEN router bgp route-import from-evpn route-target 65201:4002 
cumulus@leaf03:mgmt:~$ nv set vrf RED evpn enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED evpn vni 4001 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp enable on 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp route-export to-evpn route-target auto 
cumulus@leaf03:mgmt:~$ nv set vrf RED router bgp route-import from-evpn route-target 65201:4001 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on 
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.20.1/32 
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
cumulus@spine03:mgmt:~$ nv set interface lo ip address 10.10.20.103/32
cumulus@spine03:mgmt:~$ nv set router bgp autonomous-system 65299
cumulus@spine03:mgmt:~$ nv set router bgp enable on
cumulus@spine03:mgmt:~$ nv set router bgp router-id 10.10.20.103
cumulus@spine03:mgmt:~$ nv set system config auto-save enable on
cumulus@spine03:mgmt:~$ nv set system hostname spine03
cumulus@spine03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on
cumulus@spine03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.20.103/32
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
cumulus@borderleaf04:mgmt:~$ nv set service lldp 
cumulus@borderleaf04:mgmt:~$ nv set system config auto-save enable on 
cumulus@borderleaf04:mgmt:~$ nv set system global anycast-id 20 
cumulus@borderleaf04:mgmt:~$ nv set system global fabric-id 20 
cumulus@borderleaf04:mgmt:~$ nv set system hostname borderleaf04 
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
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 address-family l2vpn-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group dci_group1 remote-as external 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on 
cumulus@borderleaf04:mgmt:~$ nv set vrf default router bgp peer-group underlay remote-as external 
```
</div>

{{< /tab >}}
{{< /tabs >}}

## Diagnostic Commands

The following commands can troubleshoot and validate the DCI configuration.

{{< tabs "TabID426 ">}}
{{< tab "DC1 ">}}

<div class=scroll>

```
cumulus@leaf01:mgmt:~$ net show evpn es detail 
ESI: 03:00:00:00:00:00:aa:00:00:01 
 Type: Local,Remote 
 Interface: bond1 
 State: up 
 Bridge port: yes 
 Ready for BGP: yes 
 VNI Count: 1 
 MAC Count: 2 
 DF status: df 
 DF preference: 50000 
 Nexthop group: 536870913 
 VTEPs: 
     10.10.10.2(local) df_alg: preference df_pref: 10000 sph: tc-filter 
 nh: 268435459 
 
ESI: 03:00:00:00:00:00:aa:00:00:02 
 Type: Local,Remote 
 Interface: bond2 
 State: up 
 Bridge port: yes 
 Ready for BGP: yes 
 VNI Count: 1 
 MAC Count: 2 
 DF status: df 
 DF preference: 50000 
 Nexthop group: 536870914 
 VTEPs: 
     10.10.10.2(local) df_alg: preference df_pref: 10000 sph: tc-filter 
 nh: 268435459 
 
ESI: 03:00:00:00:00:00:bb:00:00:01 
 Type: Remote 
 Interface: - 
 Ready for BGP: no 
 VNI Count: 0 
 MAC Count: 3 
 DF preference: 0 
 Nexthop group: 536870918 
 VTEPs: 
     10.10.20.1 nh: 268435463 
     10.10.20.2 nh: 268435461 
 
ESI: 03:00:00:00:00:00:bb:00:00:02 
 Type: Remote 
 Interface: - 
 Ready for BGP: no 
 VNI Count: 0 
 MAC Count: 3 
 DF preference: 0 
 Nexthop group: 536870916 
 VTEPs: 
     10.10.20.1 nh: 268435463 
     10.10.20.2 nh: 268435461
```

``` 
cumulus@leaf01:mgmt:~$ net show bgp l2vpn evpn es 
ES Flags: B - bypass, L local, R remote, I inconsistent 
VTEP Flags: E ESR/Type-4, A active nexthop 
ESI                            Flags RD                    #VNIs    VTEPs 
03:00:00:00:00:00:aa:00:00:01  LR    10.10.10.1:3          1        10.10.10.2(EA) 
03:00:00:00:00:00:aa:00:00:02  LR    10.10.10.1:4          1        10.10.10.2(EA) 
03:00:00:00:00:00:bb:00:00:01  R     -                     1        10.10.20.1(A),10.10.20.2(A) 
03:00:00:00:00:00:bb:00:00:02  R     -                     1        10.10.20.1(A),10.10.20.2(A) 
```

```
cumulus@leaf01:mgmt:~$ net show bgp l2vpn evpn es-evi 
Flags: L local, R remote, I inconsistent 
VTEP-Flags: E EAD-per-ES, V EAD-per-EVI 
VNI      ESI                            Flags VTEPs 
20       03:00:00:00:00:00:aa:00:00:02  LR    10.10.10.2(EV) 
20       03:00:00:00:00:00:bb:00:00:02  R     10.10.20.1(EV),10.10.20.2(EV) 
10       03:00:00:00:00:00:aa:00:00:01  LR    10.10.10.2(EV) 
10       03:00:00:00:00:00:bb:00:00:01  R     10.10.20.1(EV),10.10.20.2(EV) 
```

```
cumulus@leaf01:mgmt:~$ net show bgp l2vpn evpn es-vrf 
ES-VRF Flags: A Active 
ESI                            VRF             Flags IPv4-NHG IPv6-NHG Ref 
03:00:00:00:00:00:aa:00:00:01  VRF RED         A     72580645 72580646 1 
03:00:00:00:00:00:aa:00:00:02  VRF GREEN       A     72580647 72580648 1 
03:00:00:00:00:00:bb:00:00:01  VRF RED         A     72580651 72580652 1 
03:00:00:00:00:00:bb:00:00:02  VRF GREEN       A     72580649 72580650 1 
```

```
cumulus@leaf01:mgmt:~$ net show evpn vni 
VNI        Type VxLAN IF              # MACs   # ARPs   # Remote VTEPs  Tenant VRF 
10         L2   vxlan48               10       3        3               RED 
20         L2   vxlan48               10       2        3               GREEN 
4001       L3   vxlan99               0        0        n/a             RED 
4002       L3   vxlan99               0        0        n/a             GREEN 
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
* 4002       L3   10.10.10.1:5          65101:4002                65101:4002               GREEN 
* 4001       L3   10.10.10.1:6          65101:4001                65101:4001               RED 
```

``` 
cumulus@leaf01:mgmt:~$ net show interface bond1 
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
RX_OK  RX_ERR  RX_DRP  RX_OVR  TX_OK  TX_ERR  TX_DRP  TX_OVR 
-----  ------  ------  ------  -----  ------  ------  ------ 
14533       0       1       0   6906       0       0       0 
 
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
  ARP-ND redirect enabled: ARP 19 ND 130 
```

```
cumulus@leaf02:mgmt:~$ net show evpn es detail 
ESI: 03:00:00:00:00:00:aa:00:00:01 
 Type: Local,Remote 
 Interface: bond1 
 State: up 
 Bridge port: yes 
 Ready for BGP: yes 
 VNI Count: 1 
 MAC Count: 2 
 DF status: non-df 
 DF preference: 10000 
 Nexthop group: 536870913 
 VTEPs: 
     10.10.10.1(local) df_alg: preference df_pref: 50000 sph: tc-filter 
 nh: 268435459 
 
ESI: 03:00:00:00:00:00:aa:00:00:02 
 Type: Local,Remote 
 Interface: bond2 
 State: up 
 Bridge port: yes 
 Ready for BGP: yes 
 VNI Count: 1 
 MAC Count: 2 
 DF status: non-df 
 DF preference: 10000 
 Nexthop group: 536870914 
 VTEPs: 
     10.10.10.1(local) df_alg: preference df_pref: 50000 sph: tc-filter 
 nh: 268435459 
 
ESI: 03:00:00:00:00:00:bb:00:00:01 
 Type: Remote 
 Interface: - 
 Ready for BGP: no 
 VNI Count: 0 
 MAC Count: 3 
 DF preference: 0 
 Nexthop group: 536870918 
 VTEPs: 
     10.10.20.1 nh: 268435463 
     10.10.20.2 nh: 268435461 
 
ESI: 03:00:00:00:00:00:bb:00:00:02 
 Type: Remote 
 Interface: - 
 Ready for BGP: no 
 VNI Count: 0 
 MAC Count: 3 
 DF preference: 0 
 Nexthop group: 536870916 
 VTEPs: 
     10.10.20.1 nh: 268435463 
     10.10.20.2 nh: 268435461
```

``` 
cumulus@leaf02:mgmt:~$ net show interface bond1 
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
RX_OK  RX_ERR  RX_DRP  RX_OVR  TX_OK  TX_ERR  TX_DRP  TX_OVR 
-----  ------  ------  ------  -----  ------  ------  ------ 
14734       0       0       0   8873       0       0       0 
 
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
  ARP-ND redirect enabled: ARP 23 ND 170 
```

```
cumulus@leaf02:mgmt:~$ net show bgp l2vpn evpn vni 
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
* 4001       L3   10.10.10.2:4          65102:4001                65102:4001               RED 
* 4002       L3   10.10.10.2:5          65102:4002                65102:4002               GREEN 
```

Verify that the bridge `br_default` is learning MAC entries:

```
cumulus@leaf01:mgmt:~$ nv show bridge domain br_default mac-table 
    age    bridge-domain  entry-type  interface   last-update  MAC address        src-vni  vlan  vni   Summary 
--  -----  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  ---------------------- 
0   5      br_default     static      bond2       984          48:b0:2d:9d:31:ae           20 
1   186    br_default     static      bond2       11241        a6:e0:55:25:f3:b2           20 
2   14743  br_default     permanent   bond2       14743        48:b0:2d:ce:f9:6f 
3   954    br_default                 vxlan48     954          48:b0:2d:72:28:ff           10    None 
4   957    br_default                 vxlan48     957          48:b0:2d:a7:e2:6e           20    None 
5   957    br_default                 vxlan48     957          48:b0:2d:82:05:04           10    None 
6   974    br_default                 vxlan48     974          b6:4b:0f:ea:f2:02           10    None 
7   979    br_default                 vxlan48     979          44:38:39:22:bb:08           10    None  remote-dst: 10.10.20.1 
8   982    br_default                 vxlan48     982          44:38:39:22:bb:09           10    None  remote-dst: 10.10.20.2 
9   982    br_default                 vxlan48     982          ee:54:69:be:3a:3f           20    None 
10  982    br_default                 vxlan48     982          48:b0:2d:75:8e:7a           20    None 
11  984    br_default                 vxlan48     984          48:b0:2d:7f:a9:bd           20    None  remote-dst: 10.10.10.2 
12  984    br_default                 vxlan48     186          44:38:39:22:bb:07           20    None  remote-dst: 10.10.10.2 
13  984    br_default                 vxlan48     984          48:b0:2d:bc:7e:83           10    None  remote-dst: 10.10.10.2 
14  14743  br_default     permanent   vxlan48     14743        96:8b:4a:de:a2:71                 None 
15  979                   permanent   vxlan48     11           00:00:00:00:00:00  10             None  remote-dst: 10.10.10.2 
                                                                                                       remote-dst: 10.10.20.1 
                                                                                                       remote-dst: 10.10.20.2 
16  5      br_default     static      bond1       984          48:b0:2d:33:24:a3           10 
17  126    br_default     static      bond1       11237        42:20:47:91:95:a7           10 
18  14743  br_default     permanent   bond1       14743        48:b0:2d:3d:e9:84 
19                        permanent   br_default               00:00:5e:00:01:0a 
20  4359   br_default     permanent   br_default  4359         44:38:39:22:bb:06           10 
```

``` 
cumulus@leaf02:mgmt:~$ nv show bridge domain br_default mac-table 
    age    bridge-domain  entry-type  interface   last-update  MAC address        src-vni  vlan  vni   Summary 
--  -----  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  ---------------------- 
0   11259  br_default     static      bond2       11259        48:b0:2d:9d:31:ae           20 
1   64     br_default     static      bond2       11244        a6:e0:55:25:f3:b2           20 
2   13     br_default                 bond2       14685        48:b0:2d:7f:a9:bd           20 
3   14751  br_default     permanent   bond2       14751        48:b0:2d:aa:08:bd 
4   11259  br_default     static      bond1       11259        48:b0:2d:33:24:a3           10 
5   177    br_default     static      bond1       11240        42:20:47:91:95:a7           10 
6   13     br_default                 bond1       14685        48:b0:2d:bc:7e:83           10 
7   14751  br_default     permanent   bond1       14751        48:b0:2d:f0:64:6e 
8   957    br_default                 vxlan48     957          48:b0:2d:72:28:ff           10    None 
9   960    br_default                 vxlan48     960          48:b0:2d:a7:e2:6e           20    None 
10  960    br_default                 vxlan48     960          48:b0:2d:82:05:04           10    None 
11  977    br_default                 vxlan48     977          b6:4b:0f:ea:f2:02           10    None 
12  982    br_default                 vxlan48     982          44:38:39:22:bb:08           10    None  remote-dst: 10.10.20.1 
13  985    br_default                 vxlan48     985          44:38:39:22:bb:09           10    None  remote-dst: 10.10.20.2 
14  985    br_default                 vxlan48     985          ee:54:69:be:3a:3f           20    None 
15  985    br_default                 vxlan48     985          48:b0:2d:75:8e:7a           20    None 
16  987    br_default                 vxlan48     987          44:38:39:22:bb:06           10    None  remote-dst: 10.10.10.1 
17  14751  br_default     permanent   vxlan48     14751        1a:64:66:e8:14:39           1     None 
18  982                   permanent   vxlan48     50           00:00:00:00:00:00  10             None  remote-dst: 10.10.10.1 
                                                                                                       remote-dst: 10.10.20.1 
                                                                                                       remote-dst: 10.10.20.2 
19                        permanent   br_default               00:00:5e:00:01:0a 
20  4365   br_default     permanent   br_default  4365         44:38:39:22:bb:07           10 
```

Verify the host routes over the layer 3 VNI on VRF RED; the route for 192.168.1.110/32 points to remote VTEP destinations with ECMP:

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
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 02:21:20 
C * 192.168.1.0/24 [0/1024] is directly connected, vlan10-v0, 02:21:20 
C>* 192.168.1.0/24 is directly connected, vlan10, 02:21:20 
B>* 192.168.1.110/32 [20/0] via 10.10.20.1, vlan220_l3 onlink, weight 1, 00:31:40 
  *                         via 10.10.20.2, vlan220_l3 onlink, weight 1, 00:31:40 

show ipv6 route vrf RED 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 02:21:20 
C * fe80::/64 is directly connected, vlan220_l3, 02:21:20 
C * fe80::/64 is directly connected, vlan10-v0, 02:21:20 
C>* fe80::/64 is directly connected, vlan10, 02:21:20 
```

Verify EVPN type-2 routes at the ingress PE (leaf01) for the end host *42:20:47:91:95:a7*:

```
cumulus@leaf01:mgmt:~$ net show bgp l2vpn evpn route type 2 | grep 42:20:47:91:95:a7 -A 4 
*> [2]:[0]:[48]:[42:20:47:91:95:a7] RD 10.10.10.1:7 
                    10.10.10.1 (leaf01) 
                                                       32768 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    ET:8 RT:65101:10 MM:1 
*> [2]:[0]:[48]:[42:20:47:91:95:a7]:[32]:[192.168.1.10] RD 10.10.10.1:7 
                    10.10.10.1 (leaf01) 
                                                       32768 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    ET:8 RT:65101:10 RT:65101:4001 Rmac:44:38:39:22:bb:06 MM:1 
*> [2]:[0]:[48]:[42:20:47:91:95:a7]:[128]:[fe80::4020:47ff:fe91:95a7] RD 10.10.10.1:7 
                    10.10.10.1 (leaf01) 
                                                       32768 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    ET:8 RT:65101:10 MM:1 
-- 
*  [2]:[0]:[48]:[42:20:47:91:95:a7] RD 10.10.10.2:3 
                    10.10.10.2 (spine02) 
                                                           0 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 ET:8 MM:1 
*> [2]:[0]:[48]:[42:20:47:91:95:a7] RD 10.10.10.2:3 
                    10.10.10.2 (spine01) 
                                                           0 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 ET:8 MM:1 
*  [2]:[0]:[48]:[42:20:47:91:95:a7]:[32]:[192.168.1.10] RD 10.10.10.2:3 
                    10.10.10.2 (spine02) 
                                                           0 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 RT:65102:4001 ET:8 MM:1 Rmac:44:38:39:22:bb:07 
*> [2]:[0]:[48]:[42:20:47:91:95:a7]:[32]:[192.168.1.10] RD 10.10.10.2:3 
                    10.10.10.2 (spine01) 
                                                           0 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 RT:65102:4001 ET:8 MM:1 Rmac:44:38:39:22:bb:07 
*  [2]:[0]:[48]:[42:20:47:91:95:a7]:[128]:[fe80::4020:47ff:fe91:95a7] RD 10.10.10.2:3 
                    10.10.10.2 (spine02) 
                                                           0 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 ET:8 MM:1 
*> [2]:[0]:[48]:[42:20:47:91:95:a7]:[128]:[fe80::4020:47ff:fe91:95a7] RD 10.10.10.2:3 
                    10.10.10.2 (spine01) 
                                                           0 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 ET:8 MM:1 
```

Verify EVPN type-2 routes at the egress PE (leaf03) for the end host *42:20:47:91:95:a7*:

```
cumulus@leaf03:mgmt:~$ net show bgp l2vpn evpn route type 2 | grep 42:20:47:91:95:a7 -A 4 
*  [2]:[0]:[48]:[42:20:47:91:95:a7] RD 10.10.10.1:7 
                    10.10.10.1 (spine04) 
                                                           0 65299 65210 65110 65199 65101 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65101:10 ET:8 MM:1 
*> [2]:[0]:[48]:[42:20:47:91:95:a7] RD 10.10.10.1:7 
                    10.10.10.1 (spine03) 
                                                           0 65299 65210 65110 65199 65101 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65101:10 ET:8 MM:1 
*  [2]:[0]:[48]:[42:20:47:91:95:a7]:[32]:[192.168.1.10] RD 10.10.10.1:7 
                    10.10.10.1 (spine04) 
                                                           0 65299 65210 65110 65199 65101 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65101:10 RT:65101:4001 ET:8 MM:1 Rmac:44:38:39:22:bb:06 
*> [2]:[0]:[48]:[42:20:47:91:95:a7]:[32]:[192.168.1.10] RD 10.10.10.1:7 
                    10.10.10.1 (spine03) 
                                                           0 65299 65210 65110 65199 65101 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65101:10 RT:65101:4001 ET:8 MM:1 Rmac:44:38:39:22:bb:06 
*  [2]:[0]:[48]:[42:20:47:91:95:a7]:[128]:[fe80::4020:47ff:fe91:95a7] RD 10.10.10.1:7 
                    10.10.10.1 (spine04) 
                                                           0 65299 65210 65110 65199 65101 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65101:10 ET:8 MM:1 
*> [2]:[0]:[48]:[42:20:47:91:95:a7]:[128]:[fe80::4020:47ff:fe91:95a7] RD 10.10.10.1:7 
                    10.10.10.1 (spine03) 
                                                           0 65299 65210 65110 65199 65101 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65101:10 ET:8 MM:1 
-- 
*  [2]:[0]:[48]:[42:20:47:91:95:a7] RD 10.10.10.2:3 
                    10.10.10.2 (spine04) 
                                                           0 65299 65210 65110 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 ET:8 MM:1 
*> [2]:[0]:[48]:[42:20:47:91:95:a7] RD 10.10.10.2:3 
                    10.10.10.2 (spine03) 
                                                           0 65299 65210 65110 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 ET:8 MM:1 
*  [2]:[0]:[48]:[42:20:47:91:95:a7]:[32]:[192.168.1.10] RD 10.10.10.2:3 
                    10.10.10.2 (spine04) 
                                                           0 65299 65210 65110 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 RT:65102:4001 ET:8 MM:1 Rmac:44:38:39:22:bb:07 
*> [2]:[0]:[48]:[42:20:47:91:95:a7]:[32]:[192.168.1.10] RD 10.10.10.2:3 
                    10.10.10.2 (spine03) 
                                                           0 65299 65210 65110 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 RT:65102:4001 ET:8 MM:1 Rmac:44:38:39:22:bb:07 
*  [2]:[0]:[48]:[42:20:47:91:95:a7]:[128]:[fe80::4020:47ff:fe91:95a7] RD 10.10.10.2:3 
                    10.10.10.2 (spine04) 
                                                           0 65299 65210 65110 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 ET:8 MM:1 
*> [2]:[0]:[48]:[42:20:47:91:95:a7]:[128]:[fe80::4020:47ff:fe91:95a7] RD 10.10.10.2:3 
                    10.10.10.2 (spine03) 
                                                           0 65299 65210 65110 65199 65102 i 
                    ESI:03:00:00:00:00:00:aa:00:00:01 
                    RT:65102:10 ET:8 MM:1 
```
</div>

{{< /tab >}}
{{< tab "DC2 ">}}

<div class=scroll>

```
cumulus@leaf03:mgmt:~$ net show evpn es detail 
ESI: 03:00:00:00:00:00:aa:00:00:01 
 Type: Remote 
 Interface: - 
 Ready for BGP: no 
 VNI Count: 0 
 MAC Count: 2 
 DF preference: 0 
 Nexthop group: 536870915 
 VTEPs: 
     10.10.10.1 nh: 268435460 
     10.10.10.2 nh: 268435462 
 
ESI: 03:00:00:00:00:00:aa:00:00:02 
 Type: Remote 
 Interface: - 
 Ready for BGP: no 
 VNI Count: 0 
 MAC Count: 2 
 DF preference: 0 
 Nexthop group: 536870917 
 VTEPs: 
     10.10.10.1 nh: 268435460 
     10.10.10.2 nh: 268435462 
 
ESI: 03:00:00:00:00:00:bb:00:00:01 
 Type: Local,Remote 
 Interface: bond1 
 State: up 
 Bridge port: yes 
 Ready for BGP: yes 
 VNI Count: 1 
 MAC Count: 3 
 DF status: df 
 DF preference: 50000 
 Nexthop group: 536870913 
 VTEPs: 
     10.10.20.2(local) df_alg: preference df_pref: 10000 sph: tc-filter 
 nh: 268435463 
 
ESI: 03:00:00:00:00:00:bb:00:00:02 
 Type: Local,Remote 
 Interface: bond2 
 State: up 
 Bridge port: yes 
 Ready for BGP: yes 
 VNI Count: 1 
 MAC Count: 3 
 DF status: df 
 DF preference: 50000 
 Nexthop group: 536870914 
 VTEPs: 
     10.10.20.2(local) df_alg: preference df_pref: 10000 sph: tc-filter 
 nh: 268435463 
```

```
cumulus@leaf03:mgmt:~$ net show bgp l2vpn evpn es 
ES Flags: B - bypass, L local, R remote, I inconsistent 
VTEP Flags: E ESR/Type-4, A active nexthop 
ESI                            Flags RD                    #VNIs    VTEPs 
03:00:00:00:00:00:aa:00:00:01  R     -                     1        10.10.10.1(A),10.10.10.2(A) 
03:00:00:00:00:00:aa:00:00:02  R     -                     1        10.10.10.1(A),10.10.10.2(A) 
03:00:00:00:00:00:bb:00:00:01  LR    10.10.20.1:3          1        10.10.20.2(EA) 
03:00:00:00:00:00:bb:00:00:02  LR    10.10.20.1:4          1        10.10.20.2(EA) 
```

```
cumulus@leaf03:mgmt:~$ net show bgp l2vpn evpn es-evi 
Flags: L local, R remote, I inconsistent 
VTEP-Flags: E EAD-per-ES, V EAD-per-EVI 
VNI      ESI                            Flags VTEPs 
20       03:00:00:00:00:00:aa:00:00:02  R     10.10.10.1(EV),10.10.10.2(EV) 
20       03:00:00:00:00:00:bb:00:00:02  LR    10.10.20.2(EV) 
10       03:00:00:00:00:00:aa:00:00:01  R     10.10.10.1(EV),10.10.10.2(EV) 
10       03:00:00:00:00:00:bb:00:00:01  LR    10.10.20.2(EV) 
```

```
cumulus@leaf03:mgmt:~$ net show bgp l2vpn evpn es-vrf 
ES-VRF Flags: A Active 
ESI                            VRF             Flags IPv4-NHG IPv6-NHG Ref 
03:00:00:00:00:00:aa:00:00:01  VRF RED         A     72580649 72580650 1 
03:00:00:00:00:00:aa:00:00:02  VRF GREEN       A     72580651 72580652 1 
03:00:00:00:00:00:bb:00:00:01  VRF RED         A     72580647 72580648 1 
03:00:00:00:00:00:bb:00:00:02  VRF GREEN       A     72580645 72580646 1 
```

```
cumulus@leaf03:mgmt:~$ net show evpn vni 
VNI        Type VxLAN IF              # MACs   # ARPs   # Remote VTEPs  Tenant VRF 
10         L2   vxlan48               10       4        3               RED 
20         L2   vxlan48               10       2        3               GREEN 
4001       L3   vxlan99               0        0        n/a             RED 
4002       L3   vxlan99               0        0        n/a             GREEN 
```

```
cumulus@leaf03:mgmt:~$ net show bgp evpn vni 
Advertise Gateway Macip: Disabled 
Advertise SVI Macip: Disabled 
Advertise All VNI flag: Enabled 
BUM flooding: Head-end replication 
VXLAN flooding: Enabled 
Number of L2 VNIs: 4 
Number of L3 VNIs: 2 
Flags: * - Kernel 
  VNI        Type RD                    Import RT                 Export RT                 Tenant VRF 
  4001       L2   10.10.20.1:10         65201:4001                65201:4001               default 
* 20         L2   10.10.20.1:2          65201:20                  65201:20                 GREEN 
* 10         L2   10.10.20.1:7          65201:10                  65201:10                 RED 
  4002       L2   10.10.20.1:11         65201:4002                65201:4002               default 
* 4002       L3   10.10.20.1:5          65201:4002                65201:4002               GREEN 
* 4001       L3   10.10.20.1:6          65201:4001                65201:4001               RED 
```

```
cumulus@leaf03:mgmt:~$ net show interface bond1 
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
10 
 
Untagged 
-------- 
10 
 
cl-netstat counters 
------------------- 
RX_OK  RX_ERR  RX_DRP  RX_OVR  TX_OK  TX_ERR  TX_DRP  TX_OVR 
-----  ------  ------  ------  -----  ------  ------  ------ 
 9791       0       0       0   5870       0       0       0 
 
LLDP Details 
------------ 
LocalPort  RemotePort(RemoteHost) 
---------  --------------------------- 
swp3       48:b0:2d:72:28:ff(server03) 
 
Routing 
------- 
  Interface bond1 is up, line protocol is up 
  Link ups:       5    last: 2023/04/14 16:07:55.32 
  Link downs:     0    last: (never) 
  PTM status: disabled 
  vrf: default 
  index 8 metric 0 mtu 9216 speed 1000 
  flags: <UP,BROADCAST,RUNNING,MULTICAST> 
  Type: Ethernet 
  HWaddr: 48:b0:2d:7d:9c:74 
  Interface Type bond 
  Master interface: br_default PVID: 10 
  EVPN-MH: ES id 1 ES sysmac 00:00:00:00:00:bb 
  protodown: off (n/a) 
  ARP-ND redirect enabled: ARP 49 ND 128 
```

```
cumulus@leaf04:mgmt:~$ net show evpn es detail 
ESI: 03:00:00:00:00:00:aa:00:00:01 
 Type: Remote 
 Interface: - 
 Ready for BGP: no 
 VNI Count: 0 
 MAC Count: 2 
 DF preference: 0 
 Nexthop group: 536870915 
 VTEPs: 
     10.10.10.1 nh: 268435460 
     10.10.10.2 nh: 268435462 
 
ESI: 03:00:00:00:00:00:aa:00:00:02 
 Type: Remote 
 Interface: - 
 Ready for BGP: no 
 VNI Count: 0 
 MAC Count: 2 
 DF preference: 0 
 Nexthop group: 536870917 
 VTEPs: 
     10.10.10.1 nh: 268435460 
     10.10.10.2 nh: 268435462 
 
ESI: 03:00:00:00:00:00:bb:00:00:01 
 Type: Local,Remote 
 Interface: bond1 
 State: up 
 Bridge port: yes 
 Ready for BGP: yes 
 VNI Count: 1 
 MAC Count: 3 
 DF status: non-df 
 DF preference: 10000 
 Nexthop group: 536870913 
 VTEPs: 
     10.10.20.1(local) df_alg: preference df_pref: 50000 sph: tc-filter 
 nh: 268435463 
 
ESI: 03:00:00:00:00:00:bb:00:00:02 
 Type: Local,Remote 
 Interface: bond2 
 State: up 
 Bridge port: yes 
 Ready for BGP: yes 
 VNI Count: 1 
 MAC Count: 3 
 DF status: non-df 
 DF preference: 10000 
 Nexthop group: 536870914 
 VTEPs: 
     10.10.20.1(local) df_alg: preference df_pref: 50000 sph: tc-filter 
 nh: 268435463 
```

```
cumulus@leaf04:mgmt:~$ net show interface bond1 
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
10 
 
Untagged 
-------- 
10 
 
cl-netstat counters 
------------------- 
RX_OK  RX_ERR  RX_DRP  RX_OVR  TX_OK  TX_ERR  TX_DRP  TX_OVR 
-----  ------  ------  ------  -----  ------  ------  ------ 
18877       0       0       0  11047       0       0       0 
 
LLDP Details 
------------ 
LocalPort  RemotePort(RemoteHost) 
---------  --------------------------- 
swp3       48:b0:2d:82:05:04(server03) 
 
Routing 
------- 
  Interface bond1 is up, line protocol is up 
  Link ups:       6    last: 2023/04/14 16:07:53.92 
  Link downs:     0    last: (never) 
  PTM status: disabled 
  vrf: default 
  index 8 metric 0 mtu 9216 speed 1000 
  flags: <UP,BROADCAST,RUNNING,MULTICAST> 
  Type: Ethernet 
  HWaddr: 48:b0:2d:84:e8:0f 
  Interface Type bond 
  Master interface: br_default PVID: 10 
  EVPN-MH: ES id 1 ES sysmac 00:00:00:00:00:bb 
  protodown: off (n/a) 
  ARP-ND redirect enabled: ARP 84 ND 254 
```

```  
cumulus@leaf04:mgmt:~$ net show bgp l2vpn evpn vni 
Advertise Gateway Macip: Disabled 
Advertise SVI Macip: Disabled 
Advertise All VNI flag: Enabled 
BUM flooding: Head-end replication 
VXLAN flooding: Enabled 
Number of L2 VNIs: 4 
Number of L3 VNIs: 2 
Flags: * - Kernel 
  VNI        Type RD                    Import RT                 Export RT                 Tenant VRF 
  4001       L2   10.10.20.2:10         65202:4001                65202:4001               default 
* 20         L2   10.10.20.2:2          65202:20                  65202:20                 GREEN 
* 10         L2   10.10.20.2:9          65202:10                  65202:10                 RED 
  4002       L2   10.10.20.2:11         65202:4002                65202:4002               default 
* 4002       L3   10.10.20.2:7          65202:4002                65202:4002               GREEN 
* 4001       L3   10.10.20.2:8          65202:4001                65202:4001               RED 
```

Verify that the bridge `br_default` is learning MAC entries:

```
cumulus@leaf03:mgmt:~$ nv show bridge domain br_default mac-table 
    age    bridge-domain  entry-type  interface   last-update  MAC address        src-vni  vlan  vni   Summary 
--  -----  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  ---------------------- 
0   4      br_default     static      bond1       1924         48:b0:2d:72:28:ff           10 
1   1927   br_default     static      bond1       1927         48:b0:2d:82:05:04           10 
2   3      br_default     static      bond1       466          b6:4b:0f:ea:f2:02           10 
3   10120  br_default     permanent   bond1       10120        48:b0:2d:7d:9c:74 
4   1949   br_default                 vxlan48     1949         44:38:39:22:bb:09           20    None  remote-dst: 10.10.20.2 
5   1949   br_default                 vxlan48     1949         48:b0:2d:7f:a9:bd           20    None  remote-dst: 10.10.10.2 
6   1949   br_default                 vxlan48     1949         44:38:39:22:bb:07           20    None  remote-dst: 10.10.10.2 
7   1949   br_default                 vxlan48     1949         48:b0:2d:bc:7e:83           10    None  remote-dst: 10.10.10.2 
8   1949   br_default                 vxlan48     1949         48:b0:2d:9d:31:ae           20    None 
9   1949   br_default                 vxlan48     1949         a6:e0:55:25:f3:b2           20    None 
10  1949   br_default                 vxlan48     1939         44:38:39:22:bb:06           20    None  remote-dst: 10.10.10.1 
11  1949   br_default                 vxlan48     466          42:20:47:91:95:a7           10    None 
12  1949   br_default                 vxlan48     1949         48:b0:2d:33:24:a3           10    None 
13  10120  br_default     permanent   vxlan48     10120        5e:cd:93:67:98:eb                 None 
14  1949                  permanent   vxlan48     941          00:00:00:00:00:00  20             None  remote-dst: 10.10.10.1 
                                                                                                       remote-dst: 10.10.10.2 
                                                                                                       remote-dst: 10.10.20.2 
15  1927   br_default     static      bond2       1927         48:b0:2d:a7:e2:6e           20 
16  4      br_default     static      bond2       1949         48:b0:2d:75:8e:7a           20 
17  158    br_default     static      bond2       1939         ee:54:69:be:3a:3f           20 
18  10120  br_default     permanent   bond2       10120        48:b0:2d:d5:d5:91 
19                        permanent   br_default               00:00:5e:00:01:14 
20  1950   br_default     permanent   br_default  1950         44:38:39:22:bb:08           10 
```

``` 
cumulus@leaf04:mgmt:~$ nv show bridge domain br_default mac-table 
    age    bridge-domain  entry-type  interface   last-update  MAC address        src-vni  vlan  vni   Summary 
--  -----  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  ---------------------- 
0   9      br_default     static      bond1       1929         48:b0:2d:82:05:04           10 
1   9847   br_default     static      bond1       9847         48:b0:2d:72:28:ff           1010 
2   2027   br_default     static      bond1       9975         b6:4b:0f:ea:f2:02           1010 
3   18889  br_default     permanent   bond1       18889        48:b0:2d:84:e8:0f 
4   1952   br_default                 vxlan48     130          44:38:39:22:bb:08           10    None  remote-dst: 10.10.20.1 
5   1954   br_default                 vxlan48     1954         48:b0:2d:7f:a9:bd           20    None  remote-dst: 10.10.10.2 
6   1954   br_default                 vxlan48     1941         44:38:39:22:bb:07           20    None  remote-dst: 10.10.10.2 
7   1954   br_default                 vxlan48     1954         48:b0:2d:bc:7e:83           10    None  remote-dst: 10.10.10.2 
8   1954   br_default                 vxlan48     1954         48:b0:2d:9d:31:ae           20    None 
9   1954   br_default                 vxlan48     1954         a6:e0:55:25:f3:b2           20    None 
10  1954   br_default                 vxlan48     1954         44:38:39:22:bb:06           20    None  remote-dst: 10.10.10.1 
11  1954   br_default                 vxlan48     1954         42:20:47:91:95:a7           10    None 
12  1954   br_default                 vxlan48     1954         48:b0:2d:33:24:a3           10    None 
13  18889  br_default     permanent   vxlan48     18889        9e:13:6b:7f:3a:82                 None 
14  1952                  permanent   vxlan48     1952         00:00:00:00:00:00  20             None  remote-dst: 10.10.10.1 
                                                                                                       remote-dst: 10.10.10.2 
                                                                                                       remote-dst: 10.10.20.1 
15  9      br_default     static      bond2       1929         48:b0:2d:a7:e2:6e           20 
16  9847   br_default     static      bond2       9847         48:b0:2d:75:8e:7a           2020 
17  2147   br_default     static      bond2       9976         ee:54:69:be:3a:3f           2020 
18  18889  br_default     permanent   bond2       18889        48:b0:2d:95:3f:b0 
19                        permanent   br_default               00:00:5e:00:01:14 
20  1955   br_default     permanent   br_default  1955         44:38:39:22:bb:09           10 
```

Verify that the host routes over the layer 3 VNI on `vrf RED`:

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
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 02:25:33 
C * 192.168.1.0/24 [0/1024] is directly connected, vlan10-v0, 02:25:33 
C>* 192.168.1.0/24 is directly connected, vlan10, 02:25:33 
B>* 192.168.1.10/32 [20/0] via 10.10.10.1, vlan220_l3 onlink, weight 1, 00:06:30 
  *                        via 10.10.10.2, vlan220_l3 onlink, weight 1, 00:06:30 

show ipv6 route vrf RED 
======================== 
Codes: K - kernel route, C - connected, S - static, R - RIPng, 
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table, 
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR, 
       f - OpenFabric, Z - FRR, 
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup 
       t - trapped, o - offload failure 
 
VRF RED: 
K>* ::/0 [255/8192] unreachable (ICMP unreachable), 02:25:33 
C * fe80::/64 is directly connected, vlan220_l3, 02:25:32 
C * fe80::/64 is directly connected, vlan10-v0, 02:25:33 
C>* fe80::/64 is directly connected, vlan10, 02:25:33 
```

Verify EVPN type-2 routes from the egress PE (leaf01) for the end host *b6:4b:0f:ea:f2:02*:

```
cumulus@leaf01:mgmt:~$ net show bgp l2vpn evpn route type 2 | grep -A 4 b6:4b:0f:ea:f2:02 
*  [2]:[0]:[48]:[b6:4b:0f:ea:f2:02] RD 10.10.20.1:9 
                    10.10.20.1 (spine02) 
                                                           0 65199 65110 65210 65299 65201 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65201:10 ET:8 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02] RD 10.10.20.1:9 
                    10.10.20.1 (spine01) 
                                                           0 65199 65110 65210 65299 65201 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65201:10 ET:8 
*  [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[32]:[192.168.1.110] RD 10.10.20.1:9 
                    10.10.20.1 (spine02) 
                                                           0 65199 65110 65210 65299 65201 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65201:10 RT:65201:4001 ET:8 Rmac:44:38:39:22:bb:08 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[32]:[192.168.1.110] RD 10.10.20.1:9 
                    10.10.20.1 (spine01) 
                                                           0 65199 65110 65210 65299 65201 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65201:10 RT:65201:4001 ET:8 Rmac:44:38:39:22:bb:08 
*  [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[128]:[fe80::b44b:fff:feea:f202] RD 10.10.20.1:9 
                    10.10.20.1 (spine02) 
                                                           0 65199 65110 65210 65299 65201 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65201:10 ET:8 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[128]:[fe80::b44b:fff:feea:f202] RD 10.10.20.1:9 
                    10.10.20.1 (spine01) 
                                                           0 65199 65110 65210 65299 65201 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65201:10 ET:8 
-- 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02] RD 10.10.20.2:5 
                    10.10.20.2 (spine01) 
                                                           0 65199 65110 65210 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 ET:8 
*  [2]:[0]:[48]:[b6:4b:0f:ea:f2:02] RD 10.10.20.2:5 
                    10.10.20.2 (spine02) 
                                                           0 65199 65110 65210 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 ET:8 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[32]:[192.168.1.110] RD 10.10.20.2:5 
                    10.10.20.2 (spine01) 
                                                           0 65199 65110 65210 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 RT:65202:4001 ET:8 Rmac:44:38:39:22:bb:09 ND:Proxy 
*  [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[32]:[192.168.1.110] RD 10.10.20.2:5 
                    10.10.20.2 (spine02) 
                                                           0 65199 65110 65210 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 RT:65202:4001 ET:8 Rmac:44:38:39:22:bb:09 ND:Proxy 
*  [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[128]:[fe80::b44b:fff:feea:f202] RD 10.10.20.2:5 
                    10.10.20.2 (spine02) 
                                                           0 65199 65110 65210 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 ET:8 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[128]:[fe80::b44b:fff:feea:f202] RD 10.10.20.2:5 
                    10.10.20.2 (spine01) 
                                                           0 65199 65110 65210 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 ET:8 
```

Verify EVPN type-2 routes from the ingress PE (leaf03) for the end host *b6:4b:0f:ea:f2:02*:

```
cumulus@leaf03:mgmt:~$ net show bgp l2vpn evpn route type 2 | grep -A 4 b6:4b:0f:ea:f2:02 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02] RD 10.10.20.1:9 
                    10.10.20.1 (leaf03) 
                                                       32768 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    ET:8 RT:65201:10 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[32]:[192.168.1.110] RD 10.10.20.1:9 
                    10.10.20.1 (leaf03) 
                                                       32768 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    ET:8 RT:65201:10 RT:65201:4001 Rmac:44:38:39:22:bb:08 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[128]:[fe80::b44b:fff:feea:f202] RD 10.10.20.1:9 
                    10.10.20.1 (leaf03) 
                                                       32768 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    ET:8 RT:65201:10 
-- 
*  [2]:[0]:[48]:[b6:4b:0f:ea:f2:02] RD 10.10.20.2:5 
                    10.10.20.2 (spine03) 
                                                           0 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 ET:8 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02] RD 10.10.20.2:5 
                    10.10.20.2 (spine04) 
                                                           0 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 ET:8 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[32]:[192.168.1.110] RD 10.10.20.2:5 
                    10.10.20.2 (spine03) 
                                                           0 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 RT:65202:4001 ET:8 Rmac:44:38:39:22:bb:09 
*  [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[32]:[192.168.1.110] RD 10.10.20.2:5 
                    10.10.20.2 (spine04) 
                                                           0 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 RT:65202:4001 ET:8 Rmac:44:38:39:22:bb:09 
*  [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[128]:[fe80::b44b:fff:feea:f202] RD 10.10.20.2:5 
                    10.10.20.2 (spine03) 
                                                           0 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 ET:8 
*> [2]:[0]:[48]:[b6:4b:0f:ea:f2:02]:[128]:[fe80::b44b:fff:feea:f202] RD 10.10.20.2:5 
                    10.10.20.2 (spine04) 
                                                           0 65299 65202 i 
                    ESI:03:00:00:00:00:00:bb:00:00:01 
                    RT:65202:10 ET:8 
```
</div>

{{< /tab >}}
{{< /tabs >}}
