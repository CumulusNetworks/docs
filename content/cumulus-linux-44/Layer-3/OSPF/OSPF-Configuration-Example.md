---
title: OSPF Configuration Example
author: NVIDIA
weight: 920
toc: 3
---
This section shows an OSPF configuration example based on the reference topology.

{{< img src = "/images/cumulus-linux/ospf-scalability-areas.png" >}}

In the example configuration:
- OSPFv2 *unnumbered* is configured on all leafs and spines
- MLAG is configured on leaf01 and leaf02, and on border01 and border02
- leaf01, leaf02, spine01, and spine02 are in area 0
- border01 and border02 are ABRs and are in area 0 (lo, swp51, swp52) and area 1 (swp1, swp2)

## NCLU Commands

{{< tabs "TabID17 ">}}
{{< tab "NCLU Commands ">}}

{{< tabs "TabID20 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@leaf01:~$ net add interface swp51 ip address 10.10.10.1/32
cumulus@leaf01:~$ net add interface swp52 ip address 10.10.10.1/32
cumulus@leaf01:~$ net add bond bond1 bond slaves swp1
cumulus@leaf01:~$ net add bond bond2 bond slaves swp2
cumulus@leaf01:~$ net add bond bond3 bond slaves swp3
cumulus@leaf01:~$ net add bond bond1 clag id 1
cumulus@leaf01:~$ net add bond bond1 bond lacp-bypass-allow
cumulus@leaf01:~$ net add bond bond1 stp bpduguard
cumulus@leaf01:~$ net add bond bond1 stp portadminedge
cumulus@leaf01:~$ net add bond bond1 bridge access 10
cumulus@leaf01:~$ net add bond bond2 clag id 2
cumulus@leaf01:~$ net add bond bond2 bond lacp-bypass-allow
cumulus@leaf01:~$ net add bond bond2 stp bpduguard
cumulus@leaf01:~$ net add bond bond2 stp portadminedge
cumulus@leaf01:~$ net add bond bond2 bridge access 20
cumulus@leaf01:~$ net add bond bond3 clag id 3
cumulus@leaf01:~$ net add bond bond3 bond lacp-bypass-allow
cumulus@leaf01:~$ net add bond bond3 stp bpduguard
cumulus@leaf01:~$ net add bond bond3 stp portadminedge
cumulus@leaf01:~$ net add bond bond3 bridge access 30
cumulus@leaf01:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf01:~$ net add clag peer sys-mac 44:38:39:BE:EF:AA interface swp49-50 primary backup-ip 10.10.10.2
cumulus@leaf01:~$ net add vlan 10 ip address 10.1.10.2/24
cumulus@leaf01:~$ net add vlan 20 ip address 10.1.20.2/24
cumulus@leaf01:~$ net add vlan 30 ip address 10.1.30.2/24
cumulus@leaf01:~$ net add bridge bridge vids 10,20,30
cumulus@leaf01:~$ net add bridge bridge pvid 1
cumulus@leaf01:~$ net add ospf router-id 10.10.10.1
cumulus@leaf01:~$ net add loopback lo ospf area 0
cumulus@leaf01:~$ net add interface swp51 ospf area 0
cumulus@leaf01:~$ net add interface swp51 ospf network point-to-point
cumulus@leaf01:~$ net add interface swp51 ospf hello-interval 5
cumulus@leaf01:~$ net add interface swp51 ospf dead-interval 60
cumulus@leaf01:~$ net add interface swp52 ospf area 0
cumulus@leaf01:~$ net add interface swp52 ospf network point-to-point
cumulus@leaf01:~$ net add interface swp52 ospf hello-interval 5
cumulus@leaf01:~$ net add interface swp52 ospf dead-interval 60
cumulus@leaf01:~$ net add vlan 10 ospf area 0
cumulus@leaf01:~$ net add vlan 20 ospf area 0
cumulus@leaf01:~$ net add vlan 30 ospf area 0
cumulus@leaf01:~$ net add ospf passive-interface vlan10
cumulus@leaf01:~$ net add ospf passive-interface vlan20
cumulus@leaf01:~$ net add ospf passive-interface vlan30
cumulus@leaf01:~$ net add ospf timers throttle spf 80 100 6000
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ net add loopback lo ip address 10.10.10.2/32
cumulus@leaf02:~$ net add interface swp51 ip address 10.10.10.2/32
cumulus@leaf02:~$ net add interface swp52 ip address 10.10.10.2/32
cumulus@leaf02:~$ net add bond bond1 bond slaves swp1
cumulus@leaf02:~$ net add bond bond2 bond slaves swp2
cumulus@leaf02:~$ net add bond bond3 bond slaves swp3
cumulus@leaf02:~$ net add bond bond1 clag id 1
cumulus@leaf02:~$ net add bond bond1 bond lacp-bypass-allow
cumulus@leaf02:~$ net add bond bond1 stp bpduguard
cumulus@leaf02:~$ net add bond bond1 stp portadminedge
cumulus@leaf02:~$ net add bond bond1 bridge access 10
cumulus@leaf02:~$ net add bond bond2 clag id 2
cumulus@leaf02:~$ net add bond bond2 bond lacp-bypass-allow
cumulus@leaf02:~$ net add bond bond2 stp bpduguard
cumulus@leaf02:~$ net add bond bond2 stp portadminedge
cumulus@leaf02:~$ net add bond bond2 bridge access 20
cumulus@leaf02:~$ net add bond bond3 clag id 3
cumulus@leaf02:~$ net add bond bond3 bond lacp-bypass-allow
cumulus@leaf02:~$ net add bond bond3 stp bpduguard
cumulus@leaf02:~$ net add bond bond3 stp portadminedge
cumulus@leaf02:~$ net add bond bond3 bridge access 30
cumulus@leaf02:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf02:~$ net add clag peer sys-mac 44:38:39:BE:EF:AA interface swp49-50 primary backup-ip 10.10.10.1
cumulus@leaf02:~$ net add vlan 10 ip address 10.1.10.2/24
cumulus@leaf02:~$ net add vlan 20 ip address 10.1.20.2/24
cumulus@leaf02:~$ net add vlan 30 ip address 10.1.30.2/24
cumulus@leaf02:~$ net add bridge bridge vids 10,20,30
cumulus@leaf02:~$ net add bridge bridge pvid 1
cumulus@leaf02:~$ net add ospf router-id 10.10.10.2
cumulus@leaf02:~$ net add loopback lo ospf area 0
cumulus@leaf02:~$ net add interface swp51 ospf area 0
cumulus@leaf02:~$ net add interface swp51 ospf network point-to-point
cumulus@leaf02:~$ net add interface swp51 ospf hello-interval 5
cumulus@leaf02:~$ net add interface swp51 ospf dead-interval 60
cumulus@leaf02:~$ net add interface swp52 ospf area 0
cumulus@leaf02:~$ net add interface swp52 ospf network point-to-point
cumulus@leaf02:~$ net add interface swp52 ospf hello-interval 5
cumulus@leaf02:~$ net add interface swp52 ospf dead-interval 60
cumulus@leaf02:~$ net add vlan 10 ospf area 0
cumulus@leaf02:~$ net add vlan 20 ospf area 0
cumulus@leaf02:~$ net add vlan 30 ospf area 0
cumulus@leaf02:~$ net add ospf passive-interface vlan10
cumulus@leaf02:~$ net add ospf passive-interface vlan20
cumulus@leaf02:~$ net add ospf passive-interface vlan30
cumulus@leaf02:~$ net add ospf timers throttle spf 80 100 6000
cumulus@leaf02:~$ net pending
cumulus@leaf02:~$ net commit
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add loopback lo ip address 10.10.10.101/32
cumulus@spine01:~$ net add interface swp1 ip address 10.10.10.101/32
cumulus@spine01:~$ net add interface swp2 ip address 10.10.10.101/32
cumulus@spine01:~$ net add interface swp5 ip address 10.10.10.101/32
cumulus@spine01:~$ net add interface swp6 ip address 10.10.10.101/32
cumulus@spine01:~$ net add ospf router-id 10.10.10.101
cumulus@spine01:~$ net add loopback lo ospf area 0
cumulus@spine01:~$ net add interface swp1 ospf area 0
cumulus@spine01:~$ net add interface swp1 ospf network point-to-point
cumulus@spine01:~$ net add interface swp1 ospf hello-interval 5
cumulus@spine01:~$ net add interface swp1 ospf dead-interval 60
cumulus@spine01:~$ net add interface swp2 ospf area 0
cumulus@spine01:~$ net add interface swp2 ospf network point-to-point
cumulus@spine01:~$ net add interface swp2 ospf hello-interval 5
cumulus@spine01:~$ net add interface swp2 ospf dead-interval 60
cumulus@spine01:~$ net add interface swp5 ospf area 0
cumulus@spine01:~$ net add interface swp5 ospf network point-to-point
cumulus@spine01:~$ net add interface swp5 ospf hello-interval 5
cumulus@spine01:~$ net add interface swp5 ospf dead-interval 60
cumulus@spine01:~$ net add interface swp6 ospf area 0
cumulus@spine01:~$ net add interface swp6 ospf network point-to-point
cumulus@spine01:~$ net add interface swp6 ospf hello-interval 5
cumulus@spine01:~$ net add interface swp6 ospf dead-interval 60
cumulus@spine01:~$ net add ospf timers throttle spf 80 100 6000
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ net add loopback lo ip address 10.10.10.102/32
cumulus@spine02:~$ net add interface swp1 ip address 10.10.10.102/32
cumulus@spine02:~$ net add interface swp2 ip address 10.10.10.102/32
cumulus@spine02:~$ net add interface swp5 ip address 10.10.10.102/32
cumulus@spine02:~$ net add interface swp6 ip address 10.10.10.102/32
cumulus@spine02:~$ net add ospf router-id 10.10.10.102
cumulus@spine02:~$ net add loopback lo ospf area 0
cumulus@spine02:~$ net add interface swp1 ospf area 0
cumulus@spine02:~$ net add interface swp1 ospf network point-to-point
cumulus@spine02:~$ net add interface swp1 ospf hello-interval 5
cumulus@spine02:~$ net add interface swp1 ospf dead-interval 60
cumulus@spine02:~$ net add interface swp2 ospf area 0
cumulus@spine02:~$ net add interface swp2 ospf network point-to-point
cumulus@spine02:~$ net add interface swp2 ospf hello-interval 5
cumulus@spine02:~$ net add interface swp2 ospf dead-interval 60
cumulus@spine02:~$ net add interface swp5 ospf area 0
cumulus@spine02:~$ net add interface swp5 ospf network point-to-point
cumulus@spine02:~$ net add interface swp5 ospf hello-interval 5
cumulus@spine02:~$ net add interface swp5 ospf dead-interval 60
cumulus@spine02:~$ net add interface swp6 ospf area 0
cumulus@spine02:~$ net add interface swp6 ospf network point-to-point
cumulus@spine02:~$ net add interface swp6 ospf hello-interval 5
cumulus@spine02:~$ net add interface swp6 ospf dead-interval 60
cumulus@spine02:~$ net add ospf timers throttle spf 80 100 6000
cumulus@spine02:~$ net pending
cumulus@spine02:~$ net commit
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ net add loopback lo ip address 10.10.10.63/32
cumulus@border01:~$ net add interface swp51 ip address 10.10.10.63/32
cumulus@border01:~$ net add interface swp52 ip address 10.10.10.63/32
cumulus@border01:~$ net add bond bond1 bond slaves swp1
cumulus@border01:~$ net add bond bond2 bond slaves swp2
cumulus@border01:~$ net add bond bond1 clag id 1
cumulus@border01:~$ net add bond bond1 bond lacp-bypass-allow
cumulus@border01:~$ net add bond bond1 stp bpduguard
cumulus@border01:~$ net add bond bond1 stp portadminedge
cumulus@border01:~$ net add bond bond1 bridge access 10
cumulus@border01:~$ net add bond bond2 clag id 2
cumulus@border01:~$ net add bond bond2 bond lacp-bypass-allow
cumulus@border01:~$ net add bond bond2 stp bpduguard
cumulus@border01:~$ net add bond bond2 stp portadminedge
cumulus@border01:~$ net add bond bond2 bridge access 20
cumulus@border01:~$ net add bridge bridge ports bond1,bond2
cumulus@border01:~$ net add clag peer sys-mac 44:38:39:BE:EF:FF interface swp49-50 primary backup-ip 10.10.10.64
cumulus@border01:~$ net add bridge bridge pvid 1
cumulus@border01:~$ net add ospf router-id 10.10.10.63
cumulus@border01:~$ net add loopback lo ospf area 0
cumulus@border01:~$ net add interface swp51 ospf area 0
cumulus@border01:~$ net add interface swp51 ospf network point-to-point
cumulus@border01:~$ net add interface swp51 ospf hello-interval 5
cumulus@border01:~$ net add interface swp51 ospf dead-interval 60
cumulus@border01:~$ net add interface swp52 ospf area 0
cumulus@border01:~$ net add interface swp52 ospf network point-to-point
cumulus@border01:~$ net add interface swp52 ospf hello-interval 5
cumulus@border01:~$ net add interface swp52 ospf dead-interval 60
cumulus@border01:~$ net add interface swp1 ospf area 1
cumulus@border01:~$ net add interface swp2 ospf area 1
cumulus@border01:~$ net add ospf timers throttle spf 80 100 6000
cumulus@border01:~$ net pending
cumulus@border01:~$ net commit
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ net add loopback lo ip address 10.10.10.64/32
cumulus@border02:~$ net add interface swp51 ip address 10.10.10.64/32
cumulus@border02:~$ net add interface swp52 ip address 10.10.10.64/32
cumulus@border02:~$ net add bond bond1 bond slaves swp1
cumulus@border02:~$ net add bond bond2 bond slaves swp2
cumulus@border02:~$ net add bond bond1 clag id 1
cumulus@border02:~$ net add bond bond1 bond lacp-bypass-allow
cumulus@border02:~$ net add bond bond1 stp bpduguard
cumulus@border02:~$ net add bond bond1 stp portadminedge
cumulus@border02:~$ net add bond bond1 bridge access 10
cumulus@border02:~$ net add bond bond2 clag id 2
cumulus@border02:~$ net add bond bond2 bond lacp-bypass-allow
cumulus@border02:~$ net add bond bond2 stp bpduguard
cumulus@border02:~$ net add bond bond2 stp portadminedge
cumulus@border02:~$ net add bond bond2 bridge access 20
cumulus@border02:~$ net add bridge bridge ports bond1,bond2
cumulus@border02:~$ net add vlan 10 vlan-id 10
cumulus@border02:~$ net add vlan 20 vlan-id 20
cumulus@border02:~$ net add bridge bridge vids 10,20
cumulus@border02:~$ net add vlan 10 ip forward off
cumulus@border02:~$ net add vlan 10 ipv6 forward off
cumulus@border02:~$ net add vlan 20 ip forward off
cumulus@border02:~$ net add vlan 20 ipv6 forward off
cumulus@border02:~$ net add clag peer sys-mac 44:38:39:BE:EF:FF interface swp49-50 primary backup-ip 10.10.10.63
cumulus@border02:~$ net add bridge bridge pvid 1
cumulus@border02:~$ net add ospf router-id 10.10.10.64
cumulus@border02:~$ net add loopback lo ospf area 0
cumulus@border02:~$ net add interface swp51 ospf area 0
cumulus@border02:~$ net add interface swp51 ospf network point-to-point
cumulus@border02:~$ net add interface swp51 ospf hello-interval 5
cumulus@border02:~$ net add interface swp51 ospf dead-interval 60
cumulus@border02:~$ net add interface swp52 ospf area 0
cumulus@border02:~$ net add interface swp52 ospf network point-to-point
cumulus@border02:~$ net add interface swp52 ospf hello-interval 5
cumulus@border02:~$ net add interface swp52 ospf dead-interval 60
cumulus@border02:~$ net add interface swp1 ospf area 1
cumulus@border02:~$ net add interface swp2 ospf area 1
cumulus@border02:~$ net add ospf timers throttle spf 80 100 6000
cumulus@border02:~$ net pending
cumulus@border02:~$ net commit
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID44 ">}}
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
    address 10.10.10.1/32

auto swp52
iface swp52
    address 10.10.10.1/32

auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto bond3
iface bond3
    bond-lacp-bypass-allow yes
    bond-slaves swp3
    bridge-access 30
    clag-id 3
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

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
iface swp51
    address 10.10.10.2/32

auto swp52
iface swp52
    address 10.10.10.2/32

auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto bond3
iface bond3
    bond-lacp-bypass-allow yes
    bond-slaves swp3
    bridge-access 30
    clag-id 3
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

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
    clagd-backup-ip 10.10.10.1
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
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.101/32

auto swp1
iface swp1
    address 10.10.10.101/32

auto swp2
iface swp2
    address 10.10.10.101/32

auto swp5
iface swp5
    address 10.10.10.101/32

auto swp6
iface swp6
    address 10.10.10.101/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.102/32

auto swp1
iface swp1
    address 10.10.10.102/32

auto swp2
iface swp2
    address 10.10.10.102/32

auto swp5
iface swp5
    address 10.10.10.102/32

auto swp6
iface swp6
    address 10.10.10.102/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.63/32

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
    address 10.10.10.63/32

auto swp52
iface swp52
    address 10.10.10.63/32

auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto bridge
iface bridge
    bridge-ports bond1 bond2 peerlink
    bridge-pvid 1
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
    clagd-backup-ip 10.10.10.64
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:FF
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.64/32

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
    address 10.10.10.64/32

auto swp52
iface swp52
    address 10.10.10.64/32

auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp1
    bridge-access 10
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto bond2
iface bond2
    bond-lacp-bypass-allow yes
    bond-slaves swp2
    bridge-access 20
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto bridge
iface bridge
    bridge-ports bond1 bond2 peerlink
    bridge-pvid 1
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
    clagd-backup-ip 10.10.10.63
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:FF

auto vlan10
iface vlan10
    ip6-forward off
    ip-forward off
    vlan-id 10
    vlan-raw-device bridge

auto vlan20
iface vlan20
    ip6-forward off
    ip-forward off
    vlan-id 20
    vlan-raw-device bridge
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID560 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
router ospf
 ospf router-id 10.10.10.1
 passive-interface vlan10
 passive-interface vlan20
 passive-interface vlan30
 timers throttle spf 80 100 6000
interface lo
 ip ospf area 0
interface swp51
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp52
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface vlan10
 ip ospf area 0
interface vlan20
 ip ospf area 0
interface vlan30
 ip ospf area 0
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
router ospf
 ospf router-id 10.10.10.2
 passive-interface vlan10
 passive-interface vlan20
 passive-interface vlan30
 timers throttle spf 80 100 6000
interface lo
 ip ospf area 0
interface swp51
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp52
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface vlan10
 ip ospf area 0
interface vlan20
 ip ospf area 0
interface vlan30
 ip ospf area 0
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
router ospf
 ospf router-id 10.10.10.101
 timers throttle spf 80 100 6000
interface lo
 ip ospf area 0
interface swp1
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp2
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp5
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp6
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
router ospf
 ospf router-id 10.10.10.102
 timers throttle spf 80 100 6000
interface lo
 ip ospf area 0
interface swp1
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp2
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp5
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp6
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf
...
router ospf
 ospf router-id 10.10.10.63
 timers throttle spf 80 100 6000
interface lo
 ip ospf area 0
interface swp51
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp52
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp1
 ip ospf area 1
interface swp2
 ip ospf area 1
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/frr/frr.conf
...
router ospf
 ospf router-id 10.10.10.64
 timers throttle spf 80 100 6000
interface lo
 ip ospf area 0
interface swp51
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp52
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
interface swp1
 ip ospf area 1
interface swp2
 ip ospf area 1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## NVUE Commands

{{< tabs "TabID801 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID804 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp51 ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp52 ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond3 bond member swp3
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf01:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf01:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond3 bond lacp-bypass on
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
cumulus@leaf01:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf01:~$ nv set vrf default router ospf router-id 10.10.10.1
cumulus@leaf01:~$ nv set interface lo router ospf area 0
cumulus@leaf01:~$ nv set interface swp51 router ospf area 0
cumulus@leaf01:~$ nv set interface swp52 router ospf area 0
cumulus@leaf01:~$ nv set interface swp51 router ospf network-type point-to-point
cumulus@leaf01:~$ nv set interface swp52 router ospf network-type point-to-point
cumulus@leaf01:~$ nv set interface swp51 router ospf timers hello-interval 5
cumulus@leaf01:~$ nv set interface swp51 router ospf timers dead-interval 60
cumulus@leaf01:~$ nv set interface swp52 router ospf timers hello-interval 5
cumulus@leaf01:~$ nv set interface swp52 router ospf timers dead-interval 60
cumulus@leaf01:~$ nv set interface vlan10 router ospf area 0
cumulus@leaf01:~$ nv set interface vlan20 router ospf area 0
cumulus@leaf01:~$ nv set interface vlan30 router ospf area 0
cumulus@leaf01:~$ nv set interface vlan10 router ospf passive on
cumulus@leaf01:~$ nv set interface vlan20 router ospf passive on
cumulus@leaf01:~$ nv set interface vlan30 router ospf passive on
cumulus@leaf01:~$ nv set router ospf timers spf delay 80
cumulus@leaf01:~$ nv set router ospf timers spf holdtime 100
cumulus@leaf01:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp51 ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp52 ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:~$ nv set interface bond3 bond member swp3
cumulus@leaf02:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf02:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf02:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf02:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf02:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf02:~$ nv set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf02:~$ nv set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf02:~$ nv set bridge domain br_default untagged 1
cumulus@leaf02:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf02:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf02:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf02:~$ nv set vrf default router ospf router-id 10.10.10.2
cumulus@leaf02:~$ nv set interface lo router ospf area 0
cumulus@leaf02:~$ nv set interface swp51 router ospf area 0
cumulus@leaf02:~$ nv set interface swp52 router ospf area 0
cumulus@leaf02:~$ nv set interface swp51 router ospf network-type point-to-point
cumulus@leaf02:~$ nv set interface swp52 router ospf network-type point-to-point
cumulus@leaf02:~$ nv set interface swp51 router ospf timers hello-interval 5
cumulus@leaf02:~$ nv set interface swp51 router ospf timers dead-interval 60
cumulus@leaf02:~$ nv set interface swp52 router ospf timers hello-interval 5
cumulus@leaf02:~$ nv set interface swp52 router ospf timers dead-interval 60
cumulus@leaf02:~$ nv set interface vlan10 router ospf area 0
cumulus@leaf02:~$ nv set interface vlan20 router ospf area 0
cumulus@leaf02:~$ nv set interface vlan30 router ospf area 0
cumulus@leaf02:~$ nv set interface vlan10 router ospf passive on
cumulus@leaf02:~$ nv set interface vlan20 router ospf passive on
cumulus@leaf02:~$ nv set interface vlan30 router ospf passive on
cumulus@leaf02:~$ nv set router ospf timers spf delay 80
cumulus@leaf02:~$ nv set router ospf timers spf holdtime 100
cumulus@leaf02:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1 ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp2 ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp5 ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp6 ip address 10.10.10.101/32
cumulus@spine01:~$ nv set vrf default router ospf router-id 10.10.10.101
cumulus@spine01:~$ nv set interface lo router ospf area 0
cumulus@spine01:~$ nv set interface swp1 router ospf area 0
cumulus@spine01:~$ nv set interface swp1 router ospf network-type point-to-point
cumulus@spine01:~$ nv set interface swp1 router ospf timers hello-interval 5
cumulus@spine01:~$ nv set interface swp1 router ospf timers dead-interval 60
cumulus@spine01:~$ nv set interface swp2 router ospf area 0
cumulus@spine01:~$ nv set interface swp2 router ospf network-type point-to-point
cumulus@spine01:~$ nv set interface swp2 router ospf timers hello-interval 5
cumulus@spine01:~$ nv set interface swp2 router ospf timers dead-interval 60
cumulus@spine01:~$ nv set interface swp5 router ospf area 0
cumulus@spine01:~$ nv set interface swp5 router ospf network-type point-to-point
cumulus@spine01:~$ nv set interface swp5 router ospf timers hello-interval 5
cumulus@spine01:~$ nv set interface swp5 router ospf timers dead-interval 60
cumulus@spine01:~$ nv set interface swp6 router ospf area 0
cumulus@spine01:~$ nv set interface swp6 router ospf network-type point-to-point
cumulus@spine01:~$ nv set interface swp6 router ospf timers hello-interval 5
cumulus@spine01:~$ nv set interface swp6 router ospf timers dead-interval 60
cumulus@spine01:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@spine01:~$ nv set router ospf timers spf holdtime 100
cumulus@spine01:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ nv set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp1 ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp2 ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp5 ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp6 ip address 10.10.10.102/32
cumulus@spine02:~$ nv set vrf default router ospf router-id 10.10.10.102
cumulus@spine02:~$ nv set interface lo router ospf area 0
cumulus@spine02:~$ nv set interface swp1 router ospf area 0
cumulus@spine02:~$ nv set interface swp1 router ospf network-type point-to-point
cumulus@spine02:~$ nv set interface swp1 router ospf timers hello-interval 5
cumulus@spine02:~$ nv set interface swp1 router ospf timers dead-interval 60
cumulus@spine02:~$ nv set interface swp2 router ospf area 0
cumulus@spine02:~$ nv set interface swp2 router ospf network-type point-to-point
cumulus@spine02:~$ nv set interface swp2 router ospf timers hello-interval 5
cumulus@spine02:~$ nv set interface swp2 router ospf timers dead-interval 60
cumulus@spine02:~$ nv set interface swp5 router ospf area 0
cumulus@spine02:~$ nv set interface swp5 router ospf network-type point-to-point
cumulus@spine02:~$ nv set interface swp5 router ospf timers hello-interval 5
cumulus@spine02:~$ nv set interface swp5 router ospf timers dead-interval 60
cumulus@spine02:~$ nv set interface swp6 router ospf area 0
cumulus@spine02:~$ nv set interface swp6 router ospf network-type point-to-point
cumulus@spine02:~$ nv set interface swp6 router ospf timers hello-interval 5
cumulus@spine02:~$ nv set interface swp6 router ospf timers dead-interval 60
cumulus@spine02:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@spine02:~$ nv set router ospf timers spf holdtime 100
cumulus@spine02:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@spine02:~$ nv config apply
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ nv set interface lo ip address 10.10.10.63/32
cumulus@border01:~$ nv set interface swp51 ip address 10.10.10.63/32
cumulus@border01:~$ nv set interface swp52 ip address 10.10.10.63/32
cumulus@border01:~$ nv set interface bond1 bond member swp1
cumulus@border01:~$ nv set interface bond2 bond member swp2
cumulus@border01:~$ nv set interface bond1 bond mlag id 1
cumulus@border01:~$ nv set interface bond2 bond mlag id 2
cumulus@border01:~$ nv set interface bond1 bond lacp-bypass on
cumulus@border01:~$ nv set interface bond2 bond lacp-bypass on
cumulus@border01:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@border01:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@border01:~$ nv set interface bond1-2 bridge domain br_default
cumulus@border01:~$ nv set interface peerlink bond member swp49-50
cumulus@border01:~$ nv set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border01:~$ nv set mlag backup 10.10.10.64
cumulus@border01:~$ nv set mlag peer-ip linklocal
cumulus@border01:~$ nv set bridge domain br_default untagged 1
cumulus@border01:~$ nv set vrf default router ospf router-id 10.10.10.63
cumulus@border01:~$ nv set interface lo router ospf area 0
cumulus@border01:~$ nv set interface swp51 router ospf area 0
cumulus@border01:~$ nv set interface swp51 router ospf network-type point-to-point
cumulus@border01:~$ nv set interface swp51 router ospf timers hello-interval 5
cumulus@border01:~$ nv set interface swp51 router ospf timers dead-interval 60
cumulus@border01:~$ nv set interface swp52 router ospf area 0
cumulus@border01:~$ nv set interface swp52 router ospf network-type point-to-point
cumulus@border01:~$ nv set interface swp52 router ospf timers hello-interval 5
cumulus@border01:~$ nv set interface swp52 router ospf timers dead-interval 60
cumulus@border01:~$ nv set interface swp1 router ospf area 1
cumulus@border01:~$ nv set interface swp2 router ospf area 1
cumulus@border01:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@border01:~$ nv set router ospf timers spf holdtime 100
cumulus@border01:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@border01:~$ nv config apply
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ nv set interface lo ip address 10.10.10.64/32
cumulus@border02:~$ nv set interface swp51 ip address 10.10.10.64/32
cumulus@border02:~$ nv set interface swp52 ip address 10.10.10.64/32
cumulus@border02:~$ nv set interface bond1 bond member swp1
cumulus@border02:~$ nv set interface bond2 bond member swp2
cumulus@border02:~$ nv set interface bond1 bond mlag id 1
cumulus@border02:~$ nv set interface bond2 bond mlag id 2
cumulus@border02:~$ nv set interface bond1 bond lacp-bypass on
cumulus@border02:~$ nv set interface bond2 bond lacp-bypass on
cumulus@border02:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@border02:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@border02:~$ nv set interface bond1-2 bridge domain br_default
cumulus@border02:~$ nv set interface vlan10
cumulus@border02:~$ nv set interface vlan20
cumulus@border02:~$ nv set interface vlan10 ip ipv4 forward off
cumulus@border02:~$ nv set interface vlan10 ip ipv6 forward off
cumulus@border02:~$ nv set interface vlan20 ip ipv4 forward off
cumulus@border02:~$ nv set interface vlan20 ip ipv6 forward off
cumulus@border02:~$ nv set interface peerlink bond member swp49-50
cumulus@border02:~$ nv set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border02:~$ nv set mlag backup 10.10.10.63
cumulus@border02:~$ nv set mlag peer-ip linklocal
cumulus@border02:~$ nv set bridge domain br_default untagged 1
cumulus@border02:~$ nv set vrf default router ospf router-id 10.10.10.64
cumulus@border02:~$ nv set interface lo router ospf area 0
cumulus@border02:~$ nv set interface swp51 router ospf area 0
cumulus@border02:~$ nv set interface swp51 router ospf network-type point-to-point
cumulus@border02:~$ nv set interface swp51 router ospf timers hello-interval 5
cumulus@border02:~$ nv set interface swp51 router ospf timers dead-interval 60
cumulus@border02:~$ nv set interface swp52 router ospf area 0
cumulus@border02:~$ nv set interface swp52 router ospf network-type point-to-point
cumulus@border02:~$ nv set interface swp52 router ospf timers hello-interval 5
cumulus@border02:~$ nv set interface swp52 router ospf timers dead-interval 60
cumulus@border02:~$ nv set interface swp1 router ospf area 1
cumulus@border02:~$ nv set interface swp2 router ospf area 1
cumulus@border02:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@border02:~$ nv set router ospf timers spf holdtime 100
cumulus@border02:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@border02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

{{< tabs "TabID828 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        type: loopback
        router:
          ospf:
            area: 0
            enable: on
      swp51:
        ip:
          address:
            10.10.10.1/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
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
        type: svi
        vlan: 10
        router:
          ospf:
            passive: on
            enable: on
            area: 0
      vlan20:
        ip:
          address:
            10.1.20.2/24: {}
        type: svi
        vlan: 20
        router:
          ospf:
            passive: on
            enable: on
            area: 0
      vlan30:
        ip:
          address:
            10.1.30.2/24: {}
        type: svi
        vlan: 30
        router:
          ospf:
            passive: on
            enable: on
            area: 0
      swp52:
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
        type: swp
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.2: {}
      peer-ip: linklocal
    bridge:
      domain:
        br_default:
          vlan:
            '10': {}
            '20': {}
            '30': {}
          untagged: 1
     vrf:
      default:
        router:
          ospf:
            router-id: 10.10.10.1
            enable: on
    router:
      ospf:
        enable: on
        timers:
          spf:
            delay: 80
            holdtime: 100
            max-holdtime: 6000
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.2/32: {}
        type: loopback
        router:
          ospf:
            area: 0
            enable: on
      swp51:
        ip:
          address:
            10.10.10.2/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
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
        type: svi
        vlan: 10
        router:
          ospf:
            area: 0
            enable: on
            passive: on
      vlan20:
        ip:
          address:
            10.1.20.2/24: {}
        type: svi
        vlan: 20
        router:
          ospf:
            area: 0
            enable: on
            passive: on
      vlan30:
        ip:
          address:
            10.1.30.2/24: {}
        type: svi
        vlan: 30
        router:
          ospf:
            area: 0
            enable: on
            passive: on
      swp52:
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
        type: swp
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.1: {}
      peer-ip: linklocal
    bridge:
      domain:
        br_default:
          vlan:
            '10': {}
            '20': {}
            '30': {}
          untagged: 1
     vrf:
      default:
        router:
          ospf:
            router-id: 10.10.10.2
            enable: on
    router:
      ospf:
        enable: on
        timers:
          spf:
            delay: 80
            holdtime: 100
            max-holdtime: 6000
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.101/32: {}
        type: loopback
        router:
          ospf:
            area: 0
            enable: on
      swp1:
        ip:
          address:
            10.10.10.101/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      swp2:
        ip:
          address:
            10.10.10.101/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      swp5:
        ip:
          address:
            10.10.10.101/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      swp6:
        ip:
          address:
            10.10.10.101/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
    vrf:
      default:
        router:
          ospf:
            router-id: 10.10.10.101
            enable: on
    router:
      ospf:
        enable: on
        timers:
          spf:
            max-holdtime: 6000
            holdtime: 100
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.102/32: {}
        type: loopback
        router:
          ospf:
            area: 0
            enable: on
      swp1:
        ip:
          address:
            10.10.10.102/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      swp2:
        ip:
          address:
            10.10.10.102/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      swp5:
        ip:
          address:
            10.10.10.102/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      swp6:
        ip:
          address:
            10.10.10.102/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
    vrf:
      default:
        router:
          ospf:
            router-id: 10.10.10.102
            enable: on
    router:
      ospf:
        enable: on
        timers:
          spf:
            max-holdtime: 6000
            holdtime: 100
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.63/32: {}
        type: loopback
        router:
          ospf:
            area: 0
            enable: on
      swp51:
        ip:
          address:
            10.10.10.63/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      swp52:
        ip:
          address:
            10.10.10.63/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
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
      swp1:
        router:
          ospf:
            area: 1
            enable: on
        type: swp
      swp2:
        router:
          ospf:
            area: 1
            enable: on
        type: swp
    mlag:
      mac-address: 44:38:39:BE:EF:FF
      backup:
        10.10.10.64: {}
      peer-ip: linklocal
    bridge:
      domain:
        br_default:
          untagged: 1
    vrf:
      default:
        router:
          ospf:
            router-id: 10.10.10.63
            enable: on
    router:
      ospf:
        enable: on
        timers:
          spf:
            max-holdtime: 6000
            holdtime: 100
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.64/32: {}
        type: loopback
        router:
          ospf:
            area: 0
            enable: on
      swp51:
        ip:
          address:
            10.10.10.64/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      swp52:
        ip:
          address:
            10.10.10.64/32: {}
        type: swp
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              hello-interval: 5
              dead-interval: 60
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
          lacp-bypass: on
        type: bond
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
        bridge:
          domain:
            br_default:
              access: 20
      vlan10:
        type: svi
        vlan: 10
        ip:
          ipv4:
            forward: off
          ipv6:
            forward: off
      vlan20:
        type: svi
        vlan: 20
        ip:
          ipv4:
            forward: off
          ipv6:
            forward: off
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
      swp1:
        router:
          ospf:
            area: 1
            enable: on
        type: swp
      swp2:
        router:
          ospf:
            area: 1
            enable: on
        type: swp
    mlag:
      mac-address: 44:38:39:BE:EF:FF
      backup:
        10.10.10.63: {}
      peer-ip: linklocal
    bridge:
      domain:
        br_default:
          untagged: 1
    vrf:
      default:
        router:
          ospf:
            router-id: 10.10.10.102
            enable: onrouter:
      ospf:
        enable: on
        timers:
          spf:
            max-holdtime: 6000
            holdtime: 100
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}
