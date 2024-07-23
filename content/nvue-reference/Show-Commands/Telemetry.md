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
```
