---
title: Bridge
author: Cumulus Networks
weight: 140

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge</h>

Shows the configured bridge domains on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge
         operational  applied     pending   
--------  -----------  ----------  ----------
[domain]  br_default   br_default  br_default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain</h>

Shows configuration settings for the all configured bridge domains.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain
          ageing  encap   MAC       multicas…  multica…  stp.prio…  stp.sta…  type       untagged  vlan-vn…  Summary   
                          address                                                                                      
-------…  ------  ------  -------…  --------…  -------…  --------…  -------…  --------…  --------  -------…  ----------
br_defa…  1800    802.1Q            off        off       32768      up        vlan-awa…                      vlan:   10
                                                                                                             vlan: 1000
                                                                                                             vlan:   20
                                                                                                             vlan:   30
                                                                                                             vlan: 3000

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\></h>

Shows configuration settings for the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default
                 operational  applied     pending   
---------------  -----------  ----------  ----------
ageing           1800         1800        1800      
encap            802.1Q       802.1Q      802.1Q    
mac-address                   auto        auto      
type             vlan-aware   vlan-aware  vlan-aware
untagged                      1           1         
vlan-vni-offset               0           0         
multicast                                           
  snooping                                          
    enable       off          on          on        
    querier                                         
      enable     off          off         off       
stp                                                 
  priority       32768        32768       32768     
  state          up           up          up        
[vlan]           10           10          10        
[vlan]           20           20          20        
[vlan]           30           30          30        
[vlan]           1000         1000        1000      
[vlan]           3000         3000        3000      
[mdb]                                               
[router-port]
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> mac-table</h>

Shows the layer 2 forwarding database for the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default mac-table
    age     bridge-domain  entry-type  interface   last-update  MAC address      src-vni  vlan  vni   Summary          
--  ------  -------------  ----------  ----------  -----------  --------------…  -------  ----  ----  ----------------…
0   180582  br_default     permanent   swp6        180582       48:b0:2d:26:a1…                                        
1   180582  br_default     permanent   swp7        180582       48:b0:2d:45:49…                                        
2   292622  br_default     static      bond3       180582       48:b0:2d:a8:51…           30                           
3   23      br_default     static      bond3       180582       48:b0:2d:09:b9…           30                           
4   320097  br_default     permanent   bond3       320097       48:b0:2d:37:20…                                        
5   292622  br_default     static      bond2       180582       48:b0:2d:76:bf…           20                           
6   23      br_default     static      bond2       108          48:b0:2d:36:9e…           20                           
7   320097  br_default     permanent   bond2       320097       48:b0:2d:24:cb…                                        
8   292622  br_default                 vxlan48     292622       44:38:39:22:01…           20    None                   
9   292622  br_default                 vxlan48     292622       44:38:39:22:01…           30    None                   
10  292622  br_default                 vxlan48     292622       44:38:39:22:01…           10    None  remote-dst:      
                                                                                                      10.10.10.4       
11  292622  br_default                 vxlan48     140          44:38:39:22:01…           20    None                   
12  292622  br_default                 vxlan48     292622       48:b0:2d:1b:21…           10    None                   
13  292622  br_default                 vxlan48     292622       48:b0:2d:d0:1e…           10    None                   
14  292622  br_default                 vxlan48     292622       44:38:39:22:01…           30    None                   
15  292622  br_default                 vxlan48     292622       44:38:39:22:01…           10    None  remote-dst:      
                                                                                                      10.10.10.3
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> mdb</h>

Shows the MDB entries in the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default mdb
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> multicast</h>

Shows the multicast configuration settings on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default multicast
            operational  applied  pending
----------  -----------  -------  -------
snooping                                 
  enable    off          on       on     
  querier                                
    enable  off          off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> multicast snooping</h>

Shows the IGMP or MLD snooping configuration settings on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default multicast snooping
          operational  applied  pending
--------  -----------  -------  -------
enable    off          on       on     
querier                                
  enable  off          off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> multicast snooping querier</h>

Shows the IGMP or MLD querier configuration settings on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default multicast snooping querier
        operational  applied  pending
------  -----------  -------  -------
enable  off          off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> router-port</h>

Shows the multicast router ports for the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default router-port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> stp</h>

Shows the STP settings for the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default stp
          operational  applied  pending
--------  -----------  -------  -------
priority  32768        32768    32768  
state     up           up       up
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> stp state</h>

Shows the STP state (up or down) of the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default stp state
  operational  applied  pending
  -----------  -------  -------
  up           up       up
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan</h>

