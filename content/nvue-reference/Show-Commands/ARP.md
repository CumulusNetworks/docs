---
title: ARP
author: Cumulus Networks
weight: 127

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
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

## <h>nv show interface \<interface-id\> neighbor ipv4</h>

Shows all the entries in the ARP table for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp51 neighbor ipv4 
IPV4         LLADR(MAC)         State      Flag
-----------  -----------------  ---------  ----
169.254.0.1  48:b0:2d:2b:5b:b9  permanent      
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> neighbor ipv4 \<neighbor-id\></h>

Shows table entries for an interface with a specific IPv4 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface. |
| `<neighbor-id>` | The IPv4 address of the neighbor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp51 neighbor ipv4 169.254.0.1
lladdr
=========
    LLADR(MAC)         State      Flag
    -----------------  ---------  ----
    48:b0:2d:2b:5b:b9  permanent   
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> neighbor ipv4 \<neighbor-id\> lladdr \<lladdr-id\> flag</h>

Shows the flag set for the neighbor in the ARP table for the specified interface and associated MAC address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface. |
| `<neighbor-id>` | The IPv4 address of the neighbor. |
| `<lladdr-id>` |  The MAC address associated with IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp51 neighbor ipv4 169.254.0.1 lladdr 48:b0:2d:2b:5b:b9 flag
  operational  applied  
   -----------  ---------
   is-router    is-router
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> neighbor ipv4 \<neighbor-id\> lladdr \<lladdr-id\> state</h>

Shows the state of the neighbor in the ARP table for the specified interface and associated MAC address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface. |
| `<neighbor-id>` | The IPv4 address of the neighbor. |
| `<lladdr-id>` |  The MAC address associated with IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp51 neighbor ipv4 169.254.0.1 lladdr 48:b0:2d:2b:5b:b9 state
  operational  applied  
   -----------  ---------
   permanent    permanent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global arp</h>

Shows ARP settings, such as the neighbor base reachable timer and garbage collection settings.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system global arp
                              operational  applied
----------------------------  -----------  -------
base-reachable-time           50           50   
garbage-collection-threshold                      
  effective                   35840               
  maximum                     40960               
  minimum                     128            
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global arp garbage-collection-threshold</h>

Shows the ARP garbage collection threshold settings.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system global arp garbage-collection-threshold
           operational  applied
---------  -----------  -------
effective  35840               
maximum    40960               
minimum    128           
```
