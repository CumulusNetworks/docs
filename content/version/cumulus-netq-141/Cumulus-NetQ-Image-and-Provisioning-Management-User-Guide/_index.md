---
title: Cumulus NetQ Image and Provisioning Management User Guide
author: Cumulus Networks
weight: 11
aliases:
 - /display/NETQ141/Cumulus+NetQ+Image+and+Provisioning+Management+User+Guide
 - /pages/viewpage.action?pageId=10453535
pageID: 10453535
---
This guide is intended for network administrators who are responsible
for provisioning switches with Cumulus Linux operating system and
network configuration, whether initially or as an upgrade, in their data
center environment. The Image and Provisioning Management (IPM)
application provides local storage and distribution services for the
Cumulus Linux network operating system (NOS) and installation and
provisioning scripts used to deploy Cumulus Linux and NetQ software. A
command line interface (CLI) simplifies the provisioning of these
assets. IPM is installed by default with NetQ 1.4 and later. It is
disabled by default during NetQ installation and requires minor
configuration and activation to enable the software.

NetQ IPM is supported on:

  - Cumulus Linux version 3.6.2 and later.
  - Cumulus Linux version 3.6.1 if static mapping is used between a MAC
    address and a Network Operating System or provisioning script.

{{%notice note%}}

NetQ has [early access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878-Early-Access-Features-Defined) features that provide advanced access to new functionality before it
becomes generally available. The NetQ IPM application is introduced as an early access feature with
version 1.4.0.

{{%/notice%}}
