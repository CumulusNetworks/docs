---
title: Routing
author: Cumulus Networks
weight: 19
aliases:
 - /display/RMP31/Routing
 - /pages/viewpage.action?pageId=5122800
pageID: 5122800
product: Cumulus RMP
version: 3.1.2
imgData: cumulus-rmp-312
siteSlug: cumulus-rmp-312
---
This chapter discusses routing on switches running Cumulus RMP.

## <span>Commands</span>

  - ip route

## <span>Static Routing via ip route</span>

A static route can be persistently added by adding `up ip route add ..`
into `/etc/network/interfaces`. For example:

    cumulus@switch:~$ cat /etc/network/interfaces
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).
     
    # The loopback network interface
    auto lo
    iface lo inet loopback
     
    auto swp3
    iface swp3
        address 198.51.100.1/24
        up ip route add 203.0.113.0/24 via 198.51.100.2

{{%notice note%}}

Notice the simpler configuration of swp3 due to `ifupdown2`. For more
information, see [Configuring and Managing Network
Interfaces](/version/cumulus-rmp-312/Configuring_and_Managing_Network_Interfaces/).

{{%/notice%}}

The `ip route` command allows manipulating the kernel routing table
directly from the Linux shell. See `man ip(8)` for details.

To display the routing table:

    cumulus@switch:~$ ip route show
    default via 10.0.1.2 dev eth0
    10.0.1.0/24 dev eth0  proto kernel  scope link  src 10.0.1.52
    192.0.2.0/24 dev swp1  proto kernel  scope link  src 192.0.2.12
    192.0.2.10/24 via 192.0.2.1 dev swp1  proto zebra  metric 20
    192.0.2.20/24  proto zebra  metric 20
         nexthop via 192.0.2.1  dev swp1 weight 1
         nexthop via 192.0.2.2  dev swp2 weight 1
    192.0.2.30/24 via 192.0.2.1 dev swp1  proto zebra  metric 20
    192.0.2.40/24 dev swp2  proto kernel  scope link  src 192.0.2.42
    192.0.2.50/24 via 192.0.2.2 dev swp2  proto zebra  metric 20
    192.0.2.60/24 via 192.0.2.2 dev swp2  proto zebra  metric 20
    192.0.2.70/24  proto zebra  metric 30
         nexthop via 192.0.2.1  dev swp1 weight 1
         nexthop via 192.0.2.2  dev swp2 weight 1
    198.51.100.0/24 dev swp3  proto kernel  scope link  src 198.51.100.1
    198.51.100.10/24 dev swp4  proto kernel  scope link  src 198.51.100.11
    198.51.100.20/24 dev br0  proto kernel  scope link  src 198.51.100.21

Runtime configuration (Advanced)

{{%notice warning%}}

A runtime configuration does not persist across reboots of the switch.

{{%/notice%}}

To add a static route:

    cumulus@switch:~$ sudo ip route add 203.0.113.0/24 via 198.51.100.2
    cumulus@switch:~$ ip route
    default via 10.0.1.2 dev eth0
    10.0.1.0/24 dev eth0  proto kernel  scope link  src 10.0.1.52
    192.0.2.0/24 dev swp1  proto kernel  scope link  src 192.0.2.12
    192.0.2.10/24 via 192.0.2.1 dev swp1  proto zebra  metric 20
    192.0.2.20/24  proto zebra  metric 20
         nexthop via 192.0.2.1  dev swp1 weight 1
         nexthop via 192.0.2.2  dev swp2 weight 1
    192.0.2.30/24 via 192.0.2.1 dev swp1  proto zebra  metric 20
    192.0.2.40/24 dev swp2  proto kernel  scope link  src 192.0.2.42
    192.0.2.50/24 via 192.0.2.2 dev swp2  proto zebra  metric 20
    192.0.2.60/24 via 192.0.2.2 dev swp2  proto zebra  metric 20
    192.0.2.70/24  proto zebra  metric 30
         nexthop via 192.0.2.1  dev swp1 weight 1
         nexthop via 192.0.2.2  dev swp2 weight 1
    198.51.100.0/24 dev swp3  proto kernel  scope link  src 198.51.100.1
    198.51.100.10/24 dev swp4  proto kernel  scope link  src 198.51.100.11
    198.51.100.20/24 dev br0  proto kernel  scope link  src 198.51.100.21
    203.0.113.0/24 via 198.51.100.2 dev swp3

To delete a static route:

    cumulus@switch:~$ sudo ip route del 203.0.113.0/24
    cumulus@switch:~$ ip route
    default via 10.0.1.2 dev eth0
    10.0.1.0/24 dev eth0  proto kernel  scope link  src 10.0.1.52
    192.0.2.0/24 dev swp1  proto kernel  scope link  src 192.0.2.12
    192.0.2.10/24 via 192.0.2.1 dev swp1  proto zebra  metric 20
    192.0.2.20/24  proto zebra  metric 20
         nexthop via 192.0.2.1  dev swp1 weight 1
         nexthop via 192.0.2.2  dev swp2 weight 1
    192.0.2.30/24 via 192.0.2.1 dev swp1  proto zebra  metric 20
    192.0.2.40/24 dev swp2  proto kernel  scope link  src 192.0.2.42
    192.0.2.50/24 via 192.0.2.2 dev swp2  proto zebra  metric 20
    192.0.2.60/24 via 192.0.2.2 dev swp2  proto zebra  metric 20
    192.0.2.70/24  proto zebra  metric 30
         nexthop via 192.0.2.1  dev swp1 weight 1
         nexthop via 192.0.2.2  dev swp2 weight 1
    198.51.100.0/24 dev swp3  proto kernel  scope link  src 198.51.100.1
    198.51.100.10/24 dev swp4  proto kernel  scope link  src 198.51.100.11
    198.51.100.20/24 dev br0  proto kernel  scope link  src 198.51.100.21

Configuration Files

  - /etc/network/interfaces

## <span>Useful Links</span>

  - [linux-ip.net/html/tools-ip-route.html](http://linux-ip.net/html/tools-ip-route.html)

  - [www.nongnu.org/quagga/docs/docs-info.html\#Static-Route-Commands](http://www.nongnu.org/quagga/docs/docs-info.html#Static-Route-Commands)
