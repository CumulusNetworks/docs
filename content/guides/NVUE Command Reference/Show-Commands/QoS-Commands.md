---
title: QoS Commands
author: Cumulus Networks
weight: 260
product: Cumulus Linux
type: nojsscroll
---
## nv show qos

Shows detailed information about the configured buffers, utilization, and DSCP markings for QoS.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos
```

- - -

## nv show qos advance-buffer-config

Shows QoS advanced buffer configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config
```

- - -

## nv show qos advance-buffer-config <profile-id>

Shows configuration for the specified QoS advanced buffer profile.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global
```

- - -

## nv show qos advance-buffer-config <profile-id> ingress-pool

Shows all ingress service pool settings for the specified QoS advanced buffer profile.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-pool
```

- - -

## nv show qos advance-buffer-config <profile-id> ingress-pool <pool-id>

Shows the configuration settings for the specified ingress service pool for the specified QoS advanced buffer profile.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-pool ???
```

- - -

## nv show qos advance-buffer-config <profile-id> egress-pool

Shows all egress service pool settings for the specified QoS advanced buffer profile.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-pool
```

- - -

## nv show qos advance-buffer-config <profile-id> egress-pool <pool-id>

Shows the configuration settings for the specified egress service pool for the specified QoS advanced buffer profile.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-pool ???
```

- - -

## nv show qos advance-buffer-config <profile-id> ingress-lossy-buffer

Shows ingress lossy configuration settings for the specified QoS advanced buffer profile.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer
```

- - -

## nv show qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group

Shows ingress lossy priority group configuration settings for the specified QoS advanced buffer profile.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group
```
- - -

## nv show qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id>

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group ??? 
```

- - -

## nv show qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> switch-priority

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group ??? switch-priority
```

- - -

## nv show qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> switch-priority <qos-sp-id>

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group ??? switch-priority ???
```

- - -

## nv show qos advance-buffer-config <profile-id> ingress-lossless-buffer

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer
```

- - -

## nv show qos advance-buffer-config <profile-id> egress-lossless-buffer

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer
```

- - -


## nv show qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer traffic-class
```

- - -

## nv show qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id>

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer traffic-class ???
```

- - -

## nv show qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority
```

- - -

## nv show qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id>

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority ???
```

- - -

## nv show qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-port

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer multicast-port

```

- - -

## nv show qos traffic-pool

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos traffic-pool
```

- - -

## nv show qos traffic-pool <traffic-pool-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos traffic-pool ???
```

- - -

## nv show qos traffic-pool <traffic-pool-id> switch-priority

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos traffic-pool ??? switch-priority
```

- - -

## nv show qos traffic-pool <traffic-pool-id> switch-priority <qos-sp-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos traffic-pool ??? switch-priority ???
```

- - -

## nv show qos link-pause

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos link-pause
```

- - -

## nv show qos link-pause <profile-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos link-pause ??
```

- - -

## nv show qos pfc

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos pfc
```

- - -

## nv show qos pfc <profile-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos pfc ??
```

- - -

## nv show qos pfc <profile-id> switch-priority

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos pfc ?? switch-priority
```

- - -

## nv show qos pfc <profile-id> switch-priority <qos-sp-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos pfc ?? switch-priority ???
```

- - -

## nv show qos mapping

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos mapping
```

- - -

## nv show qos mapping <profile-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos mapping ??
```

- - -

## nv show qos mapping <profile-id> pcp

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos mapping ?? pcp
```

- - -

## nv show qos mapping <profile-id> pcp <qos-pcp-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos mapping ?? pcp ???
```

- - -

## nv show qos mapping <profile-id> dscp

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos mapping ?? dscp
```

- - -

## nv show qos mapping <profile-id> dscp <qos-dscp-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos mapping ?? dscp ???
```

- - -

## nv show qos remark

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos remark
```

- - -

## nv show qos remark <profile-id>

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos remark ??
```

- - -

## nv show qos remark <profile-id> switch-priority

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos remark ?? switch-priority
```

- - -

