---
title: Open Shortest Path First v3 - OSPFv3 - Protocol
author: Cumulus Networks
weight: 141
aliases:
 - /display/CL31/Open+Shortest+Path+First+v3+-+OSPFv3+-+Protocol
 - /pages/viewpage.action?pageId=5122128
pageID: 5122128
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
OSPFv3 is a revised version of OSPFv2 to support the IPv6 address
family. Refer to [Open Shortest Path First (OSPF)
Protocol](/version/cumulus-linux-312/Layer_3_Features/Open_Shortest_Path_First_-_OSPF_-_Protocol)
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
[Quagga](/version/cumulus-linux-312/Layer_3_Features/Quagga_Overview)
does not support it yet.

{{%/notice%}}

## <span>Configuring OSPFv3</span>

Configuring OSPFv3 involves the following tasks:

1.  Enabling the `zebra` and `ospf6` daemons, as described in
    [Configuring
    Quagga](/version/cumulus-linux-312/Layer_3_Features/Configuring_Quagga/)
    then start the Quagga service:
    
        cumulus@switch:~$ sudo systemctl enable quagga.service
        cumulus@switch:~$ sudo systemctl start quagga.service

2.  Enabling OSPF6 and map interfaces to areas. From Quagga's `vtysh`
    shell:
    
        cumulus@switch:~$ sudo vtysh
         
        Hello, this is Quagga (version 0.99.23.1+cl3.0).
        Copyright 1996-2005 Kunihiro Ishiguro, et al.
         
        switch# conf t
        switch# configure  terminal
        switch(config)# router ospf6
        switch(config-router)# router-id 0.0.1
        switch(config-router)# interface swp1 area 0.0.0.0
        switch(config-router)# interface swp2 area 0.0.0.1
        switch(config-router)#
    
    Or through `cl-ospf6`, from the Cumulus Linux shell:
    
        cumulus@switch:~$ sudo cl-ospf6 router set id 0.0.0.1
        cumulus@switch:~$ sudo cl-ospf6 interface swp1 set area 0.0.0.0
        cumulus@switch:~$ sudo cl-ospf6 interface swp2 set area 0.0.0.1

3.  Defining (custom) OSPF6 parameters on the interfaces:
    
    1.  Network type (such as point-to-point, broadcast)
    
    2.  Timer tuning (for example, hello interval)
    
    Using Quagga's `vtysh`:
    
        switch(config)# interface swp1
        switch(config-if)# ipv6 ospf6 network point-to-point
        switch(config-if)# ipv6 ospf6 hello-interval 5
    
    Or through `cl-ospf6`, from the Cumulus Linux shell:
    
        cumulus@switch:~$ sudo cl-ospf6 interface swp1 set network point-to-point
        cumulus@switch:~$ sudo cl-ospf6 interface swp1 set hello-interval 5

The OSPFv3 configuration is saved in `/etc/quagga/ospf6d.conf`.

## <span>Unnumbered Interfaces</span>

Unlike OSPFv2, OSPFv3 intrinsically supports unnumbered interfaces.
Forwarding to the next hop router is done entirely using IPv6 link local
addresses. Therefore, you are not required to configure any global IPv6
address to interfaces between routers.

## <span>Debugging OSPF</span>

See [Debugging
OSPF](Open_Shortest_Path_First_-_OSPF_-_Protocol.html#src-5122126_OpenShortestPathFirst-OSPF-Protocol-ospf_debug)
for OSPFv2 for the troubleshooting discussion. The equivalent commands
are:

    cumulus@switch:~$ sudo vtysh
    switch# show ipv6 ospf6 neighbor
    switch# show ipv6 ospf6 database [detail | dump | internal |
                                             as-external | group-membership |
                                             inter-prefix | inter-router |
                                             intra-prefix | link | network |
                                             router | type-7 | * | adv-router |
                                             linkstate-id | self-originated]
    switch# show ip ospf route

Another helpful command is `show ipv6 ospf6 [area <id>] spf tree`. It
dumps the node topology as computed by SPF to help visualize the network
view.

## <span>Configuration Files</span>

  - /etc/quagga/ospf6d.conf

## <span>Supported RFCs</span>

  - [RFC5340](http://tools.ietf.org/rfc/rfc5340)

  - [RFC3137](http://tools.ietf.org/rfc/rfc3137)

## <span>Useful Links</span>

  - [Bidirectional forwarding
    detection](/version/cumulus-linux-312/Layer_3_Features/Bidirectional_Forwarding_Detection_-_BFD)
    (BFD) and OSPF

  - [en.wikipedia.org/wiki/Open\_Shortest\_Path\_First](http://en.wikipedia.org/wiki/Open_Shortest_Path_First)

  - [www.nongnu.org/quagga/docs/docs-info.html\#OSPFv3](http://www.nongnu.org/quagga/docs/docs-info.html#OSPFv3)
