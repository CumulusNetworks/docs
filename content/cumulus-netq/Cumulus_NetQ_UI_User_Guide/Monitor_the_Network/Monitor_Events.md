---
title: Monitor Events
author: Cumulus Networks
weight: 129
aliases:
 - /display/NETQ/Monitor+Events
 - /pages/viewpage.action?pageId=10456500
pageID: 10456500
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
Two event workflows, the Alarms card workflow and the Info card
workflow, provide a view into the events occurring in the network. The
Alarms card workflow tracks critical severity events, whereas the Info
card workflow tracks all warning, info, and debug severity events.

To focus on events from a single device perspective, refer to
<span style="color: #ff0000;"> [Monitor
Switches](/cumulus-netq/Cumulus_NetQ_UI_User_Guide/Monitor_Switches)
</span> .

## <span>Monitor Alarms</span>

You can easily monitor critical events occurring across your network
using the Alarms card. You can determine the number of events for the
various system, interface, and network protocols and services components
in the network. The content of the cards in the workflow is described
first, and then followed by common tasks you would perform using this
card workflow.

### <span>Alarms Card Workflow Summary</span>

The small Alarms card displays:

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
<td><p>{{% imgOld 1 %}}</p></td>
<td><p>Indicates data is for all critical severity events in the network</p></td>
</tr>
<tr class="even">
<td><p>Alarm trend</p></td>
<td><p>Trend of alarm count, represented by an arrow:</p>
<ul>
<li><p><strong>Pointing upward and green</strong>: alarm count is higher than the last two time periods, an increasing trend</p></li>
<li><p><strong>Pointing downward and bright pink</strong>: alarm count is lower than the last two time periods, a decreasing trend</p></li>
<li><p><strong>No arrow</strong>: alarm count is unchanged over the last two time periods, trend is steady</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Alarm score</p></td>
<td><p>Current count of alarms during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Alarm rating</p></td>
<td><p>Count of alarms relative to the average count of alarms during the designated time period:</p>
<ul>
<li><p><strong>Low</strong>: Count of alarms is below the average count; a nominal count</p></li>
<li><p><strong>Med</strong>: Count of alarms is in range of the average count; some room for improvement</p></li>
<li><p><strong>High</strong>: Count of alarms is above the average count; user intervention recommended</p></li>
</ul>
<p>{{% imgOld 2 %}}</p></td>
</tr>
<tr class="odd">
<td><p>Chart</p></td>
<td><p>Distribution of all alarms received during the designated time period</p></td>
</tr>
</tbody>
</table>

The medium Alarms card displays:

{{% imgOld 3 %}}

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
<td><p>{{% imgOld 4 %}}</p></td>
<td><p>Indicates data is for all critical events in the network</p></td>
</tr>
<tr class="odd">
<td><p>Count</p></td>
<td><p>Total number of alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Alarm trend</p></td>
<td><p>Trend of alarm count, represented by an arrow:</p>
<ul>
<li><p><strong>Pointing upward and green</strong>: alarm count is higher than the last two time periods, an increasing trend</p></li>
<li><p><strong>Pointing downward and bright pink</strong>: alarm count is lower than the last two time periods, a decreasing trend</p></li>
<li><p><strong>No arrow</strong>: alarm count is unchanged over the last two time periods, trend is steady</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Alarm score</p></td>
<td><p>Current count of alarms received from each category (overall, system, interface, and network services) during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Chart</p></td>
<td><p>Distribution of all alarms received from each category during the designated time period</p></td>
</tr>
</tbody>
</table>

The large Alarms card has one tab.

The *System, Trace and Interfaces* tab displays:

{{% imgOld 5 %}}

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
<p>{{% imgOld 6 %}}</p></td>
<td><p>Indicates data is for all system, trace and interface critical events in the network</p></td>
</tr>
<tr class="odd">
<td><p>Alarm Distribution</p></td>
<td><p>Chart: Distribution of all alarms received from each category (services, NetQ Agents, Cumulus Linux licenses, sensors, ports, links, MTU, LLDP and configuration changes) during the designated time period</p>
<p>Count: Total number of alarms received from each category during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Table</p></td>
<td><p>Listing of items that match the filter selection for the selected alarm categories:</p>
<ul>
<li><p>Events by Most Recent: Most recent event are listed at the top</p></li>
<li><p>Devices by Event Count: Devices with the most events are listed at the top</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Show All Events</p></td>
<td><p>Opens full screen Events | Alarms card with a listing of all events</p></td>
</tr>
</tbody>
</table>

