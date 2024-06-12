---
title: QoS
author: Cumulus Networks
weight: 320

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos</h>

Shows QoS configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 qos
                  operational  applied    
----------------  -----------  -----------
egress-scheduler                          
  profile                      list2      
mapping                                   
  profile                      customports
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos buffer</h>

Shows QoS buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos buffer
Buffer Statistics - Ingress Port
===================================
    Pool ID  Mode     Reserved Size  Current Usage  Max Usage  Shared Max
    -------  -------  -------------  -------------  ---------  ----------
    1        DYNAMIC  0 Bytes        0 Bytes        0 Bytes    ALPHA_8   
    2        DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_8   

Buffer Statistics - Ingress Priority Group
=============================================
    priori…  Pool ID  Mode     Reserv…  Current  Max      Shared  Lossy/…  XON Th  XOFF Th  HR      HR/PL    HR/PL   
                               Size     Usage    Usage    Max                                       Usage    Max     
    ------…  -------  -------  ------…  ------…  ------…  -----…  ------…  -----…  -------  -----…  ------…  -------…
    0        2        DYNAMIC  0 Bytes  0 Bytes  0 Bytes  ALPHA…  Lossy    0       0 Bytes  18.98   0 Bytes  0 Bytes 
                                                                           Bytes            KB                       
    9        1        DYNAMIC  9.98 KB  0 Bytes  0 Bytes  ALPHA…  Lossy    0       0 Bytes  9.98    0 Bytes  0 Bytes 
                                                                           Bytes            KB                       

Buffer Statistics - Egress Port
==================================
    Pool ID  Mode     Reserved Size  Current Usage  Max Usage  Shared Max
    -------  -------  -------------  -------------  ---------  ----------
    12       DYNAMIC  0 Bytes        0 Bytes        0 Bytes    ALPHA_8   
    13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_16  

Buffer - Egress Traffic Class
================================
    traffic-class  Pool ID  Mode          Reserved Size  Current Usage  Max Usage  Shared Max
    -------------  -------  ------------  -------------  -------------  ---------  ----------
    0              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
    1              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
    2              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
    3              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
    4              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
    5              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
    6              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
    7              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
    8              10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
    9              10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
    10             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
    11             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
    12             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
    13             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
    14             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
    15             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
    16             12       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   

Buffer - Egress Multicast
============================
    Pool ID  Mode          Reserved Size  Current Usage  Max Usage  Shared Max
    -------  ------------  -------------  -------------  ---------  ----------
    10       BUFFER UNITS  9.98 KB        0 Bytes        0 Bytes    90.00 KB  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos buffer ingress-port</h>

Shows QoS ingress port buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos buffer ingress-port
Pool ID  Mode     Reserved Size  Current Usage  Max Usage  Shared Max
-------  -------  -------------  -------------  ---------  ----------
1        DYNAMIC  0 Bytes        0 Bytes        0 Bytes    ALPHA_8   
2        DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_8 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos buffer ingress-priority-group</h>

Shows QoS priority group ingress buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos buffer ingress-priority-group
priori…  Pool ID  Mode     Reserv…  Current  Max      Shared    Lossy/…  XON Th   XOFF Th  HR        HR/PL    HR/PL Max
                           Size     Usage    Usage    Max                                            Usage             
------…  -------  -------  ------…  ------…  ------…  -------…  ------…  -------  -------  --------  ------…  ---------
0        2        DYNAMIC  0 Bytes  0 Bytes  0 Bytes  ALPHA_8   Lossy    0 Bytes  0 Bytes  18.98 KB  0 Bytes  0 Bytes  
9        1        DYNAMIC  9.98 KB  0 Bytes  0 Bytes  ALPHA_8   Lossy    0 Bytes  0 Bytes  9.98 KB   0 Bytes  0 Bytes
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos buffer egress-port</h>

Shows QoS egress port buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos buffer egress-port
Pool ID  Mode     Reserved Size  Current Usage  Max Usage  Shared Max
-------  -------  -------------  -------------  ---------  ----------
12       DYNAMIC  0 Bytes        0 Bytes        0 Bytes    ALPHA_8   
13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_16
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos buffer egress-traffic-class</h>

Shows QoS egress traffic class buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos buffer egress-traffic-class
traffic-class  Pool ID  Mode          Reserved Size  Current Usage  Max Usage  Shared Max
-------------  -------  ------------  -------------  -------------  ---------  ----------
0              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
1              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
2              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
3              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
4              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
5              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
6              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
7              13       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8   
8              10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
9              10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
10             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
11             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
12             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
13             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
14             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
15             10       BUFFER UNITS  0 Bytes        0 Bytes        0 Bytes    infinity  
16             12       DYNAMIC       1008 Bytes     0 Bytes        0 Bytes    ALPHA_8
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos buffer egress-multicast</h>

Shows QoS egress multicast traffic buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos buffer egress-multicast
Pool ID  Mode          Reserved Size  Current Usage  Max Usage  Shared Max
-------  ------------  -------------  -------------  ---------  ----------
10       BUFFER UNITS  9.98 KB        0 Bytes        0 Bytes    90.00 KB
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos congestion-control</h>

Shows QoS congestion control configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos congestion-control
ECN configuration
====================
    traffic-class  ECN     RED      Min Th     Max Th   Probability
    -------------  ------  -------  ---------  -------  -----------
    0              enable  disable  153.00 KB  1.43 MB  100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos congestion-control traffic-class</h>

Shows QoS congestion control traffic class configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos congestion-control traffic-class
traffic-class  ECN     RED      Min Th     Max Th   Probability
-------------  ------  -------  ---------  -------  -----------
0              enable  disable  153.00 KB  1.43 MB  100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos congestion-control traffic-class \<qos-tc-id\></h>

