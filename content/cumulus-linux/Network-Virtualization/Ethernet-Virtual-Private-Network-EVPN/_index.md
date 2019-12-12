---
title: Ethernet Virtual Private Network - EVPN
author: Cumulus Networks
weight: 143
aliases:
 - /display/DOCS/Ethernet+Virtual+Private+Network+++EVPN
 - /pages/viewpage.action?pageId=8366455
product: Cumulus Linux
version: '4.0'
---
VXLAN is the de facto technology for implementing network virtualization in the data center, enabling layer 2 segments to be extended over an IP core (the underlay). The initial definition of VXLAN ([RFC 7348](https://tools.ietf.org/html/rfc7348)) did not include any control plane and relied on a flood-and-learn approach for MAC address learning.

Ethernet Virtual Private Network (EVPN) is a standards-based control plane for VXLAN defined in [RFC 7432](https://tools.ietf.org/html/rfc7432) and [draft-ietf-bess-evpn-overlay](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-overlay/) that allows for building and deploying VXLANs at scale. It relies on multi-protocol BGP (MP-BGP) to exchange information and is based on BGP-MPLS IP VPNs ([RFC 4364](https://tools.ietf.org/html/rfc4364)). It enables not only bridging between end systems in the same layer 2 segment but also routing between different segments (subnets). There is also inherent support for multi-tenancy. EVPN is often referred to as the means of implementing *controller-less VXLAN*.

Cumulus Linux fully supports EVPN as the control plane for VXLAN, including for both intra-subnet bridging and inter-subnet routing, and provides these key features:

- VNI membership exchange between VTEPs using EVPN type-3 (Inclusive multicast Ethernet tag) routes.
- Host MAC and IP address exchange using EVPN type-2 (MAC/IP advertisement) routes.
- [Host/VM mobility](../Ethernet-Virtual-Private-Network-EVPN/EVPN-Enhancements#extended-mobility) support (MAC and IP moves) through exchange of the MAC Mobility Extended community.
- Dual-attached hosts via [VXLAN active-active mode](../VXLAN-Active-Active-Mode/). MAC synchronization between the peer switches is done using [MLAG](../../Layer-2/Multi-Chassis-Link-Aggregation-MLAG/).
- [ARP/ND suppression](../Ethernet-Virtual-Private-Network-EVPN/Basic-Configuration#arp-and-nd-suppression), which enables VTEPs to suppress ARP flooding over VXLAN tunnels is enabled by default on VNIs in Cumulus Linux.
- Exchange of [static MAC addresses](../Ethernet-Virtual-Private-Network-EVPN/EVPN-Enhancements#configure-static-mac-addresses) through EVPN.
- [Inter-subnet routing](../Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing/) for both IPv4 and IPv6 hosts: Distributed symmetric routing between different subnets, distributed asymmetric routing between different subnets, and centralized routing.
- [Prefix-based routing](../Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing/#prefix-based-routing-evpn-type-5-routes) using EVPN type-5 routes (EVPN IP prefix route)
- Layer 3 multi-tenancy.
- IPv6 tenant routing.
- ECMP for overlay networks on RIOT-capable Broadcom ASICs (Trident 3, Maverick, Trident 2+) in addition to Tomahawk and Mellanox Spectrum-A1 ASICs. No configuration is needed, ECMP occurs in the overlay when there are multiple next hops.
- Head end replication is enabled by default in Cumulus Linux on Broadcom Tomahawk, Maverick, Trident3, Trident II+, and Trident II ASICs and switches with Mellanox Spectrum ASICs. Cumulus Linux supports up to 128 VTEPs with head end replication.

The EVPN address-family is supported with both eBGP and iBGP peering. If the underlay routing is provisioned using eBGP, you can use the same eBGP session to carry EVPN routes. For example, in a typical 2-tier Clos network topology where the leaf switches are the VTEPs, if eBGP sessions are in use between the leaf and spine switches for the underlay routing, the same sessions can be used to exchange EVPN routes; the spine switches merely act as *route forwarders* and do not install any forwarding state as they are not VTEPs. When EVPN routes are exchanged over iBGP peering, OSPF can be used as the IGP or the next hops can also be resolved using iBGP.

{{%notice note%}}

- The routing control plane (including EVPN) is installed as part of the [FRRouting](https://frrouting.org/) (FRR) package. For more information about FRR, refer to the [FRR Overview](../../Layer-3/FRRouting-Overview/).
- Data plane MAC learning is disabled by default on VXLAN interfaces. Do *not* enable MAC learning on VXLAN interfaces: EVPN is responsible for installing remote MACs.

{{%/notice%}}

For information about VXLAN routing, including platform and hardware limitations, see [VXLAN Routing](../VXLAN-Routing/).
