---
title: IGMP
author: Cumulus Networks
weight: 570

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip igmp state</h>

Enables and disables <span class="a-tooltip">[IGMP](## "Internet Group Management Protocol")</span> on the specified interface. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip igmp state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip igmp fast-leave</h>

Enables and disables fast leave processing on the interface. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip igmp fast-leave enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip igmp last-member-query-count</h>

Sets the number of group-specific queries that a querier sends after receiving a leave message on the interface. You can set a value between 1 and 255. The default setting is 2.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip igmp last-member-query-count 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip igmp last-member-query-interval</h>

Configures the maximum response time advertised in IGMP group-specific queries. You can specify a value between 1 and 6553 seconds. The default setting is 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip igmp last-member-query-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip igmp query-interval</h>

Configures how often IGMP sends query-host messages to discover which multicast groups have members on the attached networks.

- In Cumulus Linux 5.6 and later, you can specify a value between 1 and 65535 seconds. The default setting is 100.
- In Cumulus Linux 5.5 and earlier, you can specify a value between 1 and 1800 seconds. The default setting is 180.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip igmp query-interval 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip igmp query-max-response-time</h>

Configures the maximum response time for IGMP general queries. You can specify a value between 10 and 6553 seconds. The default setting is 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip igmp query-max-response-time 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip igmp static-group \<static-group-id\></h>

Configures the IGMP static multicast mroute destination. This is the IPv4 address of the member associated with the specified multicast group address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<static-group-id>` | The IGMP static multicast mroute destination. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip igmp static-group 234.10.10.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip igmp static-group \<static-group-id\> source-address \<ipv4-unicast\></h>

Configures the IPv4 unicast address of the IGMP static multicast mroute source.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<static-group-id>` | The IGMP static multicast mroute destination. |
| `<ipv4-unicast>` | The IPv4 unicast address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip igmp static-group 234.10.10.10 source-address 234.1.1.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip igmp version</h>

Configures the IGMP version on the specified interface. You can specify version 2 or version 3. The default setting is `3`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip igmp version 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router igmp state</h>

Enables and disables IGMP globally. The default setting is `disabled`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router igmp state enabled
```
