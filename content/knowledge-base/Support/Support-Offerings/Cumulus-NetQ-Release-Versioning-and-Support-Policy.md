---
title: NetQ Release Versioning and Support Policy
author: NVIDIA
weight: 703
toc: 4
---

This article outlines the release version numbering structure and support policies for NetQ.
## Version Definitions

NetQ software installation file names include a version number, in the form of x.y.z-OS\~TAG\_CPU.

- **x** represents the major release version number. An increased major release version means that the release might include:
    - New functionality within the existing market.
    - New market entries.
    - Major positioning changes.
    - A significant engineering rebase.
- **y** represents the minor release version number. An increased minor release version means that the release might include:
    - New hardware platforms.
    - New features within the existing market.
    - Bug fixes.
    - Security updates.
- **z** represents the maintenance release version number. An increased maintenance release version might include:
    - Feature improvements.
    - Bug fixes and updates.
    - Security updates.
- **OS** indicates the Network Operating System information (cl for Cumulus Linux, deb10 for SONiC, ub for Ubuntu)
- **TAG** represents a timestamp for the release of the version.
- **CPU** architecture represents architecture.

For example:

- netq-apps_<strong>4.10.0</strong>-deb10u<strong>46</strong>~1713949850.127fb0c1b_amd64.deb
- netq-agent_<strong>4.10.0</strong>-deb10u<strong>46</strong>~1713949850.127fb0c1b_amd64.deb

## Release, Support Lifecycle and Support Policy

NetQ is offered with a per switch subscription that includes support for 1, 3, and 5 years options. The subscription model allows customers to upgrade the software as updates and new versions become available, for the period of the subscription.

- Review the NetQ user guide for the supported Network Operating System (NOS) versions. Note that when your Network Operating System is no longer supported, NetQ customer support ends along with it. Access to NetQ is permitted until the end of the subscription period.
- Use matching versions of NetQ Server and both NetQ Agent and NetQ Apps packages on switches (for example, NetQ 4.2.0 Server with NetQ 4.2.0 Agents and Apps on the switches).
- The product is supported for the period of the subscription and bug fixes are received by upgrading to new versions of software.
- A NetQ version is supported for two years from its release date. After that date, it is necessary to upgrade to a later release to continue receiving support for the period of the subscription.

## NetQ Support Matrix

The following table depicts the NetQ release support matrix:

| NetQ Release | Release Date | End of Support |
| :--------: | --------- | --------- |
| 4.10.z | 30-Apr-2024 | 30-Apr-2026 |
| 4.9.z | 18-Mar-2024 | 18-Mar-2026 |
| 4.8.z | 10-Nov-2023 | 10-Nov-2025 |
| 4.7.z | 11-Aug-2023 | 11-Aug-2025 |
| 4.6.z | 01-May-2023 | 01-May-2025 |
| 4.5.z | 27-Feb-2023 | 27-Feb-2025 |
| 4.4.z | 09-Nov-2022 | 09-Nov-2024 |
| 4.3.z | 05-Aug-2022 | 05-Aug-2024 |
| 4.2.z | 24-May-2022 | 24-May-2024 |
| 4.1.z | 13-Jan-2022 | 13-Jan-2024 |

**NetQ 1.y, 2.y, and 3.y releases are End of Support.**

## Upgrade Process

For information regarding upgrading from previous NetQ releases, refer to the [NetQ Deployment Guide]({{<ref "/cumulus-netq-410/Installation-Management" >}}).
