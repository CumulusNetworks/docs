---
title: Show Commands
author: Cumulus Networks
weight: 20
product: Cumulus Linux
type: nojsscroll
---
This section describes all the `nv show` commands, together with their attributes and identifiers. To see the `[options]` for all the commands, refer to {{<link url="Common-Options" text="Common Options">}}.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

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

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
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

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
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

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
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

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
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

## nv show router policy ext-community-list <list-id> rule <rule-id> ext-community rt

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

## nv show router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id>

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

## nv show router policy ext-community-list <list-id> rule <rule-id> ext-community

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

## nv show router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id>

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

## nv show router policy large-community-list <list-id>

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

## nv show router policy large-community-list <list-id> rule

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

## nv show router policy large-community-list <list-id> rule <rule-id>

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

## nv show router policy large-community-list <list-id> rule <rule-id> large-community

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

## nv show router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id>

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

## nv show router policy prefix-list <prefix-list-id>

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

## nv show router policy prefix-list <prefix-list-id> rule <rule-id>

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

## nv show router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id>

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

## nv show router policy route-map <route-map-id>

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

## nv show router policy route-map <route-map-id> rule <rule-id>

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

## nv show router policy route-map <route-map-id> rule <rule-id> match

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

## nv show router policy route-map <route-map-id> rule <rule-id> set

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

## nv show router policy route-map <route-map-id> rule <rule-id> set as-path-prepend

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

## nv show router policy route-map <route-map-id> rule <rule-id> set community <community-id>

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

## nv show router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id>

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

## nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id>

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

## nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id>

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

## nv show router policy route-map <route-map-id> rule <rule-id> action

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

## nv show router policy route-map <route-map-id> rule <rule-id> action deny

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

## nv show router policy route-map <route-map-id> rule <rule-id> action permit

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

## nv show router policy route-map <route-map-id> rule <rule-id> action permit exit-policy

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

## nv show platform hardware component <component-id>

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

## nv show platform hardware component <component-id> linecard

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

## nv show platform hardware component <component-id> port

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

## nv show platform hardware component <component-id> port <port-id>

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

## nv show platform hardware component <component-id> port <port-id> breakout-mode

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

## nv show platform hardware component <component-id> port <port-id> breakout-mode <mode-id>

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

## nv show platform environment fan <fan-id>

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

## nv show platform environment sensor <sensor-id>

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

## nv show platform environment psu <psu-id>

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

## nv show platform environment led <led-id>

A LED

### Usage

nv show platform environment led <led-id> [options]`

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

## nv show platform software installed <installed-id>

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

## nv show bridge domain <domain-id>

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

## nv show bridge domain <domain-id> stp

attributes related to global stp

### Usage

nv show bridge domain <domain-id> stp [options] [<attribute> ...]`

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

## nv show bridge domain <domain-id> stp state

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

## nv show bridge domain <domain-id> multicast

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

## nv show bridge domain <domain-id> multicast snooping

### Usage

  `nv show bridge domain <domain-id> multicast snooping [options] [<attribute> ...]



  IGMP/MLD snooping configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  querier               IGMP/MLD querier configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> multicast snooping querier

### Usage

  `nv show bridge domain <domain-id> multicast snooping querier [options]



  IGMP/MLD querier configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> vlan <vid>

### Usage

  `nv show bridge domain <domain-id> vlan <vid> [options] [<attribute> ...]



  A VLAN tag identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  vni                   L2 VNI

  ptp                   VLAN PTP configuration. Inherited by interfaces in this VLAN.

  multicast             Configure multicast on the vlan

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> vlan <vid> vni <vni-id>

### Usage

  `nv show bridge domain <domain-id> vlan <vid> vni <vni-id> [options] [<attribute> ...]



  VNI

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

  <vni-id>              VxLAN ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  flooding              Handling of BUM traffic

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding

### Usage

  `nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding [options] [<attribute> ...]



  Handling of BUM traffic

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

  <vni-id>              VxLAN ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  head-end-replication  BUM traffic is replicated and individual copies sent to remote destinations.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id>

### Usage

  `nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id> [options]



  Set of IPv4 unicast addresses or "evpn".

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

  <vni-id>              VxLAN ID

  <hrep-id>             IPv4 unicast addresses or "evpn"

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> vlan <vid> ptp

### Usage

  `nv show bridge domain <domain-id> vlan <vid> ptp [options]



  VLAN PTP configuration.  Inherited by interfaces in this VLAN.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> vlan <vid> multicast

### Usage

  `nv show bridge domain <domain-id> vlan <vid> multicast [options] [<attribute> ...]



  Configure multicast on the vlan

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

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

## nv show bridge domain <domain-id> vlan <vid> multicast snooping

### Usage

  `nv show bridge domain <domain-id> vlan <vid> multicast snooping [options] [<attribute> ...]



  IGMP/MLD snooping configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  querier               IGMP/MLD querier configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> vlan <vid> multicast snooping querier

### Usage

  `nv show bridge domain <domain-id> vlan <vid> multicast snooping querier [options]



  IGMP/MLD querier configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> mac-table

### Usage

  `nv show bridge domain <domain-id> mac-table [options]



  L2 FDB

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> mdb

### Usage

  `nv show bridge domain <domain-id> mdb [options]



  Set of mdb entries in the bridge domain

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain <domain-id> router-port

### Usage

  `nv show bridge domain <domain-id> router-port [options]



  Set of multicast router ports

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag

### Usage

  `nv show mlag [options] [<attribute> ...]



  Global Multi-chassis Link Aggregation properties

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  lacp-conflict         Configure the mlag lacp-conflict parameters

  consistency-checker   Consistency-checker parameters for mlag nodes

  backup                Set of MLAG backups

  fdb                   Macs owned by local/peer mlag switch

  mdb                   Mdb owned by local/peer switch

  multicast-router-port   Multicast Router Ports owned by local/peer mlag switch

  vni                   Local VNIs

  lacpdb                Mlag Local Lacp Info

  neighbor              Local/peer Neighbour Entries

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacp-conflict

### Usage

  `nv show mlag lacp-conflict [options]



  Configure the mlag lacp-conflict parameters

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag consistency-checker

### Usage

  `nv show mlag consistency-checker [options] [<attribute> ...]



  Show the mlag consistency-checker parameters

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  global                mlag global consistency-checker

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag consistency-checker global

### Usage

  `nv show mlag consistency-checker global [options]



  Global Consistency-checker

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag backup

### Usage

  `nv show mlag backup [options] [<backup-ip> ...]



  Set of MLAG backups

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <backup-ip>           Backup IP of MLAG peer

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag backup <backup-ip>

### Usage

  `nv show mlag backup <backup-ip> [options]



  alternative ip address or interface for peer to reach us

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <backup-ip>           Backup IP of MLAG peer

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb

### Usage

  `nv show mlag fdb [options] [<attribute> ...]



  Set of all mlag macs

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  local                 Locally learnt macs

  peer                  Peer Synced Macs

  permanent             Permanent Macs installed on local/peer

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb local

### Usage

  `nv show mlag fdb local [options]



  Set of MLAG Macs learnt/sync between mlag peers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb peer

### Usage

  `nv show mlag fdb peer [options]



  Set of MLAG Macs learnt/sync between mlag peers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb permanent

### Usage

  `nv show mlag fdb permanent [options]



  Permanent Mac Entry

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag mdb

### Usage

  `nv show mlag mdb [options] [<attribute> ...]



  Set of Mlag Multicast Database Entries

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  local                 Local Multicast Database

  peer                  Peer Multicast Database

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag mdb local

### Usage

  `nv show mlag mdb local [options]



  Multicast Groups Info

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag mdb peer

### Usage

  `nv show mlag mdb peer [options]



  Multicast Groups Info

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag multicast-router-port

### Usage

  `nv show mlag multicast-router-port [options] [<attribute> ...]



  Set of all Mlag Multicast Router Ports

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  local                 Local Multicast Router Ports

  peer                  Peer Multicast Router Ports

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag multicast-router-port local

### Usage

  `nv show mlag multicast-router-port local [options]



  Multicast Router Ports

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag multicast-router-port peer

### Usage

  `nv show mlag multicast-router-port peer [options]



  Multicast Router Ports

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag vni

### Usage

  `nv show mlag vni [options] [<attribute> ...]



  Set of all vnis

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  local                 Local Vnis

  peer                  Peer Vnis

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag vni local

### Usage

  `nv show mlag vni local [options]



  Set of VNIs configured

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag vni peer

### Usage

  `nv show mlag vni peer [options]



  Set of VNIs configured

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacpdb

### Usage

  `nv show mlag lacpdb [options] [<attribute> ...]



  Set of all mlag local/peer lacpdb

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  local                 Local Lacp Database

  peer                  Peer Lacp Database

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacpdb local

### Usage

  `nv show mlag lacpdb local [options]



  Lacp DB

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacpdb peer

