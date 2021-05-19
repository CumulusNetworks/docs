---
title: Cumulus NetQ Release Versioning and Support Policy
author: Cumulus Networks
weight: 703
toc: 4
---

This article outlines the release version numbering structure, and support policies, for:

- Cumulus NetQ 3.x
- Cumulus NetQ 2.x
- Cumulus NetQ 1.4

## Version Definitions

Cumulus NetQ software installation file names include a version number,
in the form of x.y.z-OS\~TAG\_CPU.

- **x** represents the major release version number. An increased
    major release version means that the release may include:
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

The following diagram illustrates the release version and support relationship.

{{<img src="/images/knowledge-base/NQ-rel-vers-and-sup-pol.png" width="700">}}

Customers running NetQ 1.4.x and earlier, can continue to use their
current license until their support expires.  These customers have the
option to transfer their existing license to the subscription license
where they will receive the new NetQ 2.1 software, all the support, and
upgrades for the next five years for free.  Alternately, these customers
can continue to use NetQ 1.4 and deploy NetQ 3.x at the same time with
the new subscription license.

## Product End of Life

Currently, there are no end of life plans for Cumulus NetQ 1.x or 2.x.

## Upgrade Process

For information regarding upgrading from previous Cumulus NetQ releases,
refer to the [Cumulus NetQ Deployment Guide]({{<ref "/cumulus-netq-33/Manage-Deployment" >}}).
