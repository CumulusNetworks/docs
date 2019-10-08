---
title: Network Troubleshooting
author: Cumulus Networks
weight: 173
aliases:
 - /display/CL25ESR/Network+Troubleshooting
 - /pages/viewpage.action?pageId=5115968
pageID: 5115968
product: Cumulus Linux
version: 2.5 ESR
imgData: cumulus-linux-25esr
siteSlug: cumulus-linux-25esr
---
Cumulus Linux contains a number of command line and analytical tools to
help you troubleshoot issues with your network.

## Commands

  - arp
  - cl-acltool
  - ip
  - mz
  - ping
  - tcpdump
  - traceroute

## Checking Reachability Using ping

`ping` is used to check reachability of a host. `ping` also calculates
the time it takes for packets to travel the round trip. See `man ping`
for details.

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

## Printing Route Trace Using traceroute

`traceroute` tracks the route that packets take from an IP network on
their way to a given host. See `man traceroute` for details.

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

## Manipulating the System ARP Cache

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

## Generating Traffic Using mz

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

## Creating Counter ACL Rules

In Linux, all ACL rules are always counted. To create an ACL rule for
counting purposes only, set the rule action to ACCEPT. See the
[Netfilter](/version/cumulus-linux-25esr/System-Management/Netfilter-ACLs)
chapter for details on how to use `cl-acltool` to set up
iptables-/ip6tables-/ebtables-based ACLs.

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

{{%notice warning%}}

The `-p` option clears out all other rules, and the `-i` option is used
to reinstall all the rules.

{{%/notice%}}

## Configuring SPAN and ERSPAN

SPAN (Switched Port Analyzer) provides for the mirroring of all packets
coming in from or going out of an interface (the *SPAN source*), and
being copied and transmitted out of a local port (the *SPAN
destination*) for monitoring. The SPAN destination port is referred to
as a *mirror-to-port* (MTP). The original packet is still switched,
while a mirrored copy of the packet is sent out of the MTP port.

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

{{%notice note%}}

Mirrored traffic is not guaranteed. If the MTP is congested, mirrored
packets may be discarded.

{{%/notice%}}

SPAN and ERSPAN are configured via `cl-acltool`, the 
[same utility for security ACL configuration](/version/cumulus-linux-25esr/System-Management/Netfilter-ACLs).
The match criteria for SPAN and ERSPAN can only be an interface; more
granular match terms are not supported. This SPAN source interface can
be a port, a subinterface or a bond interface. Both ingress and egress
traffic on interfaces can be matched.

Cumulus Linux supports a maximum of 2 SPAN destinations. Multiple rules
(SPAN sources) can point to the same SPAN destination, although a given
SPAN source cannot specify 2 SPAN destinations. The SPAN destination
(MTP) interface can be a physical port, a subinterface, or a bond
interface. The SPAN/ERSPAN action is independent of security ACL
actions. If packets match both a security ACL rule and a SPAN rule, both
actions will be carried out.

{{%notice note%}}

Always place your rules files under `/etc/cumulus/acl/policy.d/`.

{{%/notice%}}

### Configuring SPAN for Switch Ports

This section describes how to set up, install, verify and uninstall SPAN
rules. In the examples that follow, you will span (mirror) switch port
swp4 input traffic and swp4 output traffic to destination switch port swp19.

First, create a rules file in `/etc/cumulus/acl/policy.d/`:

    cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/span.rules 
    [iptables]
    -A FORWARD --in-interface swp4 -j SPAN --dport swp19
    -A FORWARD --out-interface swp4 -j SPAN --dport swp19
    EOF'

{{%notice note%}}

Using `cl-acltool` with the `--out-interface` rule applies to transit
traffic only; it does not apply to traffic sourced from the switch.

{{%/notice%}}

Next, verify all the rules that are currently installed:

``` 
cumulus@switch:~$ sudo iptables -L -v
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 DROP       all  --  swp+   any     240.0.0.0/5          anywhere            
    0     0 DROP       all  --  swp+   any     loopback/8           anywhere            
    0     0 DROP       all  --  swp+   any     base-address.mcast.net/8  anywhere            
    0     0 DROP       all  --  swp+   any     255.255.255.255      anywhere            
    0     0 SETCLASS   ospf --  swp+   any     anywhere             anywhere             SETCLASS  class:7
    0     0 POLICE     ospf --  any    any     anywhere             anywhere             POLICE  mode:pkt rate:2000 burst:2000
    0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp dpt:bgp SETCLASS  class:7
    0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bgp POLICE  mode:pkt rate:2000 burst:2000
    0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp spt:bgp SETCLASS  class:7
    0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp spt:bgp POLICE  mode:pkt rate:2000 burst:2000
    0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp dpt:5342 SETCLASS  class:7
    0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:5342 POLICE  mode:pkt rate:2000 burst:2000
    0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp spt:5342 SETCLASS  class:7
    0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp spt:5342 POLICE  mode:pkt rate:2000 burst:2000
    0     0 SETCLASS   icmp --  swp+   any     anywhere             anywhere             SETCLASS  class:2
    0     0 POLICE     icmp --  any    any     anywhere             anywhere             POLICE  mode:pkt rate:100 burst:40
   15  5205 SETCLASS   udp  --  swp+   any     anywhere             anywhere             udp dpts:bootps:bootpc SETCLASS  class:2
   11  3865 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:bootps POLICE  mode:pkt rate:100 burst:100
    0     0 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:bootpc POLICE  mode:pkt rate:100 burst:100
    0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp dpts:bootps:bootpc SETCLASS  class:2
    0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bootps POLICE  mode:pkt rate:100 burst:100
    0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bootpc POLICE  mode:pkt rate:100 burst:100
   17  1088 SETCLASS   igmp --  swp+   any     anywhere             anywhere             SETCLASS  class:6
   17  1156 POLICE     igmp --  any    any     anywhere             anywhere             POLICE  mode:pkt rate:300 burst:100
  394 41060 POLICE     all  --  swp+   any     anywhere             anywhere             ADDRTYPE match dst-type LOCAL POLICE  mode:pkt rate:1000 burst:1000 class:0
    0     0 POLICE     all  --  swp+   any     anywhere             anywhere             ADDRTYPE match dst-type IPROUTER POLICE  mode:pkt rate:400 burst:100 class:0
  988  279K SETCLASS   all  --  swp+   any     anywhere             anywhere             SETCLASS  class:0

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 DROP       all  --  swp+   any     240.0.0.0/5          anywhere            
    0     0 DROP       all  --  swp+   any     loopback/8           anywhere            
    0     0 DROP       all  --  swp+   any     base-address.mcast.net/8  anywhere            
    0     0 DROP       all  --  swp+   any     255.255.255.255      anywhere            
26864 4672K SPAN       all  --  swp4   any     anywhere             anywhere             dport:swp19  <---- input packets on swp4

40722   47M SPAN       all  --  any    swp4    anywhere             anywhere             dport:swp19  <---- output packets on swp4


Chain OUTPUT (policy ACCEPT 67398 packets, 5757K bytes)
 pkts bytes target     prot opt in     out     source               destination         
```

Install the rules:

    cumulus@switch:~$ sudo cl-acltool -i 
    [sudo] password for cumulus:
    Reading rule file /etc/cumulus/acl/policy.d/00control_plane.rules ...
    Processing rules in file /etc/cumulus/acl/policy.d/00control_plane.rules ...
    Reading rule file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
    Processing rules in file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
    Reading rule file /etc/cumulus/acl/policy.d/span.rules ...
    Processing rules in file /etc/cumulus/acl/policy.d/span.rules ...
    Installing acl policy
    done.

{{%notice warning%}}

Running the following command is incorrect and will remove **all**
existing control-plane rules or other installed rules and only install
the rules defined in `span.rules`:

    cumulus@switch:~$ sudo cl-acltool -i  -P /etc/cumulus/acl/policy.d/span.rules

{{%/notice%}}

Verify that the SPAN rules were installed:

    cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
    38025 7034K SPAN       all  --  swp4   any     anywhere             anywhere             dport:swp19
    50832   55M SPAN       all  --  any    swp4    anywhere             anywhere             dport:swp19

### Configuring SPAN for Bonds

This section describes how to configure SPAN for all packets going out
of `bond0` locally to `bond1`.

First, create a rules file in `/etc/cumulus/acl/policy.d/`:

    cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/span_bond.rules 
    [iptables]
    -A FORWARD --out-interface bond0 -j SPAN --dport bond1
    EOF'

{{%notice note%}}

Using `cl-acltool` with the `--out-interface` rule applies to transit
traffic only; it does not apply to traffic sourced from the switch.

{{%/notice%}}

Install the rules:

    cumulus@switch:~$ sudo cl-acltool -i 
    [sudo] password for cumulus:
    Reading rule file /etc/cumulus/acl/policy.d/00control_plane.rules ...
    Processing rules in file /etc/cumulus/acl/policy.d/00control_plane.rules ...
    Reading rule file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
    Processing rules in file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
    Reading rule file /etc/cumulus/acl/policy.d/span_bond.rules ...
    Processing rules in file /etc/cumulus/acl/policy.d/span_bond.rules ...
    Installing acl policy
    done.

Verify that the SPAN rules were installed:

    cumulus@switch:~$ sudo iptables -L -v | grep SPAN
       19  1938 SPAN       all  --  any    bond0   anywhere             anywhere             dport:bond1

### Configuring ERSPAN

This section describes how to configure ERSPAN for all packets coming in
from `swp1` to 12.0.0.2:

First, create a rules file in `/etc/cumulus/acl/policy.d/`:

    cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/erspan.rules 
    [iptables]
    -A FORWARD --in-interface swp1 -j ERSPAN --src-ip 12.0.0.1 --dst-ip 12.0.0.2  --ttl 64
    EOF'