### Usage

  `nv show mlag lacpdb peer [options]



  Lacp DB

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag neighbor

### Usage

  `nv show mlag neighbor [options] [<attribute> ...]



  Set of all mlag neigh entries

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  dynamic               Dynamic Neighbor

  permanent             Permanent Neighbor

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag neighbor dynamic

### Usage

  `nv show mlag neighbor dynamic [options]



  Neighs

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag neighbor permanent

### Usage

  `nv show mlag neighbor permanent [options]



  Permanent Neighbors

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn

### Usage

  `nv show evpn [options] [<attribute> ...]



  Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route-advertise       Route advertising

  dad                   Advertise

  evi                   EVI

  multihoming           Multihoming global configuration parameters

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn route-advertise

### Usage

  `nv show evpn route-advertise [options]



  Route dvertising

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn dad

### Usage

  `nv show evpn dad [options] [<attribute> ...]



  Duplicate address detection

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  duplicate-action    Action to take when a MAC is flagged as a possible duplicate. If 'warning-only', generates a log message. If 'freeze', further move events for the MAC will not be acted upon.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn dad duplicate-action

### Usage

  `nv show evpn dad duplicate-action [options] [<attribute> ...]



  Handling of BUM traffic

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  freeze                Further move events for the MAC will not be acted upon.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn dad duplicate-action freeze

### Usage

  `nv show evpn dad duplicate-action freeze [options]



  Advertise

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi

### Usage

  `nv show evpn evi [options] [<evi-id> ...]



  EVIs

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi <evi-id>

### Usage

  `nv show evpn evi <evi-id> [options] [<attribute> ...]



  Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route-advertise       Route advertise

  route-target          Route targets

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi <evi-id> route-advertise

### Usage

  `nv show evpn evi <evi-id> route-advertise [options]



  Route advertise

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi <evi-id> route-target

### Usage

  `nv show evpn evi <evi-id> route-target [options] [<attribute> ...]



  EVPN control plane config and info for VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  export                Route targets to export

  import                Route targets to import

  both                  Route targets to import and export

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi <evi-id> route-target export

### Usage

  `nv show evpn evi <evi-id> route-target export [options] [<rt-id> ...]



  Set of route target identifiers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi <evi-id> route-target export <rt-id>

### Usage

  `nv show evpn evi <evi-id> route-target export <rt-id> [options]



  A route target identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi <evi-id> route-target import

### Usage

  `nv show evpn evi <evi-id> route-target import [options] [<rt-id> ...]



  Set of route target identifiers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi <evi-id> route-target import <rt-id>

### Usage

  `nv show evpn evi <evi-id> route-target import <rt-id> [options]



  A route target identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi <evi-id> route-target both

### Usage

  `nv show evpn evi <evi-id> route-target both [options] [<rt-id> ...]



  Set of route target identifiers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi <evi-id> route-target both <rt-id>

### Usage

  `nv show evpn evi <evi-id> route-target both <rt-id> [options]



  A route target identifier

### Identifiers

|  Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn multihoming

### Usage

  `nv show evpn multihoming [options] [<attribute> ...]



  Multihoming global configuration parameters

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ead-evi-route         Ethernet Auto-discovery per EVPN instance routes

  segment               Multihoming interface segment

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn multihoming ead-evi-route

### Usage

  `nv show evpn multihoming ead-evi-route [options]



  Ethernet Auto-discovery per EVPN instance routes

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn multihoming segment

### Usage

  `nv show evpn multihoming segment [options]



  Multihoming interface segment

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos

### Usage

  `nv show qos [options] [<attribute> ...]



  QOS

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  roce                  Properties associated with the RDMA over Converged

                        Ethernet (RoCE) feature.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos roce

### Usage

  `nv show qos roce [options] [<attribute> ...]



  Properties associated with the RDMA over Converged Ethernet (RoCE) feature.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  prio-map              RoCE PCP/DSCP->SP mapping configurations

  tc-map                RoCE SP->TC mapping and ETS configurations

  pool-map              System Roce pool config

  pool                  System Roce pools

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos roce prio-map

### Usage

  `nv show qos roce prio-map [options]



  RoCE PCP/DSCP->SP mapping configurations

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos roce tc-map

### Usage

  `nv show qos roce tc-map [options]



  RoCE SP->TC mapping and ETS configurations

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos roce pool-map

### Usage

  `nv show qos roce pool-map [options]



  System Roce pool config

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show qos roce pool

### Usage

  `nv show qos roce pool [options]



  System Roce pools

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface

### Usage

  `nv show interface [options] [<interface-id> ...]



  Interfaces

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id>

### Usage

  `nv show interface <interface-id> [options] [<attribute> ...]



  An interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  pluggable             An interface sfp details

  router                interface router

  bond                  The state of the interface

  bridge                attributed related to a bridged interface

  ip                    IP configuration for an interface

  lldp                  LLDP on for an interface

  link                  An physical interface

  qos                   QOS

  evpn                  EVPN control plane config and info for VRF

  acl                   Interface ACL rules

  ptp                   Interface Specific PTP configuration.

  tunnel                The state of the interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> pluggable

### Usage

  `nv show interface <interface-id> pluggable [options]



  An interface sfp details

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router

### Usage

  `nv show interface <interface-id> router [options] [<attribute> ...]



  interface router

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  pbr                   PBR interface configuration.

  ospf                  OSPF interface configuration.

  pim                   PIM interface configuration.

  adaptive-routing      Adaptive routing interface configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router pbr

### Usage

  `nv show interface <interface-id> router pbr [options] [<attribute> ...]



  PBR interface configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  map                   PBR map to use on this interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router pbr map <pbr-map-id>

### Usage

  `nv show interface <interface-id> router pbr map <pbr-map-id> [options]



  Interface Pbr map

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <pbr-map-id>          Route Map ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router ospf

### Usage

  `nv show interface <interface-id> router ospf [options] [<attribute> ...]



  OSPF interface configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  timers                Timers configuration

  authentication        md5 authentication configuration

  bfd                   BFD configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router ospf timers

### Usage

  `nv show interface <interface-id> router ospf timers [options]



  Timers configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router ospf authentication

### Usage

  `nv show interface <interface-id> router ospf authentication [options]



  md5 authentication configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router ospf bfd

### Usage

  `nv show interface <interface-id> router ospf bfd [options]



  BFD configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router pim

### Usage

  `nv show interface <interface-id> router pim [options] [<attribute> ...]



  PIM interface configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  timers                Timers

  bfd                   BFD configuration

  address-family        Address family specific configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router pim timers

### Usage

  `nv show interface <interface-id> router pim timers [options]



  Timers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router pim bfd

### Usage

  `nv show interface <interface-id> router pim bfd [options]



  BFD configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router pim address-family

### Usage

  `nv show interface <interface-id> router pim address-family [options] [<attribute> ...]



  Address family specific configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4-unicast          IPv4 unicast address family

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router pim address-family ipv4-unicast

### Usage

  `nv show interface <interface-id> router pim address-family ipv4-unicast [options] [<attribute> ...]



  IPv4 unicast address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-rp              Allow RP feature, which allows RP address to be accepts for the received

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router pim address-family ipv4-unicast allow-rp

### Usage

  `nv show interface <interface-id> router pim address-family ipv4-unicast allow-rp [options]



  Allow RP feature, which allows RP address to be accepts for the received

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> router adaptive-routing

### Usage

  `nv show interface <interface-id> router adaptive-routing [options]



  Adaptive routing interface configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> bond

### Usage

  `nv show interface <interface-id> bond [options] [<attribute> ...]



  The state of the interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  member                Set of bond members

  mlag                  MLAG configuration on the bond interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> bond member <member-id>

### Usage

  `nv show interface <interface-id> bond member <member-id> [options]



  A bond member

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <member-id>           Bond memer interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> bond mlag

### Usage

  `nv show interface <interface-id> bond mlag [options] [<attribute> ...]



  MLAG configuration on the bond interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  lacp-conflict         Configure the mlag lacp-conflict parameters

  consistency-checker   Consistency-checker parameters for mlag interfaces

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> bond mlag lacp-conflict

### Usage

  `nv show interface <interface-id> bond mlag lacp-conflict [options]



  Configure the mlag lacp-conflict parameters

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> bond mlag consistency-checker

### Usage

  `nv show interface <interface-id> bond mlag consistency-checker [options]



  Interface MLAG Consistency-checker

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> bridge

### Usage

  `nv show interface <interface-id> bridge [options] [<attribute> ...]



  attributed related to a bridged interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  domain                Bridge domains on this interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> bridge domain <domain-id>

### Usage

  `nv show interface <interface-id> bridge domain <domain-id> [options] [<attribute> ...]



  Bridge domain on this interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface
  <domain-id>           Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  stp                   attributed related to a stpd interface
  vlan                  Set of allowed vlans for this bridge domain on this  interface. If "all", inherit all vlans from the bridge domain, if appropriate. This is the default.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> bridge domain <domain-id> stp

