---
title: SPDM Attestation
author: NVIDIA
weight: 285
toc: 3
draft: true
---
<!-- Alpha in 5.19-->
SPDM (Security Protocol and Data Model) attestation lets an external verifier confirm that the hardware components in a switch are genuine and are running the firmware they are meant to run. Each component that has a root of trust signs a set of measurements, such as hashes of its running firmware and configuration, with a private identity key fused into the component during manufacturing. The switch BMC collects this evidence from the components, and Cumulus Linux exposes it through NVUE.

Cumulus Linux does not decide whether a component passes or fails. It gathers the evidence and returns it to the verifier, which validates the certificate chain against the NVIDIA root certificate authorities, checks the signature on the measurements, and compares the measurements against the reference values that NVIDIA publishes. Read the output of these commands as raw evidence, not as a verdict.

Use attestation to detect a component that has been swapped or physically altered since manufacturing, to confirm that a switch runs the firmware you expect, and to audit a switch before you allow it to carry production traffic.

<!-- REVIEW: two behaviors are left open in the specification and are therefore not documented here.
     First, requirement 6 says the commands are pruned on a platform without a BMC or without SPDM
     support, but adds "will check if error instead of pruning will be supported" — so the note below
     states the requirement and stops, without saying what happens elsewhere. Second, section 5.1
     says Cumulus Linux saves no attestation state and queries the BMC from scratch after a reboot,
     but does not say whether previously generated measurements survive on the BMC and remain
     readable. Confirm both, then add them. Delete this comment before publishing. -->

{{%notice note%}}
- SPDM attestation requires a switch with a BMC that supports SPDM hardware attestation.
- If the BMC is unreachable, or if a measurement request fails or times out, the commands return an error. Cumulus Linux never presents previously generated measurements as current evidence.
{{%/notice%}}

## Show the Attestable Components

The components you can attest depend on the switch hardware. To list them, run the `nv show system security spdm` command:

<!-- TODO: capture `nv show system security spdm` output on a switch and paste here. The
     specification provides no NVUE sample output for any command on this page. -->

```
cumulus@switch:~$ nv show system security spdm
```

Component identifiers name the root of trust and the component it protects, such as `ERoT_BMC_0` for the BMC and `ERoT_CPU_0` for the CPU.

## Generate Signed Measurements

Before you read measurements, generate a fresh set. The switch asks the component to measure its current firmware state, sign the result, and return it.

<!-- REVIEW: the specification gives this command two ways. Its command-syntax table and its REST
     table both put the component directly after `spdm`, which is the form drafted below; its flow
     descriptions, its "Format:" line and its test cases insert `measurements` between `spdm` and the
     component. Resolved in favour of the syntax and REST tables, because the REST table defines the
     object model and its POST endpoint is /generate/system/security/spdm/{component-id}, with no
     measurements node — and because `measurements` is a show leaf everywhere else in the document.
     Confirm against a candidate build. Delete this comment before publishing. -->

To generate measurements for a component, run the `nv action generate system security spdm <component-id> nonce <nonce>` command:

```
cumulus@switch:~$ nv action generate system security spdm ERoT_CPU_0 nonce 3f8a1c07d4b962e5a08c17fe4d3b25908e6c1a74bf03d582971ea6c4b85d0f13
```

The nonce is a random 64-character hexadecimal string, and it is optional. Supply one when you want proof that the measurements are fresh: the component includes the nonce in the data it signs, so a verifier that finds its own nonce inside the signed payload knows the measurements were calculated for this request and are not a replayed copy of an earlier response.

<!-- TODO: capture the `nv action generate system security spdm` output on a switch and add it to the
     code block above. -->

## Show the Attestation Evidence

To show both the certificate chain and the most recent signed measurements for a component, run the `nv show system security spdm <component-id>` command:

<!-- TODO: capture the output of all three commands in this section on a switch and paste it after
     each command. -->

```
cumulus@switch:~$ nv show system security spdm ERoT_CPU_0
```

To show only the measurements, run the `nv show system security spdm <component-id> measurements` command:

```
cumulus@switch:~$ nv show system security spdm ERoT_CPU_0 measurements
```

To show only the certificate chain, run the `nv show system security spdm <component-id> certificate` command:

```
cumulus@switch:~$ nv show system security spdm ERoT_CPU_0 certificate
```

These commands show the measurements from the most recent generate action. To collect current evidence, generate measurements again before you read them.
