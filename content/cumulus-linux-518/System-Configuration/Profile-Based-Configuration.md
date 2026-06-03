---
title: Profile Based Configuration
author: NVIDIA
weight: 299
toc: 3
---
Cumulus Linux provides a simplified, profile‑based way to configure a switch that replaces many NVUE commands. You can select an NVIDIA‑predefined profile such as `leaf` or `spine-2tier` and provide interface ranges and breakout values. Cumulus Linux generates and applies all immutable configuration, such as link breakout, ISSU, traffic class, adaptive routing, telemetry, and optionally, QoS and PFC based on a RoCE QoS profile.

{{%notice note%}}
- Profile‑based switch configuration is supported on Spectrum‑X platforms only (Spectrum-4, Spectrum-5, and Spectrum-6).
- Profile‑based switch configuration supports only the `leaf` and `spine-2tier` profiles in a two tier topology.
- Layer 3 addressing, routing protocols, EVPN, and telemetry OTLP export are not supported.
- Before you use the profile‑based configuration on the switch, you must set up physical connectivity.
- Profile‑based switch configuration does not introduce new authentication or authorization mechanisms. It relies on existing NVUE role-based access control.
- The switch stores profile‑based configuration in the standard NVUE configuration files with the same file permissions and access controls.
{{%/notice%}}

## Set Profile-based Configuration

To use profile‑based configuration on the switch:
- Specify the role: `leaf` or `spine-2tier`.
- Specify the upinks and downlinks on the `leaf` role or the downlinks only on the `spine-2tier` role. Downlink configuration is mandatory for both `leaf` and `spine-2tier` profiles. Uplink configuration is required only for the `leaf` profile.
- Optional: Set the QoS RoCE profile. You can set the profile to `dci-1` (DC‑to‑DC RoCE QoS) or to `lossy-multi-tc` (MRC QoS). If you do not specify a QoS RoCE profile, the switch applies the default intra-DC lossless RoCE QoS profile.

  QoS RoCE mode is a global switch‑level setting. If uplink and downlink specify different QoS profiles, the last applied profile sets the global mode.

The following example sets profile-based configuration on the leaf switch:

```
cumulus@switch:~$ nv set system do-spx role leaf 
cumulus@switch:~$ nv set system do-spx uplink swp1-swp32 breakout x4 
cumulus@switch:~$ nv set system do-spx downlink swp33-swp64 breakout x1 
cumulus@switch:~$ nv config apply 
```

{{%notice note%}}
The breakout is required if you specify an interface-range. With breakout x4, parent ports swp1-32 split into sub-interfaces swp1s0-swp32s3 (128 ports). Breakout x1 keeps ports as-is (swp33-64). All subsequent per-interface commands target the split ports.
{{%/notice%}}

The following example sets profile-based configuration on the spine switch:

```
cumulus@switch:~$ nv set system do-spx role spine-2tier 
cumulus@switch:~$ nv set system do-spx downlink swp1-swp64 breakout x1 
cumulus@switch:~$ nv config apply 
```

The following example sets profile-based configuration on the leaf switch and includes setting the QoS profile to dc1-1:

```
cumulus@switch:~$ nv set system do-spx role leaf 
cumulus@switch:~$ nv set system do-spx uplink swp1-swp32  breakout x4 
cumulus@switch:~$ nv set system do-spx downlink swp33-swp64 breakout x1
cumulus@switch:~$ nv set system do-spx qos profile dci-1 
cumulus@switch:~$ nv config apply 
```

To unset profile-based configuration on a switch, run the `nv unset system do-spx` command:

```
cumulus@switch:~$ nv unset system do-spx 
cumulus@switch:~$ nv config apply 
```

After you run the `nv unset system do-spx` command, breakout remains active so sub-interfaces, IP addresses, BGP peering, and EVPN sessions continue working; Only the Spectrum-X optimizations (adaptive routing, telemetry, QoS, and PFC) are removed.

## Show Profile‑based Configuration

To show the profile‑based configuration on a switch, run the `nv show system do-spx` command:

```
cumulus@switch:~$ nv show system do-spx
role: leaf 
  direction    interface-range    breakout    source 
   ---------    ---------------    --------    -------- 
   uplink       swp33-swp64        x4          explicit 
   downlink     swp1-swp32         x1          explicit 
  qos profile: dci-1 
```

The persistent configuration records only the profile name and the parameters you provide. Other operational NVUE show commands show the fully resolved state.
