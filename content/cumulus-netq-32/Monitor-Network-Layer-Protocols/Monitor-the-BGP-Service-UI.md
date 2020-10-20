---
title: Monitor the BGP Service Using NetQ UI
author: Cumulus Networks
weight: 950
toc: 4
---
The Cumulus NetQ UI enables operators to view the health of the BGP service on a networkwide and a per session basis, giving greater insight into all aspects of the service. This is accomplished through two card workflows, one for the service and one for the session.

For an overview and how to configure BGP to run in your data center network, refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-3/Border-Gateway-Protocol-BGP/" text="Border Gateway Protocol - BGP">}}.

## Monitor the BGP Service (All Sessions)

With NetQ UI, you can monitor the number of nodes running the BGP service, view switches with the most established and unestablished BGP sessions, and view alarms triggered by the BGP service. With the NetQ CLII, you can view the associated neighbors, ASN (autonomous system number), peer ASN, receive IP or EVPN address prefixes, and VRF assignment for each device.

### View Service Status Summary

The Network Services card workflow is used to show a summary of the BGP service, including the number of nodes running the service, the number of BGP-related alarms, and a distribution of those alarms.

To view the summary, open the small BGP Service card.

{{< figure src="/images/netq/ntwk-svcs-all-bgp-small-300.png" width="200" >}}

For more detail, select a different size BGP Service card.

### View the Distribution of Sessions and Alarms

It is useful to know the number of network nodes running the BGP protocol over a period of time, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol. It is also useful to compare the number of nodes running BGP with unestablished sessions with the alarms present at the same time to determine if there is any correlation between the issues and the ability to establish a BGP session.

To view these distributions, open the medium BGP Service card.

{{< figure src="/images/netq/ntwk-svcs-all-bgp-medium-300.png" width="200" >}}

If a visual correlation is apparent, you can dig a little deeper with the large BGP Service card tabs.

### View Devices with the Most BGP Sessions

You can view the load from BGP on your switches and hosts using the large Network Services card. This data enables you to see which switches are handling the most BGP traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most BGP sessions:

1. Open the large BGP Service card.

2. Select **Switches With Most Sessions** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes running the most BGP sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-bgp-large-summary-tab-300.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large BGP Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the original time. We chose *Past Week* for this example.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-bgp-large-summary-tab-past-week-300.png" width="500">}}

    You can now see whether there are significant differences between this time and the original time. If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running BGP than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Unestablished BGP Sessions

You can identify switches and hosts that are experiencing difficulties establishing BGP sessions; both currently and in the past.

To view switches with the most unestablished BGP sessions:

1. Open the large BGP Service card.

2. Select **Switches with Most Unestablished Sessions** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes with the most unestablished BGP sessions at the top. Scroll down to view those with the fewest unestablished sessions.

    {{< figure src="/images/netq/ntwk-svcs-allbgp-large-unestab-sessions-300.png" width="500" >}}

Where to go next depends on what data you see, but a couple of options
include:

- Change the time period for the data to compare with a prior time.

    If the same switches are consistently indicating the most unestablished sessions, you might want to look more carefully at those switches using the Switches card workflow to determine probable causes. Refer to {{<link title="Monitor Switch Performance">}}.

- Click **Show All Sessions** to investigate all BGP sessions with events in the full screen card.

### View Devices with the Most BGP-related Alarms

Switches or hosts experiencing a large number of BGP alarms may indicate a configuration or performance issue that needs further investigation. You can view the devices sorted by the number of BGP alarms and then use the Switches card workflow or the Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with the most BGP alarms:

1. Open the large BGP Service card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Switches with Most Alarms** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes with the most BGP alarms at the top. Scroll down to view those with the fewest alarms.

    {{< figure src="/images/netq/ntwk-svcs-all-bgp-large-alarms-tab-300.png" width="500" >}}

Where to go next depends on what data you see, but a few options
include:

- Change the time period for the data to compare with a prior time.

    If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.

- Click **Show All Sessions** to investigate all BGP sessions with events in the full screen card.

### View All BGP Events

The BGP Network Services card workflow enables you to view all of the BGP events in the designated time period.

To view all BGP events:

1. Open the full screen BGP Service card.

