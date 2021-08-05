---
title: Monitor the EVPN Service
author: Cumulus Networks
weight: 380
toc: 4
---
The Cumulus NetQ UI enables operators to view the health of the EVPN service on a network-wide and a per session basis, giving greater insight into all aspects of the service. This is accomplished through two card workflows, one for the service and one for the session. They are described separately here.

## Monitor the EVPN Service (All Sessions)

With NetQ, you can monitor the number of nodes running the EVPN service, view switches with the sessions, total number of VNIs, and alarms triggered by the EVPN service. For an overview and how to configure EVPN in your data center network, refer to [Ethernet Virtual Private Network-EVPN]({{<ref "/cumulus-linux-43/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN" >}}).

### EVPN Service Card Workflow Summary

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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | All EVPN Sessions</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the EVPN service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of EVPN-related alarms received during the designated time period</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the EVPN service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running EVPN last week or last month might be more or less than the number of nodes running EVPN currently.</p></td>
</tr>
<tr class="odd">
<td>Total Open Alarms chart</td>
<td><p>Distribution of EVPN-related alarms received during the designated time period, and the total number of current EVPN-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="even">
<td>Total Sessions chart</td>
<td>Distribution of EVPN sessions during the designated time period, and the total number of sessions running on the network currently.</td>
</tr>
</tbody>
</table>

The large EVPN service card contains two tabs.

The *Sessions Summary* tab which displays:

{{< figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-230.png" width="500" >}}

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
<td>Sessions Summary (visible when you hover over card)</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the EVPN service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of EVPN-related alarms received during the designated time period</td>
</tr>
<tr class="even">
<td>Total Nodes Running chart</td>
<td><p>Distribution of switches and hosts with the EVPN service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running EVPN last week or last month might be more or less than the number of nodes running EVPN currently.</p></td>
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
<td>Link to view data for all EVPN sessions network-wide in the full screen card</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in header)</td>
<td>Indicates data is for all alarms for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Alarms (visible when you hover over card)</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the EVPN service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in summary bar)</td>
<td>Total number of EVPN-related alarms received during the designated time period</td>
</tr>
<tr class="even">
<td>Total Alarms chart</td>
<td><p>Distribution of EVPN-related alarms received during the designated time period, and the total number of current BGP-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td>When the <strong>Events by Most Active Device</strong> filter is selected, the table displays devices running EVPN sessions in decreasing order of alarm count-devices with the largest number of alarms are listed first</td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view data for all EVPN sessions in the full screen card</td>
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
<td>Displays all EVPN sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
<ul>
<li><strong>Adv All Vni</strong>: Indicates whether the VNI state is advertising all VNIs (true) or not (false)</li>
<li><strong>Adv Gw Ip</strong>: Indicates whether the host device is advertising the gateway IP address (true) or not (false)</li>
<li><strong>DB State</strong>: Session state of the DB</li>
<li><strong>Export RT</strong>: IP address and port of the export route target used in the filtering mechanism for BGP route exchange</li>
<li><strong>Import RT</strong>: IP address and port of the import route target used in the filtering mechanism for BGP route exchange</li>
<li><strong>In Kernel</strong>: Indicates whether the associated VNI is in the kernel (in kernel) or not (not in kernel)</li>
<li><strong>Is L3</strong>: Indicates whether the session is part of a layer 3 configuration (true) or not (false)</li>
<li><strong>Origin Ip</strong>: Host device's local VXLAN tunnel IP address for the EVPN instance</li>
<li><strong>OPID</strong>: LLDP service identifier</li>
<li><strong>Rd</strong>: Route distinguisher used in the filtering mechanism for BGP route exchange</li>
<li><strong>Timestamp</strong>: Date and time the session was started, deleted, updated or marked as dead (device is down)</li>
<li><strong>Vni</strong>: Name of the VNI where session is running</li>
</ul></td>
</tr>
<tr class="odd">
<td>All Alarms tab</td>
<td>Displays all EVPN events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a EVPN-related event. Example: VNI 3 kernel state changed from down to up</li>
<li><strong>Source</strong>: Hostname of network device that generated the event</li>
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>evpn</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### View Service Status Summary

A summary of the EVPN service is available from the Network Services card workflow, including the number of nodes running the service, the number of EVPN-related alarms, and a distribution of those alarms.

To view the summary, open the small EVPN Network Service card.

{{< figure src="/images/netq/ntwk-svcs-all-evpn-small-230.png" width="200" >}}

For more detail, select a different size EVPN Network Service card.

### View the Distribution of Sessions and Alarms

It is useful to know the number of network nodes running the EVPN protocol over a period of time, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol. It is also useful to compare the number of nodes running EVPN with the alarms present at the same time to determine if there is any correlation between the issues and the ability to establish an EVPN session.

To view these distributions, open the medium EVPN Service card.