### Usage

  `nv show interface <interface-id> bridge domain <domain-id> stp [options]



  attributed related to a stpd interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <domain-id>           Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> bridge domain <domain-id> vlan <vid>

### Usage

  `nv show interface <interface-id> bridge domain <domain-id> vlan <vid> [options]



  A VLAN tag identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <domain-id>           Domain

  <vid>                 VLAN ID, or all

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip

### Usage

  `nv show interface <interface-id> ip [options] [<attribute> ...]



  IP configuration for an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  address               ipv4 and ipv6 address

  neighbor              IP neighbors

  vrr                   Configuration for VRR

  gateway               default ipv4 and ipv6 gateways

  ipv4                  IPv4 configuration for an interface

  ipv6                  IPv6 configuration for an interface

  igmp                  Configuration for IGMP

  vrrp                  Configuration for VRRP

  neighbor-discovery    Neighbor discovery configuration for an interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip address <ip-prefix-id>

### Usage

  `nv show interface <interface-id> ip address <ip-prefix-id> [options]



  An IP address with prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <ip-prefix-id>        IPv4 or IPv6 address and route prefix in CIDR notation

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip neighbor

### Usage

  `nv show interface <interface-id> ip neighbor [options] [<attribute> ...]



  IP neighbors

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4                  IPv4 neighbors

  ipv6                  IPv6 neighbors

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip neighbor ipv4 <neighbor-id>

### Usage

  `nv show interface <interface-id> ip neighbor ipv4 <neighbor-id> [options]



  A neighbor

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <neighbor-id>         The IPv4 address of the neighbor node.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip neighbor ipv6 <neighbor-id>

### Usage

  `nv show interface <interface-id> ip neighbor ipv6 <neighbor-id> [options]



  A neighbor

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <neighbor-id>         The IPv6 address of the neighbor node.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip vrr

### Usage

  `nv show interface <interface-id> ip vrr [options] [<attribute> ...]



  Configuration for VRR

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  address               Virtual addresses with prefixes

  state                 The state of the interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip vrr address <ip-prefix-id>

### Usage

  `nv show interface <interface-id> ip vrr address <ip-prefix-id> [options]



  An IP address with prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <ip-prefix-id>        IPv4 or IPv6 address and route prefix in CIDR notation

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip vrr state

### Usage

  `nv show interface <interface-id> ip vrr state [options]



  The state of the interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip gateway <ip-address-id>

### Usage

  `nv show interface <interface-id> ip gateway <ip-address-id> [options]



  An IP address

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <ip-address-id>       IPv4 or IPv6 address

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip ipv4

### Usage

  `nv show interface <interface-id> ip ipv4 [options]



  IPv4 configuration for an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip ipv6

### Usage

  `nv show interface <interface-id> ip ipv6 [options]



  IPv6 configuration for an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip igmp

### Usage

  `nv show interface <interface-id> ip igmp [options] [<attribute> ...]



  Configuration for IGMP

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  static-group          IGMP static mutlicast mroutes

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip igmp static-group <static-group-id>

### Usage

  `nv show interface <interface-id> ip igmp static-group <static-group-id> [options]



  IGMP static multicast mroute

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <static-group-id>     IGMP static multicast mroute destination

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip vrrp

### Usage

  `nv show interface <interface-id> ip vrrp [options] [<attribute> ...]



  Configuration for VRRP

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  virtual-router        Group of virtual gateways implemented with VRRP

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id>

### Usage

  `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> [options] [<attribute> ...]



  A virtual gateway implemented with VRRP

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <virtual-router-id>   Virtual Router IDentifier (VRID)

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  address               A set of virtual addresses for VRRPv3

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>

### Usage

  `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id> [options]



  An IP address

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <virtual-router-id>   Virtual Router IDentifier (VRID)

  <ip-address-id>       IPv4 or IPv6 address

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip neighbor-discovery

### Usage

  `nv show interface <interface-id> ip neighbor-discovery [options] [<attribute> ...]



  Neighbor discovery configuration for an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  rdnss                 Recursive DNS server addresses to be advertised using type 25 option RFC8016

  prefix                IPv6 prefix configuration

  dnssl                 Advertise DNS search list using type 31 option RFC8106

  router-advertisement  Router advertisement

  home-agent            Home agent configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>

### Usage

  `nv show interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> [options]



  A recursive DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <ipv6-address-id>     IPv6 address

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>

### Usage

  `nv show interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> [options]



  A IPv6 prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <ipv6-prefix-id>      IPv6 address and route prefix in CIDR notation

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>

### Usage

  `nv show interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> [options]



  A DNS search list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <domain-name-id>      The domain portion of a hostname (RFC 1123) or an internationalized hostname (RFC 5890).

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip neighbor-discovery router-advertisement

### Usage

  `nv show interface <interface-id> ip neighbor-discovery router-advertisement [options]



  Router advertisement configuration for an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ip neighbor-discovery home-agent

### Usage

  `nv show interface <interface-id> ip neighbor-discovery home-agent [options]



  Indicates to neighbors that this router acts as a Home Agent and includes a Home Agent Option. Not defined by default

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> lldp

### Usage

  `nv show interface <interface-id> lldp [options] [<attribute> ...]



  LLDP on for an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  neighbor              LLDP neighbors

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> lldp neighbor <neighbor-id>

### Usage

  `nv show interface <interface-id> lldp neighbor <neighbor-id> [options] [<attribute> ...]



  LLDP on an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <neighbor-id>         System generated identifier for the neighbor on the interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  bridge                Bridge properties, such as VLANs, of the neighbor

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> lldp neighbor <neighbor-id> bridge

### Usage

  `nv show interface <interface-id> lldp neighbor <neighbor-id> bridge [options] [<attribute> ...]



  An LLDP bridge

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <neighbor-id>         System generated identifier for the neighbor on the interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  vlan                  Set of vlans understood by this neighbor.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> lldp neighbor <neighbor-id> bridge vlan <vid>

### Usage

  `nv show interface <interface-id> lldp neighbor <neighbor-id> bridge vlan <vid> [options]



  A VLAN tag identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <neighbor-id>         System generated identifier for the neighbor on the interface

  <vid>                 VLAN ID, or all

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> link

### Usage

  `nv show interface <interface-id> link [options] [<attribute> ...]



  An physical interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  state                 The state of the interface

  dot1x                 An physical interface

  stats                 Interface stats

  traffic-engineering   Traffic engineering stats

  flag                  link flags

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> link state

### Usage

  `nv show interface <interface-id> link state [options]



  The state of the interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> link dot1x

### Usage

  `nv show interface <interface-id> link dot1x [options]



  An physical interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> link stats

### Usage

  `nv show interface <interface-id> link stats [options]



  Interface stats

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> link traffic-engineering

### Usage

  `nv show interface <interface-id> link traffic-engineering [options]



  Traffic engineering stats

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> link flag

### Usage

  `nv show interface <interface-id> link flag [options]



  link flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos

### Usage

  `nv show interface <interface-id> qos [options] [<attribute> ...]

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  counters
  roce

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos counters

### Usage

  `nv show interface <interface-id> qos counters [options] [<attribute> ...]



  Interface QoS counters

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  port-stats            QoS Statistics for Interface

  egress-queue-stats    Egress queue statistics per egress traffic-class

  ingress-buffer-stats  Ingress Buffer statistics per priority-group

  pfc-stats             PFC statistics per internal switch-priority

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos counters port-stats

### Usage

  `nv show interface <interface-id> qos counters port-stats [options] [<attribute> ...]



  QoS Statistics for Interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  rx-stats              QoS Rx Statistics for Interface

  tx-stats              QoS Tx Statistics for Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos counters port-stats rx-stats

### Usage

  `nv show interface <interface-id> qos counters port-stats rx-stats [options]



  QoS Rx Statistics for Interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos counters port-stats tx-stats

### Usage

  `nv show interface <interface-id> qos counters port-stats tx-stats [options]



  QoS Tx Statistics for Interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos counters egress-queue-stats

### Usage

  `nv show interface <interface-id> qos counters egress-queue-stats [options]



  Egress queue statistics per egress traffic-class

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos counters ingress-buffer-stats

### Usage

  `nv show interface <interface-id> qos counters ingress-buffer-stats [options]



  Ingress Buffer statistics per priority-group

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos counters pfc-stats

### Usage

  `nv show interface <interface-id> qos counters pfc-stats [options]



  PFC statistics per internal switch-priority

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos roce

### Usage

  `nv show interface <interface-id> qos roce [options] [<attribute> ...]

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  counters
  status

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos roce counters

### Usage

  `nv show interface <interface-id> qos roce counters [options]



  Interface roce counters

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos roce status

### Usage

  `nv show interface <interface-id> qos roce status [options] [<attribute> ...]



  Interface status

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  pool-map              Interface Roce pools

  prio-map              RoCE PCP/DSCP->SP mapping configurations

  tc-map                RoCE SP->TC mapping and ETS configurations

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos roce status pool-map

### Usage

  `nv show interface <interface-id> qos roce status pool-map [options]



  Interface Roce pools

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos roce status prio-map

