---
title: Routing
author: Cumulus Networks
weight: 121
aliases:
 - /display/CL25ESR/Routing
 - /pages/viewpage.action?pageId=5116102
pageID: 5116102
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
This chapter discusses routing on switches running Cumulus Linux.

## <span>Commands</span>

  - ip route

## <span>Static Routing via ip route</span>

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

To add a static route (does not persist across reboots):

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

To delete a static route (does not persist across reboots):

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

### <span>Persistently Adding a Static Route</span>

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
information, see [Configuring Network Interfaces with
ifupdown](/version/cumulus-linux-2512-esr/Configuring_and_Managing_Network_Interfaces/)
.

{{%/notice%}}

## <span>Static Routing via quagga</span>

Static routes can also be managed via the `quagga` CLI. The routes are
added to the `quagga` routing table, and then will be updated into the
kernel routing table as well.

To add a static route (does not persist across reboot):

    cumulus@switch:~$ sudo vtysh
    
    Hello, this is Quagga (version 0.99.21).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.
    
    switch# conf t
    switch(config)# ip route 203.0.113.0/24 198.51.100.2
    switch(config)# end
    switch# show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, A - Babel,
           > - selected route, * - FIB route
    
    K>* 0.0.0.0/0 via 10.0.1.2, eth0
    C>* 10.0.1.0/24 is directly connected, eth0
    O   192.0.2.0/24 [110/10] is directly connected, swp1, 00:13:25
    C>* 192.0.2.0/24 is directly connected, swp1
    O>* 192.0.2.10/24 [110/20] via 192.0.2.1, swp1, 00:13:09
    O>* 192.0.2.20/24 [110/20] via 192.0.2.1, swp1, 00:13:09
      *                      via 192.0.2.41, swp2, 00:13:09
    O>* 192.0.2.30/24 [110/20] via 192.0.2.1, swp1, 00:13:09
    O   192.0.2.40/24 [110/10] is directly connected, swp2, 00:13:25
    C>* 192.0.2.40/24 is directly connected, swp2
    O>* 192.0.2.50/24 [110/20] via 192.0.2.41, swp2, 00:13:09
    O>* 192.0.2.60/24 [110/20] via 192.0.2.41, swp2, 00:13:09
    O>* 192.0.2.70/24 [110/30] via 192.0.2.1, swp1, 00:13:09
      *                      via 192.0.2.41, swp2, 00:13:09
    O   198.51.100.0/24 [110/10] is directly connected, swp3, 00:13:22
    C>* 198.51.100.0/24 is directly connected, swp3
    O   198.51.100.10/24 [110/10] is directly connected, swp4, 00:13:22
    C>* 198.51.100.10/24 is directly connected, swp4
    O   198.51.100.20/24 [110/10] is directly connected, br0, 00:13:22
    C>* 198.51.100.20/24 is directly connected, br0
    S>* 203.0.113.0/24 [1/0] via 198.51.100.2, swp3
    C>* 127.0.0.0/8 is directly connected, lo

To delete a static route (does not persist across reboot):

    cumulus@switch:~$ sudo vtysh
    
    Hello, this is Quagga (version 0.99.21).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.
    
    switch# conf t
    switch(config)# no ip route 203.0.113.0/24 198.51.100.2
    switch(config)# end
    switch# show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, A - Babel,
           > - selected route, * - FIB route
    
    K>* 0.0.0.0/0 via 10.0.1.2, eth0
    C>* 10.0.1.0/24 is directly connected, eth0
    O   192.0.2.0/24 [110/10] is directly connected, swp1, 00:13:55
    C>* 192.0.2.0/24 is directly connected, swp1
    O>* 192.0.2.10/24 [110/20] via 11.0.0.1, swp1, 00:13:39
    O>* 192.0.2.20/24 [110/20] via 11.0.0.1, swp1, 00:13:39
      *                      via 11.0.4.1, swp2, 00:13:39
    O>* 192.0.2.30/24 [110/20] via 11.0.0.1, swp1, 00:13:39
    O   192.0.2.40/24 [110/10] is directly connected, swp2, 00:13:55
    C>* 192.0.2.40/24 is directly connected, swp2
    O>* 192.0.2.50/24 [110/20] via 11.0.4.1, swp2, 00:13:39
    O>* 192.0.2.60/24 [110/20] via 11.0.4.1, swp2, 00:13:39
    O>* 192.0.2.70/24 [110/30] via 11.0.0.1, swp1, 00:13:39
      *                      via 11.0.4.1, swp2, 00:13:39
    O   198.51.100.0/24 [110/10] is directly connected, swp3, 00:13:52
    C>* 198.51.100.0/24 is directly connected, swp3
    O   198.51.100.10/24 [110/10] is directly connected, swp4, 00:13:52
    C>* 198.51.100.10/24 is directly connected, swp4
    O   198.51.100.20/24 [110/10] is directly connected, br0, 00:13:52
    C>* 198.51.100.20/24 is directly connected, br0
    C>* 127.0.0.0/8 is directly connected, lo
    switch#

### <span>Persistent Configuration</span>

From the quagga CLI, the running configuration can be saved so it
persists between reboots:

    switch# write mem
    Configuration saved to /etc/quagga/zebra.conf
    switch# end

## <span>Supported Route Table Entries</span>

Cumulus Linux supports different numbers of route entries, depending
upon your switch platform (Trident, Trident+, or Trident II; see the
[HCL](http://cumulusnetworks.com/support/hcl/)) and whether the routes
are IPv4 or IPv6.

In addition, switches on the Trident II platform are configured to
manage route table entries using Algorithm Longest Prefix Match (ALPM).
In ALPM mode, the hardware can store significantly more route entries.

Following are the number of route supported on Trident II switches with
ALPM:

  - 32K IPv4 routes

  - 16K IPv6 routes

  - 32K total routes (both IPv4 and IPv6)

Following are the number of route supported on Trident and Trident+
switches:

  - 16K IPv4 routes

  - 8K IPv6 routes

  - 16K total routes (both IPv4 and IPv6)

## <span>Configuration Files</span>

  - /etc/network/interfaces

  - /etc/quagga/zebra.conf

## <span>Useful Links</span>

  - <http://linux-ip.net/html/tools-ip-route.html>

  - <http://www.nongnu.org/quagga/docs/docs-info.html#Static-Route-Commands>

## <span>Caveats and Errata</span>

  - Static routes added via `quagga` can be deleted via Linux shell.
    This operation, while possible, should be avoided. Routes added by
    `quagga` should only be deleted by `quagga`, otherwise `quagga`
    might not be able to clean up all its internal state completely and
    incorrect routing can occur as a result.
