---
title: Monitor the LLDP Service
author: Cumulus Networks
weight: 390
toc: 4
---
The Cumulus NetQ UI enables operators to view the health of the LLDP service on a network-wide and a per session basis, giving greater insight into all aspects of the service. This is accomplished through two card workflows, one for the service and one for the session. They are described separately here.

## Monitor the LLDP Service (All Sessions)

With NetQ, you can monitor the number of nodes running the LLDP service, view nodes with the most LLDP neighbor nodes, those nodes with the least neighbor nodes, and view alarms triggered by the LLDP service. For an overview and how to configure LLDP in your data center network, refer to [Link Layer Discovery Protocol]({{<ref "/cumulus-linux-43/Layer-2/Link-Layer-Discovery-Protocol" >}}).

### LLDP Service Card Workflow Summary

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
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="even">
<td>Title</td>
<td>LLDP: All LLDP Sessions, or the LLDP Service</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the LLDP service enabled during the designated time period</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of LLDP-related alarms received during the designated time period</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of LLDP-related alarms received during the designated time period</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>LLDP: All LLDP Sessions, or the LLDP Service</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the LLDP service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of LLDP-related alarms received during the designated time period</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Sessions Summary (Network Services | All LLDP Sessions)</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the LLDP service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of LLDP-related alarms received during the designated time period</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the LLDP service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running LLDP last week or last month might be more or less than the number of nodes running LLDP currently.</p></td>
</tr>
<tr class="odd">
<td>Total Sessions chart</td>
<td>Distribution of LLDP sessions running during the designated time period, and the total number of sessions running on the network currently</td>
</tr>
<tr class="even">
<td>Total Sessions with No Nbr chart</td>
<td>Distribution of LLDP sessions missing neighbor information during the designated time period, and the total number of session missing neighbors in the network currently</td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td><p>When the <strong>Switches with Most Sessions</strong> filter is selected, the table displays switches running LLDP sessions in decreasing order of session count-devices with the largest number of sessions are listed first</p>
<p>When the <strong>Switches with Most Unestablished Sessions</strong> filter is selected, the table displays switches running LLDP sessions in decreasing order of unestablished session count-devices with the largest number of unestablished sessions are listed first</p></td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view all LLDP sessions in the full screen card</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in header)</td>
<td>Indicates data is all alarms for all LLDP sessions</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Alarms (visible when you hover over card)</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches with the LLDP service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in summary bar)</td>
<td>Total number of LLDP-related alarms received during the designated time period</td>
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
<td>Link to view all LLDP sessions in the full screen card</td>
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
<td>Network Services | LLDP</td>
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
<li>Revision: Release version of the platform</li>
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
<li><strong>Message</strong>: Text description of a LLDP-related event. Example: LLDP Session with host leaf02 swp6 modified fields leaf06 swp21</li>
<li><strong>Source</strong>: Hostname of network device that generated the event</li>
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>lldp</em> in this card workflow.</li>
</ul></td>
</tr>
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### View Service Status Summary

A summary of the LLDP service is available from the Network Services card workflow, including the number of nodes running the service, the number of LLDP-related alarms, and a distribution of those alarms.

To view the summary, open the small LLDP Service card.

{{< figure src="/images/netq/ntwk-svcs-all-lldp-small-230.png" width="200" >}}

In this example, there are no LLDP alarms present on the network of 14 devices.

For more detail, select a different size LLDP Network Services card.

### View the Distribution of Nodes, Alarms, and Sessions

It is useful to know the number of network nodes running the LLDP protocol over a period of time, as it gives you insight into nodes that might be misconfigured or experiencing communication issues. Additionally, if there are a large number of alarms, it is worth investigating either the service or particular devices.

To view the distribution, open the medium LLDP Service card.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-medium.png" width="200">}}

In this example, we see that 13 nodes are running the LLDP protocol, that there are 52 sessions established, and that no LLDP-related alarms have occurred in the last 24 hours.

### View the Distribution of Missing Neighbors

You can view the number of missing neighbors in any given time period and how that number has changed over time. This is a good indicator of link communication issues.

To view the distribution, open the large LLDP Service card and view the bottom chart on the left, **Total Sessions with No Nbr**.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-no-nbr-highlight-230.png" width="500">}}

In this example, we see that 16 of the 52 sessions are missing the neighbor (peer) device.

### View Devices with the Most LLDP Sessions

You can view the load from LLDP on your switches using the large LLDP Service card. This data enables you to see which switches are handling the most LLDP traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most LLDP sessions:

1. Open the large LLDP Service card.

2. Select **Switches with Most Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes running the most LLDP sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-300.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large LLDP Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4.  Select the time period that you want to compare with the current time. You can now see whether there are significant differences between     this time period and the previous time period.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-past-week-300.png" width="500" >}}

    In this case, notice that their are fewer nodes running the protocol, but the total number of sessions running has nearly doubled. If the changes are unexpected, you can investigate further by looking at another timeframe, determining if more nodes are now running LLDP than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Unestablished LLDP Sessions