### Usage

  `nv show interface <interface-id> qos roce status prio-map [options]



  RoCE PCP/DSCP->SP mapping configurations

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> qos roce status tc-map

### Usage

  `nv show interface <interface-id> qos roce status tc-map [options]



  RoCE SP->TC mapping and ETS configurations

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> evpn

### Usage

  `nv show interface <interface-id> evpn [options] [<attribute> ...]



  EVPN control plane config and info for VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  multihoming           Multihoming interface configuration parameters

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> evpn multihoming

### Usage

  `nv show interface <interface-id> evpn multihoming [options] [<attribute> ...]



  Multihoming interface configuration parameters

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  segment               Multihoming interface segment

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> evpn multihoming segment

### Usage

  `nv show interface <interface-id> evpn multihoming segment [options]



  Multihoming interface segment

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> acl <acl-id>

### Usage

  `nv show interface <interface-id> acl <acl-id> [options] [<attribute> ...]



  An ACL is used for matching packets and take actions

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <acl-id>              ACL ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               ACL applied for inbound direction

  outbound              ACL applied for outbound direction

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> acl <acl-id> inbound

### Usage

  `nv show interface <interface-id> acl <acl-id> inbound [options] [<attribute> ...]



  inbound direction

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <acl-id>              ACL ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  control-plane         ACL applied for control plane

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> acl <acl-id> inbound control-plane

### Usage

  `nv show interface <interface-id> acl <acl-id> inbound control-plane [options]



  State details

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <acl-id>              ACL ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> acl <acl-id> outbound

### Usage

  `nv show interface <interface-id> acl <acl-id> outbound [options] [<attribute> ...]



  State details

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <acl-id>              ACL ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  control-plane

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> acl <acl-id> outbound control-plane

### Usage

  `nv show interface <interface-id> acl <acl-id> outbound control-plane [options]



  State details

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <acl-id>              ACL ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ptp

### Usage

  `nv show interface <interface-id> ptp [options] [<attribute> ...]



  Interface Specific PTP configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  timers                Interface PTP timers

  counters              Interface PTP counters

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ptp timers

### Usage

  `nv show interface <interface-id> ptp timers [options]



  Interface PTP timerss

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> ptp counters

### Usage

  `nv show interface <interface-id> ptp counters [options]



  Interface PTP counters

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface <interface-id> tunnel

### Usage

  `nv show interface <interface-id> tunnel [options]



  The state of the interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service

### Usage

  `nv show service [options] [<attribute> ...]



  A service

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  dns                   collection of DNS

  syslog                collection of syslog

  ntp                   NTPs

  dhcp-relay            DHCP-relays

  dhcp-relay6           DHCP-relays

  ptp                   Collection of PTP instances

  dhcp-server           DHCP-servers

  dhcp-server6          DHCP-servers6

  lldp                  Global LLDP

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dns

### Usage

  `nv show service dns [options] [<vrf-id> ...]



  collection of DNS

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

## nv show service dns <vrf-id>

### Usage

  `nv show service dns <vrf-id> [options] [<attribute> ...]



  Domain Name Service

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  server                Remote DNS servers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dns <vrf-id> server <dns-server-id>

### Usage

  `nv show service dns <vrf-id> server <dns-server-id> [options]



  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <dns-server-id>       IPv4 or IPv6 address of a DNS server

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service syslog

### Usage

  `nv show service syslog [options] [<vrf-id> ...]



  collection of syslog

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

## nv show service syslog <vrf-id>

### Usage

  `nv show service syslog <vrf-id> [options] [<attribute> ...]



  Domain Name Service

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  server                Remote DNS servers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service syslog <vrf-id> server <server-id>

### Usage

  `nv show service syslog <vrf-id> server <server-id> [options]



  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <server-id>           Hostname or IP address of a syslog server

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ntp

### Usage

  `nv show service ntp [options] [<vrf-id> ...]



  NTPs

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

## nv show service ntp <vrf-id>

### Usage

  `nv show service ntp <vrf-id> [options] [<attribute> ...]



  Network Time Protocol

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  server                Remote NTP Servers

  pool                  Remote NTP Servers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ntp <vrf-id> server <server-id>

### Usage

  `nv show service ntp <vrf-id> server <server-id> [options]



  A remote NTP Server

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

## nv show service ntp <vrf-id> pool <server-id>

### Usage

  `nv show service ntp <vrf-id> pool <server-id> [options]



  A remote NTP Server

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

### Usage

  `nv show service dhcp-relay [options] [<vrf-id> ...]



  DHCP-relays

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

## nv show service dhcp-relay <vrf-id>

### Usage

  `nv show service dhcp-relay <vrf-id> [options] [<attribute> ...]



  DHCP relay

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  server                DHCP servers

  interface             Set of interfaces on which to handle DHCP relay traffic

  giaddress-interface   Configures DHCP relay giaddress on the interfaes.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay <vrf-id> server <server-id>

### Usage

  `nv show service dhcp-relay <vrf-id> server <server-id> [options]



  A DHCP server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <server-id>           DHCP server

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay <vrf-id> interface <interface-id>

### Usage

  `nv show service dhcp-relay <vrf-id> interface <interface-id> [options]



  An interface on which DHCP relay is configured.

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

## nv show service dhcp-relay <vrf-id> giaddress-interface <interface-id>

### Usage

  `nv show service dhcp-relay <vrf-id> giaddress-interface <interface-id> [options]



  An interface on which DHCP relay giaddress is configured.

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

  `nv show service dhcp-relay6 [options] [<vrf-id> ...]



  DHCP-relays

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

## nv show service dhcp-relay6 <vrf-id>

### Usage

  `nv show service dhcp-relay6 <vrf-id> [options] [<attribute> ...]



  DHCP relay

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

## nv show service dhcp-relay6 <vrf-id> interface

### Usage

  `nv show service dhcp-relay6 <vrf-id> interface [options] [<attribute> ...]



  DHCP relay interfaces

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  upstream              Configures DHCP relay on the interfaes.

  downstream            Configures DHCP relay on the interfaes.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6 <vrf-id> interface upstream <interface-id>

### Usage

  `nv show service dhcp-relay6 <vrf-id> interface upstream <interface-id> [options]



  An interface on which DPCH relay is configured.

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

## nv show service dhcp-relay6 <vrf-id> interface downstream <interface-id>

### Usage

  `nv show service dhcp-relay6 <vrf-id> interface downstream <interface-id> [options]



  An interface on which DPCH relay is configured.

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

### Usage

  `nv show service ptp [options] [<instance-id> ...]



  Collection of PTP instances

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

## nv show service ptp <instance-id>

### Usage

  `nv show service ptp <instance-id> [options] [<attribute> ...]



  Global PTP configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  acceptable-master     Collection of acceptable masters

  monitor               PTP monitor configuration

  current               Local states learned from the exchange of PTP messages

  clock-quality         Clock Quality Status

  parent                Local states learned from the exchange of PTP messages

  time-properties       Time attributes of the clock

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp <instance-id> acceptable-master

### Usage

  `nv show service ptp <instance-id> acceptable-master [options] [<clock-id> ...]



  Collection of acceptable masters

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

## nv show service ptp <instance-id> acceptable-master <clock-id>

### Usage

  `nv show service ptp <instance-id> acceptable-master <clock-id> [options]



  List of clocks that the local clock can accept as master clock

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

## nv show service ptp <instance-id> monitor

### Usage

  `nv show service ptp <instance-id> monitor [options] [<attribute> ...]



  PTP monitor configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  timestamp-log         Collection of violations logs
  violations            PTP violations

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp <instance-id> monitor timestamp-log

### Usage

  `nv show service ptp <instance-id> monitor timestamp-log [options]



  Collection of violations logs

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

## nv show service ptp <instance-id> monitor violations

### Usage

  `nv show service ptp <instance-id> monitor violations [options] [<attribute> ...]



  PTP violations

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  log                   PTP violations log

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp <instance-id> monitor violations log

### Usage

  `nv show service ptp <instance-id> monitor violations log [options] [<attribute> ...]



  PTP violations log

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  acceptable-master     Collection of master violations

  forced-master         Collection of master violations

  max-offset            Collection of violations logs

  min-offset            Collection of violations logs

  path-delay            Collection of violations logs

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp <instance-id> monitor violations log acceptable-master

### Usage

  `nv show service ptp <instance-id> monitor violations log acceptable-master [options]



  Collection of master violations

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

## nv show service ptp <instance-id> monitor violations log forced-master

### Usage

  `nv show service ptp <instance-id> monitor violations log forced-master [options]



  Collection of master violations

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

## nv show service ptp <instance-id> monitor violations log max-offset

### Usage

  `nv show service ptp <instance-id> monitor violations log max-offset [options]



  Collection of violations logs

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

