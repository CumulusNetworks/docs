---
title: Monitor the MLAG Service
author: Cumulus Networks
weight: 400
toc: 4
---
The Cumulus NetQ UI enables operators to view the health of the MLAG service on a network-wide and a per session basis, giving greater insight into all aspects of the service. This is accomplished through two card workflows, one for the service and one for the session. They are described separately here.

{{%notice note%}}
**MLAG or CLAG?**
The Cumulus Linux implementation of MLAG is referred to by other vendors as MLAG, MC-LAG or VPC. The Cumulus NetQ UI uses the MLAG terminology predominantly.
{{%/notice%}}

## Monitor the MLAG Service (All Sessions)

With NetQ, you can monitor the number of nodes running the MLAG service, view sessions running, and view alarms triggered by the MLAG service. For an overview and how to configure MLAG in your data center network, refer to [Multi-Chassis Link Aggregation - MLAG]({{<ref "/cumulus-linux-43/Layer-2/Multi-Chassis-Link-Aggregation-MLAG" >}}).

### MLAG Service Card Workflow Summary

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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | All MLAG Sessions</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the MLAG service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of MLAG-related alarms received during the designated time period</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/48-Maps-Navigation/11-Pins-Style%20Two/style-two-pin-off-map.svg" height="18" width="18"/></td>
<td>Total number of sessions with an inactive backup IP address during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/27-Link-Unlink/link-broken-1.svg" height="18" width="18"/></td>
<td>Total number of bonds with only a single connection during the designated time period</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the MLAG service enabled during the designated time period, and a total number of nodes running the service currently.</p>
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running MLAG last week or last month might be more or less than the number of nodes running MLAG currently.</p></td>
</tr>
<tr class="odd">
<td>Total Open Alarms chart</td>
<td><p>Distribution of MLAG-related alarms received during the designated time period, and the total number of current MLAG-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="even">
<td>Total Sessions chart</td>
<td>Distribution of MLAG sessions running during the designated time period, and the total number of sessions running on the network currently</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>All MLAG Sessions Summary</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the MLAG service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of MLAG-related alarms received during the designated time period</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the MLAG service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running MLAG last week or last month might be more or less than the number of nodes running MLAG currently.</p></td>
</tr>
<tr class="odd">
<td>Total Sessions chart</td>
<td><p>Distribution of MLAG sessions running during the designated time period, and the total number of sessions running on the network currently</p></td>
</tr>
<tr class="even">
<td>Total Sessions with Inactive-backup-ip chart</td>
<td>Distribution of sessions without an active backup IP defined during the designated time period, and the total number of these sessions running on the network currently</td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td><p>When the <strong>Switches with Most Sessions</strong> filter is selected, the table displays switches running MLAG sessions in decreasing order of session count-devices with the largest number of sessions are listed first</p>
<p>When the <strong>Switches with Most Unestablished Sessions</strong> filter is selected, the table displays switches running MLAG sessions in decreasing order of unestablished session count-devices with the largest number of unestablished sessions are listed first</p></td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view all MLAG sessions in the full screen card</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in header)</td>
<td>Indicates alarm data for all MLAG sessions</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | All MLAG Alarms (visible when you hover over card)</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the MLAG service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in summary bar)</td>
<td>Total number of MLAG-related alarms received during the designated time period</td>
</tr>
<tr class="even">
<td>Total Alarms chart</td>
<td><p>Distribution of MLAG-related alarms received during the designated time period, and the total number of current MLAG-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td>When the <strong>Events by Most Active Device</strong> filter is selected, the table displays switches running MLAG sessions in decreasing order of alarm count-devices with the largest number of sessions are listed first</td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view all MLAG sessions in the full screen card</td>
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
<li>Revision: Release version of the platform</li>
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
<li><strong>Backup Ip</strong>: IP address of the interface to use if the peerlink (or bond) goes down</li>
<li><strong>Backup Ip Active</strong>: Indicates whether the backup IP address has been specified and is active (true) or not (false)</li>
<li><strong>Bonds</strong>
<ul>
<li>Conflicted: Identifies the set of interfaces in a bond that do not match on each end of the bond</li>
<li>Single: Identifies a set of interfaces connecting to only one of the two switches</li>
<li>Dual: Identifies a set of interfaces connecting to both switches</li>
<li>Proto Down: Interface on the switch brought down by the <code>clagd</code> service. Value is blank if no interfaces are down due to <code>clagd</code> service.</li>
</ul></li>
<li><strong>Clag Sysmac</strong>: Unique MAC address for each bond interface pair. <strong>Note</strong>: Must be a value between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff.</li>
<li><strong>Peer</strong>:
<ul>
<li>If: Name of the peer interface</li>
<li>Role: Role of the peer device. Values include primary and secondary.</li>
<li>State: Indicates if peer device is up (true) or down (false)</li>
</ul></li>
<li><strong>Role</strong>: Role of the host device. Values include primary and secondary.</li>
<li><strong>Timestamp</strong>: Date and time the MLAG session was started, deleted, updated, or marked dead (device went down)</li>
<li><strong>Vxlan Anycast</strong>: Anycast IP address used for VXLAN termination</li>
</ul></td>
</tr>
<tr class="odd">
<td>All Alarms tab</td>
<td>Displays all MLAG events network-wide. By default, the event list is sorted by time, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a MLAG-related event. Example: Clag conflicted bond changed from swp7 swp8 to swp9 swp10</li>
<li><strong>Source</strong>: Hostname of network device that generated the event</li>
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>clag</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### View Service Status Summary

