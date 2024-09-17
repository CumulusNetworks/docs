---
title: Neighbor Discovery
author: Cumulus Networks
weight: 220

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery</h>

Shows <span class="a-tooltip">[ND](## "Neighbor Discovery")</span> settings for an interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip neighbor-discovery
                      applied              
--------------------  ---------------------
enable                on                   
mtu                   1500                 
[dnssl]               accounting.nvidia.com
home-agent                                 
  enable              on                   
  lifetime            200                  
  preference          0                    
[prefix]              2001:db8:1::100/32   
[rdnss]               2001:db8:1::100      
router-advertisement                       
  enable              off                  
  fast-retransmit     off                  
  hop-limit           64                   
  interval            600000               
  interval-option     off                  
  lifetime            1800                 
  managed-config      off                  
  other-config        off                  
  reachable-time      0                    
  retransmit-time     0                    
  router-preference   medium
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery dnssl</h>

Shows the <span class="a-tooltip">[DNSSL](## "DNS search list")</span>domain suffixes configured on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip neighbor-discovery dnssl
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery dnssl \<domain-name-id\></h>

Shows configuration information for the specified <span class="a-tooltip">[DNSSL](## "DNS search list")</span>domain suffix.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<domain-name-id>`   |  The domain portion of a hostname (RFC 1123) or an internationalized hostname (RFC 5890).|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip neighbor-discovery dnssl accounting.nvidia.com
          applied 
--------  --------
lifetime  infinite
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery home-agent</h>

Shows Home Agent configuration for an interface, such as the maximum amount of time the router acts as a Home Agent and the router preference.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip neighbor-discovery home-agent
            applied
----------  -------
enable      on     
lifetime    200    
preference  0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery prefix</h>

Shows the ND prefixes for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip neighbor-discovery prefix
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\></h>

Shows ND prefix configuration for the specified interface, such as the amount of time the prefix is valid for on-link determination, the amount of time that addresses generated from a prefix remain preferred, and if the specified prefix uses the IPv6 autoconfiguration setting.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<ipv6-prefix-id>`  | The IPv6 address and route prefix.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32
                    applied   
------------------  ----------
autoconfig          on        
off-link            on        
preferred-lifetime  100000    
router-address      on        
valid-lifetime      2000000000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery rdnss</h>

Shows the <span class="a-tooltip">[RDNSS](## "recursive DNS servers")</span> configured on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip neighbor-discovery rdnss
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery rdnss \<ipv6-address-id\></h>

Shows configuration for the specified <span class="a-tooltip">[RDNSS](## "recursive DNS server")</span> configured on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<ipv6-address-id>`  | The IPv6 address of the RDNSS.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip neighbor-discovery rdnss 2001:db8:1::100
          applied 
--------  --------
lifetime  infinite
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery router-advertisement</h>

Shows router advertisement configuration for an interface, such as the hop limit value advertised in a router advertisement message, the maximum amount of time that router advertisement messages can exist on the route, the interval at which neighbor solicitation messages retransmit, and if fast transmit mode is on.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip neighbor-discovery router-advertisement
                   applied
-----------------  -------
enable             off    
fast-retransmit    off    
hop-limit          64     
interval           600000 
interval-option    off    
lifetime           1800   
managed-config     off    
other-config       off    
reachable-time     0      
retransmit-time    0      
router-preference  medium
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface neighbor</h>

Shows all the entries in the IP neighbor table.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface neighbor
Interface      IP/IPV6                    LLADR(MAC)         State      Flag      
-------------  -------------------------  -----------------  ---------  ----------
eth0           192.168.200.251            48:b0:2d:00:00:01  stale                
               192.168.200.1              48:b0:2d:aa:8b:45  reachable            
               fe80::4ab0:2dff:fe00:1     48:b0:2d:00:00:01  reachable  router    
peerlink.4094  169.254.0.1                48:b0:2d:3f:69:d6  permanent            
               fe80::4ab0:2dff:fe3f:69d6  48:b0:2d:3f:69:d6  reachable  router    
swp51          169.254.0.1                48:b0:2d:a2:4c:79  permanent            
               fe80::4ab0:2dff:fea2:4c79  48:b0:2d:a2:4c:79  reachable  router    
swp52          169.254.0.1                48:b0:2d:48:f1:ae  permanent            
               fe80::4ab0:2dff:fe48:f1ae  48:b0:2d:48:f1:ae  reachable  router    
swp53          169.254.0.1                48:b0:2d:2d:de:93  permanent            
               fe80::4ab0:2dff:fe2d:de93  48:b0:2d:2d:de:93  reachable  router    
swp54          169.254.0.1                48:b0:2d:80:8c:21  permanent            
               fe80::4ab0:2dff:fe80:8c21  48:b0:2d:80:8c:21  reachable  router    
vlan10         10.1.10.3                  44:38:39:22:01:78  permanent            
               10.1.10.101                48:b0:2d:a1:3f:4b  reachable            
               10.1.10.104                48:b0:2d:1d:d7:e8  noarp      |ext_learn
               fe80::4ab0:2dff:fea1:3f4b  48:b0:2d:a1:3f:4b  reachable            
               fe80::4ab0:2dff:fe1d:d7e8  48:b0:2d:1d:d7:e8  noarp      |ext_learn
               fe80::4638:39ff:fe22:178   44:38:39:22:01:78  permanent
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> neighbor</h>

Shows all the entries in the IP neighbor table for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp51 neighbor
ipv4
=========
    IPV4         LLADR(MAC)         State      Flag
    -----------  -----------------  ---------  ----
    10.5.5.51    00:00:5e:00:53:51  permanent      
    169.254.0.1  48:b0:2d:a2:4c:79  permanent
ipv6
=========
    IPV6                       LLADR(MAC)         State      Flag     
    -------------------------  -----------------  ---------  ---------
    fe80::4ab0:2dff:fea2:4c79  48:b0:2d:a2:4c:79  reachable  is-router
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> neighbor ipv6</h>

Shows all IPv6 table entries for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 neighbor ipv6
IPV6                       LLADR(MAC)         State      Flag
-------------------------  -----------------  ---------  ---------
fe80::1e34:daff:fe6c:dd8   1c:34:da:6c:0d:d8  stale
fe80::3e2c:30ff:fe4b:800   3c:2c:30:4b:08:00  reachable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> neighbor ipv6 \<neighbor-id\></h>

Shows table entries for an interface with a specific IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface. |
| `<neighbor-id>` | The IPv6 address of the neighbor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp51 neighbor ipv6 fe80::4ab0:2dff:fea2:4c79
lladdr
=========
    LLADR(MAC)         State      Flag
    -----------------  ---------  ----
    00:00:5E:00:53:51  permanent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> neighbor ipv6 \<neighbor-id\> lladdr \<lladdr-id\> state</h>

Shows the state of the neighbor in the IP neighbor table for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface. |
| `<neighbor-id>` | The IPv6 address of the neighbor. |
| `<lladdr-id>` |  The MAC address associated with IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp51 neighbor ipv6 fe80::4ab0:2dff:fea2:4c79 lladdr 00:00:5E:00:53:51 state
  operational  applied  
   -----------  ---------
   permanent    permanent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> neighbor ipv6 \<neighbor-id\> lladdr \<lladdr-id\> flag</h>

Shows the flag set for the neighbor in the IP neighbor table for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface. |
| `<neighbor-id>` | The IPv6 address of the neighbor. |
| `<lladdr-id>` |  The MAC address associated with IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp51 neighbor ipv6 fe80::4ab0:2dff:fea2:4c79 lladdr 00:00:5E:00:53:51 flag
  operational  applied  
   -----------  ---------
   is-router    is-router
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global nd</h>

Shows <span class="a-tooltip">[ND](## "Neighbor Discovery")</span> settings, such as the neighbor base reachable timer and garbage collection settings.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system global nd
                              operational  applied  
----------------------------  -----------  ------- 
base-reachable-time           50           50      
garbage-collection-threshold                               
  effective                   17920                        
  maximum                     20480                        
  minimum                     128           
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global nd garbage-collection-threshold</h>

Shows the <span class="a-tooltip">[ND](## "Neighbor Discovery")</span> garbage collection threshold settings.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system global nd garbage-collection-threshold
           operational  applied
---------  -----------  -------
effective  35840               
maximum    40960               
minimum    128           
```
