---
title: Monitor the BGP Service
author: Cumulus Networks
weight: 370
toc: 4
---
The Cumulus NetQ UI enables operators to view the health of the BGP service on a network-wide and a per session basis, giving greater insight into all aspects of the service. This is accomplished through two card workflows, one for the service and one for the session. They are described separately here.

## Monitor the BGP Service (All Sessions)

With NetQ, you can monitor the number of nodes running the BGP service, view switches with the most established and unestablished BGP sessions, and view alarms triggered by the BGP service. For an overview and how to configure BGP to run in your data center network, refer to [Border Gateway Protocol - BGP]({{<ref "/cumulus-linux-43/Layer-3/Border-Gateway-Protocol-BGP" >}}).

### BGP Service Card Workflow

The small BGP Service card displays:

{{< figure src="/images/netq/ntwk-svcs-all-bgp-small-230.png" width="200" >}}

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

{{< figure src="/images/netq/ntwk-svcs-all-bgp-medium-230.png" width="200" >}}

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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg" height="18" width="18"/></td>
<td>Indicates data is for all sessions of a Network Service or Protocol</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Network Services | All BGP Sessions</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the BGP service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of BGP-related alarms received during the designated time period</td>
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

{{< figure src="/images/netq/ntwk-svcs-all-bgp-large-summary-tab-230.png" width="500" >}}

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
<td>Total number of switches and hosts with the BGP service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/></td>
<td>Total number of BGP-related alarms received during the designated time period</td>
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
<td><p>When the <strong>Switches with Most Sessions</strong> filter option is selected, the table displays the switches and hosts running BGP sessions in decreasing order of session count-devices with the largest number of sessions are listed first</p>
<p>When the <strong>Switches with Most Unestablished Sessions</strong> filter option is selected, the table switches and hosts running BGP sessions in decreasing order of unestablished sessions-devices with the largest number of unestablished sessions are listed first</p></td>
</tr>
<tr class="odd">
<td>Show All Sessions</td>
<td>Link to view data for all BGP sessions in the full screen card</td>
</tr>
</tbody>
</table>

The *Alarms* tab displays:

{{< figure src="/images/netq/ntwk-svcs-all-bgp-large-alarms-tab-230.png" width="500" >}}

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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in header)</td>
<td>Indicates data is for all alarms for all BGP sessions</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Alarms (visible when you hover over card)</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg" height="18" width="18"/></td>
<td>Total number of switches and hosts with the BGP service enabled during the designated time period</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> (in summary bar)</td>
<td>Total number of BGP-related alarms received during the designated time period</td>
</tr>
<tr class="even">
<td>Total Alarms chart</td>
<td><p>Distribution of BGP-related alarms received during the designated time period, and the total number of current BGP-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="odd">
<td>Table/Filter options</td>
<td>When the selected filter option is <strong>Switches with Most Alarms</strong>, the table displays <strong></strong> switches and hosts running BGP in decreasing order of the count of alarms-devices with the largest number of BGP alarms are listed first</td>
</tr>
<tr class="even">
<td>Show All Sessions</td>
<td>Link to view data for all BGP sessions in the full screen card</td>
</tr>
</tbody>
</table>

The full screen BGP Service card provides tabs for all switches, all sessions, and all alarms.

