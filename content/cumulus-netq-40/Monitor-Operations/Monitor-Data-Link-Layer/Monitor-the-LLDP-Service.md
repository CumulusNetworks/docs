---
title: Monitor the LLDP Service
author: NVIDIA
weight: 890
toc: 4
---
LLDP is used by network devices for advertising their identity, capabilities, and neighbors on a LAN. You can view this information for one or more devices. You can also view the information at an earlier point in time or view changes that have occurred to the information during a specified time period. For an overview and how to configure LLDP in your network, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-2/Link-Layer-Discovery-Protocol/" text="Link Layer Discovery Protocol">}}.

NetQ enables operators to view the overall health of the LLDP service on a networkwide and a per session basis, giving greater insight into all aspects of the service. This is accomplished in the NetQ UI through two card workflows, one for the service and one for the session and in the NetQ CLI with the `netq show lldp` command.

## Monitor the LLDP Service Networkwide

With NetQ, you can monitor LLDP performance across the network:

- Network Services|All LLDP Sessions
    - Small: view number of nodes running LLDP service and number of alarms
    - Medium: view number of nodes running LLDP service, number of sessions, and number of alarms
    - Large: view number of nodes running LLDP service, number of sessions and alarms, number of sessions without neighbors, switches with the most established/unestablished sessions
    - Full-screen: view all switches, all sessions, and all alarms
- `netq show evpn` command: view associated host interface, peer hostname and interface, and last time a change was made for each session running LLDP

{{%notice note%}}

When entering a time value in the `netq show lldp` command, you must include a numeric value *and* the unit of measure:

- **w**: weeks
- **d**: days
- **h**: hours
- **m**: minutes
- **s**: seconds
- **now**

When using the `between` option, the start time (`text-time`) and end time (`text-endtime`) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.

{{%/notice%}}

### View Service Status Summary

You can view a summary of the LLDP service from the NetQ UI or the NetQ CLI.

{{<tabs "TabID41" >}}

{{<tab "NetQ UI" >}}

Open the small Network Services|All LLDP Sessions card. In this example, the number of devices running the LLDP service is 14 and no alarms are present.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-small-230.png" width="200" >}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view LLDP service status, run `netq show lldp`.

This example shows the Cumulus reference topology, where LLDP runs on all border, firewall, leaf, and spine switches, all servers, and the out-of-band management server. You can view the host interface, peer hostname and interface, and last time a change was made for each session.

```
cumulus@switch:~$ netq show lldp

Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
border01          swp3                      fw1               swp1                      Mon Oct 26 04:13:29 2020
border01          swp49                     border02          swp49                     Mon Oct 26 04:13:29 2020
border01          swp51                     spine01           swp5                      Mon Oct 26 04:13:29 2020
border01          swp52                     spine02           swp5                      Mon Oct 26 04:13:29 2020
border01          eth0                      oob-mgmt-switch   swp20                     Mon Oct 26 04:13:29 2020
border01          swp53                     spine03           swp5                      Mon Oct 26 04:13:29 2020
border01          swp50                     border02          swp50                     Mon Oct 26 04:13:29 2020
border01          swp54                     spine04           swp5                      Mon Oct 26 04:13:29 2020
border02          swp49                     border01          swp49                     Mon Oct 26 04:13:11 2020
border02          swp3                      fw1               swp2                      Mon Oct 26 04:13:11 2020
border02          swp51                     spine01           swp6                      Mon Oct 26 04:13:11 2020
border02          swp54                     spine04           swp6                      Mon Oct 26 04:13:11 2020
border02          swp52                     spine02           swp6                      Mon Oct 26 04:13:11 2020
border02          eth0                      oob-mgmt-switch   swp21                     Mon Oct 26 04:13:11 2020
border02          swp53                     spine03           swp6                      Mon Oct 26 04:13:11 2020
border02          swp50                     border01          swp50                     Mon Oct 26 04:13:11 2020
fw1               eth0                      oob-mgmt-switch   swp18                     Mon Oct 26 04:38:03 2020
fw1               swp1                      border01          swp3                      Mon Oct 26 04:38:03 2020
fw1               swp2                      border02          swp3                      Mon Oct 26 04:38:03 2020
fw2               eth0                      oob-mgmt-switch   swp19                     Mon Oct 26 04:46:54 2020
leaf01            swp1                      server01          mac:44:38:39:00:00:32     Mon Oct 26 04:13:57 2020
leaf01            swp2                      server02          mac:44:38:39:00:00:34     Mon Oct 26 04:13:57 2020
leaf01            swp52                     spine02           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp49                     leaf02            swp49                     Mon Oct 26 04:13:57 2020
leaf01            eth0                      oob-mgmt-switch   swp10                     Mon Oct 26 04:13:57 2020
leaf01            swp3                      server03          mac:44:38:39:00:00:36     Mon Oct 26 04:13:57 2020
leaf01            swp53                     spine03           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp50                     leaf02            swp50                     Mon Oct 26 04:13:57 2020
leaf01            swp54                     spine04           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp51                     spine01           swp1                      Mon Oct 26 04:13:57 2020
...
```

{{</tab>}}

{{</tabs>}}

<!-- ### View Devices Running LLDP Service

You can view the devices running the LLDP service with either the NetQ UI or the NetQ CLI.

{{<tabs "TabID41" >}}

{{<tab "NetQ UI" >}}

1. Open the LLDP Service card.

    icon (add card) > Click **Network Services** > Click All LLDP Sessions card > Click **Open Cards**

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-medium.png" width="200">}}

2. Change to the full-screen card using the size picker.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-allswitches-tab-320.png" width="700">}}

    If you have more than one page of switches running LLDP, the total count is indicated in the pagination bar.

{{</tab>}}

{{<tab "NetQ CLI" >}}

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

{{</tab>}}

{{</tabs>}} -->

### View the Distribution of Nodes, Alarms, and Sessions

It is useful to know the number of network nodes running the LLDP protocol over a period of time and how many sessions are established on a given node, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol. Additionally, if there are a large number of alarms, it is worth investigating either the service or particular devices.

Nodes which have a large number of unestablished sessions might be misconfigured or experiencing communication issues. This is visible with the NetQ UI.

{{<tabs "TabID178" >}}

{{<tab "NetQ UI" >}}

