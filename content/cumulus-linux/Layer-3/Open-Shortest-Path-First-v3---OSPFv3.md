---
title: Open Shortest Path First v3 - OSPFv3
author: Cumulus Networks
weight: 1837
aliases:
 - /display/CL3740/Open-Shortest-Path-First-v3---OSPFv3
 - /pages/viewpage.action?pageId=83629246648
pageID: 83629246648
product: Cumulus Linux
version: 3.7.7'4.0'
imgData: cumulus-linux-37740
siteSlug: cumulus-linux-37740
---
<details>

OSPFv3 is a revised version of OSPFv2 toand supports the IPv6 address
family. Refer to [Open Shortest Path First (OSPF)
Protocol](/version/cumulus-linux-37740/Layer-3/Open-Shortest-Path-First---OSPF)
for a discussion on the basic concepts, which remain the same between
the two versions.

OSPFv3 has changed the formatting in some of the packets and LSAs either
as a necessity to to
support IPv6 orand to improve the protocol behavior based
on OSPFv2 experience. Most notably, . OSPFv3 defines a new 
LSA, called
 intra-area prefix LSA, to separate out the advertisement of stub 
networks
 attached to a router from the router LSA. It is a clear 
separation of
 node topology from prefix reachability and lends itself 
well to an
 optimized SPF computation.

{{%notice note%}}

IETF has defined extensions to OSPFv3 to support multiple address
families (that is, both IPv6 and IPv4).
[FRR](/version/cumulus-linux-37740/Layer-3/FRRouting-Overview/) does not
support it yetcurrently support multiple address families.

{{%/notice%}}

## <span>Configure OSPFv3</span>

CTo configuringe OSPFv3 involves the following tasks:, you need to specify the router ID and map
interfaces to areas. The following commands provide examples.

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add ospf6 router-id 0.0.0.1
    cumulus@switch:~$ net add ospf6 interface swp1 area 0.0.0.0
    cumulus@switch:~$ net add ospf6 interface swp2 area 0.0.0.1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

1.  Enablinge the `zebra` and `ospf6` daemons, as described then start the FRRouting
    service. See [Configuring
    FRRouting](/version/cumulus-linux-37740/Layer-3/Configuring-FRRouting/)
    then start the FRRouting service:
    
        cumulus@switch:~$ sudo systemctl enable frr.service
        cumulus@switch:~$ sudo systemctl start frr.service

2.  Enabling OSPFv3 and map interfaces to areas:
    
        cumulus@switch:~$ net add ospf6 router-id 0.0.0.1
        cumulus@switch:~$ net add ospf6 interface swp1 area 0.0.0.0
        cumulus@switch:~$ net add ospf6.

2.  From the vtysh shell, configure OSPFv3:

<!-- end list -->

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf6
    switch(config-ospf6)# router-id 0.0.0.1
    switch(config-ospf6)# interface swp1 area 0.0.0.0
    switch(config-ospf6)# interface swp2 area 0.0.0.1
    switch(config-ospf6)#exit
    switch(config)#exit
    switch# write memory
    switch# exit
    cumulus@switch:~$

The NCLU and `vtysh` commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    router ospf6
     ospf6 router-id 0.0.0.1
     interface swp1 area 0.0.0.0
     interface swp2 area 0.0.0.1