## nv show service ptp <instance-id> monitor violations log min-offset

### Usage

  `nv show service ptp <instance-id> monitor violations log min-offset [options]



  Collection of violations logs

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

## nv show service ptp <instance-id> monitor violations log path-delay

### Usage

  `nv show service ptp <instance-id> monitor violations log path-delay [options]



  Collection of violations logs

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

## nv show service ptp <instance-id> current

### Usage

  `nv show service ptp <instance-id> current [options]



  Local states learned from the exchange of PTP messages

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

## nv show service ptp <instance-id> clock-quality

### Usage

  `nv show service ptp <instance-id> clock-quality [options]



  Clock Quality Status

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

## nv show service ptp <instance-id> parent

### Usage

  `nv show service ptp <instance-id> parent [options] [<attribute> ...]



  Local states learned from the exchange of PTP messages

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  grandmaster-clock-quality
                        Clock Quality Status

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ptp <instance-id> parent grandmaster-clock-quality

### Usage

  `nv show service ptp <instance-id> parent grandmaster-clock-quality [options]



  Clock Quality Status

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

## nv show service ptp <instance-id> time-properties

### Usage

  `nv show service ptp <instance-id> time-properties [options]



  Time attributes of the clock

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

### Usage

`nv show service dhcp-server [options] [<vrf-id> ...]`



  DHCP-servers

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

## nv show service dhcp-server <vrf-id>

### Usage

`nv show service dhcp-server <vrf-id> [options] [<attribute> ...]`



  Dynamic Host Configuration Protocol Server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  interface             Assign DHCP options to clients directly attached to these interfaes.

  pool                  DHCP Pools

  domain-name           DHCP domain names

  domain-name-server    DHCP domain name servers

  static                DHCP clients with fixed IP address assignments

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server <vrf-id> interface <interface-id>

### Usage

  `nv show service dhcp-server <vrf-id> interface <interface-id> [options]



  An interface on which DPCH clients are attached.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <interface-id>        DHCP client interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server <vrf-id> pool <pool-id>

### Usage

  `nv show service dhcp-server <vrf-id> pool <pool-id> [options] [<attribute> ...]



  DHCP Pool

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <pool-id>             DHCP pool subnet.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  domain-name-server    DHCP domain name servers

  domain-name           DHCP domain names

  gateway               DHCP gateway

  range                 IP Address range assignments

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>

### Usage

  `nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id> [options]



  A remote DNS server

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

## nv show service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id>

### Usage

  `nv show service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> [options]



  TBD

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

## nv show service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>

### Usage

  `nv show service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id> [options]



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

## nv show service dhcp-server <vrf-id> pool <pool-id> range <range-id>

### Usage

  `nv show service dhcp-server <vrf-id> pool <pool-id> range <range-id> [options]



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

## nv show service dhcp-server <vrf-id> domain-name <domain-name-id>

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

## nv show service dhcp-server <vrf-id> domain-name-server <server-id>

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

## nv show service dhcp-server <vrf-id> static <static-id>

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

## nv show service dhcp-server6 <vrf-id>

### Usage

  `nv show service dhcp-server6 <vrf-id> [options] [<attribute> ...]



  Dynamic Host Configuration Protocol IPv6 Server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  interface             Assign DHCP options to clients directly attached to these interfaes.

  pool                  DHCP IP Pools

  domain-name           DHCP domain names

  domain-name-server    DHCP domain name servers

  static                DHCP clients with fixed IP address assignments

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 <vrf-id> interface <interface-id>

### Usage

  `nv show service dhcp-server6 <vrf-id> interface <interface-id> [options]



  An interface on which DPCH clients are attached.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| <interface-id>` | DHCP client interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 <vrf-id> pool <pool-id>

### Usage

  `nv show service dhcp-server6 <vrf-id> pool <pool-id> [options] [<attribute> ...]



  DHCP Pool

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

## nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id>

### Usage

  `nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id> [options]



  A remote DNS server

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

## nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id>

### Usage

  `nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> [options]



  TBD

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

## nv show service dhcp-server6 <vrf-id> pool <pool-id> range <range-id>

### Usage

  `nv show service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> [options]



  DHCP Pool range

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

## nv show service dhcp-server6 <vrf-id> domain-name <domain-name-id>

### Usage

  `nv show service dhcp-server6 <vrf-id> domain-name <domain-name-id> [options]



  TBD

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

## nv show service dhcp-server6 <vrf-id> domain-name-server <server-id>

### Usage

  `nv show service dhcp-server6 <vrf-id> domain-name-server <server-id> [options]



  A remote DNS server

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

## nv show service dhcp-server6 <vrf-id> static <static-id>

### Usage

  `nv show service dhcp-server6 <vrf-id> static <static-id> [options]



  static entry

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

### Usage

  `nv show service lldp [options]



  Global LLDP

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system

### Usage

  `nv show system [options] [<attribute> ...]



  Top-level node which contains system-wide properties.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  control-plane         Control Plane specific configurations

  message               System pre-login and post-login messages

  global                global system configuration

  ztp                   System Zero Touch Provisioning

  reboot                Platform reboot info

  port-mirror           Port mirror

  config                Affect how config operations are performed.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system control-plane

### Usage

  `nv show system control-plane [options] [<attribute> ...]



  Control Plane specific configurations

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  trap                  Traps

  policer               Policers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system control-plane trap <trap-id>

### Usage

  `nv show system control-plane trap <trap-id> [options]



  Trap

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

## nv show system control-plane policer <policer-id>

### Usage

  `nv show system control-plane policer <policer-id> [options] [<attribute> ...]



  Policer

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

## nv show system control-plane policer <policer-id> statistics

### Usage

  `nv show system control-plane policer <policer-id> statistics [options]



  Policer Statistics

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

### Usage

  `nv show system message [options]



  System pre-login and post-login messages

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system global

### Usage

  `nv show system global [options] [<attribute> ...]



  global system configuration

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

### Usage

  `nv show system global reserved [options] [<attribute> ...]



  reserved ranges

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

### Usage

  `nv show system global reserved routing-table [options] [<attribute> ...]



  reserved routing table ranges

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

### Usage

  `nv show system global reserved routing-table pbr [options]



  reserved routing table ranges for PBR

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

## nv show system port-mirror session <session-id>

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

## nv show system port-mirror session <session-id> span

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

## nv show system port-mirror session <session-id> span source-port

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

## nv show system port-mirror session <session-id> span source-port <port-id>

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

## nv show system port-mirror session <session-id> span destination

The SPAN destination port.

### Usage

`nv show system port-mirror session <session-id> span destination [options] [<port-id> ...]`

### Identifiers

|| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` | Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show system port-mirror session <session-id> span destination <port-id>

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

## nv show system port-mirror session <session-id> span truncate

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

## nv show system port-mirror session <session-id> erspan

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

## nv show system port-mirror session <session-id> erspan source-port

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

## nv show system port-mirror session <session-id> erspan source-port <port-id>

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

## nv show system port-mirror session <session-id> erspan destination

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

## nv show system port-mirror session <session-id> erspan destination source-ip

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

## nv show system port-mirror session <session-id> erspan destination source-ip <source-ip>

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

## nv show system port-mirror session <session-id> erspan destination dest-ip

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

## nv show system port-mirror session <session-id> erspan destination dest-ip <dest-ip>

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

## nv show system port-mirror session <session-id> erspan truncate

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

## nv show system config apply ignore <ignore-id>

### Usage

`nv show system config apply ignore <ignore-id> [options]`



  File to ignore during config apply operations.

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

## nv show vrf <vrf-id>

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

## nv show vrf <vrf-id> loopback

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

## nv show vrf <vrf-id> loopback ip

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

## nv show vrf <vrf-id> loopback ip address <ip-prefix-id>

An IP address with prefix

### Usage

`nv show vrf <vrf-id> loopback ip address <ip-prefix-id> [options] |


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<ip-prefix-id>` |    IPv4 or IPv6 address and route prefix in CIDR notation \

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> evpn

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

## nv show vrf <vrf-id> evpn vni <vni-id>

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

## nv show vrf <vrf-id> router

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

## nv show vrf <vrf-id> router rib <afi>

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

## nv show vrf <vrf-id> router rib <afi> protocol <import-protocol-id>

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

## nv show vrf <vrf-id> router rib <afi> route <route-id>

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

## nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id>

Protocol types from where routes are known

### Usage

`nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <afi>                 Route address family.

  <route-id>            IP prefix

  <protocol-id>         Route entry list keys.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  entry-index           Route entries

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp

### Usage

  `nv show vrf <vrf-id> router bgp [options] [<attribute> ...]



  BGP VRF configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  address-family        Address family specific configuration

  path-selection        BGP path-selection configuration.

  route-reflection      BGP route-reflection configuration.

  peer-group            Peers

  route-export          Controls for exporting ipv4 and ipv6 routes from this VRF

  route-import          Controls for importing of ipv4 and ipv6 routes from this VRF

  timers                timer values for all peers in this VRF

  confederation         BGP Confederation options.

  neighbor              Peers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family

### Usage

  `nv show vrf <vrf-id> router bgp address-family [options] [<attribute> ...]



  Address family specific configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4-unicast          IPv4 unicast address family

  l2vpn-evpn            BGP VRF configuration. L2VPN EVPN address family

  ipv6-unicast          IPv6 unicast address family

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast [options] [<attribute> ...]



  IPv4 unicast address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  redistribute          Route redistribute

  aggregate-route       IPv4 aggregate routes

  network               IPv4 static networks.

  route-import          Route import

  multipaths            Multipaths

  admin-distance        Admin distances.

  route-export          Route export

  loc-rib               IPv4 local RIB

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute [options] [<attribute> ...]



  Route redistribute

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  static                Route redistribution of ipv4 static routes

  connected             Route redistribution of ipv4 connected routes

  kernel                Route redistribution of ipv4 kernel routes

  ospf                  Route redistribution of ipv4 ospf routes

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static [options]



  Source route type.

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

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected [options]



  Source route type.

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

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel [options]



  Source route type.

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

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf [options]



  Source route type.

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

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> [options]



  An IPv4 aggregate route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <aggregate-route-id>  IPv4 address and route prefix in CIDR notation

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> [options]



  An IPv4 static network.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <static-network-id>   IPv4 address and route prefix in CIDR notation

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import [options] [<attribute> ...]



  Route import

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  from-vrf              Controls for VRF to VRF route leaking for this address-family

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf [options] [<attribute> ...]



  Controls for VRF to VRF route leaking for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  list                  List of VRFs the routes can be imported from

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id> [options]



  A VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <leak-vrf-id>         VRF

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast multipaths

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast multipaths [options]



  Multipaths

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

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance [options]



  Admin distances.

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

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export [options] [<attribute> ...]



  Route export

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  to-evpn               Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn [options]



  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

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

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib [options] [<attribute> ...]



  IPv4 local RIB

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route                 IPv6 routes

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> [options] [<attribute> ...]



  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv4 address and route prefix in CIDR notation

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  path                  IP route paths

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> [options] [<attribute> ...]



  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  nexthop               Route nexthops

  peer                  Nexthop peer information

  flags                 Route flags

  bestpath              A bestpath information

  aspath                AS paths

  community             Set of community names for community-list

  large-community       Set of community names for large community list

  ext-community         extended communities

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id> [options]



  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

  <nexthop-id>          Nexthop Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> peer

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> peer [options]



  Nexthop peer information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> flags

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> flags [options]



  Route flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> bestpath

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> bestpath [options]



  A bestpath information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> aspath

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> aspath [options]



  AS paths

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> community

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> community [options]



  Set of community names for community-list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> large-community

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> large-community [options]



  Set of community names for large community list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> ext-community

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> ext-community [options]



  extended communities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family l2vpn-evpn

### Usage

  `nv show vrf <vrf-id> router bgp address-family l2vpn-evpn [options]



  BGP VRF configuration. L2VPN EVPN address family

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast [options] [<attribute> ...]



  IPv6 unicast address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  aggregate-route       IPv6 aggregate routes

  network               IPv6 static networks.

  route-import          Route import

  multipaths            Multipaths

  admin-distance        Admin distances.

  route-export          Route export

  redistribute          Route redistribute

  loc-rib               IPv6 local RIB

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> [options]



  An IPv6 aggregate route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <aggregate-route-id>  IPv6 address and route prefix in CIDR notation

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> [options]



  An IPv6 static network.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <static-network-id>   IPv6 address and route prefix in CIDR notation

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import [options] [<attribute> ...]



  Route import

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  from-vrf              Controls for VRF to VRF route leaking for this address-family

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf [options] [<attribute> ...]



  Controls for VRF to VRF route leaking for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  list                  List of VRFs the routes can be imported from

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list [options]



  Set of VRFs

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast multipaths

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast multipaths [options]



  Multipaths

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance [options]



  Admin distances.

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export [options] [<attribute> ...]



  Route export

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  to-evpn               Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn [options]



  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute [options] [<attribute> ...]



  Route redistribute

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  static                Route redistribution of ipv4 static routes

  connected             Route redistribution of ipv4 connected routes

  kernel                Route redistribution of ipv4 kernel routes

  ospf6                 Route redistribution of ipv6 ospf routes

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static [options]



  Source route type.

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected [options]



  Source route type.

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel [options]



  Source route type.

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 [options]



  Source route type.

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib [options] [<attribute> ...]



  IPv6 local RIB

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route                 IPv6 routes

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> [options] [<attribute> ...]



  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv6 address and route prefix in CIDR notation

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  path                  IP route paths

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> [options] [<attribute> ...]



  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  nexthop               Route nexthops

  peer                  Nexthop peer information

  flags                 Route flags

  bestpath              A bestpath information

  aspath                AS paths

  community             Set of community names for community-list

  large-community       Set of community names for large community list

  ext-community         extended communities

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id>

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id> [options]



  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

  <nexthop-id>          Nexthop Id


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> peer

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> peer [options]



  Nexthop peer information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> flags

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> flags [options]



  Route flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> bestpath

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> bestpath [options]



  A bestpath information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> aspath

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> aspath [options]



  AS paths

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> community

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> community [options]



  Set of community names for community-list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> large-community

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> large-community [options]



  Set of community names for large community list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> ext-community

### Usage

  `nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> ext-community [options]



  extended communities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp path-selection

### Usage

  `nv show vrf <vrf-id> router bgp path-selection [options] [<attribute> ...]



  BGP path-selection configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  aspath                BGP aspath path-selection config, applicable to this BGP instance

  med                   BGP med path-selection config, applicable to this BGP instance

  multipath             BGP multipath path-selection config, applicable to this BGP instance

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp path-selection aspath

### Usage

  `nv show vrf <vrf-id> router bgp path-selection aspath [options]



  BGP aspath path-selection config, applicable to this BGP instance

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

## nv show vrf <vrf-id> router bgp path-selection med

### Usage

  `nv show vrf <vrf-id> router bgp path-selection med [options]



  BGP med path-selection config, applicable to this BGP instance

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

## nv show vrf <vrf-id> router bgp path-selection multipath

### Usage

  `nv show vrf <vrf-id> router bgp path-selection multipath [options]



  BGP multipath path-selection config, applicable to this BGP instance

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

## nv show vrf <vrf-id> router bgp route-reflection

### Usage

  `nv show vrf <vrf-id> router bgp route-reflection [options]



  BGP route-reflection configuration.

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

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id>

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> [options] [<attribute> ...]



  BGP global configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  bfd                   Specifies whether to track BGP peering sessions using this configuration via BFD.

  ttl-security          RFC 5082

  capabilities          Capabilities

  graceful-restart      Graceful restart

  local-as              Local AS feature

  timers                Peer peer-timers

  address-family        Address family specific configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> bfd

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> bfd [options]



  Specifies whether to track BGP peering sessions using this configuration via BFD.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security [options]



  RFC 5082

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities [options]



  Capabilities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart [options]



  BGP Graceful restart per neighbor configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> local-as

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> local-as [options]



  Local AS feature

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> timers

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> timers [options]



  Peer peer-timers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family [options] [<attribute> ...]



  Address family specific configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4-unicast          Peer IPv4 unicast address family. Always on, unless disabled globaly.

  ipv6-unicast          Peer IPv6 unicast address family.

  l2vpn-evpn            Peer l2vpn EVPN address family.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast [options] [<attribute> ...]



  Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  community-advertise   Community advertise for address family.

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  prefix-limits         Limits on prefix from the peer for this address-family

  default-route-origination Default route origination

  policy                Policies for ipv4 unicast

  conditional-advertise Conditional advertise for address family.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise [options]



  Community advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod [options]



  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn [options]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]



  Limits on prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Limits on inbound prefix from the peer for this address-family

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound [options]



  Limits on inbound prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination [options]



  Default route origination

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy [options] [<attribute> ...]



  Policies for ipv4 unicast

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Outbound unicast policy

  outbound              Outbound unicast policy

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound [options]



  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound [options]



  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise [options]



  Conditional advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast [options] [<attribute> ...]



  Peer IPv6 unicast address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  policy                Policies for ipv4 unicast

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  prefix-limits         Limits on prefix from the peer for this address-family

  default-route-origination Default route origination

  community-advertise   Community advertise for address family.

  attribute-mod         Attribute mod for address family.

  conditional-advertise Conditional advertise for address family.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy [options] [<attribute> ...]



  Policies for ipv6 unicast

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Outbound unicast policy

  outbound              Outbound unicast policy

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound [options]



  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound [options]



  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn [options]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]



  Limits on prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Limits on inbound prefix from the peer for this address-family

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound [options]



  Limits on inbound prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination [options]



  Default route origination

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise [options]



  Community advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod [options]



  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise [options]



  Conditional advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn [options] [<attribute> ...]



  Peer l2vpn EVPN address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  policy                Policies for l2vpn evpn

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod [options]



  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn [options]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy [options] [<attribute> ...]



  Policies for l2vpn evpn

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Inbound l2vpn-evpn policy

  outbound              Outbound l2vpn-evpn policy

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound [options]



  Inbound l2vpn-evpn policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound

### Usage

  `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound [options]



  Outbound l2vpn-evpn policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <peer-group-id>       Domain

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp route-export