You can identify switches that are experiencing difficulties establishing LLDP sessions; both currently and in the past.

To view switches with the most unestablished LLDP sessions:

1. Open the large LLDP Service card.

2. Select **Switches with Most Unestablished Sessions** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes with the most unestablished CLAG sessions at the top. Scroll down to     view those with the fewest unestablished sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-most-unestab-300.png" width="500">}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time.

    If the same switches are consistently indicating the most unestablished sessions, you might want to look more carefully at those switches using the Switches card workflow to determine probable causes. Refer to {{<link title="Monitor Switches">}}.

- Click **Show All Sessions** to investigate all LLDP sessions with events in the full screen card.

### View Switches with the Most LLDP-related Alarms

Switches experiencing a large number of LLDP alarms may indicate a configuration or performance issue that needs further investigation. You can view the switches sorted by the number of LLDP alarms and then use the Switches card workflow or the Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with most LLDP alarms:

1. Open the large LLDP Service card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Events by Most Active Device** from the filter above the  table.

    The table content is sorted by this characteristic, listing nodes with the most BGP alarms at the top. Scroll down to view those with the fewest alarms.

    {{< figure src="/images/netq/ntwk-svcs-all-lldp-large-alarms-tab.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Hover over the Total Alarms chart to focus on the switches exhibiting alarms during that smaller time slice. The table content changes to match the hovered content. Click on the chart to persist the table changes.
- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.
- Click **Show All Sessions** to investigate all switches running LLDP sessions in the full screen card.

### View All LLDP Events

The LLDP Network Services card workflow enables you to view all of the LLDP events in the designated time period.

To view all LLDP events:

1. Open the full screen LLDP Service card.

2. Click the **All Alarms** tab.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-alarms-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open the **All Switches** or **All Sessions** tabs to look more closely at the alarms from the switch or session perspective.
- Sort on other parameters:
    - by **Message** to determine the frequency of particular events
    - by **Severity** to determine the most critical events
    - by **Time** to find events that may have occurred at a particular time to try to correlate them with other system events
- Export data to a file
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner

### View Details About All Switches Running LLDP

You can view all stored attributes of all switches running LLDP in your network in the full screen card.

To view all switch details, open the LLDP Service card, and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-allswitches-tab-241.png" width="700">}}

Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View Detailed Information About All LLDP Sessions

You can view all stored attributes of all LLDP sessions in your network
in the full screen card.

To view all session details, open the LLDP Service card, and click the
**All Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-allsess-tab-241.png" width="700">}}

Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}} for more detail. To return to original display of results, click the associated tab.

## Monitor a Single LLDP Session

With NetQ, you can monitor the number of nodes running the LLDP service, view neighbor state changes, and compare with events occurring at the same time, as well as monitor the running LLDP configuration and changes to the configuration file. For an overview and how to configure LLDP in your data center network, refer to [Link Layer Discovery Protocol]({{<ref "/cumulus-linux-43/Layer-2/Link-Layer-Discovery-Protocol" >}}).

{{%notice note%}}
To access the single session cards, you must open the full screen LLDP Service card, click the All Sessions tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18"/> (Open Cards).
{{%/notice%}}

### Granularity of Data Shown Based on Time Period

On the medium and large single LLDP session cards, the status of the neighboring peers is represented in heat maps stacked vertically; one for peers that are reachable (neighbor detected), and one for peers that are unreachable (neighbor not detected). Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all peers during that time period were detected for the entire time block, then the top block is 100% saturated (white) and the neighbor not detected block is zero percent saturated (gray). As peers become reachable, the neighbor detected block increases in saturation, the peers that are unreachable (neighbor not detected) block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks.

