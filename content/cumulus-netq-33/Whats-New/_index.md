---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
cascade:
    product: Cumulus NetQ
    version: "3.3"
    imgData: cumulus-netq
    siteSlug: cumulus-netq
---
NVIDIA NetQ {{<version>}} eases your customers deployment and maintenance activities for their data center networks with new configuration, performance, and security features and improvements.

## What's New in NetQ 3.3.0

NetQ 3.3.0 includes the following new features and improvements:

- Multi-site for the on-premises deployment: On-prem customer can now manage multiple sites from a single console, same as cloud
- Authentication and authorization with SAML and OAuth for the NetQ cloud administrator
- Redesigned NetQ UI topology view enables repositioning of switches and provides more detail about each switch and its performance
- Monitor MAC address movement over time for security and visibility
- Sort and export very large tables in NetQ UI
- User-defined threshold support for WJH (What Just Happened) events
- WJH filtering based on type, drop reason, or event severity
- Network snapshot comparison detail view now shows updated items in addition to the added and removed items
- Grafana 7.x support
- Configuration file restore during upgrade from Cumulus Linux 3.x to 4.x
- LLDP parameter specification in network templates

As an early access feature, NetQ 3.3.0 also expanded life cycle management (LCM) template-based switch configuration to include:

- VLANs
- MLAG
- IP address assignment
- Bond, subinterface, SVI, and port interface profiles
- Bond, subinterface, SVI, and port interfaces

## Upgrade Paths

You can upgrade NetQ versions 2.4.x through 3.2.x directly to version 3.3.0:

- NetQ 2.4.x to NetQ 3.3.0
- NetQ 3.0.0 to NetQ 3.3.0
- NetQ 3.1.x to NetQ 3.3.0
- NetQ 3.2.x to NetQ 3.3.0

Upgrades from NetQ 2.3.x and earlier require a fresh installation.

## Additional Information

For information regarding bug fixes and known issues present in this release, refer to the {{<link title="NVIDIA NetQ 3.3 Release Notes" text="release notes">}}.
