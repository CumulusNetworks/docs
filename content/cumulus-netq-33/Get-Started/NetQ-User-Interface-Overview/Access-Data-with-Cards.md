---
title: Access Data with Cards
author: NVIDIA
weight: 140
toc: 4
---
Cards present information about your network for monitoring and troubleshooting. This is where you can expect to spend most of your time. Each card describes a particular aspect of the network. Cards are available in multiple sizes, from small to full screen. The level of the content on a card varies in accordance with the size of the card, with the highest level of information on the smallest card to the most detailed information on the full-screen card. Cards are collected onto a workbench where you see all of the data relevant to a task or set of tasks. You can add and remove cards from a workbench, move between cards and card sizes, change the time period of the data shown on a card, and make copies of cards to show different levels of data at the same time.

## Card Sizes

The various sizes of cards enables you to view your content at just the right level. For each aspect that you are monitoring there is typically a single card, that presents increasing amounts of data over its four sizes. For example, a snapshot of your total inventory may be sufficient, but to monitor the distribution of hardware vendors may requires a bit more space.

### Small Cards

Small cards are most effective at providing a quick view of the performance or statistical value of a given aspect of your network. They are commonly comprised of an icon to identify the aspect being monitored, summary performance or statistics in the form of a graph and/or counts, and often an indication of any related events. Other content items may be present. Some examples include a Devices Inventory card, a Switch Inventory card, an Alarm Events card, an Info Events card, and a Network Health card, as shown here:

{{<figure src="/images/netq/access-data-small-group-230.png" width="700">}}

### Medium Cards

Medium cards are most effective at providing the key measurements for a given aspect of your network. They are commonly comprised of an icon to identify the aspect being monitored, one or more key measurements that make up the overall performance. Often additional information is also included, such as related events or components. Some examples include a Devices Inventory card, a Switch Inventory card, an Alarm Events card, an Info Events card, and a Network Health card, as shown here. Compare these with their related small- and large-sized cards.

{{<figure src="/images/netq/access-data-medium-group-230.png" width="700">}}

### Large Cards

Large cards are most effective at providing the detailed information for monitoring specific components or functions of a given aspect of your network. These can aid in isolating and resolving existing issues or preventing potential issues. They are commonly comprised of detailed statistics and graphics. Some large cards also have tabs for additional detail about a given statistic or other related information. Some examples include a Devices Inventory card, an Alarm Events card, and a Network Health card, as shown here. Compare these with their related small- and medium-sized cards.

{{<figure src="/images/netq/access-data-large-group-300.png" width="500">}}

### Full-Screen Cards

Full-screen cards are most effective for viewing all available data about an aspect of your network all in one place. When you cannot find what you need in the small, medium, or large cards, it is likely on the full-screen card. Most full-screen cards display data in a grid, or table; however, some contain visualizations. Some examples include All Events card and All Switches card, as shown here.

{{<figure src="/images/netq/events-alarms-fullscr-allevents-tab.png" width="700">}}

