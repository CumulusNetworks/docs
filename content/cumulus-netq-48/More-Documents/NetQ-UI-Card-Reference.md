---
title: NetQ UI Card Reference
author: NVIDIA
weight: 1120
toc: 3
pdfhidden: true
bookhidden: true
---

This reference describes the cards available in the NetQ graphical user interface (NetQ UI). You can open cards using one of two methods:

- Search for the card by name in the Global Search field in the application header
- Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}}. Select a card category or scroll down. Click the desired card. Click **Open Cards**.

Cards opened on the default NetQ Workbench are not saved. Create a new workbench and open cards there to save and view the cards at a later time.

## Events Card

The Events card appears on the default NetQ Workbench. You can also add it to user-created workbenches. Use this card to monitor events across your network. You can determine the number of events for the various systems, interfaces, devices, and network protocols and services components in the network.

The following table reflects the information in the small Events card.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/></td>
<td>Indicates data is for all events in the network.</td>
</tr>
<tr class="even">
<td>Alarm trend</td>
<td>Trend of alarm count, represented by an arrow:
<ul>
<li><strong>Pointing upward and <strong>bright pink</strong></strong>: alarm count is higher than the last two time periods, an increasing trend</li>
<li><strong>Pointing downward and <strong>green</strong></strong>: alarm count is lower than the last two time periods, a decreasing trend</li>
<li><strong>No arrow</strong>: alarm count did not change over the last two time periods, trend is steady</li>
</ul></td>
</tr>
<tr class="odd">
<td>Event type</td>
<td>Number of events, categorized by severity.</td>
</tr>
<tr class="even">
<td>Alarm rating</td>
<td>Count of alarms relative to the average count of alarms during the designated time period:
<ul>
<li><strong>Low</strong>: Count of alarms is below the average count; a nominal count</li>
<li><strong>Med</strong>: Count of alarms is in range of the average count; some room for improvement</li>
<li><strong>High</strong>: Count of alarms is above the average count; user intervention recommended</li>
</ul>
<p>{{< figure src="/images/netq/alarms-perf-rating.png" width="350" >}}</p></td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution alarms received during the designated time period and a total count of all alarms present in the system.</td>
</tr>
</tbody>
</table>

The following table reflects the information in the medium Events card.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<!-- vale off -->
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
<!-- vale on -->
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/></td>
<td>Indicates data is for all events in the network.</td>
</tr>
<tr class="odd">
<td>Count</td>
<td>Total number of events received during the designated time period.</td>
</tr>
<tr class="even">
<td>Event type</td>
<td>Number of events, categorized by severity.</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of all events received from each category during the designated time period.</td>
</tr>
</tbody>
</table>

The following table reflects the information in the large Events card.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<!-- vale off -->
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
<!-- vale on -->
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/></td>
<td>Indicates data is for all events in the network.</td>
</tr>
<tr class="odd">
<td>Event distribution</td>
<td><p><strong>Chart</strong>: Distribution of all events received from each category during the designated time period:
<ul><li>NetQ Agent</li><li>BTRFS Information</li><li>CL Support</li><li>Config Diff</li><li>Installed Packages</li><li>Link</li><li>LLDP</li><li>MTU</li><li>Node</li><li>Port</li><li>Resource</li><li>Running Config Diff</li><li>Sensor</li><li>Services</li><li>SSD Utilization</li><li>TCA Interface Stats</li><li>TCA Resource Utilization</li><li>TCA Sensors</li></ul>  
The categories sort in descending order based on total count of events, with the largest number of events appearing at the top.</p>
<p><strong>Count</strong>: Total number of events received from each category during the designated time period.</p></td>
</tr>
<tr class="even">
<td>Table</td>
<td>Listing of items that match the filter selection for the selected alarm categories:
<ul>
<li><strong>Events by Most Recent</strong>: Most-recent events appear at the top</li>
<li><strong>Devices by Event Count</strong>: Devices with the most events appear at the top</li>
</ul></td>
</tr>
<tr class="odd">
<td>View all</td>
<td>Opens full-screen Events card with a listing of all events.</td>
</tr>
</tbody>
</table>

The following table reflects the information in the full-screen Events card.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Events</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full-screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Default time</td>
<!-- vale off -->
<td>Range of time in which the displayed data was collected.</td>
<!-- vale on -->
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Filters</td>
<td>Restrict the number of results displayed in the charts and table by time, device, or severity.</td>
</tr>
<tr class="odd">
<td>Event visualizations</td>
<td>Displays events in charts and graphs that reflect the filter parameters. Select the tabs to either limit or expand the types of events reflected in the charts and graphs.
</td>
</tr>
<tr class="even">
<td>Table</td>
<td>Displays events matching the filter parameters. From here, you can select, sort, and export events. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}. You can also acknowledge events or create rules to suppress events.</td>
</tr>
</tbody>
</table>

## Inventory Cards

The inventory cards are located on the default NetQ Workbench. They can also be added to user-created workbenches.

### Inventory/Devices Card

The small Devices Inventory card displays:

