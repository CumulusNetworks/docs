---
title: WJH
author: Cumulus Networks
weight: 820

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh</h>

Provides commands to configure <span class="a-tooltip">[WJH](## "What Just Happened")</span> to provide real time visibility into network problems. You can diagnose network problems by looking at dropped packets.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\></h>

Configures a WJH channel where you want to monitor packet drops.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name.  |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> trigger</h>

Configures the type of packet drops you want to monitor. You can monitor layer 1 (`l1`), layer 2 (`l2`), layer 3 (`l3`), or tunnel (`tunnel1`) related packet drops.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding trigger l3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh state</h>

Enables and disables the WJH service. The default value is `enabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system wjh state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> aggregate-cache-size</h>

Configures the cache size for the WJH channel. You can specify a value between 500 and 5000.

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding aggregate-cache-size 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> polling-interval</h>

Configures aggregation interval for the WJH channel. You can specify a value between 5 and 300 seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding polling-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> buffer-threshold latency tc \<tc-id\> interface \<interface-id\> high</h>

Configures the channel buffer packet latency (the time spent in the switch) for all traffic classes or a specific traffic class for an interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |
| `<tc-id>` | The traffic class. |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding buffer-threshold latency tc all interface swp1-3 high 100

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> buffer-threshold congestion tc \<tc-id\> interface \<interface-id\> high</h>

Configures the channel buffer congestion (the percentage of the buffer occupancy on the switch) for all traffic classes or a specific traffic class for an interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |
| `<tc-id>` | The traffic class. |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding buffer-threshold congestion tc 3 interface all high 4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> drop-filter \<filter-id\> drop-type \<drop-filter-drop-type-id\> drop-reason \<drop-filter-drop-reason-id>\</h>

Configures traffic drop filters to prevent drops from being monitored based on the reason for the drop.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |
| `<filter-id>` | The filter name. |
| `<drop-filter-drop-type-id>` | The drop type. |
| `<drop-filter-drop-reason-id>` | The drop reason. See table below.|


### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding drop-filter TUNNEL1 drop-type tunnel drop-reason overlay-switch-src-mac-equals-dest-mac
```
  
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> drop-filter \<filter-id\> drop-type \<drop-filter-drop-type-id\> severity <drop-filter-severity-id></h>

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |
| `<filter-id>` | The filter name. |
| `<drop-filter-drop-type-id>` | The drop type. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ 
```
  
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> drop-filter \<filter-id\> ip</h>

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |
| `<filter-id>` | The filter name. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ 
```
