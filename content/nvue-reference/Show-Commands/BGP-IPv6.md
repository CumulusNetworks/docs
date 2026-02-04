---
title: BGP IPv6
author: Cumulus Networks
weight: 132
type: nojsscroll

---
<style>
h { color: RGB(118,185,0)}
</style>

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
        operational  applied  pending
------  -----------  -------  -------
enable               off      off 
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

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route</h>

Shows BGP IPv6 aggregate routes for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

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

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast conditional-disaggregation</h>

Shows BGP conditional disaggregation configuration.

BGP conditional disaggregation advertises specific prefixes when a failure is detected, while continuing to advertise the aggregate route. Combined with anycast Site-of-Origin (SOO) matching, this triggers peer plane leafs to conditionally originate specific routes to draw traffic instead of using the aggregate route that might lead to an unreachable destination.

To use BGP conditional disaggregation, you must also:
- Configure BGP PIC (`nv set vrf <vrf-id> router bgp address-family ipv4-unicast advertise-origin` or `nv set vrf <vrf-id> router bgp address-family ipv6-unicast advertise-origin` and `nv set vrf <vrf-id> router bgp address-family ipv4-unicast nhg-per-origin` or `nv set vrf <vrf-id> router bgp address-family ipv6-unicast nhg-per-origin`).
- Configure BGP PIC anycast (`nv set vrf <vrf-id> router bgp soo-source`).
- For 802.1X: Enable the `preserve-on-link-down` option with the `nv set system dot1x ipv6-profile <profile-id> preserve-on-link-down enabled` command to preserve IPv6 addresses when the switch reboots or a link flaps.
- Enable BGP unreachability (failure signaling) globally and on relevant peers or peer groups (`nv set vrf <vrf-id> router bgp address-family ipv4-unreachability state enabled` or `nv set vrf <vrf-id> router bgp address-family ipv6-unreachability state enabled`).
- Define the aggregate prefix and the included interfaces for which to conditionally advertise unreachability (`nv set vrf <vrf-id> router bgp address-family ipv4-unreachability advertise-unreach interfaces-match` or `nv set vrf <vrf-id> router bgp address-family ipv6-unreachability advertise-unreach interfaces-match`).

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast conditional-disaggregation
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib</h>

Shows the IPv6 local RIB for the specified VRF.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route` command instead.
{{%/notice%}}

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
    PathCount - Number of paths present for the prefix, MultipathCount - Number of   
    paths that are part of the ECMP, DestFlags - * - bestpath-exists, w - fib-wait-  
    for-install, s - fib-suppress, i - fib-installed, x - fib-install-failed,        
    LocalPref - Local Preference, Best - Best path, Reason - Reason for selection    
                                                                            
    Prefix         PathCount  MultipathCount  DestFlags  Nexthop  Metric  Weight  LocalPref  Aspath  Best  Reason  Flags 
    -------------  ---------  --------------  ---------  -------  ------  ------  ---------  ------  ----  ------  ----- 
    2001:db8::/64  2          1               *                             
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\></h>

Shows information about the specified IPv6 route in the local RIB, such as the BGP neighbor to which the path is advertised and the path count.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
{{%/notice%}}

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
            operational
----------  -----------
[path]           1    
[path]           2   
[advertised-to]  swp1
[advertised-to]  swp2
path-count       2
multipath-count  1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path</h>

Shows the paths for the specified IPv6 route in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
{{%/notice%}}

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
    "bestpath": { 
      "overall": "yes", 
      "selection-reason": "Origin" 
    }, 
    "flags": { 
      "bestpath": {}, 
      "valid": {} 
    }, 
    "flags-string": "*v", 
    "last-update": "2024-08-06T04:52:35Z", 
    "local": "on", 
    "metric": 0, 
    "nexthop": { 
      "1": { 
        "accessible": "on", 
        "afi": "ipv6", 
        "ip": "::", 
        "metric": 0, 
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
    "valid": "on", 
    "weight": 32768 
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\></h>

Shows information about the paths for the specified IPv6 route in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
{{%/notice%}}

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
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 1 -o json
{ 
  "aspath": {}, 
  "bestpath": { 
    "overall": "yes", 
    "selection-reason": "Origin" 
  }, 
  "flags": { 
    "bestpath": {}, 
    "valid": {} 
  }, 
  "flags-string": "*v", 
  "last-update": "2024-08-06T04:52:36Z", 
  "local": "on", 
  "metric": 0, 
  "nexthop": { 
    "1": { 
      "accessible": "on", 
      "afi": "ipv6", 
      "ip": "::", 
      "metric": 0, 
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
  "valid": "on", 
  "weight": 32768
}  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> nexthop</h>

Shows the next hops for the specified IPv6 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
{{%/notice%}}

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
    "metric": 0,
    "scope": "global",
    "used": "on"
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\></h>

Shows next hop information for the specified IPv6 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
{{%/notice%}}

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

Shows BGP neighbor information for the specified IPv6 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
{{%/notice%}}

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
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
{{%/notice%}}

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

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
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
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 1 bestpath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> aspath</h>

Shows the AS paths for the specified IPv6 route in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
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
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> community</h>

Shows the community names for the community list for the specified IPv6 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
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
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> large-community</h>

Shows the community names for the large community list for the specified IPv6 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
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
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> ext-community</h>

Shows the community names for the extended community list for the specified IPv6 route path in the local RIB.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>` command instead.
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
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 ext-community
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
No Data
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
-----------  -----------  ------- 
static 
  enable                  off 
