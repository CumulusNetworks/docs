---
title: PTP
author: Cumulus Networks
weight: 310
product: Cumulus Linux
type: nojsscroll
---
## nv show bridge domain \<domain-id\> vlan \<vid\> ptp

Shows configuration and counters for the specified VLAN interface on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`   |  The interface name. |
| `<vid-id>`   |  The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show bridge domain br_default vlan 10 ptp
```

- - -

## nv show interface \<interface-id\> counters ptp

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
cumulus@leaf01:mgmt:~$ nv show interface swp1 counters ptp
```

- - -

## nv show interface \<interface-id\> ptp

Shows configuration and counters for the specified PTP interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`   |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show interface swp1 ptp
```

- - -

## nv show interface \<interface-id\> ptp shaper

Shows if PTP shaper is enabled on the specified PTP interface.

This command is available for the NVIDA Spectrum 1 switch only for PTP-enabled ports with speeds lower than 100G.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`   |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ptp shaper
```

- - -

## nv show interface \<interface-id\> ptp timers

Shows PTP timer settings for the specified PTP interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`   |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ptp timers
```

- - -

## nv show service ptp

Shows global PTP configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp
```

- - -

## nv show service ptp \<instance-id\>

Shows configuration for the specified PTP instance. PTP commands require an instance number for management purposes.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1
```

- - -

## nv show service ptp \<instance-id\> acceptable-master

Shows the acceptable master clocks for the specified PTP instance.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 acceptable-master
```

- - -

## nv show service ptp \<instance-id\> acceptable-master \<clock-id\>

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
cumulus@leaf01:mgmt:~$  nv show service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06
```

- - -

## nv show service ptp \<instance-id\> current

Shows the local states learned from the exchange of PTP messages for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 current
```

- - -

## nv show service ptp \<instance-id\> clock-quality

Shows the clock quality status, such as accuracy, class and the offset scaled log variance, for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 clock-quality
```

- - -

## nv show service ptp \<instance-id\> monitor

Shows the PTP monitor configuration for the specified PTP instance, such as the minimum and maximum difference allowed between the master and slave time, the mean time that PTP packets take to travel between the master and slave, the maximum number of timestamp entries allowed, the maximum number of violation log sets allowed and the maximum number of violation log entries allowed for each set, and the violation log interval.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 monitor
```

- - -

## nv show service ptp \<instance-id\> monitor timestamp-log

Shows the monitor timestamp log for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 monitor timestamp-log
```

- - -

## nv show service ptp \<instance-id\> monitor violations

Shows the PTP violations for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 monitor violations
```

- - -

## nv show service ptp \<instance-id\> monitor violations log

Shows all the PTP violation logs for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 monitor violations log
```

- - -

## nv show service ptp \<instance-id\> monitor violations log acceptable-master

Shows the acceptable master violation logs for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$   nv show service ptp 1 monitor violations log acceptable-master
```

- - -

## nv show service ptp \<instance-id\> monitor violations log forced-master

Shows the forced master violation logs for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 monitor violations log forced-master
```

- - -

## nv show service ptp \<instance-id\> monitor violations log max-offset

Shows violation logs for the maximum difference allowed between the master and slave time for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 monitor violations log max-offset
```

- - -

## nv show service ptp \<instance-id\> monitor violations log min-offset

Shows violation logs for the minimum difference allowed between the master and slave time for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 monitor violations log min-offset
```

- - -

## nv show service ptp \<instance-id\> monitor violations log path-delay

Shows violation logs for the mean time that PTP packets take to travel between the master and slave for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 monitor violations log path-delay
```

- - -

## nv show service ptp \<instance-id\> parent

Shows global PTP parent information.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 parent
```

- - -

## nv show service ptp \<instance-id\> parent grandmaster-clock-quality

Shows the grandmaster clock quality for the PTP parent.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 parent grandmaster-clock-quality
```

- - -

## nv show service ptp \<instance-id\> profile

Shows the PTP profiles configured for the specified PTP instance. PTP profiles are a standardized set of configurations and rules intended to meet the requirements of a specific application. Profiles define required, allowed, and restricted PTP options, network restrictions, and performance requirements.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service ptp 1 profile
```

- - -

## nv show service ptp \<instance-id\> profile \<profile-id\>

Shows configuration settings for a specific PTP profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service ptp 1 profile CUSTOM1
```

- - -

## nv show service ptp \<instance-id\> status

Shows PTP status.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>` | The PTP instance number. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service ptp 1 status
```

- - -

## nv show service ptp \<instance-id\> time-properties

Shows time properties for the specified PTP instance, such as the current UTC offset and the PTP time scale.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>` | The PTP instance number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 time-properties
```

- - -

## nv show service ptp \<instance-id\> unicast-master

Shows the PTP unicast master table configuration on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show service ptp 1 unicast-master
```

- - -

## nv show service ptp \<instance-id\> unicast-master \<table-id\>

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
cumulus@leaf01:mgmt:~$ nv show service ptp 1 unicast-master 1
```

- - -

## nv show service ptp \<instance-id\> unicast-master \<table-id\> address

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
cumulus@leaf01:mgmt:~$ nv show service ptp 1 unicast-master 1 address
```

- - -

## nv show service ptp \<instance-id\> unicast-master \<table-id\> address \<ip-mac-address-id\>

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
cumulus@leaf01:mgmt:~$ nv show service ptp 1 unicast-master 1 address 10.10.10.1
```

- - -

## nv show vrf \<vrf-id\> ptp

Shows PTP configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$  nv show vrf default ptp
```

- - -
