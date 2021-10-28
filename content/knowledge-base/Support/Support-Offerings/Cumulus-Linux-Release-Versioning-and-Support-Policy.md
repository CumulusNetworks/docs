---
title: Cumulus Linux Release Versioning and Support Policy
author: Cumulus Networks
weight: 702
toc: 4
---

This article outlines the release version numbering structure and support policies for:
- Cumulus Linux 4.0 and later
- Cumulus Linux and Cumulus RMP 3.0 and later (including 3.7 ESR and later)

{{%notice note%}}
Earlier releases of Cumulus Linux and Cumulus RMP are no longer supported.
{{%/notice%}}

## Version Definitions

The Cumulus Linux installation file name includes the version number, in the form of CumulusLinux\_x.y.z; for Cumulus RMP, it is CumulusRMP\_x.y.z.

- **x** represents the major release version number. An increased major release version means that the release might include:
    - Significant architectural or engineering changes.
    - New hardware platforms, including new ASICs or chipsets.
    - New functionality and features.
    - Bug fixes.
    - Security updates.
- **y** represents the minor release version number. An increased minor release version means that the release might include:
    - New hardware platforms, including new ASICs or chipsets.
    - New functionality and features.
    - Bug fixes.
    - Security updates.
- **z** represents the maintenance release version number. An increased maintenance release version might include:
    - New hardware platforms for existing ASICs or chipsets.
    - Bug fixes and updates.
    - Security updates.

## Release, Support Lifecycle and Support Policy

NVIDIA supports both mainline and Extended Support Releases (ESRs). This support mechanism allows NVIDIA to maintain its desire to innovate, while providing stable releases as soon as it meets the architectural needs.

Consistent with this two-pronged approach, the mainline and ESR code branches are separate code bases. As such, issues and fixes in one branch are independent of the other. NVIDIA prioritizes the ESR branch for stability; any fixes on that branch focus on critical-impact security fixes and urgent bug fixes. This ensures that if you deploy an ESR release, you experience minimal disruption in day to day network operations.

The following diagram illustrates the ESR and mainline branches, and the table below it describes the characteristics of each.

{{<img src="/images/knowledge-base/support-version_policy.png" width="800">}}

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<th> </th>
<th>Mainline</th>
<th>Extended-Support Release (ESR)</th>
</tr>
<tr class="even">
<td>Functionality</td>
<td>Latest features</td>
<td>No new functionality</td>
</tr>
<tr class="odd">
<td>Stability</td>
<td>Stable and robust</td>
<td>Highly stable and robust</td>
</tr>
<tr class="even">
<td>Frequency</td>
<td>Minor releases every quarter; maintenance releases as needed</td>
<td>Maintenance releases as needed</td>
</tr>
<tr class="odd">
<td>Support Duration (Software updates and support)</td>
<td><p>ESR branch, before releasing ESR: Software updates and Global Support Services (GSS) support</p>
<p>ESR branch, after releasing ESR: 12 months GSS support only from date of ESR release</p></td>
<td>3 years from release date of version</td>
</tr>
<tr class="even">
<td>Software Updates</td>
<td>New functionality, security updates, bug fixes</td>
<td>Security updates and critical bug fixes</td>
</tr>
<tr class="odd">
<td>Security Updates</td>
<td>ASAP</td>
<td>ASAP</td>
</tr>
</tbody>
</table>

## Product End of Life

Cumulus Linux and Cumulus RMP 3.7.12 have transitioned into the extended support phase (ESR). You can choose to continue using Cumulus Linux 3.7 ESR, a mature and stable operating system, or you can upgrade to Cumulus Linux 4.y.z, with the latest and greatest features. NVIDIA supports and maintains Cumulus Linux and Cumulus RMP 3.7 ESR for 3 years, until 21 February, 2023.

### Cumulus Linux 5.y.z

| Cumulus Linux Version | ESR Start Date    | End of Life Date  |
| --------------------- | ----------------- | ----------------- |
| 5.0.z                 | N/A               | November 2024     |
| 5.y.z                 | February 2024     | February 2027     |

- All Cumulus Linux 5.y releases are supported until November 2024. The February 2024 release will be an ESR release.
- Cumulus Linux 5.y.z supports Spectrum based switches only.

### Cumulus Linux 4.y.z

| Cumulus Linux Version | ESR Start Date    | End of Life Date  |
| --------------------- | ----------------- | ----------------- |
| 4.y.z (Spectrum based switches) | N/A     | December 2022     |
| 4.3.z (Broadcom based switches) | N/A     | December 2025     |

- The Cumulus Linux 4.y.z release will not have an ESR version. NVIDIA recommends that you run the latest Cumulus Linux 4.3.z release on Broadcom switches and the Cumulus Linux 4.4.z release on Spectrum switches.
- Cumulus Linux 4.y.z through 4.3.z is in maintenance mode; no new features are planned.

### Cumulus Linux 3.y.z

| Cumulus Linux Version | ESR Start Date    | End of Life Date  |
| --------------------- | ----------------- | ----------------- |
| 3.7.12 and later      |February 2020      | February 2023     |
| 3.7.11 and earlier    | N/A               | December 2020     |

- Cumulus Linux 3.7.z is an ESR release for versions 3.7.12 and later. Support for Cumulus Linux 3.7 ESR will continue until February 2023. All earlier versions of Cumulus Linux 3.7.z are considered end of life and are no longer supported.
- Cumulus Linux 3.y.z supports both Spectrum and Broadcom based switches.

### Cumulus Linux 2.y.z

All Cumulus Linux 2.y.z releases reached end of life on February 2019 and are no longer supported.

## Upgrade Process

For information regarding upgrading from previous Cumulus Linux releases, refer to the [Cumulus Linux upgrade documentation]({{<ref "/cumulus-linux-43/Installation-Management/Upgrading-Cumulus-Linux" >}}).