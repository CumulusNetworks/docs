---
title: What's New in Cumulus NetQ 2.3
author: Cumulus Networks
weight: 300
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
siteSlug: cumulus-netq
---

Cumulus NetQ 2.3 improves your operational efficiency by providing LDAP integration to work in conjunction with your enterprise management strategies and network state and configuration comparisons to reduce network downtime from unexpected behaviors due to configuration changes or upgrades.

**Cumulus NetQ 2.3.1** includes bug fixes and the following new features and improvements:

*For on-premises and cloud solutions*

  - Added [topology view](../../Cumulus-NetQ-UI-User-Guide/Monitor-Using-Topology-View/) to NetQ UI for on-premises deployments (cloud  deployment was available in 2.3.0)
  - Added monitoring for BTRFS utilization through full screen [Switches](../../Cumulus-NetQ-UI-User-Guide/Monitor-Devices/Monitor-Switches/#view-disk-storage-after-btrfs-allocation) card in UI and [`netq show cl-btrfs-info`](../../Cumulus-NetQ-CLI-User-Guide/Monitor-Switch-Hardware-and-Software/#view-disk-storage-utilization-after-btrfs-allocation) CLI command
  - Added monitoring for SSD utilization for type 3ME3 drives through full  screen [Switches](../../Cumulus-NetQ-UI-User-Guide/Monitor-Devices/Monitor-Switches/#view-ssd-utilization) card in UI and [`netq show cl-ssd-util`](../../Cumulus-NetQ-CLI-User-Guide/Monitor-Switch-Hardware-and-Software/#view-ssd-utilization) CLI command
  - Added monitoring of software package versions through full screen [Switches](../../Cumulus-NetQ-UI-User-Guide/Monitor-Devices/Monitor-Switches/#view-all-software-packages-on-a-switch) card in UI and [`netq show cl-pkg-info`](../../Cumulus-NetQ-CLI-User-Guide/Monitor-Switch-Hardware-and-Software/#view-all-software-packages-installed-on-switches) CLI command
  - Added [events](../../Cumulus-NetQ-UI-User-Guide/Monitor-Network-Performance/Monitor-Events/#events-reference) for BTRFS and SSD utilization, software package versions,  and NetQ agents
  - Added [auto-refresh](../../Cumulus-NetQ-UI-User-Guide/NetQ-User-Interface-Overview/Focus-Your-Montoring-Using-Workbenches/#manage-auto-refresh-for-your-workbenches) for workbenches in UI, and ability to manage its  settings
  - Updated workbench selection [menu](../../Cumulus-NetQ-UI-User-Guide/NetQ-User-Interface-Overview/Focus-Your-Montoring-Using-Workbenches/#open-an-existing-workbench) in UI
  - Updated NetQ Agent installation instructions to include configuration  through [YML file](../../Cumulus-NetQ-Deployment-Guide/Install-NetQ/Install-NetQ-Agents-and-CLI-on-Switches/#configure-netq-agents-using-a-configuration-file)

*For on-premises solution only*

- Added support for host proxy on NetQ Server or Appliance
- Updated [LDAP integration] (../../Cumulus-NetQ-Integration-Guide/Integrate-NetQ-with-Your-LDAP-Server/) configuration options

*Early Access Features*

- Added [`netq show mac-history`](../../Cumulus-NetQ-CLI-User-Guide/CLI-Early-Access-Features/) command to track where MAC addresses have resided
- Expanded [`netq check`](../../Cumulus-NetQ-CLI-User-Guide/CLI-Early-Access-Features/) validation commands to increase visibility and control of tests performed

**Cumulus NetQ 2.3.0** includes the following new features and improvements:

*For on-premises and cloud solutions*

  - Graphical User Interface (UI)
    - Added lifecycle management feature that enables a user to compare [snapshots](../../Cumulus-NetQ-UI-User-Guide/NetQ-Configuration-Management/Lifecycle-Management/) of the live network state and configuration before and after changes are made
    - Added [disk utilization](../../Cumulus-NetQ-UI-User-Guide/Monitor-Devices/Monitor-Switches/#view-current-resource-utilization-for-a-switch) to large Switches card
    - Added [interface statistics](../../Cumulus-NetQ-UI-User-Guide/Monitor-Devices/Monitor-Switches/#view-interface-statistics-for-a-switch) and utilization to large Switches card
    - Added [validation events](../../Cumulus-NetQ-UI-User-Guide/Monitor-Network-Performance/Monitor-Events/#events-reference)
    - Changed references of CLAG to MLAG
  - Integrations
    - Added optional integration with open source [Grafana](../../Cumulus-NetQ-Integration-Guide/Integrate-with-Grafana/) analytics and monitoring tool
  - Command Line Interface (CLI)
    - Added `netq show platform` command to view NetQ software version running on device
    - Added [`netq show interface-utils`](../../Cumulus-NetQ-CLI-User-Guide/Monitor-Switch-Hardware-and-Software/#view-interface-statistics-and-utilization) command to view interface statistics, utilization, and port speed
    - Added `netq check cl-version` to validate the Cumulus Linux version running on all devices

*For cloud solution only*

  - Modified secure access process to use symmetric keys instead of asymmetric keys

*For on-premises solution only*

  - Added role-based access control (RBAC) that can be integrated with your LDAP server


For further information regarding new features, improvements, bug fixes, and known issues present in this release, refer to the [release notes](https://support.cumulusnetworks.com/hc/en-us/articles/360036416953).
