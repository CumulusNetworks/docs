---
title: NetQ User Interface Overview
author: Cumulus Networks
weight: 89
aliases:
 - /display/NETQ/NetQ+User+Interface+Overview
 - /pages/viewpage.action?pageId=12321856
pageID: 12321856
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
The NetQ 2.2 graphical user interface
(UI) enables you to access NetQ capabilities through a web
browser as opposed to through a terminal window using the
Command Line Interface (CLI). Visual
representations of the health of the network, inventory, and system
events make it easy to both find faults and misconfigurations, and to fix
them.

The UI is accessible in both on-site and in-cloud deployments. It is supported on Google Chrome. Other popular
browsers may be used, but have not been tested and may have some
presentation issues.

{{%notice tip%}}

Before you get started, you should refer to the [release notes](https://support.cumulusnetworks.com/hc/en-us/articles/360025451374) for this version.

{{%/notice%}}

## Access the NetQ UI

Logging in to the NetQ UI is as easy as opening any web page.

To log in to the UI:

1.  Open a new Internet browser window or
    tab.
2.  Enter the following URL into the Address bar
    for the on-site NetQ Platform/NetQ Appliance or the NetQ
    Cloud Appliance:  
    - On-site: *http://\<netq-platform/appliance-ipaddress\>:32666*  
    - In-cloud: *http//netq.cumulusnetworks.com*

    {{% imgOld 0 %}}

3.  Select your language of choice (English or Spanish) from the dropdown at the top of the window.

    {{% imgOld 1 %}}

4.  Enter your username and then your password:  
    - NetQ Platform: *admin, admin* by default  
    - NetQ Appliance: *cumulus, CumulusLinux\!* by default  
    - NetQ Cloud Appliance: Use credentials provided by Cumulus via email titled *Welcome to Cumulus NetQ\!* and
    accept the terms of use.

    {{% imgOld 2 %}}

    On your first login, the default
    Cumulus Workbench opens, with your username shown in the upper right
    corner of the application. The NetQ Cloud UI has a **Premises** list
    in the application header, but is otherwise the same. On future
    logins, the last workbench that you were viewing is displayed.

To log out of the UI:

1.  Click the user icon at the top right of the application.

2.  Select **Log Out**.  

    {{% imgOld 3 %}}


## Application Layout

The NetQ UI contains two areas:

  - **Application Header** (1): Contains the main menu, navigation
    history, search capabilities, NetQ version, quick health status
    chart, local time zone, premises list (cloud-only), and user account
    information.
  - **Workbench** (2): Contains a task bar and content cards (with
    status and configuration information about your network and its
    various components).

{{% imgOld 4 %}}

## Main Menu

Found in the application header, click {{% imgOld 5 %}} to open the main menu which provides navigation to:

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

## Recent Actions

Found in the header, the Recent Actions keeps track of every action you
take on your workbench. This enables you to go back to a previous state
or repeat an action.

To open Recent Actions, click {{% imgOld 7 %}}. Click on any of the actions to perform that action again.

{{% imgOld 8 %}}

## Search

The Global Search field in the UI header enables you to search for
devices.

### Create a Search

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

    {{% imgOld 9 %}}

    {{%notice note%}}

If you have more matches than fit in the window, click the **See All
    \# Results** link to view all found matches. The count represents
    the number of devices found. It does not include cards found.

    {{%/notice%}}

### Run a Recent Search

You can re-run a recent search, saving time if you are comparing data
from two or more devices.

To re-run a recent search:

1.  Click in the **Global Search** field.

2.  When the desired search appears in the suggested searches list,
    select it.  

    {{% imgOld 10 %}}

    {{%notice note%}}

You may need to click **See All \# Results** to find the desired
    search. If you do not find it in the list, you may still be able to
    find it in the **Recent Actions** list.

    {{%/notice%}}

## Quick Network Health View

Found in the header, the graph and performance rating provide a view
into the health of your network at a glance.

{{% imgOld 11 %}}

{{%notice note%}}

On initial start up of the application, it may take up to an hour to
reach an accurate health indication as some processes run every 30
minutes.

{{%/notice%}}

## Workbenches

A workbench is comprised of a given set of cards. In this release, a
preconfigured default workbench, Cumulus Workbench, is available to get
you started. It contains Device Inventory, Switch Inventory, Alarm and
Info Events, and Network Health cards. On initial login, this workbench
is opened. You can modify a workbench by adding or removing cards or
card decks, as described in [Add or Remove a Card](#add-or-remove-a-card).

## Cards

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

### Card Sizes

The various sizes of cards enables you to view your content at just the
right level. For each aspect that you are monitoring there is typically
a single card, that presents increasing amounts of data over its four
sizes. For example, a snapshot of your total inventory may be
sufficient, but to monitor the distribution of hardware vendors may
requires a bit more space.

#### Small Cards

Small cards are most effective at providing a quick view of the
performance or statistical value of a given aspect of your network. They
are commonly comprised of an icon to identify the aspect being
monitored, summary performance or statistics in the form of a graph
and/or counts, and often an indication of any related events. Other
content items may be present. Some examples include a Devices Inventory
card, a Switch Inventory card, an Alarm Events card, an Info Events
card, and a Network Health card, as shown here:

{{% imgOld 12 %}}

#### Medium Cards

Medium cards are most effective at providing the key measurements for a
given aspect of your network. They are commonly comprised of an icon to
identify the aspect being monitored, one or more key measurements that
make up the overall performance. Often additional information is also
included, such as related events or components. Some examples include a
Devices Inventory card, a Switch Inventory card, an Alarm Events card,
an Info Events card, and a Network Health card, as shown here. Compare
these with their related small- and large-sized cards.

{{% imgOld 13 %}}

#### Large Cards

Large cards are most effective at providing the detailed information for
monitoring specific components or functions of a given aspect of your
network. These can aid in isolating and resolving existing issues or
preventing potential issues. They are commonly comprised of detailed
statistics and graphics. Some large cards also have tabs for additional
detail about a given statistic or other related information. Some
examples include a Devices Inventory card, an Alarm Events card, and a
Network Health card, as shown here. Compare these with their related
small- and medium-sized cards.

{{% imgOld 14 %}}

#### Full-Screen Cards

Full-screen cards are most effective for viewing all available data
about an aspect of your network all in one place. When you cannot find
what you need in the small, medium, or large cards, it is likely on the
full-screen card. Most full-screen cards are comprised of data grid, or
table; however, some contain visualizations. Some examples include All
Events card and All Switches card, as shown here.

{{% imgOld 15 %}}

{{% imgOld 16 %}}

#### Data Grid Settings

You can manipulate the data in a data grid in a full screen card in
several ways.

*Sort Data by Column*

Hover over a column header and click {{% imgOld 17 %}}.

*Choose Columns to Display*

1.  Click {{% imgOld 18 %}} at the top right of the card.
2.  Click **Change Columns** from the **Display Settings**.
3.  Click the checkbox next to each column name to toggle on/off the
    columns you would like displayed. Columns listed under **Active**
    are displayed. Columns listed under **Inactive** are not displayed.

    {{%notice tip%}}

When you have a large number of possible columns for display, you
    can search for the column name using the **Quick Filter** to find
    and select or deselect the column more quickly.

    {{%/notice%}}

4.  Click {{% imgOld 19 %}} to close the selection box and view the updated data grid.

*Change Order of Columns*

1.  Click {{% imgOld 20 %}} and then click **Change Columns**.
2.  Hover over a column name.

    {{%notice tip%}}

You use the **Quick Filter** to find the column when you have a large
    number of columns.

    {{%/notice%}}

3.  Point to the six dots to the left of the checkbox.
4.  Click and drag the selected column up or down in the list.

    {{% imgOld 21 %}}

5.  Click {{% imgOld 22 %}} to close the selection box and view the updated data grid.

*Take Actions on Items*

In the full screen cards, you can determine which results are displayed
in the results list, and which are exported.

To take actions on the data, click in the blank column at the very left
of a row. A checkbox appears, selecting that item, and an edit menu is
shown at the bottom of the card (shown enlarged here).

{{% imgOld 23 %}}

{{% imgOld 24 %}}

You can perform the following actions on the results list. **Note**:
The actions vary based on the card displayed.

| Option                   | Action or Behavior on Click                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Select All               | Selects all items in the results list                                                                            |
| Clear All                | Clears all existing selections of items in the results list. This also hides the edit menu.                      |
| Edit                     | Edit the selected items                                                                                          |
| Delete                   | Remove the selected items                                                                                        |
| Generate/Delete AuthKeys | Create or remove NetQ Cloud authorization keys                                                                   |
| Open Cards               | Open the corresponding validation or trace result card                                                           |
| Hide Selected            | Hide selected items (switches, sessions, alarms, and so forth) from the results list                             |
| Show Only Selected       | Hide unselected items (switches, sessions, alarms, and so forth) from the results list                           |
| Export Selected          | Exports selected data into a .csv file. If you want to export to a .json file format, use the **Export** button. |

To return to original display of results, click the associated tab.

#### Export Data

You can export tabular data from a full screen card to a CSV- or
JSON-formatted file.

To export the data:

1.  If you want to export only a subset of the data listed, select those
    items first.
2.  Click **EXPORT**.

    {{% imgOld 25 %}}

3.  Select all data or selected data for export in the dialog box:

    {{% imgOld 26 %}}

4.  Select the export format.
5.  Click **EXPORT** to save the file to your downloads directory.

{{%notice tip%}}

You can quickly export all data to a .csv file in one of two ways:

  - Click **Export** at top of list, and click **Export** in the dialog,
    or
  - Select one item, click **Select All**, click **Export Selected**.

{{%/notice%}}

#### Card Size Summary

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
<td><p>Card Size</p></td>
<td><p>Small</p></td>
<td><p>Medium</p></td>
<td><p>Large</p></td>
<td><p>Full Screen</p></td>
</tr>
<tr class="even">
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

### Card Interactions

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

#### Change the Time Period for the Card Data

All cards have a default time period for the data shown on the card,
typically the last 24 hours. You can change the time period to view the
data during a different time range to aid analysis of previous or
existing issues.

To change the time period for a card:

1.  Hover over any card.
2.  Click {{% imgOld 27 %}} in the header.
3.  Select a time period from the dropdown list.

    {{% imgOld 28 %}}

{{%notice tip%}}

Changing the time period in this manner only changes the time period for
the given card.

{{%/notice%}}

#### Switch to a Different Card Size

You can switch between the different card sizes at any time. Only one
size is visible at a time. To view the same card in different sizes,
open a second copy of the card.

To change the card size:

1.  Hover over the card.
2.  Hover over the Card Size Picker and move the cursor to the right or
    left until the desired size option is highlighted.

    {{% imgOld 29 %}}

    Single width opens a small card. Double width opens a medium card.
    Triple width opens large cards. Full width opens full-screen cards.

3.  Click the Picker.  
    The card changes to the selected size, and may move its location on
    the workbench.

#### View a Description of the Card Content

When you hover over a medium or large card, the bottom right corner
turns up and is highlighted. Clicking the corner turns the card over
where a description of the card and any relevant tabs are described.
Hover and click again to turn it back to the front side.

{{% imgOld 30 %}}

{{% imgOld 31 %}}

#### Reposition a Card on Your Workbench

You can also move cards around on the workbench, using a simple drag and
drop method.

To move a card:

1.  Simply click and drag the card to left or right of another card,
    next to where you want to place the card.
2.  Release your hold on the card when the other card becomes
    highlighted with a dotted line. In this example, we are moving the
    medium Network Health card to the left of the medium Devices
    Inventory card.  

    {{% imgOld 32 %}}

    {{% imgOld 33 %}}

    {{% imgOld 34 %}}

### Add or Remove a Card

You can add or remove cards from a workbench at any time.

To add a card:

1.  Click {{% imgOld 35 %}}.

    {{% imgOld 36 %}}

2.  Select a card from the available list.

The card is placed at the end of the set of cards currently on the
workbench. You might need to scroll down to see it. By default, the
medium size of the card is added to your workbench. You can move it to
another location as described above.

To remove a card:

1.  Hover over the card you want to remove.
2.  Click {{% imgOld 37 %}} (*More Actions* menu).
3.  Click **Remove**.

    {{% imgOld 38 %}}

The card is removed from the workbench, but not from the application.

## Card Workflows

The UI provides a number of card workflows. Card workflows focus on a
particular aspect of your network and are a linked set of each size
card—a small card, a medium card, one or more large cards, and one or
more full screen cards. The following card workflows are available:

  - **Network Health**: network-wide view of network health
  - **Devices|Switches**: health of a given switch
  - **Inventory|Devices**: information about all switches and hosts in
    the network
  - **Inventory|Switches**: information about the components on a given
    switch
  - **Events|Alarms**: information about all critical severity events in
    the system
  - **Events|Info**: information about all warning, info, and debug
    events in the system
  - **Network Services**: information about the network services and
    sessions
  - **Validation Request** (and Results): network-wide validation of
    network protocols and services
  - **Trace Request** (and Results): find available paths between two
    devices in the network fabric

### Access a Card Workflow

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

1.  Click {{% imgOld 39 %}} in the workbench task bar.

2.  Select the relevant workbench.

    {{% imgOld 40 %}}

    The workbench opens, hiding your previous workbench.

To open the card workflow from a prior search:

1.  Browse your search list in the navigation panel.
2.  Look for an "Add: \<card name\>" item.
3.  If it is still available, click the item.

    The card appears on the current workbench, at the bottom.

To access the card workflow by adding the card:

1.  Click {{% imgOld 41 %}} in the workbench task bar.
2.  Select the relevant card.

    The card appears on the current workbench, at the bottom.

To access the card workflow by searching for the card:

1.  Click in the **Global Search** field.
2.  Begin typing the name of the card.
3.  Select it from the list.

    {{% imgOld 42 %}}

    The card appears on a current workbench, at the bottom.

## Card Decks

A card deck is a collection of related cards that can be added and
removed from a workbench all at once. They are distinct from card
workflows, which focus on a particular aspect of your network. A card
deck pulls multiple cards with related information to aid the user in
performing a broader task. It also simplifies the creation of new
workbenches when a card deck is available. The following card decks are
provided by default:

  - **Inventory**: includes the medium Inventory | Switches and
    Inventory | Devices cards
  - **Events**: includes the medium Events | Alarms and Events | Info
    cards

To add a card deck:

1.  Click {{% imgOld 43 %}} in the workbench task bar.
2.  Select the deck you want to add to your workbench.

## User Settings

You can customize the NetQ application display, change their account
password, and manage their workbenches.

### Configure Display Settings

The Display card contains the options for setting the application theme,
language, time zone, and date formats. There are two themes available: a
Light theme and a Dark theme (default). The screen captures in this
document are all displayed with the Dark theme. English is the only
language available for this release. You can choose to view data in the
time zone where you or your data center resides. You can also select the
date and time format, choosing words or number format and a 12- or
24-hour clock. All changes take effect immediately.

To configure the display settings:

1.  Click {{% imgOld 44 %}} in the application header to open the **User Settings** options.

    {{% imgOld 45 %}}

2.  Click **Profile & Preferences**.
3.  Locate the Display card.

    {{% imgOld 46 %}}

4.  In the **Theme** field, click {{% imgOld 47 %}} to select your choice of theme. This figure shows the light theme. Switch back and forth as desired.

    {{% imgOld 48 %}}

5.  In the **Time Zone** field, click {{% imgOld 49 %}} to change the time zone from the default.  
    By default, the time zone is set to the user's local time zone. If a
    time zone has not been selected, NetQ defaults to the current local
    time zone where NetQ is installed. All time values are based on this
    setting. This is displayed in the application header, and is based
    on Greenwich Mean Time (GMT).  

    {{% imgOld 50 %}}

    **Note**: You can also change the time zone from the header
    display.

    If your deployment is not local to you (for example, you want to
    view the data from the perspective of a data center in another time
    zone) you can change the display to another time zone. The
    following table presents a sample of time zones:

    | Time Zone | Description                             | Abbreviation |
    | --------- | --------------------------------------- | ------------ |
    | GMT +12   | New Zealand Standard Time               | NST          |
    | GMT +11   | Solomon Standard Time                   | SST          |
    | GMT +10   | Australian Eastern Time                 | AET          |
    | GMT +9:30 | Australia Central Time                  | ACT          |
    | GMT +9    | Japan Standard Time                     | JST          |
    | GMT +8    | China Taiwan Time                       | CTT          |
    | GMT +7    | Vietnam Standard Time                   | VST          |
    | GMT +6    | Bangladesh Standard Time                | BST          |
    | GMT +5:30 | India Standard Time                     | IST          |
    | GMT+5     | Pakistan Lahore Time                    | PLT          |
    | GMT +4    | Near East Time                          | NET          |
    | GMT +3:30 | Middle East Time                        | MET          |
    | GMT +3    | Eastern African Time/Arab Standard Time | EAT/AST      |
    | GMT +2    | Eastern European Time                   | EET          |
    | GMT +1    | European Central Time                   | ECT          |
    | GMT       | Greenwich Mean Time                     | GMT          |
    | GMT -1    | Central African Time                    | CAT          |
    | GMT -2    | Uruguay Summer Time                     | UYST         |
    | GMT -3    | Argentina Standard/Brazil Eastern Time  | AGT/BET      |
    | GMT -4    | Atlantic Standard Time/Puerto Rico Time | AST/PRT      |
    | GMT -5    | Eastern Standard Time                   | EST          |
    | GMT -6    | Central Standard Time                   | CST          |
    | GMT -7    | Mountain Standard Time                  | MST          |
    | GMT -8    | Pacific Standard Time                   | PST          |
    | GMT -9    | Alaskan Standard Time                   | AST          |
    | GMT -10   | Hawaiian Standard Time                  | HST          |
    | GMT -11   | Samoa Standard Time                     | SST          |
    | GMT -12   | New Zealand Standard Time               | NST          |


6.  In the **Date Format** field, select the data and time format you
    want displayed on the cards.  

    {{% imgOld 51 %}}

    The four options include the date displayed in words or abbreviated
    with numbers, and either a 12- or 24-hour time representation.

7.  Return to your workbench by clicking {{% imgOld 52 %}} and selecting a workbench from the NetQ list.

### Change Your Password

You can change your account password at any time should you suspect
someone has hacked your account or your administrator requests you to do
so.

To change your password:

1.  Click {{% imgOld 53 %}} in the application header to open the **User Settings** options.

    {{% imgOld 54 %}}

2.  Click **Profile & Preferences**.
3.  Locate the Basic Account Info card.

    {{% imgOld 55 %}}

4.  Click **Change Password**.
5.  Enter your current password.
6.  Enter and confirm a new password.

    {{% imgOld 56 %}}

7.  Click **Save** to change to the new password, or click **Cancel** to
    discard your changes.
8.  Return to your workbench by clicking {{% imgOld 57 %}} and selecting a workbench from the NetQ list.

### Manage Your Workbenches

You can view all of your workbenches in a list form, making it possible
to manage various aspects of them. There are public and private
workbenches. Public workbenches are visible by all users. Private
workbenches are visible only by the user who created the workbench. From
the Workbenches card, you can:

  - **Specify a favorite workbench**: This tells NetQ to open with that
    workbench when you log in instead of the default Cumulus Workbench.
  - **Search for a workbench**: If you have a large number of
    workbenches, you can search for a particular workbench by name, or
    sort workbenches by their access type or cards that reside on them.
  - **Delete a workbench:** Perhaps there is one that you no longer use.
    You can remove workbenches that you have created (private
    workbenches). An administrative role is required to remove
    workbenches that are common to all users (public workbenches).

    {{%notice info%}}

It is strongly recommended that you do not delete the default
    Cumulus Networks workbench. Once deleted, you must contact support
    to regain access to it. Extreme caution is recommended when deleting
    all other workbenches. Once they have been deleted, they cannot be
    restored.

    {{%/notice%}}

To manage your workbenches:

1.  Click {{% imgOld 58 %}} in the application header to open the **User Settings** options.

    {{% imgOld 59 %}}

2.  Click **Profile & Preferences**.
3.  Locate the Workbenches card.

    {{% imgOld 60 %}}

4.  To specify a favorite workbench, click and drag {{% imgOld 61 %}} next to the left of the desired workbench name.
5.  To search and/or sort the workbench list by name, access type, and
    cards present on the workbench, click the relevant header and begin
    typing your search criteria.
6.  To delete a workbench, hover over the workbench name to view the
    **Delete** button. As an administrator, you can delete both private
    and public workbenches.
7.  Return to your workbench by clicking {{% imgOld 62 %}} and selecting a workbench from the NetQ list.

## Format Cues

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

## Get Help

You can access the online user documentation for the UI from the Main
Menu. Just click {{% imgOld 63 %}} and select *Help Documentation* under the ADMIN category.
