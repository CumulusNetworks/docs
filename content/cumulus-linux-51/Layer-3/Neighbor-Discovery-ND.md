---
title: Neighbor Discovery - ND
author: NVIDIA
weight: 1002
toc: 3
---
[ND](## "Neighbor Discovery") is the IPv6 equivalent of the IPv4 ARP for layer 2 address resolution. ND uses IPv6 ICMP messages to discover IPv6 devices, such as switches and servers on the same interface.

ND is on by default in Cumulus Linux. You can tune certain parameters for security reasons and to properly support IPv6 networks.

## ND Configuration Options

Cumulus Linux provides options to disable ND and to configure these ND settings:
- Recursive DNS servers (RDNSS)
- IPv6 prefixes
- DNS Search Lists (DNSSL)
- Router advertisement
- Home agents
- The MTU for neighbor discovery messages

### Recursive DNS Servers

Recursive DNS servers you want to advertise
To set the maximum amount of time in seconds to use the recursive DNS server for domain name resolution:

The following command example sets the recursive DNS server to 2001:db8:1::100 and sets the lifetime to infinite:

{{< tabs "TabID28 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery rdnss 2001:db8:1::100
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery rdnss 2001:db8:1::100 lifetime infinite
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd rdnss 2001:db8:1::100
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

### IPv6 Prefixes

nv set interface swp1 ip neighbor-discovery prefix <ipv6-prefix-id>

Time in seconds the prefix is valid for on-link determination

nv set interface swp1 ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime 0-4294967295

Time in seconds that addresses generated from a prefix remain preferred

nv set interface swp1 ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime 0-4294967295

Indicates that adverisement makes no statement about on-link or off-link properties of the prefix

nv set interface swp1 ip neighbor-discovery prefix <ipv6-prefix-id> off-link (on|off)

Indicates to hosts on the local link that the specified prefix can be used for v6 autoconfiguration

nv set interface swp1 ip neighbor-discovery prefix <ipv6-prefix-id> autoconfig (on|off)

Indicates to hosts on the local link that the specified prefix contains a complete IP address by setting the R flag

nv set interface swp1 ip neighbor-discovery prefix <ipv6-prefix-id> router-address (on|off)

### DNS Search List

To configure the DNS search lists that you want Cumulus Linux to advertise, set the the domain portion of the hostname (RFC 1123) or internationalized hostname (RFC 5890):

To set the maximum amount of time in seconds that Cumulus Linux uses the domain suffix for domain name resolution:

The following example command configures the DNS search list to `.com` and the lifetime to `infinite`:

{{< tabs "TabID87 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery dnssl .com
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery dnssl .com lifetime infinite
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd dnssl .com infinite
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

### Router Advertisement

You can set the following router advertisement parameters:

|                  |                                     |
| ---------------- | ----------------------------------- |
| enable           | Set router advertisement `on` or `off`. The default setting is `on`. |
| fast-retransmit  | Allow consecutive router advertisement packets more frequently than every 3 seconds. Set this parameter to `on` or `off`. The default setting is `on`. |
| hop-limit        | The value in the hop count field of the IP header in the outgoing router advertisement packet. You can set a value between 0 and 255. The default value is 64.|
| interval         | The maximum amount of time in milliseconds allowed between sending unsolicited multicast router advertisement from the interface. You can set a value between 70 and 1800000 milliseconds. The default value is 600000. |
| interval-option  | Indicates to hosts that the router uses an advertisement interval to send router advertisements. Set this parameter to `on` or `off`. The default setting is `on`. |
| lifetime         | The maximum amount of time in seconds that the router is a default gateway. You can set a value between 0 and 9000. The default value is 1800 seconds. |
| managed-config   | Allows a dynamic host to use a managed (stateful) protocol for address autoconfiguration in addition to any addresses autoconfigured using stateless address autoconfiguration. Set this parameter to `on` or `off`. By default, this parameter is not set. |
| other-config     | Allows a dynamic host to use managed (stateful) protocol for autoconfiguration information other than addresses. Set this parameter to `on` or `off`. By default, this parameter is not set. |
| reachable-time   | Time in milliseconds that a IPv6 node is considered reachable. You can set a value between 0 and 3600000 milliseconds. The default value is 0.|
| retransmit-time  | Time in milliseconds between retransmission of neighbor solicitation messages. You can set aa value between 0 and 4294967295 milliseconds. The default value is 0. |
| router-preference| Hosts use the router preference to select the default router. You can set a value of high, medium, or low. The default value is medium. |

The following command example sets the router advertisement interval to 600000 milliseconds and the router preference to high:

{{< tabs "TabID132 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement interval 600000
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement router-preference high
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd ra-interval 600000
leaf01(config-if)# ipv6 nd ra-prefernce high
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

The following command example disables router advertisement on swp1:

{{< tabs "TabID164 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement enable off
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd suppress-ra
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

### Home Agent

Mobile IPv6 defines an additional flag in the router advertisement message that indicates if the advertising router is capable of being a home agent. Each of the home agents on the home link sets this flag when it sends its router advertisements, and each home agent receives each router advertisement. 

The value to be placed in Home Agent Option, when Home Agent config flag is set, which indicates to hosts Home Agent preference. 0-65535 The default value of 0 stands for the lowest preference possible. Default: 0  

The value to be placed in Home Agent Option, when Home Agent config flag is set, which indicates to hosts Home Agent Lifetime. 0-65520The default value of 0 means to place the current Router Lifetime value.

The following command example configures the switch as a home agent by setting the preference to 100 and the lifetime to 0:

{{< tabs "TabID210 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery home-agent preference 100
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery home-agent lifetime 0
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd home-agent-preference 100
leaf01(config-if)# ipv6 nd home-agent-lifetime 0
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

### MTU

You can set the [MTU](## "Maximum Transmission Unit") for neighbor discovery messages on an interface. You can configure a value between 1 and 65535.

To following command example sets the MTU on swp1 to 1500:

{{< tabs "TabID244 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery mtu 1500
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd mtu 1500
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

## Disable ND

To disable ND:

{{< tabs "TabID274 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery enable off
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd

{{< /tab >}}
{{< /tabs >}}
