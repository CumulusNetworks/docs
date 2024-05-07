---
title: BGP
author: Cumulus Networks
weight: 130
type: nojsscroll

---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router bgp</h>

Shows global BGP configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router bgp
                                applied    
------------------------------  -----------
enable                          on         
autonomous-system               65101      
graceful-shutdown               off        
policy-update-timer             5          
router-id                       10.10.10.1 
wait-for-install                off        
convergence-wait                           
  establish-wait-time           0          
  time                          0          
graceful-restart                           
  mode                          helper-only
  path-selection-deferral-time  360        
  restart-time                  120        
  stale-routes-time             360
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router bgp convergence-wait</h>

Shows global readonly mode configuration. Readonly mode reduces CPU and network usage when restarting the BGP process.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router bgp convergence-wait
                     applied
-------------------  -------
establish-wait-time  0      
time                 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router bgp graceful-restart</h>

Shows global BGP graceful restart configuration. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router bgp graceful-restart
                              applied    
----------------------------  -----------
mode                          helper-only
path-selection-deferral-time  360        
restart-time                  120        
stale-routes-time             360
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router bgp queue-limit</h>

Shows the input and output message queue configuration settings.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show router bgp queue-limit
        applied
------  -------
input   2048  
output  2048 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp</h>

Shows a summary of the BGP configuration information for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp
                              operational  applied  
----------------------------  -----------  ---------
enable                                     on       
autonomous-system                          auto     
rd                                         none     
router-id                     10.10.10.1   auto     
address-family                                      
  ipv4-unicast                                      
    rib-filter                             none     
    admin-distance                                  
      external                             20       
      internal                             200      
    multipaths                                      
      compare-cluster-length               off      
      ebgp                                 64       
      ibgp                                 64       
    route-export                                    
      to-evpn                                       
        enable                             off      
    route-import                                    
      from-vrf                                      
        enable                             off      
    enable                                 on       
    [aggregate-route]                               
    [network]                                       
    redistribute                                    
      connected                                     
        enable                             on       
        metric                             auto     
        route-map                          none
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family</h>

Shows a summary of the BGP configuration information for the specified VRF for all address families: IPv4 unicast, IPv6 unicast, and EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family
                           operational  applied
--------------------------  -----------  -------
ipv4-unicast                                    
  rib-filter                             none   
  admin-distance                                
    external                             20     
    internal                             200    
  multipaths                                    
    compare-cluster-length               off    
    ebgp                                 64     
    ibgp                                 64     
  route-export                                  
    to-evpn                                     
      enable                             off    
  route-import                                  
    from-vrf                                    
      enable                             off    
  enable                                 on
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast</h>

Shows a summary of the BGP IPv4 configuration information for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast
                          operational  applied
------------------------  -----------  -------
rib-filter                             none   
admin-distance                                
  external                             20     
  internal                             200    
multipaths                                    
  compare-cluster-length               off    
  ebgp                                 64     
  ibgp                                 64     
route-export                                  
  to-evpn                                     
    enable                             off    
route-import                                  
  from-vrf                                    
    enable                             off    
enable                                 on
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute</h>

Shows configuration information for BGP IPv4 route redistribution for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute
             operational  applied
-----------  -----------  -------
connected                        
  enable                  on     
  metric                  auto   
  route-map               none   
kernel                           
  enable                  off    
static                           
  enable                  off    
ospf                             
  enable                  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static</h>

Shows configuration information for IPv4 BGP static route redistribution for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute static
        operational  applied
------  -----------  -------
enable               off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected</h>

Shows configuration information for BGP IPv4 connected route redistribution for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute connected
           operational  applied
---------  -----------  -------
enable                  on     
metric                  auto   
route-map               none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel</h>

Shows configuration information for BGP IPv4 kernel route redistribution for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute kernel
        operational  applied
------  -----------  -------
enable               off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf</h>

Shows configuration information for redistributing OSPF IPv4 routes into BGP for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute ospf
        operational  applied
------  -----------  -------
enable               off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route</h>

Shows BGP IPv4 aggregate routes (a range of networks in your routing table aggregated into a single prefix) for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast aggregate-route

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\></h>

Shows information about a specific BGP IPv4 aggregate route (a range of networks in your routing table aggregated into a single prefix).

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.  |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16
              operational  applied  
------------  -----------  ---------
as-set                     on       
route-map                  routemap1
summary-only               on 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast network</h>

Shows BGP IPv4 static networks for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast network
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast network \<static-network-id\></h>

Shows information about a specific BGP IPv4 static network for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<static-network-id>` |   The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32
           operational  applied
---------  -----------  -------
route-map               HI-PRIO

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import</h>

Shows configuration information about BGP IPV4 route import (route leaking) for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast route-import
                operational  applied
--------------  -----------  -------
from-vrf                            
  enable                     off    
  [list]        none                
[route-target]  none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf</h>

Shows configuration information about VRF to VRF IPv4 route leaking.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast route-import from-vrf
       operational  applied
------  -----------  -------
enable               off    
[list]  none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf list</h>

Shows the IPv4 routes in the BGP RIB imported from the VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast route-import from-vrf list
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast route-import from-vrf list

----
none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf list \<leak-vrf-id\></h>

Shows IPv4 routes in the BGP RIB that leak between VRFs.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<leak-vrf-id>` |  The VRF from which routes are leaked. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast route-import from-vrf list BLUE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths</h>

Shows BGP IPv4 multipath configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast multipaths
                        operational  applied
----------------------  -----------  -------
compare-cluster-length               off    
ebgp                                 64     
ibgp                                 64
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance</h>

Shows the BGP IPv4 admin distances configured for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast admin-distance
          operational  applied
--------  -----------  -------
external               20     
internal               200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export</h>

Shows BGP IPv4 route export configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast route-export
                operational  applied
--------------  -----------  -------
to-evpn                             
  enable                     off    
[route-target]  none                
to-vrf
  [list]        none                
rd              none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn</h>

Shows the controls for exporting IPv4 routes from the specified VRF into EVPN (as type-5 routes).

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast route-export to-evpn
        operational  applied
------  -----------  -------
enable               off 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib</h>

Shows the IPv4 local RIB for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib

IPV4 Routes
==============
                                                                             
    LocalPref - Local Preference, Best - Best path, Reason - Reason for selection
                                                                             
    IPv4 Prefix      Nexthop  Metric  Weight  LocalPref  Aspath  Best  Reason      Flags
    ---------------  -------  ------  ------  ---------  ------  ----  ----------  -----
    10.0.0.9/32      swp51    0                                  on    Router ID        
                     swp52                                                              
                              0                                                         
                                                                                    
    10.0.0.10/32     swp51    0                                  on    Router ID        
                     swp52                                                              
                              0                                                         
                                                                                    
    10.10.10.1/32             0       32768                      on    First path       
                                                                       received         
    10.10.10.2/32    swp51    0                                                         
                     swp52                                       on    Older Path       
                              0                                                         
                                                                                    
    10.10.10.3/32    swp51    0                                                         
                     swp52                                       on    Older Path       
                              0                                                         
                                                                                    
    10.10.10.4/32    swp51    0                                                         
                     swp52                                       on    Older Path       
                              0                                                         
                                                                                    
    10.10.10.101/32  swp51    0                                  on    First path       
                                                                       received         
                                                                                    
    10.10.10.102/32  swp52    0                                  on    First path       
                                                                       received
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route</h>

Shows information about the IPv4 routes in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route
LocalPref - Local Preference, Best - Best path, Reason - Reason for selection
                                                                             
IPv4 Prefix      Nexthop  Metric  Weight  LocalPref  Aspath  Best  Reason      Flags    
---------------  -------  ------  ------  ---------  ------  ----  ---------…  ---------
10.0.0.9/32      swp51    0                          65103   on    Router ID   multipath
                                                     65199                              
                 swp52    0                          65103                     multipath
                                                     65199                              
10.0.0.10/32     swp51    0                          65103   on    Router ID   multipath
                                                     65199                              
                 swp52    0                          65103                     multipath
                                                     65199                              
10.10.10.1/32             0       32768                      on    First path           
                                                                   received             
10.10.10.2/32    swp51    0                          65102                     multipath
                                                     65199                              
                 swp52    0                          65102   on    Older Path  multipath
                                                     65199                              
10.10.10.3/32    swp51    0                          65103                     multipath
                                                     65199                              
                 swp52    0                          65103   on    Older Path  multipath
                                                     65199                              
10.10.10.4/32    swp51    0                          65104                     multipath
                                                     65199                              
                 swp52    0                          65104   on    Older Path  multipath
                                                     65199                              
10.10.10.101/32  swp51    0                          65199   on    First path           
                                                                   received             
                                                                                        