A summary of the MLAG service is available from the MLAG Service card workflow, including the number of nodes running the service, the number of MLAG-related alarms, and a distribution of those alarms.

To view the summary, open the small MLAG Service card.

{{< figure src="/images/netq/ntwk-svcs-all-mlag-small-230.png" width="200" >}}

For more detail, select a different size MLAG Service card.

### View the Distribution of Sessions and Alarms

It is useful to know the number of network nodes running the MLAG protocol over a period of time, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol. It is also useful to compare the number of nodes running MLAG with the alarms present at the same time to determine if there is any correlation between the issues and the ability to establish a MLAG session.

To view these distributions, open the medium MLAG Service card.

{{< figure src="/images/netq/ntwk-svcs-all-mlag-medium-230.png" width="200" >}}

If a visual correlation is apparent, you can dig a little deeper with the large MLAG Service card tabs.

### View Devices with the Most CLAG Sessions

You can view the load from MLAG on your switches using the large MLAG Service card. This data enables you to see which switches are handling the most MLAG traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most MLAG sessions:

1. Open the large MLAG Service card.

2. Select **Switches with Most Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes running the most MLAG sessions at the top. Scroll down to view those with the fewest sessions.

    {{< figure src="/images/netq/ntwk-svcs-all-mlag-large-most-sessions-230.png" width="500" >}}

To compare this data with the same data at a previous time:

1. Open another large MLAG Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the current time. You can now see whether there are significant differences between this time period and the previous time period.  

    {{< figure src="/images/netq/time-picker-popup-narrow-222.png" width="150" >}}

    {{< figure src="/images/netq/ntwk-svcs-all-mlag-large-most-sessions-6hr-230.png" width="500" >}}

    If the changes are unexpected, you can investigate further by looking at another timeframe, determining if more nodes are now running MLAG than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Unestablished MLAG Sessions

You can identify switches that are experiencing difficulties establishing MLAG sessions; both currently and in the past.

To view switches with the most unestablished MLAG sessions:

1. Open the large MLAG Service card.