To view the distribution, open the medium Network Services|All LLDP Sessions card.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-medium.png" width="200">}}

In this example, we see that 13 nodes are running the LLDP protocol, that there are 52 sessions established, and that no LLDP-related alarms have occurred in the last 24 hours. If there was a visual correlation between the alarms and sessions, you could dig a little deeper with the large Network Services|All LLDP Sessions card.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view the number of switches running the LLDP service, run:

```
netq show lldp
```

Count the switches in the output.

This example shows two border, two firewall, four leaf switches, four spine, and one out-of-band management switches, plus eight host servers are all running the LLDP service, for a total of 23 devices.

```
cumulus@switch:~$ netq show lldp
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
border01          swp3                      fw1               swp1                      Mon Oct 26 04:13:29 2020
border01          swp49                     border02          swp49                     Mon Oct 26 04:13:29 2020
border01          swp51                     spine01           swp5                      Mon Oct 26 04:13:29 2020
border01          swp52                     spine02           swp5                      Mon Oct 26 04:13:29 2020
border01          eth0                      oob-mgmt-switch   swp20                     Mon Oct 26 04:13:29 2020
border01          swp53                     spine03           swp5                      Mon Oct 26 04:13:29 2020
border01          swp50                     border02          swp50                     Mon Oct 26 04:13:29 2020
border01          swp54                     spine04           swp5                      Mon Oct 26 04:13:29 2020
border02          swp49                     border01          swp49                     Mon Oct 26 04:13:11 2020
border02          swp3                      fw1               swp2                      Mon Oct 26 04:13:11 2020
border02          swp51                     spine01           swp6                      Mon Oct 26 04:13:11 2020
border02          swp54                     spine04           swp6                      Mon Oct 26 04:13:11 2020
border02          swp52                     spine02           swp6                      Mon Oct 26 04:13:11 2020
border02          eth0                      oob-mgmt-switch   swp21                     Mon Oct 26 04:13:11 2020
border02          swp53                     spine03           swp6                      Mon Oct 26 04:13:11 2020
border02          swp50                     border01          swp50                     Mon Oct 26 04:13:11 2020
fw1               eth0                      oob-mgmt-switch   swp18                     Mon Oct 26 04:38:03 2020
fw1               swp1                      border01          swp3                      Mon Oct 26 04:38:03 2020
fw1               swp2                      border02          swp3                      Mon Oct 26 04:38:03 2020
fw2               eth0                      oob-mgmt-switch   swp19                     Mon Oct 26 04:46:54 2020
leaf01            swp1                      server01          mac:44:38:39:00:00:32     Mon Oct 26 04:13:57 2020
leaf01            swp2                      server02          mac:44:38:39:00:00:34     Mon Oct 26 04:13:57 2020
leaf01            swp52                     spine02           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp49                     leaf02            swp49                     Mon Oct 26 04:13:57 2020
leaf01            eth0                      oob-mgmt-switch   swp10                     Mon Oct 26 04:13:57 2020
leaf01            swp3                      server03          mac:44:38:39:00:00:36     Mon Oct 26 04:13:57 2020
leaf01            swp53                     spine03           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp50                     leaf02            swp50                     Mon Oct 26 04:13:57 2020
leaf01            swp54                     spine04           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp51                     spine01           swp1                      Mon Oct 26 04:13:57 2020
leaf02            swp52                     spine02           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp54                     spine04           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp2                      server02          mac:44:38:39:00:00:3a     Mon Oct 26 04:14:57 2020
leaf02            swp3                      server03          mac:44:38:39:00:00:3c     Mon Oct 26 04:14:57 2020
leaf02            swp53                     spine03           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp50                     leaf01            swp50                     Mon Oct 26 04:14:57 2020
leaf02            swp51                     spine01           swp2                      Mon Oct 26 04:14:57 2020
leaf02            eth0                      oob-mgmt-switch   swp11                     Mon Oct 26 04:14:57 2020
leaf02            swp49                     leaf01            swp49                     Mon Oct 26 04:14:57 2020
leaf02            swp1                      server01          mac:44:38:39:00:00:38     Mon Oct 26 04:14:57 2020
leaf03            swp2                      server05          mac:44:38:39:00:00:40     Mon Oct 26 04:16:09 2020
leaf03            swp49                     leaf04            swp49                     Mon Oct 26 04:16:09 2020
leaf03            swp51                     spine01           swp3                      Mon Oct 26 04:16:09 2020
leaf03            swp50                     leaf04            swp50                     Mon Oct 26 04:16:09 2020
leaf03            swp54                     spine04           swp3                      Mon Oct 26 04:16:09 2020
leaf03            swp1                      server04          mac:44:38:39:00:00:3e     Mon Oct 26 04:16:09 2020
leaf03            swp52                     spine02           swp3                      Mon Oct 26 04:16:09 2020
leaf03            eth0                      oob-mgmt-switch   swp12                     Mon Oct 26 04:16:09 2020
leaf03            swp53                     spine03           swp3                      Mon Oct 26 04:16:09 2020
leaf03            swp3                      server06          mac:44:38:39:00:00:42     Mon Oct 26 04:16:09 2020
leaf04            swp1                      server04          mac:44:38:39:00:00:44     Mon Oct 26 04:15:57 2020
leaf04            swp49                     leaf03            swp49                     Mon Oct 26 04:15:57 2020
leaf04            swp54                     spine04           swp4                      Mon Oct 26 04:15:57 2020
leaf04            swp52                     spine02           swp4                      Mon Oct 26 04:15:57 2020
leaf04            swp2                      server05          mac:44:38:39:00:00:46     Mon Oct 26 04:15:57 2020
leaf04            swp50                     leaf03            swp50                     Mon Oct 26 04:15:57 2020
leaf04            swp51                     spine01           swp4                      Mon Oct 26 04:15:57 2020
leaf04            eth0                      oob-mgmt-switch   swp13                     Mon Oct 26 04:15:57 2020
leaf04            swp3                      server06          mac:44:38:39:00:00:48     Mon Oct 26 04:15:57 2020
leaf04            swp53                     spine03           swp4                      Mon Oct 26 04:15:57 2020
oob-mgmt-server   eth1                      oob-mgmt-switch   swp1                      Sun Oct 25 22:46:24 2020
server01          eth0                      oob-mgmt-switch   swp2                      Sun Oct 25 22:51:17 2020
server01          eth1                      leaf01            swp1                      Sun Oct 25 22:51:17 2020
server01          eth2                      leaf02            swp1                      Sun Oct 25 22:51:17 2020
server02          eth0                      oob-mgmt-switch   swp3                      Sun Oct 25 22:49:41 2020
server02          eth1                      leaf01            swp2                      Sun Oct 25 22:49:41 2020
server02          eth2                      leaf02            swp2                      Sun Oct 25 22:49:41 2020
server03          eth2                      leaf02            swp3                      Sun Oct 25 22:50:08 2020
server03          eth1                      leaf01            swp3                      Sun Oct 25 22:50:08 2020
server03          eth0                      oob-mgmt-switch   swp4                      Sun Oct 25 22:50:08 2020
server04          eth0                      oob-mgmt-switch   swp5                      Sun Oct 25 22:50:27 2020
server04          eth1                      leaf03            swp1                      Sun Oct 25 22:50:27 2020
server04          eth2                      leaf04            swp1                      Sun Oct 25 22:50:27 2020
server05          eth0                      oob-mgmt-switch   swp6                      Sun Oct 25 22:49:12 2020
server05          eth1                      leaf03            swp2                      Sun Oct 25 22:49:12 2020
server05          eth2                      leaf04            swp2                      Sun Oct 25 22:49:12 2020
server06          eth0                      oob-mgmt-switch   swp7                      Sun Oct 25 22:49:22 2020
server06          eth1                      leaf03            swp3                      Sun Oct 25 22:49:22 2020
server06          eth2                      leaf04            swp3                      Sun Oct 25 22:49:22 2020
server07          eth0                      oob-mgmt-switch   swp8                      Sun Oct 25 22:29:58 2020
server08          eth0                      oob-mgmt-switch   swp9                      Sun Oct 25 22:34:12 2020
spine01           swp1                      leaf01            swp51                     Mon Oct 26 04:13:20 2020
spine01           swp3                      leaf03            swp51                     Mon Oct 26 04:13:20 2020
spine01           swp2                      leaf02            swp51                     Mon Oct 26 04:13:20 2020
spine01           swp5                      border01          swp51                     Mon Oct 26 04:13:20 2020
spine01           eth0                      oob-mgmt-switch   swp14                     Mon Oct 26 04:13:20 2020
spine01           swp4                      leaf04            swp51                     Mon Oct 26 04:13:20 2020
spine01           swp6                      border02          swp51                     Mon Oct 26 04:13:20 2020
spine02           swp4                      leaf04            swp52                     Mon Oct 26 04:16:26 2020
spine02           swp3                      leaf03            swp52                     Mon Oct 26 04:16:26 2020
spine02           swp6                      border02          swp52                     Mon Oct 26 04:16:26 2020
spine02           eth0                      oob-mgmt-switch   swp15                     Mon Oct 26 04:16:26 2020
spine02           swp5                      border01          swp52                     Mon Oct 26 04:16:26 2020
spine02           swp2                      leaf02            swp52                     Mon Oct 26 04:16:26 2020
spine02           swp1                      leaf01            swp52                     Mon Oct 26 04:16:26 2020
spine03           swp2                      leaf02            swp53                     Mon Oct 26 04:13:48 2020
spine03           swp6                      border02          swp53                     Mon Oct 26 04:13:48 2020
spine03           swp1                      leaf01            swp53                     Mon Oct 26 04:13:48 2020
spine03           swp3                      leaf03            swp53                     Mon Oct 26 04:13:48 2020
spine03           swp4                      leaf04            swp53                     Mon Oct 26 04:13:48 2020
spine03           eth0                      oob-mgmt-switch   swp16                     Mon Oct 26 04:13:48 2020
spine03           swp5                      border01          swp53                     Mon Oct 26 04:13:48 2020
spine04           eth0                      oob-mgmt-switch   swp17                     Mon Oct 26 04:11:23 2020
spine04           swp3                      leaf03            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp2                      leaf02            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp4                      leaf04            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp1                      leaf01            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp5                      border01          swp54                     Mon Oct 26 04:11:23 2020
spine04           swp6                      border02          swp54                     Mon Oct 26 04:11:23 2020
```

