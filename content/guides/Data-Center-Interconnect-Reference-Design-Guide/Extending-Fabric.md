---
title: Extending the EVPN/VXLAN Fabric with DCI
author: Cumulus Networks
weight: 30
product: Cumulus Networks Guides
imgData: guides
---

In this section we describe how to extend EVPN/VXLAN fabrics across data centers and use EVPN/VXLAN to interconnect them. Since EVPN/VXLAN leverages control-plane MAC learning, as opposed to traditional Ethernet switching, we need to extend the signaling (control-plane) domain across data centers or interconnect multiple control-plane domains. 

This environment demonstrates a best-practice configuration for several use cases including Layer-2 extension using EVPN signaling with Type-1, Type-2 and Type-4 routes; L3 extension and routing using EVPN Type-5 routes; and inter-VLAN routing using the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing/" text="EVPN symetric routing">}} for {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/EVPN-Network-Reference/EVPN-Deployment-Scenarios/#distributed-routing" text="distributed routing">}} in an EVPN/VXLAN fabric. We will also touch upon a route leaking scenario for inter POD communication. We will use the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-Object-Model/" text="NVUE Object Model">}} and NVUE CLI {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-CLI/" text="NVUE CLI">}} to set an all-active-server-redundant environment with an {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-Multihoming/" text="EVPN multihoming">}} to configure an EVPN fabric with standardized L2 redundancy on ToR switches. It's important to note that all PODs referenced in this document belong to the same administrative domain or are under the same organization. This document does not address interconnects of different fabrics belonging to different administrative domains. The design on each POD is orthogonal to the other.  

When using the symmetric model, each VTEP bridges and routes the traffic (ingress and egress). Layer 2 traffic is bridged (VLAN-L2VNI) on the leaf ingress host port, then routed to a special transit VNI which is used for all routed VXLAN traffic, called L3VNI. All VXLAN traffic must be routed onto this L3VNI, tunneled across the layer 3 infrastructure, and routed off L3VNI to the appropriate VLAN at the destination VTEP, and ultimately bridged to the destination host. 

In this model, the leaf switches only need to host the VLANs (mapped to VNIs) located on the rack, the L3VNI, and its associated VLAN. This is because the ingress leaf switch does not need to know the destination VNI. 

Multitenancy requires one L3VNI per VRF, and all switches participating in that VRF must be configured with the same L3VNI. The egress leaf uses the L3VNI to identify the VRF that routes the packet. For additional examples, refer to the Cumulus Linux documentation {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing/" text="Cumulus Linux documentation">}} and {{<exlink url="https://developer.nvidia.com/blog/looking-behind-the-curtain-of-evpn-traffic-flows/" text="EVPN traffic flows in a virtualized environment">}}.

{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-54/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-Multihoming/" text="EVPN multihoming">}}(EVPN-MH) is the standards-based MLAG replacement for providing L2 server redundancy on the top-of-rack level.

## BUM Traffic

Head-end-replication (HER), or ingress replication, uses an inclusive multicast Ethernet tag (IMET) route (Type-3) for auto discovery of remote PEs to set up BUM traffic over VXLAN. This is the default configuration option. You can alternatively use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Protocol-Independent-Multicast-PIM/" text="Protocol-Independent Multicast Sparse Mode">}} (PIM-SM), however for DCI environments, PIM design is complex and requires additional planning. It’s important to keep in mind that most third-party E-LINE, E-LAN, L3VPN, and VPWS service providers do not support multicast traffic. For data center interconnect over dark fiber, DWDM using multicast underlay routing with PIM-SM equates to a significant multicast network design challenge. NVIDIA recommends HER for the DCI context. 

## Designing your EVPN/VXLAN Fabric

The section covers the basic considerations for designing your DCI's EVPN/VXLAN fabric. For detailed information, refer to the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/EVPN-Network-Reference/" text="Cumulus Linux VXLAN and EVPN Network Reference Design Guide">}}.

### Planning an Autonomous System Number Schema

The following is a list of autonomous system (AS) numbering schema considerations across the DCI's {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/EVPN-Network-Reference/Data-Center-Networking-Concepts/#ethernet-virtual-private-network" text="EVPN fabric">}}: 

https://docs.nvidia.com/networking-ethernet-software/guides/EVPN-Network-Reference/Data-Center-Networking-Concepts/#ethernet-virtual-private-network

- Assign a unique identifier (AS number) to each logical group of devices. 
- Assign each leaf its own, unique AS number. 
- Assign each group of spines (all the spines connected to the same set of leaves or PODs) a common AS number. Each POD in the network should have a unique set of AS numbers for its spines. 
- Assign each group of super-spines (connected to the same set of spines) a common AS number. 
- Assign each border leaf pair (or triplet) belonging to the same POD a common AS number. Each POD in the network should have a unique set of AS numbers for its border leafs.  

The purpose of assigning each border-leaf pair a common AS number is to prevent locally advertised prefixes from each POD from circling back over the redundant path via the border leafs of the interconnected POD (via DCI). This problem is avoided with a single DCI link in between PODs, as there’s only one path between each POD, without any redundancy. One caveat of having a common AS number on border leaf nodes is that it prevents border leaf nodes from serving hosts with EVPN-MH connections, as EVPN-MH requires different AS numbers on participating leaf nodes. 

### Underlay and Overlay Considerations

EVPN/VXLAN is an overlay technology which creates an underlay topology independent fabric with multitenancy, redundancy, and load-balancing capabilities. However, to establish VXLAN tunnels from leaf-to-leaf, the network must distribute tunnel source addresses (usually a loopback) via an underlay routing protocol. This allows all VXLAN peers to have each tunnel destination’s host-route as a /32 prefix in their respective routing tables. This is a fundamental principle of EVPN/VXLAN---each leaf requires a host route of all the corresponding PEs’ VXLAN tunnel destination addresses in its routing table so that it can establish end-to-end VXLAN tunnels.

You can show this through the following command:

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan source 
         operational  applied 
-------  -----------  ---------- 
address  10.10.10.1   10.10.10.1    
```
The VXLAN tunnel source address configuration is applied with the following NVUE configuration statement: 

```
nv set nve vxlan source address 10.10.10.1 
```

For underlay, any well-known IGP that can quickly converge and provide multipath is sufficient, such as OSPF, IS-IS, and BGP. OSPF is popular in enterprise environments and is a safe choice. However, OSPF has been rejected by web-scale operators due to its lack of multiprotocol support. OSPFv2 is used in enterprise environments because IGP has been designed for IPv4 and OSPFv3 is for IPv6. Therefore, if you would like an OSPF-only underlay with multiprotocol support, you will need to run two separate instances of OSPF, which means additional configurations, more troubleshooting, and increased operational burden. 

For IS-IS, many operators felt that a link-state protocol was inherently unsuited for a richly connected network such as the Clos topology. Link-state protocols propagate link-state changes to all routers in their respective area, even to routers that have no direct connection or dependency on the failed link.  

BGP addresses these limitations and was designed to scale and provide a loop-free topology at any size. It powers the internet, is well-known to engineers and has a standardized implementation across the entire vendor ecosystem. It’s less chatty than link-state routing protocols and natively supports multi-protocol extensions (IPv4, IPv6, MPLS, and EVPN). However, it requires {{<exlink url="https://www.rfc-editor.org/rfc/rfc7938" text="a few modifications">}} for it to operate in a data center.

Our next question is whether to use iBGP, eBGP, or both in an underlay + overlay environment. Given that the entire network is under the same administrative domain and therefore belongs to the same entity or company, iBGP seems like the obvious choice. However, in modern data centers eBGP is the most common deployment model. The main reason is that eBGP is simpler to understand and deploy than iBGP. iBGP’s path-selection algorithm can be confusing in terms of the rules that govern which routes are forwarded and which are not. There are also limitations to iBGP’s multipath support under certain conditions, such as when a route is advertised by two different nodes. And there is still no consensus on the positioning of iBGP route reflectors.  

The routing protocol stack used by Cumulus Linux is FRR. When used with Cumulus Linux, FRR uses a “datac center” profile configuration, which configures the hold timer to 9 seconds and keepalive timer to 3 seconds for BGP. This is to reduce BGP’s default convergence timers. Because of this, BGP used in a data center environment has a unique behavior, detailed extensively in {{<exlink url="https://www.nvidia.com/en-us/networking/border-gateway-protocol/" text="BGP in the Data Center">}}.

This document focuses on eBGP as an underlay and overlay environment. We use the default routing instance (VRF) for underlay communication and distributing our VTEP sources and use non-default (also non-mgmt) VRF instances for individual EVPN tenants.  
### Planning Route Targets and Route Distinguishers

When there is no explicit configuration for {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-Enhancements/#define-rds-and-rts" text="RD and RT">}} import/export statements for a VNI, Cumulus Linux derives them automatically in `<vxlan-local-tunnelip>:<VNI>` format for RD and `<AS>:<VNI>` format for RT. Although it’s possible to explicitly define an RD per VNI, it’s also acceptable auto-derive it (by not defining an RD).  

Route targets are used to define which VPN a BGP learned or locally injected prefix belongs to. They’re the mechanism we use to control VPN memberships of prefixes. A prefix could be a member of a single VPN or multiple VPNs. For this reason, in this document, we’d rather not use auto generated route-targets but instead use auto-import/export functionality. We will manually define our own route-targets and will import/export them. In the case that different VNIs are used per DC location or POD (like in downstream VNI), we need to make sure that import statements cover the corresponding route-targets. This is how the examples in this document have been set up.  

### Planning Ethernet Segment Identifiers

Ethernet segment identifiers (ESIs) define multihomed Ethernet segments and use EVPN Type-1 and Type-4 routes. When extending Layer 2 across data centers, these routes are also exchanged over DCI and ESIs local to a POD become globally significant across the entire EVPN fabric and must be unique for each Ethernet segment. Cumulus Linux derives a 10-byte ESI value (Type 3) from Ethernet segment system MAC address (6-byte) and a local discriminator value (3-byte) as described in this document.  

However, you can also plan and configure the ESI numbering scheme across the entire fabric manually. You must have a unique ESI, which you can configure with the following command:

```
nv set interface <interface> evpn multihoming segment identifier <ESI number> 
```

Note that the ESI number for the configuration must start with ‘00’ (which indicates that the ESI is managed and configured by the operator) and must be separated by colons, for example `00:00:00:00:00:00:aa:00:00:01`.

For a Layer 3 extension (VRF handover) where only Type-5 prefixes are exchanged, ESI numbers are less significant. This is because Type-1 and Type-4 prefixes are not passed on to DCI. However, consistent, unique ESIs across the fabric are a design best practice.

<!--insert EVPN deployment with eBGP diagram>