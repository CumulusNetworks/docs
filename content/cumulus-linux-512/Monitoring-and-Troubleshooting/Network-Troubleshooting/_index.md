---
title: Network Troubleshooting
author: NVIDIA
weight: 1110
toc: 3
---
Cumulus Linux includes command line and analytical tools to help you troubleshoot issues with your network.

## Check if a Host is Reachable with ping

Use `ping` to check that a host is reachable. `ping` also calculates the time it takes for packets to travel round trip. See `man ping` for details.

Use the ping tool to check that a destination on a network is reachable. Ping sends <span class="a-tooltip">[ICMP](## "Internet Control Message Protocol")</span> Echo Request packets to the specified address and listens for Echo Reply packets.  

You send Echo Request packets to a destination (IP address or a hostname) to check if it is reachable. In addition, you can specify the following options:
- The number of Echo Request packets to send. You can specify a value between 1 and 10. The default packet count is 3.
- How often two send Echo Request packets. You can specify a value between 0.1 and 5 seconds???. The default value is ???.
- The packet size in bytes. You can specify a value between 1 and 9216. The default value is ???
- The number of seconds to wait for an Echo Reply packet before the ping request times out. You can specify a value between 0.1 and 10. The default value is ???.
- The source IP address from which to send the Echo Request packets.
- Do not fragment. If the packet is larger than the maximum transmission unit (MTU) of any network segment it traverses, drop the packet instead of fragmenting the packet.
- The layer 3 protocol you want to use to send the Echo Request packets. You can specify IPv4 or IPv6.
- The VRF for which you want to test the routing paths.
- A source interface for which you want to test the routing path for a link local address. IPv6 only.

{{< tabs "TabID26 ">}}
{{< tab "NVUE Commands ">}}

The following example checks if destination 10.10.10.10 is reachable on the network.

```
cumulus@switch:~$ nv action ping system 10.10.10.10
```

The following example sends 5 Echo Request packets to check if destination 10.10.10.10 is reachable on the network.

```
cumulus@switch:~$ nv action ping system 10.10.10.10 count 5
```

The following example sends Echo Request packets every two seconds to check if destination 10.10.10.10 is reachable on the network.

```
cumulus@switch:~$ nv action ping system 10.10.10.10 interval 2
```

The following example sends 50-byte Echo Request packets to check if destination 10.10.10.10 is reachable on the network.

```
cumulus@switch:~$ nv action ping system 10.10.10.10 size 200
```

The following example checks if destination 10.10.10.10 is reachable on the network and waits for 3 seconds for an Echo Reply packet before timing out.

```
cumulus@switch:~$ nv action ping system 10.10.10.10 time 3
```

The following example checks if destination 10.10.10.10 is reachable on the network and sets the `do not fragment` bit.

```
cumulus@switch:~$ nv action ping system 10.10.10.10 do-not-fragment
```

The following example sends Echo Request packets to destination 10.10.10.10 from the source IP address 10.10.5.1.

```
cumulus@switch:~$ nv action ping system 10.10.10.10 source 10.10.5.1
```

The following example sends Echo Request packets to destination 10.10.10.10 for the management VRF.

```
cumulus@switch:~$ nv action ping system 10.10.10.10 vrf mgmt
```

The following example sends Echo Request packets to destination 10.10.10.10 for IPv4.

```
cumulus@switch:~$ nv action ping system 10.10.10.10 l3protocol ipv4 
```

The following example sends Echo Request packets from source interface eth0.

```
cumulus@switch:~$ nv action ping system fe80::a00:27ff:fe00:0 source-interface eth0 
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

The following example checks if destination 10.10.10.10 is reachable on the network.

```
cumulus@switch:~$ ping 10.10.10.10
```

The following example sends 5 Echo Request packets to check if destination 10.10.10.10 is reachable on the network.

```
cumulus@switch:~$ ping -c 5 10.10.10.10
```

The following example sends Echo Request packets every two seconds to check if destination 10.10.10.10 is reachable on the network.

```
cumulus@switch:~$ ping -i 2 10.10.10.10
```

The following example sends 50-byte Echo Request packets to check if destination 10.10.10.10 is reachable on the network.

```
cumulus@switch:~$ ping -s 50 10.10.10.10
```

The following example checks if destination 10.10.10.10 is reachable and waits for 3 seconds for an Echo Reply packet before the ping request times out.

```
cumulus@switch:~$ ping -W 10.10.10.10
```

The following example checks if destination 10.10.10.10 is reachable and sets the `do not fragment` bit for IPv4.

```
cumulus@switch:~$ ping –4 -M do 10.10.10.10
```

The following example sends Echo Request packets to destination 10.10.10.10 from the source IP address 10.10.5.1.

```
cumulus@switch:~$ ping system -1 10.10.5.1 10.10.10.10
```

The following example sends Echo Request packets to destination 10.10.10.10 for the management VRF.

```
cumulus@switch:~$ ping vrf mgmt 10.10.10.10
```

The following example sends Echo Request packets to destination 10.10.10.10 for IPv4.

```
cumulus@switch:~$ ping -1 ipv4 10.10.10.10
```

The following example sends Echo Request packets to destination fe80::a00:27ff:fe00:0 from source interface eth0.

```
cumulus@switch:~$ ping -5 fe80::a00:27ff:fe00:0%eth0 
```

{{< /tab >}}
{{< /tabs >}}

When troubleshooting intermittent connectivity issues, it is helpful to send continuous pings to a host.

## Print Route Trace with traceroute

Use the traceroute tool for network troubleshooting, identifying routing issues, measuring latency, mapping network paths, detecting performance bottlenecks, and diagnosing connectivity problems.

You send traceroute packets to a destination to which you want to trace the route. You can specify either an IP address or a domain name. In addition, you can specify the following options:
- The hop count (the maximum number of hops). You can specify a value between 1 and 255.
- The traceroute packet size in bytes. You can specify a value between 28 and 65000 bytes.
- The source IP address to use for sending the `traceroute` packets.
- The layer 4 protocol packets to send. You can specify ICMP, TCP, or UDP.

{{< tabs "TabID167 ">}}
{{< tab "NVUE Commands ">}}

The following example validates the path to destination 10.10.10.10.

```
cumulus@switch:~$ nv action traceroute interface 10.10.10.10
```

The following example sends 50-byte packets to validate the path to destination 10.10.10.10.

```
cumulus@switch:~$ nv action traceroute interface 10.10.10.10 packet_len 50 
```

The following example validates the path to destination 10.10.10.10 with 4 maximum hops.

```
cumulus@switch:~$ nv action traceroute interface 10.10.10.10  hop-count 4
```

The following example validates the path to destination 10.10.10.10 from the source IP address 10.10.5.1

```
cumulus@switch:~$ nv action traceroute interface 10.10.10.10 source-address 10.10.5.1
```

The following example sends UDP packets to validate the path to destination 10.10.10.10:

```
cumulus@switch:~$ nv action traceroute interface 10.10.10.10 protocol udp
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

The following example validates the path to destination 10.10.10.10.

```
cumulus@switch:~$ traceroute 10.10.10.10
```

The following example sends 50-byte packets to validate the path to destination 10.10.10.10.

```
cumulus@switch:~$ traceroute 10.10.10.10 packet_len 50
```

The following example validates the path to destination 10.10.10.10 with 4 maximum hops.

```
cumulus@switch:~$ traceroute 10.10.10.10 -m 4
```

The following example validates the path to destination 10.10.10.10 from the source IP address 10.10.5.1

```
cumulus@switch:~$ traceroute 10.10.10.10 -s 10.10.5.1
```

The following example sends UDP packets to validate the path to destination 10.10.10.10:

```
cumulus@switch:~$ traceroute 10.10.10.10 -U
```

To send TCP packets, use the -T option. To send ICMP packets, use the -I option.

{{< /tab >}}
{{< /tabs >}}
<!-- vale off -->

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
