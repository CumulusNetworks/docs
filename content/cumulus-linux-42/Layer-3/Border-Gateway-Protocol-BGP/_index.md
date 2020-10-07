---
title: Border Gateway Protocol - BGP
author: Cumulus Networks
weight: 810
toc: 3
---
BGP is the routing protocol that runs the Internet. It manages how packets get routed from network to network by exchanging routing and reachability information.

BGP is an increasingly popular protocol for use in the data center as it lends itself well to the rich interconnections in a Clos topology. {{<exlink url="https://tools.ietf.org/html/rfc7938" text="RFC 7938">}} provides further details about using BGP in the data center.

## How does BGP Work?

BGP directs packets between autonomous systems (AS), which are a set of routers under a common administration.
Each router maintains a routing table that controls how packets are forwarded. The BGP process on the router generates information in the routing table based on information coming from other routers and from information in the BGP routing information base (RIB). The RIB is a database that stores routes and continually updates the routing table as changes occur.

### Autonomous System

Because BGP was originally designed to peer between independently managed enterprises and/or service providers, each such enterprise is treated as an autonomous system, responsible for a set of network addresses. Each such autonomous system is given a unique number called an *autonomous system number* (ASN). ASNs are handed out by a central authority (ICANN); however, ASNs between 64512 and 65535 are reserved for private use. Using BGP within the data center relies on either using this number space or using the single ASN you own.

The ASN is central to how BGP builds a forwarding topology. A BGP route advertisement carries  with it not only the ASN of the originator, but also the list of ASNs that this route advertisement passes through. When forwarding a route advertisement, a BGP speaker adds itself to this list. This list of ASNs is called the *AS path*. BGP uses the AS path to detect and avoid loops.

ASNs were originally 16-bit numbers, but were later modified to be 32-bit. FRRouting supports both 16-bit and 32-bit ASNs, but many implementations still run with 16-bit ASNs.

{{%notice note%}}

In a VRF-lite deployment (where multiple independent routing tables working simultaneously on the same switch), Cumulus Linux supports multiple ASNs.

{{%/notice%}}

### Auto BGP

In a two-tier leaf and spine environment, you can use *auto BGP* to generate 32-bit ASN numbers automatically so that you don't have to think about which numbers to allocate. Auto BGP helps build optimal ASN configurations in your data center to avoid suboptimal routing and path hunting, which occurs when you assign the wrong spine ASNs. Auto BGP makes no changes to standard BGP behavior or configuration.

Auto BGP assigns private ASN numbers in the range 4200000000 through 4294967294. This is the private space defined in {{<exlink url="https://tools.ietf.org/html/rfc6996" text="RFC 6996">}}. Each leaf is assigned a random and unique value in the range 4200000001 through 4294967294. Each spine is assigned 4200000000; the first number in the range. For information about configuring auto BGP, refer to {{<link url="Basic-BGP-Configuration" text="Basic BGP Configuration">}} below.

{{%notice note%}}

- Cumulus Networks recommends you use auto BGP in new deployments to avoid conflicting ASNs in an existing configuration.
- It is not necessary to use auto BGP across all switches in your configuration. For example, you can use auto BGP to configure one switch but allocate ASN numbers manually to other switches.
- Auto BGP is intended for use in two-tier spine and leaf networks. Using auto BGP in three-tier networks with superspines might result in incorrect ASN assignments.
- The `leaf` keyword generates the ASN based on a hash of the switch MAC address. The ASN assigned might change after a switch replacement.
- Auto BGP is supported for NCLU only.

{{%/notice%}}

### eBGP and iBGP

When BGP is used to peer between autonomous systems, the peering is referred to as *external BGP* or eBGP. When BGP is used within an autonomous system, the peering used is referred to as *internal BGP* or iBGP. eBGP peers have different ASNs while iBGP peers have the same ASN.

The heart of the protocol is the same when used as eBGP or iBGP but there is a key difference in the protocol behavior between eBGP and iBGP. To prevent loops, an iBGP speaker does not forward routing information learned from one iBGP peer to another iBGP peer. eBGP prevents loops using the `AS_Path` attribute.

