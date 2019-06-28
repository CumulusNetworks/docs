---
title: Network Troubleshooting
author: Cumulus Networks
weight: 113
aliases:
 - /display/RMP321/Network+Troubleshooting
 - /pages/viewpage.action?pageId=5127560
pageID: 5127560
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
Cumulus RMP contains a number of command line and analytical tools to
help you troubleshoot issues with your network.

## <span>Checking Reachability Using ping</span>

`ping` is used to check reachability of a host. `ping` also calculates
the time it takes for packets to travel the round trip. See `man ping`
for details.

To test the connection to an IPv4 host:

    cumulus@switch:~$ ping 192.0.2.45
    PING 192.0.2.45 (192.0.2.45) 56(84) bytes of data.
    64 bytes from 192.0.2.45: icmp_req=1 ttl=53 time=40.4 ms
    64 bytes from 192.0.2.45: icmp_req=2 ttl=53 time=39.6 ms
    ...

To test the connection to an IPv6 host:

    cumulus@switch:~$ ping6 -I swp1 2001::db8:ff:fe00:2
    PING 2001::db8:ff:fe00:2(2001::db8:ff:fe00:2) from 2001::db8:ff:fe00:1 swp1: 56 data bytes
    64 bytes from 2001::db8:ff:fe00:2: icmp_seq=1 ttl=64 time=1.43 ms
    64 bytes from 2001::db8:ff:fe00:2: icmp_seq=2 ttl=64 time=0.927 ms

## <span>Printing Route Trace Using traceroute</span>

`traceroute` tracks the route that packets take from an IP network on
their way to a given host. See `man traceroute` for details.

To track the route to an IPv4 host:

    cumulus@switch:~$ traceroute www.google.com
    traceroute to www.google.com (74.125.239.49), 30 hops max, 60 byte packets
    1  cumulusnetworks.com (192.168.1.1)  0.614 ms  0.863 ms  0.932 ms
    ...
    5  core2-1-1-0.pao.net.google.com (198.32.176.31)  22.347 ms  22.584 ms  24.328 ms
    6  216.239.49.250 (216.239.49.250)  24.371 ms  25.757 ms  25.987 ms
    7  72.14.232.35 (72.14.232.35)  27.505 ms  22.925 ms  22.323 ms
    8  nuq04s19-in-f17.1e100.net (74.125.239.49)  23.544 ms  21.851 ms  22.604 ms

## <span>Manipulating the System ARP Cache</span>

`arp` manipulates or displays the kernel’s IPv4 network neighbor cache.
See `man arp` for details.

To display the ARP cache:

    cumulus@switch:~$ arp -a
    ? (11.0.2.2) at 00:02:00:00:00:10 [ether] on swp3
    ? (11.0.3.2) at 00:02:00:00:00:01 [ether] on swp4
    ? (11.0.0.2) at 44:38:39:00:01:c1 [ether] on swp1

To delete an ARP cache entry:

    cumulus@switch:~$ arp -d 11.0.2.2
    cumulus@switch:~$ arp -a
    ? (11.0.2.2) at <incomplete> on swp3
    ? (11.0.3.2) at 00:02:00:00:00:01 [ether] on swp4
    ? (11.0.0.2) at 44:38:39:00:01:c1 [ether] on swp1

To add a static ARP cache entry:

    cumulus@switch:~$ arp -s 11.0.2.2 00:02:00:00:00:10
    cumulus@switch:~$ arp -a
    ? (11.0.2.2) at 00:02:00:00:00:10 [ether] PERM on swp3
    ? (11.0.3.2) at 00:02:00:00:00:01 [ether] on swp4
    ? (11.0.0.2) at 44:38:39:00:01:c1 [ether] on swp1

## <span>Generating Traffic Using mz</span>

`mz` is a fast traffic generator. It can generate a large variety of
packet types at high speed. See `man mz` for details.

For example, to send two sets of packets to TCP port 23 and 24, with
source IP 11.0.0.1 and destination 11.0.0.2, do the following:

    cumulus@switch:~$ sudo mz swp1 -A 11.0.0.1 -B 11.0.0.2 -c 2 -v -t tcp "dp=23-24"
     
    Mausezahn 0.40 - (C) 2007-2010 by Herbert Haas - http://www.perihel.at/sec/mz/
    Use at your own risk and responsibility!
    -- Verbose mode --
     
    This system supports a high resolution clock.
     The clock resolution is 4000250 nanoseconds.
    Mausezahn will send 4 frames...
     IP:  ver=4, len=40, tos=0, id=0, frag=0, ttl=255, proto=6, sum=0, SA=11.0.0.1, DA=11.0.0.2,
          payload=[see next layer]
     TCP: sp=0, dp=23, S=42, A=42, flags=0, win=10000, len=20, sum=0,
          payload=
     
     IP:  ver=4, len=40, tos=0, id=0, frag=0, ttl=255, proto=6, sum=0, SA=11.0.0.1, DA=11.0.0.2,
          payload=[see next layer]
     TCP: sp=0, dp=24, S=42, A=42, flags=0, win=10000, len=20, sum=0,
          payload=
     
     IP:  ver=4, len=40, tos=0, id=0, frag=0, ttl=255, proto=6, sum=0, SA=11.0.0.1, DA=11.0.0.2,
          payload=[see next layer]
     TCP: sp=0, dp=23, S=42, A=42, flags=0, win=10000, len=20, sum=0,
          payload=
     
     IP:  ver=4, len=40, tos=0, id=0, frag=0, ttl=255, proto=6, sum=0, SA=11.0.0.1, DA=11.0.0.2,
          payload=[see next layer]
     TCP: sp=0, dp=24, S=42, A=42, flags=0, win=10000, len=20, sum=0,
          payload= 

## <span>Related Information</span>

  - [www.perihel.at/sec/mz/mzguide.html](http://www.perihel.at/sec/mz/mzguide.html)

  - [en.wikipedia.org/wiki/Ping](http://en.wikipedia.org/wiki/Ping)

  - [en.wikipedia.org/wiki/Traceroute](https://en.wikipedia.org/wiki/Traceroute)
