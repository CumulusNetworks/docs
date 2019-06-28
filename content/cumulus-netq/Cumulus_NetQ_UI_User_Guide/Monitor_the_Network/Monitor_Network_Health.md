---
title: Monitor Network Health
author: Cumulus Networks
weight: 123
aliases:
 - /display/NETQ/Monitor+Network+Health
 - /pages/viewpage.action?pageId=10456458
pageID: 10456458
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
<span style="color: #000000;"> As with any network, one of the
challenges is keeping track of all of the moving parts. With the NetQ
GUI, you can view the overall health of your network at a glance and
then delve deeper for periodic checks or as conditions arise that
require attention. For a general understanding of how well your network
is operating, the Network Health card workflow is the best place to
start as it contains the highest view and performance rollups. </span>

## <span>Network Health Card Workflow Summary</span>

The small Network Health card displays:

{{% imgOld 0 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span style="color: #222222;"> </span></p>
<p>{{% imgOld 1 %}}</p></td>
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
<col style="width: 50%" />
<col style="width: 50%" />
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
<td><p><span style="color: #222222;"> </span></p>
<p>{{% imgOld 3 %}}</p></td>
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
<li><p><strong>Network services health</strong>: BGP, CLAG, EVPN, LNV, NTP, and VXLAN health</p></li>
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

The large Network Health card contains three tabs.

The *System Health* tab displays:

{{% imgOld 4 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
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
<td><p><span style="color: #222222;"> </span></p>
<p>{{% imgOld 5 %}}</p></td>
<td><p>Indicates data is for overall Network Health</p></td>
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
<td><p>Show All Devices</p></td>
<td><p>Opens full screen Network Health card with a listing of all events</p></td>
</tr>
</tbody>
</table>

The *Network Services Health* tab displays:

{{% imgOld 6 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
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
<td><p><span style="color: #222222;"> </span></p>
<p>{{% imgOld 7 %}}</p></td>
<td><p>Indicates data is for overall Network Health</p></td>
</tr>
<tr class="odd">
<td><p>Health trend</p></td>
<td><p>Trend of BGP, CLAG, EVPN, LNV, NTP, and VXLAN services health, represented by an arrow:</p>
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
<td><p>Show All Devices</p></td>
<td><p>Opens full screen Network Health card with a listing of all events</p></td>
</tr>
</tbody>
</table>

The *Interfaces Health* tab displays:

{{% imgOld 8 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
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
<td><p><span style="color: #222222;"> </span></p>
<p>{{% imgOld 9 %}}</p></td>
<td><p>Indicates data is for overall Network Health</p></td>
</tr>
<tr class="odd">
<td><p>Health trend</p></td>
<td><p>Trend of interfaces, MTU, and VLAN health, represented by an arrow:</p>
<ul>
<li><p><strong>Pointing upward and green</strong>: Health score in the most recent window is higher than in the last two data collection windows, an increasing trend</p></li>
<li><p><strong>Pointing downward and bright pink</strong>: Health score in the most recent window is lower than in the last two data collection windows, a decreasing trend</p></li>
<li><p><strong>No arrow</strong>: Health score is unchanged over the last two data collection windows, trend is steady</p></li>
</ul>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="even">
<td><p>Health score</p></td>
<td><p>Percentage of devices which passed validation versus the number of devices checked during the time window for for interfaces, MTUs, and VLANs.</p>
<p>The data collection window varies based on the time period of the card. For a 24 hour time period (default), the window is one hour. This gives you current, hourly, updates about your network health.</p></td>
</tr>
<tr class="odd">
<td><p>Charts</p></td>
<td><p>Distribution of health score for interfaces, MTUs, and VLANs during the designated time period</p></td>
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
<td><p>Show All Devices</p></td>
<td><p>Opens full screen Network Health card with a listing of all events</p></td>
</tr>
</tbody>
</table>

The full screen Network Health card displays all events in the network.

{{% imgOld 10 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
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
<td><p>{{% imgOld 11 %}}</p></td>
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
<td><p>All Events</p></td>
<td><p>Displays all events (both alarms and info) received in the time period. By default, the requests list is sorted by the date and time that the event occurred (<strong>Time</strong>). This tab provides the following additional data about each request:</p>
<ul>
<li><p><strong>Source</strong>: Hostname(, IP address or MAC address?) of the given event</p></li>
<li><p><strong>Type</strong>: Name of network protocol and/or service that triggered the given event</p></li>
<li><p><strong>Message</strong>: Text describing the alarm or info event that occurred</p></li>
<li><p><strong>Severity</strong>: Importance of the event–critical, warning, info, or debug</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 12 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

## <span>View Network Health Summary </span>

Overall network health is based on successful validation results. The
summary includes the percentage of successful results, a trend
indicator, and a distribution of the validation results.

<span style="color: #000000;"> To view a summary of your network health,
open the small Network Health card. </span>

<span style="color: #000000;"> </span>

{{% imgOld 13 %}}

<span style="color: #000000;"> In this example, the overall health is
quite low and digging further for causes is definitely warranted. Refer
to the next section for viewing the key health metrics. </span>

## <span>View Key Metrics of Network Health</span>

<span style="color: #000000;"> Overall network health is a calculated
average of several key health metrics: System, Network Services, and
Interface health. </span>

<span style="color: #000000;"> To view these key metrics, open the
medium Network Health card. Each metric is shown with the the percentage
of successful validations, a trend indicator, and a distribution of the
validation results. </span>

<span style="color: #000000;"> </span>

{{% imgOld 14 %}}

<span style="color: #000000;"> In this example, the health of each of
the three key metrics are all good. You might choose to dig further on
the system health if it did not continue to improve. Refer to the
following section for additional details. </span>

## <span>View System Health</span>

<span style="color: #000000;"> The system health is a calculated average
of the NetQ Agent, Cumulus Linux license, and sensor health metrics. In
all cases, validation is performed on the agents and licenses.. If you
are monitoring platform sensors, the calculation includes these as well.
You can view the overall health of the system from the medium Network
Health card and information about each component from the large Network
Health card. </span>

<span style="color: #000000;"> To view information about each system
component: </span>

1.  <span style="color: #000000;"> Open the large Network Health card.
    </span>

2.  <span style="color: #000000;"> Hover over the card and click
    <span style="color: #222222;"> </span></span>
    
    {{% imgOld 15 %}}
    
    .  
    
    {{% imgOld 16 %}}

<span style="color: #000000;"> <span style="color: #000000;"> The health
of each protocol or service is represented on the left side of the card
by a distribution of the health score, a trend indicator, and a
percentage of successful results. The right side of the card provides a
listing of devices running the services. </span> </span>

### <span>View Devices with the Most Issues</span>

<span style="color: #000000;"> It is useful to know which devices are
experiencing the most issues with their system services in general, as
this can help focus troubleshooting efforts toward selected devices
versus the service itself. To view devices with the most issues, select
**Most Failures** from the filter above the table on the right. </span>

<span style="color: #000000;"> </span>

{{% imgOld 17 %}}

<span style="color: #000000;"> Devices with the highest number of issues
are listed at the top. Scroll down to view those with fewer issues. To
further investigate the critical devices, open the Event cards and
filter on the indicated switches. </span>

### <span>View Devices with Recent Issues</span>

<span style="color: #000000;"> It is useful to know which devices are
experiencing the most issues with their network services right now, as
this can help focus troubleshooting efforts toward selected devices
versus the service itself. To view devices with recent issues, select
**Recent Failures** from the filter above the table on the right.
</span> <span style="color: #000000;"> Devices with the highest number
of issues are listed at the top. Scroll down to view those with fewer
issues. To further investigate the critical devices, open the </span>
<span style="color: #000000;"> Switch card or the </span>
<span style="color: #000000;"> Event cards and filter on the indicated
switches. </span>

### <span>Filter Results by System Service</span>

<span style="color: #000000;"> You can focus the data in the table on
the right, by unselecting one or more services. Click the checkbox next
to the service you want to remove from the data. In this example, we
have unchecked Licenses. </span>

{{% imgOld 18 %}}

<span style="color: #000000;"> This grays out the associated chart and
temporarily removes the data related to that service from the table.
</span>

## <span>View Network Services Health </span>

<span style="color: #000000;"> The network services health is a
calculated average of the individual network protocol and services
health metrics. In all cases, validation is performed on NTP. If you are
running BGP, CLAG, EVPN, LNV, OSPF, or VXLAN protocols the calculation
includes these as well. You can view the overall health of network
services from the medium Network Health card and information about
individual services from the large Network Health card. </span>

<span style="color: #000000;"> To view information about each network
protocol or service: </span>

1.  <span style="color: #000000;"> Open the large Network Health card.
    </span>

2.  <span style="color: #000000;"> Hover over the card and click
    <span style="color: #222222;"> </span></span>
    
    {{% imgOld 19 %}}
    
    .  
    
    {{% imgOld 20 %}}
    
      

<span style="color: #000000;"> The health of each protocol or service is
represented on the left side of the card by a distribution of the health
score, a trend indicator, and a percentage of successful results. The
right side of the card provides a listing of devices running the
services. </span>

{{%notice tip%}}

If you have more services running than fit naturally into the chart
area, a scroll bar appears for you to access their data.

Use the scroll bars on the table to view more columns and rows.

{{%/notice%}}

### <span>View Devices with the Most Issues</span>

<span style="color: #000000;"> It is useful to know which devices are
experiencing the most issues with their network services in general, as
this can help focus troubleshooting efforts toward selected devices
versus the protocol or service. To view devices with the most issues,
open the large Network Health card. Select **Most Failures** from the
dropdown above the table on the right. </span>

<span style="color: #000000;"> </span>

{{% imgOld 21 %}}

<span style="color: #000000;"> Devices with the highest number of issues
are listed at the top. Scroll down to view those with fewer issues. To
further investigate the critical devices, open the Event cards and
filter on the indicated switches. </span>

### <span>View Devices with Recent Issues</span>

<span style="color: #000000;"> It is useful to know which devices are
experiencing the most issues with their network services right now, as
this can help focus troubleshooting efforts toward selected devices
versus the protocol or service. To view devices with the most issues,
open the large Network Health card. Select **Recent Failures** from the
dropdown above the table on the right. Devices with the highest number
of issues are listed at the top. Scroll down to view those with fewer
issues. To further investigate the critical devices, open
<span style="color: #000000;"> the </span>
<span style="color: #000000;"> Switch card or the </span>
<span style="color: #000000;"> Event cards and filter on the indicated
switches. </span> </span>

### <span>Filter Results by Network Service</span>

<span style="color: #000000;"> You can focus the data in the table on
the right, by unselecting one or more services. Click the checkbox next
to the service you want to remove. In this example, we are removed NTP
and LNV and are in the process of removing OSPF. </span>

<span style="color: #000000;"> </span>

{{% imgOld 22 %}}

<span style="color: #000000;"> This grays out the charts and temporarily
removes the data related to that service from the table. </span>

## <span>View All Events</span>

<span style="color: #000000;"> The Network Health card workflow enables
you to view all of the alarms and info events in the network during the
designated time period. </span>

To view all events:

1.  Open the full screen Network Health card.

2.  Click **All Events** tab in the navigation panel.

3.  Sort event data by **Time** column to view events in most recent to
    least recent order.

{{% imgOld 23 %}}

Where to go next depends on what data you see, but a few options
include: <span style="color: #000000;"> </span>

  - Sort or filter event data instead by severity, for example, or type.

  - Export the data for use in another analytics tool, by clicking
    **Export** and providing a name for the data file.

<span style="color: #000000;">  
</span>

<span style="color: #000000;">  
</span>
