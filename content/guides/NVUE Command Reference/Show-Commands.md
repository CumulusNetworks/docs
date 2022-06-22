---
title: Show Commands
author: Cumulus Networks
weight: 20
product: Cumulus Linux
type: nojsscroll
---
This section describes all the `nv show` commands, together with their attributes and identifiers. To see the `[options]` for all the commands, refer to {{<link url="Common-Options" text="Common Options">}}.

## nv show router

Shows global routing configuration settings on the switch. You can see which routing features are on or off, such as BGP, IGMP, PIM, PBR, VRR, VRRP, and adaptive routing.

### Usage

`nv show router [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
|`nexthop-group` | Shows the configuration settings for the next hop group you specify with the `<nexthop-group-id>` identifier.|
| `pbr` | Shows global PBR configuration settings.|
|`policy`| Shows global policy configuration settings.|
|`bgp` | Shows global BGP configuration settings.|
|`ospf` | Shows global OSPF configuration settings.|
`pim` | Shows global PIM configuration settings.|
|`igmp` | Shows global IGMP configuration settings.|
|`vrrp` | Shows global VRRP configuration settings.|
`vrr` | Shows global VRR configuration settings.|
|`adaptive-routing` | Shows adaptive routing configuration settings.|

### Version History

Introduced in Cumulus Linux 4.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router
```

## nv show router nexthop-group

Shows the configuration settings for next hop groups.

### Usage

`nv show router nexthop-group [options] [<nexthop-group-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group name.|

### Version History

Introduced in Cumulus Linux 4.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop-group
```

## nv show router nexthop-group \<nexthop-group-id\>

Shows the configuration settings for the next hop group you specify.

### Usage

`nv show router nexthop-group <nexthop-group-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group name. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `via` |  Shows the next hop in the next hop group.|

### Version History

Introduced in Cumulus Linux 4.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop-group group1
```

## nv show router nexthop-group \<nexthop-group-id\> via

Shows the IP addresses of the next hops in the next hop group.

### Usage

`nv show router nexthop-group <nexthop-group-id> via [options] [<via-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group name.|
| `<via-id>` | The IP address of the next hop. |

### Version History

Introduced in Cumulus Linux 4.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop-group group 1 via
```

## nv show router nexthop-group \<nexthop-group-id\> via \<via-id\>

Shows the egress interface and VRF on the switch.

### Usage

`nv show router nexthop-group <nexthop-group-id> via <via-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
|`<nexthop-group-id>` | The nexthop group name. |
| `<via-id>`| The IP address of the next hop. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop-group group1 via 192.168.0.32
```

## nv show router pbr

Shows global PBR configuration settings.

### Usage

`nv show router pbr [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `map` | Shows PBR map information.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr
```

## nv show router pbr map

Shows settings for PBR maps. If you do not provide a specific map name, this command shows configuration settings for all configured maps.

### Usage

