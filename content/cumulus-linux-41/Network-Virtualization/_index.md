---
title: Network Virtualization
author: NVIDIA
weight: 520
toc: 2
---
*VXLAN* (Virtual Extensible LAN) is a standard overlay protocol that abstracts logical virtual networks from the physical network underneath. You can deploy simple and scalable layer 3 Clos architectures while extending layer 2 segments over that layer 3 network.

VXLAN uses a VLAN-like encapsulation technique to encapsulate MAC-based layer 2 Ethernet frames within layer 3 UDP packets. Each virtual network is a VXLAN logical layer 2 segment. VXLAN scales to 16 million segments - a 24-bit VXLAN network identifier (VNI ID) in the VXLAN header - for multi-tenancy.

Hosts on a given virtual network are joined together through an overlay protocol that initiates and terminates tunnels at the edge of the multi-tenant network, typically the hypervisor vSwitch or top of rack. These edge points are the VXLAN tunnel end points (VTEP).

Cumulus Linux can initiate and terminate VTEPs in hardware and supports wire-rate VXLAN. VXLAN provides an efficient hashing scheme across the IP fabric during the encapsulation process; the source UDP port is unique, with the hash based on layer 2 through layer 4 information from the original frame. The UDP destination port is the standard port 4789.

VXLAN is supported only on switches in the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Cumulus Linux HCL">}} using the Broadcom Tomahawk, Trident II, Trident II+ and Trident3 chipsets, as well as the Mellanox Spectrum chipset.

{{%notice note%}}

VXLAN encapsulation over layer 3 subinterfaces (for example, swp3.111) or SVIs is not supported as traffic transiting through the switch may get dropped; even if the subinterface is used only for underlay traffic and does not perform VXLAN encapsulation, traffic may still get dropped. Only configure VXLAN uplinks as layer 3 interfaces without any subinterfaces (for example, swp3).

The VXLAN tunnel endpoints cannot share a common subnet; there must be at least one layer 3 hop between the VXLAN source and destination.

{{%/notice%}}

## Caveats and Errata

### Cut-through Mode and Store and Forward Switching

On switches using Broadcom Tomahawk, Trident II, Trident II+, and Trident3 ASICs, Cumulus Linux supports store and forward switching for VXLANs but does **not** support {{<link url="Buffer-and-Queue-Management#cut-through-mode-and-store-and-forward-switching" text="cut-through mode">}}.

On switches using Mellanox Spectrum ASICs, Cumulus Linux supports cut-through mode for VXLANs but does **not** support store and forward switching.

### MTU Size for Virtual Network Interfaces

The maximum transmission unit (MTU) size for a virtual network interface should be 50 bytes smaller than the MTU for the physical interfaces on the switch. For more information on setting MTU, read {{<link url="Switch-Port-Attributes#mtu" text="Layer 1 and Switch Port Attributes">}}.

### Layer 3 and Layer 2 VNIs Cannot Share the Same ID

A layer 3 VNI and a layer 2 VNI cannot have the same ID. If the VNI IDs are the same, the layer 2 VNI does not get created.

### TC Filters

NVIDIA recommends you run TC filter commands on each VLAN interface on the VTEP to install rules to protect the UDP port that Cumulus Linux uses for VXLAN encapsulation against VXLAN hopping vulnerabilities. If you have VRR configured on the VLAN, add a similar rule for the VRR device.

The following example installs an IPv4 and an IPv6 filter on vlan10 to protect the default port 4879:

```
cumulus@switch:mgmt:~$ tc filter add dev vlan10 prio 1 protocol ip ingress flower ip_proto udp dst_port 4879 action drop
cumulus@switch:mgmt:~$ tc filter add dev vlan10 prio 2 protocol ipv6 ingress flower ip_proto udp dst_port 4879 action drop
```

The following example installs an IPv4 and an IPv6 filter on VRR device vlan10-v0 to protect port 4879:

```
cumulus@switch:mgmt:~$ tc filter add dev vlan10-v0 prio 1 protocol ip ingress flower ip_proto udp dst_port 4879 action drop
cumulus@switch:mgmt:~$ tc filter add dev vlan10-v0 prio 2 protocol ipv6 ingress flower ip_proto udp dst_port 4879 action drop
```

## Useful Links

- {{<exlink url="https://tools.ietf.org/html/rfc7348" text="VXLAN - RFC 7348">}}
- {{<exlink url="http://openvswitch.org/support/dist-docs/ovsdb-server.1.html" text="ovsdb-server">}}
