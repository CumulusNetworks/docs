---
title: Telemetry
author: Cumulus Networks
weight: 785

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry bw-gauge enable</h>

Enables (`on`) and disables (`off`) bandwidth gauge to track bandwidth usage for the specified interface.

{{%notice note%}}
Cumulus Linux supports the bandwidth gauge option on the Spectrum-4 switch only.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1 telemetry bw-gauge enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram counter counter-type \<counter-type-id\></h>

Configures the counter type you want to monitor. You can specify:
- Received packet counters (`rx-packet`)
- Transmitted packet counters (`tx-packet`)
- Received byte counters (`rx-byte`)
- Transmitted byte counters (`tx-byte`)
- CRC counters (`crc`)
- Layer 1 received byte counters (`l1-rx-byte`). The byte count includes layer 1IPG bytes.
- Layer 1 transmitted byte counters (`l1-tx-byte`). The byte count includes layer 1IPG bytes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<counter-type-id>`| The counter type you want to monitor: `rx-packet`,`tx-packet`, `rx-byte`, `tx-byte`, `crc`, `l1-rx-byte`, or `l1-tx-byte`. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-swp8 telemetry histogram counter counter-type rx-packet
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram counter counter-type \<counter-type-id\> threshold action log</h>

Configures the switch to send log messages to the `/var/log/syslog` file when the number of counters reach a specified value (`threshold value` described below).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<counter-type-id>`| The counter type you want to monitor: `rx-packet`,`tx-packet`, `rx-byte`, `tx-byte`, `crc`, `l1-rx-byte`, or `l1-tx-byte`. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-swp8 telemetry histogram counter counter-type rx-packet threshold action log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram counter counter-type \<counter-type-id\> threshold value</h>

Configures the number of counters to reach before the switch sends log messages to the `/var/log/syslog` file. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<counter-type-id>`| The counter type you want to monitor: `rx-packet`,`tx-packet`, `rx-byte`, `tx-byte`, `crc`, `l1-rx-byte`, or `l1-tx-byte`. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-swp8 telemetry histogram counter counter-type rx-packet threshold value 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram counter counter-type \<counter-type-id\> bin-min-boundary</h>

Configures the minimum boundary size of the counter histogram for the specified interface. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the range of queue lengths per bin. You can specify a value, which must be a multiple of 96, between 1 and 4294967295. The default minimum boundary size is 960 bytes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<counter-type-id>`| The counter type you want to monitor: `rx-packet`,`tx-packet`, `rx-byte`, `tx-byte`, `crc`, `l1-rx-byte`, or `l1-tx-byte`. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-swp8 telemetry histogram counter counter-type tx-packet bin-min-boundary 960
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram counter counter-type \<counter-type-id\> histogram-size</h>

Configures the size of the counter histogram for the specified interface. Adding this number to the minimum boundary size of the histogram produces the maximum boundary size. These values represent the range of queue lengths or counters per bin. You can specify a value, which must be a multiple of 96, between 1 and 4294967295. The default minimum boundary size is 960 bytes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<counter-type-id>`| The counter type you want to monitor: `rx-packet`,`tx-packet`, `rx-byte`, `tx-byte`, `crc`, `l1-rx-byte`, or `l1-tx-byte`. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-swp8 telemetry histogram counter counter-type tx-packet histogram-size 12288
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram counter counter-type \<counter-type-id\> sample-interval</h>

Configures the counter histogram sampling interval for the specified interface. You can specify a value between 128 and 1000000000. The default value is 1024 nanoseconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<counter-type-id>`| The counter type you want to monitor: `rx-packet`,`tx-packet`, `rx-byte`, `tx-byte`, `crc`, `l1-rx-byte`, or `l1-tx-byte`. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-swp8 telemetry histogram counter counter-type tx-packet sample-interval 1024
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram ingress-buffer priority-group \<pg-id\></h>

Configures the priority group you want to monitor for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<pg-id>` |  The priority group you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram ingress-buffer priority-group 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram ingress-buffer priority-group \<pg-id\> bin-min-boundary</h>

Configures the minimum boundary size of the ingress buffer histogram for the specified priority group and interface. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the range of counters per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295. The default minimum boundary size is 960 bytes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<pg-id>` |  The priority group you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram ingress-buffer priority-group 1 bin-min-boundary 768
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram ingress-buffer priority-group \<pg-id\> histogram-size</h>

