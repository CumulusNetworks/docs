---
title: EVPN
author: Cumulus Networks
weight: 170

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn</h>

Shows global EVPN control plane information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn
                       operational   applied        pending      
---------------------  ------------  -------------  -------------
enable                               on             on           
dad                                                              
  enable               off           on             on           
  mac-move-threshold   5             5              5            
  move-window          180           180            180          
  duplicate-action     warning-only  warning-only   warning-only 
multihoming                                                      
  enable                             on             on           
  mac-holdtime         1080          1080           1080         
  neighbor-holdtime    1080          1080           1080         
  startup-delay        180           180            180          
  ead-evi-route                                                  
    rx                               on             on           
    tx                               on             on           
  segment                                                        
    df-preference                    32767          32767        
  startup-delay-timer  --:--:--                                  
  uplink-active        2                                         
  uplink-count         2                                         
route-advertise                                                  
  default-gateway      off           off            off          
  nexthop-setting                    system-ip-mac  system-ip-mac
  svi-ip               off           off            off          
[vni]                                                            
l2vni-count            5                                         
l3vni-count            2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info</h>

Shows access VLAN information.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info
        operational  applied  pending
------  -----------  -------  -------
[vlan]  10                           
[vlan]  20                           
[vlan]  30                           
[vlan]  220                          
[vlan]  297                          
[vlan]  1000                         
[vlan]  3000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info vlan</h>

Shows all EVPN access VLANs.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info vlan
Vlan-id  member-interface-count  vni   vni-count  vxlan-interface  Summary                
-------  ----------------------  ----  ---------  ---------------  -----------------------
10       1                       10    1          vxlan48          member-interface: bond1
20       1                       20    1          vxlan48          member-interface: bond2
30       1                       30    1          vxlan48          member-interface: bond3
220                                    1          vxlan99                                 
297                                    1          vxlan99                                 
1000                             1000  1          vxlan48                                 
3000                             3000  1          vxlan48
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info vlan \<vlan-id\></h>

Shows EVPN access VLAN information for the specified VLAN.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info vlan 10
                        operational  applied  pending
----------------------  -----------  -------  -------
member-interface-count  1                            
vni                     10                           
vni-count               1                            
vxlan-interface         vxlan48                      

member-interface
===================
     
    -----
    bond1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info vlan \<vlan-id\> member-interface</h>

Shows EVPN access VLAN member interface information.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info vlan 10 member-interface

-----
bond1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn dad</h>

Shows EVPN duplicate address detection information. The VTEP considers a host MAC or IP address to be duplicate if the address moves across the network more than a certain number of times within a certain number of seconds. In addition to legitimate host or VM mobility scenarios, address movement can occur when you configure IP addresses incorrectly on a host or when packet looping occurs in the network due to faulty configuration or behavior.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn dad
                    operational   applied       pending     
------------------  ------------  ------------  ------------
enable              off           on            on          
mac-move-threshold  5             5             5           
move-window         180           180           180         
duplicate-action    warning-only  warning-only  warning-only
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn dad duplicate-action</h>

Shows the action to take when there is a duplicate address detected.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn dad duplicate-action
 operational   applied       pending     
  ------------  ------------  ------------
  warning-only  warning-only  warning-only
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn dad duplicate-action freeze</h>

Shows all EVPN duplicate address freeze actions.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn dad duplicate-action freeze
          operational  applied
--------  -----------  -------
duration  1000         1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn l2-nhg</h>

Shows EVPN next hop groups.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn l2-nhg

vtep-ip
==========
    Vtepip      es-ref-count  nexthop-group
    ----------  ------------  -------------
    10.10.10.2  3             268435460    
    10.10.10.3  1             268435462    
    10.10.10.4  1             268435463
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn l2-nhg vtep-ip</h>

