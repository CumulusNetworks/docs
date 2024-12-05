---
title: Ethernet Virtual Private Network - EVPN
author: NVIDIA
weight: 540
toc: 3
---
VXLAN enables layer 2 segments to extend over an IP core (the underlay). The initial definition of VXLAN ({{<exlink url="https://tools.ietf.org/html/rfc7348" text="RFC 7348">}}) does not include any control plane and relied on a flood-and-learn approach for MAC address learning.

<span class="a-tooltip">[EVPN](## "Ethernet Virtual Private Network")</span> is a standards-based control plane for VXLAN defined in {{<exlink url="https://tools.ietf.org/html/rfc7432" text="RFC 7432">}} and {{<exlink url="https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-overlay/" text="draft-ietf-bess-evpn-overlay">}} that allows for building and deploying VXLANs at scale. It relies on multi-protocol BGP (MP-BGP) to exchange information and uses BGP-MPLS IP VPNs ({{<exlink url="https://tools.ietf.org/html/rfc4364" text="RFC 4364">}}). It enables not only bridging between end systems in the same layer 2 segment but also routing between different segments (subnets). There is also inherent support for multi-tenancy.

Cumulus Linux installs the routing control plane (including EVPN) as part of the {{<exlink url="https://frrouting.org/" text="FRR">}} package. For more information about FRR, refer to {{<link url="FRRouting">}}.

## Key Features

Cumulus Linux fully supports EVPN as the control plane for VXLAN, including for both intra-subnet bridging and inter-subnet routing, and provides these key features:

- VNI membership exchange between <span class="a-tooltip">[VTEPs](## "Virtual Tunnel End Points")</span> using EVPN type-3 (Inclusive multicast Ethernet tag) routes.
- Host MAC and IP address exchange using EVPN type-2 (MAC and IP advertisement) routes.
- {{<link url="EVPN-Enhancements#extended-mobility" text="Host/VM mobility">}} support (MAC and IP moves) through exchange of the MAC Mobility Extended community.
- Dual-attached hosts via {{<link url="VXLAN-Active-active-Mode" text="VXLAN active-active mode">}}. {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} synchronizes MAC addresses between the peer switches.
- {{<link url="Basic-Configuration#arp-and-nd-suppression" text="ARP/ND suppression">}} is on VNIs by default, which enables VTEPs to suppress <span class="a-tooltip">[ARP](## "Address Resolution Protocol")</span> flooding over VXLAN tunnels.
- Exchange of {{<link url="EVPN-Enhancements#configure-static-mac-addresses" text="static MAC addresses">}} through EVPN.
- {{<link url="Inter-subnet-Routing" text="Inter-subnet routing">}} for both IPv4 and IPv6 hosts: Distributed symmetric routing between different subnets and centralized routing.
- {{<link url="Inter-subnet-Routing#prefix-based-routing-evpn-type-5-routes" text="Prefix-based routing">}} using EVPN type-5 routes (EVPN IP prefix route).
- Layer 3 multi-tenancy.
- IPv6 tenant routing.
- <span class="a-tooltip">[ECMP](## "Equal Cost Multi Path")</span> for overlay networks on NVIDIA Spectrum-A1 ASICs. ECMP occurs in the overlay when there are multiple next hops.
- Head end replication is on by default.

Cumulus Linux supports the EVPN address family with both <span class="a-tooltip">[eBGP](## "external BGP")</span> and <span class="a-tooltip">[iBGP](## "internal BGP")</span> peering. If you configure underlay routing with eBGP, you can use the same eBGP session to carry EVPN routes. In a typical 2-tier Clos network where the leafs are VTEPs, if you use eBGP sessions between the leafs and spines for underlay routing, the same sessions exchange EVPN routes. The spine switches act as *route forwarders* and do not install any forwarding state as they are not VTEPs. When the switch exchanges EVPN routes over iBGP peering, you can use OSPF as the IGP or resolve next hops using iBGP.

{{%notice note%}}
Cumulus Linux disables data plane MAC learning by default on VXLAN interfaces. Do *not* enable MAC learning on VXLAN interfaces: EVPN installs remote MACs.
{{%/notice%}}
