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
- <span class="a-tooltip">[MLAG](## "Multi-chassis Link Aggregation")</span> on leaf01 and leaf02, and on border01 and border02
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
cumulus@leaf01:~$ nv set mlag mac-address 44:38:39:FF:00:AA
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
cumulus@leaf02:~$ nv set mlag mac-address 44:38:39:FF:00:AA
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
cumulus@border01:~$ nv set interface bond1 bridge domain br_default access 2001
cumulus@border01:~$ nv set interface bond2 bridge domain br_default access 2001
cumulus@border01:~$ nv set interface bond1-2 bridge domain br_default
cumulus@border01:~$ nv set interface vlan2001
cumulus@border01:~$ nv set interface vlan2001 ip address 10.1.201.2/24
cumulus@border01:~$ nv set interface vlan2001 ip vrr address 10.1.201.1/24
cumulus@border01:~$ nv set interface vlan2001 ip vrr mac-address 00:00:5e:00:01:00
cumulus@border01:~$ nv set interface vlan2001 ip vrr state up
cumulus@border01:~$ nv set interface peerlink bond member swp49-50
cumulus@border01:~$ nv set mlag mac-address 44:38:39:FF:00:FF
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
cumulus@border02:~$ nv set mlag mac-address 44:38:39:FF:00:FF
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
    bridge:
      domain:
        br_default:
          untagged: 1
          vlan:
            10,20,30: {}
    interface:
      bond1:
        bond:
          lacp-bypass: on
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default:
              access: 10
        type: bond
      bond2:
        bond:
          lacp-bypass: on
          member:
            swp2: {}
          mlag:
            enable: on
            id: 2
        bridge:
          domain:
            br_default:
              access: 20
        type: bond
      bond3:
        bond:
          lacp-bypass: on
          member:
            swp3: {}
          mlag:
            enable: on
            id: 3
        bridge:
          domain:
            br_default:
              access: 30
        type: bond
      eth0:
        ip:
          address:
            dhcp: {}
          vrf: mgmt
        type: eth
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        type: loopback
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        base-interface: peerlink
        type: sub
        vlan: 4094
      swp51:
        ip:
          address:
            10.10.10.1/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      swp52:
        ip:
          address:
            10.10.10.1/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      vlan10:
        ip:
          address:
            10.1.10.2/24: {}
          vrr:
            address:
              10.1.10.1/24: {}
            enable: on
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        router:
          ospf:
            area: 0
            enable: on
            passive: on
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.2/24: {}
          vrr:
            address:
              10.1.20.1/24: {}
            enable: on
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        router:
          ospf:
            area: 0
            enable: on
            passive: on
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.2/24: {}
          vrr:
            address:
              10.1.30.1/24: {}
            enable: on
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        router:
          ospf:
            area: 0
            enable: on
            passive: on
        type: svi
        vlan: 30
    mlag:
      backup:
        10.10.10.2: {}
      enable: on
      init-delay: 5
      mac-address: 44:38:39:FF:00:AA
      peer-ip: linklocal
    router:
      ospf:
        enable: on
        timers:
          spf:
            delay: 80
            holdtime: 100
            max-holdtime: 6000
      vrr:
        enable: on
    service:
      ntp:
        mgmt:
          server:
            0.cumulusnetworks.pool.ntp.org: {}
            1.cumulusnetworks.pool.ntp.org: {}
            2.cumulusnetworks.pool.ntp.org: {}
            3.cumulusnetworks.pool.ntp.org: {}
    system:
      aaa:
        class:
          nvapply:
            action: allow
            command-path:
              /:
                permission: all
          nvshow:
            action: allow
            command-path:
              /:
                permission: ro
          sudo:
            action: allow
            command-path:
              /:
                permission: all
        role:
          nvue-admin:
            class:
              nvapply: {}
          nvue-monitor:
            class:
              nvshow: {}
          system-admin:
            class:
              nvapply: {}
              sudo: {}
        user:
          cumulus:
            full-name: cumulus,,,
            hashed-password: $6$LVtX8JO1GJbiiVfq$Lqn/7MDaxbfgkKbDETAB.2sPuqvXJxGFnldbuJqMUBqczlMM1nNTrV5Kld7KwBvAkky6vJlQziYPqJS/ge88n.
            role: system-admin
      api:
        state: enabled
      config:
        auto-save:
          enable: on
      control-plane:
        acl:
          acl-default-dos:
            inbound: {}
          acl-default-whitelist:
            inbound: {}
      global:
        system-mac: 44:38:39:22:01:7a
      hostname: leaf01
      reboot:
        mode: cold
      ssh-server:
        state: enabled
      wjh:
        channel:
          forwarding:
            trigger:
              l2: {}
              l3: {}
              tunnel: {}
        enable: on
    vrf:
      default:
        router:
          ospf:
            area:
              '0':
                network:
                  10.10.10.1/32: {}
            enable: on
            router-id: 10.10.10.1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    bridge:
      domain:
        br_default:
          untagged: 1
          vlan:
            10,20,30: {}
    interface:
      bond1:
        bond:
          lacp-bypass: on
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default:
              access: 10
        type: bond
      bond2:
        bond:
          lacp-bypass: on
          member:
            swp2: {}
          mlag:
            enable: on
            id: 2
        bridge:
          domain:
            br_default:
              access: 20
        type: bond
      bond3:
        bond:
          lacp-bypass: on
          member:
            swp3: {}
          mlag:
            enable: on
            id: 3
        bridge:
          domain:
            br_default:
              access: 30
        type: bond
      eth0:
        ip:
          address:
            dhcp: {}
          vrf: mgmt
        type: eth
      lo:
        ip:
          address:
            10.10.10.2/32: {}
        type: loopback
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        base-interface: peerlink
        type: sub
        vlan: 4094
      swp51:
        ip:
          address:
            10.10.10.2/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      swp52:
        ip:
          address:
            10.10.10.2/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      vlan10:
        ip:
          address:
            10.1.10.3/24: {}
          vrr:
            address:
              10.1.10.1/24: {}
            enable: on
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        router:
          ospf:
            area: 0
            enable: on
            passive: on
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.3/24: {}
          vrr:
            address:
              10.1.20.1/24: {}
            enable: on
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        router:
          ospf:
            area: 0
            enable: on
            passive: on
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.3/24: {}
          vrr:
            address:
              10.1.30.1/24: {}
            enable: on
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        router:
          ospf:
            area: 0
            enable: on
            passive: on
        type: svi
        vlan: 30
    mlag:
      backup:
        10.10.10.1: {}
      enable: on
      init-delay: 5
      mac-address: 44:38:39:FF:00:AA
      peer-ip: linklocal
    router:
      ospf:
        enable: on
        timers:
          spf:
            delay: 80
            holdtime: 100
            max-holdtime: 6000
      vrr:
        enable: on
    service:
      ntp:
        mgmt:
          server:
            0.cumulusnetworks.pool.ntp.org: {}
            1.cumulusnetworks.pool.ntp.org: {}
            2.cumulusnetworks.pool.ntp.org: {}
            3.cumulusnetworks.pool.ntp.org: {}
    system:
      aaa:
        class:
          nvapply:
            action: allow
            command-path:
              /:
                permission: all
          nvshow:
            action: allow
            command-path:
              /:
                permission: ro
          sudo:
            action: allow
            command-path:
              /:
                permission: all
        role:
          nvue-admin:
            class:
              nvapply: {}
          nvue-monitor:
            class:
              nvshow: {}
          system-admin:
            class:
              nvapply: {}
              sudo: {}
        user:
          cumulus:
            full-name: cumulus,,,
            hashed-password: $6$VYY4ykwe0LrdedRG$MNfa/eX7COUh57bGG2pZJROnvBWDfOQCnowaOiuKumvVyno/4fvWbEMEbaACLqsAQMGw5SYtgtTn.5WU5USFo.
            role: system-admin
      api:
        state: enabled
      config:
        auto-save:
          enable: on
      control-plane:
        acl:
          acl-default-dos:
            inbound: {}
          acl-default-whitelist:
            inbound: {}
      global:
        system-mac: 44:38:39:22:01:78
      hostname: leaf02
      reboot:
        mode: cold
      ssh-server:
        state: enabled
      wjh:
        channel:
          forwarding:
            trigger:
              l2: {}
              l3: {}
              tunnel: {}
        enable: on
    vrf:
      default:
        router:
          ospf:
            area:
              '0':
                network:
                  10.10.10.2/32: {}
            enable: on
            router-id: 10.10.10.2
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      eth0:
        ip:
          address:
            dhcp: {}
          vrf: mgmt
        type: eth
      lo:
        ip:
          address:
            10.10.10.101/32: {}
        type: loopback
      swp1:
        ip:
          address:
            10.10.10.101/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      swp2:
        ip:
          address:
            10.10.10.101/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      swp5:
        ip:
          address:
            10.10.10.101/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      swp6:
        ip:
          address:
            10.10.10.101/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
    router:
      ospf:
        enable: on
        timers:
          spf:
            holdtime: 100
            max-holdtime: 6000
    service:
      ntp:
        mgmt:
          server:
            0.cumulusnetworks.pool.ntp.org: {}
            1.cumulusnetworks.pool.ntp.org: {}
            2.cumulusnetworks.pool.ntp.org: {}
            3.cumulusnetworks.pool.ntp.org: {}
    system:
      aaa:
        class:
          nvapply:
            action: allow
            command-path:
              /:
                permission: all
          nvshow:
            action: allow
            command-path:
              /:
                permission: ro
          sudo:
            action: allow
            command-path:
              /:
                permission: all
        role:
          nvue-admin:
            class:
              nvapply: {}
          nvue-monitor:
            class:
              nvshow: {}
          system-admin:
            class:
              nvapply: {}
              sudo: {}
        user:
          cumulus:
            full-name: cumulus,,,
            hashed-password: $6$m.snt3F/unawCsit$8frw1.klD4wdYPMjb/chqYLihsDvjLtoT2913fZ/3p9vZfXRsAkcjV0O2mpOoLrvrM2uZlLIYVgxqoHZH7c6t/
            role: system-admin
      api:
        state: enabled
      config:
        auto-save:
          enable: on
      control-plane:
        acl:
          acl-default-dos:
            inbound: {}
          acl-default-whitelist:
            inbound: {}
      global:
        system-mac: 44:38:39:22:01:82
      hostname: spine01
      reboot:
        mode: cold
      ssh-server:
        state: enabled
      wjh:
        channel:
          forwarding:
            trigger:
              l2: {}
              l3: {}
              tunnel: {}
        enable: on
    vrf:
      default:
        router:
          ospf:
            area:
              '0':
                network:
                  10.10.10.101/32: {}
            enable: on
            router-id: 10.10.10.101
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      eth0:
        ip:
          address:
            dhcp: {}
          vrf: mgmt
        type: eth
      lo:
        ip:
          address:
            10.10.10.102/32: {}
        type: loopback
      swp1:
        ip:
          address:
            10.10.10.102/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      swp2:
        ip:
          address:
            10.10.10.102/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      swp5:
        ip:
          address:
            10.10.10.102/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      swp6:
        ip:
          address:
            10.10.10.102/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
    router:
      ospf:
        enable: on
        timers:
          spf:
            holdtime: 100
            max-holdtime: 6000
    service:
      ntp:
        mgmt:
          server:
            0.cumulusnetworks.pool.ntp.org: {}
            1.cumulusnetworks.pool.ntp.org: {}
            2.cumulusnetworks.pool.ntp.org: {}
            3.cumulusnetworks.pool.ntp.org: {}
    system:
      aaa:
        class:
          nvapply:
            action: allow
            command-path:
              /:
                permission: all
          nvshow:
            action: allow
            command-path:
              /:
                permission: ro
          sudo:
            action: allow
            command-path:
              /:
                permission: all
        role:
          nvue-admin:
            class:
              nvapply: {}
          nvue-monitor:
            class:
              nvshow: {}
          system-admin:
            class:
              nvapply: {}
              sudo: {}
        user:
          cumulus:
            full-name: cumulus,,,
            hashed-password: $6$UWQi/FawiF0WBP.8$zlLS2.FiUHsZ37L6v/8MmV9W0CVjdbyn4PSDwm5Cr6Ct02EtvAihYXgUy9owXAx0jQYIm2XbKBunxN6VpEr4X1
            role: system-admin
      api:
        state: enabled
      config:
        auto-save:
          enable: on
      control-plane:
        acl:
          acl-default-dos:
            inbound: {}
          acl-default-whitelist:
            inbound: {}
      global:
        system-mac: 44:38:39:22:01:92
      hostname: spine02
      reboot:
        mode: cold
      ssh-server:
        state: enabled
      wjh:
        channel:
          forwarding:
            trigger:
              l2: {}
              l3: {}
              tunnel: {}
        enable: on
    vrf:
      default:
        router:
          ospf:
            area:
              '0':
                network:
                  10.10.10.102/32: {}
            enable: on
            router-id: 10.10.10.102
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    bridge:
      domain:
        br_default:
          untagged: 1
          vlan:
            '2001': {}
    interface:
      bond1:
        bond:
          lacp-bypass: on
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default:
              access: 2001
        type: bond
      bond2:
        bond:
          lacp-bypass: on
          member:
            swp2: {}
          mlag:
            enable: on
            id: 2
        bridge:
          domain:
            br_default:
              access: 2001
        type: bond
      eth0:
        ip:
          address:
            dhcp: {}
          vrf: mgmt
        type: eth
      lo:
        ip:
          address:
            10.10.10.63/32: {}
        type: loopback
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        base-interface: peerlink
        type: sub
        vlan: 4094
      swp51:
        ip:
          address:
            10.10.10.63/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      swp52:
        ip:
          address:
            10.10.10.63/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      vlan2001:
        ip:
          address:
            10.1.201.2/24: {}
          vrr:
            address:
              10.1.201.1/24: {}
            enable: on
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        router:
          ospf:
            area: 1
            enable: on
        type: svi
        vlan: 2001
    mlag:
      backup:
        10.10.10.64: {}
      enable: on
      init-delay: 5
      mac-address: 44:38:39:FF:00:FF
      peer-ip: linklocal
    router:
      ospf:
        enable: on
        timers:
          spf:
            holdtime: 100
            max-holdtime: 6000
      vrr:
        enable: on
    service:
      ntp:
        mgmt:
          server:
            0.cumulusnetworks.pool.ntp.org: {}
            1.cumulusnetworks.pool.ntp.org: {}
            2.cumulusnetworks.pool.ntp.org: {}
            3.cumulusnetworks.pool.ntp.org: {}
    system:
      aaa:
        class:
          nvapply:
            action: allow
            command-path:
              /:
                permission: all
          nvshow:
            action: allow
            command-path:
              /:
                permission: ro
          sudo:
            action: allow
            command-path:
              /:
                permission: all
        role:
          nvue-admin:
            class:
              nvapply: {}
          nvue-monitor:
            class:
              nvshow: {}
          system-admin:
            class:
              nvapply: {}
              sudo: {}
        user:
          cumulus:
            full-name: cumulus,,,
            hashed-password: $6$siKWEoNyDqJpzgTg$kjQ12uQTIHRnsbF0hYbbPfRP6PRuCSk66Q79KHKEJVcx.raueCfL3hiW4FxqgDBOxWxLTC.U8fYeASiKvBS7A0
            role: system-admin
      api:
        state: enabled
      config:
        auto-save:
          enable: on
      control-plane:
        acl:
          acl-default-dos:
            inbound: {}
          acl-default-whitelist:
            inbound: {}
      global:
        system-mac: 44:38:39:22:01:74
      hostname: border01
      reboot:
        mode: cold
      ssh-server:
        state: enabled
      wjh:
        channel:
          forwarding:
            trigger:
              l2: {}
              l3: {}
              tunnel: {}
        enable: on
    vrf:
      default:
        router:
          ospf:
            area:
              '0':
                network:
                  10.10.10.63/32: {}
            enable: on
            router-id: 10.10.10.63
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    bridge:
      domain:
        br_default:
          untagged: 1
          vlan:
            '2001': {}
    interface:
      bond1:
        bond:
          lacp-bypass: on
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default:
              access: 2001
        type: bond
      bond2:
        bond:
          lacp-bypass: on
          member:
            swp2: {}
          mlag:
            enable: on
            id: 2
        bridge:
          domain:
            br_default:
              access: 2001
        type: bond
      eth0:
        ip:
          address:
            dhcp: {}
          vrf: mgmt
        type: eth
      lo:
        ip:
          address:
            10.10.10.64/32: {}
        type: loopback
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        base-interface: peerlink
        type: sub
        vlan: 4094
      swp51:
        ip:
          address:
            10.10.10.64/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      swp52:
        ip:
          address:
            10.10.10.64/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point
            timers:
              dead-interval: 60
              hello-interval: 5
        type: swp
      vlan2001:
        ip:
          address:
            10.1.201.3/24: {}
          vrr:
            address:
              10.1.201.1/24: {}
            enable: on
            mac-address: 00:00:5e:00:01:00
            state:
              up: {}
        router:
          ospf:
            area: 1
            enable: on
        type: svi
        vlan: 2001
    mlag:
      backup:
        10.10.10.63: {}
      enable: on
      init-delay: 5
      mac-address: 44:38:39:FF:00:FF
      peer-ip: linklocal
    router:
      ospf:
        enable: on
        timers:
          spf:
            holdtime: 100
            max-holdtime: 6000
      vrr:
        enable: on
    service:
      ntp:
        mgmt:
          server:
            0.cumulusnetworks.pool.ntp.org: {}
            1.cumulusnetworks.pool.ntp.org: {}
            2.cumulusnetworks.pool.ntp.org: {}
            3.cumulusnetworks.pool.ntp.org: {}
    system:
      aaa:
        class:
          nvapply:
            action: allow
            command-path:
              /:
                permission: all
          nvshow:
            action: allow
            command-path:
              /:
                permission: ro
          sudo:
            action: allow
            command-path:
              /:
                permission: all
        role:
          nvue-admin:
            class:
              nvapply: {}
          nvue-monitor:
            class:
              nvshow: {}
          system-admin:
            class:
              nvapply: {}
              sudo: {}
        user:
          cumulus:
            full-name: cumulus,,,
            hashed-password: $6$tJNymcft48141Lz5$cEJBzLJTIQSgIIPOLRSLFPgVPR0QkBUXY1pVAPraVuatKWGS9s.AdUZCd0ayHqgCfwvYyECf9e93VYkdl4wgM0
            role: system-admin
      api:
        state: enabled
      config:
        auto-save:
          enable: on
      control-plane:
        acl:
          acl-default-dos:
            inbound: {}
          acl-default-whitelist:
            inbound: {}
      global:
        system-mac: 44:38:39:22:01:7c
      hostname: border02
      reboot:
        mode: cold
      ssh-server:
        state: enabled
      wjh:
        channel:
          forwarding:
            trigger:
              l2: {}
              l3: {}
              tunnel: {}
        enable: on
    vrf:
      default:
        router:
          ospf:
            area:
              '0':
                network:
                  10.10.10.64/32: {}
            enable: on
            router-id: 10.10.10.64
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
    clagd-sys-mac 44:38:39:FF:00:AA
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
    clagd-sys-mac 44:38:39:FF:00:AA
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
    clagd-sys-mac 44:38:39:FF:00:FF
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
    clagd-sys-mac 44:38:39:FF:00:FF
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
timers throttle spf 80 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
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
timers throttle spf 80 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
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
vrf default
exit-vrf
vrf mgmt
exit-vrf
router ospf
ospf router-id 10.10.10.101
timers throttle spf 0 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
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
vrf default
exit-vrf
vrf mgmt
exit-vrf
router ospf
ospf router-id 10.10.10.102
timers throttle spf 0 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf
...
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
interface vlan2001
ip ospf area 1
vrf default
exit-vrf
vrf mgmt
exit-vrf
router ospf
ospf router-id 10.10.10.63
timers throttle spf 0 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< tab "border02 ">}}

```
cumulus@border02:~$ sudo cat /etc/frr/frr.conf
...
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
interface vlan2001
ip ospf area 1
vrf default
exit-vrf
vrf mgmt
exit-vrf
router ospf
ospf router-id 10.10.10.64
timers throttle spf 0 100 6000
! end of router ospf block
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Try It " >}}
    {{< simulation name="Try It CL510 - OSPFv2" showNodes="leaf01,leaf02,spine01,spine02,border01,border02,server01,server02,server03,server07,server08" >}}

The simulation starts with the example OSPF configuration. The demo is pre-configured using {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/" text="NVUE">}} commands.

To validate the configuration, run the commands listed in the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/OSPF/Open-Shortest-Path-First-v2-OSPFv2/#troubleshooting" text="Troubleshooting">}} section.

{{< /tab >}}
{{< /tabs >}}