Shows specific QoS congestion control traffic class configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-tc-id>` | The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos congestion-control traffic-class 0
               operational  applied
-------------  -----------  -------
ecn            enable              
max-threshold  1.43 MB             
min-threshold  153.00 KB           
probability    100                 
red            disable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> counters qos</h>

Shows all QoS statistics for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv show interface <interface-id> qos counters`
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters qos
Ingress Buffer Statistics
============================
    priority-group  rx-frames  rx-buffer-discards  rx-shared-buffer-discards
    --------------  ---------  ------------------  -------------------------
    0               0          0 Bytes             0 Bytes                  
    1               0          0 Bytes             0 Bytes                  
    2               0          0 Bytes             0 Bytes                  
    3               0          0 Bytes             0 Bytes                  
    4               0          0 Bytes             0 Bytes                  
    5               0          0 Bytes             0 Bytes                  
    6               0          0 Bytes             0 Bytes                  
    7               0          0 Bytes             0 Bytes                  

Egress Queue Statistics
==========================
    traffic-class  tx-frames  tx-bytes  tx-uc-buffer-discards  wred-discards
    -------------  ---------  --------  ---------------------  -------------
    0              0          0 Bytes   0 Bytes                0            
    1              0          0 Bytes   0 Bytes                0            
    2              0          0 Bytes   0 Bytes                0            
    3              0          0 Bytes   0 Bytes                0            
    4              0          0 Bytes   0 Bytes                0            
    5              0          0 Bytes   0 Bytes                0            
    6              0          0 Bytes   0 Bytes                0            
    7              0          0 Bytes   0 Bytes                0            

PFC Statistics
=================
    switch-priority  rx-pause-frames  rx-pause-duration  tx-pause-frames  tx-pause-duration
    ---------------  ---------------  -----------------  ---------------  -----------------
    0                0                0                  0                0                
    1                0                0                  0                0                
    2                0                0                  0                0                
    3                0                0                  0                0                
    4                0                0                  0                0                
    5                0                0                  0                0                
    6                0                0                  0                0                
    7                0                0                  0                0                

Qos Port Statistics
======================
    Counter             Receive  Transmit
    ------------------  -------  --------
    ecn-marked-packets  n/a      0       
    mc-buffer-discards  n/a      0       
    pause-frames        0        0
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> counters qos egress-queue-stats</h>

Shows all QoS egress queue statistics for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv show interface <interface-id> qos counters egress-queue-stats`
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters qos egress-queue-stats

ECN configuration
====================
cumulus@leaf01:mgmt:~$ nv show interface swp1 counters qos egress-queue-stats
traffic-class  tx-frames  tx-bytes  tx-uc-buffer-discards  wred-discards
-------------  ---------  --------  ---------------------  -------------
0              0          0 Bytes   0 Bytes                0            
1              0          0 Bytes   0 Bytes                0            
2              0          0 Bytes   0 Bytes                0            
3              0          0 Bytes   0 Bytes                0            
4              0          0 Bytes   0 Bytes                0            
5              0          0 Bytes   0 Bytes                0            
6              0          0 Bytes   0 Bytes                0            
7              0          0 Bytes   0 Bytes                0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> counters qos ingress-buffer-stats</h>

Shows all QoS ingress buffer statistics for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv show interface <interface-id> qos counters ingress-buffer-stats`
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters qos ingress-buffer-stats
priority-group  rx-frames  rx-buffer-discards  rx-shared-buffer-discards
--------------  ---------  ------------------  -------------------------
0               0          0 Bytes             0 Bytes                  
1               0          0 Bytes             0 Bytes                  
2               0          0 Bytes             0 Bytes                  
3               0          0 Bytes             0 Bytes                  
4               0          0 Bytes             0 Bytes                  
5               0          0 Bytes             0 Bytes                  
6               0          0 Bytes             0 Bytes                  
7               0          0 Bytes             0 Bytes
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> counters qos pfc-stats</h>

Shows all QoS PFC statistics for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv show interface <interface-id> qos counters pfc-stats`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters qos pfc-stats
switch-priority  rx-pause-frames  rx-pause-duration  tx-pause-frames  tx-pause-duration
---------------  ---------------  -----------------  ---------------  -----------------
0                0                0                  0                0                
1                0                0                  0                0                
2                0                0                  0                0                
3                0                0                  0                0                
4                0                0                  0                0                
5                0                0                  0                0                
6                0                0                  0                0                
7                0                0                  0                0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> counters qos port-stats</h>

Shows all QoS port statistics for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv show interface <interface-id> qos counters port-stats`
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters qos port-stats
Counter             Receive  Transmit
------------------  -------  --------
ECN Marked Packets  n/a      0       
MC Buffer Discards  n/a      0       
Pause Frames        0        0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos egress-queue-mapping</h>

Shows QoS egress queue mapping configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos egress-queue-mapping
SP->TC mapping configuration
===============================
    switch-priority  traffic-class
    ---------------  -------------
    0                0            
    1                1            
    2                2            
    3                3            
    4                4            
    5                5            
    6                6            
    7                7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos egress-queue-mapping switch-priority</h>

Shows QoS egress queue switch priority mapping configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos egress-queue-mapping switch-priority
switch-priority  traffic-class
---------------  -------------
0                0            
1                1            
2                2            
3                3            
4                4            
5                5            
6                6            
7                7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos egress-queue-mapping switch-priority \<qos-sp-id\></h>

Shows specific QoS egress queue switch priority mapping configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-sp-id>` | The switch priority value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos egress-queue-mapping switch-priority 2
               operational  applied
-------------  -----------  -------
traffic-class  2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos egress-scheduler</h>

Shows QoS egress scheduler configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos egress-scheduler
TC->DWRR weight configuration
================================
    traffic-class  mode  bw-percent
    -------------  ----  ----------
    0              dwrr  12        
    1              dwrr  13        
    2              dwrr  12        
    3              dwrr  13        
    4              dwrr  12        
    5              dwrr  13        
    6              dwrr  12        
    7              dwrr  13
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos egress-scheduler traffic-class</h>

Shows QoS egress scheduler traffic class configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos egress-scheduler traffic-class
traffic-class  mode  bw-percent
-------------  ----  ----------
0              dwrr  12        
1              dwrr  13        
2              dwrr  12        
3              dwrr  13        
4              dwrr  12        
5              dwrr  13        
6              dwrr  12        
7              dwrr  13
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos egress-scheduler traffic-class \<qos-tc-id\></h>

Shows specific QoS egress scheduler traffic class configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-tc-id>` | The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos egress-scheduler traffic-class 2
            operational  applied
