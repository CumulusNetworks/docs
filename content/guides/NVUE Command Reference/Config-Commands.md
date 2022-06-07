---
title: Config Commands
author: Cumulus Networks
weight: 50
product: Cumulus Linux
---
## nv config save

Overwrites the startup file with the applied revision.

**Usage**

`nv config save [options]`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config save
```

## nv config detach

Detaches the confoiguration from the current pending revision.

**Usage**

`nv config detach [options]`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config detach
```

## nv config show

Shows the currently applied configuration.

**Usage**

`nv config show [options]`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config show
```

## nv action

Action configuration attributes.

**Usage**

`nv action [options]`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config action
```
