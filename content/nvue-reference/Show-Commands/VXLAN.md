---
title: VXLAN
author: Cumulus Networks
weight: 450

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan</h>

Shows global VXLAN configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan
                          operational  applied 
------------------------  -----------  --------
enable                    on           on      
arp-nd-suppress           on           on      
mac-learning              off          off     
mtu                       9216         9216    
port                      4789         4789    
decapsulation                                  
  dscp                                         
    action                derive       derive  
encapsulation                                  
  dscp                                         
    action                derive       derive  
flooding                                       
  enable                  on           on      
  [head-end-replication]  evpn         evpn    
mlag                                           
  shared-address          none         none    
source                                         
  address                 10.0.0.1     10.0.0.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan decapsulation

Shows VXLAN decapsulation configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show nve vxlan decapsulation
          operational  applied
--------  -----------  -------
dscp                          
  action  derive       derive
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan decapsulation dscp</h>

Shows the configured DSCP action and value during VXLAN decapsulation.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show nve vxlan decapsulation dscp
        operational  applied
------  -----------  -------
action  derive       derive
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan encapsulation

Shows VXLAN encapsulation configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show nve vxlan encapsulation
          operational  applied
--------  -----------  -------
dscp                          
  action  derive       derive
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv show nve vxlan encapsulation dscp</h>

Shows the configured DSCP action and value during VXLAN encapsulation.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show nve vxlan encapsulation dscp
        operational  applied
------  -----------  -------
action  derive       derive 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan flooding</h>

Shows VXLAN flooding configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan flooding
                        operational  applied
----------------------  -----------  -------
enable                  on           on     
[head-end-replication]  evpn         evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan flooding head-end-replication</h>

Shows VXLAN head end replication information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan flooding head-end-replication
IP Address
----------
evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan flooding head-end-replication \<hrep-id\></h>

Shows VXLAN head end replication information for the specified IP address or for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<hrep-id>` | The IPv4 unicast address or `evpn`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan flooding head-end-replication evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan mlag</h>

Shows VXLAN specific MLAG configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan mlag
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan source</h>

Shows the VXLAN source address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan source
         operational  applied 
-------  -----------  --------
address  10.0.0.1     10.0.0.1
```
