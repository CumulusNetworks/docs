---
title: Manage Switches through Their Lifecycle
author: Cumulus Networks
weight: 620
subsection: true
toc: 1
---
{{<notice info>}}

Only administrative users can perform the tasks described in this topic.

{{</notice>}}

As an administrator, you want to manage the deployment of Cumulus Networks product software onto your network devices (servers, appliances, and switches) in the most efficient way and with the most information about the process as possible. With this release, NetQ expands its  lifecycle management (LCM) capabilities to support configuration management for Cumulus Linux switches.

Using the NetQ UI or CLI, lifecycle management enables you to:

- Manage Cumulus Linux and Cumulus NetQ images in a local repository
- Configure switch access credentials (required for installations and upgrades)
- Manage Cumulus Linux switches
- Create snapshots of the network state at various times
- Create Cumulus Linux switch configurations, with or without network templates
- Create Cumulus NetQ configuration profiles
- Upgrade Cumulus NetQ (Agents and CLI) on Cumulus Linux switches with Cumulus NetQ Agents version 2.4.x or later
- Install or upgrade Cumulus NetQ (Agents and CLI) on Cumulus Linux switches with or without Cumulus NetQ Agents; all in a single job
- Upgrade Cumulus Linux on switches with Cumulus NetQ Agents version 2.4.x or later (includes upgrade of NetQ to 3.x)
- View a result history of upgrade attempts

{{<notice note>}}

This feature is fully enabled for on-premises deployments and fully disabled for cloud deployments. Contact your local Cumulus Networks sales representative or {{<exlink url="https://support.mellanox.com/s/" text="submit a support ticket">}} to activate LCM on cloud deployments.

{{</notice>}}

## Access Lifecycle Management Features in the NetQ UI

To manage the various lifecycle management features from any workbench, click {{<img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18">}} (Switches) in the workbench header, then select **Manage switches**.

The first time you open the Manage Switch Assets view, it provides a summary card for switch inventory, uploaded Cumulus Linux images, uploaded NetQ images, NetQ configuration profiles, and switch access settings. Additional cards appear after that based on your activity.

{{<figure src="/images/netq/lcm-dashboard-320.png" width="700">}}

{{<notice tip>}}

You can also access this view by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and selecting <strong>Manage Switches</strong> from the <strong>Admin</strong> section.

{{</notice>}}

## NetQ CLI Lifecycle Management Commands Summary

The NetQ CLI provides a number of `netq lcm` commands to perform the various LCM capabilities. The syntax of these commands is:

```
netq lcm upgrade name <text-job-name> cl-version <text-cumulus-linux-version> netq-version <text-netq-version> hostnames <text-switch-hostnames> [run-restore-on-failure] [run-before-after]
netq lcm add credentials username <text-switch-username> (password <text-switch-password> | ssh-key <text-ssh-key>)
netq lcm add role (superspine | spine | leaf | exit) switches <text-switch-hostnames>
netq lcm del credentials
netq lcm show credentials [json]
netq lcm show switches [version <text-cumulus-linux-version>] [json]
netq lcm show status <text-lcm-job-id> [json]
netq lcm add cl-image <text-image-path>
netq lcm add netq-image <text-image-path>
netq lcm del image <text-image-id>
netq lcm show images [<text-image-id>] [json]
netq lcm show upgrade-jobs [json]
netq [<hostname>] show events [level info | level error | level warning | level critical | level debug] type lcm [between <text-time> and <text-endtime>] [json]
```