connected 
  enable                  on 
  metric                  auto 
  route-map               none 
kernel
  enable                  off 
ospf6 
  enable                  off 
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
metric                  auto 
route-map               none
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

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route</h>

Shows BGP IPv6 routing table.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast route
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route \<route-id\></h>

Shows information about the BGP IPv6 route.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<route-id>` | The IPv6 route. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast route 2001:db8:2::a00:1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-count</h>

Shows the BGP IPv6 route and path count.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast route-count
             operational   applied
------------  -----------  -------
total-routes  13           13
total-paths   46           46
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

Shows configuration for IPv6 prefix-based routing using EVPN type-5 routes. Type-5 routes (or prefix routes) primarily route to destinations outside of the data center fabric. EVPN prefix routes carry the layer 3 VNI and router MAC address and follow the symmetric routing model to route to the destination prefix.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast route-export to-evpn
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast soo-route</h>

Shows the BGP Site-of-Origin IPv6 routes.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unicast soo-route
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

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unreachability</h>

Shows if BGP unreachability (failure signaling) is enabled globally on the switch.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unreachability
       operational  applied         
-----  -----------  ----------------
state               enabled         
                    state           
                    advertise-origin
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf <vrf-id> router bgp address-family ipv6-unreachability advertise-origin</h>

Shows the BGP unreachability advertise-origin configuration.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unreachability advertise-origin
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf <vrf-id> router bgp address-family ipv6-unreachability advertise-unreach</h>

Shows the BGP unreachability aggregate prefix and the included interfaces for which unreachability is conditionally advertised.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unreachability advertise-unreach
                    operational    applied      
------------------  -------------  -------------
[interfaces-match]  2001:1:1::/48  2001:1:1::/48
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf <vrf-id> router bgp address-family ipv6-unreachability advertise-unreach interfaces-match</h>

Shows the interfaces for which unreachability is conditionally advertised.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unreachability advertise-unreach interfaces-match
-------------
2001:1:1::/48
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unreachability route</h>

Shows BGP unreachability routes.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unreachability route
PathCount - Number of paths present for the prefix, MultipathCount - Number of
paths that are part of the ECMP, DestFlags - * - bestpath-exists, w - fib-wait-
for-install, s - fib-suppress, i - fib-installed, x - fib-install-failed

Prefix            PathCount  MultipathCount  DestFlags
----------------  ---------  --------------  ---------
2001:1:1:1::/127  4          0               *
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unreachability route \<route-id\></h>

Shows information about the specified BGP unreachability route.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<route-id>` | The IPv6 route.|

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unreachability route 2001:1:1:1::/127
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family ipv6-unreachability route-count</h>

Shows the BGP unreachability route count.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family ipv6-unreachability route-count
             operational
-----------  -----------
total-paths  1
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
        operational  applied
------  -----------  -------
enable               off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes</h>

Shows information about the IPv6 advertised routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\></h>

Shows information about a specific IPv6 advertised route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path</h>