{{</tab>}}

{{</tabs>}}

### View the Distribution of Missing Neighbors

You can view the number of missing neighbors in any given time period and how that number has changed over time. This is a good indicator of link communication issues.

To view the distribution, open the large Network Services|ALL LLDP Sessions card and view the bottom chart on the left, **Total Sessions with No Nbr**.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-no-nbr-highlight-230.png" width="500">}}

In this example, we see that 16 of the 52 sessions are consistently missing the neighbor (peer) device over the last 24 hours.

### View Devices with the Most LLDP Sessions

You can view the load from LLDP on your switches using the large Network Services|All LLDP Sessions card or the NetQ CLI. This data enables you to see which switches are handling the most LLDP traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

{{<tabs "TabID336" >}}

{{<tab "NetQ UI" >}}

To view switches and hosts with the most LLDP sessions:

1. Open the large Network Services|All LLDP Sessions card.

2. Select **Switches with Most Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes running the most LLDP sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-300.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large LLDP Service card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4.  Select the time period that you want to compare with the current time. You can now see whether there are significant differences between this time period and the previous time period.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-past-week-300.png" width="500" >}}

<div style="padding-left: 18px;">In this case, notice that their are fewer nodes running the protocol, but the total number of sessions running has nearly doubled. If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running LLDP than previously, looking for changes in the topology, and so forth.</div>

{{</tab>}}

{{<tab "NetQ CLI" >}}

To determine the devices with the most sessions, run `netq show lldp`. Then count the sessions on each device.

In this example, border01-02 each have eight sessions, fw1-2 each have two sessions, leaf01-04 each have 10 sessions, spine01-04 switches each have four sessions, server01-06 each have three sessions, and server07-08 and oob-mgmt-server each have one session. Therefore the leaf switches have the most sessions.

