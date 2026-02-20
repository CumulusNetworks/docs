---
title: Telemetry
author: Cumulus Networks
weight: 425

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> latency-measurement</h>

Shows latency measurement information for an interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>`  | The interface name.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show interface swp1 latency-measurement
traffic-class   protocol  DSCP   Latency   Status       Timestamp 
------------------------------------------------------------------------------- 
1               ipv4      12     19         SUCCESS     2025-01-25 10:15:32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> latency-measurement traffic-class</h>

Shows latency measurement information for all traffic classes.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>`  | The interface name.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show interface swp1 latency-measurement traffic-class
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> latency-measurement traffic-class \<traffic-class\></h>

Shows latency measurement information for a specific traffic class.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>`  | The interface name.|
| `<traffic-class>`  | The traffic class.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show interface swp1 latency-measurement traffic-class 0
protocol
===========
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> latency-measurement traffic-class \<traffic-class\> protocol</h>

Shows latency measurement information for a specific traffic class for both IPv4 and IPv6.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>`  | The interface name.|
| `<traffic-class>`  | The traffic class.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show interface swp1 latency-measurement traffic-class 0 protocol
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> latency-measurement traffic-class \<traffic-class\> protocol \<protocol-id\></h>

Shows latency measurement information for a specific traffic class and protocol (IPv4 or IPv6).

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>`  | The interface name.|
| `<traffic-class>`  | The traffic class.|
| `<protocol-id>`  | IPv4 or IPv6.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show interface swp1 latency-measurement traffic-class 0 protocol ipv4
DSCP: 0 
 Current Latency: 12.3 μs 
 Status: SUCCESS 
 Last Update: 2025-01-25 10:15:32 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry</h>

Shows the histogram configuration settings for the specified interface and operational data.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry bw-gauge</h>

Shows the bandwidth gauge setting for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry bw-gauge
        operational  applied
------  -----------  -------
enable  on           on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry congestion-event</h>

Shows congestion event data for a specific interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry congestion-event
Interface Congestion Event
=============================
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram</h>

Shows histogram details for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram ingress-buffer</h>

Shows ingress queue depth histogram samples collected for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram ingress-buffer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram ingress-buffer priority-group</h>

Shows the ingress queue depth histogram samples collected for all priority groups at the configured interval for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram ingress-buffer priority group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram ingress-buffer priority-group \<pg-id\></h>

Shows the ingress queue depth histogram samples collected at the configured interval for the specified priority group and interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `<pg-id>` |  The priority group ID. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram ingress-buffer priority-group 0
Time      0-863     864:2303    2304:3743  3744:5183   5184:6623   6624:8063   8064:9503 9. 504:10943   10944:12383 
12384:* 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
08:56:19  978065        0          0           0           0            0           0           0             0
08:56:20  978532        0          0           0           0            0           0           0             0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram ingress-buffer priority-group \<pg-id\> threshold</h>

Show the configured interval set for ingress queue depth histogram samples.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `<pg-id>` |  The priority group ID. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram ingress-buffer priority-group 0 threshold
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram ingress-buffer priority-group \<pg-id\> snapshot</h>

Shows the snapshot collected for the ingress queue depth histogram samples.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `<pg-id>` |  The priority group ID. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram ingress-buffer priority-group 0 snapshot
Sl.No  Date-Time            Bin-0   Bin-1    Bin-2    Bin-3    Bin-4    Bin-5    Bin-6    Bin-7     Bin-8     Bin-9
-----  -------------------  ------  -------  -------  -------  -------  -------  -------  --------  --------  ---------
0      -                    (<864)  (<2304)  (<3744)  (<5184)  (<6624)  (<8064)  (<9504)  (<10944)  (<12384)  (>=12384)
1      2023-12-13 11:02:44  980318  0        0        0        0        0        0        0         0         0
2      2023-12-13 11:02:43  980318  0        0        0        0        0        0        0         0         0
3      2023-12-13 11:02:42  980318  0        0        0        0        0        0        0         0         0
4      2023-12-13 11:02:41  980318  0        0        0        0        0        0        0         0         0
5      2023-12-13 11:02:40  980488  0        0        0        0        0        0        0         0         0
6      2023-12-13 11:02:39  980149  0        0        0        0        0        0        0         0         0
7      2023-12-13 11:02:38  979809  0        0        0        0        0        0        0         0         0
8      2023-12-13 11:02:37  980488  0        0        0        0        0        0        0         0         0
9      2023-12-13 11:02:36  980318  0        0        0        0        0        0        0         0         0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram egress-buffer</h>

Shows the egress queue depth histogram samples collected at the configured interval for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram egress-buffer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram egress-buffer traffic-class</h>

Shows the ingress queue depth histogram samples collected for all traffic classes at the configured interval for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram egress-buffer traffic class
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram egress-buffer traffic-class \<tc-id\></h>

Shows the egress queue depth histogram samples collected at the configured interval for the specified traffic class and interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `<tc-id>` |  The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram egress-buffer traffic class 4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram egress-buffer traffic-class \<tc-id\> threshold</h>

Shows the configured interval set for egress queue depth histogram samples.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `<tc-id>` |  The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram egress-buffer traffic class 4 threshold
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram egress-buffer traffic-class \<tc-id\> snapshot</h>

Shows the snapshot collected for the egress queue depth histogram samples.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `<tc-id>` |  The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram egress-buffer traffic class 4 snapshot
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram counter</h>

Shows the counter histogram samples collected at the configured interval for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram counter
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram counter counter-type</h>

Shows the counter histogram samples collected at the configured interval for all counter types for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram counter counter-type
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram counter counter-type \<counter-type-id\></h>

Shows the counter histogram samples collected at the configured interval for the specified counter type for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `<counter-type-id>` |  The counter type ID. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram counter counter-type rx-packet
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram counter counter-type \<counter-type-id\> threshold</h>

Shows the configured interval set for counter histogram samples for the specified counter type.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `<counter-type-id>` |  The counter type ID. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram counter counter-type rx-packet threshold
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram counter counter-type \<counter-type-id\> snapshot</h>

Shows the snapshot collected for the counter histogram samples for the specified counter type.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `<counter-type-id>` |  The counter type ID. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram counter counter-type rx-packet snapshot
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram latency</h>

Shows the latency histogram details for the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram latency
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram latency traffic-class</h>

Shows the latency histogram samples collected for all traffic classes for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram latency traffic-class
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram latency traffic-class \<tc-id\></h>

Shows the latency histogram samples collected for the specified traffic class on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `tc-id`| The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram latency traffic-class 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram latency traffic-class \<tc-id\> threshold</h>

Shows the configured interval set for latency histogram samples for the specified traffic class on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `tc-id` | The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram latency traffic-class 2 threshold
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> telemetry histogram latency traffic-class \<tc-id\> snapshot</h>

Shows the snapshot collected for latency histogram samples for the specified traffic class on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface name. |
| `tc-id` | The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram latency traffic-class 2 snapshot
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry buffer-stats</h>

Shows telemetry buffer statistics configuration settings.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry buffer-stats
                 operational  applied
---------------  -----------  -------
sample-interval               1      
export                               
  state                       enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry buffer-stats export</h>

Shows if collection and export of buffer statistics is enabled.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry buffer-stats export
       operational  applied
-----  -----------  -------
state               enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry bw-gauge</h>

Shows a summary of the bandwidth gauge for all interfaces.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv show service telemetry bw-gauge`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system telemetry bw-gauge
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry bw-gauge interface</h>

