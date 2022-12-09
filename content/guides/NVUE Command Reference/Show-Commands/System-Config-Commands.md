---
title: System Config Commands
author: Cumulus Networks
weight: 330
product: Cumulus Linux
type: nojsscroll
---
## nv show system config

Affect how config operations are performed.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system config apply

Affect how config apply operations are performed.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system config apply ignore

Set of files to ignore during config apply operations.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<ignore-id>` |   Ignored file |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system config apply ignore \<ignore-id\>

File to ignore during config apply operations.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<ignore-id>` |   Ignored file |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system config snippet

Configuration file snippets that will be loaded as written into the appropriate configuration file during a foundation unit's lifecycle.  This is essentially a copy-paste operation to handle gaps in the current CUE OM.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
