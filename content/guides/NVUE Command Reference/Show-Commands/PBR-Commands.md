---
title: PBR Commands
author: Cumulus Networks
weight: 190
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> router pbr

Shows PBR configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 router pbr
```

- - -

## nv show interface \<interface-id\> router pbr map

Shows the PBR maps configured for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 router pbr map
```

- - -

## nv show interface \<interface-id\> router pbr map \<pbr-map-id\>

Shows configuration settings for the specified PBR map on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |
| `<pbr-map-id>`   |  The route map name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 router pbr map map1
```

- - -

## nv show system global reserved routing-table pbr

Shows the PBR reserved routing table ranges.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system global reserved routing-table pbr
```

- - -

## nv show router pbr

Shows global PBR configuration settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router pbr
```

- - -

## nv show router pbr map

Shows settings for PBR maps. If you do not provide a specific map name, this command shows configuration settings for all configured maps.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router pbr map
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
cumulus@leaf01:mgmt:~$ nv show router pbr map map1
```

- - -

## nv show router pbr map \<pbr-map-id\> rule

Shows the rules for the specified PBR route map.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<pbr-map-id>` | The name of the route map. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router pbr map map1 rule
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
cumulus@leaf01:mgmt:~$ nv show router pbr map map1 rule 1
```

- - -

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\> match

Shows the rule match criteria for a PBR route map.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` | The route map name. |
| `<rule-id>` | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router pbr map map1 rule 1 match
```

- - -

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\> action

Shows the rule action for a PBR route map.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` | The route map name. |
| `<rule-id>` | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router pbr map map1 rule 1 action
```

- - -

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\> action nexthop-group

Shows the next hop groups in the PBR route map rule action.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` |  The route map name. |
| `<rule-id>` | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router pbr map map1 rule 1 action nexthop-group
```

## nv show router pbr map \<pbr-map-id\> rule \<rule-id\> action nexthop-group \<nexthop-group-id\>

Shows configuration for the specified next hop group including the IP route table number of the default route.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` |  The route map name. |
| `<rule-id>` | The PBR rule number. |
| `<nexthop-group-id>` | The next hop group name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router pbr map map1 rule 1 action nexthop-group group1
```