```
cumulus@switch:~$ netq show lldp
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
border01          swp3                      fw1               swp1                      Mon Oct 26 04:13:29 2020
border01          swp49                     border02          swp49                     Mon Oct 26 04:13:29 2020
border01          swp51                     spine01           swp5                      Mon Oct 26 04:13:29 2020
border01          swp52                     spine02           swp5                      Mon Oct 26 04:13:29 2020
border01          eth0                      oob-mgmt-switch   swp20                     Mon Oct 26 04:13:29 2020
border01          swp53                     spine03           swp5                      Mon Oct 26 04:13:29 2020
border01          swp50                     border02          swp50                     Mon Oct 26 04:13:29 2020
border01          swp54                     spine04           swp5                      Mon Oct 26 04:13:29 2020
border02          swp49                     border01          swp49                     Mon Oct 26 04:13:11 2020
border02          swp3                      fw1               swp2                      Mon Oct 26 04:13:11 2020
border02          swp51                     spine01           swp6                      Mon Oct 26 04:13:11 2020
border02          swp54                     spine04           swp6                      Mon Oct 26 04:13:11 2020
border02          swp52                     spine02           swp6                      Mon Oct 26 04:13:11 2020
border02          eth0                      oob-mgmt-switch   swp21                     Mon Oct 26 04:13:11 2020
border02          swp53                     spine03           swp6                      Mon Oct 26 04:13:11 2020
border02          swp50                     border01          swp50                     Mon Oct 26 04:13:11 2020
fw1               eth0                      oob-mgmt-switch   swp18                     Mon Oct 26 04:38:03 2020
fw1               swp1                      border01          swp3                      Mon Oct 26 04:38:03 2020
fw1               swp2                      border02          swp3                      Mon Oct 26 04:38:03 2020
fw2               eth0                      oob-mgmt-switch   swp19                     Mon Oct 26 04:46:54 2020
leaf01            swp1                      server01          mac:44:38:39:00:00:32     Mon Oct 26 04:13:57 2020
leaf01            swp2                      server02          mac:44:38:39:00:00:34     Mon Oct 26 04:13:57 2020
leaf01            swp52                     spine02           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp49                     leaf02            swp49                     Mon Oct 26 04:13:57 2020
leaf01            eth0                      oob-mgmt-switch   swp10                     Mon Oct 26 04:13:57 2020
leaf01            swp3                      server03          mac:44:38:39:00:00:36     Mon Oct 26 04:13:57 2020
leaf01            swp53                     spine03           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp50                     leaf02            swp50                     Mon Oct 26 04:13:57 2020
leaf01            swp54                     spine04           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp51                     spine01           swp1                      Mon Oct 26 04:13:57 2020
leaf02            swp52                     spine02           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp54                     spine04           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp2                      server02          mac:44:38:39:00:00:3a     Mon Oct 26 04:14:57 2020
leaf02            swp3                      server03          mac:44:38:39:00:00:3c     Mon Oct 26 04:14:57 2020
leaf02            swp53                     spine03           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp50                     leaf01            swp50                     Mon Oct 26 04:14:57 2020
leaf02            swp51                     spine01           swp2                      Mon Oct 26 04:14:57 2020
leaf02            eth0                      oob-mgmt-switch   swp11                     Mon Oct 26 04:14:57 2020
leaf02            swp49                     leaf01            swp49                     Mon Oct 26 04:14:57 2020
leaf02            swp1                      server01          mac:44:38:39:00:00:38     Mon Oct 26 04:14:57 2020
leaf03            swp2                      server05          mac:44:38:39:00:00:40     Mon Oct 26 04:16:09 2020
leaf03            swp49                     leaf04            swp49                     Mon Oct 26 04:16:09 2020
leaf03            swp51                     spine01           swp3                      Mon Oct 26 04:16:09 2020
leaf03            swp50                     leaf04            swp50                     Mon Oct 26 04:16:09 2020
leaf03            swp54                     spine04           swp3                      Mon Oct 26 04:16:09 2020
leaf03            swp1                      server04          mac:44:38:39:00:00:3e     Mon Oct 26 04:16:09 2020
leaf03            swp52                     spine02           swp3                      Mon Oct 26 04:16:09 2020
leaf03            eth0                      oob-mgmt-switch   swp12                     Mon Oct 26 04:16:09 2020
leaf03            swp53                     spine03           swp3                      Mon Oct 26 04:16:09 2020
leaf03            swp3                      server06          mac:44:38:39:00:00:42     Mon Oct 26 04:16:09 2020
leaf04            swp1                      server04          mac:44:38:39:00:00:44     Mon Oct 26 04:15:57 2020
leaf04            swp49                     leaf03            swp49                     Mon Oct 26 04:15:57 2020
leaf04            swp54                     spine04           swp4                      Mon Oct 26 04:15:57 2020
leaf04            swp52                     spine02           swp4                      Mon Oct 26 04:15:57 2020
leaf04            swp2                      server05          mac:44:38:39:00:00:46     Mon Oct 26 04:15:57 2020
leaf04            swp50                     leaf03            swp50                     Mon Oct 26 04:15:57 2020
leaf04            swp51                     spine01           swp4                      Mon Oct 26 04:15:57 2020
leaf04            eth0                      oob-mgmt-switch   swp13                     Mon Oct 26 04:15:57 2020
leaf04            swp3                      server06          mac:44:38:39:00:00:48     Mon Oct 26 04:15:57 2020
leaf04            swp53                     spine03           swp4                      Mon Oct 26 04:15:57 2020
oob-mgmt-server   eth1                      oob-mgmt-switch   swp1                      Sun Oct 25 22:46:24 2020
server01          eth0                      oob-mgmt-switch   swp2                      Sun Oct 25 22:51:17 2020
server01          eth1                      leaf01            swp1                      Sun Oct 25 22:51:17 2020
server01          eth2                      leaf02            swp1                      Sun Oct 25 22:51:17 2020
server02          eth0                      oob-mgmt-switch   swp3                      Sun Oct 25 22:49:41 2020
server02          eth1                      leaf01            swp2                      Sun Oct 25 22:49:41 2020
server02          eth2                      leaf02            swp2                      Sun Oct 25 22:49:41 2020
server03          eth2                      leaf02            swp3                      Sun Oct 25 22:50:08 2020
server03          eth1                      leaf01            swp3                      Sun Oct 25 22:50:08 2020
server03          eth0                      oob-mgmt-switch   swp4                      Sun Oct 25 22:50:08 2020
server04          eth0                      oob-mgmt-switch   swp5                      Sun Oct 25 22:50:27 2020
server04          eth1                      leaf03            swp1                      Sun Oct 25 22:50:27 2020
server04          eth2                      leaf04            swp1                      Sun Oct 25 22:50:27 2020
server05          eth0                      oob-mgmt-switch   swp6                      Sun Oct 25 22:49:12 2020
server05          eth1                      leaf03            swp2                      Sun Oct 25 22:49:12 2020
server05          eth2                      leaf04            swp2                      Sun Oct 25 22:49:12 2020
server06          eth0                      oob-mgmt-switch   swp7                      Sun Oct 25 22:49:22 2020
server06          eth1                      leaf03            swp3                      Sun Oct 25 22:49:22 2020
server06          eth2                      leaf04            swp3                      Sun Oct 25 22:49:22 2020
server07          eth0                      oob-mgmt-switch   swp8                      Sun Oct 25 22:29:58 2020
server08          eth0                      oob-mgmt-switch   swp9                      Sun Oct 25 22:34:12 2020
spine01           swp1                      leaf01            swp51                     Mon Oct 26 04:13:20 2020
spine01           swp3                      leaf03            swp51                     Mon Oct 26 04:13:20 2020
spine01           swp2                      leaf02            swp51                     Mon Oct 26 04:13:20 2020
spine01           swp5                      border01          swp51                     Mon Oct 26 04:13:20 2020
spine01           eth0                      oob-mgmt-switch   swp14                     Mon Oct 26 04:13:20 2020
spine01           swp4                      leaf04            swp51                     Mon Oct 26 04:13:20 2020
spine01           swp6                      border02          swp51                     Mon Oct 26 04:13:20 2020
spine02           swp4                      leaf04            swp52                     Mon Oct 26 04:16:26 2020
spine02           swp3                      leaf03            swp52                     Mon Oct 26 04:16:26 2020
spine02           swp6                      border02          swp52                     Mon Oct 26 04:16:26 2020
spine02           eth0                      oob-mgmt-switch   swp15                     Mon Oct 26 04:16:26 2020
spine02           swp5                      border01          swp52                     Mon Oct 26 04:16:26 2020
spine02           swp2                      leaf02            swp52                     Mon Oct 26 04:16:26 2020
spine02           swp1                      leaf01            swp52                     Mon Oct 26 04:16:26 2020
spine03           swp2                      leaf02            swp53                     Mon Oct 26 04:13:48 2020
spine03           swp6                      border02          swp53                     Mon Oct 26 04:13:48 2020
spine03           swp1                      leaf01            swp53                     Mon Oct 26 04:13:48 2020
spine03           swp3                      leaf03            swp53                     Mon Oct 26 04:13:48 2020
spine03           swp4                      leaf04            swp53                     Mon Oct 26 04:13:48 2020
spine03           eth0                      oob-mgmt-switch   swp16                     Mon Oct 26 04:13:48 2020
spine03           swp5                      border01          swp53                     Mon Oct 26 04:13:48 2020
spine04           eth0                      oob-mgmt-switch   swp17                     Mon Oct 26 04:11:23 2020
spine04           swp3                      leaf03            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp2                      leaf02            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp4                      leaf04            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp1                      leaf01            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp5                      border01          swp54                     Mon Oct 26 04:11:23 2020
spine04           swp6                      border02          swp54                     Mon Oct 26 04:11:23 2020
```

