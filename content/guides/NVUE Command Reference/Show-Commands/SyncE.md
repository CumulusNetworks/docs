---
title: SyncE
author: Cumulus Networks
weight: 475
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> synce

Shows SyncE configuration information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`  |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp2 synce
```

- - -

## nv show interface \<interface-id\> synce counters

Shows SyncE statistics for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`  |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp2 synce counters
```

- - -

## nv show service synce

Shows global SyncE configuration.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service synce
```

- - -
