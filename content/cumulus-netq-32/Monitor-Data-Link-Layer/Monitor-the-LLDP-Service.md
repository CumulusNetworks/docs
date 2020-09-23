---
title: Monitor the LLDP Service
author: Cumulus Networks
weight: 890
toc: 4
---
LLDP is used by network devices for advertising their identity, capabilities, and neighbors on a LAN. You can view this information for one or more devices. You can also view the information at an earlier point in time or view changes that have occurred to the information during a specified time period. The NetQ UI also enables operators to view the overall health of the LLDP service on a network-wide and a per session basis.

## Monitor the LLDP Service (All Sessions)

### View Devices Running LLDP Service

You can view the devices running the LLDP service with either the NetQ UI or the NetQ CLI.

{{< tabs "TabID15" >}}

{{< tab "NetQ UI" >}}

1. Open the LLDP Service card.

    icon (add card) > Click **Network Services** > Click All LLDP Sessions card > Click **Open Cards**

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-medium.png" width="200">}}

2. Change to the full-screen card using the size picker.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-allswitches-tab-320.png" width="700">}}

    If you have more than one page of switches running LLDP, the total count is indicated in the pagination bar.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view the devices running LLDP, run:

```
netq [<hostname>] show lldp [<remote-physical-interface>] [around <text-time>] [json]
```

This example shows the interface and peer information that is advertised for each device.

```
cumulus@switch:~$ netq show lldp 
    
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
exit01            swp1                      edge01            swp5                      Thu Feb  7 18:31:53 2019
exit01            swp2                      edge02            swp5                      Thu Feb  7 18:31:53 2019
exit01            swp3                      spine01           swp9                      Thu Feb  7 18:31:53 2019
exit01            swp4                      spine02           swp9                      Thu Feb  7 18:31:53 2019
exit01            swp5                      spine03           swp9                      Thu Feb  7 18:31:53 2019
exit01            swp6                      firewall01        mac:00:02:00:00:00:11     Thu Feb  7 18:31:53 2019
exit01            swp7                      firewall02        swp3                      Thu Feb  7 18:31:53 2019
exit02            swp1                      edge01            swp6                      Thu Feb  7 18:31:49 2019
exit02            swp2                      edge02            swp6                      Thu Feb  7 18:31:49 2019
exit02            swp3                      spine01           swp10                     Thu Feb  7 18:31:49 2019
exit02            swp4                      spine02           swp10                     Thu Feb  7 18:31:49 2019
exit02            swp5                      spine03           swp10                     Thu Feb  7 18:31:49 2019
exit02            swp6                      firewall01        mac:00:02:00:00:00:12     Thu Feb  7 18:31:49 2019
exit02            swp7                      firewall02        swp4                      Thu Feb  7 18:31:49 2019
firewall01        swp1                      edge01            swp14                     Thu Feb  7 18:31:26 2019
firewall01        swp2                      edge02            swp14                     Thu Feb  7 18:31:26 2019
firewall01        swp3                      exit01            swp6                      Thu Feb  7 18:31:26 2019
firewall01        swp4                      exit02            swp6                      Thu Feb  7 18:31:26 2019
firewall02        swp1                      edge01            swp15                     Thu Feb  7 18:31:31 2019
firewall02        swp2                      edge02            swp15                     Thu Feb  7 18:31:31 2019
firewall02        swp3                      exit01            swp7                      Thu Feb  7 18:31:31 2019
firewall02        swp4                      exit02            swp7                      Thu Feb  7 18:31:31 2019
server11          swp1                      leaf01            swp7                      Thu Feb  7 18:31:43 2019
server11          swp2                      leaf02            swp7                      Thu Feb  7 18:31:43 2019
server11          swp3                      edge01            swp16                     Thu Feb  7 18:31:43 2019
server11          swp4                      edge02            swp16                     Thu Feb  7 18:31:43 2019
server12          swp1                      leaf01            swp8                      Thu Feb  7 18:31:47 2019
server12          swp2                      leaf02            swp8                      Thu Feb  7 18:31:47 2019
```

{{< /tab >}}

{{< /tabs >}}

### View Service Status Summary

A summary of the LLDP service is available from the Network Services card workflow, including the number of nodes running the service, the number of LLDP-related alarms, and a distribution of those alarms.

To view the summary, open the small LLDP Service card.

