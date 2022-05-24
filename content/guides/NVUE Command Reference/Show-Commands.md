---
title: Show Commands
author: Cumulus Networks
weight: 20
product: Cumulus Linux
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
| `via` |  A next hop in the next hop group.|

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

Introduced in Cumulus Linux 4.0.0

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
| `map` | The collection of PBR maps.|

### Version History

Introduced in Cumulus Linux 4.4.0

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

Introduced in Cumulus Linux 4.4.0

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
| `rule` | The PBR map rule number. |

### Version History

Introduced in Cumulus Linux 4.4.0

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
| match | The PBR match criteria. |
| action | The PBR set criteria. |

### Version History

Introduced in Cumulus Linux 4.4.0

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

Introduced in Cumulus Linux 4.4.0

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
| `nexthop-group` | Route with nexthop-group |

### Version History

Introduced in Cumulus Linux 4.4.0

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

Introduced in Cumulus Linux 4.4.0

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
| `community-list` | Community lists. |
| `as-path-list` |  AS path lists. |
| `ext-community-list` | Extended community lists. |
| `large-community-list` | Large community lists. |
| `prefix-list`  | Prefix list rules. |
| `route-map` | The collection of route maps. |

## nv show router policy community-list

### Usage

`nv show router policy community-list [options] [<list-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| <list-id> |  Community List ID |

## nv show router policy community-list \<list-id\>

### Usage

`nv show router policy community-list <list-id> [options] [<attribute> ...]`

### Description

A community list is used for matching BGP community policies.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| <list-id> |  Community List ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| rule | Community List rule |

## nv show router policy community-list \<list-id\> rule

### Usage

`nv show router policy community-list <list-id> rule [options] [<rule-id> ...]`

### Description

Community list rules

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| <list-id> |  Community List ID |
| <rule-id> |  Prefix List rule number |

## nv show router policy community-list \<list-id\> rule \<rule-id\>

### Usage

`nv show router policy community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

### Description

Community list Matching criteria and action rule

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| <list-id> |  Community List ID |
| <rule-id> |  Prefix List rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
|  community |  Community expression |

## nv show router policy community-list \<list-id\> rule \<rule-id\> community

### Usage

`nv show router policy community-list <list-id> rule <rule-id> community [options] [<community-id> ...]`

### Description

Set of community names for community-list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| <list-id> |  Community List ID |
| <rule-id> |  Prefix List rule number |
| <community-id> | Community number in AA:NN format or well known name |

## nv show router policy community-list \<list-id\> rule \<rule-id\> community \<community-id\>

### Usage

`nv show router policy community-list <list-id> rule <rule-id> community <community-id> [options]`

### Description

A community name

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| <list-id> |  Community List ID |
| <rule-id> |  Prefix List rule number |
| <community-id> | Community number in AA:NN format or well known name |

## nv show router policy as-path-list

### Usage

`nv show router policy as-path-list [options] [<list-id> ...]`

### Description

AS Path lists

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
|`<list-id>` | AS Path List ID |

## nv show router policy as-path-list \<list-id\>

### Usage

`nv show router policy as-path-list <list-id> [options] [<attribute> ...]`

### Description

An AS Path list is used for matching BGP AS Path

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
|`<list-id>` |  AS Path List ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| rule | AS Path List rule |

## nv show router policy as-path-list \<list-id>\ rule \<rule-id\>

### Usage

`nv show router policy as-path-list <list-id> rule <rule-id> [options]`

### Description

AS Path list Matching criteria and action rule

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| ` <list-id>` |  AS Path List ID |
| `<rule-id>` | Prefix List rule number |

## nv show router policy ext-community-list

### Usage

`nv show router policy ext-community-list [options] [<list-id> ...]`

### Description

Extended Community lists

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` | Community List ID |

## nv show router policy ext-community-list \<list-id\>

### Usage

`nv show router policy ext-community-list <list-id> [options] [<attribute> ...]`

### Description

A Extended Community list used for matching BGP communities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id>` |  Community List ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| rule | Extended Community List rule |

## nv show router policy ext-community-list \<list-id\> rule

### Usage

`nv show router policy ext-community-list <list-id> rule [options] [<rule-id> ...]`

### Description

Extended Community list rules

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<list-id> |` Community List ID |
| `<rule-id>` |  Prefix List rule number |

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\>

### Usage

`nv show router policy ext-community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

### Description

Extended Community list Matching criteria and action rule

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

  <rule-id>             Prefix List rule number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ext-community         Extended Community expression

## nv show router policy ext-community-list <list-id> rule <rule-id> ext-community

### Usage

  nv show router policy ext-community-list <list-id> rule <rule-id> ext-community [options] [<attribute> ...]

### Description

  A Extended community name

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

  <rule-id>             Prefix List rule number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  rt                    Route Target Extended Community

  soo                   Site of Origin Extended Community

## nv show router policy ext-community-list <list-id> rule <rule-id> ext-community rt

### Usage

  nv show router policy ext-community-list <list-id> rule <rule-id> ext-community rt [options] [<ext-community-id> ...]

### Description

  Set of extended communities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

  <rule-id>             Prefix List rule number

  <ext-community-id>    Community number in AA:NN or IP:NN format

## nv show router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id>

### Usage

  nv show router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id> [options]

### Description

  A extended community name

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

  <rule-id>             Prefix List rule number

  <ext-community-id>    Community number in AA:NN or IP:NN format

## nv show router policy ext-community-list <list-id> rule <rule-id> ext-community

### Usage

  nv show router policy ext-community-list <list-id> rule <rule-id> ext-community soo [options] [<ext-community-id> ...]

### Description

  Set of extended communities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

  <rule-id>             Prefix List rule number

  <ext-community-id>    Community number in AA:NN or IP:NN format

## nv show router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id>

### Usage

  nv show router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id> [options]

### Description

  A extended community name

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

  <rule-id>             Prefix List rule number

  <ext-community-id>    Community number in AA:NN or IP:NN format

## nv show router policy large-community-list

### Usage

  nv show router policy large-community-list [options] [<list-id> ...]

### Description

  Large Community lists

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

## nv show router policy large-community-list <list-id>

### Usage

  nv show router policy large-community-list <list-id> [options] [<attribute> ...]

### Description

  A Large Community list used for matching community based BGP policies

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  rule                  Large Community List rules

## nv show router policy large-community-list <list-id> rule

### Usage

  nv show router policy large-community-list <list-id> rule [options] [<rule-id> ...]

### Description

  Large Community list rules

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

  <rule-id>             Prefix List rule number

## nv show router policy large-community-list <list-id> rule <rule-id>

### Usage

  nv show router policy large-community-list <list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Large Community list Matching criteria and action rule

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

  <rule-id>             Prefix List rule number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  large-community       Large Community expression

## nv show router policy large-community-list <list-id> rule <rule-id> large-community

### Usage

  nv show router policy large-community-list <list-id> rule <rule-id> large-community [options] [<large-community-id> ...]

### Description

  Set of community names for large community list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

  <rule-id>             Prefix List rule number

  <large-community-id>  Community number in AA:BB:CC format

## nv show router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id>

### Usage

  nv show router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id> [options]

### Description

  Set of community names for large community list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <list-id>             Community List ID

  <rule-id>             Prefix List rule number

  <large-community-id>  Community number in AA:BB:CC format

## nv show router policy prefix-list

### Usage

  nv show router policy prefix-list [options] [<prefix-list-id> ...]

### Description

  Prefix list rules

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <prefix-list-id>      Prefix List ID

## nv show router policy prefix-list <prefix-list-id>

### Usage

  nv show router policy prefix-list <prefix-list-id> [options] [<attribute> ...]

### Description

  A prefix list is used for matching IPv4 and IPv6 address prefixes.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <prefix-list-id>      Prefix List ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  rule                  Prefix List rule

## nv show router policy prefix-list <prefix-list-id> rule <rule-id>

### Usage

  nv show router policy prefix-list <prefix-list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Prefix list Matching criteria and action rule

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <prefix-list-id>      Prefix List ID

  <rule-id>             Prefix List rule number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  match                 Prefix List rule

## nv show router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id>

### Usage

  nv show router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> [options]

### Description

  A prefix match

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <prefix-list-id>      Prefix List ID

  <rule-id>             Prefix List rule number

  <match-id>            ip v4/v6 prefix, or any

## nv show router policy route-map

### Usage

  nv show router policy route-map [options] [<route-map-id> ...]

### Description

  Collection of Route Maps

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

## nv show router policy route-map <route-map-id>

### Usage

  nv show router policy route-map <route-map-id> [options] [<attribute> ...]

### Description

  A route map is used for policy configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  rule                  Route Map rule

## nv show router policy route-map <route-map-id> rule <rule-id>

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Route Map Matching/setting criteria and action rule

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  match                 Route Map match

  set                   Route Map set

  action                Route Map set

## nv show router policy route-map <route-map-id> rule <rule-id> match

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> match [options]

### Description

  Route map rule match

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

## nv show router policy route-map <route-map-id> rule <rule-id> set

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> set [options] [<attribute> ...]

### Description

  Route map rule set

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  as-path-prepend       AS Path prepend

  community             Collection of BGP communities

  large-community       Collection of large BGP communities

  aggregator-as         Collection of aggregator AS

## nv show router policy route-map <route-map-id> rule <rule-id> set as-path-prepend

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> set as-path-prepend [options]

### Description

  AS Path prepend

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

## nv show router policy route-map <route-map-id> rule <rule-id> set community <community-id>

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> set community <community-id> [options]

### Description

  BGP Community

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

  <community-id>        Community number

## nv show router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id>

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id> [options]

### Description

  Large BGP Community

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

  <large-community-id>  Large Community number

## nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id>

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> [options] [<attribute> ...]

### Description

  Aggregator AS Number

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

  <asn-id>              Autonomous number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  address               Set of IPv4 addresses

## nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id>

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id> [options]

### Description

  An IPv4 address

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

  <asn-id>              Autonomous number

  <ipv4-address-id>     IPv4 address

## nv show router policy route-map <route-map-id> rule <rule-id> action

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> action [options] [<attribute> ...]

### Description

  Route map rule action

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  deny                  Deny action

  permit                Permit action

## nv show router policy route-map <route-map-id> rule <rule-id> action deny

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> action deny [options]

### Description

  State details

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

## nv show router policy route-map <route-map-id> rule <rule-id> action permit

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> action permit [options] [<attribute> ...]

### Description

  permit action

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  exit-policy           Permit action exit policy

## nv show router policy route-map <route-map-id> rule <rule-id> action permit exit-policy

### Usage

  nv show router policy route-map <route-map-id> rule <rule-id> action permit exit-policy [options]

### Description

  Permit action exit policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <route-map-id>        Route Map ID

  <rule-id>             Sequence to insert or delete from the route-map

## nv show router bgp

### Usage

  nv show router bgp [options] [<attribute> ...]

### Description

  BGP global configuration.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  graceful-restart      BGP Graceful restart global configuration.

  convergence-wait      BGP Graceful restart global configuration.

## nv show router bgp graceful-restart

### Usage

  nv show router bgp graceful-restart [options]

### Description

  BGP Graceful restart global configuration.

## nv show router bgp convergence-wait

### Usage

  nv show router bgp convergence-wait [options]

### Description

  BGP Graceful restart global configuration.

## nv show router ospf

### Usage

  nv show router ospf [options] [<attribute> ...]

### Description

  OSPF global configuration.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  timers                Timers

## nv show router ospf timers

### Usage

  nv show router ospf timers [options] [<attribute> ...]

