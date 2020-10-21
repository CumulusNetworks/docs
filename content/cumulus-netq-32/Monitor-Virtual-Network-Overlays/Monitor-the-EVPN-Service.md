---
title: Monitor the EVPN Service
author: Cumulus Networks
weight: 980
toc: 4
---
The Cumulus NetQ UI enables operators to view the health of the EVPN service on a networkwide and a per session basis, giving greater insight into all aspects of the service. This is accomplished through two card workflows, one for the service and one for the session. They are described separately here.

## Monitor the EVPN Service (All Sessions)

With NetQ, you can monitor the number of nodes running the EVPN service, view switches with the sessions, total number of VNIs, and alarms triggered by the EVPN service. For an overview and how to configure EVPN in your data center network, refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/" text="Ethernet Virtual Private Network-EVPN">}}.

### View Service Status Summary

A summary of the EVPN service is available from the Network Services card workflow, including the number of nodes running the service, the number of EVPN-related alarms, and a distribution of those alarms.

To view the summary, open the small EVPN Network Service card.

{{< figure src="/images/netq/ntwk-svcs-all-evpn-small-230.png" width="200" >}}

For more detail, select a different size EVPN Network Service card.

### View the Distribution of Sessions and Alarms

It is useful to know the number of network nodes running the EVPN protocol over a period of time, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol. It is also useful to compare the number of nodes running EVPN with the alarms present at the same time to determine if there is any correlation between the issues and the ability to establish an EVPN session.

To view these distributions, open the medium EVPN Service card.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-medium-230.png" width="200">}}

If a visual correlation is apparent, you can dig a little deeper with the large EVPN Service card tabs.

### View the Distribution of Layer 3 VNIs

It is useful to know the number of layer 3 VNIs, as it gives you insight into the complexity of the VXLAN.

To view this distribution, open the large EVPN Service card and view the bottom chart on the left.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-vni-chart-300.png" width="500">}}

### View Devices with the Most EVPN Sessions

You can view the load from EVPN on your switches and hosts using the large EVPN Service card. This data enables you to see which switches are handling the most EVPN traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most EVPN sessions:

1. Open the large EVPN Service card.

2. Select **Top Switches with Most Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes running the most EVPN sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-top-sessions-300.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large EVPN Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4.  Select the time period that you want to compare with the current time.  

    You can now see whether there are significant differences between this time period and the previous time period.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-past-week-230.png" width="500" >}}

If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running EVPN than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Layer 2 EVPN Sessions

You can view the number layer 2 EVPN sessions on your switches and hosts using the large EVPN Service card. This data enables you to see which switches are handling the most EVPN traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most layer 2 EVPN sessions:

1. Open the large EVPN Service card.

2. Select **Switches with Most L2 EVPN** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes running the most layer 2 EVPN sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l2evpn-300.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large EVPN Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the current time.  

    You can now see whether there are significant differences between this time period and the previous time period.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l2-pst-mo-300.png" width="500">}}

If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running EVPN than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Layer 3 EVPN Sessions

You can view the number layer 3 EVPN sessions on your switches and hosts using the large EVPN Service card. This data enables you to see which switches are handling the most EVPN traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most layer 3 EVPN sessions:

1. Open the large EVPN Service card.

