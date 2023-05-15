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
cumulus@switch:~$ nv show interface swp5 qos
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
cumulus@switch:~$ nv show interface swp5 qos congestion-control traffic-class 2
```

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
cumulus@switch:~$ nv show interface swp1 counters ingress-buffer-stats
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> counters qos pfc-stats</h>

Shows all QoS PFC statistics for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv show interface <interface-id> qos counters pfc-stats`
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
cumulus@switch:~$ nv show interface swp5 qos mapping
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
cumulus@switch:~$ nv show interface swp5 qos mapping pcp
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
cumulus@switch:~$ nv show interface swp5 qos roce status
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

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos advance-buffer-config
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
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer
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
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1
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
cumulus@switch:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 switch-priority
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
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos buffer</h>

Shows QoS buffer configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos buffer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos buffer pool</h>

Shows QoS buffer traffic pool configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos buffer pool
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos buffer multicast-switch-priority</h>

Shows QoS buffer multicast switch priority configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show qos buffer multicast-switch-priority
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos congestion-control</h>

Shows QoS congestion control configuration settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos congestion-control
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
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-queue-mapping</h>

Shows egress queue mapping configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos egress-queue-mapping
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
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos egress-scheduler</h>

Shows QoS egress scheduler configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show qos egress-scheduler
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

Shows QoS <span style="background-color:#F5F5DC">[ROCE](## "RDMA over Converged Ethernet")</span> configuration, such as the configured buffers, utilization and DSCP markings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos roce
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos roce prio-map</h>

Shows QoS ROCE priority map configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos roce prio-map
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos roce tc-map</h>

Shows QoS ROCE traffic class map configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos roce tc-map
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos roce pool-map</h>

Shows QoS ROCE traffic pool map configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos roce pool-map
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos roce pool</h>

Shows QoS ROCE traffic pool configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show qos roce pool
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
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show qos traffic-pool \<traffic-pool-id\> switch-priority</h>

Shows switch priority configuration settings for a specific QoS traffic pool.

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
