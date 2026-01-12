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

Send Echo Request packets to a destination (IP address or a hostname) to check if it is reachable. You can specify the following options:

| Option       | Description |
| ------------ | ------------ |
| `count` | The number of Echo Request packets to send. You can specify a value between 1 and 10. The default packet count is 3. |
| `interval` | How often to send Echo Request packets. You can specify a value between 0.1 and 5 seconds. The default value is 4. |
| `size` | The Echo Request packet size in bytes. You can specify a value between 1 and 9216. The default value is 64. |
| `wait` | The number of seconds to wait for an Echo Reply packet before the ping request times out. You can specify a value between 0.1 and 10. The default value is 10.|
| `source` | The source IP address from which to send the Echo Request packets. |
| `source-interface` | The source interface from which to send the Echo Request packets. |
| `do-not-fragment` | Do not fragment. If the packet is larger than the maximum transmission unit (MTU) of any network segment it traverses, drop the packet instead of fragmenting the packet. |
| `l3protocol` | The layer 3 protocol you want to use to send the Echo Request packets. You can specify IPv4 or IPv6. If you don't specify either IPv4 or IPv6, ping uses IPv4. |
| `vrf` | The VRF you want to use. |
| `source-interface` | The source interface from which to send Echo Request packets for a link-local address. IPv6 only.|

The following example sends Echo Request packets to destination 10.10.10.2 to check if it is reachable.

```
cumulus@switch:~$ nv action ping system 10.10.10.2
Action executing ...
{
    "sent": 3,
    "received": 3,
    "min_time": 602000,
    "avg_time": 790000,
    "max_time": 1090000,
    "packets_info": {
        "1": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 1090000
        },
        "2": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 680000
        },
        "3": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 602000
        }
    }
}
Action succeeded
```

The following example sends Echo Request packets to IPv6 destination fe80::4ab0:2dff:fee4:e069 to check if it is reachable.

```
cumulus@switch:~$ nv action ping system fe80::4ab0:2dff:fee4:e069 l3protocol ipv6
Action executing ...
{
    "sent": 3,
    "received": 3,
    "min_time": 58000,
    "avg_time": 87000,
    "max_time": 141000,
    "packets_info": {
        "1": {
            "bytes": 64,
            "source": "fe80::4ab0:2dff:fee4:e069%peerlink.4094",
            "ttl": 64,
            "time": 141000
        },
        "2": {
            "bytes": 64,
            "source": "fe80::4ab0:2dff:fee4:e069%peerlink.4094",
            "ttl": 64,
            "time": 58000
        },
        "3": {
            "bytes": 64,
            "source": "fe80::4ab0:2dff:fee4:e069%peerlink.4094",
            "ttl": 64,
            "time": 63000
        }
    }
}
Action succeeded
```

The following example sends 5 Echo Request packets every 2 seconds to check if destination 10.10.10.2 is reachable and waits for 3 seconds for an Echo Reply packet before timing out.

```
cumulus@switch:~$ nv action ping system 10.10.10.2 count 5 interval 2 wait 3
Action executing ...
{
    "sent": 5,
    "received": 5,
    "min_time": 569000,
    "avg_time": 647000,
    "max_time": 801000,
    "packets_info": {
        "1": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 660000
        },
        "2": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 625000
        },
        "3": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 569000
        },
        "4": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 801000
        },
        "5": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 580000
        }
    }
}
Action succeeded
```

The following example sends 50-byte Echo Request packets to check if destination 10.10.10.2 is reachable.

```
cumulus@switch:~$ nv action ping system 10.10.10.2 size 50
Action executing ...
{
    "sent": 3,
    "received": 3,
    "min_time": 610000,
    "avg_time": 845000,
    "max_time": 1008000,
    "packets_info": {
        "1": {
            "bytes": 58,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 610000
        },
        "2": {
            "bytes": 58,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 917000
        },
        "3": {
            "bytes": 58,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 1010000
        }
    }
}
Action succeeded
```

The following example checks if destination 10.10.10.2 is reachable and drops the packet instead of fragmenting it if the packet is larger than the maximum transmission unit (MTU) of any network segment it traverses.

