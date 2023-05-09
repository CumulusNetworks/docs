---
title: Bridge
author: Cumulus Networks
weight: 140
product: Cumulus Linux
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
## <h>nv show bridge</h>

Shows the configured bridge domains.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain</h>

Shows configuration settings for the all configured bridge domains.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\></h>

Shows configuration settings for the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> mac-table</h>

Shows the layer 2 Forwarding Database for the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default mac-table
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> mdb</h>

Shows the MDB entries in the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default mdb
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> multicast</h>

Shows the multicast configuration settings on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default multicast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> multicast snooping</h>

Shows the IGMP or MLD snooping configuration settings on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default multicast snooping
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> multicast snooping querier</h>

Shows the IGMP or MLD querier configuration settings on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default multicast snooping querier
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> router-port</h>

Shows the multicast router ports for the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default router-port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> stp</h>

Shows the STP settings for the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default stp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> stp state</h>

Shows the STP state (uo or down) of the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default stp state
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan</h>

Shows the VLANs on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\></h>

Shows configuration settings for the specified VLAN on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> multicast</h>

Shows the multicast configuration settings for the specified VLAN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>`      | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 multicast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> multicast snooping</h>

Shows the IGMP or MLD snooping configuration settings for the specified VLAN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>`      | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 multicast snooping
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier</h>

Shows the IGMP or MLD querier configuration settings for the specified VLAN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>`  | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 multicast snooping querier
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> ptp</h>

Shows the PTP configuration settings for the specified VLAN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>`      | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 ptp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni</h>

Shows VNIs on a specific VLAN on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 vni
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\></h>

Shows configuration settings for the specified VLAN VNI on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN name. |
| `<vni-id>` | The VXLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 vni 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding</h>

Shows configuration settings for BUM traffic flooding for the specified VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN name.  |
| `<vni-id>` | The VXLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 vni 10 flooding
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication</h>

Shows the head-end-replication settings for the specified VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN name. |
| `<vni-id>` | The VXLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 vni 10 flooding head-end-replication
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication \<hrep-id\></h>

Shows specific head-end-replication settings for the specified VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN name. |
| `<vni-id>` | The VXLAN name. |
| `<hrep-id>`  | The IPv4 unicast address or `evpn`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.0.1.34
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bridge</h>

Shows the bridge domain on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond3 bridge
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bridge domain \<domain-id\></h>

Shows configuration settings for the specified bridge domain on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`  | The interface name. |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond3 bridge domain br_default 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bridge domain \<domain-id\> stp</h>

Shows STP configuration settings for the specified bridge domain on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |
| `<domain-id>`  | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond3 bridge domain br_default stp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bridge domain \<domain-id\> vlan \<vid\></h>

Shows configuration settings for the specified VLAN on the specifies bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN name. You can also specify `all` to show settings for all VLANs. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond3 bridge domain br_default vlan 30
```
