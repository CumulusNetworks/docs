---
title: sFlow
author: Cumulus Networks
weight: 625

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow agent interface</h>

Configures the sFlow agent interface.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow agent interface eth0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow agent ip</h>

Configures the sFlow agent IP address or prefix.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow agent ip 10.0.0.0/8
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow collector

Configures the IP address of the designated sFlow collector.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow collector 192.0.2.100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow collector \<collector-ip\> interface</h>

Configures the interface for the designated sFlow collector.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<collector-ip>` |  The IP address of the collector. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow collector 192.0.2.200 interface eth0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow collector \<collector-ip\> port</h>

Configures the UDP port number for the designated sFlow collector.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<collector-ip>` |  The IP address of the collector. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow collector 192.0.2.100 port 6344
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow dropmon hw</h>

Configures sFlow to monitor dropped packets in hardware.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow dropmon shw 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow poll-interval</h>

Configures the sFlow polling interval in seconds.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow poll-interval 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow sampling-rate default</h>

Configures the sFlow sampling rate to use the default rate.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow sampling-rate default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow sampling-rate speed-100m</h>

Configures the sampling rate in number of packets for 100M interfaces.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-100m 40000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow sampling-rate speed-1g</h>

Configures the sampling rate in number of packets for 1G interfaces.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ 
```

## <h>nv set system sflow sampling-rate speed-10g</h>

Configures the sampling rate in number of packets for 10G interfaces.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-10G 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow sampling-rate speed-25g</h>

Configures the sampling rate in number of packets for 25G interfaces.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-25G 20000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow sampling-rate speed-40g</h>

Configures the sampling rate in number of packets for 40G interfaces.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-40G 40000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow sampling-rate speed-50g</h>

Configures the sampling rate in number of packets for 50G interfaces.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-50G 50000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow sampling-rate speed-100g</h>

Configures the sampling rate in number of packets for 100G interfaces.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-100G 100000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow sampling-rate speed-200g</h>

Configures the sampling rate in number of packets for 200G interfaces.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-200G 200000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow sampling-rate speed-400g</h>

Configures the sampling rate in number of packets for 400G interfaces.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-4000G 400000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow sampling-rate speed-800g</h>

Configures the sampling rate in number of packets for 800G interfaces.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-800G 800000
```
<!--
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow policer rate</h>

Configures the number of sFlow samples per second that the switch can send.

The default number of sFlow samples is 16384. You can specify a value between 0 and 16384.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow policer rate 8000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow policer burst</h>

Configures the sample burst size per second that the can switch send.

The default sample size is 16384. You can specify a value between 0 and 16384.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow policer burst 9000
```
-->
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system sflow state</h>

Enables and disables sFlow; a monitoring protocol that samples network packets, application operations, and system counters.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system sflow state enabled
```
