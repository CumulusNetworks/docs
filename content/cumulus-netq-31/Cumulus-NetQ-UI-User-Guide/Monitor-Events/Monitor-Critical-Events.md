---
title: Monitor Critical Events
author: Cumulus Networks
weight: 324
toc: 4
---
You can easily monitor critical events occurring across your network using the Alarms card. You can determine the number of events for the various system, interface, and network protocols and services components in the network. The content of the cards in the workflow is described first, and then followed by common tasks you would perform using this card workflow.

## Alarms Card Workflow Summary

The small Alarms card displays:

{{< figure src="/images/netq/events-alarms-small-231.png" width="200" >}}

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
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/></td>
<td>Indicates data is for all critical severity events in the network</td>
</tr>
<tr class="even">
<td>Alarm trend</td>
<td>Trend of alarm count, represented by an arrow:
<ul>
<li><strong>Pointing upward and <strong>bright pink</strong></strong>: alarm count is higher than the last two time periods, an increasing trend</li>
<li><strong>Pointing downward and <strong>green</strong></strong>: alarm count is lower than the last two time periods, a decreasing trend</li>
<li><strong>No arrow</strong>: alarm count is unchanged over the last two time periods, trend is steady</li>
</ul></td>
</tr>
<tr class="odd">
<td>Alarm score</td>
<td>Current count of alarms during the designated time period</td>
</tr>
<tr class="even">
<td>Alarm rating</td>
<td>Count of alarms relative to the average count of alarms during the designated time period:
<ul>
<li><strong>Low</strong>: Count of alarms is below the average count; a nominal count</li>
<li><strong>Med</strong>: Count of alarms is in range of the average count; some room for improvement</li>
<li><strong>High</strong>: Count of alarms is above the average count; user intervention recommended</li>
</ul>
<p>{{< figure src="/images/netq/alarms-perf-rating.png" width="350" >}}</p></td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution alarms received during the designated time period and a total count of all alarms present in the system</td>
</tr>
</tbody>
</table>

The medium Alarms card displays:

{{< figure src="/images/netq/events-alarms-medium-222.png" width="200" >}}

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
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/></td>
<td>Indicates data is for all critical events in the network</td>
</tr>
<tr class="odd">
<td>Count</td>
<td>Total number of alarms received during the designated time period</td>
</tr>
<tr class="even">
<td>Alarm score</td>
<td>Current count of alarms received from each category (overall, system, interface, and network services) during the designated time period</td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Distribution of all alarms received from each category during the designated time period</td>
</tr>
</tbody>
</table>

The large Alarms card has one tab.

The *Alarm Summary* tab displays:

{{< figure src="/images/netq/events-alarms-large-summ-tab-231.png" width="500" >}}

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
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-clock.svg", height="18", width="18"/></td>
<td>Indicates data is for all system, trace and interface critical events in the network</td>
</tr>
<tr class="odd">
<td>Alarm Distribution</td>
<td><p><strong>Chart</strong>: Distribution of all alarms received from each category during the designated time period:
<ul><li>NetQ Agent</li><li>BTRFS Information</li><li>CL Support</li><li>Config Diff</li><li>CL License</li><li>Installed Packages</li><li>Link</li><li>LLDP</li><li>MTU</li><li>Node</li><li>Port</li><li>Resource</li><li>Running Config Diff</li><li>Sensor</li><li>Services</li><li>SSD Utilization</li><li>TCA Interface Stats</li><li>TCA Resource Utilization</li><li>TCA Sensors</li></ul>  
The category with the largest number of alarms is shown at the top, followed by the next most, down to the chart with the fewest alarms.</p>
<p><strong>Count</strong>: Total number of alarms received from each category during the designated time period</p></td>
</tr>
<tr class="even">
<td>Table</td>
<td>Listing of items that match the filter selection for the selected alarm categories:
<ul>
<li><strong>Events by Most Recent</strong>: Most recent event are listed at the top</li>
<li><strong>Devices by Event Count</strong>: Devices with the most events are listed at the top</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Events</td>
<td>Opens full screen Events | Alarms card with a listing of all events</td>
</tr>
</tbody>
</table>

The full screen Alarms card provides tabs for all events.

