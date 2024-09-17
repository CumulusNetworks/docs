---
title: Switch Inventory
author: NVIDIA
weight: 740
toc: 4
---
With the NetQ UI and NetQ CLI, you can monitor your inventory of switches across the network or individually. A user can view operating system, motherboard, ASIC, microprocessor, disk, memory, fan, and power supply information.

For switch performance information, refer to {{<link title="Switches" text="Switch Monitoring">}}.

## Switch Inventory Commands

Several forms of this command are available based on the inventory component you'd like to view. See the {{<link title="show/#netq-show-inventory" text="command line reference">}} for additional options, definitions, and examples.

```
netq show inventory (brief | asic | board | cpu | disk | memory | os)
```
To view Cumulus Linux OS versions supported on your switches, run {{<link title="show/#netq-show-cl-manifest" text="netq show cl-manifest">}}:

```
netq show cl-manifest
```
To view all installed software packages on your switches, run {{<link title="show/#netq-show-cl-pkg-info" text="netq show cl-pkg-info">}}:

```
netq show cl-pkg-info
```
To view recommended software package information for a switch, run {{<link title="show/#netq-show-recommended-pkg-version" text="netq show recommended-pkg-version">}}:

```
netq <hostname> show recommended-pkg-version
```

Cumulus Linux, SONiC, and NetQ run services to deliver the various features of these products. You can monitor their status using the {{<link title="show/#netq-show-services" text="netq show services">}} command:

```
netq show services
```

## View Switch Inventory in the UI

Add the Inventory/Switches card to your workbench to monitor the hardware and software component inventory on switches running NetQ in your network. To add this card to your workbench, select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card**&nbsp;<span aria-label="and then">></span> **Inventory**&nbsp;<span aria-label="and then">></span> **Inventory/Switches card**&nbsp;<span aria-label="and then">></span> **Open cards**. The card displays the total number of switches in your network, divided into the number of fresh and rotten switches.

{{<img src="/images/netq/switch-med-490.png" alt="medium switch card displaying 513 fresh switches and 13 rotten switches" width="200">}}

## View Distribution and Component Counts

Open the large Inventory/Switches card to display more granular information about software and hardware distribution. By default, the card displays data for fresh switches. Select **Rotten switches** from the dropdown to display information for switches that are in a down state. Hover over the top of the card and select a category to restrict the view to ASICs, platform, or software.

{{<img src="/images/netq/switch-inventory-large-update.png" alt="switch software and hardware information" width="600">}}

Expand the Inventory/Switches card to full-screen to view, filter or export information about ASICs, motherboards, CPUs, memory, disks, and operating system.

{{<img src="/images/netq/full-switch-inventory-490.png" alt="" width="1200">}}

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