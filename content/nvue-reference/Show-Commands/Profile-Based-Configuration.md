---
title: Profile-Based Configuration
author: Cumulus Networks
weight: 293

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system do-spx</h>

Shows the configured profile on the switch.

Cumulus Linux provides a simplified, profile‑based way to configure a switch that replaces many NVUE commands. You can select an NVIDIA‑predefined profile and provide interface ranges and breakout values. Cumulus Linux generates and applies all immutable configuration, such as link breakouts, ISSU, adaptive routing, telemetry, QoS, and PFC.

- Profile‑based switch configuration is supported on Spectrum-4, Spectrum-5, and Spectrum-6.
- Layer 3 addressing, routing protocols, and EVPN are not supported.
- Before you use the profile‑based configuration on the switch, you must set up physical connectivity.
- Profile‑based switch configuration does not introduce new authentication or authorization mechanisms. It relies on existing NVUE role-based access control.
- The switch stores profile‑based configuration in the standard NVUE configuration files with the same file permissions and access controls.
- Profile‑based switch configuration uses the default RoCE lossless mode configuration.

{{%notice note%}}
In Cumulus Linux 5.18.0, profile‑based configuration is a Beta feature.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system do-spx
profile
==========
    UL Brk - Uplink Breakout, DL Brk - Downlink Breakout, OTLP IP - OTLP Dest IP
    (Profile-wide), OTLP Port - OTLP Port (Profile-wide)

    Profile Name  Uplink Interface  UL Brk  Downlink Interface  DL Brk  OTLP IP  OTLP Port
    ------------  ----------------  ------  ------------------  ------  -------  ---------
    leaf          swp1-32           4x      swp33-64            1x                        

active-profile
=================
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv show system do-spx active-profile</h>

Shows the active profile on the switch.

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system do-spx active-profile
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv show system do-spx profile</h>

Shows all configuration profiles on the switch.

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system do-spx profile

UL Brk - Uplink Breakout, DL Brk - Downlink Breakout, OTLP IP - OTLP Dest IP
(Profile-wide), OTLP Port - OTLP Port (Profile-wide)

Profile Name  Uplink Interface  UL Brk  Downlink Interface  DL Brk  OTLP IP     OTLP Port
------------  ----------------  ------  ------------------  ------  ----------  ---------
leaf          swp1-32           4x      swp33-64            4x      10.1.1.100  4317
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv show system do-spx profile \<profile-id\></h>

Shows the switch configuration for the specified profile.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<profile-id>` | The profile ID: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`.|

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system do-spx profile leaf
uplink
=========
    Interface  breakout
    ---------  --------
    swp1-32    4x      

downlink
===========
    Interface  breakout
    ---------  --------
    swp33-64   4x      

otlp-destination
===================
    OTLP Dest IP  OTLP Port
    ------------  ---------
    10.1.1.100    4317
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv show system do-spx profile \<profile-id\> uplink</h>

Shows the upinks configured for the specified profile.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<profile-id>` | The profile ID: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system do-spx profile leaf uplink
Interface  breakout
---------  --------
swp1-32    4x
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv show system do-spx profile \<profile-id\> uplink \<interface-id\></h>

Shows the breakouts configured for the specified profile uplink interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<profile-id>` | The profile ID. |
| `<interface-id>` | The interface ID. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system do-spx profile leaf uplink swp2
          operational  applied  pending
--------  -----------  -------  -------
breakout  4x           4x       4x  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv show system do-spx profile \<profile-id\> downlink</h>

Shows the downlinks configured for the specified profile.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<profile-id>` | The profile ID: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system do-spx profile leaf downlink 
Interface  breakout
---------  --------
swp33-64   4x
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv show system do-spx profile \<profile-id\> downlink \<interface-id\></h>

Shows the breakouts configured for the specified profile downlink interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<profile-id>` | The profile ID: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`. |
| `<interface-id>` | The interface ID. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system do-spx profile leaf downlink swp33
          operational  applied  pending
--------  -----------  -------  -------
breakout  4x           4x       4x
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv show system do-spx profile \<profile-id\> otlp-destination</h>

Shows the OTLP destination configured in the profile.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<profile-id>` | The profile ID: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system do-spx profile leaf otlp-destination 
OTLP Dest IP  OTLP Port
------------  ---------
10.1.1.100    4317
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv show system do-spx profile \<profile-id\> otlp-destination \<destination-id\></h>

Shows the specified OTLP destination configuration.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<profile-id>` | The profile ID: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`. |
| `<destination-id>` | The OTLP destination IP address or hostname. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv show system do-spx profile leaf otlp-destination 10.1.1.100 
           operational  applied  pending
---------  -----------  -------  -------
otlp-port  4317         4317     4317   
```
