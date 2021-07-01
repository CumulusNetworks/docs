---
title: Configuration Examples
author: NVIDIA
weight: 595
toc: 4
---
This section shows the following EVPN configuration examples:

- Layer 2 EVPN with external routing
- EVPN centralized routing
- EVPN symmetric routing

The configuration examples are based on the reference topology below:

{{< img src = "/images/cumulus-linux/reference-topology-full.png" >}}

<!-- You can see these configurations in action and explore further by selecting one of the demos in {{<exlink url="https://www.nvidia.com/en-us/networking/network-simulation/" text="Cumulus in the Cloud">}} (a free, personal, virtual data center network that provides a low-effort way to see Cumulus Linux in action). -->

## Layer 2 EVPN with External Routing

The following example configures a network infrastructure that creates a layer 2 extension between racks. Inter-VXLAN routed traffic routes between VXLANs on an external device.

- MLAG is configured between leaf01 and leaf02, and leaf03 and leaf04
- BGP unnumbered is in the underlay (configured on all leafs and spines)
- Server gateways are outside the VXLAN fabric

The following images shows traffic flow between tenants. The spines and other devices are omitted for simplicity.

|   Traffic Flow between server01 and server04  |     |
| --- | --- |
| <img width=1000/> {{< img src="/images/cumulus-linux/evpn-layer2-diagram.png" >}} | server01 and server04 are in the same VLAN but are located across different leafs.<br><ol><li>server01 makes a LACP hash decision and forwards traffic to leaf01.</li><li>leaf01 does a layer 2 lookup, has the MAC address for server04, and forwards the packet out VNI10, towards leaf04.</li><li>The VXLAN encapsulated frame arrives on leaf04, which does a layer 2 lookup and has the MAC address for server04 in VLAN10.</li></ul>|

### NCLU Commands

The NCLU commands configure traditional VXLAN devices.

{{< tabs "TabID35 ">}}
{{< tab "NCLU Commands">}}

