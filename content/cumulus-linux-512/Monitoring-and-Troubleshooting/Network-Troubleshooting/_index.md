---
title: Network Troubleshooting
author: NVIDIA
weight: 1110
toc: 3
---
Cumulus Linux includes command line and analytical tools to help you troubleshoot issues with your network.

## ping

Use the ping tool to check that a destination on a network is reachable. Ping sends <span class="a-tooltip">[ICMP](## "Internet Control Message Protocol")</span> Echo Request packets to the specified destination and listens for Echo Reply packets.  

{{< tabs "TabID26 ">}}
{{< tab "NVUE Commands ">}}

You send Echo Request packets to a destination (IP address or a hostname) to check if it is reachable. You can specify the following options:

| Option       | Description |
| ------------ | ------------ |
| `count` | The number of Echo Request packets to send. You can specify a value between 1 and 10. The default packet count is 3. |
| `interval` | How often to send Echo Request packets. You can specify a value between 0.1 and 5 seconds. The default value is 4. |
| `size` | The Echo Request packet size in bytes. You can specify a value between 1 and 9216. The default value is 64. |
| `time` | The number of seconds to wait for an Echo Reply packet before the ping request times out. You can specify a value between 0.1 and 10. The default value is 10.|
| `source` | The source IP address from which to send the Echo Request packets. |
| `do-not-fragment` | Do not fragment. If the packet is larger than the maximum transmission unit (MTU) of any network segment it traverses, drop the packet instead of fragmenting the packet. |
| `l3protocol` | The layer 3 protocol you want to use to send the Echo Request packets. You can specify IPv4 or IPv6. If you don't specify either IPv4 or IPv6, ping uses IPv4. |
| `vrf` | The VRF you want to use. |
| `source-interface` | The source interface from which to send Echo Request packets for a link local address. IPv6 only.|

The following example sends Echo Request packets to destination 10.10.10.10 to check if it is reachable.

```
cumulus@switch:~$ nv action ping system 10.10.10.10
```

The following example sends Echo Request packets to IPv6 destination fe80::a00:27ff:fe00:0 to check if it is reachable.

```
cumulus@switch:~$ nv action ping system fe80::a00:27ff:fe00:0 l3protocol ipv6
```

The following example sends 5 Echo Request packets every 2 seconds to check if destination 10.10.10.10 is reachable and waits for 3 seconds for an Echo Reply packet before timing out.

```
cumulus@switch:~$ nv action ping system 10.10.10.10 count 5 interval 2 time 3
```

The following example sends 50-byte Echo Request packets to check if destination 10.10.10.10 is reachable.

```
cumulus@switch:~$ nv action ping system 10.10.10.10 size 50
```

The following example checks if destination 10.10.10.10 is reachable and drops the packet instead of fragmenting it if the packet is larger than the maximum transmission unit (MTU) of any network segment it traverses.

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

The following example sends Echo Request packets to destination fe80::a00:27ff:fe00:0 from source interface eth0.

```
cumulus@switch:~$ nv action ping system fe80::a00:27ff:fe00:0 source-interface eth0 
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You send Echo Request packets to a destination (IP address or a hostname) to check if it is reachable. In addition, you can specify the following options:

| Option       | Description |
| ------------ | ------------ |
| `-c` | The number of Echo Request packets to send. You can specify a value between 1 and 10. The default packet count is 3.|
| `-i` | How often two send Echo Request packets. You can specify a value between 0.1 and 5 seconds. The default value is 4. |
| `-s` | The packet size in bytes. You can specify a value between 1 and 9216. The default value is 64. |
| `-W` | The number of seconds to wait for an Echo Reply packet before the ping request times out. You can specify a value between 0.1 and 10. The default value is 10.|
| `-I <ip-address>` | The source IP address from which to send the Echo Request packets. |
| `M do` | Do not fragment. If the packet is larger than the maximum transmission unit (MTU) of any network segment it traverses, drop the packet instead of fragmenting the packet. |
| `<l3protocol>` | The layer 3 protocol you want to use to send the Echo Request packets. You can specify `-4` for IPv4 or `-6` for IPv6. If you don't specify either IPv4 or IPv6, ping uses IPv4.|
| `-I <vrf-name>` | The VRF you want to use. |
| `-6 <ipv6-address>%<interface>` | The source interface from which to send Echo Request packets for a link local address. IPv6 only. |

The following example checks if destination 10.10.10.10 is reachable on the network.

```
cumulus@switch:~$ ping 10.10.10.10
```

The following example sends Echo Request packets to destination fe80::a00:27ff:fe00:0 for IPv6.

```
cumulus@switch:~$ ping -6 fe80::a00:27ff:fe00:0
```

The following example sends 5 Echo Request packets every two seconds to check if destination 10.10.10.10 is reachable on the network and waits for 3 seconds for an Echo Reply packet before timing out.

```
cumulus@switch:~$ ping -c 5 -i 2 -W 3 10.10.10.10
```

The following example sends 50-byte Echo Request packets to check if destination 10.10.10.10 is reachable on the network.

```
cumulus@switch:~$ ping -s 50 10.10.10.10
```

The following example checks if destination 10.10.10.10 is reachable and sets the `do not fragment` bit for IPv4.

```
cumulus@switch:~$ ping -M do 10.10.10.10
```

The following example sends Echo Request packets to destination 10.10.10.10 from the source IP address 10.10.5.1 for the management VRF.

```
cumulus@switch:~$ ping -I vrf mgmt 10.10.5.1 10.10.10.10 
```

The following example sends Echo Request packets to destination 10.10.10.10 for the management VRF.

```
cumulus@switch:~$ ping 10.10.10.10 vrf mgmt
```

The following example sends Echo Request packets to destination fe80::a00:27ff:fe00:0 from source interface eth0.

```
cumulus@switch:~$ ping -6 fe80::a00:27ff:fe00:0%eth0 
```

{{< /tab >}}
{{< /tabs >}}

## traceroute

The traceroute tool traces the path of data packets from a source to a destination across an IP network, showing the sequence of routers (hops) the data passes through.  

By measuring the round-trip time for each hop, traceroute helps identify latency problems, routing inefficiencies, or potential network failures, enabling you to troubleshoot and optimize network performance.

{{< tabs "TabID167 ">}}
{{< tab "NVUE Commands ">}}

You send traceroute packets to a destination with the `nv action traceroute system <destination>` command. The destination can be either an IP address or a domain name. You can specify the following options:

| Option | Description |
| ------ | ----------- |
| `max-ttl` | The maximum number of hops to reach the destination. You can specify a value between 1 and 30. The default is 30. |
| `initial-ttl` | The minimum number of hops to reach the destination. You can specify a value between 1 and 30. The default is 1. The minimum number of hops must be less than or equal to the maximum number of hops. |
| `wait` | The maximum number of nanoseconds to wait for a response from each hop. You can specify a value between 0.1 and 10. The maximum number of hops must be more than or equal to the minimum number of hops.|
| `vrf` | The VRF to use. |
| `source` | The source IP address from which the route originates. |
| `l3protocol` | The layer 3 protocol; `ipv4` or `ipv6`. The default is `ipv4`.|
| `l4protocol` | The layer 4 protocol; `icmp`, `tcp`, or `udp`. The default is `icmp`.|
| `do-not-fragment` | Do not fragment. Trace the route to the destination without fragmentation. |

The following example validates the route path to IPv4 destination 10.10.10.10.

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10
```

The following example validates the route path to IPv6 destination fe80::a00:27ff:fe00:0.

```
cumulus@switch:~$ nv action traceroute system fe80::a00:27ff:fe00:0 ipv6
```

The following example validates the path to destination 10.10.10.10 with 5 minimum hops and 10 maximum hops.

```
cumulus@switch:~$ nv action traceroute system 127.0.0.1 initial-ttl 5 max-ttl 10
```

The following example sends UDP packets to validate the path to destination 10.10.10.10 and waits 2 nanoseconds for a response.

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10 l4protocol udp wait 2
```

The following example validates the path to destination 10.10.10.10 from the source IP address 10.10.5.1.

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10 source 10.10.5.1
```

The following example validates the path to destination 10.10.10.10 from the source IP address 10.10.5.1 in VRF RED.

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10 source 10.10.5.1 vrf RED 
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You send traceroute packets to a destination with the `traceroute ` command. The destination can be either an IP address or a domain name. You can specify the following options:

| Option | Description |
| ------ | ----------- |
| `-m` | The maximum number of hops to reach the destination. You can specify a value between 1 and 30. The default is 30. |
| `-s` | The source IP address from which the route originates.|
| `-f` |The minimum number of hops to reach the destination. You can specify a value between 1 and 30. The default is 1. The minimum number of hops must be less than or equal to the maximum number of hops.|
| `-w` | The maximum number of nanoseconds to wait for a response from each hop. You can specify a value between 0.1 and 10.|
| `-i` | The VRF to use. |
| `<layer3-protocol>` | The layer 3 protocol; `-4` for IPv4 or `-6` for IPv6. The default is IPv4.|
| `<layer4-protocol>` | The layer 4 protocol packets to send; `-I` for ICMP, `-T` for TCP, or `-U` for UDP.|
| `-F` | Do not fragment. Trace the route to the destination without fragmentation. |

The following example validates the route path to IPv4 destination 10.10.10.10.

```
cumulus@switch:~$ traceroute 10.10.10.10
```

The following example validates the route path to IPv6 destination fe80::a00:27ff:fe00:0.

```
cumulus@switch:~$ traceroute fe80::a00:27ff:fe00:0 -6
```

The following example validates the path to destination 10.10.10.10 with 5 minimum hops and 10 maximum hops.

```
cumulus@switch:~$ traceroute 10.10.10.10 -f 5 -m 10
```

The following example sends UDP packets to validate the path to destination 10.10.10.10 and waits 2 nanoseconds for a response.

```
cumulus@switch:~$ traceroute 10.10.10.10 -U -w 2
```

The following example validates the path to destination 10.10.10.10 from the source IP address 10.10.5.1.

```
cumulus@switch:~$ traceroute 10.10.10.10 -s 10.10.5.1
```

The following example validates the path to destination 10.10.10.10 from the source IP address 10.10.5.1 in VRF RED.

```
cumulus@switch:~$ traceroute 10.10.10.10 -s 10.10.5.1 -i RED
```

{{< /tab >}}
{{< /tabs >}}

## tcpdump

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
