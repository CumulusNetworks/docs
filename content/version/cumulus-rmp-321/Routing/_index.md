---
title: Routing
author: Cumulus Networks
weight: 19
aliases:
 - /display/RMP321/Routing
 - /pages/viewpage.action?pageId=5127623
pageID: 5127623
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
This chapter discusses routing on switches running Cumulus RMP.

## <span>Managing Static Routes</span>

You manage static routes using
[NCLU](/version/cumulus-rmp-321/System_Configuration/Network_Command_Line_Utility)
or the Cumulus Linux `ip route` command. The routes are added to
theLinux kernel routing table. To add a static route, run:

    cumulus@switch:~$ net add routing route 203.0.113.0/24 198.51.100.2
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/quagga/Quagga.conf` file:

    !
    ip route 203.0.113.0/24 198.51.100.2
    !

To delete a static route, run:

    cumulus@switch:~$ net del routing route 203.0.113.0/24 198.51.100.2
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

To view static routes, run:

    cumulus@switch:~$ net show route static 
    RIB entry for static
    ====================
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, P - PIM, T - Table,
           > - selected route, * - FIB route
    S>* 203.0.113.0/24 [1/0] via 198.51.100.2, swp3

### <span>Static Routing via ip route</span>

A static route can also be created by adding ` post-up ip route add
 `command to a switch port configuration. For example:

    cumulus@switch:~$ net add interface swp3 ip address 198.51.100.1/24 
    cumulus@switch:~$ net add interface swp3 post-up ip route add 203.0.113.0/24 via 198.51.100.2
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands produce the following configuration in the
`/etc/network/interfaces` file:

    auto swp3
    iface swp3
        address 198.51.100.1/24
        post-up ip route add 203.0.113.0/24 via 198.51.100.2

{{%notice note%}}

If an IPv6 address is assigned to a DOWN interface, the associated route
is still installed into the routing table. The type of IPv6 address
doesn't matter: link local, site local and global all exhibit the same
problem.

If the interface is bounced up and down, then the routes are no longer
in the route table.

{{%/notice%}}

The `ip route` command allows manipulating the kernel routing table
directly from the Linux shell. See `man ip(8)` for details. `quagga`
monitors the kernel routing table changes and updates its own routing
table accordingly.

To display the routing table:

    cumulus@switch:~$ ip route show
    default via 10.0.1.2 dev eth0
    10.0.1.0/24 dev eth0  proto kernel  scope link  src 10.0.1.52
    192.0.2.0/24 dev swp1  proto kernel  scope link  src 192.0.2.12
    192.0.2.10/24 via 192.0.2.1 dev swp1  proto zebra  metric 20
    192.0.2.20/24  proto zebra  metric 20
    192.0.2.30/24 via 192.0.2.1 dev swp1  proto zebra  metric 20
    192.0.2.40/24 dev swp2  proto kernel  scope link  src 192.0.2.42
    192.0.2.50/24 via 192.0.2.2 dev swp2  proto zebra  metric 20
    192.0.2.60/24 via 192.0.2.2 dev swp2  proto zebra  metric 20
    192.0.2.70/24  proto zebra  metric 30
    198.51.100.0/24 dev swp3  proto kernel  scope link  src 198.51.100.1
    198.51.100.10/24 dev swp4  proto kernel  scope link  src 198.51.100.11
    198.51.100.20/24 dev br0  proto kernel  scope link  src 198.51.100.21

### <span>Applying a Route Map for Route Updates</span>

To apply a [route
map](http://www.nongnu.org/quagga/docs/docs-multi/Route-Map.html#Route-Map)
to filter route updates from Zebra into the Linux kernel:

    cumulus@switch:$ net add ip protocol static route-map <route-map-name>

## <span>Caveats and Errata</span>

### <span>Adding IPv6 Default Route with src Address on eth0 Fails without Adding Delay</span>

Attempting to install an IPv6 default route on eth0 with a source
address fails at reboot or when running `ifup` on eth0.

The first execution of `ifup -dv` returns this warning and does not
install the route:

    cumulus@switch:~$ sudo ifup -dv eth0
    warning: eth0: post-up cmd '/sbin/ip route add default via 2001:620:5ca1:160::1 /
    src 2001:620:5ca1:160::45 dev eth0' failed (RTNETLINK answers: Invalid argument)<<<<<<<<<<

Running `ifup` a second time on eth0 successfully installs the route.

There are two ways you can work around this issue.

  - Add a sleep 2 to the eth0 interface in `/etc/network/interfaces`:
    
        cumulus@switch:~$ net add interface eth0 ipv6 address 2001:620:5ca1:160::45/64 post-up /bin/sleep 2s
        cumulus@switch:~$ net add interface eth0 post-up /sbin/ip route add default via 2001:620:5ca1:160::1 src 2001:620:5ca11:160::45 dev eth0

  - Exclude the `src` parameter to the `ip route add` that causes the
    need for the delay. If the `src` parameter is removed, the route is
    added correctly.
    
        cumulus@switch:~$ net add interface eth0 post-up /sbin/ip route add default via 2001:620:5ca1:160::1 dev eth0
    
        cumulus@switch:~$ ifdown eth0
        Stopping NTP server: ntpd.
        Starting NTP server: ntpd.
        cumulus@switch:~$ ip -6 r s
        cumulus@switch:~$ ifup eth0
        Stopping NTP server: ntpd.
        Starting NTP server: ntpd.
        cumulus@switch:~$ ip -6 r s
        2001:620:5ca1:160::/64 dev eth0  proto kernel  metric 256 
        fe80::/64 dev eth0  proto kernel  metric 256 
        default via 2001:620:5ca1:160::1 dev eth0  metric 1024 

## <span>Related Information</span>

  - [Linux IP - ip route
    command](http://linux-ip.net/html/tools-ip-route.html)

  - [Quagga docs - static route
    commands](http://www.nongnu.org/quagga/docs/docs-info.html#Static-Route-Commands)