Configures the size of the ingress buffer histogram for the specified priority group and interface. Adding this number to the minimum boundary size of the histogram produces the maximum boundary size. These values represent the range of counters per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295. The default minimum boundary size is 960 bytes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<pg-id>` |  The priority group you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram ingress-buffer priority-group 1 histogram-size 9600
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram ingress-buffer priority-group \<pg-id\> sample-interval</h>

Configures the ingress buffer histogram sampling interval for the specified priority group and interface. You can specify a value between 128 and 1000000000. The default value is 1024 nanoseconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<pg-id>` |  The priority group you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram ingress-buffer priority-group 1 sample-interval 204
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram ingress-buffer priority-group \<pg-id\> threshold action log</h>

Configures the switch to send log messages to the `/var/log/syslog` file when the ingress queue length for the specified priority group and interface reaches a specified value (`threshold value` described below).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<pg-id>` |  The priority group you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp9-swp16 telemetry histogram ingress-buffer priority-group 1 threshold action log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram ingress-buffer priority-group \<if-pg-id\> threshold value</h>

Configures the ingress queue length to reach for the specified priority group and interface before the switch sends log messages to the `/var/log/syslog` file. You can specify a value between 96 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<pg-id>` |  The priority group you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp9-swp16 telemetry histogram ingress-buffer priority-group 1 threshold value 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram egress-buffer traffic-class \<tc-id\></h>

Configures the egress-buffer traffic class you want to monitor.

Traffic class 0 through 7 is for unicast traffic and traffic class 8 through 15 is for multicast traffic.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram egress-buffer traffic-class 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram egress-buffer traffic-class \<tc-id\> bin-min-boundary</h>

Configures the minimum boundary size of the egress-buffer histogram for the specified traffic class and interface. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the range of queue lengths per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295. The default minimum boundary size is 960 bytes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram egress-buffer traffic-class 0 bin-min-boundary 768
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram egress-buffer traffic-class \<tc-id\> histogram-size</h> 

Configures the size of the egress buffer histogram for the specified traffic class and interface. Adding this number to the minimum boundary size of the histogram produces the maximum boundary size. These values represent the range of queue lengths per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram egress-buffer traffic-class 0 histogram-size 9600
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram egress-buffer traffic-class \<tc-id\> sample-interval</h>

Configures the egress buffer histogram sampling interval for the specified traffic class and interface. You can specify a value between 128 and 1000000000. The default value is 1024 nanoseconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram egress-buffer traffic-class 0 sample-interval 2048
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram egress-buffer traffic-class \<tc-id\> threshold action log</h>

Configures the switch to send log messages to the `/var/log/syslog` file when the egress queue length for the specified traffic class reaches a specified value (`threshold value` described below).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram egress-buffer traffic-class 0 threshold action log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram egress-buffer traffic-class \<tc-id\> threshold value</h>

Configures the egress queue length to reach for the specified traffic class before the switch sends log messages to the `/var/log/syslog` file. You can specify a value between 96 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram egress-buffer traffic-class 0 threshold value 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram latency traffic-class \<tc-id\></h>

Enables the latency histogram for the specified traffic class on the specified interfaces.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram latency traffic-class 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram latency traffic-class \<tc-id\> threshold action log</h>

Configures the switch to send a message to the `/var/log/syslog` file after packet latency for the specified traffic class on the specified interfaces reaches the set threshold.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram latency traffic-class 0 threshold action log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram latency traffic-class \<tc-id\> threshold value</h>

Configures the threshold (in nannoseconds) after which the switch sends a message to the `/var/log/syslog` file.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram latency traffic-class 0 threshold action log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram latency traffic-class \<tc-id\> bin-min-boundary</h>

Configures the minimum boundary for the latency histogram for the specified traffic class on the specified interfaces.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram latency traffic-class 1 bin-min-boundary 768
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> telemetry histogram latency traffic-class \<tc-id\> histogram-size</h>

Configures the size of the latency histogram for the specified traffic class on the specified interfaces.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram latency traffic-class 1 histogram-size 9600
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry adaptive-routing-stats export state</h>

Enables and disables export for adaptive routing statistics. You can specify `enabled` or `disabled`.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system telemetry adaptive-routing-stats export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry adaptive-routing-stats sample-interval</h>

