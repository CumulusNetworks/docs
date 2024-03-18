---
title: NetQ Cloud Release Versioning and Support Policy
author: NVIDIA
weight: 704
toc: 4
---

This article outlines the release version numbering and support policies for the cloud version of NetQ.

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

This number corresponds to the release version of the software. NetQ requires two Debian packages per release. For example:

- netq-apps_<strong>4.9.0</strong>-deb10u<strong>45</strong>~1710407608.ea9740d7c_amd64.deb
- netq-agent_<strong>4.9.0</strong>-deb10u<strong>45</strong>~1710407608.ea9740d7c_amd64.deb
## Release, Support Lifecycle and Support Policy

NetQ is offered with a per switch subscription that includes support for 1, 3, and 5 years options. The subscription model allows customers to upgrade the software as updates and new versions become available, for the period of the subscription.

Updates are automatically applied to the NetQ Server running in the Cloud. NVIDIA notifies customers before performing upgrades, and makes release notes available for each release.

It is necessary to upgrade the NetQ Agents and NetQ Apps running on switches to the NetQ Server version that is running in the Cloud. NetQ Server compatibility is tested with the current version and one prior version of Agent and Apps software. Review the NetQ user guide for the supported Network Operating System (NOS) versions. 

Note that when your Network Operating System is no longer supported, NetQ customer support ends along with it. Access to NetQ is permitted until the end of the subscription period.
## Upgrade Process

For information regarding upgrading from previous NetQ releases, refer to the [NetQ Deployment Guide]({{<ref "/cumulus-netq-49/Installation-Management" >}}).
