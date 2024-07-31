---
title: QoS
author: Cumulus Networks
weight: 690

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set interface \<interface-id\> qos congestion-control profile \<profile-name\></h>

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
cumulus@switch:~$ nv set interface swp1 qos congestion-control profile MYPROFILE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> qos egress-scheduler profile \<profile-name\></h>

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
cumulus@switch:~$ nv set interface swp1 qos egress-scheduler profile MYPROFILE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> qos egress-shaper profile \<profile-name\></h>

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
cumulus@switch:~$ nv set interface swp1 qos egress-shaper profile MYPROFILE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> qos link-pause profile \<profile-name\></h>

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
cumulus@switch:~$ nv set interface swp1 qos link-pause profile MYPROFILE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> qos mapping profile \<profile-name\></h>

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
cumulus@switch:~$ nv set interface swp1 qos mapping profile MYPROFILE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> qos pfc profile \<profile-name\></h>

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
cumulus@switch:~$ nv set interface swp1 qos pfc profile MYPROFILE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> qos remark profile \<profile-name\></h>

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
cumulus@switch:~$ nv set interface swp1 qos remark profile MYPROFILE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> qos pfc-watchdog state</h>

Enables or disables PFC watchdog on the interface. PFC watchdog detects and mitigates pause storms on ports where PFC or link pause is ON. The default setting is `disable`.

- PFC watchdog only works for lossless traffic queues.
- You can only configure PFC watchdog on a port with PFC (or link pause) configuration.
- You can only enable PFC watchdog on a physical interface (swp).
- You cannot enable the watchdog on a bond (for example, bond0) but you can enable the watchdog on a port that is a member of a bond (for example, swp1).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set interface swp1 qos qos pfc-watchdog state enable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossless-buffer reserved</h>

Configures the reserved buffer allocation in bytes for the egress lossless buffer. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer reserved 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossless-buffer service-pool \<integer\></h>

Configures the service pool for the egress lossless buffer.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer service-pool 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossless-buffer shared-alpha</h>

Configures the dynamic shared buffer alpha allocation for the egress lossless buffer. You can set enum data types such as `alpha_1`, `alpha_2`, and so on.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer shared-alpha alpha_1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossless-buffer shared-bytes</h>

Configures the static shared buffer allocation in bytes for the egress lossless buffer. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer shared-bytes 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-port reserved</h>

Configures the reserved multicast port buffer allocation in bytes for the egress lossy buffer. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer reserved 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-port shared-bytes</h>

Configures the multicast port static buffer allocation in bytes for the egress lossy buffer. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossless-buffer shared-bytes 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\> reserved</h>

Configures the reserved buffer allocation in bytes for the egress lossy buffer multicast switch priority. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-sp-id>` |   The multicast switch priority. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 5,7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\> service-pool \<integer\></h>

Configures the service pool ID for the egress lossy buffer multicast switch priority.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-sp-id>` |   The multicast switch priority. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 5,7 service-pool 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\> shared-alpha</h>

Configures the dynamic shared buffer alpha allocation for the egress lossy buffer multicast switch priority.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-sp-id>` |   The multicast switch priority. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 5,7 shared-alpha alpha_2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer multicast-switch-priority \<qos-sp-id\> shared-bytes</h>

Configures the static shared buffer allocation in bytes for the egress lossy buffer multicast switch priority. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-sp-id>` |   The multicast switch priority. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer multicast-switch-priority 5,7 shared-bytes 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\> reserved</h>

Configures the reserved buffer allocation in bytes for the egress lossy buffer traffic class. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<traffic-class-id>` |   The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer traffic-class 3 reserved 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\> service-pool \<integer\></h>

Configures the service pool ID for the egress lossy buffer traffic class.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<traffic-class-id>` |   The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer traffic-class 3 service-pool 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\> shared-alpha</h>

