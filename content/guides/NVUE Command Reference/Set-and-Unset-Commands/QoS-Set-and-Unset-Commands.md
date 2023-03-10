---
title: QoS Set and Unset Commands
author: Cumulus Networks
weight: 680
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set qos

Configures global Quality of Service (QOS) settings.

- - -

## nv set qos advance-buffer-config \<profile-id\>

Configures the QoS advanced buffer profile settings. Advanced buffer configuration can override the base traffic-pool profiles configured on the system.

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\>

Configures the QoS ingress service pool name.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-pool 3
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> memory-percent

Configures the ingress service pool memory percent allocation. You can specify a value between 0 and 100.

The sum of `memory-percent` values across all ingress pools must be less than or equal to 100 percent.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-pool 3 memory-percent 20
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> infinite

Configures the ingress service pool flag to infinite. You can specify `true` or `false`. The default setting is `false`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-pool 3 infinite true
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> mode

Configures the ingress service pool mode. You can specify `static` or `dynamic`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-pool 3 mode dynamic
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> reserved

Configures the ingress service pool reserved buffer allocation in bytes. You can specify a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-pool 3 reserved 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> shared-bytes

Configures the ingress service pool static shared buffer allocation in bytes. You can specify a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-pool 3 shared-bytes 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> shared-alpha

Configures the ingress service pool dynamic shared buffer alpha allocation.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-pool 3 shared-alpha alpha_1_4
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\>

Configures the QoS egress service pool ID.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-pool 3
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> memory-percent

Configures the egress service pool memory percent allocation. You can specify a value between 0 and 100.

The sum of `memory-percent` values across all egress pools must be less than or equal to 100 percent.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-pool 3 memory-percent 20
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> infinite

Configures the egress service pool flag to infinite. You can specify `true` or `false`. The default setting is `false`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-pool 3 infinite true
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> mode

Configures the egress service pool mode. You can specify `static` or `dynamic`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-pool 3 mode dynamic
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> reserved

Configures the egress service pool reserved buffer allocation in bytes. You can specify a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-pool 3 reserved 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> shared-bytes

Configures the egress service pool static shared buffer allocation in bytes. You can specify a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-pool 3 shared-bytes 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> shared-alpha

Configures the egress service pool dynamic shared buffer alpha allocation.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-pool 3 shared-alpha alpha_1_4
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer

Configures the ingress lossy buffer.

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\>

Configures the priority group alias name for the ingress lossy buffer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> switch-priority \<qos-sp-id\>

Configures the switch priority for the ingress lossy buffer priority group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |
| `<qos-sp-id>` |  The switch priority. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 switch-priority 0,1,3,4,5,6,7
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> name \<value\>

Configures an alias name for the ingress lossy buffer priority group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 name SERVERS
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> reserved

Configures the reserved buffer allocation in bytes for the ingress lossy buffer priority group. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 reserved 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> shared-bytes

Configures the static shared buffer allocation in bytes for the ingress lossy buffer priority group. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 shared-bytes  10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> shared-alpha

Configures dynamic shared buffer alpha allocation in bytes for the ingress lossy buffer priority group. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 shared-alpha  10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> service-pool \<integer\>

Configures the service pool for the ingress lossy buffer priority group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 service-pool 2
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossless-buffer

Configures the ingress lossless buffer settings.

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossless-buffer service-pool \<integer\>

Configures the service pool for the ingress lossless buffer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-lossless-buffer service-pool 3
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossless-buffer shared-alpha

Configures the dynamic shared buffer alpha allocation for the ingress lossless buffer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-lossless-buffer shared-alpha alpha_1_8
```

- - -

## nv set qos advance-buffer-config \<profile-id\> ingress-lossless-buffer shared-bytes

Configures the static shared buffer allocation in bytes for the ingress lossless buffer. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global ingress-lossless-buffer shared-bytes 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossless-buffer

Configures egress lossless buffer settings.

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossless-buffer service-pool \<integer\>

Configures the service pool for the egress lossless buffer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer service-pool 3
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossless-buffer reserved

Configures the reserved buffer allocation in bytes for the egress lossless buffer. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer reserved 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossless-buffer shared-alpha

Configures the dynamic shared buffer alpha allocation in bytes for the egress lossless buffer. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer shared-alpha 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossless-buffer shared-bytes

Configures the static shared buffer allocation in bytes for the egress lossless buffer. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer shared-bytes 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer

Configures the egress lossy buffer.

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\>

Configures the traffic classes for the egress lossy buffer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<traffic-class-id>` |   The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer traffic-class 3
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\> reserved

