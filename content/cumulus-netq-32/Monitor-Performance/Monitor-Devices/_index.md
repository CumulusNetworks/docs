---
title: Monitor Devices
author: Cumulus Networks
weight: 810
toc: 3
---
With the NetQ UI and CLI, a user can monitor the network inventory of switches and hosts, including such items as the number of each and what operating systems are installed. Additional details are available about the hardware and software components on individual switches, such as  the motherboard, ASIC, microprocessor, disk, memory, fan and power supply information. The commands and cards available to obtain this type of information help you to answer questions such as:

- What switches do I have in the network?
- What is the distribution of ASICs across my network?
- Do all switches have valid licenses?
- Are NetQ agents running on all of my switches?
- What hardware is installed on my switches?
- How many transmit and receive packets have been dropped?
- How healthy are the fans and power supply?
- What software is installed on my switches?
- Are all switches licensed correctly?
- What is the ACL and forwarding resources usage?
- Do all switches have NetQ Agents running?

## Relevant CLI Commands and UI Card Workflows

The following commands and cards are used to monitor devices.

{{< tabs "TabID21" >}}

{{< tab "NetQ CLI" >}}

NetQ uses {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Link-Layer-Discovery-Protocol/" text="LLDP">}} (Link Layer Discovery Protocol) to collect port information. NetQ can also identify peer ports connected to DACs (Direct Attached Cables) and AOCs (Active Optical Cables) without using LLDP, even if the link is not UP.

The CLI supports hardware-, software-, and event-related commands:

- {{<link title="#Hardware Commands" text="Hardware Commands">}}
- {{<link title="#Software Commands" text="Software Commands">}}
- {{<link title="#Events" text="Events">}}

### Hardware Commands

The NetQ CLI provides a number of commands to monitor hardware inventory on switches. The syntax of these commands is:

```
netq [<hostname>] show inventory brief [opta] [json]
netq [<hostname>] show inventory asic [vendor <asic-vendor>|model <asic-model>|model-id <asic-model-id>] [opta] [json]
netq [<hostname>] show inventory board [vendor <board-vendor>|model <board-model>] [opta] [json]
netq [<hostname>] show inventory cpu [arch <cpu-arch>] [opta] [json]
netq [<hostname>] show inventory disk [name <disk-name>|transport <disk-transport>|vendor <disk-vendor>] [opta] [json]
netq [<hostname>] show inventory license [cumulus] [status ok|status missing] [around <text-time>] [opta] [json]
netq [<hostname>] show inventory memory [type <memory-type>|vendor <memory-vendor>] [opta] [json]
netq [<hostname>] show inventory os [version <os-version>|name <os-name>] [opta] [json]

netq [<hostname>] show sensors all [around <text-time>] [json]
netq [<hostname>] show sensors psu [<psu-name>] [around <text-time>] [json]
netq [<hostname>] show sensors temp [<temp-name>] [around <text-time>] [json]
netq [<hostname>] show sensors fan [<fan-name>] [around <text-time>] [json]

netq [<hostname>] show interface-stats [errors|all] [<physical-port>] [around <text-time>] [json]
netq [<hostname>] show interface-utilization [<text-port>] [tx|rx] [around <text-time>] [json]
netq [<hostname>] show resource-util [cpu | memory] [around <text-time>] [json]
netq [<hostname>] show resource-util disk [<text-diskname>] [around <text-time>] [json]
netq [<hostname>] show cl-ssd-util [around <text-time>] [json]
netq [<hostname>] show cl-btrfs-info [around <text-time>] [json]
```

{{<notice note>}}
The keyword values for the <code>vendor</code>, <code>model</code>, <code>model-id</code>, <code>arch</code>, <code>name</code>, <code>transport</code>, <code>type</code>, <code>version</code>, <code>psu</code>, <code>temp</code>, and <code>fan</code> keywords are specific to your deployment. For example, if you have devices with CPU architectures of only one type, say Intel x86, then that is the only option available for the <code>cpu-arch</code> keyword value. If you have multiple CPU architectures, say you also have ARMv7, then that would also be an option for you.
{{</notice>}}

### Software Commands

The NetQ CLI provides a number of commands to monitor software inventory on switches. The syntax for these commands is:

```
netq [<hostname>] show agents
netq [<hostname>] show inventory brief [json]
netq [<hostname>] show inventory license [cumulus] [status ok|status missing] [around <text-time>] [json]
netq [<hostname>] show inventory os [version <os-version>|name <os-name>] [json]

netq [<hostname>] show cl-manifest [json]
netq [<hostname>] show cl-pkg-info [<text-package-name>] [around <text-time>] [json]
netq [<hostname>] show recommended-pkg-version [release-id <text-release-id>] [package-name <text-package-name>] [json]
netq [<hostname>] show cl-resource acl [ingress | egress] [around <text-time>] [json]
netq [<hostname>] show cl-resource forwarding [around <text-time>] [json]
```

{{<notice note>}}
The values for the <code>name</code> option are specific to your deployment. For example, if you have devices with only one type of OS, say Cumulus Linux, then that is the only option available for the <code>os-name</code> option value. If you have multiple OSs running, say you also have Ubuntu, then that would also be an option for you.
{{</notice>}}

### Events

To view events related to hardware and software devices, use the `netq show events` command.

```
netq [<hostname>] show events [level info | level error | level warning | level critical | level debug] [type agents | type inventory-physical | type license | type os | type sensors | type btrfsinfo] [between <text-time> and <text-endtime>] [json]
```

{{<notice note>}}
When entering a time value, you must include a numeric value <em>and</em> the unit of measure:

- **w**: week(s)
- **d**: day(s)
- **h**: hour(s)
- **m**: minute(s)
- **s**: second(s)
- **now**

For the <code>between</code> option, the start (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{</notice>}}

{{< /tab >}}

{{< tab "NetQ UI" >}}
Two card workflows are available for viewing network inventory (switches and hosts) and individual switch inventory: Inventory|Devices, Inventory|Switches. The Switch card workflow enables you to view performance for individual switches.

- {{<link title="#Devices Inventory Card Workflow" text="Devices Inventory Card Workflow">}}
- {{<link title="#Switch Inventory Card Workflow" text="Switch Inventory Card Workflow">}}
- {{<link title="#Switch Performance Card Workflow" text="Switch Performance Card Workflow">}}

### Devices Inventory Card Workflow

The small Devices Inventory card displays:

{{< figure src="/images/netq/inventory-devices-small-240.png" width="200" >}}

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

{{< figure src="/images/netq/inventory-devices-medium-240.png" width="200" >}}

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

{{< figure src="/images/netq/inventory-devices-large-switches-tab-230.png" width="500" >}}

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

{{< figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700" >}}

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

### Switch Inventory Card Workflow

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

### Switch Performance Card Workflow

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
<td>Displays displays events based on conditions detected in the data plane on the switch. Refer to {{<link url="Monitor-Network-Elements#view-what-just-happened" text="What Just Happened" >}} for descriptions of the fields in this table.</td>
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

{{< /tab >}}

{{< /tabs >}}
