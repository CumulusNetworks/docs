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
                                applied      pending    
------------------------------  -----------  -----------
enable                          on           on         
autonomous-system               65101        65101      
router-id                       10.10.10.1   10.10.10.1 
policy-update-timer             5            5          
graceful-shutdown               off          off        
wait-for-install                off          off        
graceful-restart                                        
  mode                          helper-only  helper-only
  restart-time                  120          120        
  path-selection-deferral-time  360          360        
  stale-routes-time             360          360        
convergence-wait                                        
  time                          0            0          
  establish-wait-time           0            0          
queue-limit                                             
  input                         10000        10000      
  output                        10000        10000
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
time                 0
establish-wait-time  0
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
                              operational  applied        pending      
----------------------------  -----------  -------------  -------------
enable                                     on             on           
autonomous-system                          auto           auto         
router-id                     10.10.10.1   auto           auto         
rd                                         none           none         
address-family                                                         
  ipv4-unicast                                                         
    rib-filter                             none           none         
    route-export                                                       
      to-evpn                                                          
        enable                             off            off          
    route-import                                                       
      from-vrf                                                         
        enable                             off            off          
    admin-distance                                                     
      external                             20             20           
      internal                             200            200          
    multipaths                                                         
      ebgp                                 64             64           
      ibgp                                 64             64           
      compare-cluster-length               off            off          
    enable                                 on             on           
    redistribute                                                       
      static                                                           
        enable                             off            off          
      connected                                                        
        enable                             on             on           
        metric                             auto           auto         
        route-map                          none           none
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
                            operational  applied  pending
--------------------------  -----------  -------  -------
ipv4-unicast                                             
  rib-filter                             none     none   
  route-export                                           
    to-evpn                                              
      enable                             off      off    
  route-import                                           
    from-vrf                                             
      enable                             off      off    
  admin-distance                                         
    external                             20       20     
    internal                             200      200    
  multipaths                                             
    ebgp                                 64       64     
    ibgp                                 64       64     
    compare-cluster-length               off      off    
  enable                                 on       on     
  redistribute                                           
    static                                               
      enable                             off      off    
    connected                                            
      enable                             on       on     
      metric                             auto     auto   
      route-map                          none     none   
    kernel                                               
      enable                             off      off    
    ospf                                                 
      enable                             off      off    
  [network]                                              
  [aggregate-route]                                      
ipv6-unicast                                             
  enable                                 off      off    
l2vpn-evpn                                               
  enable                                 on       on
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
                          operational  applied  pending
------------------------  -----------  -------  -------
rib-filter                             none     none   
route-export                                           
  to-evpn                                              
    enable                             off      off    
route-import                                           
  from-vrf                                             
    enable                             off      off    
admin-distance                                         
  external                             20       20     
  internal                             200      200    
multipaths                                             
  ebgp                                 64       64     
  ibgp                                 64       64     
  compare-cluster-length               off      off    
enable                                 on       on     
redistribute                                           
  static                                               
    enable                             off      off    
  connected                                            
    enable                             on       on     
    metric                             auto     auto   
    route-map                          none     none   
  kernel                                               
    enable                             off      off    
  ospf                                                 
    enable                             off      off    
[network]                                              
[aggregate-route]
...
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
              applied      pending  
------------  -----------  ---------
as-set        on          on       
route-map                 routemap1
summary-only  on          on 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib</h>

Shows the IPv4 local RIB for the specified VRF.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route` command instead.
{{%/notice%}}

nv show vrf <vrf-id> router bgp address-family <afi>> route

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
    PathCount - Number of paths present for the prefix, MultipathCount - Number of paths that are part of the ECMP, DestFlags - * - bestpath-exists, w - fib-wait-  for-install, s - fib-suppress, i - fib-installed, x - fib-install-failed, LocalPref - Local Preference, Best - Best path, Reason - Reason for selection                                                
                                                                                
    Prefix           PathCount  MultipathCount  DestFlags        Nexthop  Metric  Weight  LocalPref  Aspath  Best  Reason  Flags
    ---------------  ---------  --------------  ---------------  -------  ------  ------  ---------  ------  ----  ------  -----
    10.0.1.12/32     3          1               bestpath-exists                                                                 
    10.0.1.34/32     5          4               bestpath-exists                                                                 
    10.0.1.255/32    5          4               bestpath-exists                                                                 
    10.10.10.1/32    1          1               bestpath-exists                                                                 
    10.10.10.2/32    5          1               bestpath-exists                                                                 
    10.10.10.3/32    5          4               bestpath-exists                                                                 
    10.10.10.4/32    5          4               bestpath-exists                                                                 
    10.10.10.63/32   5          4               bestpath-exists                                                                 
    10.10.10.64/32   5          4               bestpath-exists                                                                 
    10.10.10.101/32  2          1               bestpath-exists                                                                 
    10.10.10.102/32  2          1               bestpath-exists                                                                 
    10.10.10.103/32  2          1               bestpath-exists                                                                 
    10.10.10.104/32  2          1               bestpath-exists
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route</h>

Shows information about the IPv4 routes in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route` command instead.
{{%/notice%}}

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