### Description

  Timers

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  lsa                   LSA timers

  spf                   SPF timers

## nv show router ospf timers lsa

### Usage

  nv show router ospf timers lsa [options]

### Description

  LSA timers

## nv show router ospf timers spf

### Usage

  nv show router ospf timers spf [options]

### Description

  SPF timers

## nv show router pim

### Usage

  nv show router pim [options] [<attribute> ...]

### Description

  PIM global configuration.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  timers                Timers

## nv show router pim timers

### Usage

  nv show router pim timers [options]

### Description

  Timers

## nv show router igmp

### Usage

  nv show router igmp [options]

### Description

  IGMP global configuration.

## nv show router vrrp

### Usage

  nv show router vrrp [options]

### Description

  VRRP global configuration.

## nv show router vrr

### Usage

  nv show router vrr [options]

### Description

  VRR global configuration.

## nv show router adaptive-routing

### Usage

  nv show router adaptive-routing [options]

### Description

  Adaptive routing global configuration.

## nv show platform

### Usage

  nv show platform [options] [<attribute> ...]

### Description

  Top-level container for the components in the system. This node represents a system component inventory, which includes hardware and software elements.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  capabilities          Capabilities of this platform

  hardware              The platform's hardware

  environment           Platform environment information

  software              The platform's software

## nv show platform capabilities

### Usage

  nv show platform capabilities [options]

### Description

  Capabilities of this platform

## nv show platform hardware

### Usage

  nv show platform hardware [options] [<attribute> ...]

### Description

  The platform's hardware

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  component             Set of components making up the platform.

## nv show platform hardware component

### Usage

  nv show platform hardware component [options] [<component-id> ...]

### Description

  Set of components making up the platform.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <component-id>        Component identifier

## nv show platform hardware component <component-id>

### Usage

  nv show platform hardware component <component-id> [options] [<attribute> ...]

### Description

  A component in the platform.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <component-id>        Component identifier

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  linecard              Properties of a linecard component

  port                  Set of physical ports on this component

## nv show platform hardware component <component-id> linecard

### Usage

  nv show platform hardware component <component-id> linecard [options]

### Description

  Properties of a linecard component

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <component-id>        Component identifier

## nv show platform hardware component <component-id> port

### Usage

  nv show platform hardware component <component-id> port [options] [<port-id> ...]

### Description

  Set of physical ports on this component

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <component-id>        Component identifier

  <port-id>             Physical port identifier

## nv show platform hardware component <component-id> port <port-id>

### Usage

  nv show platform hardware component <component-id> port <port-id> [options] [<attribute> ...]

### Description

  A physical port on the component.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <component-id>        Component identifier

  <port-id>             Physical port identifier

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  breakout-mode         Set of breakout modes supported by this port

## nv show platform hardware component <component-id> port <port-id> breakout-mode

### Usage

  nv show platform hardware component <component-id> port <port-id> breakout-mode [options] [<mode-id> ...]

### Description

  Set of breakout modes

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <component-id>        Component identifier

  <port-id>             Physical port identifier

  <mode-id>             Breakout mode identifier

## nv show platform hardware component <component-id> port <port-id> breakout-mode <mode-id>

### Usage

  nv show platform hardware component <component-id> port <port-id> breakout-mode <mode-id> [options]

### Description

  A breakout mode

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <component-id>        Component identifier

  <port-id>             Physical port identifier

  <mode-id>             Breakout mode identifier

## nv show platform environment

### Usage

  nv show platform environment [options] [<attribute> ...]

### Description

  Platform environment information

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  fan                   The fans on the switch.

  sensor                The sensors on the switch.

  psu                   The PSUs on the switch.

  led                   The LEDs on the switch.

## nv show platform environment fan

### Usage

  nv show platform environment fan [options] [<fan-id> ...]

### Description

  The fans on the switch.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <fan-id>              Physical fan identifier

## nv show platform environment fan <fan-id>

### Usage

  nv show platform environment fan <fan-id> [options]

### Description

  A physical fan on the component.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <fan-id>              Physical fan identifier

## nv show platform environment sensor

### Usage

  nv show platform environment sensor [options] [<sensor-id> ...]

### Description

  The sensors on the switch.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <sensor-id>           Physical sensor identifier

## nv show platform environment sensor <sensor-id>

### Usage

  nv show platform environment sensor <sensor-id> [options]

### Description

  A physical sensor on the component.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <sensor-id>           Physical sensor identifier

## nv show platform environment psu

### Usage

  nv show platform environment psu [options] [<psu-id> ...]

### Description

  The PSUs on the switch.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <psu-id>              Physical PSU identifier

## nv show platform environment psu <psu-id>

### Usage

  nv show platform environment psu <psu-id> [options]

### Description

  A PSU

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <psu-id>              Physical PSU identifier

## nv show platform environment led

### Usage

  nv show platform environment led [options] [<led-id> ...]

### Description

  The LEDs on the switch.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <led-id>              Physical LED identifier

## nv show platform environment led <led-id>

### Usage

  nv show platform environment led <led-id> [options]

### Description

  A LED

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <led-id>              Physical LED identifier

## nv show platform software

### Usage

  nv show platform software [options] [<attribute> ...]

### Description

  The platform's software

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  installed             List of installed software

## nv show platform software installed

### Usage

  nv show platform software installed [options] [<installed-id> ...]

### Description

  List of installed software

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <installed-id>        Package name

## nv show platform software installed <installed-id>

### Usage

  nv show platform software installed <installed-id> [options]

### Description

  An installed package

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <installed-id>        Package name

## nv show bridge

### Usage

  nv show bridge [options] [<attribute> ...]

### Description

  Properties associated with an instance of a bridge.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  domain                Bridge domains

## nv show bridge domain

### Usage

  nv show bridge domain [options] [<domain-id> ...]

### Description

  Bridge domains

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

## nv show bridge domain <domain-id>

### Usage

  nv show bridge domain <domain-id> [options] [<attribute> ...]

### Description

  Bridge domain

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  stp                   attributes related to global stp

  multicast             Configure multicast on the bridge

  vlan                  Set of vlans in the bridge domain. Only applicable when the domain type is "vlan-aware".

  mac-table             L2 FDB

  mdb                   Set of mdb entries in the bridge domain

  router-port           Set of multicast router ports

## nv show bridge domain <domain-id> stp

### Usage

  nv show bridge domain <domain-id> stp [options] [<attribute> ...]

### Description

  attributes related to global stp

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  state                 The state of STP on the bridge

## nv show bridge domain <domain-id> stp state

### Usage

  nv show bridge domain <domain-id> stp state [options]

### Description

  The state of STP on the bridge

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

## nv show bridge domain <domain-id> multicast

### Usage

  nv show bridge domain <domain-id> multicast [options] [<attribute> ...]

### Description

  Configure multicast on the bridge

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  snooping              IGMP/MLD snooping configuration

## nv show bridge domain <domain-id> multicast snooping

### Usage

  nv show bridge domain <domain-id> multicast snooping [options] [<attribute> ...]

### Description

  IGMP/MLD snooping configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  querier               IGMP/MLD querier configuration

## nv show bridge domain <domain-id> multicast snooping querier

### Usage

  nv show bridge domain <domain-id> multicast snooping querier [options]

### Description

  IGMP/MLD querier configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

## nv show bridge domain <domain-id> vlan <vid>

### Usage

  nv show bridge domain <domain-id> vlan <vid> [options] [<attribute> ...]

### Description

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

## nv show bridge domain <domain-id> vlan <vid> vni <vni-id>

### Usage

  nv show bridge domain <domain-id> vlan <vid> vni <vni-id> [options] [<attribute> ...]

### Description

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

## nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding

### Usage

  nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding [options] [<attribute> ...]

### Description

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

## nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id>

### Usage

  nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id> [options]

### Description

  Set of IPv4 unicast addresses or "evpn".

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

  <vni-id>              VxLAN ID

  <hrep-id>             IPv4 unicast addresses or "evpn"

## nv show bridge domain <domain-id> vlan <vid> ptp

### Usage

  nv show bridge domain <domain-id> vlan <vid> ptp [options]

### Description

  VLAN PTP configuration.  Inherited by interfaces in this VLAN.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

## nv show bridge domain <domain-id> vlan <vid> multicast

### Usage

  nv show bridge domain <domain-id> vlan <vid> multicast [options] [<attribute> ...]

### Description

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

## nv show bridge domain <domain-id> vlan <vid> multicast snooping

### Usage

  nv show bridge domain <domain-id> vlan <vid> multicast snooping [options] [<attribute> ...]

### Description

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

## nv show bridge domain <domain-id> vlan <vid> multicast snooping querier

### Usage

  nv show bridge domain <domain-id> vlan <vid> multicast snooping querier [options]

### Description

  IGMP/MLD querier configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

  <vid>                 VLAN ID

## nv show bridge domain <domain-id> mac-table

### Usage

  nv show bridge domain <domain-id> mac-table [options]

### Description

  L2 FDB

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

## nv show bridge domain <domain-id> mdb

### Usage

  nv show bridge domain <domain-id> mdb [options]

### Description

  Set of mdb entries in the bridge domain

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

## nv show bridge domain <domain-id> router-port

### Usage

  nv show bridge domain <domain-id> router-port [options]

### Description

  Set of multicast router ports

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <domain-id>           Domain

## nv show mlag

### Usage

  nv show mlag [options] [<attribute> ...]

### Description

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

## nv show mlag lacp-conflict

### Usage

  nv show mlag lacp-conflict [options]

### Description

  Configure the mlag lacp-conflict parameters

## nv show mlag consistency-checker

### Usage

  nv show mlag consistency-checker [options] [<attribute> ...]

### Description

  Show the mlag consistency-checker parameters

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  global                mlag global consistency-checker

## nv show mlag consistency-checker global

### Usage

  nv show mlag consistency-checker global [options]

### Description

  Global Consistency-checker

## nv show mlag backup

### Usage

  nv show mlag backup [options] [<backup-ip> ...]

### Description

  Set of MLAG backups

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <backup-ip>           Backup IP of MLAG peer

## nv show mlag backup <backup-ip>

### Usage

  nv show mlag backup <backup-ip> [options]

### Description

  alternative ip address or interface for peer to reach us

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <backup-ip>           Backup IP of MLAG peer

## nv show mlag fdb

### Usage

  nv show mlag fdb [options] [<attribute> ...]

### Description

  Set of all mlag macs

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  local                 Locally learnt macs

  peer                  Peer Synced Macs

  permanent             Permanent Macs installed on local/peer

## nv show mlag fdb local

### Usage

  nv show mlag fdb local [options]

### Description

  Set of MLAG Macs learnt/sync between mlag peers

## nv show mlag fdb peer

### Usage

  nv show mlag fdb peer [options]

### Description

  Set of MLAG Macs learnt/sync between mlag peers

## nv show mlag fdb permanent

### Usage

  nv show mlag fdb permanent [options]

### Description

  Permanent Mac Entry

## nv show mlag mdb

### Usage

  nv show mlag mdb [options] [<attribute> ...]

### Description

  Set of Mlag Multicast Database Entries

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  local                 Local Multicast Database

  peer                  Peer Multicast Database

## nv show mlag mdb local

### Usage

  nv show mlag mdb local [options]

### Description

  Multicast Groups Info

## nv show mlag mdb peer

### Usage

  nv show mlag mdb peer [options]

### Description

  Multicast Groups Info

## nv show mlag multicast-router-port

### Usage

  nv show mlag multicast-router-port [options] [<attribute> ...]

