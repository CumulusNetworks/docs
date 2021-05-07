---
title: Cumulus Linux Release Versioning and Support Policy
author: Cumulus Networks
weight: 702
toc: 4
---

This article outlines the release version numbering structure, and support policies, for:

- Cumulus Linux 4.0 and later
- Cumulus Linux and Cumulus RMP 3.0 and later (including 3.7 ESR and later)

{{%notice note%}}

Earlier releases of Cumulus Linux and Cumulus RMP are no longer supported.

{{%/notice%}}

## Version Definitions

The Cumulus Linux installation file name includes the version number, in
the form of CumulusLinux\_x.y.z; for Cumulus RMP, it is CumulusRMP\_x.y.z.

- **x** represents the major release version number. An increased major release version means that the release may include:
    - Significant architectural or engineering changes.
    - New hardware platforms, including new ASICs or chipsets.
    - New functionality and features.
    - Bug fixes.
    - Security updates.
- **y** represents the minor release version number. An increased
    minor release version means that the release may include:
    - New hardware platforms, including new ASICs or chipsets.
    - New functionality and features.
    - Bug fixes.
    - Security updates.
- **z** represents the maintenance release version number. An
    increased maintenance release version may include:
    - New hardware platforms for existing ASICs or chipsets.
    - Bug fixes and updates.
    - Security updates.

## Release, Support Lifecycle and Support Policy

Cumulus Networks supports both mainline and Extended Support Releases
(ESRs). This support mechanism allows us to maintain our desire to
innovate, while providing customers with stable releases once the
architectural needs are met.

Consistent with this two-pronged approach, the mainline and ESR code
branches are separate code bases. As such, issues and fixes in one
branch are independent of the other. The ESR branch is prioritized for
stability first and foremost, so any fixes there are focused on
critical-impact security fixes and urgent bug fixes. This ensures
customers deploying an ESR release can experience minimal disruption in
their day to day network operations.

The following diagram illustrates the ESR and mainline branches, and the
table below it describes the characteristics of each.

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
<td>Minor releases quarterly; maintenance releases as needed</td>
<td>Maintenance releases as needed</td>
</tr>
<tr class="odd">
<td>Support Duration (Software updates and support)</td>
<td><p>ESR branch, before ESR is released: Software updates and Global Support Services (GSS) support</p>
<p>ESR branch, after ESR is released: 12 months GSS support only from date of ESR release</p></td>
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

Cumulus Linux and Cumulus RMP 3.7.12 has transitioned into the extended
support phase (ESR). Customers can choose to continue using Cumulus
Linux 3.7 ESR, a mature and stable operating system, or they can upgrade
to Cumulus Linux 4.y.z, with the latest and greatest features. Cumulus
Networks will continue support and maintain Cumulus Linux and Cumulus
RMP 3.7 ESR for 3 years, until 21 February, 2023.

| Cumulus Linux Version | ESR Start Date    | End of Life Date  |
| --------------------- | ----------------- | ----------------- |
| 4.y.z                 | TBD               | TBD               |
| 3.7.12 - 3.7.z ESR    | 21 February, 2020 | 21 February, 2023 |
| 3.0.0 - 3.7.11        | N/A               | 31 December, 2020 |
| 2.5.6 - 2.5.12        | 2 February, 2016  | 2 February, 2019  |
| 2.5.5 and earlier     | N/A               | 31 December, 2016 |

## Upgrade Process

For information regarding upgrading from previous Cumulus Linux releases, refer to the {{<kb_link url="cumulus-linux-43/Installation-Management/Upgrading-Cumulus-Linux/" text="Cumulus Linux upgrade documentation">}}.
