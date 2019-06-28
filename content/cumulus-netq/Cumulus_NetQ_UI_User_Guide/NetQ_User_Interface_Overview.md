---
title: NetQ User Interface Overview
author: Cumulus Networks
weight: 89
aliases:
 - /display/NETQ/NetQ+User+Interface+Overview
 - /pages/viewpage.action?pageId=10457097
pageID: 10457097
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
The NetQ 2.1 <span style="color: #353744;"> graphical user interface
(UI) </span> enables you to access NetQ capabilities through a web
browser as opposed to through a terminal window using the
<span style="color: #353744;"> Command Line Interface (CLI). Visual
representations of the health of the network, inventory, and system
events make it easy to both find faults and misconfigurations and to fix
them. </span>

<span style="color: #333333;"> The UI is supported on Google Chrome.
Other popular browsers may be used, but have not been tested and may
have some presentation issues. </span>

{{%notice tip%}}

<span style="color: #333333;"> Before you get started, you should refer
to the [release
notes](https://wiki.cumulusnetworks.com/display/PC/NetQ+2.0+EA+User+Documentation)
for this version. </span>

{{%/notice%}}

## <span>Access the NetQ UI</span>

<span style="color: #353744;"> Logging in to the NetQ UI is as easy as
opening any web page. </span>

<span style="color: #353744;"> To log in to the UI: </span>

1.  <span style="color: #353744;"> Open a new Internet browser window or
    tab. </span>

2.  <span style="color: #353744;"> Enter the following URL into the
    Address bar: *http://* </span> *<span style="color: #353744;"> \<
    </span> netq-platform/appliance-ipaddress\>:32666.*
    
    {{% imgOld 0 %}}

3.  <span style="color: #353744;"> Select your language of choice
    (English or Spanish) from the dropdown at the top of the window.  
    </span>
    
    {{% imgOld 1 %}}
    
      

4.  <span style="color: #353744;"> Enter your username and then your
    password ( </span> *admin, admin* by default).
    <span style="color: #353744;">  
    </span>
    
    {{% imgOld 2 %}}
    
      
    <span style="color: #353744;"> The default Cumulus Workbench opens,
    with your username showing in the upper right corner of the
    application. </span>

<span style="color: #353744;"> To log out of the UI: </span>

1.  <span style="color: #353744;"> Click the user icon at the top right
    of the application. </span>

2.  <span style="color: #353744;"> Select </span>
    **<span style="color: #000000;"> Log Out.  
    </span>**
    
    **{{% imgOld 3 %}}**
    
    **  
    **

## <span>Application Layout</span>

The NetQ UI contains two areas:

  - **Application Header** (1): Contains the main menu, navigation
    history, search capabilities, NetQ version, quick health status
    chart, local time zone, and user account information.

  - **Workbench** (2): Contains a task bar and content cards (with
    status and configuration information about your network and its
    various components).

{{% imgOld 4 %}}

## <span>Main Menu</span>

Found in the application header, click

{{% imgOld 5 %}}

to open the main menu which provides navigation to:

  - **Favorites**: contains list of links to workbenches that you have
    designated as favorites; Home is listed by default

  - **NetQ**: contains list of links to all workbenches in the
    application

  - **Network**: contains list of links to tabular data about various
    network elements; return to a workbench by selecting it from the
    NetQ menu

  - **Admin**: contains link to user documentation and application
    management

{{% imgOld 6 %}}

## <span>Navigation History</span>

Found in the header, the navigation history keeps track of every action
you take on your workbench. This enables the user to go back to a
previous state or repeat an action.

To open the navigation history, click

{{% imgOld 7 %}}

. Click on any of the actions to perform that action again.

{{% imgOld 8 %}}

## <span>Quick Network Health View</span>

Found in the header, the graph and performance rating provide a view
into the health of your network at a glance.

{{% imgOld 9 %}}

## <span id="src-10457097_safe-id-TmV0UVVzZXJJbnRlcmZhY2VPdmVydmlldy0jVXNyU2V0" class="confluence-anchor-link"></span><span>User Settings</span>

Based on where you reside and your visual preferences, you can specify
how you want your application to look and how data is displayed.

### <span>Choose a Theme</span>

There are two themes available: a Light theme and a Jade (or dark)
theme. The screen captures in this document are all displayed with the
Jade theme.

To choose a theme:

1.  Click
    
    {{% imgOld 10 %}}
    
    in the application header to open the **User Settings** options.
    
    {{% imgOld 11 %}}

2.  Select your choice of theme. It changes on selection. This figure
    shows the light theme.
    
    {{% imgOld 12 %}}

3.  Switch back and forth as desired.

### <span>Choose a Time Zone</span>

By default, the time zone is set to the current local time zone. All
time values are based on this setting. This is displayed in the
application header, and is based on Greenwich Mean Time (GMT).

{{% imgOld 13 %}}

If your deployment is not in this time zone, or if you want to view the
data from the perspective of a data center in another time zone, you can
change the time zone by clicking <span style="color: #353744;"> </span>

{{% imgOld 14 %}}

. The following table presents a sample of time zones:

|           |                                                                                |         |
| --------- | ------------------------------------------------------------------------------ | ------- |
| GMT +12   | New Zealand Standard Time                                                      | NST     |
| GMT +11   | Solomon Standard Time                                                          | SST     |
| GMT +10   | Australian Eastern Time                                                        | AET     |
| GMT +9:30 | Australia Central Time                                                         | ACT     |
| GMT +9    | Japan Standard Time                                                            | JST     |
| GMT +8    | China Taiwan Time                                                              | CTT     |
| GMT +7    | Vietnam Standard Time                                                          | VST     |
| GMT +6    | Bangladesh Standard Time                                                       | BST     |
| GMT +5:30 | India Standard Time                                                            | IST     |
| GMT+5     | Pakistan Lahore Time                                                           | PLT     |
| GMT +4    | Near East Time                                                                 | NET     |
| GMT +3:30 | Middle East Time                                                               | MET     |
| GMT +3    | <span style="color: #000000;"> Eastern African Time/Arab Standard Time </span> | EAT/AST |
| GMT +2    | <span style="color: #000000;"> Eastern European Time </span>                   | EET     |
| GMT +1    | <span style="color: #000000;"> European Central Time </span>                   | ECT     |
| GMT       | Greenwich Mean Time                                                            | GMT     |
| GMT -1    | Central African Time                                                           | CAT     |
| GMT -2    | Uruguay Summer Time                                                            | UYST    |
| GMT -3    | Argentina Standard/Brazil Eastern Time                                         | AGT/BET |
| GMT -4    | Atlantic Standard Time/Puerto Rico Time                                        | AST/PRT |
| GMT -5    | Eastern Standard Time                                                          | EST     |
| GMT -6    | Central Standard Time                                                          | CST     |
| GMT -7    | Mountain Standard Time                                                         | MST     |
| GMT -8    | Pacific Standard Time                                                          | PST     |
| GMT -9    | Alaskan Standard Time                                                          | AST     |
| GMT -10   | Hawaiian Standard Time                                                         | HST     |
| GMT -11   | Samoa Standard Time                                                            | SST     |
| GMT -12   | New Zealand Standard Time                                                      | NST     |

## <span>Search</span>

The Global Search field in the UI header enables you to search for
devices.

### <span>Create a Search</span>

As with most search fields, simply begin entering the criteria in the
search field. As you type, items that match the search criteria are
shown in the search history dropdown along with the last time the search
was viewed. Wildcards are not allowed, but this predictive matching
eliminates the need for them. By default, the most recent searches are
shown. If more have been performed, they can be accessed. This may
provide a quicker search by reducing entry specifics and suggesting
recent searches. Selecting a suggested search from the list provides a
preview of the search results to the right.

To create a new search:

1.  Click in the **Global Search** field.

2.  Enter your search criteria.

3.  Click the device hostname or card workflow in the search list to
    open the associated information.  
    
    {{% imgOld 15 %}}
    
    {{%notice info%}}
    
    If you have more matches than fit in the window, click the **See All
    \# Results** link to view all found matches. The count represents
    the number of devices found. It does not include cards found.
    
    {{%/notice%}}

### <span>Run a Recent Search</span>

You can re-run a recent search, saving time if you are comparing data
from two or more devices.

To re-run a recent search:

1.  Click in the **Global Search** field.

2.  When the desired search appears in the suggested searches list,
    select it.  
    
    {{% imgOld 16 %}}
    
    {{%notice info%}}
    
    You may need to click **See All \# Results** to find the desired
    search. If you do not find it in the list, you may still be able to
    find it in the **Navigation History**.
    
    {{%/notice%}}

## <span>Workbenches</span>

A workbench is comprised of a given set of cards. In this release, a
preconfigured default workbench, Cumulus Workbench, is available to get
you started. It contains Device Inventory, Switch Inventory, Alarm and
Info Events, and Network Health cards. On initial login, this workbench
is opened. You can modify a workbench by adding or removing cards or
card decks, as described in <span style="color: #ff0000;"> [Add or
Remove a Card](#src-10457097_NetQUserInterfaceOverview-AddDelCard)
</span> .

## <span>Cards</span>

Cards present information about your network for monitoring and
troubleshooting. This is where you can expect to spend most of your
time. Each card describes a particular aspect of the network. Cards are
available in multiple sizes, from small to full screen. The level of the
content on a card varies in accordance with the size of the card, with
the highest level of information on the smallest card to the most
detailed information on the full-screen view. Cards are collected onto a
workbench where you see all of the data relevant to a task or set of
tasks. You can add and remove cards from a workbench, move between cards
and card sizes, and make copies of cards to show different levels of
data at the same time.

### <span>Card Sizes</span>

The various sizes of cards enables you to view your content at just the
right level. For each aspect that you are monitoring there is typically
a single card, that presents increasing amounts of data over its four
sizes. For example, a snapshot of your total inventory may be
sufficient, but to monitor the distribution of hardware vendors may
requires a bit more space.

#### <span>Small Cards</span>

Small cards are most effective at providing a quick view of the
performance or statistical value of a given aspect of your network. They
are commonly comprised of an icon to identify the aspect being
monitored, summary performance or statistics in the form of a graph
and/or counts, and often an indication of any related events. Other
content items may be present. Some examples include a Devices Inventory
card, a Switch Inventory card, an Alarm Events card, an Info Events
card, and a Network Health card, as shown here:

{{% imgOld 17 %}}

#### <span>Medium Cards</span>

Medium cards are most effective at providing the key measurements for a
given aspect of your network. They are commonly comprised of an icon to
identify the aspect being monitored, one or more key measurements that
make up the overall performance. Often additional information is also
included, such as related events or components. Some examples include a
Devices Inventory card, a Switch Inventory card, an Alarm Events card,
an Info Events card, and a Network Health card, as shown here. Compare
these with their related small- and large-sized cards.

{{% imgOld 18 %}}

#### <span>Large Cards</span>

Large cards are most effective at providing the detailed information for
monitoring specific components or functions of a given aspect of your
network. These can aid in isolating and resolving existing issues or
preventing potential issues. They are commonly comprised of detailed
statistics and graphics. Some large cards also have tabs for additional
detail about a given statistic or other related information. Some
examples include a Devices Inventory card, an Alarm Events card, and a
Network Health card, as shown here. Compare these with their related
small- and medium-sized cards.

{{% imgOld 19 %}}

#### <span>Full-Screen Cards</span>

Full-screen cards are most effective for viewing all available data
about an aspect of your network all in one place. When you cannot find
what you need in the small, medium, or large cards, it is likely on the
full-screen card. Most full-screen cards are comprised of data grid, or
table; however, some contain visualizations. Some examples include All
Events card and All Switches card, as shown here.

{{% imgOld 20 %}}

{{% imgOld 21 %}}

#### <span>Data Grid Settings</span>

You can manipulate the data in a data grid in a full screen card in
several ways.

*Sort Data by Column*

Hover over a column header and click <span style="color: #353744;">
</span>

{{% imgOld 22 %}}

.

*Choose Columns to Display*

1.  Click <span style="color: #353744;"> </span>
    
    {{% imgOld 23 %}}
    
    at the top right of the card.

2.  Click **Change Columns** from the **Display Settings**.

3.  Click the checkbox next to each column name to toggle on/off the
    columns you would like displayed. Columns listed under **Active**
    are displayed. Columns listed under **Inactive** are not displayed.
    
    {{%notice tip%}}
    
    When you have a large number of possible columns for display, you
    can search for the column name using the **Quick Filter** to find
    and select or deselect the column more quickly.
    
    {{%/notice%}}

4.  Click <span style="color: #353744;"> </span>
    
    {{% imgOld 24 %}}
    
    to close the selection box and view the updated data grid.

*Change Order of Columns*

1.  Click
    
    {{% imgOld 25 %}}
    
    and then click **Change Columns**.

2.  Hover over a column name.

3.  Point to the six dots to the left of the checkbox.

4.  Click and drag the selected column up or down in the list.
    
    {{% imgOld 26 %}}

5.  Click <span style="color: #353744;"> </span>
    
    {{% imgOld 27 %}}
    
    to close the selection box and view the updated data grid.

*<span style="color: #36424a;"> Take Actions on Items </span>*

In the full screen cards, you can determine which results are displayed
in the results list, and which are exported.

To take actions on the data, click in the blank column at the very left
of a row. A checkbox appears, selecting that item, and an edit menu is
shown at the bottom of the card (shown enlarged here).

{{% imgOld 28 %}}

{{% imgOld 29 %}}

You can perform the following actions on the results list:

| Option             | Action or Behavior on Click                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Select All         | Selects all items in the results list                                                                            |
| Clear All          | Clears all existing selections of items in the results list. This also hides the edit menu.                      |
| Export Selected    | Exports selected data into a .csv file. If you want to export to a .json file format, use the **Export** button. |
| Show Only Selected | Hide unselected switches, sessions, or alarms.                                                                   |
| Remove Selected    | Remove selected switches, sessions, or alarms from the results list.                                             |

To return to original display of results, click the associated tab.

#### <span>Export Data</span>

You can export tabular data from a full screen card to a CSV- or
JSON-formatted file.

To export the data:

1.  If you want to export only a subset of the data listed, select those
    items first.

2.  Click **EXPORT**.
    
    {{% imgOld 30 %}}

3.  Select all data or selected data for export in the dialog box:
    
    {{% imgOld 31 %}}

4.  Select the export format.

5.  Click **EXPORT** to save the file to your downloads directory.

{{%notice tip%}}

You can quickly export all data to a .csv file in one of two ways:

  - Click **Export** at top of list, and click **Export** in the dialog,
    or

  - Select one item, click **Select All**, click **Export Selected**.

{{%/notice%}}

#### <span>Card Size Summary</span>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Card Size</p></th>
<th><p>Small</p></th>
<th><p>Medium</p></th>
<th><p>Large</p></th>
<th><p>Full Screen</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Primary Purpose</p></td>
<td><ul>
<li><p>Quick view of status, typically at the level of good or bad</p></li>
<li><p>Enable quick actions, run a validation or trace for example</p></li>
</ul></td>
<td><ul>
<li><p>View key performance parameters or statistics</p></li>
<li><p>Perform an action</p></li>
<li><p>Look for potential issues</p></li>
</ul></td>
<td><ul>
<li><p>View detailed performance and statistics</p></li>
<li><p>Perform actions</p></li>
<li><p>Compare and review related information</p></li>
</ul></td>
<td><ul>
<li><p>View all attributes for given network aspect</p></li>
<li><p>Free-form data analysis and visualization</p></li>
<li><p>Export data to third-party tools</p></li>
</ul></td>
</tr>
</tbody>
</table>

### <span>Card Interactions</span>

Every card contains a standard set of interactions, including the
ability to switch between card sizes, and change the time period of the
presented data. Most cards also have additional actions that can be
taken, in the form of links to other cards, scrolling, and so forth. The
four sizes of cards for a particular aspect of the network are connected
into a flow; however, you can have duplicate cards displayed at the
different sizes. Cards with tabular data provide filtering, sorting, and
export of data. The medium and large cards have descriptive text on the
back of the cards.

To access the time period, card size, and additional actions, hover over
the card. These options appear, covering the card header, enabling you
to select the desired option.

#### <span>Change the Time Period for the Card Data</span>

All cards have a default time period for the data shown on the card,
typically the last 24 hours. You can change the time period to view the
data during a different time range to aid analysis of previous or
existing issues.

To change the time period for a card:

1.  Hover over any card.

2.  Click <span style="color: #353744;"> </span>
    
    {{% imgOld 32 %}}
    
    in the header .

3.  Select a time period from the dropdown list.
    
    {{% imgOld 33 %}}

{{%notice tip%}}

Changing the time period in this manner only changes the time period for
the given card.

{{%/notice%}}

#### <span>Switch to a Different Card Size</span>

You can switch between the different card sizes at any time. Only one
size is visible at a time. To view the same card in different sizes,
open a second copy of the card.

To change the card size:

1.  Hover over the card.

2.  Hover over the Card Size Picker and move the cursor to the right or
    left until the desired size option is highlighted.
    
    {{% imgOld 34 %}}
    
    Single width opens a small card. Double width opens a medium card.
    Triple width opens large cards. Full width opens full-screen cards.

3.  Click the Picker.  
    The card changes to the selected size, and may move its location on
    the workbench.

#### <span>Reposition a Card on Your Workbench</span>

You can also move cards around on the workbench, using a simple drag and
drop method.

To move a card:

1.  Simply click and drag the card to left or right of another card,
    next to where you want to place the card.

2.  Release your hold on the card when the other card becomes
    highlighted with a dotted line. In this example, we are moving the
    medium Network Health card to the left of the medium Devices
    Inventory card.  
    
    {{% imgOld 35 %}}
    
    {{% imgOld 36 %}}
    
    {{% imgOld 37 %}}

### <span id="src-10457097_NetQUserInterfaceOverview-AddDelCard" class="confluence-anchor-link"></span><span>Add or Remove a Card</span>

You can add or remove cards from a workbench at any time.

To add a card:

1.  Click
    
    {{% imgOld 38 %}}
    
    .
    
    {{% imgOld 39 %}}

2.  Select a card from the available list.

The card is placed at the end of the set of cards currently on the
workbench. You might need to scroll down to see it. By default, the
medium size of the card is added to your workbench. You can move it to
another location as described above.

To remove a card:

1.  Hover over the card you want to remove.

2.  Click <span style="color: #000000;"> </span>
    
    {{% imgOld 40 %}}
    
    (*More Actions* menu).

3.  Click **Remove**.
    
    {{% imgOld 41 %}}

The card is removed from the workbench, but not from the application.

## <span>Card Workflows</span>

The UI provides a number of card workflows. Card workflows focus on a
particular aspect of your network and are a linked set of each size
card—a small card, a medium card, one or more large cards, and one or
more full screen cards. The following card workflows are available:

  - Network Health: network-wide view of network health

  - Devices|Switches: health of a given switch

  - Inventory|Devices: information about all switches and hosts in the
    network

  - Inventory|Switches: information about the components on a given
    switch

  - Events|Alarms: information about all critical severity events in the
    system

  - Events|Info: information about all warning, info, and debug events
    in the system

  - Network Services: information about the BGP, CLAG, EVPN, and LLDP
    services and sessions

  - Validation Request (and Results): network-wide validation of network
    protocols and services

  - Trace Request (and Results): find available paths between two
    devices in the network fabric

### <span>Access a Card Workflow</span>

You can access a card workflow in multiple ways:

  - For workbenches available from the main menu, open the workbench
    that contains the card flow

  - Open a prior search

  - Add it to a workbench

  - Search for it

{{%notice tip%}}

If you have multiple cards open on your workbench already, you might
need to scroll down to see the card you have just added.

{{%/notice%}}

To open the card workflow through an existing workbench:

1.  Click <span style="color: #353744;"> </span>
    
    {{% imgOld 42 %}}
    
    in the workbench header .

2.  Select the relevant workbench.
    
    {{% imgOld 43 %}}

The workbench opens, hiding your previous workbench.

To open the card workflow from a prior search:

1.  Browse your search list in the navigation panel.

2.  Look for an "Add: \<card name\>" item.

3.  If it is still available, click the item.

The card appears on the current workbench, at the bottom.

To access the card workflow by adding the card:

1.  Click <span style="color: #353744;"> </span>
    
    {{% imgOld 44 %}}
    
    .

2.  Select the relevant card.

The card appears on the current workbench, at the bottom.

To access the card workflow by searching for the card:

1.  Click in the **Global Search** field.

2.  Begin typing the name of the card.

3.  Select it from the list.
    
    {{% imgOld 45 %}}

The card appears on a current workbench, at the bottom.

## <span>Card Decks</span>

A card deck is a collection of related cards that can be added and
removed from a workbench all at once. They are distinct from card
workflows, which focus on a particular aspect of your network. A card
deck pulls multiple cards with related information to aid the user in
performing a broader task. It also simplifies the creation of new
workbenches when a card deck is available. The following card decks are
provided by default:

  - Inventory: includes the medium Inventory | Switches and Inventory |
    Devices cards

  - Events: includes the medium Events | Alarms and Events | Info cards

## <span>Basic Terminology and Acronyms</span>

The following table covers some basic terms used throughout the NetQ
user documentation.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p><span style="color: #000000;"> Term </span></p></th>
<th><p><span style="color: #000000;"> Definition </span></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span style="color: #353744;"> Agent </span></p></td>
<td><p><span style="color: #353744;"> NetQ software that resides on a host server that provides metrics about the host to the NetQ Telemetry Server for network health analysis. </span></p></td>
</tr>
<tr class="even">
<td><p>Alarm</p></td>
<td><p>In UI, event with critical severity.</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> Bridge </span></p></td>
<td><p><span style="color: #353744;"> Device that connects two communication networks or network segments. Occurs at OSI Model Layer 2, Data Link Layer. </span></p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> Clos </span></p></td>
<td><p><span style="color: #353744;"> Multistage circuit switching network used by the telecommunications industry, first formalized by Charles Clos in 1952. </span></p></td>
</tr>
<tr class="odd">
<td><p>Device</p></td>
<td><p>UI term referring to a switch, host, or chassis or combination of these. Typically used when describing hardware and components versus a software or network topology. See also Node.</p></td>
</tr>
<tr class="even">
<td><p>Event</p></td>
<td><p><span style="color: #000000;"> Change or occurrence in network or component; may or may not trigger a notification. In the NetQ UI, there are two types of events: Alarms which indicate a critical severity event, and Info which indicate warning, informational, and debugging severity events. </span></p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> Fabric </span></p></td>
<td><p><span style="color: #353744;"> Network topology where a set of network nodes is interconnected through one or more network switches. </span></p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> Fresh </span></p></td>
<td><p><span style="color: #353744;"> Node that has been heard from in the last 90 seconds. </span></p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> High Availability </span></p></td>
<td><p><span style="color: #353744;"> Software used to provide a high percentage of uptime (running and available) for network devices. </span></p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> Host </span></p></td>
<td><p><span style="color: #353744;"> Device that is connected to a TCP/IP network. May run one or more Virtual Machines. </span></p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> Hypervisor </span></p></td>
<td><p><span style="color: #353744;"> Software which creates and runs Virtual Machines. Also called a Virtual Machine Monitor. </span></p></td>
</tr>
<tr class="even">
<td><p>Info</p></td>
<td><p>In UI, event with warning, informational, or debugging severity.</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> IP Address </span></p></td>
<td><p><span style="color: #353744;"> An Internet Protocol address is comprised of a series of numbers assigned to a network device to uniquely identify it on a given network. Version 4 addresses are 32 bits and written in dotted decimal notation with 8-bit binary numbers separated by decimal points. Example: 10.10.10.255. Version 6 addresses are 128 bits and written in 16-bit hexadecimal numbers separated by colons. Example: 2018:3468:1B5F::6482:D673. </span></p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> Leaf </span></p></td>
<td><p><span style="color: #353744;"> An access layer switch in a Spine-Leaf or Clos topology. An Exit-Leaf is switch that connects to services outside of the Data Center such as firewalls, load balancers, and Internet routers. </span></p>
<p><span style="color: #353744;"> See also Spine, CLOS, Top of Rack and Access Switch. </span></p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> Linux </span></p></td>
<td><p><span style="color: #353744;"> Set of free and open-source software operating systems built around the Linux kernel. Cumulus Linux is one available distribution packages. </span></p></td>
</tr>
<tr class="even">
<td><p>Node</p></td>
<td><p>UI term referring to a switch, host or chassis in a topology.</p></td>
</tr>
<tr class="odd">
<td><p>Notification</p></td>
<td><p><span style="color: #000000;"> Item that informs a user of an event. In UI there are two types of notifications: Alert which is a n <span style="color: #000000;"> otification sent by system to inform a user about an event; specifically received through a third-party application, and Message which is a notification <span style="color: #000000;"> sent by a user to share content with another user. </span> </span> </span></p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> Peerlink </span></p></td>
<td><p><span style="color: #353744;"> Link, or bonded links, used to connect two switches in an MLAG pair. </span></p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> Rotten </span></p></td>
<td><p><span style="color: #353744;"> Node that has not been heard from in 90 seconds or more. </span></p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> Router </span></p></td>
<td><p><span style="color: #353744;"> Device that forwards data packets (directs traffic) from nodes on one communication network to nodes on another network. Occurs at the OSI Model Layer 3, Network Layer. </span></p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> Spine </span></p></td>
<td><p><span style="color: #353744;"> Used to describe the role of a switch in a Spine-Leaf or CLOS topology. See also Aggregation switch, End of Row switch, and distribution switch. </span></p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> Switch </span></p></td>
<td><p><span style="color: #353744;"> High-speed device that connects that receives data packets from one device or node and redirects them to other devices or nodes on a network. </span></p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> Telemetry server </span></p></td>
<td><p><span style="color: #353744;"> NetQ server which receives metrics and other data from NetQ agents on leaf and spine switches and hosts. </span></p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> Top of Rack </span></p></td>
<td><p><span style="color: #353744;"> Switch that connects to the network (versus internally) </span></p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> Virtual Machine </span></p></td>
<td><p><span style="color: #353744;"> Emulation of a computer system that provides all of the functions of a particular architecture. </span></p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> Web-scale </span></p></td>
<td><p><span style="color: #353744;"> A network architecture designed to deliver capabilities of large cloud service providers within an enterprise IT environment. </span></p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> Whitebox </span></p></td>
<td><p><span style="color: #353744;"> Generic, off-the-shelf, switch or router hardware used in Software Defined Networks (SDN). </span></p></td>
</tr>
</tbody>
</table>

The following table covers some common acronyms used throughout the NetQ
user documentation.

| <span style="color: #000000;"> Acronym </span>       | <span style="color: #000000;"> Meaning </span>                                             |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| <span style="color: #353744;"> ACL </span>           | <span style="color: #353744;"> Access Control Link </span>                                 |
| <span style="color: #353744;"> ARP </span>           | <span style="color: #353744;"> Address Resolution Protocol </span>                         |
| <span style="color: #353744;"> ASN </span>           | <span style="color: #353744;"> Autonomous System Number </span>                            |
| <span style="color: #353744;"> BGP/eBGP/iBGP </span> | <span style="color: #353744;"> Border Gateway Protocol, External BGP, Internal BGP </span> |
| <span style="color: #353744;"> CLAG </span>          | <span style="color: #353744;"> Cumulus multi-chassis Link Aggregation Group </span>        |
| <span style="color: #353744;"> DHCP </span>          | <span style="color: #353744;"> Dynamic Host Control Protocol </span>                       |
| <span style="color: #353744;"> DNS </span>           | <span style="color: #353744;"> Domain Name Server </span>                                  |
| <span style="color: #353744;"> ECMP </span>          | <span style="color: #353744;"> Equal Cost Multi-Path routing </span>                       |
| <span style="color: #353744;"> EVPN </span>          | <span style="color: #353744;"> Ethernet Virtual Private Network </span>                    |
| <span style="color: #353744;"> FDB </span>           | <span style="color: #353744;"> Forwarding Data Base </span>                                |
| <span style="color: #353744;"> GNU </span>           | <span style="color: #353744;"> GNU’s Not Linux </span>                                     |
| <span style="color: #353744;"> HA </span>            | <span style="color: #353744;"> High Availability </span>                                   |
| <span style="color: #353744;"> IGMP </span>          | <span style="color: #353744;"> Internet Group Management Protocol </span>                  |
| <span style="color: #353744;"> IPv4/IPv6 </span>     | <span style="color: #353744;"> Internet Protocol, version 4 or 6 </span>                   |
| <span style="color: #353744;"> LACP </span>          | <span style="color: #353744;"> Link Aggregation Control Protocol </span>                   |
| <span style="color: #353744;"> LAN </span>           | <span style="color: #353744;"> Local Area Network </span>                                  |
| <span style="color: #353744;"> LLDP </span>          | <span style="color: #353744;"> Link Layer Data Protocol </span>                            |
| <span style="color: #353744;"> MAC </span>           | <span style="color: #353744;"> Media Access Control </span>                                |
| <span style="color: #353744;"> MIB </span>           | <span style="color: #353744;"> Management Information Base </span>                         |
| <span style="color: #353744;"> MLAG </span>          | <span style="color: #353744;"> Multi-chassis Link Aggregation Group </span>                |
| <span style="color: #353744;"> MLD </span>           | <span style="color: #353744;"> Multicast Listener Discovery </span>                        |
| <span style="color: #353744;"> NTP </span>           | <span style="color: #353744;"> Network Time Protocol </span>                               |
| <span style="color: #353744;"> OOB </span>           | <span style="color: #353744;"> Out of Band (management) </span>                            |
| <span style="color: #353744;"> OSPF </span>          | <span style="color: #353744;"> Open Shortest Path First </span>                            |
| <span style="color: #353744;"> RFC </span>           | <span style="color: #353744;"> Remote Function Call </span>                                |
| <span style="color: #353744;"> SDN </span>           | <span style="color: #353744;"> Software-Defined Network </span>                            |
| <span style="color: #353744;"> SNMP </span>          | <span style="color: #353744;"> Simple Network Management Protocol </span>                  |
| <span style="color: #353744;"> SSH </span>           | <span style="color: #353744;"> Secure SHell </span>                                        |
| <span style="color: #353744;"> SQL </span>           | <span style="color: #353744;"> Structured Query Language </span>                           |
| <span style="color: #353744;"> STP </span>           | <span style="color: #353744;"> Spanning Tree Protocol </span>                              |
| <span style="color: #353744;"> TCP </span>           | <span style="color: #353744;"> Transport Control Protocol </span>                          |
| <span style="color: #353744;"> ToR </span>           | <span style="color: #353744;"> Top of Rack </span>                                         |
| <span style="color: #353744;"> UDP </span>           | <span style="color: #353744;"> User Datagram Protocol </span>                              |
| <span style="color: #353744;"> URL </span>           | <span style="color: #353744;"> Universal Resource Locator </span>                          |
| <span style="color: #353744;"> USB </span>           | <span style="color: #353744;"> Universal Serial Bus </span>                                |
| <span style="color: #353744;"> VLAN </span>          | <span style="color: #353744;"> Virtual Local Area Network </span>                          |
| <span style="color: #353744;"> VNI </span>           | <span style="color: #353744;"> Virtual Network Instance </span>                            |
| <span style="color: #353744;"> VPN </span>           | <span style="color: #353744;"> Virtual Private Network </span>                             |
| <span style="color: #353744;"> VRF </span>           | <span style="color: #353744;"> Virtual Routing and Forwarding </span>                      |
| <span style="color: #353744;"> VRR </span>           | <span style="color: #353744;"> Virtual Router Redundancy </span>                           |
| <span style="color: #353744;"> VTEP </span>          | <span style="color: #353744;"> VXLAN Tunnel EndPoint </span>                               |
| <span style="color: #353744;"> VXLAN </span>         | <span style="color: #353744;"> Virtual Extensible Local Area Network </span>               |
| <span style="color: #353744;"> ZTP </span>           | <span style="color: #353744;"> Zero Touch Provisioning </span>                             |

<span style="color: #36424a;"> Format Cues </span>

Color is used to indicate links, options, and status within the UI.

| Item                                | Color  |
| ----------------------------------- | ------ |
| Hover on item                       | Blue   |
| Clickable item                      | Black  |
| Selected item                       | Green  |
| Highlighted item                    | Blue   |
| Link                                | Blue   |
| Good/Successful results             | Green  |
| Result with critical severity event | Pink   |
| Result with high severity event     | Red    |
| Result with medium severity event   | Orange |
| Result with low severity event      | Yellow |

## <span>Get Help</span>

You can access the user documentation for the UI from the Main Menu.
Just click

{{% imgOld 46 %}}

and select *Help Documentation* under the ADMIN category.
