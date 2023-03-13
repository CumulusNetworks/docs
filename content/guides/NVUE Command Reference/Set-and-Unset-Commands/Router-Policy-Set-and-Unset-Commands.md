---
title: Router Policy Set and Unset Commands
author: Cumulus Networks
weight: 700
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set router policy

Configures a router policy.

- - -

## nv set router policy community-list \<list-id\>

Configures the name of the community list you want to use to match BGP community policies.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list COMMUNITY1
```

- - -

## nv set router policy community-list \<list-id\> rule \<rule-id\>

Configures the community list rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>`  | The community list name. |
| `<rule-id>`  | The community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list COMMUNITY1 rule 10 action permit
```

- - -

## nv set router policy community-list \<list-id\> rule \<rule-id\> community \<community-id\>

Sets the name of the community you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The community list name. |
| `<rule-id>` | The community list rule number. |
| `<community-id>` | The community number in AA:NN format or the well-known name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list COMMUNITY1 rule 10 community 100:100
```

- - -

## nv set router policy community-list \<list-id\> rule \<rule-id\> action

Sets the action you want to take when you meet the match criteria; permit or deny.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>`  | The community list name. |
| `<rule-id>`  | The community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list COMMUNITY1 rule 10 action permit
```

- - -

## nv set router policy as-path-list \<list-id\>

Sets the name of the AS path access list you want to use to match AS paths.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The AS path list name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist
```

- - -

## nv set router policy as-path-list \<list-id\> rule \<rule-id\>

Configures the AS Path list rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The AS Path list name. |
| `<rule-id>` |  The prefix list rule number. |

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist rule 10
```

- - -

## nv set router policy as-path-list \<list-id\> rule \<rule-id\> action

Sets the action you want to take for a match; permit or deny.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The AS path list name. |
| `<rule-id>` |  The AS path list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist rule 10 action permit
```

- - -

## nv set router policy as-path-list \<list-id\> rule \<rule-id\> aspath-exp \<bgp-regex\>

Configures the regular expression you want to use to match BGP AS paths.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The AS path list name. |
| `<rule-id> ` | Th AS path list rule number. |
| `bgp-regex` | The regular expression you want to use to match BGP AS paths.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist rule 10 aspath-exp ^100_
```

- - -

## nv set router policy ext-community-list \<list-id\>

Sets the name of the Extended Community list you want to use to match BGP communities.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The extended community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist
```

- - -

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\>

Sets the extended community list rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10
```

- - -

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community

Sets the Extended Community name.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<list-id>` |  The Extended Community list name. |
| `<rule-id>` | The Extended Community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 ext-community 64510:2
```

- - -

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community rt \<ext-community-id\>

Configures the Route Target Extended Community.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The community list rule number. |
| `<ext-community-id>` | The Extended Community number in AA:NN or IP:NN format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 ext-community rt 64510:1111
```

- - -

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community soo \<ext-community-id\>

Configures the site-of-origin (SoO) Extended Community to identify routes that originate from a certain site so that you can prevent readvertising that prefix back to the source site.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id> ` | The community list name. |
| `<rule-id> ` |  The community list rule number. |
| `<ext-community-id>` | The Extended Community number in AA:NN or IP:NN format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 ext-community soo 45000:3
```

- - -

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> action

Configures the action to take on a match; permit or deny.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 action permit
```

- - -

## nv set router policy large-community-list \<list-id\>

Configures the name of the Large Community list you want to use to match community based BGP policies.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>`  | The community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist
```

- - -

## nv set router policy large-community-list \<list-id\> rule \<rule-id\>

Configures the Large Community list rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The community list name |
| `<rule-id>`  | The community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist rule 10
```

- - -

## nv set router policy large-community-list \<list-id\> rule \<rule-id\> large-community \<large-community-id\>

Configures the community names for the large community list.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id> ` | The community list rule number. |
| `<large-community-id>` | The community number in AA:BB:CC format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist rule 10 large-community ?????
```

- - -

## nv set router policy large-community-list \<list-id\> rule \<rule-id\> action

Configures the action for the large community list policy match. You can specify `permit` or `deny`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id> ` | The community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist rule 10 action permit
```

- - -

## nv set router policy prefix-list \<prefix-list-id\>

Configures the name of the prefix list you want to use to match IPv4 and IPv6 address prefixes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` |  The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist
```

- - -

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\>

Configures the prefix list rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>`  | The prefix list name. |
| `<rule-id>`  | The prefix list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10
```

- - -

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\>

Configures the prefix match criteria you want to use.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name. |
| `<rule-id> ` | The prefix list rule number. |
| `<match-id>` | The IPv4 or IPv6 prefix you want to match.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16
```