Shows the VLANs on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan
      multicast.snooping.querier.source-ip  ptp.enable  Summary  
----  ------------------------------------  ----------  ---------
10    0.0.0.0                               off         vni:   10
20    0.0.0.0                               off         vni:   20
30    0.0.0.0                               off         vni:   30
1000  0.0.0.0                               off         vni: 1000
3000  0.0.0.0                               off         vni: 3000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\></h>

Shows configuration settings for a specific VLAN on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10
                 operational  applied  pending
---------------  -----------  -------  -------
[vni]            10           10       10     
multicast                                     
  snooping                                    
    querier                                   
      source-ip  0.0.0.0      0.0.0.0  0.0.0.0
ptp                                           
  enable         off          off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> multicast</h>

Shows the multicast configuration settings for the specified VLAN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>`      | The VLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 multicast
               operational  applied  pending
-------------  -----------  -------  -------
snooping                                    
  querier                                   
    source-ip  0.0.0.0      0.0.0.0  0.0.0.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> multicast snooping</h>

Shows the IGMP or MLD snooping configuration settings for the specified VLAN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>`      | The VLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 multicast snooping
             operational  applied  pending
-----------  -----------  -------  -------
querier                                   
  source-ip  0.0.0.0      0.0.0.0  0.0.0.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier</h>

Shows the IGMP or MLD querier configuration settings for the specified VLAN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>`  | The VLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 multicast snooping querier
           operational  applied  pending
---------  -----------  -------  -------
source-ip  0.0.0.0      0.0.0.0  0.0.0.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> ptp</h>

Shows the PTP configuration settings for the specified VLAN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>`      | The VLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 ptp
        operational  applied  pending
------  -----------  -------  -------
enable  off          off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni</h>

Shows VNIs on a specific VLAN on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 vni
    flooding.enable  flooding.multicast-group  mac-learning  Summary               
--  ---------------  ------------------------  ------------  ----------------------
10  auto                                       off           IP Address: 10.10.10.2
                                                             IP Address: 10.10.10.3
                                                             IP Address: 10.10.10.4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\></h>

Shows configuration settings for a specific VLAN VNI on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN ID. |
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 vni 10
                          operational  applied  pending
------------------------  -----------  -------  -------
mac-learning              off          auto     auto   
flooding                                               
  enable                  auto         auto     auto   
  [head-end-replication]  10.10.10.2                   
  [head-end-replication]  10.10.10.3                   
  [head-end-replication]  10.10.10.4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding</h>

Shows configuration settings for BUM traffic flooding for the specified VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN ID.  |
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 vni 10 flooding
                        operational  applied  pending
----------------------  -----------  -------  -------
enable                  auto         auto     auto   
[head-end-replication]  10.10.10.2                   
[head-end-replication]  10.10.10.3                   
[head-end-replication]  10.10.10.4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication</h>

Shows the head-end-replication settings for the specified VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN ID. |
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 vni 10 flooding head-end-replication
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication \<hrep-id\></h>

Shows specific head-end-replication settings for the specified VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN ID. |
| `<vni-id>` | The VXLAN ID. |
| `<hrep-id>`  | The IPv4 unicast address or `evpn`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.0.1.34
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bridge</h>

Shows the bridge domain on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond3 bridge
         operational  applied     pending   
--------  -----------  ----------  ----------
[domain]  br_default   br_default  br_default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bridge domain \<domain-id\></h>

Shows configuration settings for the specified bridge domain on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`  | The interface name. |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond3 bridge domain br_default
               operational  applied  pending
-------------  -----------  -------  -------
access         30           30       30     
learning       on           on       on     
stp                                         
  admin-edge   off          off      off    
  auto-edge    on           on       on     
  bpdu-filter  off          off      off    
  bpdu-guard   off          off      off    
  network      off          off      off    
  restrrole    off          off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bridge domain \<domain-id\> stp</h>

Shows STP configuration settings for a specific bridge domain on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |
| `<domain-id>`  | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond3 bridge domain br_default stp
             operational  applied  pending
-----------  -----------  -------  -------
admin-edge   off          off      off    
auto-edge    on           on       on     
bpdu-filter  off          off      off    
bpdu-guard   off          off      off    
network      off          off      off    
restrrole    off          off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bridge domain \<domain-id\> vlan \<vid\></h>

Shows configuration settings for a specific VLAN on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN ID. You can also specify `all` to show settings for all VLANs. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp3 bridge domain br_default vlan 10
```
