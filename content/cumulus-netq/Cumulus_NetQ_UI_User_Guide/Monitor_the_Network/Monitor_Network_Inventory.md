---
title: Monitor Network Inventory
author: Cumulus Networks
weight: 127
aliases:
 - /display/NETQ/Monitor+Network+Inventory
 - /pages/viewpage.action?pageId=10456478
pageID: 10456478
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
With NetQ, a network administrator can monitor both the switch hardware
and its operating system for misconfigurations or misbehaving services.
The *Devices Inventory* card workflow provides a view into the switches
and hosts installed in your network and their various hardware and
software components. The workflow contains a small card with a count of
each device type in your network, a medium card displaying the operating
systems running on each set of devices, large cards with component
information statistics, and full-screen cards displaying tables with
attributes of all switches and all hosts in your network.

The Devices Inventory card workflow helps answer questions such as:

  - What switches do I have in the network?

  - What is the distribution of ASICs across my network?

  - Do all switches have valid licenses?

  - Are NetQ agents running on all of my switches?

For monitoring inventory and performance on a switch-by-switch basis,
refer to the <span style="color: #ff0000;"> [Monitor
Switches](/cumulus-netq/Cumulus_NetQ_UI_User_Guide/Monitor_Switches)
<span style="color: #333333;"> topic </span> </span> .

## <span>Devices Inventory Card Workflow Summary</span>

<span style="color: #36424a;"> The small Devices Inventory card
displays: </span>

{{% imgOld 0 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 1 %}}</p></td>
<td><p>Indicates data is for device inventory</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 2 %}}</p></td>
<td><p>Total number of switches in inventory during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 3 %}}</p></td>
<td><p>Total number of hosts in inventory during the designated time period</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 4 %}}</p></td>
<td><p>Total number of chassis in inventory during the designated time period. Not monitored in this release.</p></td>
</tr>
</tbody>
</table>

<span style="color: #36424a;"> The medium Devices Inventory card
displays: </span>

{{% imgOld 5 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 6 %}}</p></td>
<td><p>Indicates data is for device inventory</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p><strong>Inventory | Devices</strong></p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 7 %}}</p></td>
<td><p>Total number of switches in inventory during the designated time period</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 8 %}}</p></td>
<td><p>Total number of hosts in inventory during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 9 %}}</p></td>
<td><p>Total number of chassis in inventory during the designated time period. Not monitored in this release.</p></td>
</tr>
<tr class="even">
<td><p>Charts</p></td>
<td><p>Distribution of <span style="color: #36424a;"> operating systems deployed on switches and hosts, respectively </span></p></td>
</tr>
</tbody>
</table>

<span style="color: #36424a;"> The large Devices Inventory card has one
tab. </span>

<span style="color: #36424a;"> The *Switches* tab displays: </span>

<span style="color: #36424a;"> </span>

{{% imgOld 10 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Always Now for inventory by default</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 11 %}}</p></td>
<td><p>Indicates data is for device inventory</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Inventory | Devices</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 12 %}}</p></td>
<td><p>Total number of switches in inventory during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 13 %}}</p></td>
<td><p>Link to full screen listing of all switches</p></td>
</tr>
<tr class="even">
<td><p>Component</p></td>
<td><p>Switch components monitored–ASIC, Operating System (OS), Cumulus Linux license, NetQ Agent version, and Platform</p></td>
</tr>
<tr class="odd">
<td><p>Distribution charts</p></td>
<td><p>Distribution of <span style="color: #36424a;"> switch components across the network </span></p></td>
</tr>
<tr class="even">
<td><p>Unique</p></td>
<td><p>Number of unique items of each component type. For example, for License, you might have CL 2.7.2 and CL 2.7.4, giving you a unique count of two.</p></td>
</tr>
</tbody>
</table>

<span style="color: #36424a;"> The full screen Devices Inventory card
provides tabs for all switches and all hosts. </span>

<span style="color: #36424a;"> </span>

{{% imgOld 14 %}}

  