Configures the dynamic shared buffer alpha allocation for the egress lossy buffer traffic class.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<traffic-class-id>` |   The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer traffic-class 3 shared-alpha alpha_2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-lossy-buffer traffic-class \<traffic-class-id\> shared-bytes</h>

Configures the static shared buffer allocation in bytes for the egress lossy buffer traffic class. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<traffic-class-id>` |   The traffic class ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-lossy-buffer traffic-class 3 shared-bytes 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> infinite</h>

Configures the egress service pool flag to infinite. You can specify `true` or `false`. The default setting is `false`.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-pool 3 infinite true
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> memory-percent</h>

Configures the egress service pool memory percent allocation. You can specify a value between 0 and 100. The sum of `memory-percent` values across all egress pools must be less than or equal to 100 percent.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-pool 3 memory-percent 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> mode</h>

Configures the egress service pool mode. You can specify `static` or `dynamic`.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-pool 3 mode dynamic
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> reserved</h>

Configures the egress service pool reserved buffer allocation in bytes. You can specify a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-pool 3 reserved 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> shared-alpha</h>

Configures the egress service pool dynamic shared buffer alpha allocation.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-pool 3 shared-alpha alpha_1_4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-pool \<pool-id\> shared-bytes</h>

Configures the egress service pool static shared buffer allocation in bytes. You can specify a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-pool 3 shared-bytes 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-lossless-buffer service-pool \<integer\></h>

Configures the service pool for the ingress lossless buffer.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-lossless-buffer service-pool 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-lossless-buffer shared-alpha</h>

Configures the dynamic shared buffer alpha allocation for the ingress lossless buffer.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-lossless-buffer shared-alpha alpha_1_8
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-lossless-buffer shared-bytes</h>

Configures the static shared buffer allocation in bytes for the ingress lossless buffer. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-lossless-buffer shared-bytes 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> name \<value\></h>

Configures an alias name for the ingress lossy buffer priority group.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 name SERVERS
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> reserved</h>

Configures the reserved buffer allocation in bytes for the ingress lossy buffer priority group. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 reserved 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> service-pool \<integer\></h>

Configures the service pool for the ingress lossy buffer priority group.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 service-pool 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> shared-alpha</h>

Configures dynamic shared buffer alpha allocation in bytes for the ingress lossy buffer priority group.  You can set enum data types such as `alpha_1`, `alpha_2`, and so on.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 shared-alpha alpha_1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> shared-bytes</h>

Configures the static shared buffer allocation in bytes for the ingress lossy buffer priority group. You can set a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 shared-bytes  10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-lossy-buffer priority-group \<priority-group-id\> switch-priority \<qos-sp-id\></h>

Configures the switch priority for the ingress lossy buffer priority group.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

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
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 switch-priority 0,1,3,4,5,6,7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> infinite</h>

Configures the ingress service pool flag to infinite. You can specify `true` or `false`. The default setting is `false`.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-pool 3 infinite true
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> memory-percent</h>

Configures the ingress service pool memory percent allocation. You can specify a value between 0 and 100. The sum of `memory-percent` values across all ingress pools must be less than or equal to 100 percent.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-pool 3 memory-percent 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> mode</h>

Configures the ingress service pool mode. You can specify `static` or `dynamic`.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-pool 3 mode dynamic
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> reserved</h>

Configures the ingress service pool reserved buffer allocation in bytes. You can specify a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-pool 3 reserved 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> shared-alpha</h>

Configures the ingress service pool dynamic shared buffer alpha allocation.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-pool 3 shared-alpha alpha_1_4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-pool \<pool-id\> shared-bytes</h>

Configures the ingress service pool static shared buffer allocation in bytes. You can specify a value between 0 and 4294967295.

{{%notice note%}}
Only modify this command setting if you are an advanced user.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<pool-id>` |   The pool name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-pool 3 shared-bytes 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group \<priority-group\> headroom</h>

Configures the lossy headroom for a specified priority group. Lossy headroom is the buffer on top of the reserved buffer that stores packets that ingress the switch. You can configure the lossy headroom to help analyze performance for a specific priority group.

The switch calculates the default value internally based on the MTU and internal latency.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<priority-group-id>` |  The priority group alias name. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service1 headroom 50000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-mgmt-buffer reserved</h>