Shows information about the specified IPv4 route in the local RIB, such as the BGP neighbor to which the path is advertised and the path count.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
{{%/notice%}}

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
multipath-count  1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path</h>

Shows information about the paths for the specified IPv4 route in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
{{%/notice%}}

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
      "65002": {} 
    }, 
    "bestpath": { 
      "from-as": 65002, 
      "overall": "yes", 
      "selection-reason": "First path received" 
    }, 
    "flags": { 
      "bestpath": {}, 
      "valid": {} 
    }, 
    "flags-string": "*v", 
    "last-update": "2024-08-05T03:51:08Z", 
    "metric": 0, 
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
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
{{%/notice%}}

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

  "1": { 
    "aspath": { 
      "65002": {} 
    }, 
    "bestpath": { 
      "from-as": 65002, 
      "overall": "yes", 
      "selection-reason": "First path received" 
    }, 
    "flags": { 
      "bestpath": {}, 
      "valid": {} 
    }, 
    "flags-string": "*v", 
    "last-update": "2024-08-05T03:51:08Z", 
    "metric": 0, 
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

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> aspath</h>

Shows the AS paths for the specified IPv4 route in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
{{%/notice%}}

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

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> bestpath</h>

Shows best path information, such as the selection reason, for the specified IPv4 route in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
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
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 bestpath
                  operational  applied
----------------  -----------  -------
from-as           65199               
overall           on                  
selection-reason  Older Path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> community</h>

Shows the community names for the community list for the specified IPv4 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
{{%/notice%}}

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

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> ext-community</h>

Shows the community names for the extended community list for the specified IPv4 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
{{%/notice%}}

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

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> flags</h>

Shows route path flags for the specified IPv4 route in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
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
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 flags
operational  applied
-----------  -------
multipath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> large-community</h>

Shows the community names for the large community list for the specified IPv4 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
{{%/notice%}}

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

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> nexthop</h>

Shows information about the nexthops for the specified IPv4 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
{{%/notice%}}

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

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
{{%/notice%}}

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
ip          fe80::202:ff:fe00:26
afi         ipv6             
scope       global           
accessible  on
metric      0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> peer</h>

Shows BGP neighbor information for the specified IPv4 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>` command instead.
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
No Data
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
             applied  pending
-----------  -------  -------
static                       
  enable     off      off    
connected                    
  enable     on       on     
  metric     auto     auto   
  route-map  none     none   
kernel                       
  enable     off      off    
ospf                         
  enable     off      off
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
           applied  pending
---------  -------  -------
enable     on       on     
metric     auto     auto   
route-map  none     none
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
        applied  pending
------  -------  -------
enable  off      off
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
        applied  pending
------  -------  -------
enable  off      off
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
        applied  pending
------  -------  -------
enable  off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route</h>

Shows the BGP IPv4 routing table.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast route
PathCount - Number of paths present for the prefix, MultipathCount - Number of
paths that are part of the ECMP, DestFlags - * - bestpath-exists, w - fib-wait-
for-install, s - fib-suppress, i - fib-installed, x - fib-install-failed

Prefix           PathCount  MultipathCount  DestFlags
---------------  ---------  --------------  ---------
10.0.1.12/32     2          1               *
10.0.1.34/32     5          4               *
10.0.1.255/32    5          4               *
10.10.10.1/32    1          1               *
10.10.10.2/32    5          1               *
10.10.10.3/32    5          4               *
10.10.10.4/32    5          4               *
10.10.10.63/32   5          4               *
10.10.10.64/32   5          4               *
10.10.10.101/32  2          1               *
10.10.10.102/32  2          1               *
10.10.10.103/32  2          1               *
10.10.10.104/32  2          1               *
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route \<route-id\></h>

Shows information about the BGP IPv4 route.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv4 address and route prefix in CIDR notation.  |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast route 10.10.10.3/32
                 operational
---------------  -----------
path-count       5
multipath-count  4

path
=======

    Origin - Route origin, Local - Locally originated route, Sourced - Sourced
    route, Weight - Route weight, Metric - Route metric, LocalPref - Route local
    preference, PathFrom - Route path origin, LastUpdate - Route last update,
    NexthopCnt - Number of nexthops, Flags - = - multipath, * - bestpath, v - valid,
    s - suppressed, R - removed, S - stale

    Path  Origin      Local  Sourced  Weight  Metric  LocalPref  PathFrom  LastUpdate            NexthopCnt  Flags
    ----  ----------  -----  -------  ------  ------  ---------  --------  --------------------  ----------  -----
    1     incomplete                                             external  2024-11-23T12:58:55Z  2           =*v
    2     incomplete                                             external  2024-11-23T12:59:04Z  2           =v
    3     incomplete                                             external  2024-11-23T12:58:55Z  2           =v
    4     incomplete                                             external  2024-11-23T12:59:03Z  2           =v
    5     incomplete                                             external  2024-11-23T12:59:03Z  2           *v

advertised-to
================
    Neighbor       hostname
    -------------  --------
    peerlink.4094  leaf02
    swp51          spine01
    swp52          spine02
    swp53          spine03
    swp54          spine04
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-count</h>

Shows the BGP IPv4 route and path count.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast route-count
              operational  applied
------------  -----------  -------
total-routes  13           13
total-paths   46           46
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
to-vrf                                       
  [list]        none                         
[route-target]  none                         
rd              none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn</h>

Shows configuration for IPv4 prefix-based routing using EVPN type-5 routes. Type-5 routes (or prefix routes) primarily route to destinations outside of the data center fabric. EVPN prefix routes carry the layer 3 VNI and router MAC address and follow the symmetric routing model to route to the destination prefix.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast route-export to-evpn
route-export to-evpn
        operational  applied
------  -----------  -------
enable               off
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
----
none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast soo-route</h>

Shows the BGP Site-of-Origin routes.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast soo-route
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast soo-route \<ip-address\></h>

Shows information about the specific BGP Site-of-Origin route.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<ip-address>` | The IP address. |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast soo-route 10.10.10.5
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

 RouteMap - Outbound route map, MinAdvInterval - Minimum route advertisement      
interval, CreationTime - Time when the update group was created, LocalAsChange - 
LocalAs changes for inbound route, Flags - r - replace-as, x - no-prepend

UpdateGrp  RouteMap  MinAdvInterval  CreationTime          LocalAsChange  Flags 
---------  --------  --------------  --------------------  -------------  ----- 
1                    1               2024-08-05T03:51:08Z
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast update-group \<group-id\></h>

Shows information about a specific BGP IPv4 update group in the specified VRF.

{{%notice note%}}
In Cumulus Linux 5.10 and earlier, add `-o json` at the end of the command to see the output in a more readable format.
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
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast update-group 1
                                  operational         
--------------------------------  --------------------
update-group-id                   1                   
min-route-advertisement-interval  0                   
create-time                       2024-11-15T10:01:47Z

sub-group
============
                                                                                
    CreateTime - Time when the sub group was created, AdvRouteCnt - Number of routes
    advertised to peer, Refresh - Indicates if subgroup requires refresh,           
    TotalQueuePkt - Total packets in queue, TotalEnqueuePkt - Total packets         
    enqueued, PktQueueLength - Packet queue length, Neighbor - Sub group peer info  
                                                                                
    GrpID  CreateTime            AdvRouteCnt  Refresh  TotalQueuePkt  TotalEnqueuePkt  PktQueueLength  Neighbor     
    -----  --------------------  -----------  -------  -------------  ---------------  --------------  -------------
    1      2024-11-15T10:01:47Z  13           off      31             31               0               peerlink.4094
                                                                                                       swp52        
                                                                                                       swp53        
                                                                                                       swp54
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast update-group \<group-id\> sub-group</h>

Shows the subgroups for a specific BGP IPv4 update group in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<group-id>` | The group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv4-unicast update-group 1 sub-group 
                                                                                
CreateTime - Time when the sub group was created, AdvRouteCnt - Number of routes
advertised to peer, Refresh - Indicates if subgroup requires refresh,           
TotalQueuePkt - Total packets in queue, TotalEnqueuePkt - Total packets         
enqueued, PktQueueLength - Packet queue length, Neighbor - Sub group peer info  
                                                                                
GrpID  CreateTime            AdvRouteCnt  Refresh  TotalQueuePkt  TotalEnqueuePkt  PktQueueLength  Neighbor     
-----  --------------------  -----------  -------  -------------  ---------------  --------------  -------------
1      2024-11-15T10:01:47Z  13           off      31             31               0               peerlink.4094
                                                                                                   swp52        
                                                                                                   swp53        
                                                                                                   swp54
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp confederation</h>

Shows BGP confederation configuration. To reduce the number of iBGP peerings, configure a confederation to divide an AS into a smaller sub-AS.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp confederation
             operational  applied    
-----------  -----------  -----------
id                        2          
[member-as]               65101-65104   
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp confederation member-as</h>

Shows the BGP confederation member AS. A BGP confederation divides a large AS into subautonomous systems, which are uniquely identified by a sub-AS number.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp confederation member-as
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp dynamic-neighbor</h>

Shows BGP dynamic neighbor configuration on the switch. BGP dynamic neighbors provide BGP peering to remote neighbors within a specified range of IPv4 or IPv6 addresses for a BGP peer group. You can configure each range as a subnet IP address.

After you configure the dynamic neighbors, a BGP speaker can listen for, and form peer relationships with, any neighbor that is in the IP address range and maps to a peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

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

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp dynamic-neighbor listen-range
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp dynamic-neighbor listen-range \<ip-sub-prefix-id\></h>

Shows information about a specific address range for BGP peering to remote neighbors.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<ip-sub-prefix-id>` | The address range. |

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

## <h>nv show vrf \<vrf-id\> router bgp neighbor</h>

Shows information about all BGP neighbors.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor
AS - Remote Autonomous System, PeerEstablishedTime - Peer established time in
UTC format, UpTime - Uptime in milliseconds, Afi-Safi - Address family, PfxSent
- Transmitted prefix counter, PfxRcvd - Recieved prefix counter

Neighbor       AS     State        PeerEstablishedTime   UpTime   MsgRcvd  MsgSent Afi-Safi      PfxSent  PfxRcvd
-------------  -----  -----------  --------------------  -------  -------  ------- ------------  -------  -------
peerlink.4094  65102  established  2024-11-23T12:58:56Z  2136000  800      787 ipv4-unicast  13       12
 l2vpn-evpn    63       45
swp51          65199  established  2024-11-23T12:58:54Z  2136000  803      786 ipv4-unicast  13       8
 l2vpn-evpn    63       45
swp52          65199  established  2024-11-23T12:59:02Z  2136000  797      782 ipv4-unicast  13       8
 l2vpn-evpn    63       45
swp53          65199  established  2024-11-23T12:58:54Z  2136000  803      786 ipv4-unicast  13       8
 l2vpn-evpn    63       45
swp54          65199  established  2024-11-23T12:59:01Z  2136000  797      783 ipv4-unicast  13       8
 l2vpn-evpn    63       45
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\></h>

Shows global configuration and statistics for the specified BGP neighbor.

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
                               operational                applied                                
-----------------------------  -------------------------  ---------------------------------------
password                                                  $nvsec$d1a028e8c7f97db92876c2a30fcc403f
enforce-first-as                                          off                                    
passive-mode                                              off                                    
nexthop-connected-check                                   on                                     
description                                               none                                   
bfd                                                                                              
  enable                                                  off                                    
ttl-security                                                                                     
  enable                       on                         off                                    
  hops                         1                                                                 
local-as                                                                                         
  enable                                                  off                                    
timers                                                                                           
  keepalive                    3                          auto                                   
  hold                         9                          auto                                   
  connection-retry             10                         auto                                   
  route-advertisement          none                       auto                                   
address-family                                                                                   
  ipv4-unicast                                                                                   
    enable                                                on                                     
    route-reflector-client                                off                                    
    soft-reconfiguration                                  off                                    
    nexthop-setting                                       auto                                   
    add-path-tx                                           off                                    
    attribute-mod                                                                                
      aspath                   off                        on                                     
      med                      off                        on                                     
      nexthop                  off                        on                                     
    aspath                                                                                       
      replace-peer-as                                     off                                    
      private-as                                          none                                   
      allow-my-asn                                                                               
        enable                                            off                                    
    graceful-restart                                                                             
      rx-eof-rib               off                                                               
      tx-eof-rib               off                                                               
    weight                                                0                                      
    community-advertise                                                                          
      regular                  on                         on                                     
      extended                 on                         on                                     
      large                    off                        off                                    
    conditional-advertise                                                                        
      enable                                              off                                    
    policy                                                                                       
      inbound                                                                                    
        route-map                                         none                                   
        prefix-list                                       none                                   
        aspath-list                                       none
...
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
                             operational  applied
---------------------------  -----------  -------
ipv4-unicast                                     
  enable                                  on     
  route-reflector-client                  off    
  soft-reconfiguration                    off    
  nexthop-setting                         auto   
  add-path-tx                             off    
  attribute-mod                                  
    aspath                   off          on     
    med                      off          on     
    nexthop                  off          on     
  aspath                                         
    replace-peer-as                       off    
    private-as                            none   
    allow-my-asn                                 
      enable                              off    
  graceful-restart                               
    rx-eof-rib               off                 
    tx-eof-rib               off                 
  weight                                  0      
  community-advertise                            
    regular                  on           on     
    extended                 on           on     
    large                    off          off    
  conditional-advertise                          
    enable                                off
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
                           operational  applied
-------------------------  -----------  -------
enable                                  on     
route-reflector-client                  off    
route-server-client                     off    
soft-reconfiguration                    off    
nexthop-setting                         auto   
add-path-tx                             off    
attribute-mod                                  
  aspath                   off          on     
  med                      off          on     
  nexthop                  off          on     
aspath                                         
  replace-peer-as                       off    
  private-as                            none   
  allow-my-asn                                 
    enable                              off    
graceful-restart                               
  rx-eof-rib               off                 
  tx-eof-rib               off                 
weight                                  0
...
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes</h>

Shows information about the IPv4 advertised routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes
PathCount - Number of paths present for the prefix, MultipathCount - Number of  
paths that are part of the ECMP                                                 
                                                                                
IPv4 Prefix      PathCount  MultipathCount  DestFlags      
---------------  ---------  --------------  ---------------
10.0.1.12/32     2          1               bestpath-exists
10.0.1.34/32     5          4               bestpath-exists
10.0.1.255/32    5          4               bestpath-exists
10.10.10.1/32    1          1               bestpath-exists
10.10.10.2/32    5          1               bestpath-exists
10.10.10.3/32    5          4               bestpath-exists
10.10.10.4/32    5          4               bestpath-exists
10.10.10.63/32   5          4               bestpath-exists
10.10.10.64/32   5          4               bestpath-exists
10.10.10.101/32  2          1               bestpath-exists
10.10.10.102/32  2          1               bestpath-exists
10.10.10.103/32  2          1               bestpath-exists
10.10.10.104/32  2          1               bestpath-exists
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\></h>

Shows information about a specific IPv4 advertised route for a BGP neighbor in the specified VRF.

{{%notice note%}}
In Cumulus Linux 5.10 and earlier, add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 advertised route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp52 address-family ipv4-unicast advertised-routes 10.10.10.3/32
                 operational
---------------  -----------
path-count       4          
multipath-count  3          

path
=======
                                                                                
    Origin - Route origin, Local - Locally originated route, Sourced - Sourced      
    route, Weight - Route weight, Metric - Route metric, LocalPref - Route local    
    preference, PathFrom - Route path origin, LastUpdate - Route last update,       
    NexthopCnt - Number of nexthops, Flags - = - multipath, * - bestpath, v - valid,
    s - suppressed, R - removed, S - stale                                          
                                                                                
    Path  Origin      Local  Sourced  Weight  Metric  LocalPref  PathFrom  LastUpdate            NexthopCnt  Flags
    ----  ----------  -----  -------  ------  ------  ---------  --------  --------------------  ----------  -----
    1     incomplete                                             external  2024-11-15T10:03:31Z  2           =*v  
    2     incomplete                                             external  2024-11-15T10:03:26Z  2           =v   
    3     incomplete                                             external  2024-11-15T10:03:26Z  2           =v   
    4     incomplete                                             external  2024-11-15T10:03:23Z  2           *v
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path</h>

Shows path information about a specific IPv4 advertised route for a BGP neighbor in the specified VRF.

{{%notice note%}}
In Cumulus Linux 5.10 and earlier, add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 advertised route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp52 address-family ipv4-unicast advertised-routes 10.10.10.3/32 path
                                                                                
Origin - Route origin, Local - Locally originated route, Sourced - Sourced      
route, Weight - Route weight, Metric - Route metric, LocalPref - Route local    
preference, PathFrom - Route path origin, LastUpdate - Route last update,       
NexthopCnt - Number of nexthops, Flags - = - multipath, * - bestpath, v - valid,
s - suppressed, R - removed, S - stale                                          
                                                                                
Path  Origin      Local  Sourced  Weight  Metric  LocalPref  PathFrom  LastUpdate            NexthopCnt  Flags
----  ----------  -----  -------  ------  ------  ---------  --------  --------------------  ----------  -----
1     incomplete                                             external  2024-11-15T10:03:31Z  2           =*v  
2     incomplete                                             external  2024-11-15T10:03:26Z  2           =v   
3     incomplete                                             external  2024-11-15T10:03:26Z  2           =v   
4     incomplete                                             external  2024-11-15T10:03:23Z  2           *v
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\></h>

Shows information about a specific IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

{{%notice note%}}
In Cumulus Linux 5.10 and earlier, add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp52 address-family ipv4-unicast advertised-routes 10.10.10.3/32 path 1
                    operational             
------------------  ------------------------
origin              incomplete              
valid               on                      
path-from           external                
last-update         2024-11-15T10:03:31Z    
nexthop-count       2                       
flags-string        =*v                     
peer                                        
  id                fe80::4ab0:2dff:fe5e:6ad
  router-id         10.10.10.102            
  hostname          spine02                 
  interface         swp52                   
  type              external                
bestpath                                    
  from-as           65199                   
  overall           yes                     
  selection-reason  AS Path                 

nexthop
==========
    Nexthop  accessible  afi   ip                        metric  scope       used
    -------  ----------  ----  ------------------------  ------  ----------  ----
    1        on          ipv6  fe80::4ab0:2dff:fe5e:6ad  0       global          
    2        on          ipv6  fe80::4ab0:2dff:fe5e:6ad          link-local  on  

aspath
=========
    Aspath
    ------
    65103 
    65199 

community
============
No Data

ext-community
================
No Data

large-community
==================
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> aspath</h>

Shows information about the AS path for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp52 address-family ipv4-unicast advertised-routes 10.10.10.3/32 path 1 aspath 
Aspath
------
65103 
65199
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> bestpath</h>

Shows information about the bestpath for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp52 address-family ipv4-unicast advertised-routes 10.10.10.3/32 path 1 bestpath 
                  operational
----------------  -----------
from-as           65199      
overall           yes        
selection-reason  AS Path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> community</h>

Shows information about the communities for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.101/32 path 1 community
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> ext-community</h>

Shows information about the extended communities for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 ext-community
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> flags</h>

Shows information about the flags for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp52 address-family ipv4-unicast advertised-routes 10.10.10.3/32 path 1 flags 
operational
-----------
multipath  
bestpath   
valid
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> large-community</h>

Shows information about the large communities for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 large-community
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> nexthop</h>

Shows information about the next hops for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

{{%notice note%}}
In Cumulus Linux 5.10 and earlier, add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp52 address-family ipv4-unicast advertised-routes 10.10.10.3/32 path 1 nexthop
Nexthop  accessible  afi   ip                        metric  scope       used
-------  ----------  ----  ------------------------  ------  ----------  ----
1        on          ipv6  fe80::4ab0:2dff:fe5e:6ad  0       global          
2        on          ipv6  fe80::4ab0:2dff:fe5e:6ad          link-local  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> nexthop \<nexthop-id\></h>

Shows information about a specific next hop for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |
| `<nexthop-id>` |   The nexthop ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp52 address-family ipv4-unicast advertised-routes 10.10.10.3/32 path 1 nexthop 1
            operational             
----------  ------------------------
ip          fe80::4ab0:2dff:fe5e:6ad
afi         ipv6                    
scope       global                  
accessible  on                      
metric      0 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> peer</h>

Shows information about the peers for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp52 address-family ipv4-unicast advertised-routes 10.10.10.3/32 path 1 peer
           operational             
---------  ------------------------
id         fe80::4ab0:2dff:fe5e:6ad
router-id  10.10.10.102            
hostname   spine02                 
interface  swp52                   
type       external 
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
                 applied
---------------  -------
replace-peer-as  off    
private-as       none   
allow-my-asn            
  enable         off
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
        applied
------  -------
enable  off
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
          operational  applied
-------  -----------  -------
aspath   off          on     
med      off          on     
nexthop  off          on
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
No Data
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
          operational  applied
--------  -----------  -------
regular   on           on     
extended  on           on     
large     off          off
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
        operational  applied
------  -----------  -------
enable               off
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
        operational  applied
------  -----------  -------
enable               off
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
            operational
----------  -----------
rx-eof-rib  on                           
tx-eof-rib  on
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart timers</h>

Shows the BGP graceful restart selection deferral and stale path timer settings for the BGP neighbor.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast graceful-restart timers
             operational
-----------  -----------
stale-path              
  timer-sec  360
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart timers selection-deferral</h>

Shows the BGP graceful restart  selection deferral timers for the BGP neighbor.

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast graceful-restart timers selection-deferral
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart timers stale-path</h>

Shows the BGP graceful restart stale path timer settings for the BGP neighbor.

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast graceful-restart timers stale-path
           operational
---------  -----------
timer-sec  360
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
                  operational  applied
----------------  -----------  -------
inbound                               
  route-map                    none   
  prefix-list                  none   
  aspath-list                  none   
outbound                              
  route-map                    none   
  unsuppress-map               none   
  prefix-list                  none   
  aspath-list                  none
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
             operational  applied
-----------  -----------  -------
route-map                 none   
prefix-list               none   
aspath-list               none
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
                operational  applied
--------------  -----------  -------
route-map                    none   
unsuppress-map               none   
prefix-list                  none   
aspath-list                  none
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
                     operational  applied
-------------------  -----------  -------
inbound                                  
  maximum                         none   
  warning-threshold               75     
  warning-only       off
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
                   operational  applied
-----------------  -----------  -------
maximum                         none   
warning-threshold               75     
warning-only       off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes</h>

Shows information about the IPv4 received routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\></h>

Shows information about a specific IPv4 received route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path</h>

Shows information about a specific IPv4 received route path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
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
| `<neighbor-id>` |   The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> aspath</h>

Shows information about the AS paths for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> bestpath</h>

Shows information about the best paths for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 bestpath -o json
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> community</h>

Shows information about the communities for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> ext-community</h>

Shows information about the extended communities for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 ext-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> flags</h>

Shows information about flags for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 flags 
operational
-----------
multipath
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> large-community</h>

Shows information about the large communities for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> nexthop</h>

Shows information about the next hops for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 nexthop
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> nexthop \<nexthop-id\></h>

Shows information about a specific next hop for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |
| `<nexthop-id>` |   The nexthop ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 nexthop 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> peer</h>

Shows information about peers for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 peer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast route-counters</h>

Shows the number of IPv4 routes for a specific BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast route-counters
                operational
--------------  -----------
route-count     8          
adj-rib-in      0          
damped          0          
removed         0          
history         0          
stale           0          
valid           8          
all-rib         8          
routes-counted  8          
best-routes     3          
usable          8
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

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 bfd
        applied
------  -------
enable  off
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
                  operational  applied
----------------  -----------  -------
extended-nexthop               auto
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
  operational
  -----------
  inbound                      
  outbound                     
  inbound                      
  outbound
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
                 operational    applied
---------------  -------------  -------
remote-mode      NotApplicable         
rx-restart-time  120                   
mode                            auto
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
        applied
------  -------
enable  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> message-stats</h>

Shows message statistics for the BGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 message-stats 
                   operational
------------------  -----------
input-queue         0
output-queue        0
rx-opens            1
tx-opens            1
rx-keepalives       848
tx-keepalives       848
rx-route-refreshes  0
tx-route-refreshes  0
tx-total            916
rx-total            933
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
             operational               
-----------  -------------------------
ipv4         10.10.10.1                                 
ipv6-global  fe80::4ab0:2dff:fed1:9b88                  
ipv6-local   fe80::4ab0:2dff:fed1:9b88
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers</h>

Shows timer configuration for the specified BGP neighbor, such as the reconnect, advertisement and keepalive intervals, and the hold time.

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
        operational  applied
------  -----------  -------
enable  on           off    
hops    1 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp nexthop</h>

Shows BGP next hop information for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

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
                  operational              
----------------  -------------------------
valid             yes                      
complete          on                       
igp-metric        0                        
path-count        15                       
last-update-time  2024-11-14T08:58:31Z     
[resolved-via]    fe80::4ab0:2dff:fe5e:b1fc      
...
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
      "deterministic-med-selected": "on",
      "history": "off",
      "multipath": "off",
      "nexthop-self": "off",
      "removed": "off",
      "selected": "off",
      "stale": "off",
      "valid": "on"
    },
    "flags-string": "vd",
    "prefix": "[5]:[0]:[24]:[10.1.20.0]",
    "rd": "10.10.10.2:3",
    "vrf": "default"
  },
  "2": {
    "address-family": "l2vpn-evpn",
    "flags": {
      "damped": "off",
      "deterministic-med-selected": "on",
      "history": "off",
      "multipath": "off",
      "nexthop-self": "off",
      "removed": "off",
      "selected": "off",
      "stale": "off",
      "valid": "on"
    },
    "flags-string": "vd",
    "prefix": "[5]:[0]:[24]:[10.1.10.0]",
    "rd": "10.10.10.2:3",
    "vrf": "default"
  },
  "3": {
    "address-family": "l2vpn-evpn",
    "flags": {
      "damped": "off",
      "deterministic-med-selected": "on",
      "history": "off",
      "multipath": "off",
      "nexthop-self": "off",
      "removed": "off",
      "selected": "off",
      "stale": "off",
      "valid": "on"
    },
    "flags-string": "vd",
    "prefix": "[5]:[0]:[24]:[10.1.30.0]",
    "rd": "10.10.10.2:2",
    "vrf": "default"
  },
  "4": {
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
    "flags-string": "v",
    "prefix": "[5]:[0]:[24]:[10.1.20.0]",
    "rd": "10.10.10.2:3",
    "vrf": "default"
  }
