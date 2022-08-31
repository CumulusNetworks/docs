---
title: Network Troubleshooting
author: NVIDIA
weight: 1110
toc: 3
---
Cumulus Linux includes command line and analytical tools to help you troubleshoot issues with your network.

## Use ping

Use `ping` to check that a host is reachable. `ping` also calculates the time it takes for packets to travel round trip. See `man ping` for details.

To test the connection to an IPv4 host:

```
cumulus@switch:~$ ping 192.0.2.45
PING 192.0.2.45 (192.0.2.45) 56(84) bytes of data.
64 bytes from 192.0.2.45: icmp_req=1 ttl=53 time=40.4 ms
64 bytes from 192.0.2.45: icmp_req=2 ttl=53 time=39.6 ms
...
```

To test the connection to an IPv6 host:

```
cumulus@switch:~$ ping6 -I swp1 2001::db8:ff:fe00:2
PING 2001::db8:ff:fe00:2(2001::db8:ff:fe00:2) from 2001::db8:ff:fe00:1 swp1: 56 data bytes
64 bytes from 2001::db8:ff:fe00:2: icmp_seq=1 ttl=64 time=1.43 ms
64 bytes from 2001::db8:ff:fe00:2: icmp_seq=2 ttl=64 time=0.927 ms
```

When troubleshooting intermittent connectivity issues, it is helpful to send continuous pings to a host.

## Print Route Trace with traceroute

Use `traceroute` to track the route that packets take from an IP network on their way to a given host. See `man traceroute` for details.

To track the route to an IPv4 host:

```
cumulus@switch:~$ traceroute www.google.com
traceroute to www.google.com (74.125.239.49), 30 hops max, 60 byte packets
1  cumulusnetworks.com (192.168.1.1)  0.614 ms  0.863 ms  0.932 ms
...
5  core2-1-1-0.pao.net.google.com (198.32.176.31)  22.347 ms  22.584 ms  24.328 ms
6  216.239.49.250 (216.239.49.250)  24.371 ms  25.757 ms  25.987 ms
7  72.14.232.35 (72.14.232.35)  27.505 ms  22.925 ms  22.323 ms
8  nuq04s19-in-f17.1e100.net (74.125.239.49)  23.544 ms  21.851 ms  22.604 ms
```
<!-- vale off -->
## Run Commands in a Non-default VRF
<!-- vale on -->
You can use `ip vrf exec` to run commands in a non-default VRF context, which is useful for network utilities like `ping`, `traceroute`, and `nslookup`.

The full syntax is `ip vrf exec <vrf-name> <command> <arguments>`. For example:

```
cumulus@switch:~$ sudo ip vrf exec Tenant1 nslookup google.com - 8.8.8.8
```

By default, `ping` and `ping6`, and `traceroute` and `traceroute6` all use the default VRF and use a mechanism that checks the VRF context of the current shell, which you can see when you run `ip vrf id`. If the VRF context of the shell is *mgmt*, these commands run in the default VRF context.

`ping` and `traceroute` have additional arguments that you can use to specify an egress interface or a source address. In the default VRF, the source interface flag (`ping -I` or `traceroute -i`) specifies the egress interface for the `ping` or `traceroute` operation. However, you can use the source interface flag instead to specify a non-default VRF to use for the command. Doing so causes the routing lookup for the destination address to occur in that VRF.
<!-- vale off -->
With `ping -I`, you can specify the source interface or the source IP address but you cannot use the flag more than once. Either choose an egress interface/VRF or a source IP address. For `traceroute`, you can use `traceroute -s` to specify the source IP address.
<!-- vale on -->
You gain additional flexibility if you run `ip vrf exec` in combination with `ping`/`ping6`  or `traceroute`/`traceroute6`, as the VRF context is outside of the `ping` and `traceroute` commands. This allows for the most granular control of `ping` and `traceroute`, as you can specify both the VRF and the source interface flag.

For `ping`, use the following syntax:

```
ip vrf exec <vrf-name> [ping|ping6] -I [<egress_interface> | <source_ip>] <destination_ip>
```

For example:

```
cumulus@switch:~$ sudo ip vrf exec Tenant1 ping -I swp1 8.8.8.8
cumulus@switch:~$ sudo ip vrf exec Tenant1 ping -I 192.0.1.1 8.8.8.8
cumulus@switch:~$ sudo ip vrf exec Tenant1 ping6 -I swp1 2001:4860:4860::8888
cumulus@switch:~$ sudo ip vrf exec Tenant1 ping6 -I 2001:db8::1 2001:4860:4860::8888
```

For `traceroute`, use the following syntax:

```
ip vrf exec <vrf-name> [traceroute|traceroute6] -i <egress_interface> -s <source_ip> <destination_ip>
```

For example:

