---
title: Configuration Example
author: NVIDIA
weight: 880
toc: 3
---
This section shows a BGP configuration example based on the reference topology. The example configures BGP *unnumbered* on all leafs and spines. MLAG is configured on leaf01 and leaf02, and on leaf03 and leaf04.

{{< img src = "/images/cumulus-linux/mlag-config-peering.png" >}}

## Commands

{{< tabs "TabID11 ">}}
{{< tab "NCLU ">}}

{{< tabs "TabID14 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@leaf01:~$ net add bond bond1 bond slaves swp1
cumulus@leaf01:~$ net add bond bond2 bond slaves swp2
cumulus@leaf01:~$ net add bond bond3 bond slaves swp3
cumulus@leaf01:~$ net add bond bond1 clag id 1
cumulus@leaf01:~$ net add bond bond2 clag id 2
cumulus@leaf01:~$ net add bond bond3 clag id 2
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
cumulus@leaf02:~$ net add bond bond3 clag id 2
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
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
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
cumulus@leaf03:~$ net add bond bond3 clag id 2
cumulus@leaf03:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf03:~$ net add clag peer sys-mac 44:38:39:BE:EF:AA interface swp49-50 primary backup-ip 10.10.10.4
cumulus@leaf03:~$ net add vlan 40 ip address 10.1.40.4/24
cumulus@leaf03:~$ net add vlan 50 ip address 10.1.50.4/24
cumulus@leaf03:~$ net add vlan 60 ip address 10.1.60.5/24
cumulus@leaf03:~$ net add bridge bridge vids 40,50,60
cumulus@leaf03:~$ net add bridge bridge pvid 1
cumulus@leaf03:~$ net add bgp autonomous-system 65103
cumulus@leaf03:~$ net add bgp router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf03:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf03:~$ net add bgp ipv4 unicast network 10.10.10.3/32
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ net add loopback lo ip address 10.10.10.4/32
cumulus@leaf03:~$ net add bond bond1 bond slaves swp1
cumulus@leaf03:~$ net add bond bond2 bond slaves swp2
cumulus@leaf03:~$ net add bond bond3 bond slaves swp3
cumulus@leaf03:~$ net add bond bond1 clag id 1
cumulus@leaf03:~$ net add bond bond2 clag id 2
cumulus@leaf03:~$ net add bond bond3 clag id 2
cumulus@leaf03:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf03:~$ net add clag peer sys-mac 44:38:39:BE:EF:AA interface swp49-50 primary backup-ip 10.10.10.3
cumulus@leaf03:~$ net add vlan 40 ip address 10.1.40.6/24
cumulus@leaf03:~$ net add vlan 50 ip address 10.1.50.6/24
cumulus@leaf03:~$ net add vlan 60 ip address 10.1.60.6/24
cumulus@leaf03:~$ net add bridge bridge vids 40,50,60
cumulus@leaf03:~$ net add bridge bridge pvid 1
cumulus@leaf03:~$ net add bgp autonomous-system 65103
cumulus@leaf03:~$ net add bgp router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf04:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf03:~$ net add bgp ipv4 unicast network 10.10.10.101/32
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
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
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
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
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "CUE ">}}