2. Select **Switches with Most L3 EVPN** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes running the most layer 3 EVPN sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l3evpn-300.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large EVPN Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the current time.  

    You can now see whether there are significant differences between this time period and the previous time period.  

    {{< figure src="/images/netq/time-picker-popup-narrow-222.png" width="150" >}}

    {{< figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l3-pst-wk-230.png" width="500" >}}

If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running EVPN than previously, looking for changes in the topology, and so forth.

### View Devices with the Most EVPN-related Alarms

Switches experiencing a large number of EVPN alarms may indicate a configuration or performance issue that needs further investigation. You can view the switches sorted by the number of BGP alarms and then use the Switches card workflow or the Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with the most EVPN alarms:

1. Open the large EVPN Service card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Events by Most Active Device** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most EVPN alarms at the top. Scroll down to view those with the fewest alarms.

    {{< figure src="/images/netq/ntwk-svcs-all-evpn-large-alarms-tab-230.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Hover over the Total Alarms chart to focus on the switches exhibiting alarms during that smaller time slice. The table content changes to match the hovered content. Click on the chart to persist the table changes.
- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.
- Click **Show All Sessions** to investigate all EVPN sessions networkwide in the full screen card.

### View All EVPN Events

The EVPN Service card workflow enables you to view all of the EVPN events in the designated time period.

To view all EVPN events:

1. Open the full screen EVPN Service card.

2. Click **All Alarms** tab in the navigation panel. By default, events are sorted by Time, with most recent events listed first.

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-alarms-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options
include:

- Open one of the other full screen tabs in this flow to focus on devices or sessions.
- Sort by the **Message** or **Severity** to narrow your focus.
- Export the data for use in another analytics tool, by selecting all or some of the events and clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right to return to your workbench.

### View Details for All Devices Running EVPN

You can view all stored attributes of all switches running EVPN in your network in the full screen card.

To view all switch and host details, open the full screen EVPN Service card, and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-allswitches-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right.

### View Details for All EVPN Sessions

You can view all stored attributes of all EVPN sessions in your network in the full screen card.

To view all session details, open the full screen EVPN Service card, and click the **All Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-sessions-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}} for more detail.

To return to original display of results, click the associated tab.

## Monitor a Single EVPN Session

With NetQ, you can monitor the performance of a single EVPN session, including the number of associated VNI, VTEPs and type. For an overview and how to configure EVPN in your data center network, refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/" text="Ethernet Virtual Private Network - EVPN">}}.

{{%notice note%}}
To access the single session cards, you must open the full screen EVPN Service, click the All Sessions tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18"/> (Open Cards).
{{%/notice%}}

### View Session Status Summary

A summary of the EVPN session is available from the EVPN Session card workflow, showing the node and its peer and current status.

To view the summary:

1. Add the Network Services | All EVPN Sessions card.

2. Switch to the full screen card.

3. Click the **All Sessions** tab.

4. Double-click the session of interest. The full screen card closes automatically.

5. Optionally, switch to the small EVPN Session card.  

    {{<figure src="/images/netq/ntwk-svcs-single-evpn-medium-230.png" width="200">}}

    {{<figure src="/images/netq/ntwk-svcs-single-evpn-small-230.png" width="200">}}

For more detail, select a different size EVPN Session card.

### View VTEP Count

You can view the count of VTEPs for a given EVPN session from the medium
and large EVPN Session cards.

To view the count for a given EVPN session, on the *medium* EVPN Session
card:

1. Add the Network Services | All EVPN Sessions card.

2. Switch to the full screen card.

3. Click the **All Sessions** tab.

4. Double-click the session of interest. The full screen card closes automatically.

    {{<figure src="/images/netq/ntwk-svcs-single-evpn-medium-vtep-count-230.png" width="200">}}

To view the count for a given EVPN session on the *large* EVPN Session card, follow the same steps as for the medium card and then switch to the large card.

{{<figure src="/images/netq/ntwk-svcs-single-evpn-large-summary-tab-vtep-cnt-230.png" width="500">}}

### View All EVPN Session Details

You can view all stored attributes of all of the EVPN sessions running networkwide.

To view all session details, open the full screen EVPN Session card and click the **All EVPN Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-single-evpn-fullscr-allsess-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right of the card.

### View All Events

You can view all of the alarm and info events occurring network wide.

To view all events, open the full screen EVPN Session card and click the **All Events** tab.

{{<figure src="/images/netq/ntwk-svcs-single-evpn-fullscr-events-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open one of the other full screen tabs in this flow to focus on sessions.
- Sort by the **Message** or **Severity** to narrow your focus.
- Export the data for use in another analytics tool, by selecting all or some of the events and clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right to return to your workbench.