```
cumulus@switch:~$ nv action ping system 10.10.10.2 do-not-fragment
Action executing ...
{
    "sent": 3,
    "received": 3,
    "min_time": 651000,
    "avg_time": 827000,
    "max_time": 1071000,
    "packets_info": {
        "1": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 1070000
        },
        "2": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 651000
        },
        "3": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 761000
        }
    }
}
Action succeeded
```

The following example sends Echo Request packets to destination 10.10.10.2 from the source IP address 10.10.10.1

```
cumulus@switch:~$ nv action ping system 10.10.10.2 source 10.10.10.1
Action executing ...
{
    "sent": 3,
    "received": 3,
    "min_time": 434000,
    "avg_time": 574000,
    "max_time": 812000,
    "packets_info": {
        "1": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 812000
        },
        "2": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 478000
        },
        "3": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 434000
        }
    }
}
Action succeeded
```

The following example sends Echo Request packets to destination 10.10.10.2 from the source IP address 10.10.10.1 in the management VRF:

```
cumulus@switch:~$ nv action ping system 10.10.10.2 source 10.10.10.1 vrf mgmt
Action executing ...
{
    "sent": 3,
    "received": 3,
    "min_time": 617000,
    "avg_time": 695000,
    "max_time": 837000,
    "packets_info": {
        "1": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 617000
        },
        "2": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 837000
        },
        "3": {
            "bytes": 64,
            "source": "10.10.10.2",
            "ttl": 64,
            "time": 631000
        }
    }
}
Action succeeded
```

The following example sends Echo Request packets to destination fe80::4638:39ff:fe00:5a from source interface bond1.

