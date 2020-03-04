---
title: Open Shortest Path First v3 - OSPFv3 - Protocol
author: Cumulus Networks
weight: 175
aliases:
 - /display/CL35/Open+Shortest+Path+First+v3+++OSPFv3+++Protocol
 - /display/CL35/Open+Shortest+Path+First+v3+-+OSPFv3+-+Protocol
 - /display/CL35/Open+Shortest+Path+First+v3+OSPFv3+Protocol
 - /pages/viewpage.action?pageId=8357720
pageID: 8357720
---
OSPFv3 is a revised version of OSPFv2 to support the IPv6 address
family. Refer to 
[Open Shortest Path First (OSPF) Protocol](/cumulus-linux-35/Layer-3/Open-Shortest-Path-First-OSPF-Protocol)
for a discussion on the basic concepts, which remain the same between
the two versions.

OSPFv3 has changed the formatting in some of the packets and LSAs either
as a necessity to support IPv6 or to improve the protocol behavior based
on OSPFv2 experience. Most notably, v3 defines a new LSA, called
intra-area prefix LSA to separate out the advertisement of stub networks
attached to a router from the router LSA. It is a clear separation of
node topology from prefix reachability and lends itself well to an
optimized SPF computation.

{{%notice note%}}

IETF has defined extensions to OSPFv3 to support multiple address
families (that is, both IPv6 and IPv4).
[frr](/cumulus-linux-35/Layer-3/FRRouting-Overview/) does not
support it yet.

{{%/notice%}}

## Configuring OSPFv3

Configuring OSPFv3 involves the following tasks:

1.  Enabling the `zebra` and `ospf6` daemons, as described in
    [Configuring
    FRRouting](/cumulus-linux-35/Layer-3/Configuring-FRRouting/)
    then start the FRRouting service:
    
        cumulus@switch:~$ sudo systemctl enable frr.service
        cumulus@switch:~$ sudo systemctl start frr.service

2.  Enabling OSPF6 and map interfaces to areas:
    
        cumulus@switch:~$ net add ospf6 router-id 0.0.0.1
        cumulus@switch:~$ net add ospf6 interface swp1 area 0.0.0.0
        cumulus@switch:~$ net add ospf6 interface swp2 area 0.0.0.1

3.  Defining (custom) OSPF6 parameters on the interfaces, such as:
    
    1.  Network type (such as point-to-point, broadcast)
    
    2.  Timer tuning (for example, hello interval)
    
        cumulus@switch:~$ net add interface swp1 ospf6 network point-to-point
        cumulus@switch:~$ net add interface swp1 ospf6 hello-interval 5

The OSPFv3 configuration is saved in `/etc/frr/ospf6d.conf`.

## Unnumbered Interfaces

Unlike OSPFv2, OSPFv3 intrinsically supports unnumbered interfaces.
Forwarding to the next hop router is done entirely using IPv6 link local
addresses. Therefore, you are not required to configure any global IPv6
address to interfaces between routers.

## Debugging OSPF

See [Debugging OSPF](/cumulus-linux-35/Layer-3/Open-Shortest-Path-First-OSPF-Protocol/#debugging-ospf)
for OSPFv2 for the troubleshooting discussion. The equivalent commands
are:

    cumulus@switch:~$ net show ospf6 neighbor [detail|drchoice]
    cumulus@switch:~$ net show ospf6 database [adv-router|detail|dump|internal|linkstate-id|self-originated]
    cumulus@switch:~$ net show route ospf6

Another helpful command is `net show ospf6 spf tree`. It dumps the node
topology as computed by SPF to help visualize the network view.

## Related Information

  - [Bidirectional forwarding detection](/cumulus-linux-35/Layer-3/Bidirectional-Forwarding-Detection-BFD)
    (BFD) and OSPF
  - [en.wikipedia.org/wiki/Open\_Shortest\_Path\_First](http://en.wikipedia.org/wiki/Open_Shortest_Path_First)
  - [frrouting.org/user-guide/OSPFv3.html\#OSPFv3](https://frrouting.org/user-guide/OSPFv3.html#OSPFv3)