Shows a summary of the bandwidth for all interfaces with bandwidth gauge enabled.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv show service telemetry bw-gauge interface`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system telemetry bw-gauge interface
Interface  Tx (Mbps)  Rx (Mbps)
---------  ---------  ---------
swp1       4          4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry congestion-event</h>

Shows congestion notification configuration.

{{%notice note%}}
Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system telemetry congestion-event
                   operational  applied 
-----------------  -----------  --------
export                                  
  state            disabled     disabled
throttle-duration  10000        10000   

Congestion Event Interfaces
==============================
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry export</h>

Shows telemetry export configuration on the switch.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry export
                    applied   pending 
------------------  --------  --------
vrf                 default   default 
otlp                                  
  state             disabled  disabled
  grpc                                
    insecure  disabled  disabled
    port            8443      8443    
    [destination]
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry export otlp gRPC</h>

Shows OTLP gRPC export configuration on the switch.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry export otlp gRPC
          applied 
--------  --------
insecure  disabled
port      8443 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry export otlp gRPC destination</h>

Shows OTLP gRPC destination configuration on the switch.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry export otlp gRPC destination
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry export otlp gRPC destination \<destination\></h>

Shows specific OTLP gRPC destination configuration on the switch.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry export otlp gRPC destination 10.1.1.100
      applied  pending
----  -------  -------
port           4317
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry health</h>

Shows telemetry health information.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry health
                                     operational
---------------------------          -----------
service-status    
  nv-telemtry-service                active                      
  platform-stats-service             active
  histogram-export-service           active
  sdk-stats-service                  active
  routing-telemtry-service           inactive
internal-metrics 
  process 
    cpu-seconds                      3020
    memory-rss-kilobytes             182812672
    runtime-heap-alloc-bytes         28617960
    runtime-total-alloc-bytes        915541979208
    runtime-total-sys-memory-bytes   151368752
    uptime-seconds                   65313
[receivers]                          otlp/global
[receivers]                          prometheus/global
processors
  [memory-limiter]                   memory_limiter/1
  [batch]                            batch/1
[exporters]                          otlp/global

Export Destination Status
=======================
    Destination         Connectivity          Export Counter       Drop Counter
    -----------         ------------          --------------       ------------
    11.0.10.2:4317      Pass                  51534586             7087
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry health internal-metrics</h>

Shows all the telemetry health internal metrics.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry health internal-metrics
                                     operational
------------------------             -----------
process        
  cpu-seconds                        029
  memory-rss-kilobytes               182812672
  runtime-heap-alloc-bytes           28617960
  runtime-total-alloc-bytes          915541979208
  runtime-total-sys-memory-bytes     151368752
  uptime-seconds                     65313
[receivers]                          otlp/global
[receivers]                          prometheus/global
processors
  [memory-limiter]                   memory_limiter/1
  [batch]                            batch/1
[exporters]                          otlp/global
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry health internal-metrics process</h>

Shows health information about the telemetry process.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry health internal-metrics process
                                   operational
------------------------           -----------
cpu-seconds                        029
memory-rss-kilobytes               182812672
runtime-heap-alloc-bytes           28617960
runtime-total-alloc-bytes          915541979208
runtime-total-sys-memory-bytes     151368752
uptime-seconds                     65313
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry health internal-metrics receivers</h>

Shows health metrics about the telemetry receivers.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry health internal-metrics receivers
Receivers            Accepted Metric Points      Refused Metric Points
---------            ----------------------      ---------------------
otlp/global          4967144                     0
prometheus/global    46989135                    0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry health internal-metrics processors</h>

Shows health metrics about the telemetry processors.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry health internal-metrics processors
  Memory-limiter
  ==============
    memory_limiter/1
     Accepted Metric Points: 25002370
     Dropped Metric Points: 0
     Inserted Metric Points: 0
     Refused Metric Points: 0

  Batch Processor
  ===============
    batch/1
     Batch Send Size Bucket 10: 828620
     Batch Send Size Bucket 25: 828620
     Batch Send Size Bucket 50: 828620
     Batch Send Size Bucket 75: 828620
     Batch Send Size Bucket 100: 828620
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry health internal-metrics exporters</h>

Shows health metrics about the telemetry exporters.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry health internal-metrics exporters
Exporters       Enqueue Failed Metric Points   Queue Capacity   Queue Size   Send Failed Metric Points   Sent Metric Points
---------       ----------------------------   --------------   ----------   -------------------------   ------------------
otlp/global     0                              1000             0            7087                        52000844
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry hft</h>

Shows high frequency telemetry configuration.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry hft
profile
==========
    Profile   traffic-class  counter       sample-interval
    --------  -------------  ------------  ---------------
    profile2  0              rx-byte       1000           
              1              tx-byte                      
              2                                           
              3                                           
              4                                           
              5                                           
              6                                           
              7                                           
              8                                           
              9                                           
    standard  3              rx-byte       5000           
                             tc-occupancy                 
                             tx-byte
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry hft profile</h>

Shows the high frequency telemetry profiles configured on the switch.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry hft profile
Profile   traffic-class  counter       sample-interval
--------  -------------  ------------  ---------------
profile2  0              rx-byte       1000           
          1              tx-byte                      
          2                                           
          3                                           
          4                                           
          5                                           
          6                                           
          7                                           
          8                                           
          9                                           
standard  3              rx-byte       5000           
                         tc-occupancy                 
                         tx-byte
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry hft profile \<profile-id\></h>

Shows the configuration settings for a specific profile:

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |  The name of the profile. High frequency telemetry uses profiles for data collection. A profile is a set of configurations. Cumulus Linux provides a default profile called `standard`. You can create a maximum of four new profiles (four profiles in addition to the default profile).|

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry hft profile profile2
                 operational  applied
---------------  -----------  -------
sample-interval  1000         1000   
[traffic-class]  0            0      
[traffic-class]  1            1      
[traffic-class]  2            2      
[traffic-class]  3            3      
[traffic-class]  4            4      
[traffic-class]  5            5      
[traffic-class]  6            6      
[traffic-class]  7            7      
[traffic-class]  8            8      
[traffic-class]  9            9      
[counter]        rx-byte      rx-byte
[counter]        tx-byte      tx-byte
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry hft target</h>

Shows the high frequency telemetry configured targets.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry hft target
applied
-------
local
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry hft job</h>

Shows information for all data collection jobs, such as the start time, duration, status, and ports on which the data is collected.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry hft job
Job Id      Start Time               Duration(s)        Profile     Ports    Status  

---------   --------------           ------------       ---------   -------   ---------  

1           10-05-2024 09:00:00      20                 standard    all       complete 
2           12-05-2024 09:00:00      20                 standard    all       complete 
3           15-05-2024 09:00:00      20                 standard    all       complete 
4           16-05-2024 09:00:00      20                 standard    all       complete 
5           17-05-2024 09:00:00      20                 standard    all       complete 
6           19-05-2024 09:00:00      20                 standard    all       complete 
7           19-05-2024 12:00:00      20                 standard    all       running 
8           20-05-2024 09:00:00      20                 standard    all       pending
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry hft job \<job-id\></h>

Shows information about a specific high frequency telemetry data collection job.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<job-id>`| The high frequency telemetry data collection job ID. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry hft job 1 
                       operational