Shows EVPN next hop group information for all VTEPs.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn l2-nhg vtep-ip
Vtepip      es-ref-count  nexthop-group
----------  ------------  -------------
10.10.10.2  3             268435460    
10.10.10.3  1             268435462    
10.10.10.4  1             268435463
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn l2-nhg vtep-ip \<vtep-id\></h>

Shows EVPN next hop group information for the specified VTEP.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vtep-id>` | The VTEP ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn l2-nhg vtep-ip 10.10.10.2
               operational  applied  pending
-------------  -----------  -------  -------
es-ref-count   3                            
nexthop-group  268435460 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming</h>

Shows global EVPM multihoming configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming
                     operational  applied  pending
-------------------  -----------  -------  -------
enable                            on       on     
mac-holdtime         1080         1080     1080   
neighbor-holdtime    1080         1080     1080   
startup-delay        180          180      180    
ead-evi-route                                     
  rx                              on       on     
  tx                              on       on     
segment                                           
  df-preference                   32767    32767  
startup-delay-timer  --:--:--                     
uplink-active        2                            
uplink-count         2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info</h>

Shows EVPN multihoming BGP information.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info
      operational                    applied  pending
-----  -----------------------------  -------  -------
[esi]  03:44:38:39:be:ef:aa:00:00:01                  
[esi]  03:44:38:39:be:ef:aa:00:00:02                  
[esi]  03:44:38:39:be:ef:aa:00:00:03                  
[esi]  03:44:38:39:be:ef:bb:00:00:01                  
[esi]  03:44:38:39:be:ef:bb:00:00:02                  
[esi]  03:44:38:39:be:ef:bb:00:00:03
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi</h>

Shows EVPN multihoming BGP information for all ESIs.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi -o json
{
  "03:44:38:39:be:ef:aa:00:00:01": {
    "es-df-preference": 50000,
    "flags": {
      "advertise-evi": "on",
      "up": "on"
    },
    "fragments": {
      "10.10.10.1:3": {
        "evi-count": 1
      }
    },
    "inconsistent-vni-count": 0,
    "macip-global-path-count": 8,
    "macip-path-count": 4,
    "originator-ip": "10.0.0.1",
    "rd": "10.10.10.1:3",
    "remote-vtep": {
      "10.10.10.2": {
        "df-algorithm": "preference",
        "df-preference": 50000,
        "flags": {
          "active": "on",
          "esr": "on"
        }
      }
    },
    "type": {
      "local": "on",
      "remote": "on"
    },
    "vni-count": 1,
    "vrf-count": 1
  },
  "03:44:38:39:be:ef:aa:00:00:02": {
    "es-df-preference": 50000,
    "flags": {
      "advertise-evi": "on",
      "up": "on"
    },
    "fragments": {
      "10.10.10.1:8": {
        "evi-count": 1
      }
    },
    "inconsistent-vni-count": 0,
    "macip-global-path-count": 4,
    "macip-path-count": 2,
    "originator-ip": "10.0.0.1",
    "rd": "10.10.10.1:8",
    "remote-vtep": {
      "10.10.10.2": {
        "df-algorithm": "preference",
        "df-preference": 50000,
        "flags": {
          "active": "on",
          "esr": "on"
        }
      }
    },
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi \<esi-id\></h>

Shows EVPN multihoming BGP information for the specified ESI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02
                         operational   applied  pending
-----------------------  ------------  -------  -------
es-df-preference         50000                         
inconsistent-vni-count   0                             
macip-global-path-count  4                             
macip-path-count         2                             
originator-ip            10.0.0.1                      
rd                       10.10.10.1:8                  
vni-count                1                             
vrf-count                1                             
flags                                                  
  advertise-evi          on                            
  up                     on                            
[fragments]              10.10.10.1:8                  
[remote-vtep]            10.10.10.2                    
type                                                   
  local                  on                            
  remote                 on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi \<esi-id\> remote-vtep</h>

Shows EVPN multihoming BGP information for the specified ESI for all VTEPs.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep
            df-algorithm  df-preference  flags.active  flags.esr
----------  ------------  -------------  ------------  ---------
10.10.10.2  preference    50000          on            on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi \<esi-id\> remote-vtep \<ipv4-address-id\></h>

Shows EVPN multihoming BGP information for the specified ESI for a specific VTEP.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |
| `<ipv4-address-id>` | The IPv4 address of the VTEP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep 10.10.10.2
               operational  applied  pending
-------------  -----------  -------  -------
df-algorithm   preference                   
df-preference  50000                        
flags                                       
  active       on                           
  esr          on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi \<esi-id\> fragments</h>

Shows EVPN multihoming BGP remote VTEP fragment information for a specific ESI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02 fragments
              evi-count
------------  ---------
10.10.10.1:8  1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi \<esi-id\> fragments \<fragment-id\></h>

Shows specific EVPN multihoming BGP remote VTEP fragment information for a specific ESI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |
| `<fragment-id>` | The route-distinguisher. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02 fragments 10.10.10.1:8
           operational  applied  pending
---------  -----------  -------  -------
evi-count  1  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming ead-evi-route</h>

Shows EVPN multihoming Ethernet Auto-discovery per EVPN instance route information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming ead-evi-route
    operational  applied  pending
--  -----------  -------  -------
rx               on       on     
tx               on       on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming esi</h>

Shows EVPN multihoming Ethernet segment ID information.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi`
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming esi -o json
{
  "03:44:38:39:be:ef:aa:00:00:01": {
    "df-preference": 50000,
    "flags": {
      "bridge-port": "on",
      "local": "on",
      "nexthop-group-active": "on",
      "oper-up": "on",
      "ready-for-bgp": "on",
      "remote": "on"
    },
    "local-interface": "bond1",
    "mac-count": 2,
    "nexthop-group-id": 536870913,
    "remote-vtep": {
      "10.10.10.2": {
        "df-algorithm": "preference",
        "df-preference": 50000,
        "nexthop-group-id": 268435460
      }
    },
    "vni-count": 1
  },
  "03:44:38:39:be:ef:aa:00:00:02": {
    "df-preference": 50000,
    "flags": {
      "bridge-port": "on",
      "local": "on",
      "nexthop-group-active": "on",
      "oper-up": "on",
      "ready-for-bgp": "on",
      "remote": "on"
    },
    "local-interface": "bond2",
    "mac-count": 2,
    "nexthop-group-id": 536870914,
    "remote-vtep": {
      "10.10.10.2": {
        "df-algorithm": "preference",
        "df-preference": 50000,
        "nexthop-group-id": 268435460
      }
    },
    "vni-count": 1
  },
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming esi \<esi-id\></h>

Shows information about the specified EVPN multihoming Ethernet segment ID.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming esi 03:44:38:39:be:ef:aa:00:00:02
                        operational  applied  pending
----------------------  -----------  -------  -------
df-preference           50000                        
local-interface         bond2                        
mac-count               2                            
nexthop-group-id        536870914                    
vni-count               1                            
flags                                                
  bridge-port           on                           
  local                 on                           
  nexthop-group-active  on                           
  oper-up               on                           
  ready-for-bgp         on                           
  remote                on                           
[remote-vtep]           10.10.10.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming esi \<esi-id\> remote-vtep</h>

Shows information about the specified EVPN multihoming Ethernet segment ID for remote VTEPs.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep
            df-algorithm  df-preference  nexthop-group-id
----------  ------------  -------------  ----------------
10.10.10.2  preference    50000          268435460
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming esi \<esi-id\> remote-vtep \<ipv4-address-id\></h>

Shows information about a specific EVPN multihoming Ethernet segment ID for the specified remote VTEP.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |
| `<ipv4-address-id>` | The IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep 10.10.10.2
                  operational  applied  pending
----------------  -----------  -------  -------
df-algorithm      preference                   
df-preference     50000                        
nexthop-group-id  268435460
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming segment</h>

Shows EVPN multihoming segment information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming segment
               operational  applied  pending
-------------  -----------  -------  -------
df-preference               32767    32767
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn route-advertise</h>

Shows EVPN route advertise information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn route-advertise
                 operational  applied        pending      
---------------  -----------  -------------  -------------
default-gateway  off          off            off          
nexthop-setting               system-ip-mac  system-ip-mac
svi-ip           off          off            off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni</h>

Shows information about the EVPN VNIs on the switch.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni

NumMacs - Number of MACs (local and remote) known for this VNI, NumArps - Number 
of ARPs (IPv4 and IPv6, local and remote) known for this VNI                     
, NumRemVteps - Number of Remote Vteps                                           
                                                                                 
VNI   NumMacs  NumArps  NumRemVteps  TenantVrf
----  -------  -------  -----------  ---------
10    8        4        3            RED      
20    6        1        3            RED      
30    6        1        3            BLUE     
1000  0        0        0            default  
3000  0        0        0            default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\></h>

Shows configuration information about the specified VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id>`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10
                   operational  applied  pending
-----------------  -----------  -------  -------
route-advertise                                 
  default-gateway  off                          
  svi-ip           off                          
bridge-domain      br_default                   
host-count         4                            
local-vtep         10.0.0.1                     
mac-count          8                            
remote-vtep-count  3                            
tenant-vrf         RED                          
vlan               10                           
vxlan-interface    vxlan48

remote-vtep
==============
                flood
    ----------  -----
    10.10.10.2  HER  
    10.10.10.3  HER  
    10.10.10.4  HER 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> bgp-info</h>

Shows BGP configuration information for the specific VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 bgp-info
                          operational   applied  pending
-------------------------  ------------  -------  -------
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

## <h>nv show evpn vni \<vni-id\> host</h>

Shows the ARP and ND table for the specific VNI.

### Command Syntax

|  Syntax |  Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 host

LocMobSeq - local mobility sequence, RemMobSeq - remote mobility sequence, Esi - 
Remote Esi                                                                       
                                                                                 
IP address                 Type    State   LocMobSeq  RemMobSeq  Mac                Esi                       
-------------------------  ------  ------  ---------  ---------  -----------------  -------------------------…
10.1.10.101                local   active  0          0          48:b0:2d:bc:2e:e7                            
10.1.10.104                remote  active  0          0          48:b0:2d:d0:1e:4a  03:44:38:39:be:ef:bb:00:0…
fe80::4ab0:2dff:febc:2ee7  local   active  0          0          48:b0:2d:bc:2e:e7                            
fe80::4ab0:2dff:fed0:1e4a  remote  active  0          0          48:b0:2d:d0:1e:4a  03:44:38:39:be:ef:bb:00:0…
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> host \<ip-address-id\></h>

Shows a specific ARP and ND table for the specific VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |
| `<ip-address-id>` |  The IP address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 host 10.1.10.101
                     operational        applied  pending
-------------------  -----------------  -------  -------
detection-count      0                                  
duplicate            off                                
local-mobility-seq   0                                  
remote-mobility-seq  0                                  
type                 local                              
mac                  48:b0:2d:bc:2e:e7                  
state                active 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> mac</h>

Shows the MAC address for the specified EVPN VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 mac

LocMobSeq - local mobility sequence, RemMobSeq - remote mobility sequence,       
RemoteVtep - Remote Vtep address, Esi - Remote Esi                               
                                                                                 
MAC address        Type    State  LocMobSeq  RemMobSeq  Interface  RemoteVtep  Esi                          
-----------------  ------  -----  ---------  ---------  ---------  ----------  -----------------------------
44:38:39:22:01:7a  local          0          0          vlan10                                              
44:38:39:22:01:8a  remote         0          0                     10.10.10.4                               
44:38:39:22:01:78  remote         0          0                     10.10.10.2                               
44:38:39:22:01:84  remote         0          0                     10.10.10.3                               
48:b0:2d:1b:21:0e  remote         0          0                                 03:44:38:39:be:ef:bb:00:00:01
48:b0:2d:91:ee:88  local          0          0          bond1                                               
48:b0:2d:bc:2e:e7  local          0          0          bond1                                               
48:b0:2d:d0:1e:4a  remote         0          0                                 03:44:38:39:be:ef:bb:00:00:01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> mac \<mac-address-id\></h>

Shows configuration information about a specific VNI MAC address.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<mac-address-id>` | The MAC address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 mac 44:38:39:22:01:78
                     operational  applied  pending
-------------------  -----------  -------  -------
detection-count      0                            
duplicate            off                          
local-mobility-seq   0                            
remote-mobility-seq  0                            
remote-vtep          10.10.10.2                   
type                 remote                       
neigh-sync-count     0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming</h>

Shows multihoming Ethernet configuration for the specified VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming
          operational                    applied  pending
--------  -----------------------------  -------  -------
bgp-info                                                 
  [esi]   03:44:38:39:be:ef:aa:00:00:01                  
  [esi]   03:44:38:39:be:ef:bb:00:00:01                  
[esi]     03:44:38:39:be:ef:aa:00:00:01 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming bgp-info esi</h>

Shows BGP information for the multihoming Ethernet segments for the specified VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming bgp-info esi
                               type.local  type.remote  Summary                
-----------------------------  ----------  -----------  -----------------------
03:44:38:39:be:ef:aa:00:00:01  on          on           remote-vtep: 10.10.10.2
03:44:38:39:be:ef:bb:00:00:01              on           remote-vtep: 10.10.10.3
                                                        remote-vtep: 10.10.10.4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming bgp-info esi \<es-id\></h>

Shows BGP information for a specific multihoming Ethernet segment for the specified VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<es-id>` | The Ethernet segment ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02
               operational  applied  pending
-------------  -----------  -------  -------
[remote-vtep]  10.10.10.2                   
type                                        
  local        on                           
  remote       on 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming bgp-info esi \<esi-id\> remote-vtep</h>

Shows BGP information for a specific multihoming Ethernet segment for the specified VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<es-id>` | The Ethernet segment ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep
            flags.ead-per-es  flags.ead-per-evi
----------  ----------------  -----------------
10.10.10.2  on                on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming bgp-info esi \<esi-id\> remote-vtep \<ipv4-address-id\></h>

Shows BGP information for a specific multihoming Ethernet segment for the specified VNI on a specific remote VTEP.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<es-id>` | The Ethernet segment ID. |
| `<ipv4-address-id>` | The IPv4 address of the remote VTEP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:01 remote-vtep 10.10.10.2
               operational  applied  pending
-------------  -----------  -------  -------
flags                                       
  ead-per-es   on                           
  ead-per-evi  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming esi</h>

Shows the EVPN multihoming ESIs for the specified VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming esi
                               type.local  type.remote
-----------------------------  ----------  -----------
03:44:38:39:be:ef:aa:00:00:01  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming esi \<es-id\></h>

Shows information for a specific multihoming Ethernet segment for the specified VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<es-id>` | The Ethernet segment ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming esi 03:44:38:39:be:ef:aa:00:00:02
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-advertise</h>

Shows route advertisement information for the specified VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-advertise`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-advertise
                 operational  applied  pending
---------------  -----------  -------  -------
default-gateway  off                          
svi-ip           off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target</h>

Shows route target information for the specified VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target both</h>

Shows both import and export route target information for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target both`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target both
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target both \<rt-id\></h>

Shows information about both the specified import and export route target for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target both <rt-id>`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target both 65101:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target export</h>

Shows export route target information for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target export`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target export
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target export \<rt-id\></h>

Shows configuration information about a specific export route target for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target export <rt-id>`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target export 65101:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target import</h>

Shows import route target configuration for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target import`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target import
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target import \<rt-id\></h>

Shows configuration information about a specific import route target for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target import <rt-id>`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target import 65102:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> remote-vtep</h>

Shows the remote VTEPs that connect to the switch.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 remote-vtep
           flood
---------  -----
10.0.1.34  HER
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> evpn</h>

Shows EVPN control plane configuration for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond1 evpn
                   applied            pending          
-----------------  -----------------  -----------------
multihoming                                            
  uplink           off                off              
  segment                                              
    enable         on                 on               
    df-preference  50000              50000            
    local-id       1                  1                
    mac-address    44:38:39:BE:EF:AA  44:38:39:BE:EF:AA
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> evpn multihoming</h>

Shows the EVPN multihoming interface configuration parameters.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond1 evpn multihoming
                 operational  applied            pending          
---------------  -----------  -----------------  -----------------
uplink                        off                off              
segment                                                           
  enable                      on                 on               
  df-preference               50000              50000            
  local-id                    1                  1                
  mac-address                 44:38:39:BE:EF:AA  44:38:39:BE:EF:AA
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> evpn multihoming segment</h>

Shows EVPN multihoming interface segment configuration.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond1 evpn multihoming segment
               operational  applied            pending          
-------------  -----------  -----------------  -----------------
enable                      on                 on               
df-preference               50000              50000            
local-id                    1                  1                
mac-address                 44:38:39:BE:EF:AA  44:38:39:BE:EF:AA
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn</h>

Shows EVPN control plane configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn
                    operational        applied  pending
------------------  -----------------  -------  -------
enable                                 on       on     
vlan                220                auto     auto   
[vni]               4001               4001     4001   
router-mac          44:38:39:22:01:7a                  
state               Up                                 
svi                 vlan220_l3                         
system-mac          44:38:39:22:01:7a                  
vxlan-interface     vxlan99                            
prefix-routes-only  off                off      off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn bgp-info</h>

Shows layer 3 VNI information from BGP.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn bgp-info
                       operational        applied  pending
---------------------  -----------------  -------  -------
local-vtep             10.0.0.1                           
rd                     10.10.10.1:6                       
router-mac             44:38:39:22:01:7a                  
system-ip              10.10.10.1                         
system-mac             44:38:39:22:01:7a                  
[export-route-target]  65101:4001                         
[import-route-target]  65101:4001
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn nexthop-vtep</h>

Shows the EVPN next hop VTEP for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn nexthop-vtep
Nexthop     router-mac       
----------  -----------------
10.10.10.2  44:38:39:22:01:78
10.10.10.3  44:38:39:22:01:84
10.10.10.4  44:38:39:22:01:8a
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn nexthop-vtep \<nexthop-vtep-id\></h>

Shows information about a specific EVPN next hop VTEP in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<nexthop-vtep-id>` | The IP address of the nexthop VTEP.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn nexthop-vtep 10.10.10.2
            operational        applied  pending
----------  -----------------  -------  -------
router-mac  44:38:39:22:01:78
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn remote-router-mac</h>

Shows the EVPN remote router MAC addresses in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn remote-router-mac
MAC address        remote-vtep
-----------------  -----------
44:38:39:22:01:8a  10.10.10.4 
44:38:39:22:01:78  10.10.10.2 
44:38:39:22:01:84  10.10.10.3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn remote-router-mac \<mac-address-id\></h>

Shows information about a specific EVPN remote router MAC address in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<mac-address-id>` | The MAC address.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn remote-router-mac 44:38:39:22:01:8a
             operational  applied  pending
-----------  -----------  -------  -------
remote-vtep  10.10.10.4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn vni</h>

Shows all EVPN VNIs in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn vni

----
4001
```