{{</tab>}}

{{</tabs>}}

### View Devices with the Most Unestablished LLDP Sessions

You can identify switches and hosts that are experiencing difficulties establishing LLDP sessions; both currently and in the past, using the NetQ UI.

To view switches with the most unestablished LLDP sessions:

1. Open the large Network Services|All LLDP Sessions card.

2. Select **Switches with Most Unestablished Sessions** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes with the most unestablished LLDP sessions at the top. Scroll down to view those with the fewest unestablished sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-large-summary-tab-most-unestab-300.png" width="500">}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most unestablished sessions, you might want to look more carefully at those switches using the Switches card workflow to determine probable causes. Refer to {{<link title="Monitor Switch Performance">}}.
- Click **Show All Sessions** to investigate all LLDP sessions with events in the full screen card.

### View LLDP Configuration Information for a Given Device

You can view the LLDP configuration information for a given device from the NetQ UI or the NetQ CLI.

{{<tabs "View LLDP for a Device">}}

{{<tab "NetQ UI">}}

1. Open the full-screen Network Services|All LLDP Sessions card.

2. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} to filter by hostname.

3. Click **Apply**.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-allsess-tab-filterbyHn-320.png" width="500">}}

{{</tab>}}

{{<tab "NetQ CLI">}}

Run the `netq show lldp` command with the `hostname` option.

This example shows the LLDP configuration information for the *leaf01*  switch. The switch has a session between its *swp1* interface and host *server01* in the *mac:44:38:39:00:00:32* interface. It also has a session between its *swp2* interface and host *server02* on *mac:44:38:39:00:00:34* interface. And so on.

```
cumulus@netq-ts:~$ netq leaf01 show lldp
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
leaf01            swp1                      server01          mac:44:38:39:00:00:32     Mon Oct 26 04:13:57 2020
leaf01            swp2                      server02          mac:44:38:39:00:00:34     Mon Oct 26 04:13:57 2020
leaf01            swp52                     spine02           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp49                     leaf02            swp49                     Mon Oct 26 04:13:57 2020
leaf01            eth0                      oob-mgmt-switch   swp10                     Mon Oct 26 04:13:57 2020
leaf01            swp3                      server03          mac:44:38:39:00:00:36     Mon Oct 26 04:13:57 2020
leaf01            swp53                     spine03           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp50                     leaf02            swp50                     Mon Oct 26 04:13:57 2020
leaf01            swp54                     spine04           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp51                     spine01           swp1                      Mon Oct 26 04:13:57 2020
```

{{</tab>}}

{{</tabs>}}

<!-- vale off -->
### View Switches with the Most LLDP-related Alarms
<!-- vale on -->

Switches or hosts experiencing a large number of LLDP alarms may indicate a configuration or performance issue that needs further investigation. You can view this information using the NetQ UI or NetQ CLI.

{{<tabs "View switches with most LLDP alarms">}}

{{<tab "NetQ UI">}}