2. Click **All Alarms** tab in the navigation panel.  

    By default, events are listed in most recent to least recent order.

    {{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-alarms-tab-300.png" width="700">}}

Where to go next depends on what data you see, but a couple of options
include:

- Sort the list by message to see how many devices have had the same issue.
- Open one of the other full screen tabs in this flow to focus on devices or sessions.
- Export the data for use in another analytics tool, by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> and providing a name for the data file.

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View Details for All Devices Running BGP

You can view all stored attributes of all switches and hosts running BGP in your network in the full screen card.

To view all device details, open the full screen BGP Service card and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-allsw-tab-300.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View Details for All BGP Sessions

You can view all stored attributes of all BGP sessions in your network in the full-screen card.

To view all session details, open the full screen BGP Service card and click the **All Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-allsess-tab-300.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}} for more detail.

To return to original display of results, click the associated tab.

## Monitor a Single BGP Session

With NetQ, you can monitor a single session of the BGP service, view session state changes, and compare with alarms occurring at the same time, as well as monitor the running BGP configuration and changes to the configuration file. For an overview and how to configure BGP to run in your data center network, refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-3/Border-Gateway-Protocol-BGP/" text="Border Gateway Protocol - BGP">}}.

{{%notice note%}}
To access the single session cards, you must open the full screen BGP Service, click the All Sessions tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18"/> (Open Cards).
{{%/notice%}}

### Granularity of Data Shown Based on Time Period

On the medium and large single BGP session cards, the status of the sessions is represented in heat maps stacked vertically; one for established sessions, and one for unestablished sessions. Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all sessions during that time period were established for the entire time block, then the top block is 100% saturated (white) and the not established block is zero percent saturated (gray). As sessions that are not established increase in saturation, the sessions that are established block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks.

{{<figure src="/images/netq/ntwk-svcs-single-bgp-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |



### View Session Status Summary

A summary of the BGP session is available from the BGP Session card
workflow, showing the node and its peer and current status.

To view the summary:

1. Add the Network Services | All BGP Sessions card.

2. Switch to the full screen card.

3. Click the **All Sessions** tab.

4. Double-click the session of interest. The full screen card closes automatically.

5. Optionally, switch to the small BGP Session card.  

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-medium-session-status-highlight-230.png" width="200">}}

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-small-230.png" width="200">}}

### View BGP Session State Changes

You can view the state of a given BGP session from the medium and large BGP Session Network Service cards. For a given time period, you can determine the stability of the BGP session between two devices. If you experienced connectivity issues at a particular time, you can use these cards to help verify the state of the session. If it was not established more than it was established, you can then investigate further into possible causes.

To view the state transitions for a given BGP session, on the *medium* BGP Session card:

1. Add the Network Services | All BGP Sessions card.

2. Switch to the full screen card.

3. Open the large BGP Service card.

4. Click the **All Sessions** tab.

5. Double-click the session of interest. The full screen card closes automatically.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-medium-session-status-highlight-230.png" width="200">}}

The heat map indicates the status of the session over the designated time period. In this example, the session has been established for the entire time period.

From this card, you can also view the Peer ASN, name, hostname and router id identifying the session in more detail.

To view the state transitions for a given BGP session on the large BGP Session card, follow the same steps to open the medium BGP Session card and then switch to the large card.

{{<figure src="/images/netq/ntwk-svcs-single-bgp-large-session-status-highlight-230.png" width="500">}}

From this card, you can view the alarm and info event counts, Peer ASN, hostname, and router id, VRF, and Tx/Rx families identifying the session in more detail. The Connection Drop Count gives you a sense of the session performance.

### View Changes to the BGP Service Configuration File

Each time a change is made to the configuration file for the BGP service, NetQ logs the change and enables you to compare it with the last version. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

To view the configuration file changes:

1. Open the large BGP Session card.

2. Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> to open the **BGP Configuration File Evolution** tab.

3. Select the time of interest on the left; when a change may have impacted the performance. Scroll down if needed.

4. Choose between the **File** view and the **Diff** view (selected option is dark; File by default).

    The File view displays the content of the file for you to review.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-large-config-tab-file-selected-230.png" width="500">}}

    The Diff view displays the changes between this version (on left) and the most recent version (on right) side by side. The changes are highlighted, as seen in this example.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-large-config-tab-diff-selected-230.png" width="500">}}

### View All BGP Session Details

You can view all stored attributes of all of the BGP sessions associated with the two devices on this card.

To view all session details, open the full screen BGP Session card, and click the **All BGP Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-single-bgp-fullscr-allsess-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View All Events

You can view all of the alarm and info events for the two devices on this card.

To view all events, open the full screen BGP Session card, and click the **All Events** tab.

{{<figure src="/images/netq/ntwk-svcs-fullscr-events-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.
