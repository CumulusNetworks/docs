---
title: Cumulus Linux Release Versioning and Support Policy
author: NVIDIA
weight: 702
toc: 4
---

This article outlines the release version numbering structure and support policies for Cumulus Linux.
## Version Definitions

The Cumulus Linux installation file name includes the version number, in the form of CumulusLinux\_x.y.z.

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
</tbody>
</table>

## Product End of Life

NVIDIA does not provide support for end of life releases; migrate to a current release for support and bug fixes. NVIDIA recommends that you run:

- The latest Cumulus Linux 5.y.z release on Spectrum switches.
- The latest Cumulus Linux 4.3.z release on Broadcom switches.

### Cumulus Linux 5.y.z

| Cumulus Linux Version | ESR Start Date    | End of Life Date  |
| --------------------- | ----------------- | ----------------- |
| 5.y.z                 | N/A               | April 2025        |
| 5.9.z                 | April 2024        | April 2027        |

Cumulus Linux 5.y.z supports Spectrum based switches only.
### Cumulus Linux 4.y.z

| Cumulus Linux Version | ESR Start Date    | End of Life Date  |
| --------------------- | ----------------- | ----------------- |
| 4.0.0 to 4.3.0 (all switches)   | N/A     | May 2023          |
| 4.4.z (Spectrum switches)       | N/A     | May 2023          |
| 4.3.1 and later (Broadcom switches) | N/A | December 2025     |

- The Cumulus Linux 4.y.z release will not have an ESR version. 
- Cumulus Linux 4.y.z on Spectrum switches reached end of life on May 2023 and are no longer supported.
- Cumulus Linux 4.3.z is in maintenance mode; no new features are planned.

### Cumulus Linux 3.y.z

All Cumulus Linux 3.y.z releases reached end of life on February 2023 and are no longer supported.

### Cumulus Linux 2.y.z

All Cumulus Linux 2.y.z releases reached end of life on February 2019 and are no longer supported.

## Upgrade Process

For information regarding upgrading from previous Cumulus Linux releases, refer to the [Cumulus Linux upgrade documentation]({{<ref "/cumulus-linux-56/Installation-Management/Upgrading-Cumulus-Linux" >}}).