{{<figure src="/images/netq/inventory-devices-small-240.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-locker-1.svg" height="18" width="18"/></td>
<td>Indicates data is for device inventory</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-3.svg" height="18" width="18"/></td>
<td>Total number of switches in inventory during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-choose.svg" height="18" width="18"/></td>
<td>Total number of hosts in inventory during the designated time period</td>
</tbody>
</table>

The medium Devices Inventory card displays:

{{<figure src="/images/netq/inventory-devices-medium-240.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-locker-1.svg" height="18" width="18"/></td>
<td>Indicates data is for device inventory</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Inventory/ Devices</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-3.svg" height="18" width="18"/></td>
<td>Total number of switches in inventory during the designated time period</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-choose.svg" height="18" width="18"/></td>
<td>Total number of hosts in inventory during the designated time period</td>
</tr>
<tr class="odd">
<td>Charts</td>
<td>Distribution of operating systems deployed on switches and hosts, respectively </td>
</tr>
</tbody>
</table>

The large Devices Inventory card has one tab.

The *Switches* tab displays:

{{<figure src="/images/netq/inventory-devices-large-switches-tab-400.png" width="500">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Always Now for inventory by default.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-locker-1.svg" height="18" width="18"/></td>
<td>Indicates data is for device inventory.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Inventory/ Devices.</td>
</tr>
<tr class="even">
<td>{{<img src="/images/netq/inventory-devices-large-total-number-icon-230.png" width="24" height="24">}}</td>
<td>Total number of switches in inventory during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-books.svg" height="18" width="18"/></td>
<td>Link to full screen listing of all switches.</td>
</tr>
<tr class="even">
<td>Component</td>
<td>Switch components monitored-ASIC, Operating System (OS), NetQ Agent version, and Platform.</td>
</tr>
<tr class="odd">
<td>Distribution charts</td>
<td>Distribution of switch components across the network.</td>
</tr>
<tr class="even">
<td>Unique</td>
<td>Number of unique items of each component type. For example, for OS, you might have Cumulus Linux 3.7.15, 4.3 and SONiC 202012, giving you a unique count of 3.</td>
</tr>
</tbody>
</table>

The full screen Devices Inventory card provides tabs for all switches and all hosts.

{{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Inventory/ Devices | Switches.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Time period does not apply to the Inventory cards. This is always Default Time.</td>
</tr>
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>All Switches and All Hosts tabs</td>
<td>Displays all monitored switches and hosts in your network. By default, the device list is sorted by <strong>hostname</strong>. These tabs provide the following additional data about each device:
<ul>
<li><strong>Agent</strong>
<ul>
<li>State: Indicates communication state of the NetQ Agent on a given device. Values include Fresh (heard from recently) and Rotten (not heard from recently).</li>
<li>Version: Software version number of the NetQ Agent on a given device. This should match the version number of the NetQ software loaded on your server or appliance; for example, 2.1.0.</li>
</ul></li>
<li><strong>ASIC</strong>
<ul>
<li>Core BW: Maximum sustained/rated bandwidth. Example values include 2.0 T and 720 G.</li>
<li>Model: Chip family. Example values include Tomahawk, Trident, and Spectrum.</li>
<li>Model Id: Identifier of networking ASIC model. Example values include BCM56960 and BCM56854.</li>
<li>Ports: Indicates port configuration of the switch. Example values include 32 x 100G-QSFP28, 48 x 10G-SFP+, and 6 x 40G-QSFP+.</li>
<li>Vendor: Manufacturer of the chip. Example values include Broadcom and Mellanox.</li>
</ul></li>
<li><strong>CPU</strong>
<ul>
<li>Arch: Microprocessor architecture type. Values include x86_64 (Intel), ARMv7 (AMD), and PowerPC.</li>
<li>Max Freq: Highest rated frequency for CPU. Example values include 2.40 GHz and 1.74 GHz.</li>
<li>Model: Chip family. Example values include Intel Atom C2538 and Intel Atom C2338.</li>
<li>Nos: Number of cores. Example values include 2, 4, and 8.</li>
</ul></li>
<li><strong>Disk Total Size</strong>: Total amount of storage space in physical disks (not total available). Example values: 10 GB, 20 GB, 30 GB.</li>
<li><strong>Memory Size</strong>: Total amount of local RAM. Example values include 8192 MB and 2048 MB.</li>
<li><strong>OS</strong>
<ul>
<li>Vendor: Operating System manufacturer. Values include Cumulus Networks, RedHat, Ubuntu, and CentOS.</li>
<li>Version: Software version number of the OS. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</li>
<li>Version Id: Identifier of the OS version. For Cumulus, this is the same as the <em>Version</em> (3.7.x).</li>
</ul></li>
<li><strong>Platform</strong>
<ul>
<li>Date: Date and time the platform was manufactured. Example values include 7/12/18 and 10/29/2015.</li>
<li>MAC: System MAC address. Example value: 17:01:AB:EE:C3:F5.</li>
<li>Model: Manufacturer's model name. Examples values include AS7712-32X and S4048-ON. </li>
<li>Number: Manufacturer part number. Examples values include FP3ZZ7632014A, 0J09D3.</li>
<li>Revision: Release version of the platform.</li>
<li>Series: Manufacturer serial number. Example values include D2060B2F044919GD000060, CN046MRJCES0085E0004.</li>
<li>Vendor: Manufacturer of the platform. Example values include Cumulus Express, Dell, EdgeCore, Lenovo, Mellanox.</li>
</ul></li>
<li><strong>Time:</strong> Date and time the data was collected from device.</li>
</ul></td>
</tr>
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### Inventory/Switch Card

Knowing what components are included on all of your switches aids in upgrade, compliance, and other planning tasks. Viewing this data is accomplished through the Switch Inventory card.

The small Switch Inventory card displays:

{{<figure src="/images/netq/inventory-switch-small-230.png" width="200">}}

| Item              | Description  |
| ----------------- | ------------ |
| <img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-books.svg" height="22" width="22"/> | Indicates data is for switch Inventory/
| Count             | Total number of switches in the network Inventory/
| Chart             | Distribution of overall health status during the designated time period; fresh versus rotten |

The medium Switch Inventory card displays:

{{<figure src="/images/netq/inventory-switch-medium-320.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-books.svg" height="22" width="22"/></td>
<td>Indicates data is for switch inventory.</td>
</tr>
<tr class="even">
<td>Filter</p></td>
<td>View fresh switches (those you have heard from recently) or rotten switches (those you have not heard from recently) on this card.</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td><p>Distribution of switch components (disk size, OS, ASIC, NetQ Agents, CPU, platform, and memory size) during the designated time period. Hover over chart segment to view versions of each component.</p>
<p><strong>Note</strong>: You should only have one version of NetQ Agent running and it should match the NetQ Platform release number. If you have more than one, you likely need to upgrade the older agents.</p></td>
</tr>
<tr class="even">
<td>Unique</td>
<td>Number of unique versions of the various switch components. For example, for OS, you might have CL 3.7.1 and CL 3.7.4 making the unique value two.</td>
</tr>
</tbody>
</table>

The large Switch Inventory card contains four tabs.

The *Summary* tab displays:

{{<figure src="/images/netq/inventory-switch-large-summary-tab-230.png" width="500">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-books.svg" height="22" width="22"/></td>
<td>Indicates data is for switch inventory.</td>
</tr>
<tr class="even">
<td>Filter</td>
<td>View fresh switches (those you have heard from recently) or rotten switches (those you have not heard from recently) on this card.</td>
</tr>
<tr class="odd">
<td>Charts</td>
<td><p>Distribution of switch components (disk size, OS, ASIC, NetQ Agents, CPU, platform, and memory size), divided into software and hardware, during the designated time period. Hover over chart segment to view versions of each component.</p>
<p><strong>Note</strong>: You should only have one version of NetQ Agent running and it should match the NetQ Platform release number. If you have more than one, you likely need to upgrade the older agents.</p></td>
</tr>
<tr class="even">
<td>Unique</td>
<td>Number of unique versions of the various switch components. For example, for OS, you might have CL 3.7.6 and CL 3.7.4 making the unique value two.</td>
</tr>
</tbody>
</table>

The *ASIC* tab displays:

{{<figure src="/images/netq/inventory-switch-large-asic-tab-230.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/08-Microprocessor-Chips/computer-chip-core-1.svg" height="20" width="20"/></td>
<td>Indicates data is for ASIC information.</td>
</tr>
<tr class="even">
<td>Filter</td>
<td>View fresh switches (those you have heard from recently) or rotten switches (those you have not heard from recently) on this card.</td>
</tr>
<tr class="odd">
<td>Vendor chart</td>
<td>Distribution of ASIC vendors. Hover over chart segment to view the number of switches with each version.</td>
</tr>
<tr class="even">
<td>Model chart</td>
<td>Distribution of ASIC models. Hover over chart segment to view the number of switches with each version.</td>
</tr>
<tr class="odd">
<td>Show All</td>
<td>Opens full screen card displaying all components for all switches.</td>
</tr>
</tbody>
</table>

The *Platform* tab displays:

{{<figure src="/images/netq/inventory-switch-large-platform-tab-230.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>{{<img src="/images/netq/platform-icon.png" height="20" width="20">}}</td>
<td>Indicates data is for platform information.</td>
</tr>
<tr class="even">
<td>Filter</td>
<td>View fresh switches (those you have heard from recently) or rotten switches (those you have not heard from recently) on this card.</td>
</tr>
<tr class="odd">
<td>Vendor chart</td>
<td>Distribution of platform vendors. Hover over chart segment to view the number of switches with each vendor.</td>
</tr>
<tr class="even">
<td>Platform chart</td>
<td>Distribution of platform models. Hover over chart segment to view the number of switches with each model.</td>
</tr>
<tr class="odd">
<td>Show All</td>
<td>Opens full screen card displaying all components for all switches.</td>
</tr>
</tbody>
</table>

The *Software* tab displays:

{{<figure src="/images/netq/inventory-switch-large-software-tab-230.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/12-CD-Rom/cd.svg" height="20" width="20"/></td>
<td>Indicates data is for software information.</td>
</tr>
<tr class="even">
<td>Filter</td>
<td>View fresh switches (those you have heard from recently) or rotten switches (those you have not heard from recently) on this card.</td>
</tr>
<tr class="odd">
<td>Operating System chart</td>
<td>Distribution of OS versions. Hover over chart segment to view the number of switches with each version.</td>
</tr>
<tr class="even">
<td>Agent Version chart</td>
<td><p>Distribution of NetQ Agent versions. Hover over chart segment to view the number of switches with each version.</p>
<p><strong>Note</strong>: You should only have one version of NetQ Agent running and it should match the NetQ Platform release number. If you have more than one, you likely need to upgrade the older agents.</p></td>
</tr>
<tr class="odd">
<td>Show All</td>
<td>Opens full screen card displaying all components for all switches.</td>
</tr>
</tbody>
</table>

The full screen Switch Inventory card provides tabs for all components, ASIC, platform, CPU, memory, disk, and OS components.

{{<figure src="/images/netq/inventory-switch-fullscr-show-all-tab-241.png" width="700">}}

## Network Health Card

As with any network, one of the challenges is keeping track of all of the moving parts. With the NetQ GUI, you can view the overall health of your network at a glance and then delve deeper for periodic checks or as conditions arise that require attention. For a general understanding of how well your network is operating, the Network Health card workflow is the best place to start as it contains the highest view and performance roll-ups.

The Network Health card is located on the default NetQ Workbench. It can also be added to user-created workbenches.

The small Network Health card displays:

{{< figure src="/images/netq/ntwk-hlth-small-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>
<img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat.svg" height="18" width="18"/></td>
<td>Indicates data is for overall Network Health</td>
</tr>
<tr class="even">
<td>Health trend</td>
<td>Trend of overall network health, represented by an arrow:
<ul>
<li><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend</li>
<li><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend</li>
<li><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady</li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td>Health score</td>
<td><p>Average of health scores for system health, network services health, and interface health during the last data collection window. The health score for each category is calculated as the percentage of items which passed validations versus the number of items checked.</p>
<p>The collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td>Health rating</td>
<td>Performance rating based on the health score during the time window:
<ul>
<li><strong>Low</strong>: Health score is less than 40%</li>
<li><strong>Med</strong>: Health score is between 40% and 70%</li>
<li><strong>High</strong>: Health score is greater than 70%</li>
</ul></td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of overall health status during the designated time period</td>
</tr>
</tbody>
</table>

The medium Network Health card displays the distribution, score, and
trend of the:

{{< figure src="/images/netq/ntwk-hlth-medium-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat.svg" height="18" width="18"/></td>
<td>Indicates data is for overall Network Health.</td>
</tr>
<tr class="odd">
<td>Health trend</td>
<td>Trend of system, network service, and interface health, represented by an arrow:
<ul>
<li><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend.</li>
<li><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend.</li>
<li><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady.</li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td>Health score</td>
<td>Percentage of devices which passed validation versus the number of devices checked during the time window for:
<ul>
<li><strong>System health</strong>: NetQ Agent health and sensors</li>
<li><strong>Network services health</strong>: BGP, CLAG, EVPN, NTP, OSPF, and VXLAN health</li>
<li><strong>Interface health</strong>: interfaces MTU, VLAN health.</li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of overall health status during the designated time period.</td>
</tr>
</tbody>
</table>

The large Network Health card contains three tabs.

The *System Health* tab displays:

{{< figure src="/images/netq/ntwk-hlth-system-hlth-lg-400.png" width="700" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/12-Apps/app-window-heart.svg" height="18" width="18"/></td>
<td>Indicates data is for System Health.</td>
</tr>
<tr class="odd">
<td>Health trend</td>
<td>Trend of NetQ Agents and sensor health, represented by an arrow:
<ul>
<li><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend.</li>
<li><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend.</li>
<li><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady.</li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td>Health score</td>
<td><p>Percentage of devices which passed validation versus the number of devices checked during the time window for NetQ Agents and platform sensors.</p>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td>Charts</td>
<td>Distribution of health score for NetQ Agents and platform sensors during the designated time period.</td>
</tr>
<tr class="even">
<td>Table</td>
<td>Listing of items that match the filter selection:
<ul>
<li><strong>Most Failures</strong>: Devices with the most validation failures are listed at the top.</li>
<li><strong>Recent Failures</strong>: Most recent validation failures are listed at the top.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Validations</td>
<td>Opens full screen Network Health card with a listing of validations performed by network service and protocol.</td>
</tr>
</tbody>
</table>

The *Network Service Health* tab displays:

{{< figure src="/images/netq/ntwk-hlth-large-ntwk-hlth-tab-241.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-heart.svg" height="18" width="18"/></td>
<td>Indicates data is for Network Protocols and Services Health.</td>
</tr>
<tr class="odd">
<td>Health trend</td>
<td>Trend of BGP, CLAG, EVPN, NTP, OSPF, and VXLAN services health, represented by an arrow:
<ul>
<li><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend.</li>
<li><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend.</li>
<li><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady.</li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td>Health score</td>
<td><p>Percentage of devices which passed validation versus the number of devices checked during the time window for BGP, CLAG, EVPN, NTP, and VXLAN protocols and services.</p>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td>Charts</td>
<td>Distribution of passing validations for BGP, CLAG, EVPN, NTP, and VXLAN services during the designated time period.</td>
</tr>
<tr class="even">
<td>Table</td>
<td>Listing of devices that match the filter selection:
<ul>
<li><strong>Most Failures</strong>: Devices with the most validation failures are listed at the top.</li>
<li><strong>Recent Failures</strong>: Most recent validation failures are listed at the top.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Validations</td>
<td>Opens full screen Network Health card with a listing of validations performed by network service and protocol.</td>
</tr>
</tbody>
</table>

The *Interface Health* tab displays:

{{< figure src="/images/netq/ntwk-hlth-large-if-hlth-tab-241.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td>{{<img src="/images/netq/ntwk-health-if-health-icon.png" height="20" width="20" >}}</td>
<td>Indicates data is for Interface Health.</td>
</tr>
<tr class="odd">
<td>Health trend</td>
<td>Trend of interfaces, VLAN, and MTU health, represented by an arrow:
<ul>
<li><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend.</li>
<li><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend.</li>
<li><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady.</li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td>Health score</td>
<td><p>Percentage of devices which passed validation versus the number of devices checked during the time window for interfaces, VLAN, and MTU protocols and ports.</p>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td>Charts</td>
<td>Distribution of passing validations for interfaces, VLAN, and MTU protocols and ports during the designated time period.</td>
</tr>
<tr class="even">
<td>Table</td>
<td>Listing of devices that match the filter selection:
<ul>
<li><strong>Most Failures</strong>: Devices with the most validation failures are listed at the top.</li>
<li><strong>Recent Failures</strong>: Most recent validation failures are listed at the top.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Validations</td>
<td>Opens full screen Network Health card with a listing of validations performed by network service and protocol.</td>
</tr>
</tbody>
</table>

The full screen Network Health card displays all events in the network.

{{< figure src="/images/netq/ntwk-hlth-fullscr-bgp-tab-241.png" width="700" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Network Health.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Default Time</td>
<td><!-- vale off -->Range of time in which the displayed data was collected.<!-- vale on --></td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>Network protocol or service tab</td>
<td>Displays results of that network protocol or service validations that occurred during the designated time period. By default, the requests list is sorted by the date and time that the validation was completed (<strong>Time</strong>). This tab provides the following additional data about all protocols and services:
<ul>
<li><strong>Validation Label</strong>: User-defined name of a validation or Default validation</li>
<li><strong>Total Node Count</strong>: Number of nodes running the protocol or service</li>
<li><strong>Checked Node Count</strong>: Number of nodes running the protocol or service included in the validation</li>
<li><strong>Failed Node Count</strong>: Number of nodes that failed the validation</li>
<li><strong>Rotten Node Count</strong>: Number of nodes that were unreachable during the validation run</li>
<li><strong>Warning Node Count</strong>: Number of nodes that had errors during the validation run</li>
</ul>
<p>The following protocols and services have additional data:<ul>
<li>BGP<ul>
<li><strong>Total Session Count</strong>: Number of sessions running BGP included in the validation</li>
<li><strong>Failed Session Count</strong>: Number of BGP sessions that failed the validation</li></ul></li>
<li>EVPN<ul>
<li><strong>Total Session Count</strong>: Number of sessions running BGP included in the validation</li>
<li><strong>Checked VNIs Count</strong>: Number of VNIs included in the validation</li>
<li><strong>Failed BGP Session Count</strong>: Number of BGP sessions that failed the validation</li></ul></li>
<li>Interfaces<ul>
<li><strong>Checked Port Count</strong>: Number of ports included in the validation</li>
<li><strong>Failed Port Count</strong>: Number of ports that failed the validation.</li>
<li><strong>Unverified Port Count</strong>: Number of ports where a peer could not be identified</li></ul></li>
<li>MTU<ul>
<li><strong>Total Link Count</strong>: Number of links included in the validation</li>
<li><strong>Failed Link Count</strong>: Number of links that failed the validation</li></ul></li>
<li>NTP<ul>
<li><strong>Unknown Node Count</strong>: Number of nodes that NetQ sees but are not in its inventory an thus not included in the validation</li></ul></li>
<li>OSPF<ul>
<li><strong>Total Adjacent Count</strong>: Number of adjacencies included in the validation</li>
<li><strong>Failed Adjacent Count</strong>: Number of adjacencies that failed the validation</li></ul></li>
<li>Sensors<ul>
<li><strong>Checked Sensor Count</strong>: Number of sensors included in the validation</li>
<li><strong>Failed Sensor Count</strong>: Number of sensors that failed the validation</li></ul></li>
<li>VLAN<ul>
<li><strong>Total Link Count</strong>: Number of links included in the validation</li>
<li><strong>Failed Link Count</strong>: Number of links that failed the validation</li></ul></li>
</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## Network Services Cards

There are two cards for each of the supported network protocols and services&mdash;one for the service as a whole and one for a given session. The network services cards can be added to user-created workbenches.

### ALL BGP Sessions Card

This card displays performance and status information for all BGP sessions across all nodes in your network.

The small BGP Service card displays:

{{< figure src="/images/netq/ntwk-svcs-all-bgp-small-300.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="even">
<td>Title</td>
<td>BGP: All BGP Sessions, or the BGP Service</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the BGP service enabled during the designated time period</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of BGP-related alarms received during the designated time period</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of new BGP-related alarms received during the designated time period</td>
</tr>
</tbody>
</table>

The medium BGP Service card displays:

{{< figure src="/images/netq/ntwk-svcs-all-bgp-medium-300.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | All BGP Sessions</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the BGP service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of BGP-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the BGP service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of nodes running BGP last week or last month might be more or less than the number of nodes running BGP currently.</p></td>
</tr>
<tr class="odd">
<td>Total Open Alarms chart</td>
<td><p>Distribution of BGP-related alarms received during the designated time period, and the total number of current BGP-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here might be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="even">
<td>Total Nodes Not Est. chart</td>
<td><p>Distribution of switches and hosts with unestablished BGP sessions during the designated time period, and the total number of unestablished sessions in the network currently.</p>
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of unestablished session last week or last month might be more of less than the number of nodes with unestablished sessions currently.</p></td>
</tr>
</tbody>
</table>

The large BGP service card contains two tabs.

The *Sessions Summary* tab displays:  

{{< figure src="/images/netq/ntwk-svcs-all-bgp-large-summary-tab-300.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Sessions Summary (visible when you hover over card).</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the BGP service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of BGP-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the BGP service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of nodes running BGP last week or last month might be more or less than the number of nodes running BGP currently.</p></td>
</tr>
<tr class="odd">
<td>Total Nodes Not Est. chart</td>
<td><p>Distribution of switches and hosts with unestablished BGP sessions during the designated time period, and the total number of unestablished sessions in the network currently.</p>
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of unestablished session last week or last month might be more of less than the number of nodes with unestablished sessions currently.</p></td>
</tr>
<tr class="even">
<td>Table/Filter options</td>
<td><p>When the <strong>Switches with Most Sessions</strong> filter option is selected, the table displays the switches and hosts running BGP sessions in decreasing order of session count-devices with the largest number of sessions are listed first.</p>
<p>When the <strong>Switches with Most Unestablished Sessions</strong> filter option is selected, the table switches and hosts running BGP sessions in decreasing order of unestablished sessions-devices with the largest number of unestablished sessions are listed first.</p></td>
</tr>
<tr class="odd">
<td>Show All Sessions</td>
<td>Link to view data for all BGP sessions in the full screen card.</td>
</tr>
</tbody>
</table>

The *Alarms* tab displays:

{{< figure src="/images/netq/ntwk-svcs-all-bgp-large-alarms-tab-300.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in header)</td>
<td>Indicates data is for all alarms for all BGP sessions.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Alarms (visible when you hover over card).</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the BGP service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in summary bar)</td>
<td>Total number of BGP-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Alarms chart</td>
<td><p>Distribution of BGP-related alarms received during the designated time period, and the total number of current BGP-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here might be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td>When the selected filter option is <strong>Switches with Most Alarms</strong>, the table displays <strong></strong> switches and hosts running BGP in decreasing order of the count of alarms-devices with the largest number of BGP alarms are listed first.</td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view data for all BGP sessions in the full screen card.</td>
</tr>
</tbody>
</table>

The full screen BGP Service card provides tabs for all switches, all sessions, and all alarms.

{{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-allsw-tab-300.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Network Services | BGP.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>All Switches tab</td>
<td>Displays all switches and hosts running the BGP service. By default, the device list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each device:
<ul>
<li><strong>Agent</strong>
<ul>
<li>State: Indicates communication state of the NetQ Agent on a given device. Values include Fresh (heard from recently) and Rotten (not heard from recently).</li>
<li>Version: Software version number of the NetQ Agent on a given device. This should match the version number of the NetQ software loaded on your server or appliance; for example, 2.2.0.</li>
</ul></li>
<li><strong>ASIC</strong>
<ul>
<li>Core BW: Maximum sustained/rated bandwidth. Example values include 2.0 T and 720 G.</li>
<li>Model: Chip family. Example values include Tomahawk, Trident, and Spectrum.</li>
<li>Model Id: Identifier of networking ASIC model. Example values include BCM56960 and BCM56854.</li>
<li>Ports: Indicates port configuration of the switch. Example values include 32 x 100G-QSFP28, 48 x 10G-SFP+, and 6 x 40G-QSFP+.</li>
<li>Vendor: Manufacturer of the chip. Example values include Broadcom and Mellanox.</li>
</ul></li>
<li><strong>CPU</strong>
<ul>
<li>Arch: Microprocessor architecture type. Values include x86_64 (Intel), ARMv7 (AMD), and PowerPC.</li>
<li>Max Freq: Highest rated frequency for CPU. Example values include 2.40 GHz and 1.74 GHz.</li>
<li>Model: Chip family. Example values include Intel Atom C2538 and Intel Atom C2338.</li>
<li>Nos: Number of cores. Example values include 2, 4, and 8.</li>
</ul></li>
<li><strong>Disk Total Size</strong>: Total amount of storage space in physical disks (not total available). Example values: 10 GB, 20 GB, 30 GB.</li>
<li><strong>Memory Size</strong>: Total amount of local RAM. Example values include 8192 MB and 2048 MB.</li>
<li><strong>OS</strong>
<ul>
<li>Vendor: Operating System manufacturer. Values include Cumulus Networks, RedHat, Ubuntu, and CentOS.</li>
<li>Version: Software version number of the OS. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</li>
<li>Version Id: Identifier of the OS version. For Cumulus, this is the same as the <em>Version</em> (3.7.x).</li>
</ul></li>
<li><strong>Platform</strong>
<ul>
<li>Date: Date and time the platform was manufactured. Example values include 7/12/18 and 10/29/2015.</li>
<li>MAC: System MAC address. Example value: 17:01:AB:EE:C3:F5.</li>
<li>Model: Manufacturer's model name. Examples values include AS7712-32X and S4048-ON. </li>
<li>Number: Manufacturer part number. Examples values include FP3ZZ7632014A, 0J09D3.</li>
<li>Revision: Release version of the platform.</li>
<li>Series: Manufacturer serial number. Example values include D2060B2F044919GD000060, CN046MRJCES0085E0004.</li>
<li>Vendor: Manufacturer of the platform. Example values include Cumulus Express, Dell, EdgeCore, Lenovo, Mellanox.</li>
</ul></li>
<li><strong>Time:</strong> Date and time the data was collected from device.</li>
</ul></td>
</tr>
<tr class="even">
<td>All Sessions tab</td>
<td>Displays all BGP sessions networkwide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
<ul>
<li><strong>ASN</strong>: Autonomous System Number, identifier for a collection of IP networks and routers. Example values include 633284,655435.</li>
<li><strong>Conn Dropped</strong>: Number of dropped connections for a given session.</li>
<li><strong>Conn Estd</strong>: Number of connections established for a given session.</li>
<li><strong>DB State</strong>: Session state of DB.</li>
<li><strong>Evpn Pfx Rcvd</strong>: Address prefix received for EVPN traffic. Examples include 115, 35.</li>
<li><strong>Ipv4, and Ipv6 Pfx Rcvd</strong>: Address prefix received for IPv4 or IPv6 traffic. Examples include 31, 14, 12.</li>
<li><strong>Last Reset Time</strong>: Date and time at which the session was last established or reset.</li>
<li><strong>Objid</strong>: Object identifier for service.</li>
<li><strong>OPID</strong>: Customer identifier. This is always zero.</li>
<li><strong>Peer</strong>
<ul>
<li>ASN: Autonomous System Number for peer device</li>
<li>Hostname: User-defined name for peer device</li>
<li>Name: Interface name or hostname of peer device</li>
<li>Router Id: IP address of router with access to the peer device</li>
</ul></li>
<li><strong>Reason</strong>: Text describing the cause of, or trigger for, an event.</li>
<li><strong>Rx and Tx Families</strong>: Address families supported for the receive and transmit session channels. Values include ipv4, ipv6, and evpn.</li>
<li><strong>State</strong>: Current state of the session. Values include Established and NotEstd (not established).</li>
<li><strong>Timestamp</strong>: Date and time session was started, deleted, updated or marked dead (device is down).</li>
<li><strong>Upd8 Rx:</strong> Count of protocol messages received.</li>
<li><strong>Upd8 Tx</strong>: Count of protocol messages transmitted.</li>
<li><strong>Up Time</strong>: Number of seconds the session has been established, in EPOCH notation. Example: 1550147910000.</li>
<li><strong>Vrf</strong>: Name of the Virtual Route Forwarding interface. Examples: default, mgmt, DataVrf1081.</li>
<li><strong>Vrfid</strong>: Integer identifier of the VRF interface when used. Examples: 14, 25, 37.</li>
</ul></td>
</tr>
<tr class="odd">
<td>All Alarms tab</td>
<td>Displays all BGP events networkwide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Message</strong>: Text description of a BGP-related event. Example: BGP session with peer tor-1 swp7 vrf default state changed from failed to Established.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>bgp</em> in this card workflow.</li>
<li><strong>Severity</strong>: Importance of the event. Values include error, warning, info, and debug.</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### BGP Session Card

This card displays performance and status information for a single BGP session. Card is opened from the full-screen Network Services/All BGP Sessions card.

The small BGP Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-bgp-small-300.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>BGP Session.</td>
</tr>
<tr class="odd">
<td><p> </p></td>
<td>Hostnames of the two devices in a session. Arrow points from the host to the peer.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Current status of the session, either established or not established.</td>
</tr>
</tbody>
</table>

The medium BGP Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-bgp-medium-300.png" width="200">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | BGP Session.</td>
</tr>
<tr class="even">
<td><p> </p></td>
<td>Hostnames of the two devices in a session. Arrow points in the direction of the session.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Current status of the session, either established or not established.</td>
</tr>
<tr class="even">
<td>Time period for chart</td>
<td>Time period for the chart data.</td>
</tr>
<tr class="odd">
<td>Session State Changes Chart</td>
<td>Heat map of the state of the given session over the given time period. The status is sampled at a rate consistent with the time period. For example, for a 24 hour period, a status is collected every hour. Refer to {{<link url="#granularity-of-data-shown-based-on-time-period" text="Granularity of Data Shown Based on Time Period">}}.</td>
</tr>
<tr class="even">
<td>Peer Name</td>
<td>Interface name on or hostname for peer device.</td>
</tr>
<tr class="odd">
<td>Peer ASN</td>
<td>Autonomous System Number for peer device.</td>
</tr>
<tr class="even">
<td>Peer Router ID</td>
<td>IP address of router with access to the peer device.</td>
</tr>
<tr class="odd">
<td>Peer Hostname</td>
<td>User-defined name for peer device.</td>
</tr>
</tbody>
</table>

The large BGP Session card contains two tabs.

The *Session Summary* tab displays:

{{<figure src="/images/netq/ntwk-svcs-single-bgp-large-summary-tab-300.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Session Summary (Network Services | BGP Session).</td>
</tr>
<tr class="even">
<td>Summary bar</td>
<td><p>Hostnames of the two devices in a session.</p>
<p>Current status of the session-either established <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, or not established <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/>.</p></td>
</tr>
<tr class="odd">
<td>Session State Changes Chart</td>
<td>Heat map of the state of the given session over the given time period. The status is sampled at a rate consistent with the time period. For example, for a 24 hour period, a status is collected every hour. Refer to {{<link url="#granularity-of-data-shown-based-on-time-period" text="Granularity of Data Shown Based on Time Period">}}.</td>
</tr>
<tr class="even">
<td>Alarm Count Chart</td>
<td>Distribution and count of BGP alarm events over the given time period.</td>
</tr>
<tr class="odd">
<td>Info Count Chart</td>
<td>Distribution and count of BGP info events over the given time period.</td>
</tr>
<tr class="even">
<td>Connection Drop Count</td>
<td>Number of times the session entered the not established state during the time period.</td>
</tr>
<tr class="odd">
<td>ASN</td>
<td>Autonomous System Number for host device.</td>
</tr>
<tr class="even">
<td>RX/TX Families</td>
<td>Receive and Transmit address types supported. Values include IPv4, IPv6, and EVPN.
</td>
</tr>
<tr class="odd">
<td>Peer Hostname</td>
<td>User-defined name for peer device.</td>
</tr>
<tr class="even">
<td>Peer Interface</td>
<td>Interface on which the session is connected.</td>
</tr>
<tr class="odd">
<td>Peer ASN</td>
<td>Autonomous System Number for peer device.</td>
</tr>
<tr class="even">
<td>Peer Router ID</td>
<td>IP address of router with access to the peer device.</td>
</tr>
</tbody>
</table>

The *Configuration File Evolution* tab displays:

{{<figure src="/images/netq/ntwk-svcs-single-bgp-large-config-tab-300.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/></td>
<td>Indicates configuration file information for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>(Network Services | BGP Session) Configuration File Evolution.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Click on <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/>.</td>
</tr>
<tr class="even">
<td>Timestamps</td>
<td>When changes to the configuration file have occurred, the date and time are indicated. Click the time to see the changed file.</td>
</tr>
<tr class="odd">
<td>Configuration File</td>
<td><p>When <strong>File</strong> is selected, the configuration file as it was at the selected time is shown.</p>
<p>When <strong>Diff</strong> is selected, the configuration file at the selected time is shown on the left and the configuration file at the previous timestamp is shown on the right. Differences are highlighted.</p>
<p><strong>Note</strong>: If no configuration file changes have been made, only the original file date is shown.</p></td>
</tr>
</tbody>
</table>

The full screen BGP Session card provides tabs for all BGP sessions and all events.

{{<figure src="/images/netq/ntwk-svcs-single-bgp-fullscr-allsess-tab-300.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="even">
<td>Title</td>
<td>Network Services | BGP.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>All BGP Sessions tab</td>
<td>Displays all BGP sessions running on the host device. This tab provides the following additional data about each session:
<ul>
<li><strong>ASN</strong>: Autonomous System Number, identifier for a collection of IP networks and routers. Example values include 633284,655435.</li>
<li><strong>Conn Dropped</strong>: Number of dropped connections for a given session.</li>
<li><strong>Conn Estd</strong>: Number of connections established for a given session.</li>
<li><strong>DB State</strong>: Session state of DB.</li>
<li><strong>Evpn Pfx Rcvd</strong>: Address prefix for EVPN traffic. Examples include 115, 35.</li>
<li><strong>Ipv4, and Ipv6 Pfx Rcvd</strong>: Address prefix for IPv4 or IPv6 traffic. Examples include 31, 14, 12.</li>
<li><strong>Last Reset Time</strong>: Time at which the session was last established or reset.</li>
<li><strong>Objid</strong>: Object identifier for service.</li>
<li><strong>OPID</strong>: Customer identifier. This is always zero.</li>
<li><strong>Peer</strong>:
<ul>
<li>ASN: Autonomous System Number for peer device</li>
<li>Hostname: User-defined name for peer device</li>
<li>Name: Interface name or hostname of peer device</li>
<li>Router Id: IP address of router with access to the peer device</li>
</ul></li>
<li><strong>Reason</strong>: Event or cause of failure.</li>
<li><strong>Rx and Tx Families</strong>: Address families supported for the receive and transmit session channels. Values include ipv4, ipv6, and evpn.</li>
<li><strong>State</strong>: Current state of the session. Values include Established and NotEstd (not established).</li>
<li><strong>Timestamp</strong>: Date and time session was started, deleted, updated or marked dead (device is down).</li>
<li><strong>Upd8 Rx:</strong> Count of protocol messages received.</li>
<li><strong>Upd8 Tx</strong>: Count of protocol messages transmitted.</li>
<li><strong>Up Time</strong>: Number of seconds the session has be established, in EPOC notation. Example: 1550147910000.</li>
<li><strong>Vrf</strong>: Name of the Virtual Route Forwarding interface. Examples: default, mgmt, DataVrf1081.</li>
<li><strong>Vrfid</strong>: Integer identifier of the VRF interface when used. Examples: 14, 25, 37.</li>
</ul></td>
</tr>
<tr class="even">
<td>All Events tab</td>
<td>Displays all events networkwide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a BGP-related event. Example: BGP session with peer tor-1 swp7 vrf default state changed from failed to Established.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include error, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of bgp in this card workflow.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

With NetQ, you can monitor the number of nodes running the EVPN service, view switches with the sessions, total number of VNIs, and alarms triggered by the EVPN service. For an overview and how to configure EVPN in your data center network, refer to {{<kb_link latest="cl" url="Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/_index.md" text="Ethernet Virtual Private Network-EVPN">}}.

### All EVPN Sessions Card

This card displays performance and status information for all EVPN sessions across all nodes in your network.

The small EVPN Service card displays:

{{<figure src="/images/netq/ntwk-svcs-all-evpn-small-230.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="even">
<td>Title</td>
<td>EVPN: All EVPN Sessions, or the EVPN Service</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the EVPN service enabled during the designated time period</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of EVPN-related alarms received during the designated time period</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of EVPN-related alarms received during the designated time period</td>
</tr>
</tbody>
</table>

The medium EVPN Service card displays:

{{<figure src="/images/netq/ntwk-svcs-all-evpn-medium-230.png" width="200">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | All EVPN Sessions.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the EVPN service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of EVPN-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the EVPN service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of nodes running EVPN last week or last month might be more or less than the number of nodes running EVPN currently.</p></td>
</tr>
<tr class="odd">
<td>Total Open Alarms chart</td>
<td><p>Distribution of EVPN-related alarms received during the designated time period, and the total number of current EVPN-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here might be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="even">
<td>Total Sessions chart</td>
<td>Distribution of EVPN sessions during the designated time period, and the total number of sessions running on the network currently.</td>
</tr>
</tbody>
</table>

The large EVPN service card contains two tabs.

The *Sessions Summary* tab which displays:

{{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-300.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Sessions Summary (visible when you hover over card).</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the EVPN service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of EVPN-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the EVPN service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of nodes running EVPN last week or last month might be more or less than the number of nodes running EVPN currently.</p></td>
</tr>
<tr class="odd">
<td>Total Sessions chart</td>
<td>Distribution of EVPN sessions during the designated time period, and the total number of sessions running on the network currently.</td>
</tr>
<tr class="even">
<td>Total L3 VNIs chart</td>
<td>Distribution of layer 3 VXLAN Network Identifiers during this time period, and the total number of VNIs in the network currently.</td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td><p>When the <strong>Top Switches with Most Sessions</strong> filter is selected, the table displays devices running EVPN sessions in decreasing order of session count-devices with the largest number of sessions are listed first.</p>
<p>When the <strong>Switches with Most L2 EVPN</strong> filter is selected, the table displays devices running layer 2 EVPN sessions in decreasing order of session count-devices with the largest number of sessions are listed first.</p>
<p>When the <strong>Switches with</strong> <strong>Most L3 EVPN</strong> filter is selected, the table displays devices running layer 3 EVPN sessions in decreasing order of session count-devices with the largest number of sessions are listed first.</p></td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view data for all EVPN sessions network-wide in the full screen card.</td>
</tr>
</tbody>
</table>

The *Alarms* tab which displays:

{{< figure src="/images/netq/ntwk-svcs-allevpn-large-alarms-tab.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in header)</td>
<td>Indicates data is for all alarms for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Alarms (visible when you hover over card).</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the EVPN service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in summary bar)</td>
<td>Total number of EVPN-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Alarms chart</td>
<td><p>Distribution of EVPN-related alarms received during the designated time period, and the total number of current BGP-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here might be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td>When the <strong>Events by Most Active Device</strong> filter is selected, the table displays devices running EVPN sessions in decreasing order of alarm count-devices with the largest number of alarms are listed first.</td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view data for all EVPN sessions in the full screen card.</td>
</tr>
</tbody>
</table>

The full screen EVPN Service card provides tabs for all switches, all sessions, all alarms.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-allsess-tab-241.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Network Services | EVPN</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>All Switches tab</td>
<td>Displays all switches and hosts running the EVPN service. By default, the device list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each device:
<ul>
<li><strong>Agent</strong>
<ul>
<li>State: Indicates communication state of the NetQ Agent on a given device. Values include Fresh (heard from recently) and Rotten (not heard from recently).</li>
<li>Version: Software version number of the NetQ Agent on a given device. This should match the version number of the NetQ software loaded on your server or appliance; for example, 2.1.0.</li>
</ul></li>
<li><strong>ASIC</strong>
<ul>
<li>Core BW: Maximum sustained/rated bandwidth. Example values include 2.0 T and 720 G.</li>
<li>Model: Chip family. Example values include Tomahawk, Trident, and Spectrum.</li>
<li>Model Id: Identifier of networking ASIC model. Example values include BCM56960 and BCM56854.</li>
<li>Ports: Indicates port configuration of the switch. Example values include 32 x 100G-QSFP28, 48 x 10G-SFP+, and 6 x 40G-QSFP+.</li>
<li>Vendor: Manufacturer of the chip. Example values include Broadcom and Mellanox.</li>
</ul></li>
<li><strong>CPU</strong>
<ul>
<li>Arch: Microprocessor architecture type. Values include x86_64 (Intel), ARMv7 (AMD), and PowerPC.</li>
<li>Max Freq: Highest rated frequency for CPU. Example values include  2.40 GHz and 1.74 GHz.</li>
<li>Model: Chip family. Example values include Intel Atom C2538 and Intel Atom C2338.</li>
<li>Nos: Number of cores. Example values include 2, 4, and 8.</li>
</ul></li>
<li><strong>Disk Total Size</strong>: Total amount of storage space in physical disks (not total available). Example values: 10 GB, 20 GB, 30 GB.</li>
<li><strong>Memory Size</strong>: Total amount of local RAM. Example values include 8192 MB and 2048 MB.</li>
<li><strong>OS</strong>
<ul>
<li>Vendor: Operating System manufacturer. Values include Cumulus Networks, RedHat, Ubuntu, and CentOS.</li>
<li>Version: Software version number of the OS. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</li>
<li>Version Id: Identifier of the OS version. For Cumulus, this is the same as the <em>Version</em> (3.7.x).</li>
</ul></li>
<li><strong>Platform</strong>
<ul>
<li>Date: Date and time the platform was manufactured. Example values include 7/12/18 and 10/29/2015.</li>
<li>MAC: System MAC address. Example value: 17:01:AB:EE:C3:F5.</li>
<li>Model: Manufacturer's model name. Examples include AS7712-32X and S4048-ON.</li>
<li>Number: Manufacturer part number. Examples values include FP3ZZ7632014A, 0J09D3.</li>
<li>Revision: Release version of the platform.</li>
<li>Series: Manufacturer serial number. Example values include D2060B2F044919GD000060, CN046MRJCES0085E0004.</li>
<li>Vendor: Manufacturer of the platform. Example values include Cumulus Express, Dell, EdgeCore, Lenovo, Mellanox.</li>
</ul></li>
<li><strong>Time:</strong> Date and time the data was collected from device.</li>
</ul></td>
</tr>
<tr class="even">
<td>All Sessions tab</td>
<td>Displays all EVPN sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
<ul>
<li><strong>Adv All Vni</strong>: Indicates whether the VNI state is advertising all VNIs (true) or not (false).</li>
<li><strong>Adv Gw Ip</strong>: Indicates whether the host device is advertising the gateway IP address (true) or not (false).</li>
<li><strong>DB State</strong>: Session state of the DB.</li>
<li><strong>Export RT</strong>: IP address and port of the export route target used in the filtering mechanism for BGP route exchange.</li>
<li><strong>Import RT</strong>: IP address and port of the import route target used in the filtering mechanism for BGP route exchange.</li>
<li><strong>In Kernel</strong>: Indicates whether the associated VNI is in the kernel (in kernel) or not (not in kernel).</li>
<li><strong>Is L3</strong>: Indicates whether the session is part of a layer 3 configuration (true) or not (false).</li>
<li><strong>Origin Ip</strong>: Host device's local VXLAN tunnel IP address for the EVPN instance.</li>
<li><strong>OPID</strong>: LLDP service identifier.</li>
<li><strong>Rd</strong>: Route distinguisher used in the filtering mechanism for BGP route exchange.</li>
<li><strong>Timestamp</strong>: Date and time the session was started, deleted, updated or marked as dead (device is down).</li>
<li><strong>Vni</strong>: Name of the VNI where session is running.</li>
</ul></td>
</tr>
<tr class="odd">
<td>All Alarms tab</td>
<td>Displays all EVPN events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a EVPN-related event. Example: VNI 3 kernel state changed from down to up.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include error, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>evpn</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### EVPN Session Card

This card displays performance and status information for a single EVPN session. Card is opened from the full-screen Network Services/All EVPN Sessions card.

The small EVPN Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-evpn-small-230.png" width="200">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for an EVPN session</td>
</tr>
<tr class="even">
<td>Title</td>
<td>EVPN Session</td>
</tr>
<tr class="odd">
<td>VNI Name</td>
<td>Name of the VNI (virtual network instance) used for this EVPN session</td>
</tr>
<tr class="even">
<td>Current VNI Nodes</td>
<td>Total number of VNI nodes participating in the EVPN session currently</td>
</tr>
</tbody>
</table>

The medium EVPN Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-evpn-medium-230.png" width="200">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for an EVPN session</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services/EVPN Session</td>
</tr>
<tr class="even">
<td>Summary bar</td>
<td>VTEP (VXLAN Tunnel EndPoint) Count: Total number of VNI nodes participating in the EVPN session currently</td>
</tr>
<tr class="odd">
<td>VTEP Count Over Time chart</td>
<td>Distribution of VTEP counts during the designated time period</td>
</tr>
<tr class="even">
<td>VNI Name</td>
<td>Name of the VNI used for this EVPN session</td>
</tr>
<tr class="odd">
<td>Type</td>
<td>Indicates whether the session is established as part of a layer 2 (L2) or layer 3 (L3) overlay network</td>
</tr>
</tbody>
</table>

The large EVPN Session card contains two tabs.

The *Session Summary* tab displays:

{{<figure src="/images/netq/ntwk-svcs-single-evpn-large-summary-tab-231.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for an EVPN session</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Session Summary (Network Services | EVPN Session)</td>
</tr>
<tr class="even">
<td>Summary bar</td>
<td>VTEP (VXLAN Tunnel EndPoint) Count: Total number of VNI devices participating in the EVPN session currently</td>
</tr>
<tr class="odd">
<td>VTEP Count Over Time chart</td>
<td>Distribution of VTEPs during the designated time period</td>
</tr>
<tr class="even">
<td>Alarm Count chart</td>
<td>Distribution of alarms during the designated time period</td>
</tr>
<tr class="odd">
<td>Info Count chart</td>
<td>Distribution of info events during the designated time period</td>
</tr>
<tr class="even">
<td>Table</td>
<td>VRF (for layer 3) or VLAN (for layer 2) identifiers by device</td>
</tr>
</tbody>
</table>

The *Configuration File Evolution* tab displays:

{{<figure src="/images/netq/ntwk-svcs-single-evpn-large-config-tab-230.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/></td>
<td>Indicates configuration file information for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>(Network Services | EVPN Session) Configuration File Evolution.</td>
</tr>
<tr class="even">
<td>{{<img src="/images/netq/ntwk-svcs-single-evpn-vtep-count-icon-230.png" width="20" height="20">}}</td>
<td>VTEP count (currently).</td>
</tr>
<tr class="odd">
<td>Timestamps</td>
<td>When changes to the configuration file have occurred, the date and time are indicated. Click the time to see the changed file.</td>
</tr>
<tr class="even">
<td>Configuration File</td>
<td><p>When <strong>File</strong> is selected, the configuration file as it was at the selected time is shown.</p>
<p>When <strong>Diff</strong> is selected, the configuration file at the selected time is shown on the left and the configuration file at the previous timestamp is shown on the right. Differences are highlighted.</p>
<p><strong>Note</strong>: If no configuration file changes have been made, only the original file date is shown.</p></td>
</tr>
</tbody>
</table>

The full screen EVPN Session card provides tabs for all EVPN sessions
and all events.

{{<figure src="/images/netq/ntwk-svcs-single-evpn-fullscr-allsess-tab-241.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Network Services | EVPN.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>All EVPN Sessions tab</td>
<td>Displays all EVPN sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
<ul>
<li><strong>Adv All Vni</strong>: Indicates whether the VNI state is advertising all VNIs (true) or not (false).</li>
<li><strong>Adv Gw Ip</strong>: Indicates whether the host device is advertising the gateway IP address (true) or not (false).</li>
<li><strong>DB State</strong>: Session state of the DB.</li>
<li><strong>Export RT</strong>: IP address and port of the export route target used in the filtering mechanism for BGP route exchange.</li>
<li><strong>Import RT</strong>: IP address and port of the import route target used in the filtering mechanism for BGP route exchange.</li>
<li><strong>In Kernel</strong>: Indicates whether the associated VNI is in the kernel (in kernel) or not (not in kernel).</li>
<li><strong>Is L3</strong>: Indicates whether the session is part of a layer 3 configuration (true) or not (false).</li>
<li><strong>Origin Ip</strong>: Host device's local VXLAN tunnel IP address for the EVPN instance.</li>
<li><strong>OPID</strong>: LLDP service identifier.</li>
<li><strong>Rd</strong>: Route distinguisher used in the filtering mechanism for BGP route exchange.</li>
<li><strong>Timestamp</strong>: Date and time the session was started, deleted, updated or marked as dead (device is down).</li>
<li><strong>Vni</strong>: Name of the VNI where session is running.</li>
</ul></td>
</tr>
<tr class="even">
<td>All Events tab</td>
<td>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a EVPN-related event. Example: VNI 3 kernel state changed from down to up.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include error, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>evpn</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### ALL LLDP Sessions Card

This card displays performance and status information for all LLDP sessions across all nodes in your network.

With NetQ, you can monitor the number of nodes running the LLDP service, view nodes with the most LLDP neighbor nodes, those nodes with the least neighbor nodes, and view alarms triggered by the LLDP service. For an overview and how to configure LLDP in your data center network, refer to {{<kb_link latest="cl" url="Layer-2/Link-Layer-Discovery-Protocol.md" text="Link Layer Discovery Protocol">}}.

The small LLDP Service card displays:

{{< figure src="/images/netq/ntwk-svcs-all-lldp-small-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>LLDP: All LLDP Sessions, or the LLDP Service.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the LLDP service enabled during the designated time period.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of LLDP-related alarms received during the designated time period.</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of LLDP-related alarms received during the designated time period.</td>
</tr>
</tbody>
</table>

The medium LLDP Service card displays:

{{< figure src="/images/netq/ntwk-svcs-all-lldp-medium.png" width="200" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>LLDP: All LLDP Sessions, or the LLDP Service.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the LLDP service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of LLDP-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the LLDP service enabled during the designated time period, and a total number of nodes running the service currently.</p>
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of nodes running LLDP last week or last month might be more or less than the number of nodes running LLDP currently.</p></td>
</tr>
<tr class="odd">
<td>Total Open Alarms chart</td>
<td><p>Distribution of LLDP-related alarms received during the designated time period, and the total number of current LLDP-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here might be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="even">
<td>Total Sessions chart</td>
<td>Distribution of LLDP sessions running during the designated time period, and the total number of sessions running on the network currently.</td>
</tr>
</tbody>
</table>

The large LLDP service card contains two tabs.

The *Sessions Summary* tab which displays:

{{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-300.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Sessions Summary (Network Services | All LLDP Sessions).</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the LLDP service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of LLDP-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the LLDP service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of nodes running LLDP last week or last month might be more or less than the number of nodes running LLDP currently.</p></td>
</tr>
<tr class="odd">
<td>Total Sessions chart</td>
<td>Distribution of LLDP sessions running during the designated time period, and the total number of sessions running on the network currently.</td>
</tr>
<tr class="even">
<td>Total Sessions with No Nbr chart</td>
<td>Distribution of LLDP sessions missing neighbor information during the designated time period, and the total number of session missing neighbors in the network currently.</td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td><p>When the <strong>Switches with Most Sessions</strong> filter is selected, the table displays switches running LLDP sessions in decreasing order of session count-devices with the largest number of sessions are listed first.</p>
<p>When the <strong>Switches with Most Unestablished Sessions</strong> filter is selected, the table displays switches running LLDP sessions in decreasing order of unestablished session count-devices with the largest number of unestablished sessions are listed first.</p></td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view all LLDP sessions in the full screen card.</td>
</tr>
</tbody>
</table>

The *Alarms* tab which displays:

{{< figure src="/images/netq/ntwk-svcs-all-lldp-large-alarms-tab.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in header)</td>
<td>Indicates data is all alarms for all LLDP sessions.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Alarms (visible when you hover over card).</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the LLDP service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in summary bar)</td>
<td>Total number of LLDP-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Alarms chart</td>
<td><p>Distribution of LLDP-related alarms received during the designated time period, and the total number of current LLDP-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here might be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td>When the <strong>Events by Most Active Device</strong> filter is selected, the table displays switches running LLDP sessions in decreasing order of alarm count-devices with the largest number of sessions are listed first</td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view all LLDP sessions in the full screen card.</td>
</tr>
</tbody>
</table>

The full screen LLDP Service card provides tabs for all switches, all sessions, and all alarms.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-allsess-tab-241.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Network Services | LLDP.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>All Switches tab</td>
<td>Displays all switches and hosts running the LLDP service. By default, the device list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each device:
<ul>
<li><strong>Agent</strong>
<ul>
<li>State: Indicates communication state of the NetQ Agent on a given device. Values include Fresh (heard from recently) and Rotten (not heard from recently).</li>
<li>Version: Software version number of the NetQ Agent on a given device. This should match the version number of the NetQ software loaded on your server or appliance; for example, 2.1.0.</li>
</ul></li>
<li><strong>ASIC</strong>
<ul>
<li>Core BW: Maximum sustained/rated bandwidth. Example values include 2.0 T and 720 G.</li>
<li>Model: Chip family. Example values include Tomahawk, Trident, and Spectrum.</li>
<li>Model Id: Identifier of networking ASIC model. Example values include BCM56960 and BCM56854.</li>
<li>Ports: Indicates port configuration of the switch. Example values include 32 x 100G-QSFP28, 48 x 10G-SFP+, and 6 x 40G-QSFP+.</li>
<li>Vendor: Manufacturer of the chip. Example values include Broadcom and Mellanox.</li>
</ul></li>
<li><strong>CPU</strong>
<ul>
<li>Arch: Microprocessor architecture type. Values include x86_64 (Intel), ARMv7 (AMD), and PowerPC.</li>
<li>Max Freq: Highest rated frequency for CPU. Example values include  2.40 GHz and 1.74 GHz.</li>
<li>Model: Chip family. Example values include Intel Atom C2538 and Intel Atom C2338.</li>
<li>Nos: Number of cores. Example values include 2, 4, and 8.</li>
</ul></li>
<li><strong>Disk Total Size</strong>: Total amount of storage space in physical disks (not total available). Example values: 10 GB, 20 GB, 30 GB.</li>
<li><strong>Memory Size</strong>: Total amount of local RAM. Example values include 8192 MB and 2048 MB.</li>
<li><strong>OS</strong>
<ul>
<li>Vendor: Operating System manufacturer. Values include Cumulus Networks, RedHat, Ubuntu, and CentOS.</li>
<li>Version: Software version number of the OS. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</li>
<li>Version Id: Identifier of the OS version. For Cumulus, this is the same as the <em>Version</em> (3.7.x).</li>
</ul></li>
<li><strong>Platform</strong>
<ul>
<li>Date: Date and time the platform was manufactured. Example values include 7/12/18 and 10/29/2015.</li>
<li>MAC: System MAC address. Example value: 17:01:AB:EE:C3:F5.</li>
<li>Model: Manufacturer's model name. Examples include AS7712-32X and S4048-ON.</li>
<li>Number: Manufacturer part number. Examples values include FP3ZZ7632014A, 0J09D3.</li>
<li>Revision: Release version of the platform.</li>
<li>Series: Manufacturer serial number. Example values include D2060B2F044919GD000060, CN046MRJCES0085E0004.</li>
<li>Vendor: Manufacturer of the platform. Example values include Cumulus Express, Dell, EdgeCore, Lenovo, Mellanox.</li>
</ul></li>
<li><strong>Time:</strong> Date and time the data was collected from device.</li>
</ul></td>
</tr>
<tr class="even">
<td>All Sessions tab</td>
<td>Displays all LLDP sessions networkwide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
<ul>
<li><strong>Ifname</strong>: Name of the host interface where LLDP session is running</li>
<li><strong>LLDP Peer</strong>:
<ul>
<li>Os: Operating system (OS) used by peer device. Values include Cumulus Linux, RedHat, Ubuntu, and CentOS.</li>
<li>Osv: Version of the OS used by peer device. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</li>
<li>Bridge: Indicates whether the peer device is a bridge (true) or not (false)</li>
<li>Router: Indicates whether the peer device is a router (true) or not (false)</li>
<li>Station: Indicates whether the peer device is a station (true) or not (false)</li>
</ul></li>
<li><strong>Peer</strong>:
<ul>
<li>Hostname: User-defined name for the peer device</li>
<li>Ifname: Name of the peer interface where the session is running</li>
</ul></li>
<li><strong>Timestamp</strong>: Date and time that the session was started, deleted, updated, or marked dead (device is down)</li>
</ul></td>
</tr>
<tr class="odd">
<td>All Alarms tab</td>
<td>Displays all LLDP events networkwide. By default, the event list is sorted by time, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a LLDP-related event. Example: LLDP Session with host leaf02 swp6 modified fields leaf06 swp21.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include error, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>lldp</em> in this card workflow.</li>
</ul></td>
</tr>
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### LLDP Session Card

This card displays performance and status information for a single LLDP session. Card is opened from the full-screen Network Services/All LLDP Sessions card.

The small LLDP Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-lldp-small-230.png" width="200">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>LLDP Session.</td>
</tr>
<tr class="odd">
<td> </td>
<td>Host and peer devices in session. Host is shown on top, with peer below.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indicates whether the host sees the peer or not; <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> has a peer, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> no peer.</td>
</tr>
</tbody>
</table>

The medium LLDP Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-lldp-medium-230.png" width="200">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td><!-- vale off -->Range of time in which the displayed data was collected.<!-- vale on --></td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>LLDP Session.</td>
</tr>
<tr class="even">
<td> </td>
<td>Host and peer devices in session. Arrow points from host to peer.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indicates whether the host sees the peer or not; <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> has a peer, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> no peer.</td>
</tr>
<tr class="even">
<td>Time period</td>
<td>Range of time for the distribution chart.</td>
</tr>
<tr class="odd">
<td>Heat map</td>
<td>Distribution of neighbor availability (detected or undetected) during this given time period.</td>
</tr>
<tr class="even">
<td>Hostname</td>
<td>User-defined name of the host device.</td>
</tr>
<tr class="odd">
<td>Interface Name</td>
<td>Software interface on the host device where the session is running.</td>
</tr>
<tr class="even">
<td>Peer Hostname</td>
<td>User-defined name of the peer device.</td>
</tr>
<tr class="odd">
<td>Peer Interface Name</td>
<td>Software interface on the peer where the session is running.</td>
</tr>
</tbody>
</table>

The large LLDP Session card contains two tabs.

The *Session Summary* tab displays:

{{<figure src="/images/netq/ntwk-svcs-single-lldp-large-summary-tab-231.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td><!-- vale off -->Range of time in which the displayed data was collected.<!-- vale on --></td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Summary Session (Network Services | LLDP Session).</td>
</tr>
<tr class="even">
<td> </td>
<td>Host and peer devices in session. Arrow points from host to peer.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indicates whether the host sees the peer or not; <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> has a peer, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> no peer.</td>
</tr>
<tr class="even">
<td>Heat map</td>
<td>Distribution of neighbor state (detected or undetected) during this given time period.</td>
</tr>
<tr class="odd">
<td>Alarm Count chart</td>
<td>Distribution and count of LLDP alarm events during the given time period.</td>
</tr>
<tr class="even">
<td>Info Count chart</td>
<td>Distribution and count of LLDP info events during the given time period.</td>
</tr>
<tr class="odd">
<td>Host Interface Name</td>
<td>Software interface on the host where the session is running.</td>
</tr>
<tr class="even">
<td>Peer Hostname</td>
<td>User-defined name of the peer device.</td>
</tr>
<tr class="odd">
<td>Peer Interface Name</td>
<td>Software interface on the peer where the session is running.</td>
</tr>
</tbody>
</table>

The *Configuration File Evolution* tab displays:

{{<figure src="/images/netq/ntwk-svcs-single-lldp-large-config-tab-230.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/></td>
<td>Indicates configuration file information for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>(Network Services | LLDP Session) Configuration File Evolution.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indicates whether the host sees the peer or not; <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> has a peer, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> no peer.</td>
</tr>
<tr class="even">
<td>Timestamps</td>
<td>When changes to the configuration file have occurred, the date and time are indicated. Click the time to see the changed file.</td>
</tr>
<tr class="odd">
<td>Configuration File</td>
<td><p>When <strong>File</strong> is selected, the configuration file as it was at the selected time is shown. When <strong>Diff</strong> is selected, the configuration file at the selected time is shown on the left and the configuration file at the previous timestamp is shown on the right. Differences are highlighted.</p>
<p><strong>Note</strong>: If no configuration file changes have been made, the card shows no results.</p></td>
</tr>
</tbody>
</table>

The full screen LLDP Session card provides tabs for all LLDP sessions and all events.

{{<figure src="/images/netq/ntwk-svcs-single-lldp-fullscr-allsess-tab-241.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Network Services | LLDP.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>All LLDP Sessions tab</td>
<td>Displays all LLDP sessions on the host device. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
<ul>
<li><strong>Ifname</strong>: Name of the host interface where LLDP session is running.</li>
<li><strong>LLDP</strong> <strong>Peer</strong>:
<ul>
<li>Os: Operating system (OS) used by peer device. Values include Cumulus Linux, RedHat, Ubuntu, and CentOS.</li>
<li>Osv: Version of the OS used by peer device. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</li>
<li>Bridge: Indicates whether the peer device is a bridge (true) or not (false).</li>
<li>Router: Indicates whether the peer device is a router (true) or not (false).</li>
<li>Station: Indicates whether the peer device is a station (true) or not (false).</li>
</ul></li>
<li><strong>Peer</strong>:
<ul>
<li>Hostname: User-defined name for the peer device.</li>
<li>Ifname: Name of the peer interface where the session is running.</li>
</ul></li>
<li><strong>Timestamp</strong>: Date and time that the session was started, deleted, updated, or marked dead (device is down).</li>
</ul></td>
</tr>
<tr class="even">
<td>All Events tab</td>
<td>Displays all events networkwide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of an event. Example: LLDP Session with host leaf02 swp6 modified fields leaf06 swp21.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include error, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>lldp</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### All MLAG Sessions Card

This card displays performance and status information for all MLAG sessions across all nodes in your network.

The small MLAG Service card displays:

{{< figure src="/images/netq/ntwk-svcs-all-mlag-small-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="even">
<td>Title</td>
<td>MLAG: All MLAG Sessions, or the MLAG Service</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the MLAG service enabled during the designated time period</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of MLAG-related alarms received during the designated time period</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of MLAG-related alarms received during the designated time period</td>
</tr>
</tbody>
</table>

The medium MLAG Service card displays:

{{< figure src="/images/netq/ntwk-svcs-all-mlag-medium-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | All MLAG Sessions.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the MLAG service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of MLAG-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/48-Maps-Navigation/11-Pins-Style%20Two/style-two-pin-off-map.svg" height="18" width="18"/></td>
<td>Total number of sessions with an inactive backup IP address during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/27-Link-Unlink/link-broken-1.svg" height="18" width="18"/></td>
<td>Total number of bonds with only a single connection during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the MLAG service enabled during the designated time period, and a total number of nodes running the service currently.</p>
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of nodes running MLAG last week or last month might be more or less than the number of nodes running MLAG currently.</p></td>
</tr>
<tr class="odd">
<td>Total Open Alarms chart</td>
<td><p>Distribution of MLAG-related alarms received during the designated time period, and the total number of current MLAG-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here might be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="even">
<td>Total Sessions chart</td>
<td>Distribution of MLAG sessions running during the designated time period, and the total number of sessions running on the network currently.</td>
</tr>
</tbody>
</table>

The large MLAG service card contains two tabs.

The *All MLAG Sessions* summary tab which displays:

{{< figure src="/images/netq/ntwk-svcs-all-mlag-large-230.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>All MLAG Sessions Summary</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the MLAG service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of MLAG-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the MLAG service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of nodes running MLAG last week or last month might be more or less than the number of nodes running MLAG currently.</p></td>
</tr>
<tr class="odd">
<td>Total Sessions chart</td>
<td><p>Distribution of MLAG sessions running during the designated time period, and the total number of sessions running on the network currently.</p></td>
</tr>
<tr class="even">
<td>Total Sessions with Inactive-backup-ip chart</td>
<td>Distribution of sessions without an active backup IP defined during the designated time period, and the total number of these sessions running on the network currently.</td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td><p>When the <strong>Switches with Most Sessions</strong> filter is selected, the table displays switches running MLAG sessions in decreasing order of session count-devices with the largest number of sessions are listed first.</p>
<p>When the <strong>Switches with Most Unestablished Sessions</strong> filter is selected, the table displays switches running MLAG sessions in decreasing order of unestablished session count-devices with the largest number of unestablished sessions are listed first.</p></td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view all MLAG sessions in the full screen card.</td>
</tr>
</tbody>
</table>

The *All MLAG Alarms* tab which displays:

{{< figure src="/images/netq/ntwk-svcs-all-mlag-large-alarms-tab-230.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in header)</td>
<td>Indicates alarm data for all MLAG sessions.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | All MLAG Alarms (visible when you hover over card).</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the MLAG service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in summary bar)</td>
<td>Total number of MLAG-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Alarms chart</td>
<td><p>Distribution of MLAG-related alarms received during the designated time period, and the total number of current MLAG-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here might be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td>When the <strong>Events by Most Active Device</strong> filter is selected, the table displays switches running MLAG sessions in decreasing order of alarm count-devices with the largest number of sessions are listed first.</td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view all MLAG sessions in the full screen card.</td>
</tr>
</tbody>
</table>

The full screen MLAG Service card provides tabs for all switches, all
sessions, and all alarms.

{{<figure src="/images/netq/ntwk-svcs-all-mlag-fullscr-allsess-tab-241.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Network Services | MLAG.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>All Switches tab</td>
<td>Displays all switches and hosts running the MLAG service. By default, the device list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each device:
<ul>
<li><strong>Agent</strong>
<ul>
<li>State: Indicates communication state of the NetQ Agent on a given device. Values include Fresh (heard from recently) and Rotten (not heard from recently).</li>
<li>Version: Software version number of the NetQ Agent on a given device. This should match the version number of the NetQ software loaded on your server or appliance; for example, 2.1.0.</li>
</ul></li>
<li><strong>ASIC</strong>
<ul>
<li>Core BW: Maximum sustained/rated bandwidth. Example values include 2.0 T and 720 G.</li>
<li>Model: Chip family. Example values include Tomahawk, Trident, and Spectrum.</li>
<li>Model Id: Identifier of networking ASIC model. Example values include BCM56960 and BCM56854.</li>
<li>Ports: Indicates port configuration of the switch. Example values include 32 x 100G-QSFP28, 48 x 10G-SFP+, and 6 x 40G-QSFP+.</li>
<li>Vendor: Manufacturer of the chip. Example values include Broadcom and Mellanox.</li>
</ul></li>
<li><strong>CPU</strong>
<ul>
<li>Arch: Microprocessor architecture type. Values include x86_64 (Intel), ARMv7 (AMD), and PowerPC.</li>
<li>Max Freq: Highest rated frequency for CPU. Example values include 2.40 GHz and 1.74 GHz.</li>
<li>Model: Chip family. Example values include Intel Atom C2538 and Intel Atom C2338.</li>
<li>Nos: Number of cores. Example values include 2, 4, and 8.</li>
</ul></li>
<li><strong>Disk Total Size</strong>: Total amount of storage space in physical disks (not total available). Example values: 10 GB, 20 GB, 30 GB.</li>
<li><strong>Memory Size</strong>: Total amount of local RAM. Example values include 8192 MB and 2048 MB.</li>
<li><strong>OS</strong>
<ul>
<li>Vendor: Operating System manufacturer. Values include Cumulus Networks, RedHat, Ubuntu, and CentOS.</li>
<li>Version: Software version number of the OS. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</li>
<li>Version Id: Identifier of the OS version. For Cumulus, this is the same as the <em>Version</em> (3.7.x).</li>
</ul></li>
<li><strong>Platform</strong>
<ul>
<li>Date: Date and time the platform was manufactured. Example values include 7/12/18 and 10/29/2015.</li>
<li>MAC: System MAC address. Example value: 17:01:AB:EE:C3:F5.</li>
<li>Model: Manufacturer's model name. Examples values include AS7712-32X and S4048-ON.</li>
<li>Number: Manufacturer part number. Examples values include FP3ZZ7632014A, 0J09D3.</li>
<li>Revision: Release version of the platform.</li>
<li>Series: Manufacturer serial number. Example values include D2060B2F044919GD000060, CN046MRJCES0085E0004.</li>
<li>Vendor: Manufacturer of the platform. Example values include Cumulus Express, Dell, EdgeCore, Lenovo, Mellanox.</li>
</ul></li>
<li><strong>Time:</strong> Date and time the data was collected from device.</li>
</ul></td>
</tr>
<tr class="even">
<td>All Sessions tab</td>
<td>Displays all MLAG sessions network-wide. By default, the session list is sorted by hostname. This tab provides the following additional data about each session:
<ul>
<li><strong>Backup Ip</strong>: IP address of the interface to use if the peerlink (or bond) goes down.</li>
<li><strong>Backup Ip Active</strong>: Indicates whether the backup IP address has been specified and is active (true) or not (false).</li>
<li><strong>Bonds</strong>
<ul>
<li>Conflicted: Identifies the set of interfaces in a bond that do not match on each end of the bond.</li>
<li>Single: Identifies a set of interfaces connecting to only one of the two switches.</li>
<li>Dual: Identifies a set of interfaces connecting to both switches.</li>
<li>Proto Down: Interface on the switch brought down by the <code>clagd</code> service. Value is blank if no interfaces are down due to <code>clagd</code> service.</li>
</ul></li>
<li><strong>Clag Sysmac</strong>: Unique MAC address for each bond interface pair. <strong>Note</strong>: Must be a value between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff.</li>
<li><strong>Peer</strong>:
<ul>
<li>If: Name of the peer interface.</li>
<li>Role: Role of the peer device. Values include primary and secondary.</li>
<li>State: Indicates if peer device is up (true) or down (false).</li>
</ul></li>
<li><strong>Role</strong>: Role of the host device. Values include primary and secondary.</li>
<li><strong>Timestamp</strong>: Date and time the MLAG session was started, deleted, updated, or marked dead (device went down).</li>
<li><strong>Vxlan Anycast</strong>: Anycast IP address used for VXLAN termination.</li>
</ul></td>
</tr>
<tr class="odd">
<td>All Alarms tab</td>
<td>Displays all MLAG events network-wide. By default, the event list is sorted by time, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a MLAG-related event. Example: Clag conflicted bond changed from swp7 swp8 to swp9 swp10.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include error, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>clag</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### MLAG Session Card

This card displays performance and status information for a single MLAG session. Card is opened from the full-screen Network Services/All MLAG Sessions card.

The small MLAG Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-mlag-small-230.png" width="200">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>CLAG Session.</td>
</tr>
<tr class="odd">
<td> </td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/>.</td>
</tr>
</tbody>
</table>

The medium MLAG Session card displays:

{{< figure src="/images/netq/ntwk-svcs-single-mlag-medium-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period (in header)</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | MLAG Session.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/>.</td>
</tr>
<tr class="even">
<td>Time period (above chart)</td>
<td>Range of time for data displayed in peer status chart.</td>
</tr>
<tr class="odd">
<td>Peer Status chart</td>
<td>Distribution of peer availability, alive or not alive, during the designated time period. The number of time segments in a time period varies according to the length of the time period.</td>
</tr>
<tr class="even">
<td>Role</td>
<td>Role that host device is playing. Values include primary and secondary.</td>
</tr>
<tr class="odd">
<td>CLAG sysmac</td>
<td>System MAC address of the MLAG session.</td>
</tr>
<tr class="even">
<td>Peer Role</td>
<td>Role that peer device is playing. Values include primary and secondary.</td>
</tr>
<tr class="odd">
<td>Peer State</td>
<td>Operational state of the peer, up (true) or down (false).</td>
</tr>
</tbody>
</table>

The large MLAG Session card contains two tabs.

The *Session Summary* tab displays:

{{< figure src="/images/netq/ntwk-svcs-single-mlag-large-sess-sum-tab-231.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>(Network Services | MLAG Session) Session Summary.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/>.</td>
</tr>
<tr class="even">
<td>Alarm Count Chart</td>
<td>Distribution and count of CLAG alarm events over the given time period.</td>
</tr>
<tr class="odd">
<td>Info Count Chart</td>
<td>Distribution and count of CLAG info events over the given time period.</td>
</tr>
<tr class="even">
<td>Peer Status chart</td>
<td>Distribution of peer availability, alive or not alive, during the designated time period. The number of time segments in a time period varies according to the length of the time period.</td>
</tr>
<tr class="odd">
<td>Backup IP</td>
<td>IP address of the interface to use if the peerlink (or bond) goes down.</td>
</tr>
<tr class="even">
<td>Backup IP Active</td>
<td>Indicates whether the backup IP address is configured.</td>
</tr>
<tr class="odd">
<td>CLAG SysMAC</td>
<td>System MAC address of the MLAG session.</td>
</tr>
<tr class="even">
<td>Peer State</td>
<td>Operational state of the peer, up (true) or down (false).</td>
</tr>
<tr class="odd">
<td>Count of Dual Bonds</td>
<td>Number of bonds connecting to both switches.</td>
</tr>
<tr class="even">
<td>Count of Single Bonds</td>
<td>Number of bonds connecting to only one switch.</td>
</tr>
<tr class="odd">
<td>Count of Protocol Down Bonds</td>
<td>Number of bonds with interfaces that were brought down by the <code>clagd</code> service.</td>
</tr>
<tr class="even">
<td>Count of Conflicted Bonds</td>
<td>Number of bonds which have a set of interfaces that are not the same on both switches.</td>
</tr>
</tbody>
</table>

The *Configuration File Evolution* tab displays:

{{< figure src="/images/netq/ntwk-svcs-single-mlag-large-config-tab-230.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/></td>
<td>Indicates configuration file information for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>(Network Services | MLAG Session) Configuration File Evolution.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/>.</td>
</tr>
<tr class="even">
<td>Timestamps</td>
<td>When changes to the configuration file have occurred, the date and time are indicated. Click the time to see the changed file.</td>
</tr>
<tr class="odd">
<td>Configuration File</td>
<td><p>When <strong>File</strong> is selected, the configuration file as it was at the selected time is shown.</p>
<p>When <strong>Diff</strong> is selected, the configuration file at the selected time is shown on the left and the configuration file at the previous timestamp is shown on the right. Differences are highlighted.</p>
</td>
</tr>
</tbody>
</table>

The full screen MLAG Session card provides tabs for all MLAG sessions
and all events.

{{<figure src="/images/netq/ntwk-svcs-single-mlag-fullscr-allsess-tab-241.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Network Services | MLAG</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/></td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab</td>
</tr>
<tr class="odd">
<td>All MLAG Sessions tab</td>
<td>Displays all MLAG sessions for the given session. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
<ul>
<li><strong>Backup Ip</strong>: IP address of the interface to use if the peerlink (or bond) goes down.</li>
<li><strong>Backup Ip Active</strong>: Indicates whether the backup IP address has been specified and is active (true) or not (false).</li>
<li><strong>Bonds</strong>
<ul>
<li>Conflicted: Identifies the set of interfaces in a bond that do not match on each end of the bond.</li>
<li>Single: Identifies a set of interfaces connecting to only one of the two switches.</li>
<li>Dual: Identifies a set of interfaces connecting to both switches.</li>
<li>Proto Down: Interface on the switch brought down by the <code>clagd</code> service. Value is blank if no interfaces are down due to <code>clagd</code> service.</li>
</ul></li>
<li><strong>Mlag Sysmac</strong>: Unique MAC address for each bond interface pair. <strong>Note</strong>: Must be a value between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff.</li>
<li><strong>Peer</strong>:
<ul>
<li>If: Name of the peer interface.</li>
<li>Role: Role of the peer device. Values include primary and secondary.</li>
<li>State: Indicates if peer device is up (true) or down (false).</li>
</ul></li>
<li><strong>Role</strong>: Role of the host device. Values include primary and secondary.</li>
<li><strong>Timestamp</strong>: Date and time the MLAG session was started, deleted, updated, or marked dead (device went down).</li>
<li><strong>Vxlan Anycast</strong>: Anycast IP address used for VXLAN termination.</li>
</ul></td>
</tr>
<tr class="even">
<td>All Events tab</td>
<td>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of an event. Example: Clag conflicted bond changed from swp7 swp8 to swp9 swp10.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include error, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>clag</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### All OSPF Sessions Card

This card displays performance and status information for all OSPF sessions across all nodes in your network.

The small OSPF Service card displays:

{{< figure src="/images/netq/ntwk-svcs-all-ospf-small-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="even">
<td>Title</td>
<td>OSPF: All OSPF Sessions, or the OSPF Service</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the OSPF service enabled during the designated time period</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of OSPF-related alarms received during the designated time period</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of OSPF-related alarms received during the designated time period</td>
</tr>
</tbody>
</table>

The medium OSPF Service card displays:

{{< figure src="/images/netq/ntwk-svcs-all-ospf-medium-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | All OSPF Sessions.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the OSPF service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of OSPF-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the OSPF service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of nodes running OSPF last week or last month might be more or less than the number of nodes running OSPF currently.</p></td>
</tr>
<tr class="odd">
<td>Total Sessions Not Established chart</td>
<td><p>Distribution of unestablished OSPF sessions during the designated time period, and the total number of unestablished sessions in the network currently.</p>
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of unestablished session last week or last month might be more of less than the number of nodes with unestablished sessions currently.</p></td>
</tr>
<tr class="even">
<td>Total Sessions chart</td>
<td>Distribution of OSPF sessions during the designated time period, and the total number of sessions running on the network currently.</td>
</tr>
</tbody>
</table>

The large OSPF service card contains two tabs.

The *Sessions Summary* tab displays:  

{{< figure src="/images/netq/ntwk-svcs-all-ospf-large-summary-tab-300.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Sessions Summary (visible when you hover over card).</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the OSPF service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of OSPF-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the OSPF service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of nodes running OSPF last week or last month might be more or less than the number of nodes running OSPF currently.</p></td>
</tr>
<tr class="odd">
<td>Total Sessions chart</td>
<td>Distribution of OSPF sessions during the designated time period, and the total number of sessions running on the network currently.</td>
</tr>
<tr class="even">
<td>Total Sessions Not Established chart</td>
<td><p>Distribution of unestablished OSPF sessions during the designated time period, and the total number of unestablished sessions in the network currently.</p>
<p><strong>Note</strong>: The node count here might be different than the count in the summary bar. For example, the number of unestablished session last week or last month might be more of less than the number of nodes with unestablished sessions currently.</p></td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td><p>When the <strong>Switches with Most Sessions</strong> filter option is selected, the table displays the switches and hosts running OSPF sessions in decreasing order of session count-devices with the largest number of sessions are listed first</p>
<p>When the <strong>Switches with Most Unestablished Sessions</strong> filter option is selected, the table switches and hosts running OSPF sessions in decreasing order of unestablished sessions-devices with the largest number of unestablished sessions are listed first</p></td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view data for all OSPF sessions in the full screen card.</td>
</tr>
</tbody>
</table>

The *Alarms* tab displays:

{{< figure src="/images/netq/ntwk-svcs-all-ospf-large-alarms-tab-230.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in header)</td>
<td>Indicates data is all alarms for all OSPF sessions.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Alarms (visible when you hover over card).</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the OSPF service enabled during the designated time period.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in summary bar)</td>
<td>Total number of OSPF-related alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Total Alarms chart</td>
<td><p>Distribution of OSPF-related alarms received during the designated time period, and the total number of current OSPF-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here might be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td>When the selected filter option is <strong>Switches with Most Alarms</strong>, the table displays <strong></strong> switches and hosts running OSPF in decreasing order of the count of alarms-devices with the largest number of OSPF alarms are listed first</td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view data for all OSPF sessions in the full screen card.</td>
</tr>
</tbody>
</table>

The full screen OSPF Service card provides tabs for all switches, all sessions, and all alarms.

{{<figure src="/images/netq/ntwk-svcs-all-ospf-fullscr-allswitches-tab-241.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Network Services | OSPF.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab</td>
</tr>
<tr class="odd">
<td>All Switches tab</td>
<td>Displays all switches and hosts running the OSPF service. By default, the device list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each device:
<ul>
<li><strong>Agent</strong>
<ul>
<li>State: Indicates communication state of the NetQ Agent on a given device. Values include Fresh (heard from recently) and Rotten (not heard from recently).</li>
<li>Version: Software version number of the NetQ Agent on a given device. This should match the version number of the NetQ software loaded on your server or appliance; for example, 2.1.0.</li>
</ul></li>
<li><strong>ASIC</strong>
<ul>
<li>Core BW: Maximum sustained/rated bandwidth. Example values include 2.0 T and 720 G.</li>
<li>Model: Chip family. Example values include Tomahawk, Trident, and Spectrum.</li>
<li>Model Id: Identifier of networking ASIC model. Example values include BCM56960 and BCM56854.</li>
<li>Ports: Indicates port configuration of the switch. Example values include 32 x 100G-QSFP28, 48 x 10G-SFP+, and 6 x 40G-QSFP+.</li>
<li>Vendor: Manufacturer of the chip. Example values include Broadcom and Mellanox.</li>
</ul></li>
<li><strong>CPU</strong>
<ul>
<li>Arch: Microprocessor architecture type. Values include x86_64 (Intel), ARMv7 (AMD), and PowerPC.</li>
<li>Max Freq: Highest rated frequency for CPU. Example values include 2.40 GHz and 1.74 GHz.</li>
<li>Model: Chip family. Example values include Intel Atom C2538 and Intel Atom C2338.</li>
<li>Nos: Number of cores. Example values include 2, 4, and 8.</li>
</ul></li>
<li><strong>Disk Total Size</strong>: Total amount of storage space in physical disks (not total available). Example values: 10 GB, 20 GB, 30 GB.</li>
<li><strong>Memory Size</strong>: Total amount of local RAM. Example values include 8192 MB and 2048 MB.</li>
<li><strong>OS</strong>
<ul>
<li>Vendor: Operating System manufacturer. Values include Cumulus Networks, RedHat, Ubuntu, and CentOS.</li>
<li>Version: Software version number of the OS. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</li>
<li>Version Id: Identifier of the OS version. For Cumulus, this is the same as the <em>Version</em> (3.7.x).</li>
</ul></li>
<li><strong>Platform</strong>
<ul>
<li>Date: Date and time the platform was manufactured. Example values include 7/12/18 and 10/29/2015.</li>
<li>MAC: System MAC address. Example value: 17:01:AB:EE:C3:F5.</li>
<li>Model: Manufacturer's model name. Examples values include AS7712-32X and S4048-ON.</li>
<li>Number: Manufacturer part number. Examples values include FP3ZZ7632014A, 0J09D3.</li>
<li>Revision: Release version of the platform.</li>
<li>Series: Manufacturer serial number. Example values include D2060B2F044919GD000060, CN046MRJCES0085E0004.</li>
<li>Vendor: Manufacturer of the platform. Example values include Cumulus Express, Dell, EdgeCore, Lenovo, Mellanox.</li>
</ul></li>
<li><strong>Time:</strong> Date and time the data was collected from device.</li>
</ul></td>
</tr>
<tr class="even">
<td>All Sessions tab</td>
<td>Displays all OSPF sessions networkwide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
<ul>
<li><strong>Area</strong>: Routing domain for this host device. Example values include 0.0.0.1, 0.0.0.23.</li>
<li><strong>Ifname</strong>: Name of the interface on host device where session resides. Example values include swp5, peerlink-1.</li>
<li><strong>Is IPv6</strong>: Indicates whether the address of the host device is IPv6 (true) or IPv4 (false).</li>
<li><strong>Peer</strong>
<ul>
<li>Address: IPv4 or IPv6 address of the peer device.</li>
<li>Hostname: User-defined name for peer device.</li>
<li>ID: Network subnet address of router with access to the peer device.</li>
</ul></li>
<li><strong>State</strong>: Current state of OSPF. Values include Full, 2-way, Attempt, Down, Exchange, Exstart, Init, and Loading.</li>
<li><strong>Timestamp</strong>: Date and time session was started, deleted, updated or marked dead (device is down)</li>
</ul></td>
</tr>
<tr class="odd">
<td>All Alarms tab</td>
<td>Displays all OSPF events networkwide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a OSPF-related event. Example: swp4 area ID mismatch with peer leaf02</li>
<li><strong>Source</strong>: Hostname of network device that generated the event</li>
<li><strong>Severity</strong>: Importance of the event. Values include error, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>OSPF</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### OSPF Session Card

This card displays performance and status information for a single OSPF session. Card is opened from the full-screen Network Services/All OSPF Sessions card.

The small OSPF Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-ospf-small-230.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>OSPF Session.</td>
</tr>
<tr class="odd">
<td> </td>
<td>Hostnames of the two devices in a session. Host appears on top with peer below.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Current state of OSPF. <br>
<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> Full or <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/> 2-way, Attempt, Down, Exchange, Exstart, Init, and Loading.</td>
</tr>
</tbody>
</table>

The medium OSPF Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-ospf-medium-230.png" width="200">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | OSPF Session.</td>
</tr>
<tr class="even">
<td> </td>
<td>Hostnames of the two devices in a session. Host appears on top with peer below.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Current state of OSPF.<br>
<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> Full or <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/> 2-way, Attempt, Down, Exchange, Exstart, Init, and Loading.</td>
</tr>
<tr class="even">
<td>Time period for chart</td>
<td>Time period for the chart data.</td>
</tr>
<tr class="odd">
<td>Session State Changes Chart</td>
<td>Heat map of the state of the given session over the given time period. The status is sampled at a rate consistent with the time period. For example, for a 24 hour period, a status is collected every hour. Refer to {{<link url="#granularity-of-data-shown-based-on-time-period" text="Granularity of Data Shown Based on Time Period">}}.</td>
</tr>
<tr class="even">
<td>Ifname</td>
<td>Interface name on or hostname for host device where session resides.</td>
</tr>
<tr class="odd">
<td>Peer Address</td>
<td>IP address of the peer device.</td>
</tr>
<tr class="even">
<td>Peer ID</td>
<td>IP address of router with access to the peer device.</td>
</tr>
</tbody>
</table>

The large OSPF Session card contains two tabs.

The *Session Summary* tab displays:

{{<figure src="/images/netq/ntwk-svcs-single-ospf-large-summary-tab-231.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr>
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol.</td>
</tr>
<tr>
<td>Title</td>
<td>Session Summary (Network Services | OSPF Session).</td>
</tr>
<tr>
<td>Summary bar</td>
<td><p>Hostnames of the two devices in a session. Arrow points in the direction of the session.</p>
<p>Current state of OSPF. <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> Full or <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/> 2-way, Attempt, Down, Exchange, Exstart, Init, and Loading.</p></td>
</tr>
<tr>
<td>Session State Changes Chart</td>
<td>Heat map of the state of the given session over the given time period. The status is sampled at a rate consistent with the time period. For example, for a 24 hour period, a status is collected every hour. Refer to {{<link url="#granularity-of-data-shown-based-on-time-period" text="Granularity of Data Shown Based on Time Period">}}.</td>
</tr>
<tr>
<td>Alarm Count Chart</td>
<td>Distribution and count of OSPF alarm events over the given time period.</td>
</tr>
<tr>
<td>Info Count Chart</td>
<td>Distribution and count of OSPF info events over the given time period.</td>
</tr>
<tr>
<td>Ifname</td>
<td>Name of the interface on the host device where the session resides.</td>
</tr>
<tr>
<td>State</td>
<td>Current state of OSPF. <br><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> Full or <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/> 2-way, Attempt, Down, Exchange, Exstart, Init, and Loading.</td>
</tr>
<tr>
<td>Is Unnumbered</td>
<td>Indicates if the session is part of an unnumbered OSPF configuration (true) or part of a numbered OSPF configuration (false).</td>
</tr>
<tr>
<td>Nbr Count</td>
<td>Number of routers in the OSPF configuration.</td>
</tr>
<tr>
<td>Is Passive</td>
<td>Indicates if the host is in a passive state (true) or active state (false).</td>
</tr>
<tr>
<td>Peer ID</td>
<td>IP address of router with access to the peer device.</td>
</tr>
<tr>
<td>Is IPv6</td>
<td>Indicates if the IP address of the host device is IPv6 (true) or IPv4 (false).</td>
</tr>
<tr>
<td>If Up</td>
<td>Indicates if the interface on the host is up (true) or down (false).</td>
</tr>
<tr>
<td>Nbr Adj Count</td>
<td>Number of adjacent routers for this host.</td>
</tr>
<tr>
<td>MTU</td>
<td>Maximum transmission unit (MTU) on shortest path between the host and peer.</td>
</tr>
<tr>
<td>Peer Address</td>
<td>IP address of the peer device.</td>
</tr>
<tr>
<td>Area</td>
<td>Routing domain of the host device.</td>
</tr>
<tr>
<td>Network Type</td>
<td>Architectural design of the network. Values include Point-to-Point and Broadcast.</td>
</tr>
<tr>
<td>Cost</td>
<td>Shortest path through the network between the host and peer devices.</td>
</tr>
<tr>
<td>Dead Time</td>
<td>
Countdown timer, starting at 40 seconds, that is constantly reset as messages are heard from the neighbor. If the dead time gets to zero, the neighbor is presumed dead, the adjacency is torn down, and the link removed from SPF calculations in the OSPF database.</td>
</tr>
</tbody>
</table>

The *Configuration File Evolution* tab displays:

{{<figure src="/images/netq/ntwk-svcs-single-ospf-large-config-tab-file-selected-230.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/></td>
<td>Indicates configuration file information for a single session of a Network Service or Protocol.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>(Network Services | OSPF Session) Configuration File Evolution.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Current state of OSPF.<br>
<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> Full or <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/> 2-way, Attempt, Down, Exchange, Exstart, Init, and Loading.</td>
</tr>
<tr class="even">
<td>Timestamps</td>
<td>When changes to the configuration file have occurred, the date and time are indicated. Click the time to see the changed file.</td>
</tr>
<tr class="odd">
<td>Configuration File</td>
<td><p>When <strong>File</strong> is selected, the configuration file as it was at the selected time is shown.</p>
<p> When <strong>Diff</strong> is selected, the configuration file at the selected time is shown on the left and the configuration file at the previous timestamp is shown on the right. Differences are highlighted.</p></td>
</tr>
</tbody>
</table>

The full screen OSPF Session card provides tabs for all OSPF sessions
and all events.

{{<figure src="/images/netq/ntwk-svcs-single-ospf-fullscr-sessions-tab-222.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Network Services | OSPF.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>All OSPF Sessions tab</td>
<td>Displays all OSPF sessions running on the host device. The session list is sorted by <strong>hostname</strong> by default. This tab provides the following additional data about each session:
<ul>
<li><strong>Area</strong>: Routing domain for this host device. Example values include 0.0.0.1, 0.0.0.23.</li>
<li><strong>Ifname</strong>: Name of the interface on host device where session resides. Example values include swp5, peerlink-1.</li>
<li><strong>Is IPv6</strong>: Indicates whether the address of the host device is IPv6 (true) or IPv4 (false).</li>
<li><strong>Peer</strong>
<ul>
<li>Address: IPv4 or IPv6 address of the peer device.</li>
<li>Hostname: User-defined name for peer device.</li>
<li>ID: Network subnet address of router with access to the peer device.</li>
</ul></li>
<li><strong>State</strong>: Current state of OSPF. Values include Full, 2-way, Attempt, Down, Exchange, Exstart, Init, and Loading.</li>
<li><strong>Timestamp</strong>: Date and time session was started, deleted, updated or marked dead (device is down).</li>
</ul></td>
</tr>
<tr class="even">
<td>All Events tab</td>
<td>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a OSPF-related event. Example: OSPF session with peer tor-1 swp7 vrf default state changed from failed to Established.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include error, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of OSPF in this card workflow.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## Switch Card

Viewing detail about a particular switch is essential when troubleshooting performance issues. With NetQ you can view the overall performance and drill down to view attributes of the switch, interface performance and the events associated with a switch. This is accomplished through the Switches card.

Switch cards can be added to user-created workbenches. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} to open a device card.

The small Switch card displays:

{{<figure src="/images/netq/dev-switch-small-card-230.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="24" width="24"/></td>
<td>Indicates data is for a single switch.</td>
</tr>
<tr class="even">
<td>title</td>
<td>Hostname of switch.</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of switch alarms during the designated time period.</td>
</tr>
<tr class="even">
<td>Trend</td>
<td>Trend of alarm count, represented by an arrow:
<ul>
<li><strong>Pointing upward and green</strong>: alarm count is higher than the last two time periods, an increasing trend.</li>
<li><strong>Pointing downward and bright pink</strong>: alarm count is lower than the last two time periods, a decreasing trend.</li>
<li><strong>No arrow</strong>: alarm count is unchanged over the last two time periods, trend is steady.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Count</td>
<td>Current count of alarms on the switch.</td>
</tr>
<tr class="even">
<td>Rating</td>
<td>Overall performance of the switch. Determined by the count of alarms relative to the average count of alarms during the designated time period:
<ul>
<li><strong>Low</strong>: Count of alarms is below the average count; a nominal count.</li>
<li><strong>Med</strong>: Count of alarms is in range of the average count; some room for improvement.</li>
<li><strong>High</strong>: Count of alarms is above the average count; user intervention recommended.</li>
</ul>
<p>{{< figure src="/images/netq/alarms-perf-rating.png" width="350" >}}</p></td>
</tr>
</tbody>
</table>

The medium Switch card displays:

{{<figure src="/images/netq/dev-switch-medium-alarms-charts-231.png" width="420">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="24" width="24"/></td>
<td>Indicates data is for a single switch.</td>
</tr>
<tr class="even">
<td>title</td>
<td>Hostname of switch.</td>
</tr>
<tr class="odd">
<td>Alarms</td>
<td>When selected, displays distribution and count of alarms by alarm category, generated by this switch during the designated time period.</td>
</tr>
<tr class="even">
<td>Charts</p></td>
<td>When selected, displays distribution of alarms by alarm category, during the designated time period.</td>
</tr>
</tbody>
</table>

The large Switch card contains four tabs:

The *Attributes* tab displays:

{{<figure src="/images/netq/dev-switch-large-attributes-tab-320.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="24" width="24"/></td>
<td>Indicates data is for a single switch.</td>
</tr>
<tr class="even">
<td>title</td>
<td>&lt;Hostname&gt; | Attributes.</td>
</tr>
<tr class="odd">
<td>Hostname</td>
<td>User-defined name for this switch.</td>
</tr>
<tr class="even">
<td>Management IP</td>
<td>IPv4 or IPv6 address used for management of this switch.</td>
</tr>
<tr class="odd">
<td>Management MAC</td>
<td>MAC address used for management of this switch.</td>
</tr>
<tr class="even">
<td>Agent State</td>
<td>Operational state of the NetQ Agent on this switch; Fresh or Rotten.</td>
</tr>
<tr class="odd">
<td>Platform Vendor</td>
<td>Manufacturer of this switch box. Cumulus Networks is identified as the vendor for a switch in the Cumulus in the Cloud (CITC) environment, as seen here.</td>
</tr>
<tr class="even">
<td>Platform Model</td>
<td>Manufacturer model of this switch. VX is identified as the model for a switch in CITC environment, as seen here.</td>
</tr>
<tr class="odd">
<td>ASIC Vendor</td>
<td>Manufacturer of the ASIC installed on the motherboard.</td>
</tr>
<tr class="even">
<td>ASIC Model</td>
<td>Manufacturer model of the ASIC installed on the motherboard.</td>
</tr>
<tr class="odd">
<td>OS</td>
<td>Operating system running on the switch. CL indicates Cumulus Linux is installed.</td>
</tr>
<tr class="even">
<td>OS Version</td>
<td>Version of the OS running on the switch.</td>
</tr>
<tr class="odd">
<td>NetQ Agent Version</td>
<td>Version of the NetQ Agent running on the switch.</td>
</tr>
<tr class="even">
<td>Total Interfaces</td>
<td>Total number of interfaces on this switch, and the number of those that are up and down.</td>
</tr>
</tbody>
</table>

The *Utilization* tab displays:

{{<figure src="/images/netq/dev-switch-large-utilization-tab-320.png" width="500">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/06-Business-Products/12-Analytics/analytics-bars.svg" height="24" width="24"/></td>
<td>Indicates utilization data is for a single switch.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>&lt;Hostname&gt; | Utilization.</td>
</tr>
<tr class="odd">
<td>Performance</td>
<td>Displays distribution of CPU and memory usage during the designated time period.</td>
</tr>
<tr class="even">
<td>Disk Utilization</td>
<td>Displays distribution of disk usage during the designated time period.</td>
</tr>
</tbody>
</table>

The *Interfaces* tab displays:

{{<figure src="/images/netq/dev-switch-large-interfaces-tab-320.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/07-Data-Transfer/data-transfer-square-diagonal.svg" width="18" height="18"/></td>
<td>Indicates interface statistics for a single switch.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>&lt;Hostname&gt; | Interface Stats.</td>
</tr>
<tr class="odd">
<td>Interface List</td>
<td>List of interfaces present during the designated time period.</td>
</tr>
<tr class="even">
<td>Interface Filter</td>
<td>Sorts interface list by Name, Rx Util (receive utilization), or Tx Util (transmit utilization).</td>
</tr>
<tr class="odd">
<td>Interfaces Count</td>
<td>Number of interfaces present during the designated time period.</td>
</tr>
<tr class="even">
<td>Interface Statistics</td>
<td>Distribution and current value of various transmit and receive statistics associated with a selected interface:
<ul><li><strong>Broadcast</strong>: Number of broadcast packets</li>
<li><strong>Bytes</strong>: Number of bytes per second</li>
<li><strong>Drop</strong>: Number of dropped packets</li>
<li><strong>Errs</strong>: Number of errors</li>
<li><strong>Frame</strong>: Number of frames received</li>
<li><strong>Multicast</strong>: Number of multicast packets</li>
<li><strong>Packets</strong>: Number of packets per second</li>
<li><strong>Utilization</strong>: Bandwidth utilization as a percentage of total available bandwidth</li></ul></td>
</tr>
</tbody>
</table>

The *Digital Optics* tab displays:

{{<figure src="/images/netq/dev-switch-large-dom-tab-320.png" width="500">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>{{<img src="/images/netq/dom.svg" width="18" height="18" >}}</td>
<td>Indicates digital optics metrics for a single switch.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>&lt;Hostname&gt; | Digital Optics.</td>
</tr>
<tr class="odd">
<td>Interface List</td>
<td>List of interfaces present during the designated time period.</td>
</tr>
<tr class="even">
<td>Search</td>
<td>Search for an interface by Name.</td>
</tr>
<tr class="odd">
<td>Interfaces Count</td>
<td>Number of interfaces present during the designated time period.</td>
</tr>
<tr class="even">
<td>Digital Optics Statistics</td>
<td>Use the parameter dropdown to change the chart view to see metrics for Laser RX Power, Laser Output Power, Laser Bias Current, Module Temperature, and Module Voltage.</td>
</tr>
</tbody>
</table>

The full screen Switch card provides multiple tabs.

{{<figure src="/images/netq/dev-switch-fullscr-alarms-tab-320.png" width="700">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>&lt;hostname&gt;</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Default Time</td>
<td>Displayed data is current as of this moment.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>Alarms</td>
<td>Displays all known critical alarms for the switch. This tab provides the following additional data about each address:
<ul>
<li><strong>Hostname</strong>: User-defined name of the switch</li>
<li><strong>Message</strong>: Description of alarm</li>
<li><strong>Message Type</strong>: Indicates the protocol or service which generated the alarm</li>
<li><strong>Severity</strong>: Indicates the level of importance of the event; it is always critical for NetQ alarms</li>
<li><strong>Time</strong>: Date and time the data was collected</li>
</ul></td>
</tr>
<tr class="even">
<td>All Interfaces</td>
<td>Displays all known interfaces on the switch. This tab provides the following additional data about each interface:
<ul>
<li><strong>Details</strong>: Information about the interface, such as MTU, table number, members, protocols running, VLANs</li>
<li><strong>Hostname</strong>: Hostname of the given event</li>
<li><strong>IfName</strong>: Name of the interface</li>
<li><strong>Last Changed</strong>: Data and time that the interface was last enabled, updated, deleted, or changed state to down</li>
<li><strong>OpId</strong>: Process identifier; for internal use only</li>
<li><strong>State</strong>: Indicates if the interface is <em>up</em> or <em>down</em></li>
<li><strong>Time</strong>: Date and time the data was collected</li>
<li><strong>Type</strong>: Kind of interface; for example, VRF, switch port, loopback, ethernet</li>
<li><strong>VRF</strong>: Name of the associated virtual route forwarding (VRF) interface if deployed</li>
</ul></td>
</tr>
<tr class="odd">
<td>MAC Addresses</td>
<td>Displays all known MAC addresses for the switch. This tab provides the following additional data about each MAC address:
<ul>
<li><strong>Egress Port</strong>: Importance of the event-error, warning, info, or debug</li>
<li><strong>Hostname</strong>: User-defined name of the switch</li>
<li><strong>Last Changed</strong>: Data and time that the address was last updated or deleted</li>
<li><strong>MAC Address</strong>: MAC address of switch</li>
<li><strong>Origin</strong>: Indicates whether this switch owns this address (true) or if another switch owns this address (false)</li>
<li><strong>Remote</strong>: Indicates whether this address is reachable via a VXLAN on another switch (true) or is reachable locally on the switch (false)</li>
<li><strong>Time</strong>: Date and time the data was collected</li>
<li><strong>VLAN Id</strong>: Identifier of an associated VLAN if deployed</li>
</ul></td>
</tr>
<tr class="even">
<td>VLANs</td>
<td>Displays all configured VLANs on the switch. This tab provides the following additional data about each VLAN:
<ul>
<li><strong>Hostname</strong>: User-defined name of the switch</li>
<li><strong>IfName</strong>: Name of the interface</li>
<li><strong>Last Changed</strong>: Data and time that the VLAN was last updated or deleted</li>
<li><strong>Ports</strong>: Ports used by the VLAN</li>
<li><strong>SVI</strong>: Indicates whether is the VLAN has a switch virtual interface (yes) or not (no)</li>
<li><strong>Time</strong>: Date and time the data was collected</li>
<li><strong>VLANs</strong>: Name of the VLAN</li>
</ul></td>
</tr>
<tr class="odd">
<td>IP Routes</td>
<td>Displays all known IP routes for the switch. This tab provides the following additional data about each route:
<ul>
<li><strong>Hostname</strong>: User-defined name of the switch</li>
<li><strong>Is IPv6</strong>: Indicates whether the route is based on an IPv6 address (true) or an IPv4 address (false)</li>
<li><strong>Message Type</strong>: Service type; always route</li>
<li><strong>NextHops</strong>: List of hops in the route</li>
<li><strong>Origin</strong>: Indicates whether the route is owned by this switch (true) or not (false)</li>
<li><strong>Prefix</strong>: Prefix for the address</li>
<li><strong>Priority</strong>: Indicates the importance of the route; higher priority is used before lower priority</li>
<li><strong>Route Type</strong>: Kind of route, where the type is dependent on the protocol</li>
<li><strong>RT Table Id</strong>: Identifier of the routing table that contains this route</li>
<li><strong>Source</strong>: Address of source switch; *None* if this switch is the source</li>
<li><strong>Time</strong>: Date and time the data was collected</li>
<li><strong>VRF</strong>: Name of the virtual route forwarding (VRF) interface if used by the route</li>
</ul></td>
</tr>
<tr class="even">
<td>IP Neighbors</td>
<td>Displays all known IP neighbors of the switch. This tab provides the following additional data about each neighbor:
<ul>
<li><strong>Hostname</strong>: User-defined name of the switch</li>
<li><strong>IfIndex</strong>: Index of the interface</li>
<li><strong>IfName</strong>: Name of the interface</li>
<li><strong>IP Address</strong>: IP address of the neighbor</li>
<li><strong>Is IPv6</strong>: Indicates whether the address is an IPv6 address (true) or an IPv4 address (false)</li>
<li><strong>Is Remote</strong>: Indicates whether this address is reachable via a VXLAN on another switch (true) or is reachable locally on the switch (false)</li>
<li><strong>MAC Address</strong>: MAC address of neighbor</li>
<li><strong>Message Type</strong>: Service type; always neighbor</li>
<li><strong>OpId</strong>: Process identifier; for internal use only</li>
<li><strong>Time</strong>: Date and time the data was collected</li>
<li><strong>VRF</strong>: Name of the virtual route forwarding (VRF) interface if deployed</li>
</ul></td>
</tr>
<tr class="odd">
<td>IP Addresses</td>
<td>Displays all known IP addresses for the switch. This tab provides the following additional data about each address:
<ul>
<li><strong>Hostname</strong>: User-defined name of the switch</li>
<li><strong>IfName</strong>: Name of the interface</li>
<li><strong>Is IPv6</strong>: Indicates whether the address is an IPv6 address (true) or an IPv4 address (false)</li>
<li><strong>Mask</strong>: Mask for the address</li>
<li><strong>Prefix</strong>: Prefix for the address</li>
<li><strong>Time</strong>: Date and time the data was collected</li>
<li><strong>VRF</strong>: Name of the virtual route forwarding (VRF) interface if deployed</li>
</ul></td>
</tr>
<tr class="even">
<td>BTRFS Utilization</td>
<td>Displays disk utilization information for devices running Cumulus Linux 3 and the b-tree file system (BTRFS):
<ul>
<li><strong>Device Allocated</strong>: Percentage of the disk space allocated by BTRFS</li>
<li><strong>Hostname</strong>: Hostname of the given device</li>
<li><strong>Largest Chunk Size</strong>: Largest remaining chunk size on disk</li>
<li><strong>Last Changed</strong>: Data and time that the storage allocation was last updated</li>
<li><strong>Rebalance Recommended</strong>: Based on rules described in [When to Rebalance BTRFS Partitions]({{<ref "/knowledge-base/Configuration-and-Usage/Storage/When-to-Rebalance-BTRFS-Partitions">}}), a rebalance is suggested</li>
<li><strong>Unallocated Space</strong>: Amount of space remaining on the disk</li>
<li><strong>Unused Data Chunks Space</strong>: Amount of available data chunk space</li>
</ul></td>
</tr>
<tr class="odd">
<td>Installed Packages</td>
<td>Displays all known interfaces on the switch. This tab provides the following additional data about each package:
<ul>
<li><strong>CL Version</strong>: Version of Cumulus Linux associated with the package</li>
<li><strong>Hostname</strong>: Hostname of the given event</li>
<li><strong>Last Changed</strong>: Data and time that the interface was last enabled, updated, deleted, or changed state to down</li>
<li><strong>Package Name</strong>: Name of the package</li>
<li><strong>Package Status</strong>: Indicates if the package is installed</li>
<li><strong>Version</strong>: Version of the package</li>
</ul></td>
</tr>
<tr class="even">
<td>SSD Utilization</td>
<td>Displays overall health and utilization of a 3ME3 solid state drive (SSD). This tab provides the following data about each drive:
<ul>
<li><strong>Hostname</strong>: Hostname of the device with the 3ME3 drive installed</li>
<li><strong>Last Changed</strong>: Data and time that the SSD information was updated</li>
<li><strong>SSD Model</strong>: SSD model name</li>
<li><strong>Total PE Cycles Supported</strong>: PE cycle rating for the drive</li>
<li><strong>Current PE Cycles Executed</strong>: Number of PE cycle run to date</li>
<li><strong>% Remaining PE Cycles</strong>: Number of PE cycle available before drive needs to be replaced</li>
</ul></td>
</tr>
<tr class="odd">
<td>Forwarding Resources</td>
<td>Displays usage statistics for all forwarding resources on the switch. This tab provides the following additional data about each resource:
<ul>
<li><strong>ECMP Next Hops</strong>: Maximum number of hops seen in forwarding table, number used, and the percentage of this usage versus the maximum number</li>
<li><strong>Hostname</strong>: Hostname where forwarding resources reside</li>
<li><strong>IPv4 Host Entries</strong>: Maximum number of hosts in forwarding table, number of hosts used, and the percentage of usage versus the maximum</li>
<li><strong>IPv4 Route Entries</strong>: Maximum number of routes in forwarding table, number of routes used, and the percentage of usage versus the maximum</li>
<li><strong>IPv6 Host Entries</strong>: Maximum number of hosts in forwarding table, number of hosts used, and the percentage of usage versus the maximum</li>
<li><strong>IPv6 Route Entries</strong>: Maximum number of routes in forwarding table, number of routes used, and the percentage of usage versus the maximum</li>
<li><strong>MAC Entries</strong>: Maximum number of MAC addresses in forwarding table, number of MAC addresses used, and the percentage of usage versus the maximum</li>
<li><strong>MCAST Route</strong>: Maximum number of multicast routes in forwarding table, number of multicast routes used, and the percentage of usage versus the maximum</li>
<li><strong>Time</strong>: Date and time the data was collected</li>
<li><strong>Total Routes</strong>: Maximum number of total routes in forwarding table, number of total routes used, and the percentage of usage versus the maximum</li>
</ul></td>
</tr>
<tr class="even">
<td>ACL Resources</td>
<td>Displays usage statistics for all ACLs on the switch. <br>The following is diplayed for each ACL:
<ul><li>Maximum entries in the ACL</li>
<li>Number entries used</li>
<li>Percentage of this usage versus the maximum</li>
</ul>This tab also provides the following additional data about each ACL:
<ul>
<li><strong>Hostname</strong>: Hostname where the ACLs reside</li>
<li><strong>Time</strong>: Date and time the data was collected</li>
</ul></td>
</tr>
<tr class="odd">
<td>What Just Happened</td>
<td>Displays displays events based on conditions detected in the data plane on the switch. Refer to {{<link title="Configure and Monitor What Just Happened/#view-what-just-happened-metrics" text="What Just Happened" >}} for descriptions of the fields in this table.</td>
</tr>
<tr class="even">
<td>Sensors</td>
<td>Displays all known sensors on the switch. This tab provides a table for each type of sensor. Select the sensor type using the filter above the table.
<ul>
<li> <strong>Fan</strong>:<ul>
<li>Hostname: Hostname where the fan sensor resides</li>
<li>Message Type: Type of sensor; always Fan</li>
<li>Description: Text identifying the sensor</li>
<li>Speed (RPM): Revolutions per minute of the fan</li>
<li>Max: Maximum speed of the fan measured by sensor</li>
<li>Min: Minimum speed of the fan measured by sensor</li>
<li>Message: Description</li>
<li>Sensor Name: User-defined name for the fan sensor</li>
<li>Previous State: Operational state of the fan sensor before last update</li>
<li>State: Current operational state of the fan sensor</li>
<li>Time: Date and time the data was collected</li>
</ul>
<li> <strong>Temperature</strong>:<ul>
<li>Hostname: Hostname where the temperature sensor resides</li>
<li>Message Type: Type of sensor; always Temp</li>
<li>Critical: Maximum temperature (&deg;C) threshold for the sensor</li>
<li>Description: Text identifying the sensor</li>
<li>Lower Critical: Minimum temperature (&deg;C) threshold for the sensor</li>
<li>Max: Maximum temperature measured by sensor</li>
<li>Min: Minimum temperature measured by sensor</li>
<li>Message: Description</li>
<li>Sensor Name: User-defined name for the temperature sensor</li>
<li>Previous State: State of the sensor before last update</li>
<li>State: Current state of the temperature sensor</li>
<li>Temperature: Current temperature measured at sensor</li>
<li>Time: Date and time the data was collected</li>
</ul>
<li> <strong>Power Supply Unit (PSU)</strong>:<ul>
<li>Hostname: Hostname where the temperature sensor resides</li>
<li>Message Type: Type of sensor; always PSU</li>
<li>PIn: Input power (W) measured by sensor</li>
<li>POut: Output power (W) measured by sensor</li>
<li>Sensor Name: User-defined name for the power supply unit sensor</li>
<li>Previous State: State of the sensor before last update</li>
<li>State: Current state of the temperature sensor</li>
<li>Time: Date and time the data was collected</li>
<li>VIn: Input voltage (V) measured by sensor</li>
<li>VOut: Output voltage (V) measured by sensor</li>
</ul>
</ul>
</td>
</tr>
<tr class="odd">
<td>Digital Optics</td>
<td>Displays all available digital optics performance metrics. This tab provides a table for each of five metrics.
<ul>
<li><strong>Hostname</strong>: Hostname where the digital optics module resides</li>
<li><strong>Timestamp</strong>: Date and time the data was collected</li>
<li><strong>IfName</strong>: Name of the port where the digital optics module resides</li>
<li><strong>Units</strong>: Unit of measure that applies to the given metric</li>
<li><strong>Value</strong>: Measured value during the designated time period</li>
<li><strong>High Warning Threshold</strong>: Value used to generate a warning if the measured value excedes it.</li>
<li><strong>Low Warning Threshold</strong>: Value used to generate a warning if the measured value drops below it.</li>
<li><strong>High Alarm Threshold</strong>: Value used to generate an alarm if the measured value excedes it.</li>
<li><strong>Low Alarm Threshold</strong>: Value used to generate an alarm if the measured value drops below it.</li>
</ul>
</td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## Trace Cards

There are three cards used to perform on-demand and scheduled traces&mdash;one for the creation of on-demand and scheduled traces and two for the results. Trace cards can be added to user-created workbenches.

### Trace Request Card

This card is used to create new on-demand or scheduled trace requests or to run a scheduled trace on demand.

The small Trace Request card displays:

{{<figure src="/images/netq/trace-request-small-card.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/48-Maps-Navigation/06-Trip/trip-pins.svg" height="18" width="18"/></td>
<td>Indicates a trace request</td>
</tr>
<tr class="even">
<td>Select Trace list</td>
<td>Select a scheduled trace request from the list</td>
</tr>
<tr class="odd">
<td>Go</td>
<td>Click to start the trace now</td>
</tr>
</tbody>
</table>

The medium Trace Request card displays:

{{<figure src="/images/netq/trace-request-medium-320.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/48-Maps-Navigation/06-Trip/trip-pins.svg" height="18" width="18"/></td>
<td>Indicates a trace request.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>New Trace Request.</td>
</tr>
<tr class="odd">
<td>New Trace Request</td>
<td>Create a new layer 2 or layer 3 (no VRF) trace request.</td>
</tr>
<tr class="even">
<td>Source</td>
<td>(Required) Hostname or IP address of device where to begin the trace.</td>
</tr>
<tr class="odd">
<td>Destination</td>
<td>(Required) Ending point for the trace. For layer 2 traces, value must be a MAC address. For layer 3 traces, value must be an IP address.</td>
</tr>
<tr class="even">
<td>VLAN ID</td>
<td>Numeric identifier of a VLAN. Required for layer 2 trace requests.</td>
</tr>
</tr>
<tr class="odd">
<td>Run Now</td>
<td>Start the trace now.</td>
</tr>
</tbody>
</table>

The large Trace Request card displays:

{{< figure src="/images/netq/trace-request-large-222.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/48-Maps-Navigation/06-Trip/trip-pins.svg" height="18" width="18"/></td>
<td>Indicates a trace request.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>New Trace Request.</td>
</tr>
<tr class="odd">
<td>Trace selection</td>
<td>Leave <em>New Trace Request</em> selected to create a new request, or choose a scheduled request from the list.</td>
</tr>
<tr class="even">
<td>Source</td>
<td>(Required) Hostname or IP address of device where to begin the trace.</td>
</tr>
<tr class="odd">
<td>Destination</td>
<td>(Required) Ending point for the trace. For layer 2 traces, value must be a MAC address. For layer 3 traces, value must be an IP address.</td>
</tr>
<tr class="even">
<td>VRF</td>
<td>Optional for layer 3 traces. Virtual Route Forwarding interface to be used as part of the trace path.</td>
</tr>
<tr class="odd">
<td>VLAN ID</td>
<td>Required for layer 2 traces. Virtual LAN to be used as part of the trace path.</td>
</tr>
<tr class="even">
<td>Schedule</td>
<td>Sets the frequency with which to run a new trace (<strong>Run every</strong>) and when to start the trace for the first time (<strong>Starting</strong>).</td>
</tr>
<tr class="odd">
<td>Run Now</td>
<td>Start the trace now.</td>
</tr>
<tr class="even">
<td>Update</td>
<td><strong>Update</strong> is available when a scheduled trace request is selected from the dropdown list and you make a change to its configuration. Clicking <strong>Update</strong> saves the changes to the <em>existing</em> scheduled trace.</td>
</tr>
<tr class="odd">
<td>Save As New</td>
<td><strong>Save As New</strong> is available in two instances:
<ul>
<li>When you enter a source, destination, and schedule for a new trace. Clicking <strong>Save As New</strong> in this instance saves the new scheduled trace.</li>
<li>When changes are made to a selected scheduled trace request. Clicking <strong>Save As New</strong> in this instance saves the modified scheduled trace <em>without</em> changing the original trace on which it was based.</li>
</ul></td>
</tr>
</tbody>
</table>

The full screen Trace Request card displays:

{{< figure src="/images/netq/trace-request-fullscr-preview-tab-222.png" width="700" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Trace Request.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>Schedule Preview tab</td>
<td>Displays all scheduled trace requests for the given user. By default, the listing is sorted by <strong>Start Time</strong>, with the most recently started traces listed at the top. The tab provides the following additional data about each event:
<ul>
<li><strong>Action</strong>: Indicates latest action taken on the trace job. Values include Add, Deleted, Update.</li>
<li><strong>Frequency</strong>: How often the trace is scheduled to run</li>
<li><strong>Active</strong>: Indicates if trace is actively running (true), or stopped from running (false)</li>
<li><strong>ID</strong>: Internal system identifier for the trace job</li>
<li><strong>Trace Name</strong>: User-defined name for a trace</li>
<li><strong>Trace Params</strong>: Indicates source and destination, optional VLAN or VRF specified, and whether to alert on failure</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### On-demand Trace Results Card

This card is used to view the results of on-demand trace requests.

The small On-demand Trace Results card
displays:

{{< figure src="/images/netq/od-trace-result-small-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/06-Business-Products/13-Data-Files/data-file-bars-search.svg" height="18" width="18"/></td>
<td>Indicates an on-demand trace result.</td>
</tr>
<tr class="even">
<td> </td>
<td>Source and destination of the trace, identified by their address or hostname. Source is listed on top with arrow pointing to destination.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Indicates success or failure of the trace request. A successful result implies all paths were successful without any warnings or failures. A failure result implies there was at least one path with warnings or errors.</td>
</tr>
</tbody>
</table>

The medium On-demand Trace Results card displays:

{{< figure src="/images/netq/od-trace-result-medium-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/06-Business-Products/13-Data-Files/data-file-bars-search.svg" height="18" width="18"/></td>
<td>Indicates an on-demand trace result.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Trace Result.</td>
</tr>
<tr class="odd">
<td> </td>
<td>Source and destination of the trace, identified by their address or hostname. Source is listed on top with arrow pointing to destination.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Indicates success or failure of the trace request. A successful result implies all paths were successful without any warnings or failures. A failure result implies there was at least one path with warnings or errors.</td>
</tr>
<tr class="odd">
<td>Total Paths Found</td>
<td>Number of paths found between the two devices.</td>
</tr>
<tr class="even">
<td>MTU Overall</td>
<td>Average size of the maximum transmission unit for all paths.</td>
</tr>
<tr class="odd">
<td>Minimum Hops</td>
<td>Smallest number of hops along a path between the devices.</td>
</tr>
<tr class="even">
<td>Maximum Hops</td>
<td>Largest number of hops along a path between the devices.</td>
</tr>
</tbody>
</table>

The large On-demand Trace Results card contains two tabs.

The *On-demand Trace Result* tab displays:

{{< figure src="/images/netq/od-trace-result-large-summary-tab-230.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/06-Business-Products/13-Data-Files/data-file-bars-search.svg" height="18" width="18"/></td>
<td>Indicates an on-demand trace result.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Trace Result.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Indicates success or failure of the trace request. A successful result implies all paths were successful without any warnings or failures. A failure result implies there was at least one path with warnings or errors.</td>
</tr>
<tr class="even">
<td> </td>
<td>Source and destination of the trace, identified by their address or hostname. Source is listed on top with arrow pointing to destination.</td>
</tr>
<tr class="odd">
<td>Distribution by Hops chart</td>
<td>Displays the distributions of various hop counts for the available paths.</td>
</tr>
<tr class="even">
<td>Distribution by MTU chart</td>
<td>Displays the distribution of MTUs used on the interfaces used in the available paths.</td>
</tr>
<tr class="odd">
<td>Table</td>
<td>Provides detailed path information, sorted by the route identifier, including:
<ul>
<li><strong>Route ID</strong>: Identifier of each path</li>
<li><strong>MTU</strong>: Average speed of the interfaces used</li>
<li><strong>Hops</strong>: Number of hops to get from the source to the destination device</li>
<li><strong>Warnings</strong>: Number of warnings encountered during the trace on a given path</li>
<li><strong>Errors</strong>: Number of errors encountered during the trace on a given path</li>
</ul></td>
</tr>
<tr class="even">
<td>Total Paths Found</td>
<td>Number of paths found between the two devices.</td>
</tr>
<tr class="odd">
<td>MTU Overall</td>
<td>Average size of the maximum transmission unit for all paths.</td>
</tr>
<tr class="even">
<td>Minimum Hops</td>
<td>Smallest number of hops along a path between the devices.</td>
</tr>
</tbody>
</table>

The *On-demand Trace Settings* tab displays:

{{< figure src="/images/netq/od-trace-result-large-config-tab-230.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18"/></td>
<td>Indicates an on-demand trace setting</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Trace Settings</td>
</tr>
<tr class="odd">
<td>Source</td>
<td>Starting point for the trace</td>
</tr>
<tr class="even">
<td>Destination</td>
<td>Ending point for the trace</td>
</tr>
<tr class="odd">
<td>Schedule</td>
<td>Does not apply to on-demand traces</td>
</tr>
<tr class="even">
<td>VRF</td>
<td>Associated virtual route forwarding interface, when used with layer 3 traces</td>
</tr>
<tr class="odd">
<td>VLAN</td>
<td>Associated virtual local area network, when used with layer 2 traces</td>
</tr>
<tr class="even">
<td>Job ID</td>
<td>Identifier of the job; used internally</td>
</tr>
<tr class="odd">
<td>Re-run Trace</td>
<td>Clicking this button runs the trace again</td>
</tr>
</tbody>
</table>

The full screen On-demand Trace Results card displays:

{{< figure src="/images/netq/od-trace-result-fullscr-240.png" width="700" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>On-demand Trace Results</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/></td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab</td>
</tr>
<tr class="even">
<td>Trace Results tab</td>
<td>Provides detailed path information, sorted by the <strong>Resolution Time</strong> (date and time results completed), including:
<ul>
<li><strong>SCR.IP</strong>: Source IP address</li>
<li><strong>DST.IP</strong>: Destination IP address</li>
<li><strong>Max Hop Count</strong>: Largest number of hops along a path between the devices</li>
<li><strong>Min Hop Count</strong>: Smallest number of hops along a path between the devices</li>
<li><strong>Total Paths</strong>: Number of paths found between the two devices</li>
<li><strong>PMTU</strong>: Average size of the maximum transmission unit for all interfaces along the paths</li>
<li><strong>Errors</strong>: Message provided for analysis when a trace fails</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}</td>
</tr>
</tbody>
</table>

### Scheduled Trace Results Card

This card is used to view the results of scheduled trace requests.

The small Scheduled Trace Results card displays:

{{< figure src="/images/netq/sch-trace-result-small.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph.svg" height="18" width="18"/></td>
<td>Indicates a scheduled trace result.</td>
</tr>
<tr class="even">
<td> </td>
<td>Source and destination of the trace, identified by their address or hostname. Source is listed on left with arrow pointing to destination.</td>
</tr>
<tr class="odd">
<td>Results</td>
<td>Summary of trace results: a successful result implies all paths were successful without any warnings or failures; a failure result implies there was at least one path with warnings or errors.
<ul>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/21-Date-Calendar/calendar-refresh.svg" height="18" width="18"/> Number of trace runs completed in the designated time period</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/> Number of runs with warnings</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> Number of runs with errors</li>
</ul></td>
</tr>
</tbody>
</table>

The medium Scheduled Trace Results card displays:

{{< figure src="/images/netq/sch-trace-result-medium.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph.svg" height="18" width="18"/></td>
<td>Indicates a scheduled trace result.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Scheduled Trace Result.</td>
</tr>
<tr class="even">
<td>Summary</td>
<td>Name of scheduled validation and summary of trace results: a successful result implies all paths were successful without any warnings or failures; a failure result implies there was at least one path with warnings or errors.
<ul>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/21-Date-Calendar/calendar-refresh.svg" height="18" width="18"/> Number of trace runs completed in the designated time period</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/> Number of runs with warnings</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> Number of runs with errors</li>
</ul></td>
</tr>
<tr class="odd">
<td>Charts</td>
<td><p><strong>Heat map:</strong> A time segmented view of the results. For each time segment, the color represents the percentage of warning and failed results. Refer to {{<link url="#granularity-of-data-shown-based-on-time-period" text="Granularity of Data Shown Based on Time Period">}} for details on how to interpret the results.</p>
<p><strong>Unique Bad Nodes</strong>: Distribution of unique nodes that generated the indicated warnings and/or failures.</p></td>
</tr>
</tbody>
</table>

The large Scheduled Trace Results card contains two tabs:

The *Results* tab displays:

{{< figure src="/images/netq/sch-trace-result-large-sum-tab.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph.svg" height="18" width="18"/></td>
<td>Indicates a scheduled trace result.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Scheduled Trace Result.</td>
</tr>
<tr class="even">
<td>Summary</td>
<td>Name of scheduled validation and summary of trace results: a successful result implies all paths were successful without any warnings or failures; a failure result implies there was at least one path with warnings or errors.
<ul>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/21-Date-Calendar/calendar-refresh.svg" height="18" width="18"/> Number of trace runs completed in the designated time period</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/> Number of runs with warnings</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> Number of runs with errors</li>
</ul></td>
</tr>
<tr class="odd">
<td>Charts</td>
<td><p><strong>Heat map:</strong> A time segmented view of the results. For each time segment, the color represents the percentage of warning and failed results. Refer to {{<link url="#granularity-of-data-shown-based-on-time-period" text="Granularity of Data Shown Based on Time Period">}} for details on how to interpret the results.</p>
<p><strong>Small charts</strong>: Display counts for each item during the same time period, for the purpose of correlating with the warnings and errors shown in the heat map.</p></td>
</tr>
<tr class="even">
<td>Table/Filter options</td>
<td><p>When the <strong>Failures</strong> filter option is selected, the table displays the failure messages received for each run.</p>
<p>When the <strong>Paths</strong> filter option is selected, the table displays all of the paths tried during each run.</p>
<p>When the <strong>Warning</strong> filter option is selected, the table displays the warning messages received for each run.</p></td>
</tr>
</tbody>
</table>

The *Configuration* tab displays:

{{< figure src="/images/netq/sch-trace-result-large-config-tab.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18"/></td>
<td>Indicates a scheduled trace configuration.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Scheduled Trace Configuration (Scheduled Trace Result).</td>
</tr>
<tr class="even">
<td>Source</td>
<td>Address or hostname of the device where the trace was started.</td>
</tr>
<tr class="odd">
<td>Destination</td>
<td>Address of the device where the trace was stopped.</td>
</tr>
<tr class="even">
<td>Schedule</td>
<td>The frequency and starting date and time to run the trace.</td>
</tr>
<tr class="odd">
<td>VRF</td>
<td>Virtual Route Forwarding interface, when defined.</td>
</tr>
<tr class="even">
<td>VLAN</td>
<td>Virtual LAN identifier, when defined.</td>
</tr>
<tr class="odd">
<td>Name</td>
<td>User-defined name of the scheduled trace.</td>
</tr>
<tr class="even">
<td>Run Now</td>
<td>Start the trace now.</td>
</tr>
<tr class="odd">
<td>Edit</td>
<td>Modify the trace. Opens Trace Request card with this information pre-populated.</td>
</tr>
</tbody>
</table>

The full screen Scheduled Trace Results card displays:

{{< figure src="/images/netq/sch-trace-result-fullscr-230.png" width="700" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Scheduled Trace Results</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>Scheduled Trace Results tab</td>
<td>Displays the basic information about the trace, including:
<ul>
<li><strong>Resolution Time</strong>: Time that trace was run</li>
<li><strong>SRC.IP</strong>: IP address of the source device</li>
<li><strong>DST.IP</strong>: Address of the destination device</li>
<li><strong>Max Hop Count</strong>: Maximum number of hops across all paths between the devices</li>
<li><strong>Min Hop Count</strong>: Minimum number of hops across all paths between the devices</li>
<li><strong>Total Paths</strong>: Number of available paths found between the devices</li>
<li><strong>PMTU</strong>: Average of the maximum transmission units for all paths</li>
<li><strong>Errors</strong>: Message provided for analysis if trace fails</li>
</ul>
<p>Click on a result to open a detailed view of the results.</p></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## Validation Cards

There are three cards used to perform on-demand and scheduled validations&mdash;one for the creation of on-demand and scheduled validations and two for the results. Validation cards can be added to user-created workbenches.

### Validation Request Card

This card is used to create a new on-demand or scheduled validation request or run a scheduled validation on demand.

The small Validation Request card displays:

{{< figure src="/images/netq/valid-request-small-230.png" width="200" >}}
<p> </p>
<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/05-Love-it/love-it-check.svg" height="18" width="18"/></td>
<td>Indicates a validation request.</td>
</tr>
<tr class="even">
<td>Validation</td>
<td><p>Select a scheduled request to run that request on-demand. A default validation is provided for each supported network protocol and service, which runs a network-wide validation check. These validations run every 60 minutes, but you can run them on-demand at any time.</p>
<p><strong>Note</strong>: No new requests can be configured from this size card.</p></td>
</tr>
<tr class="odd">
<td>GO</td>
<td>Start the validation request. The corresponding On-demand Validation Result cards are opened on your workbench, one per protocol and service.</td>
</tr>
</tbody>
</table>

The medium Validation Request card displays:

{{< figure src="/images/netq/valid-request-medium-230.png" width="200" >}}
<p> </p>
<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/05-Love-it/love-it-check.svg" height="18" width="18"/></td>
<td>Indicates a validation request.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Validation Request.</td>
</tr>
<tr class="odd">
<td>Validation</td>
<td><p>Select a scheduled request to run that request on-demand. A default validation is provided for each supported network protocol and service, which runs a network-wide validation check. These validations run every 60 minutes, but you can run them on-demand at any time.</p>
<p><strong>Note</strong>: No new requests can be configured from this size card.</p></td>
</tr>
<tr class="even">
<td>Protocols</td>
<td>The protocols included in a selected validation request are listed here.</td>
</tr>
</tbody>
</table>

The large Validation Request card displays:

{{< figure src="/images/netq/valid-request-large-222.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/05-Love-it/love-it-check.svg" height="18" width="18"/></td>
<td>Indicates a validation request.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Validation Request.</td>
</tr>
<tr class="odd">
<td>Validation</td>
<td>Depending on user intent, this field is used to:
<ul>
<li>Select a scheduled request to run that request on-demand. A default validation is provided for each supported network protocol and service, which runs a network-wide validation check. These validations run every 60 minutes, but you can run them on-demand at any time.</li>
<li>Leave as is to create a new scheduled validation request.</li>
<li>Select a scheduled request to modify.</li>
</ul></td>
</tr>
<tr class="even">
<td>Protocols</td>
<td>For a selected scheduled validation, the protocols included in a validation request are listed here. For new on-demand or scheduled validations, click these to include them in the validation.</td>
</tr>
<tr class="odd">
<td>Schedule</td>
<td>For a selected scheduled validation, the schedule and the time of the last run are displayed. For new scheduled validations, select the frequency and starting date and time.
<ul>
<li><strong>Run Every</strong>: Select how often to run the request. Choose from 30 minutes, 1, 3, 6, or 12 hours, or 1 day.</li>
<li><strong>Starting</strong>: Select the date and time to start the first request in the series.</li>
<li><strong>Last Run</strong>: Timestamp of when the selected validation was started.</li>
</ul></td>
</tr>
<tr class="even">
<td>Scheduled Validations</td>
<td>Count of scheduled validations that are currently scheduled compared to the maximum of 15 allowed.</td>
</tr>
<tr class="odd">
<td>Run Now</td>
<td>Start the validation request.</td>
</tr>
<tr class="even">
<td>Update</td>
<td>When changes are made to a selected validation request, <strong>Update</strong> becomes available so that you can save your changes.
{{<notice info>}}
Be aware, that if you update a previously saved validation request, the historical data collected will no longer match the data results of future runs of the request. If your intention is to leave this request unchanged and create a new request, click <strong>Save As New</strong> instead.
{{</notice>}}</td>
</tr>
<tr class="odd">
<td>Save As New</td>
<td>When changes are made to a previously saved validation request, <strong>Save As New</strong> becomes available so that you can save the modified request as a new request.</td>
</tr>
</tbody>
</table>

The full screen Validation Request card displays all scheduled
validation requests.

{{< figure src="/images/netq/valid-request-fullscr-300.png" width="700" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Validation Request.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Default Time</td>
<td>No time period is displayed for this card as each validation request has its own time relationship.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>Validation Requests</td>
<td>Displays all <em>scheduled</em> validation requests. By default, the requests list is sorted by the date and time that it was originally created (<strong>Created At</strong>). This tab provides the following additional data about each request:
<ul>
<li><strong>Name</strong>: Text identifier of the validation.</li>
<li><strong>Type</strong>: Name of network protocols and/or services included in the validation.</li>
<li><strong>Start Time</strong>: Data and time that the validation request was run.</li>
<li><strong>Last Modified</strong>: Date and time of the most recent change made to the validation request.</li>
<li><strong>Cadence (Min)</strong>: How often, in minutes, the validation is scheduled to run. This is empty for new on-demand requests.</li>
<li><strong>Is Active</strong>: Indicates whether the request is currently running according to its schedule (<em>true</em>) or it is not running (<em>false</em>).</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### On-Demand Validation Result Card

This card is used to view the results of on-demand validation requests.

The small Validation Result card displays:

{{<figure src="/images/netq/valid-result-on-demand-bgp-small-222.png" width="200">}}
<p> </p>
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat-search.svg" height="18" width="18"/></td>
<td>Indicates an on-demand validation result.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Result &lt;Network Protocol or Service Name&gt; Validation.</td>
</tr>
<tr class="odd">
<td>Timestamp</td>
<td>Date and time the validation was completed.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Status of the validation job, where:
<ul>
<li><strong>Good</strong>: Job ran successfully. One or more warnings might have occurred during the run.</li>
<li><strong>Failed</strong>: Job encountered errors which prevented the job from completing, or job ran successfully, but errors occurred during the run.</li>
</ul></td>
</tr>
</tbody>
</table>

The medium Validation Result card displays:

{{<figure src="/images/netq/valid-result-on-demand-bgp-medium-222.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat-search.svg" height="18" width="18"/></td>
<td>Indicates an on-demand validation result.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Validation Result | &lt;Network Protocol or Service Name&gt;.</td>
</tr>
<tr class="odd">
<td>Timestamp</td>
<td>Date and time the validation was completed.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Status of the validation job, where:
<ul>
<li><strong>Good</strong>: Job ran successfully.</li>
<li><strong>Warning</strong>: Job encountered issues, but it did complete its run.</li>
<li><strong>Failed</strong>: Job encountered errors which prevented the job from completing.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Devices Tested</td>
<td>Chart with the total number of devices included in the validation and the distribution of the results.
<ul>
<li><strong>Pass</strong>: Number of devices tested that had successful results.</li>
<li><strong>Warn</strong>: Number of devices tested that had successful results, but also had at least one warning event.</li>
<li><strong>Fail</strong>: Number of devices tested that had one or more protocol or service failures.</li>
</ul>
<p>Hover over chart to view the number of devices and the percentage of all tested devices for each result category.</p></td>
</tr>
<tr class="even">
<td>Sessions Tested</td>
<td><p>For BGP, chart with total number of BGP sessions included in the validation and the distribution of the overall results.</p>
<p>For EVPN, chart with total number of BGP sessions included in the validation and the distribution of the overall results.</p>
<p>For Interfaces, chart with total number of ports included in the validation and the distribution of the overall results.</p>
<p>In each of these charts:</p>
<ul>
<li><strong>Pass</strong>: Number of sessions or ports tested that had successful results.</li>
<li><strong>Warn</strong>: Number of sessions or ports tested that had successful results, but also had at least one warning event.</li>
<li><strong>Fail</strong>: Number of sessions or ports tested that had one or more failure events.</li>
</ul>
<p>Hover over chart to view the number of devices, sessions, or ports and the percentage of all tested devices, sessions, or ports for each result category.</p>
<p>This chart does not apply to other Network Protocols and Services, and thus is not displayed for those cards.</p></td>
</tr>
<tr class="odd">
<td>Open &lt;Service&gt;  Card</td>
<td>Click to open the corresponding medium Network Services card, where available.</td>
</tr>
</tbody>
</table>

The large Validation Result card contains two tabs.

The *Summary* tab displays:

{{< figure src="/images/netq/od-valid-result-bgp-large.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat-search.svg" height="18" width="18"/></td>
<td>Indicates an on-demand validation result.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Validation Result | Summary | &lt;Network Protocol or Service Name&gt;.</td>
</tr>
<tr class="odd">
<td>Date</td>
<td>Day and time when the validation completed.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Status of the validation job, where:
<ul>
<li><strong>Good</strong>: Job ran successfully.</li>
<li><strong>Warning</strong>: Job encountered issues, but it did complete its run.</li>
<li><strong>Failed</strong>: Job encountered errors which prevented the job from completing.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Devices Tested</td>
<td>Chart with the total number of devices included in the validation and the distribution of the results.
<ul>
<li><strong>Pass</strong>: Number of devices tested that had successful results.</li>
<li><strong>Warn</strong>: Number of devices tested that had successful results, but also had at least one warning event.</li>
<li><strong>Fail</strong>: Number of devices tested that had one or more protocol or service failures.</li>
</ul>
<p>Hover over chart to view the number of devices and the percentage of all tested devices for each result category.</p></td>
</tr>
<tr class="even">
<td>Sessions Tested</td>
<td><p>For BGP, chart with total number of BGP sessions included in the validation and the distribution of the overall results.</p>
<p>For EVPN, chart with total number of BGP sessions included in the validation and the distribution of the overall results.</p>
<p>For Interfaces, chart with total number of ports included in the validation and the distribution of the overall results.</p>
<p>For OSPF, chart with total number of OSPF sessions included in the validation and the distribution of the overall results.</p>
<p>In each of these charts:</p>
<ul>
<li><strong>Pass</strong>: Number of sessions or ports tested that had successful results.</li>
<li><strong>Warn</strong>: Number of sessions or ports tested that had successful results, but also had at least one warning event.</li>
<li><strong>Fail</strong>: Number of sessions or ports tested that had one or more failure events.</li>
</ul>
<p>Hover over chart to view the number of devices, sessions, or ports and the percentage of all tested devices, sessions, or ports for each result category.</p>
<p>This chart does not apply to other Network Protocols and Services, and thus is not displayed for those cards.</p></td>
</tr>
<tr class="odd">
<td>Open &lt;Service&gt; Card</td>
<td>Click to open the corresponding medium Network Services card, when available.</td>
</tr>
<tr class="even">
<td>Table/Filter options</td>
<td><p>When the <strong>Most Active</strong> filter option is selected, the table displays switches and hosts running the given service or protocol in decreasing order of alarm counts. Devices with the largest number of warnings and failures are listed first. You can click on the device name to open its switch card on your workbench.</p>
<p>When the <strong>Most Recent</strong> filter option is selected, the table displays switches and hosts running the given service or protocol sorted by <strong>timestamp</strong>, with the device with the most recent warning or failure listed first. The table provides the following additional information:</p>
<ul>
<li><strong>Hostname</strong>: User-defined name for switch or host.</li>
<li><strong>Message Type</strong>: Network protocol or service which triggered the event.</li>
<li><strong>Message</strong>: Short description of the event.</li>
<li><strong>Severity</strong>: Indication of importance of event; values in decreasing severity include critical, warning, error, info, debug.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Results</td>
<td>Click to open the full screen card with all on-demand validation results sorted by timestamp.</td>
</tr>
</tbody>
</table>

The *Configuration* tab displays:

{{< figure src="/images/netq/od-valid-result-bgp-large-config-tab-230.png" width="500" >}}
<p> </p>
<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18"/></td>
<td>Indicates an on-demand validation request configuration.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Validation Result | Configuration | &lt;Network Protocol or Service Name&gt;.</td>
</tr>
<tr class="odd">
<td>Validations</td>
<td>List of network protocols or services included in the request that produced these results.</td>
</tr>
<tr class="even">
<td>Schedule</td>
<td>Not relevant to on-demand validation results. Value is always N/A.</td>
</tr>
</tbody>
</table>

The full screen Validation Result card provides a tab for all on-demand validation results.

{{< figure src="/images/netq/od-valid-result-bgp-fullscr-300.png" width="700" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Validation Results | On-demand.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/></td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>On-demand Validation Result | &lt;network protocol or service&gt;</td>
<td>Displays all unscheduled validation results. By default, the results list is sorted by <strong>Timestamp</strong>. This tab provides the following additional data about each result:
<ul>
<li><strong>Job ID</strong>: Internal identifier of the validation job that produced the given results</li>
<li><strong>Timestamp</strong>: Date and time the validation completed</li>
<li><strong>Type</strong>: Network protocol or service type</li>
<li><strong>Total Node Count</strong>: Total number of nodes running the given network protocol or service</li>
<li><strong>Checked Node Count</strong>: Number of nodes on which the validation ran</li>
<li><strong>Failed Node Count</strong>: Number of checked nodes that had protocol or service failures</li>
<li><strong>Rotten Node Count</strong>: Number of nodes that could not be reached during the validation</li>
<li><strong>Unknown Node Count</strong>: Applies only to the Interfaces service. Number of nodes with unknown port states.</li>
<li><strong>Failed Adjacent Count</strong>: Number of adjacent nodes that had protocol or service failures</li>
<li><strong>Total Session Count</strong>: Total number of sessions running for the given network protocol or service</li>
<li><strong>Failed Session Count</strong>: Number of sessions that had session failures</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### Scheduled Validation Result Card

This card is used to view the results of scheduled validation requests.

The small Scheduled Validation Result card displays:

{{< figure src="/images/netq/sch-valid-result-small-4cards-230.png" width="700" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph-line.svg" height="18" width="18"/></td>
<td>Indicates a scheduled validation result.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Scheduled Result &lt;Network Protocol or Service Name&gt; Validation.</td>
</tr>
<tr class="odd">
<td>Results</td>
<td>Summary of validation results:
<ul>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/21-Date-Calendar/calendar-refresh.svg" height="18" width="18"/> Number of validation runs completed in the designated time period.</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/> Number of runs with warnings.</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> Number of runs with errors.</li>
</ul></td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Status of the validation job, where:
<ul>
<li><strong>Pass</strong>: Job ran successfully. One or more warnings might have occurred during the run.</li>
<li><strong>Failed</strong>: Job encountered errors which prevented the job from completing, or job ran successfully, but errors occurred during the run.</li>
</ul></td>
</tr>
</tbody>
</table>

The medium Scheduled Validation Result card displays:

{{<figure src="/images/netq/sch-valid-result-medium-222.png" width="425">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph-line.svg" height="18" width="18"/></td>
<td>Indicates a scheduled validation result.</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Scheduled Validation Result | &lt;Network Protocol or Service Name&gt;.</td>
</tr>
<tr class="even">
<td>Summary</td>
<td>Summary of validation results:
<ul>
<li>Name of scheduled validation.</li>
<li>Status of the validation job, where:
<ul>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> <strong>Pass</strong>: Job ran successfully. One or more warnings might have occurred during the run.</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> <strong>Failed</strong>: Job encountered errors which prevented the job from completing, or job ran successfully, but errors occurred during the run.</li>
</ul></li>
</ul></td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Validation results, where:
<ul>
<li><strong>Time period</strong>: Range of time in which the data on the heat map was collected.</li>
<li><strong>Heat map</strong>: A time segmented view of the results. For each time segment, the color represents the percentage of warning, passing, and failed results. Refer to {{<link title="#Granularity of Data Shown Based on Time Period">}} for details on how to interpret the results.</li>
</ul></td>
</tr>
<tr class="even">
<td>Open &lt;Service&gt; Card</td>
<td>Click to open the corresponding medium Network Services card, when available.</td>
</tr>
</tbody>
</table>

The large Scheduled Validation Result card contains two tabs.

   The *Summary* tab displays:

   {{< figure src="/images/netq/sch-valid-result-large-sum-tab-222.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph-line.svg" height="18" width="18"/></td>
<td>Indicates a scheduled validation result.</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Validation Summary (Scheduled Validation Result | &lt;Network Protocol or Service Name&gt;).</td>
</tr>
<tr class="odd">
<td>Summary</td>
<td>Summary of validation results:
<ul>
<li>Name of scheduled validation.</li>
<li>Status of the validation job, where:
<ul>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> <strong>Pass</strong>: Job ran successfully. One or more warnings might have occurred during the run.</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> <strong>Failed</strong>: Job encountered errors which prevented the job from completing, or job ran successfully, but errors occurred during the run.</li>
</ul></li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/53-Resize/expand-horizontal-3.svg" height="18" width="18"/> <strong>Expand/Collapse</strong>: Expand the heat map to full width of card, collapse the heat map to the left.</li>
</ul></td>
</tr>
<tr class="even">
<td>Chart</td>
<td>Validation results, where:
<ul>
<li><strong>Time period</strong>: Range of time in which the data on the heat map was collected.</li>
<li><strong>Heat map</strong>: A time segmented view of the results. For each time segment, the color represents the percentage of warning, passing, and failed results. Refer to {{<link title="#Granularity of Data Shown Based on Time Period">}} for details on how to interpret the results.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Open &lt;Service&gt; Card</td>
<td>Click to open the corresponding medium Network Services card, when available.</td>
</tr>
<tr class="even">
<td>Table/Filter options</td>
<td><p>When the <strong>Most Active</strong> filter option is selected, the table displays switches and hosts running the given service or protocol in decreasing order of alarm counts-devices with the largest number of warnings and failures are listed first.</p>
<p>When the <strong>Most Recent</strong> filter option is selected, the table displays switches and hosts running the given service or protocol sorted by <strong>timestamp</strong>, with the device with the most recent warning or failure listed first. The table provides the following additional information:</p>
<ul>
<li><strong>Hostname</strong>: User-defined name for switch or host.</li>
<li><strong>Message Type</strong>: Network protocol or service which triggered the event.</li>
<li><strong>Message</strong>: Short description of the event.</li>
<li><strong>Severity</strong>: Indication of importance of event; values in decreasing severity include critical, warning, error, info, debug.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Results</td>
<td>Click to open the full screen card with all scheduled validation results sorted by timestamp.</td>
</tr>
</tbody>
</table>

The *Configuration* tab displays:

{{< figure src="/images/netq/sch-valid-result-large-config-tab-222.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18"/></td>
<td>Indicates a scheduled validation configuration</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Configuration (Scheduled Validation Result | &lt;Network Protocol or Service Name&gt;)</td>
</tr>
<tr class="odd">
<td>Name</td>
<td>User-defined name for this scheduled validation</td>
</tr>
<tr class="even">
<td>Validations</td>
<td>List of validations included in the validation request that created this result</td>
</tr>
<tr class="odd">
<td>Schedule</td>
<td>User-defined schedule for the validation request that created this result</td>
</tr>
<tr class="even">
<td>Open Schedule Card</td>
<td>Opens the large Validation Request card for editing this configuration</td>
</tr>
</tbody>
</table>

The full screen Scheduled Validation Result card provides tabs for all scheduled
validation results for the service.

{{< figure src="/images/netq/sch-valid-result-fullscr-300.png" width="700" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Scheduled Validation Results | &lt;Network Protocol or Service&gt;.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/>.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab.</td>
</tr>
<tr class="odd">
<td>Scheduled Validation Result | &lt;network protocol or service&gt;</td>
<td>Displays all unscheduled validation results. By default, the results list is sorted by timestamp. This tab provides the following additional data about each result:
<ul>
<li><strong>Job ID</strong>: Internal identifier of the validation job that produced the given results</li>
<li><strong>Timestamp</strong>: Date and time the validation completed</li>
<li><strong>Type:</strong> Protocol of Service Name</li>
<li><strong>Total Node Count</strong>: Total number of nodes running the given network protocol or service</li>
<li><strong>Checked Node Count</strong>: Number of nodes on which the validation ran</li>
<li><strong>Failed Node Count</strong>: Number of checked nodes that had protocol or service failures</li>
<li><strong>Rotten Node Count</strong>: Number of nodes that could not be reached during the validation</li>
<li><strong>Unknown Node Count</strong>: Applies only to the Interfaces service. Number of nodes with unknown port states.</li>
<li><strong>Failed Adjacent Count</strong>: Number of adjacent nodes that had protocol or service failures</li>
<li><strong>Total Session Count</strong>: Total number of sessions running for the given network protocol or service</li>
<li><strong>Failed Session Count</strong>: Number of sessions that had session failures</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>