Configures the egress management reserved buffer allocation in bytes.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-mgmt-buffer reserved 30000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-mgmt-buffer service-pool</h>

Configures the QoS egress management buffer service pool mapping. You can specify a value between 0 and 7.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-mgmt-buffer service-pool 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-mgmt-buffer shared-alpha</h>

Configures the dynamic egress management shared buffer alpha allocation. You can specify one of these values: `alpha_0`, `alpha_1_128`, `alpha_1_64`, `alpha_1_32`, `alpha_1_16`, `alpha_1_8`, `alpha_1_4`, `alpha_1_2`, `alpha_1`, `alpha_2`, `alpha_4`, `alpha_8`, `alpha_16`, `alpha_32`, `alpha_64`, or `alpha_infinity`.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-mgmt-buffer shared-alpha alpha_2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> egress-mgmt-buffer shared-bytes</h>

Configures the QoS static egress management shared buffer allocation in bytes.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global egress-mgmt-buffer shared-bytes 14000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-mgmt-buffer headroom</h>

Configures the QoS ingress management buffer headroom in bytes.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-mgmt-buffer headroom 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-mgmt-buffer service-pool</h>

Configures the QoS ingress management buffer service pool mapping. You can specify a value between 0 and 7.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-mgmt-buffer service-pool 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-mgmt-buffer shared-alpha</h>

Configures the QoS dynamic ingress management shared buffer alpha allocation. You can specify one of these values: `alpha_0`, `alpha_1_128`, `alpha_1_64`, `alpha_1_32`, `alpha_1_16`, `alpha_1_8`, `alpha_1_4`, `alpha_1_2`, `alpha_1`, `alpha_2`, `alpha_4`, `alpha_8`, `alpha_16`, `alpha_32`, `alpha_64`, or `alpha_infinity`.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-mgmt-buffer shared-alpha alpha_2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos advance-buffer-config \<profile-id\> ingress-mgmt-buffer shared-bytes</h>

Configures the static ingress management shared buffer allocation in bytes.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set qos advance-buffer-config default-global ingress-mgmt-buffer shared-bytes 14000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos congestion-control \<profile-id\></h>