### Usage

  `nv show vrf <vrf-id> router bgp route-export [options] [<attribute> ...]



  Controls for exporting ipv4 and ipv6 routes from this VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  to-evpn               Controls for exporting routes from this VRF into EVPN

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp route-export to-evpn

### Usage

  `nv show vrf <vrf-id> router bgp route-export to-evpn [options] [<attribute> ...]



  Controls for exporting routes from this VRF into EVPN

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route-target          List the RTs to attach to host or prefix routes when exporting them into EVPN or "auto". If "auto", the RT  will be derived. This is the default.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id>

### Usage

  `nv show vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id> [options]



  A route target identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <rt-id>               Route targets or "auto"

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp route-import

### Usage

  `nv show vrf <vrf-id> router bgp route-import [options] [<attribute> ...]



  Controls for importing of ipv4 and ipv6 routes from this VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  from-evpn             Controls for importing EVPN type-2 and type-5 routes into this VRF

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp route-import from-evpn

### Usage

  `nv show vrf <vrf-id> router bgp route-import from-evpn [options] [<attribute> ...]



  Controls for importing EVPN type-2 and type-5 routes into this VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route-target          List the RTs to attach to host or prefix routes when importing them into VRF or "auto". If "auto", the RT will be derived. This is the default.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id>

### Usage

  `nv show vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id> [options]



  A route target identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <rt-id>               Route targets or "auto"

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp timers

### Usage

  `nv show vrf <vrf-id> router bgp timers [options]



  timer values for all peers in this VRF

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

## nv show vrf <vrf-id> router bgp confederation

### Usage

  `nv show vrf <vrf-id> router bgp confederation [options] [<attribute> ...]



  BGP Confederation options.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  member-as             Confederation ASNs of the peers, maps to BGP  confederation peers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp confederation member-as

### Usage

  `nv show vrf <vrf-id> router bgp confederation member-as [options]



  Set of autonomous numbers

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

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id>

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> [options] [<attribute> ...]



  BGP global configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  bfd                   Specifies whether to track BGP peering sessions using this configuration via BFD.

  capabilities          Capabilities

  local-as              Local AS feature

  graceful-restart      BGP Graceful restart per neighbor configuration

  ttl-security          RFC 5082

  nexthop               Nexthop

  message-stats         Message statistics

  ebgp-policy           EBGP Policy RFC8212

  address-family        Address family specific configuration

  timers                Peer peer-timers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> bfd

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> bfd [options]



  Specifies whether to track BGP peering sessions using this configuration via BFD.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities [options]



  Capabilities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> local-as

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> local-as [options]



  Local AS feature

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart [options]



  BGP Graceful restart per neighbor configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security [options]



  RFC 5082

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop [options]



  Nexthop

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> message-stats

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> message-stats [options]



  Message statistics

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ebgp-policy

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ebgp-policy [options]



  EBGP Policy RFC8212

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family [options] [<attribute> ...]



  Address family specific configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4-unicast          Peer IPv4 unicast address family. Always on, unless disabled globaly.

  ipv6-unicast          Peer IPv6 unicast address family.

  l2vpn-evpn            Peer l2vpn EVPN address family.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast [options] [<attribute> ...]



  Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  policy                Policies for ipv4 unicast

  prefix-limits         Limits on prefix from the peer for this address-family
  default-route-origination Default route origination

  community-advertise   Community advertise for address family.

  conditional-advertise Conditional advertise for address family.

  capabilities          AF capabilities advertised and received

  graceful-restart      graceful restart information

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod [options]



  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn [options]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy [options] [<attribute> ...]



  Policies for ipv4 unicast

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Outbound unicast policy

  outbound              Outbound unicast policy

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound [options]



  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound [options]



  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
  
  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]



  Limits on prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Limits on inbound prefix from the peer for this address-family

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound [options]



  Limits on inbound prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination [options]



  Default route origination

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise [options]



  Community advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise [options]



  Conditional advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast capabilities

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast capabilities [options]



  AF capabilities advertised and received

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast graceful-restart

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast graceful-restart [options]



  graceful restart information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast [options] [<attribute> ...]



  Peer IPv6 unicast address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  prefix-limits         Limits on prefix from the peer for this address-family

  default-route-origination Default route origination

  policy                Policies for ipv4 unicast

  community-advertise   Community advertise for address family.

  conditional-advertise  Conditional advertise for address family.

  capabilities          AF capabilities advertised and received

  graceful-restart      graceful restart information

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod [options]



  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn [options]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]



  Limits on prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Limits on inbound prefix from the peer for this  address-family

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound [options]



  Limits on inbound prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination [options]



  Default route origination

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy [options] [<attribute> ...]



  Policies for ipv6 unicast

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Outbound unicast policy

  outbound              Outbound unicast policy

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound [options]



  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound [options]



  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise [options]



  Community advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise [options]



  Conditional advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast capabilities

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast capabilities [options]



  AF capabilities advertised and received

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast graceful-restart

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast graceful-restart [options]



  graceful restart information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn

## Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn [options] [<attribute> ...]



  Peer l2vpn EVPN address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  policy                Policies for l2vpn evpn

  capabilities          AF capabilities advertised and received

  graceful-restart      graceful restart information

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod [options]



  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn [options]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy [options] [<attribute> ...]



  Policies for l2vpn evpn

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Inbound l2vpn-evpn policy

  outbound              Outbound l2vpn-evpn policy

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound [options]



  Inbound l2vpn-evpn policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound [options]



  Outbound l2vpn-evpn policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn capabilities

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn capabilities [options]



  AF capabilities advertised and received

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn graceful-restart

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn graceful-restart [options]



  graceful restart information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> timers

### Usage

  `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> timers [options]



  Peer peer-timers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <neighbor-id>         Peer ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router static <route-id>

### Usage

  `nv show vrf <vrf-id> router static <route-id> [options] [<attribute> ...]



  A route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IP prefix

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  distance              Paths

  via                   Nexthops

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router static <route-id> distance <distance-id>

### Usage

  `nv show vrf <vrf-id> router static <route-id> distance <distance-id> [options] [<attribute> ...]



  A path

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IP prefix

  <distance-id>         A path distance

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  via                   Nexthops

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id>

### Usage

  `nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> [options] [<attribute> ...]



  A via

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IP prefix

  <distance-id>         A path distance

  <via-id>              IP address, interface, or "blackhole".

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  flag                  Nexthop flags

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag

### Usage

  `nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag [options]



  Nexthop flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IP prefix

  <distance-id>         A path distance

  <via-id>              IP address, interface, or "blackhole".

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router static <route-id> via <via-id>

### Usage

  `nv show vrf <vrf-id> router static <route-id> via <via-id> [options] [<attribute> ...]



  A via

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IP prefix

  <via-id>              IP address, interface, or "blackhole".

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  flag                  Nexthop flags

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router static <route-id> via <via-id> flag

### Usage

  `nv show vrf <vrf-id> router static <route-id> via <via-id> flag [options]



  Nexthop flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <route-id>            IP prefix

  <via-id>              IP address, interface, or "blackhole".

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router pim

### Usage

  `nv show vrf <vrf-id> router pim [options] [<attribute> ...]



  PIM VRF configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  timers                Timers

  ecmp                  Choose all available ECMP paths for a particular RPF. If 'off', the first nexthop found will be used. This is the default.

  msdp-mesh-group       To connect multiple PIM-SM multicast domains using RPs.

  address-family        Address family specific configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router pim timers

### Usage

  `nv show vrf <vrf-id> router pim timers [options]



  Timers

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

## nv show vrf <vrf-id> router pim ecmp

### Usage

  `nv show vrf <vrf-id> router pim ecmp [options]



  Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.

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

## nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id>

### Usage

  `nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> [options] [<attribute> ...]



  MSDP mesh-group

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <msdp-mesh-group-id>  MSDP mesh group name

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  member-address        Set of member-address

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id>

### Usage

  `nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id> [options]



  A MSDP mesh member

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <msdp-mesh-group-id>  MSDP mesh group name

  <mesh-member-id>      MSDP mesh-group member IP address

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router pim address-family

### Usage

  `nv show vrf <vrf-id> router pim address-family [options] [<attribute> ...]



  Address family specific configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4-unicast          IPv4 unicast address family

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router pim address-family ipv4-unicast

