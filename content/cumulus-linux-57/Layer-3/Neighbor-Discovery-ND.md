---
title: Neighbor Discovery - ND
author: NVIDIA
weight: 1002
toc: 3
---
<span class="a-tooltip">[ND](## "Neighbor Discovery")</span> allows different devices on the same link to advertise their existence to their neighbors and to learn about the existence of their neighbors. ND is the IPv6 equivalent of IPv4 ARP for layer 2 address resolution.

ND is on by default. Cumulus Linux provides a set of configuration options to support IPv6 networks and adjust your security settings.

Cumulus Linux provides options to configure:
- Router Advertisement
- IPv6 prefixes
- Recursive DNS servers
- DNS Search Lists
- Home Agents
- MTU for neighbor discovery messages
- Global timer settings

## Router Advertisement
<!-- vale off -->
Router Advertisement is disabled by default. To enable Router Advertisment for an interface:
<!-- vale on -->
{{< tabs "TabID135 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement enable on
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# interface swp1
leaf01(config-if)# no ipv6 nd suppress-ra
```

{{< /tab >}}
{{< /tabs >}}

You can configure these optional settings:

- Allow consecutive Router Advertisement packets to transmit more frequently than every three seconds (fast retransmit). You can set this parameter to `on` or `off`. The default setting is `on`.
- Set the hop limit value advertised in a Router Advertisement message. You can set a value between 0 and 255. The default value is 64.
- Set the interval between unsolicited multicast router advertisements from the interface. You can set a value between 70 and 1800000 miliseconds. The default value is 600000 miliseconds.
- Set the maximum amount of time that Router Advertisement messages can exist on the route. You can set a value between 0 and 9000 seconds. The default value is 1800.
- Allow a dynamic host to use a managed protocol, such as DHCPv6 to configure IP addresses automatically (managed configuration). Set this parameter to `on` or `off`. By default, this parameter is not set.
- Allow a dynamic host to use a managed protocol to configure additional information through DHCPv6. Set this parameter to `on` or `off`. By default, this parameter is not set.
- Set the amount of time that an IPv6 node is reachable. You can set a value between 0 and 3600000 milliseconds. The default value is 0.
- Set the interval at which neighbor solicitation messages retransmit. You can set a value between 0 and 4294967295 milliseconds. The default value is 0.
- Allow hosts to use router preference to select the default router. You can set a value of high, medium, or low. The default value is medium.

The following example commands set:
- The Router Advertisement interval to 60000 milliseconds (60 seconds).
- The router preference to high.
- The amount of time that an IPv6 node is reachable to 3600000.
- The interval at which neighbor solicitation messages retransmit to 4294967295.
- The hop limit value in the Router Advertisement message to 100.
- The maximum amount of time that Router Advertisement messages exist on the route to 4000.

{{< tabs "TabID43 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement interval 60000
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement router-preference high
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement reachable-time 3600000
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement retransmit-time 4294967295
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement hop-limit 100
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement lifetime 4000
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd ra-interval 60
leaf01(config-if)# ipv6 nd router-preference high
leaf01(config-if)# ipv6 nd reachable-time 3600000
leaf01(config-if)# ipv6 nd ra-retrans-interval 4294967295
leaf01(config-if)# ipv6 nd ra-hop-limit 100
leaf01(config-if)# ipv6 nd ra-lifetime 4000
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

The vtysh commands save the configuration in the `etc/frr/frr.conf` file:

```
cumulus@leaf01:mgmt:~$ sudo cat etc/frr/frr.conf
...
interface swp1
 ipv6 nd ra-hop-limit 100
 ipv6 nd ra-interval 60
 ipv6 nd ra-lifetime 4000
 ipv6 nd ra-retrans-interval 4294967295
 ipv6 nd reachable-time 3600000
 ipv6 nd router-preference high
```

{{< /tab >}}
{{< /tabs >}}

The following example commands set fast retransmit to off and managed configuration to on:

{{< tabs "TabID95 ">}}
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
leaf01# configure terminal
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd ra-fast-retrans
leaf01(config-if)# ipv6 nd managed-config-flag
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:mgmt:~$ 
```

The vtysh commands save the configuration in the `etc/frr/frr.conf` file:

```
cumulus@leaf01:mgmt:~$ sudo cat etc/frr/frr.conf
...
interface swp1
 ipv6 nd ra-fast-retrans
 ipv6 nd managed-config-flag
```

{{< /tab >}}
{{< /tabs >}}

## IPv6 Prefixes

To configure IPv6 prefixes, you must specify the IPv6 prefixes you want to include in router advertisements. In addition, you can configure these optional settings:
- Set the amount of time that the prefix is valid for on-link determination. You can set a value between 0 and 4294967295 seconds. The default value is 2592000.
- Set the amount of time that addresses generated from a prefix remain preferred. You can set a value between 0 and 4294967295 seconds. The default value is 604800.
- Enable adverisement to make no statement about prefix on-link or off-link properties. By default, this setting is off.
- Enable the specified prefix to use IPv6 autoconfiguration. By default, this setting is on.
- Indicate to hosts on the local link that the specified prefix contains a complete IP address by setting the R flag. By default, this setting is off.

The following example commands set the IPv6 prefix to 2001:db8:1::100/32, the amount of time that the prefix is valid for on-link determination to 2000000000, and the amount of time that addresses generated from a prefix remain preferred to 1000000000.

{{< tabs "TabID168 ">}}
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
leaf01# configure terminal
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd prefix 2001:db8:1::100/32 2000000000 1000000000
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
 ipv6 nd prefix 2001:db8::/32 2000000000 1000000000
 ...
```

{{< /tab >}}
{{< /tabs >}}

The following example commands set advertisement to make no statement about prefix on-link or off-link properties, enable the specified prefix to use IPv6 autoconfiguration, and indicate to hosts on the local link that the specified prefix contains a complete IP address.

{{< tabs "TabID207 ">}}
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
leaf01# configure terminal
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd prefix 2001:db8:1::100/32 off-link
leaf01(config-if)# ipv6 nd prefix 2001:db8:1::100/32 no-autoconfig
leaf01(config-if)# ipv6 nd prefix 2001:db8:1::100/32 router-address
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
 ipv6 nd prefix 2001:db8::/32 off-link
 ipv6 nd prefix 2001:db8::/32 router-address
 ipv6 nd prefix 2001:db8::/32 no-autoconfig
 ...
```

{{< /tab >}}
{{< /tabs >}}

## Recursive DNS Servers

To configure recursive DNS servers (RDNSS), you must specify the IPv6 address of each RDNSS you want to advertise.

An optional parameter lets you set the maximum amount of time you want to use the RDNSS for domain name resolution. You can set a value between 0 and 4294967295 seconds or use the keyword `infinte` to set the time to never expire. If you set the value to 0, Cumulus Linux no longer advertises the RDNSS address.

The following example commands set the RDNSS address to 2001:db8:1::100 and the lifetime to infinite:

{{< tabs "TabID257 ">}}
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
leaf01# configure terminal
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd rdnss 2001:db8:1::100 infinite
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

## DNS Search Lists

To configure DNS search lists (DNSSL), you must specify the domain suffix you want to advertise.

An optional parameter lets you set the maximum amount of time you want to use the domain suffix for domain name resolution. You can set a value between 0 and 4294967295 seconds or use the keyword `infinte` to set the time to never expire. If you set the value to 0, the host does not use the DNSSL.

The following example command sets the domain suffix to `accounting.nvidia.com` and the maximum amount of time you want to use the domain suffix to `infinite`:

{{< tabs "TabID303 ">}}
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
leaf01# configure terminal
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd dnssl accounting.nvidia.com infinite
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
 ipv6 nd dnssl accounting.nvidia.com infinite
...
```

{{< /tab >}}
{{< /tabs >}}

## Home Agents

Mobile IPv6 defines an additional flag in the router advertisement message that indicates if the advertising router is capable of being a Home Agent. Each Home Agent on the home link sets this flag when it sends router advertisements.

You can configure the switch to be a Home Agent with these settings:
- Set the maximum amount of time you want the router to act as a Home Agent. You can set a value between 0 and 65520 seconds. The default value is 0 (the router is not a Home Agent).
- Set the Home Agent router preference. You can set a value between 0 and 65535. The default value is 0 (the lowest preference).

The following example commands configure the switch as a Home Agent by setting the maximum amount of time the router acts as a Home Agent to 20000 seconds and the router preference to 100:

{{< tabs "TabID349 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery home-agent preference 100
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery home-agent lifetime 20000
cumulus@leaf01:mgmt:~$ nv config apply
```

{{%notice note%}}
When you run the above commands, NVUE adds the `ipv6 nd home-agent-config-flag` line under the interface stanza in the `/etc/network/interfaces` file in addition to the `ipv6 nd home-agent-preference` and `ipv6 nd home-agent-lifetime` lines.
{{%/notice%}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd home-agent-config-flag
leaf01(config-if)# ipv6 nd home-agent-preference 100
leaf01(config-if)# ipv6 nd home-agent-lifetime 0
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
 ipv6 nd home-agent-config-flag
 ipv6 nd home-agent-lifetime 0
 ipv6 nd home-agent-preference 100
...
```

{{< /tab >}}
{{< /tabs >}}

## MTU

You can set the <span class="a-tooltip">[MTU](## "Maximum Transmission Unit")</span> for neighbor discovery messages on an interface. You can configure a value between 1 and 65535.

To following example commands set the MTU on swp1 to 1500:

{{< tabs "TabID396 ">}}
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
leaf01# configure terminal
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 nd mtu 1500
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
 ipv6 nd mtu 1500
...
```

{{< /tab >}}
{{< /tabs >}}

## Neighbor Base Reachable Timer

You can set how long a neighbor cache entry is valid with the NVUE `nv set system global nd base-reachable-time` command. The entry is valid for at least the value between the base reachable time divided by two and three times the base reachable time divided by two. You can specify a value between 30 and 2147483 seconds. The default value is `auto`; NVUE derives the value for `auto` from the `/etc/sysctl.d/neigh.conf` file.

The following example configures the neighbor base reachable timer to 50 seconds.

```
cumulus@leaf01:~$ nv set system global nd base-reachable-time 50
cumulus@leaf01:~$ nv config apply
```

To reset the neighbor base reachable timer to the default setting, run the `nv unset system global nd base-reachable-time` command.

{{%notice note%}}
NVIDIA recommends that you run the NVUE command to change the neighbor base reachable timer instead of modifying the `/etc/sysctl.d/neigh.conf` file manually.
{{%/notice%}}

To show the neighbor base reachable timer setting, run the `nv show system global nd` command:

```
cumulus@leaf01:~$ nv show system global nd
                              operational  applied  
----------------------------  -----------  ------- 
base-reachable-time           50           50      
garbage-collection-threshold                               
  effective                   17920                        
  maximum                     20480                        
  minimum                     128       
```

## Disable ND

To disable ND, run the NVUE `nv set interface <interface> ip neighbor-discovery enable off` command:

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery enable off
cumulus@leaf01:mgmt:~$ nv config apply
```

## Troubleshooting

To show the ND settings for an interface, run the NVUE `nv show interface <interface-id> ip neighbor-discovery` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery
                      applied             description
--------------------  ------------------  ----------------------------------------------------------------------
enable                on                  Turn the feature 'on' or 'off'.  The default is 'on'.
home-agent
  lifetime            0                   Lifetime of a home agent in seconds
  preference          0                   Home agent's preference value that is used to order the addresses r...
[prefix]              2001:db8:1::100/32  IPv6 prefix configuration
router-advertisement
  enable              on                  Turn the feature 'on' or 'off'.  The default is 'on'.
  fast-retransmit     off                 Allow consecutive RA packets more frequently than every 3 seconds
  hop-limit           100                 Value in hop count field in IP header of the outgoing router advert...
  interval            6000                Maximum time in milliseconds allowed between sending unsolicited mu...
  interval-option     on                  Indicates hosts that the router will use advertisement interval to...
  lifetime            4000                Maximum time in seconds that the router can be treated as default g...
  managed-config      on                  Knob to allow dynamic host to use managed (stateful) protocol for a...
  other-config        off                 Knob to allow dynamic host to use managed (stateful) protocol for a...
  reachable-time      3600000             Time in milliseconds that a IPv6 node is considered reachable
  retransmit-time     4294967295          Time in milliseconds between retransmission of neighbor solicitatio...
  router-preference   high                Hosts use router preference in selection of the default router
```

To show prefix configuration for an interface, run the `nv show interface <interface> ip neighbor-discovery prefix <prefix>` command.

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32
                    applied     description
------------------  -------     ----------------------------------------------------------------------
autoconfig          on          Indicates to hosts on the local link that the specified prefix can...
off-link            on          Indicates that adverisement makes no statement about on-link or off...
preferred-lifetime  1000000000  Time in seconds that addresses generated from a prefix remain prefe...
router-address      on          Indicates to hosts on the local link that the specified prefix cont...
valid-lifetime      2000000000  Time in seconds the prefix is valid for on-link determination
```

To show Home Agent configuration for an interface, run the `nv show interface <interface> ip neighbor-discovery home-agent` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery home-agent
            applied  description
----------  -------  ----------------------------------------------------------------------
lifetime    20000    Lifetime of a home agent in seconds
preference  100      Home agent's preference value that is used to order the addresses r...
```

To show router advertisement configuration for an interface, run the `nv show interface <interface> ip neighbor-discovery router-advertisement` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery router-advertisement
                   applied   description
-----------------  -------   ----------------------------------------------------------------------
enable             on        Turn the feature 'on' or 'off'.  The default is 'on'.
fast-retransmit    on        Allow consecutive RA packets more frequently than every 3 seconds
hop-limit          64        Value in hop count field in IP header of the outgoing router advert...
interval           600000    Maximum time in milliseconds allowed between sending unsolicited mu...
interval-option    on        Indicates hosts that the router will use advertisement interval to...
lifetime           1800      Maximum time in seconds that the router can be treated as default g...
managed-config     off       Knob to allow dynamic host to use managed (stateful) protocol for a...
other-config       off       Knob to allow dynamic host to use managed (stateful) protocol for a...
reachable-time     0         Time in milliseconds that a IPv6 node is considered reachable
retransmit-time    0         Time in milliseconds between retransmission of neighbor solicitatio...
router-preference  medium    Hosts use router preference in selection of the default router
```

To show RDNSS configuration for an interface, run the `nv show interface <interface> ip neighbor-discovery rdnss <address>` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery rdnss 2001:db8:1::100
          applied   description
--------  --------  ----------------------------------------------------------------------
lifetime  infinite  Maximum time in seconds for which the server may be used for domain...
```

To show DNSSL configuration for an interface, run the `nv show interface <interface> ip neighbor-discovery dnssl <domain-suffix>` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery dnssl accounting.nvidia.com
          applied   description
--------  --------  ----------------------------------------------------------------------
lifetime  infinite  Maximum time in seconds for which the domain suffix may be used for...
```
