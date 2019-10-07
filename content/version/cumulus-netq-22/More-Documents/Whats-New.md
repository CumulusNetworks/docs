---
title: What's New in Cumulus NetQ 2.2
author: Cumulus Networks
weight: 300
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---

Cumulus NetQ is now available as a cloud service, making it even easier
to scale with your network growth. Just like Cumulus NetQ deployed in
your premises, real-time data collection and fabric-wide performance
analysis are available through the cloud service. New functionality has
also been added to the NetQ UI.

**Cumulus NetQ 2.2.2** includes bug fixes and the following new features and improvements:

*For on-premises and in-cloud*

- Command Line Interface (CLI)
   - Support of syslog for event notifications
   - Improved install procedure includes CLI update in NetQ upgrade process
- Graphical User Interface (UI)
   - Improved interaction for adding cards to workbenches
   - Modified alarm reporting on Events | Alarms cards to include only alarms occurring during the designated time period on the card

*For on-premises only*

- Simplified upgrade process for NetQ Appliance includes upgrade of netq-apps

*For in-cloud only*

- Command Line Interface (CLI)
   - Added CLI proxy to NetQ Cloud Appliance to remove internet access requirement when installing CLI on hosts and servers
   - Improved netq install opta interface command enables download and installation of cloud software in single step

**Cumulus NetQ 2.2.1** includes the following new features and improvements:

*For on-premises and in-cloud solutions*

- Command Line Interface (CLI)
   - Upgraded [Interface Statistics](../../Cumulus-NetQ-CLI-User-Guide/Monitor-Switch-Hardware-and-Software/#view-interface-statistics) from an early access feature to a generally available feature
   - Added ability to view [NetQ Agent status and inventory for NetQ server/appliance](../../Cumulus-NetQ-CLI-User-Guide/Manage-NetQ-Agents)
- Graphical User Interface (UI)
   - Added ability to save user workbenches
   - Added OSPF events
- Reorganized documentation
   - Modified installation and upgrade procedures in Deployment Guide
   - Created Integration Guide to collect all integration options together
   - Created More Documents topic to contain generic information about Cumulus Networks documents and this NetQ release
   - Format fixes

*For on-premises solutions only*

- Added NetQ data backup and restore procedure.

*For in-cloud solutions only*

- Command Line Interface (CLI)
   - Modified installation and upgrade commands
   - Added ability to store and retrieve authentication keys from a file

**Cumulus NetQ 2.2.0** includes the following new features and
improvements:

*For on-site and in-cloud solutions*

  - Graphical User Interface (UI)
      - Added ability to monitor and validate OSPF network protocol and
        services operation
      - Added ability to validate MTU, Sensors, VLAN and VXLAN protocols
      - Added events for MTU, OSPF, VLAN, and VXLAN
      - Added new standard user role, *user*, with reduced access
        permission compared to the administrative user
      - Added Prescriptive Topology Manager (PTM) events
  - Command Line Interface (CLI)
      - Included Interface Statistics as an early access feature

*For in-cloud solution only*

  - Released new Cumulus NetQ Cloud Appliance to speed deployment and
    get monitoring as quickly as possible
  - Added CLI support for installation and configuration of the Cumulus
    NetQ Cloud Appliance
  - Added support for multiple data centers

For further information regarding new features, improvements, bug fixes, and known issues present in this release, refer to the [release notes](https://support.cumulusnetworks.com/hc/en-us/articles/360025451374).
