---
title: Common DCI Topologies
author: Cumulus Networks
weight: 20
product: Cumulus Networks Guides
imgData: guides
---

## Physical Layer Topologies

Several options are available to interconnect the physical layer of multiple data centers.  

Dark fibers provide for network redundancy through path diversity for each route; colored optics running over a passive dense wavelength division multiplexing (DWDM) provide the flexibility to scale interconnect capacity while using the same cabling infrastructure; colorless (gray) optics with an active DWDM environment provide the same advantages. You can terminate the physical DCI links directly on the border leaf nodes that are part of the EVPN/VXLAN fabric, or create an additional layer, outside the fabric and directly attached to border leaf nodes. Choosing between these options depends on the existing network design, routing architecture, and physical constraints.

The choice of DCI architecture also influences the type of pluggable optics used on border devices, irrespective of its physical termination location. When using a third-party DCI service provide for interconnection, and if the DCI provider's equipment is located in close proximity or on the same floor as the interconnect, use the most cost-effective and the simplest solution (for example, SR4, DR4, or FR4 optics). If the DCI provider’s closest point of presence (PoP) is not in close proximity to the data center, use long-distance optics such as LR4 or IR4. 

For dark fiber implementations, consider LR4, IR4, ER4, ZR4 optics. Alternately, build a CWDM/DWDM infrastructure for a multiplexing implementation that joins 100G connections over a single fiber pair. In such circumstances, the utilization of colored and gray optics becomes relevant and the choice depends on the type of xWDM equipment being used, as well as factors such as cost, time, and available resources. 

Regardless of your architecture, it's important to make sure that your devices and pluggables are compatible. Refer to NVIDIA's {{<exlink url=https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/ text="hardware compatibility list">}} for more information about hardware support.

{{<img src= "/images/guides/dwdm-interconnect-i.png">}}

{{<img src= "/images/guides/dwdm-interconnect-ii.png">}}

## Using a Third-Party Ethernet Services Provider

The following sections address important physical layer considerations when implementing a solution through a third-party Ethernet services provider.

### MTU and Jumbo Frame Support

All overlay technologies (including EVPN/VXLAN) add overhead to data-plane encapsulation. In the case of VXLAN, although the VXLAN header itself is only 8 bytes, it introduces greater overhead to the data packets. This is to preserve the original L2 + L3 + L4 headers inside the newly-constructed VXLAN tunnel frames that become part of the overlay payload. Additionally, these VXLAN frames still require their own L2/L3 destination address (VTEP destination), a UDP header, and the VXLAN header itself. The resulting overhead is *50 bytes*.

The following diagram compares VXLAN encapsulation overhead to an Ethernet frame:

{{<img src= "/images/guides/vxlan-overhead.png">}}

Increasing the end-to-end MTU size avoids host-side and network-side fragmentation while receiving peak network performance. Local data centers typically achieve by using jumbo frames. This means that traffic crossing a third-party's L2/L3 domain must have the same end-to-end jumbo frame capabilities. Otherwise, DCI traffic might experience bottlenecks or other problems caused by payload mismatches.
### ELINE and ELAN Interconnect

The figure below is an example of a point-to-point EVC (Ethernet Virtual Connection) or multipoint-to-multipoint EVC service provided by a third party. These services are called ELINE and ELAN, respectively. An example of an ELINE service is a pseudowire with emulated end-to-end Ethernet service over MPLS; an example of an ELAN service is VPLS. It helps to know how these services work, what their limitations are. You can request their KPIs from the third-party provider, but keep in mind that jumbo frame support remains the most important consideration.  

{{<img src= "/images/guides/eline-interconnect.png">}}

### Security

Securing an L2 or L3 VPN service, either through a third-party provider or a dark fiber, is essential for customers who place an emphasis on security. 

In the DCI context, security primarily refers to the data security pillar called “Confidentiality.” Confidentiality means that your data is protected from unauthorized access and cannot be altered. There are two main ways to achieve confidentiality on the network layer for a point-to-point line. One of them is IPSEC, which operates at layer 3 and the other is MACsec, which operates at layer 2. IPSEC is not typically used for switching hardware and is usually covered by vendors implementing firewall hardware and software.Because MACsec operates at layer 2, MACsec-encrypted traffic cannot cross a layer 2 boundary. That means MACsec-encrypted traffic cannot be routed across an IP network. DCIs with dark fiber or CWDM/DWDM infrastructures support MACsec encryption.