<span style="color: #36424a;"> View the Number of Each Device Type in
Your Network </span>

<span style="color: #36424a;"> You can view the number of switches and
hosts deployed in your network. As you grow your network this can be
useful for validating that devices have been added as scheduled. </span>

<span style="color: #36424a;"> To view the quantity of devices in your
network, o </span> <span style="color: #36424a;"> pen the small Devices
Inventory card. </span>

{{% imgOld 15 %}}

{{%notice tip%}}

Chassis are not monitored in this release, so an N/A (not applicable)
value is displayed for these devices, even if you have chassis in your
network.

{{%/notice%}}

## <span>View Which Operating Systems Are Running on Your Network Devices</span>

You can view the distribution of operating systems running on your
switches and hosts. This is useful for verifying which versions of the
OS are deployed and for upgrade planning. It also provides a view into
the relative dependence on a given OS in your network.

To view the OS distribution, open the medium Devices Inventory card if
it is not already on your workbench.

{{% imgOld 16 %}}

{{%notice tip%}}

Chassis are not monitored in this release, so an N/A (not applicable)
value is displayed for these devices, even if you have chassis in your
network.

{{%/notice%}}

## <span>View Switch Components</span>

To view switch components, open the large Devices Inventory card. By
default the Switches tab is shown displaying the total number of
switches, ASIC vendor, OS versions, license status, NetQ Agent versions,
and specific platforms deployed on all of your switches.

{{% imgOld 17 %}}

### <span>Highlight a Selected Component Type</span>

You can hover over any of the segments in a component distribution chart
to highlight a specific type of the given component. When you *hover*, a
tooltip appears displaying:

  - the name or value of the component type, such as the version number
    or status

  - the total number of switches with that type of component deployed
    compared to the total number of switches

  - percentage of this type with respect to all component types.  
    
    {{% imgOld 18 %}}
    
    {{% imgOld 19 %}}

Additionally, sympathetic highlighting is used to show the related
component types relevant to the highlighted segment and the number of
unique component types associated with this type (shown in blue here).

### <span>Focus on a Selected Component Type</span>

To dig deeper on a particular component type, you can filter the card
data by that type. In this procedure, the result of filtering on the OS
is shown.

To view component type data:

1.  *Click* a segment of the component distribution charts.
    
    {{% imgOld 20 %}}

2.  Select the first option from the popup, *Filter* \<*component
    name*\>. The card data is filtered to show only the components
    associated with selected component type. A filter tag appears next
    to the total number of switches indicating the filter criteria.
    
    {{% imgOld 21 %}}

3.  Hover over the segments to view the related components.
    
    {{% imgOld 22 %}}

4.  To return to the full complement of components, click the
    
    {{% imgOld 23 %}}
    
    in the filter tag.

### <span>Navigate to Related Cards</span>

The large Switches card provides quick links to full-screen cards in the
Device Inventory workflow.

To navigate to a related card:

1.  Click the component name or a segment of a component on the
    distribution chart.

2.  Select the desired card from the dropdown list.
    
    {{% imgOld 24 %}}

### <span>Navigate to the Switch Inventory Workflow</span>

While the Device Inventory cards provide a network-wide view, you may
want to see more detail about your switch inventory. This can be found
in the Switches Inventory card workflow. To open that workflow, click
the **Switch Inventory** button at the top right of the Switches card.

{{% imgOld 25 %}}

## <span>View All Switches</span>

You can view all stored attributes for all switches in your network. To
view all switch details, open the full screen Devices Inventory card and
click the **All Switches** tab in the navigation panel.

{{% imgOld 26 %}}

To return to your workbench, click

{{% imgOld 27 %}}

in the top right corner of the card.

## <span>View All Hosts</span>

You can view all stored attributes for all hosts in your network. To
view all hosts details, open the full screen Devices Inventory card and
click the **All Hosts** tab in the navigation panel.

{{% imgOld 28 %}}

To return to your workbench, click

{{% imgOld 29 %}}

in the top right corner of the card.
