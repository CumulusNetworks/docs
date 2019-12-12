---
title: Network Virtualization
author: Cumulus Networks
weight: 21
aliases:
 - /display/DOCS/Network+Virtualization
 - /pages/viewpage.action?pageId=8366427
product: Cumulus Linux
version: '4.0'
---
Cumulus Linux supports these forms of [network virtualization](http://en.wikipedia.org/wiki/Network_virtualization):

*VXLAN* (Virtual Extensible LAN) is a standard overlay protocol that abstracts logical virtual networks from the physical network underneath. You can deploy simple and scalable layer 3 Clos architectures while extending layer 2 segments over that layer 3 network.

VXLAN uses a VLAN-like encapsulation technique to encapsulate MAC-based layer 2 Ethernet frames within layer 3 UDP packets. Each virtual network is a VXLAN logical layer 2 segment. VXLAN scales to 16 million segments – a 24-bit VXLAN network identifier (VNI ID) in the VXLAN header – for multi-tenancy.

Hosts on a given virtual network are joined together through an overlay protocol that initiates and terminates tunnels at the edge of the multi-tenant network, typically the hypervisor vSwitch or top of rack. These edge points are the VXLAN tunnel end points (VTEP).

Cumulus Linux can initiate and terminate VTEPs in hardware and supports wire-rate VXLAN. VXLAN provides an efficient hashing scheme across the IP fabric during the encapsulation process; the source UDP port is unique, with the hash based on layer 2 through layer 4 information from the original frame. The UDP destination port is the standard port 4789.

Cumulus Linux includes the native Linux VXLAN kernel support and integrates with controller-based overlay solutions like [VMware NSX](Virtualization-Integrations/Integrating-Hardware-VTEPs-with-VMware-NSX-MH/) and [Midokura MidoNet](Virtualization-Integrations/Integrating-Hardware-VTEPs-with-Midokura-MidoNet-and-OpenStack/).

VXLAN is supported only on switches in the [Cumulus Linux HCL](https://www.cumulusnetworks.com/hcl/) using the Broadcom Tomahawk, Trident II, Trident II+ and Trident3 chipsets, as well as the Mellanox Spectrum chipset.

{{%notice note%}}

VXLAN encapsulation over layer 3 subinterfaces (for example, swp3.111) or SVIs is not supported as traffic transiting through the switch may get dropped; even if the subinterface is used only for underlay traffic and does not perform VXLAN encapsulation, traffic may still get dropped. Only configure VXLAN uplinks as layer 3 interfaces without any subinterfaces (for example, swp3).

The VXLAN tunnel endpoints cannot share a common subnet; there must be at least one layer 3 hop between the VXLAN source and destination.

{{%/notice%}}

## Caveats and Errata

### Cut-through Mode and Store and Forward Switching

On switches using Broadcom Tomahawk, Trident II, Trident II+, and Trident3 ASICs, Cumulus Linux supports store and forward switching for VXLANs but does **not** support [cut-through mode](../../Layer-1-and-Switch-Ports/Buffer-and-Queue-Management#configure-cut-through-mode-and-store-and-forward-switching).

On switches using Mellanox Spectrum ASICs, Cumulus Linux supports cut-through mode for VXLANs but does **not** support store and forward switching.

### MTU Size for Virtual Network Interfaces

The maximum transmission unit (MTU) size for a virtual network interface should be 50 bytes smaller than the MTU for the physical interfaces on the switch. For more information on setting MTU, read [Layer 1 and Switch Port Attributes](../Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes/).

### VLANs and VXLANs Cannot Share the Same ID

The layer 3 VNI and layer 2 VNI cannot share the same number space; that is, you cannot have *vlan10* and *vxlan10*, for example. Otherwise, the layer 2 VNI does not get created.

## Useful Links

- [VXLAN - RFC 7348](https://tools.ietf.org/html/rfc7348)
- [ovsdb-server](http://openvswitch.org/support/dist-docs/ovsdb-server.1.html)
