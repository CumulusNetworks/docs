---
title: Monitor Network Health
author: Cumulus Networks
weight: 340
toc: 4
---
As with any network, one of the challenges is keeping track of all of the moving parts. With the NetQ GUI, you can view the overall health of your network at a glance and then delve deeper for periodic checks or as conditions arise that require attention. For a general understanding of how well your network is operating, the Network Health card workflow is the best place to start as it contains the highest view and performance roll-ups.

## Network Health Card Workflow Summary

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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat.svg" height="18" width="18"/></td>
<td>Indicates data is for overall Network Health</td>
</tr>
<tr class="odd">
<td>Health trend</td>
<td>Trend of system, network service, and interface health, represented by an arrow:
<ul>
<li><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend</li>
<li><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend</li>
<li><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady</li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td>Health score</td>
<td>Percentage of devices which passed validation versus the number of devices checked during the time window for:
<ul>
<li><strong>System health</strong>: NetQ Agent health, Cumulus Linux license status, and sensors</li>
<li><strong>Network services health</strong>: BGP, CLAG, EVPN, LNV, NTP, OSPF, and VXLAN health</li>
<li><strong>Interface health</strong>: interfaces MTU, VLAN health</li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of overall health status during the designated time period</td>
</tr>
</tbody>
</table>

The large Network Health card contains three tabs.

The *System Health* tab displays:

{{< figure src="/images/netq/ntwk-hlth-large-sys-hlth-tab-241.png" width="500" >}}

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
<td><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/12-Apps/app-window-heart.svg" height="18" width="18"/></td>
<td>Indicates data is for System Health</td>
</tr>
<tr class="odd">
<td>Health trend</td>
<td>Trend of NetQ Agents, Cumulus Linux licenses, and sensor health, represented by an arrow:
<ul>
<li><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend</li>
<li><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend</li>
<li><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady</li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td>Health score</td>
<td><p>Percentage of devices which passed validation versus the number of devices checked during the time window for NetQ Agents, Cumulus Linux license status, and platform sensors.</p>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td>Charts</td>
<td>Distribution of health score for NetQ Agents, Cumulus Linux license status, and platform sensors during the designated time period</td>
</tr>
<tr class="even">
<td>Table</td>
<td>Listing of items that match the filter selection:
<ul>
<li><strong>Most Failures</strong>: Devices with the most validation failures are listed at the top</li>
<li><strong>Recent Failures</strong>: Most recent validation failures are listed at the top</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Validations</td>
<td>Opens full screen Network Health card with a listing of validations performed by network service and protocol</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-heart.svg" height="18" width="18"/></td>
<td>Indicates data is for Network Protocols and Services Health</td>
</tr>
<tr class="odd">
<td>Health trend</td>
<td>Trend of BGP, CLAG, EVPN, LNV, NTP, OSPF, and VXLAN services health, represented by an arrow:
<ul>
<li><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend</li>
<li><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend</li>
<li><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady</li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td>Health score</td>
<td><p>Percentage of devices which passed validation versus the number of devices checked during the time window for BGP, CLAG, EVPN, LNV, NTP, and VXLAN protocols and services.</p>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td>Charts</td>
<td>Distribution of passing validations for BGP, CLAG, EVPN, LNV, NTP, and VXLAN services during the designated time period</td>
</tr>
<tr class="even">
<td>Table</td>
<td>Listing of devices that match the filter selection:
<ul>
<li><strong>Most Failures</strong>: Devices with the most validation failures are listed at the top</li>
<li><strong>Recent Failures</strong>: Most recent validation failures are listed at the top</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Validations</td>
<td>Opens full screen Network Health card with a listing of validations performed by network service and protocol</td>
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
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td>{{<img src="/images/netq/ntwk-health-if-health-icon.png" height="20" width="20" >}}</td>
<td>Indicates data is for Interface Health</td>
</tr>
<tr class="odd">
<td>Health trend</td>
<td>Trend of interfaces, VLAN, and MTU health, represented by an arrow:
<ul>
<li><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend</li>
<li><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend</li>
<li><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady</li>
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
<td>Distribution of passing validations for interfaces, VLAN, and MTU protocols and ports during the designated time period</td>
</tr>
<tr class="even">
<td>Table</td>
<td>Listing of devices that match the filter selection:
<ul>
<li><strong>Most Failures</strong>: Devices with the most validation failures are listed at the top</li>
<li><strong>Recent Failures</strong>: Most recent validation failures are listed at the top</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Validations</td>
<td>Opens full screen Network Health card with a listing of validations performed by network service and protocol</td>
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
<td>Network Health</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench</td>
</tr>
<tr class="odd">
<td>Default Time</td>
<td>Range of time in which the displayed data was collected</td>
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
<li>Licenses<ul>
<li><strong>Checked License Count</strong>: Number of licenses included in the validation</li>
<li><strong>Failed License Count</strong>: Number of licenses that failed the validation</li></ul></li>
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
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## View Network Health Summary

