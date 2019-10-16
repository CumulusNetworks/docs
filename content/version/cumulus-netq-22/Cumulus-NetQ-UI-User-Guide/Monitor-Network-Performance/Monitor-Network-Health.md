---
title: Monitor Network Health
author: Cumulus Networks
weight: 139
pageID: 12321072
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
As with any network, one of the challenges is keeping track of all of
the moving parts. With the NetQ GUI, you can view the overall health of
your network at a glance and then delve deeper for periodic checks or as
conditions arise that require attention. For a general understanding of
how well your network is operating, the Network Health card workflow is
the best place to start as it contains the highest view and performance
rollups.

## Network Health Card Workflow Summary

The small Network Health card displays:

{{% imgOld 0 %}}

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
<td>
<p><img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat.svg", height="18", width="18"/></p></td>
<td><p>Indicates data is for overall Network Health</p></td>
</tr>
<tr class="even">
<td><p>Health trend</p></td>
<td><p>Trend of overall network health, represented by an arrow:</p>
<ul>
<li><p><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend</p></li>
<li><p><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend</p></li>
<li><p><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady</p></li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td><p>Health score</p></td>
<td><p>Average of health scores for system health, network services health, and interface health during the last data collection window. The health score for each category is calculated as the percentage of items which passed validations versus the number of items checked.</p>
<p>The collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td><p>Health rating</p></td>
<td><p>Performance rating based on the health score during the time window:</p>
<ul>
<li><p><strong>Low</strong>: Health score is less than 40%</p></li>
<li><p><strong>Med</strong>: Health score is between 40% and 70%</p></li>
<li><p><strong>High</strong>: Health score is greater than 70%</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Chart</p></td>
<td><p>Distribution of overall health status during the designated time period</p></td>
</tr>
</tbody>
</table>

The medium Network Health card displays the distribution, score, and
trend of the:

{{% imgOld 2 %}}

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
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat.svg", height="18", width="18"/></p></td>
<td><p>Indicates data is for overall Network Health</p></td>
</tr>
<tr class="odd">
<td><p>Health trend</p></td>
<td><p>Trend of system, network service, and interface health, represented by an arrow:</p>
<ul>
<li><p><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend</p></li>
<li><p><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend</p></li>
<li><p><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady</p></li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td><p>Health score</p></td>
<td><p>Percentage of devices which passed validation versus the number of devices checked during the time window for:</p>
<ul>
<li><p><strong>System health</strong>: NetQ Agent health, Cumulus Linux license status, and sensors</p></li>
<li><p><strong>Network services health</strong>: BGP, CLAG, EVPN, LNV, NTP, OSPF, and VXLAN health</p></li>
<li><p><strong>Interface health</strong>: interfaces MTU, VLAN health</p></li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td><p>Chart</p></td>
<td><p>Distribution of overall health status during the designated time period</p></td>
</tr>
</tbody>
</table>

The large Network Health card contains two tabs.

The *System Health* tab displays:

{{< figure src="/images/netq/ntwk-hlth-large-sys-hlth-tab-222.png" width="500" >}}

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
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/12-Apps/app-window-heart.svg", height="18", width="18"/></p></td>
<td><p>Indicates data is for System Health</p></td>
</tr>
<tr class="odd">
<td><p>Health trend</p></td>
<td><p>Trend of NetQ Agents, Cumulus Linux licenses, and sensor health, represented by an arrow:</p>
<ul>
<li><p><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend</p></li>
<li><p><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend</p></li>
<li><p><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady</p></li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td><p>Health score</p></td>
<td><p>Percentage of devices which passed validation versus the number of devices checked during the time window for NetQ Agents, Cumulus Linux license status, and platform sensors.</p>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td><p>Charts</p></td>
<td><p>Distribution of health score for NetQ Agents, Cumulus Linux license status, and platform sensors during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Table</p></td>
<td><p>Listing of items that match the filter selection:</p>
<ul>
<li><p><strong>Most Failures</strong>: Devices with the most validation failures are listed at the top</p></li>
<li><p><strong>Recent Failures</strong>: Most recent validation failures are listed at the top</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Show All Validations</p></td>
<td><p>Opens full screen Network Health card with a listing of validations performed by network service and protocol</p></td>
</tr>
</tbody>
</table>

The *Network Health* tab displays:

