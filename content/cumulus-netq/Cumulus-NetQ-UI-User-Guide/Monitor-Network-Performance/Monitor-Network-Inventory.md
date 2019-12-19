---
title: Monitor Network Inventory
author: Cumulus Networks
weight: 143
aliases:
 - /display/NETQ/Monitor+Network+Inventory
 - /pages/viewpage.action?pageId=12321095
pageID: 12321095
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
With NetQ, a network administrator can monitor both the switch hardware
and its operating system for misconfigurations or misbehaving services.
The Devices Inventory card workflow provides a view into the switches
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
refer to the [Monitor Switches](../../Monitor-Devices/Monitor-Switches).

## Devices Inventory Card Workflow Summary

The small Devices Inventory card displays:

{{< figure src="/images/netq/inventory-devices-small-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-locker-1.svg", height="18", width="18"/></p></td>
<td><p>Indicates data is for device inventory</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-3.svg", height="18", width="18"/></p></td>
<td><p>Total number of switches in inventory during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-choose.svg", height="18", width="18"/></p></td>
<td><p>Total number of hosts in inventory during the designated time period</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-4.svg", height="18", width="18"/></p></td>
<td><p>Total number of chassis in inventory during the designated time period. Not monitored in this release.</p></td>
</tr>
</tbody>
</table>

The medium Devices Inventory card displays:

{{< figure src="/images/netq/inventory-devices-medium-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-locker-1.svg", height="18", width="18"/></p></td>
<td><p>Indicates data is for device inventory</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p>Inventory | Devices</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-3.svg", height="18", width="18"/></p></td>
<td><p>Total number of switches in inventory during the designated time period</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-choose.svg", height="18", width="18"/></p></td>
<td><p>Total number of hosts in inventory during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Charts</p></td>
<td><p>Distribution of operating systems deployed on switches and hosts, respectively </p></td>
</tr>
</tbody>
</table>

The large Devices Inventory card has one tab.

The *Switches* tab displays:

{{< figure src="/images/netq/inventory-devices-large-switches-tab-230.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
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
<td><p><img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-locker-1.svg", height="18", width="18"/></p></td>
<td><p>Indicates data is for device inventory</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Inventory | Devices</p></td>
</tr>
<tr class="even">
<td><p>{{<img src="/images/netq/inventory-devices-large-total-number-icon-230.png" width="24" height="24">}}</p></td>
<td><p>Total number of switches in inventory during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-books.svg", height="18", width="18"/></p></td>
<td><p>Link to full screen listing of all switches</p></td>
</tr>
<tr class="even">
<td><p>Component</p></td>
<td><p>Switch components monitored–ASIC, Operating System (OS), Cumulus Linux license, NetQ Agent version, and Platform</p></td>
</tr>
<tr class="odd">
<td><p>Distribution charts</p></td>
<td><p>Distribution of switch components across the network</p></td>
</tr>
<tr class="even">
<td><p>Unique</p></td>
<td><p>Number of unique items of each component type. For example, for License, you might have CL 2.7.2 and CL 2.7.4, giving you a unique count of two.</p></td>
</tr>
</tbody>
</table>

The full screen Devices Inventory card provides tabs for all switches and all hosts.

{{< figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-230.png" width="700" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Inventory | Devices | Switches</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/></p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Time period does not apply to the Inventory cards. This is always Default Time.</p></td>
</tr>
<tr class="even">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="odd">
<td><p>All Switches and All Hosts tabs</p></td>
<td><p>Displays all monitored switches and hosts in your network. By default, the device list is sorted by <strong>hostname</strong>. These tabs provide the following additional data about each device:</p>
<ul>
<li><p><strong>Agent</strong></p>
<ul>
<li><p>State: Indicates communication state of the NetQ Agent on a given device. Values include Fresh (heard from recently) and Rotten (not heard from recently).</p></li>
<li><p>Version: Software version number of the NetQ Agent on a given device. This should match the version number of the NetQ software loaded on your server or appliance; for example, 2.1.0.</p></li>
</ul></li>
<li><p><strong>ASIC</strong></p>
<ul>
<li><p>Core BW: Maximum sustained/rated bandwidth. Example values include 2.0 T and 720 G.</p></li>
<li><p>Model: Chip family. Example values include Tomahawk, Trident, and Spectrum.</p></li>
<li><p>Model Id: Identifier of networking ASIC model. Example values include BCM56960 and BCM56854.</p></li>
<li><p>Ports: Indicates port configuration of the switch. Example values include 32 x 100G-QSFP28, 48 x 10G-SFP+, and 6 x 40G-QSFP+.</p></li>
<li><p>Vendor: Manufacturer of the chip. Example values include Broadcom and Mellanox.</p></li>
</ul></li>
<li><p><strong>CPU</strong></p>
<ul>
<li><p>Arch: Microprocessor architecture type. Values include x86_64 (Intel), ARMv7 (AMD), and PowerPC.</p></li>
<li><p>Max Freq: Highest rated frequency for CPU. Example values include 2.40 GHz and 1.74 GHz.</p></li>
<li><p>Model: Chip family. Example values include Intel Atom C2538 and Intel Atom C2338.</p></li>
<li><p>Nos: Number of cores. Example values include 2, 4, and 8.</p></li>
</ul></li>
<li><p><strong>Disk Total Size</strong>: Total amount of storage space in physical disks (not total available). Example values: 10 GB, 20 GB, 30 GB.</p></li>
<li><p><strong>License State</strong>: Indicator of validity. Values include ok and bad.</p></li>
<li><p><strong>Memory Size</strong>: Total amount of local RAM. Example values include 8192 MB and 2048 MB.</p></li>
<li><p><strong>OS</strong></p>
<ul>
<li><p>Vendor: Operating System manufacturer. Values include Cumulus Networks, RedHat, Ubuntu, and CentOS.</p></li>
<li><p>Version: Software version number of the OS. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</p></li>
<li><p>Version Id: Identifier of the OS version. For Cumulus, this is the same as the <em>Version</em> (3.7.x).</p></li>
</ul></li>
<li><p><strong>Platform</strong></p>
<ul>
<li><p>Date: Date and time the platform was manufactured. Example values include 7/12/18 and 10/29/2015.</p></li>
<li><p>MAC: System MAC address. Example value: 17:01:AB:EE:C3:F5.</p></li>
<li><p>Model: Manufacturer's model name. Examples values include AS7712-32X and S4048-ON. </span></p></li>
<li><p>Number: Manufacturer part number. Examples values include FP3ZZ7632014A, 0J09D3.</p></li>
<li><p>Revision: Release version of the platform</p></li>
<li><p>Series: Manufacturer serial number. Example values include D2060B2F044919GD000060, CN046MRJCES0085E0004.</p></li>
<li><p>Vendor: Manufacturer of the platform. Example values include Cumulus Express, Dell, EdgeCore, Lenovo, Mellanox.</p></li>
</ul></li>
<li><p><strong>Time:</strong> Date and time the data was collected from device.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## View the Number of Each Device Type in Your Network

You can view the number of switches and
hosts deployed in your network. As you grow your network this can be
useful for validating that devices have been added as scheduled.

To view the quantity of devices in your network, open the small Devices Inventory card.

{{< figure src="/images/netq/inventory-devices-small-230.png" width="200" >}}

{{%notice tip%}}

Chassis are not monitored in this release, so an N/A (not applicable)
value is displayed for these devices, even if you have chassis in your
network.

{{%/notice%}}

## View Which Operating Systems Are Running on Your Network Devices

You can view the distribution of operating systems running on your
switches and hosts. This is useful for verifying which versions of the
OS are deployed and for upgrade planning. It also provides a view into
the relative dependence on a given OS in your network.

To view the OS distribution, open the medium Devices Inventory card if
it is not already on your workbench.

{{< figure src="/images/netq/inventory-devices-medium-230.png" width="200" >}}

## View Switch Components

To view switch components, open the large Devices Inventory card. By
default the Switches tab is shown displaying the total number of
switches, ASIC vendor, OS versions, license status, NetQ Agent versions,
and specific platforms deployed on all of your switches.

{{< figure src="/images/netq/inventory-devices-large-switches-tab-230.png" width="500" >}}

### Highlight a Selected Component Type

You can hover over any of the segments in a component distribution chart
to highlight a specific type of the given component. When you *hover*, a
tooltip appears displaying:

  - the name or value of the component type, such as the version number
    or status
  - the total number of switches with that type of component deployed
    compared to the total number of switches
  - percentage of this type with respect to all component types.  

    {{< figure src="/images/netq/inventory-devices-large-switches-tab-component-highlight-230.png" width="650" >}}

Additionally, sympathetic highlighting is used to show the related
component types relevant to the highlighted segment and the number of
unique component types associated with this type (shown in blue here).

### Focus on a Selected Component Type

To dig deeper on a particular component type, you can filter the card
data by that type. In this procedure, the result of filtering on the OS
is shown.

To view component type data:

1.  Click a segment of the component distribution charts.

    {{< figure src="/images/netq/inventory-devices-large-switches-tab-component-filter.png" width="300" >}}

2.  Select the first option from the popup, *Filter* \<*component
    name*\>. The card data is filtered to show only the components
    associated with selected component type. A filter tag appears next
    to the total number of switches indicating the filter criteria.

    {{< figure src="/images/netq/inventory-devices-large-switches-tab-component-filter-os-230.png" width="250" >}}

3.  Hover over the segments to view the related components.

    {{< figure src="/images/netq/inventory-devices-large-switches-tab-component-highlight2-230.png" width="500" >}}

4.  To return to the full complement of components, click the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/> in the filter tag.

### Navigate to the Switch Inventory Workflow

While the Device Inventory cards provide a network-wide view, you may
want to see more detail about your switch inventory. This can be found
in the Switches Inventory card workflow. To open that workflow, click
the **Switch Inventory** button at the top right of the Switches card.

{{< figure src="/images/netq/inventory-devices-large-switches-tab-switch-inv-button-230.png" width="500" >}}

## View All Switches

You can view all stored attributes for all switches in your network. To
view all switch details, open the full screen Devices Inventory card and
click the **All Switches** tab in the navigation panel.

{{< figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-230.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/> in the top right corner of the card.

## View All Hosts

You can view all stored attributes for all hosts in your network. To
view all hosts details, open the full screen Devices Inventory card and
click the **All Hosts** tab in the navigation panel.

{{< figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-230.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/> in the top right corner of the card.