Configures <span class="a-tooltip">[ECN](## "Explicit Congestion Notification")</span>; an end-to-end flow control technology. Instead of telling adjacent devices to stop transmitting during times of buffer congestion, ECN sets the ECN bits of the transit IPv4 or IPv6 header to indicate to end hosts that congestion might occur. As a result, the sending hosts reduce their sending rate until the transit switch no longer sets ECN bits.

ECN operates by having a transit switch that marks packets between two end hosts. You use ECN with RDMA over Converged Ethernet (RoCE).

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> ecn</h>

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
cumulus@switch:~$ nv set qos congestion-control default-global traffic-class 4,5,7 ecn enable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> max-threshold \<value\></h>

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
cumulus@switch:~$ nv set qos congestion-control default-global traffic-class 4,5,7 max-threshold 200000 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> min-threshold \<value\></h>

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
cumulus@switch:~$ nv set qos congestion-control default-global traffic-class 4,5,7 min-threshold 40000 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> probability</h>

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
cumulus@switch:~$ nv set qos congestion-control default-global traffic-class 4,5,7 probability 80 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos congestion-control \<profile-id\> traffic-class \<qos-tc-id\> red</h>

Turns <span class="a-tooltip">[RED](## "Random Early Detection")</span> on or off. 

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
cumulus@switch:~$ nv set qos congestion-control default-global traffic-class 4,5,7 red enable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-queue-mapping \<profile-id\></h>

Configures egress queues. Cumulus Linux supports eight egress queues to provide different classes of service. By default switch priority values map directly to the matching egress queue. For example, switch priority value 0 maps to egress queue 0.

You can remap queues by changing the switch priority value to the corresponding queue value. You can map multiple switch priority values to a single egress queue.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-queue-mapping \<profile-id\> switch-priority \<qos-sp-id\></h>

Configures the switch priority for the egress queue profile.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-queue-mapping \<profile-id\> switch-priority \<qos-sp-id\> traffic-class</h>

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
cumulus@switch:~$ nv set qos egress-queue-mapping default-global switch-priority 2 traffic-class 7
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-scheduler \<profile-id\></h>

Configures the egress scheduler. Cumulus Linux supports 802.1Qaz, Enhanced Transmission Selection, which allows the switch to assign bandwidth to egress queues and then schedule the transmission of traffic from each queue. 802.1Qaz supports Priority Queuing.

Cumulus Linux provides a default egress scheduler that applies to all ports, where the bandwidth allocated to egress queues 0,2,4,6 is 12 percent and the bandwidth allocated to egress queues 1,3,5,7 is 13 percent.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\></h>

Configures the traffic class for the specified egress scheduler profile. The traffic class defines the egress queue where you want to assign bandwidth. For example, traffic-class 2 defines the bandwidth allocation for egress queue 2.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\> bw-percent</h>

Configures the bandwidth percent value between 1 and 100 for the specified egress queue. If you do not specify a value for an egress queue, Cumulus Linux uses a DWRR value of 0 (no egress scheduling). The combined total of values you assign must be less than or equal to 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 2,6 bw-percent 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-scheduler \<profile-id\> traffic-class \<qos-tc-id\> mode</h>

Configures the traffic class mode (`dwrr` or `strict`) for the specified egress scheduler profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 2,6 mode dwrr 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-shaper \<profile-id\></h>

Configures traffic shaping, which allows a switch to send traffic at an average bitrate lower than the physical interface. Traffic shaping prevents a receiving device from dropping bursty traffic if the device is either not capable of that rate of traffic or has a policer that limits what it accepts.

Traffic shaping works by holding packets in the buffer and releasing them at specific time intervals.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-shaper \<profile-id\> port-max-rate</h>

Configures the maximum packet shaper rate for the specified profile. You can set a value between 0 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos egress-shaper shaper1 port-max-rate 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\></h>

Configures the traffic class (egress queue) for the specified traffic shaper profile.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\> max-rate</h>

Configures the maximum bandwidth for the specified egress queue for a traffic shaper profile. You can set a value between 0 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos egress-shaper shaper1 traffic-class 2 max-rate 500
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos egress-shaper \<profile-id\> traffic-class \<qos-tc-id\> min-rate</h>

Configures the minimum bandwidth for the specified egress queue for a traffic shaper profile. You can set a value between 0 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |
| `<qos-tc-id>` |   The traffic class (egress queue). |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos egress-shaper shaper1 traffic-class 2 min-rate 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos link-pause \<profile-id\></h>

Configures QoS link pause; an older congestion control mechanism that causes all traffic on a link between two switches, or between a host and switch, to stop transmitting during times of congestion. Pause frames start and stop depending on buffer congestion. You configure pause frames on a per-direction, per-interface basis. You can receive pause frames to stop the switch from transmitting when requested, send pause frames to request neighboring devices to stop transmitting, or both.

{{%notice note%}}
Before configuring pause frames, you must first modify the switch buffer allocation.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos link-pause \<profile-id\> cable-length</h>

Configures the cable length in meters for the specified link pause profile. You can specify a value between 1 and 100000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos link-pause my_pause_ports cable-length 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos link-pause \<profile-id\> port-buffer \<value\></h>

Configures the port buffer allocation in bytes for the specified link pause profile.

{{%notice note%}}
- The headroom equals the `port-buffer` setting plus the `xoff-threshold` setting.
- NVIDIA recommends you do **not** manually change this setting but let Cumulus Linux configure the setting dynamically.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos link-pause my_pause_ports port-buffer 20000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos link-pause \<profile-id\> rx</h>

Turns receiving pause frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos link-pause my_pause_ports rx disable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos link-pause \<profile-id\> tx</h>

Turns sending pause frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos link-pause my_pause_ports tx enable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos link-pause \<profile-id\> xoff-threshold \<value\></h>

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
cumulus@switch:~$ nv set qos link-pause my_pause_ports xoff-threshold 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos link-pause \<profile-id\> xon-threshold \<value\></h>

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
cumulus@switch:~$ nv set qos link-pause my_pause_ports xon-threshold 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos mapping \<profile-id\></h>

Configures trust 802.1p and DSCP marking.

When a frame or packet arrives on the switch, Cumulus Linux maps it to an internal COS (switch priority) value. This value never writes to the frame or packet but classifies and schedules traffic internally through the switch.

You can define the trusted values: 802.1p, DSCP, or both.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos mapping \<profile-id\> dscp \<qos-dscp-id\></h>

Configures trust DSCP marking.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos mapping \<profile-id\> dscp \<qos-dscp-id\> switch-priority</h>

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
cumulus@switch:~$ nv set qos mapping default-global dscp 10,21,36 switch-priority 0 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos mapping \<profile-id\> pcp \<qos-pcp-id\></h>

Configures trust 802.1p marking.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos mapping \<profile-id\> pcp \<qos-pcp-id\> switch-priority</h>

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
cumulus@switch:~$ nv set qos mapping default-global pcp 0 switch-priority 4 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos mapping \<profile-id\> port-default-sp</h>

Assigns all the traffic to a specific internal switch priority if the trust configuration on the port is set to `port` or according to the fallback mechanism when incoming traffic does not match the port trust setting.

| Trust Setting | VLAN Tagged? | IP or Non-IP | Result |
| ------ | ------ | -------- | -------- |
| Layer 2 | yes | IP | Accept incoming 802.1p marking. |
| Layer 2 | yes | non IP | Accept incoming 802.1p marking. |
| Layer 2 | no | IP | Use the default priority setting. |
| Layer 2 | no | non IP | Use the default priority setting. |
| Layer 3 | yes | IP | Accept incoming DSCP IP header marking. |
| Layer 3 | yes | non IP | Use the default priority setting. |
| Layer 3 | no | IP | Accept incoming DSCP IP header marking. |
| Layer 3 | no | non IP | Use the default priority setting. |
| Both | yes | IP | Accept incoming DSCP IP header marking. |
| Both | yes | non IP | Accept incoming 802.1p marking.
| Both | no | IP | Accept incoming DSCP IP header marking. |
| Both | no | non IP | Use the default priority setting. |
| Port | either | either | Ignore any existing markings and use the default priority setting. |

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos mapping default-global port-default-sp 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos mapping \<profile-id\> trust</h>

Configures the port trust. You can specify `l2`, `l3`, `port`, or `both`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos mapping default-global trust l3 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos pfc \<profile-id\></h>

Configures Priority flow control (PFC) settings. PFC extends the capabilities of pause frames by the frames for a specific 802.1p value instead of stopping all traffic on a link. If a switch supports PFC and receives a PFC pause frame for a given 802.1p value, the switch stops transmitting frames from that queue, but continues transmitting frames for other queues.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos pfc default-global
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos pfc \<profile-id\> cable-length</h>

Configures the cable length in meters for the specified PFC profile. You can specify a value between 1 and 100000.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv set qos roce cable-length`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos pfc default-global cable-length 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos pfc \<profile-id\> port-buffer \<value\></h>

Configures the port buffer allocation in bytes for the specified PFC profile.

{{%notice note%}}
- The headroom equals the `port-buffer` setting plus the `xoff-threshold` setting.
- NVIDIA recommends you do **not** manually change this setting but let Cumulus Linux configure the setting dynamically.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos pfc default-global port-buffer 20000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos pfc \<profile-id\> rx</h>

Turns receiving PFC frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos pfc default-global rx enable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos pfc \<profile-id\> switch-priority \<qos-sp-id\></h>

Configures the switch priority for the specified PFC profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos pfc default-global switch-priority 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos pfc \<profile-id\> tx</h>

Turns sending PFC frames on and off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos pfc default-global tx enable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos pfc \<profile-id\> xoff-threshold \<value\></h>

Configures the frame transmission stop threshold in bytes for the specified PFC profile.

{{%notice note%}}
NVIDIA recommends you do **not** manually change this setting but let Cumulus Linux configure the setting dynamically.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos pfc default-global xoff-threshold 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos pfc \<profile-id\> xon-threshold \<value\></h>

Configures the frame transmission start threshold in bytes for the specified PFC profile.

{{%notice note%}}
NVIDIA recommends you do **not** manually change this setting but let Cumulus Linux configure the setting dynamically.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos pfc default-global xon-threshold 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos remark \<profile-id\></h>

Configures 802.1p or DSCP traffic marking.

To change the marked value on a packet, the switch ASIC reads the enable or disable rewrite flag on the ingress port and refers to the mapping configuration on the egress port to change the marked value. To remark 802.1p or DSCP values, you have to enable the rewrite on the ingress port and configure the mapping on the egress port.


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos remark \<profile-id\> rewrite</h>

You can specify `l2`, `l3`, or `both`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos remark default-global rewrite
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos remark \<profile-id\> switch-priority \<qos-sp-id\></h>

Configures switch priority to 802.1p or DSCP traffic marking.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos remark \<profile-id\> switch-priority \<qos-sp-id\> dscp</h>

Configures switch priority to egress DSCP mapping for the specified remark profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos remark default-global switch-priority 0 dscp 22 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos remark \<profile-id\> switch-priority \<qos-sp-id\> pcp</h>

Configures switch priority to egress 802.1p (PCP) mapping for the specified remark profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |   The profile name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set qos remark default-global switch-priority 0 pcp 4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos roce</h>

Configures RDMA over Converged Ethernet lossless (RoCE).

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos roce enable</h>

Turns QoS RoCE on or off on the switch. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set qos roce enable off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos roce mode</h>

Configures the RoCE mode. You can specify `lossy` or `lossless`. The default setting is `lossless`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set qos roce mode lossy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos traffic-pool \<traffic-pool-id\> memory-percent</h>

Configures the percent of memory allocated to the specified traffic pool.

Cumulus Linux supports adjusting the following traffic pools:

| Traffic Pool | Description |
| ------------ | ----------- |
| `default-lossy` | The default traffic pool for all switch priorities.|
| `default-lossless` | The traffic pool for lossless traffic when you enable flow control.|
| `mc-lossy` | The traffic pool for multicast traffic.|
| `roce-lossy` | The traffic pool for RoCE lossy mode.|
| `roce-lossless` | The traffic pool for RoCE lossless mode.|

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<traffic-pool-id>` | The traffic pool ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos traffic-pool default-lossy memory percent 80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos traffic-pool \<traffic-pool-id\> switch-priority \<qos-sp-id\></h>

Configures the QoS switch priority for the specified traffic pool.

Cumulus Linux supports adjusting the following traffic pools:

| Traffic Pool | Description |
| ------------ | ----------- |
| `default-lossy` | The default traffic pool for all switch priorities.|
| `default-lossless` | The traffic pool for lossless traffic when you enable flow control.|
| `mc-lossy` | The traffic pool for multicast traffic.|
| `roce-lossy` | The traffic pool for RoCE lossy mode.|
| `roce-lossless` | The traffic pool for RoCE lossless mode.|

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<traffic-pool-id>` | The traffic pool ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set qos traffic-pool default-lossy switch-priority 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos pfc-watchdog polling-interval</h> 

Configures the PFC watchdog polling interval. The default polling interval is 100 milliseconds.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set qos pfc-watchdog polling-interval 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set qos pfc-watchdog robustness</h> 

Configures how many polling intervals the PFC watchdog must wait before it mitigates the storm condition. The default number of polling intervals is 3.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set qos pfc-watchdog robustness 5
```