All iBGP speakers need to be peered with each other in a full mesh. In a large network, this requirement can quickly become unscalable. The most popular method to scale iBGP networks is to introduce a *route reflector*. See {{<link url="#Optional-BGP-Configuration#route-reflectors" text="Route Reflectors">}} below.

### BGP Path Selection

BGP is a path-vector routing algorithm that does not rely on a single routing metric to determine the lowest cost route, unlike interior gateway protocols (IGPs) like OSPF.

The BGP path selection algorithm looks at multiple factors to determine exactly which path is best. {{<link url="Optional-BGP-Configuration#ecmp" text="BGP multipath">}} is enabled by default in Cumulus Linux so that multiple equal cost routes can be installed in the routing table but only a single route is advertised to BGP peers.

The order of the BGP algorithm process is as follows:

- **Highest Weight**: Weight is a value from 0 to 65535. Weight is not carried in a BGP update but is used locally to influence the best path selection. Locally generated routes have a weight of 32768.

- **Highest Local Preference**: Local Preference is exchanged between iBGP neighbors only. Routes received from eBGP peers are assigned a Local Preference of 0. Whereas weight is used to make route selections without sending additional information to peers, Local Preference can be used to influence routing to iBGP peers.

- **Locally Originated Routes**: Any route that we are responsible for placing into BGP is selected as best. This includes static routes, aggregate routes and redistributed routes.

- **Shortest AS Path**: The path received with the fewest number of ASN hops is selected.

- **Origin Check**: Prefer routes with an IGP origin (those routes placed into BGP with a `network` statement) over Incomplete origins (routes places into BGP through redistribution). The EGP origin attribute is no longer used.

- **Lowest MED**: The Multi-Exit Discriminator or MED is sent to eBGP peers to indicate a preference on how traffic enters an AS. A MED received from an eBGP peer is exchanged with iBGP peers but is reset to a value of 0 before advertising a prefix to another AS.

- **eBGP Routes**: A route received from an eBGP peer is prefered over a route learned from an iBGP peer.

- **Lowest IGP Cost to the next hop**: The route with the lowest IGP metric to reach the BGP next hop.

- **iBGP ECMP over eBGP ECMP**: If {{<link url="Optional-BGP-Configuration#ecmp" text="BGP Multipath">}} is configured, prefer equal iBGP routes over equal eBGP routes, unless {{<link url="Optional-BGP-Configuration#ecmp" text="as-path multipath-relax">}} is also configured.

- **Oldest Route**: Prefer the oldest route in the BGP table.

- **Lowest RouterID**: Prefer the route received from the peer with the lowest Router ID attribute. If the route is received from a route reflector, the `ORIGINATOR_ID` attribute is used to compare.

- **Shortest Route Reflector Cluster List**: If a route has passed through multiple route reflectors, prefer the route with the shortested route reflector cluster list.

- **Highest Peer IP Address**: Prefer the route received from the peer with the highest IP address.

Cumulus Linux provides the reason it is selecting one path over another in NCLU `net show bgp` and vtysh `show ip bgp` command output for a specific prefix.

When BGP multipath is in use, if multiple paths are equal, BGP still selects a single best path to advertise to peers. This path is indicated as best with the reason, although multiple paths might be installed into the routing table.

### BGP Unnumbered

Historically, peers connect through IPv4 over TCP port 179 and after they establish a session, they exchange prefixes. When a BGP peer advertises an IPv4 prefix, it must include an IPv4 next hop address, which is usually the address of the advertising router. This requires that each BGP peer has an IPv4 address, which in a large network can consume a lot of address space, requiring a separate IP address for each peer-facing interface.

The BGP unnumbered standard, specified in {{<exlink url="https://tools.ietf.org/html/rfc5549" text="RFC 5549">}} uses *extended next hop encoding* (ENHE) and no longer requires an IPv4 prefix to be advertised along with an IPv4 next hop. This means that you can set up BGP peering between your Cumulus Linux switches and exchange IPv4 prefixes without having to configure an IPv4 address on each switch; the interfaces used by BGP are unnumbered.

The next hop address for each prefix is an IPv6 link-local address, which is assigned automatically to each interface. Using the IPv6 link-local address as a next hop instead of an IPv4 unicast address, BGP unnumbered saves you from having to configure IPv4 addresses on each interface.