----------  -----------  -------
bw-percent  12                  
mode        dwrr
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos egress-shaper</h>

Shows QoS egress shaper configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos egress-shaper
                       operational  applied
---------------------  -----------  -------
port-max-rate          2147483647          
port-max-shaper-state  enable              

Shaper Min/Max Rate
======================
    traffic-class  min-shaper-state  min-rate(kbps)  max-shaper-state  max-rate(kbps)
    -------------  ----------------  --------------  ----------------  --------------
    0              enable            0               enable            2147483647    
    1              enable            0               enable            2147483647    
    2              enable            0               enable            2147483647    
    3              enable            0               enable            2147483647    
    4              enable            0               enable            2147483647    
    5              enable            0               enable            2147483647    
    6              enable            0               enable            2147483647    
    7              enable            0               enable            2147483647 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos egress-shaper traffic-class</h>

Shows QoS egress shaper traffic class configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos egress-shaper traffic-class
traffic-class  min-shaper-state  min-rate(kbps)  max-shaper-state  max-rate(kbps)
-------------  ----------------  --------------  ----------------  --------------
0              enable            0               enable            2147483647    
1              enable            0               enable            2147483647    
2              enable            0               enable            2147483647    
3              enable            0               enable            2147483647    
4              enable            0               enable            2147483647    
5              enable            0               enable            2147483647    
6              enable            0               enable            2147483647    
7              enable            0               enable            2147483647

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos egress-shaper traffic-class \<qos-tc-id\></h>

Shows specific QoS egress shaper traffic class configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-tc-id>` | The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos egress-shaper traffic-class 2
                  operational  applied
----------------  -----------  -------
max-rate          2147483647          
max-shaper-state  enable              
min-rate          0                   
min-shaper-state  enable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos link-pause</h>

Shows QoS link pause configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos link-pause
    operational  applied
--  -----------  -------
rx  disable             
tx  disable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos mapping</h>

Shows QoS mapping configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp1 qos mapping
                 operational  applied
---------------  -----------  -------
port-default-sp  0
trust            l2

PCP->SP mapping configuration
================================
    802.1p  switch-priority
    ------  ---------------
    0       0              
    1       1              
    2       2              
    3       3              
    4       4              
    5       5              
    6       6              
    7       7              

DSCP->SP mapping configuration
=================================
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos mapping dscp</h>

Shows DSCP mapping configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos mapping dscp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos mapping dscp \<qos-dscp-id\></h>

Shows specific DSCP mapping configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-dscp-id>` | The DSCP value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos qos mapping dscp 22
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos mapping pcp</h>

Shows QoS 802.1p (PCP) mapping configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp1 qos mapping pcp
802.1p  switch-priority
------  ---------------
0       0              
1       1              
2       2              
3       3              
4       4              
5       5              
6       6              
7       7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos mapping pcp \<qos-pcp-id\></h>

Shows specific QoS 802.1p (PCP) mapping configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-pcp-id>` | The 802.1p (PCP) value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos mapping pcp 2
                 operational  applied
---------------  -----------  -------
switch-priority  2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos pfc</h>

Shows QoS PFC configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos pfc
    operational  applied
--  -----------  -------
rx  disable             
tx  disable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos remark</h>

Shows QoS remarking configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos remark
SP->PCP/DSCP remark configuration
====================================
    switch-priority  pcp  dscp
    ---------------  ---  ----
    0                0    0   
    1                1    8   
    2                2    16  
    3                3    24  
    4                4    32  
    5                5    40  
    6                6    48  
    7                7    56
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos remark switch-priority</h>

Shows QoS switch priority remarking configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos remark switch-priority
switch-priority  pcp  dscp
---------------  ---  ----
0                0    0   
1                1    8   
2                2    16  
3                3    24  
4                4    32  
5                5    40  
6                6    48  
7                7    56

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos remark switch-priority \<qos-sp-id\></h>

Shows specific QoS switch priority remarking configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-sp-id>` | The switch priority value. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos remark switch-priority 2
      operational  applied
----  -----------  -------
dscp  16                  
pcp   2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos roce</h>

Shows a summary of RoCE information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos roce
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos roce counters</h>

Shows RoCE counters for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos roce counters
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos roce status</h>

Shows RoCE status information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp16 qos roce status
                    operational    applied  description
------------------  -------------  -------  ---------------------------------------------------
congestion-control
  congestion-mode   ecn, absolute           Congestion config mode
  enabled-tc        0,3                     Congestion config enabled Traffic Class
  max-threshold     1.43 MB                 Congestion config max-threshold
  min-threshold     153.00 KB               Congestion config min-threshold
pfc
  pfc-priority      3                       switch-prio on which PFC is enabled
  rx-enabled        yes                     PFC Rx Enabled status
  tx-enabled        yes                     PFC Tx Enabled status
trust
  trust-mode        pcp,dscp                Trust Setting on the port for packet classification
mode                lossless                Roce Mode
 
RoCE PCP/DSCP->SP mapping configurations
===========================================
          pcp  dscp  switch-prio
    ----  ---  ----  -----------
    cnp   6    48    6
    roce  3    26    3
 
RoCE SP->TC mapping and ETS configurations
=============================================
          switch-prio  traffic-class  scheduler-weight
    ----  -----------  -------------  ----------------
    cnp   6            6              strict priority
    roce  3            3              dwrr-50%
 