...
}
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
                              operational             
----------------------------  ------------------------
address-family                l2vpn-evpn              
prefix                        [5]:[0]:[24]:[10.1.20.0]
rd                            10.10.10.2:3            
vrf                           default                 
flags-string                  vd                      
flags                                                 
  damped                      off                     
  history                     off                     
  selected                    off                     
  valid                       on                      
  deterministic-med-selected  on                      
  stale                       off                     
  removed                     off                     
  multipath                   off                     
  nexthop-self                off
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
                         applied  
-----------------------  ---------
routerid-compare         off      
aspath                            
  compare-lengths        on       
  compare-confed         off      
med                               
  compare-always         off      
  compare-deterministic  on       
  compare-confed         off      
  missing-as-max         off      
multipath                         
  aspath-ignore          off      
  generate-asset         off      
  bandwidth              all-paths
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp path-selection aspath</h>

Shows the BGP AS path selection configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp path-selection aspath
                 applied
---------------  -------
compare-lengths  on     
compare-confed   off 
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
                       applied
---------------------  -------
compare-always         off    
compare-deterministic  on     
compare-confed         off    
missing-as-max         off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp path-selection multipath</h>

Shows BGP multipath path selection configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp path-selection multipath
                applied  
--------------  ---------
aspath-ignore   off      
generate-asset  off      
bandwidth       all-paths
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
RemoteAs - Remote Autonomous System, Afi-Safi - Address family
                                                              