2. Select **Switches with Most Unestablished Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most unestablished MLAG sessions at the top. Scroll down to view those with the fewest unestablished sessions.

    {{< figure src="/images/netq/ntwk-svcs-all-mlag-large-most-unestab-230.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most unestablished sessions, you might want to look more carefully at those switches using the Switches card workflow to determine probable causes. Refer to {{<link title="Monitor Switches">}}.

- Click **Show All Sessions** to investigate all MLAG sessions with events in the full screen card.

### View Switches with the Most MLAG-related Alarms

Switches experiencing a large number of MLAG alarms may indicate a configuration or performance issue that needs further investigation. You can view the switches sorted by the number of MLAG alarms and then use the Switches card workflow or the Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with most MLAG alarms:

1. Open the large MLAG Service card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Events by Most Active Device** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most MLAG alarms at the top. Scroll down to view those with the fewest alarms.

    {{< figure src="/images/netq/ntwk-svcs-all-mlag-large-alarms-tab-230.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.  

- Click **Show All Sessions** to investigate all MLAG sessions with alarms in the full screen card.

### View All MLAG Events

The MLAG Service card workflow enables you to view all of the MLAG events in the designated time period.

To view all MLAG events:

1. Open the full screen MLAG Service card.

2. Click **All Alarms** tab.

    {{<figure src="/images/netq/ntwk-svcs-all-mlag-fullscr-all-alarms-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open the **All Switches** or **All Sessions** tabs to look more closely at the alarms from the switch or session perspective.
- Sort on other parameters:
    - by **Message** to determine the frequency of particular events
    - by **Severity** to determine the most critical events
    - by **Time** to find events that may have occurred at a particular time to try to correlate them with other system events
- Export the data to a file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner

### View Details About All Switches Running MLAG

You can view all stored attributes of all switches running MLAG in your network in the full-screen card.

To view all switch details, open the full screen MLAG Service card, and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-mlag-fullscr-all-switches-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}} for more detail. To return to original display of results, click the associated tab.

## Monitor a Single MLAG Session

With NetQ, you can monitor the number of nodes running the MLAG service, view switches with the most peers alive and not alive, and view alarms triggered by the MLAG service. For an overview and how to configure MLAG in your data center network, refer to [Multi-Chassis Link Aggregation - MLAG]({{<ref "/cumulus-linux-43/Layer-2/Multi-Chassis-Link-Aggregation-MLAG" >}}).

{{%notice note%}}
To access the single session cards, you must open the full screen MLAG Service, click the All Sessions tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Open Cards).
{{%/notice%}}

### Granularity of Data Shown Based on Time Period

On the medium and large single MLAG session cards, the status of the peers is represented in heat maps stacked vertically; one for peers that are reachable (alive), and one for peers that are unreachable (not alive). Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all peers during that time period were alive for the entire time block, then the top block is 100% saturated (white) and the not alive block is zero percent saturated (gray). As peers that are not alive increase in saturation, the peers that are alive block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks.

{{<figure src="/images/netq/ntwk-svcs-single-mlag-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### MLAG Session Card Workflow Summary

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
<td>Indicates data is for a single session of a Network Service or Protocol</td>
</tr>
<tr class="even">
<td>Title</td>
<td>CLAG Session</td>
</tr>
<tr class="odd">
<td> </td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | MLAG Session</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
</tr>
<tr class="even">
<td>Time period (above chart)</td>
<td>Range of time for data displayed in peer status chart</td>
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
<td>System MAC address of the MLAG session</td>
</tr>
<tr class="even">
<td>Peer Role</td>
<td>Role that peer device is playing. Values include primary and secondary.</td>
</tr>
<tr class="odd">
<td>Peer State</td>
<td>Operational state of the peer, up (true) or down (false)</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>(Network Services | MLAG Session) Session Summary</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
</tr>
<tr class="even">
<td>Alarm Count Chart</td>
<td>Distribution and count of CLAG alarm events over the given time period</td>
</tr>
<tr class="odd">
<td>Info Count Chart</td>
<td>Distribution and count of CLAG info events over the given time period</td>
</tr>
<tr class="even">
<td>Peer Status chart</td>
<td>Distribution of peer availability, alive or not alive, during the designated time period. The number of time segments in a time period varies according to the length of the time period.</td>
</tr>
<tr class="odd">
<td>Backup IP</td>
<td>IP address of the interface to use if the peerlink (or bond) goes down</td>
</tr>
<tr class="even">
<td>Backup IP Active</td>
<td>Indicates whether the backup IP address is configured</td>
</tr>
<tr class="odd">
<td>CLAG SysMAC</td>
<td>System MAC address of the MLAG session</td>
</tr>
<tr class="even">
<td>Peer State</td>
<td>Operational state of the peer, up (true) or down (false)</td>
</tr>
<tr class="odd">
<td>Count of Dual Bonds</td>
<td>Number of bonds connecting to both switches</td>
</tr>
<tr class="even">
<td>Count of Single Bonds</td>
<td>Number of bonds connecting to only one switch</td>
</tr>
<tr class="odd">
<td>Count of Protocol Down Bonds</td>
<td>Number of bonds with interfaces that were brought down by the <code>clagd</code> service</td>
</tr>
<tr class="even">
<td>Count of Conflicted Bonds</td>
<td>Number of bonds which have a set of interfaces that are not the same on both switches</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/></td>
<td>Indicates configuration file information for a single session of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>(Network Services | MLAG Session) Configuration File Evolution</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
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
<li><strong>Backup Ip</strong>: IP address of the interface to use if the peerlink (or bond) goes down</li>
<li><strong>Backup Ip Active</strong>: Indicates whether the backup IP address has been specified and is active (true) or not (false)</li>
<li><strong>Bonds</strong>
<ul>
<li>Conflicted: Identifies the set of interfaces in a bond that do not match on each end of the bond</li>
<li>Single: Identifies a set of interfaces connecting to only one of the two switches</li>
<li>Dual: Identifies a set of interfaces connecting to both switches</li>
<li>Proto Down: Interface on the switch brought down by the <code>clagd</code> service. Value is blank if no interfaces are down due to <code>clagd</code> service.</li>
</ul></li>
<li><strong>Mlag Sysmac</strong>: Unique MAC address for each bond interface pair. <strong>Note</strong>: Must be a value between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff.</li>
<li><strong>Peer</strong>:
<ul>
<li>If: Name of the peer interface</li>
<li>Role: Role of the peer device. Values include primary and secondary.</li>
<li>State: Indicates if peer device is up (true) or down (false)</li>
</ul></li>
<li><strong>Role</strong>: Role of the host device. Values include primary and secondary.</li>
<li><strong>Timestamp</strong>: Date and time the MLAG session was started, deleted, updated, or marked dead (device went down)</li>
<li><strong>Vxlan Anycast</strong>: Anycast IP address used for VXLAN termination</li>
</ul></td>
</tr>
<tr class="even">
<td>All Events tab</td>
<td>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of an event. Example: Clag conflicted bond changed from swp7 swp8 to swp9 swp10</li>
<li><strong>Source</strong>: Hostname of network device that generated the event</li>
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>clag</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### View Session Status Summary

A summary of the MLAG session is available from the MLAG Session card workflow, showing the node and its peer and current status.

To view the summary:

1. Open the full screen MLAG Service card.

2. Select a session from the listing to view.

3. Close the full screen card to view the medium MLAG Session card.  

    {{< figure src="/images/netq/ntwk-svcs-single-mlag-medium-summ-highlighted-bad-230.png" width="200" >}}
    
    {{< figure src="/images/netq/ntwk-svcs-single-mlag-medium-summ-highlighted-230.png" width="200" >}}

    In the left example, we see that the tor1 switch plays the secondary role in this session with the switch at 44:38:39:ff:01:01. In the right example, we see that the leaf03 switch plays the primary role in this session with leaf04.

### View MLAG Session Peering State Changes

You can view the peering state for a given MLAG session from the medium and large MLAG Session cards. For a given time period, you can determine the stability of the MLAG session between two devices. If you experienced connectivity issues at a particular time, you can use these cards to help verify the state of the peer. If the peer was not alive more than it was alive, you can then investigate further into possible causes.

To view the state transitions for a given MLAG session:

1. Open the full screen MLAG Service card.

2. Select a session from the listing to view.

3. Close the full screen card to view the medium MLAG Session card.

    {{< figure src="/images/netq/ntwk-svcs-single-mlag-medium-chart-highlighted-230.png" width="200" >}}

    In this example, the peer switch has been alive for the entire 24-hour period.

From this card, you can also view the node role, peer role and state, and MLAG system MAC address which identify the session in more detail.

To view the peering state transitions for a given MLAG session on the large MLAG Session card, open that card.

{{< figure src="/images/netq/ntwk-svcs-single-mlag-large-session-tab-chart-highlighted-230.png" width="500" >}}

From this card, you can also view the alarm and info event counts, node role, peer role, state, and interface, MLAG system MAC address, active backup IP address, single, dual, conflicted, and protocol down bonds, and the VXLAN anycast address identifying the session in more detail.

### View Changes to the MLAG Service Configuration File

Each time a change is made to the configuration file for the MLAG service, NetQ logs the change and enables you to compare it with the last version. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

To view the configuration file changes:

1. Open the large MLAG Session card.

2. Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> to open the **Configuration File Evolution** tab.

3. Select the time of interest on the left; when a change may have impacted the performance. Scroll down if needed.

4. Choose between the **File** view and the **Diff** view (selected option is dark; File by default).  

    The File view displays the content of the file for you to review.

    {{< figure src="/images/netq/ntwk-svcs-single-mlag-large-config-tab-file-230.png" width="500" >}}

    The Diff view displays the changes between this version (on left) and the most recent version (on right) side by side. The changes are     highlighted in red and green. In this example, we don't have any changes after this first creation, so the same file is shown on both sides and no highlighting is present.

    {{< figure src="/images/netq/ntwk-svcs-single-mlag-large-config-tab-diff-230.png" width="500" >}}

### All MLAG Session Details

You can view all stored attributes of all of the MLAG sessions associated with the two devices on this card.

To view all session details, open the full screen MLAG Session card, and click the **All MLAG Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-single-mlag-fullscr-allsess-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open the **All Events** tabs to look more closely at the alarm and info events fin the network.
- Sort on other parameters:
    - by **Single Bonds** to determine which interface sets are only connected to one of the switches
    - by **Backup IP and Backup IP Active** to determine if the correct backup IP address is specified for the service
- Export the data to a file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner

### View All MLAG Session Events

You can view all of the alarm and info events for the two devices on this card.

To view all events, open the full screen MLAG Session card, and click the **All Events** tab.

{{<figure src="/images/netq/ntwk-svcs-single-mlag-fullscr-events-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open the **All MLAG Sessions** tabs to look more closely at the individual sessions.
- Sort on other parameters:
    - by **Message** to determine the frequency of particular events
    - by **Severity** to determine the most critical events
    - by **Time** to find events that may have occurred at a particular time to try to correlate them with other system events
- Export the data to a file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner
