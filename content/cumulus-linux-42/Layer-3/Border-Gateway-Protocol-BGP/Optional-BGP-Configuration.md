---
title: Optional BGP Configuration
author: Cumulus Networks
weight: 814
toc: 3
---
This section describes optional configuration procedures. The steps provided in this section assume that you have followed the basic configuration steps described in {{<link url="Basic-BGP-Configuration" >}}.

## ECMP

BGP supports equal-cost multipathing (ECMP). If a BGP node hears a certain prefix from multiple peers, it has all the information necessary to program the routing table and forward traffic for that prefix through all of these peers. BGP typically choses one best path for each prefix and installs that route in the forwarding table.

In Cumulus Linux, the *BGP multipath* option is enabled by default with the maximum number of paths set to 64 so that the switch can install multiple equal-cost BGP paths to the forwarding table and load balance traffic across multiple links.

To change the number of paths allowed, run the following commands. The example commands change the maximum number of paths to 120. You can set a value between 1 and 256. 1 disables the BGP multipath option.

{{< tabs "297 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp maximum-paths 120
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# address-family ipv4
switch(config-router-af)# maximum-paths 120
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `address-family` stanza of the `/etc/frr/frr.conf` file. For example:

```
...
!
address-family ipv4 unicast
 network 10.1.10.0/24
 network 10.10.10.1/32
 maximum-paths 120
exit-address-family
...
```

When *BGP multipath* is enabled, only BGP routes from the same AS are load balanced. If the routes go across several different AS neighbors, even if the AS path length is same, they are not load balanced. To be able to load balance between multiple paths received from different AS neighbors, you need to set the *bestpath as-path multipath-relax* option.

{{< tabs "12 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp bestpath as-path multipath-relax
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# bgp bestpath as-path multipath-relax
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  bgp router-id 10.0.0.1
  bgp bestpath as-path multipath-relax
...
```

{{%notice note%}}

When you disable the *bestpath as-path multipath-relax* option, EVPN type-5 routes do not use the updated configuration. Type-5 routes continue to use all available ECMP paths in the underlay fabric, regardless of ASN.

{{%/notice%}}

## Route Reflectors

iBGP rules state that a route learned from an iBGP peer can not be sent to another iBGP peer. In a datacenter spine and leaf network using iBGP, this prevents a spine from sending a route learned from a leaf to any other leaf. As a workaround, BGP introduced the concept of a *route reflector* that selectively violates this rule; when an iBGP speaker is configured as a route reflector, it *can* send iBGP learned routes to other iBGP peers.

In the following example, spine01 is acting as a route reflector. The leaf switches, leaf01, leaf02 and leaf03 are *route reflector clients*. Any route that spine01 learns from a route reflector client is sent to other route reflector clients.

{{< img src = "/images/cumulus-linux/bgp-route-reflectors-example.png" >}}

To configure the BGP node as a route reflector, set the `route-reflector-client` option. The following example sets spine01 shown in the illustration above to be a route reflector for leaf01:

{{< tabs "344 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@spine01:~$ net add bgp neighbor 10.10.10.1 route-reflector-client
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@spine01:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65199
switch(config-router)# address-family ipv4
switch(config-router-af)# neighbor 10.10.10.1 route-reflector-client
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor 10.10.10.1 remote-as external
 !
 address-family ipv4 unicast
  network 10.10.10.101/32
  neighbor 10.10.10.1 route-reflector-client
 exit-address-family
...
```

{{%notice info%}}

- For IPv6, you must run the `route-reflector-client` command **after** the `activate` command; otherwise, the `route-reflector-client` command is ignored.
- In certain topologies that use BGP and route reflectors, next hop resolution might be impacted by advertising the spine-leaf link addresses from the leafs themselves. The problem is seen primarily with multiple links between each pair of spine and leaf switches, and redistribute connected configured on the leafs. To work around this issue, only advertise the spine to leaf addresses from the spine switches (or use IGP for next-hop propagation). You can use network statements for the interface addresses that you need to advertise to limit the addresses advertised by the leaf switches. Or, define redistribute connected with route maps to filter the outbound updates and remove the spine to leaf addresses from being sent from the leafs.

{{%/notice%}}

## Advertise IPv4 Prefixes with IPv6 Next Hops

{{<exlink url="https://tools.ietf.org/html/rfc5549" text="RFC 5549">}} defines the method used for BGP to advertise IPv4 prefixes with IPv6 next hops. The RFC does not make a distinction between whether the IPv6 peering and next hop values should be global unicast addresses (GUA) or link-local addresses. Cumulus Linux supports advertising IPv4 prefixes with IPv6 global unicast and link-local next hop addresses, with either *unnumbered* or *numbered* BGP.

When BGP peering uses IPv6 global addresses and IPv4 prefixes are being advertised and installed, IPv6 route advertisements are used to derive the MAC address of the peer so that FRR can create an IPv4 route with a link-local IPv4 next hop address (defined by RFC 3927). This is required to install the route into the kernel. These route advertisement settings are configured automatically when FRR receives an update from a BGP peer using IPv6 global addresses that contain an IPv4 prefix with an IPv6 next hop, and the enhanced-next hop capability has been negotiated.

To enable advertisement of IPv4 prefixes with IPv6 next hops over global IPv6 peerings, add the `extended-nexthop` capability to the global IPv6 neighbor statements on each end of the BGP sessions.

{{< tabs "18 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp neighbor 2001:db8:0002::0a00:0002 capability extended-nexthop
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# neighbor 2001:db8:0002::0a00:0002 capability extended-nexthop
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  ...
  neighbor 2001:db8:0002::0a00:0002 capability extended-nexthop
...
```

Ensure that the IPv6 peers are activated under the IPv4 unicast address family; otherwise, all peers are activated in the IPv4 unicast address family by default. If `no bgp default ipv4-unicast` is configured, you need to explicitly activate the IPv6 neighbor under the IPv4 unicast address family as shown below:

{{< tabs "20 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp neighbor 2001:db8:0002::0a00:0002 capability extended-nexthop
cumulus@switch:~$ net add bgp ipv4 unicast neighbor 2001:db8:0002::0a00:0002 activate
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# neighbor 2001:db8:0002::0a00:0002 capability extended-nexthop
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# neighbor 2001:db8:0002::0a00:0002 activate
switch(config-router-af)# end
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
router-id 10.10.10.1
no bgp default ipv4-unicast
neighbor 2001:db8:0002::0a00:0002 remote-as external
neighbor 2001:db8:0002::0a00:0002 capability extended-nexthop
!
address-family ipv4 unicast
  neighbor 2001:db8:0002::0a00:0002 activate
exit-address-family
...
```

## BGP add-path

Cumulus Linux supports both BGP add-path RX and BGP add-path TX.

### BGP add-path RX

*BGP add-path RX* allows BGP to receive multiple paths for the same prefix. A path identifier is used so that additional paths do not override previously advertised paths. No additional configuration is required for BGP add-path RX.

{{%notice note%}}

BGP advertises the add-path RX capability by default. Add-Path TX requires an administrator to enable it. Enabling TX resets the session.

{{%/notice%}}

To view the existing capabilities, run the NCLU `net show bgp neighbor` command or the vtysh `show ip bgp neighbors` command. The existing capabilities are listed in the subsection *Add Path*, below *Neighbor capabilities.*

```
cumulus@leaf01:~$ net show bgp neighbor
BGP neighbor is 10.10.10.101, remote AS 0, local AS 65101, external link
  BGP version 4, remote router ID 10.10.10.101, local router ID 10.10.10.1
  BGP state = Active
  Last read 00:04:13, Last write never
  Hold time is 9, keepalive interval is 3 seconds
  Neighbor capabilities:
    4 Byte AS: advertised and received
    AddPath:
      IPv4 Unicast: RX advertised IPv4 Unicast and received
    Extended nexthop: advertised and received
      Address families by peer:
                    IPv4 Unicast
    Route refresh: advertised and received(old & new)
    Address family IPv4 Unicast: advertised and received
    Hostname Capability: advertised and received
    Graceful Restart Capabilty: advertised and received
      Remote Restart timer is 120 seconds
      Address families by peer:
        none
...
```

The example output above shows that additional BGP paths can be sent and received (TX and RX are advertised). It also shows that the BGP neighbor, e80::7c41:fff:fe93:b711, supports both.

To view the current additional paths, run the NCLU `net show bgp <router-id>` command or the `vtysh show ip bgp <router-id>` command.

The example output shows an additional path that has been added by the TX node for receiving. Each path has a unique AddPath ID.

```
cumulus@leaf01:mgmt:~$ net show bgp 10.10.10.1
BGP routing table entry for 10.10.10.1/32
Paths: (1 available, best #1, table default)
  Advertised to non peer-group peers:
  spine01(swp51) spine02(swp52) spine03(swp53) spine04(swp54) leaf02(peerlink.4094)
  Local
    0.0.0.0 from 0.0.0.0 (10.10.10.1)
      Origin incomplete, metric 0, weight 32768, valid, sourced, bestpath-from-AS Local, best (First path received)
      Last update: Fri Oct  2 03:56:33 2020
```

### BGP add-path TX

AddPath TX allows BGP to advertise more than just the bestpath for a prefix. Consider the following topology:

```
          r8
          |
          |
  r1 ----    ---- r6
  r2 ---- r7 ---- r5
          ||
          ||
        r3 r4
```

In this topology:

- r1 and r2 are in AS 100
- r3 and r4 are in AS 300
- r5 and r6 are in AS 500
- r7 is in AS 700
- r8 is in AS 800
- r7 learns 1.1.1.1/32 from r1, r2, r3, r4, r5, and r6; r7 picks the path from r1 as the bestpath for 1.1.1.1/32

{{< tabs "28 ">}}

{{< tab "NCLU Commands ">}}

The example below configures the r7 session to advertise the bestpath learned from each AS. In this case, a path from AS 100, a path from AS 300, and a path from AS 500. The `net show bgp 1.1.1.1/32` from r7 has `bestpath-from-AS 100` so you can see what the bestpath is from each AS:

```
cumulus@r7:~$ net add bgp autonomous-system 700
cumulus@r7:~$ net add bgp neighbor 192.0.2.2 addpath-tx-bestpath-per-AS
cumulus@r7:~$ net pending
cumulus@r7:~$ net commit
```

The output below shows the result on r8:

```
cumulus@r8:~$ net show bgp 1.1.1.1/32
BGP routing table entry for 1.1.1.1/32
Paths: (3 available, best #3, table Default-IP-Routing-Table)
  Advertised to non peer-group peers:
  r7(10.7.8.1)
  700 100
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external
      Community: 1:1
      AddPath ID: RX 2, TX 4
      Last update: Thu Jun  2 00:57:14 2016

  700 300
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external
      Community: 3:3
      AddPath ID: RX 4, TX 3
      Last update: Thu Jun  2 00:57:14 2016

  700 500
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external, bestpath-from-AS 700, best (First path received)
      Community: 5:5
      AddPath ID: RX 6, TX 2
      Last update: Thu Jun  2 00:57:14 2016
```

The example below shows the results when r7 is configured to advertise all paths to r8:

```
cumulus@r7:~$ net add bgp autonomous-system 700
cumulus@r7:~$ net add bgp neighbor 192.0.2.2 addpath-tx-all-paths
cumulus@r7:~$ net pending
cumulus@r7:~$ net commit
```

The output below shows the result on r8:

```
cumulus@r8:~$ net show bgp 1.1.1.1/32
BGP routing table entry for 1.1.1.1/32
Paths: (3 available, best #3, table Default-IP-Routing-Table)
  Advertised to non peer-group peers:
  r7(10.7.8.1)
  700 100
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external
      Community: 1:1
      AddPath ID: RX 2, TX 4
      Last update: Thu Jun  2 00:57:14 2016

  700 300
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external
      Community: 3:3
      AddPath ID: RX 4, TX 3
      Last update: Thu Jun  2 00:57:14 2016

  700 500
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external, bestpath-from-AS 700, best (First path received)
      Community: 5:5
      AddPath ID: RX 6, TX 2
      Last update: Thu Jun  2 00:57:14 2016
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

The example below configures the r7 session to advertise the bestpath learned from each AS. In this case, a path from AS 100, a path from AS 300, and a path from AS 500. The `show ip bgp 1.1.1.1/32` from r7 has
`bestpath-from-AS 100` so you can see what the bestpath is from each AS:

```
cumulus@switch:~$ sudo vtysh

r7# configure terminal
r7(config)# router bgp 700
r7(config-router)# neighbor 192.0.2.2 addpath-tx-bestpath-per-AS
r7(config-router)#
```

The output below shows the result on r8:

```
cumulus@switch:~$ sudo vtysh

r8# show ip bgp 1.1.1.1/32
BGP routing table entry for 1.1.1.1/32
Paths: (3 available, best #3, table Default-IP-Routing-Table)
  Advertised to non peer-group peers:
  r7(10.7.8.1)
  700 100
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external
      Community: 1:1
      AddPath ID: RX 2, TX 4
      Last update: Thu Jun  2 00:57:14 2016

  700 300
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external
      Community: 3:3
      AddPath ID: RX 4, TX 3
      Last update: Thu Jun  2 00:57:14 2016

  700 500
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external, bestpath-from-AS 700, best
      Community: 5:5
      AddPath ID: RX 6, TX 2
      Last update: Thu Jun  2 00:57:14 2016

r8#
```

The example below shows the results when r7 is configured to advertise all paths to r8:

```
cumulus@switch:~$ sudo vtysh

r7# configure terminal
r7(config)# router bgp 700
r7(config-router)# neighbor 192.0.2.2 addpath-tx-all-paths
r7(config-router)#
```

The output below shows the result on r8:

```
cumulus@switch:~$ sudo vtysh

r8# show ip bgp 1.1.1.1/32
BGP routing table entry for 1.1.1.1/32
Paths: (3 available, best #3, table Default-IP-Routing-Table)
  Advertised to non peer-group peers:
  r7(10.7.8.1)
  700 100
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external
      Community: 1:1
      AddPath ID: RX 2, TX 4
      Last update: Thu Jun  2 00:57:14 2016

  700 300
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external
      Community: 3:3
      AddPath ID: RX 4, TX 3
      Last update: Thu Jun  2 00:57:14 2016

  700 500
    10.7.8.1 from r7(10.7.8.1) (10.0.0.7)
      Origin IGP, localpref 100, valid, external, bestpath-from-AS 700, best
      Community: 5:5
      AddPath ID: RX 6, TX 2
      Last update: Thu Jun  2 00:57:14 2016
```

{{< /tab >}}

{{< /tabs >}}

## BGP Dynamic Neighbors

*BGP dynamic neighbor* provides BGP peering to a group of remote neighbors within a specified range of IPv4 or IPv6 addresses for a BGP peer group. You can configure each range as a subnet IP address.

You configure dynamic neighbors using the `bgp listen range <ip-address> peer-group <group>` command. After you configure the dynamic neighbors, a BGP speaker can listen for, and form peer relationships with, any neighbor in the IP address range and mapped to a peer group.

{{< tabs "36 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp listen limit 5
cumulus@switch:~$ net add bgp listen range 10.10.10.100/24 peer-group SPINE
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The `net add bgp listen limit` command limits the number of dynamic peers. The default value is *100*.

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# bgp listen range 10.10.10.100/24 peer-group SPINE
switch(config-router)# bgp listen limit 5
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

The `bgp listen limit` command limits the number of dynamic peers. The default value is *100*.

{{< /tab >}}

{{< /tabs >}}

These commands produce an IPv4 configuration that looks like this:

```
router bgp 65101
  neighbor SPINE peer-group
  neighbor SPINE remote-as 65000
  bgp listen limit 5
  bgp listen range 10.10.10.100/24 peer-group SPINE
```

## MD5-enabled BGP Neighbors

You can authenticate your BGP peer connection to prevent interference with your routing tables.

To enable MD5 authentication for BGP peers, set the same password on the each peer.

The following example commands set the password *mypassword* on BGP peers leaf01 and spine01:

{{< tabs "40 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "1273 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 password mypassword
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add bgp neighbor swp1 password mypassword
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "vtysh Commands ">}}

{{< tabs "1295 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 password mypassword
leaf01(config-router)# exit
leaf01(config)# exit
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo vtysh

spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# neighbor swp1 password mypassword
spine01(config-router)# end
spine01# write memory
spine01# exit
cumulus@spine01:~$
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

You can confirm the configuration with the NCLU `net show bgp neighbor` command or the with the vtysh `show ip bgp neighbor` command. The following example shows that a session with the peer is established and that authentication is enabled (the output shows `Peer Authentication Enabled` towards the end):

```
cumulus@spine01:~$ net show bgp neighbor swp51
BGP neighbor on swp51: fe80::2294:15ff:fe02:7bbf, remote AS 65101, local AS 65199, external link
Hostname: leaf01
  BGP version 4, remote router ID 10.10.10.1, local router ID 10.10.10.101
  BGP state = Established, up for 00:00:39
  Last read 00:00:00, Last write 00:00:00
  Hold time is 9, keepalive interval is 3 seconds
  Neighbor capabilities:
    4 Byte AS: advertised and received
    AddPath:
      IPv4 Unicast: RX advertised IPv4 Unicast and received
    Route refresh: advertised and received(old & new)
    Address Family IPv4 Unicast: advertised and received
    Hostname Capability: advertised (name: spine01,domain name: n/a) received (name: leaf01,domain name: n/a)
    Graceful Restart Capability: advertised and received
      Remote Restart timer is 120 seconds
      Address families by peer:
        none
  Graceful restart information:
    End-of-RIB send: IPv4 Unicast
    End-of-RIB received: IPv4 Unicast
  Message statistics:
    Inq depth is 0
    Outq depth is 0
                         Sent       Rcvd
    Opens:                  2          2
    Notifications:          0          2
    Updates:              424        369
    Keepalives:           633        633
    Route Refresh:          0          0
    Capability:             0          0
    Total:               1059       1006
  Minimum time between advertisement runs is 0 seconds
  For address family: IPv4 Unicast
  Update group 1, subgroup 1
  Packet Queue length 0
  Community attribute sent to this neighbor(all)
  3 accepted prefixes
  Connections established 2; dropped 1
  Last reset 00:02:37,   Notification received (Cease/Other Configuration Change)
Local host: fe80::7c41:fff:fe93:b711, Local port: 45586
Foreign host: fe80::2294:15ff:fe02:7bbf, Foreign port: 179
Nexthop: 10.10.10.101
Nexthop global: fe80::7c41:fff:fe93:b711
Nexthop local: fe80::7c41:fff:fe93:b711
BGP connection: shared network
BGP Connect Retry Timer in Seconds: 10
Peer Authentication Enabled
Read thread: on  Write thread: on  FD used: 27
```

{{%notice note%}}

The MD5 password configured against a BGP listen-range peer group (used to accept and create dynamic BGP neighbors) is not enforced. This means that connections are accepted from peers that do not specify a password.

{{%/notice%}}

## eBGP Multihop

The eBGP multihop option lets you use BGP to exchange routes with an external peer that is more than one hop away.

To establish a connection between two eBGP peers that are not directly connected:

{{< tabs "42 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp neighbor 10.10.10.103 ebgp-multihop
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@spine01:~$ sudo vtysh

spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# neighbor 10.10.10.103 remote-as external
spine01(config-router)# neighbor 10.10.10.103 ebgp-multihop
spine01(config)# exit
spine01# write memory
spine01# exit
cumulus@spine01:~$
```

{{< /tab >}}

{{< /tabs >}}

## BGP TTL Security

Configure BGP TTL security to specify the minimum number of seconds allowed before the switch no longer accepts incoming IP packets from a specific eBGP peer. You can specify a value between 1 and 254 seconds.

To set BGP TTL security to 200 seconds on a switch:

{{< tabs "44 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor 10.10.10.101 ttl-security hops 200
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor 10.10.10.101 ttl-security hops 200
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

- When you configure BGP TTL security on a peer group instead of a specific neighbor, FRR does not add BGP `ttl-security` to either the running configuration or to the `/etc/frr/frr.conf` file. To work around this issue, add `ttl-security` to individual neighbors instead of the peer group.
- Enabling `ttl-security` does not program the hardware with relevant information. Frames are forwarded to the CPU and are dropped. Cumulus Networks recommends that you use the `net add acl` command to explicitly add the relevant entry to hardware. For example, configure a file, such as `/etc/cumulus/acl/policy.d/01control_plane_bgp.rules`, with a rule similar to the following:

   ```
   INGRESS_INTF = swp1
       INGRESS_CHAIN = INPUT, FORWARD

       [iptables]
       -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p tcp --dport bgp -m ttl --ttl 255 POLICE --set-mode pkt --set-rate 2000 --set-burst 1000
   -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p tcp --dport bgp DROP
   ```

   For more information about ACLs, see {{<link title="Netfilter - ACLs">}}.

{{%/notice%}}

## Graceful BGP Shutdown

To reduce packet loss during planned maintenance of a router or link, you can configure graceful BGP shutdown, which forces traffic to route around the node.

To configure graceful BGP shutdown:

{{< tabs "Graceful BGP shutdown">}}

{{< tab "NCLU Commands ">}}

To enable graceful shutdown:

```
cumulus@switch:~$ net add bgp graceful-shutdown
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To disable graceful shutdown:

```
cumulus@switch:~$ net del bgp graceful-shutdown
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

To enable graceful shutdown:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# bgp graceful-shutdown
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

To disable graceful shutdown:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# no bgp graceful-shutdown
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

When configured, the `graceful-shutdown` community is added to all paths from eBGP peers and the `local-pref` for that route is set to `0`. To see the configuration, run the NCLU `net show bgp <address>` command or the vtysh `show ip bgp <address>` command. For example:

```
cumulus@switch:~$ net show bgp 10.10.10.0/24
BGP routing table entry for 10.10.10.0/24
Paths: (2 available, best #1, table Default-IP-Routing-Table)
  Advertised to non peer-group peers:
  bottom0(10.10.10.2)
  30 20
    10.10.10.2 (metric 10) from top1(10.10.10.2) (10.10.10.2)
      Origin IGP, localpref 100, valid, internal, bestpath-from-AS 30, best
      Community: 99:1
      AddPath ID: RX 0, TX 52
      Last update: Mon Sep 18 17:01:18 2017

  20
    10.10.10.3 from bottom0(10.10.10.32) (10.10.10.10)
      Origin IGP, metric 0, localpref 0, valid, external, bestpath-from-AS 20
      Community: 99:1 graceful-shutdown
      AddPath ID: RX 0, TX 2
      Last update: Mon Sep 18 17:01:18 2017
```

## Enable Read-only Mode

As BGP peers are established and updates are received, prefixes might be installed in the RIB and advertised to BGP peers even though the information from all peers is not yet received and processed. Depending on the timing of the updates, prefixes might be installed and propagated through BGP, and then immediately withdrawn and replaced with new routing information. Read-only mode minimizes this BGP route churn in both the local RIB and with BGP peers.

Enable read-only mode to reduce CPU and network usage when you restart the BGP process, or when you issue the `clear` `ip bgp` command. Because intermediate best paths are possible for the same prefix as peers get established and start receiving updates at different times, read-only mode is particularly useful in topologies where BGP learns a prefix from many peers and the network has a high number of prefixes.

To enable read-only mode:

{{< tabs "48 ">}}

{{< tab "NCLU Commands ">}}

Run the `net add bgp update-delay <seconds> [<establish-wait-seconds>]` command, where the update delay and establish wait can be any value between 0 and 3600 seconds. The following example command enables read-only mode, sets the `max-delay` timer to 300 seconds and the `establish-wait` timer to 90 seconds.

```
cumulus@switch:~$ net add bgp update-delay 300 90
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

Run the `update-delay <seconds> [<establish-wait-seconds>]` command, where the update delay and establish wait can be any value between 0 and 3600 seconds. The following example command enables read-only mode, sets the `max-delay` timer to 300 seconds and the `establish-wait` timer to 90 seconds.

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp
switch(config-router)# update-delay 300 90
switch(config-router)# end
switch# write memory
switch# switch
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

The default value for max-delay is 0, which disables read-only mode. The `establish-wait` setting is optional; however, if specified, it must be shorter than the `max-delay`.

{{%/notice%}}

Read-only mode begins as soon as the first peer reaches its established state and the `max-delay` timer starts, and continues until either of the following two conditions are met:

- All the configured peers (except the shutdown peers) have sent an explicit EOR (End-Of-RIB) or an implicit EOR. The first keep-alive after BGP has reached the established state is considered an implicit EOR.  If you specify the `establish-wait` option, BGP only considers peers that have reached the established state from the moment the `max-delay` timer starts until the `establish-wait` period ends.

  The minimum set of established peers for which EOR is expected are the peers that are established during the `establish-wait window,` not necessarily all the configured neighbors.

- The timer reaches the configured `max-delay`.

While in read-only mode, BGP does not run best-path or generate any updates to its peers.

To show information about the state of the update delay, run the NCLU `net show bgp summary` command or the vtysh `show ip bgp summary` command.

## Apply a Route Map for Route Updates

You can apply {{<exlink url="http://docs.frrouting.org/en/latest/routemap.html" text="route maps">}} in BGP in one of two ways

- Filter routes from BGP into Zebra
- Filter routes from Zebra into the Linux kernel

{{%notice info%}}
In NCLU, you can only set the community number in a route map. You cannot set other community options such as `no-export`, `no-advertise`, or `additive`.

This is a known limitation in `network-docopt`, which NCLU uses to parse commands.
{{%/notice%}}

### Filter Routes from BGP into Zebra

You can apply a route map on route updates from BGP to Zebra. All the applicable match operations are allowed, such as match on prefix, next hop, communities, and so on. Set operations for this attach-point are limited to metric and next hop only. Any operation of this feature does not affect the BGP internal RIB.

Both IPv4 and IPv6 address families are supported. Route maps work on multi-paths; however, the metric setting is based on the best path only.

To apply a route map to filter route updates from BGP into Zebra, run the following command:

{{< tabs "50 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp table-map routemap1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp
switch(config-router)# table-map routemap1
switch(config-router)# end
switch# write memory
switch# switch
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

### Filter Routes from Zebra into the Linux Kernel

To apply a route map to filter route updates from Zebra into the Linux kernel, run the following commands:

{{< tabs "52 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add routing protocol bgp route-map routemap1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp
switch(config-router)# bgp route-map routemap1
switch(config-router)# end
switch# write memory
switch# switch
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

## BGP Community Lists

You can use *{{<exlink url="http://docs.frrouting.org/en/latest/bgp.html#community-lists" text="community lists">}}* to define a BGP community to tag one or more routes. You can then use the communities to apply acroute policy on either egress or ingress.

The BGP community list can be either *standard* or *expanded.* The standard BGP community list is a pair of values (such as *100:100*) that can be tagged on a specific prefix and advertised to other neighbors or applied on route ingress. Or, it can be one of four BGP default communities:

- *internet*: a BGP community that matches all routes
- *local-AS*: a BGP community that restricts routes to your confederation's sub-AS
- *no-advertise*: a BGP community that is not advertised to anyone
- *no-export*: a BGP community that is not advertised to the eBGP peer

An expanded BGP community list takes a regular expression of communities and matches the listed communities.

When the neighbor receives the prefix, it examines the community value and takes action accordingly, such as permitting or denying the community member in the routing policy.

Here is an example of a standard community list filter:

{{< tabs "54 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add routing community-list standard COMMUNITY1 permit 100:100
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# bgp community-list standard COMMUNITY1 permit 100:100
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

You can apply the community list to a route map to define the routing policy:

{{< tabs "Apply community list to route map">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp table-map ROUTE-MAP1
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# table-map ROUTE-MAP1
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

## Neighbor Maximum Prefixes

To configure the maximum number of route announcements (prefixes) that can be received from a BGP neighbor, run the `neighbor <peer> maximum-prefix <value>` command from the `vtysh` shell. For example:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65001
switch(config-router)# neighbor 10.10.10.101 maximum-prefix 3000
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

## Related Information

- {{<exlink url="https://tools.ietf.org/html/rfc4360" text="RFC 4360, BGP Extended Communities Attribute">}}
- {{<exlink url="https://tools.ietf.org/html/rfc4456" text="RFC 4456, BGP Route Reflection - An Alternative to Full Mesh Internal BGP (iBGP)">}}