{{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-allsess-tab-241.png" width="700">}}

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
<td>Network Services | BGP</td>
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
<li>Revision: Release version of the platform</li>
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
<li><strong>Conn Dropped</strong>: Number of dropped connections for a given session</li>
<li><strong>Conn Estd</strong>: Number of connections established for a given session</li>
<li><strong>DB State</strong>: Session state of DB</li>
<li><strong>Evpn Pfx Rcvd</strong>: Address prefix received for EVPN traffic. Examples include 115, 35.</li>
<li><strong>Ipv4, and Ipv6 Pfx Rcvd</strong>: Address prefix received for IPv4 or IPv6 traffic. Examples include 31, 14, 12.</li>
<li><strong>Last Reset Time</strong>: Date and time at which the session was last established or reset</li>
<li><strong>Objid</strong>: Object identifier for service</li>
<li><strong>OPID</strong>: Customer identifier. This is always zero.</li>
<li><strong>Peer</strong>
<ul>
<li>ASN: Autonomous System Number for peer device</li>
<li>Hostname: User-defined name for peer device</li>
<li>Name: Interface name or hostname of peer device</li>
<li>Router Id: IP address of router with access to the peer device</li>
</ul></li>
<li><strong>Reason</strong>: Text describing the cause of, or trigger for, an event</li>
<li><strong>Rx and Tx Families</strong>: Address families supported for the receive and transmit session channels. Values include ipv4, ipv6, and evpn.</li>
<li><strong>State</strong>: Current state of the session. Values include Established and NotEstd (not established).</li>
<li><strong>Timestamp</strong>: Date and time session was started, deleted, updated or marked dead (device is down)</li>
<li><strong>Upd8 Rx:</strong> Count of protocol messages received</li>
<li><strong>Upd8 Tx</strong>: Count of protocol messages transmitted</li>
<li><strong>Up Time</strong>: Number of seconds the session has been established, in EPOCH notation. Example: 1550147910000</li>
<li><strong>Vrf</strong>: Name of the Virtual Route Forwarding interface. Examples: default, mgmt, DataVrf1081</li>
<li><strong>Vrfid</strong>: Integer identifier of the VRF interface when used. Examples: 14, 25, 37</li>
</ul></td>
</tr>
<tr class="odd">
<td>All Alarms tab</td>
<td>Displays all BGP events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Source</strong>: Hostname of network device that generated the event</li>
<li><strong>Message</strong>: Text description of a BGP-related event. Example: BGP session with peer tor-1 swp7 vrf default state changed from failed to Established</li>
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

### View Service Status Summary

A summary of the BGP service is available from the Network Services card workflow, including the number of nodes running the service, the number of BGP-related alarms, and a distribution of those alarms.

To view the summary, open the small BGP Service card.

{{< figure src="/images/netq/ntwk-svcs-all-bgp-small-230.png" width="200" >}}

For more detail, select a different size BGP Service card.

### View the Distribution of Sessions and Alarms

It is useful to know the number of network nodes running the BGP protocol over a period of time, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol. It is also useful to compare the number of nodes running BGP with unestablished sessions with the alarms present at the same time to determine if there is any correlation between the issues and the ability to establish a BGP session.

To view these distributions, open the medium BGP Service card.

{{< figure src="/images/netq/ntwk-svcs-all-bgp-medium-230.png" width="200" >}}

If a visual correlation is apparent, you can dig a little deeper with the large BGP Service card tabs.

### View Devices with the Most BGP Sessions

You can view the load from BGP on your switches and hosts using the large Network Services card. This data enables you to see which switches are handling the most BGP traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most BGP sessions:

1. Open the large BGP Service card.

2. Select **Switches With Most Sessions** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes running the most BGP sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-bgp-large-summary-tab-230.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large BGP Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the original time. We chose *Past Week* for this example.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-bgp-large-summary-tab-past-week-230.png" width="500">}}

    You can now see whether there are significant differences between this time and the original time. If the changes are unexpected, you can investigate further by looking at another timeframe, determining if more nodes are now running BGP than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Unestablished BGP Sessions

You can identify switches and hosts that are experiencing difficulties establishing BGP sessions; both currently and in the past.

To view switches with the most unestablished BGP sessions:

1. Open the large BGP Service card.

2. Select **Switches with Most Unestablished Sessions** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes with the most unestablished BGP sessions at the top. Scroll down to view those with the fewest unestablished sessions.

    {{< figure src="/images/netq/ntwk-svcs-allbgp-large-unestab-sessions.png" width="500" >}}

Where to go next depends on what data you see, but a couple of options
include:

- Change the time period for the data to compare with a prior time.

    If the same switches are consistently indicating the most unestablished sessions, you might want to look more carefully at those switches using the Switches card workflow to determine probable causes. Refer to {{<link title="Monitor Switches">}}.

- Click **Show All Sessions** to investigate all BGP sessions with events in the full screen card.

### View Devices with the Most BGP-related Alarms

Switches or hosts experiencing a large number of BGP alarms may indicate a configuration or performance issue that needs further investigation. You can view the devices sorted by the number of BGP alarms and then use the Switches card workflow or the Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with the most BGP alarms:

1. Open the large BGP Service card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Switches with Most Alarms** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes with the most BGP alarms at the top. Scroll down to view those with the fewest alarms.

    {{< figure src="/images/netq/ntwk-svcs-all-bgp-large-alarms-tab-230.png" width="500" >}}

Where to go next depends on what data you see, but a few options
include:

- Change the time period for the data to compare with a prior time.

    If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.

- Click **Show All Sessions** to investigate all BGP sessions with events in the full screen card.

### View All BGP Events

The BGP Network Services card workflow enables you to view all of the BGP events in the designated time period.

To view all BGP events:

1. Open the full screen BGP Service card.

2. Click **All Alarms** tab in the navigation panel.  

    By default, events are listed in most recent to least recent order.

    {{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-alarms-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a couple of options
include:

- Sort the list by message to see how many devices have had the same issue.
- Open one of the other full screen tabs in this flow to focus on devices or sessions.
- Export the data for use in another analytics tool, by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> and providing a name for the data file.

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View Details for All Devices Running BGP

You can view all stored attributes of all switches and hosts running BGP in your network in the full screen card.

To view all device details, open the full screen BGP Service card and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-switches-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View Details for All BGP Sessions

You can view all stored attributes of all BGP sessions in your network in the full-screen card.

To view all session details, open the full screen BGP Service card and click the **All Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-allsess-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}} for more detail.

To return to original display of results, click the associated tab.

## Monitor a Single BGP Session

With NetQ, you can monitor a single session of the BGP service, view session state changes, and compare with alarms occurring at the same time, as well as monitor the running BGP configuration and changes to the configuration file. For an overview and how to configure BGP to run in your data center network, refer to [Border Gateway Protocol - BGP]({{<ref "/cumulus-linux-43/Layer-3/Border-Gateway-Protocol-BGP" >}}).

{{%notice note%}}
To access the single session cards, you must open the full screen BGP Service, click the All Sessions tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18"/> (Open Cards).
{{%/notice%}}

### Granularity of Data Shown Based on Time Period

On the medium and large single BGP session cards, the status of the sessions is represented in heat maps stacked vertically; one for established sessions, and one for unestablished sessions. Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all sessions during that time period were established for the entire time block, then the top block is 100% saturated (white) and the not established block is zero percent saturated (gray). As sessions that are not established increase in saturation, the sessions that are established block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks.

{{<figure src="/images/netq/ntwk-svcs-single-bgp-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### BGP Session Card Workflow Summary

The small BGP Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-bgp-small-230.png" width="200">}}

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
<td>Indicates data is for a single session of a Network Service or Protocol</td>
</tr>
<tr class="even">
<td>Title</td>
<td>BGP Session</td>
</tr>
<tr class="odd">
<td><p> </p></td>
<td>Hostnames of the two devices in a session. Arrow points from the host to the peer.</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Current status of the session, either established or not established</td>
</tr>
</tbody>
</table>

The medium BGP Session card displays:

{{<figure src="/images/netq/ntwk-svcs-single-bgp-medium-230.png" width="200">}}

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
<td>Network Services | BGP Session</td>
</tr>
<tr class="even">
<td><p> </p></td>
<td>Hostnames of the two devices in a session. Arrow points in the direction of the session.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Current status of the session, either established or not established</td>
</tr>
<tr class="even">
<td>Time period for chart</td>
<td>Time period for the chart data</td>
</tr>
<tr class="odd">
<td>Session State Changes Chart</td>
<td>Heat map of the state of the given session over the given time period. The status is sampled at a rate consistent with the time period. For example, for a 24 hour period, a status is collected every hour. Refer to {{<link url="#granularity-of-data-shown-based-on-time-period" text="Granularity of Data Shown Based on Time Period">}}.</td>
</tr>
<tr class="even">
<td>Peer Name</td>
<td>Interface name on or hostname for peer device</td>
</tr>
<tr class="odd">
<td>Peer ASN</td>
<td>Autonomous System Number for peer device</td>
</tr>
<tr class="even">
<td>Peer Router ID</td>
<td>IP address of router with access to the peer device</td>
</tr>
<tr class="odd">
<td>Peer Hostname</td>
<td>User-defined name for peer device</td>
</tr>
</tbody>
</table>

The large BGP Session card contains two tabs.

The *Session Summary* tab displays:

{{<figure src="/images/netq/ntwk-svcs-single-bgp-large-summary-tab-231.png" width="500">}}

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
<td>Session Summary (Network Services | BGP Session)</td>
</tr>
<tr class="even">
<td>Summary bar</td>
<td><p>Hostnames of the two devices in a session.</p>
<p>Current status of the session-either established <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, or not established <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></p></td>
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
<td>Number of times the session entered the not established state during the time period</td>
</tr>
<tr class="odd">
<td>ASN</td>
<td>Autonomous System Number for host device</td>
</tr>
<tr class="even">
<td>RX/TX Families</td>
<td>Receive and Transmit address types supported. Values include IPv4, IPv6, and EVPN.
</td>
</tr>
<tr class="odd">
<td>Peer Hostname</td>
<td>User-defined name for peer device</td>
</tr>
<tr class="even">
<td>Peer Interface</td>
<td>Interface on which the session is connected</td>
</tr>
<tr class="odd">
<td>Peer ASN</td>
<td>Autonomous System Number for peer device</td>
</tr>
<tr class="even">
<td>Peer Router ID</td>
<td>IP address of router with access to the peer device</td>
</tr>
</tbody>
</table>

The *Configuration File Evolution* tab displays:

{{<figure src="/images/netq/ntwk-svcs-single-bgp-large-config-tab-230.png" width="500">}}

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
<td>(Network Services | BGP Session) Configuration File Evolution</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/></td>
<td>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Click on <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to open associated device card.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
<td>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"/></td>
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

{{<figure src="/images/netq/ntwk-svcs-single-bgp-fullscr-allsess-tab-241.png" width="700">}}

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
<td>Network Services | BGP</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
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
<td>All BGP Sessions tab</td>
<td>Displays all BGP sessions running on the host device. This tab provides the following additional data about each session:
<ul>
<li><strong>ASN</strong>: Autonomous System Number, identifier for a collection of IP networks and routers. Example values include 633284,655435.</li>
<li><strong>Conn Dropped</strong>: Number of dropped connections for a given session</li>
<li><strong>Conn Estd</strong>: Number of connections established for a given session</li>
<li><strong>DB State</strong>: Session state of DB</li>
<li><strong>Evpn Pfx Rcvd</strong>: Address prefix for EVPN traffic. Examples include 115, 35.</li>
<li><strong>Ipv4, and Ipv6 Pfx Rcvd</strong>: Address prefix for IPv4 or IPv6 traffic. Examples include 31, 14, 12.</li>
<li><strong>Last Reset Time</strong>: Time at which the session was last established or reset</li>
<li><strong>Objid</strong>: Object identifier for service</li>
<li><strong>OPID</strong>: Customer identifier. This is always zero.</li>
<li><strong>Peer</strong>
<ul>
<li>ASN: Autonomous System Number for peer device</li>
<li>Hostname: User-defined name for peer device</li>
<li>Name: Interface name or hostname of peer device</li>
<li>Router Id: IP address of router with access to the peer device</li>
</ul></li>
<li><strong>Reason</strong>: Event or cause of failure</li>
<li><strong>Rx and Tx Families</strong>: Address families supported for the receive and transmit session channels. Values include ipv4, ipv6, and evpn.</li>
<li><strong>State</strong>: Current state of the session. Values include Established and NotEstd (not established).</li>
<li><strong>Timestamp</strong>: Date and time session was started, deleted, updated or marked dead (device is down)</li>
<li><strong>Upd8 Rx:</strong> Count of protocol messages received</li>
<li><strong>Upd8 Tx</strong>: Count of protocol messages transmitted</li>
<li><strong>Up Time</strong>: Number of seconds the session has be established, in EPOC notation. Example: 1550147910000</li>
<li><strong>Vrf</strong>: Name of the Virtual Route Forwarding interface. Examples: default, mgmt, DataVrf1081</li>
<li><strong>Vrfid</strong>: Integer identifier of the VRF interface when used. Examples: 14, 25, 37</li>
</ul></td>
</tr>
<tr class="even">
<td>All Events tab</td>
<td>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:
<ul>
<li><strong>Message</strong>: Text description of a BGP-related event. Example: BGP session with peer tor-1 swp7 vrf default state changed from failed to Established</li>
<li><strong>Source</strong>: Hostname of network device that generated the event</li>
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

### View Session Status Summary

A summary of the BGP session is available from the BGP Session card
workflow, showing the node and its peer and current status.

To view the summary:

1. Add the Network Services | All BGP Sessions card.

2. Switch to the full screen card.

3. Click the **All Sessions** tab.

4. Double-click the session of interest. The full screen card closes automatically.

5. Optionally, switch to the small BGP Session card.  

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-medium-session-status-highlight-230.png" width="200">}}

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-small-230.png" width="200">}}

### View BGP Session State Changes

You can view the state of a given BGP session from the medium and large BGP Session Network Service cards. For a given time period, you can determine the stability of the BGP session between two devices. If you experienced connectivity issues at a particular time, you can use these cards to help verify the state of the session. If it was not established more than it was established, you can then investigate further into possible causes.

To view the state transitions for a given BGP session, on the *medium* BGP Session card:

1. Add the Network Services | All BGP Sessions card.

2. Switch to the full screen card.

3. Open the large BGP Service card.

4. Click the **All Sessions** tab.

5. Double-click the session of interest. The full screen card closes automatically.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-medium-session-status-highlight-230.png" width="200">}}

The heat map indicates the status of the session over the designated time period. In this example, the session has been established for the entire time period.

From this card, you can also view the Peer ASN, name, hostname and router id identifying the session in more detail.

To view the state transitions for a given BGP session on the large BGP Session card, follow the same steps to open the medium BGP Session card and then switch to the large card.

{{<figure src="/images/netq/ntwk-svcs-single-bgp-large-session-status-highlight-230.png" width="500">}}

From this card, you can view the alarm and info event counts, Peer ASN, hostname, and router id, VRF, and Tx/Rx families identifying the session in more detail. The Connection Drop Count gives you a sense of the session performance.

### View Changes to the BGP Service Configuration File

Each time a change is made to the configuration file for the BGP service, NetQ logs the change and enables you to compare it with the last version. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

To view the configuration file changes:

1. Open the large BGP Session card.

2. Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> to open the **BGP Configuration File Evolution** tab.

3. Select the time of interest on the left; when a change may have impacted the performance. Scroll down if needed.

4. Choose between the **File** view and the **Diff** view (selected option is dark; File by default).

    The File view displays the content of the file for you to review.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-large-config-tab-file-selected-230.png" width="500">}}

    The Diff view displays the changes between this version (on left) and the most recent version (on right) side by side. The changes are highlighted, as seen in this example.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-large-config-tab-diff-selected-230.png" width="500">}}

### View All BGP Session Details

You can view all stored attributes of all of the BGP sessions associated with the two devices on this card.

To view all session details, open the full screen BGP Session card, and click the **All BGP Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-single-bgp-fullscr-allsess-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View All Events

You can view all of the alarm and info events for the two devices on this card.

To view all events, open the full screen BGP Session card, and click the **All Events** tab.

{{<figure src="/images/netq/ntwk-svcs-fullscr-events-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.