{{< figure src="/images/netq/ntwk-svcs-all-lldp-small-230.png" width="200" >}}

In this example, there are no LLDP alarms present on the network of 14 devices.

For more detail, select a different size LLDP Network Services card.

### View the Distribution of Nodes, Alarms, and Sessions

It is useful to know the number of network nodes running the LLDP protocol over a period of time, as it gives you insight into nodes that might be misconfigured or experiencing communication issues. Additionally, if there are a large number of alarms, it is worth investigating either the service or particular devices.

To view the distribution, open the medium LLDP Service card.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-medium.png" width="200">}}

In this example, we see that 13 nodes are running the LLDP protocol, that there are 52 sessions established, and that no LLDP-related alarms have occurred in the last 24 hours.

### View the Distribution of Missing Neighbors

You can view the number of missing neighbors in any given time period and how that number has changed over time. This is a good indicator of link communication issues.

To view the distribution, open the large LLDP Service card and view the bottom chart on the left, **Total Sessions with No Nbr**.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-no-nbr-highlight-230.png" width="500">}}

In this example, we see that 16 of the 52 sessions are missing the neighbor (peer) device.

### View Devices with the Most LLDP Sessions

You can view the load from LLDP on your switches using the large LLDP Service card. This data enables you to see which switches are handling the most LLDP traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

To view switches and hosts with the most LLDP sessions:

1. Open the large LLDP Service card.

2. Select **Switches with Most Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes running the most LLDP sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-300.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large LLDP Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4.  Select the time period that you want to compare with the current time. You can now see whether there are significant differences between     this time period and the previous time period.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-past-week-300.png" width="500" >}}

    In this case, notice that their are fewer nodes running the protocol, but the total number of sessions running has nearly doubled. If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running LLDP than previously, looking for changes in the topology, and so forth.

### View Devices with the Most Unestablished LLDP Sessions

You can identify switches that are experiencing difficulties establishing LLDP sessions; both currently and in the past.

To view switches with the most unestablished LLDP sessions:

1. Open the large LLDP Service card.

2. Select **Switches with Most Unestablished Sessions** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes with the most unestablished CLAG sessions at the top. Scroll down to     view those with the fewest unestablished sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-most-unestab-300.png" width="500">}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time.

    If the same switches are consistently indicating the most unestablished sessions, you might want to look more carefully at those switches using the Switches card workflow to determine probable causes. Refer to {{<link title="Monitor Switch Performance">}}.

- Click **Show All Sessions** to investigate all LLDP sessions with events in the full screen card.

### View Switches with the Most LLDP-related Alarms

Switches experiencing a large number of LLDP alarms may indicate a configuration or performance issue that needs further investigation. You can view the switches sorted by the number of LLDP alarms and then use the Switches card workflow or the Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with most LLDP alarms:

1. Open the large LLDP Service card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Events by Most Active Device** from the filter above the  table.

    The table content is sorted by this characteristic, listing nodes with the most BGP alarms at the top. Scroll down to view those with the fewest alarms.

    {{< figure src="/images/netq/ntwk-svcs-all-lldp-large-alarms-tab.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Hover over the Total Alarms chart to focus on the switches exhibiting alarms during that smaller time slice. The table content changes to match the hovered content. Click on the chart to persist the table changes.
- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.
- Click **Show All Sessions** to investigate all switches running LLDP sessions in the full screen card.

### View All LLDP Events

The LLDP Network Services card workflow enables you to view all of the LLDP events in the designated time period.

To view all LLDP events:

1. Open the full screen LLDP Service card.

2. Click the **All Alarms** tab.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-alarms-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open the **All Switches** or **All Sessions** tabs to look more closely at the alarms from the switch or session perspective.
- Sort on other parameters:
    - by **Message** to determine the frequency of particular events
    - by **Severity** to determine the most critical events
    - by **Time** to find events that may have occurred at a particular time to try to correlate them with other system events
- Export data to a file
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner

### View Details About All Switches Running LLDP

You can view all stored attributes of all switches running LLDP in your network in the full screen card.

To view all switch details, open the LLDP Service card, and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-allswitches-tab-241.png" width="700">}}

Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View Detailed Information About All LLDP Sessions

You can view all stored attributes of all LLDP sessions in your network
in the full screen card.

To view all session details, open the LLDP Service card, and click the
**All Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-allsess-tab-241.png" width="700">}}

Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}} for more detail. To return to original display of results, click the associated tab.