{{< figure src="/images/netq/ntwk-hlth-large-ntwk-hlth-tab-222.png" width="500" >}}

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
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-heart.svg", height="18", width="18"/></p></td>
<td><p>Indicates data is for Network Protocols and Services Health</p></td>
</tr>
<tr class="odd">
<td><p>Health trend</p></td>
<td><p>Trend of BGP, CLAG, EVPN, LNV, NTP, OSPF, and VXLAN services health, represented by an arrow:</p>
<ul>
<li><p><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend</p></li>
<li><p><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend</p></li>
<li><p><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady</p></li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td><p>Health score</p></td>
<td><p>Percentage of devices which passed validation versus the number of devices checked during the time window for BGP, CLAG, EVPN, LNV, NTP, and VXLAN protocols and services.</p>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td><p>Charts</p></td>
<td><p>Distribution of passing validations for BGP, CLAG, EVPN, LNV, NTP, and VXLAN services during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Table</p></td>
<td><p>Listing of devices that match the filter selection:</p>
<ul>
<li><p><strong>Most Failures</strong>: Devices with the most validation failures are listed at the top</p></li>
<li><p><strong>Recent Failures</strong>: Most recent validation failures are listed at the top</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Show All Validations</p></td>
<td><p>Opens full screen Network Health card with a listing of validations performed by network service and protocol</p></td>
</tr>
</tbody>
</table>

The full screen Network Health card displays all events in the network.

{{% imgOld 8 %}}

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
<td><p>Network Health</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/></p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Default Time</p></td>
<td><p>Range of time in which the displayed data was collected</p></td>
</tr>
<tr class="even">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="odd">
<td><p>Each network protocol or service</p></td>
<td><p>Displays results of that network protocol or service validations that occurred during the designated time period. By default, the requests list is sorted by the date and time that the validation was completed (<strong>Time</strong>). This tab provides the following additional data about each protocol and service:</p>
<ul>
<li><p><strong>Validation Label</strong>: User-defined name of a validation or Default validation</p></li>
<li><p><strong>Checked Node Count</strong>: Number of nodes running the service included in the validation</p></li>
<li><p><strong>Failed Node Count</strong>: Number of nodes that failed the validation</p></li>
<li><p><strong>Failed Session Count</strong>: Number of sessions that failed the validation. Only applies to BGP, CLAG, EVPN, and OSPF.</p></li>
<li><p><strong>Total Session Count</strong>: Number of sessions running the protocol or service included in the validation. Only applies to BGP, CLAG, EVPN, and OSPF.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg", height="18", width="18"/></p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

## View Network Health Summary

Overall network health is based on successful validation results. The
summary includes the percentage of successful results, a trend
indicator, and a distribution of the validation results.

To view a summary of your network health, open the small Network Health
card.

{{% imgOld 11 %}}

In this example, the overall health is quite low and digging further for
causes is definitely warranted. Refer to the next section for viewing
the key health metrics.

## View Key Metrics of Network Health

Overall network health is a calculated average of several key health
metrics: System, Network Services, and Interface health.

To view these key metrics, open the medium Network Health card. Each
metric is shown with the the percentage of successful validations, a
trend indicator, and a distribution of the validation results.

{{% imgOld 12 %}}

In this example, the health of each of the three key metrics are all
good. You might choose to dig further on the system health if it did not
continue to improve. Refer to the following section for additional
details.

## View System Health

The system health is a calculated average of the NetQ Agent, Cumulus
Linux license, and sensor health metrics. In all cases, validation is
performed on the agents and licenses. If you are monitoring platform
sensors, the calculation includes these as well. You can view the
overall health of the system from the medium Network Health card and
information about each component from the large Network Health card.

To view information about each system component:

1.  Open the large Network Health card.
2.  Hover over the card and click <img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/12-Apps/app-window-heart.svg", height="18", width="18"/>.

    {{< figure src="/images/netq/ntwk-hlth-large-sys-hlth-tab-222.png" width="500" >}}

    The health of each protocol or service is represented on the left side
of the card by a distribution of the health score, a trend indicator,
and a percentage of successful results. The right side of the card
provides a listing of devices running the services.

### View Devices with the Most Issues

It is useful to know which devices are experiencing the most issues with
their system services in general, as this can help focus troubleshooting
efforts toward selected devices versus the service itself. To view
devices with the most issues, select **Most Failures** from the filter
above the table on the right.

{{<figure src="/images/netq/ntwk-health-large-table-options-222.png" width="300">}}

