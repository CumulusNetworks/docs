---
title: Access Data with Cards
author: NVIDIA
weight: 140
toc: 4
---

Cards present information about your network for monitoring and troubleshooting; each card describes a particular aspect of the network. Cards are collected onto a {{<link title="Focus Your Monitoring Using Workbenches" text="workbench">}} where all data relevant to a task or set of tasks is visible. You can add and remove cards from a workbench, increase or decrease their sizes, change the time period of the data shown on a card, and make copies of cards to show different levels of data at the same time.

## Available Cards

Each card focuses on a particular aspect of your network. They include:

- **Validation summary**: overview of your network's health
- **Events**: system anomalies and threshold-crossing events
- **What Just Happened**: network issues and packet drops 
- **Device groups**: distribution of device components
- **Trace request**: discovery workflow for paths between two devices in the network fabric
- **MAC move commentary**: info about changes to a MAC address on a specific VLAN
- Network services cards: **BGP**, **MLAG**, **EVPN**, **OSPF**, and **LLDP**
- Inventory cards: **Devices**, **Switches**, **DPUs**, **NICs**, and **Hosts**

## Card Sizes

Cards are available in 4 sizes. The granularity of the content on a card varies with the size of the card, with the highest level of information on the smallest card to the most detailed information on the full-screen card.

### Card Size Summary

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
</colgroup>
<tbody>
<tr class="odd">
<th>Card Size</th>
<th>Small</th>
<th>Medium</th>
<th>Large</th>
<th>Full Screen</th>
</tr>
<tr class="even">
<th>Primary Purpose</th>
<td><ul>
<li>Quick view of status, typically at the level of good or bad</li>
</ul></td>
<td><ul>
<li>View key performance parameters or statistics</li>
<li>Perform quick actions</li>
<li>Monitor for potential issues</li>
</ul></td>
<td><ul>
<li>View detailed performance and statistics</li>
<li>Perform actions</li>
<li>Compare and review related information</li>
</ul></td>
<td><ul>
<li>View all attributes for given network aspect</li>
<li>Analyze and visualize detailed data</li>
<li>Export and filter data</li>
</ul></td>
</tr>
</tbody>
</table>

## Card Actions
### Add Cards to Your Workbench

1. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card** in the header.

2. Select the card(s) you want to add to your workbench.

3. When you have selected the cards you want to add to your workbench, select **Open cards**.

The cards are placed at the end of the set of cards currently on the workbench. You might need to scroll down to see them. Drag and drop the cards on the workbench to rearrange them.

### Add Switch Cards to Your Workbench

You can add switch cards to a workbench by selecting {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in the header or by searching for it in the Global Search field. To add a switch card from the header:

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices**, then select **Open a device card**.

2. Select the device from the suggestions that appear:

      {{<figure src="/images/netq/open-device-card-450.png" alt="dropdown displaying switches" width="250">}}

3. Choose the card's size, then select **Add**.

### Remove Cards from Your Workbench

To remove all the cards from your workbench, click the **Clear** icon in the header. To remove an individual card: 

1. Hover over the card you want to remove.
2. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18"/> (*More Actions* menu).
3. Select **Remove**.

    {{<figure src="/images/netq/remove-this-card.png" alt="" width="140">}}

The card is removed from the workbench, but not from the application.

### Change the Size of the Card

1. Hover over the top portion of the card until you see a rectangular box divided into four segments.

2. Move your cursor over the box until the desired size option is highlighted.

    {{<figure src="/images/netq/size-picker-450.png" alt="" width="200" >}}

    One-quarter width opens a small card. One-half width opens a medium card. Three-quarters width opens a large card. Full width opens a full-screen card.

3. Select the size. When the card changes to the selected size, it might move to a different area on the workbench.

### Change the Time Period for the Card Data

All cards have a default time period for the data shown on the card, typically the last 24 hours. You can change the time period to view the data during a different time range to aid analysis of previous or existing issues.

To change the time period for a card:

1. Hover over the top portion of the card and select the clock icon <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

3. Select a time period from the dropdown list.

    {{<figure src="/images/netq/time-clock-450.png" alt="time options" width="300">}}

{{<notice tip>}}
Changing the time period in this manner only changes the time period for the given card.
{{</notice>}}


### Table Settings

You can manipulate the tabular data displayed in a full-screen card by filtering and sorting the columns. Hover over the column header and select it to sort the column. The data is sorted in ascending or descending order: A-Z, Z-A, 1-n, or n-1. The number of rows that can be sorted via the UI is limited to 10,000. To reposition the columns, drag and drop them using your mouse. 

Select <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> **Export** to download and export the tabular data. You can sort and filter tables that exceed 10,000 rows by exporting the data as a CSV file and opening it in a spreadsheet program.

The following icons are common in the full-screen card view:

| Icon | Action | Description |
| ---- | ---- | ---- |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> | Select All | Selects all items in the list. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/subtract-circle.svg" height="18" width="18"/> | Clear All | Clears all existing selections in the list. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18"/> | Add Item | Adds item to the list. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18"/> | Edit | Edits the selected item. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/> | Delete | Removes the selected items. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18"/> | Filter | Filters the list using available parameters. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18"/>, {{<img src="/images/netq/netq-mgmt-delete-keys-icon.png" height="18" width="18" >}} | Generate/Delete AuthKeys | Creates or removes NetQ CLI authorization keys. |
| <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> | Open Cards | Opens the corresponding validation or trace card(s). |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18"/> | Assign role | Opens role assignment options for switches. |
| <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> | Export | Exports selected data into either a .csv or JSON-formatted file. |

When there are many items in a table, NetQ loads up to 25 rows by default and provides the rest in additional table pages, accessible through the pagination controls. Pagination is displayed under the table.

{{<figure src="/images/netq/pagination-controls.png" alt="" width="400">}}
