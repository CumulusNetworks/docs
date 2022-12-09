---
title: PBR Commands
author: Cumulus Networks
weight: 200
product: Cumulus Linux
type: nojsscroll
---
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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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