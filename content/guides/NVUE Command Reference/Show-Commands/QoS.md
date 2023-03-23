---
title: QoS
author: Cumulus Networks
weight: 340
product: Cumulus Linux
type: nojsscroll
---
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

## nv show interface \<interface-id\> qos buffer

Shows QoS buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos buffer
```

- - -

## nv show interface \<interface-id\> qos buffer ingress-port

Shows QoS ingress port buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos buffer ingress-port
```

- - -

## nv show interface \<interface-id\> qos buffer ingress-priority-group

Shows QoS priority group ingress buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos buffer ingress-priority-group
```

- - -

## nv show interface \<interface-id\> qos buffer egress-port

Shows QoS egress port buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos buffer egress-port
```

- - -

## nv show interface \<interface-id\> qos buffer egress-traffic-class

Shows QoS egress traffic class buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos buffer egress-traffic-class
```

- - -

## nv show interface \<interface-id\> qos buffer egress-multicast

Shows QoS egress multicast traffic buffer configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos buffer egress-multicast
```

- - -

## nv show interface \<interface-id\> qos congestion-control

Shows QoS congestion control configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos congestion-control
```

- - -

## nv show interface \<interface-id\> qos congestion-control traffic-class

Shows QoS congestion control traffic class configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos congestion-control traffic-class
```

- - -

## nv show interface \<interface-id\> qos congestion-control traffic-class \<qos-tc-id\>

Shows specific QoS congestion control traffic class configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-tc-id>` | The traffic class value. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos congestion-control traffic-class 2
```

- - -

## nv show interface \<interface-id\> qos counter

Shows the QoS counters for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.1, this command is `nv show interface <interface-id> qos counters`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter
```

- - -

## nv show interface \<interface-id\> qos counter egress-queue-stats

Shows egress queue statistics per egress traffic class for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.1, this command is `nv show interface <interface-id> qos counters egress-queue-stats`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter egress-queue-stats
```

- - -

## nv show interface \<interface-id\> qos counter ingress-buffer-stats

Shows ingress buffer statistics per priority group for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.1, this command is `nv show interface <interface-id> qos counters ingress-buffer-stats`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter ingress-buffer-stats
```

- - -

## nv show interface \<interface-id\> qos counter pfc-stats

Shows PFC statistics per switch priority for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.1, this command is `nv show interface <interface-id> qos counters pfc-stats`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter pfc-stats
```

- - -

## nv show interface \<interface-id\> qos counter port-stats

Shows QoS port statistics for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.1, this command is `nv show interface <interface-id> qos counters port-stats`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter port-stats
```

- - -

## nv show interface \<interface-id\> qos counter port-stats rx-stats

Shows QoS statistics for received packets on the specified interface.

{{%notice note%}}
In Cumulus Linux 5.1, this command is `nv show interface <interface-id> qos counters rx-stats`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter port-stats rx-stats
```

- - -

## nv show interface \<interface-id\> qos counter port-stats tx-stats

Shows QoS statistics for transmitted packets on the specified interface.

{{%notice note%}}
In Cumulus Linux 5.1, this command is `nv show interface <interface-id> qos counters port-stats tx-stats`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos counter port-stats tx-stats
```

- - -

## nv show interface \<interface-id\> qos egress-queue-mapping

Shows QoS egress queue mapping configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos egress-queue-mapping
```

- - -

## nv show interface \<interface-id\> qos egress-queue-mapping switch-priority

Shows QoS egress queue switch priority mapping configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos egress-queue-mapping switch-priority
```

- - -

## nv show interface \<interface-id\> qos egress-queue-mapping switch-priority \<qos-sp-id\>

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
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos egress-queue-mapping switch-priority 2
```

- - -

## nv show interface \<interface-id\> qos egress-scheduler

Shows QoS egress scheduler configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos egress-scheduler
```

- - -

## nv show interface \<interface-id\> qos egress-scheduler traffic-class

Shows QoS egress scheduler traffic class configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos egress-scheduler traffic-class
```

- - -

## nv show interface \<interface-id\> qos egress-scheduler traffic-class \<qos-tc-id\>

Shows specific QoS egress scheduler traffic class configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-tc-id>` | The traffic class value. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos egress-scheduler traffic-class 2
```

- - -

## nv show interface \<interface-id\> qos egress-shaper

Shows QoS egress shaper configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos egress-shaper
```

- - -

## nv show interface \<interface-id\> qos egress-shaper traffic-class

Shows QoS egress shaper traffic class configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos egress-shaper traffic-class

```

- - -

## nv show interface \<interface-id\> qos egress-shaper traffic-class \<qos-tc-id\>

Shows specific QoS egress shaper traffic class configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<qos-tc-id>` | The traffic class value. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos egress-shaper traffic-class 2
```

- - -

## nv show interface \<interface-id\> qos link-pause