RoCE Pool Status
===================
        name                   mode     pool-id  switch-priorities  traffic-class  size      current-usage  max-usage
    --  ---------------------  -------  -------  -----------------  -------------  --------  -------------  ---------
    0   lossy-default-ingress  DYNAMIC  2        0,1,2,4,5,6,7      -              15.16 MB  0 Bytes        16.00 MB
    1   roce-reserved-ingress  DYNAMIC  3        3                  -              15.16 MB  7.30 MB        7.90 MB
    2   lossy-default-egress   DYNAMIC  13       -                  0,6            15.16 MB  0 Bytes        16.01 MB
    3   roce-reserved-egress   DYNAMIC  14       -                  3              inf       7.29 MB        13.47 MB
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos roce status pool-map</h>

Shows ingress and egress service pool configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos roce pool-map
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos roce status prio-map</h>

Shows the RoCE 802.1p (PCP) or DSCP to switch priority mapping configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos roce prio-map
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos roce status tc-map</h>

Shows the RoCE switch priority to traffic class mapping for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp5 qos roce status tc-map
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos pfc-watchdog</h>

Shows if the PFC watchdog setting is ON or OFF and shows the state for each traffic class. PFC watchdog detects and mitigates pause storms on ports where PFC or link pause is ON.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show interface swp1 qos pfc-watchdog
                 operational  applied 
---------------  -----------  ------- 
state            enabled      enabled 

PFC WD Status 
=========================== 
    traffic-class  status    deadlock-count 
    -------------  --------  -------------- 

    0              OK        0 
    1              OK        3 
    2              DEADLOCK  2  
    3              OK        0 
    4              OK        0 
    5              OK        0 
    6              OK        0 
    7              DEADLOCK  3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos pfc-watchdog status</h>

Shows PFC watchdog data for every traffic class. PFC watchdog detects and mitigates pause storms on ports where PFC or link pause is ON.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show interface swp1 qos pfc-watchdog status
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> qos pfc-watchdog status \<qos-tc-id\></h>

Shows PFC watchdog data for a specific traffic class. PFC watchdog detects and mitigates pause storms on ports where PFC or link pause is ON.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-tc-id>` | The Traffic class. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show interface swp1 qos pfc-watchdog status 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos</h>

Shows detailed information about the configured buffers, utilization, and DSCP markings for QoS.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config</h>

Shows QoS advanced buffer configuration.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config -o json
{
  "default-global": {
    "egress-lossy-buffer": {
      "multicast-switch-priority": {
        "0": {
          "service-pool": "0"
        },
        "1": {
          "service-pool": "0"
        },
        "2": {
          "service-pool": "0"
        },
        "3": {
          "service-pool": "0"
        },
        "4": {
          "service-pool": "0"
        },
        "5": {
          "service-pool": "0"
        },
        "6": {
          "service-pool": "0"
        },
        "7": {
          "service-pool": "0"
        }
      },
      "traffic-class": {
        "0": {
          "service-pool": "0"
        },
        "1": {
          "service-pool": "0"
        },
        "2": {
          "service-pool": "0"
        },
        "3": {
          "service-pool": "0"
        },
        "4": {
          "service-pool": "0"
        },
        "5": {
          "service-pool": "0"
        },
        "6": {
          "service-pool": "0"
        },
        "7": {
          "service-pool": "0"
        }
      }
    },
    "egress-pool": {
      "0": {
        "memory-percent": 100,
        "mode": "dynamic"
      }
    },
    "ingress-lossy-buffer": {
      "priority-group": {
        "bulk": {
          "id": "0",
          "service-pool": "0",
          "switch-priority": {
            "0": {},
            "1": {},
            "2": {},
            "3": {},
            "4": {},
            "5": {},
            "6": {},
            "7": {}
          }
        }
      }
    },
    "ingress-pool": {
      "0": {
        "memory-percent": 100,
        "mode": "dynamic"
      }
    }
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\></h>

Shows configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global
                               operational  applied
-----------------------------  -----------  -------
egress-lossy-buffer                                
  [multicast-switch-priority]  0            0      
  [multicast-switch-priority]  1            1      
  [multicast-switch-priority]  2            2      
  [multicast-switch-priority]  3            3      
  [multicast-switch-priority]  4            4      
  [multicast-switch-priority]  5            5      
  [multicast-switch-priority]  6            6      
  [multicast-switch-priority]  7            7      
  [traffic-class]              0            0      
  [traffic-class]              1            1      
  [traffic-class]              2            2      
  [traffic-class]              3            3      
  [traffic-class]              4            4      
  [traffic-class]              5            5      
  [traffic-class]              6            6      
  [traffic-class]              7            7      
[egress-pool]                  0            0      
ingress-lossy-buffer                               
  [priority-group]             bulk         bulk   
[ingress-pool]                 0            0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> egress-lossless-buffer</h>

Shows egress lossless buffer configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer
                             operational  applied
---------------------------  -----------  -------
[multicast-switch-priority]  0            0      
[multicast-switch-priority]  1            1      
[multicast-switch-priority]  2            2      
[multicast-switch-priority]  3            3      
[multicast-switch-priority]  4            4      
[multicast-switch-priority]  5            5      
[multicast-switch-priority]  6            6      
[multicast-switch-priority]  7            7      
[traffic-class]              0            0      
[traffic-class]              1            1      
[traffic-class]              2            2      
[traffic-class]              3            3      
[traffic-class]              4            4      
[traffic-class]              5            5      
[traffic-class]              6            6      
[traffic-class]              7            7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-port</h>

Shows egress lossless buffer multicast port configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer multicast-port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority</h>

Shows egress lossless buffer multicast switch priority configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority
switch-priority  reserved  service-pool  shared-alpha  shared-bytes
---------------  --------  ------------  ------------  ------------
0                          0                                       
1                          0                                       
2                          0                                       
3                          0                                       
4                          0                                       
5                          0                                       
6                          0                                       
7                          0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\></h>

Shows configuration settings for a specific egress lossless buffer multicast switch priority for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-sp-id>` | The switch priority value.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 2
              operational  applied
