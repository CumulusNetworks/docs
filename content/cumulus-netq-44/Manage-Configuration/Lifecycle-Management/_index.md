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

- Manage Cumulus Linux and NetQ images in a local repository
- Configure switch access credentials (required for installations and upgrades)
- Manage Cumulus Linux switch inventory and roles
- Create snapshots of the network state at various times
- Install or upgrade NetQ (Agents and CLI) on Cumulus Linux switches
- View a result history of upgrade attempts

## Access Lifecycle Management in the UI

To access LCM, open the Manage Switch Assets page in one of the following ways:

- Expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18">}} Menu, then select **Manage switches**
- Click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" width="18" height="18">}} Upgrade in a workbench header
- Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} Devices in a workbench header, then select **Manage switches**

The Manage Switch Assets view provides access to switch management, image management, NetQ Agent configurations, and job history.

{{<figure src="/images/netq/updated-lcm-dashboard.png" alt="dashboard displaying switch management tab" width="700">}}

## LCM Summary

To manage the various lifecycle management features using the NetQ CLI, use the `netq lcm` command set. The following table summarizes LCM's capabilities:

| <div style="width:30px">Function </div> | <div style="width:220px">Description</div> | <div style="width:220px">NetQ UI Cards</div> | <div style="width:220px">NetQ CLI Commands</div> |
| --- | --- | --- | --- |
| Switch Management | Discover switches, view switch inventory, assign roles, set user access credentials, perform software installation and upgrade networkwide | <ul><li>Switches</li><li>Access</li></ul> | <ul><li>`netq lcm show switches`</li><li>`netq lcm add role`</li><li>`netq lcm upgrade`</li><li>`netq lcm add/del/show credentials`</li><li>`netq lcm discover`</li></ul> |
| Image Management | View, add, and remove images for software installation and upgrade | <ul><li>Cumulus Linux Images</li><li>NetQ Images</li></ul> | <ul><li>`netq lcm add/del/show netq-image`</li><li>`netq lcm add/del/show cl-images`</li><li>`netq lcm add/show default-version`</li></ul> |
| Job History | View the results of installation, upgrade, and configuration assignment jobs | <ul><li>CL Upgrade History</li><li>NetQ Install and Upgrade History</li><li>Config Assignment History</li></ul> | <ul><li>`netq lcm show status`</li><li>`netq lcm show upgrade-jobs`</li></ul> |