### Description

  Set of all Mlag Multicast Router Ports

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  local                 Local Multicast Router Ports

  peer                  Peer Multicast Router Ports

## nv show mlag multicast-router-port local

### Usage

  nv show mlag multicast-router-port local [options]

### Description

  Multicast Router Ports

## nv show mlag multicast-router-port peer

### Usage

  nv show mlag multicast-router-port peer [options]

### Description

  Multicast Router Ports

## nv show mlag vni

### Usage

  nv show mlag vni [options] [<attribute> ...]

### Description

  Set of all vnis

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  local                 Local Vnis

  peer                  Peer Vnis

## nv show mlag vni local

### Usage

  nv show mlag vni local [options]

### Description

  Set of VNIs configured

## nv show mlag vni peer

### Usage

  nv show mlag vni peer [options]

### Description

  Set of VNIs configured

## nv show mlag lacpdb

### Usage

  nv show mlag lacpdb [options] [<attribute> ...]

### Description

  Set of all mlag local/peer lacpdb

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  local                 Local Lacp Database

  peer                  Peer Lacp Database

## nv show mlag lacpdb local

### Usage

  nv show mlag lacpdb local [options]

### Description

  Lacp DB

## nv show mlag lacpdb peer

### Usage

  nv show mlag lacpdb peer [options]

### Description

  Lacp DB

## nv show mlag neighbor

### Usage

  nv show mlag neighbor [options] [<attribute> ...]

### Description

  Set of all mlag neigh entries

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  dynamic               Dynamic Neighbor

  permanent             Permanent Neighbor

## nv show mlag neighbor dynamic

### Usage

  nv show mlag neighbor dynamic [options]

### Description

  Neighs

## nv show mlag neighbor permanent

### Usage

  nv show mlag neighbor permanent [options]

### Description

  Permanent Neighbors

## nv show evpn

### Usage

  nv show evpn [options] [<attribute> ...]

### Description

  Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route-advertise       Route advertising

  dad                   Advertise

  evi                   EVI

  multihoming           Multihoming global configuration parameters

## nv show evpn route-advertise

### Usage

  nv show evpn route-advertise [options]

### Description

  Route dvertising

## nv show evpn dad

### Usage

  nv show evpn dad [options] [<attribute> ...]

### Description

  Duplicate address detection

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  duplicate-action    Action to take when a MAC is flagged as a possible duplicate. If 'warning-only', generates a log message. If 'freeze', further move events for the MAC will not be acted upon.

## nv show evpn dad duplicate-action

### Usage

  nv show evpn dad duplicate-action [options] [<attribute> ...]

### Description

  Handling of BUM traffic

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  freeze                Further move events for the MAC will not be acted upon.

## nv show evpn dad duplicate-action freeze

### Usage

  nv show evpn dad duplicate-action freeze [options]

### Description

  Advertise

## nv show evpn evi

### Usage

  nv show evpn evi [options] [<evi-id> ...]

### Description

  EVIs

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

## nv show evpn evi <evi-id>

### Usage

  nv show evpn evi <evi-id> [options] [<attribute> ...]

### Description

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

## nv show evpn evi <evi-id> route-advertise

### Usage

  nv show evpn evi <evi-id> route-advertise [options]

### Description

  Route advertise

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

## nv show evpn evi <evi-id> route-target

### Usage

  nv show evpn evi <evi-id> route-target [options] [<attribute> ...]

### Description

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

## nv show evpn evi <evi-id> route-target export

### Usage

  nv show evpn evi <evi-id> route-target export [options] [<rt-id> ...]

### Description

  Set of route target identifiers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

## nv show evpn evi <evi-id> route-target export <rt-id>

### Usage

  nv show evpn evi <evi-id> route-target export <rt-id> [options]

### Description

  A route target identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

## nv show evpn evi <evi-id> route-target import

### Usage

  nv show evpn evi <evi-id> route-target import [options] [<rt-id> ...]

### Description

  Set of route target identifiers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

## nv show evpn evi <evi-id> route-target import <rt-id>

### Usage

  nv show evpn evi <evi-id> route-target import <rt-id> [options]

### Description

  A route target identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

## nv show evpn evi <evi-id> route-target both

### Usage

  nv show evpn evi <evi-id> route-target both [options] [<rt-id> ...]

### Description

  Set of route target identifiers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

## nv show evpn evi <evi-id> route-target both <rt-id>

### Usage

  nv show evpn evi <evi-id> route-target both <rt-id> [options]

### Description

  A route target identifier

### Identifiers

|  Identifier |  Description   |
| --------- | -------------- |

  <evi-id>              VRF

  <rt-id>               Route target ID

## nv show evpn multihoming

### Usage

  nv show evpn multihoming [options] [<attribute> ...]

### Description

  Multihoming global configuration parameters

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ead-evi-route         Ethernet Auto-discovery per EVPN instance routes

  segment               Multihoming interface segment

## nv show evpn multihoming ead-evi-route

### Usage

  nv show evpn multihoming ead-evi-route [options]

### Description

  Ethernet Auto-discovery per EVPN instance routes

## nv show evpn multihoming segment

### Usage

  nv show evpn multihoming segment [options]

### Description

  Multihoming interface segment

## nv show qos

### Usage

  nv show qos [options] [<attribute> ...]

### Description

  QOS

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  roce                  Properties associated with the RDMA over Converged

                        Ethernet (RoCE) feature.

## nv show qos roce

### Usage

  nv show qos roce [options] [<attribute> ...]

### Description

  Properties associated with the RDMA over Converged Ethernet (RoCE) feature.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  prio-map              RoCE PCP/DSCP->SP mapping configurations

  tc-map                RoCE SP->TC mapping and ETS configurations

  pool-map              System Roce pool config

  pool                  System Roce pools

## nv show qos roce prio-map

### Usage

  nv show qos roce prio-map [options]

### Description

  RoCE PCP/DSCP->SP mapping configurations

## nv show qos roce tc-map

### Usage

  nv show qos roce tc-map [options]

### Description

  RoCE SP->TC mapping and ETS configurations

## nv show qos roce pool-map

### Usage

  nv show qos roce pool-map [options]

### Description

  System Roce pool config

## nv show qos roce pool

### Usage

  nv show qos roce pool [options]

### Description

  System Roce pools

## nv show interface

### Usage

  nv show interface [options] [<interface-id> ...]

### Description

  Interfaces

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id>

