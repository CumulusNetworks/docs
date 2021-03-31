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

## What's New in NetQ 3.3.1

NetQ 3.3.1 is a maintenance release that contains bug fixes. A new {{<link url="NetQ-CLI-Reference">}} manual has also been published.

## What's New in NetQ 3.3.0

NetQ 3.3.0 includes the following new features and improvements:

- {{<link title="Install NetQ" text="Multi-site for the on-premises deployment">}}: On-prem customer can now manage multiple sites from a single console, same as cloud
- Authentication and authorization with {{<link title="Manage the NetQ UI/#integrate-with-your-microsoft-azure-or-google-cloud-for-sso" text="SAML and OAuth">}} for the NetQ cloud administrator
- Redesigned NetQ UI {{<link title="Monitor Using Topology View" text="topology view">}} enables repositioning of switches and provides more detail about each switch and its performance
- Monitor {{<link title="Monitor MAC Addresses/#view-the-history-of-a-mac-address" text="MAC address movement">}} over time for security and visibility
- Sort and export very large tables in NetQ UI
- User-defined threshold support for WJH (What Just Happened) events
- {{<link title="Configure and Monitor What Just Happened/#configure-filters" text="WJH filtering">}} based on type, drop reason, or event severity
- {{<link title="Manage Network Snapshots/#compare-network-snapshots" text="Network snapshot comparison">}} detail view now shows updated items in addition to the added and removed items
- {{<link title="Integrate NetQ with Grafana" text="Grafana 7.x">}} support
- Configuration file restore during upgrade from Cumulus Linux 3.x to 4.x
- {{<link title="Manage Switch Configurations/#create-network-templates" text="LLDP">}} parameter specification in network templates

As an early access feature, NetQ 3.3.0 also expanded life cycle management (LCM) template-based {{<link title="Manage Switch Configurations" text="switch configuration">}} to include:

- VLANs
- MLAG
- IP address assignment
- Bond, subinterface, SVI, and port interface profiles
- Bond, subinterface, SVI, and port interfaces

## Upgrade Paths

You can upgrade NetQ versions 2.4.x through 3.3.0 directly to version 3.3.1:

- NetQ 2.4.x to NetQ 3.3.1
- NetQ 3.0.0 to NetQ 3.3.1
- NetQ 3.1.x to NetQ 3.3.1
- NetQ 3.2.x to NetQ 3.3.1
- NetQ 3.3.0 to NetQ 3.3.1

Upgrades from NetQ 2.3.x and earlier require a fresh installation.

## Additional Information

For information regarding bug fixes and known issues present in this release, refer to the {{<link title="NVIDIA NetQ 3.3 Release Notes" text="release notes">}}.