Configures the reserved buffer allocation in bytes for the egress lossy buffer traffic class. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<traffic-class-id>` |   The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer traffic-class 3 reserved 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\> shared-bytes

Configures the static shared buffer allocation in bytes for the egress lossy buffer traffic class. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<traffic-class-id>` |   The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer traffic-class 3 shared-bytes 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\> shared-alpha

Configures the dynamic shared buffer alpha allocation for the egress lossy buffer traffic class.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<traffic-class-id>` |   The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer traffic-class 3 shared-alpha alpha_2
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\> service-pool \<integer\>

Configures the service pool ID for the egress lossy buffer traffic class.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<traffic-class-id>` |   The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer traffic-class 3 service-pool 3
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\>

Configures the multicast switch priority for the egress lossy buffer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-sp-id>` |   The multicast switch priority. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 5,7
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\> reserved 

Configures the reserved buffer allocation in bytes for the egress lossy buffer multicast switch priority. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-sp-id>` |   The multicast switch priority. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 5,7
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\> shared-bytes 

Configures the static shared buffer allocation in bytes for the egress lossy buffer multicast switch priority. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-sp-id>` |   The multicast switch priority. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 5,7 shared-bytes 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\> shared-alpha

Configures the dynamic shared buffer alpha allocation for the egress lossy buffer multicast switch priority.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-sp-id>` |   The multicast switch priority. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 5,7 shared-alpha alpha_2
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\> service-pool \<integer\>

Configures the service pool ID for the egress lossy buffer multicast switch priority.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-sp-id>` |   The multicast switch priority. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 5,7 service-pool 3
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-port

Configures the multicast port for the egress lossy buffer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer multicast-port 
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-port reserved

Configures the reserved multicast port buffer allocation in bytes for the egress lossy buffer. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer reserved 10000
```

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-port shared-bytes

Configures the multicast port static buffer allocation in bytes for the egress lossy buffer. You can set a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer shared-bytes 10000
```

- - -

## nv set qos traffic-pool \<traffic-pool-id\>

Configures the Q0S traffic pool ID.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<traffic-pool-id>` | The traffic pool ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos traffic-pool 3
```

- - -

## nv set qos traffic-pool \<traffic-pool-id\> switch-priority \<qos-sp-id\>

Configures the QoS switch priority for the specified traffic pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<traffic-pool-id>` | The traffic pool ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos traffic-pool 3
```

- - -

## nv set qos traffic-pool \<traffic-pool-id\> memory-percent

Configures the percent of memory allocated to the specified traffic pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<traffic-pool-id>` | The traffic pool ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos traffic-pool 3 memory percent 80
```

- - -

## nv set qos link-pause \<profile-id\>

Configures QoS link pause; an older congestion control mechanism that causes all traffic on a link between two switches, or between a host and switch, to stop transmitting during times of congestion. Pause frames start and stop depending on buffer congestion. You configure pause frames on a per-direction, per-interface basis. You can receive pause frames to stop the switch from transmitting when requested, send pause frames to request neighboring devices to stop transmitting, or both.

{{%notice note%}}
Before configuring pause frames, you must first modify the switch buffer allocation.
{{%/notice%}}

- - -

## nv set qos link-pause \<profile-id\> xoff-threshold \<value\>

Configures the frame transmission stop threshold in bytes for the specified link pause profile.

NVIDIA recommends that you do not change this setting but, instead, let Cumulus Linux configure the settings dynamically. Only change the threshold setting if you are an advanced user who understands the buffer configuration requirements for lossless traffic to work seamlessly.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos link-pause my_pause_ports xoff-threshold 1000
```

- - -

## nv set qos link-pause \<profile-id\> xon-threshold \<value\>

Configures the frame transmission start threshold in bytes for the specified link pause profile.

NVIDIA recommends that you do not change these settings but, instead, let Cumulus Linux configure the settings dynamically. Only change the threshold this setting if you are an advanced user who understands the buffer configuration requirements for lossless traffic to work seamlessly.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos link-pause my_pause_ports xon-threshold 1000
```

- - -

## nv set qos link-pause \<profile-id\> port-buffer \<value\>

Configures the port buffer allocation in bytes for the specified link pause profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos link-pause my_pause_ports port-buffer 20000
```

- - -

## nv set qos link-pause \<profile-id\> cable-length

Configures the cable length in meters for the specified link pause profile. You can specify a value between 1 and 100000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos link-pause my_pause_ports cable-length 50
```

- - -

## nv set qos link-pause \<profile-id\> tx

Turns sending pause frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos link-pause my_pause_ports tx enable
```

- - -

## nv set qos link-pause \<profile-id\> rx