Sets the sample interval for adaptive routing metrics. The default value is 60 seconds.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system telemetry adaptive-routing-stats sample-interval 40
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry buffer-stats export state</h>

Enables collection and export of switch buffer occupancy and watermark metrics. You can specify `enabled` or `disabled`.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry buffer-stats export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry buffer-stats sample-interval</h>

Configures the sample interval for buffer statistics. You can specify a value between 1 and 86400. The default value is 1.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry buffer-stats sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry export otlp state</h>

Enables and disables open telemetry export so that you can export interface counters and histogram collection data to an external collector. You can specify `enabled` or `disabled`.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry export otlp state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry hft profile \<profile-id\> counter</h>

Configures the type of data you want to collect for the high frequency telemetry profile. You can specify `tx-byte`, `rx-byte`, or `tc-occupancy`. The standard profile collects all three data types.

{{%notice note%}}
- Cumulus Linux supports high frequency telemetry on Spectrum-4 switches only.
- Cumulus Linux does not support high frequency telemetry on ports using 8 lanes. On the Spectrum-4 switch, swp1 through swp64 use all 8 lanes; to run high frequency telemetry, you must break out these ports.
- To correlate counters from different switches, the switches must have the same time (Cumulus Linux adds timestamps in the metadata of the counters it collects). You can use either NTP or PTP; however, NVIDIA recommends using PTP because the timestamp is accurate between switches in the fabric at the microsecond level.
- The collected data is available on the switch until you trigger the next data collection job or until you reboot the switch.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |  The name of the profile. High frequency telemetry uses profiles for data collection. A profile is a set of configurations. Cumulus Linux provides a default profile called `standard`. You can create a maximum of four new profiles (four profiles in addition to the default profile).|

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry hft profile profile1 counter tc-occupancy 
```

{{%notice note%}}
You must specify the `nv set system telemetry hft profile <profile-id> counter` command for each data type you want to collect; For example:

```
cumulus@switch:~$ nv set system telemetry hft profile profile1 counter tx-byte
cumulus@switch:~$ nv set system telemetry hft profile profile1 counter rx-byte
```
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry hft profile \<profile-id\> sample-interval</h>

Configures the high frequency telemetry sampling interval in microseconds for the profile. You can specify a value between 100 and 12750. The value must be a multiple of 50. The default value is 5000 microseconds (30 seconds).

{{%notice note%}}
- Cumulus Linux supports high frequency telemetry on Spectrum-4 switches only.
- Cumulus Linux does not support high frequency telemetry on ports using 8 lanes. On the Spectrum-4 switch, swp1 through swp64 use all 8 lanes; to run high frequency telemetry, you must break out these ports.
- To correlate counters from different switches, the switches must have the same time (Cumulus Linux adds timestamps in the metadata of the counters it collects). You can use either NTP or PTP; however, NVIDIA recommends using PTP because the timestamp is accurate between switches in the fabric at the microsecond level.
- The collected data is available on the switch until you trigger the next data collection job or until you reboot the switch.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |  The name of the profile. High frequency telemetry uses profiles for data collection. A profile is a set of configurations. Cumulus Linux provides a default profile called `standard`. You can create a maximum of four new profiles (four profiles in addition to the default profile).|

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry hft profile profile1 sample-interval 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry hft profile \<profile-id\> traffic-class</h>

Sets the high frequency telemetry egress queue priorities (traffic class 0-15) for the profile if the data types you want to collect include current traffic class buffer occupancy. The standard profile setting is 3.

{{%notice note%}}
Use commas (no spaces) to separate the list of traffic classes. For example, to set traffic class 1, 3, and 6, specify 1,3,6.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |  The name of the profile. High frequency telemetry uses profiles for data collection. A profile is a set of configurations. Cumulus Linux provides a default profile called `standard`. You can create a maximum of four new profiles (four profiles in addition to the default profile).|

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry hft profile profile1 traffic-class 0,3,7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry hft target local</h>

Configures the switch to save the collected data locally in the `/var/run/cumulus/hft` directory. You can then export the `json` file to an external location with NVUE commands (or the API). The `json` file includes the data for each sampling interval and a timestamp showing when the data was collected.

{{%notice note%}}
- Cumulus Linux supports high frequency telemetry on Spectrum-4 switches only.
- Cumulus Linux does not support high frequency telemetry on ports using 8 lanes. On the Spectrum-4 switch, swp1 through swp64 use all 8 lanes; to run high frequency telemetry, you must break out these ports.
- To correlate counters from different switches, the switches must have the same time (Cumulus Linux adds timestamps in the metadata of the counters it collects). You can use either NTP or PTP; however, NVIDIA recommends using PTP because the timestamp is accurate between switches in the fabric at the microsecond level.
- The collected data is available on the switch until you trigger the next data collection job or until you reboot the switch.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry hft target local
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry hft profile \<profile-id\> traffic-class</h>

Configures the egress queue priorities (traffic class 0 through 15) for the high frequency telemetry profile. The standard profile setting is 3.

{{%notice note%}}
- Cumulus Linux supports high frequency telemetry on Spectrum-4 switches only.
- Cumulus Linux does not support high frequency telemetry on ports using 8 lanes. On the Spectrum-4 switch, swp1 through swp64 use all 8 lanes; to run high frequency telemetry, you must break out these ports.
- To correlate counters from different switches, the switches must have the same time (Cumulus Linux adds timestamps in the metadata of the counters it collects). You can use either NTP or PTP; however, NVIDIA recommends using PTP because the timestamp is accurate between switches in the fabric at the microsecond level.
- The collected data is available on the switch until you trigger the next data collection job or until you reboot the switch.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |  The name of the profile. High frequency telemetry uses profiles for data collection. A profile is a set of configurations. Cumulus Linux provides a default profile called `standard`. You can create a maximum of four new profiles (four profiles in addition to the default profile).|

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry hft profile profile1 traffic-class 0,3,7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram counter bin-min-boundary</h>

Configures the minimum boundary size of the counter histograms. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the number of counters per bin. You can specify a value, which must be a multiple of 96, between 1 and 4294967295. The default minimum boundary size is 960 bytes.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram counter bin-min-boundary`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram counter bin-min-boundary 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram counter histogram-size</h>