---------------------  ----------------- 
start-time             01-01-2024 12:00:00 
duration               20 
traffic-class          3 
counter                tx-byte,rx-byte,tc-occupancy 
sample-interval        5000 
ports                  swp1-swp64 
status                 pending 
target                 scp://abc@server1:/hft-data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry histogram</h>

Shows telemetry histogram configuration settings and operational data.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv show service telemetry histogram`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system telemetry histogram
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry histogram ingress-buffer</h>

Shows ingress queue length histogram configuration settings and operational data.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv show service telemetry histogram ingress-buffer`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system telemetry histogram ingress-buffer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry histogram egress-buffer</h>

Shows egress queue length histogram configuration settings and operational data.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv show service telemetry histogram egress-buffer`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system telemetry histogram egress-buffer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry histogram counter</h>

Shows counter histogram configuration settings and operational data.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv show service telemetry histogram counter`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system telemetry histogram counter
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry histogram interface</h>

Shows a list of the interfaces with enabled histograms.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv show service telemetry histogram interface`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system telemetry histogram interface
Interface         ingress-buffer          egress-buffer            counter 
--------------------------------------------------------------------------------------- 
swp1              0,1,2                   -                        tx-byte,rx-byte 
swp2              -                       0,1,8                    tx-byte,tx-byte
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry histogram latency</h>

Shows latency Histogram configuration and operational data.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv show service telemetry histogram latency`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show system telemetry histogram latency
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry interface-stats</h>

