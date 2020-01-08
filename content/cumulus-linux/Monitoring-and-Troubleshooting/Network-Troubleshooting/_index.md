---
title: Network Troubleshooting
author: Cumulus Networks
weight: 227
aliases:
 - /display/DOCS/Network+Troubleshooting
 - /pages/viewpage.action?pageId=8366317
product: Cumulus Linux
version: '4.0'
---
Cumulus Linux includes a number of command line and analytical tools to help you troubleshoot issues with your network.

## Check Reachability Using ping

Use `ping` to check reachability of a host. `ping` also calculates the time it takes for packets to travel the round trip. See `man ping` for details.

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

## Print Route Trace Using traceroute

`traceroute` tracks the route that packets take from an IP network on their way to a given host. See `man traceroute` for details.

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

## Run Commands in a Non-default VRF

You can use `ip vrf exec` to run commands in a non-default VRF context. This is particularly useful for network utilities like `ping`, `traceroute`, and `nslookup`.

The full syntax is `ip vrf exec <vrf-name> <command> <arguments>`. For example:

```
cumulus@switch:~$ sudo ip vrf exec Tenant1 nslookup google.com - 8.8.8.8
```

By default, `ping`/`ping6` and `traceroute`/`traceroute6` all use the default VRF. This is done using a mechanism that checks the VRF context of the current shell - which can be seen when you run `ip vrf id` - at the time one of these commands is run. If the shell's VRF context is *mgmt*, then these commands are run in the default VRF context.

`ping` and `traceroute` have additional arguments that you can use to specify an egress interface and/or a source address. In the default VRF, the source interface flag (`ping -I` or `traceroute -i`) specifies the egress interface for the `ping`/`traceroute` operation. However, you can use the source interface flag instead to specify a non-default VRF to use for the command. Doing so causes the routing lookup for the destination address to occur in that VRF.

With `ping -I`, you can specify the source interface or the source IP address, but you cannot use the flag more than once. Thus, you can choose either an egress interface/VRF or a source IP address. For `traceroute`, you can use `traceroute -s` to specify the source IP address.

You gain some additional flexibility if you run `ip vrf exec` in combination with `ping`/`ping6`  or `traceroute`/`traceroute6`, as the VRF context is specified outside of the `ping` and `traceroute` commands. This allows for the most granular control of `ping` and `traceroute`, as you can specify both the VRF and the source interface flag.

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

Because the VRF context for `ping` and `traceroute` commands is automatically shifted to the default VRF context, you must use the source interface flag to specify the management VRF. Typically, this is not an issue since there is only a single interface in the management VRF - eth0 - and in most situations only a single IPv4 address or IPv6 global unicast address is assigned to it. But it is worth mentioning since, as stated earlier, you cannot specify both a source interface and a source IP address with `ping -I`.

## Manipulate the System ARP Cache

`arp` manipulates or displays the kernel's IPv4 network neighbor cache. See `man arp` for details.

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

`mz` is a fast traffic generator. It can generate a large variety of packet types at high speed. See `man mz` for details.

For example, to send two sets of packets to TCP port 23 and 24, with source IP address 11.0.0.1 and destination IP address 11.0.0.2:

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

## Create Counter ACL Rules

In Linux, all ACL rules are always counted. To create an ACL rule for counting purposes only, set the rule action to ACCEPT. See the [Netfilter](../../System-Configuration/Netfilter-ACLs/) chapter for details on how to use `cl-acltool` to set up iptables-/ip6tables-/ebtables-based ACLs.

{{%notice note%}}

Always place your rules files under `/etc/cumulus/acl/policy.d/`.

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

## Configure SPAN and ERSPAN

SPAN (Switched Port Analyzer) provides for the mirroring of all packets coming in from or going out of an interface (the *SPAN source*), and being copied and transmitted out of a local port (the *SPAN destination*) for monitoring. The SPAN destination port is also referred to as a mirror-to-port (MTP). The original packet is still switched, while a mirrored copy of the packet is sent out of the MTP.

ERSPAN (Encapsulated Remote SPAN) enables the mirrored packets to be sent to a monitoring node located anywhere across the routed network. The switch finds the outgoing port of the mirrored packets by doing a lookup of the destination IP address in its routing table. The original L2 packet is encapsulated with GRE for IP delivery. The encapsulated packets have the following format:

```
 ----------------------------------------------------------
| MAC_HEADER | IP_HEADER | GRE_HEADER | L2_Mirrored_Packet |
 ----------------------------------------------------------
```

{{%notice note%}}

- Mirrored traffic is not guaranteed. If the MTP is congested, mirrored packets might be discarded.
- A SPAN and ERSPAN destination interface that is oversubscribed might result in data plane buffer depletion and buffer drops. Exercise caution when enabling SPAN and ERSPAN when the aggregate speeds of all source ports exceeds the destination port. Selective SPAN is recommended when possible to limit traffic in this scenario.

