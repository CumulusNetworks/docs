---
title: Routing
author: Cumulus Networks
weight: 19
aliases:
 - /display/RMP25ESR/Routing
 - /pages/viewpage.action?pageId=5116359
pageID: 5116359
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
This chapter discusses routing on switches running Cumulus RMP.

## <span>Commands</span>

  - ip route

## <span>Configuring Static Routing</span>

The `ip route` command allows manipulating the kernel routing table
directly from the Linux shell. See `man ip(8)` for details.

To display the routing table:

    cumulus@switch:~$ ip route show
    default via 10.0.1.2 dev eth0
    default via 10.42.0.1 dev eth0 
    10.42.0.0/22 dev eth0  proto kernel  scope link  src 10.42.0.65 
    10.168.2.0/24 dev swp2  proto kernel  scope link  src 10.168.2.1 
    10.168.26.0/24 dev swp26  proto kernel  scope link  src 10.168.26.1 

### <span>Persistently Adding a Static Route</span>

A static route can be persistently added by adding `up ip route add ..`
into `/etc/network/interfaces`. For example:

    cumulus@switch:~$ cat /etc/network/interfaces
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5), ifup(8)
    #
    # Please see /usr/share/doc/python-ifupdown2/examples/ for examples
    #
    #
    
    # The loopback network interface
    auto lo
    iface lo inet loopback
    
    # The primary network interface
    auto eth0
    iface eth0 inet dhcp
    
    auto swp2
    iface swp2 inet static
       address 10.168.2.1/24
       up ip route add 203.0.113.0/24 via 10.168.2.2
    
    auto swp26
    iface swp26 inet static
       address 10.168.26.1/24

Configuration Files

  - /etc/network/interfaces

## <span>Useful Links</span>

  - <http://linux-ip.net/html/tools-ip-route.html>