## nv show qos remark <profile-id> switch-priority <qos-sp-id>

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos remark ?? switch-priority ???
```

- - -

## nv show qos congestion-control

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos congestion-control
```

- - -

## nv show qos congestion-control <profile-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos congestion-control ??
```

- - -

## nv show qos congestion-control <profile-id> traffic-class

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos congestion-control ?? traffic-class
```

- - -

## nv show qos congestion-control <profile-id> traffic-class <qos-tc-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos congestion-control ?? traffic-class ???
```

- - -

## nv show qos egress-queue-mapping

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-queue-mapping
```

- - -

## nv show qos egress-queue-mapping <profile-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-queue-mapping ??
```

## nv show qos egress-queue-mapping <profile-id> switch-priority

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-queue-mapping ?? switch-priority
```

- - -

## nv show qos egress-queue-mapping <profile-id> switch-priority <qos-sp-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-queue-mapping ?? switch-priority ???
```

- - -

## nv show qos egress-scheduler

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-scheduler
```

- - -

## nv show qos egress-scheduler <profile-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-scheduler ??
```

- - -

## nv show qos egress-scheduler <profile-id> traffic-class

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-scheduler ?? traffic-class
```

- - -

## nv show qos egress-scheduler <profile-id> traffic-class <qos-tc-id>

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-scheduler ?? traffic-class ???
```

- - -

## nv show qos egress-shaper

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-shaper
```

- - -

## nv show qos egress-shaper <profile-id>

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-shaper ??
```

- - -

## nv show qos egress-shaper <profile-id> traffic-class

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-shaper ?? traffic-class
```

- - -

## nv show qos egress-shaper <profile-id> traffic-class <qos-tc-id>

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-shaper ?? traffic-class ???
```

- - -

## nv show qos roce

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos
```

- - -

## nv show qos roce prio-map

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos
```

- - -

## nv show qos roce tc-map

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos
```

- - -

## nv show qos roce pool-map

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos
```

- - -

## nv show qos roce pool

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos
```

- - -

## nv show qos buffer

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos
```

- - -

## nv show qos buffer pool

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos
```

- - -

## nv show qos buffer multicast-switch-priority

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos
```

- - -

## nv show interface \<interface-id\> qos

Shows QoS configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos
```

- - -

## nv show interface \<interface-id\> qos counter

Shows the QoS counters for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter
```

- - -

## nv show interface \<interface-id\> qos counter port-stats

Shows QoS port statistics for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter port-stats
```

- - -

## nv show interface \<interface-id\> qos counter port-stats rx-stats

Shows QoS statistics for received packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter port-stats rx-stats
```

- - -

## nv show interface \<interface-id\> qos counter port-stats tx-stats

Shows QoS statistics for transmitted packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter port-stats tx-stats
```

- - -

## nv show interface \<interface-id\> qos counter egress-queue-stats

Shows egress queue statistics per egress traffic class for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter egress-queue-stats
```

- - -

## nv show interface \<interface-id\> qos counter ingress-buffer-stats

Shows ingress buffer statistics per priority group for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter ingress-buffer-stats
```

- - -

## nv show interface \<interface-id\> qos counter pfc-stats

Shows PFC statistics per internal switch priority for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter pfc-stats
```

- - -

## nv show interface \<interface-id\> qos roce

Shows a summary of RoCE information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos roce
```

- - -

## nv show interface \<interface-id\> qos roce counters

Shows RoCE counters for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos roce counters
```

- - -

## nv show interface \<interface-id\> qos roce status

Shows RoCE status information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos roce status
```

- - -

## nv show interface \<interface-id\> qos roce status pool-map

Shows ingress and egress service pool configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos roce pool-map
```

- - -

## nv show interface \<interface-id\> qos roce status prio-map

Shows the RoCE PCP or DSCP to switch priority mapping configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos roce prio-map
```

- - -

## nv show interface \<interface-id\> qos roce status tc-map

Shows the RoCE switch priority to traffic class mapping and ETS configurations for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos roce status tc-map
```
