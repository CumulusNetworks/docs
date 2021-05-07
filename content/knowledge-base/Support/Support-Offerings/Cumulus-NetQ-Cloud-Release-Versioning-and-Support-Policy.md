---
title: Cumulus NetQ Cloud Release Versioning and Support Policy
author: NVIDIA
weight: 704
toc: 4
---

This article outlines the release version numbering and support policies for the cloud version of:

- Cumulus NetQ 3.x
- Cumulus NetQ 2.2.0-2.4.1

## Version Definitions

The Cumulus NetQ Cloud software installation file names include a
version number, in the form of x.y.z-OS\~TAG\_CPU.

- **x** represents the major release version number. An increased major release version means that the release may include:
    - New functionality within the existing market.
    - New market entries.
    - Major positioning changes.
    - A significant engineering rebase.
- **y** represents the minor release version number. An increased
    minor release version means that the release may include:
    - New hardware platforms.
    - New features within the existing market.
    - Bug fixes.
    - Security updates.
- **z** represents the maintenance release version number. An
    increased maintenance release version may include:
    - Feature improvements.
    - Bug fixes and updates.
    - Security updates.
- **OS** indicates the operating system. Support is available for
    Cumulus Linux, Ubuntu, Red Hat and CentOS.
- **TAG** represents a timestamp when the version was released.
- **CPU** architecture represents architecture. Support is available
    for x86\_64 and ARM.

This number corresponds to the release version of the software. For NetQ
there are two Debian packages that are required per release. This
example shows the first minor release of the third major release, for
the Ubuntu OS and x86\_64 CPU architecture:

- netq-agent\_3.1.0-ub18.04u28\~1594095612.8f00ba1\_amd64.deb
- netq-apps\_3.1.0-ub18.04u28\~1594095612.8f00ba1\_amd64.deb

## Release, Support Lifecycle and Support Policy

Cumulus NetQ is licensed per Cumulus Linux switch. NetQ is a
subscription-based license that includes support for 1, 3, and 5 years
options. NetQ has one set of SKUs for 1G switches and one set of SKUs
for switches that are 10G and greater. The NetQ agent can be installed
free-of-charge on Ubuntu, Red Hat, and CentOS endpoint that is connected
to a NetQ-licensed Cumulus Linux switch. The subscription model
enables customers to upgrade the software as updates and new versions
become available, for the period of the subscription.

Updates are automatically applied. Minor releases are planned each
quarter, with maintenance releases as needed. Customers are notified
before upgrades are performed, and release notes are available for each release.

Customers with current NetQ 1.4 and earlier perpetual licenses have the
option to transfer to the five (5) year NetQ Cloud subscription where
they will receive the NetQ 3.x software, support, and upgrades for free.  

## Product End of Life

Currently, there are no end of life plans for Cumulus NetQ 2.2.

## Upgrade Process

For information regarding upgrading from previous Cumulus NetQ releases, refer to the {{<kb_link url="cumulus-netq-33/Manage-Deployment/" text="Cumulus NetQ Deployment Guide">}}.
