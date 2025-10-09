---
title: Border Gateway Protocol - BGP
author: NVIDIA
weight: 520
product: SONiC
version: 202012
siteSlug: sonic
---

BGP is the routing protocol that runs the Internet. It manages how packets get routed from network to network by exchanging routing and reachability information.

BGP is an increasingly popular protocol for use in the data center as it lends itself well to the rich interconnections in a Clos topology. {{<exlink url="https://tools.ietf.org/html/rfc7938" text="RFC 7938">}} provides further details about using BGP in the data center.

## How BGP Works

BGP directs packets between autonomous systems (AS), which are a set of routers under a common administration.

Each router maintains a routing table that controls how packets are forwarded. The BGP process on the router generates information in the routing table based on information coming from other routers and from information in the BGP routing information base (RIB). The RIB is a database that stores routes and continuously updates the routing table as changes occur.

### Autonomous System

Because BGP was originally designed to peer between independently managed enterprises and service providers, each such enterprise is treated as an autonomous system responsible for a set of network addresses. Each such autonomous system is given a unique number called an *autonomous system number* (ASN). ASNs are handed out by a central authority (ICANN); however, ASNs between 64512 and 65535 are reserved for private use. Using BGP within the data center relies on either using this number space or using the single ASN you own.

The ASN is central to how BGP builds a forwarding topology. A BGP route advertisement carries with it not only the ASN of the originator, but also the list of ASNs that this route advertisement passes through. When forwarding a route advertisement, a BGP speaker adds itself to this list. This list of ASNs is called the *AS path*. BGP uses the AS path to detect and avoid loops.

ASNs were originally 16-bit numbers, but were later modified to be 32-bit. FRRouting supports both 16-bit and 32-bit ASNs, but many implementations still run with 16-bit ASNs.

### eBGP and iBGP

When BGP is used to peer between autonomous systems, the peering is referred to as *external BGP* or eBGP. When BGP is used within an autonomous system, the peering used is referred to as *internal BGP* or iBGP. eBGP peers have different ASNs while iBGP peers have the same ASN.

The heart of the protocol is the same when used as eBGP or iBGP but there is a key difference in the protocol behavior between eBGP and iBGP. To prevent loops, an iBGP speaker does not forward routing information learned from one iBGP peer to another iBGP peer. eBGP prevents loops using the `AS_Path` attribute.

All iBGP speakers need to be peered with each other in a full mesh. In a large network, this requirement can quickly become unscalable. The most popular method to scale iBGP networks is to introduce a {{<link url="#route-reflectors" text="route reflector">}}.

### BGP Path Selection

BGP is a path-vector routing algorithm that does not rely on a single routing metric to determine the lowest cost route, unlike interior gateway protocols (IGPs) like OSPF.

The BGP path selection algorithm looks at multiple factors to determine exactly which path is best. {{<link url="#ecmp" text="BGP multipath">}} is enabled by default in SONiC so that multiple equal cost routes can be installed in the routing table but only a single route is advertised to BGP peers.

The order of the BGP algorithm process is as follows:

- **Highest Weight**: Weight is a value from 0 to 65535. Weight is not carried in a BGP update but is used locally to influence the best path selection. Locally generated routes have a weight of 32768.
- **Highest Local Preference**: Local preference is exchanged between iBGP neighbors only. Routes received from eBGP peers are assigned a local preference of 0. Whereas weight is used to make route selections without sending additional information to peers, local preference can be used to influence routing to iBGP peers.
- **Locally Originated Routes**: Any route that the local switch is responsible for placing into BGP is selected as best. This includes static routes, aggregate routes and redistributed routes.
- **Shortest AS Path**: The path received with the fewest number of ASN hops is selected.
- **Origin Check**: Preference is given to routes with an IGP origin (routes placed into BGP with a `network` statement) over incomplete origins (routes places into BGP through redistribution). The EGP origin attribute is no longer used.
- **Lowest MED**: The Multi-Exit Discriminator or MED is sent to eBGP peers to indicate a preference on how traffic enters an AS. A MED received from an eBGP peer is exchanged with iBGP peers but is reset to a value of 0 before advertising a prefix to another AS.
- **eBGP Routes**: A route received from an eBGP peer is preferred over a route learned from an iBGP peer.
- **Lowest IGP Cost to the Next Hop**: The route with the lowest IGP metric to reach the BGP next hop.
- **iBGP ECMP over eBGP ECMP**: If {{<link url="#ecmp" text="BGP multipath">}} is configured, prefer equal iBGP routes over equal eBGP routes, unless {{<link url="#ecmp" text="as-path multipath-relax">}} is also configured.
- **Oldest Route**: Preference is given to the oldest route in the BGP table.
- **Lowest Router ID**: Preference is given to the route received from the peer with the lowest Router ID attribute. If the route is received from a route reflector, the `ORIGINATOR_ID` attribute is used for comparison.
- **Shortest Route Reflector Cluster List**: If a route passes through multiple route reflectors, prefer the route with the shortest route reflector cluster list.
- **Highest Peer IP Address**: Preference is given to the route received from the peer with the highest IP address.

