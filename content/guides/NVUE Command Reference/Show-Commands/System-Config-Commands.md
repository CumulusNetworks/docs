---
title: System Config Commands
author: Cumulus Networks
weight: 330
product: Cumulus Linux
type: nojsscroll
---
## nv show system config

Shows the system configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system config
```

- - -

## nv show system config apply

Shows the system configuration apply settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system config apply
```

- - -

## nv show system config apply ignore

Shows which files are ignored when you run the `nv config apply` command.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ 
```

- - -

## nv show system config apply ignore \<ignore-id\>

Shows information about the specified file you set to ignore when you run the `nv config apply` command.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<ignore-id>` | The ignored file. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system config apply ignore /etc/frr/frr.conf
```

- - -

## nv show system config snippet

Shows the file snippets you configure on the system.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system config snippet
```
