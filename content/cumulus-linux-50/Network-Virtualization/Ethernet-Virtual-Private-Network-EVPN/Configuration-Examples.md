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

<!-- You can see these configurations in action and explore further by selecting one of the demos in {{<exlink url="https://cumulusnetworks.com/products/cumulus-in-the-cloud/" text="Cumulus in the Cloud">}} (a free, personal, virtual data center network that provides a low-effort way to see Cumulus Linux in action). -->

## Layer 2 EVPN with External Routing

The following example configures a network infrastructure that creates a layer 2 extension between racks. Inter-VXLAN routed traffic routes between VXLANs on an external device.

- MLAG is configured between leaf01 and leaf02, and leaf03 and leaf04
- BGP unnumbered is in the underlay (configured on all leafs and spines)
- Server gateways are outside the VXLAN fabric

The following images shows traffic flow between tenants. The spines and other devices are omitted for simplicity.

|   Traffic Flow between server01 and server04  |     |
| --- | --- |
| <img width=1000/> {{< img src="/images/cumulus-linux/evpn-layer2-diagram.png" >}} | server01 and server04 are in the same VLAN but are located across different leafs.<br><ol><li>server01 makes a LACP hash decision and forwards traffic to leaf01.</li><li>leaf01 does a layer 2 lookup, has the MAC address for server04, and forwards the packet out VNI10, towards leaf04.</li><li>The VXLAN encapsulated frame arrives on leaf04, which does a layer 2 lookup and has the MAC address for server04 in VLAN10.</li></ul>|

### CUE Commands

