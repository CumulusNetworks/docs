---
title: Troubleshooting
author: Cumulus Networks
weight: 818
toc: 3
---
Use the following commands to troubleshoot BGP.

## Basic Troubleshooting Commands

To show a summary of the BGP configuration on the switch, run the NCLU `net show bgp summary` command or the vtysh `show ip bgp summary`. For example:

```
cumulus@switch:~$ net show bgp summary
how bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0
BGP table version 13
RIB entries 25, using 4800 bytes of memory
Peers 5, using 106 KiB of memory
Peer groups 1, using 64 bytes of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
spine01(swp51)        4      65199      1614      1616        0    0    0 01:17:22            7
spine02(swp52)        4      65199      1614      1616        0    0    0 01:17:22            7
spine03(swp53)        4      65199      1613      1616        0    0    0 01:17:22            7
spine04(swp54)        4      65199      1613      1616        0    0    0 01:17:22            7
leaf02(peerlink.4094) 4      65101      1561      1564        0    0    0 01:17:21           12

Total number of neighbors 5


show bgp ipv6 unicast summary
=============================
% No BGP neighbors found
```

{{%notice tip%}}

To determine if the sessions above are iBGP or eBGP sessions, look at the ASNs.

{{%/notice%}}

To view the routing table as defined by BGP, run the NCLU `net show bgp ipv4 unicast` command or the vtysh `show ip bgp` command. For example:

```
cumulus@leaf01:~$ net show bgp ipv4 unicast
BGP table version is 13, local router ID is 10.10.10.1, vrf id 0
Default local pref 100, local AS 65101
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath,
               i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes:  i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
* i10.0.1.1/32      peerlink.4094            0    100      0 ?
*>                  0.0.0.0                  0         32768 ?
* i10.0.1.2/32      peerlink.4094                 100      0 65199 65102 ?
*=                  swp54                                  0 65199 65102 ?
*=                  swp52                                  0 65199 65102 ?
*>                  swp51                                  0 65199 65102 ?
*=                  swp53                                  0 65199 65102 ?
* i10.0.1.254/32    peerlink.4094                 100      0 65199 65132 ?
*=                  swp52                                  0 65199 65132 ?
*=                  swp53                                  0 65199 65132 ?
*=                  swp54                                  0 65199 65132 ?
*>                  swp51                                  0 65199 65132 ?
*> 10.10.10.1/32    0.0.0.0                  0         32768 ?
*>i10.10.10.2/32    peerlink.4094            0    100      0 ?
* i10.10.10.3/32    peerlink.4094                 100      0 65199 65102 ?
*=                  swp54                                  0 65199 65102 ?
*=                  swp53                                  0 65199 65102 ?
*=                  swp52                                  0 65199 65102 ?
*>                  swp51                                  0 65199 65102 ?
* i10.10.10.4/32    peerlink.4094                 100      0 65199 65102 ?
*=                  swp54                                  0 65199 65102 ?
*=                  swp53                                  0 65199 65102 ?
*=                  swp52                                  0 65199 65102 ?
*>                  swp51                                  0 65199 65102 ?
* i10.10.10.63/32   peerlink.4094                 100      0 65199 65132 ?
*=                  swp54                                  0 65199 65132 ?
*=                  swp53                                  0 65199 65132 ?
*=                  swp52                                  0 65199 65132 ?
*>                  swp51                                  0 65199 65132 ?
* i10.10.10.64/32   peerlink.4094                 100      0 65199 65132 ?
*=                  swp54                                  0 65199 65132 ?
*=                  swp53                                  0 65199 65132 ?
*=                  swp52                                  0 65199 65132 ?
*>                  swp51                                  0 65199 65132 ?
* i10.10.10.101/32  peerlink.4094            0    100      0 65199 ?
*>                  swp51                    0             0 65199 ?
* i10.10.10.102/32  peerlink.4094            0    100      0 65199 ?
*>                  swp52                    0             0 65199 ?
* i10.10.10.103/32  peerlink.4094            0    100      0 65199 ?
*>                  swp53                    0             0 65199 ?
* i10.10.10.104/32  peerlink.4094            0    100      0 65199 ?
*>                  swp54                    0             0 65199 ?

Displayed  13 routes and 42 total paths
```