------------  -----------  -------
service-pool  0            0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class</h>

Shows egress lossless buffer traffic class configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer traffic-class
traffic-class  reserved  service-pool  shared-alpha  shared-bytes
-------------  --------  ------------  ------------  ------------
0                        0                                       
1                        0                                       
2                        0                                       
3                        0                                       
4                        0                                       
5                        0                                       
6                        0                                       
7                        0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\></h>

Shows configuration settings for a specific egress lossless buffer traffic class for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<traffic-class-id>` | The traffic class value.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer traffic-class 2
              operational  applied
------------  -----------  -------
service-pool  0            0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> egress-pool</h>

Shows all egress service pool settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global egress-pool
Pool-Id  infinite  memory-percent  mode     reserved  shared-alpha  shared-bytes
-------  --------  --------------  -------  --------  ------------  ------------
0                  100             dynamic
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\></h>

Shows configuration settings for a specific egress service pool for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<pool-id>` | The service pool name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global egress-pool 3
                operational  applied
--------------  -----------  -------
memory-percent  100          100    
mode            dynamic      dynamic
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> ingress-lossless-buffer</h>

Shows ingress lossless buffer configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-lossless-buffer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> ingress-lossy-buffer</h>

Shows ingress lossy buffer configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer
                  operational  applied
----------------  -----------  -------
[priority-group]  bulk         bulk
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group</h>

Shows ingress lossy buffer priority group configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group
Priority Group  id  name  reserved  service-pool  shared-alpha  shared-bytes  Summary           
--------------  --  ----  --------  ------------  ------------  ------------  ------------------
bulk            0                   0                                         switch-priority: 0
                                                                              switch-priority: 1
                                                                              switch-priority: 2
                                                                              switch-priority: 3
                                                                              switch-priority: 4
                                                                              switch-priority: 5
                                                                              switch-priority: 6
                                                                              switch-priority: 7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\></h>

Shows configuration for a specific ingress lossy buffer priority group for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<priority-group-id>` | The priority group name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group bulk
                   operational  applied
-----------------  -----------  -------
id                 0                   
service-pool       0            0      
[switch-priority]  0            0      
[switch-priority]  1            1      
[switch-priority]  2            2      
[switch-priority]  3            3      
[switch-priority]  4            4      
[switch-priority]  5            5      
[switch-priority]  6            6      
[switch-priority]  7            7 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> switch-priority</h>

Shows ingress lossy buffer priority group switch priorities for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<priority-group-id>` | The priority group name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group bulk switch-priority
switch-priority
---------------
0              
1              
2              
3              
4              
5              
6              
7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> switch-priority \<qos-sp-id\></h>

Shows configuration settings for a specific ingress lossy buffer priority group switch priority for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<priority-group-id>` | The priority group name.|
| `<qos-sp-id>` | The switch priority value.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 switch-priority 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> ingress-pool</h>

Shows all ingress service pool settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-pool
Pool-Id  infinite  memory-percent  mode     reserved  shared-alpha  shared-bytes
-------  --------  --------------  -------  --------  ------------  ------------
0                  80              dynamic                                      
3                  20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\></h>

Shows configuration settings for a specific ingress service pool for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<pool-id>` | The service pool name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-pool 3
                operational  applied
--------------  -----------  -------
memory-percent  100          100    
mode            dynamic      dynamic
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config default-global egress-mgmt-buffer</h>

Shows the lossy egress management buffer settings that you can configure to isolate management traffic to a different priority group. Management traffic consists of OSPF and BGP hello and update packets, and BFD packets that ingress and egress the CPU. Cumulus Linux uses traffic class `tc[16]` for egress management buffer traffic, which has a dedicated pool that other traffic cannot share.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global egress-mgmt-buffer 
              operational       applied 
------------  -----------       ---- 
reserved       1200 Bytes       1200 Bytes 
shared-bytes   13.53 KB         13.53 KB 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos advance-buffer-config default-global ingress-mgmt-buffer</h>

Shows the lossy ingress management buffer settings that you can configure to isolate management traffic to a different priority group. Management traffic consists of OSPF and BGP hello and update packets, and BFD packets that ingress and egress the CPU. Cumulus Linux uses priority group `pg[9]` for ingress management buffer traffic.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-mgmt-buffer
              operational       applied
------------  -----------       ---- 
headroom       1000 Bytes       1000 Bytes 
shared-bytes   19.53 KB         19.53 KB 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos buffer</h>

Shows QoS buffer configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos buffer
Pool Buffers Occupancy Counters
==================================
    Pool ID  Pool Type               Direction  Mode          Pool Size  Current Usage  Max Usage
    -------  ----------------------  ---------  ------------  ---------  -------------  ---------
    0        Ingress Data            INGRESS    DYNAMIC       25.14 MB   0 Bytes        0 Bytes  
    1        Ingress Management      INGRESS    DYNAMIC       255.94 KB  0 Bytes        0 Bytes  
    2        User data buffer        INGRESS    DYNAMIC       29.99 MB   0 Bytes        0 Bytes  
    10       Multicast               EGRESS     BUFFER UNITS  32.75 MB   0 Bytes        0 Bytes  
    11       Egress Data             EGRESS     DYNAMIC       25.14 MB   0 Bytes        0 Bytes  
    12       Egress Management       EGRESS     DYNAMIC       255.94 KB  0 Bytes        0 Bytes  
    13       User data buffer        EGRESS     DYNAMIC       29.99 MB   0 Bytes        0 Bytes  
    21       Ingress Descriptor      INGRESS    DYNAMIC       18.81 MB   0 Bytes        0 Bytes  
    22       User descriptor buffer  INGRESS    DYNAMIC       18.01 MB   0 Bytes        0 Bytes  
    30       Egress Descriptor       EGRESS     DYNAMIC       18.81 MB   0 Bytes        0 Bytes  
    31       User descriptor buffer  EGRESS     DYNAMIC       18.01 MB   0 Bytes        0 Bytes