10.10.10.102/32  swp52    0                          65199   on    First path           
                                                                   received
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\></h>

Shows information about the specified IPv4 route in the local RIB, such as the BGP peer to which the path is advertised and the path count.

### Command Syntax

| Syntax |  Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32
                 operational  applied
---------------  -----------  -------
[advertised-to]  swp51               
[advertised-to]  swp52               
[path]           1                   
[path]           2                   
path-count       2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path</h>

Shows information about the paths for the specified IPv4 route in the local RIB.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.0.0.9/32 path -o json
{
  "1": {
    "aspath": {
      "65103": {},
      "65199": {}
    },
    "flags": {
      "multipath": {}
    },
    "last-update": 1682960995,
    "nexthop": {
      "1": {
        "accessible": "on",
        "afi": "ipv6",
        "ip": "fe80::4ab0:2dff:fe08:9898",
        "metric": 0,
        "scope": "global"
      },
      "2": {
        "accessible": "on",
        "afi": "ipv6",
        "ip": "fe80::4ab0:2dff:fe08:9898",
        "scope": "link-local",
        "used": "on"
      }
    },
    "nexthop-count": 2,
    "origin": "incomplete",
    "path-from": "external",
    "peer": {
      "hostname": "spine01",
      "id": "fe80::4ab0:2dff:fe08:9898",
      "interface": "swp51",
      "router-id": "10.10.10.101",
      "type": "external"
    },
    "valid": "on"
  },
  "2": {
    "aspath": {
      "65103": {},
      "65199": {}
    },
    "bestpath": {
      "from-as": 65199,
      "overall": "on",
      "selection-reason": "Older Path"
    },
    "flags": {
      "multipath": {}
    },
    "last-update": 1682960995,
    "nexthop": {
      "1": {
        "accessible": "on",
        "afi": "ipv6",
        "ip": "fe80::4ab0:2dff:fed8:67cb",
        "metric": 0,
        "scope": "global"
      },
      "2": {
        "accessible": "on",
        "afi": "ipv6",
        "ip": "fe80::4ab0:2dff:fed8:67cb",
        "scope": "link-local",
        "used": "on"
      }
    },
    "nexthop-count": 2,
    "origin": "incomplete",
    "path-from": "external",
    "peer": {
      "hostname": "spine02",
      "id": "fe80::4ab0:2dff:fed8:67cb",
      "interface": "swp52",
      "router-id": "10.10.10.102",
      "type": "external"
    },
    "valid": "on"
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\></h>

Shows information about a specific IPv4 route path in the local RIB.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation.  |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.0.0.9/32 path 1 -o json
{
  "aspath": {
    "65103": {},
    "65199": {}
  },
  "flags": {
    "multipath": {}
  },
  "last-update": 1682960994,
  "nexthop": {
    "1": {
      "accessible": "on",
      "afi": "ipv6",
      "ip": "fe80::4ab0:2dff:fe08:9898",
      "metric": 0,
      "scope": "global"
    },
    "2": {
      "accessible": "on",
      "afi": "ipv6",
      "ip": "fe80::4ab0:2dff:fe08:9898",
      "scope": "link-local",
      "used": "on"
    }
  },
  "nexthop-count": 2,
  "origin": "incomplete",
  "path-from": "external",
  "peer": {
    "hostname": "spine01",
    "id": "fe80::4ab0:2dff:fe08:9898",
    "interface": "swp51",
    "router-id": "10.10.10.101",
    "type": "external"
  },
  "valid": "on"
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> nexthop</h>

Shows information about the nexthops for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 nexthop
Nexthop  accessible  afi   ip                         metric  scope       used
-------  ----------  ----  -------------------------  ------  ----------  ----
1        on          ipv6  fe80::4ab0:2dff:fed8:67cb  0       global          
2        on          ipv6  fe80::4ab0:2dff:fed8:67cb          link-local  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\></h>

Shows next hop information for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation |
| `<path-id>` | The path ID. |
| `<nexthop-id>`| The nexthop ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 nexthop 2
            operational                applied
----------  -------------------------  -------
accessible  on                                
afi         ipv6                              
ip          fe80::4ab0:2dff:fed8:67cb         
scope       link-local                        
used        on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> peer</h>

Shows BGP peer information for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation.  |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 peer
           operational                applied
---------  -------------------------  -------
hostname   spine02                           
id         fe80::4ab0:2dff:fed8:67cb         
interface  swp52                             
router-id  10.10.10.102                      
type       external
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> flags</h>

Shows route path flags for the specified IPv4 route in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation.  |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 flags
operational  applied
-----------  -------
multipath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> bestpath</h>

Shows best path information, such as the selection reason, for the specified IPv4 route in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation.  |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 bestpath
                  operational  applied
----------------  -----------  -------
from-as           65199               
overall           on                  
selection-reason  Older Path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> aspath</h>

Shows the AS paths for the specified IPv4 route in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 aspath
Aspath
------
65103 
65199
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> community</h>

Shows the community names for the community list for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> large-community</h>

Shows the community names for the large community list for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> ext-community</h>

Shows the community names for the extended community list for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<route-id>` | The IPv4 address and route prefix in CIDR notation. |
| `<path-id>`  | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 ext-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast update-group</h>

Shows the BGP IPv4 update groups for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast update-group
  Time created  LocalAs change  Prepend Flag  Replace AS flag  Minimum             Routemap  Update group  Summary     
                                                                advertisement                                           
                                                                interval                                                
-  ------------  --------------  ------------  ---------------  -----------------…  --------  ------------  ------------
1  1682551553                                                   0                             1             sub-group: 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast update-group \<group-id\></h>

Shows information about a specific BGP IPv4 update group in the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<group-id>` | The group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast update-group 3 -o json
{
  "create-time": 1682967480,
  "min-route-advertisement-interval": 0,
  "sub-group": {
    "7": {
      "adjacency-count": 8,
      "coalesce-time": 1250,
      "counters": {
        "join-events": 6,
        "merge-check-events": 0,
        "merge-events": 4,
        "peer-refresh-events": 0,
        "prune-events": 4,
        "split-events": 0,
        "switch-events": 0
      },
      "create-time": 1682967480,
      "needs-refresh": "off",
      "neighbor": {
        "swp51": {},
        "swp52": {}
      },
      "packet-counters": {
        "queue-hwm-len": 5,
        "queue-len": 0,
        "queue-total": 42,
        "total-enqueued": 42
      },
      "sub-group-id": 7,
      "version": 106
    }
  },
  "update-group-id": "3"
}

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast update-group \<group-id\> sub-group</h>

Shows the subgroups for a specific BGP IPv4 update group in the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<group-id>` | The group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast update-group 3 subgroup
 -o json
{
  "7": {
    "adjacency-count": 8,
    "coalesce-time": 1250,
    "counters": {
      "join-events": 6,
      "merge-check-events": 0,
      "merge-events": 4,
      "peer-refresh-events": 0,
      "prune-events": 4,
      "split-events": 0,
      "switch-events": 0
    },
    "create-time": 1682967480,
    "needs-refresh": "off",
    "neighbor": {
      "swp51": {},
      "swp52": {}
    },
    "packet-counters": {
      "queue-hwm-len": 5,
      "queue-len": 0,
      "queue-total": 42,
      "total-enqueued": 42
    },
    "sub-group-id": 7,
    "version": 106
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast</h>

Shows BGP IPv6 configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast
        operational  applied
------  -----------  -------
enable               on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route</h>

Shows BGP IPv6 aggregate routes for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<aggregate-route-id>` | The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast aggregate-route 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\></h>

Shows IPv6 aggregate routes. Aggregating a range of networks in your routing table into a single prefix can minimize the size of the routing table and save bandwidth.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<aggregate-route-id>` | The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast aggregate-route 2001:db8::1/128
              operational  applied  
------------  -----------  ---------
as-set                     on       
route-map                  routemap1
summary-only               on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast network</h>

Shows the IPv6 static networks for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast network
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast network \<static-network-id\></h>

Shows information about a specific IPv6 static network for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<static-network-id>` | The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast network 2001:db8::1/128
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import</h>

Shows BGP IPv6 route import configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast route-import
               operational  applied
--------------  -----------  -------
from-vrf                            
  enable                     off    
  [list]        none                
[route-target]  none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf</h>

Shows configuration information about VRF to VRF IPv6 route leaking.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast route-import from-vrf
        operational  applied
------  -----------  -------
enable               off    
[list]  none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf list</h>

Shows IPv6 routes in the BGP RIB that are dynamically leaked between VRFs.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast route-import from-vrf list
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths</h>

Shows BGP IPv6 multipath configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast multipaths
                       operational  applied
----------------------  -----------  -------
compare-cluster-length               off    
ebgp                                 120    
ibgp                                 120
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance</h>

Shows the BGP IPv6 admin distances configured for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast admin-distance
          operational  applied
--------  -----------  -------
external               20     
internal               200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export</h>

Shows BGP IPv6 route export configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast route-export
                operational  applied
--------------  -----------  -------
to-evpn                             
  enable                     off    
[route-target]  none                
to-vrf                              
  [list]        none                
rd              none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn</h>

Shows BGP IPv6 route export to EVPN configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast route-export to-evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute</h>

Shows configuration information for BGP IPv6 route redistribution for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast redistribute
           operational  applied
---------  -----------  -------
connected                      
  enable                on    
kernel                         
  enable                off    
static                         
  enable                off    
ospf6                          
  enable                on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static</h>

Shows configuration information for BGP IPv6 static route redistribution for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast redistribute static
        operational  applied
------  -----------  -------
enable               on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected</h>

Shows configuration information for BGP IPv6 connected route redistribution for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast redistribute connected
        operational  applied
------  -----------  -------
enable               on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel</h>

Shows configuration information for BGP IPv6 kernel route redistribution for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast redistribute kernel
        operational  applied
------  -----------  -------
enable               off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6</h>

Shows configuration information for BGP OSPF IPv6 route redistribution for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast redistribute ospf6
       operational  applied
------  -----------  -------
enable               on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib</h>

Shows the IPv6 local RIB for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib

IPV6 Routes
==============
                                                                             
    LocalPref - Local Preference, Best - Best path, Reason - Reason for selection
                                                                             
    IPv6 Prefix      Nexthop  Metric  Weight  LocalPref  Aspath  Best  Reason  Flags
    ---------------  -------  ------  ------  ---------  ------  ----  ------  -----
    2001:db8::1/128                   32768
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\></h>

Shows information about the specified IPv6 route in the local RIB, such as the BGP peer to which the path is advertised and the path count.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128
            operational  applied
----------  -----------  -------
[path]      1                   
path-count  1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path</h>

Shows the paths for the specified IPv6 route in the local RIB.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path -o json
{
  "1": {
    "aspath": {},
    "flags": {},
    "last-update": 1685650645,
    "local": "on",
    "metric": 0,
    "nexthop": {
      "1": {
        "accessible": "off",
        "afi": "ipv6",
        "ip": "::",
        "scope": "global",
        "used": "on"
      }
    },
    "nexthop-count": 1,
    "origin": "IGP",
    "peer": {
      "id": "::",
      "router-id": "10.10.10.1"
    },
    "sourced": "on",
    "valid": "off",
    "weight": 32768
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\></h>

Shows information about the paths for the specified IPv6 route in the local RIB.

{{%notice note%}}
You must add `-o json` at the end of the command to see the output.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 1 -o json
{
  "aspath": {},
  "flags": {},
  "last-update": 1685650646,
  "local": "on",
  "metric": 0,
  "nexthop": {
    "1": {
      "accessible": "off",
      "afi": "ipv6",
      "ip": "::",
      "scope": "global",
      "used": "on"
    }
  },
  "nexthop-count": 1,
  "origin": "IGP",
  "peer": {
    "id": "::",
    "router-id": "10.10.10.1"
  },
  "sourced": "on",
  "valid": "off",
  "weight": 32768
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> nexthop</h>

Shows the next hops for the specified IPv6 route path in the local RIB.

{{%notice note%}}
You must add `-o json` at the end of the command to see the output.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 nexthop -o json
{
  "1": {
    "accessible": "off",
    "afi": "ipv6",
    "ip": "::",
    "scope": "global",
    "used": "on"
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\></h>

Shows next hop information for the specified IPv6 route path in the local RIB.

{{%notice note%}}
You must add `-o json` at the end of the command to see the output.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id` | The path ID. |
| `<nexthop-id>` | The nexthop ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 1 nexthop 1 -o json
{
  "accessible": "off",
  "afi": "ipv6",
  "ip": "::",
  "scope": "global",
  "used": "on"
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> peer</h>

Shows BGP peer information for the specified IPv6 route path in the local RIB.

{{%notice note%}}
You must add `-o json` at the end of the command to see the output.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 1 peer -o json
{
  "id": "::",
  "router-id": "10.10.10.1"
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> flags</h>

Shows route path flags for the specified IPv6 route in the local RIB.

{{%notice note%}}
You must add `-o json` at the end of the command to see the output.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 1 flags  -o json
{}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> bestpath</h>

Shows best path information, such as the selection reason, for the specified IPv6 route in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 1 bestpath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> aspath</h>

Shows the AS paths for the specified IPv6 route in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> community</h>

Shows the community names for the community list for the specified IPv6 route path in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> large-community</h>

Shows the community names for the large community list for the specified IPv6 route path in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> ext-community</h>

Shows the community names for the extended community list for the specified IPv6 route path in the local RIB.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 ext-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast update-group</h>

Shows the BGP IPv6 update groups for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast update-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast update-group \<group-id\></h>

Shows information about a specific BGP IPv6 update group in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<group-id>` | The group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast update-group 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast update-group \<group-id\> sub-group</h>

Shows the subgroups for a specific BGP IPv6 update group in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<group-id>` | The group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast update-group 2 subgroup
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn</h>

Shows EVPN BGP configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn
        operational  applied
------  -----------  -------
enable               off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib</h>

Shows the EVPN local RIB for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib
rd
=====
              Summary      
------------  -------------
10.10.10.1:2  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:3  route-type: 1
              route-type: 4
10.10.10.1:4  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:5  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:6  route-type: 5
10.10.10.1:7  route-type: 5
10.10.10.1:8  route-type: 1
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd</h>

Shows the EVPN local RIB <span class="a-tooltip">[RDs](## "Route Distinguisher")</span> for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd
              Summary      
------------  -------------
10.10.10.1:2  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:3  route-type: 1
              route-type: 4
10.10.10.1:4  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:5  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:6  route-type: 5
10.10.10.1:7  route-type: 5
10.10.10.1:8  route-type: 1
              route-type: 4
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\></h>

Shows a specific EVPN local RIB <span class="a-tooltip">[RD](## "Route Distinguisher")</span> for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:9
              operational  applied
------------  -----------  -------
[route-type]  1                   
[route-type]  4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type</h>

Shows the EVPN local RIB <span class="a-tooltip">[RD](## "Route Distinguisher")</span> route distinguisher route types for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:9 route-type
  Summary                                                                          
-  ---------------------------------------------------------------------------------
1  route: 03:44:38:39:be:ef:aa:00:00:03+::]/352+03:44:38:39:be:ef:aa:00:00:03+::/352
4  route:                               03:44:38:39:be:ef:aa:00:00:03+10.10.10.1/352
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type \<route-type-id\></h>

Shows information about a specific EVPN local RIB <span class="a-tooltip">[RD](## "Route Distinguisher")</span> route distinguisher route type for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|
| `<route-type-id>` |  The route type: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20 route-type multicast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type \<route-type-id\> route</h>

Shows the routes in the EVPN local RIB for the specified VRF with a specific <span class="a-tooltip">[RD](## "Route Distinguisher")</span> and route type.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|
| `<route-type-id>` |  The route type: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20 route-type multicast route
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type \<route-type-id\> route \<evpn-route-id\></h>

Shows the routes in the EVPN local RIB for the specified VRF with a specific <span class="a-tooltip">[RD](## "Route Distinguisher")</span> route type and EVPN route type.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|
| `<route-type-id>` |  The route type: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5.|
| `<evpn-route-id>` |  The EVPN route type.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20 route-type multicast route 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn update-group</h>

Shows information about BGP EVPN update group events.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn update-group
   Time created  LocalAs change  Prepend Flag  Replace AS flag  Minimum advertisement interval  Routemap  Update group  Summary     
-  ------------  --------------  ------------  ---------------  ------------------------------  --------  ------------  ------------
2  1682551553                                                   0                                         2             sub-group: 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn update-group \<group-id\></h>

Shows information about a specific BGP EVPN update group.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<group ID>` |  The BGP group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn update-group 2 -o json
{
  "create-time": 1682551552,
  "min-route-advertisement-interval": 0,
  "sub-group": {
    "2": {
      "adjacency-count": 90,
      "coalesce-time": 1150,
      "counters": {
        "join-events": 3,
        "merge-check-events": 0,
        "merge-events": 2,
        "peer-refresh-events": 0,
        "prune-events": 1,
        "split-events": 0,
        "switch-events": 0
      },
      "create-time": 1682551552,
      "needs-refresh": "off",
      "neighbor": {
        "swp51": {},
        "swp52": {}
      },
      "packet-counters": {
        "queue-hwm-len": 39,
        "queue-len": 0,
        "queue-total": 222,
        "total-enqueued": 222
      },
      "sub-group-id": 2,
      "version": 38
    }
  },
  "update-group-id": "2"
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn update-group \<group-id\> sub-group</h>

Shows the subgroup information for a specific BGP EVPN update group.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<group ID>` |  The BGP group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn update-group 2 sub-group -o json
{
  "2": {
    "adjacency-count": 90,
    "coalesce-time": 1150,
    "counters": {
      "join-events": 3,
      "merge-check-events": 0,
      "merge-events": 2,
      "peer-refresh-events": 0,
      "prune-events": 1,
      "split-events": 0,
      "switch-events": 0
    },
    "create-time": 1682551552,
    "needs-refresh": "off",
    "neighbor": {
      "swp51": {},
      "swp52": {}
    },
    "packet-counters": {
      "queue-hwm-len": 39,
      "queue-len": 0,
      "queue-total": 222,
      "total-enqueued": 222
    },
    "sub-group-id": 2,
    "version": 38
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast route-counters</h>

Shows the number of IPv4 routes for a specific BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast route-counters
                operational  applied
--------------  -----------  -------
adj-rib-in      0                   
all-rib         6                   
best-routes     1                   
damped          0                   
history         0                   
removed         0                   
route-count     7                   
routes-counted  6                   
stale           0                   
usable          6                   
valid           6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes</h>

Shows information about the IPv4 advertised routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes
IPv4 Prefix      Summary
---------------  -------
10.0.0.9/32      Path: 1
                 Path: 2
10.0.0.10/32     Path: 1
                 Path: 2
10.10.10.1/32    Path: 1
10.10.10.2/32    Path: 1
                 Path: 2
10.10.10.3/32    Path: 1
                 Path: 2
10.10.10.4/32    Path: 1
                 Path: 2
10.10.10.101/32  Path: 1
10.10.10.102/32  Path: 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\></h>

Shows information about a specific IPv4 advertised route for a BGP neighbor in the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 -o json
{
  "path": {
    "1": {
      "aspath": {},
      "bestpath": {
        "overall": "on",
        "selection-reason": "First path received"
      },
      "flags": {},
      "last-update": 1682551550,
      "metric": 0,
      "nexthop": {
        "1": {
          "accessible": "on",
          "afi": "ipv4",
          "ip": "0.0.0.0",
          "metric": 0,
          "used": "on"
        }
      },
      "nexthop-count": 1,
      "origin": "incomplete",
      "peer": {
        "id": "0.0.0.0",
        "router-id": "10.10.10.1"
      },
      "sourced": "on",
      "valid": "on",
      "weight": 32768
    }
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path</h>

Shows path information about a specific IPv4 advertised route for a BGP neighbor in the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path -o json
{
  "1": {
    "aspath": {},
    "bestpath": {
      "overall": "on",
      "selection-reason": "First path received"
    },
    "flags": {},
    "last-update": 1682551549,
    "metric": 0,
    "nexthop": {
      "1": {
        "accessible": "on",
        "afi": "ipv4",
        "ip": "0.0.0.0",
        "metric": 0,
        "used": "on"
      }
    },
    "nexthop-count": 1,
    "origin": "incomplete",
    "peer": {
      "id": "0.0.0.0",
      "router-id": "10.10.10.1"
    },
    "sourced": "on",
    "valid": "on",
    "weight": 32768
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\></h>

Shows information about a specific IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 -o json
{
  "1": {
    "aspath": {},
    "bestpath": {
      "overall": "on",
      "selection-reason": "First path received"
    },
    "flags": {},
    "last-update": 1682551549,
    "metric": 0,
    "nexthop": {
      "1": {
        "accessible": "on",
        "afi": "ipv4",
        "ip": "0.0.0.0",
        "metric": 0,
        "used": "on"
      }
    },
    "nexthop-count": 1,
    "origin": "incomplete",
    "peer": {
      "id": "0.0.0.0",
      "router-id": "10.10.10.1"
    },
    "sourced": "on",
    "valid": "on",
    "weight": 32768
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> nexthop</h>

Shows information about the next hops for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 nexthop -o json
{
  "1": {
    "accessible": "on",
    "afi": "ipv4",
    "ip": "0.0.0.0",
    "metric": 0,
    "used": "on"
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> nexthop \<nexthop-id\></h>

Shows information about the a specific next hop for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |
| `<nexthop-id>` |   The nexthop ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 nexthop 1
            operational  applied
----------  -----------  -------
accessible  on                  
afi         ipv4                
ip          0.0.0.0             
metric      0                   
used        on 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> peer</h>

Shows information about the peers for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 peer
           operational  applied
---------  -----------  -------
id         0.0.0.0             
router-id  10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> flags</h>

Shows information about the flags for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 flags
 operational  applied
  -----------  -------
  multipath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> bestpath</h>

Shows information about the bestpath for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 bestpath
                  operational          applied
----------------  -------------------  -------
overall           on                          
selection-reason  First path received
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> aspath</h>

Shows information about the AS path for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.101/32 path 1 aspath
Aspath
------
65199
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> community</h>

Shows information about the communities for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.101/32 path 1 community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> large-community</h>

Shows information about the large communities for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 large-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> ext-community</h>

Shows information about the extended communities for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.101/32 path 1 ext-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart timers</h>

Shows the BGP graceful restart selection deferral and stale path timer settings for the BGP peer.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast graceful-restart timers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart timers stale-path</h>

Shows the BGP graceful restart stale path timer settings for the BGP peer.

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast graceful-restart timers stale-path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart timers selection-deferral</h>

Shows the BGP graceful restart  selection deferral timers for the BGP peer.

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast graceful-restart timers selection-deferral
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes</h>

Shows information about the IPv4 received routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\></h>

Shows information about a specific IPv4 received route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv4 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path</h>

Shows information about a specific IPv4 received route path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv4 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\></h>

Shows information about a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> nexthop</h>

Shows information about the next hops for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 nexthop -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> nexthop \<nexthop-id\></h>

Shows information about a specific next hop for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |
| `<nexthop-id>` |   The nexthop ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 nexthop 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> peer</h>

Shows information about peers for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 peer -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> flags</h>

Shows information about flags for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 flags 
operational  applied
-----------  -------
multipath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> bestpath</h>

Shows information about the best paths for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 bestpath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> aspath</h>

Shows information about the AS paths for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 aspath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> community</h>

Shows information about the communities for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> large-community</h>

Shows information about the large communities for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 large-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> ext-community</h>

Shows information about the extended communities for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 ext-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart timers</h>

Shows the BGP graceful restart selection deferral and stale path timer settings for the BGP peer.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast graceful-restart timers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart timers stale-path</h>

Shows the BGP graceful restart stale path timer settings for the BGP peer.

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast graceful-restart timers stale-path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart timers selection-deferral</h>

Shows the BGP graceful restart selection deferral timers for the BGP peer.

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast graceful-restart timers selection-deferral
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes</h>

Shows information about the IPv6 received routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\></h>

Shows information about a specific IPv6 received route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path</h>

Shows information about IPv6 received route paths for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\></h>

Shows information about a specific IPv6 received route path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> nexthop</h>

Shows information about the IPv6 received route path nexthops for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 nexthop -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> nexthop \<nexthop-id\></h>

Shows information about a specific IPv6 received route path nexthop for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |
| `<nexthop-id>` |   The nexthop ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 nexthop 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> peer</h>

Shows information about the IPv6 received route path peers for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 peer -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> flags</h>

Shows information about the IPv6 received route path flags for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 flags -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> bestpath</h>

Shows information about the IPv6 received route path bestpath for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 bestpath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> aspath</h>

Shows information about the IPv6 received route path AS path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 aspath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> community</h>

Shows information about the IPv6 received route path communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> large-community</h>

Shows information about the IPv6 received route path large communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 large-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> ext-community</h>

Shows information about the IPv6 received route path extended communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 ext-community -o json
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast route-counters</h>

Shows the number of IPv6 routes for a specific BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast route-counters -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes</h>

Shows information about the IPv6 advertised routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\></h>

Shows information about a specific IPv6 advertised route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path</h>

Shows information about the IPv6 advertised route paths for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes  2001:db8::1/128 path -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\></h>

Shows information about a specific IPv6 advertised route path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> nexthop</h>

Shows information about the IPv6 advertised route nexthops for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 nexthop -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> peer</h>

Shows information about the IPv6 advertised route peers for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 peers -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> flags</h>

Shows information about the IPv6 advertised route flags for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 flags -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> bestpath</h>

Shows information about the IPv6 advertised route best path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 bestpath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> aspath</h>

Shows information about the IPv6 advertised route AS path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 aspath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> community</h>

Shows information about the IPv6 advertised route communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> large-community</h>

Shows information about the IPv6 advertised route large communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 large-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> ext-community</h>

Shows information about the IPv6 advertised route extended communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 ext-community -o json
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> bgp-info</h>

Shows BGP information for the specified EVPN VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 bgp-info
                           operational   applied
-------------------------  ------------  -------
advertise-default-gateway  off                  
advertise-svi-ip           off                  
in-kernel                  on                   
local-vtep                 10.0.0.1             
rd                         10.10.10.1:5         
type                       L2                   
[export-route-target]      65101:10             
[import-route-target]      65101:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn bgp-info</h>

Shows layer 3 VNI information from BGP for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn bgp-info
                       operational        applied
---------------------  -----------------  -------
local-vtep             10.0.1.12                 
rd                     10.10.10.1:3              
router-mac             44:38:39:be:ef:aa         
system-ip              10.10.10.1                
system-mac             44:38:39:22:01:7a         
[export-route-target]  65101:4001                
[import-route-target]  65101:4001
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp confederation</h>

Shows BGP confederation configuration.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp confederation
             operational  applied
-----------  -----------  -------
id                        none   
[member-as]   
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp confederation member-as</h>

Shows the BGP confederation member AS. A BGP confederation divides a large AS into subautonomous systems, which are uniquely identified by a sub-AS number.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp confederation member-as
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp dynamic-neighbor</h>

Shows BGP dynamic neighbor configuration on the switch. BGP dynamic neighbors provide BGP peering to remote neighbors within a specified range of IPv4 or IPv6 addresses for a BGP peer group. You can configure each range as a subnet IP address.

After you configure the dynamic neighbors, a BGP speaker can listen for, and form peer relationships with, any neighbor that is in the IP address range and maps to a peer group.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp dynamic-neighbor
[listen-range]               10.0.1.0/24
limit                        5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp dynamic-neighbor listen-range</h>

Shows the address range configuration for BGP peering to remote neighbors.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp dynamic-neighbor listen-range
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp dynamic-neighbor listen-range \<ip-sub-prefix-id\></h>

Shows information about a specific address range for BGP peering to remote neighbors.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp dynamic-neighbor listen-range 10.0.1.0/24
            operational  applied
----------  -----------  -------
peer-group               SPINE 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\></h>

Shows global configuration for the specified BGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  | The BGP neighbor name or interface (for BGP unnumbered). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51
                               operational                applied     pending   
-----------------------------  -------------------------  ----------  ----------
description                                               none        none      
enforce-first-as                                          off         off       
multihop-ttl                                              auto        auto      
nexthop-connected-check                                   on          on        
passive-mode                                              off         off       
password                                                  none        none      
address-family                                                                  
  ipv4-unicast                                                                  
    enable                                                on          on        
    add-path-tx                                           off         off       
    nexthop-setting                                       auto        auto      
    route-reflector-client                                off         off       
    route-server-client                                   off         off       
    soft-reconfiguration                                  off         off       
    aspath                                                                      
      private-as                                          none        none      
      replace-peer-as                                     off         off       
      allow-my-asn                                                              
        enable                                            off         off       
    attribute-mod                                                               
      aspath                   off                        on          on        
      med                      off                        on          on        
      nexthop                  off                        on          on
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd</h>

Shows BFD configuration for the specified BGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 bfd
        operational  applied  pending
------  -----------  -------  -------
enable               off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> capabilities</h>

Shows the capabilities for the specified BGP neighbor, such as if extended next hop and 32-bit ASN transmission are enabled.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 capabilities
                     operational  applied  pending
-------------------  -----------  -------  -------
extended-nexthop     on           auto     auto   
rx-asn32             off                          
rx-extended-nexthop  off                          
rx-graceful-restart  on                           
rx-restart-r-bit     off                          
rx-route-refresh     on                           
tx-asn32             on                           
tx-graceful-restart  on                           
tx-route-refresh     on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as</h>

Shows the local AS for the specified BGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 local-as
        operational  applied  pending
------  -----------  -------  -------
enable               off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> graceful-restart</h>

Shows BGP graceful restart configuration for the specified BGP neighbor. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 graceful-restart
      operational  applied  pending
----  -----------  -------  -------
mode               auto     auto
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security</h>

Shows BGP TTL security configuration for the specified BGP neighbor. BGP TTL security prevents attacks against eBGP, such as denial of service (DoS) attacks.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 ttl-security
        operational  applied  pending
------  -----------  -------  -------
enable  off          off      off  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> nexthop</h>

Shows the BGP neighbor next hop.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 nexthop
             operational                applied  pending
-----------  -------------------------  -------  -------
ipv4         10.10.10.1                                 
ipv6-global  fe80::4ab0:2dff:fed1:9b88                  
ipv6-local   fe80::4ab0:2dff:fed1:9b88
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> message-stats</h>

Shows BGP neighbor message statistics.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 message-stats
                    operational  applied  pending
------------------  -----------  -------  -------
input-queue         0                            
output-queue        0                            
rx-keepalives       93900                        
rx-opens            1                            
rx-route-refreshes  0                            
rx-total            93980                        
tx-keepalives       93898                        
tx-opens            1                            
tx-route-refreshes  0                            
tx-total            94007
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ebgp-policy</h>

Shows the Default External BGP (EBGP) route propagation behavior for the specified BGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 ebgp-policy
  operational  applied  pending
  -----------  -------  -------
  inbound                      
  outbound                     
  inbound                      
  outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family</h>

Shows all address family configuration for the specified BGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family
                             operational  applied  pending
---------------------------  -----------  -------  -------
ipv4-unicast                                              
  enable                                  on       on     
  add-path-tx                             off      off    
  nexthop-setting                         auto     auto   
  route-reflector-client                  off      off    
  route-server-client                     off      off    
  soft-reconfiguration                    off      off    
  aspath                                                  
    private-as                            none     none   
    replace-peer-as                       off      off    
    allow-my-asn                                          
      enable                              off      off    
  attribute-mod                                           
    aspath                   off          on       on     
    med                      off          on       on     
    nexthop                  off          on       on     
  rx-prefix                  17                           
  tx-prefix                  8                            
  update-group               1                            
  capabilities                                            
    rx-addpath               on                           
    rx-graceful-restart      on                           
    rx-mpbgp                 on                           
    rx-restart-f-bit         off
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast</h>

Shows configuration information for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast
                           operational  applied  pending
-------------------------  -----------  -------  -------
enable                                  on       on     
add-path-tx                             off      off    
nexthop-setting                         auto     auto   
route-reflector-client                  off      off    
route-server-client                     off      off    
soft-reconfiguration                    off      off    
aspath                                                  
  private-as                            none     none   
  replace-peer-as                       off      off    
  allow-my-asn                                          
    enable                              off      off    
attribute-mod                                           
  aspath                   off          on       on     
  med                      off          on       on     
  nexthop                  off          on       on     
rx-prefix                  17                           
tx-prefix                  8                            
update-group               1                            
capabilities                                            
  rx-addpath               on                           
  rx-graceful-restart      on                           
  rx-mpbgp                 on                           
  rx-restart-f-bit         off                          
  tx-addpath               off                          
  tx-mpbgp                 on
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast attribute-mod</h>

Shows the attribute modification configuration settings for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast attribute-mod
         operational  applied  pending
-------  -----------  -------  -------
aspath   off          on       on     
med      off          on       on     
nexthop  off          on       on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath</h>

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath
                 operational  applied  pending
---------------  -----------  -------  -------
private-as                    none     none   
replace-peer-as               off      off    
allow-my-asn                                  
  enable                      off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath allow-my-asn</h>

Shows if it is acceptable for a received AS path from the specified IPv4 neighbor to contain the ASN of the local system.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath allow-my-asn
        operational  applied  pending
------  -----------  -------  -------
enable               off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy</h>

Shows the policies for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy
                  operational  applied  pending
----------------  -----------  -------  -------
inbound                                        
  route-map                    none     none   
  aspath-list                  none     none   
  prefix-list                  none     none   
outbound                                       
  route-map                    none     none   
  unsuppress-map               none     none   
  aspath-list                  none     none   
  prefix-list                  none     none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound</h>

Shows the inbound policy for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy inbound
             operational  applied  pending
-----------  -----------  -------  -------
route-map                 none     none   
aspath-list               none     none   
prefix-list               none     none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound</h>

Shows the outbound policy for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy outbound
                operational  applied  pending
--------------  -----------  -------  -------
route-map                    none     none   
unsuppress-map               none     none   
aspath-list                  none     none   
prefix-list                  none     none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits</h>

Shows the limits on prefixes from the specified IPv4 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast prefix-limits
                     operational  applied  pending
-------------------  -----------  -------  -------
inbound                                           
  maximum                         none     none   
  warning-only       off                          
  warning-threshold               75       75
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound</h>

Shows the limits on inbound prefixes from the specified IPv4 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast prefix-limits inbound
                   operational  applied  pending
-----------------  -----------  -------  -------
maximum                         none     none   
warning-only       off                          
warning-threshold               75       75
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast default-route-origination</h>

Shows default route origination configuration for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast default-route-origination
        operational  applied  pending
------  -----------  -------  -------
enable               off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast community-advertise</h>

Shows community advertise configuration information for the specified BGP IPv4 neighbor. The community advertise option determines if the neighbor can advertise a prefix to any iBGP or eBGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast community-advertise
extended  on           on       on     
large     off          off      off    
regular   on           on       on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise</h>

Shows conditional advertisement configuration information for the specified BGP IPv4 neighbor. The BGP conditional advertisement option lets you advertise certain routes only if other routes either do or do not exist.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise
        operational  applied  pending
------  -----------  -------  -------
enable               off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast capabilities</h>

Shows all advertised and received capabilities for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast capabilities
                     operational  applied  pending
-------------------  -----------  -------  -------
rx-addpath           on                           
rx-graceful-restart  on                           
rx-mpbgp             on                           
rx-restart-f-bit     off                          
tx-addpath           off                          
tx-mpbgp             on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart</h>

Shows BGP graceful restart configuration information for the specified BGP IPv4 neighbor. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast graceful-restart
            operational  applied  pending
----------  -----------  -------  -------
rx-eof-rib  on                           
tx-eof-rib  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast</h>

Shows configuration information for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast attribute-mod</h>

Shows the attribute modification configuration settings for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast attribute-mod
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath</h>

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn</h>

Shows if it is acceptable for a received AS path from the specified IPv6 neighbor to contain the ASN of the local system.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast aspath allow-my-asn
        operational  applied  pending
------  -----------  -------  -------
enable                        on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits</h>

Shows limits on prefixes from the specified IPv6 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast prefix-limits
                     operational  applied  pending
-------------------  -----------  -------  -------
inbound                                           
  maximum                                  none   
  warning-threshold                        75
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound</h>

Shows the limits on inbound prefixes from the specified IPv6 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast prefix-limits inbound
                   operational  applied  pending
-----------------  -----------  -------  -------
maximum                                  none   
warning-threshold                        75
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast default-route-origination</h>

Shows default route origination configuration for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast default-route-origination
        operational  applied  pending
------  -----------  -------  -------
enable                        on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy</h>

Shows policies for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast policy
inbound                                        
  route-map                             map-inbound   
  aspath-list                           none   
  prefix-list                           none   
outbound                                       
  route-map                             map-outbound   
  unsuppress-map                        none   
  aspath-list                           none   
  prefix-list                           none 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound</h>

Shows the inbound policy for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast policy inbound
             operational  applied  pending
-----------  -----------  -------  -------
route-map                          map-inbound    
aspath-list                        none   
prefix-list                        none 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound</h>

Shows the outbound policy for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast policy outbound
                operational  applied  pending
--------------  -----------  -------  -------
route-map                             map-outbound   
unsuppress-map                        none   
aspath-list                           none   
prefix-list                           none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast community-advertise</h>

Shows community advertise configuration information for the specified BGP IPv6 neighbor. The community advertise option determines if the neighbor can advertise a prefix to any iBGP or eBGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast community-advertise
         operational  applied  pending
--------  -----------  -------  -------
extended                        on     
large                           off    
regular                         on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise</h>

Shows conditional advertisement configuration information for the specified BGP IPv6 neighbor. The BGP conditional advertisement option lets you advertise certain routes only if other routes either do or do not exist.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast conditional-advertise
       operational  applied  pending
------  -----------  -------  -------
enable                        on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast capabilities</h>

Shows all advertised and received capabilities for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast capabilities
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart</h>

Shows BGP graceful restart configuration information for the specified BGP IPv6 neighbor. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast graceful-restart
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn</h>

Shows EVPN configuration for the specified BGP neighbor.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn
                       operational  applied  pending
---------------------  -----------  -------  -------
enable                              on       on     
attribute-mod                                       
  aspath               off                          
  med                  off                          
  nexthop              on                           
rx-prefix              63                           
tx-prefix              90                           
update-group           2                            
capabilities                                        
  rx-addpath           on                           
  rx-graceful-restart  on                           
  rx-mpbgp             on                           
  tx-addpath           off                          
  tx-mpbgp             on                           
graceful-restart                                    
  rx-eof-rib           on                           
  tx-eof-rib           on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod</h>

Shows the attribute modification configuration settings for the specified neighbor for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn attribute-mod
         operational  applied  pending
-------  -----------  -------  -------
aspath   off                          
med      off                          
nexthop  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath</h>

Shows the configuration options for handling the AS path for prefixes to and from the specified BGP neighbor for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn</h>

Shows if it is acceptable for a received AS path to contain the ASN of the local system for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath allow-my-asn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart</h>

Shows graceful restart configuration for the specified BGP peer for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn graceful-restart
            operational  applied  pending
----------  -----------  -------  -------
rx-eof-rib  on                           
tx-eof-rib  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart timers</h>

Shows the BGP graceful restart selection deferral and stale path timer settings for the specified neighbor for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn graceful-restart timers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart timers stale-path</h>

Shows the BGP graceful restart stale path timer settings for the specified neighbor for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn graceful-restart timers stale-path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart timers selection-deferral</h>

Shows the BGP graceful restart selection deferral timer for the specified neighbor for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn graceful-restart timers selection-deferral
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy</h>

Shows EVPN policies for the specified neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy
                  operational  applied
----------------  -----------  -------
inbound                               
  route-map       MAP1         MAP1   
outbound                              
  route-map                    none   
  unsuppress-map               none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound</h>

Shows the inbound EVPN policy for the specified BGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy inbound
           operational  applied
---------  -----------  -------
route-map  MAP1         MAP1  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound</h>

Shows the outbound EVPN policy for the specified BGP neighbor.


### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy outbound
                operational  applied
--------------  -----------  -------
route-map                    none   
unsuppress-map               none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn capabilities</h>

Shows all advertised and received EVPN capabilities for the specified BGP neighbor.


### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn capabilities
                     operational  applied  pending
-------------------  -----------  -------  -------
rx-addpath           on                           
rx-graceful-restart  on                           
rx-mpbgp             on                           
tx-addpath           off                          
tx-mpbgp             on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers</h>

Shows timer configuration for the specified BGP peer, such as the reconnect, advertisement and keepalive intervals, and the hold time.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp52 timers
                     operational  applied  pending
-------------------  -----------  -------  -------
connection-retry     10           auto     auto   
hold                 9000         auto     auto   
keepalive            3000         auto     auto   
route-advertisement               auto     auto
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp nexthop</h>

Shows BGP next hop information for the specified VRF.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp nexthop
PathCnt - Number of paths pointing to this Nexthop, ResolvedVia - Resolved via   
address or interface, Interface - Resolved via interface                         
                                                                                 
Afi   Address                    IGPMetric  Valid  PathCnt  ResolvedVia                Interface
----  -------------------------  ---------  -----  -------  -------------------------  ---------
ipv4  10.10.10.2                 0          on     54       fe80::4ab0:2dff:fe08:9898  swp51    
                                                            fe80::4ab0:2dff:fed8:67cb  swp52    
      10.10.10.3                 0          on     36       fe80::4ab0:2dff:fe08:9898  swp51    
                                                            fe80::4ab0:2dff:fed8:67cb  swp52    
      10.10.10.4                 0          on     36       fe80::4ab0:2dff:fe08:9898  swp51    
                                                            fe80::4ab0:2dff:fed8:67cb  swp52    
ipv6  fe80::4ab0:2dff:fe08:9898  0          on     6        swp51                               
      fe80::4ab0:2dff:fed8:67cb  0          on     6        swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp nexthop \<afi\></h>

Shows BGP next hop information for IPv4 or IPv6 for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp nexthop ipv4
Nexthops
===========
                                                                                 
    PathCnt - Number of paths pointing to this Nexthop, ResolvedVia - Resolved via   
    address or interface, Interface - Resolved via interface                         
                                                                                 
    Address     IGPMetric  Valid  PathCnt  ResolvedVia                Interface
    ----------  ---------  -----  -------  -------------------------  ---------
    10.10.10.2  0          on     54       fe80::4ab0:2dff:fe08:9898  swp51    
                                           fe80::4ab0:2dff:fed8:67cb  swp52    
    10.10.10.3  0          on     36       fe80::4ab0:2dff:fe08:9898  swp51    
                                           fe80::4ab0:2dff:fed8:67cb  swp52    
    10.10.10.4  0          on     36       fe80::4ab0:2dff:fe08:9898  swp51    
                                           fe80::4ab0:2dff:fed8:67cb  swp52
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp nexthop \<afi\> ip-address</h>

Shows BGP IPv4 or IPv6 next hops for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp nexthop ipv4 ip-address
PathCnt - Number of paths pointing to this Nexthop, ResolvedVia - Resolved via   
address or interface, Interface - Resolved via interface                         
                                                                                 
Address     IGPMetric  Valid  PathCnt  ResolvedVia                Interface
----------  ---------  -----  -------  -------------------------  ---------
10.10.10.2  0          on     54       fe80::4ab0:2dff:fe08:9898  swp51    
                                                                  swp52    
10.10.10.3  0          on     36       fe80::4ab0:2dff:fe08:9898  swp51    
                                                                  swp52    
10.10.10.4  0          on     36       fe80::4ab0:2dff:fe08:9898  swp51    
                                                                  swp52
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp nexthop \<afi\> ip-address \<ip-address-id\></h>

Shows information about a specific BGP IPv4 or IPv6 next hop for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |
| `<ip-address-id>` |  The IPv4 or IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.2
nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.2
                  operational  applied     pending   
----------------  -----------  ----------  ----------
complete          on           on          on        
igp-metric        0            0           0         
last-update-time  1682551559   1682551559  1682551560
path-count        54           54          54        
valid             on           on          on        

resolved-via
===============
    Nexthop                    interface
    -------------------------  ---------
    fe80::4ab0:2dff:fe08:9898  swp51    
    fe80::4ab0:2dff:fed8:67cb  swp52
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp nexthop \<afi\> ip-address \<ip-address-id\> resolved-via</h>

Shows the recursive BGP IPv4 or IPv6 next hops for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |
| `<ip-address-id>` |  The IPv4 or IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.2 resolved-via
Nexthop                    interface
-------------------------  ---------
fe80::4ab0:2dff:fe08:9898  swp51    
fe80::4ab0:2dff:fed8:67cb  swp52
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp nexthop \<afi\> ip-address \<ip-address-id\> path</h>

Shows all paths associated with BGP IPv4 or IPv6 nexthops for the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |
| `<ip-address-id>` |  The IPv4 or IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.2 path -o json
{
  "1": {
    "address-family": "l2vpn-evpn",
    "flags": {
      "damped": "off",
      "deterministic-med-selected": "off",
      "history": "off",
      "multipath": "off",
      "nexthop-self": "off",
      "removed": "off",
      "selected": "off",
      "stale": "off",
      "valid": "on"
    },
    "prefix": "[5]:[0]:[10.1.20.0/24]/352",
    "rd": "10.10.10.2:3",
    "vrf": "default"
  },
  "10": {
    "address-family": "l2vpn-evpn",
    "flags": {
      "damped": "off",
      "deterministic-med-selected": "on",
      "history": "off",
      "multipath": "off",
      "nexthop-self": "off",
      "removed": "off",
      "selected": "on",
      "stale": "off",
      "valid": "on"
    },
    "prefix": "[5]:[0]:[10.1.30.0/24]/352",
    "rd": "10.10.10.2:2",
    "vrf": "default"
  },
  "11": {
    "address-family": "l2vpn-evpn",
    "flags": {
      "damped": "off",
      "deterministic-med-selected": "on",
      "history": "off",
      "multipath": "off",
      "nexthop-self": "off",
      "removed": "off",
      "selected": "on",
      "stale": "off",
      "valid": "on"
    },
    "prefix": "[5]:[0]:[10.1.20.0/24]/352",
    "rd": "10.10.10.2:3",
    "vrf": "default"
  },
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp nexthop \<afi\> ip-address \<ip-address-id\> path \<path-id\></h>

Shows information about a specific path associated with BGP IPv4 or IPv6 nexthops for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |
| `<ip-address-id>` |  The IPv4 or IPv6 address. |
| `<path-id>` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.2 path 1
                              operational                 applied                     pending                   
----------------------------  --------------------------  --------------------------  --------------------------
address-family                l2vpn-evpn                  l2vpn-evpn                  l2vpn-evpn                
prefix                        [5]:[0]:[10.1.30.0/24]/352  [5]:[0]:[10.1.30.0/24]/352  [5]:[0]:[10.1.30.0/24]/352
rd                            10.10.10.2:9                10.10.10.2:9                10.10.10.2:9              
vrf                           default                     default                     default                   
flags                                                                                                           
  damped                      off                         off                         off                       
  deterministic-med-selected  off                         off                         off                       
  history                     off                         off                         off                       
  multipath                   off                         off                         off                       
  nexthop-self                off                         off                         off                       
  removed                     off                         off                         off                       
  selected                    off                         off                         off                       
  stale                       off                         off                         off                       
  valid                       on                          on                          on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp path-selection</h>

Shows the BGP path selection configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp path-selection
                         operational  applied    pending  
-----------------------  -----------  ---------  ---------
routerid-compare                      off        off      
aspath                                                    
  compare-confed                      off        off      
  compare-lengths                     on         on       
med                                                       
  compare-always                      off        off      
  compare-confed                      off        off      
  compare-deterministic               on         on       
  missing-as-max                      off        off      
multipath                                                 
  aspath-ignore                       off        off      
  bandwidth                           all-paths  all-paths
  generate-asset                      off        off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp path-selection aspath</h>

Shows the BGP AS path path selection configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp path-selection aspath
                 operational  applied  pending
---------------  -----------  -------  -------
compare-confed                off      off    
compare-lengths               on       on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp path-selection med</h>

Shows the BGP med path selection configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp path-selection med
                       operational  applied  pending
---------------------  -----------  -------  -------
compare-always                      off      off    
compare-confed                      off      off    
compare-deterministic               on       on     
missing-as-max                      off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp path-selection multipath</h>

Shows BGP multipath path-selection configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp path-selection multipath
                operational  applied    pending  
--------------  -----------  ---------  ---------
aspath-ignore                off        off      
bandwidth                    all-paths  all-paths
generate-asset               off        off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group</h>

Shows the peer groups configured for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\></h>

Shows global configuration for the specified peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES
                               applied   
-----------------------------  ----------
description                    none      
enforce-first-as               off       
multihop-ttl                   auto      
nexthop-connected-check        on        
passive-mode                   off       
password                       none      
address-family                           
  ipv4-unicast                           
    enable                     on        
    add-path-tx                off       
    nexthop-setting            auto      
    route-reflector-client     off       
    route-server-client        off       
    soft-reconfiguration       off       
    aspath                               
      private-as               none      
      replace-peer-as          off       
      allow-my-asn                       
        enable                 off       
    attribute-mod                        
      aspath                   on        
      med                      on        
      nexthop                  on        
    weight                     0         
    community-advertise                  
      extended                 on        
      large                    off       
      regular                  on        
    conditional-advertise                
      enable                   on       
    default-route-origination            
      enable                   off       
    policy                               
      inbound                            
        route-map              myroutemap
        aspath-list            none      
        prefix-list            none      
      outbound                           
        route-map              none      
        unsuppress-map         none      
        aspath-list            none      
        prefix-list            none      
    prefix-limits                        
      inbound                            
        maximum                3000      
        warning-threshold      4         
  ipv6-unicast                           
    enable                     off       
  l2vpn-evpn                             
    enable                     on       
bfd                                      
  enable                       off       
local-as                                 
  enable                       off       
timers                                   
  connection-retry             auto      
  hold                         auto      
  keepalive                    auto      
  route-advertisement          auto      
ttl-security                             
  enable                       off       
capabilities                             
  extended-nexthop             auto      
graceful-restart                         
  mode                         auto 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd</h>

Shows BFD configuration for the specified BGP peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES bfd
        applied
------  -------
enable  on 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security</h>

Shows BGP TTL security configuration for the specified BGP peer group. BGP TTL security prevents attacks against eBGP, such as denial of service (DoS) attacks.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES ttl-security
        applied
------  -------
enable  on     
hops    3 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities</h>

Shows the capabilities for the specified BGP peer group, such as if extended next hop and 32-bit ASN transmission are enabled.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES capabilities
                  applied
----------------  -------
extended-nexthop  auto
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> graceful-restart</h>

Shows BGP graceful restart configuration for the specified peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES graceful-restart
      applied    
----  -----------
mode  helper-only
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as</h>

Shows the local AS for the specified BGP peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES local-as
        applied
------  -------
enable  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers</h>

Shows BGP timer configuration for the peer group in the specified VRF, such the conditional advertisement, connection retry,
and keepalive interval and the hold time for keepalive messages.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES timers
                     applied
-------------------  -------
connection-retry     auto   
hold                 30     
keepalive            10     
route-advertisement  auto
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family</h>

Shows configuration information for the address families (IPv4, IPv6, EVPN).

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family
                             applied   
---------------------------  ----------
ipv4-unicast                           
  enable                     on        
  add-path-tx                off       
  nexthop-setting            auto      
  route-reflector-client     off       
  route-server-client        off       
  soft-reconfiguration       off       
  aspath                               
    private-as               none      
    replace-peer-as          off       
    allow-my-asn                       
      enable                 off       
  attribute-mod                        
    aspath                   on        
    med                      on        
    nexthop                  on        
  weight                     0         
  community-advertise                  
    extended                 on        
    large                    off       
    regular                  on        
  conditional-advertise                
    enable                   off       
  default-route-origination            
    enable                   off       
  policy                               
    inbound                            
      route-map              myroutemap
      aspath-list            none      
      prefix-list            none      
    outbound                           
      route-map              none      
      unsuppress-map         none      
      aspath-list            none      
      prefix-list            none      
  prefix-limits                        
    inbound                            
      maximum                3000      
      warning-threshold      4         
ipv6-unicast                           
  enable                     off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast</h>

Shows the configuration for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast
                           applied   
-------------------------  ----------
enable                     on        
add-path-tx                off       
nexthop-setting            auto      
route-reflector-client     off       
route-server-client        off       
soft-reconfiguration       off       
aspath                               
  private-as               none      
  replace-peer-as          off       
  allow-my-asn                       
    enable                 off       
attribute-mod                        
  aspath                   on        
  med                      on        
  nexthop                  on        
weight                     0         
community-advertise                  
  extended                 on        
  large                    off       
  regular                  on        
conditional-advertise                
  enable                   off       
default-route-origination            
  enable                   off       
policy                               
  inbound                            
    route-map              myroutemap
    aspath-list            none      
    prefix-list            none      
  outbound                           
    route-map              none      
    unsuppress-map         none      
    aspath-list            none      
    prefix-list            none      
prefix-limits                        
  inbound                            
    maximum                3000      
    warning-threshold      4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise</h>

Shows community advertise configuration information for the specified BGP IPv4 peer group. The community advertise option determines if the neighbor can advertise a prefix to any iBGP or eBGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast community-advertise
          applied
--------  -------
extended  off    
large     off    
regular   off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod</h>

Shows the attribute modification configuration settings for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast attribute-mod
         applied
-------  -------
aspath   on     
med      on     
nexthop  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath</h>

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP IPv4 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath
                 applied
---------------  -------
private-as       none   
replace-peer-as  off    
allow-my-asn            
  enable         off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn</h>

Shows if it is acceptable for a received AS path from the specified BGP IPv4 peer group to contain the ASN of the local system.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath allow-my-asn
        applied
------  -------
enable  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits</h>

Shows the limits on prefixes from the specified IPv4 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits
                     applied
-------------------  -------
inbound                     
  maximum            3000   
  warning-threshold  4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound</h>

Shows the limits on inbound prefixes from the specified IPv4 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits inbound
                   applied
-----------------  -------
maximum            3000   
warning-threshold  4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast default-route-origination</h>

Shows default route origination configuration for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast default-route-origination
        applied
------  -------
enable  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy</h>

Shows the policies configured for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy
                  applied   
----------------  ----------
inbound                     
  route-map       myroutemap-in
  aspath-list     none      
  prefix-list     none      
outbound                    
  route-map       myroutemap-out      
  unsuppress-map  none      
  aspath-list     none      
  prefix-list     none 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound</h>

Shows the inbound policy for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound
             applied   
-----------  ----------
route-map    myroutemap-in
aspath-list  none      
prefix-list  non
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound</h>

Shows the outbound policy for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound
                applied
--------------  -------
route-map       myroutemap-out   
unsuppress-map  none   
aspath-list     none   
prefix-list     none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise</h>

Shows conditional advertisement configuration information for the specified BGP IPv4 peer group. The BGP conditional advertisement option lets you advertise certain routes only if other routes either do or do not exist.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise
               applied  pending    
-------------  -------  -----------
enable         off      on         
advertise-map           myadvertise
exist-map               EXIST      
non-exist-map           NONEXIST 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast</h>

Shows the configuration for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast
        applied  pending
------  -------  -------
enable  off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy</h>

Shows the policies for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy
                  applied     
----------------  ------------
inbound                       
  route-map       MAP1        
  aspath-list     none        
  prefix-list     none        
outbound                      
  route-map       none        
  unsuppress-map  none        
  aspath-list     myaspathlist
  prefix-list     none 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound</h>

Shows the inbound policy for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy inbound
             applied
-----------  -------
route-map    MAP1   
aspath-list  none   
prefix-list  none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound</h>

Shows the outbound policy for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy outbound
                applied     
--------------  ------------
route-map       none        
unsuppress-map  none        
aspath-list     myaspathlist
prefix-list     none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath</h>

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP IPv6 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast aspath
                 applied
---------------  -------
private-as       none   
replace-peer-as  off    
allow-my-asn            
  enable         on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn</h>

Shows if it is acceptable for a received AS path from the specified BGP IPv6 peer group to contain the ASN of the local system.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast aspath allow-my-asn
        applied
------  -------
enable  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits</h>

Shows the limits on prefixes from the specified IPv6 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits
                     applied
-------------------  -------
inbound                     
  maximum            none   
  warning-threshold  75
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound</h>

Shows the limits on inbound prefixes from the specified IPv6 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits inbound
                   applied
-----------------  -------
maximum            none   
warning-threshold  75
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination</h>

Shows default route origination configuration for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast default-route-origination
        applied
------  -------
enable  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise</h>

Shows community advertise configuration information for the specified BGP IPv6 peer group. The community advertise option determines if the neighbor can advertise a prefix to any iBGP or eBGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast community-advertise
          applied
--------  -------
extended  on     
large     off    
regular   on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod</h>

Shows the attribute modification configuration settings for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast attribute-mod
         applied
-------  -------
aspath   on     
med      on     
nexthop  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise</h>

Shows conditional advertisement configuration information for the specified BGP IPv6 peer group. The BGP conditional advertisement option lets you advertise certain routes only if other routes either do or do not exist.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast conditional-advertise
        applied
------  -------
enable  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn</h>

Shows configuration information for the specified BGP peer group for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn
        applied
------  -------
enable  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod</h>

Shows the attribute modification configuration settings for the specified BGP peer group for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn attribute-mod
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath</h>

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP peer group for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn</h>

Shows if it is acceptable for a received AS path from the specified BGP peer group to contain the ASN of the local system for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn aspath allow-my-asn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy</h>

Shows the EVPN policies for the specified BGP peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound</h>

Shows the inbound EVPN policy for the specified BGP peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound</h>

Shows the outbound EVPN policy for the specified BGP peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-export</h>

Shows BGP route export configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-export
                  operational  applied  pending
----------------  -----------  -------  -------
to-evpn                                        
  [route-target]               auto     auto
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-export to-evpn</h>

Shows BGP route export to EVPN configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-export to-evpn route-target 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-export to-evpn route-target</h>

Shows the RTs configured for BGP route export for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-export to-evpn route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-export to-evpn route-target \<rt-id\></h>

Shows BGP route export configuration for a specific RT in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-export to-evpn route-target 10.10.10.1:20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-import</h>

Shows BGP route import configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-import
                  operational  applied      
----------------  -----------  -------------
from-evpn                                   
  [route-target]               10.10.10.1:20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-import from-evpn</h>

Shows BGP route import from EVPN configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-import from-evpn route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-import from-evpn route-target</h>

Shows the RTs configured for BGP route import from EVPN for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-import from-evpn route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-import from-evpn route-target \<rt-id\></h>

Shows configuration for a specific RD and layer 3 RT for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<rt-id>` | The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-import from-evpn route-target 10.10.10.1:20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-reflection</h>

Shows BGP route reflection configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-reflection
        operational  applied  pending
------  -----------  -------  -------
enable               off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp timers</h>

Shows BGP timer configuration for all peers in the specified VRF, such the conditional advertisement, connection retry,
and keepalive interval and the hold time for keepalive messages.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp timers
                       operational  applied  pending
---------------------  -----------  -------  -------
conditional-advertise               60       60     
connection-retry                    10       10     
hold                                9        9      
keepalive                           3        3      
route-advertisement                 none     none
```