With the NetQ UI, you can view the switches sorted by the number of LLDP alarms and then use the Switches card workflow or the Events|Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with most LLDP alarms:

1. Open the large Network Services|All LLDP Sessions card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Events by Most Active Device** from the filter above the  table.

    The table content is sorted by this characteristic, listing nodes with the most LLDP alarms at the top. Scroll down to view those with the fewest alarms.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-large-alarms-tab.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.
- Click **Show All Sessions** to investigate all switches running LLDP sessions in the full-screen card.

{{</tab>}}

{{<tab "NetQ CLI">}}

To view the switches and hosts with the most LLDP alarms and informational events, run the `netq show events` command with the `type` option set to *lldp*, and optionally the `between` option set to display the events within a given time range. Count the events associated with each switch.

This example shows that no LLDP events have occurred in the last 24 hours.

```
cumulus@switch:~$ netq show events type lldp
No matching event records found
```

This example shows all LLDP events between now and 30 days ago, a total of 21 info events.

```
cumulus@switch:~$ netq show events type lldp between now and 30d
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
spine02           lldp                     info             LLDP Session with hostname spine02  Fri Oct  2 22:28:57 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
leaf04            lldp                     info             LLDP Session with hostname leaf04 a Fri Oct  2 22:28:39 2020
                                                            nd eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
border02          lldp                     info             LLDP Session with hostname border02 Fri Oct  2 22:28:35 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
spine04           lldp                     info             LLDP Session with hostname spine04  Fri Oct  2 22:28:35 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
server07          lldp                     info             LLDP Session with hostname server07 Fri Oct  2 22:28:34 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
server08          lldp                     info             LLDP Session with hostname server08 Fri Oct  2 22:28:33 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
fw2               lldp                     info             LLDP Session with hostname fw2 and  Fri Oct  2 22:28:32 2020
                                                            eth0 modified fields {"new lldp pee
                                                            r osv":"4.2.1","old lldp peer osv":
                                                            "3.7.12"}
server02          lldp                     info             LLDP Session with hostname server02 Fri Oct  2 22:28:31 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
server03          lldp                     info             LLDP Session with hostname server03 Fri Oct  2 22:28:28 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
border01          lldp                     info             LLDP Session with hostname border01 Fri Oct  2 22:28:28 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
leaf03            lldp                     info             LLDP Session with hostname leaf03 a Fri Oct  2 22:28:27 2020
                                                            nd eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
fw1               lldp                     info             LLDP Session with hostname fw1 and  Fri Oct  2 22:28:23 2020
                                                            eth0 modified fields {"new lldp pee
                                                            r osv":"4.2.1","old lldp peer osv":
                                                            "3.7.12"}
server05          lldp                     info             LLDP Session with hostname server05 Fri Oct  2 22:28:22 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
server06          lldp                     info             LLDP Session with hostname server06 Fri Oct  2 22:28:21 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
spine03           lldp                     info             LLDP Session with hostname spine03  Fri Oct  2 22:28:20 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
server01          lldp                     info             LLDP Session with hostname server01 Fri Oct  2 22:28:15 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
server04          lldp                     info             LLDP Session with hostname server04 Fri Oct  2 22:28:13 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
leaf01            lldp                     info             LLDP Session with hostname leaf01 a Fri Oct  2 22:28:05 2020
                                                            nd eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
spine01           lldp                     info             LLDP Session with hostname spine01  Fri Oct  2 22:28:05 2020
                                                            and eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
oob-mgmt-server   lldp                     info             LLDP Session with hostname oob-mgmt Fri Oct  2 22:27:54 2020
                                                            -server and eth1 modified fields {"
                                                            new lldp peer osv":"4.2.1","old lld
                                                            p peer osv":"3.7.12"}
leaf02            lldp                     info             LLDP Session with hostname leaf02 a Fri Oct  2 22:27:39 2020
                                                            nd eth0 modified fields {"new lldp
                                                            peer osv":"4.2.1","old lldp peer os
                                                            v":"3.7.12"}
```

{{</tab>}}

{{</tabs>}}

### View All LLDP Events

The Network Services|All LLDP Sessions card workflow and the `netq show events type lldp` command enable you to view all LLDP events in a designated time period.

{{<tabs "View all LLDP events">}}

{{<tab "NetQ UI">}}

To view all LLDP events:

1. Open the Network Services|All LLDP Sessions card.

2. Change to the full-screen card using the card size picker.

3. Click the **All Alarms** tab.

    By default, events are listed in most recent to least recent order.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-alarms-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Sort on various parameters:
    - by **Message** to determine the frequency of particular events
    - by **Severity** to determine the most critical events
    - by **Time** to find events that may have occurred at a particular time to try to correlate them with other system events
- Open one of the other full-screen tabs in this flow to focus on devices or sessions
- Export data to a file for use in another analytics tool by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> and providing a name for the data file.
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

{{</tab>}}

{{<tab "NetQ CLI">}}

To view all LLDP alarms, run:

```
netq show events [level info | level error | level warning | level critical | level debug] type lldp [between <text-time> and <text-endtime>] [json]
```

Use the `level` option to set the severity of the events to show. Use the `between` option to show events within a given time range.

This example shows that no LLDP events have occurred in the last three days.

```
cumulus@switch:~$ netq show events type lldp between now and 3d
No matching event records found
```

{{</tab>}}

{{</tabs>}}

### View Details About All Switches Running LLDP

You can view attributes of all switches running LLDP in your network in the full-screen card.

To view all switch details, open the Network Services|All LLDP Sessions card, and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-allswitches-tab-241.png" width="700">}}

<div style="padding-left: 18px;">Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}} for more detail.</div>

Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View Details for All LLDP Sessions

You can view attributes of all LLDP sessions in your network with the NetQ UI or NetQ CLI.

{{<tabs "TabID766" >}}

{{<tab "NetQ UI" >}}

To view all session details:

1. Open the Network Services|All LLDP Sessions card.

2. Change to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

    {{<figure src="/images/netq/ntwk-svcs-all-lldp-fullscr-allsess-tab-320.png" width="700">}}

<div style="padding-left: 18px;">Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}} for more detail.</div>

Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view session details, run `netq show lldp`.

This example shows all current sessions (one per row) and the attributes associated with them.

