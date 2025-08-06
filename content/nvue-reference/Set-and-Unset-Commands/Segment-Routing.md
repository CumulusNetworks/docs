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
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF prefix fcbb::/16
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing srv6 locator \<locator-name\> block-length</h>

Configures the SRv6 locator block length for segment routing. You can specify a value between 16 and 64. The default value is 16.

The following table provides the supported formats for block length.

| Format | Block Length |
| -------| -------------|
| uN      | 32 |
| uA + uN | 16 |
| uN only | 16 |
| uA only | 16 |

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

The following table provides the supported formats for node length.

| Format  | Node Length |
| --------| -------------|
| uN      | 16 |
| uA + uN | 16 |
| uN only | 16 |
| uA only | 0  |

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<locator-name>` | The SRv6 locator name.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF node-length 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing srv6 locator \<locator-name\> func-length</h>

Configures the SRv6 locator function length for segment routing. You can specify a value between 0 and 64. The default value is 0.

The following table provides the supported formats for function length.

| Format  | Function Length |
| --------| -------------|
| uN      | 0 |
| uA + uN | 16 |
| uN only | 0 |
| uA only | 16 |

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<locator-name>` | The SRv6 locator name.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF func-length 16
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router segment-routing srv6 state</h>

Enables and disables segment routing. You can specify `enabled` or `disabled`.

Cumulus Linux supports source based routing with SRv6. The NICs connected to the switch fabric perform SRv6 origination and termination, and the switches act as SRv6-aware nodes. SRv6 allows NICs to directly control the path that traffic takes throughout the fabric by encoding an ordered list of SRv6 segment identifiers (uSIDs) in the packet header.

Cumulus Linux supports uN (End with NEXT-CSID) and uA (End.X with NEXT-CSID) endpoint behaviors, defined in RFC9800.

{{%notice note%}}
Cumulus Linux supports segment routing:
- On the Spectrum-4 switch only.
- In the default VRF only.
{{%/notice%}}

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

Configures the static segment identifier endpoint. You can specify uA or uN. For uA segment identifiers, next hop (peer link-local) learning occurs with router advertisements. Spectrum switches enable router advertisements on the interface automatically when you configure a uA segment identifier; however, if the adjacent device is a non-Spectrum switch, you need to enable router advertisements on the adjacent device on the connected interface to ensure proper next hop discovery.

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

Configures the interface for the static segment identifier uA endpoint behavior.

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