{{< figure src="/images/netq/ntwk-svcs-all-evpn-medium-230.png" width="200" >}}

If a visual correlation is apparent, you can dig a little deeper with the large EVPN Service card tabs.

### View the Distribution of Layer 3 VNIs

It is useful to know the number of layer 3 VNIs, as it gives you insight into the complexity of the VXLAN.

To view this distribution, open the large EVPN Service card and view the bottom chart on the left.

{{< figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-vni-chart-230.png" width="500" >}}

### View Devices with the Most EVPN Sessions

You can view the load from EVPN on your switches and hosts using the large EVPN Service card. This data enables you to see which switches are handling the most EVPN traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most EVPN sessions:

1. Open the large EVPN Service card.

2. Select **Top Switches with Most Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes running the most EVPN sessions at the top. Scroll down to view those with the fewest sessions.

    {{< figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-top-sessions-230.png" width="500" >}}

To compare this data with the same data at a previous time:

1. Open another large EVPN Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4.  Select the time period that you want to compare with the current time.  

    You can now see whether there are significant differences between this time period and the previous time period.  

    {{< figure src="/images/netq/time-picker-popup-narrow-222.png" width="150" >}}

    {{< figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-past-week-230.png" width="500" >}}

If the changes are unexpected, you can investigate further by looking at another timeframe, determining if more nodes are now running EVPN than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Layer 2 EVPN Sessions

You can view the number layer 2 EVPN sessions on your switches and hosts using the large EVPN Service card. This data enables you to see which switches are handling the most EVPN traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most layer 2 EVPN sessions:

1. Open the large EVPN Service card.

2. Select **Switches with Most L2 EVPN** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes running the most layer 2 EVPN sessions at the top. Scroll down to view those with the fewest sessions.

    {{< figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l2evpn-230.png" width="500" >}}

To compare this data with the same data at a previous time:

1. Open another large EVPN Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the current time.  

    You can now see whether there are significant differences between this time period and the previous time period.  

    {{< figure src="/images/netq/time-picker-popup-narrow-222.png" width="150" >}}

    {{< figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l2-pst-wk-230.png" width="500" >}}

If the changes are unexpected, you can investigate further by looking at another timeframe, determining if more nodes are now running EVPN than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Layer 3 EVPN Sessions

You can view the number layer 3 EVPN sessions on your switches and hosts using the large EVPN Service card. This data enables you to see which switches are handling the most EVPN traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most layer 3 EVPN sessions:

1. Open the large EVPN Service card.

2. Select **Switches with Most L3 EVPN** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes running the most layer 3 EVPN sessions at the top. Scroll down to view those with the fewest sessions.

    {{< figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l3evpn-230.png" width="500" >}}

To compare this data with the same data at a previous time:

1. Open another large EVPN Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the current time.  

    You can now see whether there are significant differences between this time period and the previous time period.  

    {{< figure src="/images/netq/time-picker-popup-narrow-222.png" width="150" >}}

    {{< figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l3-pst-wk-230.png" width="500" >}}

If the changes are unexpected, you can investigate further by looking at another timeframe, determining if more nodes are now running EVPN than previously, looking for changes in the topology, and so forth.

### View Devices with the Most EVPN-related Alarms

Switches experiencing a large number of EVPN alarms may indicate a configuration or performance issue that needs further investigation. You can view the switches sorted by the number of BGP alarms and then use the Switches card workflow or the Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with the most EVPN alarms:

1. Open the large EVPN Service card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Events by Most Active Device** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most EVPN alarms at the top. Scroll down to view those with the fewest alarms.

    {{< figure src="/images/netq/ntwk-svcs-all-evpn-large-alarms-tab-230.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Hover over the Total Alarms chart to focus on the switches exhibiting alarms during that smaller time slice. The table content changes to match the hovered content. Click on the chart to persist the table changes.
- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.
- Click **Show All Sessions** to investigate all EVPN sessions network-wide in the full screen card.

### View All EVPN Events

The EVPN Service card workflow enables you to view all of the EVPN events in the designated time period.

To view all EVPN events:

1. Open the full screen EVPN Service card.

2. Click **All Alarms** tab in the navigation panel. By default, events are sorted by Time, with most recent events listed first.

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-alarms-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options
include:

- Open one of the other full screen tabs in this flow to focus on devices or sessions.
- Sort by the **Message** or **Severity** to narrow your focus.
- Export the data for use in another analytics tool, by selecting all or some of the events and clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right to return to your workbench.

### View Details for All Devices Running EVPN

You can view all stored attributes of all switches running EVPN in your network in the full screen card.

To view all switch and host details, open the full screen EVPN Service card, and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-allswitches-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right.

### View Details for All EVPN Sessions

You can view all stored attributes of all EVPN sessions in your network in the full screen card.

To view all session details, open the full screen EVPN Service card, and click the **All Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-sessions-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}} for more detail.

To return to original display of results, click the associated tab.

## Monitor a Single EVPN Session

With NetQ, you can monitor the performance of a single EVPN session, including the number of associated VNI, VTEPs and type. For an overview and how to configure EVPN in your data center network, refer to [Ethernet Virtual Private Network - EVPN]({{<ref "/cumulus-linux-43/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN" >}}).

{{%notice note%}}
To access the single session cards, you must open the full screen EVPN Service, click the All Sessions tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18"/> (Open Cards).
{{%/notice%}}

### EVPN Session Card Workflow Summary

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
<td>Network Services | EVPN Session</td>
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
<td>Indicates whether the session is established as part of a layer 2 or layer 3 overlay network</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/></td>
<td>Indicates configuration file information for a single session of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>(Network Services | EVPN Session) Configuration File Evolution</td>
</tr>
<tr class="even">
<td>{{<img src="/images/netq/ntwk-svcs-single-evpn-vtep-count-icon-230.png" width="20" height="20">}}</td>
<td>VTEP count (currently)</td>
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
<td>Network Services | EVPN</td>
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
<td>All EVPN Sessions tab</td>
<td>Displays all EVPN sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:
<ul>
<li><strong>Adv All Vni</strong>: Indicates whether the VNI state is advertising all VNIs (true) or not (false)</li>
<li><strong>Adv Gw Ip</strong>: Indicates whether the host device is advertising the gateway IP address (true) or not (false)</li>
<li><strong>DB State</strong>: Session state of the DB</li>
<li><strong>Export RT</strong>: IP address and port of the export route target used in the filtering mechanism for BGP route exchange</li>
<li><strong>Import RT</strong>: IP address and port of the import route target used in the filtering mechanism for BGP route exchange</li>
<li><strong>In Kernel</strong>: Indicates whether the associated VNI is in the kernel (in kernel) or not (not in kernel)</li>
<li><strong>Is L3</strong>: Indicates whether the session is part of a layer 3 configuration (true) or not (false)</li>
<li><strong>Origin Ip</strong>: Host device's local VXLAN tunnel IP address for the EVPN instance</li>
<li><strong>OPID</strong>: LLDP service identifier</li>
<li><strong>Rd</strong>: Route distinguisher used in the filtering mechanism for BGP route exchange</li>
<li><strong>Timestamp</strong>: Date and time the session was started, deleted, updated or marked as dead (device is down)</li>
<li><strong>Vni</strong>: Name of the VNI where session is running</li>
</ul></td>
</tr>
<tr class="even">
<td>All Events tab</td>
<td>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a EVPN-related event. Example: VNI 3 kernel state changed from down to up</li>
<li><strong>Source</strong>: Hostname of network device that generated the event</li>
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>evpn</em> in this card workflow.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### View Session Status Summary

A summary of the EVPN session is available from the EVPN Session card workflow, showing the node and its peer and current status.

To view the summary:

1. Add the Network Services | All EVPN Sessions card.

2. Switch to the full screen card.

3. Click the **All Sessions** tab.

4. Double-click the session of interest. The full screen card closes automatically.

5. Optionally, switch to the small EVPN Session card.  

    {{<figure src="/images/netq/ntwk-svcs-single-evpn-medium-230.png" width="200">}}

    {{<figure src="/images/netq/ntwk-svcs-single-evpn-small-230.png" width="200">}}

For more detail, select a different size EVPN Session card.

### View VTEP Count

You can view the count of VTEPs for a given EVPN session from the medium
and large EVPN Session cards.

To view the count for a given EVPN session, on the *medium* EVPN Session
card:

1. Add the Network Services | All EVPN Sessions card.

2. Switch to the full screen card.

3. Click the **All Sessions** tab.

4. Double-click the session of interest. The full screen card closes automatically.

    {{<figure src="/images/netq/ntwk-svcs-single-evpn-medium-vtep-count-230.png" width="200">}}

To view the count for a given EVPN session on the *large* EVPN Session card, follow the same steps as for the medium card and then switch to the large card.

{{<figure src="/images/netq/ntwk-svcs-single-evpn-large-summary-tab-vtep-cnt-230.png" width="500">}}

### View All EVPN Session Details

You can view all stored attributes of all of the EVPN sessions running network-wide.

To view all session details, open the full screen EVPN Session card and click the **All EVPN Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-single-evpn-fullscr-allsess-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right of the card.

### View All Events

You can view all of the alarm and info events occurring network wide.

To view all events, open the full screen EVPN Session card and click the **All Events** tab.

{{<figure src="/images/netq/ntwk-svcs-single-evpn-fullscr-events-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open one of the other full screen tabs in this flow to focus on sessions.
- Sort by the **Message** or **Severity** to narrow your focus.
- Export the data for use in another analytics tool, by selecting all or some of the events and clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right to return to your workbench.