```
cumulus@netq-ts:~$ netq show lldp

Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
border01          swp3                      fw1               swp1                      Mon Oct 26 04:13:29 2020
border01          swp49                     border02          swp49                     Mon Oct 26 04:13:29 2020
border01          swp51                     spine01           swp5                      Mon Oct 26 04:13:29 2020
border01          swp52                     spine02           swp5                      Mon Oct 26 04:13:29 2020
border01          eth0                      oob-mgmt-switch   swp20                     Mon Oct 26 04:13:29 2020
border01          swp53                     spine03           swp5                      Mon Oct 26 04:13:29 2020
border01          swp50                     border02          swp50                     Mon Oct 26 04:13:29 2020
border01          swp54                     spine04           swp5                      Mon Oct 26 04:13:29 2020
border02          swp49                     border01          swp49                     Mon Oct 26 04:13:11 2020
border02          swp3                      fw1               swp2                      Mon Oct 26 04:13:11 2020
border02          swp51                     spine01           swp6                      Mon Oct 26 04:13:11 2020
border02          swp54                     spine04           swp6                      Mon Oct 26 04:13:11 2020
border02          swp52                     spine02           swp6                      Mon Oct 26 04:13:11 2020
border02          eth0                      oob-mgmt-switch   swp21                     Mon Oct 26 04:13:11 2020
border02          swp53                     spine03           swp6                      Mon Oct 26 04:13:11 2020
border02          swp50                     border01          swp50                     Mon Oct 26 04:13:11 2020
fw1               eth0                      oob-mgmt-switch   swp18                     Mon Oct 26 04:38:03 2020
fw1               swp1                      border01          swp3                      Mon Oct 26 04:38:03 2020
fw1               swp2                      border02          swp3                      Mon Oct 26 04:38:03 2020
fw2               eth0                      oob-mgmt-switch   swp19                     Mon Oct 26 04:46:54 2020
leaf01            swp1                      server01          mac:44:38:39:00:00:32     Mon Oct 26 04:13:57 2020
leaf01            swp2                      server02          mac:44:38:39:00:00:34     Mon Oct 26 04:13:57 2020
leaf01            swp52                     spine02           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp49                     leaf02            swp49                     Mon Oct 26 04:13:57 2020
leaf01            eth0                      oob-mgmt-switch   swp10                     Mon Oct 26 04:13:57 2020
leaf01            swp3                      server03          mac:44:38:39:00:00:36     Mon Oct 26 04:13:57 2020
leaf01            swp53                     spine03           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp50                     leaf02            swp50                     Mon Oct 26 04:13:57 2020
leaf01            swp54                     spine04           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp51                     spine01           swp1                      Mon Oct 26 04:13:57 2020
leaf02            swp52                     spine02           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp54                     spine04           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp2                      server02          mac:44:38:39:00:00:3a     Mon Oct 26 04:14:57 2020
leaf02            swp3                      server03          mac:44:38:39:00:00:3c     Mon Oct 26 04:14:57 2020
...
```

{{</tab>}}

{{</tabs>}}

## Monitor a Single LLDP Session

With NetQ, you can monitor the number of nodes running the LLDP service, view neighbor state changes, and compare with events occurring at the same time, as well as monitor the running LLDP configuration and changes to the configuration file. For an overview and how to configure LLDP in your data center network, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-2/Link-Layer-Discovery-Protocol/" text="Link Layer Discovery Protocol">}}.

{{<notice note>}}

To access the single session cards, you must open the full-screen Network Services|All LLDP Sessions card, click the <strong>All Sessions</strong> tab, select the desired session, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}} (Open Card).

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

You can view information about a given LLDP session using the NetQ UI or NetQ CLI.

{{<tabs "TabID862" >}}

{{<tab "NetQ UI" >}}

A summary of the LLDP session is available from the Network Services|LLDP Session card workflow, showing the node and its peer and current status.

To view the summary:

1. Open the or add the Network Services|All LLDP Sessions card.

2. Change to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Locate the medium Network Services|LLDP Session card.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-medium-summary-highlight-230.png" width="200">}}

6. Optionally, open the small Network Services|LLDP Session card to keep track of the session health. 

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-small-230.png" width="200">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

Run the `netq show lldp` command with the `hostname` and `remote-physical-interface` options.

This example show the session information for the *leaf02* switch on *swp49* interface of the *leaf01* peer.

```
cumulus@switch:~$ netq leaf02 show lldp swp49
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
leaf02            swp49                     leaf01            swp49                     Mon Oct 26 04:14:57 2020
```

{{</tab>}}

{{</tabs>}}

### View LLDP Session Neighbor State Changes

You can view the neighbor state for a given LLDP session from the medium and large LLDP Session cards. For a given time period, you can determine the stability of the LLDP session between two devices. If you experienced connectivity issues at a particular time, you can use these cards to help verify the state of the neighbor. If the neighbor was not alive more than it was alive, you can then investigate further into possible causes.

To view the neighbor availability for a given LLDP session on the *medium* card:

1. Open the or add the Network Services|All LLDP Sessions card.

2. Change to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Locate the medium Network Services|LLDP Session card.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-medium-nbr-state-highlight-230.png" width="200">}}

    In this example, the heat map tells us that this LLDP session has been able to detect a neighbor for the entire time period.

    From this card, you can also view the host name and interface, and the peer name and interface.

To view the neighbor availability for a given LLDP session on the *large* LLDP Session card:

1. Open a Network Services|LLDP Session card.

2. Hover over the card, and change to the large card using the card size picker.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-large-nbr-state-highlight-320.png" width="500">}}

    From this card, you can also view the alarm and info event counts, host interface name, peer hostname, and peer interface identifying the session in more detail.

### View Changes to the LLDP Service Configuration File

Each time a change is made to the configuration file for the LLDP service, NetQ logs the change and enables you to compare it with the last version using the NetQ UI. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

To view the configuration file changes:

1. Open or add the Network Services|All LLDP Sessions card.

2. Switch to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Locate the medium Network Services|LLDP Session card.

6. Hover over the card, and change to the large card using the card size picker.

7. Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> to open the **LLDP Configuration File Evolution** tab.

8. Select the time of interest on the left; when a change may have impacted the performance. Scroll down if needed.

