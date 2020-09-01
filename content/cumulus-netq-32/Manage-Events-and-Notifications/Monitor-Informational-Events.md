---
title: Monitor Informational Events
author: Cumulus Networks
weight: 680
toc: 4
---
You can easily monitor warning, info, and debug severity events occurring across your network using the Info card. You can determine the number of events for the various system, interface, and network protocols and services components in the network. The content of the cards in the workflow is described first, and then followed by common tasks you would perform using this card workflow.

Refer to the {{<link title="NetQ UI Card Reference" text="NetQ UI Card Reference">}} for details of the cards used with the following procedures.

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

{{<notice tip>}}
You can open the switch card for any of the listed devices by clicking on the device name.
{{</notice>}}

## View All Events

You can view all events in the network either by clicking the **Show All Events** link under the table on the large Info Events card, or by opening the full screen Info Events card.

{{< figure src="/images/netq/events-alarms-large-show-all-events-link-222.png" width="200" >}}

OR

{{<figure src="/images/netq/events-info-fullscr-300.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.
