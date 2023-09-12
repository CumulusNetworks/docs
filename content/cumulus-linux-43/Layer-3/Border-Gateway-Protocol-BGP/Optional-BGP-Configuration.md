---
title: Optional BGP Configuration
author: NVIDIA
weight: 860
toc: 3
---
This section describes optional configuration. The steps provided in this section assume that you already configured basic BGP as described in {{<link url="Basic-BGP-Configuration" >}}.

## Peer Groups

Instead of specifying properties of each individual peer, you can define one or more peer groups and associate all the attributes common to that peer session to a peer group. A peer needs to be attached to a peer group only once, when it then inherits all address families activated for that peer group.

{{%notice note%}}

If the peer you want to add to a group already exists in the BGP configuration, delete it first, than add it to the peer group.

{{%/notice%}}

The following example commands create a peer group called SPINE that includes two external peers.

{{< tabs "34 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor SPINE peer-group
cumulus@leaf01:~$ net add bgp neighbor SPINE remote-as external
cumulus@leaf01:~$ net add bgp neighbor 10.0.1.0 peer-group SPINE
cumulus@leaf01:~$ net add bgp neighbor 10.0.1.12 peer-group SPINE
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor SPINE peer-group
leaf01(config-router)# neighbor SPINE remote-as external
leaf01(config-router)# neighbor 10.0.1.0 peer-group SPINE
leaf01(config-router)# neighbor 10.0.1.12 peer-group SPINE
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$

```

{{< /tab >}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer-group SPINE
cumulus@leaf01:~$ cl set vrf default router bgp peer-group SPINE remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp peer 10.0.1.0 peer-group SPINE
cumulus@leaf01:~$ cl set vrf default router bgp peer 10.0.1.12 peer-group SPINE
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

For an unnumbered configuration, you can use a single command to configure a neighbor and attach it to a peer group.

{{< tabs "16 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 interface peer-group SPINE
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
leaf01(config-router)# neighbor swp51 interface peer-group SPINE
```

{{< /tab >}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 peer-group SPINE
```

{{< /tab >}}
{{< /tabs >}}

## BGP Dynamic Neighbors

*BGP dynamic neighbor* provides BGP peering to a group of remote neighbors within a specified range of IPv4 or IPv6 addresses for a BGP peer group. You can configure each range as a subnet IP address.

You configure dynamic neighbors using the `bgp listen range <ip-address> peer-group <group>` command. After you configure the dynamic neighbors, a BGP speaker can listen for, and form peer relationships with, any neighbor that is in the IP address range and is mapped to a peer group.

The following example commands create the peer group SPINE and configure BGP peering to remote neighbors within the address range 10.0.1.0/31.

{{< tabs "36 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor SPINE peer-group
cumulus@leaf01:~$ net add bgp neighbor SPINE remote-as external
cumulus@leaf01:~$ net add bgp listen range 10.0.1.0/24 peer-group SPINE
cumulus@leaf01:~$ net add bgp listen limit 5
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The `net add bgp listen limit` command limits the number of dynamic peers. The default value is *100*.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp listen range 10.0.1.0/24 peer-group SPINE
leaf01(config-router)# bgp listen limit 5
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

The `bgp listen limit` command limits the number of dynamic peers. The default value is *100*.

{{< /tab >}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer-group SPINE
cumulus@leaf01:~$ cl set vrf default router bgp peer-group SPINE remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp peer-group SPINE NEED COMMAND
cumulus@leaf01:~$ cl set vrf default router bgp listen limit 5
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
router bgp 65101
  neighbor SPINE peer-group
  neighbor SPINE remote-as external
  bgp listen limit 5
  bgp listen range 10.0.1.0/24 peer-group SPINE
```

## eBGP Multihop

The eBGP multihop option lets you use BGP to exchange routes with an external peer that is more than one hop away.

To establish a connection between two eBGP peers that are not directly connected:

{{< tabs "42 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor 10.10.10.101 remote-as external
cumulus@leaf01:~$ net add bgp neighbor 10.10.10.101 ebgp-multihop
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor 10.10.10.101 remote-as external
leaf01(config-router)# neighbor 10.10.10.101 ebgp-multihop
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer 10.10.10.101 remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp peer 10.10.10.101 NEED COMMAND
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

## BGP TTL Security Hop Count

You can use the TTL security hop count option to prevent attacks against eBGP, such as denial of service (DoS) attacks.
By default, BGP messages are sent to eBGP neighbors with an IP time-to-live (TTL) of 1, which requires the peer to be directly connected, otherwise, the packets expire along the way. (You can adjust the TTL with the {{<link url="#ebgp-multihop" text="eBGP multihop">}} option.) An attacker can easily adjust the TTL of packets so that they appear to be originating from a peer that is directly connected.

The BGP TTL security hops option inverts the direction in which the TTL is counted. Instead of accepting only packets with a TTL set to 1, only BGP messages with a TTL greater than or equal to 255 minus the specified hop count are accepted.

When TTL security is in use, eBGP multihop is no longer needed.

The following command example sets the TTL security hop count value to 200:

{{< tabs "44 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 ttl-security hops 200
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 ttl-security hops 200
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 multihop-ttl 200
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  ...
  neighbor swp51 ttl-security hops 200
...
```

{{%notice note%}}

- When you configure `ttl-security hops` on a peer group instead of a specific neighbor, FRR does not add it to either the running configuration or to the `/etc/frr/frr.conf` file. To work around this issue, add `ttl-security hops` to individual neighbors instead of the peer group.
- Enabling `ttl-security hops` does not program the hardware with relevant information. Frames are forwarded to the CPU and are dropped. Use the `net add acl` command to explicitly add the relevant entry to hardware. For more information about ACLs, see {{<link title="Netfilter - ACLs">}}.

{{%/notice%}}

## MD5-enabled BGP Neighbors

You can authenticate your BGP peer connection to prevent interference with your routing tables.

To enable MD5 authentication for BGP peers, set the same password on each peer.

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
leaf01(config-router)# end
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

{{< tab "CUE Commands ">}}

{{< tabs "350 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 password mypassword
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cl set vrf default router bgp peer swp1 password mypassword
cumulus@spine01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

You can confirm the configuration with the NCLU `net show bgp neighbor <neighbor>` command, the `vtysh` command `show ip bgp neighbor <neighbor>`, or the CUE `cl show vrf <vrf> router bgp peer <neighbor>` command.

{{< expand "net show bgp neighbor <neighbor> example" >}}

The following example shows that a session with the peer is established and that authentication is enabled. The output shows `Peer Authentication Enabled` towards the end.

```
cumulus@spine01:~$ net show bgp neighbor swp1
BGP neighbor on swp1: fe80::2294:15ff:fe02:7bbf, remote AS 65101, local AS 65199, external link
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

{{< /expand >}}

{{%notice note%}}

The MD5 password configured against a BGP listen-range peer group (used to accept and create dynamic BGP neighbors) is not enforced; connections are accepted from peers that do not specify a password.

{{%/notice%}}

## Remove Private BGP ASNs

If you use private ASNs in the data center, any routes you send out to the internet contain your private ASNs. You can remove all the private ASNs from routes to a specific neighbor.

The following example command removes private ASNs from routes sent to the neighbor on swp51 (an unnumbered interface):

{{< tabs "445 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 remove-private-AS
```

You can replace the private ASNs with your public ASN with the following command:

```
cumulus@leaf01:~$ net add bgp neighbor swp51 remove-private-AS replace-AS
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 NEED COMMAND
cumulus@leaf01:~$ cl config apply
```

You can replace the private ASNs with your public ASN with the following command:

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 NEED COMMAND
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

## Multiple BGP ASNs

Cumulus Linux supports the use of distinct ASNs for different VRF instances.

The following example configures VRF RED and VRF BLUE on border01 to use ASN 65532 towards fw1 and 65533 towards fw2:

{{< img src = "/images/cumulus-linux/asn-vrf-config.png" >}}

{{< tabs "400 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@border01:~$ net add bgp vrf RED autonomous-system 65532        
cumulus@border01:~$ net add bgp vrf RED router-id 10.10.10.63
cumulus@border01:~$ net add bgp vrf RED neighbor swp3 interface remote-as external
cumulus@border01:~$ net add bgp vrf BLUE autonomous-system 65533 
cumulus@border01:~$ net add bgp vrf BLUE router-id 10.10.10.63
cumulus@border01:~$ net add bgp vrf BLUE neighbor swp4 interface remote-as external
cumulus@border01:~$ net pending
cumulus@border01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@border01:~$ sudo vtysh

border01# configure terminal
border01(config)# router bgp 65532 vrf RED
border01(config-router)# bgp router-id 10.10.10.63
border01(config-router)# neighbor swp3 interface remote-as external
border01(config-router)# exit
border01(config)# router bgp 65533 vrf BLUE
border01(config-router)# bgp router-id 10.10.10.63
border01(config-router)# neighbor swp4 interface remote-as external
border01(config-router)# end
border01# write memory
border01# exit
cumulus@border01:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@border01:~$ cl set vrf RED router bgp autonomous-system 65532        
cumulus@border01:~$ cl set vrf RED router bgp router-id 10.10.10.63
cumulus@border01:~$ cl set vrf RED router bgp peer swp3 interface remote-as external NEED COMMAND
cumulus@border01:~$ cl set vrf BLUE router bgp autonomous-system 65533 
cumulus@border01:~$ cl set vrf BLUE router bgp router-id 10.10.10.63
cumulus@border01:~$ cl set vrf BLUE router bgp peer swp4 interface remote-as external NEED COMMAND
cumulus@border01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

The following example shows the `/etc/frr/frr.conf` configuration for border01.

```
cumulus@border01:~$ cat /etc/frr/frr.conf
...
log syslog informational
!
vrf RED
  vni 4001
vrf BLUE
  vni 4002
!
router bgp 65132
 bgp router-id 10.10.10.63
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
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
router bgp 65532 vrf RED
 bgp router-id 10.10.10.63
 neighbor swp3 remote-as external
 !
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
router bgp 65533 vrf BLUE
 bgp router-id 10.10.10.63
 neighbor swp4 remote-as external
 !
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
line vty
```

With the above configuration, the `net show bgp vrf RED summary` command shows the local ASN as 65532.

```
cumulus@border01:mgmt:~$ net show bgp vrf RED summary
show bgp vrf RED ipv4 unicast summary
=========================================
BGP router identifier 10.10.10.63, local AS number 65532 vrf-id 35
BGP table version 1
RIB entries 1, using 192 bytes of memory
Peers 1, using 21 KiB of memory

Neighbor      V      AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
fw1(swp3)     4   65199      2015      2015        0    0    0 01:40:36            1        1

Total number of neighbors 1
...
```

The `net show bgp summary` command displays the global table, where the local ASN 65132 is used to peer with spine01.

```
cumulus@border01:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.63, local AS number 65132 vrf-id 0
BGP table version 3
RIB entries 5, using 960 bytes of memory
Peers 1, using 43 KiB of memory
Peer groups 1, using 64 bytes of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
spine01(swp51)  4      65199      2223      2223        0    0    0 01:50:18            1        3

Total number of neighbors 1
...
```

## ECMP

BGP supports equal-cost multipathing ({{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP" text="ECMP">}}). If a BGP node hears a certain prefix from multiple peers, it has all the information necessary to program the routing table and forward traffic for that prefix through all of these peers. BGP typically choses one best path for each prefix and installs that route in the forwarding table.

In Cumulus Linux, the *BGP multipath* option is enabled by default with the maximum number of paths set to 64 so that the switch can install multiple equal-cost BGP paths to the forwarding table and load balance traffic across multiple links. You can change the number of paths allowed, according to your needs.

The example commands change the maximum number of paths to 120. You can set a value between 1 and 256. 1 disables the BGP multipath option.

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

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ NEED COMMAND
cumulus@border01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `address-family` stanza of the `/etc/frr/frr.conf` file. For example:

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

When *BGP multipath* is enabled, only BGP routes from the same AS are load balanced. If the routes go across several different AS neighbors, even if the AS path length is the same, they are not load balanced. To be able to load balance between multiple paths received from different AS neighbors, you need to set the `bestpath as-path multipath-relax` option.

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

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ NEED COMMAND
cumulus@border01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

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

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set vrf default router bgp peer 2001:db8:0002::0a00:0002 NEED COMMAND (maybe address-family ipv6-unicast nexthop-setting?????)
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

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
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set vrf default router bgp peer 2001:db8:0002::0a00:0002 NEED COMMAND (maybe address-family ipv6-unicast nexthop-setting?????)
cumulus@switch:~$ cl set vrf default router bgp peer 2001:db8:0002::0a00:0002 address-family ipv4-unicast enable on?????
cumulus@switch:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

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

## Neighbor Maximum Prefixes

To protect against an internal network connectivity disruption caused by BGP, you can control how many route announcements (prefixes) can be received from a BGP neighbor.

The following example commands set the maximum number of prefixes allowed from the BGP neighbor on swp51 to 3000:

{{< tabs "878 ">}}

{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65001
leaf01(config-router)# neighbor swp51 maximum-prefix 3000
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set vrf default router bgp peer swp51 NEED COMMAND
cumulus@switch:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

## Aggregate Addresses

To minimize the size of the routing table and save bandwidth, you can aggregate a range of networks in your routing table into a single prefix.

The following example command aggregates a range of addresses, such as 10.1.1.0/24, 10.1.2.0/24, 10.1.3.0/24 into the single prefix 10.1.0.0/16.

{{< tabs "913 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp aggregate-address 10.1.0.0/16
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The `summary-only` option ensures that longer-prefixes inside the aggregate address are suppressed before sending BGP updates:

```
cumulus@switch:~$ net add bgp aggregate-address 10.1.0.0/16 summary-only
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

CUE commands are not provided.

{{< /tab >}}

{{< /tabs >}}

<!--## Suppress Route Advertisement

You can configure BGP to wait for a response from the RIB indicating that the routes installed in the RIB are also installed in the ASIC before sending updates to peers.

{{< tabs "TabID784 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp wait-for-install
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# bgp suppress-fib-pending
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

CUE commands are not provided.

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp51 remote-as external
 bgp suppress-fib-pending
...
```

The {{<link url="Smart-System-Manager" text="Smart System Manager">}} suppresses route advertisement automatically when upgrading or troubleshooting an active switch so that there is minimal disruption to the network.-->

## BGP add-path

Cumulus Linux supports both BGP add-path RX and BGP add-path TX.

### BGP add-path RX

BGP add-path RX allows BGP to receive multiple paths for the same prefix. A path identifier is used so that additional paths do not override previously advertised paths. BGP add-path RX is enabled by default; no additional configuration is required.

To view the existing capabilities, run the NCLU command `net show bgp neighbor` or the `vtysh` command `show ip bgp neighbors`. The existing capabilities are listed in the subsection *Add Path*, below *Neighbor capabilities.*

The following example output shows that additional BGP paths can be sent and received and that the BGP neighbor on swp51 supports both.

```
cumulus@leaf01:~$ net show bgp neighbor
BGP neighbor on swp51: fe80::7c41:fff:fe93:b711, remote AS 65199, local AS 65101, external link
Hostname: spine01
  BGP version 4, remote router ID 10.10.10.101, local router ID 10.10.10.1
  BGP state = Established, up for 1d12h39m
  Last read 00:00:03, Last write 00:00:01
  Hold time is 9, keepalive interval is 3 seconds
  Neighbor capabilities:
    4 Byte AS: advertised and received
    AddPath:
      IPv4 Unicast: RX advertised IPv4 Unicast and received
    Extended nexthop: advertised and received
      Address families by peer:
                   IPv4 Unicast
    Route refresh: advertised and received(old & new)
    Address Family IPv4 Unicast: advertised and received
    Hostname Capability: advertised (name: leaf01,domain name: n/a) received (name: spine01,domain name: n/a)
    Graceful Restart Capability: advertised and received
...
```

To view the current additional paths, run the NCLU command `net show bgp <prefix>` or the `vtysh` command `show ip bgp <prefix>`. The example output shows an additional path that has been added by the TX node for receiving. Each path has a unique AddPath ID.

```
cumulus@leaf01:mgmt:~$ net show bgp 10.10.10.9
BGP routing table entry for 10.10.10.9/32
Paths: (2 available, best #1, table Default-IP-Routing-Table)
  Advertised to non peer-group peers:
  spine01(swp51) spine02(swp52)
  65020 65012
    fe80::4638:39ff:fe00:5c from spine01(swp51) (10.10.10.12)
    (fe80::4638:39ff:fe00:5c) (used)
      Origin incomplete, localpref 100, valid, external, multipath, bestpath-from-AS 65020, best (Older Path)
      AddPath ID: RX 0, TX 6
      Last update: Wed Nov 16 22:47:00 2016
  65020 65012
    fe80::4638:39ff:fe00:2b from spine02(swp52) (10.10.10.12)
    (fe80::4638:39ff:fe00:2b) (used)
      Origin incomplete, localpref 100, valid, external, multipath
      AddPath ID: RX 0, TX 3
      Last update: Fri Oct  2 03:56:33 2020
```

### BGP add-path TX

BGP add-path TX enables BGP to advertise more than just the best path for a prefix. Cumulus Linux includes two options:
- `addpath-tx-all-paths` advertises all known paths to a neighbor
- `addpath-tx-bestpath-per-AS` advertises only the best path learned from each AS to a neighbor

The following example commands configure leaf01 to advertise the best path learned from each AS to the BGP neighbor on swp50:

{{< tabs "897 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp autonomous-system 65101
cumulus@leaf01:~$ net add bgp neighbor swp50 addpath-tx-bestpath-per-AS
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp50 addpath-tx-bestpath-per-AS
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$ 
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set vrf default router bgp peer swp50 NEED COMMAND
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

The following example commands configure leaf01 to advertise all paths learned from each AS to the BGP neighbor on swp50:

{{< tabs "927 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp autonomous-system 65101
cumulus@leaf01:~$ net add bgp neighbor swp50 addpath-tx-all-paths
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp50 addpath-tx-all-paths
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$ 
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set vrf default router bgp peer swp50 NEED COMMAND
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

The following example configuration shows how BGP add-path TX is used to advertise the best path learned from each AS.
<!-- vale off -->
| <div style="width:500px">   |    |
| -- | -- |
| {{< img src = "/images/cumulus-linux/bgp-add-path-tx.png" >}} | In this configuration:<ul><li>Every leaf and every spine has a different ASN</li><li>eBGP is configured between:<ul><li>leaf01 and spine01, spine02</li><li>leaf03 and spine01, spine02</li><li>leaf01 and leaf02 (leaf02 only has a single peer, which is leaf01)</li></ul><li>leaf01 is configured to advertise the best path learned from each AS to BGP neighbor leaf02</li><li>leaf03 generates a loopback IP address (10.10.10.3/32) into BGP with a network statement</li></ul>|
<!-- vale on -->
When you run the `net show bgp 10.10.10.3/32` command on leaf02, the command output shows the leaf03 loopback IP address and that two BGP paths are learned, both from leaf01:

```
cumulus@leaf02:mgmt:~$ net show bgp 10.10.10.3/32
BGP routing table entry for 10.10.10.3/32
Paths: (2 available, best #2, table default)
       Advertised to non peer-group peers:
       leaf01(swp50)
  65101 65199 65103
    fe80::4638:39ff:fe00:13 from leaf01(swp50) (10.10.10.1)
    (fe80::4638:39ff:fe00:13) (used)
      Origin IGP, valid, external
      AddPath ID: RX 4, TX-All 0 TX-Best-Per-AS 0
      Last update: Thu Oct 15 18:31:46 2020
  65101 65198 65103
    fe80::4638:39ff:fe00:13 from leaf01(swp50) (10.10.10.1)
    (fe80::4638:39ff:fe00:13) (used)
      Origin IGP, valid, external, bestpath-from-AS 65101, best (Nothing left to compare)
      AddPath ID: RX 3, TX-All 0 TX-Best-Per-AS 0
      Last update: Thu Oct 15 18:31:46 2020
```

## BGP Timers

BGP includes several timers that you can configure.

### Keepalive Interval and Hold Time

By default, BGP exchanges periodic keepalive messages to measure and ensure that a peer is still alive and functioning. If a keepalive or update message is not received from the peer within the hold time, the peer is declared down and all routes received by this peer are withdrawn from the local BGP table. By default, the keepalive interval is set to 3 seconds and the hold time is set to 9 seconds. To decrease CPU load, especially in the presence of a lot of neighbors, you can increase the values of these timers or disable the exchange of keepalives entirely. When manually configuring new values, the keepalive interval can be less than or equal to one third of the hold time, but cannot be less than 1 second. Setting the keepalive and hold time values to 0 disables the exchange of keepalives.

The following example commands set the keepalive interval to 10 seconds and the hold time to 30 seconds.

{{< tabs "64 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 timers 10 30
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp
leaf01(config-router)# neighbor swp51 timers 10 30
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 timers keepalive 10
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 timers hold 30
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  ...
  neighbor swp51 timers 10 30
...
```

### Reconnect Interval

By default, the BGP process attempts to connect to a peer after a failure (or on startup) every 10 seconds. You can change this value to suit your needs.

The following example commands set the reconnect value to 30 seconds:

{{< tabs "204 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 timers connect 30
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp
leaf01(config-router)# neighbor swp51 timers connect 30
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 timers connection-retry 30
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:
```
...
router bgp 65101
  ...
  neighbor swp51 timers connect 30
...
```

### Advertisement Interval

After making a new best path decision for a prefix, BGP can optionally insert a delay before advertising the new results to a peer. This delay is used to rate limit the amount of changes advertised to downstream peers and lowers processing requirements by slowing down convergence. By default, this interval is set to 0 seconds for both eBGP and iBGP sessions, which allows for very fast convergence. For more information about the advertisement interval, see {{<exlink url="http://tools.ietf.org/html/draft-jakma-mrai-02" text="this IETF draft">}}.

The following example commands set the advertisement interval to 5 seconds:

{{< tabs "68 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 advertisement-interval 5
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp
leaf01(config-router)# neighbor swp51 advertisement-interval 5
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 timers route-advertisement 5
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  ...
  neighbor swp51 advertisement-interval 5
...
```

### Wait for Convergence

BGP *wait for convergence* lets you delay the initial best path calculation after you reboot the switch, restart FRR, or run the vtysh `clear ip bgp *` command. This allows peers to become established and converge before BGP installs the resulting routes in zebra or sends updates to peers.

To enable BGP wait for convergence, you configure the following BGP timers globally:

| <div style="width:200px">Timer | Description |
| ----- | ----------- |
| `update-delay` | The longest BGP waits for all eligible peers to converge. A peer is considered converged if it reaches the established state and sends an explicit or implicit EoR. |
| `establish-wait`| Optional. The time by which peers must reach the established state to be considered for convergence. This guards against extremely slow peers or peers that are configured but not reachable.<br><br>Peers that are locally shutdown are not considered for the convergence event.|

BGP *wait for convergence* is run automatically by the {{<link url="Smart-System-Manager" text="Smart System Manager">}} to upgrade or troubleshoot an active switch with minimal disruption to the network.

{{%notice note%}}
- The `update-delay` and `establish-wait` timers are used by all VRFs, including the default VRF and any VRFs that you add later.
- You can set the `update-delay` timer per VRF. However, you cannot set the timer *both* globally and per VRF. If a VRF (including the default VRF) is configured with the `update-delay` timer, you must delete it before configuring the timer globally.
{{%/notice%}}

The following example commands set the `update-delay` timer to 300 seconds and the `establish-wait` timer to 200 seconds:

{{< tabs "TabID12 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add routing bgp update-delay 300 establish-wait 200
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# update-delay 300 200
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

CUE commands are not provided.

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp51 remote-as external
 bgp update-delay 300 200
...
```

To show the configured timers and information about the transitions when a convergence event occurs, run the NCLU `net show bgp summary` command or the vtysh `show ip bgp summary` command.

```
cumulus@leaf01:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0
Read-only mode update-delay limit: 300 seconds
                   Establish wait: 200 seconds
BGP table version 0
RIB entries 3, using 576 bytes of memory
Peers 1, using 21 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
spine01(swp51)  4      65199     30798     30802        0    0    0 1d01h09m            0        0

Total number of neighbors 1
...
```

The last convergence event is retained in the output of the NCLU `net show bgp summary json` command or the vtysh `show ip bgp summary json` command.

## Route Reflectors

iBGP rules state that a route learned from an iBGP peer can not be sent to another iBGP peer. In a data center spine and leaf network using iBGP, this prevents a spine from sending a route learned from a leaf to any other leaf. As a workaround, BGP introduced the concept of a *route reflector* that selectively ignores this rule so that when an iBGP speaker is configured as a route reflector, it *can* send iBGP learned routes to other iBGP peers.

In the following example, spine01 is acting as a route reflector. The leaf switches, leaf01, leaf02 and leaf03 are *route reflector clients*. Any route that spine01 learns from a route reflector client is sent to other route reflector clients.

{{< img src = "/images/cumulus-linux/bgp-route-reflectors-example.png" >}}

To configure the BGP node as a route reflector for a BGP peer, set the neighbor `route-reflector-client` option. The following example sets spine01 shown in the illustration above to be a route reflector for leaf01 (on swp1), which is a route reflector client. No configuration is required on the client.

{{< tabs "344 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@spine01:~$ net add bgp neighbor swp1 route-reflector-client
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@spine01:~$ sudo vtysh

spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# address-family ipv4
spine01(config-router-af)# neighbor swp1 route-reflector-client
spine01(config-router-af)# end
spine01# write memory
spine01# exit
cumulus@spine01:~$
```

{{< /tab >}}
{{< tab "CUE Commands ">}}

```
cumulus@spine01:~$ cl set vrf default router bgp peer swp1 address-family ipv4-unicast route-reflector-client on
cumulus@spine01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp51 remote-as external
 !
 address-family ipv4 unicast
  network 10.10.10.101/32
  neighbor swp51 route-reflector-client
 exit-address-family
...
```

{{%notice info%}}
When configuring BGP for IPv6, you must run the `route-reflector-client` command **after** the NCLU or vtysh `activate` command; otherwise, the `route-reflector-client` command is ignored. STILL THE CASE FOR CUE COMMAND??????
{{%/notice%}}

## Administrative Distance

Cumulus Linux uses the administrative distance to choose which routing protocol to use when two different protocols provide route information for the same destination. The smaller the distance, the more reliable the protocol. For example, if the switch receives a route from OSPF with an administrative distance of 110 and the same route from BGP with an administrative distance of 100, the switch chooses BGP.

The following example commands set the administrative distance for routes from 10.10.10.101 to 100:

{{< tabs "1489 ">}}
{{< tab "vtysh Commands ">}}

```
cumulus@spine01:~$ sudo vtysh

spine01# configure terminal
spine01(config)# router bgp 65101
spine01(config-router)# distance 100 10.10.10.101/32
spine01(config-router)# end
spine01# write memory
spine01# exit
cumulus@spine01:~$
```

{{< /tab >}}
{{< tab "CUE Commands ">}}

```
cumulus@spine01:~$ cl set vrf default router bgp peer NEED COMMAND
cumulus@spine01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

The following example commands set the administrative distance for routes external to the AS to 150, routes internal to the AS to 110, and local routes to 100:

{{< tabs "1514 ">}}
{{< tab "vtysh Commands ">}}

```
cumulus@spine01:~$ sudo vtysh

spine01# configure terminal
spine01(config)# router bgp 65101
spine01(config-router)# distance bgp 150 110 100
spine01(config-router)# end
spine01# write memory
spine01# exit
cumulus@spine01:~$
```

{{< /tab >}}
{{< tab "CUE Commands ">}}

CUE commands are not provided.

{{< /tab >}}
{{< /tabs >}}

## Graceful BGP Shutdown

To reduce packet loss during planned maintenance of a router or link, you can configure graceful BGP shutdown, which forces traffic to route around the BGP node:

{{< tabs "Graceful BGP shutdown">}}
{{< tab "NCLU Commands ">}}

To enable graceful shutdown:

```
cumulus@leaf01:~$ net add bgp graceful-shutdown
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

To disable graceful shutdown:

```
cumulus@leaf01:~$ net del bgp graceful-shutdown
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To enable graceful shutdown:

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp graceful-shutdown
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

To disable graceful shutdown:

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# no bgp graceful-shutdown
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set router bgp graceful-shutdown on
cumulus@leaf01:~$ cl config apply
```

To disable graceful shutdown:

```
cumulus@leaf01:~$ cl set router bgp graceful-shutdown off
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

When configured, the `graceful-shutdown` community is added to all inbound and outbound routes from eBGP peers and the `local-pref` for that route is set to `0` (refer to {{<exlink url="https://datatracker.ietf.org/doc/html/rfc8326" text="RFC8326">}}). To see the configuration, run the NCLU command `net show bgp <route>` or the `vtysh` command `show ip bgp <route>`. For example:

```
cumulus@leaf01:~$ net show bgp 10.10.10.0/24
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

As optional configuration, you can create a route map to do a prepend AS so that reduced preference using a longer AS path can be propagated to other parts of network.

{{< expand "Example Configuration Using a Route Map" >}}

```
router bgp 65101
 bgp router-id 10.10.10.1
 bgp graceful-restart
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor swp51 interface remote-as external

 address-family ipv4 unicast
  redistribute connected
  neighbor swp51 route-map prependas out
 exit-address-family

bgp community-list standard gshut seq 5 permit graceful-shutdown

route-map prependas permit 10
 match community gshut exact-match
 set as-path prepend 65101

route-map prependas permit 20
```

With the above configuration, the peer sees:

```
cumulus@spine01:~$ net show bgp 10.10.10.1/32
BGP routing table entry for 10.10.10.1/32
Paths: (1 available, best #1, table default)
Advertised to non peer-group peers:
65101 65101
10.10.10.1 from leaf01(10.10.10.1) (10.10.10.1)
Origin incomplete, metric 0, localpref 0, valid, external, bestpath-from-AS 65101, best (First path received)
Community: graceful-shutdown
Last update: Sun Dec 20 03:04:53 2020
```

{{< /expand >}}

## Graceful BGP Restart

When BGP restarts on a switch, all BGP peers detect that the session goes down and comes back up. This session transition results in a routing flap on BGP peers that causes BGP to recompute routes, generate route updates, and add unnecessary churn to the forwarding tables. The routing flaps can create transient forwarding blackholes and loops, and also consume resources on the switches affected by the flap, which can affect overall network performance.

To help minimize the negative effects that occur when BGP restarts, you can enable the BGP graceful restart feature. This enables a BGP speaker to signal to its peers that it can preserve its forwarding state and continue data forwarding during a restart. It also enables a BGP speaker to continue to use routes previously announced by a peer even after the peer has gone down.

When a BGP session is established, BGP peers use the BGP OPEN message to negotiate a graceful restart. If the BGP peer also supports graceful restart, it is activated for that neighbor session. If the BGP session is lost, the BGP peer (the restart helper) flags all routes associated with the device as stale but continues to forward packets to these routes for a certain period of time. The restarting device also continues to forward packets during the graceful restart. After it comes back up and re-establishes BGP sessions with its peers (restart helpers), it waits to learn all routes announced by these peers before doing a cumulative path selection; after which, it updates its forwarding tables and re-announces the appropriate routes to its peers. These procedures ensure that if there are any routing changes while the BGP speaker is restarting, they are considered post restart and the network converges.

{{%notice note%}}
BGP graceful restart is supported for both IPv4 and IPv6.
{{%/notice%}}

BGP graceful restart helper mode is enabled by default. You can enable restarting router mode in one of two ways:
- Globally, where all BGP peers inherit the graceful restart capability.
- Per BGP peer or peer group, which can be useful for misbehaving peers or when working with third party devices. You can also configure a peer or peer group to run in helper mode only, where routes originated and advertised from a BGP peer are not deleted.

You must enable BGP graceful restart (restarting router mode) as described above to achieve a switch restart or switch software upgrade with minimal traffic loss in a BGP configuration. Refer to {{<link url="Smart-System-Manager" text="Smart System Manager">}} for more information.

{{%notice note%}}
BGP goes through a graceful restart (as a restarting router) only with a planned switch restart event initiated by the Smart System Manager. Any other restart of BGP, such as an autonomous restart of the BGP daemon due to a software exception or a user-initiated restart of the FRR service, results in BGP going through a regular restart where the BGP session with peers is  terminated explicitly and BGP learned routes are removed from the forwarding plane during restart.
{{%/notice%}}

The following example commands enable global graceful BGP restart:

{{< tabs "TabID19 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add routing bgp graceful-restart-mode helper-and-restarter
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp graceful-restart
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 NEED COMMAND
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

The following example commands enable BGP graceful restart on the BGP peer connected on swp51.

{{< tabs "TabID51 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 graceful-restart-mode helper-and-restarter
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 graceful-restart
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 graceful-restart-mode full?????
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

The following example commands enable helper mode only for the BGP peer connected on swp51. Routes originated and advertised from the peer are not deleted.

{{< tabs "TabID83 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 graceful-restart-mode helper
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 graceful-restart-helper
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 graceful-restart-mode helper-only?????
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp51 remote-as external
 neighbor swp51 graceful-restart
...
```

You can configure the following graceful restart timers, which are set globally.

|<div style="width:250px">Timer | Description |
| ---- | ----------- |
| `restart-time` | The number of seconds to wait for a graceful restart capable peer to re-establish BGP peering. The default is 120 seconds. You can set a value between 1 and 4095.|
| `pathselect-defer-time` | The number of seconds a restarting peer defers path-selection when waiting for the EOR marker from peers. The default is 360 seconds. You can set a value between 0 and 3600. |
| `stalepath-time` | The number of seconds to hold stale routes for a restarting peer. The default is 360 seconds. You can set a value between 1 and 4095.|

The following example commands set the `restart-time` to 400 seconds, `pathselect-defer-time` to 300 seconds, and `stalepath-time` to 400 seconds:

{{< tabs "TabID125 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add routing bgp graceful-restart restart-time 400
cumulus@leaf01:~$ net add routing bgp graceful-restart pathselect-defer-time 300
cumulus@leaf01:~$ net add routing bgp graceful-restart stalepath-time 400
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp graceful-restart restart-time 400
leaf01(config-router)# bgp graceful-restart select-defer-time 300
leaf01(config-router)# bgp graceful-restart stalepath-time 400
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$ 
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ NEED COMMAND
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp51 remote-as external
 bgp graceful-restart restart-time 400
 bgp graceful-restart select-defer-time 300
 bgp graceful-restart stalepath-time 400
...
```

The following example commands disable global graceful restart:

{{< tabs "TabID162 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add routing bgp graceful-restart-mode disabled
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp graceful-restart-disable
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$ 
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

CUE commands are not provided.

{{< /tab >}}

{{< /tabs >}}

The following example commands disable graceful BGP restart on a BGP peer:

{{< tabs "TabID169 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 graceful-restart-disable
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 graceful-restart-disable
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$ 
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 graceful-restart-mode off
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

To show BGP graceful restart information, run the NCLU `net show bgp neighbor <neighbour> graceful-restart` command or the vtysh `show bgp neighbor <neighbor> graceful-restart` command.

```
cumulus@leaf01:mgmt:~$ net show bgp neighbor swp51 graceful-restart
Codes: GR - Graceful Restart, * -  Inheriting Global GR Config,
       Restart - GR Mode-Restarting, Helper - GR Mode-Helper,
       Disable - GR Mode-Disable.

BGP neighbor on swp51: fe80::4638:39ff:fe00:2, remote AS 65199, local AS 65101, external link
  BGP state = Established, up for 00:15:54
  Neighbor GR capabilities:
    Graceful Restart Capability: advertised and received
      Remote Restart timer is 120 seconds
      Address families by peer:
        none
  Graceful restart information:
    End-of-RIB send: IPv4 Unicast
    End-of-RIB received: IPv4 Unicast
    Local GR Mode: Helper*
    Remote GR Mode: Helper
    R bit: False
    Timers:
      Configured Restart Time(sec): 120
      Received Restart Time(sec): 120
    IPv4 Unicast:
      F bit: False
      End-of-RIB sent: Yes
      End-of-RIB sent after update: Yes
      End-of-RIB received: Yes
      Timers:
        Configured Stale Path Time(sec): 360
```

## Enable Read-only Mode

As BGP peers are established and updates are received, prefixes might be installed in the RIB and advertised to BGP peers even though the information from all peers is not yet received and processed. Depending on the timing of the updates, prefixes might be installed and propagated through BGP, and then immediately withdrawn and replaced with new routing information. Read-only mode minimizes this BGP route churn in both the local RIB and with BGP peers.

Enable read-only mode to reduce CPU and network usage when restarting the BGP process. Because intermediate best paths are possible for the same prefix as peers get established and start receiving updates at different times, read-only mode is particularly useful in topologies where BGP learns a prefix from many peers and the network has a high number of prefixes.

{{%notice note%}}

While in read-only mode, BGP does not run best-path or generate any updates to its peers.

{{%/notice%}}

To enable read-only mode, you set the `max-delay` timer and, optionally, the `establish-wait` timer. Read-only mode begins as soon as the first peer reaches its established state and the `max-delay` timer starts, and continues until either of the following two conditions are met:

- All the configured peers (except the shutdown peers) have sent an explicit EOR or an implicit EOR. The first keep-alive after BGP reaches the established state is considered an implicit EOR.  If you specify the `establish-wait` option, BGP only considers peers that have reached the established state from the moment the `max-delay` timer starts until the `establish-wait` period ends. The minimum set of established peers for which EOR is expected are the peers that are established during the `establish-wait` window, not necessarily all the configured neighbors.

- The timer reaches the configured `max-delay`.

The default value for `max-delay` is 0, which disables read-only mode. The `update delay` and `establish wait` can be any value between 0 and 3600 seconds. The `establish-wait` setting is optional; however, if specified, it must be shorter than the `max-delay`.

The following example commands enable read-only mode by setting the `max-delay` timer to 300 seconds and the `establish-wait` timer to 90 seconds.

{{< tabs "48 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp update-delay 300 90
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp
switch(config-router)# update-delay 300 90
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ NEED COMMAND
```

{{< /tab >}}

{{< /tabs >}}

To show information about the state of the update delay, run the NCLU command `net show bgp summary` or the `vtysh` command `show ip bgp summary`.

## BGP Community Lists

You can use *{{<exlink url="http://docs.frrouting.org/en/latest/bgp.html#community-lists" text="community lists">}}* to define a BGP community to tag one or more routes. You can then use the communities to apply a route policy on either egress or ingress.

The BGP community list can be either *standard* or *expanded.* The standard BGP community list is a pair of values (such as *100:100*) that can be tagged on a specific prefix and advertised to other neighbors or applied on route ingress. Or, it can be one of four BGP default communities:

- *internet*: a BGP community that matches all routes
- *local-AS*: a BGP community that restricts routes to your confederation's sub-AS
- *no-advertise*: a BGP community that is not advertised to anyone
- *no-export*: a BGP community that is not advertised to the eBGP peer

An expanded BGP community list takes a regular expression of communities and matches the listed communities.

When the neighbor receives the prefix, it examines the community value and takes action accordingly, such as permitting or denying the community member in the routing policy.

Here is an example of a standard community list filter:

{{< tabs "2086 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add routing community-list standard COMMUNITY1 permit 100:100
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
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

{{< tabs "1127">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add routing protocol bgp route-map ROUTE-MAP1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# route-map ROUTEMAP1 
switch(config-route-map)# match community COMMUNITY1
switch(config-route-map)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

## Related Information

- {{<exlink url="https://tools.ietf.org/html/rfc4360" text="RFC 4360, BGP Extended Communities Attribute">}}
- {{<exlink url="https://tools.ietf.org/html/rfc4456" text="RFC 4456, BGP Route Reflection - An Alternative to Full Mesh Internal BGP (iBGP)">}}
