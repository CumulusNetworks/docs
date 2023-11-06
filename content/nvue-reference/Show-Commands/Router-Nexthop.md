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

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router nexthop group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop group \<nexthop-group-id\></h>

Shows information about the specified next hop group in the RIB.

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
cumulus@switch:~$ nv show router nexthop rib 108
                operational  applied
--------------  -----------  -------
address-family  unspecified         
installed       on                  
ref-count       6                   
type            zebra               
valid           on                  
vrf             default             

resolved-via
===============
    Nexthop                    type        vrf      weight  Summary         
    -------------------------  ----------  -------  ------  ----------------
    fe80::4ab0:2dff:fe60:910e  ip-address  default  1       Interface: swp54
    fe80::4ab0:2dff:fea7:7852  ip-address  default  1       Interface: swp53
    fe80::4ab0:2dff:fec8:8fb9  ip-address  default  1       Interface: swp52
    fe80::4ab0:2dff:feff:e147  ip-address  default  1       Interface: swp51

resolved-via-backup
======================

depends
==========
    Nexthop-group
    -------------
    65           
    90           
    96           
    109          

dependents
=============
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> depends</h>

Shows information about the next hops on which a specific next hop relies.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show router nexthop rib 39 depends
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> dependents</h>

Shows information about the next hop dependents on which a specific next hop relies.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show router nexthop rib 10 dependents
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> resolved-via</h>

Shows details about the next hop address for a particular next hop.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$  nv show router nexthop rib 39 resolved-via
Nexthop  type       vrf      weight  Summary
-------  ---------  -------  ------  -------
vxlan99  interface  default 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> resolved-via \<resolved-via-id\></h>

Shows details of a particular next hop specified by the next hop IP address.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |
| `<resolved-via-id>` | The next hop IP address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show router nexthop rib 39 resolved-via vxlan99
      operational  applied  pending
----  -----------  -------  -------
type  interface                    
vrf   default                      

interface
============
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> resolved-via-backup</h>

Shows information about the backup next hops for the specified next hop.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show router nexthop rib 39 resolved-via-backup
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router nexthop rib \<nhg-id\> resolved-via-backup \<resolved-via-id\></h>

Shows information about a specific backup next hop.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |
| `<resolved-via-id>` | The IP address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show router nexthop rib 20 resolved-via-backup 
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
      resolved-via-default  Summary                              
----  --------------------  -------------------------------------
ipv4                        ip-address:                10.10.10.2
                            ip-address:                10.10.10.3
                            ip-address:                10.10.10.4
                            ip-address:              192.168.0.22
ipv6                        ip-address: fe80::4ab0:2dff:fe08:9898
                            ip-address: fe80::4ab0:2dff:fed8:67cb
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

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family (IPv4 or IPv6). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\></h>

Shows the IPv4 or IPv6 next hop tracking information for a specific route map in the specified VRF.

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
cumulus@switch:~$ nv show vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\> protocol</h>

Shows the IPv4 or IPv6 next hop tracking information for all protocols in the route map in the specified VRF.

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
cumulus@switch:~$ nv show vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\> protocol \<nht-protocol-id\></h>

Shows the IPv4 or IPv6 next hop tracking information for a specific route map protocol for the specified VRF.

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
cumulus@switch:~$ nv show vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1 bgp
```