Shows telemetry interface statistics configuration.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry interface-stats
                 applied   pending 
---------------  --------  --------
sample-interval  1         1       
export                             
  state          enabled  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry interface-stats class</h>

Shows interface statistics class configuration settings.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry interface-stats class
         operational  applied 
-------  -----------  --------
phy                           
  state               disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry interface-stats class phy</h>

Shows if interface PHY statistics export is enabled.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$  nv show system telemetry interface-stats class phy
       operational  applied 
-----  -----------  --------
state               disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry interface-stats egress-buffer</h>

Shows the telemetry interface statistics egress buffer configuration.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry interface-stats egress-buffer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry interface-stats export</h>

Shows if interface statistics export is enabled or disabled.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry interface-stats export
      applied   pending 
-----  --------  --------
state  enabled  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry interface-stats ingress-buffer</h>

Shows telemetry interface statistics ingress buffer configuration.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system telemetry interface-stats ingress-buffer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry latency-measurement</h>

Shows latency measurement configuration.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system telemetry latency-measurement 
                 operational  applied
---------------  -----------  -------
state                         enabled
sample-interval               2      
export                               
  state                       enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry latency-measurement export</h>

Shows if latency measurement export is enabled for so that you can export latency data to a configured telemetry module

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system telemetry latency-measurement export
                 operational  applied