To show a more detailed breakdown of a specific neighbor, run the NCLU `net show bgp neighbor <neighbor>` command or the vtysh `show ip bgp neighbor <neighbor>` command:

```
cumulus@switch:~$ net show bgp neighbor swp51
BGP neighbor on swp51: fe80::7c41:fff:fe93:b711, remote AS 65199, local AS 65101, external link
Hostname: spine01
 Member of peer-group underlay for session parameters
  BGP version 4, remote router ID 10.10.10.101, local router ID 10.10.10.1
  BGP state = Established, up for 01:22:18
  Last read 00:00:02, Last write 00:00:02
  Hold time is 9, keepalive interval is 3 seconds
  Neighbor capabilities:
    4 Byte AS: advertised and received
    AddPath:
      IPv4 Unicast: RX advertised IPv4 Unicast and received
      L2VPN EVPN: RX advertised L2VPN EVPN and received
    Extended nexthop: advertised and received
      Address families by peer:
                   IPv4 Unicast
    Route refresh: advertised and received(old & new)
    Address Family IPv4 Unicast: advertised and received
    Address Family L2VPN EVPN: advertised and received
    Hostname Capability: advertised (name: leaf01,domain name: n/a) received (name: spine01,domain name: n/a)
    Graceful Restart Capability: advertised
  Graceful restart information:
    Local GR Mode: Helper*
    Remote GR Mode: Disable
    R bit: False
    Timers:
      Configured Restart Time(sec): 120
      Received Restart Time(sec): 0
  Message statistics:
    Inq depth is 0
    Outq depth is 0
                         Sent       Rcvd
    Opens:                  2          1
    Notifications:          0          0
    Updates:               67         66
    Keepalives:          1646       1646
    Route Refresh:          0          0
    Capability:             0          0
    Total:               1715       1713
  Minimum time between advertisement runs is 0 seconds

 For address family: IPv4 Unicast
  underlay peer-group member
  Update group 2, subgroup 2
  Packet Queue length 0
  Community attribute sent to this neighbor(all)
  7 accepted prefixes
Local host: fe80::2294:15ff:fe02:7bbf, Local port: 179
Foreign host: fe80::7c41:fff:fe93:b711, Foreign port: 45548
Nexthop: 10.10.10.1
Nexthop global: fe80::2294:15ff:fe02:7bbf
Nexthop local: fe80::2294:15ff:fe02:7bbf
BGP connection: shared network
BGP Connect Retry Timer in Seconds: 10
Read thread: on  Write thread: on  FD used: 30
```

To see details of a specific route, such as from where it is received and where it is sent, run the NCLU `net show bgp <route>` command or the vtysh `show ip bgp <route>` command. For example:

```
cumulus@switch:~$ net show bgp 10.10.10.2/32
BGP routing table entry for 10.10.10.2/32
Paths: (1 available, best #1, table Default-IP-Routing-Table)
  Advertised to non peer-group peers:
  spine01(swp51) spine02(swp52)
  Local
    0.0.0.0 from 0.0.0.0 (10.10.10.2)
      Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, bestpath-from-AS Local, best
      AddPath ID: RX 0, TX 9
          Last update: Mon Oct 5 15:51:34 2020
```

The above example shows that the routing table prefix seen by BGP is 10.10.10.2/32, that this route is advertised to two neighbors, and that it is not heard by any neighbors.

### Log Neighbor State Changes

To log the changes that a neighbor goes through so that you can troubleshoot issues associated with that neighbor, run the `log-neighbor-changes` command. The output is sent to the specified log file, usually `/var/log/frr/bgpd.log`, and looks like this:

```
2016/07/08 10:12:06.572827 BGP: %NOTIFICATION: sent to neighbor 10.0.0.2 6/3 (Cease/Peer Unconfigured) 0 bytes
2016/07/08 10:12:06.572954 BGP: Notification sent to neighbor 10.0.0.2: type 6/3
2016/07/08 10:12:16.682071 BGP: %ADJCHANGE: neighbor 192.0.2.2 Up
2016/07/08 10:12:16.682660 BGP: %ADJCHANGE: neighbor 10.0.0.2 Up
```