9. Choose between the **File** view and the **Diff** view (selected option is dark; File by default).

    The File view displays the content of the file for you to review.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-large-config-tab-file-selected-230.png" width="500">}}

    The Diff view displays the changes between this version (on left) and the most recent version (on right) side by side. The changes are highlighted in red and green. In this example, we don't have any changes to the file, so the same file is shown on both sides, and thus no highlighted lines.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-large-config-tab-diff-selected-230.png" width="500">}}

### View All LLDP Session Details

You can view attributes of all of the LLDP sessions for the devices participating in a given session with the NetQ UI and the NetQ CLI.

{{<tabs "TabID974" >}}

{{<tab "NetQ UI" >}}

To view all session details:

1. Open or add the Network Services|All LLDP Sessions card.

2. Switch to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Locate the medium Network Services|LLDP Session card.

6. Hover over the card, and change to the full-screen card using the card size picker. The **All LLDP Sessions** tab is displayed by default.

    {{<figure src="/images/netq/ntwk-svcs-single-lldp-fullscr-allsess-tab-241.png" width="700">}}

7. To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right of the card.

{{</tab>}}

{{<tab "NetQ CLI" >}}

Run the `netq show lldp` command.

This example shows all LLDP sessions in the last 24 hours.

```
cumulus@netq-ts:~$ netq show lldp

Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
border01          swp3                      fw1               swp1                      Mon Oct 26 04:13:29 2020
border01          swp49                     border02          swp49                     Mon Oct 26 04:13:29 2020
border01          swp51                     spine01           swp5                      Mon Oct 26 04:13:29 2020
border01          swp52                     spine02           swp5                      Mon Oct 26 04:13:29 2020
border01          eth0                      oob-mgmt-switch   swp20                     Mon Oct 26 04:13:29 2020
border01          swp53                     spine03           swp5                      Mon Oct 26 04:13:29 2020
border01          swp50                     border02          swp50                     Mon Oct 26 04:13:29 2020
border01          swp54                     spine04           swp5                      Mon Oct 26 04:13:29 2020
border02          swp49                     border01          swp49                     Mon Oct 26 04:13:11 2020
border02          swp3                      fw1               swp2                      Mon Oct 26 04:13:11 2020
border02          swp51                     spine01           swp6                      Mon Oct 26 04:13:11 2020
border02          swp54                     spine04           swp6                      Mon Oct 26 04:13:11 2020
border02          swp52                     spine02           swp6                      Mon Oct 26 04:13:11 2020
border02          eth0                      oob-mgmt-switch   swp21                     Mon Oct 26 04:13:11 2020
border02          swp53                     spine03           swp6                      Mon Oct 26 04:13:11 2020
border02          swp50                     border01          swp50                     Mon Oct 26 04:13:11 2020
fw1               eth0                      oob-mgmt-switch   swp18                     Mon Oct 26 04:38:03 2020
fw1               swp1                      border01          swp3                      Mon Oct 26 04:38:03 2020
fw1               swp2                      border02          swp3                      Mon Oct 26 04:38:03 2020
fw2               eth0                      oob-mgmt-switch   swp19                     Mon Oct 26 04:46:54 2020
leaf01            swp1                      server01          mac:44:38:39:00:00:32     Mon Oct 26 04:13:57 2020
leaf01            swp2                      server02          mac:44:38:39:00:00:34     Mon Oct 26 04:13:57 2020
leaf01            swp52                     spine02           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp49                     leaf02            swp49                     Mon Oct 26 04:13:57 2020
leaf01            eth0                      oob-mgmt-switch   swp10                     Mon Oct 26 04:13:57 2020
leaf01            swp3                      server03          mac:44:38:39:00:00:36     Mon Oct 26 04:13:57 2020
leaf01            swp53                     spine03           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp50                     leaf02            swp50                     Mon Oct 26 04:13:57 2020
leaf01            swp54                     spine04           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp51                     spine01           swp1                      Mon Oct 26 04:13:57 2020
leaf02            swp52                     spine02           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp54                     spine04           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp2                      server02          mac:44:38:39:00:00:3a     Mon Oct 26 04:14:57 2020
leaf02            swp3                      server03          mac:44:38:39:00:00:3c     Mon Oct 26 04:14:57 2020
leaf02            swp53                     spine03           swp2                      Mon Oct 26 04:14:57 2020
leaf02            swp50                     leaf01            swp50                     Mon Oct 26 04:14:57 2020
leaf02            swp51                     spine01           swp2                      Mon Oct 26 04:14:57 2020
leaf02            eth0                      oob-mgmt-switch   swp11                     Mon Oct 26 04:14:57 2020
leaf02            swp49                     leaf01            swp49                     Mon Oct 26 04:14:57 2020
leaf02            swp1                      server01          mac:44:38:39:00:00:38     Mon Oct 26 04:14:57 2020
leaf03            swp2                      server05          mac:44:38:39:00:00:40     Mon Oct 26 04:16:09 2020
leaf03            swp49                     leaf04            swp49                     Mon Oct 26 04:16:09 2020
leaf03            swp51                     spine01           swp3                      Mon Oct 26 04:16:09 2020
leaf03            swp50                     leaf04            swp50                     Mon Oct 26 04:16:09 2020
leaf03            swp54                     spine04           swp3                      Mon Oct 26 04:16:09 2020
...
spine04           swp3                      leaf03            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp2                      leaf02            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp4                      leaf04            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp1                      leaf01            swp54                     Mon Oct 26 04:11:23 2020
spine04           swp5                      border01          swp54                     Mon Oct 26 04:11:23 2020
spine04           swp6                      border02          swp54                     Mon Oct 26 04:11:23 2020
```

{{</tab>}}

{{</tabs>}}

### View All Events for a Given LLDP Session

You can view all alarm and info events for the devices participating in a given session with the NetQ UI.

To view all events:

1. Open or add the Network Services|All LLDP Sessions card.

2. Switch to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Locate the medium Network Services|LLDP Session card.

6. Hover over the card, and change to the full-screen card using the card size picker.

7. Click the **All Events** tab.

{{<figure src="/images/netq/ntwk-svcs-single-lldp-fullscr-events-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Sort on other parameters:
  - By **Message** to determine the frequency of particular events.
  - By **Severity** to determine the most critical events.
  - By **Time** to find events that may have occurred at a particular time to try to correlate them with other system events.
- Export data to a file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.