{{%/notice%}}

SPAN and ERSPAN are configured via `cl-acltool`, the [same utility for security ACL configuration](../../System-Configuration/Netfilter-ACLs/). The match criteria for SPAN and ERSPAN is usually an interface; for more granular match terms, use [selective spanning](#selective-spanning). The SPAN source interface can be a port, a subinterface, or a bond interface. Ingress traffic on interfaces can be matched, and on switches with [Spectrum ASICs](https://cumulusnetworks.com/products/hardware-compatibility-list/?asic%5B0%5D=Mellanox%20Spectrum&asic%5B1%5D=Mellanox%20Spectrum_A1), egress traffic can be matched. See the [list of limitations](#limitations-for-span-and-erspan) below.

Cumulus Linux supports a maximum of two SPAN destinations. Multiple rules (SPAN sources) can point to the same SPAN destination, although a given SPAN source cannot specify two SPAN destinations. The SPAN destination (MTP) interface can be a physical port, a subinterface, or a bond interface. The SPAN and ERSPAN action is independent of security ACL actions. If packets match both a security ACL rule and a SPAN rule, both actions are carried out.

{{%notice note%}}

Always place your rules files under `/etc/cumulus/acl/policy.d/`.

{{%/notice%}}

### Limitations for SPAN and ERSPAN

- For Broadcom switches, Cumulus Linux supports a maximum of two SPAN destinations.
- Because SPAN and ERSPAN is done in hardware, eth0 is not supported as a  destination.
- For Mellanox Spectrum switches, Cumulus Linux supports only a single SPAN destination in atomic mode or three SPAN destinations in non-atomic mode.
- Multiple rules (SPAN sources) can point to the same SPAN destination, but a given SPAN source *cannot* specify two SPAN destinations.
- To configure SPAN or ERSPAN on a Tomahawk or Trident3 switch, you must enable [non-atomic update  mode](../../System-Configuration/Netfilter-ACLs#nonatomic-update-mode-and-atomic-update-mode).
- Mellanox Spectrum switches reject SPAN ACL rules for an output interface that is a subinterface.
- Mirrored traffic is not guaranteed. If the MTP is congested, mirrored packets might be discarded.
- Cut-through mode is not supported for ERSPAN in Cumulus Linux on switches using Broadcom Tomahawk, Trident II+ and Trident II ASICs.
- On Broadcom switches, SPAN does not capture egress traffic.
- Cumulus Linux does not support IPv6 ERSPAN destinations.
- ERSPAN does not cause the kernel to send ARP requests to resolve the next hop for the ERSPAN destination. If an ARP entry for the destination/next hop does not already exist in the kernel, you need to manually resolve this before mirrored traffic is sent (using ping or arping).

### Configure SPAN for Switch Ports

This section describes how to set up, install, verify and uninstall SPAN rules. In the examples that follow, you span (mirror) switch port swp4 input traffic and swp4 output traffic to destination switch port swp19.

First, create a rules file in `/etc/cumulus/acl/policy.d/`:

```
cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/span.rules
[iptables]
-A FORWARD --in-interface swp4 -j SPAN --dport swp19
-A FORWARD --out-interface swp4 -j SPAN --dport swp19
EOF'
```

{{%notice note%}}

Using `cl-acltool` with the `--out-interface` rule applies to transit traffic only; it does not apply to traffic sourced from the switch.

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
    15  5205 SETCLASS   udp  --  swp+   any     anywhere             anywhere             udp  dpts:bootps:bootpc SETCLASS  class:2
    11  3865 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:bootps POLICE  mode:pkt rate:100 burst:100
     0     0 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:bootpc POLICE  mode:pkt rate:100 burst:100
     0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp dpts:bootps:bootpc SETCLASS  class:2
     0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bootps POLICE  mode:pkt rate:100 burst:100
     0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bootpc POLICE  mode:pkt rate:100 burst:100
    17  1088 SETCLASS   igmp --  swp+   any     anywhere             anywhere             SETCLASS class:6
    17  1156 POLICE     igmp --  any    any     anywhere             anywhere             POLICE  mode:pkt rate:300 burst:100
    394 41060 POLICE    all  --  swp+   any     anywhere             anywhere             ADDRTYPE match dst-type LOCAL POLICE  mode:pkt rate:1000 burst:1000 class:0
     0     0 POLICE     all  --  swp+   any     anywhere             anywhere             ADDRTYPE match dst-type IPROUTER POLICE  mode:pkt rate:400 burst:100 class:0
    988  279K SETCLASS  all  --  swp+   any      anywhere            anywhere             SETCLASS  class:0

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
  pkts bytes target     prot opt in     out     source               destination
     0     0 DROP       all  --  swp+   any     240.0.0.0/5          anywhere
     0     0 DROP       all  --  swp+   any     loopback/8           anywhere
     0     0 DROP       all  --  swp+   any     base-address.mcast.net/8  anywhere
     0     0 DROP       all  --  swp+   any     255.255.255.255      anywhere
 26864 4672K SPAN       all  --  swp4   any     anywhere             anywhere             dport:swp19  <---- input packets on swp4

40722   47M  SPAN       all  --  any    swp4     anywhere             anywhere             dport:swp19  <---- output packets on swp4

Chain OUTPUT (policy ACCEPT 67398 packets, 5757K bytes)
  pkts bytes target     prot opt in     out     source               destination
```

Install the rules:

```
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
```

{{%notice warning%}}

Running the following command is incorrect and will remove **all** existing control-plane rules or other installed rules and only install the rules defined in `span.rules`:

```
cumulus@switch:~$ sudo cl-acltool -i  -P /etc/cumulus/acl/policy.d/span.rules
```

{{%/notice%}}

Verify that the SPAN rules are installed:

```
cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
38025 7034K SPAN       all  --  swp4   any     anywhere             anywhere             dport:swp19
50832   55M SPAN       all  --  any    swp4    anywhere             anywhere             dport:swp19
```

### SPAN Sessions that Reference an Outgoing Interface

SPAN sessions that reference an outgoing interface create the mirrored packets based on the ingress interface before the routing/switching decision. For example, the following rule captures traffic that is ultimately destined to leave swp2 but mirrors the packets when they arrive on swp3. The rule transmits packets that reference the original VLAN tag and source/destination MAC address at the time the packet is originally received on swp3.

```
-A FORWARD --out-interface swp2 -j SPAN --dport swp1
```

### Configure SPAN for Bonds

This section describes how to configure SPAN for all packets going out of `bond0` locally to `bond1`.

First, create a rules file in `/etc/cumulus/acl/policy.d/`:

```
cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/span_bond.rules 
[iptables]
-A FORWARD --out-interface bond0 -j SPAN --dport bond1
EOF'
```

{{%notice note%}}

Using `cl-acltool` with the `--out-interface` rule applies to transit traffic only; it does not apply to traffic sourced from the switch.

{{%/notice%}}

Install the rules:

```
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
```

Verify that the SPAN rules are installed:

```
cumulus@switch:~$ sudo iptables -L -v | grep SPAN
    19  1938 SPAN       all  --  any    bond0   anywhere             anywhere             dport:bond1
```

### Configure ERSPAN

This section describes how to configure ERSPAN for all packets coming in from `swp1` to 12.0.0.2.

{{%notice note%}}

[Cut-through mode](../../Layer-1-and-Switch-Ports/Buffer-and-Queue-Management/#configure-cut-through-mode-and-store-and-forward-switching) is **not** supported for ERSPAN in Cumulus Linux on switches using Broadcom Tomahawk, Trident II+, and Trident II ASICs.

Cut-through mode **is** supported for ERSPAN in Cumulus Linux on switches using Mellanox Spectrum ASICs.

{{%/notice%}}

1. First, create a rules file in `/etc/cumulus/acl/policy.d/`:

```
cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/erspan.rules
[iptables]
-A FORWARD --in-interface swp1 -j ERSPAN --src-ip 12.0.0.1 --dst-ip 12.0.0.2  --ttl 64
EOF'
```

2. Install the rules:

```
cumulus@switch:~$ sudo cl-acltool -i
Reading rule file /etc/cumulus/acl/policy.d/00control_plane.rules ...
Processing rules in file /etc/cumulus/acl/policy.d/00control_plane.rules ...
Reading rule file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
Processing rules in file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
Reading rule file /etc/cumulus/acl/policy.d/erspan.rules ...
Processing rules in file /etc/cumulus/acl/policy.d/erspan.rules ...
Installing acl policy
done.
```

3. Verify that the ERSPAN rules are installed:

```
cumulus@switch:~$ sudo iptables -L -v | grep SPAN
    69  6804 ERSPAN     all  --  swp1   any     anywhere             anywhere             ERSPAN src-ip:12.0.0.1 dst-ip:12.0.0.2
```

The `src-ip` option can be any IP address, whether it exists in the routing table or not. The `dst-ip` option must be an IP address reachable via the routing table. The destination IP address must be reachable from a front-panel port, and not the management port. Use `ping` or `ip route get <ip>` to verify that the destination IP address is reachable. Setting the `--ttl` option is recommended.

{{%notice tip%}}

If a SPAN destination IP address is not available, or if the interface type or types prevent using a laptop as a SPAN destination, read this [knowledge base article](https://support.cumulusnetworks.com/hc/en-us/articles/360040711774) for a workaround.

{{%/notice%}}

#### ERSPAN and Wireshark

- When using [Wireshark](https://www.wireshark.org) to review the ERSPAN output, Wireshark may report the message "Unknown version, please report or test to use fake ERSPAN preference", and the trace is unreadable. To resolve this, go into the General preferences for Wireshark, then go to **Protocols** \> **ERSPAN** and check the **Force to decode fake ERSPAN frame** option.
- To set up a [capture filter](https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html) on the destination switch that filters for a specific IP protocol, use `ip.proto == 49` to filter for GRE-encapsulated (IP protocol 49) traffic.

### Selective Spanning

SPAN and ERSPAN traffic rules can be configured to limit the traffic that is spanned, to reduce the volume of copied data.

{{%notice note%}}

Cumulus Linux supports selective spanning for `iptables` only. `ip6tables` and `ebtables` are not supported.

{{%/notice%}}

The following matching fields are supported:

- IPv4 SIP/DIP
- IP protocol
- L4 (TCP/UDP) src/dst port
- TCP flags
- An ingress port/wildcard (swp+) can be specified in addition

{{%notice note%}}

With ERSPAN, a maximum of two `--src-ip --dst-ip` pairs are supported. Exceeding this limit produces an error when you install the rules with `cl-acltool`.

{{%/notice%}}

#### SPAN Examples

To mirror forwarded packets from all ports matching SIP 20.0.1.0 and DIP 20.0.1.2 to port swp1s1:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -d 20.0.1.2 -j SPAN --dport swp1s2
```

To mirror icmp packets from all ports to swp1s2:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -p icmp -j SPAN --dport swp1s2
```

To mirror forwarded UDP packets received from port swp1s0, towards DIP 20.0.1.2 and destination port 53:

```
-A FORWARD --in-interface swp1s0 -d 20.0.1.2 -p udp --dport 53 -j SPAN --dport swp1s2
```
  
To mirror all forwarded TCP packets with only SYN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL SYN -j SPAN --dport swp1s2
```

To mirror all forwarded TCP packets with only FIN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL FIN -j SPAN --dport swp1s2
```

#### ERSPAN Examples

To mirror forwarded packets from all ports matching SIP 20.0.1.0 and DIP 20.0.1.2:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -d 20.0.1.2 -j ERSPAN --src-ip 90.0.0.1 --dst-ip 20.0.2.2
```

To mirror ICMP packets from all ports:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -p icmp -j ERSPAN --src-ip 90.0.0.1 --dst-ip 20.0.2.2
```

To mirror forwarded UDP packets received from port swp1s0, towards DIP 20.0.1.2 and destination port 53:

```
-A FORWARD --in-interface swp1s0 -d 20.0.1.2 -p udp --dport 53 -j ERSPAN --src-ip 90.0.0.1 --dst-ip 20.0.2.2
```

To mirror all forwarded TCP packets with only SYN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL SYN -j ERSPAN --src-ip 90.0.0.1 --dst-ip 20.0.2.2
```

To mirror all forwarded TCP packets with only FIN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL FIN -j ERSPAN --src-ip 90.0.0.1 --dst-ip 20.0.2.2
```

### Remove SPAN Rules

To remove your SPAN rules, run:

```
#Remove rules file:
cumulus@switch:~$ sudo rm  /etc/cumulus/acl/policy.d/span.rules
#Reload the default rules
cumulus@switch:~$ sudo cl-acltool -i
cumulus@switch:~$
```

To verify that the SPAN rules were removed:

```
cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
cumulus@switch:~$
```

### Monitor Control Plane Traffic with tcpdump

You can use `tcpdump` to monitor control plane traffic - traffic sent to and coming from the switch CPUs. `tcpdump` does **not** monitor data plane traffic; use `cl-acltool` instead (see above).

For more information on tcpdump, read [the `tcpdump` documentation](http://www.tcpdump.org/#documentation) and the [`tcpdump` man page](http://www.tcpdump.org/manpages/tcpdump.1.html).

The following example incorporates a few `tcpdump` options:

- `-i bond0`, which captures packets from bond0 to the CPU and from the CPU to bond0
- `host 169.254.0.2`, which filters for this IP address
- `-c 10`, which captures 10 packets then stops

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

## Related Information

- [en.wikipedia.org/wiki/Ping](http://en.wikipedia.org/wiki/Ping)
- [en.wikipedia.org/wiki/Traceroute](https://en.wikipedia.org/wiki/Traceroute)
- [www.tcpdump.org](http://www.tcpdump.org)
