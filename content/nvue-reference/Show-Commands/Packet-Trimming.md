---
title: Packet Trimming
author: Cumulus Networks
weight: 245

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> packet-trim</h>

Shows packet trimming information for an interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show interface swp1-3 packet-trim
Egress Eligibility TC
========================
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> counters packet-trim</h>

Shows the number of trimmed packets for a specific interface by traffic class.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show interface swp1-3 counters packet-trim
Traffic Class  Trim Eligible Packets 
-------------  --------------- 
1                 1000                
2                 2000              
3                 3000 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> packet-trim egress-eligibility</h>

Shows packet trimming eligibility information for an interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show interface swp1-3 packet-trim egress-eligibility
Egress Eligibility TC
========================
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> packet-trim egress-eligibility traffic-class</h>

Shows packet trimming eligibility traffic class information for an interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show interface swp1-3 packet-trim egress-eligibility traffic-class
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> packet-trim egress-eligibility traffic-class \<tc-id\></h>

Shows packet trimming eligibility information for a specific traffic class.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<tc-id>` | The traffic class ID.|

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show interface swp1-3 packet-trim egress-eligibility traffic-class 4
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system forwarding packet-trim</h>

Shows packet trimming configuration and data. The `trimmed-packet-counters` field shows the number of trimmed packets.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show system forwarding packet-trim
nv show system forwarding packet-trim 
                           operational                           applied                         
-------------------------  ------------------------------------  -------------------  
state                      disabled                              enabled                       
profile                                                          packet-trim-default  
service-port               swp65                                                                         
size                       253                                                                           
traffic-class              4                                                                             
switch-priority            4                                                                             
remark                                                                                                   
  dscp                     11                                                                            
session-info                                                                                             
  session-id               0xffff                                                                        
  trimmed-packet-counters  0                                                                             
  session-down-reason      Failed to create/update span session                                          

Egress Eligibility TC-to-Interface Information
=================================================
    TC  interface              
    --  -----------------------
    1   swp1-60,63-64,swp61s0-7
    2   swp1-60,63-64,swp61s0-7
    3   swp1-60,63-64,swp61s0-7

Port-Level SP to DSCP Remark Information
===========================================
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system forwarding packet-trim remark</h>

Shows packet trimming remark information.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show system forwarding packet-trim remark 
      operational  applied
----  -----------  -------
dscp               11
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system forwarding packet-trim counters</h>

Shows the number of trimmed packets at both the global and interface levels.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system forwarding packet-trim counters
Global 
 trimmed-packets      20,000 
Port-Level 
------------- 
Interface  Trim Eligible Packets Trimmed TxPackets 
---------  ------------------  ---------------- 
swp1        1000                  N/A 
swp2        2000                  N/A 
swp3        4000                  N/A 
swp4        5000                  N/A
```