Shows QoS link pause configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos link-pause
```

- - -

## nv show interface \<interface-id\> qos mapping

Shows QoS mapping configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos mapping
```

- - -

## nv show interface \<interface-id\> qos mapping dscp

Shows DSCP mapping configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos mapping dscp
```

- - -

## nv show interface \<interface-id\> qos mapping dscp \<qos-dscp-id\>

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
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos qos mapping dscp 22
```

- - -

## nv show interface \<interface-id\> qos mapping pcp

Shows QoS 802.1p (PCP) mapping configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos mapping pcp
```

- - -

## nv show interface \<interface-id\> qos mapping pcp \<qos-pcp-id\>

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
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos mapping pcp 2
```

- - -

## nv show interface \<interface-id\> qos pfc

Shows QoS PFC configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos pfc
```

- - -

## nv show interface \<interface-id\> qos remark

Shows QoS remarking configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos remark
```

- - -

## nv show interface \<interface-id\> qos remark switch-priority

Shows QoS switch priority remarking configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos remark switch-priority

```

- - -

## nv show interface \<interface-id\> qos remark switch-priority \<qos-sp-id\>

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
cumulus@leaf01:mgmt:~$ nv show interface swp5 qos remark switch-priority 2
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

Shows the RoCE 802.1p (PCP) or DSCP to switch priority mapping configuration for the specified interface.

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

Shows the RoCE switch priority to traffic class mapping for the specified interface.

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

- - -

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

## nv show qos advance-buffer-config \<profile-id\>

Shows configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global
```

- - -

## nv show qos advance-buffer-config \<profile-id\> egress-pool

Shows all egress service pool settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-pool
```

- - -

## nv show qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-pool 3
```

- - -

## nv show qos advance-buffer-config \<profile-id\> egress-lossless-buffer

Shows egress lossless buffer configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer
```

- - -

## nv show qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-port

Shows egress lossless buffer multicast port configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer multicast-port
```

- - -

## nv show qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority

Shows egress lossless buffer multicast switch priority configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority
```

- - -

## nv show qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 2
```

- - -

## nv show qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class

Shows egress lossless buffer traffic class configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer traffic-class
```

- - -

## nv show qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global egress-lossy-buffer traffic-class 2
```

- - -

## nv show qos advance-buffer-config \<profile-id\> ingress-pool

Shows all ingress service pool settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-pool
```

- - -

## nv show qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-pool 3
```

- - -

## nv show qos advance-buffer-config \<profile-id\> ingress-lossless-buffer

Shows ingress lossless buffer configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer
```

- - -

## nv show qos advance-buffer-config \<profile-id\> ingress-lossy-buffer

Shows ingress lossy buffer configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer
```

- - -

## nv show qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group

Shows ingress lossy buffer priority group configuration settings for the specified QoS advanced buffer profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group
```
- - -

## nv show qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1
```

- - -

## nv show qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> switch-priority

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
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 switch-priority
```

- - -

## nv show qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> switch-priority \<qos-sp-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 switch-priority 2
```

- - -

## nv show qos buffer

Shows QoS buffer configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos buffer
```

- - -

## nv show qos buffer pool

Shows QoS buffer traffic pool configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos buffer pool
```

- - -

## nv show qos buffer multicast-switch-priority

Shows QoS buffer multicast switch priority configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos buffer multicast-switch-priority
```

- - -

## nv show qos congestion-control

Shows QoS congestion control configuration settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos congestion-control
```

- - -

## nv show qos congestion-control \<profile-id\>

Shows configuration settings for the specified QoS congestion control profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos congestion-control default-global
```

- - -

## nv show qos congestion-control \<profile-id\> traffic-class

Shows traffic class configuration settings for the specified QoS congestion control profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos congestion-control default-global traffic-class
```

- - -

## nv show qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\>

Shows specific traffic class configuration settings for the specified QoS congestion control profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-tc-id>` | The traffic class value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos congestion-control default-global traffic-class 4
```

- - -

## nv show qos egress-queue-mapping

Shows egress queue mapping configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-queue-mapping
```

- - -

## nv show qos egress-queue-mapping \<profile-id\>

Shows configuration settings for the specified egress queue mapping profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-queue-mapping default-global
```

- - -

## nv show qos egress-queue-mapping \<profile-id\> switch-priority

Shows switch priority configuration settings for the specified egress queue mapping profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-queue-mapping default-global switch-priority
```

- - -

## nv show qos egress-queue-mapping \<profile-id\> switch-priority \<qos-sp-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos egress-queue-mapping default-global switch-priority 2
```

- - -

## nv show qos egress-scheduler

Shows QoS egress scheduler configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-scheduler
```

- - -

## nv show qos egress-scheduler \<profile-id\>

Shows configuration settings for the specified QoS egress scheduler profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-scheduler default-global
```

