---
title: Border Gateway Protocol - BGP
author: NVIDIA
weight: 840
toc: 3
---
BGP is the routing protocol that runs the Internet. It manages how packets get routed from network to network by exchanging routing and reachability information.

BGP is an increasingly popular protocol for use in the data center as it lends itself well to the rich interconnections in a Clos topology. {{<exlink url="https://tools.ietf.org/html/rfc7938" text="RFC 7938">}} provides further details about using BGP in the data center.

## How Does BGP Work?

BGP directs packets between autonomous systems (AS), which are a set of routers under a common administration.
Each router maintains a routing table that controls how packets are forwarded. The BGP process on the router generates information in the routing table based on information coming from other routers and from information in the BGP routing information base (RIB). The RIB is a database that stores routes and continually updates the routing table as changes occur.

### Autonomous System

Because BGP was originally designed to peer between independently managed enterprises and service providers, each such enterprise is treated as an autonomous system responsible for a set of network addresses. Each such autonomous system is given a unique number called an *autonomous system number* (ASN). ASNs are handed out by a central authority (ICANN); however, ASNs between 64512 and 65535 are reserved for private use. Using BGP within the data center relies on either using this number space or using the single ASN you own.

The ASN is central to how BGP builds a forwarding topology. A BGP route advertisement carries  with it not only the ASN of the originator, but also the list of ASNs that this route advertisement passes through. When forwarding a route advertisement, a BGP speaker adds itself to this list. This list of ASNs is called the *AS path*. BGP uses the AS path to detect and avoid loops.

ASNs were originally 16-bit numbers, but were later modified to be 32-bit. FRRouting supports both 16-bit and 32-bit ASNs, but many implementations still run with 16-bit ASNs.

### Auto BGP

In a two-tier leaf and spine environment, you can use *auto BGP* to generate 32-bit ASNs automatically so that you do not have to think about which numbers to configure. Auto BGP helps build optimal ASN configurations in your data center to avoid suboptimal routing and path hunting, which occurs when you assign the wrong spine ASNs. Auto BGP makes no changes to standard BGP behavior or configuration.

Auto BGP assigns private ASNs in the range 4200000000 through 4294967294. This is the private space defined in {{<exlink url="https://tools.ietf.org/html/rfc6996" text="RFC 6996">}}. Each leaf is assigned a random and unique value in the range 4200000001 through 4294967294. Each spine is assigned 4200000000; the first number in the range. For information about configuring auto BGP, refer to {{<link url="Basic-BGP-Configuration" text="Basic BGP Configuration">}}.

{{%notice note%}}
- Use auto BGP in new deployments to avoid conflicting ASNs in an existing configuration.
- It is not necessary to use auto BGP across all switches in your configuration. For example, you can use auto BGP to configure one switch but set ASNs manually to other switches.
- Auto BGP is intended for use in two-tier spine and leaf networks. Using auto BGP in three-tier networks with super spines might result in incorrect ASN assignments.
- The `leaf` keyword generates the ASN based on a hash of the switch MAC address. The ASN assigned might change after a switch replacement.
- You can configure auto BGP with NCLU or NVUE.
{{%/notice%}}

### eBGP and iBGP

When BGP is used to peer between autonomous systems, the peering is referred to as *external BGP* or eBGP. When BGP is used within an autonomous system, the peering used is referred to as *internal BGP* or iBGP. eBGP peers have different ASNs while iBGP peers have the same ASN.

The heart of the protocol is the same when used as eBGP or iBGP but there is a key difference in the protocol behavior between eBGP and iBGP. To prevent loops, an iBGP speaker does not forward routing information learned from one iBGP peer to another iBGP peer. eBGP prevents loops using the `AS_Path` attribute.

All iBGP speakers need to be peered with each other in a full mesh. In a large network, this requirement can quickly become unscalable. The most popular method to scale iBGP networks is to introduce a {{<link url="Optional-BGP-Configuration/#route-reflectors" text="route reflector">}}.

### BGP Path Selection

BGP is a path-vector routing algorithm that does not rely on a single routing metric to determine the lowest cost route, unlike interior gateway protocols (IGPs) like OSPF.

The BGP path selection algorithm looks at multiple factors to determine exactly which path is best. {{<link url="Optional-BGP-Configuration#ecmp" text="BGP multipath">}} is enabled by default in Cumulus Linux so that multiple equal cost routes can be installed in the routing table but only a single route is advertised to BGP peers.

The order of the BGP algorithm process is as follows:

- **Highest Weight**: Weight is a value from 0 to 65535. Weight is not carried in a BGP update but is used locally to influence the best path selection. Locally generated routes have a weight of 32768.

- **Highest Local Preference**: Local preference is exchanged between iBGP neighbors only. Routes received from eBGP peers are assigned a local preference of 0. Whereas weight is used to make route selections without sending additional information to peers, local preference can be used to influence routing to iBGP peers.

