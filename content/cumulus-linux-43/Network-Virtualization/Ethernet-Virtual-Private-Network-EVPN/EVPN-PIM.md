---
title: EVPN BUM Traffic with PIM-SM
author: NVIDIA
weight: 580
toc: 4
---
Without EVPN and PIM-SM, HER is the default way to replicate BUM traffic to remote VTEPs, where the ingress VTEP generates as many copies as VTEPs for each overlay BUM packet. This might not be optimal in certain deployments.

The following example shows a EVPN-PIM configuration, where underlay multicast is used to distribute BUM traffic. A multicast distribution tree (MDT) optimizes the flow of overlay BUM in the underlay network.

{{< img src = "/images/cumulus-linux/evpn-pim.png" >}}

In the above example, host01 sends an ARP request to resolve host03. leaf01 (in addition to flooding the packet to host02) sends an encapsulated packet over the underlay network, which is forwarded using the MDT to leaf02 and leaf03.

For PIM-SM, type-3 routes do not result in any forwarding entries. Cumulus Linux does **not** advertise type-3 routes for a layer 2 VNI when BUM mode for that VNI is PIM-SM.

{{%notice note%}}

EVPN-PIM is supported on Broadcom Trident3 and Trident 2+ switches, and Mellanox Spectrum, Spectrum-2 and Spectrum-3 switches.

{{%/notice%}}

## Configure Multicast VXLAN Tunnels

To configure multicast VXLAN tunnels, you need to configure PIM-SM in the underlay:

- Enable PIM-SM on the appropriate layer 3 interfaces.
- Configure static RP on all the PIM routers.
- Configure MSDP on the RPs for RP redundancy.

The configuration steps needed to configure PIM-SM in the underlay are provided in {{<link url="Protocol-Independent-Multicast-PIM">}}.

In addition to the PIM-SM configuration, you need to run the following commands on each VTEP to provide the layer 2 VNI to MDT mapping.

{{< tabs "TabID37 ">}}

{{< tab "NCLU Commands ">}}

Run the `net add vxlan <interface> vxlan mcastgrp <ip-address>` command. For example:

```
cumulus@switch:~$ net add vxlan vxlan1000111 vxlan mcastgrp 239.1.1.111
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add `vxlan-mcastgrp <ip-address>` to the interface stanza. For example:

```
cumulus@switch:~$ sudo vi /etc/network/interfaces
...
auto vxlan1000111
iface vxlan1000111
  vxlan-id 1000111
  vxlan-local-tunnelip 10.0.0.28
  vxlan-mcastgrp 239.1.1.111
```

Run the `ifreload -a` command to load the new configuration:

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ 
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

One multicast group per layer 2 VNI is optimal configuration for underlay bandwidth utilization. However, you can specify the same multicast group for more than one layer 2 VNI.

{{%/notice%}}

## Verify EVPN-PIM

Run the NCLU `net show mroute` command or the vtysh `show ip mroute` command to review the multicast route information in FRRouting. When using EVPN-PIM, every VTEP acts as both source and destination for a VNI-MDT group, therefore, mroute entries on each VTEP should look like this:

```
cumulus@switch:~$ net show mroute
Source          Group           Proto  Input            Output           TTL  Uptime
*               239.1.1.111     IGMP   swp2             pimreg           1    21:37:36
                                PIM                     ipmr-lo          1    21:37:36
10.0.0.28       239.1.1.111     STAR   lo               ipmr-lo          1    21:36:41
                                PIM                     swp2             1    21:36:41
*               239.1.1.112     IGMP   swp2             pimreg           1    21:37:36
                                PIM                     ipmr-lo          1    21:37:36
10.0.0.28       239.1.1.112     STAR   lo               ipmr-lo          1    21:36:41
                                PIM                     swp2             1    21:36:41
```

(*,G) entries should show `ipmr-lo` in the OIL (Outgoing Interface List) and (S,G) entries should show `lo` as the Source interface or incoming interface and `ipmr-lo` in the OIL.

Run the `ip mroute` command to review the multicast route information in the kernel. The kernel information should match the FRR information.

```
cumulus@switch:~$ ip mroute
(10.0.0.28,239.1.1.112)      Iif: lo     Oifs: swp2   State: resolved
(10.0.0.28,239.1.1.111)      Iif: lo     Oifs: swp2   State: resolved
(0.0.0.0,239.1.1.111)        Iif: swp2   Oifs: pimreg ipmr-lo swp2  State: resolved
(0.0.0.0,239.1.1.112)        Iif: swp2   Oifs: pimreg ipmr-lo swp2  State: resolved
```

Run the `bridge fdb show | grep 00:00:00:00:00:00` command to verify that all zero MAC addresses for every VXLAN device point to the correct multicast group destination.

```
cumulus@switch:~$ bridge fdb show | grep 00:00:00:00:00:00
00:00:00:00:00:00 dev vxlan1000112 dst 239.1.1.112 self permanent
00:00:00:00:00:00 dev vxlan1000111 dst 239.1.1.111 self permanent
```

{{%notice note%}}

The `show ip mroute count` command, often used to check multicast packet counts does *not* update for encapsulated BUM traffic originating or terminating on the VTEPs.

{{%/notice%}}

Run the NCLU `net show evpn vni <vni>` command or the vtysh `show evpn vni <vni>` command to ensure that your layer 2 VNI has the correct flooding information:

```
cumulus@switch:~$ net show evpn vni 10
VNI: 10
 Type: L2
 Tenant VRF: default
 VxLAN interface: vni10
 VxLAN ifIndex: 18
 Local VTEP IP: 10.0.0.28
 Mcast group: 239.1.1.112   <<<<<<<
 Remote VTEPs for this VNI:
  10.0.0.26 flood: -
  10.0.0.27 flood: -
 Number of MACs (local and remote) known for this VNI: 9
 Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 14
 Advertise-gw-macip: No
