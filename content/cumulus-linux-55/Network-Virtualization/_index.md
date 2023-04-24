---
title: Network Virtualization
author: NVIDIA
weight: 530
toc: 2
---
<span style="background-color:#F5F5DC">[VXLAN](## "Virtual Extensible LAN")</span> is a standard overlay protocol that abstracts logical virtual networks from the physical network underneath. You can deploy simple and scalable layer 3 Clos architectures while extending layer 2 segments over that layer 3 network.

VXLAN uses a VLAN-like encapsulation technique to encapsulate MAC-based layer 2 Ethernet frames within layer 3 UDP packets. Each virtual network is a VXLAN logical layer 2 segment. VXLAN scales to 16 million segments - a 24-bit VXLAN network identifier (VNI ID) in the VXLAN header - for multi-tenancy.

Hosts on a given virtual network join together through an overlay protocol that initiates and terminates tunnels at the edge of the multi-tenant network, typically the hypervisor vSwitch or top of rack. These edge points are the VXLAN tunnel end points (VTEP).

Cumulus Linux can start and stop VTEPs in hardware and supports wire-rate VXLAN. VXLAN provides an efficient hashing scheme across the IP fabric during the encapsulation process; the source UDP port is unique, with the hash based on layer 2 through layer 4 information from the original frame. The UDP destination port is the standard port 4789.

{{%notice note%}}
Cumulus Linux does not support VXLAN encapsulation over layer 3 subinterfaces (for example, swp3.111) or SVIs as traffic transiting through the switch drops, even if you use the subinterface only for underlay traffic and it does not perform VXLAN encapsulation. Only configure VXLAN uplinks as layer 3 interfaces without any subinterfaces (for example, swp3).
The VXLAN tunnel endpoints cannot share a common subnet; there must be at least one layer 3 hop between the VXLAN source and destination.

{{%/notice%}}

## Considerations
<!-- vale off -->
### Cut-through Mode and Store and Forward Switching
<!-- vale on -->
On switches with the NVIDIA Spectrum ASICs, Cumulus Linux supports cut-through mode for VXLANs but does **not** support store and forward switching.

### MTU Size for Virtual Network Interfaces

The maximum transmission unit (MTU) size for a virtual network interface should be 50 bytes smaller than the MTU for the physical interfaces on the switch. For more information on setting MTU, read {{<link url="Switch-Port-Attributes#mtu" text="Layer 1 and Switch Port Attributes">}}.

### Layer 3 and Layer 2 VNIs Cannot Share the Same ID

A layer 3 VNI and a layer 2 VNI cannot have the same ID. If the VNI IDs are the same, the layer 2 VNI does not get created.

## Related Information

- {{<exlink url="https://tools.ietf.org/html/rfc7348" text="VXLAN - RFC 7348">}}
