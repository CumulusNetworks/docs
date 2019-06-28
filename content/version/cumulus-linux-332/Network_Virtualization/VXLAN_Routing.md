---
title: VXLAN Routing
author: Cumulus Networks
weight: 149
aliases:
 - /display/CL332/VXLAN+Routing
 - /pages/viewpage.action?pageId=5869077
pageID: 5869077
product: Cumulus Linux
version: 3.3.2
imgData: cumulus-linux-332
siteSlug: cumulus-linux-332
---
VXLAN routing, sometimes referred to as inter-VXLAN routing, provides IP
routing between VXLAN VNIs in the overlay networks. The routing of
traffic is based on the inner header or the overlay tenant IP address.

Features in the early access release of VXLAN routing include:

  - Centralized and asymmetric routing

  - [VRF](/version/cumulus-linux-332/Layer_Three/Virtual_Routing_and_Forwarding_-_VRF)
    support for overlay networks

  - Anycast routing

{{%notice warning%}}

VXLAN routing is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus Linux. Before you can install the VXLAN routing packages, you
must enable the Early Access repository. For more information about the
Cumulus Linux repository, read [this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/217422127).

VXLAN routing works on Broadcom Trident II+ switches only.

Because it is an EA feature, it has these limitations:

  - Overlay ECMP

  - EVPN control plane to exchange topology and routes

  - Symmetric routing

{{%/notice%}}

## <span>Installing the VXLAN Routing Package</span>

To install the VXLAN routing package on a Cumulus Linux switch, [follow
these
steps](https://support.cumulusnetworks.com/hc/en-us/articles/202933878),
using *cumulus-vxlan-routing* as the `EA_PACKAGENAME` in step 3. This
article also has steps for removing the package.

## <span>Configuring VXLAN Routing</span>

1.  Configure VXLAN routing between two overlay subnets.:
    
        cumulus@switch:~$ net add vxlan VNI-11000 vxlan id 11000
        cumulus@switch:~$ net add vxlan VNI-11000 bridge access 1000
        cumulus@switch:~$ net add vxlan VNI-11000 vxlan local-tunnelip 27.0.0.15
        cumulus@switch:~$ net add vxlan VNI-11000 mtu 9152
        cumulus@switch:~$ net add vxlan VNI-11001 vxlan id 11001
        cumulus@switch:~$ net add vxlan VNI-11001 bridge access 1001
        cumulus@switch:~$ net add vxlan VNI-11001 vxlan local-tunnelip 27.0.0.15
        cumulus@switch:~$ net add vxlan VNI-11001 mtu 9152
        cumulus@switch:~$ net add bridge bridge ports VNI-11000 VNI-11001

2.  Create the SVIs on the bridge, which enable routing:
    
        cumulus@switch:~$ net add vlan 1000 ip address 45.0.0.16/26
        cumulus@switch:~$ net add vlan 1001 ip address 45.0.0.80/26

3.  If you are using
    [VRF](/version/cumulus-linux-332/Layer_Three/Virtual_Routing_and_Forwarding_-_VRF),
    create a VRF and enable it on the SVIs:
    
        cumulus@switch:~$ net add vrf vrf1001
        cumulus@switch:~$ net add vlan 1000 vrf vrf1001
        cumulus@switch:~$ net add vlan 1001 vrf vrf1001

4.  If you are using anycast routing, use VRR syntax for the SVIs:
    
        cumulus@switch:~$ net add vlan 1000 ip address-virtual 00:00:5e:00:01:01 45.0.0.17/26
        cumulus@switch:~$ net add vlan 1001 ip address-virtual 00:00:5e:00:01:01 45.0.0.87/26

5.  Review and commit your changes:
    
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto bridge
    iface bridge
        bridge-ports VNI-11000 VNI-11001
        bridge-vids 1000-1001
        bridge-vlan-aware yes
     
    auto vlan1000
    iface vlan1000
        address 45.0.0.16/26
        address-virtual 00:00:5e:00:01:01 45.0.0.17/26
        vlan-id 1000
        vlan-raw-device bridge
        vrf vrf1001
     
    auto vlan1001
    iface vlan1001
        address 45.0.0.80/26
        address-virtual 00:00:5e:00:01:01 45.0.0.87/26
        vlan-id 1001
        vlan-raw-device bridge
        vrf vrf1001
     
    auto vrf1001
    iface vrf1001
        vrf-table auto
     
    auto VNI-11000
    iface VNI-11000
        bridge-access 1000
        mstpctl-bpduguard  yes
        mstpctl-portbpdufilter yes
        mtu 9152
        vxlan-id 11000
        vxlan-local-tunnelip 27.0.0.15
     
    auto VNI-11001
    iface VNI-11001
        bridge-access 1001
        mstpctl-bpduguard  yes
        mstpctl-portbpdufilter yes
        mtu 9152
        vxlan-id 11001
        vxlan-local-tunnelip 27.0.0.15

## <span>Viewing VXLAN Routing Information</span>

You can use the following commands to display VXLAN routing-related
information:

  - ip link show dev \<DEVICE\>

  - ip route

  - ip neighbor

  - bridge fdb show

To get basic information about a VXLAN, use `ip link show`:

    cumulus@switch:~$ ip link show VNI-11000
    68: VNI-11000: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9152 state UP mode DEFAULT group default  
     link/ether 0a:09:cd:9d:f0:c7 brd ff:ff:ff:ff:ff:ff

To view the routing table, use `ip route`:

    cumulus@switch:~$ ip route
    45.0.0.0/26 dev vlan1000 proto kernel  scope link  src 45.0.0.16 
    45.0.0.64/26 dev vlan1001  proto kernel  scope link  src 45.0.0.80
     

To view the neighbor table, run `ip neighbor`:

    cumulus@switch:~$ ip neighbor 
    45.0.0.70 dev vlan1001 lladdr 00:02:00:00:00:0c STALE
    45.0.0.72 dev vlan1001 lladdr 00:02:00:00:00:10 REACHABLE
    45.0.0.5 dev vlan1000 lladdr 00:02:00:00:00:0a REACHABLE

To view the forwarding database, use `bridge fdb show`:

    cumulus@switch:~$ bridge fdb show
    ca:0b:56:be:a7:74 dev VNI-11000 master bridge permanent
    ba:08:bc:60:b2:15 dev VNI-11001 master bridge permanent
    00:00:5e:00:01:01 dev bridge vlan 1001 master bridge permanent
    00:00:5e:00:01:01 dev bridge vlan 1000 master bridge permanent
