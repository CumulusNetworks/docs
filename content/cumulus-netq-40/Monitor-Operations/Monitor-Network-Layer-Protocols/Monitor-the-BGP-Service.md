---
title: Monitor the BGP Service
author: NVIDIA
weight: 950
toc: 4
---
BGP is the routing protocol that runs the Internet. It is an increasingly popular protocol for use in the data center as it lends itself well to the rich interconnections in a Clos topology. Specifically, BGP:

- Does not require the routing state to be periodically refreshed, unlike OSPF.
- Is less chatty than its link-state siblings. For example, a link or node transition can result in a bestpath change, causing BGP to send updates.
- Is multi-protocol and extensible.
- Has many robust vendor implementations.
- Is very mature as a protocol and comes with many years of operational experience.

{{<exlink url="https://tools.ietf.org/html/rfc7938" text="RFC 7938">}} provides further details of the use of BGP within the data center. For an overview and how to configure BGP to run in your data center network, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Border-Gateway-Protocol-BGP/" text="Border Gateway Protocol - BGP">}}.

NetQ enables operators to view the health of the BGP service on a networkwide or per session basis, giving greater insight into all aspects of the service. This is accomplished in the NetQ UI through two card workflows, one for the service and one for the session and in the NetQ CLI with the `netq show bgp` command.

## Monitor the BGP Service Networkwide

With NetQ, you can monitor BGP performance across the network:

- Network Services|All BGP Sessions
    - Small: view number of nodes running BGP service and distribution and number of alarms
    - Medium: view number and distribution of nodes running BGP service, alarms, and with unestablished sessions
    - Large: view number and distribution of nodes running BGP service and those with unestablished sessions, and view nodes with the most established and unestablished BGP sessions
    - Full-screen: view all switches, all sessions, and all alarms
- `netq show evpn` command: view associated neighbors, ASN (autonomous system number), peer ASN, receive IP or EVPN address prefixes, and VRF assignment for each node

{{<notice note>}}
When entering a time value in the <code>netq show evpn</code> command, you must include a numeric value <em>and</em> the unit of measure:
<ul>
<li><strong>w</strong>: weeks</li>
<li><strong>d</strong>: days</li>
<li><strong>h</strong>: hours</li>
<li><strong>m</strong>: minutes</li>
<li><strong>s</strong>: seconds</li>
<li><strong>now</strong>
</ul>

<p>When using the <code>between</code> option, the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p>
{{</notice>}}

### View Service Status Summary

You can view a summary of BGP service with the NetQ UI or the NetQ CLI.

{{<tabs "TabID48" >}}

{{<tab "NetQ UI" >}}

To view the summary, open the small Network Services|All BGP Sessions card.

