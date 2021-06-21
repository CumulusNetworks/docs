---
title: Configuration Example
author: NVIDIA
weight: 880
toc: 3
---
This section shows a BGP configuration example based on the reference topology. The example configures BGP *unnumbered* on all leafs and spines and uses the peer group *underlay*. MLAG is configured on leaf01 and leaf02, and on leaf03 and leaf04.
<!-- laclac: Showing these underlying Linux files is going to be tricky with CUE as the CUE rendered files will not be the same as in the past. CUE exposes the single CUE config file and should leave viewing/manipulating these Linux files to the SuperUser.  How do we manage this in the docs?   -->

<!-- AniaR:We will show the CUE commands required to configure the example -->

{{< img src = "/images/cumulus-linux/mlag-config-peering.png" >}}

## /etc/network/interfaces

{{< tabs "TabID901 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/network/interfaces
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

auto swp52
iface swp52
    alias leaf to spine

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
cumulus@leaf02:~$ cat /etc/network/interfaces
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

auto swp52
iface swp52
    alias leaf to spine

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

{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.3/32

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
    bridge-vids 40 50 60
    bridge-vlan-aware yes

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

auto swp51
iface swp51
    alias leaf to spine

auto swp52
iface swp52
    alias leaf to spine

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
    clagd-backup-ip 10.10.10.4
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:BB

auto swp1
iface swp1
    alias bond member of bond1
    mtu 9000

auto bond1
iface bond1
    alias bond1 on swp1
    mtu 9000
    clag-id 1
    bridge-access 40
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
    bridge-access 50
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
    bridge-access 60
    bond-slaves swp3
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
```

{{< /tab >}}

{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.4/32

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
    bridge-vids 40 50 60
    bridge-vlan-aware yes

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

auto swp51
iface swp51
    alias leaf to spine

auto swp52
iface swp52
    alias leaf to spine

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
    clagd-backup-ip 10.10.10.3
    clagd-peer-ip linklocal
    clagd-priority 32768
    clagd-sys-mac 44:38:39:BE:EF:BB

auto swp1
iface swp1
    alias bond member of bond1
    mtu 9000

auto bond1
iface bond1
    alias bond1 on swp1
    mtu 9000
    clag-id 1
    bridge-access 40
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
    bridge-access 50
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
    bridge-access 60
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

auto swp2
iface swp2
    alias leaf to spine

auto swp3
iface swp3
    alias leaf to spine

auto swp4
iface swp4
    alias leaf to spine
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

auto swp2
iface swp2
    alias leaf to spine

auto swp3
iface swp3
    alias leaf to spine

auto swp4
iface swp4
    alias leaf to spine
```

{{< /tab >}}

{{< /tabs >}}

## /etc/frr/frr.conf

{{< tabs "TabID944 ">}}

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
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
line vty
```

{{< /tab >}}

{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf
...
log syslog informational
!
router bgp 65101
 bgp router-id 10.10.10.2
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
line vty
```

{{< /tab >}}

{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf
...
log syslog informational
!
router bgp 65102
 bgp router-id 10.10.10.3
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
line vty
```

{{< /tab >}}

{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf
...
log syslog informational
!
router bgp 65102
 bgp router-id 10.10.10.4
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
line vty
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/frr/frr.conf
...
log syslog informational
!
router bgp 65199
 bgp router-id 10.10.10.101
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
line vty
```

{{< /tab >}}

{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cat /etc/frr/frr.conf
...
log syslog informational
!
router bgp 65199
 bgp router-id 10.10.10.102
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
line vty
```

{{< /tab >}}

{{< /tabs >}}
