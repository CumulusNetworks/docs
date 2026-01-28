---
title: FIB
author: Cumulus Networks
weight: 173

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router fib</h>

Shows both IPv4 and IPv6 FIB table entries for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf BLUE router fib
AFI   Prefix
----  ---------
ipv4  0.0.0.0/0
      10.1.10.0/24
      10.1.20.0/24
      10.1.30.0/24
      10.1.30.106/32
      127.0.0.0/8
ipv6  ::/0
      ::1/128
      fe80::/128
      fe80::/64
      ff00::/8
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router fib ipv4</h>

Shows IPv4 FIB table entries for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf BLUE router fib ipv4
Prefix          Next-hop     Protocol  Scope   Summary
--------------  -----------  --------  ------  ------------------
0.0.0.0/0       unreachable  boot      global  Metric: 4278198272
10.1.10.0/24    nhid 460     bgp       global  Metric: 20
10.1.20.0/24    nhid 460     bgp       global  Metric: 20
10.1.30.0/24    dev vlan30   kernel    link    PrefSrc: 10.1.30.3
10.1.30.106/32  nhid 459     bgp       global  Metric: 20
127.0.0.0/8     dev BLUE     kernel    link    PrefSrc: 127.0.0.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router fib ipv6</h>

Shows IPv6 FIB table entries for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf BLUE router fib ipv6
Prefix      Next-hop       Protocol  Scope   Summary
----------  -------------  --------  ------  ------------------
::/0        unreachable    boot      global  Metric: 4278198272
::1/128     dev BLUE       kernel    global  Metric: 256
fe80::/128  dev vlan30-v0  kernel    global  Metric: 0
fe80::/64   dev vlan30     kernel    global  Metric: 256
ff00::/8    dev vlan30     kernel    global  Metric: 256
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router fib ipv4 route \<route-id\></h>

Shows IPv4 FIB table entries for a specific prefix in a VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router fib ipv4 route 10.10.10.1/32 

Prefix             Next-hop               Proto  Scope  Summary 
------------------ ---------------------- ------ ------ ----------------------- 
10.10.10.1/32      nhid 68                bgp    global Metric: 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router fib ipv6 route \<route-id\></h>

Shows IPv6 FIB table entries for a specific prefix in a VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<route-id>` | The IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf RED router fib ipv6 route fe80::/64
Prefix     Next-hop    Protocol  Scope   Summary
---------  ----------  --------  ------  -----------
fe80::/64  dev vlan10  kernel    global  Metric: 256
```
