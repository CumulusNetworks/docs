---
title: Extending the EVPN/VXLAN Fabric with DCI
author: Cumulus Networks
weight: 30
product: Cumulus Networks Guides
imgData: guides
---

In this section we describe how to extend EVPN/VXLAN fabrics across data centers and use EVPN/VXLAN to interconnect them. Since EVPN/VXLAN leverages control-plane MAC learning, as opposed to traditional ethernet switching, we need to extend the signaling (control-plane) domain across data centers or interconnect multiple control-plane domains. 

This environment demonstrates a best-practice configuration for several use cases including Layer-2 extension using EVPN signaling with Type-1, Type-2 and Type-4 routes, L3 extension/routing use case using EVPN Type-5 routes and inter-VLAN routing using EVPN symmetric model for an edge routed - distributed routing at the leaves – in an  EVPN/VXLAN fabric. We will also touch upon a route leaking scenario for inter POD communication. We use the NVUE Object Model and NVUE CLI to set an all-active-server-redundant environment with an EVPN Multihoming configuration to present an EVPN fabric with standardized L2 redundancy on the ToR switches. One of the important aspects here is that we assume all PODs in upcoming use cases belong to the same administrative domain or under the same organization. We are not covering any use case here that interconnects different fabrics belonging to different administrative domains. This is important so that the design on each POD is orthogonal to the  other.  

When using the symmetric model, each VTEP bridges and routes the traffic (ingress and egress). The layer 2 traffic is  bridged (VLAN-L2VNI) on the leaf ingress host port, then routed to a special transit VNI which is used for all routed VXLAN traffic, called L3VNI. All VXLAN traffic must be routed onto this L3VNI, tunneled across the layer 3 infrastructure, and routed off L3VNI to the appropriate VLAN at the destination VTEP and ultimately bridged to the destination host. 

In this model, the leaf switches only need to host the VLANs (mapped to VNIs) located on its rack and L3VNI and its associated VLAN. This is because the ingress leaf switch doesn’t need to know the destination VNI. 

Multitenancy requires one L3VNI per VRF, and all switches participating in that VRF must be configured with the same L3VNI. The egress leaf uses the L3VNI to identify the VRF by which to route the packet. 

Check out the Cumulus Linux documentation for more information and examples. 

This blog that explains the EVPN traffic flows in a virtualized environment. 

EVPN Multihoming EVPN-MH is the standards-based replacement for MLAG to provide L2 server redundancy on to the Top-of-Rack level.

## BUM Traffic

Head-End-Replication (HER) or Ingress Replication uses Inclusive Multicast Ethernet Route (Type-3) for auto discovery of remote PEs to set up BUM traffic over VXLAN. This is the default configuration option. Alternatively Protocol Independent Multicast Sparse Mode - PIM-SM can be used, however for DCI environments, PIM would require complex design and planning. It’s important to keep in mind that most of 3rd party E-LINE, E-LAN, L3VPN, VPWS service providers do not support multicast traffic over the managed ethernet service they provide. For the scenarios involving data center interconnect over dark fiber, DWDM using multicast underlay routing with PIM-SM means a significant multicast network design challenge. Therefore, for DCI scenarios sticking with HER is strongly recommended. 

## Designing your EVPN/VXLAN Fabric

For a detailed understanding of EVPN/VXLAN Fabrics and design principles, refer to the Cumulus Linux VXLAN and EVPN Network Reference Design Guide before continuing with the following parts. 
### Planning an Autonomous System Number Schema

One thing to add on top of Ethernet Virtual Private Network section of the document is the AS numbering schema across EVPN Fabric with DCI consideration and border leaf nodes: 

- Assign a unique identifier (AS number) to each logical group of devices. 
- Assign each leaf its own, unique AS number. 
- Assign each group of spines (all the spines connected to the same set of leaves or PODs) a common autonomous-system (AS number) number. Each POD in the network should have a unique set of AS numbers for its spines. 
- Assign each group of super-spines (connected to the same set of spines) a common AS number. 
- Assign each border leaf pair (or triplet) belonging to the same POD a common AS number. Every POD in the network should have a unique set of AS numbers for its border leaves.  

The purpose of assigning each border leaf pair a common AS number is to prevent locally advertised prefixes by each POD to be circled back to itself over the redundant path via border leaves of the interconnected POD (via DCI). This problem doesn’t occur when there’s a single DCI link in between PODs, as there’s only a single path between each POD without any redundancy. One caveat of this common AS number on border leaf nodes is that prevents border leaf nodes to serve hosts with EVPN-MH connections, as EVPN-MH requires different AS numbers on participating leaf nodes. 

### Underlay and Overlay Considerations

EVPN/VXLAN is an overlay technology which creates an underlay topology independent fabric with multitenancy, redundancy, and load-balancing capabilities. However, to establish VXLAN tunnels from leaf to leaf, we  need to distribute tunnel source addresses (usually loopback) via an underlay routing protocol. This allows all VXLAN peers to have each tunnel destination’s host-route as a /32 prefix in their respective routing tables. This is a  fundamental principle of EVPN/VXLAN---that each leaf needs a host route of all the corresponding PEs’ VXLAN tunnel destination address in its routing table, so that it can establish end-to-end VXLAN tunnels. 

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan source 
         operational  applied 