The full screen Alarms card provides tabs for all events.

{{% imgOld 7 %}}

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
<td><p>Events | Alarms</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 8 %}}</p></td>
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
<li><p><strong>Source</strong>: Hostname of the given event</p></li>
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
<p>{{% imgOld 9 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### <span>View Alarm Status Summary</span>

A summary of the critical alarms in the network includes the number of
alarms, a trend indicator, a performance indicator, and a distribution
of those alarms.

To view the summary, open the small Alarms card.

{{% imgOld 10 %}}

In this example, there are a small number of alarms (3), the number of
alarms is increasing, and there are more alarms right now than the
average number of alarms during this time period. This would indicate a
need to investigate further. Note that with such a small number of
alarms, the rating may be a bit skewed.

### <span>View the Distribution of Alarms</span>

It is helpful to know where and when alarms are occurring in your
network. The Alarms card workflow enables you to see the distribution of
alarms based on its source—network services, interfaces, or other system
services. You can also view the trend of alarms in each source category.

To view the alarm distribution, open the medium Alarms card. Scroll down
to view all of the charts.

{{% imgOld 11 %}}

### <span>Monitor System and Interface Alarm Details</span>

The Alarms card workflow enables users to easily view and track critical
severity system and interface alarms occurring anywhere in your network.

#### <span>View All System and Interface Alarms</span>

You can view the alarms associated with the system and interfaces using
the Alarms card workflow. You can sort alarms based on their occurrence
or view devices with the most network services alarms.

To view network services alarms, open the large Alarms card.

{{% imgOld 12 %}}

From this card, you can view the distribution of alarms for each of the
categories over time. Scroll down to view any hidden charts. A list of
the associated alarms is also displayed.

By default, the list of the most recent alarms for the systems and
interfaces is displayed when viewing the large cards.

#### <span>View Devices with the Most Alarms</span>

You can filter instead for the devices that have the most alarms.

To view devices with the most alarms, open the large Alarms card, and
then select **Devices by event count** from the dropdown.

{{% imgOld 13 %}}

#### <span>Filter Alarms by System or Interface</span>

You can focus your view to include alarms for selected system or
interface categories.

To filter for selected categories:

1.  Click the checkbox to the left of one or more charts to remove those
    set of alarms from the table on the right.

2.  Select the **Devices by event count** to view the devices with the
    most alarms for the selected categories.

3.  Switch back to most recent events by selecting **Events by most
    recent**.

4.  Click the checkbox again to return a category's data to the table.

In this example, we removed the Services from the event listing.

{{% imgOld 14 %}}

#### <span>Compare Alarms with a Prior Time</span>

You can change the time period for the data to compare with a prior
time. If the same devices are consistently indicating the most alarms,
you might want to look more carefully at those devices using the
Switches card workflow.

To compare two time periods:

1.  Open a second Alarm Events card. Remember it goes to the bottom of
    the workbench.

2.  Switch to the large size view.

3.  Move the card to be next to the original Alarm Events card. Note
    that moving large cards can take a few extra seconds since they
    contain a large amount of data.

4.  Hover over the card and click <span style="color: #353744;"> </span>
    
    {{% imgOld 15 %}}
    
    .
    
    {{% imgOld 16 %}}

5.  Select a different time period.  
    
    {{% imgOld 17 %}}
    
    {{% imgOld 18 %}}

6.  Compare the two cards with the **Devices by event count** filter
    applied.  
    In this example, the total alarm count is down, but the same device
    has the most alarms in each time period, so it might be worth
    investigating this device in more detail.

### <span>View All Events</span>

You can view all events in the network either by clicking the **Show All
Events** link under the table on the large Alarm Events card, or by
opening the full screen Alarm Events card.

{{% imgOld 19 %}}

OR

{{% imgOld 20 %}}

To return to your workbench, click

{{% imgOld 21 %}}

in the top right corner of the card.

## <span>Monitor Info Events</span>

You can easily monitor warning, info, and debug severity events
occurring across your network using the Info card. You can determine the
number of events for the various system, interface, and network
protocols and services components in the network. The content of the
cards in the workflow is described first, and then followed by common
tasks you would perform using this card workflow.

### <span>Info Card Workflow Summary</span>

The Info card workflow enables users to easily view and track
informational alarms occurring anywhere in your network.

The small Info card displays:

{{% imgOld 22 %}}

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
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 23 %}}</p></td>
<td><p>Indicates data is for all warning, info, and debug severity events in the network</p></td>
</tr>
<tr class="even">
<td><p>Info count</p></td>
<td><p>Number of info events received during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Alarm count</p></td>
<td><p>Number of alarm events received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Chart</p></td>
<td><p>Distribution of all info events and alarms received during the designated time period</p></td>
</tr>
</tbody>
</table>

