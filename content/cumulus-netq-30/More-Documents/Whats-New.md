---
title: What's New
author: Cumulus Networks
weight: 630
---

Cumulus NetQ 2.4 extends its visibility into network-wide and device issues, and makes deployment easier. Moving to this release requires a fresh installation; however, you can backup and restore data from prior versions. You can upgrade from NetQ 2.4.0 to 2.4.1.

**Cumulus NetQ 2.4.1** is a maintenance release that includes the following new features and improvements that enable you to:

- {{<link url="Lifecycle-Management/#manage-network-snapshots" text="Select multiple network snapshots">}} for viewing or deletion
- Manage table data in full-screen NetQ UI cards using {{<link url="Access-Data-with-Cards/#table-settings" text="pagination and a modified filtering mechanism">}}
- Manage {{<link url="Application-Management/#manage-threshold-crossing-rules" text="threshold crossing alerts (TCAs)">}} through NetQ UI
- Restore master server using Admin UI
- Add more than two worker nodes to your server cluster using {{<link title="Install NetQ Using the Admin UI" text="Admin UI">}}
- Specify a proxy during NetQ Platform or Appliance provisioning
- Set a {{<link url="Manage-NetQ-Agents/#modify-the-configuration-of-the-netq-agent-on-a-node" text="CPU usage threshold">}} for NetQ Agents
- Track {{<link url="Monitor-Data-Link-Layer-Devices-and-Protocols/#view-the-history-of-a-mac-address" text="MAC address history">}} in the network using `netq show mac-history` command

**Cumulus NetQ 2.4.0** includes the following new features and improvements:

- NetQ server clustering that provides high availability and 24x7 manageability
- A push-button NetQ installation UI that makes the deployment of NetQ easy
- What Just Happened (WJH) that provides visibility into network problems with real-time telemetry data for Mellanox switches
- Threshold Crossing Alerts (TCAs) that allow detection and prevention of network failures for selected interface, utilization, and sensor events
- Fast lookup memory table monitoring that enables detection of critical resource depletion
- Early detection of the hardware issues by monitoring the sensors on Mellanox SN2700 and SN2410 platforms
- Show or hide events on the topology diagram
- Miscellaneous improvements in card displays in NetQ UI
- Ubuntu 18.04 deployed as base OS for NetQ appliances

For further information regarding new features, improvements, bug fixes, and known issues present in this release, refer to the {{<link title="Cumulus NetQ 2.4 Release Notes" text="release notes">}}.
