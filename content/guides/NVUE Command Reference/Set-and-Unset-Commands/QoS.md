---
title: QoS
author: Cumulus Networks
weight: 690
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set interface \<interface-id\> qos

Configures QoS on the specified interface.

- - -

## nv set interface \<interface-id\> qos congestion-control

Configures QoS congestion control on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos congestion-control
```

- - -

## nv set interface \<interface-id\> qos congestion-control profile \<profile-name\>

Configures the QoS congestion control profile on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<profile-name>` | The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos congestion-control profile MYPROFILE
```

- - -

## nv set interface \<interface-id\> qos egress-scheduler

Configures QoS egress scheduling on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<profile-name>` | The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos egress-scheduler
```

- - -

## nv set interface \<interface-id\> qos egress-scheduler profile \<profile-name\>

Configures the QoS egress scheduler profile on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<profile-name>` | The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos egress-scheduler profile MYPROFILE
```

- - -

## nv set interface \<interface-id\> qos egress-shaper

Configures QoS egress shapeing on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<profile-name>` | The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos egress-shaper
```

- - -

## nv set interface \<interface-id\> qos egress-shaper profile \<profile-name\>

Configures the QoS egress scheduler profile on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<profile-name>` | The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos egress-shaper profile MYPROFILE
```

- - -

## nv set interface \<interface-id\> qos link-pause

Configures QoS link pause on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos link-pause
```

- - -

## nv set interface \<interface-id\> qos link-pause profile \<profile-name\>

Configures the QoS link pause profile on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<profile-name>` | The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos link-pause profile
```

- - -

## nv set interface \<interface-id\> qos mapping

Configures QoS mapping on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos mapping
```

- - -

## nv set interface \<interface-id\> qos mapping profile \<profile-name\>

Configures the QoS mapping profile on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<profile-name>` | The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos mapping profile MYPROFILE
```

- - -

## nv set interface \<interface-id\> qos pfc

Configures QoS PFC on the specifies interface.

- - -

## nv set interface \<interface-id\> qos pfc profile \<profile-name\>

Configures the QoS PFC profile on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<profile-name>` | The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos pfc profile
```

- - -

## nv set interface \<interface-id\> qos remark

Configures QoS remarking on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos remark
```

- - -

## nv set interface \<interface-id\> qos remark profile \<profile-name\>

Configures the QoS mapping profile on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<profile-name>` | The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 qos remark profile MYPROFILE
```

- - -

## nv set qos

Configures global Quality of Service (QOS) settings.

- - -

## nv set qos advance-buffer-config \<profile-id\>

Configures the QoS advanced buffer profile settings. Advanced buffer configuration can override the base traffic-pool profiles configured on the system.

- - -

## nv set qos advance-buffer-config \<profile-id\> egress-lossless-buffer

Configures egress lossless buffer settings.

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

## nv set qos congestion-control \<profile-id\>

Configures Explicit Congestion Notification (ECN); an end-to-end flow control technology. Instead of telling adjacent devices to stop transmitting during times of buffer congestion, ECN sets the ECN bits of the transit IPv4 or IPv6 header to indicate to end hosts that congestion might occur. As a result, the sending hosts reduce their sending rate until the transit switch no longer sets ECN bits.

ECN operates by having a transit switch that marks packets between two end hosts.

You use ECN with RDMA over Converged Ethernet - RoCE.

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\>

Configures traffic class settings for the specified ECN profile.

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> ecn

Turns ECN bit marking on or off for the traffic class in the specified ECN profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos congestion-control default-global traffic-class 4,5,7 ecn enable
```

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> max-threshold \<value\>

Configures the maximum buffer threshold in bytes. Cumulus Linux marks all ECN-capable packets when buffer congestion crosses this threshold.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos congestion-control default-global traffic-class 4,5,7 max-threshold 200000 
```

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> min-threshold \<value\>