```

## Configure EVPN-PIM in VXLAN Active-active Mode

{{< img src = "/images/cumulus-linux/evpn-pim-anycast-vteps.png" >}}

To configure EVPN-PIM in VXLAN active-active mode, enable PIM on the peer link on each MLAG peer switch (**in addition to** the configuration described in {{<link url="#configure-multicast-vxlan-tunnels" text="Configure Multicast VXLAN Tunnels">}}, above).

{{< tabs "TabID318 ">}}

{{< tab "NCLU Commands ">}}

Run the `net add interface <peerlink> pim` command. For example:

```
cumulus@switch:~$ net add interface peerlink.4094 pim
cumulus@switch:~$ net commit
cumulus@switch:~$ net pending
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

In the vtysh shell, run the following commands:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# interface peerlink.4094
switch(config-if)# ip pim
switch(config-if)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ 
```

{{< /tab >}}

{{< /tabs >}}

## Example Configuration

The following example shows an EVPN-PIM configuration on the VTEP, where:

- PIM is enabled on swp1, swp2, and the loopback interface (shown in the example `/etc/frr/frr.conf` file below).
- The group mapping 192.168.0.1 is configured for a static RP (shown at the top of the `/etc/frr/frr.conf` file example below).
- Multicast group 239.1.1.111 is mapped to VXLAN1000111. Multicast group 239.1.1.112 is mapped to VXLAN1000112 (shown in the example `/etc/network/interfaces` file below).

{{< tabs "TabID87 ">}}

{{< tab "/etc/frr/frr.conf file ">}}

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
ip pim rp 192.168.0.1
ip pim keep-alive-timer 3600
...
vrf vrf1
 vni 104001
 exit-vrf
!
vrf vrf2
 vni 104002
 exit-vrf
!
interface swp1
 description swp1 > leaf-11's swp3
 ip ospf network point-to-point
 ip pim
!
interface swp2
 description swp2 > leaf-12's swp3
 ip ospf network point-to-point
 ip pim
!
interface swp3
 description swp3 > host-111's swp1
!
interface swp6
 description swp6 > host-112's swp1
!
interface lo
 ip pim
!
router bgp 650000
 bgp router-id 10.0.0.28
 bgp bestpath as-path multipath-relax
 bgp bestpath compare-routerid
 neighbor RR peer-group
 neighbor RR remote-as internal
 neighbor RR advertisement-interval 0
 neighbor RR timers 3 10
 neighbor RR timers connect 5
 neighbor 10.0.0.26 peer-group RR
 neighbor 10.0.0.26 update-source lo
 neighbor 10.0.0.27 peer-group RR
 neighbor 10.0.0.27 update-source lo
 !
 address-family ipv4 unicast
  redistribute connected
  maximum-paths ibgp 16
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor RR activate
  advertise-all-vni
 exit-address-family
!
router ospf
 ospf router-id 10.0.0.28
 network 10.0.0.28/32 area 0.0.0.0
!
line vty
 exec-timeout 0 0
!
end
```

{{< /tab >}}

{{< tab "/etc/network/interfaces file ">}}

```
cumulus@switch:~$ sudo cat /etc/network/interfaces
auto lo
iface lo
    address 10.0.0.28/32
# The primary network interface
auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1
    link-speed 10000
    link-duplex full
    link-autoneg off
    address 10.0.0.28/32

auto swp2
iface swp2
    link-speed 10000
    link-duplex full
    link-autoneg off
    address 10.0.0.28/32

auto swp3
iface swp3
    link-speed 10000
    link-duplex full
    link-autoneg off
    bridge-access 111

auto swp6
iface swp6
    link-speed 10000
    link-duplex full
    link-autoneg off
    bridge-access 112

auto vxlan1000111
iface vxlan1000111
    vxlan-id 1000111
    vxlan-local-tunnelip 10.0.0.28
    bridge-access 111
    vxlan-mcastgrp 239.1.1.111
auto vxlan1000112
iface vxlan1000112
    vxlan-id 1000112
    vxlan-local-tunnelip 10.0.0.28
    bridge-access 112
    vxlan-mcastgrp 239.1.1.112
auto vrf1
iface vrf1
    vrf-table auto
auto vrf2
iface vrf2
    vrf-table auto
auto vxlan104001
iface vxlan104001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.28
    bridge-access 4001
auto vxlan104002
iface vxlan104002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.28
    bridge-access 4002
auto bridge
iface bridge
    bridge-ports swp3 swp6 swp56s0 swp56s1 vxlan1000111 vxlan1000112 vxlan104001 vxlan104002
    bridge-vlan-aware yes
    bridge-vids 111 112 4001 4002
auto vlan111
iface vlan111
    address 10.1.1.11/24
    address 2060:1:1:1::11/64
    vlan-id 111
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 10.1.1.250/24 2060:1:1:1::250/64
    vrf vrf2
auto vlan112
iface vlan112
    address 50.1.1.11/24
    address 2050:1:1:1::11/64
    vlan-id 112
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 10.10.1.250/24 2050:1:1:1::250/64
    vrf vrf1
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2
```

{{< /tab >}}

{{< /tabs >}}
