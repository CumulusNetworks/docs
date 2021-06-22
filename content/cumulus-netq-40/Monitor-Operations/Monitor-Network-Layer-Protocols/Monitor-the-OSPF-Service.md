---
title: Monitor the OSPF Service
author: NVIDIA
weight: 960
toc: 4
---
OSPF maintains the view of the network topology conceptually as a directed graph. Each router represents a vertex in the graph. Each link between neighboring routers represents a unidirectional edge and has an associated weight (called cost) that is either automatically derived from its bandwidth or administratively assigned. Using the weighted topology graph, each router computes a shortest path tree (SPT) with itself as the root, and applies the results to build its forwarding table. For more information about OSPF operation and how to configure OSPF to run in your data center network, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Open-Shortest-Path-First-OSPF/" text="Open Shortest Path First - OSPF">}} or {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Open-Shortest-Path-First-v3-OSPFv3/" text="Open Shortest Path First v3 - OSPFv3">}}.

If you have OSPF running on your switches and hosts, NetQ enables you to view the health of the OSPF service on a networkwide and a per session basis, giving greater insight into all aspects of the service. For each device, you can view its associated interfaces, areas, peers, state, and type of OSPF running (numbered or unnumbered). Additionally, you can view the information at an earlier point in time and filter against a particular device, interface, or area.

This is accomplished in the NetQ UI through two card workflows, one for the service and one for the session, and in the NetQ CLI with the `netq show ospf` command.

## Monitor the OSPF Service Networkwide

With NetQ, you can monitor OSPF performance across the network:

- Network Services|All OSPF Sessions
    - Small: view number of nodes running OSPF service and number and distribution of alarms
    - Medium: view number and distribution of nodes running OSPF service, total sessions, unestablished sessions, and alarms
    - Large: view number and distribution of nodes running OSPF service, total sessions, unestablished sessions, and alarms, switches with the most established sessions/alarms
    - Full-screen: view and filter configuration and status for all switches, all sessions, and all alarms
- `netq show evpn` command: view configuration and status for all devices, including interface, area, type, state, peer hostname and interface, and last time a change was made for each device

{{%notice note%}}
When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: weeks
- **d**: days
- **h**: hours
- **m**: minutes
- **s**: seconds
- **now**

For the `between` option, the start (`text-time`) and end time (`text-endtime`) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{%/notice%}}

### View Service Status Summary

You can view a summary of the OSPF service from the NetQ UI or the NetQ CLI.

{{<tabs "TabID41" >}}

{{<tab "NetQ UI" >}}

To view the summary, open the Network Services|All OSPF Sessions card. In this example, the number of devices running the OSPF service is nine (9) and the number and distribution of related critical severity alarms is zero (0).

