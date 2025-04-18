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
    Flags - * - selected, q - queued, o - offloaded, i - installed, S - fib-        
    selected, x - failed                                                            
                                                                                
    Route            Protocol   Distance  ResolvedVia  ResolvedViaIntf  Uptime                NHGId  Metric  TableId  Flags
    ---------------  ---------  --------  -----------  ---------------  --------------------  -----  ------  -------  -----
    10.0.1.12/32     connected  0                                       2024-11-14T08:58:30Z  35     0                *Sio 
    10.0.1.34/32     bgp        20                                      2024-11-14T09:00:07Z  127    0                *Si  
    10.0.1.255/32    bgp        20                                      2024-11-14T09:00:12Z  127    0                *Si  
    10.10.10.1/32    connected  0                                       2024-11-14T08:58:22Z  35     0                *Sio 
    10.10.10.2/32    bgp        20                                      2024-11-14T08:59:58Z  62     0                *Si  
    10.10.10.3/32    bgp        20                                      2024-11-14T09:00:08Z  127    0                *Si  
    10.10.10.4/32    bgp        20                                      2024-11-14T09:00:07Z  127    0                *Si  
    10.10.10.63/32   bgp        20                                      2024-11-14T09:00:12Z  127    0                *Si  
    10.10.10.64/32   bgp        20                                      2024-11-14T09:00:08Z  127    0                *Si  
    10.10.10.101/32  bgp        20                                      2024-11-14T08:59:58Z  102    0                *Si  
    10.10.10.102/32  bgp        20                                      2024-11-14T08:59:58Z  115    0                *Si  
    10.10.10.103/32  bgp        20                                      2024-11-14T08:59:58Z  121    0                *Si  
    10.10.10.104/32  bgp        20                                      2024-11-14T08:59:58Z  113    0                *Si
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route</h>

Shows the routing table for IPv4 routes.

{{%notice note%}}
Cumulus Linux 5.10.0 and later includes redesigned flags in the command ouput.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route

Flags - * - selected, q - queued, o - offloaded, i - installed, S - fib-        
selected, x - failed                                                            
                                                                                
Route            Protocol   Distance  Uptime                NHGId  Metric  Flags
---------------  ---------  --------  --------------------  -----  ------  -----
10.1.10.0/24     connected  0         2024-07-18T21:57:29Z  46     0       *Sio 
10.1.20.0/24     connected  0         2024-07-18T21:57:29Z  47     0       *Sio 
10.1.30.0/24     connected  0         2024-07-18T21:57:29Z  48     0       *Sio 
10.1.40.0/24     bgp        20        2024-07-18T22:02:22Z  57     0       *Si  
10.1.50.0/24     bgp        20        2024-07-18T22:02:22Z  57     0       *Si  
10.1.60.0/24     bgp        20        2024-07-18T22:02:22Z  57     0       *Si  
10.10.10.1/32    connected  0         2024-07-18T21:55:54Z  7      0       *Sio 
10.10.10.2/32    bgp        20        2024-07-18T21:57:29Z  34     0       *Si  
10.10.10.3/32    bgp        20        2024-07-18T22:02:22Z  57     0       *Si  
10.10.10.4/32    bgp        20        2024-07-18T22:02:27Z  57     0       *Si  
10.10.10.101/32  bgp        20        2024-07-18T22:01:14Z  50     0       *Si  
10.10.10.102/32  bgp        20        2024-07-18T22:02:22Z  58     0       *Si
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf\> router rib \<afi\> route-count</h>

Shows the total number of routes in the routing table.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route-count
                 operational 
------------     ----------- 
total-routes    34 
[protocol]      bgp 
[protocol]      connected 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf\> router rib \<afi\> route-count protocol</h>

Shows the total number of routes per protocol in the routing table.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route-count protocol
Protocol   Total 
---------  ----- 
bgp        6 
connected  3 
ospf       8 
static     3
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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.10.10.63/32
route-entry
==============                                                                               
    Protocol - Protocol name, TblId - Table Id, NHGId - Nexthop group Id, Flags - u 
    - unreachable, r - recursive, o - onlink, i - installed, d - duplicate, c -     
    connected, A - active                                                           
                                                                                
    EntryIdx  Protocol  TblId  NHGId  Distance  Metric  ResolvedVia                ResolvedViaIntf  Weight  Flags
    --------  --------  -----  -----  --------  ------  -------------------------  ---------------  ------  -----
    1         bgp       254    127    20        0       fe80::4ab0:2dff:fe4d:1aed  swp51            1       iA   
                                                        fe80::4ab0:2dff:fe5e:6ad   swp52            1       iA   
                                                        fe80::4ab0:2dff:febf:7c74  swp54            1       iA   
                                                        fe80::4ab0:2dff:fec2:1f26  swp53            1       iA  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\></h>

Shows the routing table for the specified protocol route.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.1.40.0/24 protocol bgp
entry-index
==============
    Entry
    -----
    1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index</h>

Shows the route entry index values for the specified protocol route.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.1.40.0/24 protocol bgp entry-index
Entry
-----
1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\></h>

Shows detailed information about the specified protocol route entry index.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.1.40.0/24 protocol bgp entry-index 1
                  operational              
----------------  -------------------------
distance          20                       
metric            0                        
uptime            2024-07-18T22:02:22Z     
nexthop-group-id  57                       
table-id          254                      
flags-string      *Si                      
[via]             fe80::4ab0:2dff:fe50:8cbb
[via]             fe80::4ab0:2dff:feba:6208
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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.1.40.0/24 protocol bgp entry-index 1 flags
operational 
------------
selected    
fib-selected
installed 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via</h>

Shows the routing table next hop information for the specified protocol route entry index.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.1.40.0/24 protocol bgp entry-index 1 via
Nexthop                    flags-string  type        vrf  weight  Summary         
-------------------------  ------------  ----------  ---  ------  ----------------
fe80::4ab0:2dff:fe50:8cbb  iA            ip-address       1       Interface: swp51
fe80::4ab0:2dff:feba:6208  iA            ip-address       1       Interface: swp52
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\></h>

Shows the routing table next hop resolution information for the specified protocol route entry index.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.1.40.0/24 protocol bgp entry-index 1 via fe80::4ab0:2dff:fe50:8cbb
              operational
------------  -----------
type          ip-address 
weight        1          
flags-string  iA 
resolved-via
===============
No Data
interface
============
    Interface
    ---------
    swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> flags</h>

Shows the routing table flags for the specified protocol route entry index next hop.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.1.40.0/24 protocol bgp entry-index 1 via fe80::4ab0:2dff:fe50:8cbb flags
operational
-----------
installed  
active
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> label</h>

Shows the routing table label information for the specified protocol route entry index next hop.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.1.40.0/24 protocol bgp entry-index 1 via fe80::4ab0:2dff:fe50:8cbb label

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> resolved-via</h>

Shows the routing table recursive next hop resolution information for the specified protocol route entry index next hop.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.1.40.0/24 protocol bgp entry-index 1 via 10.0.1.0 resolved-via
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index via \<via-id\> resolved-via \<resolved-via-id\></h>

Shows the routing table information for a specific recursive next hop for the specified protocol route entry index next hop.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

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
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.1.40.0/24 protocol bgp entry-index 1 via 10.0.1.0 resolved-via 10.0.10.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf\> router rib \<afi\> fib-filter protocol \<protocol-id\></h>

Shows the route map configuration for the routes of the import protocol specified.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<protocol-id>`  | The protocol name, such as `bgp` or `ospf`.|

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router rib ipv4 fib-filter protocol bgp
           applied
---------  ------- 
route-map  routemap
```