{{<figure src="/images/netq/ntwk-svcs-single-lldp-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### LLDP Session Card Workflow Summary

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
<td>Indicates data is for a single session of a Network Service or Protocol</td>
</tr>
<tr class="even">
<td>Title</td>
<td>LLDP Session</td>
</tr>
<tr class="odd">
<td> </td>
<td>Host and peer devices in session. Host is shown on top, with peer below.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indicates whether the host sees the peer or not; <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> has a peer, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> no peer</td>
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
<td>Range of time in which the displayed data was collected</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>LLDP Session</td>
</tr>
<tr class="even">
<td> </td>
<td>Host and peer devices in session. Arrow points from host to peer.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indicates whether the host sees the peer or not; <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> has a peer, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> no peer</td>
</tr>
<tr class="even">
<td>Time period</td>
<td>Range of time for the distribution chart</td>
</tr>
<tr class="odd">
<td>Heat map</td>
<td>Distribution of neighbor availability (detected or undetected) during this given time period</td>
</tr>
<tr class="even">
<td>Hostname</td>
<td>User-defined name of the host device</td>
</tr>
<tr class="odd">
<td>Interface Name</td>
<td>Software interface on the host device where the session is running</td>
</tr>
<tr class="even">
<td>Peer Hostname</td>
<td>User-defined name of the peer device</td>
</tr>
<tr class="odd">
<td>Peer Interface Name</td>
<td>Software interface on the peer where the session is running</td>
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
<td>Range of time in which the displayed data was collected</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg" height="22" width="22"/></td>
<td>Indicates data is for a single session of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Summary Session (Network Services | LLDP Session)</td>
</tr>
<tr class="even">
<td> </td>
<td>Host and peer devices in session. Arrow points from host to peer.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indicates whether the host sees the peer or not; <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> has a peer, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> no peer</td>
</tr>
<tr class="even">
<td>Heat map</td>
<td>Distribution of neighbor state (detected or undetected) during this given time period</td>
</tr>
<tr class="odd">
<td>Alarm Count chart</td>
<td>Distribution and count of LLDP alarm events during the given time period</td>
</tr>
<tr class="even">
<td>Info Count chart</td>
<td>Distribution and count of LLDP info events during the given time period</td>
</tr>
<tr class="odd">
<td>Host Interface Name</td>
<td>Software interface on the host where the session is running</td>
</tr>
<tr class="even">
<td>Peer Hostname</td>
<td>User-defined name of the peer device</td>
</tr>
<tr class="odd">
<td>Peer Interface Name</td>
<td>Software interface on the peer where the session is running</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/></td>
<td>Indicates configuration file information for a single session of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>(Network Services | LLDP Session) Configuration File Evolution</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Indicates whether the host sees the peer or not; <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> has a peer, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> no peer</td>
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
<td>Network Services | LLDP</td>
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
<td>All LLDP Sessions tab</td>
<td>Displays all LLDP sessions on the host device. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
<ul>
<li><strong>Ifname</strong>: Name of the host interface where LLDP session is running</li>
<li><strong>LLDP</strong> <strong>Peer</strong>:
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
<tr class="even">
<td>All Events tab</td>
<td>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of an event. Example: LLDP Session with host leaf02 swp6 modified fields leaf06 swp21</li>
<li><strong>Source</strong>: Hostname of network device that generated the event</li>
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

### View Session Status Summary

A summary of the LLDP session is available from the LLDP Session card workflow, showing the node and its peer and current status.

To view the summary:

1. Open the full screen LLDP Service card.

2. Double-click on a session. The full screen card closes automatically.

3. Locate the medium LLDP Session card.

4. Optionally, open the small LLDP Session card.  

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-medium-summary-highlight-230.png" width="200">}}

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-small-230.png" width="200">}}

### View LLDP Session Neighbor State Changes

You can view the neighbor state for a given LLDP session from the medium and large LLDP Session cards. For a given time period, you can determine the stability of the LLDP session between two devices. If you experienced connectivity issues at a particular time, you can use these cards to help verify the state of the neighbor. If the neighbor was not alive more than it was alive, you can then investigate further into possible causes.

To view the neighbor availability for a given LLDP session on the medium card:

1. Open the full screen LLDP Service card.

2. Double-click on a session. The full screen card closes automatically.

3. Locate the medium LLDP Session card.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-medium-nbr-state-highlight-230.png" width="200">}}

In this example, the heat map tells us that this LLDP session has been able to detect a neighbor for the entire time period.

From this card, you can also view the host name and interface name, and the peer name and interface name.

To view the neighbor availability for a given LLDP session on the large LLDP Session card, open that card.

{{<figure src="/images/netq/ntwk-svcs-single-lldp-large-nbr-state-highlight-230.png" width="500">}}

From this card, you can also view the alarm and info event counts, host interface name, peer hostname, and peer interface identifying the session in more detail.

### View Changes to the LLDP Service Configuration File

Each time a change is made to the configuration file for the LLDP service, NetQ logs the change and enables you to compare it with the last version. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

To view the configuration file changes:

1. Open the large LLDP Session card.

2. Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> to open the **LLDP Configuration File Evolution** tab.

3. Select the time of interest on the left; when a change may have impacted the performance. Scroll down if needed.

4. Choose between the **File** view and the **Diff** view (selected option is dark; File by default). 

    The File view displays the content of the file for you to review.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-large-config-tab-file-selected-230.png" width="500">}}

    The Diff view displays the changes between this version (on left) and the most recent version (on right) side by side. The changes are     highlighted in red and green. In this example, we don't have any changes to the file, so the same file is shown on both sides, and thus no highlighted lines.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-large-config-tab-diff-selected-230.png" width="500">}}

### View All LLDP Session Details

You can view all stored attributes of all of the LLDP sessions associated with the two devices on this card.

To view all session details, open the full screen LLDP Session card, and click the **All LLDP Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-single-lldp-fullscr-allsess-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right of the card.

### View All Events

You can view all of the alarm and info events in the network.

To view all events, open the full screen LLDP Session card, and click the **All Events** tab.

{{<figure src="/images/netq/ntwk-svcs-single-lldp-fullscr-events-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open the **All LLDP Sessions** tabs to look more closely at the details of the sessions between these two devices.
- Sort on other parameters:
  - by **Message** to determine the frequency of particular events
  - by **Severity** to determine the most critical events
  - by **Time** to find events that may have occurred at a particular time to try to correlate them with other system events
- Export data to a file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner
