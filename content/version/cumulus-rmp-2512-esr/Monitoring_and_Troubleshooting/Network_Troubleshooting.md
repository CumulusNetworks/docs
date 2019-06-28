---
title: Network Troubleshooting
author: Cumulus Networks
weight: 101
aliases:
 - /display/RMP25ESR/Network+Troubleshooting
 - /pages/viewpage.action?pageId=5116329
pageID: 5116329
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
Cumulus RMP contains a number of command line and analytical tools to
help you troubleshoot issues with your network.

## <span>Commands</span>

  - arp

  - cl-acltool

  - ip

  - mz

  - ping

  - traceroute

## <span>Checking Reachability Using ping</span>

` ping  `is used to check reachability of a host. ` ping  `also
calculates the time it takes for packets to travel the round trip. See
` man  `` ping  `for details.

To test the connection to an IPv4 host:

    cumulus@switch:~$ ping 206.190.36.45
    PING 206.190.36.45 (206.190.36.45) 56(84) bytes of data.
    64 bytes from 206.190.36.45: icmp_req=1 ttl=53 time=40.4 ms
    64 bytes from 206.190.36.45: icmp_req=2 ttl=53 time=39.6 ms
    ...

To test the connection to an IPv6 host:

    cumulus@switch:~$ ping6 -I swp1 fe80::202:ff:fe00:2
    PING fe80::202:ff:fe00:2(fe80::202:ff:fe00:2) from fe80::202:ff:fe00:1 swp1: 56 data bytes
    64 bytes from fe80::202:ff:fe00:2: icmp_seq=1 ttl=64 time=1.43 ms
    64 bytes from fe80::202:ff:fe00:2: icmp_seq=2 ttl=64 time=0.927 ms

## <span>Printing Route Trace Using traceroute</span>

` trace route  `tracks the route that packets take from an IP network on
their way to a given host. See ` man traceroute  `for details.

To track the route to an IPv4 host:

    cumulus@switch:~$ traceroute www.google.com
    traceroute to www.google.com (74.125.239.49), 30 hops max, 60 byte packets
    1  fw.cumulusnetworks.com (192.168.1.1)  0.614 ms  0.863 ms  0.932 ms
    2  router.hackerdojo.com (157.22.42.1)  15.459 ms  16.447 ms  16.818 ms
    3  gw-cpe-hackerdojo.via.net (157.22.10.97)  18.470 ms  18.473 ms  18.897 ms
    4  ge-1-5-v223.core1.uspao.via.net (157.22.10.81)  20.419 ms  20.422 ms  21.026 ms
    5  core2-1-1-0.pao.net.google.com (198.32.176.31)  22.347 ms  22.584 ms  24.328 ms
    6  216.239.49.250 (216.239.49.250)  24.371 ms  25.757 ms  25.987 ms
    7  72.14.232.35 (72.14.232.35)  27.505 ms  22.925 ms  22.323 ms
    8  nuq04s19-in-f17.1e100.net (74.125.239.49)  23.544 ms  21.851 ms  22.604 ms

## <span>Manipulating the System ARP Cache</span>

` arp  `manipulates or displays the kernel’s IPv4 network neighbor
cache. See ` man arp  `for details.

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

## <span>Traffic Generation Using mz</span>

` mz  `is a fast traffic generator. It can generate a large variety of
packet types at high speed. See ` man mz  `for details.

For example, to send two sets of packets to TCP port 23 and 24, with
source IP 11.0.0.1 and destination 11.0.0.2, do the following:

``` 
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
```

<span id="src-5116329_NetworkTroubleshooting-counter_acl"></span>

## <span>Counter ACL</span>

In Linux, all ACL rules are always counted. To create an ACL rule for
counting purposes only, set the rule action to ACCEPT.

{{%notice note%}}

Always place your rules files under `/etc/cumulus/acl/policy.d/`.

{{%/notice%}}

To count all packets going to a Web server:

    cumulus@switch$ cat sample_count.rules
    
    [iptables]
    -A FORWARD -p tcp --dport 80 -j ACCEPT
    
    cumulus@switch:$ sudo cl-acltool -i -p sample_count.rules
    Using user provided rule file sample_count.rules
    Reading rule file sample_count.rules ...
    Processing rules in file sample_count.rules ...
    Installing acl policy... done.
    
    cumulus@switch$ sudo iptables -L -v
    Chain INPUT (policy ACCEPT 16 packets, 2224 bytes)
    pkts bytes target     prot opt in     out     source               destination
    
    Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination
       2   156 ACCEPT     tcp  --  any    any     anywhere             anywhere             tcp dpt:http
    
    Chain OUTPUT (policy ACCEPT 44 packets, 8624 bytes)
    pkts bytes target     prot opt in     out     source               destination

<span id="src-5116329_NetworkTroubleshooting-span"></span>

## <span>SPAN and ERSPAN</span>

SPAN (Switched Port Analyzer) provides for the mirroring of all packets
coming in from or going out of an interface to a local port for
monitoring. This port is referred to as a mirror-to-port (MTP). The
original packet is still switched, while a mirrored copy of the packet
is sent to the MTP port.

