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

Shows the configured bridges on the switch.

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

Shows configuration settings for all the bridges on the switch.

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

Shows configuration settings for a specific bridge.

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

Shows the layer 2 forwarding database for a specific bridge.

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

Shows the MDB entries for a specific bridge.

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

Shows the multicast configuration settings on a bridge.

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

Shows the IGMP or MLD snooping configuration settings on a bridge.

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

Shows the IGMP or MLD querier configuration settings for a bridge.

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

## <h>nv show bridge domain \<domain-id\> port</h>

Shows port information for a bridge.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default port
port  flags                       state     
----  --------------------------  ----------
swp1  flood,learning,mcast_flood  forwarding
swp2  flood,learning,mcast_flood  forwarding
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> port vlan</h>

Shows VLAN information for a bridge.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default port vlan
port  vlan  tag-state  fwd-state 
----  ----  ---------  ----------
swp1  1     untagged   forwarding
      10    tagged     forwarding
      20    tagged     forwarding
swp2  1     untagged   forwarding
      10    tagged     forwarding
      20    tagged     forwarding
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> router-port</h>

Shows the multicast router ports for a bridge.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default router-port
  ageing-timer  interface  type     
-  ------------  ---------  ---------
1     0.00       peerlink   permanent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> stp</h>

Shows the STP settings for a bridge.

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

## <h>nv show bridge domain \<domain-id\> stp counters</h>

Shows STP counters for a bridge.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default stp counters
port  tx-bpdu  rx-bpdu  tx-tcn  rx-tcn  fwd-trans  blk-trans  tx-pvst-tnl-bpdu  rx-pvst-tnl-bpdu
----  -------  -------  ------  ------  ---------  ---------  ----------------  ----------------
swp1  1270     0        4       0       3          2          1653              0               
swp2  1270     0        4       0       3          2          1653              0 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> stp port</h>

Shows STP information for all the ports in a bridge.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default stp port
Interface Info: swp1
--------------------------------------------------------------------------
enabled         : yes         admin-edge-port      : no
restricted-tcn  : no          bpdu-guard-port      : no
restricted-role : no          bpdu-guard-error     : no
port-path-cost  : 20000       bpdu-filter-port     : no
oper-edge-port  : yes         ba-inconsistent      : no
network-port    : no          auto-edge-port       : yes
mcheck          : no          admin-port-path-cost : 0

Interface Info: swp2
--------------------------------------------------------------------------
enabled         : yes         admin-edge-port      : no
restricted-tcn  : no          bpdu-guard-port      : no
restricted-role : no          bpdu-guard-error     : no
port-path-cost  : 20000       bpdu-filter-port     : no
oper-edge-port  : yes         ba-inconsistent      : no
network-port    : no          auto-edge-port       : yes
mcheck          : no          admin-port-path-cost : 0 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> stp port \<port-id\></h>