- - -

## nv show qos egress-scheduler \<profile-id\> traffic-class

Shows traffic class configuration settings for the specified QoS egress scheduler profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-scheduler default-global traffic-class
```

- - -

## nv show qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\>

Shows specific traffic class configuration settings for the specified QoS egress scheduler profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-tc-id>` | The traffic class value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-scheduler default-global traffic-class 2
```

- - -

## nv show qos egress-shaper

Shows QoS egress shaper configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-shaper
```

- - -

## nv show qos egress-shaper \<profile-id\>

Shows configuration settings for the specified QoS egress shaper profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-shaper shaper1
```

- - -

## nv show qos egress-shaper \<profile-id\> traffic-class

Shows traffic class configuration settings for the specified QoS egress shaper profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-shaper shaper1 traffic-class
```

- - -

## nv show qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\>

Shows specific traffic class configuration settings for the specified QoS egress shaper profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|
| `<qos-tc-id>` | The traffic class value.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos egress-shaper shaper1 traffic-class 2
```

- - -

## nv show qos link-pause

Shows QoS link pause configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos link-pause
```

- - -

## nv show qos link-pause \<profile-id\>

Shows configuration settings for the specified QoS link pause profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos link-pause my_pause_ports
```

- - -

## nv show qos mapping

Shows QoS mapping configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos mapping
```

- - -

## nv show qos mapping \<profile-id\>

Shows configuration settings for the specified QoS mapping profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos mapping default-global
```

- - -

## nv show qos mapping \<profile-id\> pcp

Shows 802.1p mapping configuration settings for the specified profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos mapping default-global pcp
```

- - -

## nv show qos mapping \<profile-id\> pcp \<qos-pcp-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos mapping default-global pcp 0
```

- - -

## nv show qos mapping \<profile-id\> dscp

Shows DSCP mapping configuration settings for the specified profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos mapping default-global dscp
```

- - -

## nv show qos mapping \<profile-id\> dscp \<qos-dscp-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos mapping default-global dscp 22
```

- - -

## nv show qos pfc

Shows QoS PFC configuration settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos pfc
```

- - -

## nv show qos pfc \<profile-id\>

Shows QoS configuration settings for the specified PFC profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos pfc default-global
```

- - -

## nv show qos pfc \<profile-id\> switch-priority

Shows switch priority configuration settings for the specified PFC profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos pfc default-global switch-priority
```

- - -

## nv show qos pfc \<profile-id\> switch-priority \<qos-sp-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos pfc default-global switch-priority 2
```

- - -

## nv show qos remark

Shows QoS remarking configuration settings.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos remark
```

- - -

## nv show qos remark \<profile-id\>

Shows configuration settings for the specified QoS remarking profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos remark default-global
```

- - -

## nv show qos remark \<profile-id\> switch-priority

Shows switch priority configuration settings for the specified QoS remarking profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<profile-id>` | The profile name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos remark default-global switch-priority
```

- - -

## nv show qos remark \<profile-id\> switch-priority \<qos-sp-id\>

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
cumulus@leaf01:mgmt:~$ nv show qos remark default-global switch-priority 2
```

- - -

## nv show qos roce

Shows QoS <span style="background-color:#F5F5DC">[ROCE](## "RDMA over Converged Ethernet")</span> configuration, such as the configured buffers, utilization and DSCP markings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos roce
```

- - -

## nv show qos roce prio-map

Shows QoS ROCE priority map configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos roce prio-map
```

- - -

## nv show qos roce tc-map

Shows QoS ROCE traffic class map configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos roce tc-map
```

- - -

## nv show qos roce pool-map

Shows QoS ROCE traffic pool map configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos roce pool-map
```

- - -

## nv show qos roce pool

Shows QoS ROCE traffic pool configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos roce pool
```

- - -

## nv show qos traffic-pool

Shows QoS traffic pool configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos traffic-pool
```

- - -

## nv show qos traffic-pool \<traffic-pool-id\>

Shows configuration settings for a specific QoS traffic pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<traffic-pool-id>` | The traffic pool name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos traffic-pool default-lossy
```

- - -

## nv show qos traffic-pool \<traffic-pool-id\> switch-priority

Shows switch priority configuration settings for a specific QoS traffic pool.

| Syntax |  Description   |
| --------- | -------------- |
| `<traffic-pool-id>` | The traffic pool name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos traffic-pool default-lossy switch-priority
```

- - -

## nv show qos traffic-pool \<traffic-pool-id\> switch-priority \<qos-sp-id\>

Shows configuration settings for a specific switch priority for the specified QoS traffic pool.

| Syntax |  Description   |
| --------- | -------------- |
| `<traffic-pool-id>` | The traffic pool name.|
| `<qos-sp-id>` | The switch priority value.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show qos traffic-pool default-lossy switch-priority 2
```

- - -