- - -

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\> min-prefix-len

Configures the minimum prefix length you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name. |
| `<rule-id>`  | The prefix list rule number. |
| `<match-id>` | The IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16 min-prefix-len 30
```

- - -

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\> max-prefix-len

Configures the maximum prefix length you want to match. You can specify a value between 0 and 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name.  |
| `<rule-id>` |  The prefix list rule number. |
| `<match-id>` |  The IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16 max-prefix-len 30
```

- - -

## nv set router policy prefix-list \<list-id\> rule \<rule-id\> action

Configures the action to take on a match; `permit` or `deny`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The prefix list name. |
| `<rule-id>` |  The prefix list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 action permit
```

- - -

## nv set router policy prefix-list \<list-id\> type

Configures the type of prefix list; IPv4 or IPv6. The default setting is `ipv4`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist type ipv4
```

- - -

## nv set router policy route-map \<route-map-id\>

Configures the name of the route map you want to use for policy configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` |  The route map name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\>

Configures the route map rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match

Configures the match criteria you want to use for the route map rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-prefix-list \<instance-name\>

Configures the IP prefix list to use as a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>`  |  The route map rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-list prefixlist1
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-prefix-len

Configures the IP address prefix length you want to match. You can specify a value between 0 and 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-len 128
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-list \<instance-name\>

Configures the IP next hop list you want to use as a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-list prefixlist1
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-len

Configures the route map to match an IP nexthop prefix length.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop-len 32
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop \<ipv4\>|\<ipv6\>

Configures the route map to match the IP address of a nexthop.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<ipv4>` or `<ipv6>` | The IPv4 or IPv6 address of the next hop.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop 10.10.101
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-type blackhole

Configures the route map to match a null route (blackhole).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop-type blackhole
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match as-path-list \<instance-name\>

Configures the name of the BGP AS path list you want use in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match as-path-list MYLIST
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match community-list \<instance-name\>

Configures the name of the BGP community list you want to use in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match community-list MYLIST
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match large-community-list \<instance-name\>

Configures the name of the BGP Large Community list you want to use in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match large-community-list MYLIST
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match metric \<value\>

Configures the route metric (the cost values used by routers to determine the best path to a destination network) you want to use as a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match metric 1
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match interface \<interface-name\>|\<vrf-name\>

Configures the interface you want to use as a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match interface swp51
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match tag

Configures the BGP tag you want to use as a match in the route map. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match tag 10
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match source-protocol

Configures the source protocol you want to use as a match in the route map. The source protocol is the protocol through which the switch learns the route. You can specify `bgp`, `connected`, `kernel`, `ospf`, `spf6`, `sharp` or `static`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match source-protocol bgp
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match origin

Configures the BGP origin you want to use as a match in the route map. You can specify `egp`, `igp`, or `incomplete`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match origin igp
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match peer

Configures the BGP peer you want to use as a match in the route map. You can specify `local`, the interface, or the IPv4 or IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match peer swp51
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match local-preference

Configures the local preference of the route you want to match in the route map. You can specify a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match local-preference 300
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match evpn-route-type

Configures the EVPN route type you want to match in the route map. You can specify type 2 (MAC or IP advertisement routes), type 3 (Inclusive multicast Ethernet tag routes), or type 5 (IP prefix routes).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match evpn-route-type macip
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match evpn-vni \<value\>

Configures the VNI ID you want to use a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match evpn-vni 10
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match evpn-default-route

Configures Cumulus Linux to match the EVPN default route in the route map. You can set the value to `on` or `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match evpn-default-route on
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match source-vrf \<vrf-name\>

Configures the source VRF you want to use as a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match source-vrf RED
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match type

Configures the the route types you want to use as a match in the route map. You can specify IPv4 or IPv6 routes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ipv4
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set

Configures the route map rule set.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend

Sets the BGP AS Path you want to prepend for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend as

Sets the BGP AS number to prepend for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend as 65101
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend last-as

Sets the last BGP AS path to prepend for a matched route. You can set a value between 1 and 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend as last-as 4
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set community \<community-id\>

