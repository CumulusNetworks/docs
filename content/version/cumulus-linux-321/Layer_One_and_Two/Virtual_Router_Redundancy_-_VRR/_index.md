---
title: Virtual Router Redundancy - VRR
author: Cumulus Networks
weight: 115
aliases:
 - /display/CL321/Virtual+Router+Redundancy+-+VRR
 - /pages/viewpage.action?pageId=5126868
pageID: 5126868
product: Cumulus Linux
version: 3.2.1
imgData: cumulus-linux-321
siteSlug: cumulus-linux-321
---
Virtual Router Redundancy (VRR) enables hosts to communicate with any
redundant router without reconfiguration, running dynamic router
protocols, or running router redundancy protocols. This means that
redundant routers will respond to Address Resolution Protocol (ARP)
requests from hosts. Routers are configured to respond in an identical
manner, but if one fails, the other redundant routers will continue to
respond, leaving the hosts with the impression that nothing has changed.

The diagram below illustrates a basic VRR-enabled network configuration.
The network includes several hosts, and two routers running Cumulus
Linux configured with [Multi-chassis Link
Aggregation](/version/cumulus-linux-321/Layer_One_and_Two/Multi-Chassis_Link_Aggregation_-_MLAG)
(MLAG):

{{% imgOld 0 %}}

{{%notice note%}}

A production implementation will have many more server hosts and network
connections than are shown here. However, this basic configuration
provides a complete description of the important aspects of the VRR
setup.

{{%/notice%}}

As the bridges in each of the redundant routers are connected, they will
each receive and reply to ARP requests for the virtual router IP
address.

{{%notice note%}}

**Multiple ARP Replies**

Each ARP request made by a host will receive replies from each router;
these replies will be identical, and so the host receiving the replies
will either ignore replies after the first, or accept them and overwrite
the previous identical reply, rather than being confused over which
response is correct.

{{%/notice%}}

{{%notice info%}}

**Reserved MAC Address Range**

A range of MAC addresses is reserved for use with VRR, in order to
prevent MAC address conflicts with other interfaces in the same bridged
network. The reserved range is `00:00:5E:00:01:00` to
`00:00:5E:00:01:ff`.

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info%}}

Cumulus Networks recommends using MAC addresses from the reserved range
when configuring VRR.

{{%/notice%}}

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info%}}

The reserved MAC address range for VRR is the same as for the Virtual
Router Redundancy Protocol (VRRP), as they serve similar purposes.

{{%/notice%}}

{{%/notice%}}

## <span>Configuring a VRR-enabled Network</span>

### <span>Configuring the Routers</span>

The routers implement the layer 2 network interconnecting the hosts and
the redundant routers. To configure the routers, add a bridge with the
following interfaces to each router:

  - One bond interface or switch port interface to each host.
    
    {{%notice note%}}
    
    For networks using MLAG, use bond interfaces. Otherwise, use switch
    port interfaces.
    
    {{%/notice%}}

  - One or more interfaces to each peer router.
    
    {{%notice note%}}
    
    Multiple inter-peer links are typically bonded interfaces, in order
    to accomodate higher bandwidth between the routers, and to offer
    link redundancy.
    
    {{%/notice%}}

{{%notice info has%}}

**Example VLAN-aware Bridge Configuration**

The example NCLU commands below create a VLAN-aware bridge interface for
a VRR-enabled network:

    cumulus@switch:~$ net add bridge
    cumulus@switch:~$ net add vlan 500 ip address 192.168.0.252/24
    cumulus@switch:~$ net add vlan 500 ip address-virtual 00:00:5e:00:01:01 192.168.0.254/24
    cumulus@switch:~$ net add vlan 500 ipv6 address 2001:aa::1/48
    cumulus@switch:~$ net add vlan 500 ipv6 address-virtual 00:00:5e:00:01:01 2001:aa::1/48
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The NCLU commands above produce the following `/etc/network/interfaces`
snippet:

    auto bridge
    iface bridge
        bridge-vids 500
        bridge-vlan-aware yes
     
    auto vlan500
    iface vlan500
        address 192.168.0.252/24
        address 2001:aa::1/48
        address-virtual 00:00:5e:00:01:01 2001:aa::1/48 192.168.0.254/24
        vlan-id 500
        vlan-raw-device bridge

{{%/notice%}}

### <span>Configuring the Hosts</span>

Each host should have two network interfaces. The routers configure the
interfaces as bonds running LACP; the hosts should also configure its
two interfaces using teaming, port aggregation, port group, or
EtherChannel running LACP. Configure the hosts, either statically or via
DHCP, with a gateway address that is the IP address of the virtual
router; this default gateway address never changes.

Configure the links between the hosts and the routers in *active-active*
mode for First Hop Redundancy Protocol.
