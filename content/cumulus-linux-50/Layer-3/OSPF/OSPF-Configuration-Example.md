---
title: OSPF Configuration Example
author: NVIDIA
weight: 920
toc: 3
---
This section shows an OSPF configuration example based on the reference topology.

{{< img src = "/images/cumulus-linux/ospf-scalability-areas.png" >}}

The example configuration configures:
- OSPFv2 *unnumbered* on all leafs and spines
- [MLAG](## "Multi-chassis Link Aggregation") on leaf01 and leaf02, and on border01 and border02
- leaf01, leaf02, spine01, and spine02 in area 0
- border01 and border02 (ABRs) in area 0 and area 1

{{< tabs "TabID801 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID936 ">}}
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
cumulus@leaf01:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr mac-address 00:00:5e:00:01:00
cumulus@leaf01:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr mac-address 00:00:5e:00:01:00
cumulus@leaf01:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf01:~$ nv set interface vlan30 ip vrr mac-address 00:00:5e:00:01:00
cumulus@leaf01:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ nv set bridge domain br_default untagged 1
cumulus@leaf01:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf01:~$ nv set vrf default router ospf router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router ospf area 0 network 10.10.10.1/32
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
cumulus@leaf02:~$ nv set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:~$ nv set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:~$ nv set interface vlan30 ip address 10.1.30.3/24
cumulus@leaf02:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf02:~$ nv set interface vlan10 ip vrr mac-address 00:00:5e:00:01:00
cumulus@leaf02:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf02:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf02:~$ nv set interface vlan20 ip vrr mac-address 00:00:5e:00:01:00
cumulus@leaf02:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf02:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf02:~$ nv set interface vlan30 ip vrr mac-address 00:00:5e:00:01:00
cumulus@leaf02:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf02:~$ nv set bridge domain br_default untagged 1
cumulus@leaf02:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf02:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf02:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf02:~$ nv set vrf default router ospf router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf default router ospf area 0 network 10.10.10.2/32
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
cumulus@spine01:~$ nv set vrf default router ospf area 0 network 10.10.10.101/32
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
cumulus@spine02:~$ nv set vrf default router ospf area 0 network 10.10.10.102/32
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
cumulus@border01:~$ nv set interface bond1 bridge domain br_default access 2001
cumulus@border01:~$ nv set interface bond2 bridge domain br_default access 2001
cumulus@border01:~$ nv set interface bond1-2 bridge domain br_default
cumulus@border01:~$ nv set interface vlan2001
cumulus@border01:~$ nv set interface vlan2001 ip address 10.1.201.2/24
cumulus@border01:~$ nv set interface vlan2001 ip vrr address 10.1.201.1/24
cumulus@border01:~$ nv set interface vlan2001 ip vrr mac-address 00:00:5e:00:01:00
cumulus@border01:~$ nv set interface vlan2001 ip vrr state up
cumulus@border01:~$ nv set interface peerlink bond member swp49-50
cumulus@border01:~$ nv set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border01:~$ nv set mlag backup 10.10.10.64
cumulus@border01:~$ nv set mlag peer-ip linklocal
cumulus@border01:~$ nv set bridge domain br_default untagged 1
cumulus@border01:~$ nv set vrf default router ospf router-id 10.10.10.63
cumulus@border01:~$ nv set vrf default router ospf area 0 network 10.10.10.63/32
cumulus@border01:~$ nv set interface swp51 router ospf area 0
cumulus@border01:~$ nv set interface swp51 router ospf network-type point-to-point
cumulus@border01:~$ nv set interface swp51 router ospf timers hello-interval 5
cumulus@border01:~$ nv set interface swp51 router ospf timers dead-interval 60
cumulus@border01:~$ nv set interface swp52 router ospf area 0
cumulus@border01:~$ nv set interface swp52 router ospf network-type point-to-point
cumulus@border01:~$ nv set interface swp52 router ospf timers hello-interval 5
cumulus@border01:~$ nv set interface swp52 router ospf timers dead-interval 60
cumulus@border01:~$ nv set interface vlan2001 router ospf area 1
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
cumulus@border02:~$ nv set interface bond1 bridge domain br_default access 2001
cumulus@border02:~$ nv set interface bond2 bridge domain br_default access 2001
cumulus@border02:~$ nv set interface bond1-2 bridge domain br_default
cumulus@border02:~$ nv set interface vlan2001
cumulus@border02:~$ nv set interface vlan2001 ip address 10.1.201.3/24
cumulus@border02:~$ nv set interface vlan2001 ip vrr address 10.1.201.1/24
cumulus@border02:~$ nv set interface vlan2001 ip vrr mac-address 00:00:5e:00:01:00
cumulus@border02:~$ nv set interface vlan2001 ip vrr state up
cumulus@border02:~$ nv set interface peerlink bond member swp49-50
cumulus@border02:~$ nv set mlag mac-address 44:38:39:BE:EF:FF
cumulus@border02:~$ nv set mlag backup 10.10.10.63
cumulus@border02:~$ nv set mlag peer-ip linklocal
cumulus@border02:~$ nv set bridge domain br_default untagged 1
cumulus@border02:~$ nv set vrf default router ospf router-id 10.10.10.64
cumulus@border02:~$ nv set vrf default router ospf area 0 network 10.10.10.64/32
cumulus@border02:~$ nv set interface swp51 router ospf area 0
cumulus@border02:~$ nv set interface swp51 router ospf network-type point-to-point
cumulus@border02:~$ nv set interface swp51 router ospf timers hello-interval 5
cumulus@border02:~$ nv set interface swp51 router ospf timers dead-interval 60
cumulus@border02:~$ nv set interface swp52 router ospf area 0
cumulus@border02:~$ nv set interface swp52 router ospf network-type point-to-point
cumulus@border02:~$ nv set interface swp52 router ospf timers hello-interval 5
cumulus@border02:~$ nv set interface swp52 router ospf timers dead-interval 60
cumulus@border02:~$ nv set interface vlan2001 router ospf area 1
cumulus@border02:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@border02:~$ nv set router ospf timers spf holdtime 100
cumulus@border02:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@border02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

{{< tabs "TabID1194 ">}}
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
      swp52:
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
          vrr:
            address:
              10.1.10.1/24: {}
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
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
          vrr:
            address:
              10.1.20.1/24: {}
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
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
          vrr:
            address:
              10.1.30.1/24: {}
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        type: svi
        vlan: 30
        router:
          ospf:
            area: 0
            enable: on
            passive: on
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
            area:
              '0':
                network:
                  10.10.10.1/32: {}
    router:
      ospf:
        enable: on
        timers:
          spf:
            delay: 80
            holdtime: 100
            max-holdtime: 6000
    platform:
      hostname:
        value: leaf01
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
      swp52:
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
            10.1.10.3/24: {}
          vrr:
            address:
              10.1.10.1/24: {}
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
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
            10.1.20.3/24: {}
          vrr:
            address:
              10.1.20.1/24: {}
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
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
            10.1.30.3/24: {}
          vrr:
            address:
              10.1.30.1/24: {}
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        type: svi
        vlan: 30
        router:
          ospf:
            area: 0
            enable: on
            passive: on
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
            area:
              '0':
                network:
                  10.10.10.2/32: {}
    router:
      ospf:
        enable: on
        timers:
          spf:
            delay: 80
            holdtime: 100
            max-holdtime: 6000
    platform:
      hostname:
        value: leaf02
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
            area:
              '0':
                network:
                  10.10.10.101/32: {}
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
            area:
              '0':
                network:
                  10.10.10.102/32: {}
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
cumulus@border01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    platform:
      hostname:
        value: border01
    interface:
      lo:
        ip:
          address:
            10.10.10.63/32: {}
        type: loopback
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
              access: 2001
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
              access: 2001
      vlan2001:
        type: svi
        vlan: 2001
        ip:
          address:
            10.1.201.2/24: {}
          vrr:
            address:
              10.1.201.1/24: {}
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        router:
          ospf:
            area: 1
            enable: on
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
            area:
              '0':
                network:
                  10.10.10.63/32: {}
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
cumulus@border02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    platform:
      hostname:
        value: border02
    interface:
      lo:
        ip:
          address:
            10.10.10.64/32: {}
        type: loopback
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
              access: 2001
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
              access: 2001
      vlan2001:
        type: svi
        vlan: 2001
        ip:
          address:
            10.1.201.3/24: {}
          vrr:
            address:
              10.1.201.1/24: {}
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        router:
          ospf:
            area: 1
            enable: on
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
            router-id: 10.10.10.64
            enable: on
            area:
              '0':
                network:
                  10.10.10.64/32: {}
    router:
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
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID1899 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32

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

auto swp51
iface swp51
    address 10.10.10.1/32

auto swp52
iface swp52
    address 10.10.10.1/32

auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10

auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20

auto bond3
iface bond3
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
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180

auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:5e:00:01:00 10.1.10.1/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:5e:00:01:00 10.1.20.1/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.2/24
    address-virtual 00:00:5e:00:01:00 10.1.30.1/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 30

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10 20 30
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

auto swp51
iface swp51
    address 10.10.10.2/32

auto swp52
iface swp52
    address 10.10.10.2/32

auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10

auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20

auto bond3
iface bond3
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
    clagd-args --initDelay 180

auto vlan10
iface vlan10
    address 10.1.10.3/24
    address-virtual 00:00:5e:00:01:00 10.1.10.1/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.3/24
    address-virtual 00:00:5e:00:01:00 10.1.20.1/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.3/24
    address-virtual 00:00:5e:00:01:00 10.1.30.1/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 30

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/network/interfaces
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
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cat /etc/network/interfaces
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
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.63/32

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

auto swp51
iface swp51
    address 10.10.10.63/32

auto swp52
iface swp52
    address 10.10.10.63/32

auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 2001

auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 2001

auto vlan2001
iface vlan2001
    address 10.1.201.2/24
    address-virtual 00:00:5e:00:01:00 10.1.201.1/24
    hwaddress 44:38:39:22:01:ab
    vlan-raw-device br_default
    vlan-id 2001

auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no

auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.64
    clagd-sys-mac 44:38:39:BE:EF:FF
    clagd-args --initDelay 180

auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink
    hwaddress 44:38:39:22:01:ab
    bridge-vlan-aware yes
    bridge-vids 1
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

auto swp51
iface swp51
    address 10.10.10.64/32

auto swp52
iface swp52
    address 10.10.10.64/32

auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 2001

auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 2001

auto vlan2001
iface vlan2001
    address 10.1.201.3/24
    address-virtual 00:00:5e:00:01:00 10.1.201.1/24
    hwaddress 44:38:39:22:01:b3
    vlan-raw-device br_default
    vlan-id 2001

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
    clagd-args --initDelay 180

auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink
    hwaddress 44:38:39:22:01:b3
    bridge-vlan-aware yes
    bridge-vids 1
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID2357 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
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
router ospf
passive-interface vlan10
interface vlan20
ip ospf area 0
router ospf
passive-interface vlan20
interface vlan30
ip ospf area 0
router ospf
passive-interface vlan30
vrf default
exit-vrf
vrf mgmt
exit-vrf
router ospf
ospf router-id 10.10.10.1
network 10.10.10.1/32 area 0
timers throttle spf 80 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
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
router ospf
passive-interface vlan10
interface vlan20
ip ospf area 0
router ospf
passive-interface vlan20
interface vlan30
ip ospf area 0
router ospf
passive-interface vlan30
vrf default
exit-vrf
vrf mgmt
exit-vrf
router ospf
ospf router-id 10.10.10.2
network 10.10.10.2/32 area 0
timers throttle spf 80 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
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
vrf default
exit-vrf
vrf mgmt
exit-vrf
router ospf
ospf router-id 10.10.10.101
network 10.10.10.101/32 area 0
timers throttle spf 0 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
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
vrf default
exit-vrf
vrf mgmt
exit-vrf
router ospf
ospf router-id 10.10.10.102
network 10.10.10.102/32 area 0
timers throttle spf 0 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf
...
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
interface vlan2001
ip ospf area 1
vrf default
exit-vrf
vrf mgmt
exit-vrf
router ospf
ospf router-id 10.10.10.63
network 10.10.10.63/32 area 0
timers throttle spf 0 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/frr/frr.conf
...
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
interface vlan2001
ip ospf area 1
vrf default
exit-vrf
vrf mgmt
exit-vrf
router ospf
ospf router-id 10.10.10.64
network 10.10.10.64/32 area 0
timers throttle spf 0 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}
