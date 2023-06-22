---
title: Configuration Example
author: NVIDIA
weight: 880
toc: 3
---
This section shows a BGP configuration example based on the reference topology. The example configures BGP *unnumbered* on all leafs and spines, and MLAG on leaf01 and leaf02, and on leaf03 and leaf04.

{{< img src = "/images/cumulus-linux/mlag-config-peering.png" >}}

{{< tabs "TabID695 ">}}
{{< tab "NVUE Commands">}}

{{< tabs "TabID38 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:mgmt:~$ nv set interface swp1-3,swp49-52
cumulus@leaf01:mgmt:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:mgmt:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:mgmt:~$ nv set interface bond3 bond member swp3
cumulus@leaf01:mgmt:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:mgmt:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf01:mgmt:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf01:mgmt:~$ nv set interface bond1-3 bridge domain br_default 
cumulus@leaf01:mgmt:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:mgmt:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:mgmt:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:mgmt:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:mgmt:~$ nv set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:mgmt:~$ nv set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default untagged 1
cumulus@leaf01:mgmt:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:mgmt:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:mgmt:~$ nv set interface swp1-3,swp49-52
cumulus@leaf02:mgmt:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:mgmt:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:mgmt:~$ nv set interface bond3 bond member swp3
cumulus@leaf02:mgmt:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf02:mgmt:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf02:mgmt:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf02:mgmt:~$ nv set interface bond1-3 bridge domain br_default 
cumulus@leaf02:mgmt:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:mgmt:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:mgmt:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:mgmt:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:mgmt:~$ nv set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:mgmt:~$ nv set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:mgmt:~$ nv set interface vlan30 ip address 10.1.30.3/24
cumulus@leaf02:mgmt:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf02:mgmt:~$ nv set bridge domain br_default untagged 1
cumulus@leaf02:mgmt:~$ nv set router bgp autonomous-system 65102
cumulus@leaf02:mgmt:~$ nv set router bgp router-id 10.10.10.2
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.2/32
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf02:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:mgmt:~$ nv set interface swp1-3,swp49-52
cumulus@leaf03:mgmt:~$ nv set interface bond1 bond member swp1
cumulus@leaf03:mgmt:~$ nv set interface bond2 bond member swp2
cumulus@leaf03:mgmt:~$ nv set interface bond3 bond member swp3
cumulus@leaf03:mgmt:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf03:mgmt:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf03:mgmt:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf03:mgmt:~$ nv set interface bond1-3 bridge domain br_default 
cumulus@leaf03:mgmt:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf03:mgmt:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf03:mgmt:~$ nv set mlag backup 10.10.10.4
cumulus@leaf03:mgmt:~$ nv set mlag peer-ip linklocal
cumulus@leaf03:mgmt:~$ nv set interface vlan40 ip address 10.1.40.4/24
cumulus@leaf03:mgmt:~$ nv set interface vlan50 ip address 10.1.50.4/24
cumulus@leaf03:mgmt:~$ nv set interface vlan60 ip address 10.1.60.4/24
cumulus@leaf03:mgmt:~$ nv set bridge domain br_default vlan 40,50,60
cumulus@leaf03:mgmt:~$ nv set bridge domain br_default untagged 1
cumulus@leaf03:mgmt:~$ nv set router bgp autonomous-system 65103
cumulus@leaf03:mgmt:~$ nv set router bgp router-id 10.10.10.3
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.3/32
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf03:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:mgmt:~$ nv set interface lo ip address 10.10.10.4/32
cumulus@leaf04:mgmt:~$ nv set interface swp1-3,swp49-52
cumulus@leaf04:mgmt:~$ nv set interface bond1 bond member swp1
cumulus@leaf04:mgmt:~$ nv set interface bond2 bond member swp2
cumulus@leaf04:mgmt:~$ nv set interface bond3 bond member swp3
cumulus@leaf04:mgmt:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf04:mgmt:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf04:mgmt:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf04:mgmt:~$ nv set interface bond1-3 bridge domain br_default 
cumulus@leaf04:mgmt:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf04:mgmt:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf04:mgmt:~$ nv set mlag backup 10.10.10.3
cumulus@leaf04:mgmt:~$ nv set mlag peer-ip linklocal
cumulus@leaf04:mgmt:~$ nv set interface vlan40 ip address 10.1.40.5/24
cumulus@leaf04:mgmt:~$ nv set interface vlan50 ip address 10.1.50.5/24
cumulus@leaf04:mgmt:~$ nv set interface vlan60 ip address 10.1.60.5/24
cumulus@leaf04:mgmt:~$ nv set bridge domain br_default vlan 40,50,60
cumulus@leaf04:mgmt:~$ nv set bridge domain br_default untagged 1
cumulus@leaf04:mgmt:~$ nv set router bgp autonomous-system 65104
cumulus@leaf04:mgmt:~$ nv set router bgp router-id 10.10.10.4
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.4/32
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf04:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:mgmt:~$ nv set interface swp1-4
cumulus@spine01:mgmt:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:mgmt:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp2 remote-as external
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp3 remote-as external
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp4 remote-as external
cumulus@spine01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32
cumulus@spine01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:mgmt:~$ nv set interface lo ip address 10.10.10.102/32
cumulus@spine02:mgmt:~$ nv set interface swp1-4
cumulus@spine02:mgmt:~$ nv set router bgp autonomous-system 65199
cumulus@spine02:mgmt:~$ nv set router bgp router-id 10.10.10.102
cumulus@spine02:mgmt:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine02:mgmt:~$ nv set vrf default router bgp neighbor swp2 remote-as external
cumulus@spine02:mgmt:~$ nv set vrf default router bgp neighbor swp3 remote-as external
cumulus@spine02:mgmt:~$ nv set vrf default router bgp neighbor swp4 remote-as external
cumulus@spine02:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.102/32
cumulus@spine02:mgmt:~$ nv config apply
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
    bridge:
      domain:
        br_default:
          untagged: 1
          vlan:
            '10': {}
            '20': {}
            '30': {}
    interface:
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default: {}
        type: bond
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            enable: on
            id: 2
        bridge:
          domain:
            br_default: {}
        type: bond
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            enable: on
            id: 3
        bridge:
          domain:
            br_default: {}
        type: bond
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
      backup:
        10.10.10.2: {}
      enable: on
      mac-address: 44:38:39:BE:EF:AA
      peer-ip: linklocal
    router:
      bgp:
        autonomous-system: 65101
        enable: on
        router-id: 10.10.10.1
    vrf:
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.1.10.0/24: {}
                  10.10.10.1/32: {}
                redistribute:
                  connected:
                    enable: on
            enable: on
            neighbor:
              swp51:
                remote-as: external
                type: unnumbered
              swp52:
                remote-as: external
                type: unnumbered
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
            '10': {}
            '20': {}
            '30': {}
    interface:
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default: {}
        type: bond
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            enable: on
            id: 2
        bridge:
          domain:
            br_default: {}
        type: bond
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            enable: on
            id: 3
        bridge:
          domain:
            br_default: {}
        type: bond
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
      backup:
        10.10.10.1: {}
      enable: on
      mac-address: 44:38:39:BE:EF:AA
      peer-ip: linklocal
    router:
      bgp:
        autonomous-system: 65102
        enable: on
        router-id: 10.10.10.2
    vrf:
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.10.10.2/32: {}
                redistribute:
                  connected:
                    enable: on
            enable: on
            neighbor:
              swp51:
                remote-as: external
                type: unnumbered
              swp52:
                remote-as: external
                type: unnumbered
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    bridge:
      domain:
        br_default:
          untagged: 1
          vlan:
            '40': {}
            '50': {}
            '60': {}
    interface:
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default: {}
        type: bond
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            enable: on
            id: 2
        bridge:
          domain:
            br_default: {}
        type: bond
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            enable: on
            id: 3
        bridge:
          domain:
            br_default: {}
        type: bond
      lo:
        ip:
          address:
            10.10.10.3/32: {}
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
      backup:
        10.10.10.4: {}
      enable: on
      mac-address: 44:38:39:BE:EF:AA
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
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.10.10.3/32: {}
                redistribute:
                  connected:
                    enable: on
            enable: on
            neighbor:
              swp51:
                remote-as: external
                type: unnumbered
              swp52:
                remote-as: external
                type: unnumbered
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    bridge:
      domain:
        br_default:
          untagged: 1
          vlan:
            '40': {}
            '50': {}
            '60': {}
    interface:
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default: {}
        type: bond
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            enable: on
            id: 2
        bridge:
          domain:
            br_default: {}
        type: bond
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            enable: on
            id: 3
        bridge:
          domain:
            br_default: {}
        type: bond
      lo:
        ip:
          address:
            10.10.10.4/32: {}
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
      backup:
        10.10.10.3: {}
      enable: on
      mac-address: 44:38:39:BE:EF:AA
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
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.10.10.4/32: {}
                redistribute:
                  connected:
                    enable: on
            enable: on
            neighbor:
              swp51:
                remote-as: external
                type: unnumbered
              swp52:
                remote-as: external
                type: unnumbered
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
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.10.10.101/32: {}
            enable: on
            neighbor:
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
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.10.10.102/32: {}
            enable: on
            neighbor:
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
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID901 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/network/interfaces
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
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.2/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.2/24
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
cumulus@leaf02:mgmt:~$ sudo cat /etc/network/interfaces
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
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180
auto vlan10
iface vlan10
    address 10.1.10.3/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.3/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.3/24
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
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.3/32
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
    clagd-backup-ip 10.10.10.4
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180
auto vlan40
iface vlan40
    address 10.1.40.4/24
    hwaddress 44:38:39:22:01:bb
    vlan-raw-device br_default
    vlan-id 40
auto vlan50
iface vlan50
    address 10.1.50.4/24
    hwaddress 44:38:39:22:01:bb
    vlan-raw-device br_default
    vlan-id 50
auto vlan60
iface vlan60
    address 10.1.60.4/24
    hwaddress 44:38:39:22:01:bb
    vlan-raw-device br_default
    vlan-id 60
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink
    hwaddress 44:38:39:22:01:bb
    bridge-vlan-aware yes
    bridge-vids 40 50 60
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:mgmt:~$ sudo cat /etc/network/interfaces
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
    clagd-backup-ip 10.10.10.3
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180
auto vlan40
iface vlan40
    address 10.1.40.5/24
    hwaddress 44:38:39:22:01:c1
    vlan-raw-device br_default
    vlan-id 40
auto vlan50
iface vlan50
    address 10.1.50.5/24
    hwaddress 44:38:39:22:01:c1
    vlan-raw-device br_default
    vlan-id 50
auto vlan60
iface vlan60
    address 10.1.60.5/24
    hwaddress 44:38:39:22:01:c1
    vlan-raw-device br_default
    vlan-id 60
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink
    hwaddress 44:38:39:22:01:c1
    bridge-vlan-aware yes
    bridge-vids 40 50 60
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo cat /etc/network/interfaces
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
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:mgmt:~$ sudo cat /etc/network/interfaces
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
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID944 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/frr/frr.conf
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
neighbor swp51 interface remote-as external
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.1.10.0/24
network 10.10.10.1/32
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
exit-address-family
! end of router bgp 65101 vrf default
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/frr/frr.conf
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
neighbor swp51 interface remote-as external
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.10.10.2/32
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
exit-address-family
! end of router bgp 65102 vrf default
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ sudo cat /etc/frr/frr.conf
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
neighbor swp51 interface remote-as external
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.10.10.3/32
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
exit-address-family
! end of router bgp 65103 vrf default
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:mgmt:~$ sudo cat /etc/frr/frr.conf
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
neighbor swp51 interface remote-as external
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.10.10.4/32
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
exit-address-family
! end of router bgp 65104 vrf default
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
neighbor swp1 interface remote-as external
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.10.10.101/32
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
exit-address-family
! end of router bgp 65199 vrf default
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
neighbor swp1 interface remote-as external
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
neighbor swp3 interface remote-as external
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
neighbor swp4 interface remote-as external
neighbor swp4 timers 3 9
neighbor swp4 timers connect 10
neighbor swp4 advertisement-interval 0
neighbor swp4 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.10.10.102/32
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
neighbor swp3 activate
neighbor swp4 activate
exit-address-family
! end of router bgp 65199 vrf default
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Try It " >}}
    {{< simulation name="Try It CL55 - BGP" showNodes="leaf01,leaf02,leaf03,leaf04,spine01,spine02,server01,server04" >}}

This simulation starts with the example BGP configuration. The demo is pre-configured using {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/" text="NVUE">}} commands.

To validate the configuration, run the commands listed in the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Border-Gateway-Protocol-BGP/Troubleshooting-BGP/" text="Troubleshooting-BGP">}} section.

{{< /tab >}}
{{< /tabs >}}
