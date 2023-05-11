---
title: PTP
author: Cumulus Networks
weight: 310

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> ptp</h>

Shows PTP configuration and counters for a specific VLAN interface on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>`   |  The bridge domain. |
| `<vid-id>`   |  The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show bridge domain br_default vlan 10 ptp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> counters ptp</h>

Shows PTP statistics for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv show interface <interface-id> ptp counters`
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters ptp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ptp</h>

Shows PTP configuration and counters for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`   |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show interface swp1 ptp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ptp shaper</h>

Shows if PTP shaper is enabled on the specified PTP interface.

{{%notice note%}}
This command is available for the NVIDIA Spectrum 1 switch only for PTP-enabled ports with speeds lower than 100G.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`   |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ptp shaper
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ptp timers</h>

Shows PTP timer settings for the specified PTP interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`   |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ptp timers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp</h>

Shows global PTP configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\></h>

Shows configuration for the specified PTP instance. PTP commands require an instance number for management purposes.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> acceptable-master</h>

Shows the acceptable master clocks for the specified PTP instance.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 acceptable-master
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> acceptable-master \<clock-id\></h>

Shows the configuration settings for the specified acceptable master clock.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|
| `<clock-id>`  |  The clock ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> current</h>

Shows the local states learned from the exchange of PTP messages for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 current
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> clock-quality</h>

Shows the clock quality status, such as accuracy, class and the offset scaled log variance, for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 clock-quality
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor</h>

Shows the PTP monitor configuration for the specified PTP instance, such as the minimum and maximum difference allowed between the master and slave time, the mean time that PTP packets take to travel between the master and slave, the maximum number of timestamp entries allowed, the maximum number of violation log sets allowed, the maximum number of violation log entries allowed for each set, and the violation log interval.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 monitor
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor timestamp-log</h>

Shows the monitor timestamp log for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 monitor timestamp-log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations</h>

Shows the PTP violations for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 monitor violations
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log</h>

Shows all the PTP violation logs for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 monitor violations log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log acceptable-master</h>

Shows the acceptable master violation logs for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$   nv show service ptp 1 monitor violations log acceptable-master
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log forced-master</h>

Shows the forced master violation logs for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 monitor violations log forced-master
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log max-offset</h>

Shows violation logs for the maximum difference allowed between the master and slave time for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 monitor violations log max-offset
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log min-offset</h>

Shows violation logs for the minimum difference allowed between the master and slave time for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 monitor violations log min-offset
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log path-delay</h>

Shows violation logs for the mean time that PTP packets take to travel between the master and slave for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 monitor violations log path-delay
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> parent</h>

Shows global PTP parent information.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 parent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> parent grandmaster-clock-quality</h>

Shows the grandmaster clock quality for the PTP parent.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 parent grandmaster-clock-quality
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> profile</h>

Shows the predefined and custom PTP profiles configured for the specified PTP instance. Predefined profiles are a standardized set of configurations and rules intended to meet the requirements of a specific application. A custom profile is based off a predefined profile. Profiles define required, allowed, and restricted PTP options, network restrictions, and performance requirements.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 profile
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> profile \<profile-id\></h>

Shows configuration settings for a specific PTP profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 profile CUSTOM1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> status</h>

Shows PTP status.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>` | The PTP instance number. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 status
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> time-properties</h>

Shows time properties for the specified PTP instance, such as the current UTC offset and the PTP time scale.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>` | The PTP instance number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 time-properties
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> unicast-master</h>

Shows the PTP unicast master table configuration on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$  nv show service ptp 1 unicast-master
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> unicast-master \<table-id\></h>

Shows information about a specific PTP unicast master table on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|
| `<table-id>`  | The unicast master table ID.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 unicast-master 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> unicast-master \<table-id\> address</h>

Shows the IP addresses of the specified PTP unicast master table.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|
| `<table-id>`  | The unicast master table ID.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 unicast-master 1 address
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> unicast-master \<table-id\> address \<ip-mac-address-id\></h>

Shows information about a specific IP or MAC address for the specified PTP unicast master table.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|
| `<table-id>`  | The unicast master table ID.|
| `<ip-mac-address-id>`  | The IP or MAC address.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 unicast-master 1 address 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> ptp</h>

Shows PTP configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$  nv show vrf default ptp
```
