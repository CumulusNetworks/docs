---
title: NetQ UI Card Reference
author: Cumulus Networks
weight: 1090
---
This reference describes the cards available with the NetQ 3.2 graphical user interface (NetQ UI). Each item and field on the four sizes of cards is shown.

## Inventory|Devices Card

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
<td>Inventory | Devices</td>
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

{{<figure src="/images/netq/inventory-devices-large-switches-tab-230.png" width="500">}}

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
<td>Inventory | Devices.</td>
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
<td>Switch components monitored-ASIC, Operating System (OS), Cumulus Linux license, NetQ Agent version, and Platform.</td>
</tr>
<tr class="odd">
<td>Distribution charts</td>
<td>Distribution of switch components across the network.</td>
</tr>
<tr class="even">
<td>Unique</td>
<td>Number of unique items of each component type. For example, for License, you might have CL 2.7.2 and CL 2.7.4, giving you a unique count of two.</td>
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
<td>Inventory | Devices | Switches.</td>
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
<li><strong>License State</strong>: Indicator of validity. Values include ok and bad.</li>
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
</tbody>
</table>

## Inventory|Switch Card

Knowing what components are included on all of your switches aids in upgrade, compliance, and other planning tasks. Viewing this data is accomplished through the Switch Inventory card.

The small Switch Inventory card displays:

{{<figure src="/images/netq/inventory-switch-small-230.png" width="200">}}

| Item              | Description  |
| ----------------- | ------------ |
| <img src="https://icons.cumulusnetworks.com/11-Content/04-Archives/archive-books.svg" height="22" width="22"/> | Indicates data is for switch inventory |
| Count             | Total number of switches in the network inventory |
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
<td><p>Distribution of switch components (disk size, OS, ASIC, NetQ Agents, CPU, Cumulus Linux licenses, platform, and memory size) during the designated time period. Hover over chart segment to view versions of each component.</p>
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
<td><p>Distribution of switch components (disk size, OS, ASIC, NetQ Agents, CPU, Cumulus Linux licenses, platform, and memory size), divided into software and hardware, during the designated time period. Hover over chart segment to view versions of each component.</p>
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
<td>License State chart</td>
<td>Distribution of Cumulus Linux license status. Hover over chart segments to highlight the vendor and platforms that have that license status.</td>
</tr>
<tr class="even">
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


With NetQ, you can monitor the number of nodes running the LLDP service, view nodes with the most LLDP neighbor nodes, those nodes with the least neighbor nodes, and view alarms triggered by the LLDP service. For an overview and how to configure LLDP in your data center network, refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Link-Layer-Discovery-Protocol/" text="Link Layer Discovery Protocol">}}.

## LLDP Service Card

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
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running LLDP last week or last month might be more or less than the number of nodes running LLDP currently.</p></td>
</tr>
<tr class="odd">
<td>Total Open Alarms chart</td>
<td><p>Distribution of LLDP-related alarms received during the designated time period, and the total number of current LLDP-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
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
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running LLDP last week or last month might be more or less than the number of nodes running LLDP currently.</p></td>
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
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
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
<li><strong>License State</strong>: Indicator of validity. Values include ok and bad.</li>
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
<td>Displays all LLDP sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
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
<td>Displays all LLDP events network-wide. By default, the event list is sorted by time, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a LLDP-related event. Example: LLDP Session with host leaf02 swp6 modified fields leaf06 swp21.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>lldp</em> in this card workflow.</li>
</ul></td>
</tr>
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## LLDP Session Card

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
<td>Range of time in which the displayed data was collected.</td>
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
<td>Range of time in which the displayed data was collected.</td>
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
<td>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of an event. Example: LLDP Session with host leaf02 swp6 modified fields leaf06 swp21.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>lldp</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## Switch Card

Viewing detail about a particular switch is essential when troubleshooting performance issues. With NetQ you can view the overall performance and drill down to view attributes of the switch, interface performance and the events associated with a switch. This is accomplished through the Switches card.

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

The large Switch card contains three tabs:

The *Attributes* tab displays:

{{<figure src="/images/netq/dev-switch-large-attributes-tab-230.png" width="500">}}

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
<td>Operating system running on the switch. CL indicates a Cumulus Linux license.</td>
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
<td>License State</td>
<td>Indicates whether the license is valid (<em>ok</em>) or invalid/missing (<em>bad</em>).</td>
</tr>
<tr class="odd">
<td>Total Interfaces</td>
<td>Total number of interfaces on this switch, and the number of those that are up and down.</td>
</tr>
</tbody>
</table>