{{<figure src="/images/netq/ntwk-svcs-all-ospf-small-230.png" width="200">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view OSPF service status, run:

```
netq show ospf
```

This example shows all devices included in OSPF unnumbered routing, the assigned areas, state, peer and interface, and the last time this information was changed.

```
cumulus@switch:~$ netq show ospf
Matching ospf records:
Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019
leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
leaf02            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp2                      Thu Feb  7 14:42:16 2019
leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
leaf03            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp3                      Thu Feb  7 14:42:16 2019
leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019
leaf04            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp4                      Thu Feb  7 14:42:16 2019
spine01           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp51                     Thu Feb  7 14:42:16 2019
spine02           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp52                     Thu Feb  7 14:42:16 2019
```

{{</tab>}}

{{</tabs>}}

### View the Distribution of Sessions

It is useful to know the number of network nodes running the OSPF protocol over a period of time, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol. It is also useful to view the health of the sessions.

{{<tabs "TabID92" >}}

{{<tab "NetQ UI" >}}

To view these distributions, open the medium Network Services|All OSPF Sessions card. In this example, there are nine nodes running the service with a total of 40 sessions. This has not changed over the past 24 hours.

{{<figure src="/images/netq/ntwk-svcs-all-ospf-medium-230.png" width="200">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view the number of switches running the OSPF service, run:

```
netq show ospf
```

Count the switches in the output.

This example shows four leaf switches and two spine switches are running the OSPF service, for a total of six switches.

```
cumulus@switch:~$ netq show ospf
Matching ospf records:
Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019
leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
leaf02            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp2                      Thu Feb  7 14:42:16 2019
leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
leaf03            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp3                      Thu Feb  7 14:42:16 2019
leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019
leaf04            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp4                      Thu Feb  7 14:42:16 2019
spine01           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp51                     Thu Feb  7 14:42:16 2019
spine02           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp52                     Thu Feb  7 14:42:16 2019
```

To compare this count with the count at another time, run the `netq show ospf` command with the `around` option. Count the devices running OSPF at that time. Repeat with another time to collect a picture of changes over time.

{{</tab>}}

{{</tabs>}}

### View Devices with the Most OSPF Sessions

You can view the load from OSPF on your switches and hosts using the large Network Services card. This data enables you to see which switches are handling the most OSPF traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

{{<tabs "TabID211" >}}

{{<tab "NetQ UI" >}}

To view switches and hosts with the most OSPF sessions:

1. Open the large Network Services|All OSPF Sessions card.

2. Select **Switches with Most Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes running the most OSPF sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-ospf-large-summary-tab-300.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large OSPF Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the original time. We chose *Past Week* for this example.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-ospf-large-summary-tab-past-week-300.png" width="500">}}

<div style="padding-left: 18px;">You can now see whether there are significant differences between this time and the original time. If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running OSPF than previously, looking for changes in the topology, and so forth.</div>

{{</tab>}}

{{<tab "NetQ CLI" >}}

To determine the devices with the most sessions, run `netq show ospf`. Then count the sessions on each device.

In this example, the leaf01-04 switches each have two sessions and the spine01-02 switches have four session each. Therefore the spine switches have the most sessions.

```
cumulus@switch:~$ netq show ospf
Matching ospf records:
Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019
leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
leaf02            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp2                      Thu Feb  7 14:42:16 2019
leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
leaf03            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp3                      Thu Feb  7 14:42:16 2019
leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019
leaf04            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp4                      Thu Feb  7 14:42:16 2019
spine01           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp51                     Thu Feb  7 14:42:16 2019
spine02           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp52                     Thu Feb  7 14:42:16 2019
```

{{</tab>}}

{{</tabs>}}

### View Devices with the Most Unestablished OSPF Sessions

You can identify switches and hosts that are experiencing difficulties establishing OSPF sessions; both currently and in the past using the NetQ UI.

To view switches with the most unestablished OSPF sessions:

1. Open the large Network Services|All OSPF Sessions card.

2. Select **Switches with Most Unestablished Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most unestablished OSPF sessions at the top. Scroll down to view those with the fewest unestablished sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-ospf-large-summary-tab-most-unestab-230.png" width="500">}}

Where to go next depends on what data you see, but a couple of options include:

- Change the time period for the data to compare with a prior time.

    {{<figure src="/images/netq/ntwk-svcs-all-ospf-large-summary-tab-most-unestab-pst-wk-230.png" width="500">}}

    If the same switches are consistently indicating the most unestablished sessions, you might want to look more carefully at those switches using the Switches card workflow to determine probable causes. Refer to {{<link title="Monitor Switch Performance">}}.

- Click **Show All Sessions** to investigate all OSPF sessions with events in the full screen card.

### View Devices with the Most OSPF-related Alarms

Switches or hosts experiencing a large number of OSPF alarms may indicate a configuration or performance issue that needs further investigation. You can view the devices sorted by the number of OSPF alarms and then use the Switches card workflow or the Alarms card workflow to gather more information about possible causes for the alarms. compare the number of nodes running OSPF with unestablished sessions with the alarms present at the same time to determine if there is any correlation between the issues and the ability to establish an OSPF session.

To view switches with the most OSPF alarms:

1. Open the large OSPF Service card.

2. Hover over the header and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18">}}.

3. Select **Switches with Most Alarms** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most OSPF alarms at the top. Scroll down to view those with the fewest alarms.

    {{<figure src="/images/netq/ntwk-svcs-all-ospf-large-alarms-tab-230.png" width="500">}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.
- Click **Show All Sessions** to investigate all OSPF sessions with events in the full screen card.

### View All OSPF Events

You can view all of the OSPF-related events in the network using the NetQ UI or the NetQ CLI.

{{<tabs "TabID286" >}}

{{<tab "NetQ UI" >}}

The Network Services|All OSPF Sessions card enables you to view all of the OSPF events in the designated time period.

To view all OSPF events:

1. Open the full-screen Network Services|All OSPF Sessions card.

2. Click **All Alarms** in the navigation panel. By default, events are listed in most recent to least recent order.

Where to go next depends on what data you see, but a couple of options include:

- Open one of the other full-screen tabs in this flow to focus on devices or sessions.
- Export the data for use in another analytics tool, by clicking {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18">}} and providing a name for the data file.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view OSPF events, run:

```
netq [<hostname>] show events [level info | level error | level warning | level critical | level debug] type ospf [between <text-time> and <text-endtime>] [json]
```

For example:

- To view all OSPF events, run `netq show events type ospf`.
- To view only critical OSPF events, run `netq show events level critical type ospf`.
- To view all OSPF events in the past three days, run `netq show events type ospf between now and 3d`.

{{</tab>}}

{{</tabs>}}

### View Details for All Devices Running OSPF

You can view all stored attributes of all switches and hosts running OSPF in your network in the full screen card.

To view all device details, open the full screen OSPF Service card and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-ospf-fullscr-allswitches-tab-241.png" width="700">}}

To return to your workbench, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the top right corner.

### View Details for All OSPF Sessions

You can view all stored attributes of all OSPF sessions in your network with the NetQ UI or the NetQ CLI.

{{<tabs "TabID337" >}}

{{<tab "NetQ UI" >}}

To view all session details, open the full screen Network Services|All OSPF Sessions card and click the **All Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-all-ospf-fullscr-sessions-tab-222.png" width="700">}}

To return to your workbench, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the top right corner.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}} for more detail. To return to original display of results, click the associated tab.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view session details, run `netq show ospf`.

This example show all current sessions and the attributes associated with them.

```
cumulus@switch:~$ netq show ospf
Matching ospf records:
Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019
leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
leaf02            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp2                      Thu Feb  7 14:42:16 2019
leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
leaf03            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp3                      Thu Feb  7 14:42:16 2019
leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019
leaf04            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp4                      Thu Feb  7 14:42:16 2019
spine01           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp51                     Thu Feb  7 14:42:16 2019
spine02           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp52                     Thu Feb  7 14:42:16 2019
```

{{</tab>}}

{{</tabs>}}

## Monitor a Single OSPF Session

With NetQ, you can monitor the performance of a single OSPF session using the NetQ UI or the NetQ CLI.

- Network Services|OSPF Session
    - Small: view devices participating in the session and summary status
    - Medium: view devices participating in the session, summary status,  session state changes, and key identifiers of the session
    - Large: view devices participating in the session, summary status, session state changes, event distribution and counts, attributes of the session, and the running OSPF configuration and changes to the configuration file
    - Full-screen: view all session attributes and all events
- `netq <hostname> show ospf` command: view configuration and status for session by hostname, including interface, area, type, state, peer hostname, peer interface, and the last time this information changed

For an overview and how to configure OSPF to run in your data center network, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Open-Shortest-Path-First-OSPF/" text="Open Shortest Path First - OSPF">}} or {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Open-Shortest-Path-First-v3-OSPFv3/" text="Open Shortest Path First v3 - OSPFv3">}}.

{{<notice note>}}
To access the single session cards, you must open the full screen Network Services|All OSPF Sessions card, click the <strong>All Sessions</strong> tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Open Card).
{{</notice>}}

### Granularity of Data Shown Based on Time Period

On the medium and large single OSPF session cards, the status of the sessions is represented in heat maps stacked vertically; one for established sessions, and one for unestablished sessions. Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all sessions during that time period were established for the entire time block, then the top block is 100% saturated (white) and the not established block is zero percent saturated (gray). As sessions that are not established increase in saturation, the sessions that are established block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks.

{{<figure src="/images/netq/ntwk-svcs-single-ospf-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### View Session Status Summary

You can view a summary of a given OSPF session from the NetQ UI or NetQ CLI.

{{<tabs "TabID420" >}}

{{<tab "NetQ UI" >}}

To view the summary:

1. Open the Network Services|All OSPF Sessions card.

2. Switch to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Optionally, switch to the small OSPF Session card.  

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-medium-state-highighted-230.png" width="200">}}

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-small-230.png" width="200">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view a session summary, run:

```
netq <hostname> show ospf [<remote-interface>] [area <area-id>] [around <text-time>] [json]
```

Where:

- `remote-interface` specifies the interface on host node
- `area` filters for sessions occurring in a designated OSPF area
- `around` shows status at a time in the past
- `json` outputs the results in JSON format

This example show OSPF sessions on the *leaf01* switch:

```
cumulus@switch:~$ netq leaf01 show ospf
Matching ospf records:
Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019
```

This example shows OSPF sessions for all devices using the *swp51*  interface on the host node.

```
cumulus@switch:~$ netq show ospf swp51
Matching ospf records:
Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019
```

{{</tab>}}

{{</tabs>}}

### View OSPF Session State Changes

You can view the state of a given OSPF session from the medium and large Network Service|All OSPF Sessions card. For a given time period, you can determine the stability of the OSPF session between two devices. If you experienced connectivity issues at a particular time, you can use these cards to help verify the state of the session. If it was not established more than it was established, you can then investigate further into possible causes.

To view the state transitions for a given OSPF session, on the *medium* OSPF Session card:

1. Open the Network Services|All OSPF Sessions card.

2. Switch to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest. The full-screen card closes automatically.

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-medium-state-highighted-230.png" width="200">}}

    The heat map indicates the status of the session over the designated time period. In this example, the session has been established for the entire time period.

    From this card, you can also view the interface name, peer address, and peer id identifying the session in more detail.

To view the state transitions for a given OSPF session on the *large* OSPF Session card:

1. Open a Network Services|OSPF Session card.

2. Hover over the card, and change to the large card using the card size picker.

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-large-state-highighted-230.png" width="500">}}

    From this card, you can view the alarm and info event counts, interface name, peer address and peer id, state, and several other parameters identifying the session in more detail.

### View Changes to the OSPF Service Configuration File

Each time a change is made to the configuration file for the OSPF service, NetQ logs the change and enables you to compare it with the last version using the NetQ UI. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

To view the configuration file changes:

1. Open or add the Network Services|All OSPF Sessions card.

2. Switch to the full-screen card.

3. Click the **All Sessions** tab.

4. Select the session of interest. The full-screen card closes automatically.

5. Hover over the card, and change to the large card using the card size picker.

6. Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> to open the **Configuration File Evolution** tab.

7. Select the time of interest on the left; when a change may have impacted the performance. Scroll down if needed.

8. Choose between the **File** view and the **Diff** view (selected option is dark; File by default).

    The File view displays the content of the file for you to review.

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-large-config-tab-file-selected-230.png" width="500">}}

    The Diff view displays the changes between this version (on left) and the most recent version (on right) side by side. The changes are highlighted in red and green. In this example, we don't have a change to highlight, so it shows the same file on both sides.

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-large-config-tab-diff-selected-230.png" width="500">}}

### View All OSPF Session Details

You can view attributes of all of the OSPF sessions for the devices participating in a given session with the NetQ UI and the NetQ CLI.

{{<tabs "TabID520" >}}

{{<tab "NetQ UI" >}}

To view all session details:

1. Open or add the Network Services|All OSPF Sessions card.

2. Switch to the full-screen card.

3. Click the **All Sessions** tab.

4. Select the session of interest. The full-screen card closes automatically.

5. Hover over the card, and change to the full-screen card using the card size picker.

    {{<figure src="/images/netq/ntwk-svcs-single-ospf-fullscr-sessions-tab-222.png" width="700">}}

6. To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

{{</tab>}}

{{<tab "NetQ CLI" >}}

Run the `netq show ospf` command.

This example shows all OSPF sessions. Filter by remote interface or area to narrow the listing. Scroll until you find the session of interest.

```
cumulus@switch:~$ netq show ospf
Matching ospf records:
Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019
leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
leaf02            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp2                      Thu Feb  7 14:42:16 2019
leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
leaf03            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp3                      Thu Feb  7 14:42:16 2019
leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019
leaf04            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp4                      Thu Feb  7 14:42:16 2019
spine01           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp51                     Thu Feb  7 14:42:16 2019
spine02           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp52                     Thu Feb  7 14:42:16 2019
```

{{</tab>}}

{{</tabs>}}

### View All Events for a Given Session

You can view all alarm and info events for the devices participating in a given session with the NetQ UI.

To view all events:

1. Open or add the Network Services|All OSPF Sessions card.

2. Switch to the full-screen card.

3. Click the **All Sessions** tab.

4. Select the session of interest. The full-screen card closes automatically.

5. Hover over the card, and change to the full-screen card using the card size picker.

6. Click the **All Events** tab.

7. To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.
