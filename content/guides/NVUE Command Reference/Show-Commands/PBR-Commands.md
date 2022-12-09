---
title: PBR Commands
author: Cumulus Networks
weight: 200
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> router pbr

PBR interface configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> router pbr map \<pbr-map-id\>

Interface Pbr map

### Command Syntax

| Syntax |  Description   |
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

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show router pbr

Shows global PBR configuration settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr
```

- - -

## nv show router pbr map

Shows settings for PBR maps. If you do not provide a specific map name, this command shows configuration settings for all configured maps.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr map
```

- - -

## nv show router pbr map \<pbr-map-id\>

Shows the configuration settings for a PBR map used for policy configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` | The name of the route map. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr map map1
```

- - -

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\>

Shows the match and set criteria, and the rule action for a route map.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<pbr-map-id>` | The name of the route map. |
|`<rule-id>`  |  The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr map map1 rule 1
```

- - -

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\> match

Shows the rule match criteria for a route map.

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` | The route map name. |
| `<rule-id>` | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pbr map map1 rule 1 action
```

- - -

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\> action nexthop-group \<nexthop-group-id\>

Shows information about next hop group you specify, such as if the policy is installed and the IP route table number of the default route.

### Command Syntax

| Syntax |  Description   |
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