When you use BGP unnumbered, BGP learns the prefixes, calculates the routes and installs them in IPv4 AFI to IPv6 AFI format. ENHE in Cumulus Linux does not install routes into the kernel in IPv4 prefix to IPv6 next hop format. For link-local peerings enabled by dynamically learning the other end's link-local address using IPv6 neighbor discovery router advertisements, an IPv6 next hop is converted into an IPv4 link-local address and a static neighbor entry is installed for this IPv4 link-local address with the MAC address derived from the link-local address of the other end.

{{%notice note%}}

- Interface-based peering with separate IPv4 and IPv6 sessions is not supported.
- If an IPv4 /30 or /31 IP address is assigned to the interface, IPv4 peering is used over IPv6 link-local peering.
- BGP unnumbered only works with two switches at a time, as it is designed to work with PTP (point-to-point protocol).
- The IPv6 implementation on the peering device uses the MAC address as the interface ID when assigning the IPv6 link-local address, as suggested by RFC 4291.

{{%/notice%}}

{{< expand "Advanced: How Next Hop Fields Are Set "  >}}

This section describes how the IPv6 next hops are set in the MP\_REACH\_NLRI ({{<exlink url="https://www.ietf.org/rfc/rfc2858.txt" text="multiprotocol reachable NLRI">}}) initiated by the system, which applies whether IPv6 prefixes or IPv4 prefixes are exchanged with ENHE. There are two main aspects to determine: how many IPv6 next hops are included in the MP\_REACH\_NLRI (the RFC allows either one or two next hops) and the values of the next hops. This section also describes how a received MP\_REACH\_NLRI is handled as far as processing IPv6 next hops.

- When peering to a global IPv6 address or link-local IPv6 address, whether to send one or two next hops is determined as follows:
    - If reflecting the route, two next hops are sent only if the peer has `nexthop-local unchanged` configured and the attribute of the received route has an IPv6 link-local next hop  otherwise, only one next hop is sent.
    - If not reflecting the route, two next hops are sent if explicitly configured (`nexthop-local unchanged`) or the peer is directly connected (either peering is on link-local address or the global IPv4 or IPv6 address is *directly connected*) and the route is either a local/self-originated route or the peer is an eBGP peer.
    - In all other cases, only one next hop is sent, unless an outbound route map adds another next hop.
- `route-map` can impose two next hops in scenarios where Cumulus Linux only sends one next hop - by specifying `set ipv6 nexthop link-local`.
- For all routes to eBGP peers and self-originated routes to iBGP peers, the global next hop (first value) is the peering address of the local system. If the peering is on the link-local address, this is the global IPv6 address on the peering interface, if present; otherwise, it is the link-local IPv6 address on the peering interface.
- For other routes to iBGP peers (eBGP to iBGP or reflected), the global next hop is the global next hop in the received attribute.

{{%notice note%}}

If this address is a link-local IPv6 address, it is reset so that the link-local IPv6 address of the eBGP peer is not passed along to an iBGP peer, which is typically on a different link.

{{%/notice%}}