Overall network health is based on successful validation results. The summary includes the percentage of successful results, a trend indicator, and a distribution of the validation results.

To view a summary of your network health, open the small Network Health card.

{{<figure src="/images/netq/ntwk-hlth-small-230.png" width="200">}}

In this example, the overall health is relatively good, but improving compared to recent status. Refer to the next section for viewing the key health metrics.

## View Key Metrics of Network Health

Overall network health is a calculated average of several key health metrics: System, Network Services, and Interface health.

To view these key metrics, open the medium Network Health card. Each metric is shown with percentage of successful validations, a trend indicator, and a distribution of the validation results.

{{<figure src="/images/netq/ntwk-hlth-medium-230.png" width="200">}}

In this example, the health of each of the system and network services are good, but interface health is on the lower side. While it is improving, you might choose to dig further if it does not continue to improve. Refer to the following section for additional details.

## View System Health

The system health is a calculated average of the NetQ Agent, Cumulus Linux license, and sensor health metrics. In all cases, validation is performed on the agents and licenses. If you are monitoring platform sensors, the calculation includes these as well. You can view the overall health of the system from the medium Network Health card and information about each component from the System Health tab on the large Network Health card.

To view information about each system component:

1.  Open the large Network Health card.
2.  Hover over the card and click <img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/12-Apps/app-window-heart.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/ntwk-hlth-large-sys-hlth-tab-241.png" width="500">}}

    The health of each system protocol or service is represented on the left side of the card by a distribution of the health score, a trend indicator, and a percentage of successful results. The right side of the card provides a listing of devices running the services.

### View Devices with the Most Issues

It is useful to know which devices are experiencing the most issues with their system services in general, as this can help focus troubleshooting efforts toward selected devices versus the service itself. To view devices with the most issues, select **Most Failures** from the filter above the table on the right.

{{<figure src="/images/netq/ntwk-health-large-table-options-222.png" width="300">}}

Devices with the highest number of issues are listed at the top. Scroll down to view those with fewer issues. To further investigate the critical devices, open the Event cards and filter on the indicated switches.

### View Devices with Recent Issues

It is useful to know which devices are experiencing the most issues with their system services right now, as this can help focus troubleshooting efforts toward selected devices versus the service itself. To view devices with recent issues, select **Recent Failures** from the filter
above the table on the right. Devices with the highest number of issues are listed at the top. Scroll down to view those with fewer issues. To further investigate the critical devices, open the Switch card or the Event cards and filter on the indicated switches.

### Filter Results by System Service

You can focus the data in the table on the right, by unselecting one or more services. Click the *checkbox* next to the service you want to remove from the data. In this example, we have unchecked Licenses.

{{<figure src="/images/netq/ntwk-hlth-large-filter-sys-hlth-in-tbl-241.png" width="500">}}

This removes the checkbox next to the associated chart and grays out the title of the chart, temporarily removing the data related to that service from the table. Add it back by hovering over the chart and clicking the checkbox that appears.

### View Details of a Particular System Service

From the System Health tab on the large Network Health card you can click on a chart to take you to the full-screen card pre-focused on that service data.

## View Network Services Health

The network services health is a calculated average of the individual network protocol and services health metrics. In all cases, validation is performed on NTP. If you are running BGP, CLAG, EVPN, LNV, OSPF, or VXLAN protocols the calculation includes these as well. You can view the overall health of network services from the medium Network Health card and information about individual services from the Network Service Health tab on the large Network Health card.

To view information about each network protocol or service:

1.  Open the large Network Health card.
2.  Hover over the card and click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-heart.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/ntwk-hlth-large-ntwk-hlth-tab-241.png" width="500">}}

The health of each network protocol or service is represented on the left side of the card by a distribution of the health score, a trend indicator, and a percentage of successful results. The right side of the card provides a listing of devices running the services.

{{%notice tip%}}
If you have more services running than fit naturally into the chart area, a scroll bar appears for you to access their data. Use the scroll bars on the table to view more columns and rows.
{{%/notice%}}

### View Devices with the Most Issues

