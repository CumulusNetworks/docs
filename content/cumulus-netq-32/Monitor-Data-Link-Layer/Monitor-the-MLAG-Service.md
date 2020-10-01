---
title: Monitor the MLAG Service
author: Cumulus Networks
weight: 920
toc: 4
---
The Cumulus NetQ UI enables operators to view the health of the MLAG service on a networkwide and a per session basis, giving greater insight into all aspects of the service. This is accomplished through two card workflows, one for the service and one for the session. They are described separately here.

{{%notice note%}}
**MLAG or CLAG?**
The Cumulus Linux implementation of MLAG is referred to by other vendors as MLAG, MC-LAG or VPC. The Cumulus NetQ UI uses the MLAG terminology predominantly.
{{%/notice%}}

## Monitor the MLAG Service (All Sessions)

With NetQ, you can monitor the number of nodes running the MLAG service, view sessions running, and view alarms triggered by the MLAG service. For an overview and how to configure MLAG in your data center network, refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/" text="Multi-Chassis Link Aggregation - MLAG">}}.

### View Service Status Summary

A summary of the MLAG service is available from the MLAG Service card workflow, including the number of nodes running the service, the number of MLAG-related alarms, and a distribution of those alarms.

To view the summary, open the small MLAG Service card.

{{< figure src="/images/netq/ntwk-svcs-all-mlag-small-230.png" width="200" >}}

For more detail, select a different size MLAG Service card.

### View the Distribution of Sessions and Alarms

It is useful to know the number of network nodes running the MLAG protocol over a period of time, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol. It is also useful to compare the number of nodes running MLAG with the alarms present at the same time to determine if there is any correlation between the issues and the ability to establish a MLAG session.

To view these distributions, open the medium MLAG Service card.

{{< figure src="/images/netq/ntwk-svcs-all-mlag-medium-230.png" width="200" >}}

If a visual correlation is apparent, you can dig a little deeper with the large MLAG Service card tabs.

### View Devices with the Most CLAG Sessions

You can view the load from MLAG on your switches using the large MLAG Service card. This data enables you to see which switches are handling the most MLAG traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most MLAG sessions:

1. Open the large MLAG Service card.

2. Select **Switches with Most Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes running the most MLAG sessions at the top. Scroll down to view those with the fewest sessions.

    {{< figure src="/images/netq/ntwk-svcs-all-mlag-large-most-sessions-230.png" width="500" >}}

To compare this data with the same data at a previous time:

1. Open another large MLAG Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the current time. You can now see whether there are significant differences between this time period and the previous time period.  

    {{< figure src="/images/netq/time-picker-popup-narrow-222.png" width="150" >}}

    {{< figure src="/images/netq/ntwk-svcs-all-mlag-large-most-sessions-6hr-230.png" width="500" >}}

    If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running MLAG than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Unestablished MLAG Sessions

You can identify switches that are experiencing difficulties establishing MLAG sessions; both currently and in the past.

To view switches with the most unestablished MLAG sessions:

1. Open the large MLAG Service card.