ERSPAN (Encapsulated Remote SPAN) enables the mirrored packets to be
sent to a monitoring node located anywhere across the routed network.
The switch finds the outgoing port of the mirrored packets by doing a
lookup of the destination IP address in its routing table. The original
L2 packet is encapsulated with GRE for IP delivery. The encapsulated
packets have the following format:

``` 
 ----------------------------------------------------------
| MAC_HEADER | IP_HEADER | GRE_HEADER | L2_Mirrored_Packet |
 ----------------------------------------------------------
```

SPAN and ERSPAN are configured via `cl-acltool`. The match criteria for
SPAN and ERSPAN can only be an interface; more granular match terms are
not supported. The interface can be a port, a subinterface or a bond
interface. Both ingress and egress interfaces can be matched.

Cumulus RMP supports a maximum of 2 SPAN destinations. Multiple rules
can point to the same SPAN destination. The MTP interface can be a
physical port, a subinterface, or a bond interface. The SPAN/ERSPAN
action is independent of security ACL actions. If packets match both a
security ACL rule and a SPAN rule, both actions will be carried out.

{{%notice note%}}

Always place your rules files under `/etc/cumulus/acl/policy.d/`.

{{%/notice%}}

To configure SPAN for all packets coming in from swp1 locally to swp3:

    cumulus@switch$ cat span.rules
    
    [iptables]
    -A FORWARD --in-interface swp1 -j SPAN --dport swp3
    
    cumulus@switch$ cl-acltool -i -p span.rules
    Using user provided rule file span.rules
    Reading rule file span.rules ...
    Processing rules in file span.rules ...
    Installing acl policy... done.
    
    cumulus@switch$ sudo iptables -L -v
    Chain INPUT (policy ACCEPT 18 packets, 3034 bytes)
     pkts bytes target     prot opt in     out     source               destination
    
     Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
      pkts bytes target     prot opt in     out     source               destination
        28  3014 SPAN       all  --  swp1   any     anywhere             anywhere             dport:swp3
    
     Chain OUTPUT (policy ACCEPT 56 packets, 12320 bytes)
      pkts bytes target     prot opt in     out     source               destination

To configure SPAN for all packets going out of bond0 locally to bond1:

    cumulus@switch$ cat span.rules
    
    [iptables]
    -A FORWARD --out-interface bond0 -j SPAN --dport bond1
    
    cumulus@switch$ cl-acltool -i -p span.rules
    Using user provided rule file span.rules
    Reading rule file span.rules ...
    Processing rules in file span.rules ...
    Installing acl policy... done.
    
    cumulus@switch$ sudo iptables -L -v
    Chain INPUT (policy ACCEPT 57 packets, 10000 bytes)
    pkts bytes target     prot opt in     out     source               destination
    
    Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination
       19  1938 SPAN       all  --  any    bond0   anywhere             anywhere             dport:bond1
    
    Chain OUTPUT (policy ACCEPT 686 packets, 119K bytes)
     pkts bytes target     prot opt in     out     source               destination

To configure ERSPAN for all packets coming in from swp1 to 12.0.0.2. :

    cumulus@switch$ cat erspan.rules
    
    [iptables]
    -A FORWARD --in-interface swp1 -j ERSPAN --src-ip 12.0.0.1 --dst-ip 12.0.0.2  --ttl 64
    
    cumulus@switch$ sudo cl-acltool -i -p erspan.rules
    Using user provided rule file erspan.rules
    Reading rule file erspan.rules ...
    Processing rules in file erspan.rules ...
    Installing acl policy... done.
    
    cumulus@switch$ sudo iptables -L -v
    Chain INPUT (policy ACCEPT 27 packets, 5526 bytes)
     pkts bytes target     prot opt in     out     source               destination
    
    Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination
       69  6804 ERSPAN     all  --  swp1   any     anywhere             anywhere             ERSPAN src-ip:12.0.0.1 dst-ip:12.0.0.2
    
    Chain OUTPUT (policy ACCEPT 822 packets, 163K bytes)
     pkts bytes target     prot opt in     out     source               destination

The `src-ip` option can be any IP address, whether it exists in the
routing table or not. The `dst-ip` option must be an IP address
reachable via the routing table. The destination IP address must be
reachable from a front-panel port, and not the management port. Use
`ping` or `ip route get <ip>` to verify that the destination IP address
is reachable. Setting the `--ttl` option is recommended.

{{%notice note%}}

When using [Wireshark](https://www.wireshark.org) to review the ERSPAN
output, Wireshark may report the message "Unknown version, please report
or test to use fake ERSPAN preference", and the trace is unreadable. To
resolve this, go into the General preferences for Wireshark, then go to
**Protocols** \> **ERSPAN** and check the **Force to decode fake ERSPAN
frame** option.

{{%/notice%}}

## <span>Configuration Files</span>

  - /etc/cumulus/acl/policy.conf

## <span>Useful Links</span>

  - <http://en.wikipedia.org/wiki/Ping>

  - <https://en.wikipedia.org/wiki/Traceroute>

  - <http://www.perihel.at/sec/mz/mzguide.html>

## <span>Caveats and Errata</span>

  - SPAN rules cannot match outgoing subinterfaces.
