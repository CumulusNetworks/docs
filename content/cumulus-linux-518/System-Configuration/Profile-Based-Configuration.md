---
title: Profile Based Configuration
author: NVIDIA
weight: 299
toc: 3
---

{{%notice note%}}
Profile based configuration is a Beta feature.
{{%/notice%}}

Cumulus Linux provides a simplified, profile‑based way to configure a switch that replaces many NVUE commands. You can select an NVIDIA‑predefined profile and provide interface ranges and breakout values. Cumulus Linux generates and applies all immutable configuration, such as link breakouts, ISSU, adaptive routing, telemetry, QoS, and PFC.

{{%notice note%}}
- Profile‑based switch configuration is supported on Spectrum-4 through Spectrum-6.
- Layer 3 addressing, routing protocols, and EVPN are not supported.
- Before you use the profile‑based configuration on the switch, you must set up physical connectivity.
- Profile‑based switch configuration does not introduce new authentication or authorization mechanisms. It relies on existing NVUE role-based access control.
- The switch stores profile‑based configuration in the standard NVUE configuration files with the same file permissions and access controls.
- Profile‑based switch configuration uses the {{<link url="RDMA-over-Converged-Ethernet-RoCE/#default-roce-configuration" text="default RoCE lossless mode configuration">}}.
{{%/notice%}}

## Set Profile-based Configuration

Before you set profile-based configuration, NVIDIA recommends you back up the current configuration on the switch with the `nv config save` command so that you can restore the saved config later, if needed. Refer to {{<link url="NVUE-CLI/#back-up-and-restore-configuration-with-nvue" text="Back Up and Restore Configuration with NVUE">}}.

To set profile‑based configuration on the switch:
- Specify the role of the switch: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`.
- Specify the upinks and, or, downlinks. For the direction rules, refer to the table below. The breakout is required. With breakout 4x, parent ports swp1 through swp32 split into sub-interfaces swp1s0 through swp32s3 (128 ports). Breakout 1x keeps ports as-is (swp33 through swp64). All subsequent per-interface commands target the split ports.
- Optional: For telemetry, set the OTLP export destination.
- Activate the profile. Make sure to activate the profile **after** you set the upinks and and downlinks. Activating the profile applies the AR, resource, telemetry, and QoS configuration.

| Role | Direction rules | Notes |
| ---- | --------------- | ----- |
| `leaf` | Both uplink and downlink required. | Adaptive routing applied on uplinks (spine-facing ports) only. ISSU in half-resource mode.|
| `spine-2` (2-tier) | Downlink only. | Adaptive routing applied on spine downlink. ISSU in full-resource mode.|
| `spine-3` (3-tier) | Both uplink (SSP-facing) and downlink (leaf-facing). | Adaptive routing applied in both directions.  ISSU in full-resource mode. |
| `super-spine` | Downlink only (spine-facing ports). | 3-tier topology only. ISSU in full-resource mode. |

The following example sets profile-based configuration on the leaf and applies the profile. The example also sets the OTLP export destination and port.

```
cumulus@switch:~$ nv set system do-spx profile leaf uplink swp1-32 breakout 4x 
cumulus@switch:~$ nv set system do-spx profile leaf downlink swp33-64 breakout 4x
cumulus@switch:~$ nv set system do-spx profile leaf otlp-destination 10.1.1.100 otlp-port 4317
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv action activate system do-spx profile leaf
cumulus@switch:~$ nv config apply 
Action succeeded
```

{{%notice note%}}
After running the `nv action activate system do-spx profile <profile-id>` command, you must run `nv config apply` to apply the configuration.
{{%/notice%}}

The following example sets profile-based configuration on a two-tier spine and applies the profile:

```
cumulus@switch:~$ nv set system do-spx role spine-2 downlink swp1-64 breakout 4x
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv action activate system do-spx profile spine-2
cumulus@switch:~$ nv config apply
Action succeeded
```

The following example sets profile-based configuration on a three-tier spine and applies the profile:

```
cumulus@switch:~$ nv set system do-spx role spine-3 uplink swp1-32 breakout 4x
cumulus@switch:~$ nv set system do-spx role spine-3 downlink swp33-64 breakout 4x
cumulus@switch:~$ nv config apply 
```

```
cumulus@switch:~$ nv action activate system do-spx profile spine-3
cumulus@switch:~$ nv config apply
Action succeeded
```

The following example sets profile-based configuration on a superspine and applies the profile:

```
cumulus@switch:~$ nv set system do-spx role super-spine downlink swp1-64 breakout 4x
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv action activate system do-spx profile super-spine
cumulus@switch:~$ nv config apply 
Action succeeded
```

If any conflicts or errors occur during `nv config apply`, you must resolve them manually.

Run the `nv config diff` command to show all the applied configuration.

## Unset Profile-based Configuration

To unset profile based configuration, restore the configuration you backed up previously with the `nv config replace` command. Refer to {{<link url="NVUE-CLI/#manual-back-up-and-restore" text="Back Up and Restore">}}.

## Show Profile‑based Configuration

To show the configured profile on a switch, run the `nv show system do-spx` command:

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

To show the active profile, run the `nv show system do-spx active-profile` command.

The persistent configuration records only the profile name and the parameters you provide. Other operational NVUE show commands show the fully resolved state.
