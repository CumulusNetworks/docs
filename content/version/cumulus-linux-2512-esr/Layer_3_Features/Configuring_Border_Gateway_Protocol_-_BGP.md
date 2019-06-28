---
title: Configuring Border Gateway Protocol - BGP
author: Cumulus Networks
weight: 135
aliases:
 - /display/CL25ESR/Configuring+Border+Gateway+Protocol+-+BGP
 - /pages/viewpage.action?pageId=5116113
pageID: 5116113
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
BGP is the routing protocol that runs the Internet. It is an
increasingly popular protocol for use in the data center as it lends
itself well to the rich interconnections in a Clos topology.
Specifically:

  - It does not require routing state to be periodically refreshed
    unlike OSPF.

  - It is less chatty than its link-state siblings. For example, a link
    or node transition can result in a bestpath change, causing BGP to
    send updates.

  - It is multi-protocol and extensible.

  - There are many robust vendor implementations.

  - The protocol is very mature and comes with many years of operational
    experience.

[This IETF
draft](http://tools.ietf.org/html/draft-lapukhov-bgp-routing-large-dc-04)
provides further details of the use of BGP within the data center.

## <span>Commands</span>

Cumulus Linux:

  - bgp

  - vtysh

Quagga:

  - bgp

  - neighbor

  - router

  - show

## <span>Autonomous System Number (ASN)</span>

One of the key concepts in BGP is an *autonomous* *system number* or
ASN. An [autonomous
system](https://en.wikipedia.org/wiki/Autonomous_System_%28Internet%29)
is defined as a set of routers under a common administration. Since BGP
was originally designed to peer between independently managed
enterprises and/or service providers, each such enterprise is treated as
an autonomous system, responsible for a set of network addresses. Each
such autonomous system is given a unique number called its ASN. ASNs are
handed out by a central authority (ICANN). However, ASNs between 64512
and 65535 are reserved for private use. Using BGP within the data center
relies on either using this number space or else using the single ASN
you own.

The ASN is central to how BGP builds a forwarding topology. A BGP route
advertisement carries with it not only the originator’s ASN, but also
the list of ASNs that this route advertisement has passed through. When
forwarding a route advertisement, a BGP speaker adds itself to this
list. This list of ASNs is called the *AS path*. BGP uses the AS path to
detect and avoid loops.

ASNs were originally 16-bit numbers, but were later modified to be
32-bit. Quagga supports both 16-bit and 32-bit ASNs, but most
implementations still run with 16-bit ASNs.

## <span>eBGP and iBGP</span>

When BGP is used to peer between autonomous systems, the peering is
referred to as *external BGP* or eBGP. When BGP is used within an
autonomous system, the peering used is referred to as *internal BGP* or
iBGP. eBGP peers have different ASNs while iBGP peers have the same ASN.

While the heart of the protocol is the same when used as eBGP or iBGP,
there is a key difference in the protocol behavior between use as eBGP
and iBGP: an iBGP node does not forward routing information learned from
one iBGP peer to another iBGP peer. It expects the originating iBGP peer
to send this information to all iBGP peers.

This implies that iBGP peers are all connected to each other. In a large
network, this requirement can quickly become unscalable. The most
popular method to avoid this problem is to introduce a *route
reflector*.

## <span>Route Reflectors</span>

Route reflectors are quite easy to understand in a Clos topology. In a
two-tier Clos network, the leaf (or tier 1) switches are the only ones
connected to end stations. Subsequently, this means that the spines
themselves do not have any routes to announce. They’re merely
**reflecting** the routes announced by one leaf to the other leaves.
Thus, the spine switches function as route reflectors while the leaf
switches serve as route reflector clients.

In a three-tier network, the tier 2 nodes (or mid-tier spines) act as
both route reflector servers and route reflector clients. They act as
route reflectors because they announce the routes learned from the tier
1 nodes to other tier 1 nodes and to tier 3 nodes. They also act as
route reflector clients to the tier 3 nodes, receiving routes learned
from other tier 2 nodes. Tier 3 nodes act only as route reflectors.

In the following illustration, tier 2 node 2.1 is acting as a route
reflector server, announcing the routes between tier 1 nodes 1.1 and 1.2
to tier 1 node 1.3. It is also a route reflector client, learning the
routes between tier 2 nodes 2.2 and 2.3 from the tier 3 node, 3.1.

{{% imgOld 0 %}}

## <span>ECMP with BGP</span>

If a BGP node hears a prefix **p** from multiple peers, it has all the
information necessary to program the routing table to forward traffic
for that prefix **p** through all of these peers. Thus, BGP supports
equal-cost multipathing.

In order to perform ECMP in BGP, you may need to configure two
parameters: *maximum paths* and, if you're using eBGP, *multipath
relax*.

### <span>Maximum Paths</span>

BGP does not install multiple routes by default. To do so, use the
`maximum-paths` command. Or, if you're using iBGP, use the
`maximum-paths ibgp` command as shown below.

    leaf1# conf t
    leaf1(config)# router bgp 65000
    leaf1(config-router)# maximum-paths 
      <1-255>  Number of paths
      ibgp     iBGP-multipath
    leaf1(config-router)# maximum-paths ibgp 
      <1-255>  Number of paths

### <span>Multipath Relax</span>

If your data center uses eBGP, you need to configure an additional
parameter for proper ECMP: the `bestpath as-path multipath-relax
no-as-set` command. You configure it under the BGP routing process.

    leaf1# conf t
    leaf1(config)# router bgp 65000
    leaf1(config-router)# bgp bestpath 
    as-path           compare-routerid  med               
    leaf1(config-router)# bgp bestpath as-path          
    confed           ignore           multipath-relax  
    leaf1(config-router)# bgp bestpath as-path multipath-relax 
      <cr>       
      no-as-set  Do not generate an AS_SET
    leaf1(config-router)# bgp bestpath as-path multipath-relax no-as-set 

For more information on the `no-as-set` option, read [the AS\_PATH
section
below](#src-5116113_ConfiguringBorderGatewayProtocol-BGP-as_path).

## <span>BGP for both IPv4 and IPv6</span>

Unlike OSPF, which has separate versions of the protocol to announce
IPv4 and IPv6 routes, BGP is a multi-protocol routing engine, capable of
announcing both IPv4 and IPv6 prefixes. It supports announcing IPv4
prefixes over an IPv4 session and IPv6 prefixes over an IPv6 session. It
also supports announcing prefixes of both these address families over a
single IPv4 session or over a single IPv6 session.

<span id="src-5116113_ConfiguringBorderGatewayProtocol-BGP-config_bgp"></span>

## <span>Configuring BGP</span>

1.  Activate the BGP and Zebra daemons:
    
      - Add the following line to `/etc/quagga/daemons`:
        
            zebra=yes
            bgpd = yes
    
      - Touch an empty `bgpd` configuration file:
        
            cumulus@switch:~$ sudo touch /etc/quagga/bgpd.conf
        
        A slightly more useful configuration file would contain the
        following lines:
        
            hostname R7
            password *****
            enable password *****
            log timestamp precision 6
            log file /var/log/quagga/bgpd.log
            !
            line vty
             exec-timeout 0 0
            !
        
        The most important information here is the specification of the
        location of the log file, where the BGP process can log
        debugging and other useful information. A common convention is
        to store the log files under `/var/log/quagga`.
        
        You must restart `quagga` when a new daemon is enabled:
        
            cumulus@switch:~$ sudo service quagga restart

2.  Identify the BGP node by assigning an ASN and `router-id`:
    
        cumulus@switch:~$ sudo vtysh
        
        Hello, this is Quagga (version 0.99.21).
        Copyright 1996-2005 Kunihiro Ishiguro, et al.
        
        R7# configure  terminal
        R7(config)# router bgp 65000
        R7(config-router)# bgp router-id 0.0.0.1

3.  Specify to whom it must disseminate routing information:
    
        R7(config-router)# neighbor 10.0.0.2 remote-as 65001
    
    If it is an iBGP session, the `remote-as` is the same as the local
    AS:
    
        R7(config-router)# neighbor 10.0.0.2 remote-as 65000
    
    Specifying the peer’s IP address allows BGP to set up a TCP socket
    with this peer, but it doesn’t distribute any prefixes to it, unless
    it is explicitly told that it must via the `activate` command:
    
        R7(config-router)# address-family ipv4 unicast
        R7(config-router-af)# neighbor 10.0.0.2 activate
        R7(config-router-af)# exit
        R7(config-router)# address-family ipv6
        R7(config-router-af)# neighbor 2002:0a00:0002::0a00:0002 activate
        R7(config-router-af)# exit
    
    As you can see, activate has to be specified for each address family
    that is being announced by the BGP session.

4.  Specify some properties of the BGP session:
    
        R7(config-router)# neighbor 10.0.0.2 next-hop-self
        R7(config-router)# address-family ipv4 unicast
        R7(config-router-af)# maximum-paths 64
    
    For iBGP, the `maximum-paths` is selected by typing:
    
        R7(config-router-af)# maximum-paths ibgp 64
    
    If this is a route-reflector client, it can be specified as follows:
    
        R3(config-router-af)# neighbor 10.0.0.1 route-reflector-client
    
    {{%notice note%}}
    
    It is node R3, the route reflector, on which the peer is specified
    as a client.
    
    {{%/notice%}}

5.  Specify what prefixes to originate:
    
        R7(config-router)# address-family ipv4 unicast
        R7(config-router-af)# network 192.0.2.0/24
        R7(config-router-af)# network 203.0.113.1/24

## <span id="src-5116113_ConfiguringBorderGatewayProtocol-BGP-unnumbered" class="confluence-anchor-link"></span><span>Using BGP Unnumbered Interfaces</span>

Unnumbered interfaces are interfaces without unique IP addresses. In
BGP, you configure unnumbered interfaces using *extended next-hop
encoding* (ENHE), which is defined by
[RFC 5549](https://tools.ietf.org/html/rfc5549). BGP unnumbered
interfaces provide a means of advertising an IPv4 route with an IPv6
next-hop. Prior to RFC 5549, an IPv4 route could be advertised only with
an IPv4 next-hop.

BGP unnumbered interfaces are particularly useful in deployments where
IPv4 prefixes are advertised through BGP over a section without any IPv4
address configuration on links. As a result, the routing entries are
also IPv4 for destination lookup and have IPv6 next-hops for forwarding
purposes.

### <span>BGP and Extended Next-hop Encoding</span>

Once enabled and active, BGP makes use of the available IPv6 next-hops
for advertising any IPv4 prefixes. BGP learns the prefixes, calculates
the routes and installs them in IPv4 AFI to IPv6 AFI format. However,
ENHE in Cumulus Linux does not install routes into the kernel in IPv4
prefix to IPv6 next-hop format. For link-local peerings enabled by
dynamically learning the other end's link-local address using IPv6
neighbor discovery router advertisements, an IPv6 next-hop is converted
into an IPv4 link-local address and a static neighbor entry is installed
for this IPv4 link-local address with the MAC address derived from the
link-local address of the other end.

{{%notice note%}}

It is assumed that the IPv6 implementation on the peering device will
use the MAC address as the interface ID when assigning the IPv6
link-local address, as suggested by RFC 4291.

{{%/notice%}}

### <span>Configuring BGP Unnumbered Interfaces</span>

Configuring a BGP unnumbered interface requires enabling IPv6 neighbor
discovery router advertisements. The `interval` you specify is measured
in seconds, and defaults to 600 seconds. Extended next-hop encoding is
sent only for the link-local address peerings:

    interface swp1
        no ipv6 nd suppress-ra
        ipv6 nd ra-interval 5
    !
    router bgp 10
        neighbor swp1 interface
        neighbor swp1 remote-as  20
        neighbor swp1 capability extended-nexthop
    !

### <span>Managing Unnumbered Interfaces</span>

All the relevant BGP commands are now capable of showing IPv6 next-hops
and/or the interface name for any IPv4 prefix:

    #  show ip bgp
    BGP table version is 66, local router ID is 6.0.0.5
    Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
                  i internal, r RIB-failure, S Stale, R Removed
    Origin codes: i - IGP, e - EGP, ? - incomplete
       Network          Next Hop            Metric LocPrf Weight Path
    *> 6.0.0.5/32       0.0.0.0                  0         32768 ?
    *= 6.0.0.6/32       swp2                          0 65534 64503 ?
    *=                  swp6                          0 65002 64503 ?
    *=                  swp5                          0 65001 64503 ?
    *=                  swp1                          0 65534 64503 ?
    *=                  swp4                          0 65534 64503 ?
    *>                  swp3                          0 65534 64503 ?
    
    # show ip bgp 6.0.0.14/32
    BGP routing table entry for 6.0.0.14/32
    Paths: (1 available, best #1, table Default-IP-Routing-Table)
      Advertised to non peer-group peers:
      swp1 swp2 swp3 swp4 swp5 swp6
      65534
        fe80::202:ff:fe00:3d from swp2 (6.0.0.14)
        (fe80::202:ff:fe00:3d) (used)
          Origin incomplete, metric 0, localpref 100, valid, external, best
          Last update: Tue May 12 17:18:41 2015

Quagga RIB commands are also modified:

    # show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, A - Babel, T - Table,
           > - selected route, * - FIB route
    K>* 0.0.0.0/0 via 192.168.0.2, eth0
    C>* 6.0.0.5/32 is directly connected, lo
    B>* 6.0.0.6/32 [20/0] via fe80::202:ff:fe00:45, swp3, 00:46:12
      *                   via fe80::202:ff:fe00:35, swp1, 00:46:12
      *                   via fe80::202:ff:fe00:3d, swp2, 00:46:12
      *                   via fe80::202:ff:fe00:4d, swp4, 00:46:12
      *                   via fe80::202:ff:fe00:55, swp5, 00:46:12
      *                   via fe80::202:ff:fe00:5a, swp6, 00:46:12

The following commands show how the IPv4 link-local address
*169.254.0.1* is used to install the route and static neighbor entry to
facilitate proper forwarding without having to install an IPv4 prefix
with IPv6 next-hop in the kernel:

    # ip route show 6.0.0.6
    6.0.0.6  proto zebra  metric 20
        nexthop via 169.254.0.1  dev swp3 weight 1 onlink
        nexthop via 169.254.0.1  dev swp1 weight 1 onlink
        nexthop via 169.254.0.1  dev swp2 weight 1 onlink
        nexthop via 169.254.0.1  dev swp4 weight 1 onlink
        nexthop via 169.254.0.1  dev swp5 weight 1 onlink
        nexthop via 169.254.0.1  dev swp6 weight 1 onlink
    
    
    # ip neigh
    fe80::202:ff:fe00:35 dev swp1 lladdr 00:02:00:00:00:35 router REACHABLE
    fe80::202:ff:fe00:5a dev swp6 lladdr 00:02:00:00:00:5a router REACHABLE
    fe80::202:ff:fe00:3d dev swp2 lladdr 00:02:00:00:00:3d router REACHABLE
    fe80::202:ff:fe00:55 dev swp5 lladdr 00:02:00:00:00:55 router REACHABLE
    fe80::202:ff:fe00:45 dev swp3 lladdr 00:02:00:00:00:45 router REACHABLE
    fe80::202:ff:fe00:4d dev swp4 lladdr 00:02:00:00:00:4d router REACHABLE
    169.254.0.1 dev swp5 lladdr 00:02:00:00:00:55 PERMANENT
    192.168.0.2 dev eth0 lladdr 52:55:c0:a8:00:02 REACHABLE
    169.254.0.1 dev swp3 lladdr 00:02:00:00:00:45 PERMANENT
    169.254.0.1 dev swp1 lladdr 00:02:00:00:00:35 PERMANENT
    169.254.0.1 dev swp4 lladdr 00:02:00:00:00:4d PERMANENT
    169.254.0.1 dev swp6 lladdr 00:02:00:00:00:5a PERMANENT
    169.254.0.1 dev swp2 lladdr 00:02:00:00:00:3d PERMANENT

### <span>How traceroute Interacts with BGP Unnumbered Interfaces</span>

Every router or end host must have an IPv4 address in order to complete
a `traceroute` of IPv4 addresses. In this case, the IPv4 address used is
that of the loopback device.

Even if ENHE is not used in the data center, link addresses are not
typically advertised. This is because:

  - Link addresses take up valuable FIB resources. In a large Clos
    environment, the number of such addresses can be quite large.

  - Link addresses expose an additional attack vector for intruders to
    use to either break in or engage in DDOS attacks.

Therefore, assigning an IP address to the loopback device is essential.

### <span>Advanced: Understanding How Next-hop Fields Are Set</span>

This section describes how the IPv6 next-hops are set in the
MP\_REACH\_NLRI ([multiprotocol reachable
NLRI](https://www.ietf.org/rfc/rfc2858.txt)) initiated by the system,
which applies whether IPv6 prefixes or IPv4 prefixes are exchanged with
ENHE. There are two main aspects to determine — how many IPv6 next-hops
are included in the MP\_REACH\_NLRI (since the RFC allows either one or
two next-hops) and the values of the next-hop(s). This section also
describes how a received MP\_REACH\_NLRI is handled as far as processing
IPv6 next-hops.

  - Whether peering to a global IPv6 address or link-local IPv6 address,
    the determination whether to send one or two next-hops is as
    follows:
    
    1.  If reflecting the route, two next-hops are sent only if the peer
        has `nexthop-local unchanged` configured and the attribute of
        the received route has an IPv6 link-local next-hop; otherwise,
        only one next-hop is sent.
    
    2.  Otherwise (if it's not reflecting the route), two next-hops are
        sent if explicitly configured (`nexthop-local unchanged`) or the
        peer is directly connected (that is, either peering is on
        link-local address or the global IPv4 or IPv6 address is
        *directly connected*) and the route is either a
        local/self-originated route or the peer is an eBGP peer.
    
    3.  In all other cases, only one next-hop gets sent, unless an
        outbound route map adds another next-hop.

  - `route-map` can impose two next-hops in scenarios where Cumulus
    Linux would only send one next-hop — by specifying `set ipv6 nexthop
    link-local`.

  - For all routes to eBGP peers and self-originated routes to iBGP
    peers, the global next-hop (first value) is the peering address of
    the local system. If the peering is on the link-local address, this
    is the global IPv6 address on the peering interface, if present;
    otherwise, it is the link-local IPv6 address on the peering
    interface.

  - For other routes to iBGP peers (eBGP to iBGP or reflected), the
    global next-hop will be the global next-hop in the received
    attribute.
    
    {{%notice note%}}
    
    If this address were a link-local IPv6 address, it would get reset
    so that the link-local IPv6 address of the eBGP peer is not passed
    along to an iBGP peer, which most likely may be on a different link.
    
    {{%/notice%}}

  - `route-map` and/or the peer configuration can change the above
    behavior. For example, `route-map` can set the global IPv6 next-hop
    or the peer configuration can set it to *self* — which is relevant
    for *iBGP* peers. The route map or peer configuration can also set
    the next-hop to unchanged, which ensures the source IPv6 global
    next-hop is passed around — which is relevant for *eBGP* peers.

  - Whenever two next-hops are being sent, the link-local next-hop (the
    second value of the two) is the link-local IPv6 address on the
    peering interface unless it is due to `nh-local-unchanged` or
    `route-map` has set the link-local next-hop.

  - Network administrators cannot set [martian
    values](http://en.wikipedia.org/wiki/Martian_packet) for IPv6
    next-hops in `route-map`. Also, global and link-local next-hops are
    validated to ensure they match the respective address types.

  - In a received update, a martian check is imposed for the IPv6 global
    next-hop. If the check fails, it gets treated as an implicit
    withdraw.

  - If two next-hops are received in an update and the second next-hop
    is not a link-local address, it gets ignored and the update is
    treated as if only one next-hop was received.

  - Whenever two next-hops are received in an update, the second
    next-hop is used to install the route into `zebra`. As per the
    previous point, it is already assured that this is a link-local IPv6
    address. Currently, this is assumed to be reachable and is not
    registered with NHT.

  - When `route-map` specifies the next-hop as `peer-address`, the
    global IPv6 next-hop as well as the link-local IPv6 next-hop (if
    it's being sent) is set to the *peering address*. If the peering is
    on a link-local address, the former could be the link-local address
    on the peering interface, unless there is a global IPv6 address
    present on this interface.

The above rules imply that there are scenarios where a generated update
has two IPv6 next-hops, and both of them are the IPv6 link-local address
of the peering interface on the local system. If you are peering with a
switch or router that is not running Cumulus Linux and expects the first
next-hop to be a global IPv6 address, a route map can be used on the
sender to specify a global IPv6 address. This conforms with the
recommendations in the Internet draft
[draft-kato-bgp-ipv6-link-local-00.txt](https://tools.ietf.org/html/draft-kato-bgp-ipv6-link-local-00),
"BGP4+ Peering Using IPv6 Link-local Address".

### <span>Limitations</span>

  - Interface-based peering with separate IPv4 and IPv6 sessions is not
    supported.

  - ENHE is sent for IPv6 link-local peerings only.

  - If a IPv4 /30 or /31 IP address is assigned to the interface IPv4
    peering will be used over IPv6 link-local peering.

## <span>Fast Convergence Design Considerations</span>

Without getting into the why (see the IETF draft cited in Useful Links
below that talks about BGP use within the data center), we strongly
recommend the following use of addresses in the design of a BGP-based
data center network:

  - Use of interface addresses: Set up BGP sessions only using
    interface-scoped addresses. This allows BGP to react quickly to link
    failures.

  - Use of next-hop-self: Every BGP node says that it knows how to
    forward traffic to the prefixes it is announcing. This reduces the
    requirement to announce interface-specific addresses and thereby
    reduces the size of the forwarding table.

### <span>Specifying the Interface Name in the neighbor Command</span>

When you are configuring BGP for the neighbors of a given interface, you
can specify the interface name instead of its IP address. All the other
`neighbor` command options remain the same.

This is equivalent to BGP peering to the link-local IPv6 address of the
neighbor on the given interface. The link-local address is learned via
IPv6 neighbor discovery router advertisements.

Consider the following example configuration:

    router bgp 65000
      bgp router-id 0.0.0.1
      neighbor swp1 interface
      neighbor swp1 remote-as 65000
      neighbor swp1 next-hop-self
    !
      address-family ipv6
      neighbor swp1 activate
      exit-address-family

{{%notice note%}}

Make sure that IPv6 neighbor discovery router advertisements are
supported and not suppressed. In Quagga, you do this by checking the
running configuration. Under the interface configuration, use `no ipv6
nd suppress-ra` to remove router suppression.

Cumulus Networks recommends you adjust the router advertisement's
interval to a shorter value (`ipv6 nd ra-interval <interval>`) to
address scenarios when nodes come up and miss router advertisement
processing to relay the neighbor’s link-local address to BGP. The
`interval` is measured in seconds and defaults to 600 seconds.

{{%/notice%}}

## <span>Configuring BGP Peering Relationships across Switches</span>

A BGP peering relationship is typically initiated with the `neighbor
x.x.x.x remote-as <AS number>` command. In order to simplify
configuration across multiple switches, you can specify the *internal*
or *external* keyword to the configuration instead of the AS number.

Specifying *internal* signifies an iBGP peering; that is, the neighbor
will only create or accept a connection with the specified neighbor if
the remote peer AS number matches this BGP's AS number.

Specifying *external* signifies an eBGP peering; that is, the neighbor
will only create a connection with the neighbor if the remote peer AS
number does **not** match this BGP AS number.

You can make this distinction using the `neighbor` command or the
`peer-group` command.

In general, use the following syntax with the `neighbor` command:

    neighbor (ipv4 addr|ipv6 addr|WORD) remote-as (<1-4294967295>|internal|external)

Some example configurations follow.

To connect to **the same AS** using the `neighbor` command, modify your
configuration similar to the following:

    router bgp 500
    neighbor 192.168.1.2 remote-as internal

To connect to a **different AS** using the `neighbor` command, modify
your configuration similar to the following:

    router bgp 500
    neighbor 192.168.1.2 remote-as external

To connect to **the same AS** using the `peer-group` command, modify
your configuration similar to the following:

    router bgp 500
    neighbor swp1 interface
    neighbor IBGP peer-group
    neighbor IBGP remote-as internal
    neighbor swp1 peer-group IBGP
    neighbor 6.0.0.3 peer-group IBGP
    neighbor 6.0.0.4 peer-group IBGP

To connect to a **different AS** using the `peer-group` command, modify
your configuration similar to the following:

    router bgp 500
    neighbor swp2 interface
    neighbor EBGP peer-group
    neighbor EBGP remote-as external
    neighbor 6.0.0.2 peer-group EBGP
    neighbor swp2 peer-group EBGP
    neighbor 6.0.0.4 peer-group EBGP

## <span>Configuration Tips</span>

### <span>Using peer-group to Simplify Configuration</span>

When there are many peers to connect to, the amount of redundant
configuration becomes overwhelming. For example, repeating the
`activate` and `next-hop-self` commands for even 60 neighbors makes for
a very long configuration file. Using `peer-group` addresses this
problem.

Instead of specifying properties of each individual peer, Quagga allows
for defining one or more peer-groups and associating all the attributes
common to that peer session to a peer-group.

After doing this, the only task is to associate an IP address with a
peer-group. Here is an example of defining and using peer-groups:

    R7(config-router)# neighbor tier-2 peer-group
    R7(config-router)# neighbor tier-2 remote-as 65000
    R7(config-router)# address-family ipv4 unicast
    R7(config-router-af)# neighbor tier-2 activate
    R7(config-router-af)# neighbor tier-2 next-hop-self
    R7(config-router-af)# maximum-paths ibgp 64
    R7(config-router-af)# exit
    R7(config-router)# neighbor 10.0.0.2 peer-group tier-2
    R7(config-router)# neighbor 192.0.2.2 peer-group tier-2

If you're using eBGP, besides specifying the neighbor's IP address, you
also have to specify the neighbor's ASN, since it is different for each
neighbor. In such a case, you wouldn't specify the `remote-as` for the
peer-group.

### <span>Preserving the AS\_PATH Setting</span>

<span id="src-5116113_ConfiguringBorderGatewayProtocol-BGP-as_path"></span>If
you plan to use multipathing with the `multipath-relax` option, Quagga
generates an AS\_SET in place of the current AS\_PATH for the bestpath.
This helps to prevent loops but is unusual behavior. To preserve the
AS\_PATH setting, use the `no-as-set` option when configuring bestpath:

    R7(config-router)# bgp bestpath as-path multipath-relax no-as-set

### <span>Utilizing Multiple Routing Tables and Forwarding</span>

You can run multiple routing tables (one for in-band/data plane traffic
and one for out-of-band/management plane traffic) on the same switch
using [management
VRF](/version/cumulus-linux-2512-esr/Layer_3_Features/Management_VRF)
(multiple routing tables and forwarding).

## <span>Troubleshooting</span>

The most common starting point for troubleshooting BGP is to view the
summary of neighbors connected to and some information about these
connections. A sample output of this command is as follows:

    R7# show ip bgp summary
    BGP router identifier 0.0.0.9, local AS number 65000
    RIB entries 7, using 672 bytes of memory
    Peers 2, using 9120 bytes of memory
    
    Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
    10.0.0.2        4 65000      11      10        0    0    0 00:06:38        3
    192.0.2.2       4 65000      11      10        0    0    0 00:06:38        3
    
    Total number of neighbors 2

(Pop quiz: Are these iBGP or eBGP sessions? Hint: Look at the ASNs.)

It is also useful to view the routing table as defined by BGP:

    R7# show ip bgp
    BGP table version is 0, local router ID is 0.0.0.9
    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
                  r RIB-failure, S Stale, R Removed
    Origin codes: i - IGP, e - EGP, ? - incomplete
    
          Network          Next Hop            Metric LocPrf Weight Path
       *> 192.0.2.29/24    0.0.0.0                  0         32768 i
       *>i192.0.2.30/24    10.0.0.2                 0    100      0 i
       * i                 192.0.2.2                0    100      0 i
       *>i192.0.2.31/24    10.0.0.2                 0    100      0 i
       * i                 192.0.2.2                0    100      0 i
       *>i192.0.2.32/24    10.0.0.2                 0    100      0 i
       * i                 192.0.2.2                0    100      0 i
    
    Total number of prefixes 4

A more detailed breakdown of a specific neighbor can be obtained using
`show ip bgp neighbor <neighbor ip address>`:

    R7# show ip bgp  neighbor 10.0.0.2
    BGP neighbor is 10.0.0.2, remote AS 65000, local AS 65000, internal link
    BGP version 4, remote router ID 0.0.0.5
    BGP state = Established, up for 00:14:03
    Last read 14:52:31, hold time is 180, keepalive interval is 60 seconds
    Neighbor capabilities:
      4 Byte AS: advertised and received
      Route refresh: advertised and received(old & new)
      Address family IPv4 Unicast: advertised and received
    Message statistics:
      Inq depth is 0
      Outq depth is 0
                           Sent       Rcvd
      Opens:                  1          1
      Notifications:          0          0
      Updates:                1          3
      Keepalives:            16         15
      Route Refresh:          0          0
      Capability:             0          0
      Total:                 18         19
    Minimum time between advertisement runs is 5 seconds
    
    For address family: IPv4 Unicast
      NEXT_HOP is always this router
      Community attribute sent to this neighbor(both)
      3 accepted prefixes
    
      Connections established 1; dropped 0
      Last reset never
    Local host: 10.0.0.1, Local port: 35258
    Foreign host: 10.0.0.2, Foreign port: 179
    Nexthop: 10.0.0.1
    Nexthop global: fe80::202:ff:fe00:19
    Nexthop local: ::
    BGP connection: non shared network
    Read thread: on  Write thread: off

To see the details of a specific route such as from whom it was
received, to whom it was sent, and so forth, use the `show ip bgp <ip
address/prefix>` command:

    R7# show ip bgp 192.0.2.0
    BGP routing table entry for 192.0.2.0/24
    Paths: (2 available, best #1, table Default-IP-Routing-Table)
      Not advertised to any peer
      Local
        10.0.0.2 (metric 1) from 10.0.0.2 (0.0.0.10)
          Origin IGP, metric 0, localpref 100, valid, internal, best
          Originator: 0.0.0.10, Cluster list: 0.0.0.5
          Last update: Mon Jul  8 10:12:17 2013
      Local
        192.0.2.2 (metric 1) from 192.0.2.2 (0.0.0.10)
          Origin IGP, metric 0, localpref 100, valid, internal
          Originator: 0.0.0.10, Cluster list: 0.0.0.6
          Last update: Mon Jul  8 10:12:17 2013

This shows that the routing table prefix seen by BGP is 192.0.2.0/24,
that this route was not advertised to any neighbor, and that it was
heard by two neighbors, *10.0.0.2* and *192.0.2.2*.

Here is another output of the same command, on a different node in the
network:

    cumulus@switch:~$ sudo vtysh -c 'sh ip bgp 192.0.2.0'
    BGP routing table entry for 192.0.2.0/24
    Paths: (1 available, best #1, table Default-IP-Routing-Table)
      Advertised to non peer-group peers:
      10.0.0.1 192.0.2.21 192.0.2.22
      Local, (Received from a RR-client)
        203.0.113.1 (metric 1) from 203.0.113.1 (0.0.0.10)
          Origin IGP, metric 0, localpref 100, valid, internal, best
          Last update: Mon Jul  8 09:07:41 2013

### <span>Debugging Tip: Logging Neighbor State Changes</span>

It is very useful to log the changes that a neighbor goes through to
troubleshoot any issues associated with that neighbor. This is done
using the log-neighbor-changes command:

    R7(config-router)# bgp log-neighbor-changes

The output is sent to the specified log file, usually
`/var/log/quagga/bgpd.log`, and looks like this:

    2013/07/08 10:12:06.572827 BGP: %NOTIFICATION: sent to neighbor 10.0.0.2 6/3 (Cease/Peer Unconfigured) 0 bytes
    2013/07/08 10:12:06.572954 BGP: Notification sent to neighbor 10.0.0.2: type 6/3
    2013/07/08 10:12:16.682071 BGP: %ADJCHANGE: neighbor 192.0.2.2 Up
    2013/07/08 10:12:16.682660 BGP: %ADJCHANGE: neighbor 10.0.0.2 Up

### <span>Troubleshooting Link-local Addresses</span>

To verify that `quagga` learned the neighboring link-local IPv6 address
via the IPv6 neighbor discovery router advertisements on a given
interface, use the `show interface <if-name>` command. If `ipv6 nd
suppress-ra` isn't enabled on both ends of the interface, then `Neighbor
address(s):` should have the other end's link-local address. That is the
address that BGP would use when BGP is enabled on that interface.

Use `vtysh` to run `quagga`, then verify the configuration:

    cumulus@switch:~$ sudo vtysh
    
    Hello, this is Quagga (version 0.99.21).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.
    
    R7# show interface  swp1
    Interface swp1 is up, line protocol is up
      PTM status: disabled
      Description: rut
      index 3 metric 1 mtu 1500
      flags: <UP,BROADCAST,RUNNING,MULTICAST>
      HWaddr: 00:02:00:00:00:09
      inet 11.0.0.1/24 broadcast 11.0.0.255
      inet6 fe80::202:ff:fe00:9/64
      ND advertised reachable time is 0 milliseconds
      ND advertised retransmit interval is 0 milliseconds
      ND router advertisements are sent every 600 seconds
      ND router advertisements lifetime tracks ra-interval
      ND router advertisement default router preference is medium
      Hosts use stateless autoconfig for addresses.
      Neighbor address(s):
      inet6 fe80::4638:39ff:fe00:129b/128

Instead of the IPv6 address, the peering interface name is displayed in
the `show ip bgp summary` command and wherever else applicable:

    R7# show ip bgp summary
    BGP router identifier 0.0.0.1, local AS number 65000
    RIB entries 1, using 112 bytes of memory
    Peers 1, using 8712 bytes of memory
    
    Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
    swp1            4 65000     161     170        0    0    0 00:02:28        0

Most of the show commands can take the interface name instead of the IP
address, if that level of specificity is needed:

    R7# show ip bgp neighbors
      <cr>
      A.B.C.D   Neighbor to display information about
      WORD      Neighbor on bgp configured interface
      X:X::X:X  Neighbor to display information about
    R7# show ip bgp neighbors swp1

## <span>Enabling Read-only Mode</span>

You can enable read-only mode for when the BGP process restarts or when
the BGP process is cleared using `clear ip bgp *`. When enabled,
read-only mode begins as soon as the first peer reaches its
*established* state and a timer for `<max-delay>` seconds is started.

While in read-only mode, BGP doesn't run best-path or generate any
updates to its peers. This mode continues until:

  - All the configured peers, except the shutdown peers, have sent an
    explicit EOR (End-Of-RIB) or an implicit EOR. The first keep-alive
    after BGP has reached the established state is considered an
    implicit EOR. If the `<establish-wait>` option is specified, then
    BGP will wait for peers to reach the established state from the
    start of the `update-delay` until the `<establish-wait>` period is
    over; that is, the minimum set of established peers for which EOR is
    expected would be peers established during the `establish-wait`
    window, not necessarily all the configured neighbors.

  - The `max-delay` period is over.

Upon reaching either of these two conditions, BGP resumes the decision
process and generates updates to its peers.

To enable read-only mode:

    cumulus@switch:$ sudo bgp update-delay <max-delay in seconds> [<establish-wait in seconds>]

The default `<max-delay>` is 0 — the feature is off by default.

Use output from `show ip bgp summary` for information about the state of
the update delay.

This feature can be useful in reducing CPU/network usage as BGP
restarts/clears. It's particularly useful in topologies where BGP learns
a prefix from many peers. Intermediate best paths are possible for the
same prefix as peers get established and start receiving updates at
different times. This feature is also valuable if the network has a high
number of such prefixes.

## <span>Applying a Route Map for Route Updates</span>

You can apply a route map on route updates from BGP to Zebra. All the
applicable match operations are allowed, such as match on prefix,
next-hop, communities, and so forth. Set operations for this
attach-point are limited to metric and next-hop only. Any operation of
this feature does not affect BGPs internal RIB.

Both IPv4 and IPv6 address families are supported. Route maps work on
multi-paths as well. However, the metric setting is based on the best
path only.

To apply a route map for route updates:

    cumulus@switch:$ sudo cl-bgp table-map <route-map-name>

## <span>Protocol Tuning</span>

### <span>Converging Quickly On Link Failures</span>

In the Clos topology, we recommend that you only use interface addresses
to set up peering sessions. This means that when the link fails, the BGP
session is torn down immediately, triggering route updates to propagate
through the network quickly. This requires the following commands be
enabled for all links: `link-detect` and `ttl-security hops <hops>`.
`ttl-security hops` specifies how many hops away the neighbor is. For
example, in a Clos topology, every peer is at most 1 hop away.

{{%notice note%}}

See Caveats and Errata below for information regarding `ttl-security
hops`.

{{%/notice%}}

Here is an example:

    cumulus@switch:~$ sudo vtysh
    
    Hello, this is Quagga (version 0.99.21).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.
    
    R7# configure  terminal
    R7(config)# interface  swp1
    R7(config-if)# link-detect
    R7(config-if)# exit
    R7(config)# router bgp 65000
    R7(config-router)# neighbor  10.0.0.2 ttl-security  hops  1

### <span>Converging Quickly On Soft Failures</span>

It is possible that the link is up, but the neighboring BGP process is
hung or has crashed. If a BGP process crashes, Quagga’s `watchquagga`
daemon, which monitors the various `quagga` daemons, will attempt to
restart it. If the process is also hung, `watchquagga` will attempt to
restart the process. BGP itself has a keepalive timer that is exchanged
between neighbors. By default, this keepalive timer is set to 60
seconds. This time can be reduced to a lower number, but this has the
disadvantage of increasing the CPU load, especially in the presence of a
lot of neighbors. `keepalive-time` is the periodicity with which the
keepalive message is sent. `hold-time` specifies how many keepalive
messages can be lost before the connection is considered invalid. It is
usually set to 3 times the keepalive time. Here is an example of
reducing these timers:

    R7(config-router)# neighbor 10.0.0.2 timers 30 90

We can make these the default for all BGP neighbors using a different
command:

    R7(config-router)# timers bgp 30 90

The following display snippet shows that the default values have been
modified for this neighbor:

    R7(config-router)# do show ip bgp neighbor 10.0.0.2
    BGP neighbor is 10.0.0.2, remote AS 65000, local AS 65000, internal link
      BGP version 4, remote router ID 0.0.0.5
      BGP state = Established, up for 05:53:59
      Last read 14:53:25, hold time is 180, keepalive interval is 60 seconds
      Configured hold time is 90, keepalive interval is 30 seconds
      ....

{{%notice tip%}}

When you're in a configuration mode, such as when you're configuring BGP
parameters, you can run any show command by adding do to the original
command. For example, `do show ip bgp neighbor` was shown above. Under a
non-configuration mode, you'd simply run:

    show ip bgp neighbor 10.0.0.2

{{%/notice%}}

### <span>Reconnecting Quickly</span>

A BGP process attempts to connect to a peer after a failure (or on
startup) every `connect-time` seconds. By default, this is 120 seconds.
To modify this value, use:

    R7(config-router)# neighbor 10.0.0.2 timers connect 30

This command has to be specified per each neighbor, peer-group doesn’t
support this option in `quagga`.

### <span>Advertisement Interval</span>

BGP by default chooses stability over fast convergence. This is very
useful when routing for the Internet. For example, unlike link-state
protocols, BGP typically waits for a duration of
`advertisement-interval` seconds between sending consecutive updates to
a neighbor. This ensures that an unstable neighbor flapping routes won’t
be propagated throughout the network. By default, this is set to 30
seconds for an eBGP session and 5 seconds for an iBGP session. For very
fast convergence, set the timer to 0 seconds. You can modify this as
follows:

    R7(config-router)# neighbor 10.0.0.2 advertisement-interval 0

The following output shows the modified value:

    R7(config-router)# do show ip bgp neighbor 10.0.0.2
    BGP neighbor is 10.0.0.2, remote AS 65000, local AS 65000, internal link
      BGP version 4, remote router ID 0.0.0.5
      BGP state = Established, up for 06:01:49
      Last read 14:53:15, hold time is 180, keepalive interval is 60 seconds
      Configured hold time is 90, keepalive interval is 30 seconds
    Neighbor capabilities:
      4 Byte AS: advertised and received
      Route refresh: advertised and received(old & new)
      Address family IPv4 Unicast: advertised and received
    Message statistics:
      Inq depth is 0
      Outq depth is 0
                           Sent       Rcvd
      Opens:                  1          1
      Notifications:          0          0
      Updates:                1          3
      Keepalives:           363        362
      Route Refresh:          0          0
      Capability:             0          0
      Total:                365        366
    Minimum time between advertisement runs is 0 seconds
    ....

{{%notice note%}}

This command is not supported with peer-groups.

{{%/notice%}}

See this [IETF draft](http://tools.ietf.org/html/draft-jakma-mrai-02)
for more details on the use of this value.

## <span>Configuration Files</span>

  - /etc/quagga/daemons

  - /etc/quagga/bgpd.conf

## <span>Useful Links</span>

  - [Bidirectional forwarding
    detection](/version/cumulus-linux-2512-esr/Layer_3_Features/Bidirectional_Forwarding_Detection_-_BFD)
    (BFD) and BGP

  - [Wikipedia entry for
    BGP](http://en.wikipedia.org/wiki/Border_Gateway_Protocol) (includes
    list of useful RFCs)

  - [Quagga online documentation for
    BGP](http://www.nongnu.org/quagga/docs/docs-info.html#BGP) (may not
    be up to date)

  - [IETF draft discussing BGP use within data
    centers](http://tools.ietf.org/html/draft-lapukhov-bgp-routing-large-dc-04)

## <span>Caveats and Errata</span>

### <span>ttl-security Issue</span>

Enabling `ttl-security` does not cause the hardware to be programmed
with the relevant information. This means that frames will come up to
the CPU and be dropped there. It is recommended that you use the
`cl-acltool` command to explicitly add the relevant entry to hardware.

For example, you can configure a file, like
`/etc/cumulus/acl/policy.d/01control_plane_bgp.rules`, with a rule like
this for TTL:

    INGRESS_INTF = swp1 
        INGRESS_CHAIN = INPUT, FORWARD 
    
        [iptables]
        -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p tcp --dport bgp -m ttl --ttl 255 POLICE --set-mode pkt --set-rate 2000 --set-burst 1000 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p tcp --dport bgp DROP

{{%notice note%}}

For more information about ACLs and `cl-acltool`, see [Netfilter
(ACLs)](/version/cumulus-linux-2512-esr/System_Management/Netfilter_-_ACLs).

{{%/notice%}}
