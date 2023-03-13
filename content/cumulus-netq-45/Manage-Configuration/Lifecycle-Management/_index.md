---
title: Lifecycle Management
author: NVIDIA
weight: 610
toc: 3
---
{{<notice info>}}

Lifecycle management is enabled for on-premises deployments by default and disabled for cloud deployments by default. Contact your local NVIDIA sales representative or submit a support ticket to activate LCM on cloud deployments.

Only administrative users can perform the tasks described in this topic.

{{</notice>}}

Using the NetQ UI or CLI, lifecycle management (LCM) allows you to:

- {{<link title="NetQ and Network OS Images" text="Manage Cumulus Linux and NetQ images">}} in a local repository
- {{<link title="Credentials and Profiles" text="Configure switch access credentials and profiles">}} (required for installations and upgrades)
- {{<link title="Switch Management" text="Manage switch inventory and roles">}}
- Install or {{<link title="Upgrade NetQ Agent Using LCM" text="upgrade NetQ (Agents and CLI)">}} and {{<link title="Upgrade Cumulus Linux Using LCM" text="Cumulus Linux">}} on switches running Cumulus Linux
- {{<link title="Network Snapshots" text="Create snapshots">}} of the network state at various times
- {{<link title="Decommission Switches" text="Decommission switches">}}
- View a history of upgrade attempts

## Access Lifecycle Management in the UI

You can access the LCM dashboard in a few ways:

- Expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18">}} **Menu**, then select **Manage switches**
- Click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" width="18" height="18">}} **Upgrade** in a workbench header
- Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in a workbench header, then select **Manage switches**

{{<figure src="/images/netq/manage-switch-assets-450.png" alt="dashboard displaying switch management tab" width="700">}}

## Access Lifecycle Management with the CLI

Lifecycle management workflows use the `netq lcm` command set. Refer to the {{<link title="lcm" text="command line reference">}} for a comprehensive list of options and definitions.