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
netq show inventory (brief | asic | board | cpu | disk | memory | license | os)
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

Add the Inventory/Switches card to your workbench to monitor the hardware and software component inventory on switches running NetQ in your network. To add this card to your workbench, select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card** > **Inventory** > **Inventory/Switches card** > **Open cards**. Select the dropdown to view additional inventory information.

{{<img src="/images/netq/inventory-switches-updated.png" width="200">}}&nbsp;&nbsp;&nbsp;&nbsp;{{<img src="/images/netq/inventory-switches-dropdown.png" width="200">}}

## View Distribution and Component Counts

Open the large Inventory/Switches card to display more granular information about software and hardware distribution. By default, the card displays data for fresh switches. Select **Rotten switches** from the dropdown to display information for switches that are in a down state. Hover over the top of the card and select a category to restrict the view to ASICs, platform, or software.

{{<figure src="/images/netq/switch-inventory-large-update.png" width="600">}}

Expand the Inventory/Switches card to full-screen to view, filter or export information about:

- ASICs
- Motherboards
- CPUs
- Disks
- Memory
- Operating system

{{<figure src="/images/netq/switch-inventory-full-460.png" alt="" width="1200">}}
## Related Information

- {{<link title="Switches" text="Switch Monitoring">}}
- {{<link title="Switch Management" text="Switch Lifecycle Management">}}