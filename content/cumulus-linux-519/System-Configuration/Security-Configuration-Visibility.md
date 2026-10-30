---
title: Security Configuration Visibility
author: NVIDIA
weight: 286
toc: 3
---
Every security-relevant setting on a switch is provisioned during manufacturing and then assumed correct for the life of the unit. Provisioning is a write with no read back, so a switch operates normally with secure boot disabled or with a debug token installed, and nothing on the operational surface reports it.

Cumulus Linux can collect the security configuration of the switch components and compare each value with the reference values for the platform. Use the security report to verify that a switch is provisioned securely, after manufacturing or during a field check.

{{%notice note%}}
The security report is supported on SN6600-LD switches. On other platforms, `profile` shows `none` and `security-status` is `fail`.
{{%/notice%}}

<!-- REVIEW: this page and SPDM-Attestation.md are neighbours that a reader confuses easily - SPDM
     attestation returns raw evidence and no verdict, this page returns a verdict. They belong
     cross-referenced in both directions. No link shortcode is drafted because SPDM-Attestation.md
     carries draft: true and does not publish, so a link resolving by its title breaks the build.
     Add links in both pages when that page publishes. Delete this comment before publishing. -->

The report covers these components:

| Component | What the report checks |
|---|---|
| `cpu-uefi` | UEFI Secure Boot state, platform mode, and the key databases (PK, KEK, db, and dbx). |
| `cpu-tpm` | TPM certificates (IAK, IDevID, and the platform certificate). |
| `asic` | ASIC security state: secure boot, firmware encryption, life cycle, production state, debug tokens, security versions, and PSID. |
| `ssd` | SSD self encryption: whether locking is supported, whether locking is enabled, and media encryption. |
| `erot-bmc` | BMC root of trust (ERoT) measurements, read over SPDM: fuses, key revocation, key hashes, debug token, and firmware versions. |

{{%notice note%}}
The `asic` component reports the ASIC's own secure boot chain. It is unrelated to UEFI Secure Boot, which the `cpu-uefi` component reports.
{{%/notice%}}

## Generate a Security Report

To collect the current security values and compare them with the reference values, run the `nv action generate system security report` command. Collection can take a few minutes.

```
cumulus@switch:~$ nv action generate system security report
Action executing ...
collecting security values...
report generated - security status fail (5 components)
Action succeeded
```

Each run replaces the previous report in full. The action shows the resulting security status.

{{%notice note%}}
- The switch does not collect the security values at boot.
- The switch keeps the report in the `/var/run` directory and clears it when the switch reboots. Run the command again after a reboot.
- The report reflects the switch as it was at the last generation. Generate a new report after a firmware update, after a service action, and before an audit or shipment check.
{{%/notice%}}

## Show the Security Report

To show the report, run the `nv show system security report` command:

```
cumulus@switch:~$ nv show system security report
                    operational
------------------  -----------------------------
state               ready
security-status     fail
generated-at        2026-10-11T14:41:18Z
file                /var/run/security_report.json
profile             SN6600_LD
reference-mismatch  cpu-tpm, asic
component
============
    Component  Status   State      Group         Channel
    ---------  -------  ---------  ------------  ----------
    asic       invalid  collected  asic-flint-1  flint
    cpu-tpm    invalid  collected  tpm-1         tpm2-tools
    cpu-uefi   valid    collected  uefi-1        efivars
    erot-bmc   valid    collected  spdm-1.1      redfish
    ssd        valid    collected  sed-1         sedutil
```

The report shows these fields:

| Field | Description |
|---|---|
| `state` | The state of the report. Before you generate the first report, `state` shows `not generated - run: nv action generate system security report`. |
| `security-status` | The result for the whole switch. `security-status` is `pass` only when every component is valid, and `fail` otherwise. Before you generate the first report, `security-status` is `fail`. |
| `generated-at` | The time that the switch generated the report. |
| `file` | The location of the report file. |
| `profile` | The reference profile that the switch uses to judge the values. |
| `reference-mismatch` | The components with a value that differs from the reference. |
| `incomplete-coverage` | The components with a value that the switch did not collect or that has no reference value. |

For each component, the table shows the status, the collection state, the group, and the channel the switch used to read the values.

To show one component and its items, run the `nv show system security report <component-id>` command, where `<component-id>` is `cpu-uefi`, `cpu-tpm`, `asic`, `ssd`, or `erot-bmc`:

```
cumulus@switch:~$ nv show system security report erot-bmc
         operational
-------  ---------
channel  redfish
group    spdm-1.1
state    collected
status   valid
item
=======
    Item      Description                      Measured                Status  Changes
    --------  -------------------------------  ----------------------  ------  ----------
    index-13  Fuses / OTP configuration hash   sha256:40faf452 (48 B)  valid   never
    index-14  EC FW rollback fuses hash        sha256:a217f6f3 (48 B)  valid   never
    index-15  EC FW key-revocation fuses hash  sha256:f899a460 (48 B)  valid   never
    index-16  AP FW rollback fuses hash        sha256:a217f6f3 (48 B)  valid   never
    index-17  AP FW key-revocation fuses hash  sha256:c9c7def2 (48 B)  valid   never
    index-20  Revocation mode                  0x01                    valid   never
    index-36  AP Firmware Version (Primary)    0x70074600              valid   on-upgrade
    index-37  AP Firmware Version (Secondary)  0x70074600              valid   on-upgrade
    index-38  EC Firmware Version (Primary)    0x30000002              valid   on-upgrade
    index-39  EC Firmware Version (Secondary)  0x30000002              valid   on-upgrade
    index-45  Firmware configuration straps    0x10                    valid   never
    index-46  EC key hash blob instance 0      sha256:2ed4262d (48 B)  valid   never
    index-47  EC key hash blob instance 1      sha256:2ed4262d (48 B)  valid   never
    index-48  AP key hash blob instance 0      sha256:a9ef8613 (48 B)  valid   never
    index-49  AP key hash blob instance 1      sha256:a9ef8613 (48 B)  valid   never
    index-51  Debug token status               0x0000000000            valid   never
```

The `Measured` column shows at most 24 characters. A longer hex value shows as a sha256 digest with its size. The report cuts other long text to 21 characters followed by `...`. To show every field in full, including the reference value, the measured value, a note, and the evidence, run the command with the `-o json` option or use the REST API.

## Interpret the Report

Each item has a status:

| Status | Meaning |
|---|---|
| `valid` | The value matches the reference. |
| `invalid` | The switch read the value and it differs from the reference. Fix the switch. |
| `not-collected` | The switch could not read the value. |
| `no-reference` | The platform has no reference value for the item. |
| `N/A` | The switch shows the value but does not judge it. |

When an item is `invalid` or `not-collected`, the report shows a reason with the corrective action.

The `Changes` column shows how a value varies:

| Changes | Meaning |
|---|---|
| `never` | The value is the same on every switch of the model. |
| `on-upgrade` | The value changes with a firmware upgrade. |
| `per-unit` | The value is unique to each switch. |

A `never` item that becomes `invalid` after a firmware update is the signal that the report exists to raise.

## Collect the Report with cl-support

The {{<link url="Understanding-the-cl-support-Output-File" text="cl-support file">}} includes the security report. When you run `cl-support`, the switch generates a new report and adds it to the support file.