The medium Info card displays:

{{% imgOld 24 %}}

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
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 25 %}}</p></td>
<td><p>Indicates data is for all warning, info, and debug severity events in the network</p></td>
</tr>
<tr class="odd">
<td><p>Types of Info</p></td>
<td><p>Chart which displays the services that have triggered events during the designated time period. Hover over chart to view a count for each type.</p></td>
</tr>
<tr class="even">
<td><p>Distribution of Info</p></td>
<td><p>Info Status</p>
<ul>
<li><p><strong>Count</strong>: Number of info events received during the designated time period</p></li>
<li><p><strong>Chart</strong>: Distribution of all info events received during the designated time period</p></li>
</ul>
<p>Alarms Status</p>
<ul>
<li><p><strong>Count</strong>: Number of alarm events received during the designated time period</p></li>
<li><p><strong>Chart</strong>: Distribution of all alarm events received during the designated time period</p></li>
</ul></td>
</tr>
</tbody>
</table>

The large Alarms card displays:

{{% imgOld 26 %}}

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
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 27 %}}</p></td>
<td><p>Indicates data is for all warning, info, and debug severity events in the network</p></td>
</tr>
<tr class="odd">
<td><p>Types of Info</p></td>
<td><p>Chart which displays the services that have triggered events during the designated time period. Hover over chart to view a count for each type.</p></td>
</tr>
<tr class="even">
<td><p>Distribution of Info</p></td>
<td><p>Info Status</p>
<ul>
<li><p><strong>Count</strong>: Current number of info events received during the designated time period</p></li>
<li><p><strong>Chart</strong>: Distribution of all info events received during the designated time period</p></li>
</ul>
<p>Alarms Status</p>
<ul>
<li><p><strong>Count</strong>: Current number of alarm events received during the designated time period</p></li>
<li><p><strong>Chart</strong>: Distribution of all alarm events received during the designated time period</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Table</p></td>
<td><p>Listing of items that match the filter selection:</p>
<ul>
<li><p><strong>Events by Most Recent</strong>: Most recent event are listed at the top</p></li>
<li><p><strong>Devices by Event Count</strong>: Devices with the most events are listed at the top</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Show All Events</p></td>
<td><p>Opens full screen Events | Info card with a listing of all events</p></td>
</tr>
</tbody>
</table>

The full screen Info card provides tabs for all events.