The *Utilization* tab displays:

{{<figure src="/images/netq/dev-switch-large-utilization-tab-230.png" width="500">}}

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

{{<figure src="/images/netq/dev-switch-large-interfaces-tab-230.png" width="500">}}

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

The full screen Switch card provides multiple tabs.

{{< figure src="/images/netq/dev-switch-fullscr-alarms-tab-241.png" width="700" >}}

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
<li><strong>Egress Port</strong>: Importance of the event-critical, warning, info, or debug</li>
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
<td>Displays disk utilization information for devices running Cumulus Linux 3.x and the b-tree file system (BTRFS):
<ul>
<li><strong>Device Allocated</strong>: Percentage of the disk space allocated by BTRFS</li>
<li><strong>Hostname</strong>: Hostname of the given device</li>
<li><strong>Largest Chunk Size</strong>: Largest remaining chunk size on disk</li>
<li><strong>Last Changed</strong>: Data and time that the storage allocation was last updated</li>
<li><strong>Rebalance Recommended</strong>: Based on rules described in {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/articles/360037394933-When-to-Rebalance-BTRFS-Partitions" text="When to Rebalance BTRFS Partitions" >}}, a rebalance is suggested</li>
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
<td>Displays displays events based on conditions detected in the data plane on the switch. Refer to {{<link title="Configure and Monitor What Just Happened Metrics/#view-what-just-happened-metrics" text="What Just Happened" >}} for descriptions of the fields in this table.</td>
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
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

You can easily monitor warning, info, and debug severity events occurring across your network using the Info card. You can determine the number of events for the various system, interface, and network protocols and services components in the network. The content of the cards in the workflow is described first, and then followed by common tasks you would perform using this card workflow.

## Events|Info Card Workflow Summary

The Info card workflow enables users to easily view and track informational alarms occurring anywhere in your network.

The small Info card displays:

{{<figure src="/images/netq/events-info-small-222.png" width="200">}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/13-Flags/flag-plain-1.svg" height="18" width="18"/></td>
<td>Indicates data is for all warning, info, and debug severity events in the network</td>
</tr>
<tr class="even">
<td>Info count</td>
<td>Number of info events received during the designated time period</td>
</tr>
<tr class="odd">
<td>Alarm count</td>
<td>Number of alarm events received during the designated time period</td>
</tr>
<tr class="even">
<td>Chart</td>
<td>Distribution of all info events and alarms received during the designated time period</td>
</tr>
</tbody>
</table>

The medium Info card displays:

{{<figure src="/images/netq/events-info-medium-222.png" width="200">}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/13-Flags/flag-1.svg" height="18" width="18"/></td>
<td>Indicates data is for all warning, info, and debug severity events in the network.</td>
</tr>
<tr class="odd">
<td>Types of Info</td>
<td>Chart which displays the services that have triggered events during the designated time period. Hover over chart to view a count for each type.</td>
</tr>
<tr class="even">
<td>Distribution of Info</td>
<td>Info Status
<ul>
<li><strong>Count</strong>: Number of info events received during the designated time period.</li>
<li><strong>Chart</strong>: Distribution of all info events received during the designated time period.</li>
</ul>
Alarms Status
<ul>
<li><strong>Count</strong>: Number of alarm events received during the designated time period.</li>
<li><strong>Chart</strong>: Distribution of all alarm events received during the designated time period.</li>
</ul></td>
</tr>
</tbody>
</table>

The large Info card displays:

{{<figure src="/images/netq/events-info-large-222.png" width="500">}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/13-Flags/flag-1.svg" height="18" width="18"/></td>
<td>Indicates data is for all warning, info, and debug severity events in the network.</td>
</tr>
<tr class="odd">
<td>Types of Info</td>
<td>Chart which displays the services that have triggered events during the designated time period. Hover over chart to view a count for each type.</td>
</tr>
<tr class="even">
<td>Distribution of Info</td>
<td>Info Status
<ul>
<li><strong>Count</strong>: Current number of info events received during the designated time period.</li>
<li><strong>Chart</strong>: Distribution of all info events received during the designated time period.</li>
</ul>
Alarms Status
<ul>
<li><strong>Count</strong>: Current number of alarm events received during the designated time period.</li>
<li><strong>Chart</strong>: Distribution of all alarm events received during the designated time period.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table</td>
<td>Listing of items that match the filter selection:
<ul>
<li><strong>Events by Most Recent</strong>: Most recent event are listed at the top.</li>
<li><strong>Devices by Event Count</strong>: Devices with the most events are listed at the top.</li>
</ul></td>
</tr>
<tr class="even">
<td>Show All Events</td>
<td>Opens full screen Events | Info card with a listing of all events.</td>
</tr>
</tbody>
</table>

The full screen Info card provides tabs for all events.

{{<figure src="/images/netq/events-info-fullscr-300.png" width="700">}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td>Events | Info</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Default Time</td>
<td>Range of time in which the displayed data was collected.</td>
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
<td>All Events</td>
<td>Displays all events (both alarms and info) received in the time period. By default, the requests list is sorted by the date and time that the event occurred (<strong>Time</strong>). This tab provides the following additional data about each request:
<ul>
<li><strong>Source</strong>: Hostname of the given event</li>
<li><strong>Message</strong>: Text describing the alarm or info event that occurred</li>
<li><strong>Type</strong>: Name of network protocol and/or service that triggered the given event</li>
<li><strong>Severity</strong>: Importance of the event-critical, warning, info, or debug</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

You can easily monitor critical events occurring across your network using the Alarms card. You can determine the number of events for the various system, interface, and network protocols and services components in the network. The content of the cards in the workflow is described first, and then followed by common tasks you would perform using this card workflow.

## Events|Alarms Card Workflow Summary

The small Alarms card displays:

{{< figure src="/images/netq/events-alarms-small-231.png" width="200" >}}

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
<td>Indicates data is for all critical severity events in the network.</td>
</tr>
<tr class="even">
<td>Alarm trend</td>
<td>Trend of alarm count, represented by an arrow:
<ul>
<li><strong>Pointing upward and <strong>bright pink</strong></strong>: alarm count is higher than the last two time periods, an increasing trend</li>
<li><strong>Pointing downward and <strong>green</strong></strong>: alarm count is lower than the last two time periods, a decreasing trend</li>
<li><strong>No arrow</strong>: alarm count is unchanged over the last two time periods, trend is steady</li>
</ul></td>
</tr>
<tr class="odd">
<td>Alarm score</td>
<td>Current count of alarms during the designated time period.</td>
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

The medium Alarms card displays:

{{< figure src="/images/netq/events-alarms-medium-222.png" width="200" >}}

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
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/></td>
<td>Indicates data is for all critical events in the network.</td>
</tr>
<tr class="odd">
<td>Count</td>
<td>Total number of alarms received during the designated time period.</td>
</tr>
<tr class="even">
<td>Alarm score</td>
<td>Current count of alarms received from each category (overall, system, interface, and network services) during the designated time period.</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of all alarms received from each category during the designated time period.</td>
</tr>
</tbody>
</table>

The large Alarms card has one tab.

The *Alarm Summary* tab displays:

{{< figure src="/images/netq/events-alarms-large-summ-tab-231.png" width="500" >}}

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
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-clock.svg", height="18", width="18"/></td>
<td>Indicates data is for all system, trace and interface critical events in the network.</td>
</tr>
<tr class="odd">
<td>Alarm Distribution</td>
<td><p><strong>Chart</strong>: Distribution of all alarms received from each category during the designated time period:
<ul><li>NetQ Agent</li><li>BTRFS Information</li><li>CL Support</li><li>Config Diff</li><li>CL License</li><li>Installed Packages</li><li>Link</li><li>LLDP</li><li>MTU</li><li>Node</li><li>Port</li><li>Resource</li><li>Running Config Diff</li><li>Sensor</li><li>Services</li><li>SSD Utilization</li><li>TCA Interface Stats</li><li>TCA Resource Utilization</li><li>TCA Sensors</li></ul>  
The categories are displayed in descending order based on total count of alarms, with the largest number of alarms is shown at the top, followed by the next most, down to the chart with the fewest alarms.</p>
<p><strong>Count</strong>: Total number of alarms received from each category during the designated time period.</p></td>
</tr>
<tr class="even">
<td>Table</td>
<td>Listing of items that match the filter selection for the selected alarm categories:
<ul>
<li><strong>Events by Most Recent</strong>: Most recent event are listed at the top</li>
<li><strong>Devices by Event Count</strong>: Devices with the most events are listed at the top</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Events</td>
<td>Opens full screen Events | Alarms card with a listing of all events.</td>
</tr>
</tbody>
</table>

The full screen Alarms card provides tabs for all events.

{{< figure src="/images/netq/events-alarms-fullscr-allevents-tab-300.png" width="700" >}}

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
<td>Events | Alarms</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench.</td>
</tr>
<tr class="odd">
<td>Default Time</td>
<td>Range of time in which the displayed data was collected.</td>
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
<td>All Events</td>
<td>Displays all events (both alarms and info) received in the time period. By default, the requests list is sorted by the date and time that the event occurred (<strong>Time</strong>). This tab provides the following additional data about each request:
<ul>
<li><strong>Source</strong>: Hostname of the given event</li>
<li><strong>Message</strong>: Text describing the alarm or info event that occurred</li>
<li><strong>Type</strong>: Name of network protocol and/or service that triggered the given event</li>
<li><strong>Severity</strong>: Importance of the event-critical, warning, info, or debug</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## BGP Service Card Workflow

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
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running BGP last week or last month might be more or less than the number of nodes running BGP currently.</p></td>
</tr>
<tr class="odd">
<td>Total Open Alarms chart</td>
<td><p>Distribution of BGP-related alarms received during the designated time period, and the total number of current BGP-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="even">
<td>Total Nodes Not Est. chart</td>
<td><p>Distribution of switches and hosts with unestablished BGP sessions during the designated time period, and the total number of unestablished sessions in the network currently.</p>
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of unestablished session last week or last month might be more of less than the number of nodes with unestablished sessions currently.</p></td>
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
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running BGP last week or last month might be more or less than the number of nodes running BGP currently.</p></td>
</tr>
<tr class="odd">
<td>Total Nodes Not Est. chart</td>
<td><p>Distribution of switches and hosts with unestablished BGP sessions during the designated time period, and the total number of unestablished sessions in the network currently.</p>
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of unestablished session last week or last month might be more of less than the number of nodes with unestablished sessions currently.</p></td>
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
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
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
<li><strong>License State</strong>: Indicator of validity. Values include ok and bad.</li>
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
<td>Displays all BGP sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
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
<td>Displays all BGP events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Message</strong>: Text description of a BGP-related event. Example: BGP session with peer tor-1 swp7 vrf default state changed from failed to Established.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>bgp</em> in this card workflow.</li>
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## OSPF Service Card Workflow

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
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running OSPF last week or last month might be more or less than the number of nodes running OSPF currently.</p></td>
</tr>
<tr class="odd">
<td>Total Sessions Not Established chart</td>
<td><p>Distribution of unestablished OSPF sessions during the designated time period, and the total number of unestablished sessions in the network currently.</p>
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of unestablished session last week or last month might be more of less than the number of nodes with unestablished sessions currently.</p></td>
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
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running OSPF last week or last month might be more or less than the number of nodes running OSPF currently.</p></td>
</tr>
<tr class="odd">
<td>Total Sessions chart</td>
<td>Distribution of OSPF sessions during the designated time period, and the total number of sessions running on the network currently.</td>
</tr>
<tr class="even">
<td>Total Sessions Not Established chart</td>
<td><p>Distribution of unestablished OSPF sessions during the designated time period, and the total number of unestablished sessions in the network currently.</p>
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of unestablished session last week or last month might be more of less than the number of nodes with unestablished sessions currently.</p></td>
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
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
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
<li><strong>License State</strong>: Indicator of validity. Values include ok and bad.</li>
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
<td>Displays all OSPF sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
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
<td>Displays all OSPF events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a OSPF-related event. Example: swp4 area ID mismatch with peer leaf02</li>
<li><strong>Source</strong>: Hostname of network device that generated the event</li>
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>OSPF</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## BGP Session Card Workflow Summary

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
<td>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a BGP-related event. Example: BGP session with peer tor-1 swp7 vrf default state changed from failed to Established.</li>
<li><strong>Source</strong>: Hostname of network device that generated the event.</li>
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of bgp in this card workflow.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