-------  -----------  ---------- 
address  10.10.10.1   10.10.10.1    
```
VXLAN tunnel source address configuration is applied with the following NVUE configuration statement: 

```
nv set nve vxlan source address 10.10.10.1 
```
This is where underlay comes into play. And for underlay any well-known IGP that can quickly converge and provide multipath is sufficient, such as OSPF, IS-IS, and BGP. OSPF is well-known to all enterprise environments, therefore it’s a safe choice. However, OSPF has been rejected by most web-scale operators due to its lack of multiprotocol support. OSPFv2 is used by almost all enterprise environments as IGP has been designed for IPv4 only and OSPFv3 is for IPv6 only. Therefore, if you would like an OSPF-only underlay with multiprotocol support, you will need to run two separate instances of OSPF,  which contributes to additional  configurations, more troubleshooting, and expanded operational burden. 

As for IS-IS, many operators felt that a link-state protocol was inherently unsuited for a richly connected network such as the Clos topology. Link-state protocols propagate link-state changes to all routers in their area, even to routers that have no direct connection or dependency on the failed link.  

This is where BGP stepped in and filled the gap which others couldn’t. BGP was designed to scale and to provide a loop-free topology at any size. It powers the internet, is well-known to seasoned engineers and has a standardized implementation across the entire vendor ecosystem. It’s less chatty than link-state routing protocols and natively supports multi-protocol extensions (IPv4, IPv6, MPLS and EVPN). However, it requires a few tweaks to operate in a data center. As a consequence, we end up with RFC7938. 

Our next question is whether to use iBGP, eBGP, or both in an underlay + overlay environment. Given that this entire network is under the same administrative domain and therefore belongs to the same entity or company, iBGP seems like the obvious choice. But, in modern data centers eBGP is the most common deployment model. The main reason is that eBGP is simpler to understand and deploy than iBGP. iBGP’s path selection algorithm can be confusing in terms of the rules that govern which routes are forwarded and which are not . There are also limitations to iBGP’s multipath support under certain conditions, such as when a route is advertised by two different nodes. And the debate about the positioning of iBGP route reflectors continues.  

The routing protocol stack used by Cumulus Linux is FRR. When used with Cumulus Linux, FRR uses a “datacenter” profile configuration, which configures the hold timer to 9 seconds and keepalive timer to 3 seconds for BGP. This is to reduce BGP’s default convergence timers. Thus, Because of this, BGP used in a data center environment has a certain behavior, which detailed extensively in  “BGP in the Data Center” . Before going into the guts of Cumulus Linux and it’s strongly recommended to read RFC 7938 and BGP in Data Center book which is available for download from our documentation. 

This document focuses on eBGP as an underlay and overlay environment. We use the default routing instance (VRF) for underlay communication and distributing our VTEP sources and use non-default (also non-mgmt) VRF instances for individual EVPN tenants.  
### Planning Route Targets and Route Distinguishers

Based on Cumulus Linux documentation - Define RDs and RTs – if there’s no explicit configuration for RD and RT import/export statements for a VNI, we know that Cumulus Linux derives them automatically in <vxlan-local-tunnelip>:<VNI> format for RD and <AS>:<VNI> format for RT. It’s possible to explicitly define an RD per VNI as mentioned in the documentation. Nevertheless, it’s acceptable to leave it to auto generation by not defining an RD.  

Route-targets are used to define which VPN a BGP learned or locally injected prefix belongs to.  They’re the knobs we use to control VPN memberships of prefixes. A prefix could be a member of a single VPN or multiple VPNs. For this reason, in this document, we’d rather not use auto generated route-targets but instead use auto-import/export functionality. We will manually define our own route-targets and will import/export them. In the case that different VNIs are used per DC location or POD (like in downstream VNI), we need to make sure that import statements cover the corresponding route-targets. This is how the examples in this document have been set up.  

### Planning Ethernet Segment Identifiers

Ethernet segment identifiers (ESIs) define multihomed Ethernet segments and use EVPN Type-1 and Type-4 routes. For the use case that we extend Layer-2 across data centers, these routes are also exchanged over DCI and ESIs local to a POD become globally significant across entire EVPN fabric and must be unique for each Ethernet Segment, therefore cannot overlap. Cumulus Linux derives 10-byte ESI value (Type 3) from Ethernet segment system MAC address (6-byte) and local discriminator value (3-byte) as described here.  

However, a user can choose to plan and configure the ESI numbering scheme across the entire fabric manually. The uniqueness of ESI is essential, and it is configured as follows:

```
nv set interface <interface> evpn multihoming segment identifier <ESI number> 
```

Note that ESI number for the configuration above must start with ‘00’ (indicates ESI is managed and configured by the operator) and must be separated by colons, for instance ‘00:00:00:00:00:00:aa:00:00:01’ 

For the Layer3 extension (VRF handover) use case where only Type-5 prefixes are exchanged, the significance of ESI numbers technically does not matter as Type-1 and Type-4 prefixes are not passed on to data center interconnect, but for a clean design it still makes sense to make sure that the ESI numbering in the entire fabric is unique. 

<!--insert EVPN deployment with eBGP diagram>