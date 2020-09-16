---
title: Monitor the OSPF Service
author: Cumulus Networks
weight: 960
toc: 4
---
The Cumulus NetQ UI enables operators to view the health of the OSPF service on a network-wide and a per session basis, giving greater insight into all aspects of the service. This is accomplished through two card workflows, one for the service and one for the session. They are described separately here.

## Monitor the OSPF Service (All Sessions)

With NetQ, you can monitor the number of nodes running the OSPF service, view switches with the most full and unestablished OSPF sessions, and view alarms triggered by the OSPF service. For an overview and how to configure OSPF to run in your data center network, refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-3/Open-Shortest-Path-First-OSPF/" text="Open Shortest Path First - OSPF">}} or {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-3/Open-Shortest-Path-First-v3-OSPFv3/" text="Open Shortest Path First v3 - OSPFv3">}}.


### View Service Status Summary

A summary of the OSPF service is available from the Network Services card workflow, including the number of nodes running the service, the number of OSPF-related alarms, and a distribution of those alarms.

To view the summary, open the small OSPF Service card.

{{<figure src="/images/netq/ntwk-svcs-all-ospf-small-230.png" width="200">}}

For more detail, select a different size OSPF Service card.

### View the Distribution of Sessions

It is useful to know the number of network nodes running the OSPF protocol over a period of time, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol. It is also useful to view the health of the sessions.

To view these distributions, open the medium OSPF Service card.

{{<figure src="/images/netq/ntwk-svcs-all-ospf-medium-230.png" width="200">}}

You can dig a little deeper with the large OSPF Service card tabs.

### View Devices with the Most OSPF Sessions

You can view the load from OSPF on your switches and hosts using the large Network Services card. This data enables you to see which switches are handling the most OSPF traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most OSPF sessions:

1. Open the large OSPF Service card.

2. Select **Switches with Most Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes running the most OSPF sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-ospf-large-summary-tab-300.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large OSPF Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the original time. We chose *Past Week* for this example.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-ospf-large-summary-tab-past-week-300.png" width="500">}}

    You can now see whether there are significant differences between this time and the original time. If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running OSPF than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Unestablished OSPF Sessions

You can identify switches and hosts that are experiencing difficulties establishing OSPF sessions; both currently and in the past.

To view switches with the most unestablished OSPF sessions:

1. Open the large OSPF Service card.

2. Select **Switches with Most Unestablished Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most unestablished OSPF sessions at the top. Scroll down to view those with the fewest unestablished sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-ospf-large-summary-tab-most-unestab-230.png" width="500">}}

Where to go next depends on what data you see, but a couple of options include:

- Change the time period for the data to compare with a prior time.

    {{<figure src="/images/netq/ntwk-svcs-all-ospf-large-summary-tab-most-unestab-pst-wk-230.png" width="500">}}

    If the same switches are consistently indicating the most unestablished sessions, you might want to look more carefully at those switches using the Switches card workflow to determine probable causes. Refer to {{<link title="Monitor Switches">}}.

- Click **Show All Sessions** to investigate all OSPF sessions with events in the full screen card.

### View Devices with the Most OSPF-related Alarms

Switches or hosts experiencing a large number of OSPF alarms may indicate a configuration or performance issue that needs further investigation. You can view the devices sorted by the number of OSPF alarms and then use the Switches card workflow or the Alarms card workflow to gather more information about possible causes for the alarms. compare the number of nodes running OSPF with unestablished sessions with the alarms present at the same time to determine if there is any correlation between the issues and the ability to establish an OSPF session.

To view switches with the most OSPF alarms:

1. Open the large OSPF Service card.

2. Hover over the header and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18">}}.

3. Select **Switches with Most Alarms** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most OSPF alarms at the top. Scroll down to view those with the fewest alarms.

    {{<figure src="/images/netq/ntwk-svcs-all-ospf-large-alarms-tab-230.png" width="500">}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.
- Click **Show All Sessions** to investigate all OSPF sessions with events in the full screen card.

### View All OSPF Events

The OSPF Network Services card workflow enables you to view all of the OSPF events in the designated time period.

To view all OSPF events:

1. Open the full screen OSPF Service card.

2. Click **All Alarms** tab in the navigation panel. By default, events are listed in most recent to least recent order.

Where to go next depends on what data you see, but a couple of options include:

- Open one of the other full screen tabs in this flow to focus on devices or sessions.
- Export the data for use in another analytics tool, by clicking {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18">}} and providing a name for the data file.

### View Details for All Devices Running OSPF

You can view all stored attributes of all switches and hosts running OSPF in your network in the full screen card.

To view all device details, open the full screen OSPF Service card and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-ospf-fullscr-allswitches-tab-241.png" width="700">}}

To return to your workbench, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the top right corner.

### View Details for All OSPF Sessions

You can view all stored attributes of all OSPF sessions in your network in the full-screen card.

To view all session details, open the full screen OSPF Service card and click the **All Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-all-ospf-fullscr-sessions-tab-222.png" width="700">}}

To return to your workbench, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the top right corner.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}} for more detail. To return to original display of results, click the associated tab.