It is useful to know which devices are experiencing the most issues with their system services in general, as this can help focus troubleshooting efforts toward selected devices versus the protocol or service. To view devices with the most issues, open the large Network Health card, then click the Network Services tab. Select **Most Failures** from the dropdown above the table on the right.

{{<figure src="/images/netq/ntwk-health-large-table-options-222.png" width="300">}}

Devices with the highest number of issues are listed at the top. Scroll down to view those with fewer issues. To further investigate the critical devices, open the Event cards and filter on the indicated switches.

### View Devices with Recent Issues

It is useful to know which devices are experiencing the most issues with their network services right now, as this can help focus troubleshooting efforts toward selected devices versus the protocol or service. To view devices with the most issues, open the large Network Health card. Select **Recent Failures** from the dropdown above the table on the right. Devices with the highest number of issues are listed at the top. Scroll down to view those with fewer issues. To further investigate the critical devices, open the Switch card or the Event cards and filter on the indicated switches.

### Filter Results by Network Service

You can focus the data in the table on the right, by unselecting one or more services. Click the *checkbox* next to the service you want to remove. In this example, we removed NTP and are in the process of removing OSPF.

{{<figure src="/images/netq/ntwk-hlth-large-filter-ntwk-hlth-in-tbl-241.png" width="500">}}

This grays out the chart title and removes the associated checkbox, temporarily removing the data related to that service from the table.

### View Details of a Particular Network Service

From the Network Service Health tab on the large Network Health card you can click on a chart to take you to the full-screen card pre-focused on that service data.

## View Interfaces Health

The interface health is a calculated average of the interfaces, VLAN, and MTU health metrics. You can view the overall health of interfaces from the medium Interface Health card and information about each component from the Interface Health tab on the large Interface Health card.

To view information about each system component:

1.  Open the large Network Health card.
2.  Hover over the card and click {{<img src="/images/netq/ntwk-health-if-health-icon.png" height="20" width="20" >}}.

    {{<figure src="/images/netq/ntwk-hlth-large-if-hlth-tab-241.png" width="500">}}

    The health of each interface protocol or service is represented on the left side of the card by a distribution of the health score, a trend indicator, and a percentage of successful results. The right side of the card provides a listing of devices running the services.

### View Devices with the Most Issues

It is useful to know which devices are experiencing the most issues with their interfaces in general, as this can help focus troubleshooting efforts toward selected devices versus the service itself. To view devices with the most issues, select **Most Failures** from the filter
above the table on the right.

{{<figure src="/images/netq/ntwk-health-large-table-options-222.png" width="300">}}

Devices with the highest number of issues are listed at the top. Scroll down to view those with fewer issues. To further investigate the critical devices, open the Event cards and filter on the indicated switches.

### View Devices with Recent Issues

It is useful to know which devices are experiencing the most issues with their network services right now, as this can help focus troubleshooting efforts toward selected devices versus the service itself. To view devices with recent issues, select **Recent Failures** from the filter
above the table on the right. Devices with the highest number of issues are listed at the top. Scroll down to view those with fewer issues. To further investigate the critical devices, open the Switch card or the Event cards and filter on the indicated switches.

### Filter Results by Interface Service

You can focus the data in the table on the right, by unselecting one or more services. Click the *checkbox* next to the interface item you want to remove from the data. In this example, we have unchecked MTU.

{{<figure src="/images/netq/ntwk-hlth-large-filter-if-hlth-in-tbl-241.png" width="500">}}

This removes the checkbox next to the associated chart and grays out the title of the chart, temporarily removing the data related to that service from the table. Add it back by hovering over the chart and clicking the checkbox that appears.

### View Details of a Particular Interface Service

From the Interface Health tab on the large Network Health card you can click on a chart to take you to the full-screen card pre-focused on that service data.

## View All Network Protocol and Service Validation Results

The Network Health card workflow enables you to view all of the results
of all validations run on the network protocols and services during the
designated time period.

To view all the validation results:

1. Open the full screen Network Health card.
2. Click *\<network protocol or service name\>* tab in the navigation panel.
3. Look for patterns in the data. For example, when did nodes, sessions, links, ports, or devices start failing validation? Was it at a specific time? Was it when you starting running the service on more nodes? Did sessions fail, but nodes were fine?

    {{< figure src="/images/netq/ntwk-hlth-fullscr-bgp-tab-241.png" width="700" >}}

Where to go next depends on what data you see, but a few options include:

- Look for matching event information for the failure points in a given protocol or service.
- When you find failures in one protocol, compare with higher level protocols to see if they fail at a similar time (or vice versa with supporting services).
- Export the data for use in another analytics tool, by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18"/> and providing a name for the data file.