---------------  -----------  -------
state                         enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router</h>

Shows which telemetry router statistics are enabled.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router
                 applied 
---------------  --------
bgp                      
  export                 
    state        enabled
rib                      
  export                 
    state        enabled
export                   
  state          enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router export</h>

Shows if the open telemetry routing service is enabled.

{{%notice note%}}
To export any of the routing metrics, you must first enable the open telemetry routing service.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router export
       applied 
-----  --------
state  disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router bgp</h>

Shows configuration settings for BGP peer state statistics across all VRFs.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router bgp
         applied 
-------  --------
export           
  state  disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router bgp export</h>

Shows if collection and export of BGP peer state statistics across all VRFs is enabled.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router bgp export
       applied 
-----  --------
state  disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router rib</h>

Shows configuration settings for routing table statistics across all VRFs.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router rib
                 applied
---------------  -------
export                
  state         enabled

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router rib export</h>

Shows if collection and export of routing table statistics across all VRFs is enabled.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router rib export
       applied 
-----  --------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router vrf \<vrf-id\> bgp</h>

Shows configuration settings for BGP peer state statistics in a specific VRF.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router vrf RED bgp
         applied
-------  -------
export          
  state  enabled
[peer]   swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router vrf \<vrf-id\> bgp export</h>

Shows if collection and export of BGP peer state statistics in a specific VRF is enabled.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router vrf RED bgp export
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router vrf \<vrf-id\> bgp peer \<neighbor-id\> export</h>

Shows if collection and export of routing statistics for a specifc peer in a VRF is enabled.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>` |  The BGP neighbor ID.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router vrf RED bgp peer swp1 export
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router vrf \<vrf-id\> rib</h>

Shows configuration settings for routing table statistics for a specific VRF.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router vrf RED rib
         applied
-------  -------
export          
  state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry router vrf \<vrf-id\> rib export</h>

Shows if collection and export of routing table statistics for a specific VRF is enabled.

### Command Syntax

|  Syntax | Description |
| ---------| ------ |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry router vrf RED rib export
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot-file</h>

Shows histogram snapshot file configuration and operational data.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv show service telemetry snapshot-file`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot-file
       operational  applied                         
-----  -----------  --------------------------------
name                /var/run/cumulus/histogram_stats
count               64
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> threshold</h>

Shows threshold configuration for the specified port group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg threshold
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> threshold \<threshold-stats-id\></h>

Shows configuration information for a specific type of threshold statistics for the port group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<threshold-stats-id>` | The type of threshold ststistics; `packet-congestion-drops` or `packet-error-drops`. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg threshold packet-error-drops
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> threshold \<threshold-stats-id\> action</h>

Shows port group threshold action configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<threshold-stats-id>` | The type of threshold ststistics; `packet-congestion-drops` or `packet-error-drops`. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg threshold packet-error-drops action
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> threshold \<threshold-stats-id\> action log</h>

Shows port group threshold log action configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<threshold-stats-id>` | The type of threshold ststistics; `packet-congestion-drops` or `packet-error-drops`. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg threshold packet-error-drops action log
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> threshold <threshold-stats-id> action collect</h>

Shows port group threshold collect action configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<threshold-stats-id>` | The type of threshold ststistics; `packet-congestion-drops` or `packet-error-drops`. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg threshold packet-error-drops action collect
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats-type</h>

Shows port group configuration for the different types of statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg stats-type
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats buffer</h>

Shows port group buffer information.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg stats buffer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats buffer pool</h>

Shows port group buffer pool information.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg stats buffer pool
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats buffer pool \<buffer-pool-id\></h>