SONiC provides the reason it selects one path over another in the `show ip bgp network` command output for a specific prefix.

When BGP multipath is in use, if multiple paths are equal, BGP still selects a single best path to advertise to peers. This path is indicated as best with the reason, although multiple paths might be installed into the routing table.

## Configure BGP

To configure BGP on a BGP node, at minimum, you need to:

- Assign an ASN to identify this BGP node.
- Assign a router ID, which is a 32-bit value and is typically the address of the loopback interface on the switch.
- Specify where to distribute routing information by providing the IP address and ASN of the neighbor.
  - This is the IP address of the interface between the two peers; the interface must be a layer 3 access port.
  - The ASN can be a number, or `internal` for a neighbor in the same AS or `external` for a neighbor in a different AS.
- Specify which prefixes to originate from this BGP node.

This example configuration here is based on the {{<exlink url="https://air.nvidia.com/" text="SONiC Virtual Test Drive">}}. It uses a 2 leaf, 1 spine configuration, named leaf01, leaf02 and spine01 respectively.

Configure spine01:

{{<tabs "BGPspine01">}}

{{<tab "config_db.json">}}

Configure BGP in `/etc/sonic/config_db.json`.

1. Configure a loopback interface:

   ```
   admin@switch:~$ sudo vi /etc/sonic/config_db.json

    "LOOPBACK_INTERFACE": {
        "Loopback0|10.10.10.101/32": {}
    },
    ...
   }
   ```

1. Configure a point-to-point link to leaf01:

   ```
   "INTERFACE": {
       ...
       "Ethernet0|10.0.0.0/31": {},
       ...
   }
   ```

1. Configure a point-to-point link to leaf02:

   ```
   "INTERFACE": {
       ...
       "Ethernet4|10.0.1.2/31": {},
       ...
   }
   ```

1. Configure BGP:

   ```
   "BGP_NEIGHBOR": {
       "10.0.1.1": {
           "asn": "65101",
           "name": "leaf01",
       },
       "10.0.1.3": {
           "asn": "65102",
           "name": "leaf02",
       },
   ...
   ```

   ```
   "DEVICE_METADATA": {
       "localhost": {
           "bgp_asn": "65199",
           "default_bgp_status": "up",
           ...
       }
   },
   ```

1. Reload the configuration:

       admin@spine01:~$ sudo config reload -y

{{</tab>}}

{{<tab "SONiC and vtysh CLI">}}

Connect to spine01 and configure the interfaces and BGP:

1. Configure a loopback interface:

       admin@spine01:~$ sudo config interface ip add Loopback0 10.10.10.101/32
1. Configure a point-to-point link to leaf01:

       admin@spine01:~$ sudo config interface ip add Ethernet0 10.0.1.0/31
1. Configure a point-to-point link to leaf02:

       admin@spine01:~$ sudo config interface ip add Ethernet4 10.0.1.2/31

1. Save the configuration:

       admin@spine01:~$ sudo config save -y
1. Configure BGP in FRRouting:

       admin@spine01:~$ sudo vtysh
       spine01# configure terminal
       spine01(config)# no router bgp 65100
       spine01(config)# router bgp 65199
       spine01(config-router)# bgp router-id 10.10.10.101 
       spine01(config-router)# bgp log-neighbor-changes
       spine01(config-router)# neighbor 10.0.1.1 remote-as 65101
       spine01(config-router)# neighbor 10.0.1.1 description leaf01
       spine01(config-router)# neighbor 10.0.1.3 remote-as 65102
       spine01(config-router)# neighbor 10.0.1.3 description leaf02
       spine01(config-router)# address-family ipv4 unicast
       spine01(config-router-af)# network 10.10.10.101/32
       spine01(config-router-af)# end
       spine01# write memory
       spine01# exit
       admin@spine01:~$

