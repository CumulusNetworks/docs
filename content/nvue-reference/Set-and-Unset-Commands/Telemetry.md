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
| `<pg-id>` |  The priority group you want to monitor |

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
| `<pg-id>` |  The priority group you want to monitor |

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
| `<pg-id>` |  The priority group you want to monitor |

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
| `<pg-id>` |  The priority group you want to monitor |

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
| `<pg-id>` |  The priority group you want to monitor |

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
| `<pg-id>` |  The priority group you want to monitor |

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
| `<tc-id>` |  The traffic class you want to monitor |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram egress-buffer traffic-class 0 threshold value 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry histogram counter bin-min-boundary</h>

Configures the minimum boundary size of the counter histograms. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the number of counters per bin. You can specify a value, which must be a multiple of 96, between 1 and 4294967295. The default minimum boundary size is 960 bytes.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry histogram counter bin-min-boundary 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry histogram counter histogram-size</h>

Configures the size of the counter buffer histogram for the specified traffic class and interface. Adding this number to the minimum boundary size of the histogram produces the maximum boundary size. These values represent the number of counters per bin. You can specify a value, which must be a multiple of 96, between 1 and 4294967295.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry histogram counter histogram-size 12288
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry histogram counter sample-interval</h>

Configures the counter histogram sampling interval. You can specify a value between 128 and 1000000000. The default value is 1024 nanoseconds.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry histogram counter sample-interval 1024
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry histogram egress-buffer bin-min-boundary</h>

Configures the minimum boundary size of the egress queue histograms. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the range of egress queues per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295. The default minimum boundary size is 960 bytes.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry histogram egress-buffer  bin-min-boundary
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry histogram egress-buffer histogram-size 96-4294967295

Configures the size of the egress queue histogram. Adding this number to the minimum boundary size of the histogram produces the maximum boundary size. These values represent the range of egress queues per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry histogram egress-buffer histogram-size 12288
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry histogram egress-buffer sample-interval</h>

Configures the egress queue histogram sampling interval. You can specify a value between 128 and 1000000000. The default value is 1024 nanoseconds.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry histogram egress-buffer sample-interval 1024
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry histogram ingress-buffer bin-min-boundary 96-4294967295

Configures the minimum boundary size of the ingress queue histograms. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the range of ingress queues per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295. The default minimum boundary size is 960 bytes.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry histogram ingress-buffer bin-min-boundary 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry histogram ingress-buffer histogram-size</h>

Configures the size of the ingress queue histogram. Adding this number to the minimum boundary size of the histogram produces the maximum boundary size. These values represent the range of ingress queues per bin. You can specify a value, which must be a multiple of 96, between 96 and 4294967295.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry histogram ingress-buffer histogram-size 12288
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry histogram ingress-buffer sample-interval</h>

Configures the ingress queue histogram sampling interval. You can specify a value between 128 and 1000000000. The default value is 1024 nanoseconds.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry histogram ingress-buffer sample-interval 1024
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry snapshot-file count</h>

Configures the number of snapshots you can create before Cumulus Linux overwrites the first snapshot file. For example, if you set the snapshot file count to 30, the first snapshot file is `histogram_stats_0` and the thirtieth snapshot is `histogram_stats_30`. After the thirtieth snapshot, Cumulus Linux overwrites the original snapshot file (`histogram_stats_0`) and the sequence restarts. The default value is 64.

You can specify a value between 3 and 100.

{{%notice note%}}
Snapshots provide you with more data; however, they can occupy a lot of disk space on the switch. To reduce disk usage, you can use a volatile partition for the snapshot files; for example, /var/run/cumulus/histogram_stats.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry snapshot-file count 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry snapshot-file name <value></h>

Configures the snapshot file name and location. The default location and file name is `/var/lib/cumulus/histogram_stats`.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry snapshot-file name /var/lib/cumulus/histogram_stats
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service telemetry snapshot-interval</h>

Configures how often to write to a snapshot file. You can specify a value between 1 and 604800. The default value is 1 second.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service telemetry snapshot-interval 5
```
