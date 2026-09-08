---
title: Security Configuration Visibility
author: NVIDIA
weight: 286
toc: 3
---
Every security-relevant setting on a switch is provisioned during manufacturing and then assumed correct for the life of the unit. Provisioning is a write with no read back, so a switch operates normally with secure boot disabled or with a debug token installed, and nothing on the operational surface reports it.

The security report closes that gap by comparing for each security component and each item, the value the platform is expected to carry against the value this switch actually carries, and returns a verdict for each item and one aggregate verdict for the whole switch. Everything the report shows is summarized, the report never shows key material.

<!-- REVIEW: the specification is an NVOS HLD that names Cumulus Linux and Spectrum-6 as a
     first-class target under separate feature requests (#4777648 and #4777699), and states no
     quality level for the Cumulus Linux delivery. The What's New entry for this feature reads
     "Support security configurations visibility for manufacturing and field inspection (Phase 1)"
     with no Beta suffix, which claims GA by default. Confirm the quality level against the 5.19
     Redmine execution query and add "(Beta)" to the notice below and to the What's New entry if
     needed. The platform sentence is drafted from the specification's platform applicability table
     and is unverified. Delete this comment before publishing. -->

{{%notice note%}}
The security report is supported on Spectrum-6 switches.
{{%/notice%}}

<!-- REVIEW: this page and SPDM-Attestation.md are neighbours that a reader confuses easily - SPDM
     attestation returns raw evidence and no verdict, this page returns a verdict. They belong
     cross-referenced in both directions. No link shortcode is drafted because SPDM-Attestation.md
     carries draft: true and does not publish, so a link resolving by its title breaks the build.
     Add links in both pages when that page publishes. Delete this comment before publishing. -->

## Generate a Security Report

To collect the security values and produce a report, run the `nv action generate system security report` command:

```
cumulus@switch:~$ nv action generate system security report
Action executing ...
collecting security values...
report generated - verdict pass (9 components)
Action succeeded
```

Each run replaces the previous report in full. The action reports the resulting verdict as its status.

{{%notice note%}}
The report reflects the switch as it was at the last generation. A change on a device becomes visible on the next generate, so generate a fresh report after a firmware update, after a service action, and before any audit or shipment check.
{{%/notice%}}

## Show the Security Report

To show the report summary, run the `nv show system security report` command:

<!-- TODO: capture this output on a Spectrum-6 switch and paste it here. The block below is adapted
     from the specification's mock output: the profile string, the component list, and the item
     counts are all platform data that must come from real hardware. -->

```
cumulus@switch:~$ nv show system security report
state         ready
verdict       fail
  reference-mismatch:  cpu-uefi
generated-at  2026-08-16T07:31:31Z
profile       Spectrum-6 v1  [GA golden]

Component   Items  Validity
----------  -----  --------
cpu-uefi    6      bad
cpu-tpm     5      good
bmc-irot    3      good
asic        9      good
ssd         2      good
```

The summary shows these fields:

| Field | Description |
|---|---|
| `state` | Collection state: *collecting* while a generation is in progress, *ready* when a report exists. |
| `verdict` | The aggregate result over the whole report, *pass* or *fail*. |
| `reference-mismatch` | The components that carry at least one mismatched item. |
| `generated-at` | When the report is produced. |
| `profile` | The reference profile the switch is judged against, including its version and milestone. |

To show the items inside one component, run the `nv show system security report <component-id>` command:

<!-- REVIEW: the specification contradicts itself on the UEFI key databases. Its UEFI measurement
     map classes db-db and dbx-db as on-upgrade, which means they are judged on presence only, while
     its black-box test case requires a foreign UEFI db key to turn a never row bad. The map section
     defines the item semantics, so the block below follows the map and uses pk-db, a never-class
     item, for the mismatched row. Confirm against a candidate build.
     Delete this comment before publishing. -->

```
cumulus@switch:~$ nv show system security report cpu-uefi
channel : local - EFI variable store
Item             Reference        Measured         Validity  Changes
---------------  ---------------  ---------------  --------  ----------
secure-boot      enabled          enabled          good      never
platform-mode    user             user             good      never
pk-db            sha384:be55..12  sha384:5d40..e2  bad       never
kek-db           sha384:77a1..3c  sha384:77a1..3c  good      never
db-db            populated        sha384:0a91..77  good      on-upgrade
dbx-db           populated        sha384:c318..90  good      on-upgrade
```

To show the full untruncated values behind a component - complete digests, certificate identities, and raw tool output - run the `nv show system security report <component-id> detail` command:

```
cumulus@switch:~$ nv show system security report cpu-uefi detail
Item             Measured (full)                               Validity
---------------  --------------------------------------------  --------
pk-db            sha384:<full 96-hex digest>                    bad
```

All three levels accept `--output json`. A scripted check gates on the `verdict` field of the JSON output.

<!-- REVIEW: the component identifiers below are drafted from the specification's CLI help listing.
     Three items need confirmation against a candidate build. First, the specification's platform
     applicability table states that Spectrum-6 units built on the AST2600 use an ERoT measurement
     map rather than the IRoT rows, and one of its examples uses the component identifier
     `erot-bmc` where the help listing uses `bmc-irot` - the identifier a user types on a
     Spectrum-6 switch is not settled. Second, the specification lists an `sma-mcu` component in its
     phase 1 scope, but does not list that component for Spectrum-6, so it is omitted here.
     Third, the specification's scope section places CPLD posture in phase 2 while its CLI examples
     show a `cpld1` component in the summary table and give it a full drill-down example. The
     `cpld1` component is omitted here because a phase 2 capability must not be documented as
     available. Confirm before publishing. Delete this comment before publishing. -->

The report covers these components:

| Component | Description |
|---|---|
| `cpu-uefi` | UEFI secure boot state and the enrolled key databases. |
| `cpu-tpm` | TPM provisioning: the identity certificates and the presence of the self-encrypting drive key banks. |
| `bmc-irot` | BMC root of trust posture: flash write protection, staged boot policy, and debug token state. |
| `asic` | ASIC security posture: life cycle state, secure firmware, fuse counters, and debug access paths. |
| `ssd` | Whether the drive supports self encryption, and whether self encryption is enabled. |

The rows a switch renders are exactly the rows in the reference profile for that platform, so they are identical on every unit of the same platform. 

{{%notice note%}}
The `asic` component reports the ASIC's own secure boot chain. It is unrelated to UEFI secure boot, which the `cpu-uefi` component reports.
{{%/notice%}}

## Interpret the Report

Each item carries a validity verdict:

| Validity | Meaning |
|---|---|
| *good* | The item matches what the platform expects. |
| *bad* | The item does not match, or a judged item is empty or zeroed. |
| *N/A* | The item is not judged. |
| *error* | The item could not be checked. |

The `Changes` column states how changeable a value is, which determines how the switch judges it:

| Changes | Meaning | How the switch judges it |
|---|---|---|
| *never* | Fixed for the lifetime of the platform: fuses, key anchors, and lock and debug state. | Compared against the reference value. A mismatch is *bad*. |
| *on-upgrade* | Moves with a software or firmware release: firmware hashes, security versions, and revocation lists. | Presence only. An empty value is *bad*. A difference in content is shown but does not affect the verdict. |
| *per-unit* | Differs from unit to unit by design: serial numbers, chip identifiers, and boot status. | Presence only. An empty value is *bad*. The value itself is never compared. |

{{%notice note%}}
A *never* row that turns *bad* after a firmware update is the signal the report exists to raise. A difference in an *on-upgrade* value after an update is expected and never affects the verdict.
{{%/notice%}}

The aggregate `verdict` is *fail* when any item in scope is *bad* or *error*, and *pass* only when every judged item matched. A coverage gap can never read as compliance.

When a component fails to answer, the switch writes a warning to the system log naming the component and the item.

## Considerations

{{%notice note%}}
- A switch with no report renders a verdict of *fail* and names the command that generates the report. An ungenerated report and a deleted report can never read as *pass*.
- A component that the reference profile expects but that does not answer renders every judged row as *error*, and the verdict as *fail*. The absent component is itself the finding.
- When a component answers in part, the switch judges the items it returs and renders each missing judged item as *error*.
- When a component is unavailable (for example, a BMC that is still starting), the switch retries, then renders those rows as *error*. Collection completes on its own when the component returns.
- When the switch carries no reference profile for its part number, or carries a profile for a different platform, the report answers that the platform is not covered. Nothing is judged against values that belong to another platform.
{{%/notice%}}

The reference profile ships inside the Cumulus Linux image, one per platform, and is generated from a tested reference switch and approved at a release milestone.

<!-- REVIEW: this note is drafted from the specification's open issue 1, which states that until the
     reference profiles are generated and approved at platform bring-up, release-class rows render
     N/A by design. Confirm whether that still holds for the 5.19 image before publishing - if the
     profiles are approved, delete the note. Delete this comment before publishing. -->

{{%notice note%}}
Until the reference profile for a platform is approved at platform bring-up, items in that profile render *N/A*.
{{%/notice%}}

A {{<link url="Understanding-the-cl-support-Output-File" text="cl-support file">}} includes the report. When the switch has no report, the cl-support collection generates one.