`nv show router pbr map [options] [<pbr-map-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<pbr-map-id>`| The name of the route map. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr map
```

## nv show router pbr map \<pbr-map-id\>

Shows the configuration settings for a PBR map used for policy configuration.

### Usage

`nv show router pbr map <pbr-map-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` | The name of the route map. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rule` | Shows the PBR map rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr map map1
```

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\>

Shows the match and set criteria, and the rule action for a route map.

### Usage

`nv show router pbr map <pbr-map-id> rule <rule-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
|`<pbr-map-id>` | The name of the route map. |
|`<rule-id>`  |  The PBR rule number. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `match` | Shows the PBR match criteria. |
| `action` | Shows the PBR set criteria. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr map map1 rule 1
```

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\> match

Shows the rule match criteria for a route map.

### Usage

`nv show router pbr map <pbr-map-id> rule <rule-id> match [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` | The route map name. |
| `<rule-id>` | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr map map1 rule 1 match
```

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\> action

Shows the route with the next hop group.

### Usage

`nv show router pbr map <pbr-map-id> rule <rule-id> action [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` | The route map name. |
| `<rule-id>` | The PBR rule number. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `nexthop-group` | Shows the route with the nexthop-group. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr map map1 rule 1 action
```

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\> action nexthop-group \<nexthop-group-id\>

Shows information about next hop group you specify, such as if the policy is installed and the IP route table number of the default route.

### Usage

`nv show router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` |  The route map name. |
| `<rule-id>` | The PBR rule number. |
| `<nexthop-group-id>` | The next hop group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr map map1 rule 1 action nexthop-group group1
```

## nv show router policy

Shows route filtering and distribution configuration information. You can see configuration settings for prefix lists, community lists, AS path lists, and route maps.

### Usage

`nv show router policy [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `community-list` | Shows community lists. |
| `as-path-list` |  Shows AS path lists. |
| `ext-community-list` | Shows Extended Community lists. |
| `large-community-list` | Shows Large Community lists. |
| `prefix-list`  | Shows prefix list rules. |
| `route-map` | Shows the collection of route maps. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy community-list

### Usage

`nv show router policy community-list [options] [<list-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  The Community List identifier. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy community-list \<list-id\>

A community list is used for matching BGP community policies.

### Usage

`nv show router policy community-list <list-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  The Community List identifier. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rule` | Shows the Cmmunity List rule. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy community-list \<list-id\> rule

Community list rules

### Usage

`nv show router policy community-list <list-id> rule [options] [<rule-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  The Community List identifier. |
| `<rule-id>` |  The prefix list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy community-list \<list-id\> rule \<rule-id\>

Community list Matching criteria and action rule

### Usage

`nv show router policy community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `community` |  Community expression |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy community-list \<list-id\> rule \<rule-id\> community

Set of community names for community-list

### Usage

`nv show router policy community-list <list-id> rule <rule-id> community [options] [<community-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |
| `<community-id>` | Community number in AA:NN format or well known name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy community-list \<list-id\> rule \<rule-id\> community \<community-id\>

A community name

### Usage

`nv show router policy community-list <list-id> rule <rule-id> community <community-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |
| `<community-id>` | Community number in AA:NN format or well known name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy as-path-list

AS Path lists

### Usage

`nv show router policy as-path-list [options] [<list-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
|`<list-id>` | AS Path List ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy as-path-list \<list-id\>

An AS Path list is used for matching BGP AS Path

### Usage

`nv show router policy as-path-list <list-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
|`<list-id>` |  AS Path List ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rule` | AS Path List rule |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy as-path-list \<list-id>\ rule \<rule-id\>

AS Path list Matching criteria and action rule

### Usage

`nv show router policy as-path-list <list-id> rule <rule-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` | AS Path List ID |
| `<rule-id>` | Prefix List rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy ext-community-list

Extended Community lists

### Usage

`nv show router policy ext-community-list [options] [<list-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` | Community List ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy ext-community-list \<list-id\>

A Extended Community list used for matching BGP communities

### Usage

`nv show router policy ext-community-list <list-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rule` | Extended Community List rule |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy ext-community-list \<list-id\> rule

Extended Community list rules

### Usage

`nv show router policy ext-community-list <list-id> rule [options] [<rule-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id> |` Community List ID |
| `<rule-id>` |  Prefix List rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\>

Extended Community list Matching criteria and action rule

### Usage

`nv show router policy ext-community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ext-community` |  Extended Community expression |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community

A Extended community name

### Usage

`nv show router policy ext-community-list <list-id> rule <rule-id> ext-community [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rt` |  Route Target Extended Community |
| `soo` | Site of Origin Extended Community |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community rt

Set of extended communities

### Usage

`nv show router policy ext-community-list <list-id> rule <rule-id> ext-community rt [options] [<ext-community-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |   Prefix List rule number |
| `<ext-community-id>` |  Community number in AA:NN or IP:NN format |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community rt \<ext-community-id\>

A extended community name

### Usage

`nv show router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |
| `<ext-community-id>` |  Community number in AA:NN or IP:NN format |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community

Set of extended communities

### Usage

`nv show router policy ext-community-list <list-id> rule <rule-id> ext-community soo [options] [<ext-community-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |   Community List ID |
| `<rule-id>` |   Prefix List rule number |
| `<ext-community-id>` |  Community number in AA:NN or IP:NN format |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community soo \<ext-community-id\>

A extended community name

### Usage

`nv show router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |
| `<ext-community-id>` | Community number in AA:NN or IP:NN format |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy large-community-list

Large Community lists

### Usage

`nv show router policy large-community-list [options] [<list-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` | The Community List ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy large-community-list \<list-id\>

A Large Community list used for matching community based BGP policies

### Usage

`nv show router policy large-community-list <list-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` | The Community List ID. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rule` |  Large Community List rules. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy large-community-list \<list-id\> rule

Large Community list rules

### Usage

`nv show router policy large-community-list <list-id> rule [options] [<rule-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy large-community-list \<list-id\> rule \<rule-id\>

Large Community list Matching criteria and action rule

### Usage

`nv show router policy large-community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `large-community` | Large Community expression |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy large-community-list \<list-id\> rule \<rule-id\> large-community

Set of community names for large community list

### Usage

`nv show router policy large-community-list <list-id> rule <rule-id> large-community [options] [<large-community-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |
| `<large-community-id>` |  Community number in AA:BB:CC format |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy large-community-list \<list-id\> rule \<rule-id\> large-community \<large-community-id\>

Set of community names for large community list

### Usage

`nv show router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |
| `<rule-id>` |  Prefix List rule number |
| `<large-community-id>` |  Community number in AA:BB:CC format |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy prefix-list

Prefix list rules

### Usage

`nv show router policy prefix-list [options] [<prefix-list-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` |  Prefix List ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy prefix-list \<prefix-list-id\>

A prefix list is used for matching IPv4 and IPv6 address prefixes.

### Usage

`nv show router policy prefix-list <prefix-list-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` |  Prefix List ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rule` |   Prefix List rule |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy prefix-list \<prefix-list-id\> rule \<rule-id\>

Prefix list Matching criteria and action rule

### Usage

`nv show router policy prefix-list <prefix-list-id> rule <rule-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` |  Prefix List ID |
| `<rule-id>` |   Prefix List rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `match` |   Prefix List rule |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\>

A prefix matc

### Usage

`nv show router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` | Prefix List ID |
| `<rule-id>` |  Prefix List rule number |
| `<match-id>` |  ip v4/v6 prefix, or any |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map

Collection of Route Maps

### Usage

`nv show router policy route-map [options] [<route-map-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\>

A route map is used for policy configuration.

### Usage

`nv show router policy route-map <route-map-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rule` | Route Map rule |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\>

Route Map Matching/setting criteria and action rule

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `match` |   Route Map match |
| `set` |    Route Map set |
| `action` |  Route Map set |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> match

Route map rule match

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> match [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set

Route map rule set

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> set [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `as-path-prepend` | AS Path prepend |
| `community` |  Collection of BGP communities |
| `large-community` |  Collection of large BGP communities |
| `aggregator-as` | Collection of aggregator AS |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend

AS Path prepend

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> set as-path-prepend [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set community \<community-id\>

BGP Community

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> set community <community-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |
| `<community-id>` |  Community number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set large-community \<large-community-id\>

Large BGP Community

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |
| `<large-community-id>` |  Large Community number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\>

Aggregator AS Number

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |
| `<asn-id>` |  Autonomous number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address` |  Set of IPv4 addresses |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\> address \<ipv4-address-id\>

An IPv4 address

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |
| `<asn-id>` |   Autonomous number ` |
| `<ipv4-address-id>`  | IPv4 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> action

Route map rule action

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> action [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `deny` |  Deny action |
| `permit` | Permit action |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> action deny

State details

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> action deny [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> action permit

permit action

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> action permit [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `exit-policy` |  Permit action exit policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy

Permit action exit policy

### Usage

`nv show router policy route-map <route-map-id> rule <rule-id> action permit exit-policy [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  Route Map ID |
| `<rule-id>` |  Sequence to insert or delete from the route-map |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router bgp

BGP global configuration.

### Usage

`nv show router bgp [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `graceful-restart` |  BGP Graceful restart global configuration. |
| `convergence-wait` |  BGP Graceful restart global configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router bgp graceful-restart

BGP Graceful restart global configuration.

### Usage

`nv show router bgp graceful-restart [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router bgp graceful-restart
```

## nv show router bgp convergence-wait

BGP Graceful restart global configuration.

### Usage

`nv show router bgp convergence-wait [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router bgp convergence-wait
```

## nv show router ospf

OSPF global configuration.

### Usage

`nv show router ospf [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timers` |  Timers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router ospf timers

Timers

### Usage

`nv show router ospf timers [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `lsa` |   LSA timers |
| `spf` | SPF timers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router ospf timers lsa

LSA timers

### Usage

`nv show router ospf timers lsa [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router ospf timers spf

SPF timers

### Usage

`nv show router ospf timers spf [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router pim

PIM global configuration.

### Usage

`nv show router pim [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timers` |    Timers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router pim timers

Timers

### Usage

`nv show router pim timers [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router igmp

IGMP global configuration.

### Usage

`nv show router igmp [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router vrrp

VRRP global configuration.

### Usage

`nv show router vrrp [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router vrr

VRR global configuration.

### Usage

`nv show router vrr [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router adaptive-routing

Adaptive routing global configuration.

### Usage

`nv show router adaptive-routing [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform

Top-level container for the components in the system. This node represents a system component inventory, which includes hardware and software elements.

### Usage

`nv show platform [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `capabilities` |  Capabilities of this platform |
| `hardware`   | The platform's hardware |
| `environment` |   Platform environment information |
| `software` |    The platform's software |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform capabilities

Capabilities of this platform

### Usage

`nv show platform capabilities [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware

The platform's hardware

### Usage

`nv show platform hardware [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `component` | Set of components making up the platform. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component

Set of components making up the platform.

### Usage

`nv show platform hardware component [options] [<component-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\>

A component in the platform.

### Usage

`nv show platform hardware component <component-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `linecard` | Properties of a linecard component |
| `port` |   Set of physical ports on this component |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\> linecard

Properties of a linecard component

### Usage

`nv show platform hardware component <component-id> linecard [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\> port

Set of physical ports on this component

### Usage

`nv show platform hardware component <component-id> port [options] [<port-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |
| `<port-id>` |  Physical port identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\> port \<port-id\>

A physical port on the component.

### Usage

`nv show platform hardware component <component-id> port <port-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |
| `<port-id>` |  Physical port identifier |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `breakout-mode` | Set of breakout modes supported by this port |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\> port \<port-id\> breakout-mode

Set of breakout modes

### Usage

`nv show platform hardware component <component-id> port <port-id> breakout-mode [options] [<mode-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |
| `<port-id>` | Physical port identifier |
| `<mode-id>` |  Breakout mode identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\> port \<port-id\> breakout-mode \<mode-id\>

A breakout mode

### Usage

`nv show platform hardware component <component-id> port <port-id> breakout-mode <mode-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |
| `<port-id>` | Physical port identifier |
| `<mode-id>` |  Breakout mode identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment

Platform environment information

### Usage

`nv show platform environment [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `fan` | The fans on the switch. |
| `sensor` | The sensors on the switch. |
| `psu` |  The PSUs on the switch. |
| `led` |  The LEDs on the switch. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment fan

The fans on the switch.

### Usage

`nv show platform environment fan [options] [<fan-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<fan-id>` |   Physical fan identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment fan \<fan-id\>

A physical fan on the component.

### Usage

`nv show platform environment fan <fan-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<fan-id>` |   Physical fan identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment sensor

The sensors on the switch.

### Usage

`nv show platform environment sensor [options] [<sensor-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<sensor-id>` |  Physical sensor identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment sensor \<sensor-id\>

A physical sensor on the component.

### Usage

`nv show platform environment sensor <sensor-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<sensor-id>` |  Physical sensor identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment psu

The PSUs on the switch.

### Usage

`nv show platform environment psu [options] [<psu-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<psu-id>` |  Physical PSU identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment psu \<psu-id\>

A PSU

### Usage

`nv show platform environment psu <psu-id> [options]`


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<psu-id>` |  Physical PSU identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment led

The LEDs on the switch.

### Usage

`nv show platform environment led [options] [<led-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<led-id>` |  Physical LED identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment led \<led-id\>

A LED

### Usage

nv show platform environment led \<led-id\> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<led-id>` |  Physical LED identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform software

The platform's software

### Usage

`nv show platform software [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `installed` |  List of installed software |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform software installed

List of installed software

### Usage

`nv show platform software installed [options] [<installed-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<installed-id>` | Package name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform software installed \<installed-id\>

An installed package

### Usage

`nv show platform software installed <installed-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<installed-id>` |  Package name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge

Properties associated with an instance of a bridge.

### Usage

`nv show bridge [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `domain` |  Bridge domains |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain

Bridge domains

### Usage

`nv show bridge domain [options] [<domain-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\>

Bridge domain

### Usage

`nv show bridge domain <domain-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `stp`  |   attributes related to global stp |
| `multicast`    | Configure multicast on the bridge |
| `vlan`         | Set of vlans in the bridge domain. Only applicable when the domain type is "vlan-aware". |
| `mac-table`    | L2 FDB |
| `mdb`          | Set of mdb entries in the bridge domain |
| `router-port`  | Set of multicast router ports |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> stp

attributes related to global stp

### Usage

`nv show bridge domain <domain-id> stp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `state` | The state of STP on the bridge |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> stp state

The state of STP on the bridge

### Usage

`nv show bridge domain <domain-id> stp state [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> multicast

Configure multicast on the bridge

### Usage

`nv show bridge domain <domain-id> multicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` Domain | 

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  snooping              IGMP/MLD snooping configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> multicast snooping

IGMP/MLD snooping configuration

### Usage

`nv show bridge domain <domain-id> multicast snooping [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `querier` |  IGMP/MLD querier configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> multicast snooping querier

IGMP/MLD querier configuration

### Usage

`nv show bridge domain <domain-id> multicast snooping querier [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\>

A VLAN tag identifier

### Usage

`nv show bridge domain <domain-id> vlan <vid> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid> |     VLAN ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `vni`       | L2 VNI |
| `ptp`       | VLAN PTP configuration. Inherited by interfaces in this VLAN. |
| `multicast` | Configure multicast on the vlan |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\>

VNI

### Usage

`nv show bridge domain <domain-id> vlan <vid> vni <vni-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>`          | Domain |
| `<vid>`                | VLAN ID |
| `<vni-id>`             | VxLAN ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flooding`  | Handling of BUM traffic |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding

Handling of BUM traffic

### Usage

`nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding [options] [<attribute> ...]`

### Identifiers

| --------- | -------------- |
| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>`          | Domain |
| `<vid>`                | VLAN ID |
| `<vni-id>`             | VxLAN ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `head-end-replication` | BUM traffic is replicated and individual copies sent to remote destinations.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication <hrep-id>

Set of IPv4 unicast addresses or "evpn".

### Usage

`nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id> [options]`

### Identifiers

| --------- | -------------- |
| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |
| `<vni-id>`   | VxLAN ID |
| `<hrep-id>`  | IPv4 unicast addresses or "evpn" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> ptp

VLAN PTP configuration.  Inherited by interfaces in this VLAN.

### Usage

`nv show bridge domain <domain-id> vlan <vid> ptp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> multicast

Configure multicast on the vlan

### Usage

`nv show bridge domain <domain-id> vlan <vid> multicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `snooping`  | IGMP/MLD snooping configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> multicast snooping

IGMP/MLD snooping configuration

### Usage

`nv show bridge domain <domain-id> vlan <vid> multicast snooping [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `querier`  | IGMP/MLD querier configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier

IGMP/MLD querier configuration

### Usage

`nv show bridge domain <domain-id> vlan <vid> multicast snooping querier [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> mac-table

L2 FDB

### Usage

`nv show bridge domain <domain-id> mac-table [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> mdb

Set of mdb entries in the bridge domain

### Usage

`nv show bridge domain <domain-id> mdb [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> router-port

Set of multicast router ports

### Usage

`nv show bridge domain <domain-id> router-port [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag

Global Multi-chassis Link Aggregation properties

### Usage

`nv show mlag [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `lacp-conflict`         | Configure the mlag lacp-conflict parameters |
| `consistency-checker`   | Consistency-checker parameters for mlag nodes |
| `backup`                | Set of MLAG backups |
| `fdb`                   | Macs owned by local/peer mlag switch |
| `mdb`                   | Mdb owned by local/peer switch |
| `multicast-router-port`  | Multicast Router Ports owned by local/peer mlag switch |
| `vni`                   | Local VNIs |
| `lacpdb`                | Mlag Local Lacp Info |
| `neighbor`              | Local/peer Neighbour Entries|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacp-conflict

Configure the mlag lacp-conflict parameters

### Usage

`nv show mlag lacp-conflict [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag consistency-checker

Show the mlag consistency-checker parameters

### Usage

`nv show mlag consistency-checker [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `global`    | mlag global consistency-checker |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag consistency-checker global

Global Consistency-checker

### Usage

`nv show mlag consistency-checker global [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag backup

Set of MLAG backups

### Usage

`nv show mlag backup [options] [<backup-ip> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<backup-ip>` | Backup IP of MLAG peer |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag backup \<backup-ip\>

alternative ip address or interface for peer to reach us

### Usage

`nv show mlag backup <backup-ip> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| <backup-ip> |  Backup IP of MLAG peer |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb

Set of all mlag macs

### Usage

`nv show mlag fdb [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`      | Locally learnt macs |
| `peer`       | Peer Synced Macs |
| `permanent`  | Permanent Macs installed on local/peer |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb local

Set of MLAG Macs learnt/sync between mlag peers

### Usage

`nv show mlag fdb local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb peer

Set of MLAG Macs learnt/sync between mlag peers

### Usage

`nv show mlag fdb peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb permanent

Permanent Mac Entry

### Usage

`nv show mlag fdb permanent [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag mdb

Set of Mlag Multicast Database Entries

### Usage

`nv show mlag mdb [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`    | Local Multicast Database |
| `peer `    | Peer Multicast Database |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag mdb local

Multicast Groups Info

### Usage

`nv show mlag mdb local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag mdb peer

Multicast Groups Info

### Usage

`nv show mlag mdb peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag multicast-router-port

Set of all Mlag Multicast Router Ports

### Usage

`nv show mlag multicast-router-port [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`   | Local Multicast Router Ports |
| `peer`    | Peer Multicast Router Ports |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag multicast-router-port local

Multicast Router Ports

### Usage

`nv show mlag multicast-router-port local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag multicast-router-port peer

### Usage

`nv show mlag multicast-router-port peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag vni

Set of all vnis

### Usage

`nv show mlag vni [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`  | Local Vnis |
| `peer`   | Peer Vnis |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag vni local

Set of VNIs configured

### Usage

`nv show mlag vni local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag vni peer

Set of VNIs configured

### Usage

`nv show mlag vni peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacpdb

Set of all mlag local/peer lacpdb

### Usage

`nv show mlag lacpdb [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local` | Local Lacp Database |
| `peer`  | Peer Lacp Database |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacpdb local

Lacp DB

### Usage

`nv show mlag lacpdb local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacpdb peer

Lacp DB

### Usage

`nv show mlag lacpdb peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag neighbor

Set of all mlag neigh entries

### Usage

`nv show mlag neighbor [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `dynamic`     | Dynamic Neighbor |
| `permanent`   | Permanent Neighbor |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag neighbor dynamic

Neighs

### Usage

`nv show mlag neighbor dynamic [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag neighbor permanent

Permanent Neighbors 
### Usage

`nv show mlag neighbor permanent [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn

Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Usage

`nv show evpn [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route-advertise`  | Route advertising |
| `dad`              | Advertise |
| `evi`              | EVI |
| `multihoming`      | Multihoming global configuration parameters |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn route-advertise

### Usage

`nv show evpn route-advertise [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn dad

Duplicate address detection

### Usage

`nv show evpn dad [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `duplicate-action`  | Action to take when a MAC is flagged as a possible duplicate. If 'warning-only', generates a log message. If 'freeze', further move events for the MAC will not be acted upon. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn dad duplicate-action

Handling of BUM traffic

### Usage

`nv show evpn dad duplicate-action [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `freeze`  |  Further move events for the MAC will not be acted upon. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn dad duplicate-action freeze

Advertise

### Usage

`nv show evpn dad duplicate-action freeze [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi

EVIs

### Usage

`nv show evpn evi [options] [<evi-id> ...]`

### Identifiers

| Identifier |  Description   |
| `<evi-id>`    |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\>

Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Usage

`nv show evpn evi <evi-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| `<evi-id>`    |  VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route-advertise` | Route advertise |
| `route-target`    | Route targets |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-advertise

Route advertise

### Usage

`nv show evpn evi <evi-id> route-advertise [options]`

### Identifiers

| Identifier |  Description   |
| `<evi-id>`    |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target

EVPN control plane config and info for VRF

### Usage

`nv show evpn evi <evi-id> route-target [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| `<evi-id>`    |  VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `export` |  Route targets to export |
| `import` |  Route targets to import |
| `both`   |  Route targets to import and export |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target export

Set of route target identifiers

### Usage

`nv show evpn evi <evi-id> route-target export [options] [<rt-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target export \<rt-id\>

A route target identifier

### Usage

`nv show evpn evi <evi-id> route-target export <rt-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target import

Set of route target identifiers

### Usage

`nv show evpn evi <evi-id> route-target import [options] [<rt-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target import \<rt-id\>

A route target identifier

### Usage

`nv show evpn evi <evi-id> route-target import <rt-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target both

Set of route target identifiers

### Usage

`nv show evpn evi <evi-id> route-target both [options] [<rt-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target both \<rt-id\>

A route target identifier

### Usage

`nv show evpn evi <evi-id> route-target both <rt-id> [options]`

### Identifiers

|  Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |  VRF |
| `<rt-id>` |Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn multihoming

Multihoming global configuration parameters

### Usage

`nv show evpn multihoming [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ead-evi-route`  | Ethernet Auto-discovery per EVPN instance routes |
| `segment`        | Multihoming interface segment |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn multihoming ead-evi-route

### Usage

`nv show evpn multihoming ead-evi-route [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn multihoming segment

Multihoming interface segment

### Usage

`nv show evpn multihoming segment [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos

QOS

### Usage

`nv show qos [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `roce` | Properties associated with the RDMA over Converged Ethernet (RoCE) feature. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos roce

Properties associated with the RDMA over Converged Ethernet (RoCE) feature.

### Usage

`nv show qos roce [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `prio-map` | RoCE PCP/DSCP->SP mapping configurations |
| `tc-map`   | RoCE SP->TC mapping and ETS configurations |
| `pool-map` | System Roce pool config |
| `pool`     | System Roce pools |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos roce prio-map

RoCE PCP/DSCP->SP mapping configurations

### Usage

`nv show qos roce prio-map [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos roce tc-map

RoCE SP->TC mapping and ETS configurations

### Usage

`nv show qos roce tc-map [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos roce pool-map

System Roce pool config

### Usage

`nv show qos roce pool-map [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos roce pool

System Roce pools

### Usage

`nv show qos roce pool [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface

Interfaces

### Usage

`nv show interface [options] [<interface-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\>

An interface

### Usage

`nv show interface <interface-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `pluggable` | An interface sfp details|
| `router`    | interface router|
| `bond`      | The state of the interface|
| `bridge`    | attributed related to a bridged interface|
| `ip`        | IP configuration for an interface|
| `lldp`      | LLDP on for an interface|
| `link`      | An physical interface|
| `qos`       | QOS|
| `evpn`      | EVPN control plane config and info for VRF|
| `acl`       | Interface ACL rules|
| `ptp`       | Interface Specific PTP configuration.|
| `tunnel`    | The state of the interface|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> pluggable

An interface sfp details

### Usage

`nv show interface <interface-id> pluggable [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router

interface router

### Usage

`nv show interface <interface-id> router [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `pbr`                   | PBR interface configuration.|
| `ospf`                  | OSPF interface configuration.|
| `pim`                   | PIM interface configuration.|
| `adaptive-routing`      | Adaptive routing interface configuration.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pbr

PBR interface configuration.

### Usage

`nv show interface <interface-id> router pbr [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `map`   | PBR map to use on this interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pbr map \<pbr-map-id\>

Interface Pbr map

### Usage

`nv show interface <interface-id> router pbr map <pbr-map-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<pbr-map-id>`   |  Route Map ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router ospf

OSPF interface configuration.

### Usage

`nv show interface <interface-id> router ospf [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timers`                | `Timers configuration |
| `authentication`        | `md5 authentication configuration |
| `bfd`                   | `BFD configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router ospf timers

Timers configuration

### Usage

`nv show interface <interface-id> router ospf timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router ospf authentication

md5 authentication configuration

### Usage

`nv show interface <interface-id> router ospf authentication [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router ospf bfd

BFD configuration

### Usage

`nv show interface <interface-id> router ospf bfd [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim

PIM interface configuration.

### Usage

`nv show interface <interface-id> router pim [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
|`timers`                | Timers |
|`bfd`                   | BFD configuration |
|`address-family`        | Address family specific configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim timers

Timers

### Usage

`nv show interface <interface-id> router pim timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim bfd

BFD configuration

### Usage

`nv show interface <interface-id> router pim bfd [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim address-family

Address family specific configuration

### Usage

`nv show interface <interface-id> router pim address-family [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4-unicast` | IPv4 unicast address family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim address-family ipv4-unicast

IPv4 unicast address family

### Usage

`nv show interface <interface-id> router pim address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-rp` |   Allow RP feature, which allows RP address to be accepts for the received |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim address-family ipv4-unicast allow-rp

Allow RP feature, which allows RP address to be accepts for the received

### Usage

`nv show interface <interface-id> router pim address-family ipv4-unicast allow-rp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router adaptive-routing

Adaptive routing interface configuration.

### Usage

`nv show interface <interface-id> router adaptive-routing [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bond

The state of the interface

### Usage

`nv show interface <interface-id> bond [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `member` | Set of bond members |
| `mlag`   | MLAG configuration on the bond interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bond member <member-id>

A bond member

### Usage

`nv show interface <interface-id> bond member <member-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<member-id>`  | Bond memer interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bond mlag

MLAG configuration on the bond interface

### Usage

`nv show interface <interface-id> bond mlag [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `lacp-conflict`         | Configure the mlag lacp-conflict parameters |
| `consistency-checker`   | Consistency-checker parameters for mlag interfaces |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bond mlag lacp-conflict

Configure the mlag lacp-conflict parameters

### Usage

`nv show interface <interface-id> bond mlag lacp-conflict [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bond mlag consistency-checker

Interface MLAG Consistency-checker

### Usage

`nv show interface <interface-id> bond mlag consistency-checker [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bridge

attributed related to a bridged interface

### Usage

`nv show interface <interface-id> bridge [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `domain`  |  Bridge domains on this interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bridge domain \<domain-id\>

Bridge domain on this interface

### Usage

`nv show interface <interface-id> bridge domain <domain-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<domain-id>`   | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `stp`  |attributed related to a stpd interface
| `vlan` | Set of allowed vlans for this bridge domain on this  interface. If "all", inherit all vlans from the bridge domain, if appropriate. This is the default. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bridge domain \<domain-id\> stp

attributed related to a stpd interface

### Usage

`nv show interface <interface-id> bridge domain <domain-id> stp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<domain-id>`   | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bridge domain \<domain-id\> vlan \<vid\>

A VLAN tag identifier

### Usage

`nv show interface <interface-id> bridge domain <domain-id> vlan <vid> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<domain-id>`   | Domain |
| `<vid>`     | VLAN ID, or all |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip

IP configuration for an interface

### Usage

`nv show interface <interface-id> ip [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address`               | ipv4 and ipv6 address |
| `neighbor`              | IP neighbors |
| `vrr`                   | Configuration for VRR |
| `gateway`               | default ipv4 and ipv6 gateways |
| `ipv4`                  | IPv4 configuration for an interface |
| `ipv6`                  | IPv6 configuration for an interface |
| `igmp`                  | Configuration for IGMP|
| `vrrp`                  | Configuration for VRRP |
| `neighbor-discovery`    | Neighbor discovery configuration for an interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip address \<ip-prefix-id\>

An IP address with prefix

### Usage

`nv show interface <interface-id> ip address <ip-prefix-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<ip-prefix-id>`  |  IPv4 or IPv6 address and route prefix in CIDR notation|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor

IP neighbors

### Usage

`nv show interface <interface-id> ip neighbor [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4`  | IPv4 neighbors |
| `ipv6`  | IPv6 neighbors |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor ipv4 \<neighbor-id\>

A neighbor

### Usage

`nv show interface <interface-id> ip neighbor ipv4 <neighbor-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>`  | The IPv4 address of the neighbor node.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor ipv6 \<neighbor-id\>

A neighbor

### Usage

`nv show interface <interface-id> ip neighbor ipv6 <neighbor-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>`  | The IPv4 address of the neighbor node.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id\> ip vrr

Configuration for VRR

### Usage

`nv show interface <interface-id> ip vrr [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address`  | Virtual addresses with prefixes
| `state`  | The state of the interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip vrr address \<ip-prefix-id\>

An IP address with prefix

### Usage

`nv show interface <interface-id> ip vrr address <ip-prefix-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<ip-prefix-id>`| IPv4 or IPv6 address and route prefix in CIDR notation|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip vrr state

The state of the interface

### Usage

`nv show interface <interface-id> ip vrr state [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip gateway \<ip-address-id\>

An IP address

### Usage

`nv show interface <interface-id> ip gateway <ip-address-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<ip-address-id>`  | IPv4 or IPv6 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip ipv4

IPv4 configuration for an interface

### Usage

`nv show interface <interface-id> ip ipv4 [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip ipv6

IPv6 configuration for an interface

### Usage

`nv show interface <interface-id> ip ipv6 [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip igmp

Configuration for IGMP

### Usage

`nv show interface <interface-id> ip igmp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `static-group`    | IGMP static mutlicast mroutes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip igmp static-group \<static-group-id\>

IGMP static multicast mroute

### Usage

`nv show interface <interface-id> ip igmp static-group <static-group-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<static-group-id>` |  IGMP static multicast mroute destination |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip vrrp

Configuration for VRRP

### Usage

`nv show interface <interface-id> ip vrrp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `virtual-router`   | Group of virtual gateways implemented with VRRP|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\>

A virtual gateway implemented with VRRP

### Usage

`nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<virtual-router-id>` |  Virtual Router IDentifier (VRID)|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address`  |     A set of virtual addresses for VRRPv3|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address \<ip-address-id\>

An IP address

### Usage

`nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<virtual-router-id>`    | Virtual Router IDentifier (VRID) |
| `<ip-address-id>`        | IPv4 or IPv6 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor-discovery

Neighbor discovery configuration for an interface

### Usage

`nv show interface <interface-id> ip neighbor-discovery [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rdnss`                 | Recursive DNS server addresses to be advertised using type 25 option RFC8016 |
| `prefix`                | IPv6 prefix configuration |
| `dnssl`                 | Advertise DNS search list using type 31 option RFC8106 |
| `router-advertisement`  | Router advertisement |
| `home-agent`            | Home agent configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor-discovery rdnss \<ipv6-address-id\>

A recursive DNS server

### Usage

`nv show interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<ipv6-address-id>`  |   IPv6 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\>

A IPv6 prefix

### Usage

`nv show interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<ipv6-address-id>`  |   IPv6 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor-discovery dnssl \<domain-name-id\>

A DNS search list

### Usage

`nv show interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<domain-name-id>`   |  The domain portion of a hostname (RFC 1123) or an internationalized hostname (RFC 5890).|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor-discovery router-advertisement

Router advertisement configuration for an interface

### Usage

`nv show interface <interface-id> ip neighbor-discovery router-advertisement [options]  

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor-discovery home-agent

Indicates to neighbors that this router acts as a Home Agent and includes a Home Agent Option. Not defined by default

### Usage

`nv show interface <interface-id> ip neighbor-discovery home-agent [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> lldp

LLDP on for an interface

### Usage

`nv show interface <interface-id> lldp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `neighbor` | LLDP neighbors |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\>

LLDP on an interface

### Usage

`nv show interface <interface-id> lldp neighbor <neighbor-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>` |  System generated identifier for the neighbor on the interface|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `bridge`  |  Bridge properties, such as VLANs, of the neighbor|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge

An LLDP bridge

### Usage

`nv show interface <interface-id> lldp neighbor <neighbor-id> bridge [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>` |  System generated identifier for the neighbor on the interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `vlan` | Set of vlans understood by this neighbor.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge vlan \<vid\>

A VLAN tag identifier

### Usage

`nv show interface <interface-id> lldp neighbor <neighbor-id> bridge vlan <vid> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>` |  System generated identifier for the neighbor on the interface |
| `<vid>` | VLAN ID, or all |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> link

An physical interface

### Usage

`nv show interface <interface-id> link [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `state`                | The state of the interface|
| `dot1x`                | An physical interface|
| `stats`                | Interface stats|
| `traffic-engineering`  | Traffic engineering stats|
| `flag`                 | link flags|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> link state

The state of the interface

### Usage

`nv show interface <interface-id> link state [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> link dot1x

An physical interface

### Usage

`nv show interface <interface-id> link dot1x [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> link stats

Interface stats

### Usage

`nv show interface <interface-id> link stats [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> link traffic-engineering

Traffic engineering stats

### Usage

`nv show interface <interface-id> link traffic-engineering [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> link flag

link flags

### Usage

`nv show interface <interface-id> link flag [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos

### Usage

`nv show interface <interface-id> qos [options] [<attribute> ...]

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `counters` | |
| `roce` | |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos counters

Interface QoS counters

### Usage

`nv show interface <interface-id> qos counters [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `port-stats`            | `QoS Statistics for Interface`
| `egress-queue-stats`    | `Egress queue statistics per egress traffic-class`
| `ingress-buffer-stats`  | `Ingress Buffer statistics per priority-group`
| `pfc-stats`             | `PFC statistics per internal switch-priority`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos counters port-stats

QoS Statistics for Interface

### Usage

`nv show interface <interface-id> qos counters port-stats [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rx-stats`   | QoS Rx Statistics for Interface |
| `tx-stats` |  QoS Tx Statistics for Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos counters port-stats rx-stats

QoS Rx Statistics for Interface

### Usage

`nv show interface <interface-id> qos counters port-stats rx-stats [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos counters port-stats tx-stats

QoS Tx Statistics for Interface

### Usage

`nv show interface <interface-id> qos counters port-stats tx-stats [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos counters egress-queue-stats

Egress queue statistics per egress traffic-class

### Usage

`nv show interface <interface-id> qos counters egress-queue-stats [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos counters ingress-buffer-stats

Ingress Buffer statistics per priority-group

### Usage

`nv show interface <interface-id> qos counters ingress-buffer-stats [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos counters pfc-stats

PFC statistics per internal switch-priority

### Usage

`nv show interface <interface-id> qos counters pfc-stats [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos roce

### Usage

`nv show interface <interface-id> qos roce [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `counters` | |
| `status` | |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos roce counters

Interface roce counters

### Usage

`nv show interface <interface-id> qos roce counters [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos roce status

Interface status

### Usage

`nv show interface <interface-id> qos roce status [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `pool-map`   |  Interface Roce pools|
| `prio-map`  |  RoCE PCP/DSCP->SP mapping configurations|
| `tc-map  | RoCE SP->TC mapping and ETS configurations|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos roce status pool-map

Interface Roce pools

### Usage

`nv show interface <interface-id> qos roce status pool-map [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos roce status prio-map

RoCE PCP/DSCP->SP mapping configurations

### Usage

`nv show interface <interface-id> qos roce status prio-map [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> qos roce status tc-map

RoCE SP->TC mapping and ETS configurations

### Usage

`nv show interface <interface-id> qos roce status tc-map [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> evpn

EVPN control plane config and info for VRF

### Usage

`nv show interface <interface-id> evpn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
|  `multihoming`    | Multihoming interface configuration parameters|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> evpn multihoming

Multihoming interface configuration parameters

### Usage

`nv show interface <interface-id> evpn multihoming [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `segment`   |  Multihoming interface segment|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> evpn multihoming segment

Multihoming interface segment

### Usage

`nv show interface <interface-id> evpn multihoming segment [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> acl \<acl-id\>

An ACL is used for matching packets and take actions

### Usage

`nv show interface <interface-id> acl <acl-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<acl-id>` |     ACL ID|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | ACL applied for inbound direction |
| `outbound` | ACL applied for outbound direction |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> acl \<acl-id\> inbound

inbound direction

### Usage

`nv show interface <interface-id> acl <acl-id> inbound [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<acl-id>` | ACL ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `control-plane`   | ACL applied for control plane |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> acl \<acl-id\> inbound control-plane

State details

### Usage

`nv show interface <interface-id> acl <acl-id> inbound control-plane [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<acl-id>` | ACL ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> acl \<acl-id\> outbound

State details

### Usage

`nv show interface <interface-id> acl <acl-id> outbound [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<acl-id>` | ACL ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `control-plane` | |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> acl \<acl-id\> outbound control-plane

State details

### Usage

`nv show interface <interface-id> acl <acl-id> outbound control-plane [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<acl-id>` | ACL ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ptp

Interface Specific PTP configuration.

### Usage

`nv show interface <interface-id> ptp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timers`  |  Interface PTP timers |
| `counters`  |  Interface PTP counters |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ptp timers

Interface PTP timers

### Usage

`nv show interface <interface-id> ptp timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ptp counters

Interface PTP counters

### Usage

`nv show interface <interface-id> ptp counters [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> tunnel

The state of the interface

### Usage

`nv show interface <interface-id> tunnel [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>` |  Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service

A service

### Usage

`nv show service [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `dns`           collection of DNS |
| `syslog`        collection of syslog |
| `ntp`           NTPs |
| `dhcp-relay`    DHCP-relays |
| `dhcp-relay6`   DHCP-relays |
| `ptp`           Collection of PTP instances |
| `dhcp-server`   DHCP-servers |
| `dhcp-server6`  DHCP-servers6 |
| `lldp`          Global LLDP |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dns

collection of DNS

### Usage

`nv show service dns [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dns \<vrf-id\>

Domain Name Service

### Usage

`nv show service dns <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `server` |   Remote DNS servers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dns \<vrf-id\> server \<dns-server-id\>

A remote DNS server

### Usage

`nv show service dns <vrf-id> server <dns-server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<dns-server-id>`  | IPv4 or IPv6 address of a DNS server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service syslog

collection of syslog

### Usage

`nv show service syslog [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service syslog \<vrf-id\>

Domain Name Service

### Usage

`nv show service syslog <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `server` | Remote DNS servers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service syslog \<vrf-id\> server \<server-id\>

A remote DNS server

### Usage

`nv show service syslog <vrf-id> server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>` | Hostname or IP address of a syslog server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ntp

NTPs

### Usage

`nv show service ntp [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ntp \<vrf-id\>

Network Time Protocol

### Usage

`nv show service ntp <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `server` | Remote NTP Servers |
| `pool`  |  Remote NTP Servers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ntp \<vrf-id\> server \<server-id\>

A remote NTP Server

### Usage

`nv show service ntp <vrf-id> server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>` |   Hostname or IP address of the NTP server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ntp \<vrf-id\> pool \<server-id\>

A remote NTP Server

### Usage

`nv show service ntp <vrf-id> pool <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>` |   Hostname or IP address of the NTP server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay

DHCP-relays

### Usage

`nv show service dhcp-relay [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay \<vrf-id\>

DHCP relay

### Usage

`nv show service dhcp-relay <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `server`                | DHCP servers |
| `interface`             | Set of interfaces on which to handle DHCP relay traffic |
| `giaddress-interface`   | Configures DHCP relay giaddress on the interfaes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay \<vrf-id\> server \<server-id\>

A DHCP server

### Usage

`nv show service dhcp-relay <vrf-id> server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>`   | DHCP server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay \<vrf-id\> interface \<interface-id\>

### Usage

`nv show service dhcp-relay <vrf-id> interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>` |  DHCP relay interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay \<vrf-id\> giaddress-interface \<interface-id\>

### Usage

`nv show service dhcp-relay <vrf-id> giaddress-interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>`  | DHCP relay giaddress interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6

### Usage

`nv show service dhcp-relay6 [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6 \<vrf-id\>

### Usage

`nv show service dhcp-relay6 <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `interface`  | DHCP relay interfaces |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6 \<vrf-id\> interface

DHCP relay interfaces

### Usage

`nv show service dhcp-relay6 <vrf-id> interface [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `upstream`   | Configures DHCP relay on the interfaes. |
| `downstream` | Configures DHCP relay on the interfaes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\>

An interface on which DPCH relay is configured.

### Usage

`nv show service dhcp-relay6 <vrf-id> interface upstream <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>` |  DHCP relay interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\>

An interface on which DPCH relay is configured.

### Usage

`nv show service dhcp-relay6 <vrf-id> interface downstream <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>` |  DHCP relay interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp

Collection of PTP instances

### Usage

`nv show service ptp [options] [<instance-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\>

Global PTP configuration.

### Usage

`nv show service ptp <instance-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `acceptable-master`     | Collection of acceptable masters |
| `monitor`               | PTP monitor configuration |
| `current`               | Local states learned from the exchange of PTP messages |
| `clock-quality`         | Clock Quality Status |
| `parent`                | Local states learned from the exchange of PTP messages |
| `time-properties`       | Time attributes of the clock |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> acceptable-master

Collection of acceptable masters

### Usage

`nv show service ptp <instance-id> acceptable-master [options] [<clock-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |
| `<clock-id>`  |  Clock ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> acceptable-master <clock-id>

List of clocks that the local clock can accept as master clock

### Usage

`nv show service ptp <instance-id> acceptable-master <clock-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |
| `<clock-id>`  |  Clock ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> monitor

PTP monitor configuration

### Usage

`nv show service ptp <instance-id> monitor [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timestamp-log`  | Collection of violations logs |
| `violations`     | PTP violations |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> monitor timestamp-log

### Usage

`nv show service ptp <instance-id> monitor timestamp-log [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> monitor violations

PTP violations

### Usage

`nv show service ptp <instance-id> monitor violations [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `log` |  PTP violations log |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> monitor violations log

PTP violations log

### Usage

`nv show service ptp <instance-id> monitor violations log [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `acceptable-master`     | Collection of master violations |
| `forced-master`         | Collection of master violations |
| `max-offset`            | Collection of violations logs |
| `min-offset`            | Collection of violations logs |
| `path-delay`            | Collection of violations logs |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> monitor violations log acceptable-master

Collection of master violations

### Usage

`nv show service ptp <instance-id> monitor violations log acceptable-master [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> monitor violations log forced-master

Collection of master violations

### Usage

`nv show service ptp <instance-id> monitor violations log forced-master [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> monitor violations log max-offset

Collection of violations logs

### Usage

`nv show service ptp <instance-id> monitor violations log max-offset [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> monitor violations log min-offset

Collection of violations logs

### Usage

`nv show service ptp <instance-id> monitor violations log min-offset [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> monitor violations log path-delay

Collection of violations logs

### Usage

`nv show service ptp <instance-id> monitor violations log path-delay [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> current

Local states learned from the exchange of PTP messages

### Usage

`nv show service ptp <instance-id> current [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> clock-quality

Clock Quality Status

### Usage

`nv show service ptp <instance-id> clock-quality [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> parent

Local states learned from the exchange of PTP messages 

### Usage

`nv show service ptp <instance-id> parent [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
|`grandmaster-clock-quality` | Clock Quality Status |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> parent grandmaster-clock-quality

Clock Quality Status

### Usage

`nv show service ptp <instance-id> parent grandmaster-clock-quality [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp \<instance-id\> time-properties

Time attributes of the clock

### Usage

`nv show service ptp <instance-id> time-properties [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>` | PTP instance number. It is used for management  purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server

DHCP-servers

### Usage

`nv show service dhcp-server [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\>

Dynamic Host Configuration Protocol Server

### Usage

`nv show service dhcp-server <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `interface`             | Assign DHCP options to clients directly attached to these interfaes. |
| `pool`                  | DHCP Pools |
| `domain-name`           | DHCP domain names |
| `domain-name-server`    | DHCP domain name servers |
| `static`                | DHCP clients with fixed IP address assignments |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> interface \<interface-id\>

An interface on which DPCH clients are attached.

### Usage

`nv show service dhcp-server <vrf-id> interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>`  | DHCP client interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\>

DHCP Pool

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` |  DHCP pool subnet. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `domain-name-server`    | DHCP domain name servers |
| `domain-name`           | DHCP domain names |
| `gateway`               | DHCP gateway |
| `range`                 | IP Address range assignments |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

A remote DNS server

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<pool-id>` |  DHCP pool subnet. |
| `<server-id>` | DNS server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

TBD

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` | DHCP pool subnet. |
| `<domain-name-id>` | DHCP domain name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> gateway \<gateway-id\>

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id> [options]`



  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` | DHCP pool subnet. |
| `<gateway-id>` |  Gateway |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\>

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> range <range-id> [options]`



  DHCP Pool range

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` | DHCP pool subnet. |
| `<range-id>` |   DHCP client interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> domain-name \<domain-name-id\>

TBD

### Usage

`nv show service dhcp-server <vrf-id> domain-name <domain-name-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<domain-name-id>` | DHCP domain name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> domain-name-server \<server-id\>

A remote DNS server

### Usage

`nv show service dhcp-server <vrf-id> domain-name-server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>` |  DNS server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> static \<static-id\>

static entry

### Usage

`nv show service dhcp-server <vrf-id> static <static-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<static-id>` | static mapping name|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6

DHCP-servers6

### Usage

`nv show service dhcp-server6 [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\>

Dynamic Host Configuration Protocol IPv6 Server

### Usage

`nv show service dhcp-server6 <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `interface`             | Assign DHCP options to clients directly attached to these interfaes.|
| `pool`                  | DHCP IP Pools |
| `domain-name`           | DHCP domain names |
| `domain-name-server`    | DHCP domain name servers |
| `static`                | DHCP clients with fixed IP address assignments |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> interface \<interface-id\>

### Usage

`nv show service dhcp-server6 <vrf-id> interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>` | DHCP client interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\>

DHCP Pool

### Usage

`nv show service dhcp-server6 <vrf-id> pool <pool-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` |   DHCP6 pool subnet. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  domain-name-server    DHCP domain name servers

  domain-name           DHCP domain names

  range                 IP Address range assignments

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

A remote DNS server

### Usage

`nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` |  DHCP6 pool subnet. |
| `<server-id>` |   DNS server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

TBD

### Usage

`nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` |  DHCP6 pool subnet. |
| `<domain-name-id>` | DHCP domain name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> range \<range-id\>

DHCP Pool range

### Usage

`nv show service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` |  DHCP6 pool subnet. |
| `<range-id>` |  DHCP client interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\>

TBD

### Usage

`nv show service dhcp-server6 <vrf-id> domain-name <domain-name-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<domain-name-id>` | DHCP domain name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> domain-name-server \<server-id\>

A remote DNS server

### Usage

`nv show service dhcp-server6 <vrf-id> domain-name-server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>` |  DNS server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> static \<static-id\>

static entry

### Usage

`nv show service dhcp-server6 <vrf-id> static <static-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<static-id>` |  static mapping name|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service lldp

Global LLDP

### Usage

`nv show service lldp [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system

Top-level node which contains system-wide properties.

### Usage

`nv show system [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `control-plane`         | Control Plane specific configurations |
| `message`               | System pre-login and post-login messages |
| `global`                | global system configuration |
| `ztp`                   | System Zero Touch Provisioning |
| `reboot`                | Platform reboot info |
| `port-mirror`           | Port mirror |
| `config`                | Affect how config operations are performed. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system control-plane

Control Plane specific configurations

### Usage

`nv show system control-plane [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `trap`    | Traps |
| `policer` | Policers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system control-plane trap \<trap-id\>

Trap

### Usage

`nv show system control-plane trap <trap-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<trap-id>` | TRAP ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system control-plane policer \<policer-id\>

Policer

### Usage

`nv show system control-plane policer <policer-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<policer-id>` |  Policer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `statistics` | Policer Statistics|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system control-plane policer \<policer-id\> statistics

Policer Statistics

### Usage

`nv show system control-plane policer <policer-id> statistics [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<policer-id>` | Policer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system message

System pre-login and post-login messages

### Usage

`nv show system message [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system global

global system configuration

### Usage

`nv show system global [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `reserved` |  reserved ranges |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system global reserved

reserved ranges

### Usage

`nv show system global reserved [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `routing-table` |  reserved routing table ranges |
| `vlan` |  reserved vlan ranges |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system global reserved routing-table

reserved routing table ranges

### Usage

`nv show system global reserved routing-table [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `pbr`  | reserved routing table ranges for PBR |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system global reserved routing-table pbr

reserved routing table ranges for PBR

### Usage

`nv show system global reserved routing-table pbr [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system global reserved vlan

reserved vlan ranges

### Usage

`nv show system global reserved vlan [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `l3-vni-vlan` |  Reserved vlans to be used with l3vni |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system global reserved vlan l3-vni-vlan

Reserved vlans to be used with l3vni

### Usage

`nv show system global reserved vlan l3-vni-vlan [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system ztp

System Zero Touch Provisioning

### Usage

`nv show system ztp [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `script` |   Zero Touch Provisioning Script |
| `status` |   Zero Touch Provisioning Last Status |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system ztp script

Zero Touch Provisioning Script

### Usage

`nv show system ztp script [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system ztp status

Zero Touch Provisioning Last Status

### Usage

`nv show system ztp status [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system reboot

Platform reboot info

### Usage

`nv show system reboot [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `reason` |  Platform reboot reason |
| `history`  | Platform reboot history |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system reboot reason

Platform reboot reason

### Usage

`nv show system reboot reason [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system reboot history

Platform reboot history

### Usage

`nv show system reboot history [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror

Port mirror

### Usage

`nv show system port-mirror [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `session` |   sessions |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session

sessions

### Usage

`nv show system port-mirror session [options] [<session-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>`  |port mirror session number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\>

port mirror session number

### Usage

`nv show system port-mirror session <session-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `span` | Switched Port Analyzer |
| `erspan` |  Encapsulated Remote Switched Port Analyzer.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> span

Switched Port Analyzer

### Usage

`nv show system port-mirror session <session-id> span [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |   port mirror session number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `source-port` | Set of source ports.|
| `destination` |  The SPAN destination port.|
| `truncate` |  TBD|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> span source-port

Set of source ports.

### Usage

`nv show system port-mirror session <session-id> span source-port [options] [<port-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` | Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> span source-port \<port-id\>

A port-mirror source port (swps or bonds only)

### Usage

`nv show system port-mirror session <session-id> span source-port <port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` | Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> span destination

The SPAN destination port.

### Usage

`nv show system port-mirror session <session-id> span destination [options] [<port-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` | Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> span destination \<port-id\>

The SPAN destination port.

### Usage

`nv show system port-mirror session <session-id> span destination <port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` | Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> span truncate

TBD

### Usage

`nv show system port-mirror session <session-id> span truncate [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> erspan

Encapsulated Remote Switched Port Analyzer.

### Usage

`nv show system port-mirror session <session-id> erspan [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `source-port` |   Set of source ports. |
| `destination` |   erspan destination |
| `truncate` |   TBD|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> erspan source-port

Set of source ports.

### Usage

`nv show system port-mirror session <session-id> erspan source-port [options] [<port-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` |   Port interface` |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> erspan source-port \<port-id\>

A port-mirror source port (swps or bonds only)

### Usage

`nv show system port-mirror session <session-id> erspan source-port <port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` |   Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> erspan destination

erspan destination

### Usage

`nv show system port-mirror session <session-id> erspan destination [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `source-ip` | TBD |
| `dest-ip` |   TBD |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> erspan destination source-ip

Set of IPv4 addresses

### Usage

`nv show system port-mirror session <session-id> erspan destination source-ip [options] [<source-ip> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<source-ip>` | IPv4 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> erspan destination source-ip \<source-ip\>

An IPv4 address

### Usage

`nv show system port-mirror session <session-id> erspan destination source-ip <source-ip> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> erspan destination dest-ip

Set of IPv4 addresses

### Usage

`nv show system port-mirror session <session-id> erspan destination dest-ip [options] [<dest-ip> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<dest-ip>` |  IPv4 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> erspan destination dest-ip \<dest-ip\>

An IPv4 address

### Usage

`nv show system port-mirror session <session-id> erspan destination dest-ip <dest-ip> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session \<session-id\> erspan truncate

TBD

### Usage

`nv show system port-mirror session <session-id> erspan truncate [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system config

Affect how config operations are performed.

### Usage

`nv show system config [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `apply`   |  Affect how config apply operations are performed.|
| `snippet`  | Configuration file snippets that will be loaded as written into the appropriate configuration file during a foundation unit's lifecycle.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system config apply

Affect how config apply operations are performed.

### Usage

`nv show system config apply [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ignore` |   Set of files to ignore during config apply operations. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system config apply ignore

Set of files to ignore during config apply operations.

### Usage

`nv show system config apply ignore [options] [<ignore-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<ignore-id>` |   Ignored file |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system config apply ignore \<ignore-id\>

File to ignore during config apply operations.

### Usage

`nv show system config apply ignore <ignore-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<ignore-id>` |   Ignored file |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system config snippet

Configuration file snippets that will be loaded as written into the appropriate configuration file during a foundation unit's lifecycle.  This is essentially a copy-paste operation to handle gaps in the current CUE OM.

### Usage

`nv show system config snippet [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf

Shows the VRFs on the switch.

### Usage

`nv show vrf [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\>

### Usage

`nv show vrf <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `loopback` |The loopback IP interface associated with this VRF.|
| `evpn`     |EVPN control plane config and info for VRF|
| `router`   |A VRF|
| `ptp`      |VRF PTP configuration. Inherited by interfaces in this VRF.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> loopback

The loopback IP interface associated with this VRF.

### Usage

`nv show vrf <vrf-id> loopback [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ip` |  Properties associated with the loopback IP address on this VRF. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> loopback ip

IP addresses associated with the VRF's loopback interface.

### Usage

`nv show vrf <vrf-id> loopback ip [options] [<attribute> ...]`


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address` |  static IPv4 or IPv6 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> loopback ip address \<ip-prefix-id\>

An IP address with prefix

### Usage

`nv show vrf <vrf-id> loopback ip address <ip-prefix-id> [options]`


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<ip-prefix-id>` |    IPv4 or IPv6 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> evpn

EVPN control plane config and info for VRF

### Usage

`nv show vrf <vrf-id> evpn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `vni`|  L3 VNI |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> evpn vni \<vni-id\>

 VNI

### Usage

`nv show vrf <vrf-id> evpn vni <vni-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<vni-id>` |  VxLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router

A VRF

### Usage

`nv show vrf <vrf-id> router [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rib`      |RIB Routes|
| `bgp`      |BGP VRF configuration.|
| `static`   |Routes|
| `pim`      |PIM VRF configuration.|
| `ospf`     |OSPF VRF configuration.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router rib \<afi\>

Vrf aware Routing-table per address-family

### Usage

`nv show vrf <vrf-id> router rib <afi> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>` |  Route address family. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `protocol` |   Import protocols from RIB to FIB |
| `route` |  RIB Routes with info.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\>

Import Protocols from where routes are known

### Usage

`nv show vrf <vrf-id> router rib <afi> protocol <import-protocol-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>` |   Route address family. |
| `<import-protocol-id>` |  Import protocol list. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <\<vrf-id\> router rib \<afi\> route \<route-id\>

A route

### Usage

`nv show vrf <vrf-id> router rib <afi> route <route-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>` |   Route address family. |
| `<route-id>`   | IP prefix |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `protocol` |   Route entries |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\>

Protocol types from where routes are known

### Usage

`nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>`          | The route address family.|
| `<route-id>`     | The IP prefix|
| `<protocol-id>`  | The route entry list keys.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `entry-index` | Route entries |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp

BGP VRF configuration.

### Usage

`nv show vrf <vrf-id> router bgp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address-family`    |Address family specific configuration |
| `path-selection`    |BGP path-selection configuration. |
| `route-reflection`  |BGP route-reflection configuration. |
| `peer-group`        |Peers |
| `route-export`      |Controls for exporting ipv4 and ipv6 routes from this VRF |
| `route-import`      |Controls for importing of ipv4 and ipv6 routes from this VRF |
| `timers`            |timer values for all peers in this VRF |
| `confederation`     |BGP Confederation options.|
| `neighbor`          |Peers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family

Address family specific configuration

### Usage

`nv show vrf <vrf-id> router bgp address-family [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4-unicast`  |IPv4 unicast address family |
| `l2vpn-evpn`    |BGP VRF configuration. L2VPN EVPN address family |
| `ipv6-unicast`  |IPv6 unicast address family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast

IPv4 unicast address family

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `redistribute`     | Route redistribute| 
| `aggregate-route`  | IPv4 aggregate routes| 
| `network`          | IPv4 static networks.| 
| `route-import `    | Route import| 
| `multipaths`       | Multipaths| 
| `admin-distance`   | Admin distances.| 
| `route-export`     | Route export| 
| `loc-rib`          | IPv4 local RIB|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute

Route redistribute

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `static`    | Route redistribution of ipv4 static routes |
| `connected` | Route redistribution of ipv4 connected routes |
| `kernel`    | Route redistribution of ipv4 kernel routes|
| `ospf`      | Route redistribution of ipv4 ospf routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\>

An IPv4 aggregate route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<aggregate-route-id>` |  IPv4 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast network \<static-network-id\>

An IPv4 static network.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<static-network-id>` |   IPv4 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import

Route import

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `from-vrf` |   Controls for VRF to VRF route leaking for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf

Controls for VRF to VRF route leaking for this address-family

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `list` |  List of VRFs the routes can be imported from|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf list \<leak-vrf-id\>

A VRF

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<leak-vrf-id>` |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths

Multipaths

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast multipaths [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance

Admin distances.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance [options]`


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export

Route export

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `to-evpn` |  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn

Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib

IPv4 local RIB

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route` |  IPv6 routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>` |  IPv4 address and route prefix in CIDR notation |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `path` | IP route paths |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-i\> path \<path-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |  IPv4 address and route prefix in CIDR notation |
| `<path-id>` |  Path Id |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `nexthop`          | Route nexthops |
| `peer`             | Nexthop peer information |
| `flags`            | Route flags |
| `bestpath`         | A bestpath information |
| `aspath`           | AS paths |
| `community`        | Set of community names for community-list |
| `large-community`  | Set of community names for large community list |
| `ext-community`    | extended communities |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>`   | IPv4 address and route prefix in CIDR notation|
| `<path-id>`    | Path Id|
| `<nexthop-id>` | Nexthop Id|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> peer

Nexthop peer information

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> peer [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>` | IPv4 address and route prefix in CIDR notation |
| `<path-id>`  | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> flags

Route flags

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> flags [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>` | IPv4 address and route prefix in CIDR notation |
| `<path-id>`  | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> bestpath

A bestpath information

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> bestpath [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`  | IPv4 address and route prefix in CIDR notation |
| `<path-id>`   | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> aspath

AS paths

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> aspath [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>`   | IPv4 address and route prefix in CIDR notation |
| `<path-id>`    | Path| 

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> community

Set of community names for community-list

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> community [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>`  | IPv4 address and route prefix in CIDR notation |
| `<path-id>`  | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> large-community

Set of community names for large community list

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> large-community [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>`  | IPv4 address and route prefix in CIDR notation |
| `<path-id>`   | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> ext-community

extended communities

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> ext-community [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` | IPv4 address and route prefix in CIDR notation |
| `<path-id>`  | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn

BGP VRF configuration. L2VPN EVPN address family

### Usage

`nv show vrf <vrf-id> router bgp address-family l2vpn-evpn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast

IPv6 unicast address family

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `aggregate-route`  | IPv6 aggregate routes|
| `network`          | IPv6 static networks.|
| `route-import`     | Route import|
| `multipaths`       | Multipaths|
| `admin-distance`   | Admin distances.|
| `route-export`     | Route export|
| `redistribute`     | Route redistribute|
| `loc-rib`          | IPv6 local RIB|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\>

An IPv6 aggregate route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<aggregate-route-id>` |  IPv6 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast network \<static-network-id\>

An IPv6 static network.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<static-network-id>`  | IPv6 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import

Route import

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `from-vrf` |  Controls for VRF to VRF route leaking for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf

Controls for VRF to VRF route leaking for this address-family

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `list` |   List of VRFs the routes can be imported from |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf list

Set of VRFs

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths

Multipaths

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast multipaths [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance

Admin distances.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export

Route export

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `to-evpn` |  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes) |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn

Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute

Route redistribute

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `static`    | Route redistribution of ipv4 static routes |
| `connected` | Route redistribution of ipv4 connected routes |
| `kernel`    | Route redistribution of ipv4 kernel routes|
| `ospf6`     | Route redistribution of ipv6 ospf routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib

IPv6 local RIB

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route` |   IPv6 routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |  IPv6 address and route prefix in CIDR notation |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `path` |  IP route paths |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` | IPv6 address and route prefix in CIDR notation |
| `<path-id> ` | Path Id |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `nexthop`         | Route nexthops |
| `peer`            | Nexthop peer information |
| `flags`           | Route flags |
| `bestpath`        | A bestpath information |
| `aspath`          | AS paths |
| `community`       | Set of community names for community-list |
| `large-community` | Set of community names for large community list |
| `ext-community`   | extended communities |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |
| `<nexthop-id>` |Nexthop Id |


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> peer

Nexthop peer information

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> peer [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> flags

Route flags

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> flags [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> bestpath

A bestpath information

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> bestpath [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> aspath

AS paths

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> aspath [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> community

Set of community names for community-list

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> community [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> large-community

Set of community names for large community list

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> large-community [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> ext-community

extended communities

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> ext-community [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp path-selection

BGP path-selection configuration.

### Usage

`nv show vrf <vrf-id> router bgp path-selection [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `aspath`     | BGP aspath path-selection config, applicable to this BGP instance |
| `med`        | BGP med path-selection config, applicable to this BGP instance |
| `multipath`  | BGP multipath path-selection config, applicable to this BGP instance |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp path-selection aspath

BGP aspath path-selection config, applicable to this BGP instance

### Usage

`nv show vrf <vrf-id> router bgp path-selection aspath [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp path-selection med

BGP med path-selection config, applicable to this BGP instance

### Usage

`nv show vrf <vrf-id> router bgp path-selection med [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp path-selection multipath

BGP multipath path-selection config, applicable to this BGP instance

### Usage

`nv show vrf <vrf-id> router bgp path-selection multipath [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-reflection

BGP route-reflection configuration.

### Usage

`nv show vrf <vrf-id> router bgp route-reflection [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\>

BGP global configuration.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `bfd`               | Specifies whether to track BGP peering sessions using this configuration via BFD.
| `ttl-security`      | RFC 5082
| `capabilities`      | Capabilities
| `graceful-restart`  | Graceful restart
| `local-as`          | Local AS feature
| `timers`            | Peer peer-timers
| `address-family`    | Address family specific configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd

Specifies whether to track BGP peering sessions using this configuration via BFD.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> bfd [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security

RFC 5082

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities

Capabilities

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> graceful-restart

BGP Graceful restart per neighbor configuration

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as

Local AS feature

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> local-as [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers

Peer peer-timers

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family

Address family specific configuration

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |   Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4-unicast`  | Peer IPv4 unicast address family. Always on, unless disabled globaly. |
| `ipv6-unicast`  | Peer IPv6 unicast address family. |
| `l2vpn-evpn`    | Peer l2vpn EVPN address family. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast

Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `community-advertise`   | Community advertise for address family.|
| `attribute-mode`        | Attribute mod for address family. |
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family |
| `prefix-limits`         | Limits on prefix from the peer for this address-family |
| `default-route-origination` | Default route origination |
| `policy`                | Policies for ipv4 unicast |
| `conditional-advertise` | Conditional advertise for address family. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise

Community advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn` | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound` |   Limits on inbound prefix from the peer for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast default-route-origination

Default route origination

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy

Policies for ipv4 unicast

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | Outbound unicast policy |
| `outbound` | Outbound unicast policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast

Peer IPv6 unicast address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `policy`                | Policies for ipv4 unicast|
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family|
| `prefix-limits`         | Limits on prefix from the peer for this address-family|
| `default-route-origination` | Default route origination|
| `community-advertise`   | Community advertise for address family.|
| `attribute-mode`        | Attribute mod for address family.|
| `conditional-advertise` | Conditional advertise for address family.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy

Policies for ipv6 unicast

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | Outbound unicast policy |
| `outbound` | Outbound unicast policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn` | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound` |   Limits on inbound prefix from the peer for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination

Default route origination

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise

Community advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn

Peer l2vpn EVPN address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `attribute-mode` | Attribute mod for address family. |
| `aspath`         | Options for handling AS_PATH for prefixes from/to peer for the specified address family |
| `policy`         | Policies for l2vpn evpn|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn`   |  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy

Policies for l2vpn evpn

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | Inbound l2vpn-evpn policy |
| `outbound` | Outbound l2vpn-evpn policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound

Inbound l2vpn-evpn policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound

Outbound l2vpn-evpn policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-export

Controls for exporting ipv4 and ipv6 routes from this VRF

### Usage

`nv show vrf <vrf-id> router bgp route-export [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `to-evpn` |  Controls for exporting routes from this VRF into EVPN |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-export to-evpn

Controls for exporting routes from this VRF into EVPN

### Usage

`nv show vrf <vrf-id> router bgp route-export to-evpn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route-target`   | List the RTs to attach to host or prefix routes when exporting them into EVPN or "auto". If "auto", the RT will be derived. This the default. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-export to-evpn route-target \<rt-id\>

A route target identifier

### Usage

`nv show vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rt-id>` |  Route targets or "auto" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-import

Controls for importing of ipv4 and ipv6 routes from this VRF

### Usage

`nv show vrf <vrf-id> router bgp route-import [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `from-evpn` |   Controls for importing EVPN type-2 and type-5 routes into this VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-import from-evpn

Controls for importing EVPN type-2 and type-5 routes into this VRF

### Usage

`nv show vrf <vrf-id> router bgp route-import from-evpn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route-target`  | List the RTs to attach to host or prefix routes when importing them into VRF or "auto". If "auto", the RT will be derived. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-import from-evpn route-target \<rt-id\>

 A route target identifier

### Usage

`nv show vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rt-id>` | Route targets or "auto" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp timers

timer values for all peers in this VRF

### Usage

`nv show vrf <vrf-id> router bgp timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp confederation

BGP Confederation options.

### Usage

`nv show vrf <vrf-id> router bgp confederation [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `member-as` |  Confederation ASNs of the peers, maps to BGP  confederation peers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp confederation member-as

Set of autonomous numbers

### Usage

`nv show vrf <vrf-id> router bgp confederation member-as [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\>

BGP global configuration.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   VRF |
| `<neighbor-id>`  | Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `bfd`                  | Specifies whether to track BGP peering sessions using this configuration via BFD.|
| `capabilities`         | Capabilities|
| `local-as`             | Local AS feature|
| `graceful-restart`     | BGP Graceful restart per neighbor configuration|
| `ttl-security`         | RFC 5082|
| `nexthop`              | Nexthop|
| `message-stats`        | Message statistics|
| `ebgp-policy`          | EBGP Policy RFC8212|
| `address-family`       | Address family specific configuration|
| `timers`               | Peer peer-timers|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd

Specifies whether to track BGP peering sessions using this configuration via BFD.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> bfd [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> capabilities

Capabilities

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>` |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as

Local AS feature

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> local-as [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>` |   Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> graceful-restart

BGP Graceful restart per neighbor configuration

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security

RFC 5082

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> nexthop

Nexthop

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`   | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> message-stats

Message statistics

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> message-stats [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ebgp-policy

EBGP Policy RFC8212

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ebgp-policy [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`   Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family

Address family specific configuration

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>` |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4-unicast` | Peer IPv4 unicast address family. Always on, unless disabled globaly. |
| `ipv6-unicast` | Peer IPv6 unicast address family. |
| `l2vpn-evpn`   | Peer l2vpn EVPN address family. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast

Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `attribute-mode`        | Attribute mod for address family. |
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family |
| `policy`                | Policies for ipv4 unicast |
| `prefix-limits`         | Limits on prefix from the peer for this address-familydefault-route-origination Default route origination |
| `community-advertise`   | Community advertise for address family. |
| `conditional-advertise` | Conditional advertise for address family. |
| `capabilities`          | AF capabilities advertised and received |
| `graceful-restart`      | graceful restart information |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>` |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn`  | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy

Policies for ipv4 unicast

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound` |  Outbound unicast policy |
| `outbound` |   Outbound unicast policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound` |   Limits on inbound prefix from the peer for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast default-route-origination

Default route origination

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination [options]

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast community-advertise

Community advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast capabilities

AF capabilities advertised and received

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast capabilities [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart

graceful restart information

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast graceful-restart [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast

Peer IPv6 unicast address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `attribute-mode`        | Attribute mod for address family. |
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family |
| `prefix-limits`         | Limits on prefix from the peer for this address-family |
| `default-route-origination` | Default route origination |
| `policy`                | Policies for ipv4 unicast |
| `community-advertise`   | Community advertise for address family. |
| `conditional-advertise` | Conditional advertise for address family. |
| `capabilities`          | AF capabilities advertised and received |
| `graceful-restart`      | graceful restart information |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn`    | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound` |  Limits on inbound prefix from the peer for this  address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family


### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast default-route-origination

Default route origination

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy

Policies for ipv6 unicast

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | Outbound unicast policy |
| `outbound` | Outbound unicast policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast community-advertise

Community advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast capabilities

AF capabilities advertised and received

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast capabilities [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart

graceful restart information

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast graceful-restart [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn

Peer l2vpn EVPN address family.

## Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn [options] [<attribute> ...]`


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `attribute-mode`   | Attribute mod for address family. |
| `aspath`           | Options for handling AS_PATH for prefixes from/to peer for the specified address family |
| `policy`           | Policies for l2vpn evpn |
| `capabilities`     | AF capabilities advertised and received |
| `graceful-restart` | graceful restart information |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn`    | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy

Policies for l2vpn evpn

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`    | Inbound l2vpn-evpn policy |
| `outbound`   | Outbound l2vpn-e |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound

Inbound l2vpn-evpn policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound

Outbound l2vpn-evpn policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn capabilities

AF capabilities advertised and received

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn capabilities [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart

graceful restart information

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn graceful-restart [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers

Peer peer-timers

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\>

A route 

### Usage

`nv show vrf <vrf-id> router static <route-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `distance` |  Paths |
| `via` |  Nexthops |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\>

A path

### Usage

`nv show vrf <vrf-id> router static <route-id> distance <distance-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<distance-id>` |  A path distance |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `via`  |  Nexthops |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\>

A via

### Usage

`nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<distance-id>` |  A path distance |
| `<via-id>` | IP address, interface, or "blackhole". |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flag` |  Nexthop flags |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> flag

Nexthop flags

### Usage

`nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<distance-id>` |  A path distance |
| `<via-id>` | IP address, interface, or "blackhole". |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\> via \<via-id\>

A via

### Usage

`nv show vrf <vrf-id> router static <route-id> via <via-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<via-id>` | IP address, interface, or "blackhole". |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flag` |  Nexthop flags |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\> via \<via-id\> flag

Nexthop flags

### Usage

`nv show vrf <vrf-id> router static <route-id> via <via-id> flag [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<via-id>` |   IP address, interface, or "blackhole". |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim

PIM VRF configuration.

### Usage

`nv show vrf <vrf-id> router pim [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timers`                | Timers |
| `ecmp`                  | Choose all available ECMP paths for a particular RPF. If 'off', the first nexthop found will be used. This is the default.|
| `msdp-mesh-group`       | To connect multiple PIM-SM multicast domains using RPs. |
| `address-family`        | Address family specific configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim timers

Timers

### Usage

`nv show vrf <vrf-id> router pim timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim ecmp

Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.

### Usage

`nv show vrf <vrf-id> router pim ecmp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\>

MSDP mesh-group

### Usage

`nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<msdp-mesh-group-id>` |  MSDP mesh group name |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `member-address` | Set of member-address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> member-address \<mesh-member-id\>

A MSDP mesh member

### Usage

`nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<msdp-mesh-group-id>`  | MSDP mesh group name |
| `<mesh-member-id>`      | MSDP mesh-group member IP address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim address-family

Address family specific configuration

### Usage

`nv show vrf <vrf-id> router pim address-family [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4-unicast`   |  IPv4 unicast address family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast

IPv4 unicast address family

### Usage

`nv show vrf <vrf-id> router pim address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
|`spt-switchover`   | Build shortest path tree towards source. |
| `rp`  |  RP address and associated group range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast spt-switchover

Build shortest path tree towards source.

### Usage

`nv show vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\>

RP

### Usage

`nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rp-id>` |  RP IP address |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `group-range`   |  Set of group range assocaited to RP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\> group-range \<group-range-id\>

A group range

### Usage

`nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rp-id>`  | RP IP address |
| `<group-range-id>`  |  Group range associated to RP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf

OSPF VRF configuration.

### Usage

`nv show vrf <vrf-id> router ospf [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `area`                  | OSPF areas |
| `default-originate`     | Advertise a default route as external lsa |
| `distance`              | Administrative distance for installation into the rib |
| `max-metric`            | Set maximum metric value in router lsa to make stub router |
| `log`                   | Log configuration |
| `redistribute`          | Route redistribute |
| `timers`                | Timers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf area \<area-id\>

An OSPF area

### Usage

`nv show vrf <vrf-id> router ospf area <area-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<area-id>` |  Area |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `filter-list`  | Filters networks between OSPF areas |
| `range`        | Area ranges |
| `network`      | Area networks |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf area \<area-id\> filter-list

Filters networks between OSPF areas
### Usage

`nv show vrf <vrf-id> router ospf area <area-id> filter-list [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<area-id>` |  Area |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf area \<area-id\> range \<range-id\>

Filters out components of the prefix

### Usage

`nv show vrf <vrf-id> router ospf area <area-id> range <range-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<area-id>` |  Area |
| `<range-id>` |  Range |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf area \<area-id\> network \<network-id\>

Filters out components of the prefix

### Usage

`nv show vrf <vrf-id> router ospf area <area-id> network <network-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<area-id>` |  Area |
| `<network-id>`  | Network |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf default-originate

Advertise a default route as external lsa

### Usage

`nv show vrf <vrf-id> router ospf default-originate [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf distance

Administrative distance for installation into the rib


### Usage

`nv show vrf <vrf-id> router ospf distance [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf max-metric

Set maximum metric value in router lsa to make stub router


### Usage

`nv show vrf <vrf-id> router ospf max-metric [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf log

Log configuration

### Usage

`nv show vrf <vrf-id> router ospf log [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf redistribute

Route redistribute

### Usage

`nv show vrf <vrf-id> router ospf redistribute [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `static`      | Route redistribute of static routes |
| `connected`   | Route redistribute of connected routes |
| `kernel`      | Route redistribute of kernel routes |
| `bgp`         | Route redistribute of bgp routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf redistribute static

Source route type.

### Usage

`nv show vrf <vrf-id> router ospf redistribute static [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf redistribute connected

 Source route type.

### Usage

`nv show vrf <vrf-id> router ospf redistribute connected [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf redistribute kernel

Source route type.

### Usage

`nv show vrf <vrf-id> router ospf redistribute kernel [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf redistribute bgp

Source route type.

### Usage

`nv show vrf <vrf-id> router ospf redistribute bgp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf timers

Timers

### Usage

`nv show vrf <vrf-id> router ospf timers [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `lsa`     | LSA timers |
| `spf`     | SPF timers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf timers lsa

LSA timers

### Usage

`nv show vrf <vrf-id> router ospf timers lsa [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router ospf timers spf

SPF timers

### Usage

`nv show vrf <vrf-id> router ospf timers spf [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> ptp

VRF PTP configuration.  Inherited by interfaces in this VRF.

### Usage

`nv show vrf <vrf-id> ptp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve

Network Virtualization configuration and operational info

### Usage

`nv show nve [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `vxlan`  | Global VxLAN configuration and operational properties. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan

VxLAN

### Usage

`nv show nve vxlan [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `mlag`      | VxLAN specific MLAG address |
| `source`    | Source address |
| `flooding`  | Configuration to specify how BUM traffic in the overlay is handled. This applies to all overlays (VNIs), but can be overridden by VNI-specific configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan mlag

VxLAN specfic MLAG configuration

### Usage

`nv show nve vxlan mlag [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan source

Source address

### Usage

`nv show nve vxlan source [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan flooding

Handling of BUM traffic

### Usage

`nv show nve vxlan flooding [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `head-end-replication` |  BUM traffic is replicated and individual copies sent to remote destinations.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan flooding head-end-replication

Set of IPv4 unicast addresses or "evpn".

### Usage

`nv show nve vxlan flooding head-end-replication [options] [<hrep-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<hrep-id>` |  IPv4 unicast addresses or "evpn" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan flooding head-end-replication \<hrep-id\>

Set of IPv4 unicast addresses or "evpn".

### Usage

`nv show nve vxlan flooding head-end-replication <hrep-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<hrep-id>` |  IPv4 unicast addresses or "evpn" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl

ACL rules

### Usage

`nv show acl [options] [<acl-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| <acl-id> |  ACL ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\>

An ACL is used for matching packets and take actions

### Usage

`nv show acl <acl-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>`  |  ACL ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rule` |  acl rule |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\>

ACL Matching criteria and action rule

### Usage

`nv show acl <acl-id> rule <rule-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `match`   | ACL match criteria |
| `action`  | ACL action |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match

An ACL match

### Usage

`nv show acl <acl-id> rule <rule-id> match [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ip` |   IPv4 and IPv6 match |
| `mac` |  MAC match |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip

An ACL IPv4/IPv6 match

### Usage

`nv show acl <acl-id> rule <rule-id> match ip [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `source-port`| source port |
| `dest-port`  | destination port |
| `fragment`   | Fragment packets |
| `ecn`        | ECN protocol packet match |
| `tcp`        | TCP protocol packet match |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip source-port \<ip-port-id\>

### Usage

`nv show acl <acl-id> rule <rule-id> match ip source-port <ip-port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |
| `<ip-port-id>` |  IP port ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip dest-port \<ip-port-id\>

L4 port

### Usage

`nv show acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |
| `<ip-port-id>` | IP port ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip fragment

State details

### Usage

`nv show acl <acl-id> rule <rule-id> match ip fragment [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip ecn

ECN

### Usage

`nv show acl <acl-id> rule <rule-id> match ip ecn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flags`  |  ECN protocol flags |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip ecn flags

ECN flags

### Usage

`nv show acl <acl-id> rule <rule-id> match ip ecn flags [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp

L4 port

### Usage

`nv show acl <acl-id> rule <rule-id> match ip tcp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flags`  | TCP protocol flags |
| `mask`   | TCP protocol flag mask |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp flags

TCP flags

### Usage

`nv show acl <acl-id> rule <rule-id> match ip tcp flags [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp mask

TCP flags

### Usage

`nv show acl <acl-id> rule <rule-id> match ip tcp mask [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match mac

An ACL MAC match

### Usage

`nv show acl <acl-id> rule <rule-id> match mac [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action

ACL rule action

### Usage

`nv show acl <acl-id> rule <rule-id> action [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `permit`  | Permit action |
| `deny`    | Deny action |
| `log`     | Provides ACL logging facility |
| `set`     | Modify the packet with appropriate values |
| `erspan`  | ERSPAN session |
| `police`  | policing of packets/bytes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action permit

Permit packets

### Usage

`nv show acl <acl-id> rule <rule-id> action permit [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action deny

deny packets

### Usage

`nv show acl <acl-id> rule <rule-id> action deny [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action log

log packets

### Usage

`nv show acl <acl-id> rule <rule-id> action log [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action set

Set action for packets

### Usage

`nv show acl <acl-id> rule <rule-id> action set [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action erspan

ERSPAN session

### Usage

`nv show acl <acl-id> rule <rule-id> action erspan [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action police

Policing of matched packets/bytes

### Usage

`nv show acl <acl-id> rule <rule-id> action police [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>`  |  ACL ID |
  
  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