{{<figure src="/images/netq/ntwk-svcs-all-bgp-small-300.png" width="200" >}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view the summary, run `netq show bgp`.

This example shows each node, their neighbor, VRF, ASN, peer ASN, received address IPv4/IPv6/EVPN prefix, and last time this was changed.

```
cumulus@switch:~$ netq show bgp
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
border01          peerlink.4094(border02)      default         65132      65132      12/-/-       Fri Oct  2 22:39:00 2020
border01          swp52(spine02)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp51(spine01)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp53(spine03)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp54(spine04)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          peerlink.4094(border01)      default         65132      65132      12/-/-       Fri Oct  2 22:39:00 2020
border02          swp51(spine01)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp53(spine03)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp52(spine02)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp54(spine04)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
leaf01            swp54(spine04)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            swp53(spine03)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            peerlink.4094(leaf02)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf01            swp52(spine02)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp53(spine03)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp54(spine04)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp52(spine02)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            peerlink.4094(leaf01)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf03            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp52(spine02)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp53(spine03)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp54(spine04)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            peerlink.4094(leaf04)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp54(spine04)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp53(spine03)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            peerlink.4094(leaf03)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp52(spine02)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
spine01           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine01           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine03           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine03           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine04           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine04           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
```

{{</tab>}}

{{</tabs>}}

### View the Distribution of Sessions and Alarms

It is useful to know the number of network nodes running the BGP protocol over a period of time, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol.

It is also useful to compare the number of nodes running BGP with unestablished sessions with the alarms present at the same time to determine if there is any correlation between the issues and the ability to establish a BGP session. This is visible with the NetQ UI.

{{<tabs "TabID135" >}}

{{<tab "NetQ UI" >}}

To view these distributions, open the medium Network Services|All BGP Sessions card.

{{<figure src="/images/netq/ntwk-svcs-all-bgp-medium-300.png" width="200" >}}

In this example, we see that 10 nodes are running the BGP protocol, there are no nodes with unestablished sessions, and that 54 LLDP-related alarms have occurred in the last 24 hours. If a visual correlation between the alarms and unestablished sessions is apparent, you can dig a little deeper with the large Network Services|All BGP Sessions card.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view the number of switches running the BGP service, run:

```
netq show bgp
```

Count the switches in the output.

This example shows two border switches, four leaf switches, and four spine switches are running the BGP service, for a total of 10.

```
cumulus@switch:~$ netq show bgp
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
border01          peerlink.4094(border02)      default         65132      65132      12/-/-       Fri Oct  2 22:39:00 2020
border01          swp52(spine02)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp51(spine01)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp53(spine03)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp54(spine04)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          peerlink.4094(border01)      default         65132      65132      12/-/-       Fri Oct  2 22:39:00 2020
border02          swp51(spine01)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp53(spine03)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp52(spine02)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp54(spine04)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
leaf01            swp54(spine04)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            swp53(spine03)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            peerlink.4094(leaf02)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf01            swp52(spine02)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp53(spine03)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp54(spine04)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp52(spine02)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            peerlink.4094(leaf01)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf03            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp52(spine02)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp53(spine03)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp54(spine04)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            peerlink.4094(leaf04)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp54(spine04)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp53(spine03)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            peerlink.4094(leaf03)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp52(spine02)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
spine01           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine01           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine03           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine03           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine04           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine04           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
```

{{</tab>}}

{{</tabs>}}

### View Devices with the Most BGP Sessions

You can view the load from BGP on your switches and hosts using the large Network Services|All BGP Sessions card or the NetQ CLI. This data enables you to see which switches are handling the most BGP sessions currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

{{<tabs "TabID228" >}}

{{<tab "NetQ UI" >}}

To view switches and hosts with the most BGP sessions:

1. Open the large Network Services|ALL BGP Sessions card.

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

<div style="padding-left: 18px;">You can now see whether there are significant differences between this time and the original time. If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running BGP than previously, looking for changes in the topology, and so forth.</div>

{{</tab>}}

{{<tab "NetQ CLI" >}}

To determine the devices with the most sessions, run `netq show bgp`. Then count the sessions on each device.

In this example, border01-02 and leaf01-04 each have four sessions. The spine01-04 switches each have five sessions. Therefore the spine switches have the most sessions.

```
cumulus@switch:~$ netq show bgp
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
border01          peerlink.4094(border02)      default         65132      65132      12/-/-       Fri Oct  2 22:39:00 2020
border01          swp52(spine02)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp51(spine01)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp53(spine03)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp54(spine04)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          peerlink.4094(border01)      default         65132      65132      12/-/-       Fri Oct  2 22:39:00 2020
border02          swp51(spine01)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp53(spine03)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp52(spine02)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp54(spine04)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
leaf01            swp54(spine04)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            swp53(spine03)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            peerlink.4094(leaf02)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf01            swp52(spine02)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp53(spine03)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp54(spine04)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp52(spine02)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            peerlink.4094(leaf01)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf03            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp52(spine02)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp53(spine03)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp54(spine04)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            peerlink.4094(leaf04)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp54(spine04)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp53(spine03)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            peerlink.4094(leaf03)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp52(spine02)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
spine01           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine01           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine03           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine03           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine04           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine04           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
```

{{</tab>}}

{{</tabs>}}

### View Devices with the Most Unestablished BGP Sessions

You can identify switches and hosts that are experiencing difficulties establishing BGP sessions; both currently and in the past, using the NetQ UI.

To view switches with the most unestablished BGP sessions:

1. Open the large Network Services|All BGP Sessions card.

2. Select **Switches with Most Unestablished Sessions** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes with the most unestablished BGP sessions at the top. Scroll down to view those with the fewest unestablished sessions.

    {{<figure src="/images/netq/ntwk-svcs-allbgp-large-unestab-sessions-300.png" width="500">}}

Where to go next depends on what data you see, but a couple of options
include:

- Change the time period for the data to compare with a prior time.

    If the same switches are consistently indicating the most unestablished sessions, you might want to look more carefully at those switches using the Switches card workflow to determine probable causes. Refer to {{<link title="Monitor Switch Performance">}}.

- Click **Show All Sessions** to investigate all BGP sessions with events in the full screen card.

### View BGP Configuration Information for a Given Device

You can view the BGP configuration information for a given device from the NetQ UI or the NetQ CLI.

{{<tabs "TabID358" >}}

{{<tab "NetQ UI" >}}

1. Open the full-screen Network Services|All BGP Sessions card.

2. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} to filter by hostname.