2. Select **Switches with Most Unestablished Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most unestablished MLAG sessions at the top. Scroll down to view those with the fewest unestablished sessions.

    {{< figure src="/images/netq/ntwk-svcs-all-mlag-large-most-unestab-230.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most unestablished sessions, you might want to look more carefully at those switches using the Switches card workflow to determine probable causes. Refer to {{<link title="Monitor Switch Performance">}}.

- Click **Show All Sessions** to investigate all MLAG sessions with events in the full screen card.

### View Switches with the Most MLAG-related Alarms

Switches experiencing a large number of MLAG alarms may indicate a configuration or performance issue that needs further investigation. You can view the switches sorted by the number of MLAG alarms and then use the Switches card workflow or the Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with most MLAG alarms:

1. Open the large MLAG Service card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Events by Most Active Device** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most MLAG alarms at the top. Scroll down to view those with the fewest alarms.

    {{< figure src="/images/netq/ntwk-svcs-all-mlag-large-alarms-tab-230.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.  

- Click **Show All Sessions** to investigate all MLAG sessions with alarms in the full screen card.

### View All MLAG Events

The MLAG Service card workflow enables you to view all of the MLAG events in the designated time period.

To view all MLAG events:

1. Open the full screen MLAG Service card.

2. Click **All Alarms** tab.

    {{<figure src="/images/netq/ntwk-svcs-all-mlag-fullscr-all-alarms-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open the **All Switches** or **All Sessions** tabs to look more closely at the alarms from the switch or session perspective.
- Sort on other parameters:
    - By **Message** to determine the frequency of particular events.
    - By **Severity** to determine the most critical events.
    - By **Time** to find events that may have occurred at a particular time to try to correlate them with other system events.
- Export the data to a file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View Details About All Switches Running MLAG

You can view all stored attributes of all switches running MLAG in your network in the full-screen card.

To view all switch details, open the full screen MLAG Service card, and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-mlag-fullscr-all-switches-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}} for more detail. To return to original display of results, click the associated tab.

## Monitor a Single MLAG Session

With NetQ, you can monitor the number of nodes running the MLAG service, view switches with the most peers alive and not alive, and view alarms triggered by the MLAG service. For an overview and how to configure MLAG in your data center network, refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/" text="Multi-Chassis Link Aggregation - MLAG">}}.

{{%notice note%}}
To access the single session cards, you must open the full screen MLAG Service, click the All Sessions tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Open Cards).
{{%/notice%}}

### Granularity of Data Shown Based on Time Period

On the medium and large single MLAG session cards, the status of the peers is represented in heat maps stacked vertically; one for peers that are reachable (alive), and one for peers that are unreachable (not alive). Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all peers during that time period were alive for the entire time block, then the top block is 100% saturated (white) and the not alive block is zero percent saturated (gray). As peers that are not alive increase in saturation, the peers that are alive block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks.

{{<figure src="/images/netq/ntwk-svcs-single-mlag-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### View Session Status Summary

A summary of the MLAG session is available from the MLAG Session card workflow, showing the node and its peer and current status.

To view the summary:

1. Open the full screen MLAG Service card.

2. Select a session from the listing to view.

3. Close the full screen card to view the medium MLAG Session card.  

    {{< figure src="/images/netq/ntwk-svcs-single-mlag-medium-summ-highlighted-bad-230.png" width="200" >}}

    {{< figure src="/images/netq/ntwk-svcs-single-mlag-medium-summ-highlighted-230.png" width="200" >}}

    In the left example, we see that the tor1 switch plays the secondary role in this session with the switch at 44:38:39:ff:01:01. In the right example, we see that the leaf03 switch plays the primary role in this session with leaf04.

### View MLAG Session Peering State Changes

You can view the peering state for a given MLAG session from the medium and large MLAG Session cards. For a given time period, you can determine the stability of the MLAG session between two devices. If you experienced connectivity issues at a particular time, you can use these cards to help verify the state of the peer. If the peer was not alive more than it was alive, you can then investigate further into possible causes.

To view the state transitions for a given MLAG session:

1. Open the full screen MLAG Service card.

2. Select a session from the listing to view.

3. Close the full screen card to view the medium MLAG Session card.

    {{< figure src="/images/netq/ntwk-svcs-single-mlag-medium-chart-highlighted-230.png" width="200" >}}

    In this example, the peer switch has been alive for the entire 24-hour period.

From this card, you can also view the node role, peer role and state, and MLAG system MAC address which identify the session in more detail.

To view the peering state transitions for a given MLAG session on the large MLAG Session card, open that card.

{{< figure src="/images/netq/ntwk-svcs-single-mlag-large-session-tab-chart-highlighted-230.png" width="500" >}}

From this card, you can also view the alarm and info event counts, node role, peer role, state, and interface, MLAG system MAC address, active backup IP address, single, dual, conflicted, and protocol down bonds, and the VXLAN anycast address identifying the session in more detail.

### View Changes to the MLAG Service Configuration File

Each time a change is made to the configuration file for the MLAG service, NetQ logs the change and enables you to compare it with the last version. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

To view the configuration file changes:

1. Open the large MLAG Session card.

2. Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> to open the **Configuration File Evolution** tab.

3. Select the time of interest on the left; when a change may have impacted the performance. Scroll down if needed.

4. Choose between the **File** view and the **Diff** view (selected option is dark; File by default).  

    The File view displays the content of the file for you to review.

    {{< figure src="/images/netq/ntwk-svcs-single-mlag-large-config-tab-file-230.png" width="500" >}}

    The Diff view displays the changes between this version (on left) and the most recent version (on right) side by side. The changes are     highlighted in red and green. In this example, we don't have any changes after this first creation, so the same file is shown on both sides and no highlighting is present.

    {{< figure src="/images/netq/ntwk-svcs-single-mlag-large-config-tab-diff-230.png" width="500" >}}

### All MLAG Session Details

You can view all stored attributes of all of the MLAG sessions associated with the two devices on this card.

To view all session details, open the full screen MLAG Session card, and click the **All MLAG Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-single-mlag-fullscr-allsess-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open the **All Events** tabs to look more closely at the alarm and info events fin the network.
- Sort on other parameters:
    - By **Single Bonds** to determine which interface sets are only connected to one of the switches.
    - By **Backup IP and Backup IP Active** to determine if the correct backup IP address is specified for the service.
- Export the data to a file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View All MLAG Session Events

You can view all of the alarm and info events for the two devices on this card.

To view all events, open the full screen MLAG Session card, and click the **All Events** tab.

{{<figure src="/images/netq/ntwk-svcs-single-mlag-fullscr-events-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open the **All MLAG Sessions** tabs to look more closely at the individual sessions.
- Sort on other parameters:
    - By **Message** to determine the frequency of particular events.
    - By **Severity** to determine the most critical events.
    - By **Time** to find events that may have occurred at a particular time to try to correlate them with other system events.
- Export the data to a file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.
