---
title: Access Data with Cards
author: NVIDIA
weight: 140
toc: 4
---

<!-- vale off -->
Cards present information about your network for monitoring and troubleshooting; each card describes a particular aspect of the network. Cards are collected onto a {{<link title="Focus Your Monitoring Using Workbenches" text="workbench">}} where all data relevant to a task or set of tasks is visible. You can add and remove cards from a workbench, increase or decrease their sizes, change the time period of the data shown on a card, and make copies of cards to show different levels of data at the same time.
<!-- vale on -->

## Card Sizes

Cards are available in multiple sizes, from small to full screen. The level of the content on a card varies with the size of the card, with the highest level of information on the smallest card to the most detailed information on the full-screen card.

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
<li>Enable quick actions, run a validation or trace for example</li>
</ul></td>
<td><ul>
<li>View key performance parameters or statistics</li>
<li>Perform an action</li>
<li>Look for potential issues</li>
</ul></td>
<td><ul>
<li>View detailed performance and statistics</li>
<li>Perform actions</li>
<li>Compare and review related information</li>
</ul></td>
<td><ul>
<li>View all attributes for given network aspect</li>
<li>Free-form data analysis and visualization</li>
<li>Export data to third-party tools</li>
</ul></td>
</tr>
</tbody>
</table>

### Small Cards

Small cards provide an overview of the performance or statistical value of a given aspect of your network. They typically include an icon to identify the aspect being monitored, summary performance or statistics in the form of a graph or counts, and an indication of any related events.

{{<figure src="/images/netq/access-data-small-group-230.png" alt="a row of small cards" width="700">}}

### Medium Cards

Medium cards provide the key measurements for a given aspect of your network. They include the same content as the small cards with additional, relevant information, such as related events or components.

{{<figure src="/images/netq/access-data-medium-group-230.png" alt="a row of medium cards" width="700">}}

### Large Cards

Large cards provide detailed information for monitoring specific components or functions of a given aspect of your network. This granular view can aid in isolating and resolving existing issues or preventing potential issues. These cards frequently display statistics or graphs that help visualize data.

{{<figure src="/images/netq/card-inventory-switches-lg-400.png" alt="a large inventory card displaying information about switches" width="600">}}

### Full-Screen Cards

Full-screen cards show all available data about an aspect of your network. They typically display data in a tabular view that can be filtered and sorted. When relevant, they also display visualizations of that data.

{{<figure src="/images/netq/card-inventory-switch-fs-400.png" alt="a full-screen inventory card displaying detailed information about switches in a table." width="700">}}

## Card Interactions

Each card focuses on a particular aspect of your network. They include:

- **Validation summary**: networkwide view of network health
- **Events**: information about all error and info events in the system
- **What Just Happened**: information about network issues and packet drops 
- **Device groups**: information about the distribution of device components
- **Inventory|Devices**: information about all switches and hosts in the network
- **Inventory|Switches**: information about the components on a given switch
- **Inventory|DPU**: information about data processing units
- **Inventory|Hosts**: information about hosts
- **Trace request**: find available paths between two devices in the network fabric

There are five additional network services cards for session monitoring, including **BGP**, **MLAG**, **EVPN**, **OSPF**, and **LLDP**.
### Add Cards to Your Workbench

Follow the steps in this section to add cards to your workbench. To add individual switch cards, refer to {{<link url="#add-switch-cards-to-your-workbench" text="Add Switch Cards to Your Workbench">}}.

To add one or more cards:

1. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> in the header.

2. Locate the card you want to add to your workbench. Use the categories in the side navigation or **Search** to help narrow down your options.

3. Click on each card you want to add to your workbench.

4. When you have selected all of the cards you want to add to your workbench, you can confirm which cards have been selected by clicking the **Cards Selected** link. Modify your selection as needed.

      {{<figure src="/images/netq/add-card-confirm-selection-300.png" alt="three selected card to be added to a workbench" width="700">}}

5. Click **Open Cards** to add the selected cards, or **Cancel** to return to your workbench without adding any cards.

The cards are placed at the end of the set of cards currently on the workbench. You might need to scroll down to see them. You can drag and drop the cards on the workbench to rearrange them.

### Add Switch Cards to Your Workbench

You can add switch cards to a workbench through the Switches icon on the header or by searching for it through Global Search.

To add a switch card using the icon:

1.  Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/>, then select **Open a device card**.

2. Begin entering the hostname of the switch you want to monitor.

3. Select the device from the suggestions that appear.

      {{<figure src="/images/netq/open-switch-card-suggest-400.png" width="250">}}

      {{<notice tip>}}
If you attempt to enter a hostname that is unknown to NetQ, a red border appears around the entry field and you are unable to select <strong>Add</strong>. Try checking for spelling errors. If you feel your entry is valid, but not an available choice, consult with your network administrator.
      {{</notice>}}

4. Click **Add** to add the switch card to your workbench, or **Cancel** to return to your workbench without adding the switch card.

To open the switch card by searching:

1. Click in **Global Search**.

2. Begin typing the name of a switch.

    {{<figure src="/images/netq/add-switch-card-thru-search-300.png" width="300">}}

3. Select it from the options that appear.

### Remove Cards from Your Workbench

To remove all the cards from your workbench, click the Clear icon in the header. To remove an individual card: 

1. Hover over the card you want to remove.
2. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18"/> (*More Actions* menu).
3. Click **Remove**.

    {{<figure src="/images/netq/remove-card-222.png" alt="" width="100">}}

The card is removed from the workbench, but not from the application.

### Change the Time Period for the Card Data

All cards have a default time period for the data shown on the card, typically the last 24 hours. You can change the time period to view the data during a different time range to aid analysis of previous or existing issues.

To change the time period for a card:

1. Hover over the card and select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/> in the header.

3. Select a time period from the dropdown list.

    {{<figure src="/images/netq/time-picker-popup-222.png" alt="" width="200">}}

{{<notice tip>}}
Changing the time period in this manner only changes the time period for the given card.
{{</notice>}}

### Change the Size of the Card

To change the card size:

1. Hover over the card.
2. Hover over the size picker and move the cursor to the right or left until the desired size option is highlighted.

    {{<figure src="/images/netq/card-size-picker-222.png" alt="" width="200" >}}

    One-quarter width opens a small card. One-half width opens a medium card. Three-quarters width opens a large card. Full width opens a full-screen card.

3. Click the picker. The card changes to the selected size, and might move its location on the workbench.
### Table Settings

You can manipulate the tabular data displayed in a full-screen card by filtering and sorting the columns. To reposition the columns, drag and drop them using your mouse. You can also export the data presented in the table.

The following icons are common in the full-screen card view.

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

When there are numerous items in a table, NetQ loads up to 25 by default and provides the rest in additional table pages. Pagination is displayed under the table.

{{<figure src="/images/netq/table-pagination-320.png" width="400">}}