Configures the size of the counter buffer histogram for the specified traffic class and interface. Adding this number to the minimum boundary size of the histogram produces the maximum boundary size. These values represent the number of counters per bin. You can specify a value, which must be a multiple of 96, between 1 and 4294967295.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram counter histogram-size`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram counter histogram-size 12288
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram counter sample-interval</h>

Configures the counter histogram sampling interval. You can specify a value between 128 and 1000000000. The default value is 1024 nanoseconds.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram counter sample-interval`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram counter sample-interval 1024
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram egress-buffer bin-min-boundary</h>

Configures the minimum boundary size of the egress queue histograms. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the range of egress queues per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295. The default minimum boundary size is 960 bytes.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram egress-buffer bin-min-boundary`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram egress-buffer  bin-min-boundary
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram egress-buffer histogram-size</h>

Configures the size of the egress queue histogram. Adding this number to the minimum boundary size of the histogram produces the maximum boundary size. These values represent the range of egress queues per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram egress-buffer histogram-size`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram egress-buffer histogram-size 12288
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram egress-buffer sample-interval</h>

Configures the egress queue histogram sampling interval. You can specify a value between 128 and 1000000000. The default value is 1024 nanoseconds.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram egress-buffer sample-interval`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram egress-buffer sample-interval 1024
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram temporality \<mode\></h>

Sets the temporality mode for open telemetry histogram collection. Histogram temporality mode lets you choose how to aggregate and report histogram metrics over time.

Cumulus Linux supports the following temporality modes:
- Delta mode captures only the new data recorded after the last export, reflecting the rate of change instead of cumulative totals. Each export includes only the counts collected within the latest time window; previous values do not carry over to the next reporting cycle. This is the default setting.
- Cumulative mode reports the total count from the beginning of the measurement period. Each export includes all previously reported values along with newly recorded data, ensuring that the metric continues to grow until the measurement cycle resets. This approach prevents the metric from resetting between reports.

{{%notice note%}}
- Impacts both snapshot file collection and metric data export.
- Restarts the histogram service, initiating a new measurement cycle.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram temporality cumulative
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry export otlp grpc insecure</h>

Enables and disables `insecure` mode for <span class="a-tooltip">[gRPC ](## "Remote Procedure Call")</span> connections for telemetry. By default, OTLP export is in **secure mode** that requires a certificate. For connections without a configured certificate, you must enable `insecure` mode. You can specify `enabled` or `disabled`.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry export otlp grpc insecure enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry export otlp grpc certificate \<certificate-id\></h>

Configures an X.509 certificate to secure the <span class="a-tooltip">[gRPC ](## "Remote Procedure Call")</span> connection for telemetry export.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
- In Cumulus Linux 5.14 and earlier, this command is `nv set system telemetry export otlp grpc cert-id`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<certificate>` | The X.509 certificate. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system telemetry export otlp grpc certificate CERT....
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry export otlp grpc destination \<destination\> port \<port-id\></h>

