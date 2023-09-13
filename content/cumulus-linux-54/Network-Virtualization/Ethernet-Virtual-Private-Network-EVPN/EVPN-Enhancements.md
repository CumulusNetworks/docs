---
title: EVPN Enhancements
author: NVIDIA
weight: 560
toc: 4
---
This section describes EVPN enhancements.

## Define RDs and RTs

When <span style="background-color:#F5F5DC">[FRR](## "FRRouting")</span> learns about a local VNI and there is no explicit configuration for that VNI in FRR, the switch derives the <span style="background-color:#F5F5DC">[RD](## "route distinguisher")</span> and import and export <span style="background-color:#F5F5DC">[RTs](## "route targets")</span> for this VNI automatically. The RD uses *RouterId:VNI-Index* and the import and export RTs use *AS:VNI*. For routes that come from a layer 2 VNI (type-2 and type-3), the RD uses the VXLAN local tunnel IP address (`vxlan-local-tunnelip`) from the layer 2 VNI interface instead of the RouterId (`vxlan-local-tunnelip:VNI`). EVPN route exchange uses the RD and RTs.

The RD disambiguates EVPN routes in different VNIs (they can have the same MAC and IP address) while the RTs describe the VPN membership for the route. The *VNI-Index* for the RD is a unique number that the switch generates. It only has local significance; on remote switches, its only role is for route disambiguation. The switch uses this number instead of the VNI value itself because this number has to be less than or equal to 65535. In the RT, the <span style="background-color:#F5F5DC">[AS](## "Autonomous System")</span> is always a 2-byte value to allow room for a large VNI. If the router has a 4-byte AS, it only uses the lower 2 bytes. This ensures a unique RT for different VNIs while having the same RT for the same VNI across routers in the same AS.

For eBGP EVPN peering, the peers are in a different AS so using an automatic RT of *AS:VNI* does not work for route import. Therefore, Cumulus Linux treats the import RT as *\*:VNI* to determine which received routes apply to a particular VNI. This only applies when the switch auto-derives the import RT.

If you do *not* want to derive RDs and RTs automatically, you can define them manually. The following example commands are per VNI.

{{< tabs "TabID19 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID52 ">}}
{{< tab "leaf01 ">}}

``` 
cumulus@leaf01:~$ nv set evpn vni 10 rd 10.10.10.1:20
cumulus@leaf01:~$ nv set evpn vni 10 route-target export 65101:10
cumulus@leaf01:~$ nv set evpn vni 10 route-target import 65102:10
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set evpn vni 10 rd 10.10.10.3:20
cumulus@leaf03:~$ nv set evpn vni 10 route-target export 65102:10
cumulus@leaf03:~$ nv set evpn vni 10 route-target import 65101:10
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

{{< tabs "TabID90 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# vni 10
leaf01(config-router-af-vni)# rd 10.10.10.1:20
leaf01(config-router-af-vni)# route-target export 65101:10
leaf01(config-router-af-vni)# route-target import 65102:10
leaf01(config-router-af-vni)# exit
leaf01(config-router-af)# advertise-all-vni
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

```
...
address-family l2vpn evpn
  advertise-all-vni
  vni 10
   rd 10.10.10.1:20
   route-target export 65101:10
   route-target import 65102:10
...
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo vtysh
...
leaf03# configure terminal
leaf03(config)# router bgp 65102
leaf03(config-router)# address-family l2vpn evpn
leaf03(config-router-af)# vni 10
leaf03(config-router-af-vni)# rd 10.10.10.3:20
leaf03(config-router-af-vni)# route-target export 65102:10
leaf03(config-router-af-vni)# route-target import 65101:10
leaf03(config-router-af-vni)# exit
leaf03(config-router-af)# advertise-all-vni
leaf03(config-router-af)# end
leaf03# write memory
leaf03# exit
```

The vtysh commands create the following configuration snippet in the `/etc/frr/frr.conf` file:

```
...
address-family l2vpn evpn
  advertise-all-vni
  vni 10
   rd 10.10.10.3:20
   route-target export 65102:10
   route-target import 65101:10
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- If you delete the RD or RT later, it reverts back to its corresponding default value.
- Route target auto derivation does not support 4-byte AS numbers; If the router has a 4-byte AS, you must define the RTs manually.
{{%/notice%}}

You can configure multiple RT values. In addition, you can configure both the import and export route targets with a single command by using `route-target both`:

{{< tabs "TabID169 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID200 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set evpn vni 10 route-target import 65102:10
cumulus@leaf01:~$ nv set evpn vni 10 route-target import 65102:20
cumulus@leaf01:~$ nv set evpn vni 20 route-target both 65101:10
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set evpn vni 10 route-target import 65101:10
cumulus@leaf03:~$ nv set evpn vni 10 route-target import 65101:20
cumulus@leaf03:~$ nv set evpn vni 20 route-target both 65102:10
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

{{< tabs "TabID238 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# vni 10
leaf01(config-router-af-vni)# route-target import 65102:10
leaf01(config-router-af-vni)# route-target import 65102:20
leaf01(config-router-af-vni)# exit
leaf01(config-router-af)# vni 20
leaf01(config-router-af-vni)# route-target both 65101:10
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands create the following configuration snippet in the `/etc/frr/frr.conf` file:

```
...
address-family l2vpn evpn
  vni 10
    route-target import 65102:10
    route-target import 65102:20
  vni 20
    route-target import 65101:10
    route-target export 65101:10
...
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo vtysh
...
leaf03# configure terminal
leaf03(config)# router bgp 65102
leaf03(config-router)# address-family l2vpn evpn
leaf03(config-router-af)# vni 10
leaf03(config-router-af-vni)# route-target import 65101:10
leaf03(config-router-af-vni)# route-target import 65101:20
leaf03(config-router-af-vni)# exit
leaf03(config-router-af)# vni 20
leaf03(config-router-af-vni)# route-target both 65102:10
leaf03(config-router-af)# end
leaf03# write memory
leaf03# exit
```

The vtysh commands create the following configuration snippet in the `/etc/frr/frr.conf` file:

```
...
address-family l2vpn evpn
  vni 10
    route-target import 65101:10
    route-target import 65101:20
  vni 20
    route-target import 65102:10
    route-target export 65102:10
...
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## Enable EVPN in an iBGP Environment with an OSPF Underlay

You can use EVPN with an {{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}} or static route underlay. This is a more complex configuration than using <span style="background-color:#F5F5DC">[eBGP](## "external BGP")</span>. In this case, <span style="background-color:#F5F5DC">[iBGP](## "internal BGP")</span> advertises EVPN routes directly between <span style="background-color:#F5F5DC">[VTEPs](## "Virtual Tunnel End Points")</span> and the spines are unaware of EVPN or BGP.

The leafs peer with each other in a full mesh within the EVPN address family without using route reflectors. The leafs generally peer to their loopback addresses, which advertise in OSPF. The receiving VTEP imports routes into a specific VNI with a matching route target community.

{{< tabs "TabID292 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.10.10.2 remote-as internal
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.10.10.3 remote-as internal
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.10.10.4 remote-as internal
cumulus@leaf01:~$ nv set evpn enable on
cumulus@leaf01:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.10.10.2 address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.10.10.3 address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.10.10.4 address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf default router ospf router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router ospf area 0 network 10.10.10.1/32
cumulus@leaf01:~$ nv set interface lo router ospf passive on
cumulus@leaf01:~$ nv set interface swp49 router ospf area 0.0.0.0
cumulus@leaf01:~$ nv set interface swp50 router ospf area 0.0.0.0
cumulus@leaf01:~$ nv set interface swp51 router ospf area 0.0.0.0
cumulus@leaf01:~$ nv set interface swp52 router ospf area 0.0.0.0
cumulus@leaf01:~$ nv set interface swp49 router ospf network-type point-to-point
cumulus@leaf01:~$ nv set interface swp50 router ospf network-type point-to-point
cumulus@leaf01:~$ nv set interface swp51 router ospf network-type point-to-point
cumulus@leaf01:~$ nv set interface swp52 router ospf network-type point-to-point
cumulus@leaf01:~$ nv config apply
```

After you run `nv config save`, the NVUE commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        router:
          ospf:
            area: 0
            enable: on
            network-type: point-to-point    
        type: loopback
      swp49:
        router:
          ospf:
            area: 0.0.0.0
            enable: on
        type: swp
      swp50:
        router:
          ospf:
            area: 0.0.0.0
            enable: on
            network-type: point-to-point
        type: swp
      swp51:
        router:
          ospf:
            area: 0.0.0.0
            enable: on
            network-type: point-to-point
        type: swp
      swp52:
        router:
          ospf:
            area: 0.0.0.0
            enable: on
            network-type: point-to-point
        type: swp
    bridge:
      domain:
        br_default:
          multicast:
            snooping:
              enable: off
              querier:
                enable: on
    router:
      bgp:
        autonomous-system: 65101
        enable: on
        router-id: 10.10.10.1
      ospf:
        router-id: 10.10.10.1
        enable: on
    vrf:
      default:
        router:
          bgp:
            peer:
              10.10.10.2:
                remote-as: internal
                type: numbered
                address-family:
                  l2vpn-evpn:
                    enable: on
              10.10.10.3:
                remote-as: internal
                type: numbered
                address-family:
                  l2vpn-evpn:
                    enable: on
              10.10.10.4:
                remote-as: internal
                type: numbered
                address-family:
                  l2vpn-evpn:
                    enable: on
            enable: on
            address-family:
              l2vpn-evpn:
                enable: on
    evpn:
      enable: on
    nve:
      vxlan:
        enable: on
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor 10.10.10.2 remote-as internal
leaf01(config-router)# neighbor 10.10.10.3 remote-as internal
leaf01(config-router)# neighbor 10.10.10.4 remote-as internal
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# neighbor 10.10.10.2 activate
leaf01(config-router-af)# neighbor 10.10.10.3 activate
leaf01(config-router-af)# neighbor 10.10.10.4 activate
leaf01(config-router-af)# advertise-all-vni
leaf01(config-router-af)# exit
leaf01(config-router)# exit
leaf01(config)# router ospf
leaf01(config-router)# router-id 10.10.10.1
leaf01(config-router)# passive-interface lo
leaf01(config-router)# exit
leaf01(config)# interface lo
leaf01(config-if)# ip ospf area 0.0.0.0
leaf01(config-if)# exit
leaf01(config)# interface swp49
leaf01(config-if)# ip ospf area 0.0.0.0
leaf01(config-if)# ospf network point-to-point
leaf01(config-if)# exit
leaf01(config)# interface swp50
leaf01(config-if)# ip ospf area 0.0.0.0
leaf01(config-if)# ospf network point-to-point
leaf01(config-if)# exit
leaf01(config)# interface swp51
leaf01(config-if)# ip ospf area 0.0.0.0
leaf01(config-if)# ospf network point-to-point
leaf01(config-if)# exit
leaf01(config)# interface swp52
leaf01(config-if)# ip ospf area 0.0.0.0
leaf01(config-if)# ospf network point-to-point
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

```
...
interface lo
  ip ospf area 0.0.0.0
!
interface swp49
  ip ospf area 0.0.0.0
  ip ospf network point-to-point
!
interface swp50
  ip ospf area 0.0.0.0
  ip ospf network point-to-point
!
interface swp51
  ip ospf area 0.0.0.0
  ip ospf network point-to-point
!
interface swp52
  ip ospf area 0.0.0.0
  ip ospf network point-to-point
!
router bgp 65101
  neighbor 10.10.10.2 remote-as internal
  neighbor 10.10.10.3 remote-as internal
  neighbor 10.10.10.4 remote-as internal
  !
  address-family l2vpn evpn
  neighbor 10.10.10.2 activate
  neighbor 10.10.10.3 activate
  neighbor 10.10.10.4 activate
  advertise-all-vni
  exit-address-family
  !
Router ospf
  Ospf router-id 10.10.10.1
  Passive-interface lo
...
```

{{< /tab >}}
{{< /tabs >}}

## ARP and ND Suppression

ARP suppression with EVPN allows a VTEP to suppress ARP flooding over VXLAN tunnels as much as possible. A local proxy handles ARP requests from locally attached hosts for remote hosts. ARP suppression is for IPv4; ND suppression is for IPv6.

Cumulus Linux enables ARP and ND suppression by default on all VNIs to reduce ARP and ND packet flooding over VXLAN tunnels; however, you must to configure layer 3 interfaces (SVIs) for ARP and ND suppression to work with EVPN.

{{%notice note%}}
- ARP and ND suppression only suppresses the flooding of known hosts. To disable all flooding refer to the {{<link title="#Disable BUM Flooding" text="Disable BUM Flooding" >}} section.
- NVIDIA recommends that you keep ARP and ND suppression enabled on all VXLAN interfaces on the switch. If you must disable suppression for a special use case, you can not disable ARP and ND suppression on some VXLAN interfaces but not others.
{{%/notice%}}

In a centralized routing deployment, you must configure layer 3 interfaces even if you configure the switch only for layer 2 (you are not using VXLAN routing). To avoid installing unnecessary layer 3 information, you can turn off IP forwarding.

The following example commands turn off IPv4 and IPv6 forwarding on VLAN 10 and VLAN 20.

{{< tabs "TabID367 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set interface vlan10 ip ipv4 forward off
cumulus@leaf01:~$ nv set interface vlan10 ip ipv6 forward off
cumulus@leaf01:~$ nv set interface vlan20 ip ipv4 forward off
cumulus@leaf01:~$ nv set interface vlan20 ip ipv6 forward off
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file.

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
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
...
```

{{< /tab >}}
{{< /tabs >}}

For a bridge in {{<link url="Traditional-Bridge-Mode" text="traditional mode">}}, you must edit the bridge configuration in the `/etc/network/interfaces` file using a text editor:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto bridge1
iface bridge1
    bridge-ports swp1.10 swp2.10 vni10
    ip6-forward off
    ip-forward off
...
```

When deploying EVPN and VXLAN using a hardware profile *other* than the default {{<link url="Supported-Route-Table-Entries#forwarding-table-profiles" text="Forwarding Table Profile">}}, ensure that the Linux kernel ARP `sysctl` settings `gc_thresh2` and `gc_thresh3` both have a value larger than the number of neighbor (ARP and ND) entries you expect in the deployment. To configure these settings, edit the `/etc/sysctl.d/neigh.conf` file, then reboot the switch. If your network has more hosts than the values in the example below, change the `sysctl` entries accordingly.

{{< expand " Example /etc/sysctl.d/neigh.conf file"  >}}

```
cumulus@leaf01:~$ sudo nano /etc/sysctl.d/neigh.conf
...
net.ipv4.neigh.default.gc_thresh3=14336
net.ipv6.neigh.default.gc_thresh3=16384
net.ipv4.neigh.default.gc_thresh2=7168
net.ipv6.neigh.default.gc_thresh2=8192
...
```

{{< /expand >}}

Keep ARP and ND suppression on to reduce ARP and ND packet flooding over VXLAN tunnels. However, if you need to disable ARP and ND suppression, follow the example commands below.

{{< tabs "TabID593 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set nve vxlan arp-nd-suppress off
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to set `bridge-arp-nd-suppress off` on the VXLAN device, then run the `ifreload -a` command.

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...

auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20 30=30 4036=4002 4024=4001
    bridge-learning off
    bridge-arp-nd-suppress off

...
```

```
cumulus@leaf01:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

## Configure Static MAC Addresses

You can configure a MAC address that you intend to pin to a particular VTEP on the VTEP as a static bridge FDB entry. EVPN picks up these MAC addresses and advertises them to peers as remote static MACs. You configure static bridge FDB entries for MAC addresses under the bridge configuration:

{{< tabs "TabID641 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this configuration.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file. For example:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports bond1 vni10
    bridge-vids 10
    bridge-vlan-aware yes
    post-up bridge fdb add 26:76:e6:93:32:78 dev bond1 vlan 10 master static sticky
...
```

{{< /tab >}}
{{< /tabs >}}

For a bridge in {{<link url="Traditional-Bridge-Mode" text="traditional mode">}}, you must edit the bridge configuration in the `/etc/network/interfaces` file using a text editor:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto br10
iface br10
    bridge-ports swp1.10 vni10
    post-up bridge fdb add 26:76:e6:93:32:78 dev swp1.10 master static sticky
...
```

## Filter EVPN Routes

It is common to subdivide the data center into multiple pods with full host mobility within a pod but only do prefix-based routing across pods. You can achieve this by only exchanging EVPN type-5 routes across pods.

The following example commands configure EVPN to advertise type-5 routes:

{{< tabs "TabID842 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router policy route-map map1 rule 10 match type ipv4
cumulus@leaf01:~$ nv set router policy route-map map1 rule 10 match evpn-route-type ip-prefix
cumulus@leaf01:~$ nv set router policy route-map map1 rule 10 action permit
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast route-export to-evpn route-map map1
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
..
leaf01# configure terminal
leaf01(config)# route-map map1 permit 1
leaf01(config)# match evpn route-type prefix
leaf01(config)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
You must apply the route map for the configuration to take effect. See {{<link url="Route-Filtering-and-Redistribution/#route-maps" text="Route Maps">}} for more information.
{{%/notice%}}

In many situations, it is also desirable to only exchange EVPN routes carrying a particular VXLAN ID.
For example, if data centers or pods within a data center only share certain tenants, you can use a route map to control the EVPN routes exchanged based on the VNI.

The following example configures a route map that only advertises EVPN routes from VNI 1000:

{{< tabs "TabID887" >}}
{{< tab "NVUE Commands" >}}

```
cumulus@switch:~$ nv set router policy route-map map1 rule 10 match evpn-vni 1000
cumulus@switch:~$ nv set router policy route-map map1 rule 10 action permit
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# route-map map1 permit 1
switch(config)# match evpn vni 1000
switch(config)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
You can only match type-2 and type-5 routes based on VNI.
{{%/notice%}}

## Advertise SVI IP Addresses

In a typical EVPN deployment, you *reuse* SVI IP addresses on VTEPs across multiple racks. However, if you use *unique* SVI IP addresses across multiple racks and you want the local SVI IP address to be reachable via remote VTEPs, you can enable the advertise SVI IP and MAC address option. This option advertises the SVI IP and MAC address as a type-2 route and eliminates the need for any flooding over VXLAN to reach the IP address from a remote VTEP or rack.

{{%notice note%}}
- When you enable the advertise SVI IP and MAC address option, the anycast IP and MAC address pair is not advertised. Be sure **not** to enable both the `advertise-svi-ip` option and the `advertise-default-gw` option at the same time. (The `advertise-default-gw` option configures the gateway VTEPs to advertise their IP and MAC address. See {{<link url="Inter-subnet-Routing#centralized-routing" text="Advertising the Default Gateway">}}.
- If you use <span style="background-color:#F5F5DC">[MLAG](## "Multi-chassis Link Aggregation")</span> on your switch, refer to {{<link url="Inter-subnet-Routing#advertise-primary-ip-address" text="Advertise Primary IP Address">}}.
{{%/notice%}}

To advertise *all* SVI IP and MAC addresses on the switch, run these commands:

{{< tabs "TabID751 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set evpn route-advertise svi-ip on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# advertise-svi-ip
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

To advertise a *specific* SVI IP/MAC address, run these commands:

{{< tabs "TabID711 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set evpn vni 10 route-advertise svi-ip on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# vni 10
leaf01(config-router-af-vni)# advertise-svi-ip
leaf01(config-router-af-vni)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
address-family l2vpn evpn
  vni 10
  advertise-svi-ip
exit-address-family
...
```

{{< /tab >}}
{{< /tabs >}}

## Disable BUM Flooding

By default, the VTEP floods all broadcast, and unknown unicast and multicast packets (such as ARP, NS, or DHCP) it receives to all interfaces (except for the incoming interface) and to all VXLAN tunnel interfaces in the same broadcast domain. When the switch receives such packets on a VXLAN tunnel interface, it floods the packets to all interfaces in the packet's broadcast domain.

You can disable BUM flooding over VXLAN tunnels so that EVPN does not advertise type-3 routes for each local VNI and stops taking action on received type-3 routes.

Disabling BUM flooding is useful in a deployment with a controller or orchestrator, where the switch is pre-provisioned and there is no need to flood any ARP, NS, or DHCP packets.

{{%notice note%}}

For information on EVPN BUM flooding with <span style="background-color:#F5F5DC">[PIM](## "Protocol Independent Multicast")</span>, refer to {{<link url="EVPN-BUM-Traffic-with-PIM-SM" text="EVPN BUM Traffic with PIM-SM">}}.

{{%/notice%}}

To disable BUM flooding:

{{< tabs "TabID872 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv unset nve vxlan flooding enable off
cumulus@leaf01:~$ nv config apply
```

To reenable BUM flooding, run the `nv set nve vxlan flooding enable on` command.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# flooding disable
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
 !
 address-family l2vpn evpn
  flooding disable
 exit-address-family
...
```

To reenable BUM flooding, run the vtysh `flooding head-end-replication` command.

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# flooding head-end-replication
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

To show that BUM flooding is off, run the vtysh `show bgp l2vpn evpn vni` command or the `net show bgp l2vpn evpn vni` command. For example:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show bgp l2vpn evpn vni
Advertise Gateway Macip: Disabled
Advertise SVI Macip: Disabled
Advertise All VNI flag: Enabled
BUM flooding: Disabled
Number of L2 VNIs: 3
Number of L3 VNIs: 2
Flags: * - Kernel
  VNI        Type RD                    Import RT                 Export RT                Tenant VRF
* 20         L2   10.10.10.1:3          65101:20                  65101:20                 RED
* 30         L2   10.10.10.1:4          65101:30                  65101:30                 BLUE
* 10         L2   10.10.10.1:6          65101:10                  65101:10                 RED
* 4002       L3   10.1.30.2:2           65101:4002                65101:4002               BLUE
* 4001       L3   10.1.20.2:5           65101:4001                65101:4001               RED
```

Run the vtysh `show bgp l2vpn evpn route type multicast` command or the `net show bgp l2vpn evpn route type multicast` command to make sure there are no EVPN type-3 routes that originate locally.

## Extended Mobility

Cumulus Linux supports scenarios where the IP to MAC binding for a host or virtual machine changes across the move. In addition to the simple mobility scenario where a host or virtual machine with a binding of `IP1`, `MAC1` moves from one rack to another, Cumulus Linux supports additional scenarios where a host or virtual machine with a binding of `IP1`, `MAC1` moves and takes on a new binding of `IP2`, `MAC1` or `IP1`, `MAC2`. The EVPN protocol mechanism to handle extended mobility continues to use the MAC mobility extended community and is the same as the standard mobility procedures. Extended mobility defines how to compute the sequence number in this attribute when binding changes occur.

Extended mobility not only supports virtual machine *moves*, but also where one virtual machine shuts down and you provision another on a different rack that uses the IP address or the MAC address of the previous virtual machine. For example, in an EVPN deployment with OpenStack, where virtual machines for a tenant provision and shut down dynamically, a new virtual machine can use the same IP address as an earlier virtual machine but with a different MAC address.

{{%notice note%}}
To reuse the same distributed gateway on VLANs fabric wide, you can set the fabric-wide MAC address; see {{<link url="/Virtual-Router-Redundancy-VRR-and-VRRP/#change-the-vrr-mac-address" text="Change the VRR MAC address">}}.
{{%/notice%}}

Cumulus Linux enables extended mobility by default.

To examine the sequence numbers for a host or virtual machine MAC address and IP address, run the vtysh `show evpn mac vni <vni> mac <address>` command or the `net show evpn mac vni <vni> mac <address>` command. For example:

```
cumulus@switch:~$ sudo vtysh
...
switch# show evpn mac vni 10100 mac 00:02:00:00:00:42
MAC: 00:02:00:00:00:42
  Remote VTEP: 10.0.0.2
  Local Seq: 0 Remote Seq: 3
  Neighbors:
    10.1.1.74 Active

switch# show evpn arp vni 10100 ip 10.1.1.74
IP: 10.1.1.74
  Type: local
  State: active
  MAC: 44:39:39:ff:00:24
  Local Seq: 2 Remote Seq: 3
```

## Duplicate Address Detection

Cumulus Linux can detect duplicate MAC and IPv4 or IPv6 addresses on hosts or virtual machines in a VXLAN-EVPN configuration. The Cumulus Linux switch (VTEP) considers a host MAC or IP address to be duplicate if the address moves across the network more than a certain number of times within a certain number of seconds (five moves within 180 seconds by default). In addition to legitimate host or VM mobility scenarios, address movement can occur when you configure IP addresses incorrectly on a host or when packet looping occurs in the network due to faulty configuration or behavior.

Cumulus Linux enables duplicate address detection by default, which triggers when:

- Two hosts have the same MAC address (the host IP addresses are the same or different)
- Two hosts have the same IP address but different MAC addresses

By default, when the switch detects a duplicate address, it flags the address as a duplicate and generates an error in syslog so that you can troubleshoot the reason and address the fault, then clear the duplicate address flag. The switch does not take any functional action on the address.

{{%notice note%}}
- If the switch flags a MAC address as duplicate, it also flags all IP addresses associated with that MAC as duplicates. However, in an MLAG configuration, sometimes only one of the MLAG peers flags the associated IP addresses as duplicates.
- In an MLAG configuration, MAC mobility detection runs independently on each switch in the MLAG pair. Based on the sequence in which local learning and, or route withdrawal from the remote VTEP occurs, the MAC mobility counter for a type-2 route increments only on one of the switches in the MLAG pair. In rare cases, it is possible for neither VTEP to increment the MAC mobility counter for the type-2 prefix.
- Duplicate address detection is not supported in an {{<link title="EVPN Multihoming" text="EVPN multihoming">}} configuration.
{{%/notice%}}

### When Does Duplicate Address Detection Trigger?

The VTEP that sees an address move from remote to local begins the detection process by starting a timer. Each VTEP runs duplicate address detection independently. Detection always starts with the first mobility event from *remote* to *local*. If the address is initially remote, the detection count can start with the first move for the address. If the address is initially local, the detection count starts only with the second or higher move for the address. If an address is undergoing a mobility event between remote VTEPs, duplicate detection does not start.

The following illustration shows VTEP-A, VTEP-B, and VTEP-C in an EVPN configuration. Duplicate address detection triggers on VTEP-A when there is a duplicate MAC address for two hosts attached to VTEP-A and VTEP-B. However, duplicate detection does *not* trigger on VTEP-A when mobility events occur between two remote VTEPs (VTEP-B and VTEP-C).

{{< img src = "/images/cumulus-linux/evpn-dad-example.png" >}}

### Configure Duplicate Address Detection

You can configure the threshold for MAC and IP address moves. The maximum number of moves allowed can be between 2 and 1000 and the detection time interval can be between 2 and 1800 seconds.

The following example command sets the maximum number of address moves allowed to 10 and the duplicate address detection time interval to 1200 seconds.

{{< tabs "TabID1021 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set evpn dad mac-move-threshold 10
cumulus@switch:~$ nv set evpn dad move-window 1200
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# dup-addr-detection max-moves 10 time 1200
switch(config-router-af)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

To disable duplicate address detection, see {{<link url="#disable-duplicate-address-detection" text="Disable Duplicate Address Detection">}} below.

### Example syslog Messages

The following example shows the syslog message that generates when Cumulus Linux detects a MAC address as a duplicate during a local update:

```
2018/11/06 18:55:29.463327 ZEBRA: [EC 4043309149] VNI 1001: MAC 00:01:02:03:04:11 detected as duplicate during local update, last VTEP 172.16.0.16
```

The following example shows the syslog message that generates when Cumulus Linux detects an IP address as a duplicate during a remote update:

```
2018/11/09 22:47:15.071381 ZEBRA: [EC 4043309151] VNI 1002: MAC aa:22:aa:aa:aa:aa IP 10.0.0.9 detected as duplicate during remote update, from VTEP 172.16.0.16
```

### Freeze a Detected Duplicate Address

Cumulus Linux provides a *freeze* option that takes action on a detected duplicate address. You can freeze the address *permanently* (until you intervene) or for a *defined amount of time*, after which it clears automatically.

When you enable the freeze option and the switch detects a duplicate address:

- If the switch learns the MAC or IP address from a remote VTEP at the time it freezes, the forwarding information in the kernel and hardware does not update, leaving it in the prior state. Any future remote updates process but they do not reflect in the kernel entry. If the remote VTEP sends a MAC-IP route withdrawal, the local VTEP removes the frozen remote entry. Then, if the local VTEP has a locally learned entry already present in its kernel, FRR originates a corresponding MAC-IP route and advertises it to all remote VTEPs.
- If the MAC or IP address is locally learned on this VTEP at the time it freezes, the address does not advertise to remote VTEPs. Future local updates process but do not advertise to remote VTEPs. If FRR receives a local entry delete event, it removes the frozen entry from the FRR database. Any remote updates (from other VTEPs) change the state of the entry to remote but the entry does not install in the kernel (until cleared).

**To recover from a freeze**, shut down the faulty host or VM or fix any other misconfiguration in the network. If the address freezes *permanently,* run the {{<link url="#clear-duplicate-addresses" text="clear command">}} on the VTEP where the address is duplicate. If the address freezes for a defined period of time, it clears automatically after the timer expires (you can clear the duplicate address before the timer expires with the {{<link url="#clear-duplicate-addresses" text="clear command">}}).

{{%notice note%}}
If you run the clear command or the timer expires before you address the fault, duplicate address detection can continue to occur.
{{%/notice%}}

After you clear a frozen address, if it is present behind a remote VTEP, the kernel and hardware forwarding tables update. If this VTEP learns the address locally, the address advertises to remote VTEPs. All VTEPs get the correct address as soon as the host communicates. The switch only learns silent hosts after the faulty entries age out, or you intervene and clear the faulty MAC and ARP table entries.

### Configure the Freeze Option

You can enable Cumulus Linux to *freeze* detected duplicate addresses. The duration can be any number of seconds between 30 and 3600.

The following example command freezes duplicate addresses for a period of 1000 seconds, after which it clears automatically:

{{< tabs "TabID1095 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set evpn dad duplicate-action freeze duration 1000
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# dup-addr-detection freeze 1000
switch(config-router-af)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Set the freeze timer to be three times the duplicate address detection window. For example, if the duplicate address detection window is 180 seconds, set the freeze timer to 540 seconds.
{{%/notice%}}

The following example command freezes duplicate addresses permanently (until you run the {{<link url="#clear-duplicate-addresses" text="clear command">}}):

{{< tabs "TabID1135 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set evpn dad duplicate-action freeze duration permanent
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# dup-addr-detection freeze permanent
switch(config-router-af)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

### Clear Duplicate Addresses

You can clear a duplicate MAC or IP address (and unfreeze a frozen address). The following example command clears IP address 10.0.0.9 for VNI 101.

{{< tabs "TabID1175 ">}}
{{< tab "NVUE Commands ">}}

You cannot run NVUE commands to clear a duplicate MAC or IP address.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# clear evpn dup-addr vni 101 ip 10.0.0.9
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

To clear duplicate addresses for all VNIs, run the following command:

{{< tabs "TabID1203 ">}}
{{< tab "NVUE Commands ">}}

You cannot run NVUE commands to clear duplicate addresses.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# clear evpn dup-addr vni all
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- In an MLAG configuration, you need to run the clear command on both the MLAG primary and secondary switch.
- When you clear a duplicate MAC address, all its associated IP addresses also clear. However, you cannot clear an associated IP address if its MAC address is still in a duplicate state.
{{%/notice%}}

### Disable Duplicate Address Detection

Duplicate address detection is on by default. The switch generates a syslog error when it detects a duplicate address. To disable duplicate address detection, run the following command.

{{< tabs "TabID1238 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set evpn dad enable off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# no dup-addr-detection
switch(config-router-af)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

When you disable duplicate address detection, Cumulus Linux clears the configuration and all existing duplicate addresses.

### Show Detected Duplicate Address Information

During the duplicate address detection process, you can see the start time and current detection count with the vtysh `show evpn mac vni <vni_id> mac <mac_addr>` command. The following command example shows that detection starts for MAC address 00:01:02:03:04:11 for VNI 1001 on Tuesday, Nov 6 at 18:55:05 and Cumulus Linux detects one move.

```
cumulus@switch:~$ sudo vtysh
...
switch# show evpn mac vni 1001 mac 00:01:02:03:04:11
MAC: 00:01:02:03:04:11
  Intf: hostbond3(15) VLAN: 1001
  Local Seq: 1 Remote Seq: 0
  Duplicate detection started at Tue Nov  6 18:55:05 2018, detection count 1
  Neighbors:
    10.0.1.26 Active
```

After the duplicate MAC address clears, the vtysh `show evpn mac vni <vni_id> mac <mac_addr>` command shows:

```
MAC: 00:01:02:03:04:11
  Remote VTEP: 172.16.0.16
  Local Seq: 13 Remote Seq: 14
  Duplicate, detected at Tue Nov  6 18:55:29 2018
  Neighbors:
    10.0.1.26 Active
```

To display information for a duplicate IP address, run the vtysh `show evpn arp-cache vni <vni_id> ip <ip_addr>` command. The following command example shows information for IP address 10.0.0.9 for VNI 1001.

```
cumulus@switch:~$ sudo vtysh
...
switch# show evpn arp-cache vni 1001 ip 10.0.0.9
IP: 10.0.0.9
  Type: remote
  State: inactive
  MAC: 00:01:02:03:04:11
  Remote VTEP: 10.0.0.34
  Local Seq: 0 Remote Seq: 14
  Duplicate, detected at Tue Nov  6 18:55:29 2018
```

To show a list of MAC addresses detected as duplicate for a specific VNI or for all VNIs, run the vtysh `show evpn mac vni <vni-id|all> duplicate` command or the `net show evpn mac vni <vni-id|all> duplicate` command. The following example command shows a list of duplicate MAC addresses for VNI 1001:

```
cumulus@switch:~$ sudo vtysh
...
switch# show evpn mac vni 1001 duplicate
Number of MACs (local and remote) known for this VNI: 16
MAC               Type   Intf/Remote VTEP      VLAN
aa:bb:cc:dd:ee:ff local  hostbond3             1001
```

To show a list of IP addresses detected as duplicate for a specific VNI or for all VNIs, run the vtysh `show evpn arp-cache vni <vni-id|all> duplicate` command or the `net show evpn arp-cache vni <vni-id|all> duplicate` command. The following example command shows a list of duplicate IP addresses for VNI 1001:

```
cumulus@switch:~$ sudo vtysh
...
switch# show evpn arp-cache vni 1001 duplicate
Number of ARPs (local and remote) known for this VNI: 20
IP                Type   State    MAC                Remote VTEP
10.0.0.8          local  active   aa:11:aa:aa:aa:aa
10.0.0.9          local  active   aa:11:aa:aa:aa:aa
10.10.0.12        remote active   aa:22:aa:aa:aa:aa  172.16.0.16
```

To show configured duplicate address detection parameters, run the vtysh `show evpn` command or the `net show evpn` command:

```
cumulus@switch:~$ sudo vtysh
...
switch# show evpn
L2 VNIs: 4
L3 VNIs: 2
Advertise gateway mac-ip: No
Duplicate address detection: Enable
  Detection max-moves 7, time 300
  Detection freeze permanent
```