```
cumulus@switch:~$ nv action ping system fe80::4638:39ff:fe00:5a source-interface bond1
nv action ping system fe80::4638:39ff:fe00:5a source-interface bond1
Error: Action failed with the following issue:

3 packets transmitted, 0 received, 100% packet loss, time 2056ms
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
| `-I <vrf-id>` | The VRF you want to use. |
| `-6 <ipv6-address>%<interface-id>` | The source interface from which to send Echo Request packets for a link-local address. IPv6 only. |

The following example checks if destination 10.10.10.2 is reachable on the network.

```
cumulus@switch:~$ ping 10.10.10.2
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
PING 10.10.10.2 (10.10.10.2) 56(84) bytes of data.
64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=0.719 ms
64 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.711 ms
64 bytes from 10.10.10.2: icmp_seq=3 ttl=64 time=0.710 ms
64 bytes from 10.10.10.2: icmp_seq=4 ttl=64 time=0.607 ms
64 bytes from 10.10.10.2: icmp_seq=5 ttl=64 time=0.882 ms
64 bytes from 10.10.10.2: icmp_seq=6 ttl=64 time=0.808 ms
64 bytes from 10.10.10.2: icmp_seq=7 ttl=64 time=0.833 ms
64 bytes from 10.10.10.2: icmp_seq=8 ttl=64 time=0.680 ms
64 bytes from 10.10.10.2: icmp_seq=9 ttl=64 time=0.790 ms
...
```

The following example sends Echo Request packets to destination fe80::4ab0:2dff:fee4:e069 for IPv6.

```
cumulus@switch:~$ ping -6 fe80::4ab0:2dff:fee4:e069
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
PING fe80::4ab0:2dff:fee4:e069(fe80::4ab0:2dff:fee4:e069) 56 data bytes
64 bytes from fe80::4ab0:2dff:fee4:e069%peerlink.4094: icmp_seq=1 ttl=64 time=0.067 ms
64 bytes from fe80::4ab0:2dff:fee4:e069%peerlink.4094: icmp_seq=2 ttl=64 time=0.058 ms
64 bytes from fe80::4ab0:2dff:fee4:e069%peerlink.4094: icmp_seq=3 ttl=64 time=0.029 ms
64 bytes from fe80::4ab0:2dff:fee4:e069%peerlink.4094: icmp_seq=4 ttl=64 time=0.061 ms
64 bytes from fe80::4ab0:2dff:fee4:e069%peerlink.4094: icmp_seq=5 ttl=64 time=0.038 ms
...
```

The following example sends 5 Echo Request packets every two seconds to check if destination 10.10.10.2 is reachable on the network and waits for 3 seconds for an Echo Reply packet before timing out.

```
cumulus@switch:~$ ping -c 5 -i 2 -W 3 10.10.10.2
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
PING 10.10.10.2 (10.10.10.2) 56(84) bytes of data.
64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=0.901 ms
64 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.833 ms
64 bytes from 10.10.10.2: icmp_seq=3 ttl=64 time=0.834 ms
64 bytes from 10.10.10.2: icmp_seq=4 ttl=64 time=1.06 ms
64 bytes from 10.10.10.2: icmp_seq=5 ttl=64 time=1.08 ms
...
```

The following example sends 50-byte Echo Request packets to check if destination 10.10.10.2 is reachable on the network.

```
cumulus@switch:~$ ping -s 50 10.10.10.2
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
PING 10.10.10.2 (10.10.10.2) 50(78) bytes of data.
58 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=1.04 ms
58 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.748 ms
58 bytes from 10.10.10.2: icmp_seq=3 ttl=64 time=0.782 ms
58 bytes from 10.10.10.2: icmp_seq=4 ttl=64 time=0.683 ms
58 bytes from 10.10.10.2: icmp_seq=5 ttl=64 time=0.951 ms
58 bytes from 10.10.10.2: icmp_seq=6 ttl=64 time=0.646 ms
58 bytes from 10.10.10.2: icmp_seq=7 ttl=64 time=0.809 ms
58 bytes from 10.10.10.2: icmp_seq=8 ttl=64 time=0.672 ms
58 bytes from 10.10.10.2: icmp_seq=9 ttl=64 time=0.640 ms
58 bytes from 10.10.10.2: icmp_seq=10 ttl=64 time=0.679 ms
58 bytes from 10.10.10.2: icmp_seq=11 ttl=64 time=0.667 m
...
```

The following example checks if destination 10.10.10.2 is reachable and sets the `do not fragment` bit for IPv4.

```
cumulus@switch:~$ ping -M do 10.10.10.2
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
PING 10.10.10.2 (10.10.10.2) 56(84) bytes of data.
64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=0.722 ms
64 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.708 ms
64 bytes from 10.10.10.2: icmp_seq=3 ttl=64 time=0.633 ms
64 bytes from 10.10.10.2: icmp_seq=4 ttl=64 time=1.11 ms
64 bytes from 10.10.10.2: icmp_seq=5 ttl=64 time=0.519 ms
64 bytes from 10.10.10.2: icmp_seq=6 ttl=64 time=1.04 ms
64 bytes from 10.10.10.2: icmp_seq=7 ttl=64 time=0.716 ms
...
```

The following example sends Echo Request packets to destination 10.10.10.2 from the source IP address 10.10.10.1 for the management VRF.

```
cumulus@switch:~$ ping -I mgmt 10.10.10.1 10.10.10.2
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
PING 10.10.10.2 (10.10.10.2) from 192.168.200.11 mgmt: 56(124) bytes of data.
64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=0.722 ms
64 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.708 ms
64 bytes from 10.10.10.2: icmp_seq=3 ttl=64 time=0.633 ms
64 bytes from 10.10.10.2: icmp_seq=4 ttl=64 time=1.11 ms
64 bytes from 10.10.10.2: icmp_seq=5 ttl=64 time=0.519 ms
64 bytes from 10.10.10.2: icmp_seq=6 ttl=64 time=1.04 ms
64 bytes from 10.10.10.2: icmp_seq=7 ttl=64 time=0.716 ms
...
```

The following example sends Echo Request packets to destination fe80::a00:27ff:fe00:0 from source interface bond1.

```
cumulus@switch:~$  ping -6 fe80::a00:27ff:fe00:0%bond1
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
PING fe80::a00:27ff:fe00:0%bond1(fe80::a00:27ff:fe00:0%bond1)
64 bytes from ::1: icmp_seq=1 ttl=64 time=0.044 ms
64 bytes from ::1: icmp_seq=2 ttl=64 time=0.058 ms
64 bytes from ::1: icmp_seq=3 ttl=64 time=0.292 ms
64 bytes from ::1: icmp_seq=4 ttl=64 time=0.026 ms
64 bytes from ::1: icmp_seq=5 ttl=64 time=0.055 ms
64 bytes from ::1: icmp_seq=6 ttl=64 time=0.056 ms
...
```

{{< /tab >}}
{{< /tabs >}}

## traceroute

The traceroute tool traces the path of data packets from a source to a destination across an IP network, showing the sequence of routers (hops) the data passes through.  

By measuring the round-trip time for each hop, traceroute helps identify latency problems, routing inefficiencies, or potential network failures, enabling you to troubleshoot and optimize network performance.

{{< tabs "TabID167 ">}}
{{< tab "NVUE Commands ">}}

Send traceroute packets to a destination with the `nv action traceroute system <destination>` command. The destination can be either an IP address or a domain name. You can specify the following options:

| Option | Description |
| ------ | ----------- |
| `max-ttl` | The maximum number of hops to reach the destination. You can specify a value between 1 and 30. The default is 30. |
| `initial-ttl` | The minimum number of hops to reach the destination. You can specify a value between 1 and 30. The default is 1. The minimum number of hops must be less than or equal to the maximum number of hops. |
| `wait` | The maximum number of nanoseconds to wait for a response from each hop. You can specify a value between 0.1 and 10. The maximum number of hops must be more than or equal to the minimum number of hops.|
| `vrf` | The VRF to use. |
| `source` | The source IP address from which the route originates. |
| `l3protocol` | The layer 3 protocol to use for the traceroute; `ipv4` or `ipv6`. The default is `ipv4`.|
| `l4protocol` | The layer 4 protocol to use for the traceroute; `icmp`, `tcp`, or `udp`. The default is `icmp`.|
| `do-not-fragment` | Do not fragment. Trace the route to the destination without fragmentation. |

The following example validates the route path to IPv4 destination 10.10.10.2.

```
cumulus@switch:~$ nv action traceroute system 10.10.10.2
Action executing ...
traceroute response 
{
  "destination_name": "10.10.10.2",
  "destination_address": "10.10.10.2",
  "hops": 30,
  "packet_size": 60,
  "trace": {
    "1": {
      "hop": 1,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "2": {
      "hop": 2,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "3": {
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
...
```

The following example validates the route path to IPv6 destination 2001:DB8::1.

```
cumulus@switch:~$ nv action traceroute system 2001:DB8::1 l3protocol ipv6
Action executing ...
traceroute response 
{
  "destination_name": "",
  "destination_address": "",
  "hops": 1,
  "packet_size": 60,
  "trace": {
    "1": {
      "hop": 0,
      "address": "",
      "name": "",
      "rtt": [],
      "state": "DEFAULT"
    }
  }
}
Action succeeded
```

The following example validates the path to destination 10.10.10.2 with 5 minimum hops and 10 maximum hops.

```
cumulus@switch:~$ nv action traceroute system 10.10.10.2 initial-ttl 5 max-ttl 10
Action executing ...
traceroute response 
{
  "destination_name": "10.10.10.2",
  "destination_address": "10.10.10.2",
  "hops": 6,
  "packet_size": 60,
  "trace": {
    "1": {
      "hop": 5,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "2": {
      "hop": 6,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "3": {
      "hop": 7,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
...
```

The following example sends UDP packets to validate the path to destination 10.10.10.2 and waits 2 nanoseconds for a response.

```
cumulus@switch:~$ nv action traceroute system 10.10.10.2 l4protocol udp wait 2
Action executing ...
traceroute response 
{
  "destination_name": "10.10.10.2",
  "destination_address": "10.10.10.2",
  "hops": 30,
  "packet_size": 60,
  "trace": {
    "1": {
      "hop": 1,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "2": {
      "hop": 2,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "3": {
      "hop": 3,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
...
```

The following example validates the path to destination 10.10.10.2 from the source IP address 10.10.10.1.

```
cumulus@switch:~$ nv action traceroute system 10.10.10.2 source 10.10.10.1
Action executing ...
traceroute response 
{
  "destination_name": "10.10.10.2",
  "destination_address": "10.10.10.2",
  "hops": 30,
  "packet_size": 60,
  "trace": {
    "1": {
      "hop": 1,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "2": {
      "hop": 2,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "3": {
      "hop": 3,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "4":
...
```

The following example validates the path to destination 10.10.10.2 from the source IP address 10.0.0.1 in the management VRF.

```
cumulus@switch:~$ nv action traceroute system 10.10.10.2 source 10.10.10.1 vrf mgmt
Action executing ...
traceroute response 
{
  "destination_name": "10.10.10.2",
  "destination_address": "10.10.10.2",
  "hops": 30,
  "packet_size": 60,
  "trace": {
    "1": {
      "hop": 1,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "2": {
      "hop": 2,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
    "3": {
      "hop": 3,
      "address": "*",
      "name": "*",
      "rtt": [],
      "state": "NONE"
    },
...
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You send traceroute packets to a destination with the `traceroute` command. The destination can be either an IP address or a domain name. You can specify the following options:

| Option | Description |
| ------ | ----------- |
| `-m` | The maximum number of hops to reach the destination. You can specify a value between 1 and 30. The default is 30. |
| `-s` | The source IP address from which the route originates.|
| `-f` |The minimum number of hops to reach the destination. You can specify a value between 1 and 30. The default is 1. The minimum number of hops must be less than or equal to the maximum number of hops.|
| `-w` | The maximum number of nanoseconds to wait for a response from each hop. You can specify a value between 0.1 and 10.|
| `-i` | The VRF to use. |
| `<layer3-protocol>` | The layer 3 protocol; `-4` for IPv4 or `-6` for IPv6. The default is IPv4.|
| `<layer4-protocol>` | The layer 4 protocol packets to send; `-I` for ICMP, `-T` for TCP, or `-U` for UDP. The last hop information might not show with the `-I` or `-T` option.|
| `-F` | Do not fragment. Trace the route to the destination without fragmentation. |

The following example validates the route path to IPv4 destination 10.10.10.2.

```
cumulus@switch:~$ traceroute 10.10.10.2
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
traceroute to 10.10.10.2 (10.10.10.2), 30 hops max, 60 byte packets
 1  * * *
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
 8  * * *
 9  * * *
10  * * *
...
```

The following example validates the route path to IPv6 destination 2001:DB8::1.

```
cumulus@switch:~$ traceroute -6 2001:DB8::1
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
traceroute to 2001:DB8::1 (::1), 30 hops max, 80 byte packets
 1  * * *
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
```

The following example validates the path to destination 10.10.10.2 with 5 minimum hops and 10 maximum hops.

```
cumulus@switch:~$ traceroute -f 5 -m 10 10.10.10.2
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
traceroute to 10.10.10.2 (10.10.10.2), 10 hops max, 60 byte packets
 5  * * *
 6  * * *
 7  * * *
 8  * * *
 9  * * *
```

The following example sends UDP packets to validate the path to destination 10.10.10.2 and waits 2 nanoseconds for a response.

```
cumulus@switch:~$ traceroute  -U -w 2 10.10.10.2
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
traceroute to 10.10.10.2 (10.10.10.2), 30 hops max, 60 byte packets
 1  * * *
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
```

The following example validates the path to destination 10.10.10.2 from the source IP address 10.10.10.1.

```
cumulus@switch:~$ traceroute -s 10.10.10.1 10.10.10.2
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
traceroute to 10.10.10.2 (10.10.10.2), 30 hops max, 60 byte packets
 1  * * *
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
 8  * * *
...
```

The following example validates the path to destination 10.10.10.2 from the source IP address 10.0.0.1 in the management VRF.

```
cumulus@switch:~$ traceroute -s 10.10.10.1 -i mgmt 10.10.10.2
vrf-wrapper.sh: switching to vrf "default"; use '--no-vrf-switch' to disable
traceroute to 10.10.10.2 (10.10.10.2), 30 hops max, 60 byte packets
 1  * * *
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
 8  * * *
...
```

{{< /tab >}}
{{< /tabs >}}

## Extended traceroute

Cumulus Linux supports RFC 5837, which extends ICMP error messages with interface information, enabling more meaningful traceroute results in unnumbered networks where router interfaces use link-local addresses.

In unnumbered networks, router interfaces are assigned IPv6 link-local addresses (such as fe80::1/64) while only the loopback interface has globally unique addresses. When parallel links exist between routers, traditional traceroute cannot identify which physical interface a packet traverses because ICMP error messages use the loopback address as the source. With extended traceroute, you can see the name, index, MTU, and IP address (if present) of the interface that received the packet, enabling accurate path tracing.

{{%notice note%}}
- You can enable or disable RFC 5837 globally.
- Cumulus Linux supports incoming interface information only.
- ICMP rate limiting applies (1000 messages per second by default).
{{%/notice%}}

Extended traceroute is disabled by default.

To enable extended traceroute for unnumbered IPv6, run the `nv set system global icmp ipv6 errors-extension ingress-interface` command:

```
cumulus@switch:~$ nv set system global icmp ipv6 errors-extension ingress-interface
```

To disable extended traceroute for IPv6 unnumbered, run the `nv unset system global icmp ipv6 errors-extension ingress-interface` command.

To enable extended traceroute for IPv4 over IPv6 unnumbered, run the `nv set system global icmp ipv4 errors-extension ingress-interface` command:

```
cumulus@switch:~$ nv set system global icmp ipv4 errors-extension ingress-interface
```

To disable extended traceroute for IPv4 over IPv6 unnumbered, run the `nv unset system global icmp ipv4 errors-extension ingress-interface` command.

To show if extended traceroute is enabled, run the `nv show system` global command.

```
cumulus@switch:~$ nv show system global
                                operational        applied     pending 
------------------------------  -----------------  ----------  ---------- 
... 

arp 

  base-reachable-time           1080               auto        auto 
  garbage-collection-threshold 
    minimum                     128 
    effective                   36178 
    maximum                     41347 
nd 
  base-reachable-time           1080               auto        auto 
  garbage-collection-threshold 
    minimum                     128 
    effective                   18088 
    maximum                     20673 
icmp                                                                
  ipv4                                                              
    [errors-extension]          ingress-interface  ingress-interface
  ipv6                                                              
    [errors-extension]          ingress-interface  ingress-interface 
```

The following example shows extended traceroute for IPv6 unnumbered:

```
cumulus@switch:~$ traceroute6 -e 2001:db8:1::3 
 traceroute to 2001:db8:1::3 (2001:db8:1::3), 30 hops max, 80 byte packets 
  1  2001:db8:1::2 (2001:db8:1::2) <INC:11,"eth1",mtu=1500>  0.214 ms  0.171 ms  0.162 ms 
  2  2001:db8:1::3 (2001:db8:1::3) <INC:12,"eth2",mtu=1500>  0.154 ms  0.135 ms  0.127 ms 
```

The following example shows extended traceroute for IPv4 over IPv6 unnumbered:

```
cumulus@switch:~$ traceroute -e 192.0.2.3 
 traceroute to 192.0.2.3 (192.0.2.3), 30 hops max, 60 byte packets 
  1  192.0.2.2 (192.0.2.2) <INC:11,"eth1",mtu=1500>  0.191 ms  0.148 ms  0.144 ms 
  2  192.0.2.3 (192.0.2.3) <INC:12,"eth2",mtu=1500>  0.137 ms  0.122 ms  0.114 ms 
```

## tcpdump

You can use the Linux `tcpdump` command to monitor control plane traffic (traffic sent to and coming from the switch CPUs). `tcpdump` does **not** monitor data plane traffic; use `cl-acltool` instead.

The example below uses the following `tcpdump` options:
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
