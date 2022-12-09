---
title: Router Policy Commands
author: Cumulus Networks
weight: 280
product: Cumulus Linux
type: nojsscroll
---
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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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