Install the rules:

    cumulus@switch:~$ sudo cl-acltool -i
    Reading rule file /etc/cumulus/acl/policy.d/00control_plane.rules ...
    Processing rules in file /etc/cumulus/acl/policy.d/00control_plane.rules ...
    Reading rule file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
    Processing rules in file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
    Reading rule file /etc/cumulus/acl/policy.d/erspan.rules ...
    Processing rules in file /etc/cumulus/acl/policy.d/erspan.rules ...
    Installing acl policy
    done.

Verify that the ERSPAN rules were installed:

    cumulus@switch:~$ sudo iptables -L -v | grep SPAN
       69  6804 ERSPAN     all  --  swp1   any     anywhere             anywhere             ERSPAN src-ip:12.0.0.1 dst-ip:12.0.0.2

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

### Removing SPAN Rules

To remove your SPAN rules, run:

    #Remove rules file:
    cumulus@switch:~$ sudo rm  /etc/cumulus/acl/policy.d/span.rules
    #Reload the default rules
    cumulus@switch:~$ sudo cl-acltool -i
    cumulus@switch:~$

To verify that the SPAN rules were removed:

    cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
    cumulus@switch:~$

## Monitoring Control Plane Traffic with tcpdump

You can use `tcpdump` to monitor control plane traffic — traffic sent to
and coming from the switch CPUs. `tcpdump` does **not** monitor data
plane traffic; use `cl-acltool` instead (see above).

For more information on tcpdump, read 
[the `tcpdump` documentation](http://www.tcpdump.org/#documentation) 
and the [`tcpdump` man page](http://www.tcpdump.org/manpages/tcpdump.1.html).

The following example incorporates a few `tcpdump` options:

  - `-i bond0`, which captures packets from bond0 to the CPU and from
    the CPU to bond0
  - `host 169.254.0.2`, which filters for this IP address
  - `-c 10`, which captures 10 packets then stops

<!-- end list -->

    cumulus@switch:~$ sudo tcpdump -i bond0 host 169.254.0.2 -c 10
    tcpdump: WARNING: bond0: no IPv4 address assigned
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on bond0, link-type EN10MB (Ethernet), capture size 65535 bytes
    16:24:42.532473 IP 169.254.0.2 > 169.254.0.1: ICMP echo request, id 27785, seq 6, length 64
    16:24:42.532534 IP 169.254.0.1 > 169.254.0.2: ICMP echo reply, id 27785, seq 6, length 64
    16:24:42.804155 IP 169.254.0.2.40210 > 169.254.0.1.5342: Flags [.], seq 266275591:266277039, ack 3813627681, win 58, options [nop,nop,TS val 590400681 ecr 530346691], length 1448
    16:24:42.804228 IP 169.254.0.1.5342 > 169.254.0.2.40210: Flags [.], ack 1448, win 166, options [nop,nop,TS val 530348721 ecr 590400681], length 0
    16:24:42.804267 IP 169.254.0.2.40210 > 169.254.0.1.5342: Flags [P.], seq 1448:1836, ack 1, win 58, options [nop,nop,TS val 590400681 ecr 530346691], length 388
    16:24:42.804293 IP 169.254.0.1.5342 > 169.254.0.2.40210: Flags [.], ack 1836, win 165, options [nop,nop,TS val 530348721 ecr 590400681], length 0
    16:24:43.532389 IP 169.254.0.2 > 169.254.0.1: ICMP echo request, id 27785, seq 7, length 64
    16:24:43.532447 IP 169.254.0.1 > 169.254.0.2: ICMP echo reply, id 27785, seq 7, length 64
    16:24:43.838652 IP 169.254.0.1.59951 > 169.254.0.2.5342: Flags [.], seq 2555144343:2555145791, ack 2067274882, win 58, options [nop,nop,TS val 530349755 ecr 590399688], length 1448
    16:24:43.838692 IP 169.254.0.1.59951 > 169.254.0.2.5342: Flags [P.], seq 1448:1838, ack 1, win 58, options [nop,nop,TS val 530349755 ecr 590399688], length 390
    10 packets captured
    12 packets received by filter
    0 packets dropped by kernel

## Configuration Files

  - /etc/cumulus/acl/policy.conf

## Useful Links

  - [www.perihel.at/sec/mz/mzguide.html](http://www.perihel.at/sec/mz/mzguide.html)
  - [en.wikipedia.org/wiki/Ping](http://en.wikipedia.org/wiki/Ping)
  - [www.tcpdump.org](http://www.tcpdump.org)
  - [en.wikipedia.org/wiki/Traceroute](https://en.wikipedia.org/wiki/Traceroute)

## Caveats and Errata

  - SPAN rules cannot match outgoing subinterfaces.
  - ERSPAN rules must include `ttl` for versions 1.5.1 and earlier.
