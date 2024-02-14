---
title: RIB
author: Cumulus Networks
weight: 330

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib</h>

Shows the routing table for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib
AFI   Prefix         
----  ---------------
ipv4  10.0.1.12/32   
      10.0.1.34/32   
      10.0.1.255/32  
      10.10.10.1/32  
      10.10.10.2/32  
      10.10.10.3/32  
      10.10.10.4/32  
      10.10.10.63/32 
      10.10.10.64/32 
      10.10.10.101/32
      10.10.10.102/32
      10.10.10.103/32
      10.10.10.104/32
ipv6  fe80::/64
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\></h>

Shows the IPv4 or IPv6 routing table for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4
route
========
    Route            Protocol   Distance  ResolvedVia  ResolvedViaIntf  Uptime    NHGId  Metric  TableId  Flags       
    ---------------  ---------  --------  -----------  ---------------  --------  -----  ------  -------  ------------
    10.0.1.12/32     connected  0                                       07:01:03  7      0                fib-selected
                                                                                                          installed   
                                                                                                          offloaded   
                                                                                                          selected    
    10.0.1.34/32     bgp        20                                      00:01:54  144    0                fib-selected
                                                                                                          installed   
                                                                                                          selected    
    10.0.1.255/32    bgp        20                                      00:01:54  144    0                fib-selected
                                                                                                          installed   
                                                                                                          selected    
    10.10.10.1/32    connected  0                                       07:03:56  7      0                fib-selected
                                                                                                          installed   
                                                                                                          offloaded   
                                                                                                          selected    
    10.10.10.2/32    bgp        20                                      00:01:53  221    0                fib-selected
                                                                                                          installed   
                                                                                                          selected    
    10.10.10.3/32    bgp        20                                      00:01:54  144    0                fib-selected
                                                                                                          installed   
                                                                                                          selected    
    10.10.10.4/32    bgp        20                                      00:01:54  144    0                fib-selected
                                                                                                          installed   
                                                                                                          selected    
    10.10.10.63/32   bgp        20                                      00:01:54  144    0                fib-selected
                                                                                                          installed   
                                                                                                          selected    
    10.10.10.64/32   bgp        20                                      00:01:54  144    0                fib-selected
                                                                                                          installed   
                                                                                                          selected    
    10.10.10.101/32  bgp        20                                      00:01:54  115    0                fib-selected
                                                                                                          installed
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> protocol</h>

Shows the IPv4 or IPv6 routing table for all protocols for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 protocol
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> protocol \<protocol\></h>

Shows the IPv4 or IPv6 routing table for the specified protocol for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<protocol>` |  The protocol name: `bgp`, `isis`, `ospf`, `rip`, `sharp`, `table`, `connected`, `kernel`, `ospf6`, `ripng`, or `static`. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 protocol bgp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\></h>

Shows the routing table for the specified route.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\></h>

Shows the routing table for the specified protocol route.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default protocol bgp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index</h>

Shows the route entry index values for the specified protocol route.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\></h>

Shows detailed information about the specified protocol route entry index.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|
| `<entry-index>` | The routing table entry index.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> flags</h>

Shows the routing table flags for the specified protocol route entry index.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|
| `<entry-index>` | The routing table entry index.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 flags
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via</h>

Shows the routing table next hop information for the specified protocol route entry index.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|
| `<entry-index>` | The routing table entry index.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\></h>

Shows the routing table next hop resolution information for the specified protocol route entry index.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|
| `<entry-index>` | The routing table entry index.|
| `<via-id>` | The IP address of the nexthop router.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via 10.0.1.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> flags</h>

Shows the routing table flags for the specified protocol route entry index next hop.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|
| `<entry-index>` | The routing table entry index.|
| `<via-id>` | The IP address of the nexthop router.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via 10.0.1.0 flags
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> label

Shows the routing table label information for the specified protocol route entry index next hop.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|
| `<entry-index>` | The routing table entry index.|
| `<via-id>` | The IP address of the nexthop router.  |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via 10.0.1.0 label
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> resolved-via

Shows the routing table recursive next hop resolution information for the specified protocol route entry index next hop.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|
| `<entry-index>` | The routing table entry index.|
| `<via-id>` | The IP address of the nexthop router.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via 10.0.1.0 resolved-via
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index via \<via-id\> resolved-via \<resolved-via-id\>

Shows the routing table information for a specific recursive next hop for the specified protocol route entry index next hop.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|
| `<entry-index>` | The routing table entry index.|
| `<via-id>` | The IP address of the nexthop router.  |
| `<resolved-via-id>` | The IP address of the nexthop router that resolves the route. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via 10.0.1.0 resolved-via 10.0.10.0
```
