---
title: Manage Inventory
author: Cumulus Networks
weight: 600
toc: 3
---
This topic describes how to use the Cumulus NetQ UI and CLI to monitor your inventory from network-wide and device-specific perspectives.

You can monitor all of the hardware and software components installed and running on the switches and hosts across the entire network. This is extremely useful for understanding the dependence on various vendors and versions, when planning upgrades or the scope of any other required changes.

## Access Network Inventory Data

The Cumulus NetQ UI provides two cards for monitoring network-wide inventory information. The Inventory | Devices card provides varying degrees of information about hardware and software on all switches and hosts running NetQ. The Inventory | Switches card provides varying degrees of information about the hardware and software on all switches running NetQ. Access these cards from the Cumulus Workbench, or add them to your own workbench by clicking <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Add card) > **Inventory**  > Inventory | Devices card  and/or Inventory | Switches > **Open Cards**.

{{<img src="/images/netq/inventory-devices-medium-240.png" width="200">}}&mdash;{{<figure src="/images/netq/inventory-switches-medium-240.png" width="200">}}

The second location is through tabular views for each network element. These are helpful when you want to see all data for a particular element in your network, or you want to export a list view. However, the tabular views only provide the current status; you cannot change the time period of the views, or graph the data within the UI.

Access these tables through the Main Menu (<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/>), under the **Network** heading.

{{<figure src="/images/netq/main-menu-admin-network-selected-310.png" width="700">}}

{{<notice tip>}}
If you do not have administrative rights, the Admin menu options are not available to you.
{{</notice>}}

Tables can be manipulated using the settings above the tables, shown here and described in {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.

{{<figure src="/images/netq/main-menu-ntwk-table-settings-241.png" width="100">}}

Pagination options are shown when there are more than 25 results.

The CLI provides detailed network inventory information through its `netq show inventory` command.

## Access Switch Inventory Data

The Cumulus NetQ UI provides the Inventory | Switches card for monitoring the hardware and software component inventory on switches running NetQ in your network. Access this card from the Cumulus Workbench, or add it to your own workbench by clicking <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Add card) > **Inventory**  > Inventory | Switches card > **Open Cards**.

The CLI provides detailed switch inventory information through its `netq <hostname> show inventory` command.

To view the network or device performance data, refer to {{<link title="Monitor Network and Device Performance">}}.