{{< tabs "TabID35 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ cl set interface swp1-2,swp49-54
cumulus@leaf01:~$ cl set interface bond1 bond member swp1
cumulus@leaf01:~$ cl set interface bond2 bond member swp2
cumulus@leaf01:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf01:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf01:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ cl set interface bond1 link mtu 9000
cumulus@leaf01:~$ cl set interface bond2 link mtu 9000
cumulus@leaf01:~$ cl set interface bond1-2 bridge domain br_default
cumulus@leaf01:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10,20
cumulus@leaf01:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf01:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ cl set mlag backup 10.10.10.2
cumulus@leaf01:~$ cl set mlag peer-ip linklocal
cumulus@leaf01:~$ cl set mlag priority 1000
cumulus@leaf01:~$ cl set mlag init-delay 10
cumulus@leaf01:~$ cl set interface vlan10
cumulus@leaf01:~$ cl set interface vlan20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ cl set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf01:~$ cl set evpn enable on
cumulus@leaf01:~$ cl set router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf01:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cl set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ cl set interface swp1-2,swp49-54
cumulus@leaf02:~$ cl set interface bond1 bond member swp1
cumulus@leaf02:~$ cl set interface bond2 bond member swp2
cumulus@leaf02:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf02:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf02:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf02:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf02:~$ cl set interface bond1 link mtu 9000
cumulus@leaf02:~$ cl set interface bond2 link mtu 9000
cumulus@leaf02:~$ cl set interface bond1-2 bridge domain br_default
cumulus@leaf02:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf02:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10,20
cumulus@leaf02:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf02:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ cl set mlag backup 10.10.10.1
cumulus@leaf02:~$ cl set mlag peer-ip linklocal
cumulus@leaf02:~$ cl set mlag priority 32768
cumulus@leaf02:~$ cl set mlag init-delay 10
cumulus@leaf02:~$ cl set interface vlan10
cumulus@leaf02:~$ cl set interface vlan20
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf02:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf02:~$ cl set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf02:~$ cl set nve vxlan source address 10.10.10.2
cumulus@leaf02:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf02:~$ cl set evpn enable on
cumulus@leaf02:~$ cl set router bgp autonomous-system 65102
cumulus@leaf02:~$ cl set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf02:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf02:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf02:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf02:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf02:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cl set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ cl set interface swp1-2,swp49-54
cumulus@leaf03:~$ cl set interface bond1 bond member swp1
cumulus@leaf03:~$ cl set interface bond2 bond member swp2
cumulus@leaf03:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf03:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf03:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf03:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf03:~$ cl set interface bond1 link mtu 9000
cumulus@leaf03:~$ cl set interface bond2 link mtu 9000
cumulus@leaf03:~$ cl set interface bond1-2 bridge domain br_default
cumulus@leaf03:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf03:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10,20
cumulus@leaf03:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf03:~$ cl set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf03:~$ cl set mlag backup 10.10.10.3
cumulus@leaf03:~$ cl set mlag peer-ip linklocal
cumulus@leaf03:~$ cl set mlag priority 1000
cumulus@leaf03:~$ cl set mlag init-delay 10
cumulus@leaf03:~$ cl set interface vlan10
cumulus@leaf03:~$ cl set interface vlan20
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf03:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf03:~$ cl set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf03:~$ cl set nve vxlan source address 10.10.10.3
cumulus@leaf03:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf03:~$ cl set evpn enable on
cumulus@leaf03:~$ cl set router bgp autonomous-system 65103
cumulus@leaf03:~$ cl set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf03:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf03:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf03:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf03:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf03:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cl set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ cl set interface swp1-2,swp49-54
cumulus@leaf04:~$ cl set interface bond1 bond member swp1
cumulus@leaf04:~$ cl set interface bond2 bond member swp2
cumulus@leaf04:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf04:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf04:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf04:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf04:~$ cl set interface bond1 link mtu 9000
cumulus@leaf04:~$ cl set interface bond2 link mtu 9000
cumulus@leaf04:~$ cl set interface bond1-2 bridge domain br_default
cumulus@leaf04:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf04:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10,20
cumulus@leaf04:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf04:~$ cl set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf04:~$ cl set mlag backup 10.10.10.3
cumulus@leaf04:~$ cl set mlag peer-ip linklocal
cumulus@leaf04:~$ cl set mlag priority 32768
cumulus@leaf04:~$ cl set mlag init-delay 10
cumulus@leaf04:~$ cl set interface vlan10
cumulus@leaf04:~$ cl set interface vlan20
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf04:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf04:~$ cl set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf04:~$ cl set nve vxlan source address 10.10.10.4
cumulus@leaf04:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf04:~$ cl set evpn enable on
cumulus@leaf04:~$ cl set router bgp autonomous-system 65104
cumulus@leaf04:~$ cl set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf04:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf04:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf04:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf04:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf04:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cl set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ cl set interface swp1-6
cumulus@spine01:~$ cl set router bgp autonomous-system 65199
cumulus@spine01:~$ cl set router bgp router-id 10.10.10.101
cumulus@spine01:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine01:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine01:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine01:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine01:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine01:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cl set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ cl set interface swp1-6
cumulus@spine02:~$ cl set router bgp autonomous-system 65199
cumulus@spine02:~$ cl set router bgp router-id 10.10.10.102
cumulus@spine02:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine02:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine02:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine02:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine02:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine02:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ cl set interface lo ip address 10.10.10.103/32
cumulus@spine03:~$ cl set interface swp1-6
cumulus@spine03:~$ cl set router bgp autonomous-system 65199
cumulus@spine03:~$ cl set router bgp router-id 10.10.10.103
cumulus@spine03:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine03:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine03:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine03:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine03:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine03:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ cl set interface lo ip address 10.10.10.104/32
cumulus@spine04:~$ cl set interface swp1-6
cumulus@spine04:~$ cl set router bgp autonomous-system 65199
cumulus@spine04:~$ cl set router bgp router-id 10.10.10.104
cumulus@spine04:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine04:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine04:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine04:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine04:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine04:~$ cl config apply
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ cl set interface lo ip address 10.10.10.63/32
cumulus@border01:~$ cl set interface swp3,swp49-54
cumulus@border01:~$ cl set interface bond3 bond member swp3
cumulus@border01:~$ cl set interface bond3 bond mlag id 1
cumulus@border01:~$ cl set interface bond3 bond lacp-bypass on
cumulus@border01:~$ cl set interface bond3 link mtu 9000
cumulus@border01:~$ cl set interface bond3 bridge domain br_default
cumulus@border01:~$ cl set interface peerlink bond member swp49-50
cumulus@border01:~$ cl set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border01:~$ cl set mlag backup 10.10.10.64
cumulus@border01:~$ cl set mlag peer-ip linklocal
cumulus@border01:~$ cl set mlag priority 1000
cumulus@border01:~$ cl set mlag init-delay 10
cumulus@border01:~$ cl set interface vlan10
cumulus@border01:~$ cl set interface vlan20
cumulus@border01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@border01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@border01:~$ cl set interface bond3 bridge domain br_default vlan 10,20
cumulus@border01:~$ cl set nve vxlan mlag shared-address 10.0.1.255
cumulus@border01:~$ cl set nve vxlan source address 10.10.10.63
cumulus@border01:~$ cl set nve vxlan arp-nd-suppress on
cumulus@border01:~$ cl set evpn enable on
cumulus@border01:~$ cl set router bgp autonomous-system 65253
cumulus@border01:~$ cl set router bgp router-id 10.10.10.63
cumulus@border01:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@border01:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@border01:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@border01:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@border01:~$ cl config apply
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ cl set interface lo ip address 10.10.10.64/32
cumulus@border02:~$ cl set interface swp3,swp49-54
cumulus@border02:~$ cl set interface bond3 bond member swp3
cumulus@border02:~$ cl set interface bond3 bond mlag id 1
cumulus@border02:~$ cl set interface bond3 bond lacp-bypass on
cumulus@border02:~$ cl set interface bond3 link mtu 9000
cumulus@border02:~$ cl set interface bond3 bridge domain br_default
cumulus@border02:~$ cl set interface peerlink bond member swp49-50
cumulus@border02:~$ cl set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border02:~$ cl set mlag backup 10.10.10.63
cumulus@border02:~$ cl set mlag peer-ip linklocal
cumulus@border02:~$ cl set mlag priority 32768
cumulus@border02:~$ cl set mlag init-delay 10
cumulus@border02:~$ cl set interface vlan10
cumulus@border02:~$ cl set interface vlan20
cumulus@border02:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@border02:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@border02:~$ cl set interface bond3 bridge domain br_default vlan 10,20
cumulus@border02:~$ cl set nve vxlan mlag shared-address 10.0.1.255
cumulus@border02:~$ cl set nve vxlan source address 10.10.10.64
cumulus@border02:~$ cl set nve vxlan arp-nd-suppress on
cumulus@border02:~$ cl set evpn enable on
cumulus@border02:~$ cl set router bgp autonomous-system 65254
cumulus@border02:~$ cl set router bgp router-id 10.10.10.64
cumulus@border02:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@border02:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@border02:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border02:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@border02:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@border02:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

### /etc/network/interfaces

{{< tabs "TabID24 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/network/interfaces

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
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/network/interfaces

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
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 10

auto vlan10
iface vlan10
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.3/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.3

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

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
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1  
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.4/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.4

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

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
    clagd-backup-ip 10.10.10.3
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10

auto vlan10
iface vlan10
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.101/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

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
cumulus@spine02:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.102/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

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
cumulus@spine03:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.103/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

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
cumulus@spine04:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.104/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

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
cumulus@border01:~$ cat /etc/network/interfaces

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
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond3 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.64/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.64

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

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
    clagd-backup-ip 10.10.10.63
    clagd-sys-mac 44:38:39:BE:EF:FF
    clagd-args --initDelay 10

auto vlan10
iface vlan10
    vlan-raw-device bridge
    vlan-id 10

auto vlan20
iface vlan20
    vlan-raw-device bridge
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    vxlan-id 10
    bridge-learning off

auto vni20
iface vni20
    bridge-access 20
    vxlan-id 20
    bridge-learning off

auto br_default
iface br_default
    bridge-ports peerlink bond3 vni10 vni20
    bridge-vids 10 20  
    bridge-vlan-aware yes
```

{{< /tab >}}
{{< /tabs >}}

### /etc/frr/frr.conf

{{< tabs "TabID240 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.1
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf
...
router bgp 65102
 bgp router-id 10.10.10.2
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf
...
router bgp 65103
 bgp router-id 10.10.10.3
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf
...
router bgp 65104
 bgp router-id 10.10.10.4
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 bgp bestpath as-path multipath-relax
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
cumulus@spine02:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.102
 bgp bestpath as-path multipath-relax
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
cumulus@spine03:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.103
 bgp bestpath as-path multipath-relax
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
cumulus@spine04:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.104
 bgp bestpath as-path multipath-relax
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
cumulus@border01:~$ cat /etc/frr/frr.conf
...
router bgp 65253
 bgp router-id 10.10.10.63
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ cat /etc/frr/frr.conf
...
router bgp 65254
 bgp router-id 10.10.10.64
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
```

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

### CUE Commands

{{< tabs "TabID1652 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ cl set interface swp1-2,swp49-54
cumulus@leaf01:~$ cl set interface bond1 bond member swp1
cumulus@leaf01:~$ cl set interface bond2 bond member swp2
cumulus@leaf01:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf01:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf01:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ cl set interface bond1 link mtu 9000
cumulus@leaf01:~$ cl set interface bond2 link mtu 9000
cumulus@leaf01:~$ cl set interface bond1-2 bridge domain br_default
cumulus@leaf01:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10,20
cumulus@leaf01:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf01:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ cl set mlag backup 10.10.10.2
cumulus@leaf01:~$ cl set mlag peer-ip linklocal
cumulus@leaf01:~$ cl set mlag priority 1000
cumulus@leaf01:~$ cl set mlag init-delay 10
cumulus@leaf01:~$ cl set interface vlan10
cumulus@leaf01:~$ cl set interface vlan20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ cl set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf01:~$ cl set evpn enable on
cumulus@leaf01:~$ cl set router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf01:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cl set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ cl set interface swp1-2,swp49-54
cumulus@leaf02:~$ cl set interface bond1 bond member swp1
cumulus@leaf02:~$ cl set interface bond2 bond member swp2
cumulus@leaf02:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf02:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf02:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf02:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf02:~$ cl set interface bond1 link mtu 9000
cumulus@leaf02:~$ cl set interface bond2 link mtu 9000
cumulus@leaf02:~$ cl set interface bond1-2 bridge domain br_default
cumulus@leaf02:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf02:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf02:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf02:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ cl set mlag backup 10.10.10.1
cumulus@leaf02:~$ cl set mlag peer-ip linklocal
cumulus@leaf02:~$ cl set mlag priority 32768
cumulus@leaf02:~$ cl set mlag init-delay 10
cumulus@leaf02:~$ cl set interface vlan10
cumulus@leaf02:~$ cl set interface vlan20
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf02:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf02:~$ cl set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf02:~$ cl set nve vxlan source address 10.10.10.2
cumulus@leaf02:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf02:~$ cl set evpn enable on
cumulus@leaf02:~$ cl set router bgp autonomous-system 65102
cumulus@leaf02:~$ cl set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf02:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf02:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf02:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf02:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf02:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cl set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ cl set interface swp1-2,swp49-54
cumulus@leaf03:~$ cl set interface bond1 bond member swp1
cumulus@leaf03:~$ cl set interface bond2 bond member swp2
cumulus@leaf03:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf03:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf03:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf03:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf03:~$ cl set interface bond1 link mtu 9000
cumulus@leaf03:~$ cl set interface bond2 link mtu 9000
cumulus@leaf03:~$ cl set interface bond1-2 bridge domain br_default
cumulus@leaf03:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf03:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10,20
cumulus@leaf03:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf03:~$ cl set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf03:~$ cl set mlag backup 10.10.10.3
cumulus@leaf03:~$ cl set mlag peer-ip linklocal
cumulus@leaf03:~$ cl set mlag priority 1000
cumulus@leaf03:~$ cl set mlag init-delay 10
cumulus@leaf03:~$ cl set interface vlan10
cumulus@leaf03:~$ cl set interface vlan20
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf03:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf03:~$ cl set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf03:~$ cl set nve vxlan source address 10.10.10.3
cumulus@leaf03:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf03:~$ cl set evpn enable on
cumulus@leaf03:~$ cl set router bgp autonomous-system 65103
cumulus@leaf03:~$ cl set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf03:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf03:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf03:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf03:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf03:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cl set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ cl set interface swp1-2,swp49-54
cumulus@leaf04:~$ cl set interface bond1 bond member swp1
cumulus@leaf04:~$ cl set interface bond2 bond member swp2
cumulus@leaf04:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf04:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf04:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf04:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf04:~$ cl set interface bond1 link mtu 9000
cumulus@leaf04:~$ cl set interface bond2 link mtu 9000
cumulus@leaf04:~$ cl set interface bond1-2 bridge domain br_default
cumulus@leaf04:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf04:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10,20
cumulus@leaf04:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf04:~$ cl set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf04:~$ cl set mlag backup 10.10.10.3
cumulus@leaf04:~$ cl set mlag peer-ip linklocal
cumulus@leaf04:~$ cl set mlag priority 32768
cumulus@leaf04:~$ cl set mlag init-delay 10
cumulus@leaf04:~$ cl set interface vlan10
cumulus@leaf04:~$ cl set interface vlan20
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf04:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf04:~$ cl set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf04:~$ cl set nve vxlan source address 10.10.10.4
cumulus@leaf04:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf04:~$ cl set evpn enable on
cumulus@leaf04:~$ cl set router bgp autonomous-system 65104
cumulus@leaf04:~$ cl set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf04:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf04:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf04:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf04:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf04:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cl set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ cl set interface swp1-6
cumulus@spine01:~$ cl set router bgp autonomous-system 65199
cumulus@spine01:~$ cl set router bgp router-id 10.10.10.101
cumulus@spine01:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine01:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine01:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine01:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine01:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine01:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cl set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ cl set interface swp1-6
cumulus@spine02:~$ cl set router bgp autonomous-system 65199
cumulus@spine02:~$ cl set router bgp router-id 10.10.10.102
cumulus@spine02:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine02:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine02:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine02:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine02:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine02:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ cl set interface lo ip address 10.10.10.103/32
cumulus@spine03:~$ cl set interface swp1-6
cumulus@spine03:~$ cl set router bgp autonomous-system 65199
cumulus@spine03:~$ cl set router bgp router-id 10.10.10.103
cumulus@spine03:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine03:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine03:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine03:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine03:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine03:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ cl set interface lo ip address 10.10.10.104/32
cumulus@spine04:~$ cl set interface swp1-6
cumulus@spine04:~$ cl set router bgp autonomous-system 65199
cumulus@spine04:~$ cl set router bgp router-id 10.10.10.104
cumulus@spine04:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine04:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine04:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine04:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine04:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine04:~$ cl config apply
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ cl set interface lo ip address 10.10.10.63/32
cumulus@border01:~$ cl set interface swp1-3,swp49-54
cumulus@border01:~$ cl set interface bond3 bond member swp3
cumulus@border01:~$ cl set interface bond3 bond mlag id 1
cumulus@border01:~$ cl set interface bond3 bond lacp-bypass on
cumulus@border01:~$ cl set interface bond3 link mtu 9000
cumulus@border01:~$ cl set interface bond3 bridge domain br_default
cumulus@border01:~$ cl set interface peerlink bond member swp49-50
cumulus@border01:~$ cl set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border01:~$ cl set mlag backup 10.10.10.64
cumulus@border01:~$ cl set mlag peer-ip linklocal
cumulus@border01:~$ cl set mlag priority 1000
cumulus@border01:~$ cl set mlag init-delay 10
cumulus@border01:~$ cl set interface vlan10 ip address 10.1.10.2/24
cumulus@border01:~$ cl set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@border01:~$ cl set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@border01:~$ cl set interface vlan10 ip vrr state up
cumulus@border01:~$ cl set interface vlan20 ip address 10.1.10.2/24
cumulus@border01:~$ cl set interface vlan20 ip vrr address 10.1.20.2/24
cumulus@border01:~$ cl set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@border01:~$ cl set interface vlan20 ip vrr state up
cumulus@border01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@border01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@border01:~$ cl set interface bond3 bridge domain br_default vlan 10,20
cumulus@border01:~$ cl set nve vxlan mlag shared-address 10.0.1.255
cumulus@border01:~$ cl set nve vxlan source address 10.10.10.63
cumulus@border01:~$ cl set nve vxlan arp-nd-suppress on
cumulus@border01:~$ cl set evpn enable on
cumulus@border01:~$ cl set router bgp autonomous-system 65253
cumulus@border01:~$ cl set router bgp router-id 10.10.10.63
cumulus@border01:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@border01:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@border01:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@border01:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@border01:~$ cl set evpn route-advertise default-gateway on
cumulus@border01:~$ cl config apply
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ cl set interface lo ip address 10.10.10.64/32
cumulus@border02:~$ cl set interface swp1-3,swp49-54
cumulus@border02:~$ cl set interface bond3 bond member swp3
cumulus@border02:~$ cl set interface bond3 bond mlag id 1
cumulus@border02:~$ cl set interface bond3 bond lacp-bypass on
cumulus@border02:~$ cl set interface bond3 link mtu 9000
cumulus@border02:~$ cl set interface bond3 bridge domain br_default
cumulus@border02:~$ cl set interface peerlink bond member swp49-50
cumulus@border02:~$ cl set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border02:~$ cl set mlag backup 10.10.10.63
cumulus@border02:~$ cl set mlag peer-ip linklocal
cumulus@border02:~$ cl set mlag priority 32768
cumulus@border02:~$ cl set mlag init-delay 10
cumulus@border02:~$ cl set interface vlan10 ip address 10.1.10.1/24
cumulus@border02:~$ cl set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@border02:~$ cl set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@border02:~$ cl set interface vlan10 ip vrr state up
cumulus@border02:~$ cl set interface vlan20 ip address 10.1.20.1/24
cumulus@border02:~$ cl set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@border02:~$ cl set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@border02:~$ cl set interface vlan20 ip vrr state up
cumulus@border02:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@border02:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@border02:~$ cl set interface bond3 bridge domain br_default vlan 10,20
cumulus@border02:~$ cl set nve vxlan mlag shared-address 10.0.1.255
cumulus@border02:~$ cl set nve vxlan source address 10.10.10.64
cumulus@border02:~$ cl set nve vxlan arp-nd-suppress on
cumulus@border02:~$ cl set evpn enable on
cumulus@border02:~$ cl set router bgp autonomous-system 65254
cumulus@border02:~$ cl set router bgp router-id 10.10.10.64
cumulus@border02:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@border02:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@border02:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border02:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@border02:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@border02:~$ cl set evpn route-advertise default-gateway on
cumulus@border02:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

### /etc/network/interfaces

{{< tabs "TabID894 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/network/interfaces

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
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/network/interfaces

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
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 10

auto vlan10
iface vlan10
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/network/interfaces

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
    clagd-backup-ip 10.10.10.3
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10

auto vlan10
iface vlan10
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/network/interfaces

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
    clagd-backup-ip 10.10.10.3
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10

auto vlan10
iface vlan10
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.101/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
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
cumulus@spine02:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.102/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
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
cumulus@spine03:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.103/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
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
cumulus@spine04:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.104/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
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
cumulus@border01:~$ cat /etc/network/interfaces

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
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.10.2/24
    address-virtual 00:00:00:00:00:20 10.1.20.2/24
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond3 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ cat /etc/network/interfaces

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
    clagd-backup-ip 10.10.10.63
    clagd-sys-mac 44:38:39:BE:EF:FF
    clagd-args --initDelay 10

auto vlan10
iface vlan10
    address 10.1.10.1/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.1/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vlan-raw-device br_default
    vlan-id 20

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond3 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

### /etc/frr/frr.conf

{{< tabs "TabID1566 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf
...
log syslog informational
!
router bgp 65101
 bgp router-id 10.10.10.1
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
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
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf
...
router bgp 65102
 bgp router-id 10.10.10.2
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
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
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf
...
router bgp 65103
 bgp router-id 10.10.10.3
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
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
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf
...
router bgp 65104
 bgp router-id 10.10.10.4
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
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
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 bgp bestpath as-path multipath-relax
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
cumulus@spine02:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.102
 bgp bestpath as-path multipath-relax
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
cumulus@spine03:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.103
 bgp bestpath as-path multipath-relax
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
cumulus@spine04:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.104
 bgp bestpath as-path multipath-relax
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
cumulus@border01:~$ cat /etc/frr/frr.conf
...
router bgp 65253
 bgp router-id 10.10.10.63
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
  advertise-default-gw
 exit-address-family
!
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ cat /etc/frr/frr.conf
...
router bgp 65254
 bgp router-id 10.10.10.64
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
  advertise-default-gw
 exit-address-family
!
```

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

### CUE Commands

{{< tabs "TabID2588 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ cl set interface swp1-3,swp49-54
cumulus@leaf01:~$ cl set interface bond1 bond member swp1
cumulus@leaf01:~$ cl set interface bond2 bond member swp2
cumulus@leaf01:~$ cl set interface bond3 bond member swp3
cumulus@leaf01:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf01:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf01:~$ cl set interface bond3 bond mlag id 3
cumulus@leaf01:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ cl set interface bond3 bond lacp-bypass on
cumulus@leaf01:~$ cl set interface bond1 link mtu 9000
cumulus@leaf01:~$ cl set interface bond2 link mtu 9000
cumulus@leaf01:~$ cl set interface bond3 link mtu 9000
cumulus@leaf01:~$ cl set interface bond1-3 bridge domain br_default
cumulus@leaf01:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ cl set interface bond3 bridge domain br_default access 30
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf01:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ cl set mlag backup 10.10.10.2
cumulus@leaf01:~$ cl set mlag peer-ip linklocal
cumulus@leaf01:~$ cl set mlag priority 1000
cumulus@leaf01:~$ cl set mlag init-delay 10
cumulus@leaf01:~$ cl set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:~$ cl set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf01:~$ cl set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf01:~$ cl set interface vlan10 ip vrr state up
cumulus@leaf01:~$ cl set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:~$ cl set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf01:~$ cl set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf01:~$ cl set interface vlan20 ip vrr state up
cumulus@leaf01:~$ cl set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:~$ cl set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf01:~$ cl set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf01:~$ cl set interface vlan30 ip vrr state up
cumulus@leaf01:~$ cl set vrf RED
cumulus@leaf01:~$ cl set vrf BLUE
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 30 vni 30
cumulus@leaf01:~$ cl set interface vlan10 ip vrf RED
cumulus@leaf01:~$ cl set interface vlan20 ip vrf RED
cumulus@leaf01:~$ cl set interface vlan30 ip vrf BLUE
cumulus@leaf01:~$ cl set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf01:~$ cl set vrf RED evpn vni 4001
cumulus@leaf01:~$ cl set vrf BLUE evpn vni 4002
cumulus@leaf01:~$ cl set bridge domain br_default vlan 4001,4002
cumulus@leaf01:~$ cl set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ cl set evpn enable on
cumulus@leaf01:~$ cl set router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf01:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cl set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ cl set interface swp1-3,swp49-54
cumulus@leaf02:~$ cl set interface bond1 bond member swp1
cumulus@leaf02:~$ cl set interface bond2 bond member swp2
cumulus@leaf02:~$ cl set interface bond3 bond member swp3
cumulus@leaf02:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf02:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf02:~$ cl set interface bond3 bond mlag id 3
cumulus@leaf02:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf02:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf02:~$ cl set interface bond3 bond lacp-bypass on
cumulus@leaf02:~$ cl set interface bond1 link mtu 9000
cumulus@leaf02:~$ cl set interface bond2 link mtu 9000
cumulus@leaf02:~$ cl set interface bond3 link mtu 9000
cumulus@leaf02:~$ cl set interface bond1-3 bridge domain br_default
cumulus@leaf02:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf02:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf02:~$ cl set interface bond3 bridge domain br_default access 30
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10,20,30
cumulus@leaf02:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf02:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ cl set mlag backup 10.10.10.1
cumulus@leaf02:~$ cl set mlag peer-ip linklocal
cumulus@leaf02:~$ cl set mlag priority 32768
cumulus@leaf02:~$ cl set mlag init-delay 10
cumulus@leaf02:~$ cl set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:~$ cl set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf02:~$ cl set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf02:~$ cl set interface vlan10 ip vrr state up
cumulus@leaf02:~$ cl set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:~$ cl set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf02:~$ cl set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf02:~$ cl set interface vlan20 ip vrr state up
cumulus@leaf02:~$ cl set interface vlan30 ip address 10.1.30.3/24
cumulus@leaf02:~$ cl set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf02:~$ cl set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf02:~$ cl set interface vlan30 ip vrr state up
cumulus@leaf02:~$ cl set vrf RED
cumulus@leaf02:~$ cl set vrf BLUE
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf02:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf02:~$ cl set bridge domain br_default vlan 30 vni 30
cumulus@leaf02:~$ cl set interface vlan10 ip vrf RED
cumulus@leaf02:~$ cl set interface vlan20 ip vrf RED
cumulus@leaf02:~$ cl set interface vlan30 ip vrf BLUE
cumulus@leaf02:~$ cl set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf02:~$ cl set nve vxlan source address 10.10.10.2
cumulus@leaf02:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf02:~$ cl set vrf RED evpn vni 4001
cumulus@leaf02:~$ cl set vrf BLUE evpn vni 4002
cumulus@leaf02:~$ cl set bridge domain br_default vlan 4001,4002
cumulus@leaf02:~$ cl set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ cl set evpn enable on
cumulus@leaf02:~$ cl set router bgp autonomous-system 65102
cumulus@leaf02:~$ cl set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf02:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf02:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf02:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf02:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf02:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf02:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cl set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ cl set interface swp1-3,swp49-54
cumulus@leaf03:~$ cl set interface bond1 bond member swp1
cumulus@leaf03:~$ cl set interface bond2 bond member swp2
cumulus@leaf03:~$ cl set interface bond3 bond member swp3
cumulus@leaf03:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf03:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf03:~$ cl set interface bond3 bond mlag id 3
cumulus@leaf03:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf03:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf03:~$ cl set interface bond3 bond lacp-bypass on
cumulus@leaf03:~$ cl set interface bond1 link mtu 9000
cumulus@leaf03:~$ cl set interface bond2 link mtu 9000
cumulus@leaf03:~$ cl set interface bond3 link mtu 9000
cumulus@leaf03:~$ cl set interface bond1-3 bridge domain br_default
cumulus@leaf03:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf03:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf03:~$ cl set interface bond3 bridge domain br_default access 30
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10,20,30
cumulus@leaf03:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf03:~$ cl set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf03:~$ cl set mlag backup 10.10.10.3
cumulus@leaf03:~$ cl set mlag peer-ip linklocal
cumulus@leaf03:~$ cl set mlag priority 1000
cumulus@leaf03:~$ cl set mlag init-delay 10
cumulus@leaf03:~$ cl set interface vlan10 ip address 10.1.10.4/24
cumulus@leaf03:~$ cl set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf03:~$ cl set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf03:~$ cl set interface vlan10 ip vrr state up
cumulus@leaf03:~$ cl set interface vlan20 ip address 10.1.20.4/24
cumulus@leaf03:~$ cl set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf03:~$ cl set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf03:~$ cl set interface vlan20 ip vrr state up
cumulus@leaf03:~$ cl set interface vlan30 ip address 10.1.30.4/24
cumulus@leaf03:~$ cl set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf03:~$ cl set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf03:~$ cl set interface vlan30 ip vrr state up
cumulus@leaf03:~$ cl set vrf RED
cumulus@leaf03:~$ cl set vrf BLUE
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf03:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf03:~$ cl set bridge domain br_default vlan 30 vni 30
cumulus@leaf03:~$ cl set interface vlan10 ip vrf RED
cumulus@leaf03:~$ cl set interface vlan20 ip vrf RED
cumulus@leaf03:~$ cl set interface vlan30 ip vrf BLUE
cumulus@leaf03:~$ cl set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf03:~$ cl set nve vxlan source address 10.10.10.3
cumulus@leaf03:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf03:~$ cl set vrf RED evpn vni 4001
cumulus@leaf03:~$ cl set vrf BLUE evpn vni 4002
cumulus@leaf03:~$ cl set bridge domain br_default vlan 4001,4002
cumulus@leaf03:~$ cl set system global anycast-mac 44:38:39:BE:EF:BB
cumulus@leaf03:~$ cl set evpn enable on
cumulus@leaf03:~$ cl set router bgp autonomous-system 65103
cumulus@leaf03:~$ cl set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf03:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf03:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf03:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf03:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf03:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf03:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cl set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ cl set interface swp1-3,swp49-54
cumulus@leaf04:~$ cl set interface bond1 bond member swp1
cumulus@leaf04:~$ cl set interface bond2 bond member swp2
cumulus@leaf04:~$ cl set interface bond3 bond member swp3
cumulus@leaf04:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf04:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf04:~$ cl set interface bond3 bond mlag id 3
cumulus@leaf04:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf04:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf04:~$ cl set interface bond3 bond lacp-bypass on
cumulus@leaf04:~$ cl set interface bond1 link mtu 9000
cumulus@leaf04:~$ cl set interface bond2 link mtu 9000
cumulus@leaf04:~$ cl set interface bond3 link mtu 9000
cumulus@leaf04:~$ cl set interface bond1-3 bridge domain br_default
cumulus@leaf04:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf04:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf04:~$ cl set interface bond3 bridge domain br_default access 30
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10,20,30
cumulus@leaf04:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf04:~$ cl set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf04:~$ cl set mlag backup 10.10.10.3
cumulus@leaf04:~$ cl set mlag peer-ip linklocal
cumulus@leaf04:~$ cl set mlag priority 32768
cumulus@leaf04:~$ cl set mlag init-delay 10
cumulus@leaf04:~$ cl set interface vlan10 ip address 10.1.10.5/24
cumulus@leaf04:~$ cl set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf04:~$ cl set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf04:~$ cl set interface vlan10 ip vrr state up
cumulus@leaf04:~$ cl set interface vlan20 ip address 10.1.20.5/24
cumulus@leaf04:~$ cl set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf04:~$ cl set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf04:~$ cl set interface vlan20 ip vrr state up
cumulus@leaf04:~$ cl set interface vlan30 ip address 10.1.30.5/24
cumulus@leaf04:~$ cl set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf04:~$ cl set interface vlan30 ip vrr mac-address 00:00:00:00:00:30cl set 
cumulus@leaf04:~$ cl set interface vlan30 ip vrr state up
cumulus@leaf04:~$ cl set vrf RED
cumulus@leaf04:~$ cl set vrf BLUE
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf04:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf04:~$ cl set bridge domain br_default vlan 30 vni 30
cumulus@leaf04:~$ cl set interface vlan10 ip vrf RED
cumulus@leaf04:~$ cl set interface vlan20 ip vrf RED
cumulus@leaf04:~$ cl set interface vlan30 ip vrf BLUE
cumulus@leaf04:~$ cl set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf04:~$ cl set nve vxlan source address 10.10.10.4
cumulus@leaf04:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf04:~$ cl set vrf RED evpn vni 4001
cumulus@leaf04:~$ cl set vrf BLUE evpn vni 4002
cumulus@leaf04:~$ cl set bridge domain br_default vlan 4001,4002
cumulus@leaf04:~$ cl set system global anycast-mac 44:38:39:BE:EF:BB
cumulus@leaf04:~$ cl set evpn enable on
cumulus@leaf04:~$ cl set router bgp autonomous-system 65104
cumulus@leaf04:~$ cl set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf04:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf04:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf04:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf04:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf04:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@leaf04:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cl set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ cl set interface swp1-6
cumulus@spine01:~$ cl set router bgp autonomous-system 65199
cumulus@spine01:~$ cl set router bgp router-id 10.10.10.101
cumulus@spine01:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine01:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine01:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine01:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine01:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine01:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine01:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cl set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ cl set interface swp1-6
cumulus@spine02:~$ cl set router bgp autonomous-system 65199
cumulus@spine02:~$ cl set router bgp router-id 10.10.10.102
cumulus@spine02:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine02:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine02:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine02:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine02:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine02:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine02:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine03 ">}}

```
cumulus@spine03:~$ cl set interface lo ip address 10.10.10.103/32
cumulus@spine03:~$ cl set interface swp1-6
cumulus@spine03:~$ cl set router bgp autonomous-system 65199
cumulus@spine03:~$ cl set router bgp router-id 10.10.10.103
cumulus@spine03:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine03:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine03:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine03:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine03:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine03:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine03:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine04 ">}}

```
cumulus@spine04:~$ cl set interface lo ip address 10.10.10.104/32
cumulus@spine04:~$ cl set interface swp1-6
cumulus@spine04:~$ cl set router bgp autonomous-system 65199
cumulus@spine04:~$ cl set router bgp router-id 10.10.10.104
cumulus@spine04:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@spine04:~$ cl set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp5 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp peer swp6 peer-group underlay
cumulus@spine04:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine04:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine04:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine04:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@spine04:~$ cl config apply
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ cl set interface lo ip address 10.10.10.63/32
cumulus@border01:~$ cl set interface swp3,swp49-54
cumulus@border01:~$ cl set interface bond3 bond member swp3
cumulus@border01:~$ cl set interface bond3 bond mlag id 1
cumulus@border01:~$ cl set interface bond3 bond lacp-bypass on
cumulus@border01:~$ cl set interface bond3 link mtu 9000
cumulus@border01:~$ cl set interface bond3 bridge domain br_default
cumulus@border01:~$ cl set interface bond3 bridge domain br_default vlan 101,102
cumulus@border01:~$ cl set interface peerlink bond member swp49-50
cumulus@border01:~$ cl set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border01:~$ cl set mlag backup 10.10.10.64
cumulus@border01:~$ cl set mlag peer-ip linklocal
cumulus@border01:~$ cl set mlag priority 1000
cumulus@border01:~$ cl set mlag init-delay 10
cumulus@border01:~$ cl set vrf RED
cumulus@border01:~$ cl set vrf BLUE
cumulus@border01:~$ cl set interface vlan101 ip address 10.1.101.64/24
cumulus@border01:~$ cl set interface vlan101 ip vrr address 10.1.101.1/24
cumulus@border01:~$ cl set interface vlan101 ip vrr mac-address 00:00:00:00:00:01
cumulus@border01:~$ cl set interface vlan101 ip vrr state up
cumulus@border01:~$ cl set interface vlan102 ip address 10.1.102.64/24
cumulus@border01:~$ cl set interface vlan102 ip vrr address 10.1.102.1/24
cumulus@border01:~$ cl set interface vlan102 ip vrr mac-address 00:00:00:00:00:02
cumulus@border01:~$ cl set interface vlan102 ip vrr state up
cumulus@border01:~$ cl set bridge domain br_default vlan 101,102
cumulus@border01:~$ cl set interface vlan101 ip vrf RED
cumulus@border01:~$ cl set interface vlan102 ip vrf BLUE
cumulus@border01:~$ cl set nve vxlan mlag shared-address 10.0.1.255
cumulus@border01:~$ cl set nve vxlan source address 10.10.10.63
cumulus@border01:~$ cl set nve vxlan arp-nd-suppress on
cumulus@border01:~$ cl set vrf RED evpn vni 4001
cumulus@border01:~$ cl set vrf BLUE evpn vni 4002
cumulus@border01:~$ cl set bridge domain br_default vlan 4001,4002
cumulus@border01:~$ cl set system global anycast-mac 44:38:39:BE:EF:FF
cumulus@border01:~$ cl set evpn enable on
cumulus@border01:~$ cl set router bgp autonomous-system 65253
cumulus@border01:~$ cl set router bgp router-id 10.10.10.63
cumulus@border01:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@border01:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@border01:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@border01:~$ cl set vrf RED router bgp autonomous-system 651063
cumulus@border01:~$ cl set vrf RED router bgp router-id 10.10.10.63
cumulus@border01:~$ cl set vrf RED router bgp path-selection multipath aspath-ignore on
cumulus@border01:~$ cl set vrf BLUE router bgp autonomous-system 65132
cumulus@border01:~$ cl set vrf BLUE router bgp router-id 10.10.10.63
cumulus@border01:~$ cl set vrf BLUE router bgp path-selection multipath aspath-ignore on
cumulus@border01:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@border01:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@border01:~$ cl config apply
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ cl set interface lo ip address 10.10.10.64/32
cumulus@border02:~$ cl set interface swp3,swp49-54
cumulus@border02:~$ cl set interface bond3 bond member swp3
cumulus@border02:~$ cl set interface bond3 bond mlag id 1
cumulus@border02:~$ cl set interface bond3 bond lacp-bypass on
cumulus@border02:~$ cl set interface bond3 link mtu 9000
cumulus@border01:~$ cl set interface bond3 bridge domain br_default
cumulus@border01:~$ cl set interface bond3 bridge domain br_default vlan 101,102
cumulus@border02:~$ cl set interface peerlink bond member swp49-50
cumulus@border02:~$ cl set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border02:~$ cl set mlag backup 10.10.10.63
cumulus@border02:~$ cl set mlag peer-ip linklocal
cumulus@border02:~$ cl set mlag priority 32768
cumulus@border02:~$ cl set mlag init-delay 10
cumulus@border02:~$ cl set vrf RED
cumulus@border02:~$ cl set vrf BLUE
cumulus@border01:~$ cl set interface vlan101 ip address 10.1.101.65/24
cumulus@border01:~$ cl set interface vlan101 ip vrr address 10.1.101.1/24
cumulus@border01:~$ cl set interface vlan101 ip vrr mac-address 00:00:00:00:00:01
cumulus@border01:~$ cl set interface vlan101 ip vrr state up
cumulus@border01:~$ cl set interface vlan102 ip address 10.1.102.65/24
cumulus@border01:~$ cl set interface vlan102 ip vrr address 10.1.102.1/24
cumulus@border01:~$ cl set interface vlan102 ip vrr mac-address 00:00:00:00:00:02
cumulus@border01:~$ cl set interface vlan102 ip vrr state up
cumulus@border02:~$ cl set bridge domain br_default vlan 101,102
cumulus@border01:~$ cl set interface vlan101 ip vrf RED
cumulus@border01:~$ cl set interface vlan102 ip vrf BLUE
cumulus@border02:~$ cl set nve vxlan mlag shared-address 10.0.1.255
cumulus@border02:~$ cl set nve vxlan source address 10.10.10.64
cumulus@border02:~$ cl set nve vxlan arp-nd-suppress on
cumulus@border02:~$ cl set vrf RED evpn vni 4001
cumulus@border02:~$ cl set vrf BLUE evpn vni 4002
cumulus@border02:~$ cl set bridge domain br_default vlan 4001,4002
cumulus@border02:~$ cl set system global anycast-mac 44:38:39:BE:EF:FF
cumulus@border02:~$ cl set evpn enable on
cumulus@border02:~$ cl set router bgp autonomous-system 65254
cumulus@border02:~$ cl set router bgp router-id 10.10.10.64
cumulus@border02:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@border02:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@border02:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@border02:~$ cl set vrf RED router bgp autonomous-system 65132
cumulus@border02:~$ cl set vrf RED router bgp router-id 10.10.10.63
cumulus@border02:~$ cl set vrf RED router bgp path-selection multipath aspath-ignore on
cumulus@border02:~$ cl set vrf BLUE router bgp autonomous-system 65132
cumulus@border02:~$ cl set vrf BLUE router bgp router-id 10.10.10.63
cumulus@border02:~$ cl set vrf BLUE router bgp path-selection multipath aspath-ignore on
cumulus@border02:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border02:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@border02:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@border02:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

### /etc/network/interfaces

{{< tabs "TabID2970 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/network/interfaces

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
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.2/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30

auto vni4001
iface vni4001
    bridge-access 4024
    bridge-learning off
    vxlan-id 4001

auto vlan4024
iface vlan4024
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:AA
    vlan-id 4024

auto vni4002
iface vni4002
    bridge-access 4036
    bridge-learning off
    vxlan-id 4002

auto vlan4036
iface vlan4036
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:AA
    vlan-id 4036

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 bond3 vni10 vni20 vni30 vni4001 vni4002
    bridge-vlan-aware yes
    bridge-vids 10 20 30 4001 4002
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/network/interfaces

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
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 10

auto vlan10
iface vlan10
    address 10.1.10.3/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.3/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.3/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30

auto vni4001
iface vni4001
    bridge-access 4024
    bridge-learning off
    vxlan-id 4001

auto vlan4024
iface vlan4024
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:AA
    vlan-id 4024

auto vni4002
iface vni4002
    bridge-access 4036
    bridge-learning off
    vxlan-id 4002

auto vlan4036
iface vlan4036
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:AA
    vlan-id 4036

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 bond3 vni10 vni20 vni30 vni4001 vni4002
    bridge-vlan-aware yes
    bridge-vids 10 20 30 4001 4002
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/network/interfaces

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
    clagd-backup-ip 10.10.10.4
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10

auto vlan10
iface vlan10
    address 10.1.10.4/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.4/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.4/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30

auto vni4001
iface vni4001
    bridge-access 4024
    bridge-learning off
    vxlan-id 4001

auto vlan4024
iface vlan4024
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:BB
    vlan-id 4024

auto vni4002
iface vni4002
    bridge-access 4036
    bridge-learning off
    vxlan-id 4002

auto vlan4036
iface vlan4036
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:BB
    vlan-id 4036

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 bond3 vni10 vni20 vni30 vni4001 vni4002
    bridge-vlan-aware yes
    bridge-vids 10 20 30 4001 4002
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/network/interfaces

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
    clagd-backup-ip 10.10.10.3
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 10

auto vlan10
iface vlan10
    address 10.1.10.5/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.5/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.5/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30

auto vni4001
iface vni4001
    bridge-access 4024
    bridge-learning off
    vxlan-id 4001

auto vlan4024
iface vlan4024
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:BB
    vlan-id 4024

auto vni4002
iface vni4002
    bridge-access 4036
    bridge-learning off
    vxlan-id 4002

auto vlan4036
iface vlan4036
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:BB
    vlan-id 4036

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 bond3 vni10 vni20 vni30 vni4001 vni4002
    bridge-vlan-aware yes
    bridge-vids 10 20 30 4001 4002
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.101/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
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
cumulus@spine02:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.102/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
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
cumulus@spine03:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.103/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
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
cumulus@spine04:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.104/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
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
cumulus@border01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.63/32
    clagd-vxlan-anycast-ip 10.0.1.255
    vxlan-local-tunnelip 10.10.10.63

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto RED
iface RED
  vrf-table auto

auto BLUE
iface BLUE
  vrf-table auto

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
    clag-id 1
    bond-slaves swp3
    bond-lacp-bypass-allow yes
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
    vrf RED
    vlan-raw-device br_default
    vlan-id 101

auto vlan102
iface vlan102
    address 10.1.102.64/24
    address-virtual 00:00:00:00:00:02 10.1.102.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 102

auto vni4001
iface vni4001
    bridge-access 4024
    bridge-learning off
    vxlan-id 4001

auto vlan4024
iface vlan4024
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:FF
    vlan-id 4024

auto vni4002
iface vni4002
    bridge-access 4036
    bridge-learning off
    vxlan-id 4002

auto vlan4036
iface vlan4036
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:FF
    vlan-id 4036

auto br_default
iface br_default
    bridge-ports peerlink bond3 vni4001 vni4002
    bridge-vlan-aware yes
    bridge-vids 4001 4002 
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ cat /etc/network/interfaces

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
    clagd-backup-ip 10.10.10.63
    clagd-sys-mac 44:38:39:BE:EF:FF
    clagd-args --initDelay 10

auto vlan101
iface vlan101
    address 10.1.101.65/24
    address-virtual 00:00:00:00:00:01 10.1.101.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 101

auto vlan102
iface vlan102
    address 10.1.102.65/24
    address-virtual 00:00:00:00:00:02 10.1.102.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 102

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

auto vni4001
iface vni4001
    bridge-access 4024
    bridge-learning off
    vxlan-id 4001

auto vlan4024
iface vlan4024
    vrf RED
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:FF
    vlan-id 4024

auto vni4002
iface vni4002
    bridge-access 4036
    bridge-learning off
    vxlan-id 4002

auto vlan4036
iface vlan4036
    vrf BLUE
    vlan-raw-device br_default
    address-virtual 44:38:39:BE:EF:FF
    vlan-id 4036

auto br_default
iface br_default
    bridge-ports peerlink bond3 vni4001 vni4002
    bridge-vlan-aware yes
    bridge-vids 4001 4002 101 102
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

### /etc/frr/frr.conf

{{< tabs "TabID3535 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf
...
vrf RED
  vni 4001
vrf BLUE
  vni 4002
!
router bgp 65101
 bgp router-id 10.10.10.1
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf
...
vrf RED
  vni 4001
vrf BLUE
  vni 4002
!
router bgp 65102
 bgp router-id 10.10.10.2
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf
...
vrf RED
  vni 4001
vrf BLUE
  vni 4002
!
router bgp 65103
 bgp router-id 10.10.10.3
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf
...
vrf RED
  vni 4001
vrf BLUE
  vni 4002
!
router bgp 65104
 bgp router-id 10.10.10.4
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 bgp bestpath as-path multipath-relax
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
cumulus@spine02:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.102
 bgp bestpath as-path multipath-relax
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
cumulus@spine03:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.103
 bgp bestpath as-path multipath-relax
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
cumulus@spine04:~$ cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.104
 bgp bestpath as-path multipath-relax
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
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ cat /etc/frr/frr.conf
...
vrf RED
  vni 4001
vrf BLUE
  vni 4002
!
router bgp 65253
 bgp router-id 10.10.10.63
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
router bgp 65132 vrf RED
 bgp router-id 10.10.10.63
 bgp bestpath as-path multipath-relax
 !
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
router bgp 65132 vrf BLUE
 bgp router-id 10.10.10.63
 bgp bestpath as-path multipath-relax
 !
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ cat /etc/frr/frr.conf
...
vrf RED
  vni 4001
vrf BLUE
  vni 4002
!
router bgp 65254
 bgp router-id 10.10.10.64
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
router bgp 65132 vrf RED
 bgp router-id 10.10.10.64
 bgp bestpath as-path multipath-relax
 !
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
router bgp 65132 vrf BLUE
 bgp router-id 10.10.10.64
 bgp bestpath as-path multipath-relax
 !
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
```

{{< /tab >}}
{{< /tabs >}}

<!-- ## EVPN Asymmetric Routing

The following example shows an EVPN asymmetric routing configuration.

{{< img src = "/images/cumulus-linux/evpn-asymmetric.png" >}}

### /etc/network/interfaces

{{< tabs "TabID1920 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.7/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9216

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9216

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9216

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9216
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.10
    clagd-backup-ip 10.0.0.8

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 45.0.0.2/24
    address 2001:fee1::2/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 45.0.1.2/24
    address 2001:fee1:0:1::2/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    address 45.0.2.2/24
    address 2001:fee1:0:2::2/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2

auto vlan1003
iface vlan1003
    address 45.0.3.2/24
    address 2001:fee1:0:3::2/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2
```

{{< /tab >}}

{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.8/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9216

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9216

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9216

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9216
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.9
    clagd-backup-ip 10.0.0.7

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 45.0.0.3/24
    address 2001:fee1::3/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 45.0.1.3/24
    address 2001:fee1:0:1::3/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    address 45.0.2.3/24
    address 2001:fee1:0:2::3/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2

auto vlan1003
iface vlan1003
    address 45.0.3.3/24
    address 2001:fee1:0:3::3/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2
```

{{< /tab >}}

{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.9/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 36.0.0.9

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9216

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9216

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9216

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9216
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.10
    clagd-backup-ip 10.0.0.10

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 45.0.0.2/24
    address 2001:fee1::2/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 45.0.1.2/24
    address 2001:fee1:0:1::2/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    address 45.0.2.2/24
    address 2001:fee1:0:2::2/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2

auto vlan1003
iface vlan1003
    address 45.0.3.2/24
    address 2001:fee1:0:3::2/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2
```

{{< /tab >}}

{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.10/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 36.0.0.9

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9216

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9216

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9216

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9216
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.9
    clagd-backup-ip 10.0.0.9

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 45.0.0.3/24
    address 2001:fee1::3/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 45.0.1.3/24
    address 2001:fee1:0:1::3/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    address 45.0.2.3/24
    address 2001:fee1:0:2::3/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2

auto vlan1003
iface vlan1003
    address 45.0.3.3/24
    address 2001:fee1:0:3::3/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.5/32
    alias BGP un-numbered Use for Vxlan Src Tunnel

auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9216

auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9216

auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9216
auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9216
```

{{< /tab >}}

{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.6/32
    alias BGP un-numbered Use for Vxlan Src Tunnel

auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9216

auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9216

auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9216

auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9216
```

{{< /tab >}}

{{< /tabs >}}

### /etc/frr/frr.conf

{{< tabs "TabID2615 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65542
 bgp router-id 10.0.0.7
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

{{< /tab >}}

{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65543
 bgp router-id 10.0.0.8
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

{{< /tab >}}

{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65544
 bgp router-id 10.0.0.9
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

{{< /tab >}}

{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65545
 bgp router-id 10.0.0.10
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.5
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

{{< /tab >}}

{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.6
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

{{< /tab >}}

{{< /tabs >}} -->
