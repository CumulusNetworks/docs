---
title: Monitor Informational Events
author: Cumulus Networks
weight: 325
toc: 4
---
You can easily monitor warning, info, and debug severity events occurring across your network using the Info card. You can determine the number of events for the various system, interface, and network
protocols and services components in the network. The content of the cards in the workflow is described first, and then followed by common tasks you would perform using this card workflow.

## Info Card Workflow Summary

The Info card workflow enables users to easily view and track informational alarms occurring anywhere in your network.

The small Info card displays:

{{<figure src="/images/netq/events-info-small-222.png" width="200">}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/13-Flags/flag-plain-1.svg" height="18" width="18"/></td>
<td>Indicates data is for all warning, info, and debug severity events in the network</td>
</tr>
<tr class="even">
<td>Info count</td>
<td>Number of info events received during the designated time period</td>
</tr>
<tr class="odd">
<td>Alarm count</td>
<td>Number of alarm events received during the designated time period</td>
</tr>
<tr class="even">
<td>Chart</td>
<td>Distribution of all info events and alarms received during the designated time period</td>
</tr>
</tbody>
</table>

The medium Info card displays:

{{<figure src="/images/netq/events-info-medium-222.png" width="200">}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/13-Flags/flag-plain-1.svg" height="18" width="18"/></td>
<td>Indicates data is for all warning, info, and debug severity events in the network</td>
</tr>
<tr class="odd">
<td>Types of Info</td>
<td>Chart which displays the services that have triggered events during the designated time period. Hover over chart to view a count for each type.</td>
</tr>
<tr class="even">
<td>Distribution of Info</td>
<td>Info Status
<ul>
<li><strong>Count</strong>: Number of info events received during the designated time period</li>
<li><strong>Chart</strong>: Distribution of all info events received during the designated time period</li>
</ul>
Alarms Status
<ul>
<li><strong>Count</strong>: Number of alarm events received during the designated time period</li>
<li><strong>Chart</strong>: Distribution of all alarm events received during the designated time period</li>
</ul></td>
</tr>
</tbody>
</table>

The large Info card displays:

{{<figure src="/images/netq/events-info-large-222.png" width="500">}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/13-Flags/flag-plain-1.svg" height="18" width="18"/></td>
<td>Indicates data is for all warning, info, and debug severity events in the network</td>
</tr>
<tr class="odd">
<td>Types of Info</td>
<td>Chart which displays the services that have triggered events during the designated time period. Hover over chart to view a count for each type.</td>
</tr>
<tr class="even">
<td>Distribution of Info</td>
<td>Info Status
<ul>
<li><strong>Count</strong>: Current number of info events received during the designated time period</li>
<li><strong>Chart</strong>: Distribution of all info events received during the designated time period</li>
</ul>
Alarms Status
<ul>
<li><strong>Count</strong>: Current number of alarm events received during the designated time period</li>
<li><strong>Chart</strong>: Distribution of all alarm events received during the designated time period</li>
</ul></td>
</tr>
<tr class="odd">
<td>Table</td>
<td>Listing of items that match the filter selection:
<ul>
<li><strong>Events by Most Recent</strong>: Most recent event are listed at the top</li>
<li><strong>Devices by Event Count</strong>: Devices with the most events are listed at the top</li>
</ul></td>
</tr>
<tr class="even">
<td>Show All Events</td>
<td>Opens full screen Events | Info card with a listing of all events</td>
</tr>
</tbody>
</table>

The full screen Info card provides tabs for all events.

{{<figure src="/images/netq/events-info-fullscr-241.png" width="700">}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td>Events | Info</td>
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

## View Info Status Summary

A summary of the informational events occurring in the network can be found on the small, medium, and large Info cards. Additional details are available as you increase the size of the card.

To view the summary with the *small* Info card, simply open the card. This card gives you a high-level view in a condensed visual, including the number and distribution of the info events along with the alarms that have occurred during the same time period.

{{<figure src="/images/netq/events-info-small-222.png" width="200">}}

To view the summary with the *medium* Info card, simply open the card. This card gives you the same count and distribution of info and alarm events, but it also provides information about the sources of the info events and enables you to view a small slice of time using the distribution charts.

{{<figure src="/images/netq/events-info-medium-222.png" width="200">}}

Use the chart at the top of the card to view the various sources of info events. The four or so types with the most info events are called out separately, with all others collected together into an *Other* category. Hover over segment of chart to view the count for each type.

{{<figure src="/images/netq/events-info-large-hover-on-type-222.png" width="500">}}

To view the summary with the large Info card, open the card. The left side of the card provides the same capabilities as the medium Info card.

## Compare Timing of Info and Alarm Events

While you can see the relative relationship between info and alarm events on the small Info card, the medium and large cards provide considerably more information. Open either of these to view individual line charts for the events. Generally, alarms have some corollary info events. For example, when a network service becomes unavailable, a
critical alarm is often issued, and when the service becomes available again, an info event of severity warning is generated. For this reason, you might see some level of tracking between the info and alarm counts and distributions. Some other possible scenarios:

- When a critical alarm is resolved, you may see a temporary increase in info events as a result.
- When you get a burst of info events, you may see a follow-on increase in critical alarms, as the info events may have been   warning you of something beginning to go wrong.
- You set logging to debug, and a large number of info events of severity debug are seen. You would not expect to see an increase in critical alarms.

## View All Info Events Sorted by Time of Occurrence

You can view all info events using the large Info card. Open the large card and confirm the **Events By Most Recent** option is selected in the filter above the table on the right. When this option is selected, all of the info events are listed with the most recently occurring event at the top. Scrolling down shows you the info events that have occurred at an earlier time within the selected time period for the card.

{{<figure src="/images/netq/events-info-large-222.png" width="500">}}

### View Devices with the Most Info Events

You can filter instead for the devices that have the most info events by selecting the **Devices by Event Count** option from the filter above the table.

{{<figure src="/images/netq/events-info-large-table-options-222.png" width="300">}}
<p> </p>
{{<figure src="/images/netq/events-info-large-by-event-count-222.png" width="500">}}

## View All Events

You can view all events in the network either by clicking the **Show All Events** link under the table on the large Info Events card, or by opening the full screen Info Events card.

{{< figure src="/images/netq/events-alarms-large-show-all-events-link-222.png" width="200" >}}

OR

{{<figure src="/images/netq/events-info-fullscr-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.
