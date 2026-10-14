---
title: WJH
author: Cumulus Networks
weight: 460

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh</h>

Shows <span class="a-tooltip">[WJH](## "What Just Happened")</span> configuration on the switch. WJH provides real time visibility into network problems.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system wjh
                operational  applied
---------------  -----------  -------
enable                        on
[channel]
[packet-buffer]
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel</h>

Shows WJH channel configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system wjh channel
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\></h>

Shows configuration for the specified WJH channel on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system wjh channel forwarding
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> trigger</h>

Shows the configuration for packet drop categories in a WJH channel.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system wjh channel forwarding trigger
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold</h>

Shows WJH channel latency and congestion threshold configuration.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold
Latency buffer threshold
===========================
    Traffic Class  Interface  High threshold
    -------------  ---------  --------------
    all            all        1000

Congestion buffer threshold
==============================
    Traffic Class  Interface  High threshold
    -------------  ---------  --------------
    all            swp1       20
                   swp2       20
                   swp3       20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold latency</h>

Shows WJH channel latency threshold information.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold latency
Latency buffer threshold
===========================
    Traffic Class  Interface  High threshold
    -------------  ---------  --------------
    all            all        1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold latency tc</h>

Shows WJH channel latency buffer thresholds for all traffic classes.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold latency tc
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold latency tc \<tc-id\></h>

Shows WJH channel latency buffer thresholds for a specific traffic class.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<tc-id>` |  The traffic class.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold latency tc 3
interface
============
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold latency tc \<tc-id\> interface</h>

Shows WJH channel latency buffer thresholds for traffic class interfaces.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<tc-id>` |  The traffic class.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold latency tc 3 interface
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold latency tc \<tc-id\> interface \<interface-id\></h>

Shows WJH channel latency buffer thresholds for a specific traffic class and interface.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<tc-id>` |  The traffic class.|
| `<interface-id>` |  The interface ID.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold latency tc 3 interface swp1
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold congestion</h>

Shows WJH channel congestion information.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold congestion
Congestion buffer threshold
==============================
    Traffic Class  Interface  High threshold
    -------------  ---------  --------------
    all            swp1       20
                   swp2       20
                   swp3       20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold congestion tc</h>

Shows WJH channel buffer congestion for all traffic classes. 

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold congestion tc
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold congestion tc \<tc-id\></h>

Shows WJH channel buffer congestion for a specific traffic class.
 

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<tc-id>` |  The traffic class.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold congestion tc 3
interface
============
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold congestion tc \<tc-id\> interface</h>

Shows WJH channel buffer congestion for traffic class interfaces. 

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<tc-id>` |  The traffic class.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold congestion tc 3 interface
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> buffer-threshold congestion tc \<tc-id\> interface \<interface-id\></h>

Shows WJH channel buffer congestion for a specific traffic class and interface.  

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<tc-id>` |  The traffic class.|
| `<interface-id>` | The interface ID.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold congestion tc 3 interface swp1
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> drop-filter</h>

Shows the drop filters configured on the switch.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel forwarding drop-filter
Filter name  Summary                
-----------  -----------------------
IP-DROPS     IP address: 10.10.10.10
TUNNEL1      Drop category:   tunnel
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> drop-filter \<filter-id\></h>

Shows drop filter configuration for a specific filter.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<filter-id>` |  The filter name.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel forwarding drop-filter TUNNEL1
             operational  applied
-----------  -----------  -------
[drop-type]  tunnel       tunnel 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> drop-filter \<filter-id\> drop-type</h>

Shows the drop filter type configuration for a specific channel.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<filter-id>` |  The filter name.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel forwarding drop-filter TUNNEL1 drop-type
Drop category  Summary                                            
-------------  ---------------------------------------------------
tunnel         Drop reason: overlay-switch-src-mac-equals-dest-mac
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> drop-filter \<filter-id\> drop-type \<drop-type-id\></h>

Shows drop filter information for a specific channel and drop filter.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<filter-id>` |  The filter name.|
| `<drop-type-id>` |  The drop type: `acl`, `buffer`, `l2`, `l3`, or `tunnel`.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel forwarding drop-filter TUNNEL1 drop-type l2
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> drop-filter \<filter-id\> drop-type \<drop-type-id\> drop-reason</h>

Shows the drop filter drop reasons configuration for a specific channel.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<filter-id>` |  The filter name.|
| `<drop-type-id>` |  The drop type: `acl`, `buffer`, `l2`, `l3`, or `tunnel`.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel forwarding drop-filter TUNNEL1 drop-type l3 drop-reason
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> drop-filter \<filter-id\> ip</h>

Shows the WJH channel drop filter IP addresses.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<filter-id>` |  The filter name.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$  nv show system wjh channel forwarding drop-filter TUNNEL1 ip 
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> drop-filter \<filter-id\> ip \<ip-address\></h>

Shows WJH channel drop filter information for a specific IP address.

| Syntax |  Description   |
| --------- | -------------- |
| `<channel-id>` |  The channel name.|
| `<filter-id>` |  The filter name.|
| `<ip-address>` |  The IP address.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system wjh channel forwarding drop-filter TUNNEL1 ip 10.10.10.10
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh packet-buffer</h>

Shows all dropped packets monitored by WJH and the reason for the drop.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system wjh packet-buffer
#   dMAC  dPort  Dst IP:Port  EthType  Drop group  IP Proto  Drop reason - Recommended action                         Severity  sMAC  sPort    Src IP:Port  Timestamp              VLAN
--  ----  -----  -----------  -------  ----------  --------  -------------------------------------------------------  --------  ----  -------  -----------  ---------------------  ----
1   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp17    N/A          22/11/03 01:00:35.458  N/A
2   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp18    N/A          22/11/03 01:00:35.458  N/A
3   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp19    N/A          22/11/03 01:00:35.458  N/A
4   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp20    N/A          22/11/03 01:00:35.458  N/A
```
