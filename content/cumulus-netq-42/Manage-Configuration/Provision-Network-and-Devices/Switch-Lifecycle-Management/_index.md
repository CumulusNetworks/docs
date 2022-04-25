---
title: Manage Switches through Their Lifecycle
author: NVIDIA
weight: 620
subsection: true
toc: 1
---
{{<notice info>}}

Only administrative users can perform the tasks described in this topic.

{{</notice>}}

As an administrator, you want to manage the deployment of NVIDIA product software onto your network devices (servers, appliances, and switches) in the most efficient way and with the most information about the process as possible.

Using the NetQ UI or CLI, lifecycle management enables you to:

- Manage Cumulus Linux and NetQ images in a local repository
- Configure switch access credentials (required for installations and upgrades)
- Manage Cumulus Linux switch inventory and roles
- Create snapshots of the network state at various times
- Create Cumulus Linux switch configurations, with or without network templates
- Create NetQ configuration profiles
- Upgrade NetQ (Agents and CLI) on Cumulus Linux switches running NetQ Agents
- Install or upgrade NetQ (Agents and CLI) on Cumulus Linux switches
- View a result history of upgrade attempts

{{<notice note>}}

This feature is fully enabled for on-premises deployments and fully disabled for cloud deployments. Contact your local NVIDIA sales representative or {{<exlink url="https://support.mellanox.com/s/" text="submit a support ticket">}} to activate LCM on cloud deployments.

{{</notice>}}

## Access Lifecycle Management Features

To manage the various lifecycle management features using the NetQ UI, open the Manage Switch Assets page in one of the following ways:

- Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18">}}, then select **Manage Switches**
- Click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" width="18" height="18">}} in a workbench header
- Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} (Devices) in a workbench header, then select **Manage switches**

The Manage Switch Assets view provides access to switch management, image management, and configuration management features as well as job history. Each tab provides cards that let the administrator manage the relevant aspect of switch assets.

{{<figure src="/images/netq/lcm-dashboard-330.png" width="700">}}

To manage the various lifecycle management features using the NetQ CLI, use the `netq lcm` command set.

## LCM Summary

This table summarizes the UI cards and CLI commands available for the LCM feature.

| <div style="width:30px">Function </div> | <div style="width:220px">Description</div> | <div style="width:220px">NetQ UI Cards</div> | <div style="width:220px">NetQ CLI Commands</div> |
| --- | --- | --- | --- |
| Switch Management | Discover switches, view switch inventory, assign roles, set user access credentials, perform software installation and upgrade networkwide | <ul><li>Switches</li><li>Access</li></ul> | <ul><li>netq lcm show switches</li><li>netq lcm add role</li><li>netq lcm upgrade</li><li>netq lcm add/del/show credentials</li><li>netq lcm discover</li></ul> |
| Image Management | View, add, and remove images for software installation and upgrade | <ul><li>Cumulus Linux Images</li><li>NetQ Images</li></ul> | <ul><li>netq lcm add/del/show netq-image</li><li>netq lcm add/del/show cl-images</li><li>netq lcm add/show default-version</li></ul> |
| Configuration Management | Set up templates for software installation and upgrade, configure and assign switch settings networkwide | <ul><li>NetQ Configurations</li><li>Network Templates</li><li>Switch Configurations</li></ul> | <ul><li>netq lcm show netq-config</li></ul> |
| Job History | View the results of installation, upgrade, and configuration assignment jobs | <ul><li>CL Upgrade History</li><li>NetQ Install and Upgrade History</li><li>Config Assignment History</li></ul> | <ul><li>netq lcm show status</li><li>netq lcm show upgrade-jobs</li></ul> |