Buffer - Multicast Switch Priority
=====================================
    switch-priority  Pool ID  Mode     Reserved Size  Current Usage  Max Usage  Shared Max
    ---------------  -------  -------  -------------  -------------  ---------  ----------
    0                13       DYNAMIC  9.98 KB        0 Bytes        288 Bytes  ALPHA_1_4 
    1                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
    2                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
    3                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
    4                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
    5                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
    6                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
    7                13       DYNAMIC  9.98 KB        0 Bytes        288 Bytes  ALPHA_1_4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos buffer pool</h>

Shows QoS buffer traffic pool configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos buffer pool
Pool ID  Pool Type               Direction  Mode          Pool Size  Current Usage  Max Usage
-------  ----------------------  ---------  ------------  ---------  -------------  ---------
0        Ingress Data            INGRESS    DYNAMIC       25.14 MB   0 Bytes        0 Bytes  
1        Ingress Management      INGRESS    DYNAMIC       255.94 KB  0 Bytes        0 Bytes  
2        User data buffer        INGRESS    DYNAMIC       29.99 MB   0 Bytes        0 Bytes  
10       Multicast               EGRESS     BUFFER UNITS  32.75 MB   0 Bytes        0 Bytes  
11       Egress Data             EGRESS     DYNAMIC       25.14 MB   0 Bytes        0 Bytes  
12       Egress Management       EGRESS     DYNAMIC       255.94 KB  0 Bytes        0 Bytes  
13       User data buffer        EGRESS     DYNAMIC       29.99 MB   0 Bytes        0 Bytes  
21       Ingress Descriptor      INGRESS    DYNAMIC       18.81 MB   0 Bytes        0 Bytes  
22       User descriptor buffer  INGRESS    DYNAMIC       18.01 MB   0 Bytes        0 Bytes  
30       Egress Descriptor       EGRESS     DYNAMIC       18.81 MB   0 Bytes        0 Bytes  
31       User descriptor buffer  EGRESS     DYNAMIC       18.01 MB   0 Bytes        0 Bytes
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos buffer multicast-switch-priority</h>

Shows QoS buffer multicast switch priority configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos buffer multicast-switch-priority
switch-priority  Pool ID  Mode     Reserved Size  Current Usage  Max Usage  Shared Max
---------------  -------  -------  -------------  -------------  ---------  ----------
0                13       DYNAMIC  9.98 KB        0 Bytes        288 Bytes  ALPHA_1_4 
1                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
2                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
3                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
4                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
5                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
6                13       DYNAMIC  9.98 KB        0 Bytes        0 Bytes    ALPHA_1_4 
7                13       DYNAMIC  9.98 KB        0 Bytes        288 Bytes  ALPHA_1_4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos congestion-control</h>

Shows QoS congestion control configuration settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos congestion-control
Profile         Summary         
--------------  ----------------
default-global  traffic-class: 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos congestion-control \<profile-id\></h>

Shows configuration settings for the specified QoS congestion control profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos congestion-control default-global
    operational  applied  description
--  -----------  -------  -----------

ECN Configurations
=====================
    traffic-class  ECN     RED     Min Th   Max Th    Probability
    -------------  ------  ------  -------  --------  -----------
    4              enable  enable  40000 B  200000 B  100
    5              enable  enable  40000 B  200000 B  100
    7              enable  enable  40000 B  200000 B  100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos congestion-control \<profile-id\> traffic-class</h>

Shows traffic class configuration settings for the specified QoS congestion control profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos congestion-control default-global traffic-class
traffic-class  ECN     RED      Min Th     Max Th   Probability
-------------  ------  -------  ---------  -------  -----------
0              enable  disable  146.48 KB  1.43 MB  100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\></h>

Shows specific traffic class configuration settings for the specified QoS congestion control profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-tc-id>` | The traffic class (egress queue).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos congestion-control default-global traffic-class 4
               operational  applied   description
-------------  -----------  --------  -----------------------------------
ecn            enable       enable    Early Congestion Notification State
max-threshold  200000 B     200000 B  Maximum Threshold (in bytes)
min-threshold  40000 B      40000 B   Minimum Threshold (in bytes)
probability    100          100       Probability
red            enable       enable    Random Early Detection State
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-queue-mapping</h>

Shows egress queue mapping configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos egress-queue-mapping
Profile         Summary           
--------------  ------------------
default-global  switch-priority: 0
                switch-priority: 1
                switch-priority: 2
                switch-priority: 3
                switch-priority: 4
                switch-priority: 5
                switch-priority: 6
                switch-priority: 7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-queue-mapping \<profile-id\></h>

Shows configuration settings for the specified egress queue mapping profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos egress-queue-mapping default-global
    operational  applied  description
--  -----------  -------  -----------

SP->TC mapping configuration
===============================
    switch-priority  traffic-class
    ---------------  -------------
    0                0
    1                1
    2                7
    3                3
    4                4
    5                5
    6                6
    7                7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-queue-mapping \<profile-id\> switch-priority</h>

Shows switch priority configuration settings for the specified egress queue mapping profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos egress-queue-mapping default-global switch-priority
switch-priority  traffic-class
---------------  -------------
0                0            
1                1            
2                2            
3                3            
4                4            
5                5            
6                6            
7                7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-queue-mapping \<profile-id\> switch-priority \<qos-sp-id\></h>

Shows specific switch priority configuration settings for the specified egress queue mapping profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-sp-id>` | The switch priority value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos egress-queue-mapping default-global switch-priority 2
               operational  applied  description
-------------  -----------  -------  -------------
traffic-class  7            7        Traffic Class
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-scheduler</h>