Devices with the highest number of issues are listed at the top. Scroll
down to view those with fewer issues. To further investigate the
critical devices, open the Event cards and filter on the indicated
switches.

### View Devices with Recent Issues

It is useful to know which devices are experiencing the most issues with
their network services right now, as this can help focus troubleshooting
efforts toward selected devices versus the service itself. To view
devices with recent issues, select **Recent Failures** from the filter
above the table on the right. Devices with the highest number of issues
are listed at the top. Scroll down to view those with fewer issues. To
further investigate the critical devices, open the Switch card or the
Event cards and filter on the indicated switches.

### Filter Results by System Service

You can focus the data in the table on the right, by unselecting one or
more services. Click the checkbox next to the service you want to remove
from the data. In this example, we have unchecked Licenses.

{{< figure src="/images/netq/ntwk-hlth-large-filter-sys-hlth-in-tbl-222.png" width="500" >}}

This removes the checkbox next to the associated chart and grays out the title of the chart, temporarily removing the data related to that service from the table. Add it back by hovering over the chart and clicking the checkbox that appears.

## View Network Services Health

The network services health is a calculated average of the individual
network protocol and services health metrics. In all cases, validation
is performed on NTP. If you are running BGP, CLAG, EVPN, LNV, OSPF, or
VXLAN protocols the calculation includes these as well. You can view the
overall health of network services from the medium Network Health card
and information about individual services from the large Network Health
card.

To view information about each network protocol or service:

1.  Open the large Network Health card.
2.  Hover over the card and click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-heart.svg", height="18", width="18"/>.

    {{< figure src="/images/netq/ntwk-hlth-large-ntwk-hlth-tab-222.png" width="500" >}}

The health of each protocol or service is represented on the left side
of the card by a distribution of the health score, a trend indicator,
and a percentage of successful results. The right side of the card
provides a listing of devices running the services.

{{%notice tip%}}

If you have more services running than fit naturally into the chart
area, a scroll bar appears for you to access their data.

Use the scroll bars on the table to view more columns and rows.

{{%/notice%}}

### View Devices with the Most Issues

It is useful to know which devices are experiencing the most issues with
their network services in general, as this can help focus
troubleshooting efforts toward selected devices versus the protocol or
service. To view devices with the most issues, open the large Network
Health card. Select **Most Failures** from the dropdown above the table
on the right.

{{<figure src="/images/netq/ntwk-health-large-table-options-222.png" width="300">}}

Devices with the highest number of issues are listed at the top. Scroll
down to view those with fewer issues. To further investigate the
critical devices, open the Event cards and filter on the indicated
switches.

### View Devices with Recent Issues

It is useful to know which devices are experiencing the most issues with
their network services right now, as this can help focus troubleshooting
efforts toward selected devices versus the protocol or service. To view
devices with the most issues, open the large Network Health card. Select
**Recent Failures** from the dropdown above the table on the right.
Devices with the highest number of issues are listed at the top. Scroll
down to view those with fewer issues. To further investigate the
critical devices, open the Switch card or the Event cards and filter on
the indicated switches.

### Filter Results by Network Service

You can focus the data in the table on the right, by unselecting one or
more services. Click the checkbox next to the service you want to
remove. In this example, we removed NTP and LNV and are in the
process of removing OSPF.

{{< figure src="/images/netq/ntwk-hlth-large-filter-ntwk-hlth-in-tbl-222.png" width="500" >}}

This grays out the chart title and removes the associated checkbox, temporarily removing the data related to that service from the table.

## View All Network Protocol and Service Validation Results

The Network Health card workflow enables you to view all of the results
of all validations run on the network protocols and services during the
designated time period.

To view all the validation results:

1.  Open the full screen Network Health card.
2.  Click *\<network protocol or service name\>* tab in the navigation
    panel.
3.  Look for patterns in the data. For example, when did nodes,
    sessions, links, ports, or devices start failing validation? Was it
    at a specific time? Was it when you starting running the service on
    more nodes? Did sessions fail, but nodes were fine?

    {{% imgOld 21 %}}

Where to go next depends on what data you see, but a few options
include:

  - Look for matching event information for the failure points in a
    given protocol or service.
  - When you find failures in one protocol, compare with higher level
    protocols to see if they fail at a similar time (or vice versa with
    supporting services).
  - Export the data for use in another analytics tool, by clicking
    **Export** and providing a name for the data file.