Connect to leaf01 and configure the interfaces and BGP:

1. Configure a loopback interface:

       admin@leaf01:~$ sudo config interface ip add Loopback0 10.10.10.1/32
1. Configure a point-to-point link to spine01:

       admin@leaf01:~$ sudo config interface ip add Ethernet12 10.0.1.1/31
1. Save the configuration:

       admin@leaf01:~$ sudo config save -y
1. Configure BGP in FRRouting:

       admin@leaf01:~$ sudo vtysh
       leaf01# configure t
       leaf01(config)# no router bgp 65100
       leaf01(config)# router bgp 65101
       leaf01(config-router)# bgp router-id 10.10.10.1
       leaf01(config-router)# bgp log-neighbor-changes
       leaf01(config-router)# neighbor 10.0.1.0 remote-as 65199
       leaf01(config-router)# neighbor 10.0.1.0 description spine01
       leaf01(config-router)# address-family ipv4 unicast
       leaf01(config-router-af)# network 10.10.10.1/32
       leaf01(config-router-af)# network 10.0.10.0/24
       leaf01(config-router-af)# end
       leaf01# write mem
       leaf01# exit
       admin@leaf01:~$

Connect to leaf02 and configure the interfaces and BGP:

1. Configure a loopback interface:

       admin@leaf02:~$ sudo config interface ip add Loopback0 10.10.10.2/32
1. Configure a point-to-point link to spine01:

       admin@leaf02:~$ sudo config interface ip add Ethernet12 10.0.1.3/31
1. Save the configuration:

       admin@leaf02:~$ sudo config save -y
1. Configure BGP in FRRouting:

       admin@leaf02:~$ sudo vtysh
       leaf02# configure t
       leaf02(config)# no router bgp 65100
       leaf02(config)# router bgp 65102
       leaf02(config-router)# bgp router-id 10.10.10.2
       leaf02(config-router)# bgp log-neighbor-changes
       leaf02(config-router)# neighbor 10.0.1.2 remote-as 65199
       leaf02(config-router)# neighbor 10.0.1.2 description spine01
       leaf02(config-router)# address-family ipv4 unicast
       leaf02(config-router-af)# network 10.10.10.2/32
       leaf02(config-router-af)# network 10.0.20.0/24
       leaf02(config-router-af)# end
       leaf02# write mem
       leaf02# exit
       admin@leaf02:~$

{{</tab>}}

{{</tabs>}}

## Route Reflectors

iBGP rules state that a route learned from an iBGP peer can not be sent to another iBGP peer. In a data center spine and leaf network using iBGP, this prevents a spine from sending a route learned from a leaf to any other leaf. As a workaround, BGP introduced the concept of a *route reflector* that selectively ignores this rule so that when an iBGP speaker is configured as a route reflector, it *can* send iBGP learned routes to other iBGP peers.

In the following example, spine01 is acting as a route reflector. The leaf switches, leaf01, leaf02 and leaf03 are *route reflector clients*. Any route that spine01 learns from a route reflector client is sent to other route reflector clients.

{{<img src="/images/cumulus-linux/bgp-route-reflectors-example.png">}}

To configure the BGP node as a route reflector for a BGP peer, set the neighbor `route-reflector-client` option. The following example sets spine01 shown in the illustration above to be a route reflector for leaf01 (on swp1), which is a route reflector client. No configuration is required on the client.

{{<tabs "Route Reflectors">}}

{{<tab "config_db.json">}}

Configure the route reflector in the PORT table in `/etc/sonic/config_db.json`. To set the port to always be administratively up, set the `admin_status` to `up`:

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"BGP_NEIGHBOR": {
    "Ethernet0": {
        ...
        "rrclient": "0",
        ...
    },
    ...
}
```

{{</tab>}}

{{<tab "vtysh CLI">}}

```
admin@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# router bgp 65199
switch(config-router)# address-family ipv4
switch(config-router-af)# neighbor Ethernet0 route-reflector-client
switch(config-router-af)# end
switch# write memory
switch# exit
admin@switch:~$
```

The `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor Ethernet0 remote-as external
 !
 address-family ipv4 unicast
  network 10.10.10.101/32
  neighbor Ethernet0 route-reflector-client
 exit-address-family