Configures open telemetry export to use <span class="a-tooltip">[gRPC ](## "Remote Procedure Call")</span> to communicate with the collector. You must provide the collector destination IP address or hostname. Specify the port to use for communication if it is different from the default port 8443.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<destination>` | The IP address of the collector. |
| `<port-id>` |  The port number (if different from the default port 8443). |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.100 port 4317
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry export otlp grpc destination \<destination\> stats-group</h>

Applies the statistics group configuration to the OTLP destination.

By default, the switch exports all statistics enabled globally (with the `nv set system telemetry <statistics>` command) to all configured OTLP destinations. If you want to export different metrics to different OTLP destinations, you can customize the export by specifying a statistics group to control which statistics you export and the sample interval for a destination.

Statistics groups inherit global OTLP export configurations by default. More specific configuration under a statistics group, such as enabling or disabling a statistic type or changing the sample interval overrides any global OTLP configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<destination>` | The IP address of the collector. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.100 stats-group STAT-GROUP2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram export state</h>

Enables or disables open telemetry export for histogram collection. You can specify `enabled` or `disabled`.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
- When you enable open telemetry export for histogram data, your histogram collection configuration defines the data that the switch exports.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram ingress-buffer bin-min-boundary</h>

Configures the minimum boundary size of the ingress queue histograms. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the range of ingress queues per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295. The default minimum boundary size is 960 bytes.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram ingress-buffer bin-min-boundary`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram ingress-buffer bin-min-boundary 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram ingress-buffer histogram-size</h>

Configures the size of the ingress queue histogram. Adding this number to the minimum boundary size of the histogram produces the maximum boundary size. These values represent the range of ingress queues per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram ingress-buffer histogram-size`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram ingress-buffer histogram-size 12288
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram ingress-buffer sample-interval</h>

Configures the ingress queue histogram sampling interval. You can specify a value between 128 and 1000000000. The default value is 1024 nanoseconds.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram ingress-buffer sample-interval`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram ingress-buffer sample-interval 1024
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry interface-stats class phy state</h>

Configures collection and export of interface PHY metrics. You can specify `enabled` or `disabled`.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry interface-stats class phy state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry interface-stats egress-buffer traffic-class</h>

Configures the egress buffer traffic class for open telemetry export for interface statistics.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry interface-stats egress-buffer traffic-class 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry interface-stats ingress-buffer priority-group</h>

Configures the ingress buffer priority group for open telemetry export for interface statistics. You can set a value between 0 and 7.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry interface-stats ingress-buffer priority-group 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry interface-stats export state</h>

Enables and disables open telemetry export for interface statistics. You can specify `enabled` or `disabled`.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
- When you enable open telemetry export for interface statistics, the switch exports counters on all interfaces.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry interface-stats export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry interface-stats sample-interval</h>

Configures the interface statistics sample interval for open telemetry export. You can specify a value between 1 and 86400. The default value is 1.

{{%notice note%}}
- Cumulus Linux supports open telemetry export on switches with the Spectrum-4 ASIC only in Cumulus Linux 5.10.0 and later.
- Open telemetry export is a beta feature in Cumulus Linux 5.10.0.
- When you enable open telemetry export for interface statistics, the switch exports counters on all interfaces.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system telemetry interface-stats sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram latency bin-min-boundary</h>

Configures the global minimum boundary size of the latency histogram. Adding this number to the size of the histogram produces the maximum boundary size. You can specify a value, which must be a multiple of 96, between 96 and 4294967295. The default minimum boundary size is 960 bytes.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram latency bin-min-boundary`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram latency bin-min-boundary 960 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry histogram latency histogram-size</h>

Configures the global latency histogram size. Adding this number to the minimum boundary size of the histogram produces the maximum boundary size. You can specify a value, which must be a multiple of 96, between 96 and 4294967295.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry histogram latency histogram-size`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system telemetry histogram latency histogram-size 12288
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry lldp export state</h>

Enables and disables open telemetry LLDP statistics. You can specify `enabled` or `disabled`.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system telemetry lldp export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry lldp sample-interval</h>

Sets the sample interval for LLDP metrics. The default value is 10 seconds.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system telemetry lldp sample-interval 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry platform-stats class transceiver-info sample-interval</h>

Sets the sample interval for transceiver metrics. The default value is 60 seconds.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system telemetry platform-stats class transceiver-info sample-interval 40
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry platform-stats class transceiver-info state</h>

Enables and disables the export of transceiver temperature and power metrics.

You can specify `enabled` or `disabled`.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system telemetry platform-stats class transceiver-info state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry router bgp export state</h>

Enables and disables open telemetry for BGP peer state statistics.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry router bgp export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry router rib export state</h>

Enables and disables open telemetry routing table statistics.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry router rib export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry router sample-interval</h>

Configures the sample interval (in seconds) for routing metrics. You can specify a value in multiples of 10, up to 60. The default value is 30.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry router sample-interval 40
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry router vrf \<vrf\> bgp export state</h>

Enables and disables open telemetry BGP statistics for a VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry router vrf RED bgp export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry router vrf \<vrf\> bgp peer \<peer-id\> export state</h>

Enables and disables open telemetry specific BGP peer statistics for a VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry router vrf RED bgp peer swp51 export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry router vrf \<vrf\> rib export state</h>

Enables and disables open telemetry routing table statistics for a VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry router vrf RED rib export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot-file count</h>

Configures the number of snapshots you can create before Cumulus Linux overwrites the first snapshot file. For example, if you set the snapshot file count to 30, the first snapshot file is `histogram_stats_0` and the thirtieth snapshot is `histogram_stats_30`. After the thirtieth snapshot, Cumulus Linux overwrites the original snapshot file (`histogram_stats_0`) and the sequence restarts. The default value is 64.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry snapshot-file count`.
{{%/notice%}}

You can specify a value between 3 and 100.

{{%notice note%}}
Snapshots provide you with more data; however, they can occupy a lot of disk space on the switch. To reduce disk usage, you can use a volatile partition for the snapshot files; for example, /var/run/cumulus/histogram_stats.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot-file count 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot-file name \<value\></h>

Configures the snapshot file name and location. The default location and file name is `/var/lib/cumulus/histogram_stats`.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry snapshot-file name`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot-file name /var/lib/cumulus/histogram_stats
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot-interval</h>

Configures how often to write to a snapshot file. You can specify a value between 1 and 604800. The default value is 1 second.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, this command is `nv set service telemetry snapshot-interval`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot-interval 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot port-group \<port-group-id\></h>

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot port-group all-packet-pg
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot port-group \<port-group-id\>snapshot-file name</h>

Configures the name of the snapshot file for all interface packet and buffer statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot port-group all-packet-pg snapshot-file name /var/run/cumulus/all_packet_stats1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot port-group \<port-group-id\>snapshot-file count</h>

Configures the number of snapshots that you can create before the first snapshot file is overwritten.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot port-group all-packet-pg snapshot-file count 80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot port-group \<port-group-id\>threshold \<threshold-stats-id\> value</h>

Configures the threshold value for the statistics type; `packet-congestion-drops` or `packet-error-drops`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<threshold-stats-id>`| The type of threshold statistics; `packet-congestion-drops` or `packet-error-drops`.  |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot port-group all-packet-pg threshold packet-error-drops value 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot port-group \<port-group-id\>threshold \<threshold-stats-id\> action log</h>

Configures the action to log for the statistics type; `packet-congestion-drops` or `packet-error-drops`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<threshold-stats-id>`| The type of threshold statistics; `packet-congestion-drops` or `packet-error-drops`. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot port-group all-packet-pg threshold packet-error-drops action log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot port-group \<port-group-id\>threshold \<threshold-stats-id\> action collect port-group <value></h>

Configures the action to collect information for the port group statistics type; `packet-congestion-drops` or `packet-error-drops`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `<threshold-stats-id>`| The type of threshold statistics; `packet-congestion-drops` or `packet-error-drops`. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot port-group all-packet-pg threshold packet-error-drops action collect port-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot port-group \<port-group-id\>stats-type</h>

Configures the type of packet and buffer statistics you want to collect. You can collect the following data types:
- All, good, and dropped packets, and the ingress and egress queue occupancy (`packet-all`)
- All and good packets (`packet`)
- All, good, and dropped packets (`packet-extended`)
- Ingress and egress queue occupancy (`buffer`)

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot port-group packet-all-pg stats-type packet
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot port-group \<port-group-id\>interface \<interface-id\></h>

Configures the interfaces on which you want to monitor interface and buffer statistics. Specify `all` to monitor all interfaces.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |
| `interface-id>`| The name of the interface. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot port-group packet-all-pg interface all
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry snapshot port-group \<port-group-id\>timer-interval</h>

Configures the interval timer (how often to send the interface statistics to the snapshot file). There is no default value for this setting. If you do not configure this setting, you must configure the collect action. You also have the option to send a message to the `/var/log/syslog` file.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-group-id>`| The port group ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system telemetry snapshot port-group packet-all-pg timer-interval 15
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\></h>

Configures a statistics group name.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> interface-stats export state</h>

Configures a statistics group to export all interface statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 interface-stats export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> interface-stats sample-interval</h>

Configures the sample interval for the statistics group for interface statistics. You can specify a value between 1 and 86400. The default value is 1.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 interface-stats sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> buffer-stats export state</h>

Configures a custom statistics group to export all buffer statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 buffer-stats export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> buffer-stats sample-interval</h>

Configures the sample interval for the custom statistics group for buffer statistics. You can specify a value between 1 and 86400. The default value is 1.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP2 buffer-stats sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> histogram export state</h>

Configures a custom statistics group to export histogram statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 histogram export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> router export state</h>

Configures a custom statistics group to export router statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 router export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> router sample-interval <interval></h>

Configures the sample interval for the custom statistics group for router statistics. You can specify a value between 1 and 86400. The default value is 1.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP2 router sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> control-plane-stats export state</h>

Configures a custom statistics group to export control plane statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 control-plane-stats export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> control-plane-stats sample-interval</h>

Configures the sample interval for the custom statistics group for control plane statistics. You can specify a value between 1 and 86400. The default value is 1.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP2 control-plane-stats sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats export state</h>

Configures a custom statistics group to export platform statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 platform-stats export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats export sample-interval</h>

Configures the sample interval for the custom statistics group for platform statistics. You can specify a value between 1 and 86400. The default value is 1.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP2 platform-stats sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats class cpu state</h>

Configures a custom statistics group to export CPU platform statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 platform-stats class cpu export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats class cpu sample-interval 

Configures the sample interval for the custom statistics group for CPU platform statistics. You can specify a value between 1 and 86400. The default value is 1.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP2 platform-stats class cpu sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats class disk state</h>

Configures a custom statistics group to export disk platform statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 platform-stats class disk export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats class disk sample-interval</h>

Configures the sample interval for the custom statistics group for disk platform statistics. You can specify a value between 1 and 86400. The default value is 1.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP2 platform-stats class disk sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats class file-system state</h>

Configures a custom statistics group to export file system platform statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 platform-stats class file-system export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats class file-system sample-interval</h>

Configures the sample interval for the custom statistics group for file system platform statistics. You can specify a value between 1 and 86400. The default value is 1.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP2 platform-stats class file-system sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats class environment-sensor state</h>

Configures a custom statistics group to export environment-sensor platform statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 platform-stats class environment-sensor export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats class environment-sensor sample-interval</h> 

Configures the sample interval for the custom statistics group for environment sensor platform statistics. You can specify a value between 1 and 86400. The default value is 1.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP2 platform-stats class environment-sensor sample-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats class memory state</h>

Configures a custom statistics group to export memory platform statistics.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP1 platform-stats class memory export state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system telemetry stats-group \<stats-group-id\> platform-stats class memory sample-interval</h>

Configures the sample interval for the custom statistics group for memory platform statistics. You can specify a value between 1 and 86400. The default value is 1.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<stats-group-id>`| The statistics group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system telemetry stats-group STAT-GROUP2 platform-stats class memory sample-interval 100
```
