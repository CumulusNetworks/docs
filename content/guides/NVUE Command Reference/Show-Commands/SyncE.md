---
title: SyncE
author: Cumulus Networks
weight: 475
product: Cumulus Linux
type: nojsscroll
draft: true
---
## <h>nv show interface \<interface-id\> synce</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> synce counters</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service synce</h>

Shows global SyncE configuration.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service synce
```