### Usage

  nv show interface <interface-id> [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> pluggable

### Usage

  nv show interface <interface-id> pluggable [options]

### Description

  An interface sfp details

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> router

### Usage

  nv show interface <interface-id> router [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> router pbr

### Usage

  nv show interface <interface-id> router pbr [options] [<attribute> ...]

### Description

  PBR interface configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  map                   PBR map to use on this interface

## nv show interface <interface-id> router pbr map <pbr-map-id>

### Usage

  nv show interface <interface-id> router pbr map <pbr-map-id> [options]

### Description

  Interface Pbr map

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <pbr-map-id>          Route Map ID

## nv show interface <interface-id> router ospf

### Usage

  nv show interface <interface-id> router ospf [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> router ospf timers

### Usage

  nv show interface <interface-id> router ospf timers [options]

### Description

  Timers configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> router ospf authentication

### Usage

  nv show interface <interface-id> router ospf authentication [options]

### Description

  md5 authentication configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> router ospf bfd

### Usage

  nv show interface <interface-id> router ospf bfd [options]

### Description

  BFD configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> router pim

### Usage

  nv show interface <interface-id> router pim [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> router pim timers

### Usage

  nv show interface <interface-id> router pim timers [options]

### Description

  Timers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> router pim bfd

### Usage

  nv show interface <interface-id> router pim bfd [options]

### Description

  BFD configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> router pim address-family

### Usage

  nv show interface <interface-id> router pim address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4-unicast          IPv4 unicast address family

## nv show interface <interface-id> router pim address-family ipv4-unicast

### Usage

  nv show interface <interface-id> router pim address-family ipv4-unicast [options] [<attribute> ...]

### Description

  IPv4 unicast address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-rp              Allow RP feature, which allows RP address to be accepts for the received

## nv show interface <interface-id> router pim address-family ipv4-unicast allow-rp

### Usage

  nv show interface <interface-id> router pim address-family ipv4-unicast allow-rp [options]

### Description

  Allow RP feature, which allows RP address to be accepts for the received

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> router adaptive-routing

### Usage

  nv show interface <interface-id> router adaptive-routing [options]

### Description

  Adaptive routing interface configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> bond

### Usage

  nv show interface <interface-id> bond [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> bond member <member-id>

### Usage

  nv show interface <interface-id> bond member <member-id> [options]

### Description

  A bond member

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <member-id>           Bond memer interface

## nv show interface <interface-id> bond mlag

### Usage

  nv show interface <interface-id> bond mlag [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> bond mlag lacp-conflict

### Usage

  nv show interface <interface-id> bond mlag lacp-conflict [options]

### Description

  Configure the mlag lacp-conflict parameters

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> bond mlag consistency-checker

### Usage

  nv show interface <interface-id> bond mlag consistency-checker [options]

### Description

  Interface MLAG Consistency-checker

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> bridge

### Usage

  nv show interface <interface-id> bridge [options] [<attribute> ...]

### Description

  attributed related to a bridged interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  domain                Bridge domains on this interface

## nv show interface <interface-id> bridge domain <domain-id>

### Usage

  nv show interface <interface-id> bridge domain <domain-id> [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> bridge domain <domain-id> stp

### Usage

  nv show interface <interface-id> bridge domain <domain-id> stp [options]

### Description

  attributed related to a stpd interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <domain-id>           Domain

## nv show interface <interface-id> bridge domain <domain-id> vlan <vid>

### Usage

  nv show interface <interface-id> bridge domain <domain-id> vlan <vid> [options]

### Description

  A VLAN tag identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <domain-id>           Domain

  <vid>                 VLAN ID, or all

## nv show interface <interface-id> ip

### Usage

  nv show interface <interface-id> ip [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> ip address <ip-prefix-id>

### Usage

  nv show interface <interface-id> ip address <ip-prefix-id> [options]

### Description

  An IP address with prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <ip-prefix-id>        IPv4 or IPv6 address and route prefix in CIDR notation

## nv show interface <interface-id> ip neighbor

### Usage

  nv show interface <interface-id> ip neighbor [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> ip neighbor ipv4 <neighbor-id>

### Usage

  nv show interface <interface-id> ip neighbor ipv4 <neighbor-id> [options]

### Description

  A neighbor

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <neighbor-id>         The IPv4 address of the neighbor node.

## nv show interface <interface-id> ip neighbor ipv6 <neighbor-id>

### Usage

  nv show interface <interface-id> ip neighbor ipv6 <neighbor-id> [options]

### Description

  A neighbor

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <neighbor-id>         The IPv6 address of the neighbor node.

## nv show interface <interface-id> ip vrr

### Usage

  nv show interface <interface-id> ip vrr [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> ip vrr address <ip-prefix-id>

### Usage

  nv show interface <interface-id> ip vrr address <ip-prefix-id> [options]

### Description

  An IP address with prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <ip-prefix-id>        IPv4 or IPv6 address and route prefix in CIDR notation

## nv show interface <interface-id> ip vrr state

### Usage

  nv show interface <interface-id> ip vrr state [options]

### Description

  The state of the interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> ip gateway <ip-address-id>

### Usage

  nv show interface <interface-id> ip gateway <ip-address-id> [options]

### Description

  An IP address

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <ip-address-id>       IPv4 or IPv6 address

## nv show interface <interface-id> ip ipv4

### Usage

  nv show interface <interface-id> ip ipv4 [options]

### Description

  IPv4 configuration for an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> ip ipv6

### Usage

  nv show interface <interface-id> ip ipv6 [options]

### Description

  IPv6 configuration for an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> ip igmp

### Usage

  nv show interface <interface-id> ip igmp [options] [<attribute> ...]

### Description

  Configuration for IGMP

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  static-group          IGMP static mutlicast mroutes

## nv show interface <interface-id> ip igmp static-group <static-group-id>

### Usage

  nv show interface <interface-id> ip igmp static-group <static-group-id> [options]

### Description

  IGMP static multicast mroute

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <static-group-id>     IGMP static multicast mroute destination

## nv show interface <interface-id> ip vrrp

### Usage

  nv show interface <interface-id> ip vrrp [options] [<attribute> ...]

### Description

  Configuration for VRRP

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  virtual-router        Group of virtual gateways implemented with VRRP

## nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id>

### Usage

  nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>

### Usage

  nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id> [options]

### Description

  An IP address

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <virtual-router-id>   Virtual Router IDentifier (VRID)

  <ip-address-id>       IPv4 or IPv6 address

## nv show interface <interface-id> ip neighbor-discovery

### Usage

  nv show interface <interface-id> ip neighbor-discovery [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>

### Usage

  nv show interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> [options]

### Description

  A recursive DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <ipv6-address-id>     IPv6 address

## nv show interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>

### Usage

  nv show interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> [options]

### Description

  A IPv6 prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <ipv6-prefix-id>      IPv6 address and route prefix in CIDR notation

## nv show interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>

### Usage

  nv show interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> [options]

### Description

  A DNS search list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <domain-name-id>      The domain portion of a hostname (RFC 1123) or an internationalized hostname (RFC 5890).

## nv show interface <interface-id> ip neighbor-discovery router-advertisement

### Usage

  nv show interface <interface-id> ip neighbor-discovery router-advertisement [options]

### Description

  Router advertisement configuration for an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> ip neighbor-discovery home-agent

### Usage

  nv show interface <interface-id> ip neighbor-discovery home-agent [options]

### Description

  Indicates to neighbors that this router acts as a Home Agent and includes a Home Agent Option. Not defined by default

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> lldp

### Usage

  nv show interface <interface-id> lldp [options] [<attribute> ...]

### Description

  LLDP on for an interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  neighbor              LLDP neighbors

## nv show interface <interface-id> lldp neighbor <neighbor-id>

### Usage

  nv show interface <interface-id> lldp neighbor <neighbor-id> [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> lldp neighbor <neighbor-id> bridge

### Usage

  nv show interface <interface-id> lldp neighbor <neighbor-id> bridge [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> lldp neighbor <neighbor-id> bridge vlan <vid>

### Usage

  nv show interface <interface-id> lldp neighbor <neighbor-id> bridge vlan <vid> [options]

### Description

  A VLAN tag identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <neighbor-id>         System generated identifier for the neighbor on the interface

  <vid>                 VLAN ID, or all

## nv show interface <interface-id> link

### Usage

  nv show interface <interface-id> link [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> link state

### Usage

  nv show interface <interface-id> link state [options]

### Description

  The state of the interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> link dot1x

### Usage

  nv show interface <interface-id> link dot1x [options]

### Description

  An physical interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> link stats

### Usage

  nv show interface <interface-id> link stats [options]

### Description

  Interface stats

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> link traffic-engineering

### Usage

  nv show interface <interface-id> link traffic-engineering [options]

### Description

  Traffic engineering stats

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> link flag

### Usage

  nv show interface <interface-id> link flag [options]

### Description

  link flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> qos

### Usage

  nv show interface <interface-id> qos [options] [<attribute> ...]

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  counters
  roce

## nv show interface <interface-id> qos counters

### Usage

  nv show interface <interface-id> qos counters [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> qos counters port-stats

### Usage

  nv show interface <interface-id> qos counters port-stats [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> qos counters port-stats rx-stats

### Usage

  nv show interface <interface-id> qos counters port-stats rx-stats [options]

### Description

  QoS Rx Statistics for Interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> qos counters port-stats tx-stats

### Usage

  nv show interface <interface-id> qos counters port-stats tx-stats [options]

### Description

  QoS Tx Statistics for Interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> qos counters egress-queue-stats

### Usage

  nv show interface <interface-id> qos counters egress-queue-stats [options]

### Description

  Egress queue statistics per egress traffic-class

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> qos counters ingress-buffer-stats

### Usage

  nv show interface <interface-id> qos counters ingress-buffer-stats [options]

### Description

  Ingress Buffer statistics per priority-group

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> qos counters pfc-stats

### Usage

  nv show interface <interface-id> qos counters pfc-stats [options]

### Description

  PFC statistics per internal switch-priority

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> qos roce

### Usage

  nv show interface <interface-id> qos roce [options] [<attribute> ...]

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  counters
  status

## nv show interface <interface-id> qos roce counters

### Usage

  nv show interface <interface-id> qos roce counters [options]

### Description

  Interface roce counters

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> qos roce status

### Usage

  nv show interface <interface-id> qos roce status [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> qos roce status pool-map

### Usage

  nv show interface <interface-id> qos roce status pool-map [options]

### Description

  Interface Roce pools

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> qos roce status prio-map

### Usage

  nv show interface <interface-id> qos roce status prio-map [options]

### Description

  RoCE PCP/DSCP->SP mapping configurations

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> qos roce status tc-map

### Usage

  nv show interface <interface-id> qos roce status tc-map [options]

### Description

  RoCE SP->TC mapping and ETS configurations

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> evpn

### Usage

  nv show interface <interface-id> evpn [options] [<attribute> ...]

### Description

  EVPN control plane config and info for VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  multihoming           Multihoming interface configuration parameters

## nv show interface <interface-id> evpn multihoming

### Usage

  nv show interface <interface-id> evpn multihoming [options] [<attribute> ...]

### Description

  Multihoming interface configuration parameters

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  segment               Multihoming interface segment

## nv show interface <interface-id> evpn multihoming segment

### Usage

  nv show interface <interface-id> evpn multihoming segment [options]

### Description

  Multihoming interface segment

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> acl <acl-id>

### Usage

  nv show interface <interface-id> acl <acl-id> [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> acl <acl-id> inbound

### Usage

  nv show interface <interface-id> acl <acl-id> inbound [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> acl <acl-id> inbound control-plane

### Usage

  nv show interface <interface-id> acl <acl-id> inbound control-plane [options]

### Description

  State details

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <acl-id>              ACL ID

## nv show interface <interface-id> acl <acl-id> outbound

### Usage

  nv show interface <interface-id> acl <acl-id> outbound [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> acl <acl-id> outbound control-plane

### Usage

  nv show interface <interface-id> acl <acl-id> outbound control-plane [options]

### Description

  State details

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

  <acl-id>              ACL ID

## nv show interface <interface-id> ptp

### Usage

  nv show interface <interface-id> ptp [options] [<attribute> ...]

### Description

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

## nv show interface <interface-id> ptp timers

### Usage

  nv show interface <interface-id> ptp timers [options]

### Description

  Interface PTP timerss

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> ptp counters

### Usage

  nv show interface <interface-id> ptp counters [options]

### Description

  Interface PTP counters

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show interface <interface-id> tunnel

### Usage

  nv show interface <interface-id> tunnel [options]

### Description

  The state of the interface

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <interface-id>        Interface

## nv show service

### Usage

  nv show service [options] [<attribute> ...]

### Description

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

## nv show service dns

### Usage

  nv show service dns [options] [<vrf-id> ...]

### Description

  collection of DNS

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show service dns <vrf-id>

### Usage

  nv show service dns <vrf-id> [options] [<attribute> ...]

### Description

  Domain Name Service

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  server                Remote DNS servers

## nv show service dns <vrf-id> server <dns-server-id>

### Usage

  nv show service dns <vrf-id> server <dns-server-id> [options]

### Description

  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <dns-server-id>       IPv4 or IPv6 address of a DNS server

## nv show service syslog

### Usage

  nv show service syslog [options] [<vrf-id> ...]

### Description

  collection of syslog

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show service syslog <vrf-id>

### Usage

  nv show service syslog <vrf-id> [options] [<attribute> ...]

### Description

  Domain Name Service

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  server                Remote DNS servers

## nv show service syslog <vrf-id> server <server-id>

### Usage

  nv show service syslog <vrf-id> server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <server-id>           Hostname or IP address of a syslog server

## nv show service ntp

### Usage

  nv show service ntp [options] [<vrf-id> ...]

### Description

  NTPs

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show service ntp <vrf-id>

### Usage

  nv show service ntp <vrf-id> [options] [<attribute> ...]

### Description

  Network Time Protocol

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  server                Remote NTP Servers

  pool                  Remote NTP Servers

## nv show service ntp <vrf-id> server <server-id>

### Usage

  nv show service ntp <vrf-id> server <server-id> [options]

### Description

  A remote NTP Server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <server-id>           Hostname or IP address of the NTP server

## nv show service ntp <vrf-id> pool <server-id>

### Usage

  nv show service ntp <vrf-id> pool <server-id> [options]

### Description

  A remote NTP Server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <server-id>           Hostname or IP address of the NTP server

## nv show service dhcp-relay

### Usage

  nv show service dhcp-relay [options] [<vrf-id> ...]

### Description

  DHCP-relays

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show service dhcp-relay <vrf-id>

### Usage

  nv show service dhcp-relay <vrf-id> [options] [<attribute> ...]

### Description

  DHCP relay

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  server                DHCP servers

  interface             Set of interfaces on which to handle DHCP relay traffic

  giaddress-interface   Configures DHCP relay giaddress on the interfaes.

## nv show service dhcp-relay <vrf-id> server <server-id>

### Usage

  nv show service dhcp-relay <vrf-id> server <server-id> [options]

### Description

  A DHCP server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <server-id>           DHCP server

## nv show service dhcp-relay <vrf-id> interface <interface-id>

### Usage

  nv show service dhcp-relay <vrf-id> interface <interface-id> [options]

### Description

  An interface on which DHCP relay is configured.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <interface-id>        DHCP relay interface

## nv show service dhcp-relay <vrf-id> giaddress-interface <interface-id>

### Usage

  nv show service dhcp-relay <vrf-id> giaddress-interface <interface-id> [options]

### Description

  An interface on which DHCP relay giaddress is configured.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <interface-id>        DHCP relay giaddress interface

## nv show service dhcp-relay6

### Usage

  nv show service dhcp-relay6 [options] [<vrf-id> ...]

### Description

  DHCP-relays

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show service dhcp-relay6 <vrf-id>

### Usage

  nv show service dhcp-relay6 <vrf-id> [options] [<attribute> ...]

### Description

  DHCP relay

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  interface             DHCP relay interfaces

## nv show service dhcp-relay6 <vrf-id> interface

### Usage

  nv show service dhcp-relay6 <vrf-id> interface [options] [<attribute> ...]

### Description

  DHCP relay interfaces

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  upstream              Configures DHCP relay on the interfaes.

  downstream            Configures DHCP relay on the interfaes.

## nv show service dhcp-relay6 <vrf-id> interface upstream <interface-id>

### Usage

  nv show service dhcp-relay6 <vrf-id> interface upstream <interface-id> [options]

### Description

  An interface on which DPCH relay is configured.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <interface-id>        DHCP relay interface

## nv show service dhcp-relay6 <vrf-id> interface downstream <interface-id>

### Usage

  nv show service dhcp-relay6 <vrf-id> interface downstream <interface-id> [options]

### Description

  An interface on which DPCH relay is configured.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <interface-id>        DHCP relay interface

## nv show service ptp

### Usage

  nv show service ptp [options] [<instance-id> ...]

### Description

  Collection of PTP instances

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

## nv show service ptp <instance-id>

### Usage

  nv show service ptp <instance-id> [options] [<attribute> ...]

### Description

  Global PTP configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  acceptable-master     Collection of acceptable masters

  monitor               PTP monitor configuration

  current               Local states learned from the exchange of PTP messages

  clock-quality         Clock Quality Status

  parent                Local states learned from the exchange of PTP messages

  time-properties       Time attributes of the clock

## nv show service ptp <instance-id> acceptable-master

### Usage

  nv show service ptp <instance-id> acceptable-master [options] [<clock-id> ...]

### Description

  Collection of acceptable masters

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

  <clock-id>            Clock ID

## nv show service ptp <instance-id> acceptable-master <clock-id>

### Usage

  nv show service ptp <instance-id> acceptable-master <clock-id> [options]

### Description

  List of clocks that the local clock can accept as master clock

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

  <clock-id>            Clock ID

## nv show service ptp <instance-id> monitor

### Usage

  nv show service ptp <instance-id> monitor [options] [<attribute> ...]

### Description

  PTP monitor configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  timestamp-log         Collection of violations logs
  violations            PTP violations

## nv show service ptp <instance-id> monitor timestamp-log

### Usage

  nv show service ptp <instance-id> monitor timestamp-log [options]

### Description

  Collection of violations logs

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

## nv show service ptp <instance-id> monitor violations

### Usage

  nv show service ptp <instance-id> monitor violations [options] [<attribute> ...]

### Description

  PTP violations

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  log                   PTP violations log

## nv show service ptp <instance-id> monitor violations log

### Usage

  nv show service ptp <instance-id> monitor violations log [options] [<attribute> ...]

### Description

  PTP violations log

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  acceptable-master     Collection of master violations

  forced-master         Collection of master violations

  max-offset            Collection of violations logs

  min-offset            Collection of violations logs

  path-delay            Collection of violations logs

## nv show service ptp <instance-id> monitor violations log acceptable-master

### Usage

  nv show service ptp <instance-id> monitor violations log acceptable-master [options]

### Description

  Collection of master violations

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

## nv show service ptp <instance-id> monitor violations log forced-master

### Usage

  nv show service ptp <instance-id> monitor violations log forced-master [options]

### Description

  Collection of master violations

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

## nv show service ptp <instance-id> monitor violations log max-offset

### Usage

  nv show service ptp <instance-id> monitor violations log max-offset [options]

### Description

  Collection of violations logs

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

## nv show service ptp <instance-id> monitor violations log min-offset

### Usage

  nv show service ptp <instance-id> monitor violations log min-offset [options]

### Description

  Collection of violations logs

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

## nv show service ptp <instance-id> monitor violations log path-delay

### Usage

  nv show service ptp <instance-id> monitor violations log path-delay [options]

### Description

  Collection of violations logs

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

## nv show service ptp <instance-id> current

### Usage

  nv show service ptp <instance-id> current [options]

### Description

  Local states learned from the exchange of PTP messages

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

## nv show service ptp <instance-id> clock-quality

### Usage

  nv show service ptp <instance-id> clock-quality [options]

### Description

  Clock Quality Status

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

## nv show service ptp <instance-id> parent

### Usage

  nv show service ptp <instance-id> parent [options] [<attribute> ...]

### Description

  Local states learned from the exchange of PTP messages

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  grandmaster-clock-quality
                        Clock Quality Status

## nv show service ptp <instance-id> parent grandmaster-clock-quality

### Usage

  nv show service ptp <instance-id> parent grandmaster-clock-quality [options]

### Description

  Clock Quality Status

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

## nv show service ptp <instance-id> time-properties

### Usage

  nv show service ptp <instance-id> time-properties [options]

### Description

  Time attributes of the clock

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <instance-id>         PTP instance number. It is used for management  purpose.

## nv show service dhcp-server

### Usage

  nv show service dhcp-server [options] [<vrf-id> ...]

### Description

  DHCP-servers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show service dhcp-server <vrf-id>

### Usage

  nv show service dhcp-server <vrf-id> [options] [<attribute> ...]

### Description

  Dynamic Host Configuration Protocol Server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  interface             Assign DHCP options to clients directly attached to these interfaes.

  pool                  DHCP Pools

  domain-name           DHCP domain names

  domain-name-server    DHCP domain name servers

  static                DHCP clients with fixed IP address assignments

## nv show service dhcp-server <vrf-id> interface <interface-id>

### Usage

  nv show service dhcp-server <vrf-id> interface <interface-id> [options]

### Description

  An interface on which DPCH clients are attached.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <interface-id>        DHCP client interface

## nv show service dhcp-server <vrf-id> pool <pool-id>

### Usage

  nv show service dhcp-server <vrf-id> pool <pool-id> [options] [<attribute> ...]

### Description

  DHCP Pool

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <pool-id>             DHCP pool subnet.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  domain-name-server    DHCP domain name servers

  domain-name           DHCP domain names

  gateway               DHCP gateway

  range                 IP Address range assignments

## nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>

### Usage

  nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <pool-id>             DHCP pool subnet.

  <server-id>           DNS server

## nv show service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id>

### Usage

  nv show service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> [options]

### Description

  TBD

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <pool-id>             DHCP pool subnet.

  <domain-name-id>      DHCP domain name

## nv show service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>

### Usage

  nv show service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id> [options]

### Description

  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <pool-id>             DHCP pool subnet.

  <gateway-id>          Gateway

## nv show service dhcp-server <vrf-id> pool <pool-id> range <range-id>

### Usage

  nv show service dhcp-server <vrf-id> pool <pool-id> range <range-id> [options]

### Description

  DHCP Pool range

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <pool-id>             DHCP pool subnet.

  <range-id>            DHCP client interface

## nv show service dhcp-server <vrf-id> domain-name <domain-name-id>

### Usage

  nv show service dhcp-server <vrf-id> domain-name <domain-name-id> [options]

### Description

  TBD

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <domain-name-id>      DHCP domain name

## nv show service dhcp-server <vrf-id> domain-name-server <server-id>

### Usage

  nv show service dhcp-server <vrf-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <server-id>           DNS server

## nv show service dhcp-server <vrf-id> static <static-id>

### Usage

  nv show service dhcp-server <vrf-id> static <static-id> [options]

### Description

  static entry

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <static-id>           static mapping nane

## nv show service dhcp-server6

### Usage

  nv show service dhcp-server6 [options] [<vrf-id> ...]

### Description

  DHCP-servers6

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show service dhcp-server6 <vrf-id>

### Usage

  nv show service dhcp-server6 <vrf-id> [options] [<attribute> ...]

### Description

  Dynamic Host Configuration Protocol IPv6 Server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  interface             Assign DHCP options to clients directly attached to these interfaes.

  pool                  DHCP IP Pools

  domain-name           DHCP domain names

  domain-name-server    DHCP domain name servers

  static                DHCP clients with fixed IP address assignments

## nv show service dhcp-server6 <vrf-id> interface <interface-id>

### Usage

  nv show service dhcp-server6 <vrf-id> interface <interface-id> [options]

### Description

  An interface on which DPCH clients are attached.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <interface-id>        DHCP client interface

## nv show service dhcp-server6 <vrf-id> pool <pool-id>

### Usage

  nv show service dhcp-server6 <vrf-id> pool <pool-id> [options] [<attribute> ...]

### Description

  DHCP Pool

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <pool-id>             DHCP6 pool subnet.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  domain-name-server    DHCP domain name servers

  domain-name           DHCP domain names

  range                 IP Address range assignments

## nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id>

### Usage

  nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <pool-id>             DHCP6 pool subnet.

  <server-id>           DNS server

## nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id>

### Usage

  nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> [options]

### Description

  TBD

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <pool-id>             DHCP6 pool subnet.

  <domain-name-id>      DHCP domain name

## nv show service dhcp-server6 <vrf-id> pool <pool-id> range <range-id>

### Usage

  nv show service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> [options]

### Description

  DHCP Pool range

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <pool-id>             DHCP6 pool subnet.

  <range-id>            DHCP client interface

## nv show service dhcp-server6 <vrf-id> domain-name <domain-name-id>

### Usage

  nv show service dhcp-server6 <vrf-id> domain-name <domain-name-id> [options]

### Description

  TBD

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <domain-name-id>      DHCP domain name

## nv show service dhcp-server6 <vrf-id> domain-name-server <server-id>

### Usage

  nv show service dhcp-server6 <vrf-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <server-id>           DNS server

## nv show service dhcp-server6 <vrf-id> static <static-id>

### Usage

  nv show service dhcp-server6 <vrf-id> static <static-id> [options]

### Description

  static entry

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <static-id>           static mapping nane

## nv show service lldp

### Usage

  nv show service lldp [options]

### Description

  Global LLDP

## nv show system

### Usage

  nv show system [options] [<attribute> ...]

### Description

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

## nv show system control-plane

### Usage

  nv show system control-plane [options] [<attribute> ...]

### Description

  Control Plane specific configurations

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  trap                  Traps

  policer               Policers

## nv show system control-plane trap <trap-id>

### Usage

  nv show system control-plane trap <trap-id> [options]

### Description

  Trap

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <trap-id>             TRAP ID

## nv show system control-plane policer <policer-id>

### Usage

  nv show system control-plane policer <policer-id> [options] [<attribute> ...]

### Description

  Policer

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <policer-id>          Policer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  statistics            Policer Statistics

## nv show system control-plane policer <policer-id> statistics

### Usage

  nv show system control-plane policer <policer-id> statistics [options]

### Description

  Policer Statistics

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <policer-id>          Policer ID

## nv show system message

### Usage

  nv show system message [options]

### Description

  System pre-login and post-login messages

## nv show system global

### Usage

  nv show system global [options] [<attribute> ...]

### Description

  global system configuration

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  reserved              reserved ranges

## nv show system global reserved

### Usage

  nv show system global reserved [options] [<attribute> ...]

### Description

  reserved ranges

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  routing-table         reserved routing table ranges

  vlan                  reserved vlan ranges

## nv show system global reserved routing-table

### Usage

  nv show system global reserved routing-table [options] [<attribute> ...]

### Description

  reserved routing table ranges

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  pbr                   reserved routing table ranges for PBR

## nv show system global reserved routing-table pbr

### Usage

  nv show system global reserved routing-table pbr [options]

### Description

  reserved routing table ranges for PBR

## nv show system global reserved vlan

### Usage

  nv show system global reserved vlan [options] [<attribute> ...]

### Description

  reserved vlan ranges

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  l3-vni-vlan           Reserved vlans to be used with l3vni

## nv show system global reserved vlan l3-vni-vlan

### Usage

  nv show system global reserved vlan l3-vni-vlan [options]

### Description

  Reserved vlans to be used with l3vni

## nv show system ztp

### Usage

  nv show system ztp [options] [<attribute> ...]

### Description

  System Zero Touch Provisioning

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  script                Zero Touch Provisioning Script

  status                Zero Touch Provisioning Last Status

## nv show system ztp script

### Usage

  nv show system ztp script [options]

### Description

  Zero Touch Provisioning Script

## nv show system ztp status

### Usage

  nv show system ztp status [options]

### Description

  Zero Touch Provisioning Last Status

## nv show system reboot

### Usage

  nv show system reboot [options] [<attribute> ...]

### Description

  Platform reboot info

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  reason                Platform reboot reason

  history               Platform reboot history

## nv show system reboot reason

### Usage

  nv show system reboot reason [options]

### Description

  Platform reboot reason

## nv show system reboot history

### Usage

  nv show system reboot history [options]

### Description

  Platform reboot history

## nv show system port-mirror

### Usage

  nv show system port-mirror [options] [<attribute> ...]

### Description

  Port mirror

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  session               sessions

## nv show system port-mirror session

### Usage

  nv show system port-mirror session [options] [<session-id> ...]

### Description

  sessions

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

## nv show system port-mirror session <session-id>

### Usage

  nv show system port-mirror session <session-id> [options] [<attribute> ...]

### Description

  port mirror session number

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  span                  Switched Port Analyzer

  erspan                Encapsulated Remote Switched Port Analyzer.

## nv show system port-mirror session <session-id> span

### Usage

  nv show system port-mirror session <session-id> span [options] [<attribute> ...]

### Description

  Switched Port Analyzer

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  source-port           Set of source ports.

  destination           The SPAN destination port.
  truncate              TBD

## nv show system port-mirror session <session-id> span source-port

### Usage

  nv show system port-mirror session <session-id> span source-port [options] [<port-id> ...]

### Description

  Set of source ports.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

  <port-id>             Port interface

## nv show system port-mirror session <session-id> span source-port <port-id>

### Usage

  nv show system port-mirror session <session-id> span source-port <port-id> [options]

### Description

  A port-mirror source port (swps or bonds only)

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

  <port-id>             Port interface

## nv show system port-mirror session <session-id> span destination

### Usage

  nv show system port-mirror session <session-id> span destination [options] [<port-id> ...]

### Description

  The SPAN destination port.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

  <port-id>             Port interface

## nv show system port-mirror session <session-id> span destination <port-id>

### Usage

  nv show system port-mirror session <session-id> span destination <port-id> [options]

### Description

  The SPAN destination port.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

  <port-id>             Port interface

## nv show system port-mirror session <session-id> span truncate

### Usage

  nv show system port-mirror session <session-id> span truncate [options]

### Description

  TBD

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

## nv show system port-mirror session <session-id> erspan

### Usage

  nv show system port-mirror session <session-id> erspan [options] [<attribute> ...]

### Description

  Encapsulated Remote Switched Port Analyzer.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  source-port           Set of source ports.

  destination           erspan destination

  truncate              TBD

## nv show system port-mirror session <session-id> erspan source-port

### Usage

  nv show system port-mirror session <session-id> erspan source-port [options] [<port-id> ...]

### Description

  Set of source ports.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

  <port-id>             Port interface

## nv show system port-mirror session <session-id> erspan source-port <port-id>

### Usage

  nv show system port-mirror session <session-id> erspan source-port <port-id> [options]

### Description

  A port-mirror source port (swps or bonds only)

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

  <port-id>             Port interface

## nv show system port-mirror session <session-id> erspan destination

### Usage

  nv show system port-mirror session <session-id> erspan destination [options] [<attribute> ...]

### Description

  erspan destination

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  source-ip             TBD

  dest-ip               TBD

## nv show system port-mirror session <session-id> erspan destination source-ip

### Usage

  nv show system port-mirror session <session-id> erspan destination source-ip [options] [<source-ip> ...]

### Description

  Set of IPv4 addresses

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

  <source-ip>           IPv4 address

## nv show system port-mirror session <session-id> erspan destination source-ip <source-ip>

### Usage

  nv show system port-mirror session <session-id> erspan destination source-ip <source-ip> [options]

### Description

  An IPv4 address

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

## nv show system port-mirror session <session-id> erspan destination dest-ip

### Usage

  nv show system port-mirror session <session-id> erspan destination dest-ip [options] [<dest-ip> ...]

### Description

  Set of IPv4 addresses

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

  <dest-ip>             IPv4 address

## nv show system port-mirror session <session-id> erspan destination dest-ip <dest-ip>

### Usage

  nv show system port-mirror session <session-id> erspan destination dest-ip <dest-ip> [options]

### Description

  An IPv4 address

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

## nv show system port-mirror session <session-id> erspan truncate

### Usage

  nv show system port-mirror session <session-id> erspan truncate [options]

### Description

  TBD

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <session-id>          port mirror session number

## nv show system config

### Usage

  nv show system config [options] [<attribute> ...]

### Description

  Affect how config operations are performed.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  apply                 Affect how config apply operations are performed.

  snippet               Configuration file snippets that will be loaded as written into the appropriate configuration file during a foundation unit's lifecycle. This is essentially a copy-paste operation to handle gaps in the current CUE
                        OM.

## nv show system config apply

### Usage

  nv show system config apply [options] [<attribute> ...]

### Description

  Affect how config apply operations are performed.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ignore                Set of files to ignore during config apply operations.

## nv show system config apply ignore

### Usage

  nv show system config apply ignore [options] [<ignore-id> ...]

### Description

  Set of files to ignore during config apply operations.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <ignore-id>           Ignored file

## nv show system config apply ignore <ignore-id>

### Usage

  nv show system config apply ignore <ignore-id> [options]

### Description

  File to ignore during config apply operations.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <ignore-id>           Ignored file

## nv show system config snippet

### Usage

  nv show system config snippet [options]

### Description

  Configuration file snippets that will be loaded as written into the appropriate configuration file during a foundation unit's
  lifecycle.  This is essentially a copy-paste operation to handle gaps in the current CUE OM.

## nv show vrf

### Usage

  nv show vrf [options] [<vrf-id> ...]

### Description

  VRFs

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id>

### Usage

  nv show vrf <vrf-id> [options] [<attribute> ...]

### Description

  A VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  loopback              The loopback IP interface associated with this VRF.

  evpn                  EVPN control plane config and info for VRF

  router                A VRF

  ptp                   VRF PTP configuration. Inherited by interfaces in this VRF.

## nv show vrf <vrf-id> loopback

### Usage

  nv show vrf <vrf-id> loopback [options] [<attribute> ...]

### Description

  The loopback IP interface associated with this VRF.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ip                    Properties associated with the loopback IP address on this VRF.

## nv show vrf <vrf-id> loopback ip

### Usage

  nv show vrf <vrf-id> loopback ip [options] [<attribute> ...]

### Description

  IP addresses associated with the VRF's loopback interface.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  address               static IPv4 or IPv6 address

## nv show vrf <vrf-id> loopback ip address <ip-prefix-id>

### Usage

  nv show vrf <vrf-id> loopback ip address <ip-prefix-id> [options]

### Description

  An IP address with prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <ip-prefix-id>        IPv4 or IPv6 address and route prefix in CIDR notation

## nv show vrf <vrf-id> evpn

### Usage

  nv show vrf <vrf-id> evpn [options] [<attribute> ...]

### Description

  EVPN control plane config and info for VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  vni                   L3 VNI

## nv show vrf <vrf-id> evpn vni <vni-id>

### Usage

  nv show vrf <vrf-id> evpn vni <vni-id> [options]

### Description

  VNI

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <vni-id>              VxLAN ID

## nv show vrf <vrf-id> router

### Usage

  nv show vrf <vrf-id> router [options] [<attribute> ...]

### Description

  A VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  rib                   RIB Routes

  bgp                   BGP VRF configuration.

  static                Routes

  pim                   PIM VRF configuration.

  ospf                  OSPF VRF configuration.

## nv show vrf <vrf-id> router rib <afi>

### Usage

  nv show vrf <vrf-id> router rib <afi> [options] [<attribute> ...]

### Description

  Vrf aware Routing-table per address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <afi>                 Route address family.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  protocol              Import protocols from RIB to FIB

  route                 RIB Routes with info.

## nv show vrf <vrf-id> router rib <afi> protocol <import-protocol-id>

### Usage

  nv show vrf <vrf-id> router rib <afi> protocol <import-protocol-id> [options]

### Description

  Import Protocols from where routes are known

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <afi>                 Route address family.

  <import-protocol-id>  Import protocol list.

## nv show vrf <vrf-id> router rib <afi> route <route-id>

### Usage

  nv show vrf <vrf-id> router rib <afi> route <route-id> [options] [<attribute> ...]

### Description

  A route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <afi>                 Route address family.

  <route-id>            IP prefix

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  protocol              Route entries

## nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id>

### Usage

  nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> [options] [<attribute> ...]

### Description

  Protocol types from where routes are known

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <afi>                 Route address family.

  <route-id>            IP prefix

  <protocol-id>         Route entry list keys.

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  entry-index           Route entries

## nv show vrf <vrf-id> router bgp

### Usage

  nv show vrf <vrf-id> router bgp [options] [<attribute> ...]

### Description

  BGP VRF configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

## nv show vrf <vrf-id> router bgp address-family

### Usage

  nv show vrf <vrf-id> router bgp address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4-unicast          IPv4 unicast address family

  l2vpn-evpn            BGP VRF configuration. L2VPN EVPN address family

  ipv6-unicast          IPv6 unicast address family

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast [options] [<attribute> ...]

### Description

  IPv4 unicast address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute [options] [<attribute> ...]

### Description

  Route redistribute

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  static                Route redistribution of ipv4 static routes

  connected             Route redistribution of ipv4 connected routes

  kernel                Route redistribution of ipv4 kernel routes

  ospf                  Route redistribution of ipv4 ospf routes

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> [options]

### Description

  An IPv4 aggregate route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <aggregate-route-id>  IPv4 address and route prefix in CIDR notation

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> [options]

### Description

  An IPv4 static network.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <static-network-id>   IPv4 address and route prefix in CIDR notation

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import [options] [<attribute> ...]

### Description

  Route import

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  from-vrf              Controls for VRF to VRF route leaking for this address-family

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf [options] [<attribute> ...]

### Description

  Controls for VRF to VRF route leaking for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  list                  List of VRFs the routes can be imported from

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id> [options]

### Description

  A VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <leak-vrf-id>         VRF

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast multipaths

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast multipaths [options]

### Description

  Multipaths

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance [options]

### Description

  Admin distances.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export [options] [<attribute> ...]

### Description

  Route export

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  to-evpn               Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn [options]

### Description

  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib [options] [<attribute> ...]

### Description

  IPv4 local RIB

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route                 IPv6 routes

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> [options] [<attribute> ...]

### Description

  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv4 address and route prefix in CIDR notation

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  path                  IP route paths

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> [options] [<attribute> ...]

### Description

  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id> [options]

### Description

  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

  <nexthop-id>          Nexthop Id

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> peer

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> peer [options]

### Description

  Nexthop peer information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> flags

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> flags [options]

### Description

  Route flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> bestpath

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> bestpath [options]

### Description

  A bestpath information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> aspath

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> aspath [options]

### Description

  AS paths

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> community

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> community [options]

### Description

  Set of community names for community-list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> large-community

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> large-community [options]

### Description

  Set of community names for large community list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> ext-community

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> ext-community [options]

### Description

  extended communities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv4 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family l2vpn-evpn

### Usage

  nv show vrf <vrf-id> router bgp address-family l2vpn-evpn [options]

### Description

  BGP VRF configuration. L2VPN EVPN address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast [options] [<attribute> ...]

### Description

  IPv6 unicast address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> [options]

### Description

  An IPv6 aggregate route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <aggregate-route-id>  IPv6 address and route prefix in CIDR notation

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> [options]

### Description

  An IPv6 static network.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <static-network-id>   IPv6 address and route prefix in CIDR notation

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import [options] [<attribute> ...]

### Description

  Route import

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  from-vrf              Controls for VRF to VRF route leaking for this address-family

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf [options] [<attribute> ...]

### Description

  Controls for VRF to VRF route leaking for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  list                  List of VRFs the routes can be imported from

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list [options]

### Description

  Set of VRFs

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast multipaths

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast multipaths [options]

### Description

  Multipaths

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance [options]

### Description

  Admin distances.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export [options] [<attribute> ...]

### Description

  Route export

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  to-evpn               Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn [options]

### Description

  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute [options] [<attribute> ...]

### Description

  Route redistribute

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  static                Route redistribution of ipv4 static routes

  connected             Route redistribution of ipv4 connected routes

  kernel                Route redistribution of ipv4 kernel routes

  ospf6                 Route redistribution of ipv6 ospf routes

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib [options] [<attribute> ...]

### Description

  IPv6 local RIB

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route                 IPv6 routes

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> [options] [<attribute> ...]

### Description

  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv6 address and route prefix in CIDR notation

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  path                  IP route paths

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> [options] [<attribute> ...]

### Description

  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id>

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id> [options]

### Description

  An IPv4/IPv6 route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

  <nexthop-id>          Nexthop Id


## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> peer

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> peer [options]

### Description

  Nexthop peer information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> flags

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> flags [options]

### Description

  Route flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> bestpath

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> bestpath [options]

### Description

  A bestpath information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> aspath

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> aspath [options]

### Description

  AS paths

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> community

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> community [options]

### Description

  Set of community names for community-list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> large-community

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> large-community [options]

### Description

  Set of community names for large community list

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> ext-community

### Usage

  nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> ext-community [options]

### Description

  extended communities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IPv6 address and route prefix in CIDR notation

  <path-id>             Path Id

## nv show vrf <vrf-id> router bgp path-selection

### Usage

  nv show vrf <vrf-id> router bgp path-selection [options] [<attribute> ...]

### Description

  BGP path-selection configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  aspath                BGP aspath path-selection config, applicable to this BGP instance

  med                   BGP med path-selection config, applicable to this BGP instance

  multipath             BGP multipath path-selection config, applicable to this BGP instance

## nv show vrf <vrf-id> router bgp path-selection aspath

### Usage

  nv show vrf <vrf-id> router bgp path-selection aspath [options]

### Description

  BGP aspath path-selection config, applicable to this BGP instance

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp path-selection med

### Usage

  nv show vrf <vrf-id> router bgp path-selection med [options]

### Description

  BGP med path-selection config, applicable to this BGP instance

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp path-selection multipath

### Usage

  nv show vrf <vrf-id> router bgp path-selection multipath [options]

### Description

  BGP multipath path-selection config, applicable to this BGP instance

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp route-reflection

### Usage

  nv show vrf <vrf-id> router bgp route-reflection [options]

### Description

  BGP route-reflection configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id>

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> [options] [<attribute> ...]

### Description

  BGP global configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF
  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  bfd                   Specifies whether to track BGP peering sessions using this configuration via BFD.

  ttl-security          RFC 5082

  capabilities          Capabilities

  graceful-restart      Graceful restart

  local-as              Local AS feature

  timers                Peer peer-timerss

  address-family        Address family specific configuration

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> bfd

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> bfd [options]

### Description

  Specifies whether to track BGP peering sessions using this configuration via BFD.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security [options]

### Description

  RFC 5082

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities [options]

### Description

  Capabilities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart [options]

### Description

  BGP Graceful restart per neighbor configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> local-as

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> local-as [options]

### Description

  Local AS feature

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> timers

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> timers [options]

### Description

  Peer peer-timerss

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4-unicast          Peer IPv4 unicast address family. Always on, unless disabled globaly.

  ipv6-unicast          Peer IPv6 unicast address family.

  l2vpn-evpn            Peer l2vpn EVPN address family.

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast [options] [<attribute> ...]

### Description

  Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise [options]

### Description

  Community advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod [options]

### Description

  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn [options]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Limits on inbound prefix from the peer for this address-family

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound [options]

### Description

  Limits on inbound prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination [options]

### Description

  Default route origination

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv4 unicast

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Outbound unicast policy

  outbound              Outbound unicast policy

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound [options]

### Description

  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound [options]

### Description

  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise [options]

### Description

  Conditional advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast [options] [<attribute> ...]

### Description

  Peer IPv6 unicast address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv6 unicast

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Outbound unicast policy

  outbound              Outbound unicast policy

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound [options]

### Description

  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound [options]

### Description

  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn [options]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Limits on inbound prefix from the peer for this address-family

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound [options]

### Description

  Limits on inbound prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination [options]

### Description

  Default route origination

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise [options]

### Description

  Community advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod [options]

### Description

  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise [options]

### Description

  Conditional advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn [options] [<attribute> ...]

### Description

  Peer l2vpn EVPN address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  policy                Policies for l2vpn evpn

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod [options]

### Description

  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn [options]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy [options] [<attribute> ...]

### Description

  Policies for l2vpn evpn

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Inbound l2vpn-evpn policy

  outbound              Outbound l2vpn-evpn policy

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound [options]

### Description

  Inbound l2vpn-evpn policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound

### Usage

  nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound [options]

### Description

  Outbound l2vpn-evpn policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <peer-group-id>       Domain

## nv show vrf <vrf-id> router bgp route-export

### Usage

  nv show vrf <vrf-id> router bgp route-export [options] [<attribute> ...]

### Description

  Controls for exporting ipv4 and ipv6 routes from this VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  to-evpn               Controls for exporting routes from this VRF into EVPN

## nv show vrf <vrf-id> router bgp route-export to-evpn

### Usage

  nv show vrf <vrf-id> router bgp route-export to-evpn [options] [<attribute> ...]

### Description

  Controls for exporting routes from this VRF into EVPN

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route-target          List the RTs to attach to host or prefix routes when exporting them into EVPN or "auto". If "auto", the RT  will be derived. This is the default.

## nv show vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id>

### Usage

  nv show vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id> [options]

### Description

  A route target identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <rt-id>               Route targets or "auto"

## nv show vrf <vrf-id> router bgp route-import

### Usage

  nv show vrf <vrf-id> router bgp route-import [options] [<attribute> ...]

### Description

  Controls for importing of ipv4 and ipv6 routes from this VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  from-evpn             Controls for importing EVPN type-2 and type-5 routes into this VRF

## nv show vrf <vrf-id> router bgp route-import from-evpn

### Usage

  nv show vrf <vrf-id> router bgp route-import from-evpn [options] [<attribute> ...]

### Description

  Controls for importing EVPN type-2 and type-5 routes into this VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  route-target          List the RTs to attach to host or prefix routes when importing them into VRF or "auto". If "auto", the RT will be derived. This is the default.

## nv show vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id>

### Usage

  nv show vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id> [options]

### Description

  A route target identifier

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <rt-id>               Route targets or "auto"

## nv show vrf <vrf-id> router bgp timers

### Usage

  nv show vrf <vrf-id> router bgp timers [options]

### Description

  timer values for all peers in this VRF

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp confederation

### Usage

  nv show vrf <vrf-id> router bgp confederation [options] [<attribute> ...]

### Description

  BGP Confederation options.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  member-as             Confederation ASNs of the peers, maps to BGP  confederation peers

## nv show vrf <vrf-id> router bgp confederation member-as

### Usage

  nv show vrf <vrf-id> router bgp confederation member-as [options]

### Description

  Set of autonomous numbers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id>

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> [options] [<attribute> ...]

### Description

  BGP global configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

  timers                Peer peer-timerss

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> bfd

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> bfd [options]

### Description

  Specifies whether to track BGP peering sessions using this configuration via BFD.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities [options]

### Description

  Capabilities

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> local-as

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> local-as [options]

### Description

  Local AS feature

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart [options]

### Description

  BGP Graceful restart per neighbor configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security [options]

### Description

  RFC 5082

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop [options]

### Description

  Nexthop

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> message-stats

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> message-stats [options]

### Description

  Message statistics

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ebgp-policy

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ebgp-policy [options]

### Description

  EBGP Policy RFC8212

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4-unicast          Peer IPv4 unicast address family. Always on, unless disabled globaly.

  ipv6-unicast          Peer IPv6 unicast address family.

  l2vpn-evpn            Peer l2vpn EVPN address family.

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast [options] [<attribute> ...]

### Description

  Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod [options]

### Description

  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn [options]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv4 unicast

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Outbound unicast policy

  outbound              Outbound unicast policy

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound [options]

### Description

  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound [options]

### Description

  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF
  
  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Limits on inbound prefix from the peer for this address-family

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound [options]

### Description

  Limits on inbound prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination [options]

### Description

  Default route origination

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise [options]

### Description

  Community advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise [options]

### Description

  Conditional advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast capabilities

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast capabilities [options]

### Description

  AF capabilities advertised and received

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast graceful-restart

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast graceful-restart [options]

### Description

  graceful restart information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast [options] [<attribute> ...]

### Description

  Peer IPv6 unicast address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod [options]

### Description

  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn [options]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Limits on inbound prefix from the peer for this  address-family

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound [options]

### Description

  Limits on inbound prefix from the peer for this address-family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination [options]

### Description

  Default route origination

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv6 unicast

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Outbound unicast policy

  outbound              Outbound unicast policy

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound [options]

### Description

  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound [options]

### Description

  Outbound unicast policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise [options]

### Description

  Community advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise [options]

### Description

  Conditional advertise for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast capabilities

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast capabilities [options]

### Description

  AF capabilities advertised and received

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast graceful-restart

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast graceful-restart [options]

### Description

  graceful restart information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn

## Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn [options] [<attribute> ...]

### Description

  Peer l2vpn EVPN address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  policy                Policies for l2vpn evpn

  capabilities          AF capabilities advertised and received

  graceful-restart      graceful restart information

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod [options]

### Description

  Attribute mod for address family.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  allow-my-asn          If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn [options]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy [options] [<attribute> ...]

### Description

  Policies for l2vpn evpn

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  inbound               Inbound l2vpn-evpn policy

  outbound              Outbound l2vpn-evpn policy

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound [options]

### Description

  Inbound l2vpn-evpn policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound [options]

### Description

  Outbound l2vpn-evpn policy

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn capabilities

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn capabilities [options]

### Description

  AF capabilities advertised and received

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn graceful-restart

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn graceful-restart [options]

### Description

  graceful restart information

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router bgp neighbor <neighbor-id> timers

### Usage

  nv show vrf <vrf-id> router bgp neighbor <neighbor-id> timers [options]

### Description

  Peer peer-timerss

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <neighbor-id>         Peer ID

## nv show vrf <vrf-id> router static <route-id>

### Usage

  nv show vrf <vrf-id> router static <route-id> [options] [<attribute> ...]

### Description

  A route

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IP prefix

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  distance              Paths

  via                   Nexthops

## nv show vrf <vrf-id> router static <route-id> distance <distance-id>

### Usage

  nv show vrf <vrf-id> router static <route-id> distance <distance-id> [options] [<attribute> ...]

### Description

  A path

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IP prefix

  <distance-id>         A path distance

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  via                   Nexthops

## nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id>

### Usage

  nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> [options] [<attribute> ...]

### Description

  A via

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IP prefix

  <distance-id>         A path distance

  <via-id>              IP address, interface, or "blackhole".

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  flag                  Nexthop flags

## nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag

### Usage

  nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag [options]

### Description

  Nexthop flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IP prefix

  <distance-id>         A path distance

  <via-id>              IP address, interface, or "blackhole".

## nv show vrf <vrf-id> router static <route-id> via <via-id>

### Usage

  nv show vrf <vrf-id> router static <route-id> via <via-id> [options] [<attribute> ...]

### Description

  A via

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IP prefix

  <via-id>              IP address, interface, or "blackhole".

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  flag                  Nexthop flags

## nv show vrf <vrf-id> router static <route-id> via <via-id> flag

### Usage

  nv show vrf <vrf-id> router static <route-id> via <via-id> flag [options]

### Description

  Nexthop flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <route-id>            IP prefix

  <via-id>              IP address, interface, or "blackhole".

## nv show vrf <vrf-id> router pim

### Usage

  nv show vrf <vrf-id> router pim [options] [<attribute> ...]

### Description

  PIM VRF configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  timers                Timers

  ecmp                  Choose all available ECMP paths for a particular RPF. If 'off', the first nexthop found will be used. This is the default.

  msdp-mesh-group       To connect multiple PIM-SM multicast domains using RPs.

  address-family        Address family specific configuration

## nv show vrf <vrf-id> router pim timers

### Usage

  nv show vrf <vrf-id> router pim timers [options]

### Description

  Timers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router pim ecmp

### Usage

  nv show vrf <vrf-id> router pim ecmp [options]

### Description

  Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id>

### Usage

  nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> [options] [<attribute> ...]

### Description

  MSDP mesh-group

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <msdp-mesh-group-id>  MSDP mesh group name

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  member-address        Set of member-address

## nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id>

### Usage

  nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id> [options]

### Description

  A MSDP mesh member

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <msdp-mesh-group-id>  MSDP mesh group name

  <mesh-member-id>      MSDP mesh-group member IP address

## nv show vrf <vrf-id> router pim address-family

### Usage

  nv show vrf <vrf-id> router pim address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  ipv4-unicast          IPv4 unicast address family

## nv show vrf <vrf-id> router pim address-family ipv4-unicast

### Usage

  nv show vrf <vrf-id> router pim address-family ipv4-unicast [options] [<attribute> ...]

### Description

  IPv4 unicast address family

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  spt-switchover        Build shortest path tree towards source.

  rp                    RP address and associated group range.

## nv show vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover

### Usage

  nv show vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover [options]

### Description

  Build shortest path tree towards source.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id>

### Usage

  nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> [options] [<attribute> ...]

### Description

  RP

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <rp-id>               RP IP address

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  group-range           Set of group range assocaited to RP.

## nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id>

### Usage

  nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id> [options]

### Description

  A group range

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <rp-id>               RP IP address

  <group-range-id>      Group range associated to RP.

## nv show vrf <vrf-id> router ospf

### Usage

  nv show vrf <vrf-id> router ospf [options] [<attribute> ...]

### Description

  OSPF VRF configuration.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

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

## nv show vrf <vrf-id> router ospf area <area-id>

### Usage

  nv show vrf <vrf-id> router ospf area <area-id> [options] [<attribute> ...]

### Description

  An OSPF area

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <area-id>             Area

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  filter-list           Filters networks between OSPF areas

  range                 Area ranges

  network               Area networks

## nv show vrf <vrf-id> router ospf area <area-id> filter-list

### Usage

  nv show vrf <vrf-id> router ospf area <area-id> filter-list [options]

### Description

  Filters networks between OSPF areas

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <area-id>             Area

## nv show vrf <vrf-id> router ospf area <area-id> range <range-id>

### Usage

  nv show vrf <vrf-id> router ospf area <area-id> range <range-id> [options]

### Description

  Filters out components of the prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <area-id>             Area

  <range-id>            Range

## nv show vrf <vrf-id> router ospf area <area-id> network <network-id>

### Usage

  nv show vrf <vrf-id> router ospf area <area-id> network <network-id> [options]

### Description

  Filters out components of the prefix

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

  <area-id>             Area

  <network-id>          Network

## nv show vrf <vrf-id> router ospf default-originate

### Usage

  nv show vrf <vrf-id> router ospf default-originate [options]

### Description

  Advertise a default route as external lsa

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router ospf distance

### Usage

  nv show vrf <vrf-id> router ospf distance [options]

### Description

  Administrative distance for installation into the rib

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router ospf max-metric

### Usage

  nv show vrf <vrf-id> router ospf max-metric [options]

### Description

  Set maximum metric value in router lsa to make stub router

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router ospf log

### Usage

  nv show vrf <vrf-id> router ospf log [options]

### Description

  Log configuration

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router ospf redistribute

### Usage

  nv show vrf <vrf-id> router ospf redistribute [options] [<attribute> ...]

### Description

  Route redistribute

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  static                Route redistribute of static routes

  connected             Route redistribute of connected routes

  kernel                Route redistribute of kernel routes

  bgp                   Route redistribute of bgp routes

## nv show vrf <vrf-id> router ospf redistribute static

### Usage

  nv show vrf <vrf-id> router ospf redistribute static [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router ospf redistribute connected

### Usage

  nv show vrf <vrf-id> router ospf redistribute connected [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router ospf redistribute kernel

### Usage

  nv show vrf <vrf-id> router ospf redistribute kernel [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router ospf redistribute bgp

### Usage

  nv show vrf <vrf-id> router ospf redistribute bgp [options]

### Description

  Source route type.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router ospf timers

### Usage

  nv show vrf <vrf-id> router ospf timers [options] [<attribute> ...]

### Description

  Timers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  lsa                   LSA timers

  spf                   SPF timers

## nv show vrf <vrf-id> router ospf timers lsa

### Usage

  nv show vrf <vrf-id> router ospf timers lsa [options]

### Description

  LSA timers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> router ospf timers spf

### Usage

  nv show vrf <vrf-id> router ospf timers spf [options]

### Description

  SPF timers

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show vrf <vrf-id> ptp

### Usage

  nv show vrf <vrf-id> ptp [options]

### Description

  VRF PTP configuration.  Inherited by interfaces in this VRF.

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <vrf-id>              VRF

## nv show nve

### Usage

  nv show nve [options] [<attribute> ...]

### Description

  Network Virtualization configuration and operational info

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  vxlan                 Global VxLAN configuration and operational properties.

## nv show nve vxlan

### Usage

  nv show nve vxlan [options] [<attribute> ...]

### Description

  VxLAN

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  mlag                  VxLAN specific MLAG address

  source                Source address

  flooding              Configuration to specify how BUM traffic in the overlay is handled. This applies to all overlays (VNIs), but can be overridden by VNI-specific configuration.

## nv show nve vxlan mlag

### Usage

  nv show nve vxlan mlag [options]

### Description

  VxLAN specfic MLAG configuration

## nv show nve vxlan source

### Usage

  nv show nve vxlan source [options]

### Description

  Source address

## nv show nve vxlan flooding

### Usage

  nv show nve vxlan flooding [options] [<attribute> ...]

### Description

  Handling of BUM traffic

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  head-end-replication  BUM traffic is replicated and individual copies sent to remote destinations.

## nv show nve vxlan flooding head-end-replication

### Usage

  nv show nve vxlan flooding head-end-replication [options] [<hrep-id> ...]

### Description

  Set of IPv4 unicast addresses or "evpn".

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <hrep-id>             IPv4 unicast addresses or "evpn"

## nv show nve vxlan flooding head-end-replication <hrep-id>

### Usage

  nv show nve vxlan flooding head-end-replication <hrep-id> [options]

### Description

  Set of IPv4 unicast addresses or "evpn".

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <hrep-id>             IPv4 unicast addresses or "evpn"

## nv show acl

### Usage

  nv show acl [options] [<acl-id> ...]

### Description

  ACL rules

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

## nv show acl <acl-id>

### Usage

  nv show acl <acl-id> [options] [<attribute> ...]

### Description

  An ACL is used for matching packets and take actions

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  rule                  acl rule

## nv show acl <acl-id> rule <rule-id>

### Usage

  nv show acl <acl-id> rule <rule-id> [options] [<attribute> ...]

### Description

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

## nv show acl <acl-id> rule <rule-id> match

### Usage

  nv show acl <acl-id> rule <rule-id> match [options] [<attribute> ...]

### Description

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

## nv show acl <acl-id> rule <rule-id> match ip

### Usage

  nv show acl <acl-id> rule <rule-id> match ip [options] [<attribute> ...]

### Description

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

## nv show acl <acl-id> rule <rule-id> match ip source-port <ip-port-id>

### Usage

  nv show acl <acl-id> rule <rule-id> match ip source-port <ip-port-id> [options]

### Description

  L4 port

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

  <ip-port-id>          IP port ID

## nv show acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id>

### Usage

  nv show acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id> [options]

### Description

  L4 port

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

  <ip-port-id>          IP port ID

## nv show acl <acl-id> rule <rule-id> match ip fragment

### Usage

  nv show acl <acl-id> rule <rule-id> match ip fragment [options]

### Description

  State details

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

## nv show acl <acl-id> rule <rule-id> match ip ecn

### Usage

  nv show acl <acl-id> rule <rule-id> match ip ecn [options] [<attribute> ...]

### Description

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

## nv show acl <acl-id> rule <rule-id> match ip ecn flags

### Usage

  nv show acl <acl-id> rule <rule-id> match ip ecn flags [options]

### Description

  ECN flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

## nv show acl <acl-id> rule <rule-id> match ip tcp

### Usage

  nv show acl <acl-id> rule <rule-id> match ip tcp [options] [<attribute> ...]

### Description

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

## nv show acl <acl-id> rule <rule-id> match ip tcp flags

### Usage

  nv show acl <acl-id> rule <rule-id> match ip tcp flags [options]

### Description

  TCP flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

## nv show acl <acl-id> rule <rule-id> match ip tcp mask

### Usage

  nv show acl <acl-id> rule <rule-id> match ip tcp mask [options]

### Description

  TCP flags

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

## nv show acl <acl-id> rule <rule-id> match mac

### Usage

  nv show acl <acl-id> rule <rule-id> match mac [options]

### Description

  An ACL MAC match

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

## nv show acl <acl-id> rule <rule-id> action

### Usage

  nv show acl <acl-id> rule <rule-id> action [options] [<attribute> ...]

### Description

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

## nv show acl <acl-id> rule <rule-id> action permit

### Usage

  nv show acl <acl-id> rule <rule-id> action permit [options]

### Description

  Permit packets

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

## nv show acl <acl-id> rule <rule-id> action deny

### Usage

  nv show acl <acl-id> rule <rule-id> action deny [options]

### Description

  deny packets

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

## nv show acl <acl-id> rule <rule-id> action log

### Usage

  nv show acl <acl-id> rule <rule-id> action log [options]

### Description

  log packets

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

## nv show acl <acl-id> rule <rule-id> action set

### Usage

  nv show acl <acl-id> rule <rule-id> action set [options]

### Description

  Set action for packets

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

## nv show acl <acl-id> rule <rule-id> action erspan

### Usage

  nv show acl <acl-id> rule <rule-id> action erspan [options]

### Description

  ERSPAN session

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID

  <rule-id>             ACL rule number

## nv show acl <acl-id> rule <rule-id> action police

### Usage

  nv show acl <acl-id> rule <rule-id> action police [options]

### Description

  Policing of matched packets/bytes

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |

  <acl-id>              ACL ID
  
  <rule-id>             ACL rule number