{{< figure src="/images/netq/events-alarms-fullscr-allevents-tab-300.png" width="700" >}}

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
<td>Events | Alarms</td>
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
<td>All Events</td>
<td>Displays all events (both alarms and info) received in the time period. By default, the requests list is sorted by the date and time that the event occurred (<strong>Time</strong>). This tab provides the following additional data about each request:
<ul>
<li><strong>Source</strong>: Hostname of the given event</li>
<li><strong>Message</strong>: Text describing the alarm or info event that occurred</li>
<li><strong>Type</strong>: Name of network protocol and/or service that triggered the given event</li>
<li><strong>Severity</strong>: Importance of the event-critical, warning, info, or debug</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

## View Alarm Status Summary

A summary of the critical alarms in the network includes the number of alarms, a trend indicator, a performance indicator, and a distribution of those alarms.

To view the summary, open the small Alarms card.

{{< figure src="/images/netq/events-alarms-small-231.png" width="200" >}}

In this example, there are a small number of alarms (2), the number of alarms is decreasing (down arrow), and there are fewer alarms right now than the average number of alarms during this time period. This would indicate no further investigation is needed. Note that with such a small number of alarms, the rating may be a bit skewed.

## View the Distribution of Alarms

It is helpful to know where and when alarms are occurring in your network. The Alarms card workflow enables you to see the distribution of alarms based on its source: network services, interfaces, system services, and threshold-based events.

To view the alarm distribution, open the medium Alarms card. Scroll down to view all of the charts.

{{< figure src="/images/netq/events-alarms-medium-222.png" width="200" >}}

## Monitor Alarm Details

The Alarms card workflow enables users to easily view and track critical severity alarms occurring anywhere in your network. You can sort alarms based on their occurrence or view devices with the most network services alarms.

To view critical alarms, open the large Alarms card.

{{< figure src="/images/netq/events-alarms-large-summary-tab-300.png" width="500" >}}

From this card, you can view the distribution of alarms for each of the categories over time. The charts are sorted by total alarm count, with the highest number of alarms i a category listed at the top. Scroll down to view any hidden charts. A list of the associated alarms is also displayed. By default, the list of the most recent alarms is displayed when viewing the large card.

### View Devices with the Most Alarms

You can filter instead for the devices that have the most alarms.

To view devices with the most alarms, open the large Alarms card, and then select **Devices by event count** from the dropdown.

{{< figure src="/images/netq/events-alarms-large-by-event-count-300.png" width="500" >}}

{{<notice tip>}}
You can open the switch card for any of the listed devices by clicking on the device name.
{{</notice>}}

### Filter Alarms by Category

You can focus your view to include alarms for one or more selected alarm categories.

To filter for selected categories:

1. Click the checkbox to the left of one or more charts to remove that set of alarms from the table on the right.

2. Select the **Devices by event count** to view the devices with the most alarms for the selected categories.

3. Switch back to most recent events by selecting **Events by most recent**.

4. Click the checkbox again to return a category's data to the table.

In this example, we removed the Services from the event listing.

{{< figure src="/images/netq/events-alarms-large-filtered-222.png" width="500" >}}

### Compare Alarms with a Prior Time

You can change the time period for the data to compare with a prior time. If the same devices are consistently indicating the most alarms, you might want to look more carefully at those devices using the Switches card workflow.

To compare two time periods:

1. Open a second Alarm Events card. Remember it goes to the bottom of the workbench.

2. Switch to the large size view.

3. Move the card to be next to the original Alarm Events card. Note that moving large cards can take a few extra seconds since they contain a large amount of data.

4. Hover over the card and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

    {{< figure src="/images/netq/time-picker-popup-narrow-222.png" width="175" >}}

5. Select a different time period.  

    {{<figure src="/images/netq/events-alarms-large-by-event-count-300.png" width="500">}}
    <p> </p>
    {{<figure src="/images/netq/events-alarms-large-by-event-count-1w-300.png" width="500">}}

6. Compare the two cards with the **Devices by event count** filter applied.

    In this example, the total alarm count and the devices with the most alarms in each time period have changed for the better overall. You could go back further in time  or investigate the current status of the largest offenders.

## View All Events

You can view all events in the network either by clicking the **Show All Events** link under the table on the large Alarm Events card, or by opening the full screen Alarm Events card.

{{< figure src="/images/netq/events-alarms-large-show-all-events-link-222.png" width="200" >}}

OR

{{< figure src="/images/netq/events-alarms-fullscr-allevents-tab-300.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.