### Usage

  `nv show vrf <vrf-id> router pim address-family ipv4-unicast [options] [<attribute> ...]



  IPv4 unicast address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  spt-switchover        Build shortest path tree towards source.

  rp                    RP address and associated group range.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover

### Usage

  `nv show vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover [options]



  Build shortest path tree towards source.

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

## nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id>

### Usage

  `nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> [options] [<attribute> ...]



  RP

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <rp-id>               RP IP address

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  group-range           Set of group range assocaited to RP.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id>

### Usage

  `nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id> [options]



  A group range

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <rp-id>               RP IP address

  <group-range-id>      Group range associated to RP.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router ospf

### Usage

  `nv show vrf <vrf-id> router ospf [options] [<attribute> ...]



  OSPF VRF configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  area                  OSPF areas

  default-originate     Advertise a default route as external lsa

  distance              Administrative distance for installation into the rib

  max-metric            Set maximum metric value in router lsa to make stub router

  log                   Log configuration

  redistribute          Route redistribute

  timers                Timers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router ospf area <area-id>

### Usage

  `nv show vrf <vrf-id> router ospf area <area-id> [options] [<attribute> ...]



  An OSPF area

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <area-id>             Area

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  filter-list           Filters networks between OSPF areas

  range                 Area ranges

  network               Area networks

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router ospf area <area-id> filter-list

### Usage

  `nv show vrf <vrf-id> router ospf area <area-id> filter-list [options]



  Filters networks between OSPF areas

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <area-id>             Area

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router ospf area <area-id> range <range-id>

### Usage

  `nv show vrf <vrf-id> router ospf area <area-id> range <range-id> [options]



  Filters out components of the prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <area-id>             Area

  <range-id>            Range

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router ospf area <area-id> network <network-id>

### Usage

  `nv show vrf <vrf-id> router ospf area <area-id> network <network-id> [options]



  Filters out components of the prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

  <area-id>             Area

  <network-id>          Network

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router ospf default-originate

### Usage

  `nv show vrf <vrf-id> router ospf default-originate [options]



  Advertise a default route as external lsa

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

## nv show vrf <vrf-id> router ospf distance

### Usage

  `nv show vrf <vrf-id> router ospf distance [options]



  Administrative distance for installation into the rib

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

## nv show vrf <vrf-id> router ospf max-metric

### Usage

  `nv show vrf <vrf-id> router ospf max-metric [options]



  Set maximum metric value in router lsa to make stub router

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

## nv show vrf <vrf-id> router ospf log

### Usage

  `nv show vrf <vrf-id> router ospf log [options]



  Log configuration

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

## nv show vrf <vrf-id> router ospf redistribute

### Usage

  `nv show vrf <vrf-id> router ospf redistribute [options] [<attribute> ...]



  Route redistribute

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  static                Route redistribute of static routes

  connected             Route redistribute of connected routes

  kernel                Route redistribute of kernel routes

  bgp                   Route redistribute of bgp routes

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router ospf redistribute static

### Usage

  `nv show vrf <vrf-id> router ospf redistribute static [options]



  Source route type.

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

## nv show vrf <vrf-id> router ospf redistribute connected

### Usage

  `nv show vrf <vrf-id> router ospf redistribute connected [options]



  Source route type.

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

## nv show vrf <vrf-id> router ospf redistribute kernel

### Usage

  `nv show vrf <vrf-id> router ospf redistribute kernel [options]



  Source route type.

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

## nv show vrf <vrf-id> router ospf redistribute bgp

### Usage

  `nv show vrf <vrf-id> router ospf redistribute bgp [options]



  Source route type.

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

## nv show vrf <vrf-id> router ospf timers

### Usage

  `nv show vrf <vrf-id> router ospf timers [options] [<attribute> ...]



  Timers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  lsa                   LSA timers

  spf                   SPF timers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <vrf-id> router ospf timers lsa

### Usage

  `nv show vrf <vrf-id> router ospf timers lsa [options]



  LSA timers

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

## nv show vrf <vrf-id> router ospf timers spf

### Usage

  `nv show vrf <vrf-id> router ospf timers spf [options]



  SPF timers

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

## nv show vrf <vrf-id> ptp

### Usage

  `nv show vrf <vrf-id> ptp [options]



  VRF PTP configuration.  Inherited by interfaces in this VRF.

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

### Usage

  `nv show nve [options] [<attribute> ...]



  Network Virtualization configuration and operational info

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  vxlan                 Global VxLAN configuration and operational properties.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan

### Usage

  `nv show nve vxlan [options] [<attribute> ...]



  VxLAN

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  mlag                  VxLAN specific MLAG address

  source                Source address

  flooding              Configuration to specify how BUM traffic in the overlay is handled. This applies to all overlays (VNIs), but can be overridden by VNI-specific configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan mlag

### Usage

  `nv show nve vxlan mlag [options]



  VxLAN specfic MLAG configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan source

### Usage

  `nv show nve vxlan source [options]



  Source address

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan flooding

### Usage

  `nv show nve vxlan flooding [options] [<attribute> ...]



  Handling of BUM traffic

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  head-end-replication  BUM traffic is replicated and individual copies sent to remote destinations.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan flooding head-end-replication

### Usage

  `nv show nve vxlan flooding head-end-replication [options] [<hrep-id> ...]



  Set of IPv4 unicast addresses or "evpn".

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <hrep-id>             IPv4 unicast addresses or "evpn"

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan flooding head-end-replication <hrep-id>

### Usage

  `nv show nve vxlan flooding head-end-replication <hrep-id> [options]



  Set of IPv4 unicast addresses or "evpn".

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <hrep-id>             IPv4 unicast addresses or "evpn"

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl

### Usage

  `nv show acl [options] [<acl-id> ...]



  ACL rules

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id>

### Usage

  `nv show acl <acl-id> [options] [<attribute> ...]



  An ACL is used for matching packets and take actions

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  rule                  acl rule

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id>

### Usage

  `nv show acl <acl-id> rule <rule-id> [options] [<attribute> ...]



  ACL Matching criteria and action rule

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  match                 ACL match criteria

  action                ACL action

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match

### Usage

  `nv show acl <acl-id> rule <rule-id> match [options] [<attribute> ...]



  An ACL match

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ip                    IPv4 and IPv6 match

  mac                   MAC match

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match ip

### Usage

  `nv show acl <acl-id> rule <rule-id> match ip [options] [<attribute> ...]



  An ACL IPv4/IPv6 match

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  source-port           source port

  dest-port             destination port

  fragment              Fragment packets

  ecn                   ECN protocol packet match

  tcp                   TCP protocol packet match

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match ip source-port <ip-port-id>

### Usage

  `nv show acl <acl-id> rule <rule-id> match ip source-port <ip-port-id> [options]



  L4 port

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

  <ip-port-id>          IP port ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id>

### Usage

  `nv show acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id> [options]



  L4 port

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

  <ip-port-id>          IP port ID

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match ip fragment

### Usage

  `nv show acl <acl-id> rule <rule-id> match ip fragment [options]



  State details

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match ip ecn

### Usage

  `nv show acl <acl-id> rule <rule-id> match ip ecn [options] [<attribute> ...]



  ECN

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  flags                 ECN protocol flags

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match ip ecn flags

### Usage

  `nv show acl <acl-id> rule <rule-id> match ip ecn flags [options]



  ECN flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match ip tcp

### Usage

  `nv show acl <acl-id> rule <rule-id> match ip tcp [options] [<attribute> ...]



  L4 port

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  flags                 TCP protocol flags
  mask                  TCP protocol flag mask

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match ip tcp flags

### Usage

  `nv show acl <acl-id> rule <rule-id> match ip tcp flags [options]



  TCP flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match ip tcp mask

### Usage

  `nv show acl <acl-id> rule <rule-id> match ip tcp mask [options]



  TCP flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> match mac

### Usage

  `nv show acl <acl-id> rule <rule-id> match mac [options]



  An ACL MAC match

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> action

### Usage

  `nv show acl <acl-id> rule <rule-id> action [options] [<attribute> ...]



  ACL rule action

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  permit                Permit action

  deny                  Deny action

  log                   Provides ACL logging facility

  set                   Modify the packet with appropriate values

  erspan                ERSPAN session

  police                policing of packets/bytes

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> action permit

### Usage

  `nv show acl <acl-id> rule <rule-id> action permit [options]



  Permit packets

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> action deny

### Usage

  `nv show acl <acl-id> rule <rule-id> action deny [options]



  deny packets

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> action log

### Usage

  `nv show acl <acl-id> rule <rule-id> action log [options]



  log packets

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> action set

### Usage

  `nv show acl <acl-id> rule <rule-id> action set [options]



  Set action for packets

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> action erspan

### Usage

  `nv show acl <acl-id> rule <rule-id> action erspan [options]



  ERSPAN session

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl <acl-id> rule <rule-id> action police

### Usage

  `nv show acl <acl-id> rule <rule-id> action police [options]



  Policing of matched packets/bytes

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID
  
  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