## Monitor a Single OSPF Session

With NetQ, you can monitor a single session of the OSPF service, view session state changes, and compare with alarms occurring at the same time, as well as monitor the running OSPF configuration and changes to the configuration file. For an overview and how to configure OSPF to run in your data center network, refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-3/Open-Shortest-Path-First-OSPF/" text="Open Shortest Path First - OSPF">}} or {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-3/Open-Shortest-Path-First-v3-OSPFv3/" text="Open Shortest Path First v3 - OSPFv3">}}.

{{<notice note>}}
To access the single session cards, you must open the full screen OSPF Service, click the <strong>All Sessions</strong> tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Open Cards).
{{</notice>}}

### Granularity of Data Shown Based on Time Period

On the medium and large single OSPF session cards, the status of the sessions is represented in heat maps stacked vertically; one for established sessions, and one for unestablished sessions. Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all sessions during that time period were established for the entire time block, then the top block is 100% saturated (white) and the not established block is zero percent saturated (gray). As sessions that are not established increase in saturation, the sessions that are established block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks.

{{<figure src="/images/netq/ntwk-svcs-single-ospf-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### OSPF Session Card Workflow Summary

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
<li><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</li>
<li><strong>Type</strong>: Network protocol or service generating the event. This always has a value of OSPF in this card workflow.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### View Session Status Summary

A summary of the OSPF session is available from the OSPF Session card workflow, showing the node and its peer and current status.

To view the summary:

1. Add the Network Services | All OSPF Sessions card.

2. Switch to the full screen card.

3. Click the **All Sessions** tab.

4. Double-click the session of interest. The full screen card closes automatically.

5. Optionally, switch to the small OSPF Session card.  

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-medium-state-highighted-230.png" width="200">}}

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-small-230.png" width="200">}}

### View OSPF Session State Changes

You can view the state of a given OSPF session from the medium and large OSPF Session Network Service cards. For a given time period, you can determine the stability of the OSPF session between two devices. If you experienced connectivity issues at a particular time, you can use these cards to help verify the state of the session. If it was not established more than it was established, you can then investigate further into possible causes.

To view the state transitions for a given OSPF session, on the *medium* OSPF Session card:

1. Add the Network Services | All OSPF Sessions card.

2. Switch to the full screen card.

3. Open the large OSPF Service card.

4. Click the **All Sessions** tab.

5. Double-click the session of interest. The full screen card closes automatically.

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-medium-state-highighted-230.png" width="200">}}

The heat map indicates the status of the session over the designated time period. In this example, the session has been established for the entire time period.

From this card, you can also view the interface name, peer address, and peer id identifying the session in more detail.

To view the state transitions for a given OSPF session on the large OSPF Session card, follow the same steps to open the medium OSPF Session card and then switch to the large card.

{{<figure src="/images/netq/ntwk-svcs-single-ospf-large-state-highighted-230.png" width="500">}}

From this card, you can view the alarm and info event counts, interface name, peer address and peer id, state, and several other parameters identifying the session in more detail.

### View Changes to the OSPF Service Configuration File

Each time a change is made to the configuration file for the OSPF service, NetQ logs the change and enables you to compare it with the last version. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

To view the configuration file changes:

1. Open the large OSPF Session card.

2. Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> to open the **Configuration File Evolution** tab.

3. Select the time of interest on the left; when a change may have impacted the performance. Scroll down if needed.

4. Choose between the **File** view and the **Diff** view (selected option is dark; File by default).

    The File view displays the content of the file for you to review.

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-large-config-tab-file-selected-230.png" width="500">}}

    The Diff view displays the changes between this version (on left) and the most recent version (on right) side by side. The changes are highlighted in red and green. In this example, we don't have a change to highlight, so it shows the same file on both sides.

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-large-config-tab-diff-selected-230.png" width="500">}}

### View All OSPF Session Details

You can view all stored attributes of all of the OSPF sessions associated with the two devices on this card.

To view all session details, open the full screen OSPF Session card, and click the **All OSPF Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-single-ospf-fullscr-sessions-tab-222.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View All Events

You can view all of the alarm and info events for the two devices on this card.

To view all events, open the full screen OSPF Session card, and click the **All Events** tab.

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.