Shows QoS egress scheduler configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos egress-scheduler
Profile         Summary         
--------------  ----------------
default-global  traffic-class: 0
                traffic-class: 1
                traffic-class: 2
                traffic-class: 3
                traffic-class: 4
                traffic-class: 5
                traffic-class: 6
                traffic-class: 7
list1           traffic-class: 0
                traffic-class: 1
                traffic-class: 2
                traffic-class: 3
                traffic-class: 4
                traffic-class: 5
                traffic-class: 6
                traffic-class: 7
list2           traffic-class: 0
                traffic-class: 1
                traffic-class: 2
                traffic-class: 3
                traffic-class: 4
                traffic-class: 5
                traffic-class: 6
                traffic-class: 7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-scheduler \<profile-id\></h>

Shows configuration settings for the specified QoS egress scheduler profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos egress-scheduler default-global
    operational  applied  description
--  -----------  -------  -----------

TC->DWRR weight configuration
================================
    traffic-class  mode    bw-percent
    -------------  ------  ----------
    0              strict
    1              strict
    2              dwrr    30
    3              dwrr    20
    4              dwrr    20
    5              strict
    6              dwrr    30
    7              strict
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-scheduler \<profile-id\> traffic-class</h>

Shows traffic class configuration settings for the specified QoS egress scheduler profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos egress-scheduler default-global traffic-class
traffic-class  mode  bw-percent
-------------  ----  ----------
0              dwrr  12        
1              dwrr  13        
2              dwrr  12        
3              dwrr  13        
4              dwrr  12        
5              dwrr  13        
6              dwrr  12        
7              dwrr  13
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\></h>

Shows specific traffic class configuration settings for the specified QoS egress scheduler profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-tc-id>` | The traffic class (egress queue).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos egress-scheduler default-global traffic-class 2
            operational  applied
----------  -----------  -------
bw-percent  12           12     
mode        dwrr         dwrr
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-shaper</h>

Shows QoS egress shaper configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos egress-shaper
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-shaper \<profile-id\></h>

Shows configuration settings for the specified QoS egress shaper profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos egress-shaper shaper1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-shaper \<profile-id\> traffic-class</h>

Shows traffic class configuration settings for the specified QoS egress shaper profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos egress-shaper shaper1 traffic-class
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\></h>

Shows specific traffic class configuration settings for the specified QoS egress shaper profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-tc-id>` | The traffic class (egress queue).|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos egress-shaper shaper1 traffic-class 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos link-pause</h>

Shows QoS link pause configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos link-pause
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos link-pause \<profile-id\></h>

Shows configuration settings for the specified QoS link pause profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos link-pause my_pause_ports
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos mapping</h>

Shows QoS mapping configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos mapping
Profile         Port Default SP  Trust  Summary  
--------------  ---------------  -----  ---------
customports     4                port            
default-global  0                l2     802.1p: 0
                                        802.1p: 1
                                        802.1p: 2
                                        802.1p: 3
                                        802.1p: 4
                                        802.1p: 5
                                        802.1p: 6
                                        802.1p: 7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos mapping \<profile-id\></h>

Shows configuration settings for the specified QoS mapping profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos mapping default-global
                 operational  applied  description
---------------  -----------  -------  ----------------------------
port-default-sp  3            3        Port Default Switch Priority
trust            port         port     Port Trust configuration
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos mapping \<profile-id\> pcp</h>

Shows 802.1p mapping configuration settings for the specified profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos mapping default-global pcp
802.1p  switch-priority
------  ---------------
0       0              
1       1              
2       2              
3       3              
4       4              
5       5              
6       6              
7       7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos mapping \<profile-id\> pcp \<qos-pcp-id\></h>

Shows specific 802.1p mapping configuration settings for the specified profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-pcp-id>` | The 802.1p (PCP) value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos mapping default-global pcp 0
                 operational  applied  description
---------------  -----------  -------  ------------------------
switch-priority  4            4        Internal Switch Priority
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos mapping \<profile-id\> dscp</h>

Shows DSCP mapping configuration settings for the specified profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos mapping default-global dscp
DSCP  switch-priority
----  ---------------
0     0              
1     0              
2     0              
3     0              
4     0              
5     0              
6     0              
7     0              
8     1              
9     1              
10    1              
11    1              
12    1              
13    1              
14    1              
15    1              
16    2              
17    2
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos mapping \<profile-id\> dscp \<qos-dscp-id\></h>

Shows specific DSCP mapping configuration settings for the specified profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-dscp-id>` | The DSCP value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos mapping default-global dscp 22
                 operational  applied  description
---------------  -----------  -------  ------------------------
switch-priority  4            4        Internal Switch Priority
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos pfc</h>

Shows QoS PFC configuration settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos pfc
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos pfc \<profile-id\></h>

Shows QoS configuration settings for the specified PFC profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos pfc default-global
                   operational  applied  description
-----------------  -----------  -------  --------------------------------
cable-length       50           50       Cable Length (in meters)
port-buffer        25000 B      25000 B  Port Buffer (in bytes)
rx                 disable      disable  PFC Rx State
tx                 enable       enable   PFC Tx State
xoff-threshold     10000 B      10000 B  Xoff Threshold (in bytes)
xon-threshold      2000 B       2000 B   Xon Threshold (in bytes)
[switch-priority]  0            0        Collection of switch priorities
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos pfc \<profile-id\> switch-priority</h>

Shows switch priority configuration settings for the specified PFC profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos pfc default-global switch-priority
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos pfc \<profile-id\> switch-priority \<qos-sp-id\></h>

Shows specific switch priority configuration settings for the specified PFC profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-sp-id>` | The switch priority value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos pfc default-global switch-priority 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos remark</h>

Shows QoS remarking configuration settings.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos remark
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos remark \<profile-id\></h>

Shows configuration settings for the specified QoS remarking profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos remark default-global
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos remark \<profile-id\> switch-priority</h>

Shows switch priority configuration settings for the specified QoS remarking profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos remark default-global switch-priority
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos remark \<profile-id\> switch-priority \<qos-sp-id\></h>

Shows specific switch priority configuration settings for the specified QoS remarking profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-sp-id>` | The switch priority value.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos remark default-global switch-priority 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos roce</h>