Name      RemoteAs  Type      Afi-Safi  MemberCount
--------  --------  --------  --------  -----------
underlay            external            5
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
cumulus@switch:~$ nv show vrf default router bgp peer-group underlay
password                                    $nvsec$d1a028e8c7f97db92876c2a30fcc403f
enforce-first-as                            off                                    
passive-mode                                off                                    
nexthop-connected-check                     on                                     
description                                 none                                   
bfd                                                                                
  enable                                    off                                    
ttl-security                                                                       
  enable                                    off                                    
local-as                                                                           
  enable                                    off                                    
timers                                                                             
  keepalive                                 auto                                   
  hold                                      auto                                   
  connection-retry                          auto                                   
  route-advertisement                       auto                                   
address-family                                                                     
  ipv4-unicast                                                                     
    enable                                  on                                     
    route-reflector-client                  off                                    
    soft-reconfiguration                    off                                    
    nexthop-setting                         auto                                   
    add-path-tx                             off                                    
    attribute-mod                                                                  
      aspath                                on                                     
      med                                   on                                     
      nexthop                               on                                     
    aspath                                                                         
      replace-peer-as                       off                                    
      private-as                            none                                   
      allow-my-asn                                                                 
        enable                              off
...
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
                             operational  applied
---------------------------  -----------  -------
ipv4-unicast                                     
  enable                                  on     
  route-reflector-client                  off    
  soft-reconfiguration                    off    
  nexthop-setting                         auto   
  add-path-tx                             off    
  attribute-mod                                  
    aspath                                on     
    med                                   on     
    nexthop                               on     
  aspath                                         
    replace-peer-as                       off    
    private-as                            none   
    allow-my-asn                                 
      enable                              off    
  weight                                  0      
  community-advertise                            
    regular                               on     
    extended                              on     
    large                                 off    
  conditional-advertise                          
    enable                                off    
  policy                                         
    inbound                                      
      route-map                           none   
      prefix-list                         none   
      aspath-list                         none
