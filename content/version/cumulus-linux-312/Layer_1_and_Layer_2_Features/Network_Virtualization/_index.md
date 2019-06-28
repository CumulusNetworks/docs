---
title: Network Virtualization
author: Cumulus Networks
weight: 115
aliases:
 - /display/CL31/Network+Virtualization
 - /pages/viewpage.action?pageId=5122021
pageID: 5122021
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
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
integrates with controller-based overlay solutions like [VMware
NSX](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Network_Virtualization/Integrating_with_VMware_NSX)
and [Midokura
MidoNet](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Network_Virtualization/Integrating_Hardware_VTEPs_with_Midokura_MidoNet_and_OpenStack).

VXLAN is supported only on switches in the [Cumulus Linux
HCL](http://cumulusnetworks.com/support/hcl/) using Tomahawk, Trident
II+ and Trident II chipsets.

{{%notice note%}}

VXLAN encapsulation over layer 3 subinterfaces (for example, swp3.111)
is not supported. Therefore, VXLAN uplinks should be only configured as
layer 3 interfaces without any subinterfaces (for example, swp3).

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

## <span>Caveats/Errata</span>

### <span>Cut-through Mode</span>

Cut-through mode is disabled in Cumulus Linux by default. With
cut-though mode enabled and link pause is asserted, Cumulus Linux
generates a TOVR and TUFL ERROR; certain error counters increment on a
given physical port.

    cumulus@switch:~$ sudo ethtool -S swp49 | grep Error
    HwIfInDot3LengthErrors: 0
    HwIfInErrors: 0
    HwIfInDot3FrameErrors: 0
    SoftInErrors: 0
    SoftInFrameErrors: 0
    HwIfOutErrors: 35495749
    SoftOutErrors: 0
     
    cumulus@switch:~$ sudo ethtool -S swp50 | grep Error
    HwIfInDot3LengthErrors: 3038098
    HwIfInErrors: 297595762
    HwIfInDot3FrameErrors: 293710518

To work around this issue, disable link pause or disable cut-through in
`/etc/cumulus/datapath/traffic.conf`.

To disable link pause, comment out the link\_pause\* section in
`/etc/cumulus/datapath/traffic.conf`:

    cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf 
    #link_pause.port_group_list = [port_group_0]
    #link_pause.port_group_0.port_set = swp45-swp54
    #link_pause.port_group_0.rx_enable = true
    #link_pause.port_group_0.tx_enable = true

To enable store and forward switching, set cut\_through\_enable to false
in `/etc/cumulus/datapath/traffic.conf`:

    cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf 
    cut_through_enable = false

### <span>MTU Size for Virtual Network Interfaces</span>

The maximum transmission unit (MTU) size for a virtual network interface
should by 50 bytes smaller than the MTU for the physical interfaces on
the switch. For more information, read [Layer 1 and Switch Port
Attributes](Layer_1_and_Switch_Port_Attributes.html#src-5122107_Layer1andSwitchPortAttributes-mtu_vxlan).

## <span>Useful Links</span>

  - [VXLAN IETF
    draft](http://tools.ietf.org/html/draft-mahalingam-dutt-dcops-vxlan-06)

  - [ovsdb-server](http://openvswitch.org/support/dist-docs/ovsdb-server.1.html)
