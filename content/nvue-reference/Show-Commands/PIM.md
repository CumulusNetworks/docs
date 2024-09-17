---
title: PIM
author: Cumulus Networks
weight: 260

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router pim</h>

Shows <span class="a-tooltip">[PIM](## "Protocol Independent Multicast")</span> configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`  |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 router pim
                            applied    
--------------------------  -----------
enable                      on         
active-active               off        
dr-priority                 1          
address-family                         
  ipv4-unicast                         
    multicast-boundary-oil  MyPrefixLis
    use-source              none       
    allow-rp                           
      enable                off        
bfd                                    
  enable                    off        
timers                                 
  hello-interval            auto
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router pim address-family</h>

Shows PIM configuration settings for all address families for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 router pim address-family
                          applied    
------------------------  -----------
ipv4-unicast                         
  multicast-boundary-oil  MyPrefixLis
  use-source              none       
  allow-rp                           
    enable                off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router pim address-family ipv4-unicast</h>

Shows IPv4 PIM configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 router pim address-family ipv4-unicast
                        applied    
----------------------  -----------
multicast-boundary-oil  MyPrefixLis
use-source              none       
allow-rp                           
  enable                off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router pim address-family ipv4-unicast allow-rp</h>

Shows PIM allow RP configuration settings for IPv4 for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 router pim address-family ipv4-unicast allow-rp
        applied
------  -------
enable  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router pim bfd</h>

Shows PIM BFD configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 router pim bfd
        applied
------  -------
enable  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router pim timers</h>

Shows PIM timer settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 router pim timers
                applied
--------------  -------
hello-interval  auto
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pim</h>

Shows global PIM configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router pim
                       applied
---------------------  -------
enable                 on     
packets                3      
timers                        
  hello-interval       30     
  join-prune-interval  100    
  keep-alive           10000  
  register-suppress    20000  
  rp-keep-alive        185
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pim timers</h>

Shows global PIM timer settings on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router pim timers
                     applied
-------------------  -------
hello-interval       30     
join-prune-interval  100    
keep-alive           10000  
register-suppress    20000  
rp-keep-alive        185
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim</h>

Shows PIM configuration settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim
                          applied         
------------------------  ----------------
enable                    on              
address-family                            
  ipv4-unicast                            
    register-accept-list  none            
    send-v6-secondary     on              
    ssm-prefix-list       MyCustomSSMrange
    [rp]                  10.10.10.101    
    spt-switchover                        
      action              infinity        
      prefix-list         SPTrange        
ecmp                                      
  enable                  on              
  rebalance               on              
timers                                    
  keep-alive              auto            
  rp-keep-alive           auto
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim address-family</h>

Shows address family specific PIM configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim address-family
                       applied         
----------------------  ----------------
ipv4-unicast                            
  register-accept-list  none            
  send-v6-secondary     on              
  ssm-prefix-list       MyCustomSSMrange
  [rp]                  10.10.10.101    
  spt-switchover                        
    action              infinity        
    prefix-list         SPTrange
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim address-family ipv4</h>

Shows IPv4 PIM configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim address-family ipv4
                      applied         
--------------------  ----------------
register-accept-list  none            
send-v6-secondary     on              
ssm-prefix-list       MyCustomSSMrange
[rp]                  10.10.10.101    
spt-switchover                        
  action              infinity        
  prefix-list         SPTrange
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim address-family ipv4 rp \<rp-id\></h>

Shows IPv4 PIM configuration settings for a specific <span class="a-tooltip">[RP](## "Rendezvous Point")</span> for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<rp-id>` |  RP IP address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim address-family ipv4 rp 10.10.10.101
               applied    
-------------  -----------
[group-range]  224.0.0.0/4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim address-family ipv4 rp \<rp-id\> group-range</h>

Shows the group ranges for the IPv4 PIM <span class="a-tooltip">[RP](## "Rendezvous Point")</span> for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<rp-id>`  | RP IP address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim address-family ipv4 rp 10.100.100.100 group-range
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim address-family ipv4 rp \<rp-id\> group-range \<group-range-id\></h>

Shows IPv4 PIM configuration settings for a specific <span class="a-tooltip">[RP](## "Rendezvous Point")</span> group range for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<rp-id>`  | RP IP address |
| `<group-range-id>`  |  The group range associated with the RP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim address-family ipv4 rp 10.100.100.100 group-range 224.0.0.0/4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim address-family ipv4 spt-switchover</h>

Shows IPv4 PIM <span class="a-tooltip">[SPT](## "Shortest Path Tree")</span> switchover configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim address-family ipv4 spt-switchover
             applied 
-----------  --------
action       infinity
prefix-list  SPTrange
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim ecmp</h>

Shows PIM ECMP settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim ecmp
           applied
---------  -------
enable     on     
rebalance  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim msdp-mesh-group</h>

Shows the MSDP mesh groups for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim msdp-mesh-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\></h>

Shows specific MSDP mesh group information for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<msdp-mesh-group-id>` |  The MSDP mesh group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim msdp-mesh-group pod1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> member-address</h>

Shows the MSDP mesh group members for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<msdp-mesh-group-id>` |  The MSDP mesh group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim msdp-mesh-group pod1 member-address
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> member-address \<mesh-member-id\></h>

Shows information about the specified MSDP mesh group member for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<msdp-mesh-group-id>` |  The MSDP mesh group name. |
| `<mesh-member-id>`      | The IP address of the MSDP mesh group member.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim msdp-mesh-group pod1 member-address 10.1.10.102
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router pim timers</h>

Shows PIM timer settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router pim timers
               applied
-------------  -------
keep-alive     auto   
rp-keep-alive  auto
```