{{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-230.png" width="700">}}

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

## Card Workflows

The UI provides a number of card workflows. Card workflows focus on a particular aspect of your network and are a linked set of each size card-a small card, a medium card, one or more large cards, and one or more full screen cards. The following card workflows are available:

- **Network Health**: networkwide view of network health
- **Devices|Switches**: health of a given switch
- **Inventory|Devices**: information about all switches and hosts in the network
- **Inventory|Switches**: information about the components on a given switch
- **Events|Alarms**: information about all critical severity events in the system
- **Events|Info**: information about all warning, info, and debug events in the system
- **Network Services**: information about the network services and sessions
- **Validation Request** (and Results): networkwide validation of network protocols and services
- **Trace Request** (and Results): find available paths between two devices in the network fabric
- **Network Snapshot**: view and compare the network state at various times

### Access a Card Workflow

You can access a card workflow in multiple ways:

- For workbenches available from the main menu, open the workbench that contains the card flow
- Open a prior search
- Add it to a workbench
- Search for it

{{<notice tip>}}
If you have multiple cards open on your workbench already, you might need to scroll down to see the card you have just added.
{{</notice>}}

To open the card workflow through an existing workbench:

1. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/> in the workbench task bar.

2. Select the relevant workbench.

    {{< figure src="/images/netq/workbench-selection-from-wb-hdr-300.png" width="200" >}}

    The workbench opens, hiding your previous workbench.

To open the card workflow from Recent Actions:

1. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-clock.svg" height="18" width="18"/> in the application header.
2. Look for an "Add: \<card name\>" item.
3. If it is still available, click the item.

    The card appears on the current workbench, at the bottom.

To access the card workflow by adding the card:

1. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> in the workbench task bar.
2. Follow the instructions in {{<link url="#add-cards-to-your-workbench" text="Add Cards to Your Workbench">}} or {{<link url="#add-switch-cards-to-your-workbench" text="Add Switch Cards to Your Workbench">}}.

    The card appears on the current workbench, at the bottom.

To access the card workflow by searching for the card:

1. Click in the **Global Search** field.
2. Begin typing the name of the card.
3. Select it from the list.

    {{< figure src="/images/netq/add-card-thru-search-300.png" width="350" >}}

    The card appears on a current workbench, at the bottom.

## Card Interactions

Every card contains a standard set of interactions, including the ability to switch between card sizes, and change the time period of the presented data. Most cards also have additional actions that can be taken, in the form of links to other cards, scrolling, and so forth. The four sizes of cards for a particular aspect of the network are connected into a flow; however, you can have duplicate cards displayed at the different sizes. Cards with tabular data provide filtering, sorting, and export of data. The medium and large cards have descriptive text on the back of the cards.

To access the time period, card size, and additional actions, hover over the card. These options appear, covering the card header, enabling you to select the desired option.

### Add Cards to Your Workbench

You can add one or more cards to a workbench at any time. To add Devices|Switches cards, refer to {{<link url="#add-switch-cards-to-your-workbench" text="Add Switch Cards to Your Workbench">}}. For all other cards, follow the steps in this section.

To add one or more cards:

1. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open the **Cards** modal.

    {{< figure src="/images/netq/add-card-modal-all-cards-300.png" width="700" >}}

2. Scroll down until you find the card you want to add, select the category of cards, or use **Search** to find the card you want to add.

    This example uses the category tab to narrow the search for a card.

    {{< figure src="/images/netq/add-card-modal-ntwk-svcs-300.png" width="700" >}}

3. Click on each card you want to add.

    As you select each card, it is grayed out and a <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> appears on top of it. If you have selected one or more cards using the category option, you can selected another category without losing your current selection. Note that the total number of cards selected for addition to your workbench is noted at the bottom.

    {{< figure src="/images/netq/add-card-2-selected-300.png" width="700" >}}

    Also note that if you change your mind and do not want to add a particular card you have selected, simply click on it again to remove it from the cards to be added. Note the total number of cards selected decreases with each card you remove.

4. When you have selected all of the cards you want to add to your workbench, you can confirm which cards have been selected by clicking the **Cards Selected** link. Modify your selection as needed.

      {{<figure src="/images/netq/add-card-confirm-selection-300.png" width="700">}}

5. Click **Open Cards** to add the selected cards, or **Cancel** to return to your workbench without adding any cards.

The cards are placed at the end of the set of cards currently on the workbench. You might need to scroll down to see them. By default, the medium size of the card is added to your workbench for all except the Validation and Trace cards. These are added in the large size by default. You can rearrange the cards as described in {{<link url="#reposition-a-card-on-your-workbench" text="Reposition a Card on Your Workbench">}}.

### Add Switch Cards to Your Workbench

You can add switch cards to a workbench at any time. For all other cards, follow the steps in {{<link url="#add-cards-to-your-workbench" text="Add Cards to Your Workbench">}}. You can either add the card through the Switches icon on a workbench header or by searching for it through Global Search.

To add a switch card using the icon:

1.  Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> to open the Add Switch Card modal.

    {{<figure src="/images/netq/add-switch-card-modal-222.png" width="250">}}

2. Begin entering the hostname of the switch you want to monitor.

3. Select the device from the suggestions that appear.

      {{<figure src="/images/netq/add-switch-card-auto-suggest-222.png" width="250">}}

      {{<notice tip>}}
If you attempt to enter a hostname that is unknown to NetQ, a pink border appears around the entry field and you are unable to select <strong>Add</strong>. Try checking for spelling errors. If you feel your entry is valid, but not an available choice, consult with your network administrator.
      {{</notice>}}

4. Optionally select the small or large size to display instead of the medium size.

5. Click **Add** to add the switch card to your workbench, or **Cancel** to return to your workbench without adding the switch card.

To open the switch card by searching:

1. Click in **Global Search**.

2. Begin typing the name of a switch.

    {{<figure src="/images/netq/add-switch-card-thru-search-300.png" width="300">}}

3. Select it from the options that appear.

### Remove Cards from Your Workbench

Removing cards is handled one card at a time.

To remove a card:

1. Hover over the card you want to remove.
2. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18"/> (*More Actions* menu).
3. Click **Remove**.

    {{< figure src="/images/netq/remove-card-222.png" width="100" >}}

The card is removed from the workbench, but not from the application.

### Change the Time Period for the Card Data

All cards have a default time period for the data shown on the card, typically the last 24 hours. You can change the time period to view the data during a different time range to aid analysis of previous or existing issues.

To change the time period for a card:

1. Hover over any card.

2. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/> in the header.

3. Select a time period from the dropdown list.

    {{<figure src="/images/netq/time-picker-popup-222.png" width="200">}}

{{<notice tip>}}
Changing the time period in this manner only changes the time period for the given card.
{{</notice>}}

### Switch to a Different Card Size

You can switch between the different card sizes at any time. Only one size is visible at a time. To view the same card in different sizes, open a second copy of the card.

To change the card size:

1. Hover over the card.
2. Hover over the Card Size Picker and move the cursor to the right or left until the desired size option is highlighted.

    {{< figure src="/images/netq/card-size-picker-222.png" width="200" >}}

    Single width opens a small card. Double width opens a medium card. Triple width opens large cards. Full width opens full-screen cards.

3. Click the Picker.  
    The card changes to the selected size, and may move its location on the workbench.

### View a Description of the Card Content

When you hover over a medium or large card, the bottom right corner turns up and is highlighted. Clicking the corner turns the card over where a description of the card and any relevant tabs are described. Hover and click again to turn it back to the front side.

{{< figure src="/images/netq/card-desc-on-back-222.png" width="400" >}}

### Reposition a Card on Your Workbench

You can also move cards around on the workbench, using a simple drag and drop method.

To move a card:

1. Simply click and drag the card to left or right of another card, next to where you want to place the card.

2. Release your hold on the card when the other card becomes highlighted with a dotted line. In this example, we are moving the medium Network Health card to the left of the medium Devices Inventory card.  

   {{< figure src="/images/netq/move-card-click-drag-222.png" width="700" >}}

   {{< figure src="/images/netq/move-card-release-222.png" width="700" >}}

### Table Settings

You can manipulate the data in a data grid in a full-screen card in several ways. The available options are displayed above each table. The options vary depending on the card and what is selected in the table.

| Icon | Action | Description |
| ---- | ---- | ---- |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> | Select All | Selects all items in the list. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/subtract-circle.svg" height="18" width="18"/> | Clear All | Clears all existing selections in the list. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18"/> | Add Item | Adds item to the list. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18"/> | Edit | Edits the selected item. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/> | Delete | Removes the selected items. |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18"/> | Filter | Filters the list using available parameters. Refer to {{<link url="#filter-table-data" text="Filter Table Data">}} for more detail.  |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18"/>, {{<img src="/images/netq/netq-mgmt-delete-keys-icon.png" height="18" width="18" >}} | Generate/Delete AuthKeys | Creates or removes NetQ CLI authorization keys. |
| <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> | Open Cards | Opens the corresponding validation or trace card(s). |
| <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18"/> | Assign role | Opens role assignment options for switches. |
| <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> | Export | Exports selected data into either a .csv or JSON-formatted file. Refer to {{<link url="#export-data" text="Export Data">}} for more detail. |

When there are numerous items in a table, NetQ loads up to 25 by default and provides the rest in additional table pages. In this case, pagination is shown under the table.

{{<figure src="/images/netq/table-pagination-320.png" width="400">}}

From there, you can:

- View the total number of items in the list
- Move forward or backward one page at a time (<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="14" width="14"/>, <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-left-1.svg" height="14" width="14"/>)
- Go to the first or last page in the list (<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-left-1.svg" height="14" width="14"/>, <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-right-1.svg" height="14" width="14"/>)

#### Change Order of Columns

You can rearrange the columns within a table. Click and hold on a column header, then drag it to the location where you want it.

#### Sort Table Data by Column

You can sort tables (with up to 10,000 rows) by a given column for tables on full-screen cards. The data is sorted in ascending or descending order; A to Z, Z to A, 1 to n, or n to 1.

To sort table data by column:

1. Open a full-screen card.

2. Hover over a column header.

3. Click the header to toggle between ascending and descending sort order.

For example, this IP Addresses table is sorted by hostname in a descending order. Click the **Hostname** header to sort the data in ascending order. Click the **IfName** header to sort the same table by interface name.

{{<figure src="/images/netq/table-column-sort-descend-320.png" width="700" caption="Sorted by descending hostname">}}

{{<figure src="/images/netq/table-column-sort-ascend-320.png" width="700" caption="Sorted by ascending hostname">}}

{{<figure src="/images/netq/table-column-sort-descend-ifname-320.png" width="700" caption="Sorted by descending interface name">}}

#### Filter Table Data

The filter option associated with tables on full-screen cards can be used to filter the data by any parameter (column name). The parameters available vary according to the table you are viewing. Some tables offer the ability to filter on more than one parameter.

*Tables that Support a Single Filter*

Tables that allow a single filter to be applied let you select the parameter and set the value. You can use partial values.

For example, to set the filter to show only BGP sessions using a particular VRF:

1. Open the full-screen Network Services | All BGP Sessions card.

2. Click the **All Sessions** tab.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18"/> above the table.

4. Select *VRF* from the **Field** dropdown.

5. Enter the name of the VRF of interest. In our example, we chose *vrf1*.

    {{<figure src="/images/netq/table-filter-single-param-241.png" width="700">}}

6. Click **Apply**.

    The filter icon displays a red dot to indicate filters are applied.

    {{<figure src="/images/netq/table-filter-single-param-example-241.png" width="700">}}

7. To remove the filter, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18"/> (with the red dot).

8. Click **Clear**.

9. Close the **Filters** dialog by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/>.

*Tables that Support Multiple Filters*

For tables that offer filtering by multiple parameters, the Filter dialog is slightly different. For example, to filter the list of IP Addresses in your system by hostname and interface:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/>.

2. Select *IP Addresses* under **Network**.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18"/> above the table.

    {{<figure src="/images/netq/table-filter-multi-param-241.png" width="700">}}

4. Enter a hostname and interface name in the respective fields.

5. Click **Apply**.

    The filter icon displays a red dot to indicate filters are applied, and each filter is presented above the table.

    {{<figure src="/images/netq/table-filter-multi-param-example-241.png" width="700">}}

6. To remove a filter, simply click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> on the filter, or to remove all filters at once, click **Clear All Filters**.

### Export Data

You can export tabular data from a full-screen card to a CSV- or JSON-formatted file.

To export *all* data:

1. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> above the table.

2. Select the export format.

3. Click **Export** to save the file to your downloads directory.

To export *selected* data:

1. Select the individual items from the list by clicking in the checkbox next to each item.

2. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> above the table.

3. Select the export format.

4. Click **Export** to save the file to your downloads directory.
