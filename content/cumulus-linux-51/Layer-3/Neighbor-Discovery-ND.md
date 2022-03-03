---
title: Neighbor Discovery - ND
author: NVIDIA
weight: 1002
toc: 3
---
[ND](## "Neighbor Discovery") allows different devices on the same link to advertise their existence to their neighbors and learn about the existence of their neighbors. ND is the IPv6 equivalent of IPv4 ARP for layer 2 address resolution.

ND is on by default in Cumulus Linux. You can tune certain parameters to properly support IPv6 networks and for security reasons.

## ND Configuration Options

Cumulus Linux provides options to configure:
- Router Advertisement
- IPv6 prefixes
- Recursive DNS servers
- DNS Search Lists
- Home Agents
- MTU for neighbor discovery messages

### Router Advertisement

Router Advertisment is on by default. You can configure these optional settings:

- Allow consecutive Router Advertisement packets to transmit more frequently than every 3 seconds (fast retransmit). You can set this parameter to `on` or `off`. The default setting is `on`.
- Set the hop limit value advertised in a Router Advertisement message. You can set a value between 0 and 255. The default value is 64.
- Set the interval between unsolicited multicast router advertisements from the interface. You can set a value between 70 and 180000 seconds. The default value is 600000 miliseconds.
- Set the maximum amount of time that you want Router Advertisement messages to exist on the route. You can set a value between 0 and 9000 seconds. The default value is 1800.
- Allow a dynamic host to use a managed (stateful) protocol for address autoconfiguration in addition to any addresses autoconfigured using stateless address autoconfiguration (managed configuration). Set this parameter to `on` or `off`. By default, this parameter is not set.
- Allow a dynamic host to use a managed (stateful) protocol for autoconfiguration information other than addresses. Set this parameter to `on` or `off`. By default, this parameter is not set.
- Set the amount of time that an IPv6 node is considered reachable. You can set a value between 0 and 3600000 milliseconds. The default value is 0.
- Set the amount of time between neighbor solicitation message retransmission. You can set a value between 0 and 4294967295 milliseconds. The default value is 0.
- Allow hosts to use router preference to select the default router. You can set a value of high, medium, or low. The default value is medium.

The following command example sets the Router Advertisement interval to 600000 milliseconds, the router preference to high, the amount of time that an IPv6 node is considered reachable to 3600000, and the amount of time between neighbor solicitation message retransmission to 4294967295:

{{< tabs "TabID179 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement interval 600000
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement router-preference high
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement reachable-time 3600000
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement retransmit-time 4294967295
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
leaf01(config-if)# ipv6 nd router-preference high
leaf01(config-if)# ipv6 nd reachable-time 3600000
leaf01(config-if)# ipv6 nd ra-retrans-interval 4294967295
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

The following command example sets fast retransmit to off, and managed configuration to on:

{{< tabs "TabID217 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement fast-retransmit off
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement managed-config on
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd ra-fast-retrans
leaf01(config-if)# ipv6 nd managed-config-flag
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

### IPv6 Prefixes

To configure IPv6 prefixes, you must specify the IPv6 prefixes you want to include in router advertisements. In addition, you can configure these optional settings:
- Set the amount of time that the prefix is valid for on-link determination. You can set a value between 0 and 4294967295 seconds. The default value is 2592000.
- Set the amount of time that addresses generated from a prefix remain preferred. You can set a value between 0 and 42949672955 seconds. The default value is 604800.
- Enable adverisement to make no statement about prefix on-link or off-link properties.
- Enable the specified prefix to use for IPv6 autoconfiguration.
- Indicate to hosts on the local link that the specified prefix contains a complete IP address by setting the R flag.

The following command example configures the IPv6 prefix 2001:db8:1::100/32, and sets the amount of time that the prefix is valid for on-link determination to 2000000000 and the amount of time that addresses generated from a prefix remain preferred to 1000000000.

{{< tabs "TabID68 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 valid-lifetime 2000000000
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 preferred-lifetime 1000000000
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd prefix 2001:db8:1::100/32 2000000000 
leaf01(config-if)# ipv6 nd prefix 2001:db8:1::100/32 ?????? 2000000000
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

The following command example enables off-link, autoconfiguration, and complete router IP address.

{{< tabs "TabID99 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 off-link on
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 autoconfig on
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 router-address on
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd prefix 2001:db8:1::100/32 off-link
leaf01(config-if)# ipv6 nd prefix 2001:db8:1::100/32 no-autoconfig
leaf01(config-if)# ipv6 nd prefix 2001:db8:1::100/32 router-address
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

### Recursive DNS Servers

To configure recursive DNS servers (RDNSS), you must specify the IPv6 address of each RDNSS you want to advertise.

An optional parameter lets you set the maximum amount of time you want to use the RDNSS for domain name resolution. You can set a value between 0 and 4294967295 seconds or use the keyword `infinte` to set the time to never expire. If you set a value of 0, Cumulus Linux no longer advertises the RDNSS address.

The following command example sets the RDNSS address to 2001:db8:1::100 and the lifetime to infinite:

{{< tabs "TabID29 ">}}
{{< tab "NVUE Commands ">}}

```
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

The vtysh commands write to the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/frr/frr.conf
...
interface swp1
 ipv6 nd rdnss 2001:db8:1::100 infinite
 ...
```

{{< /tab >}}
{{< /tabs >}}

### DNS Search Lists

To configure DNS search lists (DNSSL), you need to specify the domain suffix you want to advertise. An optional parameter lets you set the maximum amount of time you want to use the domain suffix for domain name resolution. You can set a value between 0 and 4294967295 seconds or use the keyword `infinte` to set the time to never expire. A value of 0 tells the host not to use the DNSSL.

The following example command sets the domain suffix to `accounting.nvidia.com` and the maximum amount of time you want to use the domain suffix to `infinite`:

{{< tabs "TabID133 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery dnssl accounting.nvidia.com lifetime infinite
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd dnssl accounting.nvidia.com infinite
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

{{< /tab >}}
{{< /tabs >}}

### Home Agents

Mobile IPv6 defines an additional flag in the router advertisement message that indicates if the advertising router is capable of being a Home Agent. Each Home Agent on the home link sets this flag when it sends router advertisements.

You can configure the switch to be a Home Agent with these settings:
- Set the maximum amount of time you want the router to act as a Home Agent. You can set a value between 0 and 65520 seconds. The default value is 0 (the router is not a Home Agent).
- Set the Home Agent router preference. You can set a value between 0 and 65535. The default value is 0 (the lowest preference).

The following command example configures the switch as a Home Agent by setting the preference to 100 and the lifetime to 20000 seconds:

{{< tabs "TabID245 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery home-agent preference 100
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery home-agent lifetime 20000
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# conf t
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd home-agent-config-flag
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

{{< tabs "TabID279 ">}}
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

{{< tabs "TabID309 ">}}
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
leaf01(config-if)# ipv6 nd suppress-ra
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

To show the ND settings for an interface, run the NVU `nv show interface <interface-id> ip neighbor-discovery` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery
                      applied  pending             description
--------------------  -------  ------------------  ----------------------------------------------------------------------
enable                         on                  Turn the feature 'on' or 'off'.  The default is 'on'.
[dnssl]                                            Advertise DNS search list using type 31 option RFC8106
home-agent
  lifetime                     0                   Lifetime of a home agent in seconds
  preference                   0                   Home agent's preference value that is used to order the addresses r...
[prefix]                       2001:db8:1::100/32  IPv6 prefix configuration
[rdnss]                                            Recursive DNS server addresses to be advertised using type 25 optio...
router-advertisement
  enable                       on                  Turn the feature 'on' or 'off'.  The default is 'on'.
  fast-retransmit              on                  Allow consecutive RA packets more frequently than every 3 seconds
  hop-limit                    64                  Value in hop count field in IP header of the outgoing router advert...
  interval                     600000              Maximum time in milliseconds allowed between sending unsolicited mu...
  interval-option              on                  Indicates hosts that the router will use advertisement interval to...
  lifetime                     1800                Maximum time in seconds that the router can be treated as default g...
  managed-config               off                 Knob to allow dynamic host to use managed (stateful) protocol for a...
  other-config                 off                 Knob to allow dynamic host to use managed (stateful) protocol for a...
  reachable-time               0                   Time in milliseconds that a IPv6 node is considered reachable
  retransmit-time              0                   Time in milliseconds between retransmission of neighbor solicitatio...
  router-preference            medium              Hosts use router preference in selection of the default router
```

To show prefix configuration for an interface, run the `nv show interface <interface> ip neighbor-discovery prefix <prefix>` command.

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32
                    applied  pending  description
------------------  -------  -------  ----------------------------------------------------------------------
autoconfig                   on       Indicates to hosts on the local link that the specified prefix can...
off-link                     off      Indicates that adverisement makes no statement about on-link or off...
preferred-lifetime           604800   Time in seconds that addresses generated from a prefix remain prefe...
router-address               off      Indicates to hosts on the local link that the specified prefix cont...
valid-lifetime               2592000  Time in seconds the prefix is valid for on-link determination
```

To show Home Agent configuration for an interface, run the `nv show interface <interface> ip neighbor-discovery home-agent` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery home-agent
            applied  pending  description
----------  -------  -------  ----------------------------------------------------------------------
lifetime             0        Lifetime of a home agent in seconds
preference           0        Home agent's preference value that is used to order the addresses r...
```

To show router advertisement configuration for an interface, run the `nv show interface <interface> ip neighbor-discovery router-advertisement` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery router-advertisement
                   applied  pending  description
-----------------  -------  -------  ----------------------------------------------------------------------
enable                      on       Turn the feature 'on' or 'off'.  The default is 'on'.
fast-retransmit             on       Allow consecutive RA packets more frequently than every 3 seconds
hop-limit                   64       Value in hop count field in IP header of the outgoing router advert...
interval                    600000   Maximum time in milliseconds allowed between sending unsolicited mu...
interval-option             on       Indicates hosts that the router will use advertisement interval to...
lifetime                    1800     Maximum time in seconds that the router can be treated as default g...
managed-config              off      Knob to allow dynamic host to use managed (stateful) protocol for a...
other-config                off      Knob to allow dynamic host to use managed (stateful) protocol for a...
reachable-time              0        Time in milliseconds that a IPv6 node is considered reachable
retransmit-time             0        Time in milliseconds between retransmission of neighbor solicitatio...
router-preference           medium   Hosts use router preference in selection of the default router
```

To show RDNSS configuration for an interface, run the `nv show interface <interface> ip neighbor-discovery rdnss` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery rdnss
```

To show DNSSL configuration for an interface, run the `nv show interface <interface> ip neighbor-discovery dnssl` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery dnssl
```