...
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
                           operational  applied
-------------------------  -----------  -------
enable                                  on     
route-reflector-client                  off    
route-server-client                     off    
soft-reconfiguration                    off    
nexthop-setting                         auto   
add-path-tx                             off    
attribute-mod                                  
  aspath                                on     
  med                                   on     
  nexthop                               on     
aspath                                         
  replace-peer-as                       off    
  private-as                            none   
  allow-my-asn                                 
    enable                              off    
weight                                  0      
community-advertise                            
  regular                               on     
  extended                              on     
  large                                 off    
conditional-advertise                          
  enable                                off    
policy                                         
  inbound                                      
    route-map                           none   
    prefix-list                         none   
    aspath-list                         none   
  outbound                                     
    route-map                           none   
    unsuppress-map                      none   
    prefix-list                         none   
    aspath-list                         none
...
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
                 operational  applied
---------------  -----------  -------
replace-peer-as               off    
private-as                    none   
allow-my-asn                         
  enable                      off
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
        operational  applied
------  -----------  -------
enable               off
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
         operational  applied
-------  -----------  -------
aspath                on     
med                   on     
nexthop               on
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
          operational  applied
--------  -----------  -------
regular                on     
extended               on     
large                  off
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
                     operational  applied
-------------------  -----------  -------
inbound                                  
  maximum                         none   
  warning-threshold               75
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
                   operational  applied
-----------------  -----------  -------
maximum                         none   
warning-threshold               75
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

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES bfd
        operational  applied
------  -----------  -------
enable               off
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
                  operational  applied
----------------  -----------  -------
extended-nexthop               auto
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
        operational  applied
------  -----------  -------
enable               off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers</h>

Shows BGP timer configuration for the peer group in the specified VRF, such as the conditional advertisement, connection retry,
and keepalive interval, and the hold time for keepalive messages.

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
                     operational  applied
-------------------  -----------  -------
keepalive                         auto   
hold                              auto   
connection-retry                  auto   
route-advertisement               auto
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

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-export to-evpn
                operational  applied
--------------  -----------  -------
[route-target]               auto
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
cumulus@switch:~$ nv show vrf default router bgp route-import from-evpn
                operational  applied
--------------  -----------  -------
[route-target]               auto
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

Shows BGP timer configuration for all peers in the specified VRF, such as the conditional advertisement, connection retry,
and keepalive interval, and the hold time for keepalive messages.

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