```
cumulus@switch:~$ sudo ip vrf exec Tenant1 traceroute -i swp1 -s 192.0.1.1 8.8.8.8
cumulus@switch:~$ sudo ip vrf exec Tenant1 traceroute6 -i swp1 -s 2001:db8::1 2001:4860:4860::8888
```

The VRF context for `ping` and `traceroute` commands move automatically to the default VRF context, therefore, you must use the source interface flag to specify the management VRF. Typically, there is only a single interface in the management VRF (eth0) and only a single IPv4 address or IPv6 global unicast address assigned to it. You cannot specify both a source interface and a source IP address with `ping -I`.

## Manipulate the System ARP Cache

The `arp` command manipulates or displays the kernel's IPv4 network neighbor cache. See `man arp` for details.

To display the ARP cache:

```
cumulus@switch:~$ arp -a
? (11.0.2.2) at 00:02:00:00:00:10 [ether] on swp3
? (11.0.3.2) at 00:02:00:00:00:01 [ether] on swp4
? (11.0.0.2) at 44:38:39:00:01:c1 [ether] on swp1
```

To delete an ARP cache entry:

```
cumulus@switch:~$ arp -d 11.0.2.2
cumulus@switch:~$ arp -a
? (11.0.2.2) at <incomplete> on swp3
? (11.0.3.2) at 00:02:00:00:00:01 [ether] on swp4
? (11.0.0.2) at 44:38:39:00:01:c1 [ether] on swp1
```

To add a static ARP cache entry:

```
cumulus@switch:~$ arp -s 11.0.2.2 00:02:00:00:00:10
cumulus@switch:~$ arp -a
? (11.0.2.2) at 00:02:00:00:00:10 [ether] PERM on swp3
? (11.0.3.2) at 00:02:00:00:00:01 [ether] on swp4
? (11.0.0.2) at 44:38:39:00:01:c1 [ether] on swp1
```

If you need to flush or remove an ARP entry for a specific interface, you can disable dynamic ARP learning:

```
cumulus@switch:~$ ip link set arp off dev INTERFACE
```

## Generate Traffic Using mz

`{{<exlink url="http://www.netsniff-ng.org" text="mz">}}` (or `mausezahn`) is a fast traffic generator that can generate a large variety of packet types at high speed. See `man mz` for details.

For example, to send two sets of packets to TCP port 23 and 24, with source IP address 11.0.0.1 and destination IP address 11.0.0.2:

```
cumulus@switch:~$ sudo mz swp1 -A 11.0.0.1 -B 11.0.0.2 -c 2 -v -t tcp "dp=23-24"

Mausezahn 0.40 - (C) 2007-2010 by Herbert Haas - https://packages.debian.org/unstable/mz
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

## Create Counter ACL Rules

In Linux, all ACL rules are always counted. To create an ACL rule for counting purposes only, set the rule action to ACCEPT. For details on how to use `cl-acltool` to set up iptables, ip6tables, and ebtables-based ACLs, see {{<link url="Netfilter-ACLs" text="Netfilter ACLs">}}.

{{%notice note%}}
Always place your rule files under `/etc/cumulus/acl/policy.d/`.
{{%/notice%}}

To count all packets going to a Web server:

```
cumulus@switch:~$ cat sample_count.rules

  [iptables]
  -A FORWARD -p tcp --dport 80 -j ACCEPT

  cumulus@switch:~$ sudo cl-acltool -i -p sample_count.rules
  Using user provided rule file sample_count.rules
  Reading rule file sample_count.rules ...
  Processing rules in file sample_count.rules ...
  Installing acl policy... done.

  cumulus@switch:~$ sudo iptables -L -v
  Chain INPUT (policy ACCEPT 16 packets, 2224 bytes)
  pkts bytes target     prot opt in     out     source          destination

  Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
  pkts bytes target     prot opt in     out     source          destination
    2   156 ACCEPT     tcp  --  any    any     anywhere         anywhere           tcp dpt:http

  Chain OUTPUT (policy ACCEPT 44 packets, 8624 bytes)
  pkts bytes target     prot opt in     out     source          destination
```

{{%notice warning%}}
The `-p` option clears out all other rules. The `-i` option reinstalls all the rules.
{{%/notice%}}

### Monitor Control Plane Traffic with tcpdump

You can use `tcpdump` to monitor control plane traffic (traffic sent to and coming from the switch CPUs). `tcpdump` does **not** monitor data plane traffic; use `cl-acltool` instead (see above).

For more information on `tcpdump`, read the {{<exlink url="http://www.tcpdump.org/#documentation" text="documentation">}} and the {{<exlink url="http://www.tcpdump.org/manpages/tcpdump.1.html" text="man page">}}.

The following example incorporates `tcpdump` options:

- `-i bond0` captures packets from bond0 to the CPU and from the CPU to bond0
- `host 169.254.0.2` filters for this IP address
- `-c 10` captures 10 packets then stops

```
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
```