Shows STP information for a specific bridge port.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<port-id>` | The bridge port. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default stp port swp1
enabled         : yes         admin-edge-port      : no
restricted-tcn  : no          bpdu-guard-port      : no
restricted-role : no          bpdu-guard-error     : no
port-path-cost  : 20000       bpdu-filter-port     : no
oper-edge-port  : yes         ba-inconsistent      : no
network-port    : no          auto-edge-port       : yes
mcheck          : no          admin-port-path-cost : 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> stp state</h>

Shows the STP state (up or down) for a bridge.

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

## <h>nv show bridge domain \<domain-id\> stp vlan</h>

Shows PVRST information for all bridge VLANs.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default stp vlan
Bridge Vlan: 1
--------------------------------------------------------------------------
Bridge ID                priority    : 32769   mac-address       : 44:38:39:22:01:B1   
Designated Root ID       priority    : 32769   mac-address       : 44:38:39:22:01:B1   root-port  : -
Timers                   hello-time  : 2s      forward-delay     : 15s                 max-age    : 20s
Topology Change Network  count       : 0       time since change : 1152s
                         change port : None    last change port  : None

Bridge Vlan: 10
--------------------------------------------------------------------------
Bridge ID                priority    : 4106    mac-address       : 44:38:39:22:01:B1   
Designated Root ID       priority    : 4106    mac-address       : 44:38:39:22:01:B1   root-port  : -
Timers                   hello-time  : 4s      forward-delay     : 4s                  max-age    : 6s
Topology Change Network  count       : 1       time since change : 1147s
                         change port : swp2    last change port  : swp1

Bridge Vlan: 20
--------------------------------------------------------------------------
Bridge ID                priority    : 32788   mac-address       : 44:38:39:22:01:B1   
Designated Root ID       priority    : 32788   mac-address       : 44:38:39:22:01:B1   root-port  : -
Timers                   hello-time  : 2s      forward-delay     : 15s                 max-age    : 20s
Topology Change Network  count       : 1       time since change : 1147s
                         change port : swp2    last change port  : swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> stp vlan \<vid\></h>

Shows PVRST information for a specific bridge VLAN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |
| `<vid>` | The VLAN identifier. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default stp vlan 10
Bridge ID                priority    : 4106    mac-address       : 44:38:39:22:01:B1   
Designated Root ID       priority    : 4106    mac-address       : 44:38:39:22:01:B1   root-port  : -
Timers                   hello-time  : 4s      forward-delay     : 4s                  max-age    : 6s
Topology Change Network  count       : 1       time since change : 1174s
                         change port : swp2    last change port  : swp1

Interface info: swp1
---------------------------------
port-id            : 8.001
role               : Designated
state              : forwarding
port-path-cost     : 20000
tx-hold-count      : 6
port-hello-time    : 4s
fdb-flush          : no
disputed           : no

Interface info: swp2
---------------------------------
port-id            : 8.002
role               : Designated
state              : forwarding
port-path-cost     : 20000
tx-hold-count      : 6
port-hello-time    : 4s
fdb-flush          : no
disputed           : no
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> svi-force-up</h>

Shows if the `svi-force-up` option is set to `on` for SVIs in a specific bridge.

The first time you configure a switch, all southbound bridge ports are down; therefore, by default, all SVIs are also down. You can force the SVIs in a specific bridge to always be UP with the `nv set bridge domain <bridge-id> svi-force-up enable on` option, which is beneficial if you want to perform connectivity testing.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default svi-force-up
        applied
------  -------
enable  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan</h>

Shows all the VLANs for a bridge.

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

## <h>nv show bridge domain \<domain-id\> vlan-vni-map</h>

Shows the VLAN to VNI mapping for a specific bridge.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan-vni-map
br_default  VLAN-VNI-Offset: None 

VLAN  VNI
----  -----   
10    10
20    20   
30    30   
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\></h>

Shows configuration settings for a specific bridge VLAN.

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

Shows the multicast configuration settings for a specific bridge VLAN.

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

Shows the IGMP or MLD snooping configuration settings for a specific VLAN.

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

Shows the IGMP or MLD querier configuration settings for a specific VLAN.

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

Shows the PTP configuration settings for a specific VLAN.

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

Shows all VNIs for a specific bridge VLAN.

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

Shows configuration settings for a specific bridge VLAN VNI.

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

Shows configuration settings for BUM traffic flooding for a specific bridge VLAN VNI.

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

Shows the head-end-replication settings for a specific VLAN VNI.

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
IP Address
----------
10.0.1.34
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication \<hrep-id\></h>

Shows specific head-end-replication settings for a specific VLAN VNI.

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

## <h>nv show bridge port</h>

Shows the ports mapped to each bridge on the switch.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show bridge port
domain                       port             
--------        ------------------------------
br_default      swp1,swp2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge port-vlan</h>

Shows the VLANs mapped to each bridge port on the switch.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show bridge port-vlan
domain        port            vlan   tag-state
-------    ---------     ---------   ---------
br_default    swp1               1    untagged
                                10      tagged
                                20      tagged
              swp2               1    untagged
                                10      tagged
                                20      tagged
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge vlan-vni-map</h>

Shows the VLAN to VNI mapping for all bridges.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:mgmt:~$ nv show bridge vlan-vni-map
br_default  VLAN-VNI-Offset: None 

VLAN  VNI
----  -----   
10    10  
20    20  
30    30  

br1   VLAN-VNI-Offset: None 

VLAN  VNI     
----  -----   
40   40   
50   50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bridge</h>

Shows the bridge on the specified interface.

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

Shows configuration settings for a specific bridge interface.

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

Shows STP configuration settings for a specific bridge interface.

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

## <h>nv show interface \<interface-id\> bridge domain \<domain-id\> stp vlan \<vid\></h>

Shows interface PVRST settings for a bridge.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |
| `<domain-id>`  | The name of the bridge domain. |
| `<vid>` | The VLAN ID. You can also specify `all` to show settings for all VLANs. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show interface bond3 bridge domain br_default stp vlan 10
           applied
---------  -------
path-cost  4000   
priority   240    
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bridge domain \<domain-id\> vlan \<vid\></h>

Shows configuration settings for a bridge VLAN.

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
