---
title: Routes from BGP and OSPF not Installed in the Routing Table
author: NVIDIA
weight: 391
toc: 4
---

## Issue

The route table entries for BGP and OSPF routes are missing from the routing table. For example:

    frr# show ip bgp
    BGP table version is 0, local router ID is 10.4.4.4
    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
                  r RIB-failure, S Stale, R Removed
    Origin codes: i - IGP, e - EGP, ? - incomplete

       Network          Next Hop            Metric LocPrf Weight Path
    *> 10.0.1.0/24      10.1.1.2                 1             0 65511 ?
    *> 10.1.1.0/24      10.1.1.2                 1             0 65511 ?
    *> 10.3.3.3/32      10.1.1.2                 1             0 65511 ?

    Total number of prefixes 3
    frr# show ip route
    frr# exit

    cumulus@switch:~$ ip route show
    default via 10.0.1.2 dev eth0 
    10.0.1.0/24 dev eth0  proto kernel  scope link  src 10.0.1.208 
    10.1.1.0/24 dev swp3  proto kernel  scope link  src 10.1.1.1 
    10.2.2.0/24 dev swp4  proto kernel  scope link  src 10.2.2.2

## Environment

- Cumulus Linux, all versions

## Cause

The Zebra daemon is not running. The Zebra daemon does not install routes, learned from routing protocols, into the routing table.

## Resolution

1.  Edit `/etc/frr/daemons` and set the `zebra` keyword to *yes*.

        cumulus@switch:~$ sudo vi /etc/frr/daemons
        ----------------
        zebra=no [change to yes]
        bgpd=yes
        ospfd=yes
        ----------------

2.  Restart FRRouting.

        cumulus@switch:~$ sudo systemctl restart frr
        ...
        .....
        frr# show ip route
        Codes: K - kernel route, C - connected, S - static, R - RIP,
               O - OSPF, I - IS-IS, B - BGP, A - Babel,
               > - selected route, * - FIB route

        K>* 0.0.0.0/0 via 10.0.1.2, eth0
        C>* 10.0.1.0/24 is directly connected, eth0
        C>* 10.1.1.0/24 is directly connected, swp3
        B>* 10.3.3.3/32 [20/1] via 10.1.1.2, swp3, 00:00:08 
        C>* 10.4.4.4/32 is directly connected, lo
        C>* 127.0.0.0/8 is directly connected, lo

3.  Exit FRR, then use `ip route show` in Cumulus Linux to verify.

        frr# exit

        cumulus@switch:~$ ip route show
        default via 10.0.1.2 dev eth0 
        10.0.1.0/24 dev eth0  proto kernel  scope link  src 10.0.1.208 
        10.1.1.0/24 dev swp3  proto kernel  scope link  src 10.1.1.1 
        10.2.2.0/24 dev swp4  proto kernel  scope link  src 10.2.2.2 
        10.3.3.3 via 10.1.1.2 dev swp3  proto zebra  metric 20 
