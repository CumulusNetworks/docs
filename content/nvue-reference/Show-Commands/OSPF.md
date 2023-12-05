---
title: OSPF
author: Cumulus Networks
weight: 240

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router ospf</h>

Shows all OSPF configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp51 router ospf
                       applied       
---------------------  --------------
enable                 on            
area                   0             
cost                   auto          
mtu-ignore             off           
network-type           point-to-point
passive                off           
priority               1             
authentication                       
  enable               off           
bfd                                  
  enable               off           
timers                               
  dead-interval        60            
  hello-interval       5             
  retransmit-interval  5             
  transmit-delay       1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router ospf timers</h>

Shows <span class="a-tooltip">[SPF](## "Shortest Path First")</span> timer settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp51 router ospf timers
                     applied
-------------------  -------
dead-interval        60     
hello-interval       5      
retransmit-interval  5      
transmit-delay       1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router ospf authentication</h>

Shows the MD5 authentication configuration settings on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp51 router ospf authentication
                    applied     
------------------  ------------
enable              on          
md5-key             thisisthekey
message-digest-key  1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router ospf bfd</h>

Shows the BFD configuration settings on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp51 router ospf bfd
        applied
------  -------
enable  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router ospf</h>

Shows global OSPF configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router ospf
                  applied
----------------  -------
enable            on     
router-id         none   
timers                   
  refresh         10     
  lsa                    
    min-arrival   1000   
    throttle      5000   
  spf                    
    delay         80     
    holdtime      100    
    max-holdtime  6000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router ospf timers</h>

Shows all OSPF timer settings, such as <span class="a-tooltip">[LSA](## "Link State Advertisement")</span> timers and <span class="a-tooltip">[SPF](## "Shortest Path First")</span> timers that prevent consecutive SPF from overburdening the CPU.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router ospf timers
                applied
--------------  -------
refresh         10     
lsa                    
  min-arrival   1000   
  throttle      5000   
spf                    
  delay         80     
  holdtime      100    
  max-holdtime  6000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router ospf timers lsa</h>

Shows <span class="a-tooltip">[LSA](## "Link State Advertisement")</span> throttle timer settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router ospf timers lsa
             applied
-----------  -------
min-arrival  1000   
throttle     5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router ospf timers spf</h>

Shows <span class="a-tooltip">[SPF](## "Shortest Path First")</span> timer settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router ospf timers spf
              applied
------------  -------
delay         80     
holdtime      100    
max-holdtime  6000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf</h>

Shows the OSPF configuration settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf
                     applied   
-------------------  ----------
enable               on        
reference-bandwidth  100000    
rfc1583-compatible   off       
router-id            10.10.10.1
default-originate              
  enable             off       
distance                       
  external           none      
  inter-area         none      
  intra-area         none      
log                            
  adjacency-changes  on        
max-metric                     
  administrative     off       
  on-shutdown        none      
  on-startup         none      
redistribute                   
  bgp                          
    enable           off       
  connected                    
    enable           off       
  kernel                       
    enable           off       
  static                       
    enable           off       
timers                         
  refresh            auto      
  lsa                          
    min-arrival      auto      
    throttle         auto      
  spf                          
    delay            auto      
    holdtime         auto      
    max-holdtime     auto
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf area \<area-id\></h>

Shows the specified OSPF area configuration settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<area-id>` |  Area |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf area 0
                  applied           
----------------  ------------------
default-lsa-cost  2000              
type              stub              
filter-list                         
  in              MY-OSPF-IN-FILTER 
  out             MY-OSPF-OUT-FILTER
[network]         10.10.10.1/32     
[range]           172.16.1.0/24
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf area \<area-id\> filter-list</h>

Shows the filter list for the specified OSPF area for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<area-id>` |  Area |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf area 0 filter-list
     applied           
---  ------------------
in   MY-OSPF-IN-FILTER 
out  MY-OSPF-OUT-FILTER
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf area \<area-id\> network \<network-id\></h>

Shows the configuration settings for a specific OSPF area network subnet for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<area-id>` |  The area ID. |
| `<network-id>`  | The IPv4 network subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf area 0 network 10.10.10.1/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf area \<area-id\> range \<range-id\></h>

Shows the configuration settings for the specified OSPF area prefix range for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<area-id>` |  The area ID. |
| `<range-id>` |  The IPv4 prefix range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf area 0 range 172.16.1.0/24
          applied
--------  -------
cost      65535  
suppress  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf default-originate</h>

Shows OSPF default originate information for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf default-originate
             applied  
-----------  ---------
enable       on       
metric       16777214 
metric-type  2        
route-map    ROUTEMAP1
always       on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf distance</h>

Shows the OSPF administrative distance configuration for the specified VRF. You configure the administrative distance to choose which routing protocol to use when two different protocols provide route information for the same destination. The smaller the distance, the more reliable the protocol.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf distance
            applied
----------  -------
external    220    
inter-area  150    
intra-area  150
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf interface</h>

Shows the OSPF interfaces in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf interface
Interface  Summary             
---------  --------------------
lo         local-ip: 10.10.10.1
swp51      local-ip: 10.10.10.1
swp52      local-ip: 10.10.10.1
vlan10     local-ip:  10.1.10.2
vlan20     local-ip:  10.1.20.2
vlan30     local-ip:  10.1.30.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf interface \<interface-id\></h>

Shows information about a specific OSPF interface in the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf interface swp51 -o json
{
  "local-ip": {
    "10.10.10.1": {
      "cost": 100,
      "counters": {
        "adjacent-neighbor-count": 0,
        "dbd-rx": 0,
        "dbd-tx": 0,
        "hello-rx": 0,
        "hello-tx": 98,
        "ls-ack-rx": 0,
        "ls-ack-tx": 0,
        "ls-request-rx": 0,
        "ls-request-tx": 0,
        "ls-update-rx": 0,
        "ls-update-tx": 0,
        "neighbor-count": 0
      },
      "dead-interval": 60,
      "hello-interval": 5000,
      "hello-interval-remain": 2496,
      "passive": "off",
      "priority": 1,
      "retransmit-interval": 5,
      "state": "Point-To-Point",
      "transmit-delay": 1,
      "wait-timer": 60
    }
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf interface \<interface-id\> local-ip</h>

Shows the local IP addresses for a specific OSPF interface in the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf interface swp51 local-ip -o json
{
  "10.10.10.1": {
    "cost": 100,
    "counters": {
      "adjacent-neighbor-count": 0,
      "dbd-rx": 0,
      "dbd-tx": 0,
      "hello-rx": 0,
      "hello-tx": 111,
      "ls-ack-rx": 0,
      "ls-ack-tx": 0,
      "ls-request-rx": 0,
      "ls-request-tx": 0,
      "ls-update-rx": 0,
      "ls-update-tx": 0,
      "neighbor-count": 0
    },
    "dead-interval": 60,
    "hello-interval": 5000,
    "hello-interval-remain": 1199,
    "passive": "off",
    "priority": 1,
    "retransmit-interval": 5,
    "state": "Point-To-Point",
    "transmit-delay": 1,
    "wait-timer": 60
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf interface \<interface-id\> local-ip \<ipv4-address\></h>

Shows information about a specific local IP address for the specified OSPF interface in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<interface-id>` | The interface name. |
| `<ipv4-address>`    | The local IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf interface swp51 local-ip 10.10.10.1
                           operational     applied
-------------------------  --------------  -------
cost                       100                    
dead-interval              60                     
hello-interval             5000                   
hello-interval-remain      1391                   
passive                    off                    
priority                   1                      
retransmit-interval        5                      
state                      Point-To-Point         
transmit-delay             1                      
wait-timer                 60                     
counters                                          
  adjacent-neighbor-count  0                      
  dbd-rx                   0                      
  dbd-tx                   0                      
  hello-rx                 0                      
  hello-tx                 119                    
  ls-ack-rx                0                      
  ls-ack-tx                0                      
  ls-request-rx            0                      
  ls-request-tx            0                      
  ls-update-rx             0                      
  ls-update-tx             0                      
  neighbor-count           0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf neighbor</h>

Shows the OSPF neighbors in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf neighbor
              Summary         
------------  ----------------
10.10.10.101  Interface: swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf neighbor \<neighbor-id\></h>

Shows information about a specific OSPF neighbor in the specified VRF.

{{%notice note%}}
Add `-- operational -o json` at the end of the command to see more complete output.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>` | The IP address of the OSPF neighbor.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf neighbor 10.10.10.101 --operational -o json
{
  "interface": {
    "swp51": {
      "local-ip": {
        "10.0.1.0": {
          "bdr-router-id": "10.10.10.101",
          "dead-timer-expiry": 30794,
          "dr-router-id": "10.10.10.1",
          "neighbor-ip": "10.0.1.1",
          "priority": 1,
          "role": "BDR",
          "state": "full",
          "statistics": {
            "db-summary-qlen": 0,
            "ls-request-qlen": 0,
            "ls-retrans-qlen": 0,
            "state-changes": 5
          }
        }
      }
    }
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf neighbor \<neighbor-id\> interface</h>

Shows the interfaces for a specific OSPF neighbor in the specified VRF.

### Command Syntax
| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>` | The IP address of the OSPF neighbor.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf neighbor 10.10.10.1 interface
Interface  Summary             
---------  --------------------
lo         local-ip: 10.10.10.1
swp51      local-ip: 10.10.10.1
swp52      local-ip: 10.10.10.1
vlan10     local-ip:  10.1.10.2
vlan20     local-ip:  10.1.20.2
vlan30     local-ip:  10.1.30.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf neighbor \<neighbor-id\> interface \<interface-id\></h>

Shows information about a specific OSPF neighbor interface in the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>` | The IP address of the OSPF neighbor.|
| `<interface-id>` | The OSPF neighbor interface.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf neighbor 10.10.10.1 interface swp51 -o json
{
  "local-ip": {
    "10.10.10.1": {
      "dead-timer-expiry": -1,
      "neighbor-ip": "10.10.10.1",
      "priority": 1,
      "role": "DROther",
      "state": "2-way",
      "statistics": {
        "db-summary-qlen": 0,
        "ls-request-qlen": 0,
        "ls-retrans-qlen": 0,
        "state-changes": 0
      }
    }
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf neighbor \<neighbor-id\> interface \<interface-id\> local-ip</h>

Shows the local IP address for a specific OSPF neighbor interface in the specified VRF.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>` | The IP address of the OSPF neighbor.|
| `<interface-id>` | The OSPF neighbor interface.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf neighbor 10.10.10.1 interface swp51 local-ip -o json
{
  "10.10.10.1": {
    "dead-timer-expiry": -1,
    "neighbor-ip": "10.10.10.1",
    "priority": 1,
    "role": "DROther",
    "state": "2-way",
    "statistics": {
      "db-summary-qlen": 0,
      "ls-request-qlen": 0,
      "ls-retrans-qlen": 0,
      "state-changes": 0
    }
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf neighbor \<neighbor-id\>  interface \<interface-id\> local-ip \<address\></h>

Shows information about a specific local IP address for the specified OSPF neighbor interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>` | The IP address of the OSPF neighbor.|
| `<interface-id>` | The OSPF neighbor interface.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf neighbor 10.10.10.101 interface swp51 local-ip 10.0.1.0
                   operational   applied
-----------------  ------------  -------
bdr-router-id      10.10.10.101         
dead-timer-expiry  30042                
dr-router-id       10.10.10.1           
neighbor-ip        10.0.1.1             
priority           1                    
role               BDR                  
state              full                 
statistics                              
  db-summary-qlen  0                    
  ls-request-qlen  0                    
  ls-retrans-qlen  0                    
  state-changes    5 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf log</h>

Shows the OSPF log configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf log
                   applied
-----------------  -------
adjacency-changes  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf max-metric</h>

Shows the maximum metric configuration settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf max-metric
                applied
--------------  -------
administrative  on     
on-shutdown     20     
on-startup      200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf redistribute</h>

Shows the OSPF route redistribute settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf redistribute
               applied
-------------  -------
bgp                   
  enable       on     
  metric       2000   
  metric-type  2      
  route-map    none   
connected             
  enable       on     
  metric       2000   
  metric-type  2      
  route-map    none   
kernel                
  enable       off    
static                
  enable       off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf redistribute bgp</h>

Shows configuration settings for OSPF redistribute BGP routes for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf redistribute bgp
             applied
-----------  -------
enable       on     
metric       2000   
metric-type  2      
route-map    none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf redistribute connected</h>

Shows configuration settings for OSPF redistribute connected routes for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf redistribute connected
             applied
-----------  -------
enable       on     
metric       2000   
metric-type  2      
route-map    none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf redistribute kernel</h>

Shows configuration settings for OSPF redistribute kernel routes for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf redistribute kernel
        applied
------  -------
enable  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf redistribute static</h>

Shows configuration settings for OSPF redistribute static routes for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf redistribute static
        applied
------  -------
enable  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

<!-- ## <h>nv show vrf \<vrf-id\> router ospf static-neighbor</h>

Shows information about the OSPF static neighbors in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf static-neighbor 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf static-neighbor \<ipv4-address\></h>

Shows information about a specific OSPF static neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf static-neighbor 10.10.10.1
```
-->

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf timers</h>

Shows OSPF timer settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf timers
                applied
--------------  -------
refresh         30     
lsa                    
  min-arrival   30000  
  throttle      3000   
spf                    
  delay         30000  
  holdtime      30000  
  max-holdtime  3000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf timers lsa</h>

Shows the <span class="a-tooltip">[LSA](## "Link State Advertisement")</span> throttle timer settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf timers lsa
             applied
-----------  -------
min-arrival  30000  
throttle     3000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router ospf timers spf</h>

Shows <span class="a-tooltip">[SPF](## "Shortest Path First")</span> timer settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router ospf timers spf
              applied
------------  -------
delay         30000  
holdtime      30000  
max-holdtime  3000
```
