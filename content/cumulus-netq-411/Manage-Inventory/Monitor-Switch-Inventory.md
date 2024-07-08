---
title: Switch Inventory
author: NVIDIA
weight: 740
toc: 4
---
With the NetQ UI and NetQ CLI, you can monitor your inventory of switches across the network or individually. A user can view operating system, motherboard, ASIC, microprocessor, disk, memory, fan, and power supply information.

You can access {{<link title="Switches" text="switch performance data">}} for a given switch in the UI by right-clicking a switch and opening the dashboard in a new tab.  

## Switch Inventory Commands

- To view a comprehensive list of inventory components, run {{<link title="show/#netq-show-inventory" text="netq show inventory">}}. 
- To view Cumulus Linux OS versions supported on your switches, run {{<link title="show/#netq-show-cl-manifest" text="netq show cl-manifest">}}.
- To view all installed software packages on your switches, run {{<link title="show/#netq-show-cl-pkg-info" text="netq show cl-pkg-info">}}.
- To view recommended software package information for a switch, run {{<link title="show/#netq-show-recommended-pkg-version" text="netq show recommended-pkg-version">}}.
- To view a list of services, run {{<link title="show/#netq-show-services" text="netq show services">}}.
## View Switch Inventory in the UI

To view the hardware and software component inventory for switches running NetQ in your network, search for the "Inventory | Switches" card in the global search field. The card displays the total number of switches in your network, divided into the number of fresh and rotten switches.

{{<img src="/images/netq/switch-med-490.png" alt="medium switch card displaying 513 fresh switches and 13 rotten switches" width="200">}}

## View Distribution and Component Counts

Open the large Inventory/Switches card to display more granular information about software and hardware distribution. By default, the card displays data for fresh switches. Select **Rotten switches** from the dropdown to display information for switches that are in a down state. Hover over the top of the card and select a category to restrict the view to ASICs, platform, or software.

{{<img src="/images/netq/switch-inventory-large-update.png" alt="switch software and hardware information" width="600">}}

Expand the Inventory/Switches card to full-screen to view, filter or export information about ASICs, motherboards, CPUs, memory, disks, and operating system.

{{<img src="/images/netq/inventory-switches-411.png" alt="" width="1200">}}

You can right-click the hostname of a given switch to open a monitoring dashboard for that switch in a new tab.
## Decommission a Switch

Decommissioning a switch or host removes information about the device from the NetQ database. When the NetQ Agent restarts at a later date, it sends a connection request back to the database, so NetQ can monitor the switch or host again.

{{<tabs "TabID64" >}}

{{<tab "NetQ UI" >}}

1. Locate the Inventory/Switches card on your workbench and expand it to full-screen.

2. Select the switches to decommission, then select **Decommission device** above the table.

    If you attempt to decommission a switch that is assigned a default, unmodified access profile, the process will fail. {{<link title="Credentials and Profiles" text="Create a unique access profile">}} (or update the default with unique credentials), then {{<link title="Switch Management/#attach-a-profile-to-a-switch" text="attach the profile">}} to the switch you want to decommission.

4. Confirm the devices you want to decommission.

5. Wait for the decommission process to complete, then select **Done**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To decommission a switch or host:

1. On the given switch or host, stop and disable the NetQ Agent service:

    ```
    cumulus@switch:~$ sudo systemctl stop netq-agent
    cumulus@switch:~$ sudo systemctl disable netq-agent
    ```

2. On the NetQ appliance or VM, decommission the switch or host:

    ```
    cumulus@netq-appliance:~$ netq decommission <hostname-to-decommission>
    ```
{{</tab>}}

{{</tabs>}}
## Related Information

- {{<link title="Switches" text="Switch Monitoring">}}
- {{<link title="Switch Management" text="Switch Lifecycle Management">}}