- `route-map` and/or the peer configuration can change the above behavior. For example, `route-map` can set the global IPv6 next hop or the peer configuration can set it to *self* - which is relevant for *iBGP* peers. The route map or peer configuration can also set the next hop to unchanged, which ensures the source IPv6 global next hop is passed around - which is relevant for *eBGP* peers.
- Whenever two next hops are being sent, the link-local next hop (the second value of the two) is the link-local IPv6 address on the peering interface unless it is due to `nh-local-unchanged` or `route-map` has set the link-local next hop.
- Network administrators cannot set {{<exlink url="http://en.wikipedia.org/wiki/Martian_packet" text="martian values">}} for IPv6 next hops in `route-map`. Also, global and link-local next hops are validated to ensure they match the respective address types.
- In a received update, a martian check is imposed for the IPv6 global next hop. If the check fails, it gets treated as an implicit withdraw.
- If two next hops are received in an update and the second next hop is not a link-local address, it gets ignored and the update is treated as if only one next hop was received.
- Whenever two next hops are received in an update, the second next hop is used to install the route into `zebra`. As per the previous point, it is already assured that this is a link-local IPv6 address. Currently, this is assumed to be reachable and is not registered with NHT.
- When `route-map` specifies the next hop as `peer-address`, the global IPv6 next hop as well as the link-local IPv6 next hop (if it's being sent) is set to the *peering address*. If the peering is on a link-local address, the former could be the link-local address on the peering interface, unless there is a global IPv6 address present on this interface.
- When using iBGP unnumbered with IPv6 Link Local Addresses (the default), FRR rewrites the BGP next hop to be the adjacent link. This is similar behavior to eBGP next hops. However, iBGP route advertisement rules do not change and a full mesh or route reflectors is still required.

The above rules imply that there are scenarios where a generated update has two IPv6 next hops, and both of them are the IPv6 link-local address of the peering interface on the local system. If you are peering with a switch or router that is not running Cumulus Linux and expects the first next hop to be a global IPv6 address, a route map can be used on the sender to specify a global IPv6 address. This conforms with the recommendations in the Internet draft {{<exlink url="https://tools.ietf.org/html/draft-kato-bgp-ipv6-link-local-00" text="draft-kato-bgp-ipv6-link-local-00.txt">}}, "BGP4+ Peering Using IPv6 Link-local Address."

{{< /expand >}}

## Related Information

- {{<exlink url="https://cumulusnetworks.com/lp/bgp-ebook/" text="BGP in the Data Center by Dinesh G. Dutt">}} - a complete guide to Border Gateway Protocol for the modern data center
- {{<link url="Bidirectional-Forwarding-Detection-BFD" text="Bidirectional forwarding detection">}} (BFD) and BGP
- {{<exlink url="http://en.wikipedia.org/wiki/Border_Gateway_Protocol" text="Wikipedia entry for BGP">}} (includes list of useful RFCs)
- {{<exlink url="http://docs.frrouting.org/en/latest/bgp.html" text="FRR BGP documentation">}}
- {{<exlink url="http://tools.ietf.org/html/draft-lapukhov-bgp-routing-large-dc-04" text="IETF draft discussing BGP use within data centers">}}
- {{<exlink url="https://tools.ietf.org/html/rfc1657" text="RFC 1657, Definitions of Managed Objects for the Fourth Version of the Border Gateway Protocol (BGP-4) using SMIv2">}}
- {{<exlink url="https://tools.ietf.org/html/rfc1997" text="RFC 1997, BGP Communities Attribute">}}
- {{<exlink url="https://tools.ietf.org/html/rfc2385" text="RFC 2385, Protection of BGP Sessions via the TCP MD5 Signature Option">}}
- {{<exlink url="https://tools.ietf.org/html/rfc2439" text="RFC 2439, BGP Route Flap Damping">}}
- {{<exlink url="https://tools.ietf.org/html/rfc2545" text="RFC 2545, Use of BGP-4 Multiprotocol Extensions for IPv6 Inter-Domain Routing">}}
- {{<exlink url="https://tools.ietf.org/html/rfc2918" text="RFC 2918, Route Refresh Capability for BGP-4">}}
- {{<exlink url="https://tools.ietf.org/html/rfc4271" text="RFC 4271, A Border Gateway Protocol 4 (BGP-4)">}}
- {{<exlink url="https://tools.ietf.org/html/rfc4760" text="RFC 4760, Multiprotocol Extensions for BGP-4">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5004" text="RFC 5004, Avoid BGP Best Path Transitions from One External to Another">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5065" text="RFC 5065, Autonomous System Confederations for BGP">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5291" text="RFC 5291, Outbound Route Filtering Capability for BGP-4">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5492" text="RFC 5492, Capabilities Advertisement with BGP-4">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5549" text="RFC 5549, Advertising IPv4 Network Layer Reachability Information with an IPv6 Next Hop">}}
- {{<exlink url="https://tools.ietf.org/html/rfc6793" text="RFC 6793, BGP Support for Four-Octet Autonomous System (AS) Number Space">}}
- {{<exlink url="https://tools.ietf.org/html/rfc7911" text="RFC 7911, Advertisement of Multiple Paths in BGP">}}
- {{<exlink url="https://tools.ietf.org/html/draft-walton-bgp-hostname-capability-00" text="draft-walton-bgp-hostname-capability-02, Fully Qualified Domain Name Capability for BGP">}}
