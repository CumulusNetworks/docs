---
title: GRE Tunneling
author: NVIDIA
weight: 970
toc: 3
---
<span class="a-tooltip">[GRE](## "Generic Routing Encapsulation")</span> is a tunneling protocol that encapsulates network layer protocols inside virtual point-to-point links over an Internet Protocol network. The tunnel source and tunnel destination addresses on each side identify the two endpoints.

GRE packets travel directly between the two endpoints through a virtual tunnel. As a packet comes across other routers, there is no interaction with its payload; the routers only parse the outer IP packet. When the packet reaches the endpoint of the GRE tunnel, the switch de-encapsulates the outer packet, parses the payload, then forwards it to its ultimate destination.

GRE uses multiple protocols over a single-protocol backbone and is less demanding than some of the alternative solutions, such as VPN. You can use GRE to transport protocols that the underlying network does not support, work around networks with limited hops, connect non-contiguous subnets, and allow VPNs across wide area networks.

{{%notice note%}}
- You can use only static IPv4 routes as a destination for the tunnel interface.
- You can only configure IPv4 endpoints.
- You can only configure point to point GRE tunnels; only one remote tunnel per interface.
- You cannot configure two tunnels with same local and remote tunnel IP address.
- GRE tunnels cannot coexist with VXLAN or MPLS on the switch.
- Cumulus Linux supports a maximum of 256 GRE tunnels.
- You can only configure GRE tunnels in the default VRF.
- GRE tunnels do not support layer 3 protocols, ECMP, QoS, ACLs or NAT.
- All GRE tunnels share the same <span class="a-tooltip">[TTL](## "Time to live")</span> value; Cumulus Linux uses the TTL value of the tunnel you configure last.
- You cannot configure the MTU on GRE tunnel interfaces. The GRE tunnel MTU is the maximum supported MTU on the switch by default.
{{%/notice%}}

The following example shows two sites that use IPv4 addresses. Using GRE tunneling, the two end points can encapsulate an IPv4 or IPv6 payload inside an IPv4 packet. The switch routes the packet based on the destination in the outer IPv4 header.

{{< img src = "/images/cumulus-linux/gre-tunnel-example.png" >}}

## Configure GRE Tunneling

To configure GRE tunneling, you create a GRE tunnel interface with routes for tunneling on both endpoints as follows:

- Create a tunnel interface by specifying an interface name, the tunnel mode as `gre`, the source (local) and destination (remote) underlay IP address, and the `ttl` (optional).
- Assign an IP address to the tunnel interface.
- Add route entries to encapsulate the packets using the tunnel interface.

The following configuration example shows the commands used to set up a bidirectional GRE tunnel between two endpoints: `tunnelR1` and `tunnelR2`. The local tunnel endpoint for `tunnelR1` is 10.10.10.1 and the remote endpoint is 10.10.10.3. The local tunnel endpoint for `tunnelR2` is 10.10.10.3 and the remote endpoint is 10.10.10.1.

{{< img src = "/images/cumulus-linux/gre-tunnel-config1.png" >}}

{{%notice note%}}
In NVUE, if you create the GRE interface with a name that starts with `tunnel`, NVUE automatically sets the interface type to `tunnel`. If you create a GRE interface with a name that does *not* start with `tunnel`, you must set the interface type to `tunnel` with the `nv set interface <interface-name> type tunnel` command.
{{%/notice%}}

{{< tabs "TabID35 ">}}
{{< tab "NVUE Commands">}}

{{< tabs "TabID38 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1 ip address 10.2.1.1/24
cumulus@leaf01:~$ nv set interface tunnelR2 ip address 10.1.100.1/30
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel mode gre
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel dest-ip 10.10.10.3
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel source-ip 10.10.10.1
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel ttl 255
cumulus@leaf01:~$ nv set vrf default router static 10.1.1.0/24 via tunnelR2
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ nv set interface swp1 ip address 10.1.1.1/24
cumulus@leaf03:~$ nv set interface tunnelR1 ip address 10.1.100.2/30
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel mode gre
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel dest-ip 10.10.10.1
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel source-ip 10.10.10.3
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel ttl 255
cumulus@leaf03:~$ nv set vrf default router static 10.2.1.0/24 via tunnelR1
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID58 ">}}
{{< tab "leaf01 ">}}

1. Edit the `/etc/network /interfaces` file to add the tunnel interface:

   ```
   cumulus@leaf01:~$ sudo nano /etc/network/interfaces
   ...
   auto lo
   iface lo inet loopback
      address 10.10.10.1/32
   auto swp1
   iface swp1
      address 10.2.1.1/24
   auto tunnelR2
   iface tunnelR2
      address 10.1.100.1/30
      tunnel-mode gre
      tunnel-local 10.10.10.1
      tunnel-endpoint 10.10.10.3
      tunnel-ttl 255
   ```

2. Run the `ifreload -a` command to load the configuration:

   ```
   cumulus@leaf01:mgmt:~$ sudo ifreload -a
   ```

3. Run vtysh commands to configure the static route:

   ```
   cumulus@leaf01:mgmt:~$ sudo vtysh
   ...
   leaf01# configure terminal
   leaf01(config)# ip route 10.1.1.0/24 tunnelR2
   leaf01(config)# exit
   leaf01# write memory
   leaf01# exit
   cumulus@leaf01:mgmt:~$
   ```

   The vtysh commands save the static route configuration in the `/etc/frr/frr.conf` file. For example:

   ```
   cumulus@leaf01:mgmt:~$ sudo cat /etc/frr/frr.conf
   ...
   vrf default
   ip route 10.1.1.0/24 tunnelR2
   exit-vrf
   ...
   ```

{{< /tab >}}
{{< tab "leaf03 ">}}

1. Edit the `/etc/network /interfaces` file to add the tunnel interface:

   ```
   cumulus@leaf03:~$ sudo nano /etc/network/interfaces
   ...
   auto lo
   iface lo inet loopback
      address 10.10.10.3/32
   auto swp1
   iface swp1
      address 10.1.1.1/24
   auto tunnelR1
   iface tunnelR1
      address 10.1.100.2/30
      tunnel-mode gre
      tunnel-local 10.10.10.3
      tunnel-endpoint 10.10.10.1
      tunnel-ttl 255
   ```

2. Run the `ifreload -a` command to load the configuration.

   ```
   cumulus@leaf03:mgmt:~$ sudo ifreload -a
   ```

3. Run vtysh commands to configure the static route:

   ```
   cumulus@leaf03:mgmt:~$ sudo vtysh
   ...
   leaf01# configure terminal
   leaf01(config)# ip route 10.2.1.0/24 tunnelR1
   leaf01(config)# exit
   leaf01# write memory
   leaf01# exit
   cumulus@leaf03:mgmt:~$
   ```

   The vtysh commands save the static route configuration in the `/etc/frr/frr.conf` file. For example:

   ```
   cumulus@leaf03:mgmt:~$ sudo cat /etc/frr/frr.conf
   ...
   vrf default
   ip route 10.2.1.0/24 tunnelR1
   exit-vrf
   vrf mgmt
   exit-vrf
   ...
   ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

To delete a GRE tunnel, remove the tunnel interface, and remove the routes configured with the tunnel interface. Either run the NVUE `nv unset` commands or remove the tunnel configuration from the `/etc/network/interfaces` file and run the `ifreload -a` command.

## Troubleshooting

To check GRE tunnel settings, run the NVUE `nv show interface <interface> tunnel` command, or run the Linux `ip tunnel show` or `ifquery --check` command. For example:

```
cumulus@leaf01:mgmt:~$ nv show interface tunnelR2 tunnel
           operational  applied     description
---------  -----------  ----------  -------------------------------
dest-ip    10.10.10.3   10.10.10.3  Destination underlay IP address
mode       gre          gre         tunnel mode
source-ip  10.10.10.1   10.10.10.1  Source underlay IP address
ttl                     255         time to live
```

```
cumulus@leaf01:mgmt:~$ ip tunnel show
gre0: gre/ip remote any local any ttl inherit nopmtudisc
tunnelR2: gre/ip remote 10.10.10.3 local 10.10.10.1 ttl 255
```

```
cumulus@leaf01:mgmt:~$ ifquery --check tunnelR2
auto tunnelR2
iface tunnelR2                                                      [pass]
        tunnel-mode gre                                             [pass]
        tunnel-local 10.10.10.1/32                                  [pass]
        tunnel-endpoint 10.10.10.3/32                               [pass]
        tunnel-ttl 255                                              [pass]
        address 10.1.100.1/30                                       [pass]
```

## Configuration Example

This example uses the {{<link url="Reference-Topology" text="reference topology">}}, and uses spine01 and spine02 to represent the transit IPv4 network to connect the GRE endpoints.

{{< tabs "TabID233 ">}}
{{< tab "NVUE ">}}

{{< tabs "TabID236 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1 ip address 10.2.1.1/24
cumulus@leaf01:~$ nv set interface swp1,51-52
cumulus@leaf01:~$ nv set interface tunnelR2 ip address 10.1.100.1/30
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel mode gre
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel dest-ip 10.10.10.3
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel source-ip 10.10.10.1
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel ttl 255
cumulus@leaf01:~$ nv set vrf default router static 10.1.1.0/24 via tunnelR2
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ nv set interface swp1 ip address 10.1.1.1/24
cumulus@leaf03:~$ nv set interface swp1,51-52
cumulus@leaf03:~$ nv set interface tunnelR1 ip address 10.1.100.2/30
cumulus@leaf01:~$ nv set interface tunnelR1 tunnel mode gre
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel dest-ip 10.10.10.1
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel source-ip 10.10.10.3
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel ttl 255
cumulus@leaf03:~$ nv set vrf default router static 10.2.1.0/24 via tunnelR1
cumulus@leaf03:~$ nv set router bgp autonomous-system 65103
cumulus@leaf03:~$ nv set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.3/32
cumulus@leaf03:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf03:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1,3
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp3 remote-as external
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ nv set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp1,3
cumulus@spine02:~$ nv set router bgp autonomous-system 65199
cumulus@spine02:~$ nv set router bgp router-id 10.10.10.102
cumulus@spine02:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.102/32
cumulus@spine02:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine02:~$ nv set vrf default router bgp neighbor swp3 remote-as external
cumulus@spine02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

{{< tabs "TabID257 ">}}
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
        ip:
          address:
            10.2.1.1/24: {}
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      tunnelR2:
        ip:
          address:
            10.1.100.1/30: {}
        tunnel:
          dest-ip: 10.10.10.3
          mode: gre
          source-ip: 10.10.10.1
          ttl: 255
        type: tunnel
    router:
      bgp:
        autonomous-system: 65101
        enable: on
        router-id: 10.10.10.1
    system:
      hostname: leaf01
    vrf:
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.10.10.1/32: {}
            enable: on
            neighbor:
              swp51:
                remote-as: external
                type: unnumbered
              swp52:
                remote-as: external
                type: unnumbered
          static:
            10.1.1.0/24:
              address-family: ipv4-unicast
              via:
                tunnelR2:
                  type: interface
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
        ip:
          address:
            10.1.1.1/24: {}
        type: swp
      swp51:
        type: swp
      swp52:
        type: swp
      tunnelR1:
        ip:
          address:
            10.1.100.2/30: {}
        tunnel:
          dest-ip: 10.10.10.1
          mode: gre
          source-ip: 10.10.10.3
          ttl: 255
        type: tunnel
    router:
      bgp:
        autonomous-system: 65103
        enable: on
        router-id: 10.10.10.3
    system:
      hostname: leaf03
    vrf:
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.10.10.3/32: {}
            enable: on
            neighbor:
              swp51:
                remote-as: external
                type: unnumbered
              swp52:
                remote-as: external
                type: unnumbered
          static:
            10.2.1.0/24:
              address-family: ipv4-unicast
              via:
                tunnelR1:
                  type: interface
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
      swp3:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.101
    system:
      hostname: spine01
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
              swp3:
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
      swp3:
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.102
    system:
      hostname: spine02
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
              swp3:
                remote-as: external
                type: unnumbered
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces">}}

{{< tabs "TabID523 ">}}
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
    address 10.2.1.1/24
auto swp51
iface swp51
auto swp52
iface swp52
auto tunnelR2
iface tunnelR2
    address 10.1.100.1/30
    tunnel-mode gre
    tunnel-local 10.10.10.1
    tunnel-endpoint 10.10.10.3
    tunnel-ttl 255
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
    address 10.1.1.1/24
auto swp51
iface swp51
auto swp52
iface swp52
auto tunnelR1
iface tunnelR1
    address 10.1.100.2/30
    tunnel-mode gre
    tunnel-local 10.10.10.3
    tunnel-endpoint 10.10.10.1
    tunnel-ttl 255
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
auto swp3
iface swp3
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
auto swp3
iface swp3
```

{{< /tab >}}
{{< tab "server01 ">}}

```
cumulus@server01:mgmt:~$ sudo cat /etc/network/interfaces
auto eth0
iface eth0 inet dhcp
  post-up sysctl -w net.ipv6.conf.eth0.accept_ra=2
auto eth1
iface eth1
 address 10.2.1.2/24
 post-up ip route add 10.0.0.0/8 via 10.2.1.1
```

{{< /tab >}}
{{< tab "server04 ">}}

```
cumulus@server04:mgmt:~$ sudo cat /etc/network/interfaces
auto eth0
iface eth0 inet dhcp
  post-up sysctl -w net.ipv6.conf.eth0.accept_ra=2
auto eth1
iface eth1
 address 10.1.1.2/24
 post-up ip route add 10.0.0.0/8 via 10.1.1.1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf">}}

{{< tabs "TabID689 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/frr/frr.conf
...
vrf default
ip route 10.1.1.0/24 tunnelR2
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
network 10.10.10.1/32
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
exit-address-family
! end of router bgp 65101 vrf default
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:mgmt:~$ sudo cat /etc/frr/frr.conf
...
vrf default
ip route 10.2.1.0/24 tunnelR1
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
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
exit-address-family
! end of router bgp 65103 vrf default
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
neighbor swp3 interface remote-as external
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.10.10.101/32
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp3 activate
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
neighbor swp3 interface remote-as external
neighbor swp3 timers 3 9
neighbor swp3 timers connect 10
neighbor swp3 advertisement-interval 0
neighbor swp3 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.10.10.102/32
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp3 activate
exit-address-family
! end of router bgp 65199 vrf default
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Try It " >}}
    {{< simulation name="Try It CL54 - GRE" showNodes="leaf01,leaf03,spine01,spine02,server01,server04" >}}

This simulation starts with the example GRE configuration. The demo is pre-configured using {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/" text="NVUE">}} commands.

To validate the configuration, run the commands listed in the troubleshooting section.

{{< /tab >}}
{{< /tabs >}}
