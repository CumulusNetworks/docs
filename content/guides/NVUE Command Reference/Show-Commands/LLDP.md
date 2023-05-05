---
title: LLDP
author: Cumulus Networks
weight: 200
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> lldp

Shows LLDP statistics for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 lldp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show interface \<interface-id\> lldp neighbor

Shows information about all the LLDP neighbors for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 lldp neighbor
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\>

Shows statistics for the specified LLDP neighbor for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|
| `<neighbor-id>` |  The LLDP neighbor name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 lldp neighbor spine01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge

Shows bridge information for the specified LLDP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|
| `<neighbor-id>` |  The LLDP neighbor name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 lldp neighbor spine01 bridge
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge vlan

Shows the VLANs for the specified LLDP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|
| `<neighbor-id>` |  The LLDP neighbor name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 lldp neighbor leaf02 bridge vlan
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge vlan \<vid\>

Shows information about the specified VLAN for the specified LLDP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|
| `<neighbor-id>` |  The LLDP neighbor name. |
| `<vid>` | The VLAN name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 lldp neighbor leaf02 bridge vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show service lldp

Shows global LLDP configuration, such as the LLDP mode, and LLDP timers and if 802.1 TLV transmission is on or off. By default, 802.1 TLV transmission is off and the switch sends all LLDP frames without 802.1 TLVs.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service lldp
```