Configures the minimum buffer threshold in bytes. Random ECN marking starts when buffer congestion crosses this threshold. The probability determines if ECN marking occurs.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos congestion-control default-global traffic-class 4,5,7 min-threshold 40000 
```

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> probability

Configures the probability that Cumulus Linux marks an ECN-capable packet when buffer congestion is between the minimum threshold and the maximum threshold. You can set a value between 1 and 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos congestion-control default-global traffic-class 4,5,7 probability 80 
```

- - -

## nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> red

Turns Random Early Detection (RED) on or off.

ECN prevents packet drops in the network due to congestion by signaling hosts to transmit less. However, if congestion continues after ECN marking, packets drop after the switch buffer is full. By default, Cumulus Linux tail-drops packets when the buffer is full. You can enable RED to drop packets that are in the queue randomly instead of always dropping the last arriving packet. This might improve overall performance of TCP based flows.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos congestion-control default-global traffic-class 4,5,7 red enable
```

- - -

## nv set qos egress-queue-mapping \<profile-id\>

Configures egress queues. Cumulus Linux supports eight egress queues to provide different classes of service. By default switch priority values map directly to the matching egress queue. For example, switch priority value 0 maps to egress queue 0.

You can remap queues by changing the switch priority value to the corresponding queue value. You can map multiple switch priority values to a single egress queue.

- - -

## nv set qos egress-queue-mapping \<profile-id\> switch-priority \<qos-sp-id\>

Configures the switch priority for the egress queue profile.

- - -

## nv set qos egress-queue-mapping \<profile-id\> switch-priority \<qos-sp-id\> traffic-class

Configures the switch priority to egress queue mapping.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-sp-id>` |   The switch priority. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos egress-queue-mapping default-global switch-priority 2 traffic-class 7
```

- - -

## nv set qos egress-scheduler \<profile-id\>

Configures the egress scheduler. Cumulus Linux supports 802.1Qaz, Enhanced Transmission Selection, which allows the switch to assign bandwidth to egress queues and then schedule the transmission of traffic from each queue. 802.1Qaz supports Priority Queuing.

Cumulus Linux provides a default egress scheduler that applies to all ports, where the bandwidth allocated to egress queues 0,2,4,6 is 12 percent and the bandwidth allocated to egress queues 1,3,5,7 is 13 percent.

- - -

## nv set qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\>

Configures the traffic class for the specified egress scheduler profile. The traffic class defines the egress queue where you want to assign bandwidth. For example, traffic-class 2 defines the bandwidth allocation for egress queue 2.

- - -

## nv set qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\> bw-percent

Configures the bandwidth percent value between 1 and 100 for the specified egress queue. If you do not specify a value for an egress queue, Cumulus Linux uses a DWRR value of 0 (no egress scheduling). The combined total of values you assign must be less than or equal to 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The egress queue. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos egress-scheduler default-global traffic-class 2,6 bw-percent 30
```

- - -

## nv set qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\> mode

Configures the traffic class mode (`dwrr` or `strict`) for the specified egress scheduler profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The egress queue. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos egress-scheduler default-global traffic-class 2,6 mode dwrr 
```

- - -

## nv set qos egress-shaper \<profile-id\>

Configures traffic shaping, which allows a switch to send traffic at an average bitrate lower than the physical interface. Traffic shaping prevents a receiving device from dropping bursty traffic if the device is either not capable of that rate of traffic or has a policer that limits what it accepts.

Traffic shaping works by holding packets in the buffer and releasing them at specific time intervals.

- - -

## nv set qos egress-shaper \<profile-id\> port-max-rate

Configures the maximum packet shaper rate for the specified profile. You can set a value between 0 and 2147483647.

- - -

## nv set qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\>

Configures the traffic class (egress queue) for the specified traffic shaper profile.

- - -

## nv set qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\> max-rate

Configures the maximum bandwidth for the specified egress queue for a traffic shaper profile. You can set a value between 0 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The egress queue. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos egress-shaper shaper1 traffic-class 2 max-rate 500
```

- - -

## nv set qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\> min-rate

