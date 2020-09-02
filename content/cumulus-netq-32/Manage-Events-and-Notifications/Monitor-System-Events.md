---
title: Monitor System Events
author: Cumulus Networks
weight: 680
toc: 4
---
NetQ offers multiple ways to view your event status. The NetQ UI provides a graphical and tabular view and the NetQ CLI provides a tabular view of system events. System events include events associates with network protocols and services operation, hardware and software status, and system services. You can view all events across the entire network or all events on a device. For each of these, you can filter your view of system events based on event type, severity, and time frame.

Refer to the {{<link title="NetQ UI Card Reference" text="NetQ UI Card Reference">}} for details of the cards used with the following procedures.

Refer to the {{<link title="NetQ CLI Reference" text="NetQ CLI Reference">}} for details about commands used in the following procedures.

{{< tabs "TabIDxxx" >}}

{{< tab "NetQ UI" >}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

{{< /tab >}}

{{< /tabs >}}

## Monitor All System Events

You can monitor all system events across the network or on a given device with the NetQ UI and the NetQ CLI.

### View All System Events Network-wide

{{< tabs "TabID29" >}}

{{< tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. Click **Events** under the **Network** column.

    You can filter the list by any column data (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" width="18" height="18">}}) and export a page of events at a time (click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" width="18" height="18">}}).

    {{<figure src="/images/netq/main-menu-ntwk-events-320.png" width="700">}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view all system events, run:

```
netq show events [between <text-time> and <text-endtime>] [json]
```

This example shows all events between now and an hour ago.

```
netq show events
cumulus@netq-ts:~$ netq show events
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 20:04:30 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 19:55:26 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 19:34:29 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 19:25:24 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB

```

This example shows all events between now and 24 hours ago.

```
netq show events between now and 24hr
cumulus@netq-ts:~$ netq show events between now and 24hr
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 20:04:30 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 19:55:26 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 19:34:29 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 19:25:24 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 19:04:22 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 18:55:17 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 18:34:21 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 18:25:16 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 18:04:19 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 17:55:15 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 17:34:18 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
...
```

{{< /tab >}}

{{< /tabs >}}

### View All System Events on a Device

{{< tabs "TabID126" >}}

{{< tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. Click **Events** under the **Network** column.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" width="18" height="18">}}.

4. Enter a hostname or IP address in the **Hostname** field.

5. Click **Apply**.

    {{<figure src="/images/netq/main-menu-ntwk-events-filterbyhost-320.png" width="700">}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view all system events on a switch, run:

```
netq <hostname> show events [between <text-time> and <text-endtime>] [json]
```

This example shows all events that have occurred on the *leaf01* switch between now and an hour ago.

```
cumulus@switch:~$ netq leaf01 show events

Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 20:34:31 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                critical         data storage efficiency : space lef Wed Sep  2 20:04:30 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
```

This example shows that no events have occurred on the spine01 switch in the last hour.

```
cumulus@switch:~$ netq spine01 show events
No matching event records found
```

{{< /tab >}}

{{< /tabs >}}

## Monitor System Events by Type

You can view all system events of a given type on a network-wide basis or for a given device.

### View System Events by Type Networkwide

{{< tabs "TabID181" >}}

{{< tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. Click **Events** under the **Network** column.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" width="18" height="18">}}.

4. Enter the name of network protocol or service in the **Message Type** field.

5. Click **Apply**.

    {{<figure src="/images/netq/main-menu-ntwk-events-filterbymsgtype-320.png" width="700">}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view all system events for a given network protocol or service, run:

```
netq show events (type clsupport | type ntp | type mtu | type configdiff | type vlan | type trace | type vxlan | type clag | type bgp | type interfaces | type interfaces-physical | type agents | type ospf | type evpn | type macs | type services | type lldp | type license | type os | type sensors | type btrfsinfo) [between <text-time> and <text-endtime>] [json]
```

This example shows all BGP events between now and an hour ago.

```
netq show events type bgp
```

{{< /tab >}}

{{< /tabs >}}

### View System Events by Type on a Device

## Monitor System Events by Severity

### View System Events by Severity Network-wide

### View System Events by Severity on a Device

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