Shows specific buffer pool information for a port group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<buffer-pool-id>`| The buffer pool ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg stats buffer pool 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface</h>

Shows port group interface snapshots.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg stats interface
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\></h>

Shows port group snapshots for a specific interface .

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg stats interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet</h>

Shows interface packet information for a port group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group packet-all-pg stats interface swp1 packet
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet good</h>

Shows a snapshot for good packets transmitted and received on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group nv show system telemetry snapshot port-group packet-all-pg stats interface swp1 packet good
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet good tx</h>

Shows a snapshot for good packets transmitted on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet good tx 
Id       Date-Time                 Packet         Byte             Mcast        Bcast         Mac Ctrl       Pause Mac Ctrl 

-----    -------------------       ------------   -------------    ---------    ----------    ------------   ---------------

1         2023-12-13 11:02:44      2              268              0            0             0              0
2         2023-12-13 11:02:43      2              268              0            0             0              0
3         2023-12-13 11:02:42      2              268              0            0             0              0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet good rx</h>

Shows a snapshot for good packets received on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet good rx
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet discard</h>

Shows a snapshot for discarded packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet discard
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet discard tx</h>

Shows a snapshot for discarded packets transmitted on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet discard tx
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet discard rx</h>

Shows a snapshot for discarded packets received on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet discard rx 
Id       Date-Time                  General      Policy        Vlan         Tag Type     Opcode     Buffer   Runt     Other 

-----    -------------------        ---------    -----------   -------      ----------    -------   -------  -------  -------- 

1         2023-12-13 11:02:44       2            0             0            0             0         0        0        0
2         2023-12-13 11:02:43       2            0             0            0             0         0        0        0
3         2023-12-13 11:02:42       2            0             0            0             0         0        0        0 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet discard general</h>

Shows a snapshot for general discarded packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet discard general
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet all</h>

Shows a snapshot for all packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet all
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet all tx</h>

Shows a snapshot for all transmitted packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet all tx
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet all rx</h>

Shows a snapshot for all received packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet all rx
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet tc</h>

Shows a snapshot for traffic class packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet tc
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet tc \<tc-id\></h>

Shows a snapshot for specific traffic class packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |
| `<tc-id>`| The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet tc 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet tc \<tc-id\> tx

Shows a snapshot for specific traffic class transmitted packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |
| `<tc-id>`| The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet tc 1 tx
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet pg</h>

Shows a snapshot for priority group packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet pg
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet pg \<pg-id\></h>

Shows a snapshot for specific priority group packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |
| `<pg-id>`| The priority group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet pg 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet pg \<pg-id\> tx</h>

Shows a snapshot for priority group packets transmitted on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |
| `<pg-id>`| The priority group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet pg 1 tx 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> packet pg \<pg-id\> rx</h>

Shows a snapshot for priority group packets received on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |
| `<pg-id>`| The priority group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 packet pg 1 tc
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> buffer</h>

Shows interface buffer information.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 buffer 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> buffer tc</h>

Shows interface egress buffer information.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 buffer tc
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> buffer tc \<tc-id\></h>

Shows specific interface egress buffer information.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |
| `<tc-id>`| The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 buffer tc 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> buffer pg</h>

Shows interface ingress buffer information.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 buffer pg
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> buffer pg \<pg-id\></h>

Shows specific interface ingress buffer information.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |
| `<pg-id>`| The priority group name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 buffer pg 0 
Id       Date-Time                 Current Value        Watermark        
-----    -------------------       ------------         -------------
1        2023-12-13 11:02:44       0                    0                           
2        2023-12-13 11:02:43       0                    0              
3        2023-12-13 11:02:42       0                    0 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> buffer ingress-port</h>

Shows port group snapshot interface ingress port buffer configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 buffer ingress-port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry snapshot port-group \<port-group-id\> stats interface \<interface-id\> buffer ingress-port \<buffer-pool-id\></h>

Shows port group snapshot interface ingress port buffer pool configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<interface-id>`| The interface name. |
| `<buffer-pool-id>`| The buffer pool ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system telemetry snapshot port-group all-packet-pg stats interface swp1 buffer ingress-port 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group</h>

Show telemetry statistics group configuration settings.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry stats-group
             Histogram  Interface Stats  Platform Stats  ControlPlane Stats  Buffer Stats  Routing Stats
-----------  ---------  ---------------  --------------  ------------------  ------------  -------------
STAT-GROUP1  disabled   enabled          disabled        disabled            disabled      disabled     
blah         disabled   disabled         disabled        disabled            disabled      disabled 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> interface-stats</h>