3.  Defining (c    ...

### <span>Define Custom) OSPFv3 pParameters on the interfaces, such as:
    
    1.  N</span>

You can define additional custom parameters for OSPFv3, such as such as
the network type (such as point-to-point, or broadcast)
    
    2.  Timer tuning (for example, hello interval)
    
    <!-- end list -->
    
     and the interval between
hello packets that OSPF sends.

The following command example sets the network type to point-to-point
and the hello interval to 5 seconds. The hello interval can be any value
between 1 and 65535 seconds.

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add interface swp1 ospf6 network point-to-point
        cumulus@switch:~$ net add interface swp1 ospf6 hello-interval 5
    
    The OSPFv3 configuration is saved in `/etc/frr/frr.conf`cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# interface swp1
    switch(config-if)# ipv6 ospf6 network point-to-point
    switch(config-if)# ipv6 ospf6 hello-interval 5
    switch(config-if)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

The NCLU and `vtysh` commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    interface swp1
     ipv6 ospf6 hello-interval 5
     ipv6 ospf6 network point-to-point
    ...

{{%notice note%}}

Unlike OSPFv2, OSPFv3 intrinsically supports unnumbered interfaces.
Forwarding to the next hop router is done entirely using IPv6 link local
addresses. Therefore, you are not requirYou do not need to configure any global IPv6
 address to 
interfaces between routers.

{{%/notice%}}

## <span>Configure the OSPFv3 Area</span>

DYou can use different areas can be used to control routing. You can:

  - Limit an OSPFv3 area from reaching another area.

  - Manage the size of the routing table by creating a summary route for
    all the routes in a particular address range.

The following section provides command examples.

<summary>NCLU Commands </summary>

The following example command removes the `3:3::/64` route from the
routing table. Without a route in the table, any destinations in that
network are not reachable.

    cumulus@switch:~$ net add ospf6 area 0.0.0.0 range 3:3::/64 not-advertise 
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The following example command creates a summary route for all the routes
in the range 2001::/64:

    cumulus@switch:~$ net add ospf6 area 0.0.0.0 range 2001::/64 advertise
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

You can also configure the cost for a summary route, which is used to
determine the shortest paths to the destination. For example:

    cumulus@switch:~$ net add ospf6 area 0.0.0.0 range 11.1.1.1/24 cost 160

The value for cost must
be between 0 and 16777215.

    cumulus@switch:~$ net add ospf6 area 0.0.0.0 range 2001::/64 cost 160
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

The following example command removes the `3:3::/64` route from the
routing table. Without a route in the table, any destinations in that
network are not reachable.

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf6
    switch(config-ospf6)# area 0.0.0.0 range 3:3::/64 not-advertise
    switch(config-ospf6)# end
    switch# write memory
    switch# exit
    cumulus@switch:~

The following example command creates a summary route for all the routes
in the range 2001::/64:

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf6
    switch(config-ospf6)# area 0.0.0.0 range 2001::/64 advertise
    switch(config-ospf6)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

You can also configure the cost for a summary route, which is used to
determine the shortest paths to the destination. The value for cost must 
be between 0 and 16777215.

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf6
    switch(config-ospf6)# area 0.0.0.0 range 2001::/64 cost 160
    switch(config-ospf6)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

<span style="color: #36424a;"> </span> The NCLU and `vtysh` commands
save the configuration in the `/etc/frr/frr.conf` file. For example:

    ...
    router ospf6
     area 0.0.0.0 range 3:3::/64 not-advertise
     area 0.0.0.0 range 2001::/64 advertise
     area 0.0.0.0 range 2001::/64 cost 160
    ...

## <span>Configure the OSPFv3 Distance</span>

Cumulus Linux provides several commands to change the administrative
distance for OSPF routes.

<summary>NCLU Commands </summary>

This example command sets the distance for an entire group of routes,
rather than a specific route.

    cumulus@switch:~$ net add ospf6 distance 254
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This example command changes the OSPF administrative distance to 150 for
internal routes and 220 for external routes:

    cumulus@switch:~$ net add ospf6 distance ospf6 intra-area 150 inter-area 150 external 220
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This example command changes the OSPF administrative distance to 150 for
internal routes:

    cumulus@switch:~$ net add ospf6 distance ospf6 intra-area 150 inter-area 150
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This example command changes the OSPF administrative distance to 220 for
external routes:

    cumulus@switch:~$ net add ospf6 distance ospf6 external 220
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This example command changes the OSPF administrative distance to 150 for
internal routes to a subnet or network inside the same area as the
router:

    cumulus@switch:~$ net add ospf6 distance ospf6 intra-area 150
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This example command changes the OSPF administrative distance to 150 for
internal routes to a subnet in an area of which the router is *not* a
part:

    cumulus@switch:~$ net add ospf6 distance ospf6 inter-area 150
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

This example command sets the distance for an entire group of routes,
rather than a specific route.

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf6
    switch(config-ospf6)# distance 254
    switch(config-ospf6)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

This example command changes the OSPF administrative distance to 150 for
internal routes and 220 for external routes:

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf6
    switch(config-ospf6)# distance ospf6 intra-area 150 inter-area 150 external 220
    switch(config-ospf6)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

This example command changes the OSPF administrative distance to 150 for
internal routes to a subnet or network inside the same area as the
router:

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf6
    switch(config-ospf6)# distance ospf6 intra-area 150
    switch(config-ospf6)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

This example command changes the OSPF administrative distance to 150 for
internal routes to a subnet in an area of which the router is *not* a
part:

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf6
    switch(config-ospf6)# distance ospf6 inter-area 150
    switch(config-ospf6)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

The NCLU and `vtysh` commands save the configuration to the
`/etc/frr/frr.conf` file. For example:

    ...
    router ospf6
     distance ospf6 intra-area 150 inter-area 150 external 220
    ...

## <span>Configure OSPFv3 Interfaces</span>

You can configure an interface, a bond interface, or a VLAN with an
advertise prefix list.  

<summary>NCLU Commands </summary>

The following example command configures interface swp3s1 with the IPv6
OSPF6 advertise prefix-list 192.168.0.0/24:

    cumulus@switch:~$ net add interface swp3s1 ospf6 advertise prefix-list 192.168.0.0/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

You can also configure the cost for a particular interface, bond
interface, or VLAN.  
The following example command configures the cost 
for the bond interface
swp2.

    cumulus@switch:~$ net add bondinterface swp2 ospf6 cost 1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

## <span>Troubleshooting</span>

See [Debugging
OSPF](Open-Shortest-Path-First---OSPF.html#src-8362922_OpenShortestPathFirst-OSPF-ospf_debug)
for OSPFv2 for the troubleshooting discussion. The equivalent commands
are:

    cumulus@switch:~$ net show ospf6 neighbor [detail|drchoice]
    cumulus@switch:~$ net show ospf6 database [adv-router|detail|dump|internal|linkstate-id|self-originated]
    cumulus@switch:~$ net show route ospf6

Another helpful command is<summary>vtysh Commands </summary>

The following example command configures interface swp3s1 with the IPv6
advertise prefix-list 192.168.0.0/24:

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# interface swp3s1
    switch(config-if)# ipv6 ospf advertise prefix-list 192.168.0.0/24
    switch(config-if)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

You can also configure the cost for a particular interface, bond
interface, or VLAN. The following example command configures the cost
for swp2.

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# interface swp2
    switch(config-if)# ipv6 ospf cost 1
    switch(config-if)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

The NCLU and `vtysh` commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    interface swp2
     ipv6 ospf6 cost 1
    ...

## <span>Troubleshooting</span>

Cumulus Linux provides troubleshooting commands for OSPFv3:

  - To show neighbor states, run the NCLU `net show ospf6 neighbor`
    command or the vtysh `show ip ospf6 neighbor` command.

  - To verify that the LSDB is synchronized across all routers in the
    network, run the NCLU `net show ospf6 database` command or the vtysh
    `show ip ospf6 database` command.

  - To determine why an OSPF route is not being forwarded correctly, run
    the NCLU `net show route ospf6` command or the vtysh `show ip route
    ospf6` command. These commands show the outcome of the SPF
    computation downloaded to the forwarding table.

  - To help visualize the network view, run the NCLU ` net show ospf6
    spf tree`. It dumps  `command or the ` show ip ospf6 spf tree  `command. These
    commands show the node
 topology as computed by SPF to help visualize.

For example:

    cumulus@switch:~$ net show ospf6 neighbor
    Neighbor ID     Pri    DeadTime    State/IfState         Duration I/F[State]
    10.0.0.21         1    00:00:37     Full/DROther         00:11:32 swp51[PointToPoint]
    10.0.0.22         1    00:00:37     Full/DROther         00:11:32 swp52[PointToPoint] 

Run the `network view show ospf6 help` command to show available NCLU command
options.

For a list of all the OSPF debug options, refer to
[Debugging-OSPF](http://docs.frrouting.org/en/latest/ospfd.html#id7).

## <span>Related Information</span>

  - [Bidirectional forwarding
    detection](/version/cumulus-linux-37740/Layer-3/Bidirectional-Forwarding-Detection---BFD)
    (BFD) and OSPF

  - [en.wikipedia.org/wiki/Open\_Shortest\_Path\_First](http://en.wikipedia.org/wiki/Open_Shortest_Path_First)

  - [FRR OSPFv3](https://frrouting.org/user-guide/ospf6d.html)

  - [RFC 2740 OSPFv3 OSPF for IPv6](https://tools.ietf.org/html/rfc2740)

  - [Auto-cost reference
    bandwidth](Open-Shortest-Path-First---OSPF.html#src-83629226646_OpenShortestPathFirst-OSPF-acrb)
    (OSPFv2 chapter)

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

</details>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMzI3Mjk2MjddfQ==
-->