Configures the minimum bandwidth for the specified egress queue for a traffic shaper profile. You can set a value between 0 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The egress queue. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos egress-shaper shaper1 traffic-class 2 min-rate 100
```

- - -

## nv set qos link-pause \<profile-id\>

Configures QoS link pause; an older congestion control mechanism that causes all traffic on a link between two switches, or between a host and switch, to stop transmitting during times of congestion. Pause frames start and stop depending on buffer congestion. You configure pause frames on a per-direction, per-interface basis. You can receive pause frames to stop the switch from transmitting when requested, send pause frames to request neighboring devices to stop transmitting, or both.

{{%notice note%}}
Before configuring pause frames, you must first modify the switch buffer allocation.
{{%/notice%}}

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

## nv set qos link-pause \<profile-id\> rx

Turns receiving pause frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos link-pause my_pause_ports rx disable
```

- - -

## nv set qos link-pause \<profile-id\> tx

Turns sending pause frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos link-pause my_pause_ports tx enable
```

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

## nv set qos mapping \<profile-id\>

Configures trust 802.1p and DSCP marking.

When a frame or packet arrives on the switch, Cumulus Linux maps it to an internal COS (switch priority) value. This value never writes to the frame or packet but classifies and schedules traffic internally through the switch.

You can define which values are trusted: 802.1p, DSCP, or both.

- - -

## nv set qos mapping \<profile-id\> dscp \<qos-dscp-id\>

Configures trust DSCP marking.

- - -

## nv set qos mapping \<profile-id\> dscp \<qos-dscp-id\> switch-priority

Configures the DSCP to switch priority mapping.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-dscp-id>` |   The DSCP value. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos mapping default-global dscp 10,21,36 switch-priority 0 
```

- - -

## nv set qos mapping \<profile-id\> pcp \<qos-pcp-id\>

Configures trust 802.1p marking.

- - -

## nv set qos mapping \<profile-id\> pcp \<qos-pcp-id\> switch-priority

Configures the 802.1p to switch priority mapping.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-pcp-id>` |   The 802.1p value. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos mapping default-global pcp 0 switch-priority 4 
```

- - -

## nv set qos mapping \<profile-id\> port-default-sp

Assigns all traffic to a specific switch priority regardless of the ingress marking.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos mapping default-global port-default-sp 3
```

- - -

## nv set qos mapping \<profile-id\> trust

Configures the port trust. You can specify `l2`, `l3`, `port`, or `both`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos mapping default-global trust l3 
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

## nv set qos pfc \<profile-id\> cable-length

Configures the cable length in meters for the specified PFC profile. You can specify a value between 1 and 100000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global cable-length 50
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

## nv set qos pfc \<profile-id\> rx

Turns receiving PFC frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global rx enable
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

## nv set qos pfc \<profile-id\> tx

Turns sending PFC frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos pfc default-global tx enable
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

## nv set qos remark \<profile-id\>

Configures 802.1p or DSCP traffic marking.

- - -

## nv set qos remark \<profile-id\> rewrite

You can specify `l2`, `l3`, or `both`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos remark default-global rewrite
```

- - -

## nv set qos remark \<profile-id\> switch-priority \<qos-sp-id\>

Configures switch priority to 802.1p or DSCP traffic marking.

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

## nv set qos roce

Configures RDMA over Converged Ethernet lossless (RoCE).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos egress-shaper shaper1 port-max-rate 200000
```

- - -

## nv set qos roce cable-length

Configures the cable length for RoCE lossless. You can specify a value between 1 and 100000. The default setting is 100 meters.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos roce cable-length 1000
```

- - -

## nv set qos roce enable

Turns QoS RoCE on or off on the switch. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos roce enable off
```

- - -

# nv set qos roce mode

Configures the RoCE mode. You can specify `lossy` or `lossless`. The default setting is `lossless`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos roce mode lossy
```

- - -

## nv set qos traffic-pool \<traffic-pool-id\>

Configures the Q0S traffic pool ID.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<traffic-pool-id>` | The traffic pool ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

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

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos traffic-pool 3 memory percent 80
```

- - -

## nv set qos traffic-pool \<traffic-pool-id\> switch-priority \<qos-sp-id\>

Configures the QoS switch priority for the specified traffic pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<traffic-pool-id>` | The traffic pool ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos traffic-pool 3
```

- - -
