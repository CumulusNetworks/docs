---
title: System Forwarding
author: Cumulus Networks
weight: 400

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system forwarding</h>

Shows traffic forwarding configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show system forwarding
                          applied
------------------------  -------
ecmp-hash                        
  destination-ip          on     
  destination-port        on     
  gtp-teid                off    
  ingress-interface       off    
  inner-destination-ip    off    
  inner-destination-port  off    
  inner-ip-protocol       off    
  inner-ipv6-label        off    
  inner-source-ip         off    
  inner-source-port       off    
  ip-protocol             on     
  ipv6-label              on     
  source-ip               on     
  source-port             on     
lag-hash                         
  destination-ip          on     
  destination-mac         on     
  destination-port        on     
  ether-type              on     
  gtp-teid                off    
  ip-protocol             on     
  source-ip               on     
  source-mac              on     
  source-port             on     
  vlan                    on     
programming                      
  log-level               info   
host-route-preference     route 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system forwarding ecmp-hash</h>

Shows traffic forwarding ECMP hash configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show system forwarding ecmp-hash
                       applied
----------------------  -------
destination-ip          on     
destination-port        on     
gtp-teid                off    
ingress-interface       off    
inner-destination-ip    off    
inner-destination-port  off    
inner-ip-protocol       off    
inner-ipv6-label        off    
inner-source-ip         off    
inner-source-port       off    
ip-protocol             on     
ipv6-label              on     
source-ip               on     
source-port             on  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system forwarding ecmp-weight-normalisation</h>

Shows ECMP weight normaliazation configuration settings.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system forwarding ecmp-weight-normalisation
               applied  pending
-------------  -------  -------
mode           enabled  enabled
max-hw-weight  32       32  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system forwarding lag-hash</h>

Shows traffic forwarding LAG hash configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show system forwarding lag-hash
                  applied
----------------  -------
destination-ip    on     
destination-mac   on     
destination-port  on     
ether-type        on     
gtp-teid          off    
ip-protocol       on     
source-ip         on     
source-mac        on     
source-port       on     
vlan              on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system forwarding programming</h>

Shows traffic forwarding log-level configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system forwarding programming
          applied
---------  -------
log-level  info
```