{{% imgOld 28 %}}

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
<td><p>Events | Info</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 29 %}}</p></td>
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
<li><p><strong>Source</strong>: Hostname of the given event</p></li>
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
<p>{{% imgOld 30 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### <span>View Info Status Summary</span>

A summary of the informational events occurring in the network can be
found on the small, medium, and large Info cards. Additional details are
available as you increase the size of the card.

To view the summary with the *small* Info card, simply open the card.
This card gives you a high-level view in a condensed visual, including
the number and distribution of the info events along with the alarms
that have occurred during the same time period.

{{% imgOld 31 %}}

To view the summary with the *medium* Info card, simply open the card.
This card gives you the same count and distribution of info and alarm
events, but it also provides information about the sources of the info
events and enables you to view a small slice of time using the
distribution charts.

{{% imgOld 32 %}}

Use the chart at the top of the card to view the various sources of info
events. The four or so types with the most info events are called out
separately, with all others collected together into an *Other* category.
Hover over segment of chart to view the count for each type.

{{% imgOld 33 %}}

To view the summary with the large Info card, open the card. The left
side of the card provides the same capabilities as the medium Info card.

### <span>Compare Timing of Info and Alarm Events</span>

While you can see the relative relationship between info and alarm
events on the small Info card, the medium and large cards provide
considerably more information. Open either of these to view individual
line charts for the events. Generally, alarms have some corollary info
events. For example, when a network service becomes unavailable, a
critical alarm is often issued, and when the service becomes available
again, an info event of severity warning is generated. For this reason,
you might see some level of tracking between the info and alarm counts
and distributions. Some other possible scenarios:

  - When a critical alarm is resolved, you may see a temporary increase
    in info events as a result.

  - When you get a burst of info events, you may see a follow-on
    increase in critical alarms, as the info events may have been
    warning you of something beginning to go wrong.

  - You set logging to debug, and a large number of info events of
    severity debug are seen. You would not expect to see an increase in
    critical alarms.

### <span>View All Info Events Sorted by Time of Occurrence</span>

You can view all info events using the large Info card. Open the large
card and confirm the **Events By Most Recent** option is selected in the
filter above the table on the right. When this option is selected, all
of the info events are listed with the most recently occurring event at
the top. Scrolling down shows you the info events that have occurred at
an earlier time within the selected time period for the card.

{{% imgOld 34 %}}

### <span>View Devices with the Most Info Events</span>

You can filter instead for the devices that have the most info events by
selecting the **Devices by Event Count** option from the filter above
the table.

{{% imgOld 35 %}}

{{% imgOld 36 %}}

### <span>View All Events</span>

You can view all events in the network either by clicking the **Show All
Events** link under the table on the large Info Events card, or by
opening the full screen Info Events card.

{{% imgOld 37 %}}

OR

{{% imgOld 38 %}}

To return to your workbench, click

{{% imgOld 39 %}}

in the top right corner of the card.

## <span>Event Reference</span>

The following table lists all event messages organized by severity, by
default. Click the column header to sort the list by that
characteristic. Click

{{% imgOld 40 %}}

in any column header to toggle the sort order between A-Z and Z-A.

{{%notice info%}}

The messages can be viewed through third-party notification
applications. For details about configuring notifications using the NetQ
CLI, refer to [Integrate with Third-party Software and
Hardware](/cumulus-netq/Cumulus_NetQ_Deployment_Guide/Integrate_with_Third-party_Software_and_Hardware).

{{%/notice%}}

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Type</p></th>
<th><p>Trigger</p></th>
<th><p>Severity</p></th>
<th><p>Message Format</p></th>
<th><p>Example</p></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>agent</p></td>
<td><p>NetQ Agent state changed from Fresh to Rotten (not heard from in over 15 seconds)</p></td>
<td><p>Critical</p></td>
<td><p>Agent state changed to rotten</p></td>
<td><p>Agent state changed to rotten</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>clag</p></td>
<td><p>CLAG remote peer state changed from up to down</p></td>
<td><p>Critical</p></td>
<td><p>Peer state changed to down</p></td>
<td><p>Peer state changed from up to down</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>configdiff</p></td>
<td><p>Configuration file deleted on a device</p></td>
<td><p>Critical</p></td>
<td><p>@hostname config file @type was deleted</p></td>
<td><p>spine03 config file /etc/frr/frr.conf was deleted</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>link</p></td>
<td><p>Link operational state changed from up to down</p></td>
<td><p>Critical</p></td>
<td><p>HostName @hostname changed state from @old_state to @new_state Interface:@ifname</p></td>
<td><p>HostName leaf01 changed state from up to down Interface:swp34</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>sensor</p></td>
<td><p>A temperature, fan, or power supply unit sensor has changed from low or warning to critical</p></td>
<td><p>Critical</p></td>
<td><p>Sensor @sensor state changed from @old_s_state to @new_s_state</p></td>
<td><p>Sensor temperature state changed from low to critical</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>sensor</p></td>
<td><p>A temperature, fan, or power supply unit sensor has crossed the maximum threshold for that sensor</p></td>
<td><p>Critical</p></td>
<td><p>Sensor @sensor max value @new_s_max exceeds threshold @new_s_crit</p></td>
<td><p>Sensor fan max value 2000 exceeds the threshold 1500</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>sensor</p></td>
<td><p>A temperature, fan, or power supply unit sensor has crossed the minimum threshold for that sensor</p></td>
<td><p>Critical</p></td>
<td><p>Sensor @sensor min value @new_s_lcrit fall behind threshold @new_s_min</p></td>
<td><p>Sensor psu min value 10 fell below threshold 10.5</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>services</p></td>
<td><p>The process ID for a service changed and the service status changed from down to up</p></td>
<td><p>Critical</p></td>
<td><p>Service @name with old pid @old_pid changed to @new_pid, status changed from @old_status to @new_status</p></td>
<td><p>Service bgp with old pid 12323 changed to 27651, status changed from down to up</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>services</p></td>
<td><p>The process ID for a service changed and the service status changed from up to down</p></td>
<td><p>Critical</p></td>
<td><p>Service @name with old pid @old_pid changed to @new_pid, status changed from @old_status to @new_status</p></td>
<td><p>Service lldp with old pid 32846 changed to 17493, status changed from up to down</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>agent</p></td>
<td><p>NetQ Agent state changed from Rotten to Fresh</p></td>
<td><p>Info</p></td>
<td><p>Agent state changed to fresh</p></td>
<td><p>Agent state changed to fresh</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>bgp</p></td>
<td><p>BGP Session state changed from Failed to Established</p></td>
<td><p>Info</p></td>
<td><p>BGP session with peer @peer @peerhost @neighbor vrf @vrf session state changed from Failed to Established</p></td>
<td><p>BGP session with peer swp5 spine02 spine03 vrf default session state changed from Failed to Established</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>bgp</p></td>
<td><p>BGP Session state changed from Established to Failed</p></td>
<td><p>Info</p></td>
<td><p>BGP session with peer @peer @neighbor vrf @vrf state changed from Established to Failed</p></td>
<td><p>BGP session with peer leaf03 leaf04 vrf mgmt state changed from Established to Failed</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>cable</p></td>
<td><p>The speed setting for a given port changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname speed changed from @old_speed to @new_speed</p></td>
<td><p>swp9 speed changed from 10 to 40</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>cable</p></td>
<td><p>The transceiver status for a given port changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname transreceiver changed from @old_transareceiver to @new_transareceiver</p></td>
<td><p>swp4 transreceiver changed from disabled to enabled</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>cable</p></td>
<td><p>The vendor of a given transceiver changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname vendor name changed from @old_vendor_name to @new_vendor_name</p></td>
<td><p>swp23 vendor name changed from Broadcom to Mellanox</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>cable</p></td>
<td><p>The part number of a given transceiver changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname part number changed from @old_part_number to @new_part_number</p></td>
<td><p>swp7 part number changed from FP1ZZ5654002A to MSN2700-CS2F0</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>cable</p></td>
<td><p>The serial number of a given transceiver changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname serial number changed from @old_serial_number to @new_serial_number</p></td>
<td><p>swp4 serial number changed from 571254X1507020 to MT1552X12041</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>cable</p></td>
<td><p>The status of forward error correction (FEC) support for a given port changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname supported fec changed from @old_supported_fec to @new_supported_fec</p></td>
<td><p>swp12 supported fec changed from supported to unsupported</p>
<p>swp12 supported fec changed from unsupported to supported</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>cable</p></td>
<td><p>The advertised support for FEC for a given port changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname supported fec changed from @old_advertised_fec to @new_advertised_fec</p></td>
<td><p>swp24 supported FEC changed from advertized to not advertized</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>cable</p></td>
<td><p>The FEC status for a given port changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname fec changed from @old_fec to @new_fec</p></td>
<td><p>swp15 fec changed from disabled to enabled</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>clag</p></td>
<td><p>CLAG remote peer state changed from down to up</p></td>
<td><p>Info</p></td>
<td><p>Peer state changed to up</p></td>
<td><p>Peer state changed to up</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>clag</p></td>
<td><p>Local CLAG host state changed from down to up</p></td>
<td><p>Info</p></td>
<td><p>Clag state changed from down to up</p></td>
<td><p>Clag state changed from down to up</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>clag</p></td>
<td><p>CLAG bond in Conflicted state was updated with new bonds</p></td>
<td><p>Info</p></td>
<td><p>Clag conflicted bond changed from @old_conflicted_bonds to @new_conflicted_bonds</p></td>
<td><p>Clag conflicted bond changed from swp7 swp8 to @swp9 swp10</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>clag</p></td>
<td><p>CLAG bond changed state from protodown to up state</p></td>
<td><p>Info</p></td>
<td><p>Clag conflicted bond changed from @old_state_protodownbond to @new_state_protodownbond</p></td>
<td><p>Clag conflicted bond changed from protodown to up</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>configdiff</p></td>
<td><p>Configuration file has been modified</p></td>
<td><p>Info</p></td>
<td><p>@hostname config file @type was modified</p></td>
<td><p>spine03 config file /etc/frr/frr.conf was modified</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>configdiff</p></td>
<td><p>Configuration file has been created</p></td>
<td><p>Info</p></td>
<td><p>@hostname config file @type was created</p></td>
<td><p>leaf12 config file /etc/lldp.d/README.conf was created</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>evpn</p></td>
<td><p>A VNI was configured and moved from the down state to the up state</p></td>
<td><p>Info</p></td>
<td><p>VNI @vni state changed from down to up</p></td>
<td><p>VNI 36 state changed from down to up</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>evpn</p></td>
<td><p>The kernel state changed on a VNI</p></td>
<td><p>Info</p></td>
<td><p>VNI @vni kernel state changed from @old_in_kernel_state to @new_in_kernel_state"</p></td>
<td><p>VNI 3 kernel state changed from down to up</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>evpn</p></td>
<td><p>A VNI state changed from not advertising all VNIs to advertising all VNIs</p></td>
<td><p>Info</p></td>
<td><p>VNI @vni vni state changed from @old_adv_all_vni_state to @new_adv_all_vni_state"</p></td>
<td><p>VNI 11 vni state changed from false to true</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>link</p></td>
<td><p>Link operational state changed from down to up</p></td>
<td><p>Info</p></td>
<td><p>HostName @hostname changed state from @old_state to @new_state Interface:@ifname</p></td>
<td><p>HostName leaf04 changed state from down to up Interface:swp11</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>lldp</p></td>
<td><p>Local LLDP host has new neighbor information</p></td>
<td><p>Info</p></td>
<td><p>LLDP Session with host @hostname and @ifname modified fields @changed_fields</p></td>
<td><p>LLDP Session with host leaf02 swp6 modified fields leaf06 swp21</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>lldp</p></td>
<td><p>Local LLDP host has new peer interface name</p></td>
<td><p>Info</p></td>
<td><p>LLDP Session with host @hostname and @ifname @old_peer_ifname changed to @new_peer_ifname</p></td>
<td><p>LLDP Session with host spine01 and swp5 swp12 changed to port12</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>lldp</p></td>
<td><p>Local LLDP host has new peer hostname</p></td>
<td><p>Info</p></td>
<td><p>LLDP Session with host @hostname and @ifname @old_peer_hostname changed to @new_peer_hostname</p></td>
<td><p>LLDP Session with host leaf03 and swp2 leaf07 changed to exit01</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>ntp</p></td>
<td><p>NTP sync state changed from not in sync to in sync</p></td>
<td><p>Info</p></td>
<td><p>Sync state changed from @old_state to @new_state for @hostname</p></td>
<td><p>Sync state changed from not sync to in sync for leaf06</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>sensor</p></td>
<td><p>A temperature, fan, or power supply sensor state changed from a higher severity to a lower severity</p></td>
<td><p>Info</p></td>
<td><p>Sensor @sensor state changed from @old_state to @new_state</p></td>
<td><p>Sensor temperature state changed from critical to low</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>sensor</p></td>
<td><p>A temperature, fan, or power supply sensor state changed from a low or medium severity to a medium or low severity</p></td>
<td><p>Info</p></td>
<td><p>Sensor @sensor state changed from @old_state to @new_state</p></td>
<td><p>Sensor temperature state changed from medium to low</p></td>
<td></td>
</tr>
</tbody>
</table>