{{< tabs "TabID38 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@leaf01:~$ net add bond bond1 bond slaves swp1
cumulus@leaf01:~$ net add bond bond2 bond slaves swp2
cumulus@leaf01:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf01:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf01:~$ net add bridge bridge vlan-aware
cumulus@leaf01:~$ net add bond bond1 bridge access 10
cumulus@leaf01:~$ net add bond bond1 clag id 1
cumulus@leaf01:~$ net add bond bond1-2 bond lacp-bypass-allow
cumulus@leaf01:~$ net add bond bond1-2 mtu 9000
cumulus@leaf01:~$ net add bond bond1-2 stp bpduguard
cumulus@leaf01:~$ net add bond bond1-2 stp portadminedge
cumulus@leaf01:~$ net add bond bond2 bridge access 20
cumulus@leaf01:~$ net add bond bond2 clag id 2
cumulus@leaf01:~$ net add bridge bridge ports bond1,bond2
cumulus@leaf01:~$ net add interface swp51-54 alias to spine
cumulus@leaf01:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf01:~$ net add interface swp49-50 alias peerlink
cumulus@leaf01:~$ net add bridge bridge ports peerlink
cumulus@leaf01:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf01:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.2
cumulus@leaf01:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf01:~$ net add interface peerlink.4094 clag priority 1000
cumulus@leaf01:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.12
cumulus@leaf01:~$ net add vlan 10 vlan-id 10
cumulus@leaf01:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 20 vlan-id 20
cumulus@leaf01:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf01:~$ net add bridge bridge vids 10,20
cumulus@leaf01:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf01:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf01:~$ net add bridge bridge ports vni10,vni20
cumulus@leaf01:~$ net add vxlan vni10 bridge access 10
cumulus@leaf01:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@leaf01:~$ net add vxlan vni10,20 bridge learning off
cumulus@leaf01:~$ net add vxlan vni10,20 stp bpduguard
cumulus@leaf01:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@leaf01:~$ net add vxlan vni20 bridge access 20
cumulus@leaf01:~$ net add loopback lo vxlan local-tunnelip 10.10.10.1
cumulus@leaf01:~$ net add bgp autonomous-system 65101
cumulus@leaf01:~$ net add bgp router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp neighbor underlay peer-group
cumulus@leaf01:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf01:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf01:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@leaf01:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ net add loopback lo ip address 10.10.10.2/32
cumulus@leaf02:~$ net add bond bond1 bond slaves swp1
cumulus@leaf02:~$ net add bond bond2 bond slaves swp2
cumulus@leaf02:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf02:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf02:~$ net add bond bond1 bridge access 10
cumulus@leaf02:~$ net add bond bond1 clag id 1
cumulus@leaf02:~$ net add bond bond1-2 bond lacp-bypass-allow
cumulus@leaf02:~$ net add bond bond1-2 mtu 9000
cumulus@leaf02:~$ net add bond bond1-2 stp bpduguard
cumulus@leaf02:~$ net add bond bond1-2 stp portadminedge
cumulus@leaf02:~$ net add bond bond2 bridge access 20
cumulus@leaf02:~$ net add bond bond2 clag id 2
cumulus@leaf02:~$ net add bridge bridge vlan-aware
cumulus@leaf02:~$ net add bridge bridge ports bond1,bond2
cumulus@leaf02:~$ net add interface swp51-54 alias to spine
cumulus@leaf02:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf02:~$ net add interface swp49-50 alias peerlink
cumulus@leaf02:~$ net add bridge bridge ports peerlink
cumulus@leaf02:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf02:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.1
cumulus@leaf02:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf02:~$ net add interface peerlink.4094 clag priority 2000
cumulus@leaf02:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.12
cumulus@leaf02:~$ net add vlan 10 ip forward off
cumulus@leaf02:~$ net add vlan 10 vlan-id 10
cumulus@leaf02:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 20 ip forward off
cumulus@leaf02:~$ net add vlan 20 vlan-id 20
cumulus@leaf02:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf02:~$ net add bridge bridge vids 10,20
cumulus@leaf02:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf02:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf02:~$ net add bridge bridge ports vni10,vni20
cumulus@leaf02:~$ net add vxlan vni10 bridge access 10
cumulus@leaf02:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@leaf02:~$ net add vxlan vni10,20 bridge learning off
cumulus@leaf02:~$ net add vxlan vni10,20 stp bpduguard
cumulus@leaf02:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@leaf02:~$ net add vxlan vni20 bridge access 20
cumulus@leaf02:~$ net add loopback lo vxlan local-tunnelip 10.10.10.2
cumulus@leaf02:~$ net add bgp autonomous-system 65102
cumulus@leaf02:~$ net add bgp router-id 10.10.10.2
cumulus@leaf02:~$ net add bgp neighbor underlay peer-group
cumulus@leaf02:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf02:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf02:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@leaf02:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@leaf02:~$ net commit
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ net add loopback lo ip address 10.10.10.3/32
cumulus@leaf03:~$ net add bond bond1 bond slaves swp1
cumulus@leaf03:~$ net add bond bond2 bond slaves swp2
cumulus@leaf03:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf03:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf03:~$ net add bridge bridge vlan-aware
cumulus@leaf03:~$ net add bond bond1 bridge access 10
cumulus@leaf03:~$ net add bond bond1 clag id 1
cumulus@leaf03:~$ net add bond bond1-2 bond lacp-bypass-allow
cumulus@leaf03:~$ net add bond bond1-2 mtu 9000
cumulus@leaf03:~$ net add bond bond1-2 stp bpduguard
cumulus@leaf03:~$ net add bond bond1-2 stp portadminedge
cumulus@leaf03:~$ net add bond bond2 bridge access 20
cumulus@leaf03:~$ net add bond bond2 clag id 2
cumulus@leaf03:~$ net add bridge bridge ports bond1,bond2
cumulus@lea303:~$ net add interface swp51-54 alias to spine
cumulus@leaf03:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf03:~$ net add interface swp49-50 alias peerlink
cumulus@leaf03:~$ net add bridge bridge ports peerlink
cumulus@leaf03:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf03:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.4
cumulus@leaf03:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf03:~$ net add interface peerlink.4094 clag priority 1000
cumulus@leaf03:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:BB
cumulus@leaf03:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.34
cumulus@leaf03:~$ net add vlan 10 ip forward off
cumulus@leaf03:~$ net add vlan 10 vlan-id 10
cumulus@leaf03:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 20 ip forward off
cumulus@leaf03:~$ net add vlan 20 vlan-id 20
cumulus@leaf03:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf03:~$ net add bridge bridge vids 10,20
cumulus@leaf03:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf03:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf03:~$ net add bridge bridge ports vni10,vni20
cumulus@leaf03:~$ net add vxlan vni10 bridge access 10
cumulus@leaf03:~$ net add vxlan vni20 bridge access 20
cumulus@leaf03:~$ net add bridge bridge vids 10,20
cumulus@leaf03:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@leaf03:~$ net add vxlan vni10,20 bridge learning off
cumulus@leaf03:~$ net add vxlan vni10,20 stp bpduguard
cumulus@leaf03:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@leaf03:~$ net add loopback lo vxlan local-tunnelip 10.10.10.3
cumulus@leaf03:~$ net add bgp autonomous-system 65103
cumulus@leaf03:~$ net add bgp router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp neighbor underlay peer-group
cumulus@leaf03:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf03:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf03:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf03:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@leaf03:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@leaf03:~$ net commit
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ net add loopback lo ip address 10.10.10.4/32
cumulus@leaf04:~$ net add bond bond1 bond slaves swp1
cumulus@leaf04:~$ net add bond bond2 bond slaves swp2
cumulus@leaf04:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf04:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf04:~$ net add bridge bridge vlan-aware
cumulus@leaf04:~$ net add bond bond1 bridge access 10
cumulus@leaf04:~$ net add bond bond1 clag id 1
cumulus@leaf04:~$ net add bond bond1-2 bond lacp-bypass-allow
cumulus@leaf04:~$ net add bond bond1-2 mtu 9000
cumulus@leaf04:~$ net add bond bond1-2 stp bpduguard
cumulus@leaf04:~$ net add bond bond1-2 stp portadminedge
cumulus@leaf04:~$ net add bond bond2 bridge access 20
cumulus@leaf04:~$ net add bond bond2 clag id 2
cumulus@leaf04:~$ net add bridge bridge ports bond1,bond2
cumulus@leaf04:~$ net add interface swp51-54 alias to spine
cumulus@leaf04:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf04:~$ net add interface swp49-50 alias peerlink
cumulus@leaf04:~$ net add bridge bridge ports peerlink
cumulus@leaf04:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf04:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.3
cumulus@leaf04:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf04:~$ net add interface peerlink.4094 clag priority 2000
cumulus@leaf04:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:BB
cumulus@leaf04:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.34
cumulus@leaf04:~$ net add vlan 10 ip forward off
cumulus@leaf04:~$ net add vlan 10 vlan-id 10
cumulus@leaf04:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 20 ip forward off
cumulus@leaf04:~$ net add vlan 20 vlan-id 20
cumulus@leaf04:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf04:~$ net add bridge bridge vids 10,20
cumulus@leaf04:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf04:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf04:~$ net add bridge bridge ports vni10,vni20
cumulus@leaf04:~$ net add bridge bridge vids 10,20
cumulus@leaf04:~$ net add vxlan vni10 bridge access 10
cumulus@leaf04:~$ net add vxlan vni20 bridge access 20
cumulus@leaf04:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@leaf04:~$ net add vxlan vni10,20 bridge learning off
cumulus@leaf04:~$ net add vxlan vni10,20 stp bpduguard
cumulus@leaf04:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@leaf04:~$ net add loopback lo vxlan local-tunnelip 10.10.10.4
cumulus@leaf04:~$ net add bgp autonomous-system 65104
cumulus@leaf04:~$ net add bgp router-id 10.10.10.4
cumulus@leaf04:~$ net add bgp neighbor underlay peer-group
cumulus@leaf04:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf04:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf04:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf04:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@leaf04:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@leaf04:~$ net commit
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add loopback lo ip address 10.10.10.101/32
cumulus@spine01:~$ net add interface swp1-6 alias to leaf
cumulus@spine01:~$ net add bgp autonomous-system 65199
cumulus@spine01:~$ net add bgp router-id 10.10.10.101
cumulus@spine01:~$ net add bgp neighbor underlay peer-group
cumulus@spine01:~$ net add bgp neighbor underlay remote-as external
cumulus@spine01:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine01:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine01:~$ net commit
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ net add loopback lo ip address 10.10.10.102/32
cumulus@spine02:~$ net add interface swp1-6 alias to leaf
cumulus@spine02:~$ net add bgp autonomous-system 65199
cumulus@spine02:~$ net add bgp router-id 10.10.10.102
cumulus@spine02:~$ net add bgp neighbor underlay peer-group
cumulus@spine02:~$ net add bgp neighbor underlay remote-as external
cumulus@spine02:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine02:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine02:~$ net commit
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ net add loopback lo ip address 10.10.10.103/32
cumulus@spine03:~$ net add interface swp1-6 alias to leaf
cumulus@spine03:~$ net add bgp autonomous-system 65199
cumulus@spine03:~$ net add bgp router-id 10.10.10.103
cumulus@spine03:~$ net add bgp neighbor underlay peer-group
cumulus@spine03:~$ net add bgp neighbor underlay remote-as external
cumulus@spine03:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine03:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine03:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine03:~$ net commit
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ net add loopback lo ip address 10.10.10.104/32
cumulus@spine04:~$ net add interface swp1-6 alias to leaf
cumulus@spine04:~$ net add bgp autonomous-system 65199
cumulus@spine04:~$ net add bgp router-id 10.10.10.104
cumulus@spine04:~$ net add bgp neighbor underlay peer-group
cumulus@spine04:~$ net add bgp neighbor underlay remote-as external
cumulus@spine04:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine04:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine04:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine04:~$ net commit
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ net add loopback lo ip address 10.10.10.63/32
cumulus@border01:~$ net add bond bond1 bond slaves swp3
cumulus@border01:~$ net add interface swp3 alias bond member of bond1
cumulus@border01:~$ net add interface swp51-54 alias to spine
cumulus@border01:~$ net add bond bond1 bridge vids 10,20
cumulus@border01:~$ net add bond bond1 clag id 1
cumulus@border01:~$ net add bond bond1 mtu 9000
cumulus@border01:~$ net add bridge bridge ports bond1
cumulus@border01:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@border01:~$ net add interface swp49-50 alias peerlink
cumulus@border01:~$ net add bridge bridge ports peerlink
cumulus@border01:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@border01:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.64
cumulus@border01:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@border01:~$ net add interface peerlink.4094 clag priority 1000
cumulus@border01:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:FF
cumulus@border01:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.255
cumulus@border01:~$ net add vlan 10 ip forward off
cumulus@border01:~$ net add vlan 10 vlan-id 10
cumulus@border01:~$ net add vlan 10 vlan-raw-device bridge
cumulus@border01:~$ net add vlan 20 ip forward off
cumulus@border01:~$ net add vlan 20 vlan-id 20
cumulus@border01:~$ net add vlan 20 vlan-raw-device bridge
cumulus@border01:~$ net add bridge bridge vids 10,20
cumulus@border01:~$ net add vxlan vni10 vxlan id 10
cumulus@border01:~$ net add vxlan vni20 vxlan id 20
cumulus@border01:~$ net add bridge bridge ports vni10,vni20
cumulus@border01:~$ net add bridge bridge vids 10,20
cumulus@border01:~$ net add bridge bridge vlan-aware
cumulus@border01:~$ net add loopback lo vxlan local-tunnelip 10.10.10.63
cumulus@border01:~$ net add vxlan vni10 bridge access 10
cumulus@border01:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@border01:~$ net add vxlan vni10,20 bridge learning off
cumulus@border01:~$ net add vxlan vni10,20 stp bpduguard
cumulus@border01:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@border01:~$ net add vxlan vni20 bridge access 20
cumulus@border01:~$ net add bgp autonomous-system 65253
cumulus@border01:~$ net add bgp router-id 10.10.10.63
cumulus@border01:~$ net add bgp neighbor underlay peer-group
cumulus@border01:~$ net add bgp neighbor underlay remote-as external
cumulus@border01:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@border01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@border01:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@border01:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@border01:~$ net commit
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ net add loopback lo ip address 10.10.10.64/32
cumulus@border02:~$ net add bond bond1 bond slaves swp3
cumulus@border02:~$ net add interface swp3 alias bond member of bond1
cumulus@border02:~$ net add interface swp51-54 alias to spine
cumulus@border02:~$ net add bond bond1 bridge vids 10,20
cumulus@border02:~$ net add bond bond1 clag id 1
cumulus@border02:~$ net add bond bond1 mtu 9000
cumulus@border02:~$ net add bridge bridge ports bond1
cumulus@border02:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@border02:~$ net add interface swp49-50 alias peerlink
cumulus@border02:~$ net add bridge bridge ports peerlink
cumulus@border02:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@border02:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.63
cumulus@border02:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@border02:~$ net add interface peerlink.4094 clag priority 2000
cumulus@border02:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:FF
cumulus@border02:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.255
cumulus@border02:~$ net add vlan 10 ip forward off
cumulus@border02:~$ net add vlan 10 vlan-id 10
cumulus@border02:~$ net add vlan 10 vlan-raw-device bridge
cumulus@border02:~$ net add vlan 20 ip forward off
cumulus@border02:~$ net add vlan 20 vlan-id 20
cumulus@border02:~$ net add vlan 20 vlan-raw-device bridge
cumulus@border02:~$ net add bridge bridge vids 10,20
cumulus@border02:~$ net add vxlan vni10 vxlan id 10
cumulus@border02:~$ net add vxlan vni20 vxlan id 20
cumulus@border02:~$ net add bridge bridge ports vni10,vni20
cumulus@border02:~$ net add bridge bridge vids 10,20
cumulus@border02:~$ net add bridge bridge vlan-aware
cumulus@border02:~$ net add loopback lo vxlan local-tunnelip 10.10.10.64
cumulus@border02:~$ net add vxlan vni10 bridge access 10
cumulus@border02:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@border02:~$ net add vxlan vni10,20 bridge learning off
cumulus@border02:~$ net add vxlan vni10,20 stp bpduguard
cumulus@border02:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@border02:~$ net add vxlan vni20 bridge access 20
cumulus@border02:~$ net add bgp autonomous-system 65254
cumulus@border02:~$ net add bgp router-id 10.10.10.64
cumulus@border02:~$ net add bgp neighbor underlay peer-group
cumulus@border02:~$ net add bgp neighbor underlay remote-as external
cumulus@border02:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@border02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@border02:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@border02:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@border02:~$ net commit
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID481 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.1
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 peerlink vni10 vni20
    bridge-vids 10 20
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:AA
auto vlan10
iface vlan10
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    vlan-id 20
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.2/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.2
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 peerlink vni10 vni20
    bridge-vids 10 20
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.1
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-sys-mac 44:38:39:BE:EF:AA
auto vlan10
iface vlan10
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    vlan-id 20
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.3/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.3
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 peerlink vni10 vni20
    bridge-vids 10 20
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.4
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:BB
auto vlan10
iface vlan10
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    vlan-id 20
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.4/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.4
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 peerlink vni10 vni20
    bridge-vids 10 20
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.3
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-sys-mac 44:38:39:BE:EF:BB
auto vlan10
iface vlan10
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    vlan-id 20
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.101/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.102/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.103/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.104/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.63/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.63
auto swp3
iface swp3
    alias bond member of bond1
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-slaves swp3
    bridge-vids 10 20
    clag-id 1
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 peerlink vni10 vni20
    bridge-vids 10 20
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.64
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:FF
auto vlan10
iface vlan10
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    vlan-id 20
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.64/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.64
auto swp3
iface swp3
    alias bond member of bond1
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-slaves swp3
    bridge-vids 10 20
    clag-id 1
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 peerlink vni10 vni20
    bridge-vids 10 20
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.63
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-sys-mac 44:38:39:BE:EF:FF
auto vlan10
iface vlan10
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    vlan-id 20
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID2310 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65102
 bgp router-id 10.10.10.2
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65103
 bgp router-id 10.10.10.3
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65104
 bgp router-id 10.10.10.4
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.102
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.103
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.104
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65253
 bgp router-id 10.10.10.63
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65254
 bgp router-id 10.10.10.64
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### NVUE Commands

The NVUE commands configure single VXLAN devices.

{{< tabs "TabID1615 ">}}
{{< tab "NVUE Commands">}}

{{< tabs "TabID1618 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1-2,swp49-54
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf01:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond1 link mtu 9000
cumulus@leaf01:~$ nv set interface bond2 link mtu 9000
cumulus@leaf01:~$ nv set interface bond1-2 bridge domain br_default
cumulus@leaf01:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf01:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:~$ nv set mlag priority 1000
cumulus@leaf01:~$ nv set mlag init-delay 10
cumulus@leaf01:~$ nv set interface vlan10
cumulus@leaf01:~$ nv set interface vlan20
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf01:~$ nv set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf01:~$ nv set evpn enable on
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp1-2,swp49-54
cumulus@leaf02:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf02:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf02:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond1 link mtu 9000
cumulus@leaf02:~$ nv set interface bond2 link mtu 9000
cumulus@leaf02:~$ nv set interface bond1-2 bridge domain br_default
cumulus@leaf02:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf02:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf02:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:~$ nv set mlag priority 2000
cumulus@leaf02:~$ nv set mlag init-delay 10
cumulus@leaf02:~$ nv set interface vlan10
cumulus@leaf02:~$ nv set interface vlan20
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf02:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf02:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf02:~$ nv set nve vxlan source address 10.10.10.2
cumulus@leaf02:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf02:~$ nv set evpn enable on
cumulus@leaf02:~$ nv set router bgp autonomous-system 65102
cumulus@leaf02:~$ nv set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf02:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ nv set interface swp1-2,swp49-54
cumulus@leaf03:~$ nv set interface bond1 bond member swp1
cumulus@leaf03:~$ nv set interface bond2 bond member swp2
cumulus@leaf03:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf03:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf03:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond1 link mtu 9000
cumulus@leaf03:~$ nv set interface bond2 link mtu 9000
cumulus@leaf03:~$ nv set interface bond1-2 bridge domain br_default
cumulus@leaf03:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf03:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf03:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf03:~$ nv set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf03:~$ nv set mlag backup 10.10.10.4
cumulus@leaf03:~$ nv set mlag peer-ip linklocal
cumulus@leaf03:~$ nv set mlag priority 1000
cumulus@leaf03:~$ nv set mlag init-delay 10
cumulus@leaf03:~$ nv set interface vlan10
cumulus@leaf03:~$ nv set interface vlan20
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf03:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf03:~$ nv set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf03:~$ nv set nve vxlan source address 10.10.10.3
cumulus@leaf03:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf03:~$ nv set evpn enable on
cumulus@leaf03:~$ nv set router bgp autonomous-system 65103
cumulus@leaf03:~$ nv set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf03:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf03:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ nv set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ nv set interface swp1-2,swp49-54
cumulus@leaf04:~$ nv set interface bond1 bond member swp1
cumulus@leaf04:~$ nv set interface bond2 bond member swp2
cumulus@leaf04:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf04:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf04:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond1 link mtu 9000
cumulus@leaf04:~$ nv set interface bond2 link mtu 9000
cumulus@leaf04:~$ nv set interface bond1-2 bridge domain br_default
cumulus@leaf04:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf04:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf04:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf04:~$ nv set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf04:~$ nv set mlag backup 10.10.10.3
cumulus@leaf04:~$ nv set mlag peer-ip linklocal
cumulus@leaf04:~$ nv set mlag priority 2000
cumulus@leaf04:~$ nv set mlag init-delay 10
cumulus@leaf04:~$ nv set interface vlan10
cumulus@leaf04:~$ nv set interface vlan20
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf04:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf04:~$ nv set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf04:~$ nv set nve vxlan source address 10.10.10.4
cumulus@leaf04:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf04:~$ nv set evpn enable on
cumulus@leaf04:~$ nv set router bgp autonomous-system 65104
cumulus@leaf04:~$ nv set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf04:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf04:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf04:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1-6
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine01:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ nv set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp1-6
cumulus@spine02:~$ nv set router bgp autonomous-system 65199
cumulus@spine02:~$ nv set router bgp router-id 10.10.10.102
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine02:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine02:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ nv set interface lo ip address 10.10.10.103/32
cumulus@spine03:~$ nv set interface swp1-6
cumulus@spine03:~$ nv set router bgp autonomous-system 65199
cumulus@spine03:~$ nv set router bgp router-id 10.10.10.103
cumulus@spine03:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine03:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine03:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine03:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine03:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ nv set interface lo ip address 10.10.10.104/32
cumulus@spine04:~$ nv set interface swp1-6
cumulus@spine04:~$ nv set router bgp autonomous-system 65199
cumulus@spine04:~$ nv set router bgp router-id 10.10.10.104
cumulus@spine04:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine04:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine04:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine04:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine04:~$ nv config apply
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ nv set interface lo ip address 10.10.10.63/32
cumulus@border01:~$ nv set interface swp3,swp49-54
cumulus@border01:~$ nv set interface bond3 bond member swp3
cumulus@border01:~$ nv set interface bond3 bond mlag id 1
cumulus@border01:~$ nv set interface bond3 bond lacp-bypass on
cumulus@border01:~$ nv set interface bond3 link mtu 9000
cumulus@border01:~$ nv set interface bond3 bridge domain br_default
cumulus@border01:~$ nv set interface peerlink bond member swp49-50
cumulus@border01:~$ nv set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border01:~$ nv set mlag backup 10.10.10.64
cumulus@border01:~$ nv set mlag peer-ip linklocal
cumulus@border01:~$ nv set mlag priority 1000
cumulus@border01:~$ nv set mlag init-delay 10
cumulus@border01:~$ nv set interface vlan10
cumulus@border01:~$ nv set interface vlan20
cumulus@border01:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@border01:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@border01:~$ nv set interface bond3 bridge domain br_default vlan 10,20
cumulus@border01:~$ nv set nve vxlan mlag shared-address 10.0.1.255
cumulus@border01:~$ nv set nve vxlan source address 10.10.10.63
cumulus@border01:~$ nv set nve vxlan arp-nd-suppress on
cumulus@border01:~$ nv set evpn enable on
cumulus@border01:~$ nv set router bgp autonomous-system 65253
cumulus@border01:~$ nv set router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@border01:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@border01:~$ nv config apply
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ nv set interface lo ip address 10.10.10.64/32
cumulus@border02:~$ nv set interface swp3,swp49-54
cumulus@border02:~$ nv set interface bond3 bond member swp3
cumulus@border02:~$ nv set interface bond3 bond mlag id 1
cumulus@border02:~$ nv set interface bond3 bond lacp-bypass on
cumulus@border02:~$ nv set interface bond3 link mtu 9000
cumulus@border02:~$ nv set interface bond3 bridge domain br_default
cumulus@border02:~$ nv set interface peerlink bond member swp49-50
cumulus@border02:~$ nv set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border02:~$ nv set mlag backup 10.10.10.63
cumulus@border02:~$ nv set mlag peer-ip linklocal
cumulus@border02:~$ nv set mlag priority 2000
cumulus@border02:~$ nv set mlag init-delay 10
cumulus@border02:~$ nv set interface vlan10
cumulus@border02:~$ nv set interface vlan20
cumulus@border02:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@border02:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@border02:~$ nv set interface bond3 bridge domain br_default vlan 10,20
cumulus@border02:~$ nv set nve vxlan mlag shared-address 10.0.1.255
cumulus@border02:~$ nv set nve vxlan source address 10.10.10.64
cumulus@border02:~$ nv set nve vxlan arp-nd-suppress on
cumulus@border02:~$ nv set evpn enable on
cumulus@border02:~$ nv set router bgp autonomous-system 65254
cumulus@border02:~$ nv set router bgp router-id 10.10.10.64
cumulus@border02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@border02:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@border02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

{{< tabs "TabID1976 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.2: {}
      peer-ip: linklocal
      priority: 1000
      init-delay: 10
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.12
        source:
          address: 10.10.10.1
        arp-nd-suppress: on
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65101
        router-id: 10.10.10.1
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.2/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.1: {}
      peer-ip: linklocal
      priority: 2000
      init-delay: 10
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.12
        source:
          address: 10.10.10.2
        arp-nd-suppress: on
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65102
        router-id: 10.10.10.2
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.3/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    mlag:
      mac-address: 44:38:39:BE:EF:BB
      backup:
        10.10.10.4: {}
      peer-ip: linklocal
      priority: 1000
      init-delay: 10
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.34
        source:
          address: 10.10.10.3
        arp-nd-suppress: on
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65103
        router-id: 10.10.10.3
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.4/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    mlag:
      mac-address: 44:38:39:BE:EF:BB
      backup:
        10.10.10.3: {}
      peer-ip: linklocal
      priority: 2000
      init-delay: 10
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.34
        source:
          address: 10.10.10.4
        arp-nd-suppress: on
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65104
        router-id: 10.10.10.4
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.101/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.101
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.102/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.102
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.103/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.103
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.104/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.104
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.63/32: {}
        type: loopback
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              vlan:
                '10': {}
                '20': {}
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
    mlag:
      mac-address: 44:38:39:BE:EF:FF
      backup:
        10.10.10.64: {}
      peer-ip: linklocal
      priority: 1000
      init-delay: 10
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.255
        source:
          address: 10.10.10.63
        arp-nd-suppress: on
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65253
        router-id: 10.10.10.63
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.64/32: {}
        type: loopback
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              vlan:
                '10': {}
                '20': {}
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
    mlag:
      mac-address: 44:38:39:BE:EF:FF
      backup:
        10.10.10.63: {}
      peer-ip: linklocal
      priority: 2000
      init-delay: 10
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.255
        source:
          address: 10.10.10.64
        arp-nd-suppress: on
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65254
        router-id: 10.10.10.64
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID3094 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.1
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off

auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink vxlan48
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.2/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.2
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink vxlan48
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.3/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.3
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-backup-ip 10.10.10.4
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:bb
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:bb
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink vxlan48
    hwaddress 44:38:39:22:01:bb
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.4/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.4
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-backup-ip 10.10.10.3
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:c1
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:c1
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink vxlan48
    hwaddress 44:38:39:22:01:c1
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.101/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.102/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.103/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.104/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.63/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.63
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-vids 10 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-backup-ip 10.10.10.64
    clagd-sys-mac 44:38:39:BE:EF:FF
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:ab
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:ab
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond3 peerlink vxlan48
    hwaddress 44:38:39:22:01:ab
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.64/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.64
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-vids 10 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-backup-ip 10.10.10.63
    clagd-sys-mac 44:38:39:BE:EF:FF
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:b3
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:b3
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond3 peerlink vxlan48
    hwaddress 44:38:39:22:01:b3
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
    ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID3232 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65101 vrf default
bgp router-id 10.10.10.1
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
...
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65102 vrf default
bgp router-id 10.10.10.2
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65103 vrf default
bgp router-id 10.10.10.3
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
...
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65104 vrf default
bgp router-id 10.10.10.4
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.101
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.102
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.103
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.104
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65253 vrf default
bgp router-id 10.10.10.63
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65254 vrf default
bgp router-id 10.10.10.64
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## EVPN Centralized Routing

The following example shows an EVPN centralized routing configuration:

- MLAG is configured between leaf01 and leaf02, leaf03 and leaf04, and border01 and border02
- BGP unnumbered is in the underlay (configured on all leafs and spines)
- SVIs are configured as gateways on the border leafs

The following images shows traffic flow between tenants. The spines and other devices are omitted for simplicity.

|   Traffic Flow between server01 and server05  |     |
| --- | --- |
| <img width=1000/> {{< img src="/images/cumulus-linux/evpn-central-diagram.png" >}} | server01 and server05 are in a different VLAN and are located across different leafs.<br><ol><li>server01 makes a LACP hash decision and forwards traffic to leaf01.</li><li>leaf01 does a layer 2 lookup and forwards traffic to server01's default gateway (border01) out VNI10.</li><li>border01 does a layer 3 lookup and routes the packet out VNI20 towards leaf04.</li><li>The VXLAN encapsulated frame arrives on leaf04, which does a layer 2 lookup and has the MAC address for server05 in VLAN20.</li></ul>|

### NCLU Commands

The NCLU commands configure traditional VXLAN devices.

{{< tabs "TabID3059 ">}}
{{< tab "NCLU Commands ">}}

{{< tabs "TabID3062 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@leaf01:~$ net add bond bond1 bond slaves swp1
cumulus@leaf01:~$ net add bond bond2 bond slaves swp2
cumulus@leaf01:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf01:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf01:~$ net add interface swp51-54 alias to spine
cumulus@leaf01:~$ net add bridge bridge vlan-aware
cumulus@leaf01:~$ net add bridge bridge ports bond1,bond2
cumulus@leaf01:~$ net add bond bond1 bridge access 10
cumulus@leaf01:~$ net add bond bond1 clag id 1
cumulus@leaf01:~$ net add bond bond1-2 bond lacp-bypass-allow
cumulus@leaf01:~$ net add bond bond1-2 mtu 9000
cumulus@leaf01:~$ net add bond bond1-2 stp bpduguard
cumulus@leaf01:~$ net add bond bond1-2 stp portadminedge
cumulus@leaf01:~$ net add bond bond2 bridge access 20
cumulus@leaf01:~$ net add bond bond2 clag id 2
cumulus@leaf01:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf01:~$ net add interface swp49-50 alias peerlink
cumulus@leaf01:~$ net add bridge bridge ports peerlink
cumulus@leaf01:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf01:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.2
cumulus@leaf01:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf01:~$ net add interface peerlink.4094 clag priority 1000
cumulus@leaf01:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.12
cumulus@leaf01:~$ net add loopback lo vxlan local-tunnelip 10.10.10.1
cumulus@leaf01:~$ net add vlan 10 vlan-id 10
cumulus@leaf01:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 20 vlan-id 20
cumulus@leaf01:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf01:~$ net add bridge bridge vids 10,20
cumulus@leaf01:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf01:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf01:~$ net add bridge bridge ports vni10,vni20
cumulus@leaf01:~$ net add vxlan vni10 bridge access 10
cumulus@leaf01:~$ net add vxlan vni20 bridge access 20
cumulus@leaf01:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@leaf01:~$ net add vxlan vni10,20 bridge learning off
cumulus@leaf01:~$ net add vxlan vni10,20 stp bpduguard
cumulus@leaf01:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@leaf01:~$ net add bgp autonomous-system 65101
cumulus@leaf01:~$ net add bgp router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp neighbor underlay peer-group
cumulus@leaf01:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf01:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf01:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@leaf01:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ net add loopback lo ip address 10.10.10.2/32
cumulus@leaf02:~$ net add bond bond1 bond slaves swp1
cumulus@leaf02:~$ net add bond bond2 bond slaves swp2
cumulus@leaf02:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf02:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf02:~$ net add interface swp49-50 alias peerlink
cumulus@leaf02:~$ net add interface swp51-54 alias to spine
cumulus@leaf02:~$ net add bridge bridge vlan-aware
cumulus@leaf02:~$ net add bond bond1 bridge access 10
cumulus@leaf02:~$ net add bond bond1 clag id 1
cumulus@leaf02:~$ net add bond bond1-2 bond lacp-bypass-allow
cumulus@leaf02:~$ net add bond bond1-2 mtu 9000
cumulus@leaf02:~$ net add bond bond1-2 stp bpduguard
cumulus@leaf02:~$ net add bond bond1-2 stp portadminedge
cumulus@leaf02:~$ net add bond bond2 bridge access 20
cumulus@leaf02:~$ net add bond bond2 clag id 2
cumulus@leaf02:~$ net add bridge bridge ports bond1,bond2
cumulus@leaf02:~$ net add bridge bridge ports vni10,vni20
cumulus@leaf02:~$ net add bridge bridge vids 10,20
cumulus@leaf02:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf02:~$ net add bridge bridge ports peerlink
cumulus@leaf02:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf02:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.1
cumulus@leaf02:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf02:~$ net add interface peerlink.4094 clag priority 2000
cumulus@leaf02:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.12
cumulus@leaf02:~$ net add loopback lo vxlan local-tunnelip 10.10.10.2
cumulus@leaf02:~$ net add vlan 10 vlan-id 10
cumulus@leaf02:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 20 vlan-id 20
cumulus@leaf02:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf02:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf02:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf02:~$ net add vxlan vni10 bridge access 10
cumulus@leaf02:~$ net add vxlan vni20 bridge access 20
cumulus@leaf02:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@leaf02:~$ net add vxlan vni10,20 bridge learning off
cumulus@leaf02:~$ net add vxlan vni10,20 stp bpduguard
cumulus@leaf02:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@leaf02:~$ net add bgp autonomous-system 65102
cumulus@leaf02:~$ net add bgp router-id 10.10.10.2
cumulus@leaf02:~$ net add bgp neighbor underlay peer-group
cumulus@leaf02:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf02:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf02:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@leaf02:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@leaf02:~$ net commit
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ net add loopback lo ip address 10.10.10.3/32
cumulus@leaf03:~$ net add bond bond1 bond slaves swp1
cumulus@leaf03:~$ net add bond bond2 bond slaves swp2
cumulus@leaf03:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf03:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf03:~$ net add interface swp51-54 alias to spine
cumulus@leaf03:~$ net add bridge bridge vlan-aware
cumulus@leaf03:~$ net add bond bond1 bridge access 10
cumulus@leaf03:~$ net add bond bond1 clag id 1
cumulus@leaf03:~$ net add bond bond1-2 bond lacp-bypass-allow
cumulus@leaf03:~$ net add bond bond1-2 mtu 9000
cumulus@leaf03:~$ net add bond bond1-2 stp bpduguard
cumulus@leaf03:~$ net add bond bond1-2 stp portadminedge
cumulus@leaf03:~$ net add bond bond2 bridge access 20
cumulus@leaf03:~$ net add bond bond2 clag id 2
cumulus@leaf03:~$ net add bridge bridge ports bond1,bond2
cumulus@leaf03:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf03:~$ net add interface swp49-50 alias peerlink
cumulus@leaf03:~$ net add bridge bridge ports peerlink
cumulus@leaf03:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf03:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.4
cumulus@leaf03:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf03:~$ net add interface peerlink.4094 clag priority 1000
cumulus@leaf03:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:BB
cumulus@leaf03:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.34
cumulus@leaf03:~$ net add loopback lo vxlan local-tunnelip 10.10.10.3
cumulus@leaf03:~$ net add vlan 10 vlan-id 10
cumulus@leaf03:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 20 vlan-id 20
cumulus@leaf03:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf03:~$ net add bridge bridge ports vni10,vni20
cumulus@leaf03:~$ net add bridge bridge vids 10,20
cumulus@leaf03:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf03:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf03:~$ net add vxlan vni10 bridge access 10
cumulus@leaf03:~$ net add vxlan vni20 bridge access 20
cumulus@leaf03:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@leaf03:~$ net add vxlan vni10,20 bridge learning off
cumulus@leaf03:~$ net add vxlan vni10,20 stp bpduguard
cumulus@leaf03:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@leaf03:~$ net add bgp autonomous-system 65103
cumulus@leaf03:~$ net add bgp router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp neighbor underlay peer-group
cumulus@leaf03:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf03:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf03:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf03:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@leaf03:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@leaf03:~$ net commit
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ net add loopback lo ip address 10.10.10.4/32
cumulus@leaf04:~$ net add bond bond1 bond slaves swp1
cumulus@leaf04:~$ net add bond bond2 bond slaves swp2
cumulus@leaf04:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf04:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf04:~$ net add interface swp51-54 alias to spine
cumulus@leaf04:~$ net add bridge bridge vlan-aware
cumulus@leaf04:~$ net add bond bond1 bridge access 10
cumulus@leaf04:~$ net add bond bond1 clag id 1
cumulus@leaf04:~$ net add bond bond1-2 bond lacp-bypass-allow
cumulus@leaf04:~$ net add bond bond1-2 mtu 9000
cumulus@leaf04:~$ net add bond bond1-2 stp bpduguard
cumulus@leaf04:~$ net add bond bond1-2 stp portadminedge
cumulus@leaf04:~$ net add bond bond2 bridge access 20
cumulus@leaf04:~$ net add bond bond2 clag id 2
cumulus@leaf04:~$ net add bridge bridge ports bond1,bond2
cumulus@leaf04:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf04:~$ net add interface swp49-50 alias peerlink
cumulus@leaf04:~$ net add bridge bridge ports peerlink
cumulus@leaf04:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf04:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.3
cumulus@leaf04:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf04:~$ net add interface peerlink.4094 clag priority 2000
cumulus@leaf04:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:BB
cumulus@leaf04:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.34
cumulus@leaf04:~$ net add loopback lo vxlan local-tunnelip 10.10.10.4
cumulus@leaf04:~$ net add vlan 10 vlan-id 10
cumulus@leaf04:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 20 vlan-id 20
cumulus@leaf04:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf04:~$ net add bridge bridge vids 10,20
cumulus@leaf04:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf04:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf04:~$ net add vxlan vni10 bridge access 10
cumulus@leaf04:~$ net add vxlan vni20 bridge access 20
cumulus@leaf04:~$ net add bridge bridge ports vni10,vni20
cumulus@leaf04:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@leaf04:~$ net add vxlan vni10,20 bridge learning off
cumulus@leaf04:~$ net add vxlan vni10,20 stp bpduguard
cumulus@leaf04:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@leaf04:~$ net add bgp autonomous-system 65104
cumulus@leaf04:~$ net add bgp router-id 10.10.10.4
cumulus@leaf04:~$ net add bgp neighbor underlay peer-group
cumulus@leaf04:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf04:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf04:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf04:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@leaf04:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@leaf04:~$ net commit
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add bgp autonomous-system 65199
cumulus@spine01:~$ net add bgp router-id 10.10.10.101
cumulus@spine01:~$ net add bgp neighbor underlay peer-group
cumulus@spine01:~$ net add bgp neighbor underlay remote-as external
cumulus@spine01:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine01:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine01:~$ net add interface swp1-6 alias to leaf
cumulus@spine01:~$ net add loopback lo ip address 10.10.10.101/32
cumulus@spine01:~$ net commit
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ net add bgp autonomous-system 65199
cumulus@spine02:~$ net add bgp router-id 10.10.10.102
cumulus@spine02:~$ net add bgp neighbor underlay peer-group
cumulus@spine02:~$ net add bgp neighbor underlay remote-as external
cumulus@spine02:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine02:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@spine02:~$ net add interface swp1-6 alias to leaf
cumulus@spine02:~$ net add loopback lo ip address 10.10.10.102/32
cumulus@spine02:~$ net commit
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ net add bgp autonomous-system 65199
cumulus@spine03:~$ net add bgp router-id 10.10.10.103
cumulus@spine03:~$ net add bgp neighbor underlay peer-group
cumulus@spine03:~$ net add bgp neighbor underlay remote-as external
cumulus@spine03:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine03:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine03:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@spine03:~$ net add interface swp1-6 alias to leaf
cumulus@spine03:~$ net add loopback lo ip address 10.10.10.103/32
cumulus@spine03:~$ net commit
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ net add bgp autonomous-system 65199
cumulus@spine04:~$ net add bgp router-id 10.10.10.104
cumulus@spine04:~$ net add bgp neighbor underlay peer-group
cumulus@spine04:~$ net add bgp neighbor underlay remote-as external
cumulus@spine04:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine04:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine04:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@spine04:~$ net add interface swp1-6 alias to leaf
cumulus@spine04:~$ net add loopback lo ip address 10.10.10.104/32
cumulus@spine04:~$ net commit
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ net add loopback lo ip address 10.10.10.63/32
cumulus@border01:~$ net add bond bond1 bond slaves swp3
cumulus@border01:~$ net add interface swp3 alias bond member of bond1
cumulus@border01:~$ net add interface swp51-54 alias to spine
cumulus@border01:~$ net add bridge bridge vlan-aware
cumulus@border01:~$ net add bond bond1 bridge vids 101-102
cumulus@border01:~$ net add bond bond1 clag id 1
cumulus@border01:~$ net add bond bond1 mtu 9000
cumulus@border01:~$ net add bridge bridge ports bond1
cumulus@border01:~$ net add bridge bridge ports peerlink
cumulus@border01:~$ net add bridge bridge ports vni10,vni20
cumulus@border01:~$ net add bridge bridge vids 10,20,101-102
cumulus@border01:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@border01:~$ net add interface swp49-50 alias peerlink
cumulus@border01:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@border01:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.64
cumulus@border01:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@border01:~$ net add interface peerlink.4094 clag priority 1000
cumulus@border01:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:FF
cumulus@border01:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.255
cumulus@border01:~$ net add loopback lo vxlan local-tunnelip 10.10.10.63
cumulus@border01:~$ net add vlan 10 ip address 10.1.10.2/24
cumulus@border01:~$ net add vlan 10 ip address-virtual 00:00:00:00:00:10 10.1.10.1/24
cumulus@border01:~$ net add vlan 10 vlan-id 10
cumulus@border01:~$ net add vlan 10 vlan-raw-device bridge
cumulus@border01:~$ net add vlan 101 ip address 10.1.101.2/24
cumulus@border01:~$ net add vlan 101 ip address-virtual 00:00:00:00:00:01 10.1.101.1/24
cumulus@border01:~$ net add vlan 101 vlan-id 101
cumulus@border01:~$ net add vlan 101 vlan-raw-device bridge
cumulus@border01:~$ net add vlan 102 ip address 10.1.102.2/24
cumulus@border01:~$ net add vlan 102 ip address-virtual 00:00:00:00:00:02 10.1.102.1/24
cumulus@border01:~$ net add vlan 102 vlan-id 102
cumulus@border01:~$ net add vlan 102 vlan-raw-device bridge
cumulus@border01:~$ net add vlan 20 ip address 10.1.20.2/24
cumulus@border01:~$ net add vlan 20 ip address-virtual 00:00:00:00:00:20 10.1.20.1/24
cumulus@border01:~$ net add vlan 20 vlan-id 20
cumulus@border01:~$ net add vlan 20 vlan-raw-device bridge
cumulus@border01:~$ net add vxlan vni10 vxlan id 10
cumulus@border01:~$ net add vxlan vni20 vxlan id 20
cumulus@border01:~$ net add vxlan vni10 bridge access 10
cumulus@border01:~$ net add vxlan vni20 bridge access 20
cumulus@border01:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@border01:~$ net add vxlan vni10,20 bridge learning off
cumulus@border01:~$ net add vxlan vni10,20 stp bpduguard
cumulus@border01:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@border01:~$ net add bgp autonomous-system 65253
cumulus@border01:~$ net add bgp router-id 10.10.10.63
cumulus@border01:~$ net add bgp neighbor underlay peer-group
cumulus@border01:~$ net add bgp neighbor underlay remote-as external
cumulus@border01:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@border01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@border01:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@border01:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@border01:~$ net add bgp l2vpn evpn advertise-default-gw
cumulus@border01:~$ net commit
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ net add loopback lo ip address 10.10.10.64/32
cumulus@border02:~$ net add bond bond1 bond slaves swp3
cumulus@border02:~$ net add interface swp3 alias bond member of bond1
cumulus@border02:~$ net add interface swp51-54 alias to spine
cumulus@border02:~$ net add bridge bridge vlan-aware
cumulus@border02:~$ net add bond bond1 bridge vids 101-102
cumulus@border02:~$ net add bond bond1 clag id 1
cumulus@border02:~$ net add bond bond1 mtu 9000
cumulus@border02:~$ net add bridge bridge ports bond1
cumulus@border02:~$ net add bridge bridge vids 10,20,101-102
cumulus@border02:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@border02:~$ net add interface swp49-50 alias peerlink
cumulus@border02:~$ net add bridge bridge ports peerlink
cumulus@border02:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@border02:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.63
cumulus@border02:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@border02:~$ net add interface peerlink.4094 clag priority 2000
cumulus@border02:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:FF
cumulus@border02:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.255
cumulus@border02:~$ net add loopback lo vxlan local-tunnelip 10.10.10.64
cumulus@border02:~$ net add vlan 10 ip address 10.1.10.1/24
cumulus@border02:~$ net add vlan 10 ip address-virtual 00:00:00:00:00:10 10.1.10.1/24
cumulus@border02:~$ net add vlan 10 vlan-id 10
cumulus@border02:~$ net add vlan 10 vlan-raw-device bridge
cumulus@border02:~$ net add vlan 20 ip address 10.1.20.1/24
cumulus@border02:~$ net add vlan 20 ip address-virtual 00:00:00:00:00:20 10.1.20.1/24
cumulus@border02:~$ net add vlan 20 vlan-id 20
cumulus@border02:~$ net add vlan 20 vlan-raw-device bridge
cumulus@border02:~$ net add vlan 101 ip address 10.1.101.1/24
cumulus@border02:~$ net add vlan 101 ip address-virtual 00:00:00:00:00:01 10.1.101.1/24
cumulus@border02:~$ net add vlan 101 vlan-id 101
cumulus@border02:~$ net add vlan 101 vlan-raw-device bridge
cumulus@border02:~$ net add vlan 102 ip address 10.1.102.1/24
cumulus@border02:~$ net add vlan 102 ip address-virtual 00:00:00:00:00:02 10.1.102.1/24
cumulus@border02:~$ net add vlan 102 vlan-id 102
cumulus@border02:~$ net add vlan 102 vlan-raw-device bridge
cumulus@border02:~$ net add vxlan vni10 vxlan id 10
cumulus@border02:~$ net add vxlan vni20 vxlan id 20
cumulus@border02:~$ net add vxlan vni10 bridge access 10
cumulus@border02:~$ net add vxlan vni20 bridge access 20
cumulus@border02:~$ net add bridge bridge ports vni10,vni20
cumulus@border02:~$ net add vxlan vni10,20 bridge arp-nd-suppress on
cumulus@border02:~$ net add vxlan vni10,20 bridge learning off
cumulus@border02:~$ net add vxlan vni10,20 stp bpduguard
cumulus@border02:~$ net add vxlan vni10,20 stp portbpdufilter
cumulus@border02:~$ net add bgp autonomous-system 65254
cumulus@border02:~$ net add bgp router-id 10.10.10.64
cumulus@border02:~$ net add bgp neighbor underlay peer-group
cumulus@border02:~$ net add bgp neighbor underlay remote-as external
cumulus@border02:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@border02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@border02:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@border02:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@border02:~$ net add bgp l2vpn evpn advertise-default-gw
cumulus@border02:~$ net commit
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID3518 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.1
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 peerlink vni10 vni20
    bridge-vids 10 20
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:AA
auto vlan10
iface vlan10
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    vlan-id 20
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.2/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.2
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 vni10 vni20 peerlink
    bridge-vids 10 20
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.1
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-sys-mac 44:38:39:BE:EF:AA
auto vlan10
iface vlan10
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    vlan-id 20
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.3/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.3
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 peerlink vni10 vni20
    bridge-vids 10 20
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.4
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:BB
auto vlan10
iface vlan10
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    vlan-id 20
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.4/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.4
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 peerlink vni10 vni20
    bridge-vids 10 20
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.3
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-sys-mac 44:38:39:BE:EF:BB
auto vlan10
iface vlan10
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    vlan-id 20
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.101/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.102/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
   address 10.10.10.103/32
auto swp1
iface swp1
   alias to leaf
auto swp2
iface swp2
   alias to leaf
auto swp3
iface swp3
   alias to leaf
auto swp4
iface swp4
   alias to leaf
auto swp5
iface swp5
   alias to leaf
auto swp6
iface swp6
   alias to leaf
auto mgmt
iface mgmt
   vrf-table auto
   address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
   vrf mgmt
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.104/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.63/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.63
auto swp3
iface swp3
    alias bond member of bond1
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-slaves swp3
    bridge-vids 101-102
    clag-id 1
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 peerlink vni10 vni20
    bridge-vids 10 20 101-102
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.64
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:FF
auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vlan-id 20
    vlan-raw-device bridge
auto vlan101
iface vlan101
    address 10.1.101.2/24
    address-virtual 00:00:00:00:00:01 10.1.101.1/24
    vlan-id 101
    vlan-raw-device bridge
auto vlan102
iface vlan102
    address 10.1.102.2/24
    address-virtual 00:00:00:00:00:02 10.1.102.1/24
    vlan-id 102
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.64/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.64
auto swp3
iface swp3
    alias bond member of bond1
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto bond1
iface bond1
    bond-slaves swp3
    bridge-vids 101-102
    clag-id 1
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 peerlink vni10 vni20
    bridge-vids 10 20 101-102
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.63
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-sys-mac 44:38:39:BE:EF:FF
auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vlan-id 20
    vlan-raw-device bridge
auto vlan101
iface vlan101
    address 10.1.101.2/24
    address-virtual 00:00:00:00:00:01 10.1.101.1/24
    vlan-id 101
    vlan-raw-device bridge
auto vlan102
iface vlan102
    address 10.1.102.2/24
    address-virtual 00:00:00:00:00:02 10.1.102.1/24
    vlan-id 102
    vlan-raw-device bridge
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID4333 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65102
 bgp router-id 10.10.10.2
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65103
 bgp router-id 10.10.10.3
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65104
 bgp router-id 10.10.10.4
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
!
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.102
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
!
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.103
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
!
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.104
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
!
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65253
 bgp router-id 10.10.10.63
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
  advertise-default-gw
 exit-address-family
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65254
 bgp router-id 10.10.10.64
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
  advertise-default-gw
 exit-address-family
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### NVUE Commands

The NVUE commands configure single VXLAN devices.

{{< tabs "TabID4619 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID4622 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1-2,swp49-54
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf01:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond1 link mtu 9000
cumulus@leaf01:~$ nv set interface bond2 link mtu 9000
cumulus@leaf01:~$ nv set interface bond1-2 bridge domain br_default
cumulus@leaf01:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf01:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:~$ nv set mlag priority 1000
cumulus@leaf01:~$ nv set mlag init-delay 10
cumulus@leaf01:~$ nv set interface vlan10
cumulus@leaf01:~$ nv set interface vlan20
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf01:~$ nv set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf01:~$ nv set evpn enable on
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp1-2,swp49-54
cumulus@leaf02:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf02:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf02:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond1 link mtu 9000
cumulus@leaf02:~$ nv set interface bond2 link mtu 9000
cumulus@leaf02:~$ nv set interface bond1-2 bridge domain br_default
cumulus@leaf02:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf02:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf02:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:~$ nv set mlag priority 2000
cumulus@leaf02:~$ nv set mlag init-delay 10
cumulus@leaf02:~$ nv set interface vlan10
cumulus@leaf02:~$ nv set interface vlan20
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf02:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf02:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf02:~$ nv set nve vxlan source address 10.10.10.2
cumulus@leaf02:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf02:~$ nv set evpn enable on
cumulus@leaf02:~$ nv set router bgp autonomous-system 65102
cumulus@leaf02:~$ nv set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf02:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ nv set interface swp1-2,swp49-54
cumulus@leaf03:~$ nv set interface bond1 bond member swp1
cumulus@leaf03:~$ nv set interface bond2 bond member swp2
cumulus@leaf03:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf03:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf03:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond1 link mtu 9000
cumulus@leaf03:~$ nv set interface bond2 link mtu 9000
cumulus@leaf03:~$ nv set interface bond1-2 bridge domain br_default
cumulus@leaf03:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf03:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf03:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf03:~$ nv set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf03:~$ nv set mlag backup 10.10.10.4
cumulus@leaf03:~$ nv set mlag peer-ip linklocal
cumulus@leaf03:~$ nv set mlag priority 1000
cumulus@leaf03:~$ nv set mlag init-delay 10
cumulus@leaf03:~$ nv set interface vlan10
cumulus@leaf03:~$ nv set interface vlan20
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf03:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf03:~$ nv set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf03:~$ nv set nve vxlan source address 10.10.10.3
cumulus@leaf03:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf03:~$ nv set evpn enable on
cumulus@leaf03:~$ nv set router bgp autonomous-system 65103
cumulus@leaf03:~$ nv set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf03:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf03:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ nv set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ nv set interface swp1-2,swp49-54
cumulus@leaf04:~$ nv set interface bond1 bond member swp1
cumulus@leaf04:~$ nv set interface bond2 bond member swp2
cumulus@leaf04:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf04:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf04:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond1 link mtu 9000
cumulus@leaf04:~$ nv set interface bond2 link mtu 9000
cumulus@leaf04:~$ nv set interface bond1-2 bridge domain br_default
cumulus@leaf04:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf04:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf04:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf04:~$ nv set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf04:~$ nv set mlag backup 10.10.10.3
cumulus@leaf04:~$ nv set mlag peer-ip linklocal
cumulus@leaf04:~$ nv set mlag priority 2000
cumulus@leaf04:~$ nv set mlag init-delay 10
cumulus@leaf04:~$ nv set interface vlan10
cumulus@leaf04:~$ nv set interface vlan20
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf04:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf04:~$ nv set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf04:~$ nv set nve vxlan source address 10.10.10.4
cumulus@leaf04:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf04:~$ nv set evpn enable on
cumulus@leaf04:~$ nv set router bgp autonomous-system 65104
cumulus@leaf04:~$ nv set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf04:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf04:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf04:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1-6
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine01:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ nv set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp1-6
cumulus@spine02:~$ nv set router bgp autonomous-system 65199
cumulus@spine02:~$ nv set router bgp router-id 10.10.10.102
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine02:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine02:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ nv set interface lo ip address 10.10.10.103/32
cumulus@spine03:~$ nv set interface swp1-6
cumulus@spine03:~$ nv set router bgp autonomous-system 65199
cumulus@spine03:~$ nv set router bgp router-id 10.10.10.103
cumulus@spine03:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine03:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine03:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine03:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine03:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ nv set interface lo ip address 10.10.10.104/32
cumulus@spine04:~$ nv set interface swp1-6
cumulus@spine04:~$ nv set router bgp autonomous-system 65199
cumulus@spine04:~$ nv set router bgp router-id 10.10.10.104
cumulus@spine04:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine04:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine04:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine04:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine04:~$ nv config apply
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ nv set interface lo ip address 10.10.10.63/32
cumulus@border01:~$ nv set interface swp1-3,swp49-54
cumulus@border01:~$ nv set interface bond3 bond member swp3
cumulus@border01:~$ nv set interface bond3 bond mlag id 1
cumulus@border01:~$ nv set interface bond3 bond lacp-bypass on
cumulus@border01:~$ nv set interface bond3 link mtu 9000
cumulus@border01:~$ nv set interface bond3 bridge domain br_default
cumulus@border01:~$ nv set interface peerlink bond member swp49-50
cumulus@border01:~$ nv set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border01:~$ nv set mlag backup 10.10.10.64
cumulus@border01:~$ nv set mlag peer-ip linklocal
cumulus@border01:~$ nv set mlag priority 1000
cumulus@border01:~$ nv set mlag init-delay 10
cumulus@border01:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@border01:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@border01:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@border01:~$ nv set interface vlan10 ip vrr state up
cumulus@border01:~$ nv set interface vlan20 ip address 10.1.10.2/24
cumulus@border01:~$ nv set interface vlan20 ip vrr address 10.1.20.2/24
cumulus@border01:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@border01:~$ nv set interface vlan20 ip vrr state up
cumulus@border01:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@border01:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@border01:~$ nv set interface bond3 bridge domain br_default vlan 10,20
cumulus@border01:~$ nv set nve vxlan mlag shared-address 10.0.1.255
cumulus@border01:~$ nv set nve vxlan source address 10.10.10.63
cumulus@border01:~$ nv set nve vxlan arp-nd-suppress on
cumulus@border01:~$ nv set evpn enable on
cumulus@border01:~$ nv set router bgp autonomous-system 65253
cumulus@border01:~$ nv set router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@border01:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@border01:~$ nv set evpn route-advertise default-gateway on
cumulus@border01:~$ nv config apply
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ nv set interface lo ip address 10.10.10.64/32
cumulus@border02:~$ nv set interface swp1-3,swp49-54
cumulus@border02:~$ nv set interface bond3 bond member swp3
cumulus@border02:~$ nv set interface bond3 bond mlag id 1
cumulus@border02:~$ nv set interface bond3 bond lacp-bypass on
cumulus@border02:~$ nv set interface bond3 link mtu 9000
cumulus@border02:~$ nv set interface bond3 bridge domain br_default
cumulus@border02:~$ nv set interface peerlink bond member swp49-50
cumulus@border02:~$ nv set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border02:~$ nv set mlag backup 10.10.10.63
cumulus@border02:~$ nv set mlag peer-ip linklocal
cumulus@border02:~$ nv set mlag priority 2000
cumulus@border02:~$ nv set mlag init-delay 10
cumulus@border02:~$ nv set interface vlan10 ip address 10.1.10.1/24
cumulus@border02:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@border02:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@border02:~$ nv set interface vlan10 ip vrr state up
cumulus@border02:~$ nv set interface vlan20 ip address 10.1.20.1/24
cumulus@border02:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@border02:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@border02:~$ nv set interface vlan20 ip vrr state up
cumulus@border02:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@border02:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@border02:~$ nv set interface bond3 bridge domain br_default vlan 10,20
cumulus@border02:~$ nv set nve vxlan mlag shared-address 10.0.1.255
cumulus@border02:~$ nv set nve vxlan source address 10.10.10.64
cumulus@border02:~$ nv set nve vxlan arp-nd-suppress on
cumulus@border02:~$ nv set evpn enable on
cumulus@border02:~$ nv set router bgp autonomous-system 65254
cumulus@border02:~$ nv set router bgp router-id 10.10.10.64
cumulus@border02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@border02:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@border02:~$ nv set evpn route-advertise default-gateway on
cumulus@border02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

{{< tabs "TabID6641 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.2: {}
      peer-ip: linklocal
      priority: 1000
      init-delay: 10
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.12
        source:
          address: 10.10.10.1
        arp-nd-suppress: on
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65101
        router-id: 10.10.10.1
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.2/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.1: {}
      peer-ip: linklocal
      priority: 2000
      init-delay: 10
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.12
        source:
          address: 10.10.10.2
        arp-nd-suppress: on
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65102
        router-id: 10.10.10.2
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.3/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    mlag:
      mac-address: 44:38:39:BE:EF:BB
      backup:
        10.10.10.4: {}
      peer-ip: linklocal
      priority: 1000
      init-delay: 10
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.34
        source:
          address: 10.10.10.3
        arp-nd-suppress: on
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65103
        router-id: 10.10.10.3
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.4/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    mlag:
      mac-address: 44:38:39:BE:EF:BB
      backup:
        10.10.10.3: {}
      peer-ip: linklocal
      priority: 2000
      init-delay: 10
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.34
        source:
          address: 10.10.10.4
        arp-nd-suppress: on
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65104
        router-id: 10.10.10.4
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.101/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.101
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.102/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.102
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.103/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.103
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.104/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.104
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.63/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              vlan:
                '10': {}
                '20': {}
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        ip:
          address:
            10.1.10.2/24: {}
          vrr:
            address:
              10.1.10.1/24: {}
            mac-address: 00:00:00:00:00:10
            state:
              up: {}
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.10.2/24: {}
          vrr:
            address:
              10.1.20.2/24: {}
            mac-address: 00:00:00:00:00:20
            state:
              up: {}
        type: svi
        vlan: 20
    mlag:
      mac-address: 44:38:39:BE:EF:FF
      backup:
        10.10.10.64: {}
      peer-ip: linklocal
      priority: 1000
      init-delay: 10
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.255
        source:
          address: 10.10.10.63
        arp-nd-suppress: on
    evpn:
      enable: on
      route-advertise:
        default-gateway: on
    router:
      bgp:
        enable: on
        autonomous-system: 65253
        router-id: 10.10.10.63
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.64/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              vlan:
                '10': {}
                '20': {}
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        ip:
          address:
            10.1.10.1/24: {}
          vrr:
            address:
              10.1.10.1/24: {}
            mac-address: 00:00:00:00:00:10
            state:
              up: {}
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.1/24: {}
          vrr:
            address:
              10.1.20.1/24: {}
            mac-address: 00:00:00:00:00:20
            state:
              up: {}
        type: svi
        vlan: 20
    mlag:
      mac-address: 44:38:39:BE:EF:FF
      backup:
        10.10.10.63: {}
      peer-ip: linklocal
      priority: 2000
      init-delay: 10
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.255
        source:
          address: 10.10.10.64
        arp-nd-suppress: on
    evpn:
      enable: on
      route-advertise:
        default-gateway: on
    router:
      bgp:
        enable: on
        autonomous-system: 65254
        router-id: 10.10.10.64
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID7807 ">}}
{{< tab "leaf01 ">}}

```
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.1
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink vxlan48
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
...
auto lo
iface lo inet loopback
    address 10.10.10.2/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.2
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink vxlan48
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
...
auto lo
iface lo inet loopback
    address 10.10.10.3/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.3
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-backup-ip 10.10.10.4
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink vxlan48
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
...
auto lo
iface lo inet loopback
    address 10.10.10.4/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.4
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-backup-ip 10.10.10.3
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink vxlan48
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
...
auto lo
iface lo inet loopback
    address 10.10.10.101/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
...
auto lo
iface lo inet loopback
    address 10.10.10.102/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6

```

{{< /tab >}}
{{< tab "spine03 ">}}

```
...
auto lo
iface lo inet loopback
    address 10.10.10.103/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
...
auto lo
iface lo inet loopback
    address 10.10.10.104/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "border01 ">}}

```
...
auto lo
iface lo inet loopback
    address 10.10.10.63/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.63
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-vids 10 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-backup-ip 10.10.10.64
    clagd-sys-mac 44:38:39:BE:EF:FF
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    hwaddress 44:38:39:22:01:ab
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.10.2/24
    address-virtual 00:00:00:00:00:20 10.1.20.2/24
    hwaddress 44:38:39:22:01:ab
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond3 peerlink vxlan48
    hwaddress 44:38:39:22:01:ab
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "border02 ">}}

```
...
auto lo
iface lo inet loopback
    address 10.10.10.64/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.64
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-vids 10 20
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-backup-ip 10.10.10.63
    clagd-sys-mac 44:38:39:BE:EF:FF
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    address 10.1.10.1/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    hwaddress 44:38:39:22:01:b3
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.1/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    hwaddress 44:38:39:22:01:b3
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond3 peerlink vxlan48
    hwaddress 44:38:39:22:01:b3
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID7883 ">}}
{{< tab "leaf01 ">}}

```
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65101 vrf default
bgp router-id 10.10.10.1
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65102 vrf default
bgp router-id 10.10.10.2
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65103 vrf default
bgp router-id 10.10.10.3
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65104 vrf default
bgp router-id 10.10.10.4
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.101
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.102
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.103
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.104
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
```

{{< /tab >}}
{{< tab "border01 ">}}

```
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65253 vrf default
bgp router-id 10.10.10.63
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
advertise-default-gw
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "border02 ">}}

```
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65254 vrf default
bgp router-id 10.10.10.64
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
advertise-default-gw
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## EVPN Symmetric Routing

The following example shows an EVPN symmetric routing configuration, where:
- MLAG is configured between leaf01 and leaf02, leaf03 and leaf04, and border01 and border02
- BGP unnumbered is in the underlay (configured on all leafs and spines)
- VRF BLUE and VRF RED are configured on the leafs for traffic flow between tenants for traffic isolation

The following images shows traffic flow between tenants. The spines and other devices are omitted for simplicity.

|   Traffic Flow between server01 and server04  |     |
| --- | --- |
| <img width=1000/> {{< img src="/images/cumulus-linux/EVPN-same-VLAN.png" >}} | server01 and server04 are in the same VRF and the same VLAN but are located across different leafs.<br><ol><li>server01 makes a LACP hash decision and forwards traffic to leaf01.</li><li>leaf01 does a layer 2 lookup and has the MAC address for server04, it then forwards the packet out VNI10, through leaf04.</li><li>The VXLAN encapsulated frame arrives on leaf04, which does a layer 2 lookup and has the MAC address for server04 in VLAN10.</li></ul>|

|  Traffic Flow between server01 and server05   |     |
| --- | --- |
| <img width=1150/> {{< img src="/images/cumulus-linux/EVPN-different-VLAN.png"  >}} | server01 and server05 are in the same VRF, different VLANs, and are located across different leafs.<br><ol><li>server01 makes an LACP hash decision to reach the default gateway and forwards traffic to leaf01.</li><li>leaf01 does a layer 3 lookup in VRF RED and has a route out VNIRED through leaf04.</li><li>The VXLAN encapsulated packet arrives on leaf04, which does a layer 3 lookup in VRF RED and has a route through VLAN20 to server05.</li></ul> |

|   Traffic Flow between server01 and server06  |     |
| --- | --- |
| <img width=1300/> {{< img src="/images/cumulus-linux/EVPN-different-VRF.png"  >}} | server01 and server06 are in different VRFs, different VLANs, and are located across different leafs.<br><ol><li>server01 makes an LACP hash decision to reach the default gateway and forwards traffic to leaf01.</li><li>leaf01 does a layer 3 lookup in VRF RED and has a route out VNIRED through border01.</li><li>The VXLAN encapsulated packet arrives on border01, which does a layer 3 lookup in VRF RED and has a route through VLAN101 to fw01 (the policy device).</li><li>fw01 does a layer 3 lookup (without any VRFs) and has a route in VLAN40, through border02.</li><li>border02 does a layer 3 lookup in VRF BLUE and has a route out VNIBLUE, through leaf04.</li><li>The VXLAN encapsulated packet arrives on leaf04, which does a layer 3 lookup in VRF BLUE and has a route in VLAN30 to server06.</ul>|

### NCLU Commands

The NCLU commands configure traditional VXLAN devices.

{{< tabs "TabID5728 ">}}
{{< tab "NCLU Commands ">}}

{{< tabs "TabID5731 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@leaf01:~$ net add bond bond1 bond slaves swp1
cumulus@leaf01:~$ net add bond bond2 bond slaves swp2
cumulus@leaf01:~$ net add bond bond3 bond slaves swp3
cumulus@leaf01:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf01:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf01:~$ net add interface swp3 alias bond member of bond3
cumulus@leaf01:~$ net add interface swp51-54 alias to spine
cumulus@leaf01:~$ net add bridge bridge vlan-aware
cumulus@leaf01:~$ net add bond bond1 bridge access 10
cumulus@leaf01:~$ net add bond bond1 clag id 1
cumulus@leaf01:~$ net add bond bond1-3 bond lacp-bypass-allow
cumulus@leaf01:~$ net add bond bond1-3 mtu 9000
cumulus@leaf01:~$ net add bond bond1-3 stp bpduguard
cumulus@leaf01:~$ net add bond bond1-3 stp portadminedge
cumulus@leaf01:~$ net add bond bond2 bridge access 20
cumulus@leaf01:~$ net add bond bond2 clag id 2
cumulus@leaf01:~$ net add bond bond3 bridge access 30
cumulus@leaf01:~$ net add bond bond3 clag id 3
cumulus@leaf01:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf01:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf01:~$ net add interface swp49-50 alias peerlink
cumulus@leaf01:~$ net add bridge bridge ports peerlink
cumulus@leaf01:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf01:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.2
cumulus@leaf01:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf01:~$ net add interface peerlink.4094 clag priority 1000
cumulus@leaf01:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.12
cumulus@leaf01:~$ net add vrf RED vni 4001
cumulus@leaf01:~$ net add vrf BLUE vni 4002
cumulus@leaf01:~$ net add vlan 10 ip address 10.1.10.2/24
cumulus@leaf01:~$ net add vlan 10 ip address-virtual 00:00:00:00:00:10 10.1.10.1/24
cumulus@leaf01:~$ net add vlan 10 vlan-id 10
cumulus@leaf01:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 10 vrf RED
cumulus@leaf01:~$ net add vlan 20 ip address 10.1.20.2/24
cumulus@leaf01:~$ net add vlan 20 ip address-virtual 00:00:00:00:00:20 10.1.20.1/24
cumulus@leaf01:~$ net add vlan 20 vlan-id 20
cumulus@leaf01:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 20 vrf RED
cumulus@leaf01:~$ net add vlan 30 ip address 10.1.30.2/24
cumulus@leaf01:~$ net add vlan 30 ip address-virtual 00:00:00:00:00:30 10.1.30.1/24
cumulus@leaf01:~$ net add vlan 30 vlan-id 30
cumulus@leaf01:~$ net add vlan 30 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 30 vrf BLUE
cumulus@leaf01:~$ net add vlan 4001 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add vlan 4001 vlan-id 4001
cumulus@leaf01:~$ net add vlan 4001 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 4001 vrf RED
cumulus@leaf01:~$ net add vlan 4002 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add vlan 4002 vlan-id 4002
cumulus@leaf01:~$ net add vlan 4002 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 4002 vrf BLUE
cumulus@leaf01:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf01:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf01:~$ net add vxlan vni30 vxlan id 30
cumulus@leaf01:~$ net add vxlan vniBLUE vxlan id 4002
cumulus@leaf01:~$ net add vxlan vniRED vxlan id 4001
cumulus@leaf01:~$ net add vxlan vni10 bridge access 10
cumulus@leaf01:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge arp-nd-suppress on
cumulus@leaf01:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge learning off
cumulus@leaf01:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp bpduguard
cumulus@leaf01:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp portbpdufilter
cumulus@leaf01:~$ net add vxlan vni20 bridge access 20
cumulus@leaf01:~$ net add vxlan vni30 bridge access 30
cumulus@leaf01:~$ net add vxlan vniBLUE bridge access 4002
cumulus@leaf01:~$ net add vxlan vniRED bridge access 4001
cumulus@leaf01:~$ net add bridge bridge ports vni10,vni20,vni30,vniRED,vniBLUE
cumulus@leaf01:~$ net add bridge bridge vids 10,20,30,4001-4002
cumulus@leaf01:~$ net add loopback lo vxlan local-tunnelip 10.10.10.1
cumulus@leaf01:~$ net add bgp autonomous-system 65101
cumulus@leaf01:~$ net add bgp router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp neighbor underlay peer-group
cumulus@leaf01:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf01:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf01:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@leaf01:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@leaf01:~$ net add bgp vrf RED autonomous-system 65101
cumulus@leaf01:~$ net add bgp vrf RED router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp vrf RED ipv4 unicast redistribute connected
cumulus@leaf01:~$ net add bgp vrf RED l2vpn evpn  advertise ipv4 unicast
cumulus@leaf01:~$ net add bgp vrf BLUE autonomous-system 65101
cumulus@leaf01:~$ net add bgp vrf BLUE router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp vrf BLUE ipv4 unicast redistribute connected
cumulus@leaf01:~$ net add bgp vrf BLUE l2vpn evpn advertise ipv4 unicast
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ net add loopback lo ip address 10.10.10.2/32
cumulus@leaf02:~$ net add bond bond1 bond slaves swp1
cumulus@leaf02:~$ net add bond bond2 bond slaves swp2
cumulus@leaf02:~$ net add bond bond3 bond slaves swp3
cumulus@leaf02:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf02:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf02:~$ net add interface swp3 alias bond member of bond3
cumulus@leaf02:~$ net add interface swp51-54 alias to spine
cumulus@leaf02:~$ net add bridge bridge vlan-aware
cumulus@leaf02:~$ net add bond bond1 bridge access 10
cumulus@leaf02:~$ net add bond bond1 clag id 1
cumulus@leaf02:~$ net add bond bond1-3 bond lacp-bypass-allow
cumulus@leaf02:~$ net add bond bond1-3 mtu 9000
cumulus@leaf02:~$ net add bond bond1-3 stp bpduguard
cumulus@leaf02:~$ net add bond bond1-3 stp portadminedge
cumulus@leaf02:~$ net add bond bond2 bridge access 20
cumulus@leaf02:~$ net add bond bond2 clag id 2
cumulus@leaf02:~$ net add bond bond3 bridge access 30
cumulus@leaf02:~$ net add bond bond3 clag id 3
cumulus@leaf02:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf02:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf02:~$ net add interface swp49-50 alias peerlink
cumulus@leaf02:~$ net add bridge bridge ports peerlink
cumulus@leaf02:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf02:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.1
cumulus@leaf02:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf02:~$ net add interface peerlink.4094 clag priority 2000
cumulus@leaf02:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.12
cumulus@leaf02:~$ net add vlan 10 ip address 10.1.10.3/24
cumulus@leaf02:~$ net add vlan 10 ip address-virtual 00:00:00:00:00:10 10.1.10.1/24
cumulus@leaf02:~$ net add vlan 10 vlan-id 10
cumulus@leaf02:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 10 vrf RED
cumulus@leaf02:~$ net add vlan 20 ip address 10.1.20.3/24
cumulus@leaf02:~$ net add vlan 20 ip address-virtual 00:00:00:00:00:20 10.1.20.1/24
cumulus@leaf02:~$ net add vlan 20 vlan-id 20
cumulus@leaf02:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 20 vrf RED
cumulus@leaf02:~$ net add vlan 30 ip address 10.1.30.3/24
cumulus@leaf02:~$ net add vlan 30 ip address-virtual 00:00:00:00:00:30 10.1.30.1/24
cumulus@leaf02:~$ net add vlan 30 vlan-id 30
cumulus@leaf02:~$ net add vlan 30 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 30 vrf BLUE
cumulus@leaf02:~$ net add vlan 4001 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf02:~$ net add vlan 4001 vlan-id 4001
cumulus@leaf02:~$ net add vlan 4001 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 4001 vrf RED
cumulus@leaf02:~$ net add vlan 4002 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf02:~$ net add vlan 4002 vlan-id 4002
cumulus@leaf02:~$ net add vlan 4002 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 4002 vrf BLUE
cumulus@leaf02:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf02:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf02:~$ net add vxlan vni30 vxlan id 30
cumulus@leaf02:~$ net add vxlan vniBLUE vxlan id 4002
cumulus@leaf02:~$ net add vxlan vniRED vxlan id 4001
cumulus@leaf02:~$ net add vxlan vni10 bridge access 10
cumulus@leaf02:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge arp-nd-suppress on
cumulus@leaf02:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge learning off
cumulus@leaf02:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp bpduguard
cumulus@leaf02:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp portbpdufilter
cumulus@leaf02:~$ net add vxlan vni20 bridge access 20
cumulus@leaf02:~$ net add vxlan vni30 bridge access 30
cumulus@leaf02:~$ net add vrf RED vni 4001
cumulus@leaf02:~$ net add vrf BLUE vni 4002
cumulus@leaf02:~$ net add vxlan vniBLUE bridge access 4002
cumulus@leaf02:~$ net add vxlan vniRED bridge access 4001
cumulus@leaf02:~$ net add bridge bridge ports vni10,vni20,vni30,vniRED,vniBLUE
cumulus@leaf02:~$ net add bridge bridge vids 10,20,30,4001-4002
cumulus@leaf02:~$ net add loopback lo vxlan local-tunnelip 10.10.10.2
cumulus@leaf02:~$ net add bgp autonomous-system 65102
cumulus@leaf02:~$ net add bgp router-id 10.10.10.2
cumulus@leaf02:~$ net add bgp neighbor underlay peer-group
cumulus@leaf02:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf02:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf02:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@leaf02:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@leaf02:~$ net add bgp vrf RED autonomous-system 65102
cumulus@leaf02:~$ net add bgp vrf RED router-id 10.10.10.2
cumulus@leaf02:~$ net add bgp vrf RED ipv4 unicast redistribute connected
cumulus@leaf02:~$ net add bgp vrf RED l2vpn evpn  advertise ipv4 unicast
cumulus@leaf02:~$ net add bgp vrf BLUE autonomous-system 65101
cumulus@leaf02:~$ net add bgp vrf BLUE router-id 10.10.10.2
cumulus@leaf02:~$ net add bgp vrf BLUE ipv4 unicast redistribute connected
cumulus@leaf02:~$ net add bgp vrf BLUE l2vpn evpn advertise ipv4 unicast
cumulus@leaf02:~$ net commit
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ net add loopback lo ip address 10.10.10.3/32
cumulus@leaf03:~$ net add bond bond1 bond slaves swp1
cumulus@leaf03:~$ net add bond bond2 bond slaves swp2
cumulus@leaf03:~$ net add bond bond3 bond slaves swp3
cumulus@leaf03:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf03:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf03:~$ net add interface swp3 alias bond member of bond3
cumulus@leaf03:~$ net add interface swp51-54 alias to spine
cumulus@leaf03:~$ net add bond bond1 bridge access 10
cumulus@leaf03:~$ net add bond bond1 clag id 1
cumulus@leaf03:~$ net add bond bond1-3 bond lacp-bypass-allow
cumulus@leaf03:~$ net add bond bond1-3 mtu 9000
cumulus@leaf03:~$ net add bond bond1-3 stp bpduguard
cumulus@leaf03:~$ net add bond bond1-3 stp portadminedge
cumulus@leaf03:~$ net add bond bond2 bridge access 20
cumulus@leaf03:~$ net add bond bond2 clag id 2
cumulus@leaf03:~$ net add bond bond3 bridge access 30
cumulus@leaf03:~$ net add bond bond3 clag id 3
cumulus@leaf03:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf03:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf03:~$ net add interface swp49-50 alias peerlink
cumulus@leaf03:~$ net add bridge bridge ports peerlink
cumulus@leaf03:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf03:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.4
cumulus@leaf03:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf03:~$ net add interface peerlink.4094 clag priority 1000
cumulus@leaf03:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:BB
cumulus@leaf03:~$ net add bridge bridge vlan-aware
cumulus@leaf03:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.34
cumulus@leaf03:~$ net add vlan 10 ip address 10.1.10.4/24
cumulus@leaf03:~$ net add vlan 10 ip address-virtual 00:00:00:00:00:10 10.1.10.1/24
cumulus@leaf03:~$ net add vlan 10 vlan-id 10
cumulus@leaf03:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 10 vrf RED
cumulus@leaf03:~$ net add vlan 20 ip address 10.1.20.4/24
cumulus@leaf03:~$ net add vlan 20 ip address-virtual 00:00:00:00:00:20 10.1.20.1/24
cumulus@leaf03:~$ net add vlan 20 vlan-id 20
cumulus@leaf03:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 20 vrf RED
cumulus@leaf03:~$ net add vlan 30 ip address 10.1.30.4/24
cumulus@leaf03:~$ net add vlan 30 ip address-virtual 00:00:00:00:00:30 10.1.30.1/24
cumulus@leaf03:~$ net add vlan 30 vlan-id 30
cumulus@leaf03:~$ net add vlan 30 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 30 vrf BLUE
cumulus@leaf03:~$ net add vlan 4001 hwaddress 44:38:39:BE:EF:BB
cumulus@leaf03:~$ net add vlan 4001 vlan-id 4001
cumulus@leaf03:~$ net add vlan 4001 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 4001 vrf RED
cumulus@leaf03:~$ net add vlan 4002 hwaddress 44:38:39:BE:EF:BB
cumulus@leaf03:~$ net add vlan 4002 vlan-id 4002
cumulus@leaf03:~$ net add vlan 4002 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 4002 vrf BLUE
cumulus@leaf03:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf03:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf03:~$ net add vxlan vni30 vxlan id 30
cumulus@leaf03:~$ net add vxlan vniBLUE vxlan id 4002
cumulus@leaf03:~$ net add vxlan vniRED vxlan id 4001
cumulus@leaf03:~$ net add vrf RED vni 4001
cumulus@leaf03:~$ net add vrf BLUE vni 4002
cumulus@leaf03:~$ net add vxlan vni10 bridge access 10
cumulus@leaf03:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge arp-nd-suppress on
cumulus@leaf03:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge learning off
cumulus@leaf03:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp bpduguard
cumulus@leaf03:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp portbpdufilter
cumulus@leaf03:~$ net add vxlan vni20 bridge access 20
cumulus@leaf03:~$ net add vxlan vni30 bridge access 30
cumulus@leaf03:~$ net add vxlan vniBLUE bridge access 4002
cumulus@leaf03:~$ net add vxlan vniRED bridge access 4001
cumulus@leaf03:~$ net add bridge bridge ports vni10,vni20,vni30,vniRED,vniBLUE
cumulus@leaf03:~$ net add bridge bridge vids 10,20,30,4001-4002
cumulus@leaf03:~$ net add loopback lo vxlan local-tunnelip 10.10.10.3
cumulus@leaf03:~$ net add bgp autonomous-system 65103
cumulus@leaf03:~$ net add bgp router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp neighbor underlay peer-group
cumulus@leaf03:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf03:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf03:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf03:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@leaf03:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@leaf03:~$ net add bgp vrf RED autonomous-system 65103
cumulus@leaf03:~$ net add bgp vrf RED router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp vrf RED ipv4 unicast redistribute connected
cumulus@leaf03:~$ net add bgp vrf RED l2vpn evpn  advertise ipv4 unicast
cumulus@leaf03:~$ net add bgp vrf BLUE autonomous-system 65103
cumulus@leaf03:~$ net add bgp vrf BLUE router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp vrf BLUE ipv4 unicast redistribute connected
cumulus@leaf03:~$ net add bgp vrf BLUE l2vpn evpn advertise ipv4 unicast
cumulus@leaf03:~$ net commit
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ net add loopback lo ip address 10.10.10.4/32
cumulus@leaf04:~$ net add bond bond1 bond slaves swp1
cumulus@leaf04:~$ net add bond bond2 bond slaves swp2
cumulus@leaf04:~$ net add bond bond3 bond slaves swp3
cumulus@leaf04:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf04:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf04:~$ net add interface swp3 alias bond member of bond3
cumulus@leaf04:~$ net add interface swp51-54 alias to spine
cumulus@leaf04:~$ net add bond bond1 bridge access 10
cumulus@leaf04:~$ net add bond bond1 clag id 1
cumulus@leaf04:~$ net add bond bond1-3 bond lacp-bypass-allow
cumulus@leaf04:~$ net add bond bond1-3 mtu 9000
cumulus@leaf04:~$ net add bond bond1-3 stp bpduguard
cumulus@leaf04:~$ net add bond bond1-3 stp portadminedge
cumulus@leaf04:~$ net add bond bond2 bridge access 20
cumulus@leaf04:~$ net add bond bond2 clag id 2
cumulus@leaf04:~$ net add bond bond3 bridge access 30
cumulus@leaf04:~$ net add bond bond3 clag id 3
cumulus@leaf04:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf04:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@leaf04:~$ net add interface swp49-50 alias peerlink
cumulus@leaf04:~$ net add bridge bridge ports peerlink
cumulus@leaf04:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@leaf04:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.3
cumulus@leaf04:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@leaf04:~$ net add interface peerlink.4094 clag priority 2000
cumulus@leaf04:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:BB
cumulus@leaf04:~$ net add bridge bridge vlan-aware
cumulus@leaf04:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.34
cumulus@leaf04:~$ net add vrf RED vni 4001
cumulus@leaf04:~$ net add vrf BLUE vni 4002
cumulus@leaf04:~$ net add vlan 10 ip address 10.1.10.5/24
cumulus@leaf04:~$ net add vlan 10 ip address-virtual 00:00:00:00:00:10 10.1.10.1/24
cumulus@leaf04:~$ net add vlan 10 vlan-id 10
cumulus@leaf04:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 10 vrf RED
cumulus@leaf04:~$ net add vlan 20 ip address 10.1.20.5/24
cumulus@leaf04:~$ net add vlan 20 ip address-virtual 00:00:00:00:00:20 10.1.20.1/24
cumulus@leaf04:~$ net add vlan 20 vlan-id 20
cumulus@leaf04:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 20 vrf RED
cumulus@leaf04:~$ net add vlan 30 ip address 10.1.30.5/24
cumulus@leaf04:~$ net add vlan 30 ip address-virtual 00:00:00:00:00:30 10.1.30.1/24
cumulus@leaf04:~$ net add vlan 30 vlan-id 30
cumulus@leaf04:~$ net add vlan 30 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 30 vrf BLUE
cumulus@leaf04:~$ net add vlan 4001 hwaddress 44:38:39:BE:EF:BB
cumulus@leaf04:~$ net add vlan 4001 vlan-id 4001
cumulus@leaf04:~$ net add vlan 4001 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 4001 vrf RED
cumulus@leaf04:~$ net add vlan 4002 hwaddress 44:38:39:BE:EF:BB
cumulus@leaf04:~$ net add vlan 4002 vlan-id 4002
cumulus@leaf04:~$ net add vlan 4002 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 4002 vrf BLUE
cumulus@leaf04:~$ net add vrf BLUE,mgmt,RED vrf-table auto
cumulus@leaf04:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf04:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf04:~$ net add vxlan vni30 vxlan id 30
cumulus@leaf04:~$ net add vxlan vniBLUE vxlan id 4002
cumulus@leaf04:~$ net add vxlan vniRED vxlan id 4001
cumulus@leaf04:~$ net add vxlan vni10 bridge access 10
cumulus@leaf04:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge arp-nd-suppress on
cumulus@leaf04:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge learning off
cumulus@leaf04:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp bpduguard
cumulus@leaf04:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp portbpdufilter
cumulus@leaf04:~$ net add vxlan vni20 bridge access 20
cumulus@leaf04:~$ net add vxlan vni30 bridge access 30
cumulus@leaf04:~$ net add vxlan vniBLUE bridge access 4002
cumulus@leaf04:~$ net add vxlan vniRED bridge access 4001
cumulus@leaf04:~$ net add bridge bridge ports vni10,vni20,vni30,vniRED,vniBLUE
cumulus@leaf04:~$ net add bridge bridge vids 10,20,30,4001-4002
cumulus@leaf04:~$ net add loopback lo vxlan local-tunnelip 10.10.10.4
cumulus@leaf04:~$ net add bgp autonomous-system 65104
cumulus@leaf04:~$ net add bgp router-id 10.10.10.4
cumulus@leaf04:~$ net add bgp neighbor underlay peer-group
cumulus@leaf04:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf04:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@leaf04:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf04:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@leaf04:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@leaf04:~$ net add bgp vrf RED autonomous-system 65104
cumulus@leaf04:~$ net add bgp vrf RED router-id 10.10.10.4
cumulus@leaf04:~$ net add bgp vrf RED ipv4 unicast redistribute connected
cumulus@leaf04:~$ net add bgp vrf RED l2vpn evpn  advertise ipv4 unicast
cumulus@leaf04:~$ net add bgp vrf BLUE autonomous-system 65104
cumulus@leaf04:~$ net add bgp vrf BLUE router-id 10.10.10.4
cumulus@leaf04:~$ net add bgp vrf BLUE ipv4 unicast redistribute connected
cumulus@leaf04:~$ net add bgp vrf BLUE l2vpn evpn advertise ipv4 unicast
cumulus@leaf04:~$ net commit
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add loopback lo ip address 10.10.10.101/32
cumulus@spine01:~$ net add bgp autonomous-system 65199
cumulus@spine01:~$ net add bgp router-id 10.10.10.101
cumulus@spine01:~$ net add bgp neighbor underlay peer-group
cumulus@spine01:~$ net add bgp neighbor underlay remote-as external
cumulus@spine01:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine01:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine01:~$ net add interface swp1-6 alias to leaf
cumulus@spine01:~$ net commit
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ net add loopback lo ip address 10.10.10.102/32
cumulus@spine02:~$ net add bgp autonomous-system 65199
cumulus@spine02:~$ net add bgp router-id 10.10.10.102
cumulus@spine02:~$ net add bgp neighbor underlay peer-group
cumulus@spine02:~$ net add bgp neighbor underlay remote-as external
cumulus@spine02:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine02:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine02:~$ net add interface swp1-6 alias to leaf
cumulus@spine02:~$ net commit
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ net add loopback lo ip address 10.10.10.103/32
cumulus@spine03:~$ net add bgp autonomous-system 65199
cumulus@spine03:~$ net add bgp router-id 10.10.10.103
cumulus@spine03:~$ net add bgp neighbor underlay peer-group
cumulus@spine03:~$ net add bgp neighbor underlay remote-as external
cumulus@spine03:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine03:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine03:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine03:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine03:~$ net add interface swp1-6 alias to leaf
cumulus@spine03:~$ net commit
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ net add loopback lo ip address 10.10.10.104/32
cumulus@spine04:~$ net add bgp autonomous-system 65199
cumulus@spine04:~$ net add bgp router-id 10.10.10.104
cumulus@spine04:~$ net add bgp neighbor underlay peer-group
cumulus@spine04:~$ net add bgp neighbor underlay remote-as external
cumulus@spine04:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp5 interface peer-group underlay
cumulus@spine04:~$ net add bgp neighbor swp6 interface peer-group underlay
cumulus@spine04:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine04:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine04:~$ net add interface swp1-6 alias to leaf
cumulus@spine04:~$ net commit
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ net add loopback lo ip address 10.10.10.63/32
cumulus@border01:~$ net add bond bond1 bond slaves swp3
cumulus@border01:~$ net add interface swp3 alias bond member of bond1
cumulus@border01:~$ net add interface swp49-50 alias peerlink
cumulus@border01:~$ net add interface swp51-54 alias to spine
cumulus@border01:~$ net add vxlan vniBLUE vxlan id 4002
cumulus@border01:~$ net add vxlan vniRED vxlan id 4001
cumulus@border01:~$ net add bond bond1 bridge vids 101-102
cumulus@border01:~$ net add bond bond1 clag id 1
cumulus@border01:~$ net add bond bond1 mtu 9000
cumulus@border01:~$ net add bridge bridge ports bond1
cumulus@border01:~$ net add bridge bridge ports peerlink
cumulus@border01:~$ net add bridge bridge ports vniRED,vniBLUE
cumulus@border01:~$ net add bridge bridge vids 101-102,4001-4002
cumulus@border01:~$ net add bridge bridge vlan-aware
cumulus@border01:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@border01:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@border01:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.64
cumulus@border01:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@border01:~$ net add interface peerlink.4094 clag priority 1000
cumulus@border01:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:FF
cumulus@border01:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.255
cumulus@border01:~$ net add vrf RED vni 4001
cumulus@border01:~$ net add vrf BLUE vni 4002
cumulus@border01:~$ net add vlan 101 ip address 10.1.101.64/24
cumulus@border01:~$ net add vlan 101 ip address-virtual 00:00:00:00:00:01 10.1.101.1/24
cumulus@border01:~$ net add vlan 101 vlan-id 101
cumulus@border01:~$ net add vlan 101 vlan-raw-device bridge
cumulus@border01:~$ net add vlan 101 vrf RED
cumulus@border01:~$ net add vlan 102 ip address 10.1.102.64/24
cumulus@border01:~$ net add vlan 102 ip address-virtual 00:00:00:00:00:02 10.1.102.1/24
cumulus@border01:~$ net add vlan 102 vlan-id 102
cumulus@border01:~$ net add vlan 102 vlan-raw-device bridge
cumulus@border01:~$ net add vlan 102 vrf BLUE
cumulus@border01:~$ net add vlan 4001 hwaddress 44:38:39:BE:EF:FF
cumulus@border01:~$ net add vlan 4001 vlan-id 4001
cumulus@border01:~$ net add vlan 4001 vlan-raw-device bridge
cumulus@border01:~$ net add vlan 4001 vrf RED
cumulus@border01:~$ net add vlan 4002 hwaddress 44:38:39:BE:EF:FF
cumulus@border01:~$ net add vlan 4002 vlan-id 4002
cumulus@border01:~$ net add vlan 4002 vlan-raw-device bridge
cumulus@border01:~$ net add vlan 4002 vrf BLUE
cumulus@border01:~$ net add vxlan vniBLUE bridge access 4002
cumulus@border01:~$ net add vxlan vniBLUE,vniRED bridge arp-nd-suppress on
cumulus@border01:~$ net add vxlan vniBLUE,vniRED bridge learning off
cumulus@border01:~$ net add vxlan vniBLUE,vniRED stp bpduguard
cumulus@border01:~$ net add vxlan vniBLUE,vniRED stp portbpdufilter
cumulus@border01:~$ net add vxlan vniRED bridge access 4001
cumulus@border01:~$ net add loopback lo vxlan local-tunnelip 10.10.10.63
cumulus@border01:~$ net add bgp autonomous-system 65253
cumulus@border01:~$ net add bgp router-id 10.10.10.63
cumulus@border01:~$ net add bgp neighbor underlay peer-group
cumulus@border01:~$ net add bgp neighbor underlay remote-as external
cumulus@border01:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@border01:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@border01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@border01:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@border01:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@border01:~$ net add bgp vrf RED autonomous-system 65253
cumulus@border01:~$ net add bgp vrf RED router-id 10.10.10.63
cumulus@border01:~$ net add bgp vrf RED ipv4 unicast redistribute static
cumulus@border01:~$ net add bgp vrf RED l2vpn evpn  advertise ipv4 unicast
cumulus@border01:~$ net add bgp vrf BLUE autonomous-system 65253
cumulus@border01:~$ net add bgp vrf BLUE router-id 10.10.10.63
cumulus@border01:~$ net add bgp vrf BLUE ipv4 unicast redistribute static
cumulus@border01:~$ net add bgp vrf BLUE l2vpn evpn  advertise ipv4 unicast
cumulus@border01:~$ net commit
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ net add loopback lo ip address 10.10.10.64/32
cumulus@border02:~$ net add bond bond1 bond slaves swp3
cumulus@border02:~$ net add interface swp3 alias bond member of bond1
cumulus@border02:~$ net add interface swp49-50 alias peerlink
cumulus@border02:~$ net add interface swp51-54 alias to spine
cumulus@border02:~$ net add vxlan vniBLUE vxlan id 4002
cumulus@border02:~$ net add vxlan vniRED vxlan id 4001
cumulus@border02:~$ net add bond bond1 bridge vids 101-102
cumulus@border02:~$ net add bond bond1 clag id 1
cumulus@border02:~$ net add bond bond1 mtu 9000
cumulus@border02:~$ net add bridge bridge ports bond1
cumulus@border02:~$ net add bridge bridge ports peerlink
cumulus@border02:~$ net add bridge bridge ports vniRED,vniBLUE
cumulus@border02:~$ net add bridge bridge vids 101-102,4001-4002
cumulus@border02:~$ net add bridge bridge vlan-aware
cumulus@border02:~$ net add bond peerlink bond slaves swp49,swp50
cumulus@border02:~$ net add interface peerlink.4094 clag args --initDelay 10
cumulus@border02:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.63
cumulus@border02:~$ net add interface peerlink.4094 clag peer-ip linklocal
cumulus@border02:~$ net add interface peerlink.4094 clag priority 2000
cumulus@border02:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:BE:EF:FF
cumulus@border02:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.255
cumulus@border02:~$ net add vrf RED vni 4001
cumulus@border02:~$ net add vrf BLUE vni 4002
cumulus@border02:~$ net add vlan 101 ip address 10.1.101.65/24
cumulus@border02:~$ net add vlan 101 ip address-virtual 00:00:00:00:00:01 10.1.101.1/24
cumulus@border02:~$ net add vlan 101 vlan-id 101
cumulus@border02:~$ net add vlan 101 vlan-raw-device bridge
cumulus@border02:~$ net add vlan 101 vrf RED
cumulus@border02:~$ net add vlan 102 ip address 10.1.102.65/24
cumulus@border02:~$ net add vlan 102 ip address-virtual 00:00:00:00:00:02 10.1.102.1/24
cumulus@border02:~$ net add vlan 102 vlan-id 102
cumulus@border02:~$ net add vlan 102 vlan-raw-device bridge
cumulus@border02:~$ net add vlan 102 vrf BLUE
cumulus@border02:~$ net add vlan 4001 hwaddress 44:38:39:BE:EF:FF
cumulus@border02:~$ net add vlan 4001 vlan-id 4001
cumulus@border02:~$ net add vlan 4001 vlan-raw-device bridge
cumulus@border02:~$ net add vlan 4001 vrf RED
cumulus@border02:~$ net add vlan 4002 hwaddress 44:38:39:BE:EF:FF
cumulus@border02:~$ net add vlan 4002 vlan-id 4002
cumulus@border02:~$ net add vlan 4002 vlan-raw-device bridge
cumulus@border02:~$ net add vlan 4002 vrf BLUE
cumulus@border02:~$ net add vxlan vniBLUE bridge access 4002
cumulus@border02:~$ net add vxlan vniBLUE,vniRED bridge arp-nd-suppress on
cumulus@border02:~$ net add vxlan vniBLUE,vniRED bridge learning off
cumulus@border02:~$ net add vxlan vniBLUE,vniRED stp bpduguard
cumulus@border02:~$ net add vxlan vniBLUE,vniRED stp portbpdufilter
cumulus@border02:~$ net add vxlan vniRED bridge access 4001
cumulus@border02:~$ net add loopback lo vxlan local-tunnelip 10.10.10.64
cumulus@border02:~$ net add bgp autonomous-system 65254
cumulus@border02:~$ net add bgp router-id 10.10.10.64
cumulus@border02:~$ net add bgp neighbor underlay peer-group
cumulus@border02:~$ net add bgp neighbor underlay remote-as external
cumulus@border02:~$ net add bgp neighbor peerlink.4094 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp53 interface peer-group underlay
cumulus@border02:~$ net add bgp neighbor swp54 interface peer-group underlay
cumulus@border02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@border02:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@border02:~$ net add bgp l2vpn evpn  advertise-all-vni
cumulus@border02:~$ net add bgp vrf RED autonomous-system 65254
cumulus@border02:~$ net add bgp vrf RED router-id 10.10.10.64
cumulus@border02:~$ net add bgp vrf RED ipv4 unicast redistribute static
cumulus@border02:~$ net add bgp vrf RED l2vpn evpn  advertise ipv4 unicast
cumulus@border02:~$ net add bgp vrf BLUE autonomous-system 65254
cumulus@border02:~$ net add bgp vrf BLUE router-id 10.10.10.64
cumulus@border02:~$ net add bgp vrf BLUE ipv4 unicast redistribute static
cumulus@border02:~$ net add bgp vrf BLUE l2vpn evpn  advertise ipv4 unicast
cumulus@border02:~$ net commit
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID6369 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.1
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp3
iface swp3
    alias bond member of bond3
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto BLUE
iface BLUE
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond3
iface bond3
    bond-lacp-bypass-allow yes
    bond-slaves swp3
    bridge-access 30
    clag-id 3
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 bond3 peerlink vni10 vni20 vni30 vniBLUE vniRED
    bridge-vids 10 20 30 4001-4002
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:AA
auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vlan-id 10
    vlan-raw-device bridge
    vrf RED
auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vlan-id 20
    vlan-raw-device bridge
    vrf RED
auto vlan30
iface vlan30
    address 10.1.30.2/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vlan-id 30
    vlan-raw-device bridge
    vrf BLUE
auto vlan4001
iface vlan4001
    hwaddress 44:38:39:BE:EF:AA
    vlan-id 4001
    vlan-raw-device bridge
    vrf RED
auto vlan4002
iface vlan4002
    hwaddress 44:38:39:BE:EF:AA
    vlan-id 4002
    vlan-raw-device bridge
    vrf BLUE
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
auto vni30
iface vni30
    bridge-access 30
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 30
auto vniBLUE
iface vniBLUE
    bridge-access 4002
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4002
auto vniRED
iface vniRED
    bridge-access 4001
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4001
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.2/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.2
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp3
iface swp3
    alias bond member of bond3
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto BLUE
iface BLUE
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond3
iface bond3
    bond-lacp-bypass-allow yes
    bond-slaves swp3
    bridge-access 30
    clag-id 3
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 bond3 peerlink vni10 vni20 vni30 vniBLUE vniRED
    bridge-vids 10 20 30 4001-4002
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.1
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-sys-mac 44:38:39:BE:EF:AA
auto vlan10
iface vlan10
    address 10.1.10.3/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vlan-id 10
    vlan-raw-device bridge
    vrf RED
auto vlan20
iface vlan20
    address 10.1.20.3/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vlan-id 20
    vlan-raw-device bridge
    vrf RED
auto vlan30
iface vlan30
    address 10.1.30.3/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vlan-id 30
    vlan-raw-device bridge
    vrf BLUE
auto vlan4001
iface vlan4001
    hwaddress 44:38:39:BE:EF:AA
    vlan-id 4001
    vlan-raw-device bridge
    vrf RED
auto vlan4002
iface vlan4002
    hwaddress 44:38:39:BE:EF:AA
    vlan-id 4002
    vlan-raw-device bridge
    vrf BLUE
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
auto vni30
iface vni30
    bridge-access 30
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 30
auto vniBLUE
iface vniBLUE
    bridge-access 4002
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4002
auto vniRED
iface vniRED
    bridge-access 4001
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4001
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.3/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.3
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp3
iface swp3
    alias bond member of bond3
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto BLUE
iface BLUE
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond3
iface bond3
    bond-lacp-bypass-allow yes
    bond-slaves swp3
    bridge-access 30
    clag-id 3
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 bond3 peerlink vni10 vni20 vni30 vniBLUE vniRED
    bridge-vids 10 20 30 4001-4002
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.4
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:BB
auto vlan10
iface vlan10
    address 10.1.10.4/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vlan-id 10
    vlan-raw-device bridge
    vrf RED
auto vlan20
iface vlan20
    address 10.1.20.4/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vlan-id 20
    vlan-raw-device bridge
    vrf RED
auto vlan30
iface vlan30
    address 10.1.30.4/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vlan-id 30
    vlan-raw-device bridge
    vrf BLUE
auto vlan4001
iface vlan4001
    hwaddress 44:38:39:BE:EF:BB
    vlan-id 4001
    vlan-raw-device bridge
    vrf RED
auto vlan4002
iface vlan4002
    hwaddress 44:38:39:BE:EF:BB
    vlan-id 4002
    vlan-raw-device bridge
    vrf BLUE
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
auto vni30
iface vni30
    bridge-access 30
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 30
auto vniBLUE
iface vniBLUE
    bridge-access 4002
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4002
auto vniRED
iface vniRED
    bridge-access 4001
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4001
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.4/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.4
auto swp1
iface swp1
    alias bond member of bond1
auto swp2
iface swp2
    alias bond member of bond2
auto swp3
iface swp3
    alias bond member of bond3
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto BLUE
iface BLUE
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bond3
iface bond3
    bond-lacp-bypass-allow yes
    bond-slaves swp3
    bridge-access 30
    clag-id 3
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 bond2 bond3 peerlink vni10 vni20 vni30 vniBLUE vniRED
    bridge-vids 10 20 30 4001-4002
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.3
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-sys-mac 44:38:39:BE:EF:BB
auto vlan10
iface vlan10
    address 10.1.10.5/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vlan-id 10
    vlan-raw-device bridge
    vrf RED
auto vlan20
iface vlan20
    address 10.1.20.5/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vlan-id 20
    vlan-raw-device bridge
    vrf RED
auto vlan30
iface vlan30
    address 10.1.30.5/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vlan-id 30
    vlan-raw-device bridge
    vrf BLUE
auto vlan4001
iface vlan4001
    hwaddress 44:38:39:BE:EF:BB
    vlan-id 4001
    vlan-raw-device bridge
    vrf RED
auto vlan4002
iface vlan4002
    hwaddress 44:38:39:BE:EF:BB
    vlan-id 4002
    vlan-raw-device bridge
    vrf BLUE
auto vni10
iface vni10
    bridge-access 10
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
auto vni20
iface vni20
    bridge-access 20
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20
auto vni30
iface vni30
    bridge-access 30
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 30
auto vniBLUE
iface vniBLUE
    bridge-access 4002
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4002
auto vniRED
iface vniRED
    bridge-access 4001
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4001
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.101/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.102/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.103/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.104/32
auto swp1
iface swp1
    alias to leaf
auto swp2
iface swp2
    alias to leaf
auto swp3
iface swp3
    alias to leaf
auto swp4
iface swp4
    alias to leaf
auto swp5
iface swp5
    alias to leaf
auto swp6
iface swp6
    alias to leaf
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.63/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.63
auto swp3
iface swp3
    alias bond member of bond1
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto BLUE
iface BLUE
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto bond1
iface bond1
    bond-slaves swp3
    bridge-vids 101-102
    clag-id 1
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 peerlink vniBLUE vniRED
    bridge-vids 101-102 4001-4002
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.64
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:FF
auto vlan101
iface vlan101
    address 10.1.101.64/24
    address-virtual 00:00:00:00:00:01 10.1.101.1/24
    vlan-id 101
    vlan-raw-device bridge
    vrf RED
auto vlan102
iface vlan102
    address 10.1.102.64/24
    address-virtual 00:00:00:00:00:02 10.1.102.1/24
    vlan-id 102
    vlan-raw-device bridge
    vrf BLUE
auto vlan4001
iface vlan4001
    hwaddress 44:38:39:BE:EF:FF
    vlan-id 4001
    vlan-raw-device bridge
    vrf RED
auto vlan4002
iface vlan4002
    hwaddress 44:38:39:BE:EF:FF
    vlan-id 4002
    vlan-raw-device bridge
    vrf BLUE
auto vniBLUE
iface vniBLUE
    bridge-access 4002
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4002
auto vniRED
iface vniRED
    bridge-access 4001
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4001
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.64/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.64
auto swp3
iface swp3
    alias bond member of bond1
auto swp49
iface swp49
    alias peerlink
auto swp50
iface swp50
    alias peerlink
auto swp51
iface swp51
    alias to spine
auto swp52
iface swp52
    alias to spine
auto swp53
iface swp53
    alias to spine
auto swp54
iface swp54
    alias to spine
auto BLUE
iface BLUE
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto bond1
iface bond1
    bond-slaves swp3
    bridge-vids 101-102
    clag-id 1
    mtu 9000
auto bridge
iface bridge
    bridge-ports bond1 peerlink vniBLUE vniRED
    bridge-vids 101-102 4001-4002
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 10
    clagd-backup-ip 10.10.10.63
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-sys-mac 44:38:39:BE:EF:FF
auto vlan101
iface vlan101
    address 10.1.101.65/24
    address-virtual 00:00:00:00:00:01 10.1.101.1/24
    vlan-id 101
    vlan-raw-device bridge
    vrf RED
auto vlan102
iface vlan102
    address 10.1.102.65/24
    address-virtual 00:00:00:00:00:02 10.1.102.1/24
    vlan-id 102
    vlan-raw-device bridge
    vrf BLUE
auto vlan4001
iface vlan4001
    hwaddress 44:38:39:BE:EF:FF
    vlan-id 4001
    vlan-raw-device bridge
    vrf RED
auto vlan4002
iface vlan4002
    hwaddress 44:38:39:BE:EF:FF
    vlan-id 4002
    vlan-raw-device bridge
    vrf BLUE
auto vniBLUE
iface vniBLUE
    bridge-access 4002
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4002
auto vniRED
iface vniRED
    bridge-access 4001
    bridge-arp-nd-suppress on
    bridge-learning off
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 4001
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID3535 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
vrf RED
 vni 4001
exit-vrf
vrf BLUE
 vni 4002
exit-vrf
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
router bgp 65101 vrf RED
 bgp router-id 10.10.10.1
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
router bgp 65101 vrf BLUE
 bgp router-id 10.10.10.1
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
vrf RED
 vni 4001
exit-vrf
vrf BLUE
 vni 4002
exit-vrf
router bgp 65102
 bgp router-id 10.10.10.2
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
router bgp 65102 vrf RED
 bgp router-id 10.10.10.2
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
router bgp 65101 vrf BLUE
 bgp router-id 10.10.10.2
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/frr/frr.conf
...
vrf RED
 vni 4001
exit-vrf
vrf BLUE
 vni 4002
exit-vrf
router bgp 65103
 bgp router-id 10.10.10.3
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
router bgp 65103 vrf RED
 bgp router-id 10.10.10.3
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
router bgp 65103 vrf BLUE
 bgp router-id 10.10.10.3
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/frr/frr.conf
...
vrf RED
 vni 4001
exit-vrf
vrf BLUE
 vni 4002
exit-vrf
router bgp 65104
 bgp router-id 10.10.10.4
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
router bgp 65104 vrf RED
 bgp router-id 10.10.10.4
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
router bgp 65104 vrf BLUE
 bgp router-id 10.10.10.4
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.102
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.103
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.104
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 neighbor swp5 interface peer-group underlay
 neighbor swp6 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
 exit-address-family
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf
...
vrf RED
 vni 4001
exit-vrf
vrf BLUE
 vni 4002
exit-vrf
router bgp 65253
 bgp router-id 10.10.10.63
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
router bgp 65253 vrf RED
 bgp router-id 10.10.10.63
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
router bgp 65253 vrf BLUE
 bgp router-id 10.10.10.63
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/frr/frr.conf
...
vrf RED
 vni 4001
exit-vrf
vrf BLUE
 vni 4002
exit-vrf
router bgp 65254
 bgp router-id 10.10.10.64
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface peer-group underlay
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
router bgp 65254 vrf RED
 bgp router-id 10.10.10.64
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
router bgp 65254 vrf BLUE
 bgp router-id 10.10.10.64
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### NVUE Commands

The NVUE commands create single VXLAN devices.

{{< tabs "TabID8545 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID8548 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1-3,swp49-54
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond3 bond member swp3
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf01:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf01:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond1 link mtu 9000
cumulus@leaf01:~$ nv set interface bond2 link mtu 9000
cumulus@leaf01:~$ nv set interface bond3 link mtu 9000
cumulus@leaf01:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf01:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:~$ nv set mlag priority 1000
cumulus@leaf01:~$ nv set mlag init-delay 10
cumulus@leaf01:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf01:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf01:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf01:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf01:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf01:~$ nv set vrf RED
cumulus@leaf01:~$ nv set vrf BLUE
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf01:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf01:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf01:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf01:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf01:~$ nv set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf01:~$ nv set vrf RED evpn vni 4001
cumulus@leaf01:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf01:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set evpn enable on
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf01:~$ nv set vrf RED router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set vrf RED router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf01:~$ nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn
cumulus@leaf01:~$ nv set vrf BLUE router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set vrf BLUE router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf BLUE router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf01:~$ nv set vrf BLUE router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf BLUE router bgp address-family ipv4-unicast route-export to-evpn
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp1-3,swp49-54
cumulus@leaf02:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:~$ nv set interface bond3 bond member swp3
cumulus@leaf02:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf02:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf02:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf02:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond1 link mtu 9000
cumulus@leaf02:~$ nv set interface bond2 link mtu 9000
cumulus@leaf02:~$ nv set interface bond3 link mtu 9000
cumulus@leaf02:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf02:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf02:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf02:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf02:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:~$ nv set mlag priority 2000
cumulus@leaf02:~$ nv set mlag init-delay 10
cumulus@leaf02:~$ nv set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf02:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf02:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf02:~$ nv set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf02:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf02:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf02:~$ nv set interface vlan30 ip address 10.1.30.3/24
cumulus@leaf02:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf02:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf02:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf02:~$ nv set vrf RED
cumulus@leaf02:~$ nv set vrf BLUE
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf02:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf02:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf02:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf02:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf02:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf02:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf02:~$ nv set nve vxlan source address 10.10.10.2
cumulus@leaf02:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf02:~$ nv set vrf RED evpn vni 4001
cumulus@leaf02:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf02:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set evpn enable on
cumulus@leaf02:~$ nv set router bgp autonomous-system 65102
cumulus@leaf02:~$ nv set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf02:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf02:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf02:~$ nv set vrf RED router bgp autonomous-system 65102
cumulus@leaf02:~$ nv set vrf RED router bgp router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf02:~$ nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf02:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn
cumulus@leaf02:~$ nv set vrf BLUE router bgp autonomous-system 65102
cumulus@leaf02:~$ nv set vrf BLUE router bgp router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf BLUE router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf02:~$ nv set vrf BLUE router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf02:~$ nv set vrf BLUE router bgp address-family ipv4-unicast route-export to-evpn
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ nv set interface swp1-3,swp49-54
cumulus@leaf03:~$ nv set interface bond1 bond member swp1
cumulus@leaf03:~$ nv set interface bond2 bond member swp2
cumulus@leaf03:~$ nv set interface bond3 bond member swp3
cumulus@leaf03:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf03:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf03:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf03:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond1 link mtu 9000
cumulus@leaf03:~$ nv set interface bond2 link mtu 9000
cumulus@leaf03:~$ nv set interface bond3 link mtu 9000
cumulus@leaf03:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf03:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf03:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf03:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf03:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf03:~$ nv set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf03:~$ nv set mlag backup 10.10.10.4
cumulus@leaf03:~$ nv set mlag peer-ip linklocal
cumulus@leaf03:~$ nv set mlag priority 1000
cumulus@leaf03:~$ nv set mlag init-delay 10
cumulus@leaf03:~$ nv set interface vlan10 ip address 10.1.10.4/24
cumulus@leaf03:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf03:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf03:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf03:~$ nv set interface vlan20 ip address 10.1.20.4/24
cumulus@leaf03:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf03:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf03:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf03:~$ nv set interface vlan30 ip address 10.1.30.4/24
cumulus@leaf03:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf03:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf03:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf03:~$ nv set vrf RED
cumulus@leaf03:~$ nv set vrf BLUE
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf03:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf03:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf03:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf03:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf03:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf03:~$ nv set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf03:~$ nv set nve vxlan source address 10.10.10.3
cumulus@leaf03:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf03:~$ nv set vrf RED evpn vni 4001
cumulus@leaf03:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf03:~$ nv set system global anycast-mac 44:38:39:BE:EF:BB
cumulus@leaf03:~$ nv set evpn enable on
cumulus@leaf03:~$ nv set router bgp autonomous-system 65103
cumulus@leaf03:~$ nv set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf03:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf03:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf03:~$ nv set vrf RED router bgp autonomous-system 65103
cumulus@leaf03:~$ nv set vrf RED router bgp router-id 10.10.10.3
cumulus@leaf03:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf03:~$ nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf03:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn
cumulus@leaf03:~$ nv set vrf BLUE router bgp autonomous-system 65103
cumulus@leaf03:~$ nv set vrf BLUE router bgp router-id 10.10.10.3
cumulus@leaf03:~$ nv set vrf BLUE router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf03:~$ nv set vrf BLUE router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf03:~$ nv set vrf BLUE router bgp address-family ipv4-unicast route-export to-evpn
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ nv set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ nv set interface swp1-3,swp49-54
cumulus@leaf04:~$ nv set interface bond1 bond member swp1
cumulus@leaf04:~$ nv set interface bond2 bond member swp2
cumulus@leaf04:~$ nv set interface bond3 bond member swp3
cumulus@leaf04:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf04:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf04:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf04:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond1 link mtu 9000
cumulus@leaf04:~$ nv set interface bond2 link mtu 9000
cumulus@leaf04:~$ nv set interface bond3 link mtu 9000
cumulus@leaf04:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf04:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf04:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf04:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf04:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf04:~$ nv set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf04:~$ nv set mlag backup 10.10.10.3
cumulus@leaf04:~$ nv set mlag peer-ip linklocal
cumulus@leaf04:~$ nv set mlag priority 2000
cumulus@leaf04:~$ nv set mlag init-delay 10
cumulus@leaf04:~$ nv set interface vlan10 ip address 10.1.10.5/24
cumulus@leaf04:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf04:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf04:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf04:~$ nv set interface vlan20 ip address 10.1.20.5/24
cumulus@leaf04:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf04:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf04:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf04:~$ nv set interface vlan30 ip address 10.1.30.5/24
cumulus@leaf04:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf04:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf04:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf04:~$ nv set vrf RED
cumulus@leaf04:~$ nv set vrf BLUE
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf04:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf04:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf04:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf04:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf04:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf04:~$ nv set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf04:~$ nv set nve vxlan source address 10.10.10.4
cumulus@leaf04:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf04:~$ nv set vrf RED evpn vni 4001
cumulus@leaf04:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf04:~$ nv set system global anycast-mac 44:38:39:BE:EF:BB
cumulus@leaf04:~$ nv set evpn enable on
cumulus@leaf04:~$ nv set router bgp autonomous-system 65104
cumulus@leaf04:~$ nv set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf04:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf04:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf04:~$ nv set vrf RED router bgp autonomous-system 65104
cumulus@leaf04:~$ nv set vrf RED router bgp router-id 10.10.10.4
cumulus@leaf04:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf04:~$ nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf04:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn
cumulus@leaf04:~$ nv set vrf BLUE router bgp autonomous-system 65104
cumulus@leaf04:~$ nv set vrf BLUE router bgp router-id 10.10.10.4
cumulus@leaf04:~$ nv set vrf BLUE router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf04:~$ nv set vrf BLUE router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf04:~$ nv set vrf BLUE router bgp address-family ipv4-unicast route-export to-evpn
cumulus@leaf04:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1-6
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine01:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ nv set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp1-6
cumulus@spine02:~$ nv set router bgp autonomous-system 65199
cumulus@spine02:~$ nv set router bgp router-id 10.10.10.102
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine02:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine02:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ nv set interface lo ip address 10.10.10.103/32
cumulus@spine03:~$ nv set interface swp1-6
cumulus@spine03:~$ nv set router bgp autonomous-system 65199
cumulus@spine03:~$ nv set router bgp router-id 10.10.10.103
cumulus@spine03:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine03:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine03:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine03:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine03:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine03:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ nv set interface lo ip address 10.10.10.104/32
cumulus@spine04:~$ nv set interface swp1-6
cumulus@spine04:~$ nv set router bgp autonomous-system 65199
cumulus@spine04:~$ nv set router bgp router-id 10.10.10.104
cumulus@spine04:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine04:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine04:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine04:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine04:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine04:~$ nv config apply
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ nv set interface lo ip address 10.10.10.63/32
cumulus@border01:~$ nv set interface swp3,swp49-54
cumulus@border01:~$ nv set interface bond3 bond member swp3
cumulus@border01:~$ nv set interface bond3 bond mlag id 1
cumulus@border01:~$ nv set interface bond3 bond lacp-bypass on
cumulus@border01:~$ nv set interface bond3 link mtu 9000
cumulus@border01:~$ nv set interface bond3 bridge domain br_default
cumulus@border01:~$ nv set interface bond3 bridge domain br_default vlan 101,102
cumulus@border01:~$ nv set interface peerlink bond member swp49-50
cumulus@border01:~$ nv set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border01:~$ nv set mlag backup 10.10.10.64
cumulus@border01:~$ nv set mlag peer-ip linklocal
cumulus@border01:~$ nv set mlag priority 1000
cumulus@border01:~$ nv set mlag init-delay 10
cumulus@border01:~$ nv set vrf RED
cumulus@border01:~$ nv set vrf BLUE
cumulus@border01:~$ nv set interface vlan101 ip address 10.1.101.64/24
cumulus@border01:~$ nv set interface vlan101 ip vrr address 10.1.101.1/24
cumulus@border01:~$ nv set interface vlan101 ip vrr mac-address 00:00:00:00:00:01
cumulus@border01:~$ nv set interface vlan101 ip vrr state up
cumulus@border01:~$ nv set interface vlan102 ip address 10.1.102.64/24
cumulus@border01:~$ nv set interface vlan102 ip vrr address 10.1.102.1/24
cumulus@border01:~$ nv set interface vlan102 ip vrr mac-address 00:00:00:00:00:02
cumulus@border01:~$ nv set interface vlan102 ip vrr state up
cumulus@border01:~$ nv set bridge domain br_default vlan 101,102
cumulus@border01:~$ nv set interface vlan101 ip vrf RED
cumulus@border01:~$ nv set interface vlan102 ip vrf BLUE
cumulus@border01:~$ nv set nve vxlan mlag shared-address 10.0.1.255
cumulus@border01:~$ nv set nve vxlan source address 10.10.10.63
cumulus@border01:~$ nv set nve vxlan arp-nd-suppress on
cumulus@border01:~$ nv set vrf RED evpn vni 4001
cumulus@border01:~$ nv set vrf BLUE evpn vni 4002
cumulus@border01:~$ nv set system global anycast-mac 44:38:39:BE:EF:FF
cumulus@border01:~$ nv set evpn enable on
cumulus@border01:~$ nv set router bgp autonomous-system 65253
cumulus@border01:~$ nv set router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@border01:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@border01:~$ nv set vrf RED router bgp autonomous-system 65253
cumulus@border01:~$ nv set vrf RED router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@border01:~$ nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn
cumulus@border01:~$ nv set vrf BLUE router bgp autonomous-system 65253
cumulus@border01:~$ nv set vrf BLUE router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf BLUE router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@border01:~$ nv set vrf BLUE router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ nv set vrf BLUE router bgp address-family ipv4-unicast route-export to-evpn
cumulus@border01:~$ nv config apply
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ nv set interface lo ip address 10.10.10.64/32
cumulus@border02:~$ nv set interface swp3,swp49-54
cumulus@border02:~$ nv set interface bond3 bond member swp3
cumulus@border02:~$ nv set interface bond3 bond mlag id 1
cumulus@border02:~$ nv set interface bond3 bond lacp-bypass on
cumulus@border02:~$ nv set interface bond3 link mtu 9000
cumulus@border02:~$ nv set interface bond3 bridge domain br_default
cumulus@border02:~$ nv set interface bond3 bridge domain br_default vlan 101,102
cumulus@border02:~$ nv set interface peerlink bond member swp49-50
cumulus@border02:~$ nv set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border02:~$ nv set mlag backup 10.10.10.63
cumulus@border02:~$ nv set mlag peer-ip linklocal
cumulus@border02:~$ nv set mlag priority 2000
cumulus@border02:~$ nv set mlag init-delay 10
cumulus@border02:~$ nv set vrf RED
cumulus@border02:~$ nv set vrf BLUE
cumulus@border02:~$ nv set interface vlan101 ip address 10.1.101.65/24
cumulus@border02:~$ nv set interface vlan101 ip vrr address 10.1.101.1/24
cumulus@border02:~$ nv set interface vlan101 ip vrr mac-address 00:00:00:00:00:01
cumulus@border02:~$ nv set interface vlan101 ip vrr state up
cumulus@border02:~$ nv set interface vlan102 ip address 10.1.102.65/24
cumulus@border02:~$ nv set interface vlan102 ip vrr address 10.1.102.1/24
cumulus@border02:~$ nv set interface vlan102 ip vrr mac-address 00:00:00:00:00:02
cumulus@border02:~$ nv set interface vlan102 ip vrr state up
cumulus@border02:~$ nv set bridge domain br_default vlan 101,102
cumulus@border02:~$ nv set interface vlan101 ip vrf RED
cumulus@border02:~$ nv set interface vlan102 ip vrf BLUE
cumulus@border02:~$ nv set nve vxlan mlag shared-address 10.0.1.255
cumulus@border02:~$ nv set nve vxlan source address 10.10.10.64
cumulus@border02:~$ nv set nve vxlan arp-nd-suppress on
cumulus@border02:~$ nv set vrf RED evpn vni 4001
cumulus@border02:~$ nv set vrf BLUE evpn vni 4002
cumulus@border02:~$ nv set system global anycast-mac 44:38:39:BE:EF:FF
cumulus@border02:~$ nv set evpn enable on
cumulus@border02:~$ nv set router bgp autonomous-system 65254
cumulus@border02:~$ nv set router bgp router-id 10.10.10.64
cumulus@border02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@border02:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp53 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer swp54 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border02:~$ nv set vrf default router bgp peer peerlink.4094 peer-group underlay
cumulus@border02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@border02:~$ nv set vrf RED router bgp autonomous-system 65254
cumulus@border02:~$ nv set vrf RED router bgp router-id 10.10.10.64
cumulus@border02:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@border02:~$ nv set vrf RED router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border02:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn
cumulus@border02:~$ nv set vrf BLUE router bgp autonomous-system 65254
cumulus@border02:~$ nv set vrf BLUE router bgp router-id 10.10.10.64
cumulus@border02:~$ nv set vrf BLUE router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@border02:~$ nv set vrf BLUE router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border02:~$ nv set vrf BLUE router bgp address-family ipv4-unicast route-export to-evpn
cumulus@border02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

{{< tabs "TabID9065 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 3
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 30
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        ip:
          address:
            10.1.10.2/24: {}
          vrr:
            address:
              10.1.10.1/24: {}
            mac-address: 00:00:00:00:00:10
            state:
              up: {}
          vrf: RED
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.2/24: {}
          vrr:
            address:
              10.1.20.1/24: {}
            mac-address: 00:00:00:00:00:20
            state:
              up: {}
          vrf: RED
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.2/24: {}
          vrr:
            address:
              10.1.30.1/24: {}
            mac-address: 00:00:00:00:00:30
            state:
              up: {}
          vrf: BLUE
        type: svi
        vlan: 30
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
            '30':
              vni:
                '30': {}
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.2: {}
      peer-ip: linklocal
      priority: 1000
      init-delay: 10
    vrf:
      RED:
        evpn:
          vni:
            '4001': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65101
            enable: on
            router-id: 10.10.10.1
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      BLUE:
        evpn:
          vni:
            '4002': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65101
            enable: on
            router-id: 10.10.10.1
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.12
        source:
          address: 10.10.10.1
        arp-nd-suppress: on
    system:
      global:
        anycast-mac: 44:38:39:BE:EF:AA
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65101
        router-id: 10.10.10.1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.2/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 3
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 30
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        ip:
          address:
            10.1.10.3/24: {}
          vrr:
            address:
              10.1.10.1/24: {}
            mac-address: 00:00:00:00:00:10
            state:
              up: {}
          vrf: RED
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.3/24: {}
          vrr:
            address:
              10.1.20.1/24: {}
            mac-address: 00:00:00:00:00:20
            state:
              up: {}
          vrf: RED
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.3/24: {}
          vrr:
            address:
              10.1.30.1/24: {}
            mac-address: 00:00:00:00:00:30
            state:
              up: {}
          vrf: BLUE
        type: svi
        vlan: 30
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
            '30':
              vni:
                '30': {}
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.1: {}
      peer-ip: linklocal
      priority: 2000
      init-delay: 10
    vrf:
      RED:
        evpn:
          vni:
            '4001': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65102
            enable: on
            router-id: 10.10.10.2
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      BLUE:
        evpn:
          vni:
            '4002': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65102
            enable: on
            router-id: 10.10.10.2
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.12
        source:
          address: 10.10.10.2
        arp-nd-suppress: on
    system:
      global:
        anycast-mac: 44:38:39:BE:EF:AA
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65102
        router-id: 10.10.10.2
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.3/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 3
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 30
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        ip:
          address:
            10.1.10.4/24: {}
          vrr:
            address:
              10.1.10.1/24: {}
            mac-address: 00:00:00:00:00:10
            state:
              up: {}
          vrf: RED
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.4/24: {}
          vrr:
            address:
              10.1.20.1/24: {}
            mac-address: 00:00:00:00:00:20
            state:
              up: {}
          vrf: RED
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.4/24: {}
          vrr:
            address:
              10.1.30.1/24: {}
            mac-address: 00:00:00:00:00:30
            state:
              up: {}
          vrf: BLUE
        type: svi
        vlan: 30
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
            '30':
              vni:
                '30': {}
    mlag:
      mac-address: 44:38:39:BE:EF:BB
      backup:
        10.10.10.4: {}
      peer-ip: linklocal
      priority: 1000
      init-delay: 10
    vrf:
      RED:
        evpn:
          vni:
            '4001': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65103
            enable: on
            router-id: 10.10.10.3
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      BLUE:
        evpn:
          vni:
            '4002': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65103
            enable: on
            router-id: 10.10.10.3
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.34
        source:
          address: 10.10.10.3
        arp-nd-suppress: on
    system:
      global:
        anycast-mac: 44:38:39:BE:EF:BB
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65103
        router-id: 10.10.10.3
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.4/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 10
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 20
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 3
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              access: 30
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan10:
        ip:
          address:
            10.1.10.5/24: {}
          vrr:
            address:
              10.1.10.1/24: {}
            mac-address: 00:00:00:00:00:10
            state:
              up: {}
          vrf: RED
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.5/24: {}
          vrr:
            address:
              10.1.20.1/24: {}
            mac-address: 00:00:00:00:00:20
            state:
              up: {}
          vrf: RED
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.5/24: {}
          vrr:
            address:
              10.1.30.1/24: {}
            mac-address: 00:00:00:00:00:30
            state:
              up: {}
          vrf: BLUE
        type: svi
        vlan: 30
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
            '30':
              vni:
                '30': {}
    mlag:
      mac-address: 44:38:39:BE:EF:BB
      backup:
        10.10.10.3: {}
      peer-ip: linklocal
      priority: 2000
      init-delay: 10
    vrf:
      RED:
        evpn:
          vni:
            '4001': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65104
            enable: on
            router-id: 10.10.10.4
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      BLUE:
        evpn:
          vni:
            '4002': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65104
            enable: on
            router-id: 10.10.10.4
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
    nve:
      vxlan:
        enable: on
        mlag:
          shared-address: 10.0.1.34
        source:
          address: 10.10.10.4
        arp-nd-suppress: on
    system:
      global:
        anycast-mac: 44:38:39:BE:EF:BB
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65104
        router-id: 10.10.10.4
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.101/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.101
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.102/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.102
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.103/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.103
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.104/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp4:
        type: swp
      swp5:
        type: swp
      swp6:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.104
    vrf:
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp1:
                peer-group: underlay
                type: unnumbered
              swp2:
                peer-group: underlay
                type: unnumbered
              swp3:
                peer-group: underlay
                type: unnumbered
              swp4:
                peer-group: underlay
                type: unnumbered
              swp5:
                peer-group: underlay
                type: unnumbered
              swp6:
                peer-group: underlay
                type: unnumbered
            address-family:
              l2vpn-evpn:
                enable: on
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.63/32: {}
        type: loopback
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              vlan:
                '101': {}
                '102': {}
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan101:
        ip:
          address:
            10.1.101.64/24: {}
          vrr:
            address:
              10.1.101.1/24: {}
            mac-address: 00:00:00:00:00:01
            state:
              up: {}
          vrf: RED
        type: svi
        vlan: 101
      vlan102:
        ip:
          address:
            10.1.102.64/24: {}
          vrr:
            address:
              10.1.102.1/24: {}
            mac-address: 00:00:00:00:00:02
            state:
              up: {}
          vrf: BLUE
        type: svi
        vlan: 102
    mlag:
      mac-address: 44:38:39:BE:EF:FF
      backup:
        10.10.10.64: {}
      peer-ip: linklocal
      priority: 1000
      init-delay: 10
    vrf:
      RED:
        evpn:
          vni:
            '4001': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65253
            enable: on
            router-id: 10.10.10.63
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      BLUE:
        evpn:
          vni:
            '4002': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65253
            enable: on
            router-id: 10.10.10.63
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
    bridge:
      domain:
        br_default:
          vlan:
            '101': {}
            '102': {}
    nve:
      vxlan:
        mlag:
          shared-address: 10.0.1.255
        enable: on
        source:
          address: 10.10.10.63
        arp-nd-suppress: on
    system:
      global:
        anycast-mac: 44:38:39:BE:EF:FF
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65253
        router-id: 10.10.10.63
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.64/32: {}
        type: loopback
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      swp53:
        type: swp
      swp54:
        type: swp
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
        link:
          mtu: 9000
        bridge:
          domain:
            br_default:
              vlan:
                '101': {}
                '102': {}
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        type: sub
        base-interface: peerlink
        vlan: 4094
      vlan101:
        ip:
          address:
            10.1.101.65/24: {}
          vrr:
            address:
              10.1.101.1/24: {}
            mac-address: 00:00:00:00:00:01
            state:
              up: {}
          vrf: RED
        type: svi
        vlan: 101
      vlan102:
        ip:
          address:
            10.1.102.65/24: {}
          vrr:
            address:
              10.1.102.1/24: {}
            mac-address: 00:00:00:00:00:02
            state:
              up: {}
          vrf: BLUE
        type: svi
        vlan: 102
    mlag:
      mac-address: 44:38:39:BE:EF:FF
      backup:
        10.10.10.63: {}
      peer-ip: linklocal
      priority: 2000
      init-delay: 10
    vrf:
      RED:
        evpn:
          vni:
            '4001': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65254
            enable: on
            router-id: 10.10.10.64
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      BLUE:
        evpn:
          vni:
            '4002': {}
          enable: on
        router:
          bgp:
            autonomous-system: 65254
            enable: on
            router-id: 10.10.10.64
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
                route-export:
                  to-evpn:
                    enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
      default:
        router:
          bgp:
            peer-group:
              underlay:
                remote-as: external
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            peer:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
              swp53:
                peer-group: underlay
                type: unnumbered
              swp54:
                peer-group: underlay
                type: unnumbered
              peerlink.4094:
                peer-group: underlay
                type: unnumbered
            address-family:
              ipv4-unicast:
                redistribute:
                  connected:
                    enable: on
                enable: on
    bridge:
      domain:
        br_default:
          vlan:
            '101': {}
            '102': {}
    nve:
      vxlan:
        mlag:
          shared-address: 10.0.1.255
        enable: on
        source:
          address: 10.10.10.64
        arp-nd-suppress: on
    system:
      global:
        anycast-mac: 44:38:39:BE:EF:FF
    evpn:
      enable: on
    router:
      bgp:
        enable: on
        autonomous-system: 65254
        router-id: 10.10.10.64
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID9151 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/network/interfaces 
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.1
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto BLUE
iface BLUE
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 3
    bridge-access 30
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    hwaddress 44:38:39:22:01:b1
    vrf RED
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    hwaddress 44:38:39:22:01:b1
    vrf RED
    vlan-raw-device br_default
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.2/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    hwaddress 44:38:39:22:01:b1
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30
auto vlan4024_l3
iface vlan4024_l3
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:AA
    vlan-id 4024
auto vlan4036_l3
iface vlan4036_l3
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:AA
    vlan-id 4036
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20 30=30 4024=4001 4036=4002
    bridge-vids 10 20 30 4024 4036
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink vxlan48
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.2/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.2
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto BLUE
iface BLUE
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 3
    bridge-access 30
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    address 10.1.10.3/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    hwaddress 44:38:39:22:01:af
    vrf RED
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.3/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    hwaddress 44:38:39:22:01:af
    vrf RED
    vlan-raw-device br_default
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.3/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    hwaddress 44:38:39:22:01:af
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30
auto vlan4024_l3
iface vlan4024_l3
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:AA
    vlan-id 4024
auto vlan4036_l3
iface vlan4036_l3
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:AA
    vlan-id 4036
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20 30=30 4024=4001 4036=4002
    bridge-vids 10 20 30 4024 4036
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink vxlan48
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.3/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.3
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto BLUE
iface BLUE
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 3
    bridge-access 30
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-backup-ip 10.10.10.4
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    address 10.1.10.4/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    hwaddress 44:38:39:22:01:bb
    vrf RED
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.4/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    hwaddress 44:38:39:22:01:bb
    vrf RED
    vlan-raw-device br_default
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.4/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    hwaddress 44:38:39:22:01:bb
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30
auto vlan4024_l3
iface vlan4024_l3
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:BB
    vlan-id 4024
auto vlan4036_l3
iface vlan4036_l3
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:BB
    vlan-id 4036
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20 30=30 4024=4001 4036=4002
    bridge-vids 10 20 30 4024 4036
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink vxlan48
    hwaddress 44:38:39:22:01:bb
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:mgmt:~$ sudo cat /etc/network/interfaces 
...
auto lo
iface lo inet loopback
    address 10.10.10.4/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.4
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto BLUE
iface BLUE
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 3
    bridge-access 30
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-backup-ip 10.10.10.3
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10
auto vlan10
iface vlan10
    address 10.1.10.5/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    hwaddress 44:38:39:22:01:c1
    vrf RED
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.5/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    hwaddress 44:38:39:22:01:c1
    vrf RED
    vlan-raw-device br_default
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.5/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    hwaddress 44:38:39:22:01:c1
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30
auto vlan4024_l3
iface vlan4024_l3
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:BB
    vlan-id 4024
auto vlan4036_l3
iface vlan4036_l3
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:BB
    vlan-id 4036
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20 30=30 4024=4001 4036=4002
    bridge-vids 10 20 30 4024 4036
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink vxlan48
    hwaddress 44:38:39:22:01:c1
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.101/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.102/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:mgmt:~$ sudo cat /etc/network/interfaces 
...
auto lo
iface lo inet loopback
    address 10.10.10.103/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.104/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
auto swp5
iface swp5
auto swp6
iface swp6
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.63/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.63
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto BLUE
iface BLUE
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-vids 101 102
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-backup-ip 10.10.10.64
    clagd-sys-mac 44:38:39:BE:EF:FF
    clagd-args --initDelay 10
auto vlan101
iface vlan101
    address 10.1.101.64/24
    address-virtual 00:00:00:00:00:01 10.1.101.1/24
    hwaddress 44:38:39:22:01:ab
    vrf RED
    vlan-raw-device br_default
    vlan-id 101
auto vlan102
iface vlan102
    address 10.1.102.64/24
    address-virtual 00:00:00:00:00:02 10.1.102.1/24
    hwaddress 44:38:39:22:01:ab
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 102
auto vlan4024_l3
iface vlan4024_l3
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:FF
    vlan-id 4024
auto vlan4036_l3
iface vlan4036_l3
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:FF
    vlan-id 4036
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 4024=4001 4036=4002
    bridge-vids 4024 4036
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond3 peerlink vxlan48
    hwaddress 44:38:39:22:01:ab
    bridge-vlan-aware yes
    bridge-vids 101 102
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.64/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.64
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto BLUE
iface BLUE
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto swp53
iface swp53
auto swp54
iface swp54
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-vids 101 102
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-priority 2000
    clagd-backup-ip 10.10.10.63
    clagd-sys-mac 44:38:39:BE:EF:FF
    clagd-args --initDelay 10
auto vlan101
iface vlan101
    address 10.1.101.65/24
    address-virtual 00:00:00:00:00:01 10.1.101.1/24
    hwaddress 44:38:39:22:01:b3
    vrf RED
    vlan-raw-device br_default
    vlan-id 101
auto vlan102
iface vlan102
    address 10.1.102.65/24
    address-virtual 00:00:00:00:00:02 10.1.102.1/24
    hwaddress 44:38:39:22:01:b3
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 102
auto vlan4024_l3
iface vlan4024_l3
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:FF
    vlan-id 4024
auto vlan4036_l3
iface vlan4036_l3
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:FF
    vlan-id 4036
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 4024=4001 4036=4002
    bridge-vids 4024 4036
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond3 peerlink vxlan48
    hwaddress 44:38:39:22:01:b3
    bridge-vlan-aware yes
    bridge-vids 101 102
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID9237 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/frr/frr.conf 
...
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65101 vrf default
bgp router-id 10.10.10.1
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
! end of router bgp 65101 vrf default
router bgp 65101 vrf RED
bgp router-id 10.10.10.1
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65101 vrf RED
router bgp 65101 vrf BLUE
bgp router-id 10.10.10.1
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65101 vrf BLUE
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/frr/frr.conf
...
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65102 vrf default
bgp router-id 10.10.10.2
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
! end of router bgp 65102 vrf default
router bgp 65102 vrf RED
bgp router-id 10.10.10.2
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65102 vrf RED
router bgp 65102 vrf BLUE
bgp router-id 10.10.10.2
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65102 vrf BLUE
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ sudo cat /etc/frr/frr.conf
...
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65103 vrf default
bgp router-id 10.10.10.3
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
! end of router bgp 65103 vrf default
router bgp 65103 vrf RED
bgp router-id 10.10.10.3
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65103 vrf RED
router bgp 65103 vrf BLUE
bgp router-id 10.10.10.3
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65103 vrf BLUE
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:mgmt:~$ sudo cat /etc/frr/frr.conf 
...
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65104 vrf default
bgp router-id 10.10.10.4
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
! end of router bgp 65104 vrf default
router bgp 65104 vrf RED
bgp router-id 10.10.10.4
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65104 vrf RED
router bgp 65104 vrf BLUE
bgp router-id 10.10.10.4
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65104 vrf BLUE
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.101
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:mgmt:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.102
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:mgmt:~$ sudo cat /etc/frr/frr.conf 
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.103
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:mgmt:~$ sudo cat /etc/frr/frr.conf
...
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.104
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp1 interface remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 interface peer-group underlay
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 interface peer-group underlay
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 interface peer-group underlay
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
neighbor swp5 interface remote-as external
neighbor swp5 interface peer-group underlay
neighbor swp5 timers 3 9
neighbor swp5 timers connect 10
neighbor swp5 advertisement-interval 0
neighbor swp5 capability extended-nexthop
neighbor swp6 interface remote-as external
neighbor swp6 interface peer-group underlay
neighbor swp6 timers 3 9
neighbor swp6 timers connect 10
neighbor swp6 advertisement-interval 0
neighbor swp6 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
neighbor swp5 activate
neighbor swp6 activate
neighbor underlay activate
exit-address-family
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:mgmt:~$ sudo cat /etc/frr/frr.conf
...
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65253 vrf default
bgp router-id 10.10.10.63
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
! end of router bgp 65253 vrf default
router bgp 65253 vrf RED
bgp router-id 10.10.10.63
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65253 vrf RED
router bgp 65253 vrf BLUE
bgp router-id 10.10.10.63
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65253 vrf BLUE
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:mgmt:~$ sudo cat /etc/frr/frr.conf
...
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65254 vrf default
bgp router-id 10.10.10.64
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor peerlink.4094 interface remote-as external
neighbor peerlink.4094 interface peer-group underlay
neighbor peerlink.4094 timers 3 9
neighbor peerlink.4094 timers connect 10
neighbor peerlink.4094 advertisement-interval 0
neighbor peerlink.4094 capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
neighbor swp53 interface remote-as external
neighbor swp53 interface peer-group underlay
neighbor swp53 timers 3 9
neighbor swp53 timers connect 10
neighbor swp53 advertisement-interval 0
neighbor swp53 capability extended-nexthop
neighbor swp54 interface remote-as external
neighbor swp54 interface peer-group underlay
neighbor swp54 timers 3 9
neighbor swp54 timers connect 10
neighbor swp54 advertisement-interval 0
neighbor swp54 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor peerlink.4094 activate
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor swp53 activate
neighbor swp54 activate
neighbor underlay activate
exit-address-family
! end of router bgp 65254 vrf default
router bgp 65132 vrf RED
bgp router-id 10.10.10.64
timers bgp 3 9
bgp deterministic-med
! Neighbors
! Address families
address-family l2vpn evpn
exit-address-family
! end of router bgp 65254 vrf RED
router bgp 65254 vrf BLUE
bgp router-id 10.10.10.64
timers bgp 3 9
bgp deterministic-med
! Neighbors
! Address families
address-family l2vpn evpn
exit-address-family
! end of router bgp 65254 vrf default
router bgp 65254 vrf RED
bgp router-id 10.10.10.64
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65254 vrf RED
router bgp 65254 vrf BLUE
bgp router-id 10.10.10.64
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65254 vrf BLUE
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}
