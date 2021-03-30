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

## /etc/network/interfaces

{{< tabs "TabID901 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.1/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto bridge
iface bridge
    bridge-ports peerlink bond1 bond2 bond3
    bridge-vids 10 20 30
    bridge-vlan-aware yes

auto vlan10
iface vlan10
    address 10.1.10.2/24
    vlan-raw-device bridge
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.2/24
    vlan-raw-device bridge
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.2/24
    vlan-raw-device bridge
    vlan-id 30

auto swp51
iface swp51
    alias leaf to spine
    address 10.10.10.1/32

auto swp52
iface swp52
    alias leaf to spine
     address 10.10.10.1/32

auto swp49
iface swp49
    alias peerlink

auto swp50
iface swp50
    alias peerlink

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:AA

auto swp1
iface swp1
    alias bond member of bond1
    mtu 9000

auto bond1
iface bond1
    alias bond1 on swp1
    mtu 9000
    clag-id 1
    bridge-access 10
    bond-slaves swp1
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp2
iface swp2
    alias bond member of bond2
    mtu 9000

auto bond2
iface bond2
    alias bond2 on swp2
    mtu 9000
    clag-id 2
    bridge-access 20
    bond-slaves swp2
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp3
iface swp3
    alias bond member of bond3
    mtu 9000

auto bond3
iface bond3
    alias bond3 on swp3
    mtu 9000
    clag-id 3
    bridge-access 30
    bond-slaves swp3
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
```

{{< /tab >}}

{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.2/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto bridge
iface bridge
    bridge-ports peerlink bond1 bond2 bond3
    bridge-vids 10 20 30
    bridge-vlan-aware yes

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

auto swp51
iface swp51
    alias leaf to spine
    address 10.10.10.2/32

auto swp52
iface swp52
    alias leaf to spine
    address 10.10.10.2/32

auto swp49
iface swp49
    alias peerlink

auto swp50
iface swp50
    alias peerlink

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.1
    clagd-peer-ip linklocal
    clagd-priority 32768
    clagd-sys-mac 44:38:39:BE:EF:AA

auto swp1
iface swp1
    alias bond member of bond1
    mtu 9000

auto bond1
iface bond1
    alias bond1 on swp1
    mtu 9000
    clag-id 1
    bridge-access 10
    bond-slaves swp1
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp2
iface swp2
    alias bond member of bond2
    mtu 9000

auto bond2
iface bond2
    alias bond2 on swp2
    mtu 9000
    clag-id 2
    bridge-access 20
    bond-slaves swp2
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp3
iface swp3
    alias bond member of bond3
    mtu 9000

auto bond3
iface bond3
    alias bond3 on swp3
    mtu 9000
    clag-id 3
    bridge-access 30
    bond-slaves swp3
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
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
    alias leaf to spine
    address 10.10.10.101/32

auto swp2
iface swp2
    alias leaf to spine
    address 10.10.10.101/32

auto swp5
iface swp5
    alias leaf to spine
    address 10.10.10.101/32

auto swp6
iface swp6
    alias leaf to spine
    address 10.10.10.101/32
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
    alias leaf to spine
    address 10.10.10.102/32

auto swp2
iface swp2
    alias leaf to spine
    address 10.10.10.102/32

auto swp5
iface swp5
    alias leaf to spine
    address 10.10.10.102/32

auto swp6
iface swp6
    alias leaf to spine
    address 10.10.10.102/32
```

{{< /tab >}}

{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.63/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128


auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto bridge
iface bridge
    bridge-ports peerlink bond1 bond2
    bridge-vlan-aware yes

auto swp51
iface swp51
    alias leaf to spine
    address 10.10.10.63/32

auto swp52
iface swp52
    alias leaf to spine
    address 10.10.10.63/32

auto swp49
iface swp49
    alias peerlink

auto swp50
iface swp50
    alias peerlink

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.64
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:FF

auto swp1
iface swp1
    alias bond member of bond1
    mtu 9000

auto bond1
iface bond1
    alias bond1 on swp1
    mtu 9000
    clag-id 1
    bridge-access 10
    bond-slaves swp1
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp2
iface swp2
    alias bond member of bond2
    mtu 9000

auto bond2
iface bond2
    alias bond2 on swp2
    mtu 9000
    clag-id 2
    bridge-access 20
    bond-slaves swp2
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
```

{{< /tab >}}

{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.64/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto bridge
iface bridge
    bridge-ports peerlink bond1 bond2
    bridge-vids 10 20  
    bridge-vlan-aware yes

auto vlan10
iface vlan10
    vlan-raw-device bridge
    vlan-id 10
    ip-forward off
    ip6-forward off

auto vlan20
iface vlan20
    vlan-raw-device bridge
    vlan-id 20
    ip-forward off
    ip6-forward off

auto swp51
iface swp51
    alias leaf to spine
    address 10.10.10.64/32

auto swp52
iface swp52
    alias leaf to spine
    address 10.10.10.64/32

auto swp49
iface swp49
    alias peerlink

auto swp50
iface swp50
    alias peerlink

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.63
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:FF

auto swp1
iface swp1
    alias bond member of bond1
    mtu 9000

auto bond1
iface bond1
    alias bond1 on swp1
    mtu 9000
    clag-id 1
    bridge-access 10
    bond-slaves swp1
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp2
iface swp2
    alias bond member of bond2
    mtu 9000

auto bond2
iface bond2
    alias bond2 on swp2
    mtu 9000
    clag-id 2
    bridge-access 20
    bond-slaves swp2
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
```

{{< /tab >}}

{{< /tabs >}}

## /etc/frr/frr.conf

{{< tabs "TabID944 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!
interface lo
 ip ospf area 0
!
interface vlan10
  ip ospf area 0
!
interface vlan20
  ip ospf area 0
!
interface vlan30
  ip ospf area 0
!
interface swp51
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
interface swp52
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
router ospf
 ospf router-id 10.10.10.1
 passive-interface vlan10
 passive-interface vlan20
 passive-interface vlan30
 timers throttle spf 80 100 6000
!
```

{{< /tab >}}

{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!
interface lo
 ip ospf area 0
!
interface vlan10
  ip ospf area 0
!
interface vlan20
  ip ospf area 0
!
interface vlan30
  ip ospf area 0
!
interface swp51
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
interface swp52
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
router ospf
 ospf router-id 10.10.10.2
 passive-interface vlan10
 passive-interface vlan20
 passive-interface vlan30
 timers throttle spf 80 100 6000
!
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!
interface lo
 ip ospf area 0
!
interface swp1
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
interface swp2
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
interface swp5
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
interface swp6
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
router ospf
 ospf router-id 10.10.10.101
 timers throttle spf 80 100 6000
!
```

{{< /tab >}}

{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!
interface lo
 ip ospf area 0
!
interface swp1
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
!
interface swp2
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
interface swp5
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
interface swp6
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
router ospf
 ospf router-id 10.10.10.102
 timers throttle spf 80 100 6000
!
```

{{< /tab >}}

{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!
interface lo
 ip ospf area 0

interface swp1
 ip ospf area 1
!
interface swp2
 ip ospf area 1
!
interface swp51
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
interface swp52
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
router ospf
 ospf router-id 10.10.10.63
 area 0 range 172.16.1.0/24
 timers throttle spf 80 100 6000
```

{{< /tab >}}

{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!
interface lo
 ip ospf area 0

interface swp1
 ip ospf area 1
!
interface swp2
 ip ospf area 1
!
interface swp51
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
interface swp52
 ip ospf area 0
 ip ospf network point-to-point
 ip ospf hello-interval 5
 ip ospf dead-interval 60
!
router ospf
 ospf router-id 10.10.10.64
 area 0 range 172.16.1.0/24
 timers throttle spf 80 100 6000
```

{{< /tab >}}

{{< /tabs >}}