- **Locally Originated Routes**: Any route that the local switch places into BGP is selected as best. This includes static routes, aggregate routes and redistributed routes.

- **Shortest AS Path**: The path received with the fewest number of ASN hops is selected.

- **Origin Check**: Preference is given to routes with an IGP origin (routes placed into BGP with a `network` statement) over incomplete origins (routes places into BGP through redistribution). The EGP origin attribute is no longer used.

- **Lowest MED**: The Multi-Exit Discriminator or MED is sent to eBGP peers to indicate a preference on how traffic enters an AS. A MED received from an eBGP peer is exchanged with iBGP peers but is reset to a value of 0 before advertising a prefix to another AS.

- **eBGP Routes**: A route received from an eBGP peer is preferred over a route learned from an iBGP peer.

- **Lowest IGP Cost to the Next Hop**: The route with the lowest IGP metric to reach the BGP next hop.

- **iBGP ECMP over eBGP ECMP**: If {{<link url="Optional-BGP-Configuration#ecmp" text="BGP multipath">}} is configured, prefer equal iBGP routes over equal eBGP routes, unless {{<link url="Optional-BGP-Configuration#ecmp" text="as-path multipath-relax">}} is also configured.

- **Oldest Route**: Preference is given to the oldest route in the BGP table.

- **Lowest Router ID**: Preference is given to the route received from the peer with the lowest Router ID attribute. If the route is received from a route reflector, the `ORIGINATOR_ID` attribute is used for comparison.

- **Shortest Route Reflector Cluster List**: If a route passes through multiple route reflectors, prefer the route with the shortest route reflector cluster list.

- **Highest Peer IP Address**: Preference is given to the route received from the peer with the highest IP address.

Cumulus Linux provides the reason it selects one path over another in NCLU `net show bgp` and vtysh `show ip bgp` command output for a specific prefix.

When BGP multipath is in use, if multiple paths are equal, BGP still selects a single best path to advertise to peers. This path is indicated as best with the reason, although multiple paths might be installed into the routing table.

### BGP Unnumbered

Historically, peers connect over IPv4 and TCP port 179, and after they establish a session, they exchange prefixes. When a BGP peer advertises an IPv4 prefix, it must include an IPv4 next hop address, which is usually the address of the advertising router. This requires that each BGP peer has an IPv4 address, which in a large network can consume a lot of address space, requiring a separate IP address for each peer-facing interface.

The BGP unnumbered standard, specified in {{<exlink url="https://tools.ietf.org/html/rfc5549" text="RFC 5549">}}, uses *extended next hop encoding* (ENHE) and no longer requires an IPv4 prefix to be advertised along with an IPv4 next hop. This means that you can set up BGP peering between your Cumulus Linux switches and exchange IPv4 prefixes without having to configure an IPv4 address on each switch; the interfaces that BGP uses are unnumbered.

The next hop address for each prefix is an IPv6 link-local address, which is assigned automatically to each interface. Using the IPv6 link-local address as a next hop instead of an IPv4 unicast address, BGP unnumbered saves you from having to configure IPv4 addresses on each interface.

When you use BGP unnumbered, BGP learns the prefixes, calculates the routes and installs them in IPv4 AFI to IPv6 AFI format. ENHE in Cumulus Linux does not install routes into the kernel in IPv4 prefix to IPv6 next hop format. For link-local peerings enabled by dynamically learning the other end's link-local address using IPv6 neighbor discovery router advertisements, an IPv6 next hop is converted into an IPv4 link-local address and a static neighbor entry is installed for this IPv4 link-local address with the MAC address derived from the link-local address of the other end.

{{%notice note%}}
- If an IPv4 /30 or /31 IP address is assigned to the interface, IPv4 peering is used over IPv6 link-local peering.
- BGP unnumbered only works with two switches at a time, as it is designed to work with point-to-point links.
- The IPv6 implementation on the peering device uses the MAC address as the interface ID when assigning the IPv6 link-local address, as suggested by RFC 4291.
- Every router or end host must have an IPv4 address to complete a `traceroute` of IPv4 addresses. In this case, the IPv4 address used is that of the loopback device. Even if extended next hop encoding (ENHE) is not used in the data center, link addresses are not typically advertised because they take up valuable FIB resources and also expose an additional attack vector for intruders to use to either break in or engage in DDOS attacks. Assigning an IP address to the loopback device is essential.
{{%/notice%}}

## Related Information

- {{<exlink url="https://www.nvidia.com/en-us/networking/border-gateway-protocol/" text="BGP in the Data Center by Dinesh G. Dutt">}} - a complete guide to Border Gateway Protocol for the modern data center
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
- {{<exlink url="https://tools.ietf.org/html/draft-walton-bgp-hostname-capability-02" text="draft-walton-bgp-hostname-capability-02, Fully Qualified Domain Name Capability for BGP">}}
