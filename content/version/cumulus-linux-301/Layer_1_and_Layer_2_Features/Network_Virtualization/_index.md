---
title: Network Virtualization
author: Cumulus Networks
weight: 113
aliases:
 - /display/CL30/Network+Virtualization
 - /pages/viewpage.action?pageId=5118291
pageID: 5118291
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
Cumulus Linux supports these forms of [network
virtualization](http://en.wikipedia.org/wiki/Network_virtualization):

VXLAN (Virtual Extensible LAN), is a standard overlay protocol that
abstracts logical virtual networks from the physical network underneath.
You can deploy simple and scalable layer 3 Clos architectures while
extending layer 2 segments over that layer 3 network.

VXLAN uses a VLAN-like encapsulation technique to encapsulate MAC-based
layer 2 Ethernet frames within layer 3 UDP packets. Each virtual network
is a VXLAN logical L2 segment. VXLAN scales to 16 million segments – a
24-bit VXLAN network identifier (VNI ID) in the VXLAN header – for
multi-tenancy.

Hosts on a given virtual network are joined together through an overlay
protocol that initiates and terminates tunnels at the edge of the
multi-tenant network, typically the hypervisor vSwitch or top of rack.
These edge points are the VXLAN tunnel end points (VTEP).

Cumulus Linux can initiate and terminate VTEPs in hardware and supports
wire-rate VXLAN with Tomahawk, Trident II+ and Trident II platforms.
VXLAN provides an efficient hashing scheme across IP fabric during the
encapsulation process; the source UDP port is unique, with the hash
based on L2-L4 information from the original frame. The UDP destination
port is the standard port 4789.

Cumulus Linux includes the native Linux VXLAN kernel support and
integrates with controller-based overlay solutions like VMware NSX and
Midokura MidoNet.

VXLAN is supported only on switches in the [Cumulus Linux
HCL](http://cumulusnetworks.com/support/hcl/) using Tomahawk, Trident
II+ and Trident II chipsets.

{{%notice note%}}

VXLAN encapsulation over layer 3 subinterfaces is not supported.
Therefore, VXLAN uplinks should be only configured as layer 3 interfaces
without any subinterfaces.

Furthermore the VXLAN tunnel endpoints cannot share a common subnet;
there must be at least one layer 3 hop between the VXLAN source and
destination.

{{%/notice%}}

## <span>Commands</span>

  - brctl

  - bridge fdb

  - ip link

  - ovs-pki

  - ovsdb-client

  - vtep-ctl

## <span>Useful Links</span>

  - [VXLAN IETF
    draft](http://tools.ietf.org/html/draft-mahalingam-dutt-dcops-vxlan-06)

  - [ovsdb-server](http://openvswitch.org/support/dist-docs/ovsdb-server.1.html)