{{< tabs "TabID38 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ cl set interface bond1 bond member swp1
cumulus@leaf01:~$ cl set interface bond2 bond member swp2
cumulus@leaf01:~$ cl set interface bond3 bond member swp3
cumulus@leaf01:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf01:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf01:~$ cl set interface bond3 bond mlag id 3
cumulus@leaf01:~$ cl set interface bond1-3 bridge domain br_default 
cumulus@leaf01:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf01:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ cl set mlag backup 10.10.10.2
cumulus@leaf01:~$ cl set mlag peer-ip linklocal
cumulus@leaf01:~$ cl set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:~$ cl set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:~$ cl set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ cl set bridge domain br_default untagged 1
cumulus@leaf01:~$ cl set router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp peer swp52 remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.1/32
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.1.10.0/24
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cl set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ cl set interface bond1 bond member swp1
cumulus@leaf02:~$ cl set interface bond2 bond member swp2
cumulus@leaf02:~$ cl set interface bond3 bond member swp3
cumulus@leaf02:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf02:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf02:~$ cl set interface bond3 bond mlag id 3
cumulus@leaf02:~$ cl set interface bond1-3 bridge domain br_default 
cumulus@leaf02:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf02:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ cl set mlag backup 10.10.10.1
cumulus@leaf02:~$ cl set mlag peer-ip linklocal
cumulus@leaf02:~$ cl set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:~$ cl set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:~$ cl set interface vlan30 ip address 10.1.30.3/24
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10,20,30
cumulus@leaf02:~$ cl set bridge domain br_default untagged 1
cumulus@leaf02:~$ cl set router bgp autonomous-system 65102
cumulus@leaf02:~$ cl set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ cl set vrf default router bgp peer swp51 remote-as external
cumulus@leaf02:~$ cl set vrf default router bgp peer swp52 remote-as external
cumulus@leaf02:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.2/32
cumulus@leaf02:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cl set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ cl set interface bond1 bond member swp1
cumulus@leaf03:~$ cl set interface bond2 bond member swp2
cumulus@leaf03:~$ cl set interface bond3 bond member swp3
cumulus@leaf03:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf03:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf03:~$ cl set interface bond3 bond mlag id 3
cumulus@leaf03:~$ cl set interface bond1-3 bridge domain br_default 
cumulus@leaf03:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf03:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf03:~$ cl set mlag backup 10.10.10.4
cumulus@leaf03:~$ cl set mlag peer-ip linklocal
cumulus@leaf03:~$ cl set interface vlan40 ip address 10.1.40.4/24
cumulus@leaf03:~$ cl set interface vlan50 ip address 10.1.50.4/24
cumulus@leaf03:~$ cl set interface vlan60 ip address 10.1.60.4/24
cumulus@leaf03:~$ cl set bridge domain br_default vlan 40,50,60
cumulus@leaf03:~$ cl set bridge domain br_default untagged 1
cumulus@leaf03:~$ cl set router bgp autonomous-system 65103
cumulus@leaf03:~$ cl set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ cl set vrf default router bgp peer swp51 remote-as external
cumulus@leaf03:~$ cl set vrf default router bgp peer swp52 remote-as external
cumulus@leaf03:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.3/32
cumulus@leaf03:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cl set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ cl set interface bond1 bond member swp1
cumulus@leaf04:~$ cl set interface bond2 bond member swp2
cumulus@leaf04:~$ cl set interface bond3 bond member swp3
cumulus@leaf04:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf04:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf04:~$ cl set interface bond3 bond mlag id 3
cumulus@leaf04:~$ cl set interface bond1-3 bridge domain br_default 
cumulus@leaf04:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf04:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf04:~$ cl set mlag backup 10.10.10.3
cumulus@leaf04:~$ cl set mlag peer-ip linklocal
cumulus@leaf04:~$ cl set interface vlan40 ip address 10.1.40.5/24
cumulus@leaf04:~$ cl set interface vlan50 ip address 10.1.50.5/24
cumulus@leaf04:~$ cl set interface vlan60 ip address 10.1.60.5/24
cumulus@leaf04:~$ cl set bridge domain br_default vlan 40,50,60
cumulus@leaf04:~$ cl set bridge domain br_default untagged 1
cumulus@leaf04:~$ cl set router bgp autonomous-system 65104
cumulus@leaf04:~$ cl set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ cl set vrf default router bgp peer swp51 remote-as external
cumulus@leaf04:~$ cl set vrf default router bgp peer swp52 remote-as external
cumulus@leaf04:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.4/32
cumulus@leaf04:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cl set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ cl set router bgp autonomous-system 65199
cumulus@spine01:~$ cl set router bgp router-id 10.10.10.101
cumulus@spine01:~$ cl set vrf default router bgp peer swp1 remote-as external
cumulus@spine01:~$ cl set vrf default router bgp peer swp2 remote-as external
cumulus@spine01:~$ cl set vrf default router bgp peer swp3 remote-as external
cumulus@spine01:~$ cl set vrf default router bgp peer swp4 remote-as external
cumulus@spine01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.101/32
cumulus@spine01:~$ cl config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cl set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ cl set router bgp autonomous-system 65100
cumulus@spine02:~$ cl set router bgp router-id 10.10.10.102
cumulus@spine02:~$ cl set vrf default router bgp peer swp1 remote-as external
cumulus@spine02:~$ cl set vrf default router bgp peer swp2 remote-as external
cumulus@spine02:~$ cl set vrf default router bgp peer swp3 remote-as external
cumulus@spine02:~$ cl set vrf default router bgp peer swp4 remote-as external
cumulus@spine02:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.102/32
cumulus@spine02:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## /etc/cue.d/startup.yaml

The CUE `cl config save` command saves the configuration in the `/etc/cue.d/startup.yaml` file. For example:

{{< tabs "TabID169 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/cue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        type: loopback
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
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/cue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.2/32: {}
        type: loopback
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
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ sudo cat /etc/cue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.3/32: {}
        type: loopback
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
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.4: {}
      peer-ip: linklocal
    bridge:
      domain:
        br_default:
          vlan:
            '40': {}
            '50': {}
            '60': {}
          untagged: 1
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
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:mgmt:~$ sudo cat /etc/cue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.4/32: {}
        type: loopback
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
    mlag:
      mac-address: 44:38:39:BE:EF:AA
      backup:
        10.10.10.3: {}
      peer-ip: linklocal
    bridge:
      domain:
        br_default:
          vlan:
            '40': {}
            '50': {}
            '60': {}
          untagged: 1
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
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo cat /etc/cue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.101/32: {}
        type: loopback
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
cumulus@spine02:mgmt:~$ sudo cat /etc/cue.d/startup.yaml 
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.102/32: {}
        type: loopback
    router:
      bgp:
        autonomous-system: 65100
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
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1

auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 2

auto bond3
iface bond3
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 3

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
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.2/24
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.2/24
    vlan-raw-device br_default
    vlan-id 30

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

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 bond3
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
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

auto bond1
iface bond1
    clag-id 1
    bond-slaves swp1
    bond-lacp-bypass-allow no

auto bond2
iface bond2
    clag-id 2
    bond-slaves swp2
    bond-lacp-bypass-allow no

auto bond3
iface bond3
    clag-id 3
    bond-slaves swp3
    bond-lacp-bypass-allow no

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
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.3/24
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.3/24
    vlan-raw-device br_default
    vlan-id 30

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

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 bond3
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
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

auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1

auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 2

auto bond3
iface bond3
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 3

auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.4
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:BB

auto vlan40
iface vlan40
    address 10.1.40.2/24
    vlan-raw-device br_default
    vlan-id 40

auto vlan50
iface vlan50
    address 10.1.50.2/24
    vlan-raw-device br_default
    vlan-id 50

auto vlan60
iface vlan60
    address 10.1.60.2/24
    vlan-raw-device br_default
    vlan-id 60

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

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 bond3
    bridge-vids 40 50 60
    bridge-vlan-aware yes
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
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto bond1
iface bond1
    bond-slaves swp
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1

auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 2

auto bond3
iface bond3
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 3

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
    clagd-args --initDelay 180

auto vlan40
iface vlan40
    address 10.1.40.3/24
    vlan-raw-device br_default
    vlan-id 40

auto vlan50
iface vlan50
    address 10.1.50.3/24
    vlan-raw-device br_default
    vlan-id 50

auto vlan60
iface vlan60
    address 10.1.60.3/24
    vlan-raw-device br_default
    vlan-id 60

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

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2 bond3
    bridge-vids 40 50 60
    bridge-vlan-aware yes
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
    address 127.0.0.1/8
    address ::1/128
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
cumulus@spine02:~$ cat /etc/network/interfaces
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

## /etc/frr/frr.conf

{{< tabs "TabID944 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.1
 bgp bestpath as-path multipath-relax
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface remote-as external
 neighbor swp52 interface remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.2
 bgp bestpath as-path multipath-relax
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface remote-as external
 neighbor swp52 interface remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf
...
router bgp 65102
 bgp router-id 10.10.10.3
 bgp bestpath as-path multipath-relax
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface remote-as external
 neighbor swp52 interface remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf
...
router bgp 65102
 bgp router-id 10.10.10.4
 bgp bestpath as-path multipath-relax
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface remote-as external
 neighbor swp52 interface remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
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
 neighbor swp1 interface remote-as external
 neighbor swp2 interface remote-as external
 neighbor swp3 interface remote-as external
 neighbor swp4 interface remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
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
 neighbor swp1 interface remote-as external
 neighbor swp2 interface remote-as external
 neighbor swp3 interface remote-as external
 neighbor swp4 interface remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
```

{{< /tab >}}
{{< /tabs >}}
