---
title: Profile-Based Configuration
author: Cumulus Networks
weight: 667

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system do-spx profile \<profile-id\></h>

Configures the profile role.

Cumulus Linux provides a simplified, profile‑based way to configure a switch that replaces many NVUE commands. You can select an NVIDIA‑predefined profile and provide interface ranges and breakout values. Cumulus Linux generates and applies all immutable configuration, such as link breakouts, ISSU, adaptive routing, telemetry, QoS, and PFC.


{{%notice note%}}
In Cumulus Linux 5.18.0, profile‑based configuration is a Beta feature.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` | The role of the switch: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv action activate system do-spx profile leaf
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system do-spx profile \<profile-id\> uplink \<interface-id\> breakout</h>

Configures the upinks for the profile. The breakout is required. With breakout 4x, parent ports swp1 through swp32 split into sub-interfaces swp1s0 through swp32s3 (128 ports). Breakout 1x keeps ports as-is (swp33 through swp64). All subsequent per-interface commands target the split ports.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |  The role of the switch: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`. |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system do-spx profile leaf uplink swp1-32 breakout 4x 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system do-spx profile \<profile-id\> downlink \<interface-id\> breakout</h>

Configures the downlinks for the profile. The breakout is required. With breakout 4x, parent ports swp1 through swp32 split into sub-interfaces swp1s0 through swp32s3 (128 ports). Breakout 1x keeps ports as-is (swp33 through swp64). All subsequent per-interface commands target the split ports.

Cumulus Linux provides a simplified, profile‑based way to configure a switch that replaces many NVUE commands. You can select an NVIDIA‑predefined profile and provide interface ranges and breakout values. Cumulus Linux generates and applies all immutable configuration, such as link breakouts, ISSU, adaptive routing, telemetry, QoS, and PFC.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |  The role of the switch: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`. |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system do-spx profile leaf downlink swp33-64 breakout 4x
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system do-spx profile \<profile-id\> otlp-destination \<destination-id\></h>

Configures the OTLP export destination for telemetry.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |  The role of the switch: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`. |
| `<destination-id>` |  The OTLP export destination. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system do-spx profile leaf otlp-destination 10.1.1.100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system do-spx profile \<profile-id\> otlp-destination \<destination-id\> otlp-port \<port-id\></h>

Configures the OTLP export destination and port for telemetry.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<profile-id>` |  The role of the switch: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`. |
| `<destination-id>` | The OTLP export destination. |
| `<port-id>` |  The OTLP export destination port. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system do-spx profile leaf otlp-destination 10.1.1.100 otlp-port 4317
```
