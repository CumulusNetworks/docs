---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

{{<product>}} {{<version>}} eases your customers deployment and maintenance activities for their data center networks with new configuration, performance, and security features and improvements.

<!-- vale off -->
## What's New in NetQ 4.0.1
<!-- vale on -->
NetQ 4.0.1 is a maintenance release that contains {{<link title="NVIDIA Cumulus NetQ 4.0 Release Notes" text="several bug fixes">}} and one new feature:

- Support for Cumulus Linux 4.4.

<!-- vale off -->
## What's New in NetQ 4.0.0
<!-- vale on -->

NetQ 4.0.0 includes the following new features and improvements:

- Collect What Just Happened event data using {{<link title="Configure and Monitor What Just Happened#collect-wjh-data-using-gnmi" text="gNMI">}} (gPRC network management interface) and export it to your gNMI client or keep it within NetQ.
- NetQ now monitors the SONiC operating system. Support includes traces, validations, snapshots, events, service visibility, lifecycle management and What Just Happened. This is an early access feature.
- {{<link url="Monitor-the-RoCE-Service" text="RoCE">}} (RDMA over Converged Ethernet) in Cumulus Linux now monitored.
- Improvements to the {{<link url="Validate-Operations" text="validation flow">}}.
- General user interface improvements.
- License checks <!-- vale off -->have been removed<!-- vale on --> from network health and the CLI.
- You can {{<link title="Manage the NetQ UI#rename-a-premises" text="rename premises">}}.
- The {{<link title="Integrate NetQ with Grafana" text="Grafana plugin">}} has new endpoints for:
  - Cloud: *plugin.prod.netq.cumulusnetworks.com*
  - On-premises: *\<hostname-or-ipaddr-of-netq-appl-or-vm\>/plugin*

## Upgrade Paths

You can upgrade NetQ versions 3.0.0 and later directly to version 4.0.0. Upgrades from NetQ 2.4.x and earlier require a fresh installation.

## Additional Information

For information regarding bug fixes and known issues present in this release, refer to the {{<link title="NVIDIA Cumulus NetQ 4.0 Release Notes" text="release notes">}}.