### Troubleshoot Link-local Addresses

To verify that `frr` learned the neighboring link-local IPv6 address via the IPv6 neighbor discovery router advertisements on a given interface, run following commands. If `ipv6 nd suppress-ra` is not enabled on both ends of the interface, `Neighbor address(s):` has the other end's link-local address (the address that BGP uses when BGP is enabled on that interface).

{{%notice note%}}

IPv6 route advertisements (RAs) are automatically enabled on an interface with IPv6 addresses; the `no ipv6 nd suppress-ra` command is not needed for BGP unnumbered.

{{%/notice%}}

{{< tabs "60 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net show interface swp1
Interface swp1 is up, line protocol is up
  Link ups:       0    last: (never)
  Link downs:     0    last: (never)
  PTM status: disabled
  vrf: Default-IP-Routing-Table
  index 4 metric 0 mtu 1500
  flags: <UP,BROADCAST,RUNNING,MULTICAST>
  HWaddr: 44:38:39:00:00:5c
  inet6 fe80::4638:39ff:fe00:5c/64
  ND advertised reachable time is 0 milliseconds
  ND advertised retransmit interval is 0 milliseconds
  ND router advertisements are sent every 10 seconds
  ND router advertisements lifetime tracks ra-interval
  ND router advertisement default router preference is medium
  Hosts use stateless autoconfig for addresses.
  Neighbor address(s):
  inet6 fe80::4638:39ff:fe00:5b/128
```

Instead of the IPv6 address, the peering interface name is displayed in the `net show bgp summary` command and wherever else applicable:

```
cumulus@switch:~$ net show bgp summary
BGP router identifier 10.0.0.21, local AS number 65020 vrf-id 0
BGP table version 15
RIB entries 17, using 2040 bytes of memory
Peers 6, using 97 KiB of memory
Peer groups 1, using 56 bytes of memory

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
leaf01(swp1)    4 65011    2834    2843        0    0    0 02:21:35        2
leaf02(swp2)    4 65012    2834    2844        0    0    0 02:21:36        2
leaf03(swp3)    4 65013    2834    2843        0    0    0 02:21:35        2
leaf04(swp4)    4 65014    2834    2844        0    0    0 02:21:36        2
edge01(swp29)   4 65051    8509    8505        0    0    0 02:21:37        3
edge01(swp30)   4 65051    8506    8503        0    0    0 02:21:35        3

Total number of neighbors 6
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# show interface swp1
Interface swp1 is up, line protocol is up
  Link ups:       0    last: (never)
  Link downs:     0    last: (never)
  PTM status: disabled
  vrf: Default-IP-Routing-Table
  index 4 metric 0 mtu 1500
  flags: <UP,BROADCAST,RUNNING,MULTICAST>
  HWaddr: 44:38:39:00:00:5c
  inet6 fe80::4638:39ff:fe00:5c/64
  ND advertised reachable time is 0 milliseconds
  ND advertised retransmit interval is 0 milliseconds
  ND router advertisements are sent every 10 seconds
  ND router advertisements lifetime tracks ra-interval
  ND router advertisement default router preference is medium
  Hosts use stateless autoconfig for addresses.
  Neighbor address(s):
  inet6 fe80::4638:39ff:fe00:5b/128
```

Instead of the IPv6 address, the peering interface name is displayed in the `show ip bgp summary` command and wherever else applicable:

```
cumulus@switch:~$ sudo vtysh

switch# show ip bgp summary
BGP router identifier 10.0.0.21, local AS number 65020 vrf-id 0
BGP table version 15
RIB entries 17, using 2040 bytes of memory
Peers 6, using 97 KiB of memory
Peer groups 1, using 56 bytes of memory

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
leaf01(swp1)    4 65011    2834    2843        0    0    0 02:21:35        2
leaf02(swp2)    4 65012    2834    2844        0    0    0 02:21:36        2
leaf03(swp3)    4 65013    2834    2843        0    0    0 02:21:35        2
leaf04(swp4)    4 65014    2834    2844        0    0    0 02:21:36        2
edge01(swp29)   4 65051    8509    8505        0    0    0 02:21:37        3
edge01(swp30)   4 65051    8506    8503        0    0    0 02:21:35        3

Total number of neighbors 6
```

Most of the `show ip bgp` commands can take the interface name instead of the IP address:

```
cumulus@switch:~$ sudo vtysh

switch# show ip bgp neighbor swp51
BGP neighbor on swp51: fe80::4638:39ff:fe00:5c, remote AS 65020, local AS 65011, external link
Hostname: spine01
  Member of peer-group fabric for session parameters
  BGP version 4, remote router ID 0.0.0.0
  BGP state = Connect
  Last read 20:16:21, Last write 20:55:51
  Hold time is 30, keepalive interval is 10 seconds
  Configured hold time is 30, keepalive interval is 10 seconds
  Message statistics:
    Inq depth is 0
    Outq depth is 0
                          Sent       Rcvd
    Opens:                  1          1
    Notifications:          1          0
    Updates:                7          6
    Keepalives:          2374       2373
    Route Refresh:          0          0
    Capability:             0          0
    Total:               2383       2380
  Minimum time between advertisement runs is 5 seconds
  For address family: IPv4 Unicast
  fabric peer-group member
  Not part of any update group
  Community attribute sent to this neighbor(both)
  Inbound path policy configured
  Outbound path policy configured
  Incoming update prefix filter list is *dc-leaf-in
  Outgoing update prefix filter list is *dc-leaf-out
  0 accepted prefixes
  Connections established 1; dropped 1
  Last reset 20:16:20, due to NOTIFICATION sent (Cease/Other Configuration Change)
BGP Connect Retry Timer in Seconds: 3
Next connect timer due in 1 seconds
Read thread: on  Write thread: on
```

{{< /tab >}}

{{< /tabs >}}

### Troubleshoot BGP Unnumbered Configuration

Use the following commands to show IPv6 next hops and interface names for an IPv4 prefix, routes, and how a IPv4 link-local address is used to install a route and static neighbor entry.

All the relevant BGP commands show IPv6 next hops and/or the interface name for any IPv4 prefix. Run the NCLU `net show bgp` command or the vtysh `show ip bgp` command. For example:

```
cumulus@switch:~$ net show bgp

show bgp ipv4 unicast
=====================
BGP table version is 6, local router ID is 10.0.0.11
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
              i internal, r RIB-failure, S Stale, R Removed
Origin codes: i - IGP, e - EGP, ? - incomplete
    Network         Next Hop            Metric LocPrf Weight Path
*> 10.0.0.11/32     0.0.0.0                  0         32768 ?
*> 10.0.0.12/32     swp51                         0 65020 65012 ?
*=                  swp52                         0 65020 65012 ?
*> 10.0.0.21/32     swp51           0             0 65020 ?
*> 10.0.0.22/32     swp52           0             0 65020 ?
*> 172.16.1.0/24    0.0.0.0                  0         32768 i
*> 172.16.2.0/24    swp51                         0 65020 65012 i
*=                  swp52                         0 65020 65012 i
Total number of prefixes 6

show bgp ipv6 unicast
=====================
No BGP network exists
```

FRRouting RIB commands are also modified. Run the NCLU `net show route` command or the vtysh `show ip route` command. For example:

```
cumulus@switch:~$ net show route
RIB entry for route
===================
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, P - PIM, T - Table,
       > - selected route, * - FIB route
K>* 0.0.0.0/0 via 192.168.0.254, eth0
C>* 10.0.0.11/32 is directly connected, lo
B>* 10.0.0.12/32 [20/0] via fe80::4638:39ff:fe00:5c, swp51, 1d01h04m
  *                     via fe80::4638:39ff:fe00:2b, swp52, 1d01h04m
B>* 10.0.0.21/32 [20/0] via fe80::4638:39ff:fe00:5c, swp51, 1d01h04m
B>* 10.0.0.22/32 [20/0] via fe80::4638:39ff:fe00:2b, swp52, 1d01h04m
C>* 172.16.1.0/24 is directly connected, br0
B>* 172.16.2.0/24 [20/0] via fe80::4638:39ff:fe00:5c, swp51, 1d01h04m
  *                      via fe80::4638:39ff:fe00:2b, swp52, 1d01h04m
C>* 192.168.0.0/24 is directly connected, eth0
```

The following commands show how the IPv4 link-local address *169.254.0.1* is used to install the route and static neighbor entry to facilitate proper forwarding without having to install an IPv4 prefix with IPv6 next hop in the kernel. Run the NCLU `net show route <address>` command or the vtysh `show ip route <address>` command. For example:

```
cumulus@switch:~$ net show route 10.0.0.12
RIB entry for 10.0.0.12
=======================
Routing entry for 10.0.0.12/32
  Known via "bgp", distance 20, metric 0, best
  Last update 1d01h06m ago
  * fe80::4638:39ff:fe00:5c, via swp51
  * fe80::4638:39ff:fe00:2b, via swp52

FIB entry for 10.0.0.12
=======================
10.0.0.12  proto zebra  metric 20
  nexthop via 169.254.0.1  dev swp51 weight 1 onlink
  nexthop via 169.254.0.1  dev swp52 weight 1 onlink
```

### Show IPv4 Prefixes Learned with IPv6 Next Hops

To show IPv4 prefixes learned with IPv6 next hops, run the following commands:

{{< tabs "22 ">}}

{{< tab "NCLU Commands ">}}

The following examples show an IPv4 prefix learned from a BGP peer over an IPv6 session using IPv6 global addresses, but where the next hop installed by BGP is a link-local IPv6 address. This occurs when the session is directly between peers and both link-local and global IPv6 addresses are included as next hops in the BGP update for the prefix. If both global and link-local next hops exist, BGP prefers the link-local address for route installation.

```
cumulus@spine01:~$ net show bgp ipv4 unicast summary
BGP router identifier 10.0.0.11, local AS number 1 vrf-id 0
BGP table version 3
RIB entries 1, using 152 bytes of memory
Peers 1, using 19 KiB of memory

Neighbor            V AS MsgRcvd MsgSent TblVer InQ OutQ Up/Down  State/PfxRcd
Leaf01(2001:1:1::3) 4 3   6432    6431    0      0   0   05:21:25           1

Total number of neighbors 1
```

```
cumulus@spine01:~$ net show bgp ipv4 unicast
BGP table version is 3,
local router ID is 10.0.0.11
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
              i internal, r RIB-failure, S Stale, R Removed
Origin codes: i - IGP, e - EGP, ?   - incomplete

Network         Next Hop                 Metric LocPrf Weight Path
*> 172.16.3.0/24 fe80::a00:27ff:fea6:b9fe  0       0       3     i

Displayed 1 routes and 1 total paths
```

```
cumulus@spine01:~$ net show bgp ipv4 unicast 172.16.3.0/24
BGP routing table entry for 172.16.3.0/24
Paths: (1 available, best #1, table default)
  Advertised to non peer-group peers:
  Leaf01(2001:1:1::3)
  3
    2001:1:1::3 from Leaf01(2001:1:1::3) (10.0.0.13)
    (fe80::a00:27ff:fea6:b9fe) (used)
      Origin IGP, metric 0, valid, external, bestpath-from-AS 3, best (First path received)
      AddPath ID: RX 0, TX 3
      Last update: Mon Oct 22 08:09:22 2018
```

The example output below shows the results of installing the route in the FRR RIB as well as the kernel FIB. Note that the next hop used for installation in the FRR RIB is the link-local IPv6 address, but then it is converted into an IPv4 link-local address as required for installation into the kernel FIB.

```
cumulus@spine01:~$ net show route 172.16.3.0/24
RIB entry for 172.16.3.0/24
===========================
Routing entry for 172.16.3.0/24
  Known via "bgp", distance 20, metric 0, best
  Last update 2d17h05m ago
  * fe80::a00:27ff:fea6:b9fe, via swp1

FIB entry for 172.16.3.0/24
===========================
172.16.3.0/24 via 169.254.0.1 dev swp1 proto bgp metric 20 onlink
```

If an IPv4 prefix is learned with only an IPv6 global next hop address (for example, when the route is learned through a route reflector), the command output shows the IPv6 global address as the next hop value and shows that it is learned recursively through the link-local address of the route reflector. Note that when a global IPv6 address is used as a next hop for route installation in the FRR RIB, it is still converted into an IPv4 link-local address for installation into the kernel.

```
cumulus@leaf01:~$ net show bgp ipv4 unicast summary
BGP router identifier 10.0.0.13, local AS number 1 vrf-id 0
BGP table version 1
RIB entries 1, using 152 bytes of memory
Peers 1, using 19 KiB of memory

Neighbor             V AS MsgRcvd  MsgSent  TblVer  InQ  OutQ  Up/Down  State/PfxRcd
Spine01(2001:1:1::1) 4 1   74       68         0     0     0     00:00:45      1

Total number of neighbors 1
```

```
cumulus@leaf01:~$ net show bgp ipv4 unicast
  BGP table version is 1, local router ID is 10.0.0.13
  Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
                i internal, r RIB-failure, S Stale, R Removed
  Origin codes: i - IGP, e - EGP, ? - incomplete

Network Next Hop Metric LocPrf Weight Path
*>i172.16.4.0/24 2001:2:2::4 0 100 0 i

Displayed 1 routes and 1 total paths
```

```
cumulus@leaf01:~$ net show bgp ipv4 unicast 172.16.4.0/24
BGP routing table entry for 172.16.4.0/24
Paths: (1 available, best #1, table default)
  Not advertised to any peer
  Local
  2001:2:2::4 from Spine01(2001:1:1::1) (10.0.0.14)
    Origin IGP, metric 0, localpref 100, valid, internal, bestpath-from-AS Local, best (First path received)
    Originator: 10.0.0.14, Cluster list: 10.0.0.11
    AddPath ID: RX 0, TX 5
    Last update: Mon Oct 22 14:25:30 2018
```

```
cumulus@leaf01:~$ net show route 172.16.4.0/24
RIB entry for 172.16.4.0/24
===========================
Routing entry for 172.16.4.0/24
  Known via "bgp", distance 200, metric 0, best
  Last update 00:01:13 ago
  2001:2:2::4 (recursive)
  * fe80::a00:27ff:fe5a:84ae, via swp1

FIB entry for 172.16.4.0/24
===========================
172.16.4.0/24 via 169.254.0.1 dev swp1 proto bgp metric 20 onlink
```

To have only IPv6 global addresses used for route installation into the FRR RIB, you must add an additional route map to the neighbor or peer group statement in the appropriate address family. When the route map command `set ipv6 next-hop prefer-global` is applied to a neighbor, if both a link-local and global IPv6 address are in the BGP update for a prefix, the IPv6 global address is preferred for route installation.

With this additional configuration, the output in the FRR RIB changes in the direct neighbor case as shown below:

```
router bgp 1
  bgp router-id 10.0.0.11
  neighbor 2001:2:2::4 remote-as internal
  neighbor 2001:2:2::4 capability extended-nexthop
  !
  address-family ipv4 unicast
  neighbor 2001:2:2::4 route-map GLOBAL in
  exit-address-family
!
route-map GLOBAL permit 20
  set ipv6 next-hop prefer-global
!
```

The resulting FRR RIB output is as follows:

```
cumulus@leaf01:~$ net show route
Codes: K - kernel route, C - connected, S - static, R - RIP,
    O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
    T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
    F - PBR, 
    > - selected route, * - FIB route

B 0.0.0.0/0 [200/0] via 2001:2:2::4, swp2, 00:01:00
K 0.0.0.0/0 [0/0] via 10.0.2.2, eth0, 1d02h29m
C>* 10.0.0.9/32 is directly connected, lo, 5d18h32m
C>* 10.0.2.0/24 is directly connected, eth0, 03:51:31
B>* 172.16.4.0/24 [200/0] via 2001:2:2::4, swp2, 00:01:00
C>* 172.16.10.0/24 is directly connected, swp3, 5d18h32m
```

When the route is learned through a route reflector, it appears like this:

```
router bgp 1
  bgp router-id 10.0.0.13
  neighbor 2001:1:1::1 remote-as internal
  neighbor 2001:1:1::1 capability extended-nexthop
  !
  address-family ipv6 unicast
  neighbor 2001:1:1::1 activate
  neighbor 2001:1:1::1 route-map GLOBAL in
  exit-address-family
!
route-map GLOBAL permit 10
  set ipv6 next-hop prefer-global
```

```
cumulus@leaf01:~$ net show route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR,
       > - selected route, * - FIB route

B   0.0.0.0/0 [200/0] via 2001:2:2::4, 00:00:01
K   0.0.0.0/0 [0/0] via 10.0.2.2, eth0, 3d00h26m
C>* 10.0.0.8/32 is directly connected, lo, 3d00h26m
C>* 10.0.2.0/24 is directly connected, eth0, 03:39:18
C>* 172.16.3.0/24 is directly connected, swp2, 3d00h26m
B>  172.16.4.0/24 [200/0] via 2001:2:2::4 (recursive), 00:00:01
  *                         via 2001:1:1::1, swp1, 00:00:01
C>* 172.16.10.0/24 is directly connected, swp3, 3d00h26m
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

The following examples show an IPv4 prefix learned from a BGP peer over an IPv6 session using IPv6 global addresses, but where the next hop installed by BGP is a link-local IPv6 address. This occurs when the session is directly between peers and both link-local and global IPv6 addresses are included as next hops in the BGP update for the prefix. If both global and link-local next hops exist, BGP prefers the link-local address for route installation.

```
switch# show bgp ipv4 unicast summary
BGP router identifier 10.0.0.11, local AS number 1 vrf-id 0
BGP table version 3
RIB entries 1, using 152 bytes of memory
Peers 1, using 19 KiB of memory

Neighbor            V AS MsgRcvd MsgSent TblVer InQ OutQ Up/Down  State/PfxRcd
Leaf01(2001:1:1::3) 4 3   6432    6431    0      0   0   05:21:25           1

Total number of neighbors 1
```

```
switch# show bgp ipv4 unicast
BGP table version is 3,
local router ID is 10.0.0.11
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
              i internal, r RIB-failure, S Stale, R Removed
Origin codes: i - IGP, e - EGP, ?   - incomplete

  Network         Next Hop                 Metric LocPrf Weight Path
*> 172.16.3.0/24 fe80::a00:27ff:fea6:b9fe  0       0       3     i

Displayed 1 routes and 1 total paths
```

```
switch# show bgp ipv4 unicast 172.16.3.0/24
BGP routing table entry for 172.16.3.0/24
Paths: (1 available, best #1, table default)
  Advertised to non peer-group peers:
  Leaf01(2001:1:1::3)
  3
    2001:1:1::3 from Leaf01(2001:1:1::3) (10.0.0.13)
    (fe80::a00:27ff:fea6:b9fe) (used)
      Origin IGP, metric 0, valid, external, bestpath-from-AS 3, best
      AddPath ID: RX 0, TX 3
      Last update: Mon Oct 22 08:09:22 2018
```

The example output below shows the results of installing the route in the FRR RIB as well as the kernel FIB. Note that the next hop used for installation in the FRR RIB is the link-local IPv6 address, but then it is converted into an IPv4 link-local address as required for installation into the kernel FIB.

```
switch# show route 172.16.3.0/24
RIB entry for 172.16.3.0/24
===========================
Routing entry for 172.16.3.0/24
  Known via "bgp", distance 20, metric 0, best
  Last update 2d17h05m ago
  * fe80::a00:27ff:fea6:b9fe, via swp1

FIB entry for 172.16.3.0/24
===========================
172.16.3.0/24 via 169.254.0.1 dev swp1 proto bgp metric 20 onlink
```

If an IPv4 prefix is learned with only an IPv6 global next hop address (for example, when the route is learned through a route reflector), the command output shows the IPv6 global address as the next hop value and shows that it is learned recursively through the link-local address of the route reflector. Note that when a global IPv6 address is used as a next hop for route installation in the FRR RIB, it is still converted into an IPv4 link-local address for installation into the kernel.

```
switch# show bgp ipv4 unicast summary
BGP router identifier 10.0.0.13, local AS number 1 vrf-id 0
BGP table version 1
RIB entries 1, using 152 bytes of memory
Peers 1, using 19 KiB of memory

Neighbor             V AS MsgRcvd  MsgSent  TblVer  InQ  OutQ  Up/Down  State/PfxRcd
Spine01(2001:1:1::1) 4 1   74       68         0     0     0     00:00:45      1

Total number of neighbors 1

switch# show bgp ipv4 unicast
BGP table version is 1, local router ID is 10.0.0.13
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
              i internal, r RIB-failure, S Stale, R Removed
Origin codes: i - IGP, e - EGP, ? - incomplete
  
Network Next Hop Metric LocPrf Weight Path
*>i172.16.4.0/24 2001:2:2::4 0 100 0 i

Displayed 1 routes and 1 total paths

switch# show bgp ipv4 unicast 172.16.4.0/24
BGP routing table entry for 172.16.4.0/24
Paths: (1 available, best #1, table default)
  Not advertised to any peer
  Local
  2001:2:2::4 from Spine01(2001:1:1::1) (10.0.0.14)
    Origin IGP, metric 0, localpref 100, valid, internal, bestpath-from-AS Local, best
    Originator: 10.0.0.14, Cluster list: 10.0.0.11
    AddPath ID: RX 0, TX 5
    Last update: Mon Oct 22 14:25:30 2018

switch# show route 172.16.4.0/24
RIB entry for 172.16.4.0/24
===========================
Routing entry for 172.16.4.0/24
  Known via "bgp", distance 200, metric 0, best
  Last update 00:01:13 ago
  2001:2:2::4 (recursive)
  * fe80::a00:27ff:fe5a:84ae, via swp1

FIB entry for 172.16.4.0/24
===========================
172.16.4.0/24 via 169.254.0.1 dev swp1 proto bgp metric 20 onlink
```

To have only IPv6 global addresses used for route installation into the FRR RIB, you must add an additional route map to the neighbor or peer group statement in the appropriate address family. When the route map command `set ipv6 next-hop prefer-global` is applied to a neighbor, if both a link-local and global IPv6 address are in the BGP update for a prefix, the IPv6 global address is preferred for route installation.

With this additional configuration, the output in the FRR RIB changes in the direct neighbor case as shown below:

```
...
router bgp 1
  bgp router-id 10.0.0.11
  neighbor 2001:2:2::4 remote-as internal
  neighbor 2001:2:2::4 capability extended-nexthop
  !
  address-family ipv4 unicast
  neighbor 2001:2:2::4 route-map GLOBAL in
  exit-address-family
!
route-map GLOBAL permit 20
  set ipv6 next-hop prefer-global
!
...
```

The resulting FRR RIB output is as follows:

```
switch# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR,
       > - selected route, * - FIB route

B 0.0.0.0/0 [200/0] via 2001:2:2::4, swp2, 00:01:00
K 0.0.0.0/0 [0/0] via 10.0.2.2, eth0, 1d02h29m
C>* 10.0.0.9/32 is directly connected, lo, 5d18h32m
C>* 10.0.2.0/24 is directly connected, eth0, 03:51:31
B>* 172.16.4.0/24 [200/0] via 2001:2:2::4, swp2, 00:01:00
C>* 172.16.10.0/24 is directly connected, swp3, 5d18h32m
```

When the route is learned through a route reflector, it appears like
this:

```
router bgp 1
  bgp router-id 10.0.0.13
  neighbor 2001:1:1::1 remote-as internal
  neighbor 2001:1:1::1 capability extended-nexthop
  !
  address-family ipv6 unicast
  neighbor 2001:1:1::1 activate
  neighbor 2001:1:1::1 route-map GLOBAL in
  exit-address-family
!
route-map GLOBAL permit 10
  set ipv6 next-hop prefer-global

switch# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR,
       > - selected route, * - FIB route

B   0.0.0.0/0 [200/0] via 2001:2:2::4, 00:00:01
K   0.0.0.0/0 [0/0] via 10.0.2.2, eth0, 3d00h26m
C>* 10.0.0.8/32 is directly connected, lo, 3d00h26m
C>* 10.0.2.0/24 is directly connected, eth0, 03:39:18
C>* 172.16.3.0/24 is directly connected, swp2, 3d00h26m
B>  172.16.4.0/24 [200/0] via 2001:2:2::4 (recursive), 00:00:01
  *                         via 2001:1:1::1, swp1, 00:00:01
C>* 172.16.10.0/24 is directly connected, swp3, 3d00h26m
```

{{< /tab >}}

{{< /tabs >}}