...
```

{{</tab >}}

{{</tabs >}}

## ECMP

BGP supports equal-cost multipathing ({{<link url="Equal-Cost-Multipathing-ECMP" text="ECMP">}}). If a BGP node hears a certain prefix from multiple peers, it has all the information necessary to program the routing table and forward traffic for that prefix through all of these peers. BGP typically chooses one best path for each prefix and installs that route in the forwarding table.

In SONiC, the *BGP multipath* option is enabled by default with the maximum number of paths set to 64 so that the switch can install multiple equal-cost BGP paths to the forwarding table and load balance traffic across multiple links. You can change the number of paths allowed, according to your needs.

The example commands change the maximum number of paths to 120. You can set a value between 1 and 256. 1 disables the BGP multipath option.

```
admin@spine01:~$ sudo vtysh
spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# address-family ipv4 unicast
spine01(config-router-af)# maximum-paths 120
spine01(config-router-af)# end
spine01# write memory
spine01# exit
admin@spine01:~$
```

<!--
{{<tabs "ECMP">}}

{{<tab "config_db.json">}}


{{</tab >}}

{{<tab "vtysh CLI">}}

{{< /tab >}}
{{< /tabs >}}
-->
When *BGP multipath* is enabled, only BGP routes from the same AS are load balanced. If the routes go across several different AS neighbors, even if the AS path length is the same, they are not load balanced. To be able to load balance between multiple paths received from different AS neighbors, you need to set the `bestpath as-path multipath-relax` option.

```
admin@spine01:~$ sudo vtysh
spine01# configure terminal
spine01(config)# router bgp 65101
spine01(config-router)# bgp bestpath as-path multipath-relax
spine01(config-router)# end
spine01# write memory
spine01# exit
admin@spine01:~$
```

<!--
{{<tabs "BGP multipath">}}
{{<tab "config_db.json">}}

```
admin@switch:~$ 
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

The `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  bgp router-id 10.0.0.1
  bgp bestpath as-path multipath-relax
...
```

{{< /tab >}}
{{< /tabs >}}
-->
{{%notice note%}}

When you disable the *bestpath as-path multipath-relax* option, EVPN type-5 routes do not use the updated configuration. Type-5 routes continue to use all available ECMP paths in the underlay fabric, regardless of ASN.

{{%/notice%}}

## View the Startup Configuration

You can see the startup BGP configuration by running `show startupconfiguration bgp`:

```
admin@spine01:~$ show startupconfiguration bgp
outing-Stack is: frr
!
! Zebra configuration saved from vty
!   2020/12/16 20:44:26
!
frr version 7.2.1-sonic
frr defaults traditional
!
hostname sonic
password zebra
enable password zebra
log syslog informational
log facility local4
!
!
!
router bgp 65199
 bgp router-id 10.10.10.101
 bgp log-neighbor-changes
 neighbor 10.0.1.1 remote-as 65101
 neighbor 10.0.1.1 description leaf01
 neighbor 10.0.1.3 remote-as 65102
 neighbor 10.0.1.3 description leaf02
 !
 address-family ipv4 unicast
  network 10.10.10.101/32
  maximum-paths 120
 exit-address-family
!
!
ip prefix-list PL_LoopbackV4 seq 5 permit 10.1.0.1/32
!
route-map ALLOW_LIST_DEPLOYMENT_ID_0_V4 permit 65535
 set community 5060:12345 additive
!
route-map ALLOW_LIST_DEPLOYMENT_ID_0_V6 permit 65535
 set community 5060:12345 additive
!
route-map FROM_BGP_PEER_V4 permit 2
 call ALLOW_LIST_DEPLOYMENT_ID_0_V4
 on-match next
!
route-map FROM_BGP_PEER_V4 permit 100
!
route-map FROM_BGP_PEER_V6 permit 1
 set ipv6 next-hop prefer-global
!
route-map FROM_BGP_PEER_V6 permit 2
 call ALLOW_LIST_DEPLOYMENT_ID_0_V6
 on-match next
!
route-map FROM_BGP_PEER_V6 permit 100
!
route-map RM_SET_SRC permit 10
!
route-map TO_BGP_PEER_V4 permit 100
!
route-map TO_BGP_PEER_V6 permit 100
!
agentx
!
line vty
!
admin@spine01:~$
```