Sets the BGP Community attribute for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<community-id>` | The Community number in AA:NN format or the well-known name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set community 100:100
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set large-community \<large-community-id\>

Sets the Large BGP Community for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<large-community-id>` | The Large Community number in AA:BB:CC format.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set large-community ????
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\>

Sets the aggregator AS Number for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<asn-id>` | The ASN number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set aggregator-as 65101
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\> address \<ipv4-address-id\>

Sets the originating AS of an aggregated route if there is a match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<asn-id>` | The ASN number.|
| `<ipv4-address-id>` |  The IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set aggregator-as 65101 address 10.10.10.01
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-exclude

Configures a set clause in the route map to remove the AS number from the AS Path attribute of the route. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-exclude 65101
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set atomic-aggregate (on|off)

Configures a set clause in the route map to inform BGP peers that the local router is using a less specific (aggregated) route to a destination. You can specify `on` or `off`. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set atomic-aggregate on
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-rt \<route-distinguisher\>

Sets the route target Extended Community for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
|`<route-distinguisher>` | The route distinguisher. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ext-community-rt 64510:1111
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-soo \<route-distinguisher\>

Sets the site-of-origin (SoO) Extended Community for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<route-distinguisher>` |The route distinguisher. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ext-community-soo ????
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-bw

Sets the BGP Extended Community for a matched route. You can specify `cumulative` `multipaths` `cumulative-non-transitive`, or `multipaths-non-transitive`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ext-community-bw multipaths.
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set local-preference

Sets the BGP local preference for a matched route. You can specify a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set local-preference 300
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set weight

Sets the BGP weight value for a matched route. You can specify a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set weight 300
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set metric

Configures a set clause in the route map for the metric value for the destination routing protocol. You can set `metric-plus`, `metric-minus`, `rtt`, `rtt-plus`, or `rtt-minus`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set metric metric-minus
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set metric type

Configures a set clause in the route map for the metric type for routes that match the map. The metric type is used by the the OSPF protocol. You can set OSPF external type 1 metric or OSPF external type 2 metric.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set metric type type-2
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set origin

Configures a set clause in the route map for the BGP origin code for the matched route. You can specify `egp` (the switch learns the origin of the route from an exterior routing protocol with the given autonomous system number) `igp` (the switch learns the the origin of the route from an interior routing protocol), or `incomplete` (the origin of the route is unknown).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set origin igp
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set tag

Configures a set clause in the route map for the tag value for the routing protocol.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set tag 100
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-global \<ipv6\>

Configures a set clause in the route map for IPv6 next hop global address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-global 2001:db8:0002::0a00:0002
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-local \<ipv6\>

Configures a set clause in the route map for the IPv6 next hop local address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-local 2001:db8:0002::0a00:0002
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-prefer-global

Configures a set clause in the route map to use the global address as the IPv6 next hop.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-prefer-global on
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ip-nexthop

Configures a set clause in the route map for the next hop address for an incoming packet regardless of the explicit route for the packet. You can specify the IP address of the peer, or leave it unchanged.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ip-nexthop peer-addr
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set source-ip

Configures a set clause in the route map for the source IP address. You can specify an IPv4 or IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set source-ip 10.1.10.0
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set community-delete-list

Configures a set clause in the route map to remove BGP communities from being advertised to other BGP routes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set community-delete-list communitylist1
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set large-community-delete-list

Configures a set clause in the route map to remove BGP Large Communities from being advertised to other BGP routes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set large-community-delete-list largecommunitylist1
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set originator-id

Configures the BGP IPv4 address of originator you want to set for the route in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set originator-id 10.10.10.4
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set label-index

Configures the label index value you want to set for the route in the route map. You can set a value between 0 and 1048560.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set label-index 1000
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set forwarding-address

Configures the IPv6 forwarding address you want to set for the route in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set forwarding-address 2001:100::1/64
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action

Configures the route map rule action; `permit` or `deny`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action deny

Configures the route map rule action to deny.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 deny
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit

Configures the route map rule action to permit.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 permit
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy

Configures the permit action exit policy.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 permit exit-policy
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy rule \<value\>

Configures the route map to go to specific rule when the matching conditions are met.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 permit exit-policy rule 20
```

- - -

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> description

Configures the route map rule description. If the description is more than one word, enclose it in double quotes (").

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 description none
```

- - -
