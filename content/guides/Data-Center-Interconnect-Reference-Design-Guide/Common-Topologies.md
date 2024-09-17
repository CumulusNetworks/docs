---
title: DCI Topologies
author: NVIDIA
weight: 20
product: Technical Guides
imgData: guides
---
This section of the document discusses DCI topologies.

## Physical Layer Topologies

There are several ways to interconnect the physical layer of multiple data centers. The most popular deployment strategies include dark fiber interconnect and dense wavelength division multiplexing (DWDM) interconnect.

Dark fibers provide for network redundancy through path diversity for each route; colored optics running over a *passive* DWDM provide the flexibility to scale interconnect capacity while using the same cabling infrastructure; colorless (gray) optics over an *active* DWDM environment provide the same advantages as colored optics. You can terminate the physical DCI links directly on the border leaf switches that are part of the EVPN or VXLAN fabric, or create an additional layer outside the fabric directly attached to border leaf switches. Choosing between these options depends on the existing network design, routing architecture, and physical constraints.

DCI architectures also influence the type of pluggable optics you use on border devices, regardless of physical termination location. When using a third-party DCI service provider for interconnection, if the equipment from the DCI provider is located in close proximity or on the same floor as the interconnect, use the most cost-effective and the simplest solution (for example, SR4, DR4, or FR4 optics). If the closest point of presence (PoP) for the DCI provider is not in close proximity to the data center, use long distance optics, such as LR4 or IR4.

For dark fiber implementations, consider LR4, IR4, ER4, or ZR4 optics. Alternately, build a CWDM or DWDM infrastructure for a multiplexing implementation that joins 100G connections over a single fiber pair, then choose between colored or gray optics. Choosing one optic over the other depends on the type of xWDM equipment you use, as well as factors such as cost, time, and available resources.

The following diagrams illustrate these options.

{{<img src="/images/guides/dark-fiber-interconnect.png">}}

{{<img src="/images/guides/dwdm-interconnect-i.png">}}

{{<img src="/images/guides/dwdm-interconnect-ii.png">}}

Regardless of your architecture, it is important to make sure that your devices and pluggables are compatible.

## Third-party Ethernet Services Providers

The following sections address physical layer considerations when implementing a solution through a third-party Ethernet service provider.

### MTU and Jumbo Frame Support

All overlay technologies (including EVPN and VXLAN) add overhead to data plane encapsulation. Although the VXLAN header itself is only eight bytes, it introduces greater overhead to the data packets by preserving the original layer 2, layer 3, and layer 4 headers inside the newly-constructed VXLAN tunnel frames that become part of the overlay payload. These VXLAN frames still require their own layer 2 and layer 3 destination address (VTEP destination), a UDP header, and the VXLAN header itself. The resulting overhead is *50 bytes*.

The following illustration compares VXLAN encapsulation overhead to an Ethernet frame:

{{<img src="/images/guides/vxlan-overhead.png">}}

Increasing the end-to-end MTU size avoids host-side and network-side fragmentation and ensures peak network performance. Local data centers typically achieve this by using jumbo frames. This means that traffic crossing a third-party layer 2 or layer 3 domain must have the same end-to-end jumbo frame capabilities. Otherwise, DCI traffic might experience bottlenecks or other problems caused by payload mismatches.

### ELINE and ELAN Interconnect

The example below shows a point-to-point <span class="a-tooltip">[EVC](## "Ethernet Virtual Connection")</span> or multipoint-to-multipoint EVC service provided by a third party. These services are called ELINE and ELAN. An example of an ELINE service is a pseudowire with an emulated end-to-end Ethernet service over multiprotocol label switching (MPLS). An example of an ELAN service is a virtual private LAN service (VPLS). Although it helps to know how these services work and what limitations they have, jumbo-frame support remains the most important consideration when choosing between third-party vendors.  

{{<img src="/images/guides/elineelan-interconnect.png">}}

### Security

Securing a layer 2 or layer 3 VPN service, either through a third-party provider or a dark fiber, is essential if you want to place an emphasis on security.

In the DCI context, security primarily refers to the data security pillar called *Confidentiality*, which means that your data is protected from unauthorized access and cannot be altered.

You can achieve confidentiality on the network layer with:
- <span class="a-tooltip">[IPsec](## "Internet Protocol Security")</span>, which operates at layer 3. You typically use IPsec with firewall hardware and software, not with switching hardware. 
- <span class="a-tooltip">[MACsec](## "Media Access Control security")</span>, which operates at layer 2. MACsec-encrypted traffic cannot cross a layer 2 boundary and you cannot route MACsec-encrypted traffic across an IP network. DCIs with dark fiber or CWDM/DWDM infrastructures support MACsec encryption, which is the NVIDIA recommended implementation for DCI security.
