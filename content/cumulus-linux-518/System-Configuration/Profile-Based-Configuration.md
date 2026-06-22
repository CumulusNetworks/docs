---
title: Profile Based Configuration
author: NVIDIA
weight: 299
toc: 3
---
Cumulus Linux provides a simplified, profile‑based way to configure a switch that replaces many NVUE commands. You can select an NVIDIA‑predefined profile and provide interface ranges and breakout values. Cumulus Linux generates and applies all immutable configuration, such as link breakout, ISSU, traffic class, adaptive routing, telemetry, QoS, and PFC.

{{%notice note%}}
- Profile‑based switch configuration is supported on Spectrum‑X platforms only (Spectrum-4, Spectrum-5, and Spectrum-6).
- Layer 3 addressing, routing protocols, EVPN, and telemetry OTLP export are not supported.
- Before you use the profile‑based configuration on the switch, you must set up physical connectivity.
- Profile‑based switch configuration does not introduce new authentication or authorization mechanisms. It relies on existing NVUE role-based access control.
- The switch stores profile‑based configuration in the standard NVUE configuration files with the same file permissions and access controls.
{{%/notice%}}

## Set Profile-based Configuration

Before you set profile-based configuration, NVIDIA recommends you back up the current configuration on the switch with the `nv config save` command so that you can restore the saved config later, if needed. Refer to {{<link url="NVUE-CLI/#back-up-and-restore-configuration-with-nvue" text="Back Up and Restore Configuration with NVUE">}}.

To set profile‑based configuration on the switch:
- Specify the role of the switch: `leaf`, `spine-2` (two-tier spine), `spine-3` (three-tier spine), or `super-spine`.
- Specify the upinks and, or, downlinks. For the direction rules, refer to the table below.
- Apply the profile.

| Role | Direction rules |
| ---- | --------------- |
| `leaf` | Both uplink and downlink required. Adaptive routing **not** applied on downlinks (host facing).|
| `spine-2`&nbsp;(2-tier) | Downlink only.|
| `spine-3`&nbsp;(3-tier) | Both uplink (SSP-facing) and downlink (leaf-facing). Adaptive routing applied on both directions. |
| `super-spine` | Downlink only (spine-facing). No ISSU. 3-tier topology only. |

The following example sets profile-based configuration on the leaf and applies the profile:

```
cumulus@switch:~$ nv set system do-spx profile leaf uplink swp1-swp32 breakout x4 
cumulus@switch:~$ nv set system do-spx profile leaf downlink swp33-swp64 breakout x1
cumulus@switch:~$ nv config apply 
cumulus@switch:~$ nv action activate system do-spx profile leaf
Action executing ...
Rendering do-spx profile: leaf
Action executing ...
patching rendered do-spx profile: leaf
Action executing ...
do-spx profile 'leaf' staged in revision 18. Review: nv config diff applied 18. Apply: nv config apply --rev 18.
Action succeeded
```

{{%notice note%}}
The breakout is required if you specify an interface-range. With breakout x4, parent ports swp1-32 split into sub-interfaces swp1s0-swp32s3 (128 ports). Breakout x1 keeps ports as-is (swp33-64). All subsequent per-interface commands target the split ports.
{{%/notice%}}

The following example sets profile-based configuration on a two-tier spine:

```
cumulus@switch:~$ nv set system do-spx role spine-2 downlink swp1-swp64 breakout x1
cumulus@switch:~$ nv config apply
cumulus@switch:~$ nv action activate system do-spx profile spine-2
Action executing ...
Rendering do-spx profile: spine-2
Action executing ...
patching rendered do-spx profile: spine-2
Action executing ...
do-spx profile 'spine-2' staged in revision 18. Review: nv config diff applied 18. Apply: nv config apply --rev 18.
Action succeeded
```

The following example sets profile-based configuration on a three-tier spine:

```
cumulus@switch:~$ nv set system do-spx role spine-3 uplink swp1-swp64 breakout x1
cumulus@switch:~$ nv set system do-spx role spine-3 downlink swp33-swp64 breakout x1
cumulus@switch:~$ nv config apply 
cumulus@switch:~$ nv action activate system do-spx profile spine-3
Action executing ...
Rendering do-spx profile: spine-3
Action executing ...
patching rendered do-spx profile: spine-3
Action executing ...
do-spx profile 'spine-3' staged in revision 18. Review: nv config diff applied 18. Apply: nv config apply --rev 18.
Action succeeded
```

The following example sets profile-based configuration on a superspine:

```
cumulus@switch:~$ nv set system do-spx role super-spine downlink swp33-swp64 breakout x1
cumulus@switch:~$ nv config apply
cumulus@switch:~$ nv action activate system do-spx profile super-spine
Action executing ...
Rendering do-spx profile: super-spine
Action executing ...
patching rendered do-spx profile: super-spine
Action executing ...
do-spx profile 'super-spine' staged in revision 18. Review: nv config diff applied 18. Apply: nv config apply --rev 18.
Action succeeded
```

## Unset Profile-based Configuration

To unset profile based configuration, restore the configuration you backed up previously with the `nv config replace` command. Refer to {{<link url="NVUE-CLI/#back-up-and-restore-configuration-with-nvue" text="Back Up and Restore Configuration with NVUE">}}.

## Show Profile‑based Configuration

To show the profile‑based configuration on a switch (profile, directions, interface ranges, and breakout values), run the `nv show system do-spx` command:

```
cumulus@switch:~$ nv show system do-spx
                    operational  applied
----------------  	-----------  ------------
role                           		leaf
[uplink]                       		swp1
[downlink]			                  swp2
[exception-list]               

```

The persistent configuration records only the profile name and the parameters you provide. Other operational NVUE show commands show the fully resolved state.