Shows information about the IPv6 advertised route paths for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes  2001:db8::1/128 path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\></h>

Shows information about a specific IPv6 advertised route path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> aspath</h>

Shows information about the IPv6 advertised route AS path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> bestpath</h>

Shows information about the IPv6 advertised route best path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 bestpath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> community</h>

Shows information about the IPv6 advertised route communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> ext-community</h>

Shows information about the IPv6 advertised route extended communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 ext-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> flags</h>

Shows information about the IPv6 advertised route flags for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 flags
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> large-community</h>

Shows information about the IPv6 advertised route large communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> nexthop</h>

Shows information about the IPv6 advertised route nexthops for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 nexthop
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> peer</h>

Shows information about the IPv6 advertised route peers for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 peers
```

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 flags
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
        operational  applied  
------  -----------  -------
enable               on
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
state                         enabled
```

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command output shows `enabled on` or `enabled off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

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

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart timers</h>

Shows the BGP graceful restart selection deferral and stale path timer settings for the BGP neighbor.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast graceful-restart timers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart timers selection-deferral</h>

Shows the BGP graceful restart selection deferral timers for the BGP neighbor.

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast graceful-restart timers selection-deferral
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart timers stale-path</h>

Shows the BGP graceful restart stale path timer settings for the BGP neighbor.

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast graceful-restart timers stale-path
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
                     operational  applied
-------------------  -----------  -------
inbound                                           
  maximum                         none   
  warning-threshold               75
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
                   operational  applied
-----------------  -----------  ------- 
maximum                         none   
warning-threshold               75
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes</h>

Shows information about the IPv6 received routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\></h>

Shows information about a specific IPv6 received route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path</h>

Shows information about IPv6 received route paths for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\></h>

Shows information about a specific IPv6 received route path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.  |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> aspath</h>

Shows information about the IPv6 received route path AS path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> bestpath</h>

Shows information about the IPv6 received route path bestpath for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 bestpath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> community</h>

Shows information about the IPv6 received route path communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> ext-community</h>

Shows information about the IPv6 received route path extended communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 ext-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> flags</h>

Shows information about the IPv6 received route path flags for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 flags
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> large-community</h>

Shows information about the IPv6 received route path large communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> nexthop</h>

Shows information about the IPv6 received route path nexthops for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
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
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |
| `<nexthop-id>` |   The nexthop ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 nexthop 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> peer</h>

Shows information about the IPv6 received route path peers for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 peer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast route-counters</h>

Shows the number of IPv6 routes for a specific BGP neighbor in the specified VRF.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |   The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast route-counters
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability aspath</h>

Shows BGP unreachability AS path configuration for the specified neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unreachability aspath
                 operational  applied 
---------------  -----------  --------
replace-peer-as  disabled     disabled
private-as       none         none    
allow-my-asn                          
  state          enabled      enabled 
  origin         enabled      enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability capabilities</h>

Shows BGP unreachability capabilities for the specified neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unreachability capabilities
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability graceful-restart</h>

Shows BGP unreachability graceful restart timers for the specified neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unreachability graceful-restart
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability prefix-limits</h>

Shows BGP unreachability prefix-limits for the specified neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unreachability prefix-limits
                   operational  applied
-----------------  -----------  ------- 
maximum                         6   
warning-threshold               75
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast</h>

Shows if IPv6 is configured for the peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group underlay address-family ipv6-unicast
        operational  applied
------  -----------  -------
enable               off
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
state   disabled
```

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command output shows `enabled on` or `enabled off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-origination</h>

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
cumulus@switch:~$ nv show vrf default router bgp peer-group underlay address-family ipv6-unicast default-route-origination
No Data
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

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability aspath</h>

Shows the BGP unreachability prefix limits for the peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unreachability aspath
                 operational  applied 
---------------  -----------  --------
replace-peer-as  disabled     disabled
private-as       none         none    
allow-my-asn                          
  state          enabled      enabled 
  origin         enabled      enabled 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability prefix-limits</h>

Shows the the BGP unreachability prefix limits for the peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unreachability prefix-limits
                   operational  applied
-----------------  -----------  ------- 
maximum                         6   
warning-threshold               75
```