Turns receiving pause frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos link-pause my_pause_ports rx disable
```

- - -

## nv set qos pfc \<profile-id\>

Configures Priority flow control (PFC) settings. PFC extends the capabilities of pause frames by the frames for a specific 802.1p value instead of stopping all traffic on a link. If a switch supports PFC and receives a PFC pause frame for a given 802.1p value, the switch stops transmitting frames from that queue, but continues transmitting frames for other queues.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global
```

- - -

## nv set qos pfc \<profile-id\> switch-priority \<qos-sp-id\>

Configures the switch priority for the specified PFC profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global switch-priority 0
```

- - -

## nv set qos pfc \<profile-id\> xoff-threshold \<value\>

Configures the frame transmission stop threshold in bytes for the specified PFC profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global xoff-threshold 1000
```

- - -

## nv set qos pfc \<profile-id\> xon-threshold \<value\>

Configures the frame transmission start threshold in bytes for the specified PFC profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global xon-threshold 10000
```

- - -

## nv set qos pfc \<profile-id\> port-buffer \<value\>

Configures the port buffer allocation in bytes for the specified PFC profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global port-buffer 20000
```

- - -

## nv set qos pfc \<profile-id\> cable-length

Configures the cable length in meters for the specified PFC profile. You can specify a value between 1 and 100000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global cable-length 50
```

- - -

## nv set qos pfc \<profile-id\> tx

Turns sending PFC frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global tx enable
```

- - -

## nv set qos pfc \<profile-id\> rx

Turns receiving PFC frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global rx enable
```

- - -

## nv set qos mapping \<profile-id\>

- - -

## nv set qos mapping \<profile-id\> pcp \<qos-pcp-id\>


- - -

## nv set qos mapping \<profile-id\> pcp \<qos-pcp-id\> switch-priority

0-7

- - -

## nv set qos mapping \<profile-id\> dscp \<qos-dscp-id\>

- - -

## nv set qos mapping \<profile-id\> dscp \<qos-dscp-id\> switch-priority

0-7

- - -

## nv set qos mapping \<profile-id\> port-default-sp

0-7

- - -

## nv set qos mapping \<profile-id\> trust 

(l2|l3|port|both)

- - -

## nv set qos remark \<profile-id\>

Configures 802.1p or DSCP traffic marking.

- - -

## nv set qos remark \<profile-id\> switch-priority \<qos-sp-id\>

Configures switch priority to 802.1p or DSCP traffic marking.

- - -

## nv set qos remark \<profile-id\> switch-priority \<qos-sp-id\> pcp

Configures switch priority to egress 802.1p (PCP) mapping for the specified remark profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos remark default-global switch-priority 0 pcp 4
```

- - -

## nv set qos remark \<profile-id\> switch-priority \<qos-sp-id\> dscp

Configures switch priority to egress DSCP mapping for the specified remark profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos remark default-global switch-priority 0 dscp 22 
```

- - -

## nv set qos remark \<profile-id\> rewrite

(l2|l3|both)

- - -

## nv set qos congestion-control \<profile-id\>

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\>

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> min-threshold \<value\>

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> max-threshold \<value\>

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> probability

0-100

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> red

(enable|disable)

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> ecn

(enable|disable)

- - -

## nv set qos egress-queue-mapping \<profile-id\>

- - -

## nv set qos egress-queue-mapping \<profile-id\> switch-priority \<qos-sp-id\>

- - -

## nv set qos egress-queue-mapping \<profile-id\> switch-priority \<qos-sp-id\> traffic-class

0-7

- - -

## nv set qos egress-scheduler \<profile-id\>

- - -

## nv set qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\>

- - -

## nv set qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\> mode

(dwrr|strict)

- - -

## nv set qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\> bw-percent

0-100

- - -

## nv set qos egress-shaper \<profile-id\>

- - -

## nv set qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\>

- - -

## nv set qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\> min-rate

0-2147483647

- - -

## nv set qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\> max-rate

0-2147483647

- - -

## nv set qos egress-shaper \<profile-id\> port-max-rate

0-2147483647

- - -

## nv set qos roce

Configures RDMA over Converged Ethernet lossless (RoCE).

- - -

## nv set qos roce enable

Turns QoS ROCE on or off on the switch. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos roce enable off
```

- - -

## nv set qos roce mode

Configures the Roce mode. You can specify `lossy` or `lossless`. The default setting is `lossless`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos roce mode lossy
```

- - -

## nv set qos roce cable-length

Configures the cable length for Roce lossless. You can specify a value between 1 and 100000. The default setting is 100 meters.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos roce cable-length 1000
```

- - -
