---
title: Router Nexthop
author: Cumulus Networks
weight: 340

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop</h>

Shows information about the next hops in the RIB, such as the IP address, VRF, interface, type, and so on.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router nexthop -o json
{
  "rib": {
    "29": {
      "address-family": "ipv4",
      "installed": "on",
      "interface-index": 1,
      "ref-count": 2,
      "resolved-via": {
        "lo": {
          "flags": {
            "active": {},
            "directly-connected": {},
            "installed": {}
          },
          "type": "interface",
          "vrf": "default"
        }
      },
      "type": "zebra",
      "valid": "on",
      "vrf": "default"
    },
    "30": {
      "address-family": "ipv4",
      "installed": "on",
      "interface-index": 2,
      "ref-count": 2,
      "resolved-via": {
        "eth0": {
          "flags": {
            "active": {},
            "directly-connected": {},
            "installed": {}
          },
          "type": "interface",
          "vrf": "mgmt"
        }
      },
      "type": "zebra",
      "valid": "on",
      "vrf": "default"
    },
    "31": {
      "address-family": "ipv4",
      "interface-index": 65,
      "ref-count": 2,
      "resolved-via": {
        "vlan30v0": {
          "flags": {
            "active": {},
            "directly-connected": {},
            "installed": {}
          },
          "type": "interface",
          "vrf": "BLUE"
        }
... 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop group</h>

Shows the next hop groups in the RIB. Next hop groups are a way to encapsulate ECMP information together.

{{%notice note%}}
You must use `--applied` with this command to show the output.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router nexthop group  --applied
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop group \<nexthop-group-id\></h>

Shows information about the specified next hop group in the RIB.

{{%notice note%}}
Cumulus Linux 5.4 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router nexthop 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop group \<nexthop-group-id\> via</h>

Shows information about the next hop addresses for the specified next hop group.

{{%notice note%}}
Cumulus Linux 5.4 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router nexthop 1 via
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop group \<nexthop-group-id\> via \<via-id\></h>

Shows details of a particular next hop group specified by the next hop address.

{{%notice note%}}
Cumulus Linux 5.4 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |
| `<via-id>` | The IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router nexthop 10 via fe80::a00:27ff:fea6:b9fe
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib</h>

Shows information about the next hops in the RIB, such as the IP address, VRF, interface, type, and so on.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

Cumulus Linux 5.8:

```
cumulus@switch:~$ nv show router nexthop rib                  
Installed - Install state                       
ID   Installed  UpTime    Vrf      Valid  Via                        ViaIntf        ViaVrf   Depends
---  ---------  --------  -------  -----  -------------------------  -------------  -------  -------
7    on         00:10:43  default  on     lo                                        default         
8    on         00:13:36  default  on     eth0                                      mgmt            
9    on         00:13:36  default  on     eth0                                      mgmt            
10              00:10:43  default  on                                                               
11   on         00:10:43  default  on     192.168.200.1              eth0           mgmt            
12   on         00:10:43  default  on                                                               
15   on         00:10:43  default  on                                                               
30   on         00:10:43  default  on                                                               
32   on         00:13:33  default  on     swp53                                     default         
34              00:13:33  default  on     swp51                                     default         
36              00:13:33  default  on     swp52                                     default         
38              00:13:33  default  on     swp54                                     default         
68              00:10:50  default  on     peerlink.4094                             default         
76   on         00:10:48  default  on     fe80::4ab0:2dff:fe59:eedc  peerlink.4094  default         
88              00:10:46  default  on     br_default                                default         
89              00:10:46  default  on     vlan10v0                                  RED             
90   on         00:10:46  default  on     vlan10                                    RED             
91              00:10:46  default  on     vlan10v0                                  RED             
92              00:10:46  default  on     vlan4024_l3                               RED             
93              00:10:46  default  on     vlan20                                    RED             
94   on         00:10:46  default  on     vlan10                                    RED             
95   on         00:10:46  default  on     vlan20                                    RED             
96   on         00:10:46  default  on     vlan30                                    BLUE            
97              00:10:46  default  on     vlan4036_l3                               BLUE            
98   on         00:10:46  default  on     vlan30                                    BLUE            
105             00:10:46  default  on     vlan4024_l3v0                             RED             
106             00:10:46  default  on     vlan20v0                                  RED             
107             00:10:46  default  on     vlan20v0                                  RED             
108             00:10:46  default  on     vlan30v0                                  BLUE            
109             00:10:46  default  on     vlan4036_l3v0                             BLUE            
110             00:10:46  default  on     vlan30v0                                  BLUE            
113             00:10:41  default  on     vxlan48                                   default         
115  on         00:01:57  default  on     fe80::4ab0:2dff:fe3f:44c1  swp51          default         
119  on         00:00:48  default  on     fe80::4ab0:2dff:fe25:2e13  swp52          default         
132  on         00:00:48  default  on     fe80::4ab0:2dff:fe4e:2c21  swp53          default         
138  on         00:00:48  default  on     fe80::4ab0:2dff:fead:9d3f  swp54          default       
```

Cumulus Linux 5.4.0 thru 5.7:

```
cumulus@switch:~$ nv show router nexthop rib
Nexthop-group  address-family  installed  interface-index  ref-count  type   valid  vrf      Summary           
-------------  --------------  ---------  ---------------  ---------  -----  -----  -------  ------------------
...
75             ipv4            on         74               2          zebra  on     default                    
76             ipv4            on         74               2          zebra  on     default                    
77             unspecified     on                          2          zebra  on     default  Nexthop-group:  78
                                                                                             Nexthop-group:  79
                                                                                             Nexthop-group:  78
                                                                                             Nexthop-group:  79
78             ipv4            on         67               3          zebra  on     default                    
79             ipv4            on         67               3          zebra  on     default                    
90             ipv6            on         55               8          zebra  on     default                    
96             ipv6            on         54               8          zebra  on     default                    
108            unspecified     on                          6          zebra  on     default  Nexthop-group: 109
                                                                                             Nexthop-group:  65
                                                                                             Nexthop-group:  90
                                                                                             Nexthop-group:  96
                                                                                             Nexthop-group: 109
                                                                                             Nexthop-group:  65
                                                                                             Nexthop-group:  90
                                                                                             Nexthop-group:  96
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\></h>

Shows information about the specified next hop in the RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show router nexthop rib 140
                 operational         
---------------  --------------------
type             zebra               
ref-count        3                   
vrf              default             
valid            on                  
installed        on                  
interface-index  67                  
uptime           2024-11-14T09:00:18Z

Via
======
                                                                                
    Flags - u - unreachable, r - recursive, o - onlink, i - installed, d -          
    duplicate, c - connected, A - active, Type - Type of nexthop, Weight - Weight to
    be used by the nexthop for purposes of ECMP, VRF - VRF to use for egress.       
                                                                                
    Nexthop      Flags  Type        Weight  VRF   Interface  
    -----------  -----  ----------  ------  ----  -----------
    10.10.10.63  oiA    ip-address  1       BLUE  vlan4006_l3

Via BackupNexthops
=====================
No Data

Depends
==========
No Data

Dependents
=============
    Nexthop-group
    -------------
    257
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> depends</h>

Shows information about the next hops on which a specific next hop relies.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show router nexthop rib 55 depends 
Nexthop-group 
------------- 
56
57
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> dependents</h>

Shows information about the next hop dependents on which a specific next hop relies.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show router nexthop rib 56 dependents  
Nexthop-group 
------------- 
55   
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> resolved-via</h>

Shows details about the next hop address for a particular next hop.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$  nv show router nexthop rib 140 resolved-via
Flags - u - unreachable, r - recursive, o - onlink, i - installed, d -          
duplicate, c - connected, A - active, Type - Type of nexthop, Weight - Weight to
be used by the nexthop for purposes of ECMP, VRF - VRF to use for egress.       
                                                                                
Nexthop      Flags  Type        Weight  VRF   Interface  
-----------  -----  ----------  ------  ----  -----------
10.10.10.63  oiA    ip-address  1       BLUE  vlan4006_l3 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> resolved-via \<resolved-via-id\></h>

Shows details of a particular next hop specified by the next hop IP address.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |
| `<resolved-via-id>` | The next hop IP address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show router nexthop rib 56 resolved-via 10.10.10.63
              operational 
------------  ----------- 
type          ip-address  
weight        1           
vrf           default     
flags-string  iA          

interface 
============ 
    Interface 
    --------- 
    swp5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> resolved-via-backup</h>

Shows information about the backup next hops for the specified next hop.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show router nexthop rib 39 resolved-via-backup
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router nexthop-tracking</h>

Shows the IPv4 and IPv6 next hop tracking information for the specified VRF. Next hop tracking is an optimization feature that reduces the processing time involved in the BGP bestpath algorithm by monitoring changes to the routing table.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show vrf default router nexthop-tracking

IpAddress - Nexthop ip address, Interface - Resolved via interface,             
DirectlyConnected - Indicates if nexthop is directly connected or not,          
ProtocolFiltered - Indicates whether protocol filtered or not, Flags - o -      
onlink, c - directly-connected, A - active                                      
                                                                                
AFI   IpAddress    Interface      VRF      Weight  ResolvedProtocol  DirectlyConnected  ProtocolFiltered  Flags
----  -----------  -------------  -------  ------  ----------------  -----------------  ----------------  -----
ipv4  10.0.1.34    swp51          default  1       bgp               off                off               A    
                   swp52          default  1                                                              A    
                   swp54          default  1                                                              A    
                   swp53          default  1                                                              A    
      10.10.10.2   peerlink.4094  default  1       bgp               off                off               A    
      10.10.10.3   swp51          default  1       bgp               off                off               A    
                   swp52          default  1                                                              A    
                   swp54          default  1                                                              A    
                   swp53          default  1                                                              A    
      10.10.10.4   swp51          default  1       bgp               off                off               A    
                   swp52          default  1                                                              A    
                   swp54          default  1                                                              A    
                   swp53          default  1                                                              A    
      10.10.10.63  swp51          default  1       bgp               off                off               A    
                   swp52          default  1                                                              A    
                   swp54          default  1                                                              A    
                   swp53          default  1                                                              A    
      10.10.10.64  swp51          default  1       bgp               off                off               A    
                   swp52          default  1                                                              A    
                   swp54          default  1                                                              A    
                   swp53          default  1                                                              A
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router nexthop-tracking \<afi\></h>

Shows the IPv4 or IPv6 next hop tracking information for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family (IPv4 or IPv6). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show vrf default router nexthop-tracking ipv4
              operational   applied  pending
------------  ------------  -------  -------
[ip-address]  10.10.10.2                    
[ip-address]  10.10.10.3                    
[ip-address]  10.10.10.4                    
[ip-address]  192.168.0.22
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map</h>

Shows the IPv4 or IPv6 next hop tracking information for all route maps in the specified VRF.

{{%notice note%}}
You must use `--applied` with this command to show the applied output.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family (IPv4 or IPv6). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:mgmt:~$ nv show vrf default router nexthop-tracking ipv4 route-map
 
Protocol - nexthop tracking protocol.
 
RoutemapID    Protocol
------------  --------
v4-nht-rmap   bgp
              ospf
v4-nht-rmap1  static
```

```
cumulus@switch:mgmt:~$ nv show vrf default router nexthop-tracking ipv4 route-map --applied
 
Protocol - nexthop tracking protocol.
 
RoutemapID    Protocol
------------  --------
v4-nht-rmap   bgp
              ospf
v4-nht-rmap1  static
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\></h>

Shows the IPv4 or IPv6 next hop tracking information for a specific route map in the specified VRF.

{{%notice note%}}
You must use `--applied` with this command to show the applied output.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family (IPv4 or IPv6). |
| `<nht-routemap-id>` | The next hop tracking route map name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:mgmt:~$ nv show vrf default router nexthop-tracking ipv4 route-map v4-nht-rmap
            operational  applied
----------  -----------  -------
[protocol]  bgp          bgp
[protocol]  ospf         ospf
```

```
cumulus@switch:~$ nv show vrf default router nexthop-tracking ipv4 route-map v4-nht-rmap --applied
            Rev ID: applied
----------  ---------------
[protocol]  bgp            
[protocol]  ospf  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\> protocol</h>

Shows the IPv4 or IPv6 next hop tracking information for all protocols in the route map in the specified VRF.

{{%notice note%}}
You must use `--applied` with this command to show the applied output.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family (IPv4 or IPv6). |
| `<nht-routemap-id>` | The next hop tracking route map name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show vrf default router nexthop-tracking ipv4 route-map v4-nht-rmap protocol
RoutemapProtocol
----------------
bgp             
ospf
```

```
cumulus@switch:~$ nv show vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1 protocol --applied
RoutemapProtocol
----------------
bgp             
ospf   
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\> protocol \<nht-protocol-id\></h>

Shows the IPv4 or IPv6 next hop tracking information for a specific route map protocol for the specified VRF.

{{%notice note%}}
You must use `--applied` with this command to show the applied output.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family (IPv4 or IPv6). |
| `<nht-routemap-id>` | The next hop tracking route map name. |
| `<nht-protocol-id>` | The protocol: `bgp`, `ospf`, `ospf6`, or `static`. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:mgmt:~$ nv show vrf default router nexthop-tracking ipv4 route-map v4-nht-rmap protocol bgp
No Data
```

```
cumulus@switch:~$ nv show vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1 protocol bgp --applied
No Data
```
