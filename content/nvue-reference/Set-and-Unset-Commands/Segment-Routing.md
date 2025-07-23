---
title: Segment Routing
author: Cumulus Networks
weight: 622

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing srv6 locator \<locator-name\></h>

Configures the SRv6 locator name for segment routing.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<locator-name>` | The SRv6 locator name.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing srv6 locator \<locator-name\> prefix \<ipv6-prefix\></h>

Configures the SRv6 locator prefix for segment routing. The prefix length must match the sum of block length and the node length.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<locator-name>` | The SRv6 locator name.|
| `<ipv6-prefix>` | The IPv6 prefix.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF prefix 2001:db8:1:1::/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing srv6 locator \<locator-name\> block-length</h>

Configures the SRv6 locator block length for segment routing. You can specify a value between 16 and 64. The default value is 16.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<locator-name>` | The SRv6 locator name.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF block-length 16
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing srv6 locator \<locator-name\> node-length</h>

Configures the SRv6 locator node length for segment routing. You can specify a value between 0 and 64. The default value is 16.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<locator-name>` | The SRv6 locator name.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF node-length 16
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing srv6 locator \<locator-name\> func-length</h>

Configures the SRv6 locator function length for segment routing. You can specify a value between 0 and 64. The default value is 0.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<locator-name>` | The SRv6 locator name.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF func-length 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing srv6 state</h>

Enables and disables segment routing. You can specify `enabled` or `disabled`.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing srv6 state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing static srv6-sid \<sid\></h>

Configures the static segment identifier.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<sid>` | The static segment identifier.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing static srv6-sid 2001:db8:1:1::100/48
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing static srv6-sid <sid> locator-name</h>

Configures the static segment identifier locator name. The static segment identifier must be part of the locator prefix.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<sid>` | The static segment identifier.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing static srv6-sid 2001:db8:1:1::100/48 locator-name LEAF
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing static srv6-sid \<sid\> behavior</h>

Configures the static segment identifier endpoint behavior. You can specify uA or uN. If you specify uA, you must also provide the interface. Cumulus Linux enables route advertisements on the interface on which you configure uA.

The following table provides the supported formats for block, node, and function length.

| Format | Block Length | Node Length | Function Length |
| -------| -------------| ------------| ----------------|
| uN      | 32 | 16 | 0  |
| uA + uN | 16 | 16 | 16 |
| uN only | 16 | 16 | 0  |
| uA only | 16 | 0  | 16 |

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<sid>` | The static segment identifier.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing static srv6-sid 2001:db8:1:1::100/48 behavior uA
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing static srv6-sid \<sid\> interface \<interface-name\></h>

Configures the interface for the static segment identifier endpoint behavior.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<sid>` | The static segment identifier.|
| `<interface-name>` | The name of the interface.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing static srv6-sid 2001:db8:1:1::100/48 interface swp1
```