Shows QoS <span class="a-tooltip">[ROCE](## "RDMA over Converged Ethernet")</span> configuration, such as the configured buffers, utilization and DSCP markings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos roce
                    operational  applied
------------------  -----------  -------
enable                           on     
mode                lossy        lossy  
congestion-control                      
  congestion-mode   ECN                 
  enabled-tc        0,3                 
  max-threshold     1.43 MB             
  min-threshold     146.48 KB           
  probability       100                 
lldp-app-tlv                            
  priority          3                   
  protocol-id       4791                
  selector          UDP                 
pfc                                     
  pfc-priority      -                   
trust                                   
  trust-mode        pcp,dscp            

RoCE PCP/DSCP->SP mapping configurations
===========================================
       pcp  dscp                     switch-prio
    -  ---  -----------------------  -----------
    0  0    0,1,2,3,4,5,6,7          0          
    1  1    8,9,10,11,12,13,14,15    1          
    2  2    16,17,18,19,20,21,22,23  2          
    3  3    24,25,26,27,28,29,30,31  3          
    4  4    32,33,34,35,36,37,38,39  4          
    5  5    40,41,42,43,44,45,46,47  5          
    6  6    48,49,50,51,52,53,54,55  6          
    7  7    56,57,58,59,60,61,62,63  7          

RoCE SP->TC mapping and ETS configurations
=============================================
       switch-prio  traffic-class  scheduler-weight
    -  -----------  -------------  ----------------
    0  0            0              DWRR-50%        
    1  1            0              DWRR-50%        
    2  2            0              DWRR-50%        
    3  3            3              DWRR-50%        
    4  4            0              DWRR-50%        
    5  5            0              DWRR-50%        
    6  6            6              strict-priority 
    7  7            0              DWRR-50%        

RoCE pool config
===================
       name                   mode     size  switch-priorities  traffic-class
    -  ---------------------  -------  ----  -----------------  -------------
    0  lossy-default-ingress  Dynamic  50%   0,1,2,4,5,6,7      -            
    1  roce-reserved-ingress  Dynamic  50%   3                  -            
    2  lossy-default-egress   Dynamic  50%   -                  0,6          
    3  roce-reserved-egress   Dynamic  50%   -                  3            

Exception List
=================
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos roce prio-map</h>

Shows QoS ROCE priority map configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos roce prio-map
   pcp  dscp                     switch-prio
-  ---  -----------------------  -----------
0  0    0,1,2,3,4,5,6,7          0          
1  1    8,9,10,11,12,13,14,15    1          
2  2    16,17,18,19,20,21,22,23  2          
3  3    24,25,26,27,28,29,30,31  3          
4  4    32,33,34,35,36,37,38,39  4          
5  5    40,41,42,43,44,45,46,47  5          
6  6    48,49,50,51,52,53,54,55  6          
7  7    56,57,58,59,60,61,62,63  7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos roce tc-map</h>

Shows QoS ROCE traffic class map configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos roce tc-map
   switch-prio  traffic-class  scheduler-weight
-  -----------  -------------  ----------------
0  0            0              DWRR-50%        
1  1            0              DWRR-50%        
2  2            0              DWRR-50%        
3  3            3              DWRR-50%        
4  4            0              DWRR-50%        
5  5            0              DWRR-50%        
6  6            6              strict-priority 
7  7            0              DWRR-50%
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos roce pool-map</h>

Shows QoS ROCE traffic pool map configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos roce pool-map
   name                   mode     size  switch-priorities  traffic-class
-  ---------------------  -------  ----  -----------------  -------------
0  lossy-default-ingress  Dynamic  50%   0,1,2,4,5,6,7      -            
1  roce-reserved-ingress  Dynamic  50%   3                  -            
2  lossy-default-egress   Dynamic  50%   -                  0,6          
3  roce-reserved-egress   Dynamic  50%   -                  3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos roce pool</h>

Shows QoS ROCE traffic pool configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos roce pool
   name                   mode     pool-id  size      current-usage  max-usage
-  ---------------------  -------  -------  --------  -------------  ---------
0  lossy-default-ingress  DYNAMIC  2        14.46 MB  0 Bytes        0 Bytes  
2  lossy-default-egress   DYNAMIC  13       14.46 MB  0 Bytes        0 Bytes
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos traffic-pool</h>

Shows QoS traffic pool configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos traffic-pool
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos traffic-pool \<traffic-pool-id\></h>

Shows configuration settings for a specific QoS traffic pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<traffic-pool-id>` | The traffic pool name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos traffic-pool default-lossy
                   applied
-----------------  -------
memory-percent     80     
[switch-priority]  0      
[switch-priority]  1      
[switch-priority]  2      
[switch-priority]  3      
[switch-priority]  4      
[switch-priority]  5      
[switch-priority]  6      
[switch-priority]  7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos traffic-pool \<traffic-pool-id\> switch-priority</h>

Shows switch priority configuration settings for a specific QoS traffic pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<traffic-pool-id>` | The traffic pool name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos traffic-pool default-lossy switch-priority
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos traffic-pool \<traffic-pool-id\> switch-priority \<qos-sp-id\></h>

Shows configuration settings for a specific switch priority for the specified QoS traffic pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<traffic-pool-id>` | The traffic pool name.|
| `<qos-sp-id>` | The switch priority value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos traffic-pool default-lossy switch-priority 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos pfc-watchdog</h>

Shows PFC watchdog configuration settings. PFC watchdog detects and mitigates pause storms on ports where PFC or link pause is ON. 

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show qos qos pfc-watchdog
                  operational  applied       
----------------  -----------  --------------
polling-interval  0:00:00      0:00:00.100000
robustness        0            3 
```
