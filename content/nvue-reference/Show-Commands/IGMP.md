---
title: IGMP
author: Cumulus Networks
weight: 180

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip igmp</h>

Shows IGMP configuration information on the specified interface. IGMP prevents hosts on a local network from receiving traffic for a multicast group they have not explicitly joined. IGMP snooping is for IPv4 environments.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 ip igmp
        operational  applied  pending
------  -----------  -------  -------
enable               on      on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip igmp static-group</h>

Shows information about IGMP static multicast groups configured on the interface.

### Command Syntax

| Syntax |  Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 ip igmp static-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip igmp static-group \<static-group-id\></h>

Shows information about IGMP static multicast groups configured on the interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |
| `<static-group-id>` | The IGMP static multicast mroute destination. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 ip igmp static-group 224.10.0.0
                  operational  applied   
----------------  -----------  ----------
[source-address]               10.10.10.4
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip igmp group</h>

Shows information about the IGMP groups configured on the interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show interface swp3 ip igmp group
StaticGroupID  filter-mode  source-count  timer     uptime    version  Summary
-------------  -----------  ------------  --------  --------  -------  -------------------------
225.1.101.1    exclude      1             00:02:43  00:02:56  3        source-address:         *
225.1.101.2    exclude      1             00:02:43  00:02:56  3        source-address:         *
225.1.101.3    exclude      1             00:02:43  00:02:56  3        source-address:         *
225.1.101.4    exclude      1             00:02:43  00:02:56  3        source-address:         *
225.1.101.5    exclude      1             00:02:43  00:02:56  3        source-address:         *
232.1.1.99     include      1             --:--:--  00:00:02  3        source-address: 10.1.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip igmp group \<group-id\></h>

Shows information about a specific IGMP multicast group configured on the interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |
| `<group-id>` | The IGMP multicast mroute destination. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show interface swp3 ip igmp group 225.1.101.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router igmp</h>

Shows global IGMP configuration information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router igmp
        applied  pending
------  -------  -------
enable  on      off
```