3. Click **Apply**.

    {{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-allsess-tab-filterbyHn-320.png" width="500">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

Run the `netq show bgp` command with the `hostname` option.

This example shows the BGP configuration information for the spine02
switch. The switch is peered with swp1 on leaf01, swp2 on leaf02, and so
on. Spine02 has an ASN of 65199 and each of the peers have unique ASNs.

```
cumulus@switch:~$ netq spine02 show bgp
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
spine02           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020

```

{{</tab>}}

{{</tabs>}}

### View BGP Configuration Information for a Given ASN

You can view the BGP configuration information for a given ASN from the NetQ UI or the NetQ CLI.

{{<tabs "TabID402" >}}

{{<tab "NetQ UI" >}}

1. Open the full-screen Network Services|All BGP Sessions card.

2. Locate the **ASN** column.

    {{<notice tip>}}
You may want to pause the auto-refresh feature during this process to avoid the page update while you are browsing the data.
    {{</notice>}}

3. Click the header to sort on that column.

4. Scroll down as needed to find the devices using the ASN of interest.

    {{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-allsess-tab-filterbyASN-320.png" width="700">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

Run the `netq show bgp` command with the `asn <number-asn>` option.

This example shows the BGP configuration information for ASN of
*65102*. This ASN is associated with leaf02-leaf04 and so the results show
the BGP neighbors for those switches.

```
cumulus@switch:~$ netq show bgp asn 65102
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
leaf03            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp52(spine02)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp53(spine03)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp54(spine04)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            peerlink.4094(leaf04)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp54(spine04)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp53(spine03)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            peerlink.4094(leaf03)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp52(spine02)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
```

{{</tab>}}

{{</tabs>}}

<!-- vale off -->
### View Devices with the Most BGP-related Alarms
<!-- vale on -->

Switches or hosts experiencing a large number of BGP alarms may indicate a configuration or performance issue that needs further investigation. You can view this information using the NetQ UI or NetQ CLI.

{{<tabs "TabID455" >}}

{{<tab "NetQ UI" >}}

With the NetQ UI, you can view the devices sorted by the number of BGP alarms and then use the Switches card workflow or the Events|Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with the most BGP alarms:

1. Open the large Network Services|All BGP Sessions card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Switches with Most Alarms** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes with the most BGP alarms at the top. Scroll down to view those with the fewest alarms.

    {{<figure src="/images/netq/ntwk-svcs-all-bgp-large-alarms-tab-300.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.

- Click **Show All Sessions** to investigate all BGP sessions with events in the full-screen card.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view the switches and hosts with the most BGP alarms and informational events, run the `netq show events` command with the `type` option set to *bgp*, and optionally the `between` option set to display the events within a given time range. Count the events associated with each switch.

This example shows all BGP events between now and five days ago.

```
cumulus@switch:~$ netq show events type bgp between now and 5d
Matching bgp records:
Hostname          Message Type Severity Message                             Timestamp
----------------- ------------ -------- ----------------------------------- -------------------------
leaf01            bgp          info     BGP session with peer spine01 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine02 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine03 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine01 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine03 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine02 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine03 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine02 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine01 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
...
```

{{</tab>}}

{{</tabs>}}

### View All BGP Events

The Network Services|All BGP Sessions card workflow and the `netq show events type bgp` command enable you to view all BGP events in a designated time period.

{{<tabs "TabID436" >}}

{{<tab "NetQ UI" >}}

To view all BGP events:

1. Open the full-screen Network Services|All BGP Sessions card.

2. Click **All Alarms** tab in the navigation panel.  

    By default, events are listed in most recent to least recent order.

    {{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-alarms-tab-300.png" width="700">}}

Where to go next depends on what data you see, but a couple of options include:

- Sort on various parameters:
    - by **Message** to determine the frequency of particular events
    - by **Severity** to determine the most critical events
    - by **Time** to find events that may have occurred at a particular time to try to correlate them with other system events
- Open one of the other full screen tabs in this flow to focus on devices or sessions
- Export the data for use in another analytics tool, by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> and providing a name for the data file.

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all BGP alarms, run:

```
netq show events [level info | level error | level warning | level critical | level debug] type bgp [between <text-time> and <text-endtime>] [json]
```

Use the `level` option to set the severity of the events to show. Use the `between` option to show events within a given time range.

This example shows informational BGP events in the past five days.

```
cumulus@switch:~$ netq show events type bgp between now and 5d
Matching bgp records:
Hostname          Message Type Severity Message                             Timestamp
----------------- ------------ -------- ----------------------------------- -------------------------
leaf01            bgp          info     BGP session with peer spine01 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine02 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine03 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine01 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine03 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine02 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine03 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine02 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
leaf01            bgp          info     BGP session with peer spine01 @desc 2h:10m:11s
                                        : state changed from failed to esta
                                        blished
...
```

{{</tab>}}

{{</tabs>}}

### View Details for All Devices Running BGP

You can view all stored attributes of all switches and hosts running BGP in your network in the full-screen Network Services|All BGP Sessions card in the NetQ UI.

To view all device details, open the full-screen Network Services|All BGP Sessions card and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-allsw-tab-300.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View Details for All BGP Sessions

You can view attributes of all BGP sessions in your network with the NetQ UI or NetQ CLI.

{{<tabs "TabID526" >}}

{{<tab "NetQ UI" >}}

To view all session details, open the full-screen Network Services|All BGP Sessions card and click the **All Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-all-bgp-fullscr-allsess-tab-300.png" width="700">}}

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}} for more detail.

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view session details, run `netq show bgp`.

This example shows all current sessions (one per row) and the attributes associated with them.

```
cumulus@switch:~$ netq show bgp
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
border01          peerlink.4094(border02)      default         65132      65132      12/-/-       Fri Oct  2 22:39:00 2020
border01          swp52(spine02)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp51(spine01)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp53(spine03)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border01          swp54(spine04)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          peerlink.4094(border01)      default         65132      65132      12/-/-       Fri Oct  2 22:39:00 2020
border02          swp51(spine01)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp53(spine03)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp52(spine02)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp54(spine04)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
leaf01            swp54(spine04)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            swp53(spine03)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf01            peerlink.4094(leaf02)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf01            swp52(spine02)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp53(spine03)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp54(spine04)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp52(spine02)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            peerlink.4094(leaf01)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf03            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp52(spine02)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp53(spine03)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp54(spine04)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            peerlink.4094(leaf04)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp54(spine04)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp53(spine03)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            peerlink.4094(leaf03)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp52(spine02)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
spine01           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine01           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine03           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine03           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine04           swp1(leaf01)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine04           swp3(leaf03)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
```

{{</tab>}}

{{</tabs>}}

## Monitor a Single BGP Session

With NetQ, you can monitor a single session of the BGP service, view session state changes, and compare with alarms occurring at the same time, as well as monitor the running BGP configuration and changes to the configuration file. For an overview and how to configure BGP to run in your data center network, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Border-Gateway-Protocol-BGP/" text="Border Gateway Protocol - BGP">}}.

{{<notice note>}}
To access the single session cards, you must open the full-screen Network Services|All BGP Sessions card, click the <strong>All Sessions</strong> tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18"/> (Open Card).
{{</notice>}}

{{%notice info%}}

To open the BGP single session card, verify that both the peer hostname and peer ASN are valid. This ensures the information presented is reliable.

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

You can view information about a given BGP session using the NetQ UI or NetQ CLI.

{{<tabs "TabID737" >}}

{{<tab "NetQ UI" >}}

A summary of a BGP session is available from the Network Services|BGP Session card workflow, showing the node and its peer and current status.

To view the summary:

1. Open or add the Network Services|All BGP Sessions card.

2. Switch to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Locate the medium Network Services|BGP Session card.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-medium-session-status-highlight-230.png" width="200">}}

6. Optionally, switch to the small Network Services|BGP Session card.  

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-small-230.png" width="200">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

Run the `netq show bgp` command with the `bgp-session` option.

This example first shows the available sessions, then the information for the BGP session on *swp51* of *spine01*.

```
cumulus@switch~$ netq show bgp <tab>
    around         :  Go back in time to around ...
    asn            :  BGP Autonomous System Number (ASN)
    json           :  Provide output in JSON
    peerlink.4094  :  peerlink.4094
    swp1           :  swp1
    swp2           :  swp2
    swp3           :  swp3
    swp4           :  swp4
    swp5           :  swp5
    swp6           :  swp6
    swp51          :  swp51
    swp52          :  swp52
    swp53          :  swp53
    swp54          :  swp54
    vrf            :  VRF
    <ENTER>

cumulus@switch:~$ netq show bgp swp51
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
border01          swp51(spine01)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
border02          swp51(spine01)               default         65132      65199      7/-/72       Fri Oct  2 22:39:00 2020
leaf01            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf04            swp51(spine01)               default         65102      65199      7/-/36       Fri Oct  2 22:39:00 2020
```

{{</tab>}}

{{</tabs>}}

### View BGP Session State Changes

You can view the state of a given BGP session from the medium and large Network Service|All BGP Sessions card in the NetQ UI. For a given time period, you can determine the stability of the BGP session between two devices. If you experienced connectivity issues at a particular time, you can use these cards to help verify the state of the session. If it was not established more than it was established, you can then investigate further into possible causes.

To view the state transitions for a given BGP session, on the *medium* BGP Session card:

1. Open or add the Network Services|All BGP Sessions card.

2. Switch to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Locate the medium Network Services|BGP Session card.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-medium-session-status-highlight-230.png" width="200">}}

    The heat map indicates the status of the session over the designated time period. In this example, the session has been established for the entire time period.

    From this card, you can also view the Peer ASN, name, hostname and router id identifying the session in more detail.

To view the state transitions for a given BGP session on the *large* BGP Session card:

1. Open a Network Services|BGP Session card.

2. Hover over the card, and change to the large card using the card size picker.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-large-session-status-highlight-320.png" width="500">}}

    From this card, you can view the alarm and info event counts, Peer ASN, hostname, and router id, VRF, and Tx/Rx families identifying the session in more detail. The Connection Drop Count gives you a sense of the session performance.

### View Changes to the BGP Service Configuration File

Each time a change is made to the configuration file for the BGP service, NetQ logs the change and enables you to compare it with the last version using the NetQ UI. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

To view the configuration file changes:

1. Open or add the Network Services|All BGP Sessions card.

2. Switch to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Locate the medium Network Services|BGP Session card.

6. Hover over the card, and change to the large card using the card size picker.

7. Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> to open the **BGP Configuration File Evolution** tab.

8. Select the time of interest on the left; when a change may have impacted the performance. Scroll down if needed.

9. Choose between the **File** view and the **Diff** view (selected option is dark; File by default).

    The File view displays the content of the file for you to review.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-large-config-tab-file-selected-230.png" width="500">}}

    The Diff view displays the changes between this version (on left) and the most recent version (on right) side by side. The changes are highlighted, as seen in this example.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-large-config-tab-diff-selected-230.png" width="500">}}

### View All BGP Session Details

You can view attributes of all of the BGP sessions for the devices participating in a given session with the NetQ UI and the NetQ CLI.

{{<tabs "TabID873" >}}

{{<tab "NetQ UI" >}}

To view all session details:

1. Open or add the Network Services|All BGP Sessions card.

2. Switch to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Locate the medium Network Services|BGP Session card.

6. Hover over the card, and change to the full-screen card using the card size picker.

    {{<figure src="/images/netq/ntwk-svcs-single-bgp-fullscr-allsess-tab-320.png" width="700">}}

7. To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

{{</tab>}}

{{<tab "NetQ CLI" >}}

Run the `netq show bgp` command with the `bgp-session` option.

This example shows all BGP sessions associated with *swp4*.

```
cumulus@switch:~$ netq show bgp swp4
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
spine01           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp4(leaf04)                 default         65199      65102      3/-/18       Fri Oct  2 22:39:00 2020
```

{{</tab>}}

{{</tabs>}}

### View All Events for a Given BGP Session

You can view all alarm and info events for the devices participating in a given session with the NetQ UI.

To view all events:

1. Open or add the Network Services|All BGP Sessions card.

2. Switch to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

5. Locate the medium Network Services|BGP Session card.

6. Hover over the card, and change to the full-screen card using the card size picker.

7. Click the **All Events** tab.

    {{<figure src="/images/netq/ntwk-svcs-fullscr-events-tab-320.png" width="700">}}

8. To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.