Shows configuration for the custom statistics group for interface statistics export.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry stats-group STAT-GROUP1 interface-stats
                 applied 
---------------  --------
sample-interval  100     
export                   
  state          enabled 
class                    
  phy                    
    state        disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> interface-stats export</h>

Shows if the custom statistics group for interface statistics export is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry stats-group STAT-GROUP1 interface-stats export 
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> buffer-stats</h>

Shows configuration for the custom statistics group for buffer statistics export.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry stats-group STAT-GROUP1 buffer-stats
                 applied 
---------------  --------
sample-interval  1       
export                   
  state          disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> buffer-stats export</h>

Shows if the custom statistics group for buffer statistics export is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry stats-group STAT-GROUP1 buffer-stats export 
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> histogram</h>

Shows configuration for the custom statistics group for histogram statistics export.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry stats-group STAT-GROUP1 histogram
                    applied 
------------------  --------
ingress-buffer              
  bin-min-boundary  960     
  histogram-size    12288   
  sample-interval   1024    
egress-buffer               
  bin-min-boundary  960     
  histogram-size    12288   
  sample-interval   1024    
counter                     
  bin-min-boundary  100000  
  histogram-size    10000000
  sample-interval   1024    
latency                     
  bin-min-boundary  320     
  histogram-size    5440    
export                      
  state             disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> histogram export</h>

Shows if the custom statistics group for histogram statistics export is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry stats-group STAT-GROUP1 histogram export 
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> router</h>

Shows configuration for the custom statistics group for router statistics export.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system telemetry stats-group STAT-GROUP1 router
                 applied 
---------------  --------
bgp                      
  export                 
    state        disabled
rib                      
  export                 
    state        disabled
export                   
  state          disabled
sample-interval  30      
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> router export</h>

Shows if the custom statistics group for router statistics export is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry stats-group STAT-GROUP1 router export 
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> control-plane-stats</h>

Shows configuration for the custom statistics group for control plane statistics export.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system telemetry stats-group STAT-GROUP1 control-plane-stats
                 applied 
---------------  --------
sample-interval  1       
export                   
  state          disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> control-plane-stats export</h>

Shows if the custom statistics group for control plane statistics export is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry stats-group STAT-GROUP1 control-plane-stats export 
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> platform-stats</h>

Shows configuration for the custom statistics group for platform statistics export.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system telemetry stats-group STAT-GROUP1 platform-stats
                      applied 
--------------------  --------
class                         
  cpu                         
    state             enabled 
  disk                        
    state             enabled 
  file-system                 
    state             enabled 
  memory                      
    state             enabled 
  environment-sensor          
    state             enabled 
export                        
  state               disabled
  sample-interval     60      
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> platform-stats export</h>

Shows if the custom statistics group for platform statistics export is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system telemetry stats-group STAT-GROUP1 platform-stats export 
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> platform-stats class</h>

Shows configuration for the custom statistics group for each category of platform statistics export.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system telemetry stats-group STAT-GROUP1 platform-stats class
                    applied  pending
------------------  -------  -------
cpu                                 
  state             enabled  enabled
disk                                
  state             enabled  enabled
file-system                         
  state             enabled  enabled
memory                              
  state             enabled  enabled
environment-sensor                  
  state             enabled  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> platform-stats class cpu</h>

Shows if the custom statistics group for CPU platform statistics export is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system telemetry stats-group STAT-GROUP1 platform-stats class cpu
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> platform-stats class disk</h>

Shows if the custom statistics group for disk platform statistics export  is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system telemetry stats-group STAT-GROUP1 platform-stats class disk
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> platform-stats class file-system</h>

Shows if the custom statistics group for file system platform statistics export is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system telemetry stats-group STAT-GROUP1 platform-stats class file-system
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> platform-stats class environment-sensor</h>

Shows if the custom statistics group for environment sensor platform statistics export is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system telemetry stats-group STAT-GROUP1 platform-stats class environment-sensor
       applied
-----  -------
state  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system telemetry stats-group \<stats-group-id\> platform-stats class memory</h>

Shows if the custom statistics group for memory platform statistics export is enabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system telemetry stats-group STAT-GROUP1 platform-stats class memory
       applied
-----  -------
state  enabled
```
