---
title: Configuration Example
author: NVIDIA
weight: 880
toc: 3
---
This section shows a BGP configuration example based on the reference topology. The example configures BGP *unnumbered* on all leafs and spines, and MLAG on leaf01 and leaf02, and on leaf03 and leaf04.

{{< img src = "/images/cumulus-linux/mlag-config-peering.png" >}}

## NCLU Commands

{{< tabs "TabID13 ">}}
{{< tab "NCLU Commands">}}

{{< tabs "TabID16 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@leaf01:~$ net add bond bond1 bond slaves swp1
cumulus@leaf01:~$ net add bond bond2 bond slaves swp2
cumulus@leaf01:~$ net add bond bond3 bond slaves swp3
cumulus@leaf01:~$ net add bond bond1 clag id 1
cumulus@leaf01:~$ net add bond bond2 clag id 2
cumulus@leaf01:~$ net add bond bond3 clag id 3
cumulus@leaf01:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf01:~$ net add clag peer sys-mac 44:38:39:BE:EF:AA interface swp49-50 primary backup-ip 10.10.10.2
cumulus@leaf01:~$ net add vlan 10 ip address 10.1.10.2/24
cumulus@leaf01:~$ net add vlan 20 ip address 10.1.20.2/24
cumulus@leaf01:~$ net add vlan 30 ip address 10.1.30.2/24
cumulus@leaf01:~$ net add bridge bridge vids 10,20,30
cumulus@leaf01:~$ net add bridge bridge pvid 1
cumulus@leaf01:~$ net add bgp autonomous-system 65101
cumulus@leaf01:~$ net add bgp router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf01:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf01:~$ net add bgp ipv4 unicast network 10.10.10.1/32
cumulus@leaf01:~$ net add bgp ipv4 unicast network 10.1.10.0/24
cumulus@leaf01:~$ net add bgp ipv4 unicast redistribute connected 
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ net add loopback lo ip address 10.10.10.2/32
cumulus@leaf02:~$ net add bond bond1 bond slaves swp1
cumulus@leaf02:~$ net add bond bond2 bond slaves swp2
cumulus@leaf02:~$ net add bond bond3 bond slaves swp3
cumulus@leaf02:~$ net add bond bond1 clag id 1
cumulus@leaf02:~$ net add bond bond2 clag id 2
cumulus@leaf02:~$ net add bond bond3 clag id 3
cumulus@leaf02:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf02:~$ net add clag peer sys-mac 44:38:39:BE:EF:AA interface swp49-50 primary backup-ip 10.10.10.1
cumulus@leaf02:~$ net add vlan 10 ip address 10.1.10.3/24
cumulus@leaf02:~$ net add vlan 20 ip address 10.1.20.3/24
cumulus@leaf02:~$ net add vlan 30 ip address 10.1.30.3/24
cumulus@leaf02:~$ net add bridge bridge vids 10,20,30
cumulus@leaf02:~$ net add bridge bridge pvid 1
cumulus@leaf02:~$ net add bgp autonomous-system 65102
cumulus@leaf02:~$ net add bgp router-id 10.10.10.2
cumulus@leaf02:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf02:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf02:~$ net add bgp ipv4 unicast network 10.10.10.1/32
cumulus@leaf02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf02:~$ net pending
cumulus@leaf02:~$ net commit
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ net add loopback lo ip address 10.10.10.3/32
cumulus@leaf03:~$ net add bond bond1 bond slaves swp1
cumulus@leaf03:~$ net add bond bond2 bond slaves swp2
cumulus@leaf03:~$ net add bond bond3 bond slaves swp3
cumulus@leaf03:~$ net add bond bond1 clag id 1
cumulus@leaf03:~$ net add bond bond2 clag id 2
cumulus@leaf03:~$ net add bond bond3 clag id 3
cumulus@leaf03:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf03:~$ net add clag peer sys-mac 44:38:39:BE:EF:BB interface swp49-50 primary backup-ip 10.10.10.4
cumulus@leaf03:~$ net add vlan 40 ip address 10.1.40.4/24
cumulus@leaf03:~$ net add vlan 50 ip address 10.1.50.4/24
cumulus@leaf03:~$ net add vlan 60 ip address 10.1.60.4/24
cumulus@leaf03:~$ net add bridge bridge vids 40,50,60
cumulus@leaf03:~$ net add bridge bridge pvid 1
cumulus@leaf03:~$ net add bgp autonomous-system 65103
cumulus@leaf03:~$ net add bgp router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf03:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf03:~$ net add bgp ipv4 unicast network 10.10.10.3/32
cumulus@leaf03:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf03:~$ net pending
cumulus@leaf03:~$ net commit
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ net add loopback lo ip address 10.10.10.4/32
cumulus@leaf04:~$ net add bond bond1 bond slaves swp1
cumulus@leaf04:~$ net add bond bond2 bond slaves swp2
cumulus@leaf04:~$ net add bond bond3 bond slaves swp3
cumulus@leaf04:~$ net add bond bond1 clag id 1
cumulus@leaf04:~$ net add bond bond2 clag id 2
cumulus@leaf04:~$ net add bond bond3 clag id 3
cumulus@leaf04:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf04:~$ net add clag peer sys-mac 44:38:39:BE:EF:BB interface swp49-50 primary backup-ip 10.10.10.3
cumulus@leaf04:~$ net add vlan 40 ip address 10.1.40.5/24
cumulus@leaf04:~$ net add vlan 50 ip address 10.1.50.5/24
cumulus@leaf04:~$ net add vlan 60 ip address 10.1.60.5/24
cumulus@leaf04:~$ net add bridge bridge vids 40,50,60
cumulus@leaf04:~$ net add bridge bridge pvid 1
cumulus@leaf04:~$ net add bgp autonomous-system 65103
cumulus@leaf04:~$ net add bgp router-id 10.10.10.3
cumulus@leaf04:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf04:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf04:~$ net add bgp ipv4 unicast network 10.10.10.101/32
cumulus@leaf04:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf04:~$ net pending
cumulus@leaf04:~$ net commit
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add loopback lo ip address 10.10.10.101/32
cumulus@spine01:~$ net add bgp autonomous-system 65199
cumulus@spine01:~$ net add bgp router-id 10.10.10.101
cumulus@spine01:~$ net add bgp neighbor swp1 remote-as external
cumulus@spine01:~$ net add bgp neighbor swp2 remote-as external
cumulus@spine01:~$ net add bgp neighbor swp3 remote-as external
cumulus@spine01:~$ net add bgp neighbor swp4 remote-as external
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ net add loopback lo ip address 10.10.10.102/32
cumulus@spine02:~$ net add bgp autonomous-system 65199
cumulus@spine02:~$ net add bgp router-id 10.10.10.102
cumulus@spine02:~$ net add bgp neighbor swp1 remote-as external
cumulus@spine02:~$ net add bgp neighbor swp2 remote-as external
cumulus@spine02:~$ net add bgp neighbor swp3 remote-as external
cumulus@spine02:~$ net add bgp neighbor swp4 remote-as external 
cumulus@spine02:~$ net pending
cumulus@spine02:~$ net commit
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID901 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.1/32
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
auto bond1
iface bond1
    bond-slaves swp1
    clag-id 1
auto bond2
iface bond2
    bond-slaves swp2
    clag-id 2
auto bond3
iface bond3
    bond-slaves swp3
    clag-id 3
auto bridge
iface bridge
    bridge-ports bond1 bond2 bond3 peerlink
    bridge-pvid 1
    bridge-vids 10 20 30
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
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:AA
auto vlan10
iface vlan10
    address 10.1.10.2/24
    vlan-id 10
    vlan-raw-device bridge
auto vlan20
iface vlan20
    address 10.1.20.2/24
    vlan-id 20
    vlan-raw-device bridge
auto vlan30
iface vlan30
    address 10.1.30.2/24
    vlan-id 30
    vlan-raw-device bridge
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.2/32
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
iface swp52
auto swp52
iface swp52
auto bond1
iface bond1
    clag-id 1
    bond-slaves swp1
auto bond2
iface bond2
    clag-id 2
    bond-slaves swp2
auto bond3
iface bond3
    clag-id 3
    bond-slaves swp3
auto bridge
iface bridge
    bridge-ports peerlink bond1 bond2 bond3
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
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
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
auto vlan10
iface vlan10
    address 10.1.10.3/24
    vlan-raw-device bridge
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.3/24
    vlan-raw-device bridge
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.3/24
    vlan-raw-device bridge
    vlan-id 30
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.3/32
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
auto bond1
iface bond1
    bond-slaves swp1
    clag-id 1
auto bond2
iface bond2
    bond-slaves swp2
    clag-id 2
auto bond3
iface bond3
    bond-slaves swp3
    clag-id 3
auto bridge
iface bridge
    bridge-ports peerlink bond1 bond2 bond3
    bridge-vids 40 50 60
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
    clagd-backup-ip 10.10.10.4
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:BB
auto vlan40
iface vlan40
    address 10.1.40.2/24
    vlan-raw-device bridge
    vlan-id 40
auto vlan50
iface vlan50
    address 10.1.50.2/24
    vlan-raw-device bridge
    vlan-id 50
auto vlan60
iface vlan60
    address 10.1.60.2/24
    vlan-raw-device bridge
    vlan-id 60
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.4/32
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
auto bond1
iface bond1
    bond-slaves swp
    clag-id 1
auto bond2
iface bond2
    bond-slaves swp2
    clag-id 2
auto bond3
iface bond3
    bond-slaves swp3
    clag-id 3
auto bridge
iface bridge
    bridge-ports peerlink bond1 bond2 bond3
    bridge-vids 40 50 60
    bridge-vlan-aware yes
auto mgmt
iface mgmt
    address 127.0.0.1/8
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    vrf mgmt
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.3
    clagd-sys-mac 44:38:39:BE:EF:BB
auto vlan40
iface vlan40
    address 10.1.40.3/24
    vlan-raw-device bridge
    vlan-id 40
auto vlan50
iface vlan50
    address 10.1.50.3/24
    vlan-raw-device bridge
    vlan-id 50
auto vlan60
iface vlan60
    address 10.1.60.3/24
    vlan-raw-device bridge
    vlan-id 60
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.101/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    vrf-table auto
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
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.102/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    vrf-table auto
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
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID944 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor swp51 interface
 neighbor swp51 remote-as external
 neighbor swp52 interface
 neighbor swp52 remote-as external
 address-family ipv4 unicast
  network 10.10.10.1/32
  network 10.1.10.0/24
  redistribute connected
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65102
 bgp router-id 10.10.10.2
 neighbor swp51 interface
 neighbor swp51 remote-as external
 neighbor swp52 interface
 neighbor swp52 remote-as external
 address-family ipv4 unicast
  network 10.10.10.2/32
  redistribute connected
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65103
 bgp router-id 10.10.10.3
 neighbor swp51 interface
 neighbor swp51 remote-as external
 neighbor swp52 interface
 neighbor swp52 remote-as external
 address-family ipv4 unicast
  network 10.10.10.3/32
  redistribute connected
 exit-address-family
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65104
 bgp router-id 10.10.10.4
 neighbor swp51 interface
 neighbor swp51 remote-as external
 neighbor swp52 interface
 neighbor swp52 remote-as external
 address-family ipv4 unicast
  network 10.10.10.4/32
  redistribute connected
 exit-address-family
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp1 interface
 neighbor swp1 remote-as external
 neighbor swp2 interface
 neighbor swp2 remote-as external
 neighbor swp3 interface
 neighbor swp3 remote-as external
 neighbor swp4 interface
 neighbor swp4 remote-as external
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.102
 neighbor swp1 interface
 neighbor swp1 remote-as external
 neighbor swp2 interface
 neighbor swp2 remote-as external
 neighbor swp3 interface
 neighbor swp3 remote-as external
 neighbor swp4 interface
 neighbor swp4 remote-as external
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## NVUE Commands

{{< tabs "TabID695 ">}}
{{< tab "NVUE Commands">}}

{{< tabs "TabID38 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1-3,swp49-52
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond3 bond member swp3
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf01:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf01:~$ nv set interface bond1-3 bridge domain br_default 
cumulus@leaf01:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:~$ nv set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:~$ nv set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ nv set bridge domain br_default untagged 1
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp peer swp51 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp peer swp52 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.1/32
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast static-network 10.1.10.0/24
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp1-3,swp49-52
cumulus@leaf02:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:~$ nv set interface bond3 bond member swp3
cumulus@leaf02:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf02:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf02:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf02:~$ nv set interface bond1-3 bridge domain br_default 
cumulus@leaf02:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:~$ nv set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:~$ nv set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:~$ nv set interface vlan30 ip address 10.1.30.3/24
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf02:~$ nv set bridge domain br_default untagged 1
cumulus@leaf02:~$ nv set router bgp autonomous-system 65102
cumulus@leaf02:~$ nv set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf default router bgp peer swp51 remote-as external
cumulus@leaf02:~$ nv set vrf default router bgp peer swp52 remote-as external
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.2/32
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ nv set interface swp1-3,swp49-52
cumulus@leaf03:~$ nv set interface bond1 bond member swp1
cumulus@leaf03:~$ nv set interface bond2 bond member swp2
cumulus@leaf03:~$ nv set interface bond3 bond member swp3
cumulus@leaf03:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf03:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf03:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf03:~$ nv set interface bond1-3 bridge domain br_default 
cumulus@leaf03:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf03:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf03:~$ nv set mlag backup 10.10.10.4
cumulus@leaf03:~$ nv set mlag peer-ip linklocal
cumulus@leaf03:~$ nv set interface vlan40 ip address 10.1.40.4/24
cumulus@leaf03:~$ nv set interface vlan50 ip address 10.1.50.4/24
cumulus@leaf03:~$ nv set interface vlan60 ip address 10.1.60.4/24
cumulus@leaf03:~$ nv set bridge domain br_default vlan 40,50,60
cumulus@leaf03:~$ nv set bridge domain br_default untagged 1
cumulus@leaf03:~$ nv set router bgp autonomous-system 65103
cumulus@leaf03:~$ nv set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ nv set vrf default router bgp peer swp51 remote-as external
cumulus@leaf03:~$ nv set vrf default router bgp peer swp52 remote-as external
cumulus@leaf03:~$ nv set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.3/32
cumulus@leaf03:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ nv set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ nv set interface swp1-3,swp49-52
cumulus@leaf04:~$ nv set interface bond1 bond member swp1
cumulus@leaf04:~$ nv set interface bond2 bond member swp2
cumulus@leaf04:~$ nv set interface bond3 bond member swp3
cumulus@leaf04:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf04:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf04:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf04:~$ nv set interface bond1-3 bridge domain br_default 
cumulus@leaf04:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf04:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf04:~$ nv set mlag backup 10.10.10.3
cumulus@leaf04:~$ nv set mlag peer-ip linklocal
cumulus@leaf04:~$ nv set interface vlan40 ip address 10.1.40.5/24
cumulus@leaf04:~$ nv set interface vlan50 ip address 10.1.50.5/24
cumulus@leaf04:~$ nv set interface vlan60 ip address 10.1.60.5/24
cumulus@leaf04:~$ nv set bridge domain br_default vlan 40,50,60
cumulus@leaf04:~$ nv set bridge domain br_default untagged 1
cumulus@leaf04:~$ nv set router bgp autonomous-system 65104
cumulus@leaf04:~$ nv set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ nv set vrf default router bgp peer swp51 remote-as external
cumulus@leaf04:~$ nv set vrf default router bgp peer swp52 remote-as external
cumulus@leaf04:~$ nv set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.4/32
cumulus@leaf04:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf04:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1-4
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp peer swp1 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp peer swp2 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp peer swp3 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp peer swp4 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.101/32
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ nv set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp1-4
cumulus@spine02:~$ nv set router bgp autonomous-system 65199
cumulus@spine02:~$ nv set router bgp router-id 10.10.10.102
cumulus@spine02:~$ nv set vrf default router bgp peer swp1 remote-as external
cumulus@spine02:~$ nv set vrf default router bgp peer swp2 remote-as external
cumulus@spine02:~$ nv set vrf default router bgp peer swp3 remote-as external
cumulus@spine02:~$ nv set vrf default router bgp peer swp4 remote-as external
cumulus@spine02:~$ nv set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.102/32
cumulus@spine02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

The NVUE `nv config save` command saves the configuration in the `/etc/nvue.d/startup.yaml` file. For example:

{{< tabs "TabID169 ">}}
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
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
        type: bond
        bridge:
          domain:
            br_default: {}
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
        type: bond
        bridge:
          domain:
            br_default: {}
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 3
        type: bond
        bridge:
          domain:
            br_default: {}
      vlan10:
        ip:
          address:
            10.1.10.2/24: {}
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.2/24: {}
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.2/24: {}
        type: svi
        vlan: 30
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
    bridge:
      domain:
        br_default:
          vlan:
            '10': {}
            '20': {}
            '30': {}
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.2: {}
      peer-ip: linklocal
      init-delay: 100
    router:
      bgp:
        autonomous-system: 65101
        enable: on
        router-id: 10.10.10.1
    vrf:
      default:
        router:
          bgp:
            peer:
              swp51:
                remote-as: external
                type: unnumbered
              swp52:
                remote-as: external
                type: unnumbered
            enable: on
            address-family:
              ipv4-unicast:
                static-network:
                  10.10.10.1/32: {}
                  10.1.10.0/24: {}
                enable: on
                redistribute:
                  connected:
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
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
        type: bond
        bridge:
          domain:
            br_default: {}
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
        type: bond
        bridge:
          domain:
            br_default: {}
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 3
        type: bond
        bridge:
          domain:
            br_default: {}
      vlan10:
        ip:
          address:
            10.1.10.3/24: {}
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.3/24: {}
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.3/24: {}
        type: svi
        vlan: 30
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
    bridge:
      domain:
        br_default:
          vlan:
            '10': {}
            '20': {}
            '30': {}
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.1: {}
      peer-ip: linklocal
      init-delay: 100
    router:
      bgp:
        autonomous-system: 65102
        enable: on
        router-id: 10.10.10.2
    vrf:
      default:
        router:
          bgp:
            peer:
              swp51:
                remote-as: external
                type: unnumbered
              swp52:
                remote-as: external
                type: unnumbered
            enable: on
            address-family:
              ipv4-unicast:
                static-network:
                  10.10.10.2/32: {}
                enable: on
                redistribute:
                  connected:
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
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
        type: bond
        bridge:
          domain:
            br_default: {}
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
        type: bond
        bridge:
          domain:
            br_default: {}
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 3
        type: bond
        bridge:
          domain:
            br_default: {}
      vlan40:
        ip:
          address:
            10.1.40.4/24: {}
        type: svi
        vlan: 40
      vlan50:
        ip:
          address:
            10.1.50.4/24: {}
        type: svi
        vlan: 50
      vlan60:
        ip:
          address:
            10.1.60.4/24: {}
        type: svi
        vlan: 60
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
    bridge:
      domain:
        br_default:
          vlan:
            '40': {}
            '50': {}
            '60': {}
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.4: {}
      peer-ip: linklocal
    router:
      bgp:
        autonomous-system: 65103
        enable: on
        router-id: 10.10.10.3
    vrf:
      default:
        router:
          bgp:
            peer:
              swp51:
                remote-as: external
                type: unnumbered
              swp52:
                remote-as: external
                type: unnumbered
            enable: on
            address-family:
              ipv4-unicast:
                static-network:
                  10.10.10.3/32: {}
                enable: on
                redistribute:
                  connected:
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
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
        type: bond
        bridge:
          domain:
            br_default: {}
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            id: 2
        type: bond
        bridge:
          domain:
            br_default: {}
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            id: 3
        type: bond
        bridge:
          domain:
            br_default: {}
      vlan40:
        ip:
          address:
            10.1.40.5/24: {}
        type: svi
        vlan: 40
      vlan50:
        ip:
          address:
            10.1.50.5/24: {}
        type: svi
        vlan: 50
      vlan60:
        ip:
          address:
            10.1.60.5/24: {}
        type: svi
        vlan: 60
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
    bridge:
      domain:
        br_default:
          vlan:
            '40': {}
            '50': {}
            '60': {}
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.3: {}
      peer-ip: linklocal
    router:
      bgp:
        autonomous-system: 65104
        enable: on
        router-id: 10.10.10.4
    vrf:
      default:
        router:
          bgp:
            peer:
              swp51:
                remote-as: external
                type: unnumbered
              swp52:
                remote-as: external
                type: unnumbered
            enable: on
            address-family:
              ipv4-unicast:
                static-network:
                  10.10.10.4/32: {}
                enable: on
                redistribute:
                  connected:
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
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.101
    vrf:
      default:
        router:
          bgp:
            peer:
              swp1:
                remote-as: external
                type: unnumbered
              swp2:
                remote-as: external
                type: unnumbered
              swp3:
                remote-as: external
                type: unnumbered
              swp4:
                remote-as: external
                type: unnumbered
            enable: on
            address-family:
              ipv4-unicast:
                static-network:
                  10.10.10.101/32: {}
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
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.102
    vrf:
      default:
        router:
          bgp:
            peer:
              swp1:
                remote-as: external
                type: unnumbered
              swp2:
                remote-as: external
                type: unnumbered
              swp3:
                remote-as: external
                type: unnumbered
              swp4:
                remote-as: external
                type: unnumbered
            enable: on
            address-family:
              ipv4-unicast:
                static-network:
                  10.10.10.102/32: {}
                enable: on
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Try It " >}}
    {{< simulation name="Try It CL44 - BGPv2" showNodes="leaf01,leaf02,leaf03,leaf04,spine01,spine02,server01,server04" >}}

This simulation starts with the example BGP configuration. The demo is pre-configured using {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/" text="NVUE">}} commands.

To validate the configuration, run the commands listed in the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Border-Gateway-Protocol-BGP/Troubleshooting/" text="Troubleshooting">}} section.

{{< /tab >}}
{{< /tabs >}}