## Monitor a Single LLDP Session

With NetQ, you can monitor the number of nodes running the LLDP service, view neighbor state changes, and compare with events occurring at the same time, as well as monitor the running LLDP configuration and changes to the configuration file. For an overview and how to configure LLDP in your data center network, refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Link-Layer-Discovery-Protocol/" text="Link Layer Discovery Protocol">}}.

{{<notice note>}}

To access the single session cards, you must open the full screen LLDP Service card, click the All Sessions tab, select the desired session, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}} (Open Cards).

{{</notice>}}

### Granularity of Data Shown Based on Time Period

On the medium and large single LLDP session cards, the status of the neighboring peers is represented in heat maps stacked vertically; one for peers that are reachable (neighbor detected), and one for peers that are unreachable (neighbor not detected). Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all peers during that time period were detected for the entire time block, then the top block is 100% saturated (white) and the neighbor not detected block is zero percent saturated (gray). As peers become reachable, the neighbor detected block increases in saturation, the peers that are unreachable (neighbor not detected) block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks.

{{<figure src="/images/netq/ntwk-svcs-single-lldp-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### View Session Status Summary

A summary of the LLDP session is available from the LLDP Session card workflow, showing the node and its peer and current status.

To view the summary:

1. Open the full screen LLDP Service card.

2. Double-click on a session. The full screen card closes automatically.

3. Locate the medium LLDP Session card.

4. Optionally, open the small LLDP Session card.  

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-medium-summary-highlight-230.png" width="200">}}

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-small-230.png" width="200">}}

### View LLDP Session Neighbor State Changes

You can view the neighbor state for a given LLDP session from the medium and large LLDP Session cards. For a given time period, you can determine the stability of the LLDP session between two devices. If you experienced connectivity issues at a particular time, you can use these cards to help verify the state of the neighbor. If the neighbor was not alive more than it was alive, you can then investigate further into possible causes.

To view the neighbor availability for a given LLDP session on the medium card:

1. Open the full screen LLDP Service card.

2. Double-click on a session. The full screen card closes automatically.

3. Locate the medium LLDP Session card.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-medium-nbr-state-highlight-230.png" width="200">}}

In this example, the heat map tells us that this LLDP session has been able to detect a neighbor for the entire time period.

From this card, you can also view the host name and interface name, and the peer name and interface name.

To view the neighbor availability for a given LLDP session on the large LLDP Session card, open that card.

{{<figure src="/images/netq/ntwk-svcs-single-lldp-large-nbr-state-highlight-230.png" width="500">}}

From this card, you can also view the alarm and info event counts, host interface name, peer hostname, and peer interface identifying the session in more detail.

### View Changes to the LLDP Service Configuration File

Each time a change is made to the configuration file for the LLDP service, NetQ logs the change and enables you to compare it with the last version. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

To view the configuration file changes:

1. Open the large LLDP Session card.

2. Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> to open the **LLDP Configuration File Evolution** tab.

3. Select the time of interest on the left; when a change may have impacted the performance. Scroll down if needed.

4. Choose between the **File** view and the **Diff** view (selected option is dark; File by default). 

    The File view displays the content of the file for you to review.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-large-config-tab-file-selected-230.png" width="500">}}

    The Diff view displays the changes between this version (on left) and the most recent version (on right) side by side. The changes are     highlighted in red and green. In this example, we don't have any changes to the file, so the same file is shown on both sides, and thus no highlighted lines.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-large-config-tab-diff-selected-230.png" width="500">}}

### View All LLDP Session Details

You can view all stored attributes of all of the LLDP sessions associated with the two devices on this card.

To view all session details, open the full screen LLDP Session card, and click the **All LLDP Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-single-lldp-fullscr-allsess-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right of the card.

### View All Events

You can view all of the alarm and info events in the network.

To view all events, open the full screen LLDP Session card, and click the **All Events** tab.

{{<figure src="/images/netq/ntwk-svcs-single-lldp-fullscr-events-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open the **All LLDP Sessions** tabs to look more closely at the details of the sessions between these two devices.
- Sort on other parameters:
  - By **Message** to determine the frequency of particular events.
  - By **Severity** to determine the most critical events.
  - By **Time** to find events that may have occurred at a particular time to try to correlate them with other system events.
- Export data to a file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.
