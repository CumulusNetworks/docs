---
title: Monitor the EVPN Service
author: NVIDIA
weight: 980
toc: 4
---
EVPN (Ethernet Virtual Private Network) enables network administrators in the data center to deploy a virtual layer 2 bridge overlay on top of a layer 3 IP network, creating access, or a tunnel, between two locations. This connects devices in different layer 2 domains or sites running VXLANs and their associated underlays. For an overview and how to configure EVPN in your data center network, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/" text="Ethernet Virtual Private Network-EVPN">}}.

NetQ enables operators to view the health of the EVPN service on a networkwide and a per session basis, giving greater insight into all aspects of the service. This is accomplished through two card workflows, one for the service and one for the session, and in the NetQ CLI with the `netq show evpn` command.

## Monitor the EVPN Service Networkwide

With NetQ, you can monitor EVPN performance across the network:

- Network Services|All EVPN Sessions
    - Small: view number of nodes running EVPN service and number of alarms
    - Medium: view number of nodes running EVPN service, number of sessions, and number of alarms
    - Large: view number of nodes running EVPN service, number of sessions, number of VNIs, switches with the most sessions, and alarms
    - Full-screen: view all switches, all sessions, and all alarms
- `netq show evpn` command: view configuration and status for all devices, including associated VNI, VTEP address, import and export route (showing BGP ASN and VNI path), and last time a change was made for each device running EVPN

{{%notice note%}}

When entering a time value in the `netq show evpn` command, you must include a numeric value *and* the unit of measure:

- **w**: weeks
- **d**: days
- **h**: hours
- **m**: minutes
- **s**: seconds
- **now**

When using the `between` option, the start time (`text-time`) and end time (`text-endtime`) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.

{{%/notice%}}

### View the EVPN Service Status

You can view the configuration and status of your EVPN overlay across your network or for a particular device from the NetQ UI or the NetQ CLI. The example below shows the configuration and status for all devices, including the associated VNI, VTEP address, the import and export route (showing the BGP ASN and VNI path), and the last time a change was made for each device running EVPN. Use the `hostname` option to view the configuration and status for a single device.

{{<tabs "EVPN summary">}}

{{<tab "NetQ UI">}}

Open the small Network Services|All EVPN Sessions card. In this example, the number of devices running the EVPN service is six (6) and the number and distribution of related critical severity alarms is zero (0).

{{<figure src="/images/netq/ntwk-svcs-all-evpn-small-230.png" width="200" >}}

{{</tab>}}

{{<tab "NetQ CLI">}}

To view EVPN service status, run `netq show evpn`.

This example shows the Cumulus reference topology, where EVPN runs on all border and leaf switches. Each session is represented by a single row.

```
cumulus@switch:~$ netq show evpn
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:49:27 2020
border01          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:49:27 2020
border02          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:48:47 2020
border02          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:48:47 2020
leaf01            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:49:30 2020
leaf01            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:49:30 2020
leaf01            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:49:30 2020
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:49:30 2020
leaf01            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:49:30 2020
leaf02            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:48:25 2020
leaf02            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:48:25 2020
leaf02            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:48:25 2020
leaf02            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:48:25 2020
leaf02            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:48:25 2020
leaf03            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:13 2020
leaf03            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:13 2020
leaf03            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:13 2020
leaf03            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:13 2020
leaf03            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:13 2020
leaf04            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:09 2020
leaf04            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:09 2020
leaf04            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:09 2020
leaf04            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:09 2020
leaf04            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:09 2020
```

{{</tab>}}

{{</tabs>}}

### View the Distribution of Sessions and Alarms

It is useful to know the number of network nodes running the EVPN protocol over a period of time, as it gives you insight into the amount of traffic associated with and breadth of use of the protocol.

It is also useful to compare the number of nodes running EVPN with the alarms present at the same time to determine if there is any correlation between the issues and the ability to establish an EVPN session. This is visible with the NetQ UI.

{{<tabs "TabID62" >}}

{{<tab "NetQ UI" >}}

Open the medium Network Services|All EVPN Sessions card. In this example there are no alarms, but there are three (3) VNIs.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-medium-230.png" width="200">}}

If a visual correlation is apparent, you can dig a little deeper with the large card tabs.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view the number of switches running the EVPN service, run:

```
netq show evpn
```

Count the switches in the output.

This example shows two border switches and four leaf switches are running the EVPN service, for a total of six (6).

```
cumulus@switch:~$ netq show evpn
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:49:27 2020
border01          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:49:27 2020
border02          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:48:47 2020
border02          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:48:47 2020
leaf01            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:49:30 2020
leaf01            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:49:30 2020
leaf01            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:49:30 2020
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:49:30 2020
leaf01            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:49:30 2020
leaf02            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:48:25 2020
leaf02            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:48:25 2020
leaf02            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:48:25 2020
leaf02            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:48:25 2020
leaf02            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:48:25 2020
leaf03            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:13 2020
leaf03            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:13 2020
leaf03            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:13 2020
leaf03            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:13 2020
leaf03            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:13 2020
leaf04            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:09 2020
leaf04            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:09 2020
leaf04            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:09 2020
leaf04            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:09 2020
leaf04            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:09 2020
```

To compare this count with the count at another time, run the `netq show evpn` command with the `around` option. Count the devices running EVPN at that time. Repeat with another time to collect a picture of changes over time.

{{</tab>}}

{{</tabs>}}

### View the Distribution of Layer 3 VNIs

It is useful to know the number sessions between devices and VNIs that are occurring over layer 3, as it gives you insight into the complexity of the VXLAN.

{{<tabs "TabID150" >}}

{{<tab "NetQ UI" >}}

To view this distribution, open the large Network Services|All EVPN Services card and view the bottom chart on the left. In this example, there are 12 layer 3 EVPN sessions running on the three VNIs.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-vni-chart-300.png" width="500">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view the distribution of switches running layer 3 VNIs, run:

```
netq show evpn
```

Count the switches using layer 3 VNIs (shown in the VNI and Type columns). Compare that to the total number of VNIs (count these from the VNI column) to determine the ratio of layer 3 versus the total VNIs.

This example shows two (2) layer 3 VNIs (4001 and 4002) and a total of five (5) VNIs (4001, 4002, 10, 20, 30). This then gives a distribution of 2/5 of the total, or 40%.

```
cumulus@switch:~$ netq show evpn
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:49:27 2020
border01          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:49:27 2020
border02          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:48:47 2020
border02          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:48:47 2020
leaf01            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:49:30 2020
leaf01            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:49:30 2020
leaf01            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:49:30 2020
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:49:30 2020
leaf01            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:49:30 2020
leaf02            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:48:25 2020
leaf02            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:48:25 2020
leaf02            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:48:25 2020
leaf02            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:48:25 2020
leaf02            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:48:25 2020
leaf03            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:13 2020
leaf03            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:13 2020
leaf03            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:13 2020
leaf03            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:13 2020
leaf03            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:13 2020
leaf04            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:09 2020
leaf04            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:09 2020
leaf04            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:09 2020
leaf04            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:09 2020
leaf04            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:09 2020
```

{{</tab>}}

{{</tabs>}}

### View Devices with the Most EVPN Sessions

You can view the load from EVPN on your switches and hosts using the large Network Services|All EVPN Sessions card or the NetQ CLI. This data enables you to see which switches are handling the most EVPN traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

{{<tabs "TabID211" >}}

{{<tab "NetQ UI" >}}

To view switches and hosts with the most EVPN sessions:

1. Open the large Network Services|All EVPN Sessions card.

2. Select **Top Switches with Most Sessions** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes running the most EVPN sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-top-sessions-300.png" width="500">}}

To compare this data with the same data at a previous time:

1. Open another large Network Services|All EVPN Sessions card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the current time.  

    You can now see whether there are significant differences between this time period and the previous time period.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-past-week-230.png" width="500" >}}

You can now see whether there are significant differences between this time and the original time. If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running EVPN than previously, looking for changes in the topology, and so forth.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To determine the devices with the most sessions, run `netq show evpn`. Then count the sessions on each device.

In this example, border01 and border02 each have 2 sessions. The leaf01-04 switches each have 5 sessions. Therefore the leaf switches have the most sessions.

```
cumulus@switch:~$ netq show evpn
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:49:27 2020
border01          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:49:27 2020
border02          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:48:47 2020
border02          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:48:47 2020
leaf01            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:49:30 2020
leaf01            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:49:30 2020
leaf01            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:49:30 2020
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:49:30 2020
leaf01            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:49:30 2020
leaf02            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:48:25 2020
leaf02            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:48:25 2020
leaf02            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:48:25 2020
leaf02            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:48:25 2020
leaf02            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:48:25 2020
leaf03            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:13 2020
leaf03            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:13 2020
leaf03            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:13 2020
leaf03            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:13 2020
leaf03            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:13 2020
leaf04            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:09 2020
leaf04            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:09 2020
leaf04            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:09 2020
leaf04            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:09 2020
leaf04            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:09 2020
```

To compare this with a time in the past, run `netq show evpn `.

In this example, there are significant changes from the output above, indicating a significant reconfiguration.

```
cumulus@netq-ts:~$ netq show evpn around 14d
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          3004001    10.0.1.254       L3               -              no        65254:3004001    65254:3004001    Mon Sep 28 11:00:44 2020
border01          30030      10.0.1.254       L2               -              no        65254:30030      65254:30030      Mon Sep 28 11:00:44 2020
border01          30020      10.0.1.254       L2               -              no        65254:30020      65254:30020      Mon Sep 28 11:00:44 2020
border01          3004002    10.0.1.254       L3               -              no        65254:3004002    65254:3004002    Mon Sep 28 11:00:44 2020
border01          30010      10.0.1.254       L2               -              no        65254:30010      65254:30010      Mon Sep 28 11:00:44 2020
border02          30030      10.0.1.254       L2               -              no        65254:30030      65254:30030      Mon Sep 28 11:00:32 2020
border02          3004001    10.0.1.254       L3               -              no        65254:3004001    65254:3004001    Mon Sep 28 11:00:32 2020
border02          30010      10.0.1.254       L2               -              no        65254:30010      65254:30010      Mon Sep 28 11:00:32 2020
border02          30020      10.0.1.254       L2               -              no        65254:30020      65254:30020      Mon Sep 28 11:00:32 2020
border02          3004002    10.0.1.254       L3               -              no        65254:3004002    65254:3004002    Mon Sep 28 11:00:32 2020
leaf01            30030      10.0.1.1         L2               -              no        65101:30030      65101:30030      Mon Sep 28 10:57:33 2020
leaf01            3004001    10.0.1.1         L3               -              no        65101:3004001    65101:3004001    Mon Sep 28 10:57:33 2020
leaf01            30010      10.0.1.1         L2               -              no        65101:30010      65101:30010      Mon Sep 28 10:57:33 2020
leaf01            3004002    10.0.1.1         L3               -              no        65101:3004002    65101:3004002    Mon Sep 28 10:57:33 2020
leaf01            30020      10.0.1.1         L2               -              no        65101:30020      65101:30020      Mon Sep 28 10:57:33 2020
leaf02            30010      10.0.1.1         L2               -              no        65101:30010      65101:30010      Mon Sep 28 11:00:14 2020
leaf02            30030      10.0.1.1         L2               -              no        65101:30030      65101:30030      Mon Sep 28 11:00:14 2020
leaf02            3004001    10.0.1.1         L3               -              no        65101:3004001    65101:3004001    Mon Sep 28 11:00:14 2020
leaf02            30020      10.0.1.1         L2               -              no        65101:30020      65101:30020      Mon Sep 28 11:00:14 2020
leaf02            3004002    10.0.1.1         L3               -              no        65101:3004002    65101:3004002    Mon Sep 28 11:00:14 2020
leaf03            30010      10.0.1.2         L2               -              no        65102:30010      65102:30010      Mon Sep 28 11:04:47 2020
leaf03            30030      10.0.1.2         L2               -              no        65102:30030      65102:30030      Mon Sep 28 11:04:47 2020
leaf03            30020      10.0.1.2         L2               -              no        65102:30020      65102:30020      Mon Sep 28 11:04:47 2020
leaf03            3004001    10.0.1.2         L3               -              no        65102:3004001    65102:3004001    Mon Sep 28 11:04:47 2020
leaf03            3004002    10.0.1.2         L3               -              no        65102:3004002    65102:3004002    Mon Sep 28 11:04:47 2020
leaf04            30020      10.0.1.2         L2               -              no        65102:30020      65102:30020      Mon Sep 28 11:00:59 2020
leaf04            3004001    10.0.1.2         L3               -              no        65102:3004001    65102:3004001    Mon Sep 28 11:00:59 2020
leaf04            30030      10.0.1.2         L2               -              no        65102:30030      65102:30030      Mon Sep 28 11:00:59 2020
leaf04            3004002    10.0.1.2         L3               -              no        65102:3004002    65102:3004002    Mon Sep 28 11:00:59 2020
leaf04            30010      10.0.1.2         L2               -              no        65102:30010      65102:30010      Mon Sep 28 11:00:59 2020
```

{{</tab>}}

{{</tabs>}}

### View Devices with the Most Layer 2 EVPN Sessions

You can view the number layer 2 EVPN sessions on your switches and hosts using the large Network Services|All EVPN Sessions card and the NetQ CLI. This data enables you to see which switches are handling the most EVPN traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

{{<tabs "TabID332" >}}

{{<tab "NetQ UI" >}}

To view switches and hosts with the most layer 2 EVPN sessions:

<!-- vale off -->
1. Open the large Network Services|All EVPN Sessions card.

2. Select **Switches with Most L2 EVPN** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes running the most layer 2 EVPN sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l2evpn-300.png" width="500">}}
<!-- vale on -->

To compare this data with the same data at a previous time:

1. Open another large Network Services|All EVPN Sessions card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the current time.  

    You can now see whether there are significant differences between this time period and the previous time period.  

    {{<figure src="/images/netq/time-picker-popup-narrow-222.png" width="150">}}

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l2-pst-mo-300.png" width="500">}}

If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running EVPN than previously, looking for changes in the topology, and so forth.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To determine the devices with the most layer 2 EVPN sessions, run `netq show evpn`, then count the layer 2 sessions.

In this example, border01 and border02 have no layer 2 sessions. The leaf01-04 switches each have three layer 2 sessions. Therefore the leaf switches have the most layer 2 sessions.

```
cumulus@switch:~$ netq show evpn
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:49:27 2020
border01          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:49:27 2020
border02          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:48:47 2020
border02          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:48:47 2020
leaf01            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:49:30 2020
leaf01            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:49:30 2020
leaf01            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:49:30 2020
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:49:30 2020
leaf01            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:49:30 2020
leaf02            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:48:25 2020
leaf02            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:48:25 2020
leaf02            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:48:25 2020
leaf02            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:48:25 2020
leaf02            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:48:25 2020
leaf03            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:13 2020
leaf03            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:13 2020
leaf03            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:13 2020
leaf03            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:13 2020
leaf03            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:13 2020
leaf04            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:09 2020
leaf04            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:09 2020
leaf04            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:09 2020
leaf04            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:09 2020
leaf04            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:09 2020
```

To compare this with a time in the past, run `netq show evpn around`.

In this example, border01 and border02 each have three layer 2 sessions. Leaf01-04 also have three layer 2 sessions. Therefore no switch has any more layer 2 sessions than any other running the EVPN service 14 days ago.

```
cumulus@netq-ts:~$ netq show evpn around 14d
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          3004001    10.0.1.254       L3               -              no        65254:3004001    65254:3004001    Mon Sep 28 11:00:44 2020
border01          30030      10.0.1.254       L2               -              no        65254:30030      65254:30030      Mon Sep 28 11:00:44 2020
border01          30020      10.0.1.254       L2               -              no        65254:30020      65254:30020      Mon Sep 28 11:00:44 2020
border01          3004002    10.0.1.254       L3               -              no        65254:3004002    65254:3004002    Mon Sep 28 11:00:44 2020
border01          30010      10.0.1.254       L2               -              no        65254:30010      65254:30010      Mon Sep 28 11:00:44 2020
border02          30030      10.0.1.254       L2               -              no        65254:30030      65254:30030      Mon Sep 28 11:00:32 2020
border02          3004001    10.0.1.254       L3               -              no        65254:3004001    65254:3004001    Mon Sep 28 11:00:32 2020
border02          30010      10.0.1.254       L2               -              no        65254:30010      65254:30010      Mon Sep 28 11:00:32 2020
border02          30020      10.0.1.254       L2               -              no        65254:30020      65254:30020      Mon Sep 28 11:00:32 2020
border02          3004002    10.0.1.254       L3               -              no        65254:3004002    65254:3004002    Mon Sep 28 11:00:32 2020
leaf01            30030      10.0.1.1         L2               -              no        65101:30030      65101:30030      Mon Sep 28 10:57:33 2020
leaf01            3004001    10.0.1.1         L3               -              no        65101:3004001    65101:3004001    Mon Sep 28 10:57:33 2020
leaf01            30010      10.0.1.1         L2               -              no        65101:30010      65101:30010      Mon Sep 28 10:57:33 2020
leaf01            3004002    10.0.1.1         L3               -              no        65101:3004002    65101:3004002    Mon Sep 28 10:57:33 2020
leaf01            30020      10.0.1.1         L2               -              no        65101:30020      65101:30020      Mon Sep 28 10:57:33 2020
leaf02            30010      10.0.1.1         L2               -              no        65101:30010      65101:30010      Mon Sep 28 11:00:14 2020
leaf02            30030      10.0.1.1         L2               -              no        65101:30030      65101:30030      Mon Sep 28 11:00:14 2020
leaf02            3004001    10.0.1.1         L3               -              no        65101:3004001    65101:3004001    Mon Sep 28 11:00:14 2020
leaf02            30020      10.0.1.1         L2               -              no        65101:30020      65101:30020      Mon Sep 28 11:00:14 2020
leaf02            3004002    10.0.1.1         L3               -              no        65101:3004002    65101:3004002    Mon Sep 28 11:00:14 2020
leaf03            30010      10.0.1.2         L2               -              no        65102:30010      65102:30010      Mon Sep 28 11:04:47 2020
leaf03            30030      10.0.1.2         L2               -              no        65102:30030      65102:30030      Mon Sep 28 11:04:47 2020
leaf03            30020      10.0.1.2         L2               -              no        65102:30020      65102:30020      Mon Sep 28 11:04:47 2020
leaf03            3004001    10.0.1.2         L3               -              no        65102:3004001    65102:3004001    Mon Sep 28 11:04:47 2020
leaf03            3004002    10.0.1.2         L3               -              no        65102:3004002    65102:3004002    Mon Sep 28 11:04:47 2020
leaf04            30020      10.0.1.2         L2               -              no        65102:30020      65102:30020      Mon Sep 28 11:00:59 2020
leaf04            3004001    10.0.1.2         L3               -              no        65102:3004001    65102:3004001    Mon Sep 28 11:00:59 2020
leaf04            30030      10.0.1.2         L2               -              no        65102:30030      65102:30030      Mon Sep 28 11:00:59 2020
leaf04            3004002    10.0.1.2         L3               -              no        65102:3004002    65102:3004002    Mon Sep 28 11:00:59 2020
leaf04            30010      10.0.1.2         L2               -              no        65102:30010      65102:30010      Mon Sep 28 11:00:59 2020
```

{{</tab>}}

{{</tabs>}}

### View Devices with the Most Layer 3 EVPN Sessions

You can view the number layer 3 EVPN sessions on your switches and hosts using the large Network Services|All EVPN Sessions card and the NetQ CLI. This data enables you to see which switches are handling the most EVPN traffic currently, validate that is what is expected based on your network design, and compare that with data from an earlier time to look for any differences.

{{<tabs "TabID453" >}}

{{<tab "NetQ UI" >}}

To view switches and hosts with the most layer 3 EVPN sessions:

<!-- vale off -->
1. Open the large Network Services|All EVPN Sessions card.

2. Select **Switches with Most L3 EVPN** from the filter above the table.  

    The table content is sorted by this characteristic, listing nodes running the most layer 3 EVPN sessions at the top. Scroll down to view those with the fewest sessions.

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l3evpn-300.png" width="500">}}
<!-- vale on -->

To compare this data with the same data at a previous time:

1. Open another large Network Services|All EVPN Sessions card.

2. Move the new card next to the original card if needed.

3. Change the time period for the data on the new card by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/>.

4. Select the time period that you want to compare with the current time.  

    You can now see whether there are significant differences between this time period and the previous time period.  

    {{< figure src="/images/netq/time-picker-popup-narrow-222.png" width="150" >}}

    {{< figure src="/images/netq/ntwk-svcs-all-evpn-large-summary-tab-most-l3-pst-wk-230.png" width="500" >}}

If the changes are unexpected, you can investigate further by looking at another time frame, determining if more nodes are now running EVPN than previously, looking for changes in the topology, and so forth.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To determine the devices with the most layer 3 EVPN sessions, run `netq show evpn`, then count the layer 3 sessions.

In this example, border01 and border02 each have two layer 3 sessions. The leaf01-04 switches also each have two layer 3 sessions. Therefore there is no particular switch that has the most layer 3 sessions.

```
cumulus@switch:~$ netq show evpn
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:49:27 2020
border01          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:49:27 2020
border02          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:48:47 2020
border02          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:48:47 2020
leaf01            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:49:30 2020
leaf01            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:49:30 2020
leaf01            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:49:30 2020
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:49:30 2020
leaf01            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:49:30 2020
leaf02            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:48:25 2020
leaf02            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:48:25 2020
leaf02            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:48:25 2020
leaf02            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:48:25 2020
leaf02            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:48:25 2020
leaf03            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:13 2020
leaf03            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:13 2020
leaf03            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:13 2020
leaf03            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:13 2020
leaf03            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:13 2020
leaf04            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:09 2020
leaf04            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:09 2020
leaf04            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:09 2020
leaf04            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:09 2020
leaf04            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:09 2020
```

To compare this with a time in the past, run `netq show evpn around`.

In this example, border01 and border02 each have two layer 3 sessions. Leaf01-04 also have two layer 3 sessions. Therefore no switch has any more layer 3 sessions than any other running the EVPN service 14 days ago.

```
cumulus@netq-ts:~$ netq show evpn around 14d
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          3004001    10.0.1.254       L3               -              no        65254:3004001    65254:3004001    Mon Sep 28 11:00:44 2020
border01          30030      10.0.1.254       L2               -              no        65254:30030      65254:30030      Mon Sep 28 11:00:44 2020
border01          30020      10.0.1.254       L2               -              no        65254:30020      65254:30020      Mon Sep 28 11:00:44 2020
border01          3004002    10.0.1.254       L3               -              no        65254:3004002    65254:3004002    Mon Sep 28 11:00:44 2020
border01          30010      10.0.1.254       L2               -              no        65254:30010      65254:30010      Mon Sep 28 11:00:44 2020
border02          30030      10.0.1.254       L2               -              no        65254:30030      65254:30030      Mon Sep 28 11:00:32 2020
border02          3004001    10.0.1.254       L3               -              no        65254:3004001    65254:3004001    Mon Sep 28 11:00:32 2020
border02          30010      10.0.1.254       L2               -              no        65254:30010      65254:30010      Mon Sep 28 11:00:32 2020
border02          30020      10.0.1.254       L2               -              no        65254:30020      65254:30020      Mon Sep 28 11:00:32 2020
border02          3004002    10.0.1.254       L3               -              no        65254:3004002    65254:3004002    Mon Sep 28 11:00:32 2020
leaf01            30030      10.0.1.1         L2               -              no        65101:30030      65101:30030      Mon Sep 28 10:57:33 2020
leaf01            3004001    10.0.1.1         L3               -              no        65101:3004001    65101:3004001    Mon Sep 28 10:57:33 2020
leaf01            30010      10.0.1.1         L2               -              no        65101:30010      65101:30010      Mon Sep 28 10:57:33 2020
leaf01            3004002    10.0.1.1         L3               -              no        65101:3004002    65101:3004002    Mon Sep 28 10:57:33 2020
leaf01            30020      10.0.1.1         L2               -              no        65101:30020      65101:30020      Mon Sep 28 10:57:33 2020
leaf02            30010      10.0.1.1         L2               -              no        65101:30010      65101:30010      Mon Sep 28 11:00:14 2020
leaf02            30030      10.0.1.1         L2               -              no        65101:30030      65101:30030      Mon Sep 28 11:00:14 2020
leaf02            3004001    10.0.1.1         L3               -              no        65101:3004001    65101:3004001    Mon Sep 28 11:00:14 2020
leaf02            30020      10.0.1.1         L2               -              no        65101:30020      65101:30020      Mon Sep 28 11:00:14 2020
leaf02            3004002    10.0.1.1         L3               -              no        65101:3004002    65101:3004002    Mon Sep 28 11:00:14 2020
leaf03            30010      10.0.1.2         L2               -              no        65102:30010      65102:30010      Mon Sep 28 11:04:47 2020
leaf03            30030      10.0.1.2         L2               -              no        65102:30030      65102:30030      Mon Sep 28 11:04:47 2020
leaf03            30020      10.0.1.2         L2               -              no        65102:30020      65102:30020      Mon Sep 28 11:04:47 2020
leaf03            3004001    10.0.1.2         L3               -              no        65102:3004001    65102:3004001    Mon Sep 28 11:04:47 2020
leaf03            3004002    10.0.1.2         L3               -              no        65102:3004002    65102:3004002    Mon Sep 28 11:04:47 2020
leaf04            30020      10.0.1.2         L2               -              no        65102:30020      65102:30020      Mon Sep 28 11:00:59 2020
leaf04            3004001    10.0.1.2         L3               -              no        65102:3004001    65102:3004001    Mon Sep 28 11:00:59 2020
leaf04            30030      10.0.1.2         L2               -              no        65102:30030      65102:30030      Mon Sep 28 11:00:59 2020
leaf04            3004002    10.0.1.2         L3               -              no        65102:3004002    65102:3004002    Mon Sep 28 11:00:59 2020
leaf04            30010      10.0.1.2         L2               -              no        65102:30010      65102:30010      Mon Sep 28 11:00:59 2020
```

{{</tab>}}

{{</tabs>}}

### View the Status of EVPN for a Given VNI

You can view the status of the EVPN service on a single VNI using the full-screen Network Services|All Sessions card or the NetQ CLI.

{{<tabs "TabID586" >}}

{{<tab "NetQ UI" >}}

1. Open the full-screen Network Services|All Sessions card.

2. Sort the table based on the VNI column.

3. Page forward and backward to find the VNI of interest and then view the status of the service for that VNI.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-allsessions-tab-byVNI-320.png" width="700">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

Use the `vni` option with the `netq show evpn` command to filter the result for a specific VNI.

This example only shows the EVPN configuration and status for VNI *4001*.

```
cumulus@switch:~$ netq show evpn vni 4001
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Mon Oct 12 03:45:45 2020
border02          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Mon Oct 12 03:45:11 2020
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Mon Oct 12 03:46:15 2020
leaf02            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Mon Oct 12 03:44:18 2020
leaf03            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Mon Oct 12 03:48:22 2020
leaf04            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Mon Oct 12 03:47:47 2020
```

{{</tab>}}

{{</tabs>}}

<!-- vale off -->
### View Devices with the Most EVPN-related Alarms
<!-- vale on -->

Switches experiencing a large number of EVPN alarms may indicate a configuration or performance issue that needs further investigation. You can view the switches sorted by the number of EVPN alarms and then use the Switches card workflow or the Events|Alarms card workflow to gather more information about possible causes for the alarms.

{{<tabs "View EVPN events">}}

{{<tab "NetQ UI">}}

You can view the switches sorted by the number of EVPN alarms and then use the Switches card workflow or the Events|Alarms card workflow to gather more information about possible causes for the alarms.

To view switches with the most EVPN alarms:

1. Open the large Network Services|All EVPN Sessions card.

2. Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/>.

3. Select **Events by Most Active Device** from the filter above the table.

    The table content is sorted by this characteristic, listing nodes with the most EVPN alarms at the top. Scroll down to view those with the fewest alarms.

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-large-alarms-tab-230.png" width="500" >}}

Where to go next depends on what data you see, but a few options include:

- Hover over the Total Alarms chart to focus on the switches exhibiting alarms during that smaller time slice. The table content changes to match the hovered content. Click on the chart to persist the table changes.
- Change the time period for the data to compare with a prior time. If the same switches are consistently indicating the most alarms, you might want to look more carefully at those switches using the Switches card workflow.
- Click **Show All Sessions** to investigate all EVPN sessions networkwide in the full screen card.

{{</tab>}}

{{<tab "NetQ CLI">}}

To view the switches with the most EVPN alarms and informational events, run the `netq show events` command with the `type` option set to *evpn*, and optionally the `between` option set to display the events within a given time range. Count the events associated with each switch.

This example shows the events that have occurred in the last 48 hours.

```
cumulus@switch:/$ netq show events type evpn between now and 48h
Matching events records:
Hostname          Message Type Severity Message                             Timestamp
----------------- ------------ -------- ----------------------------------- -------------------------
torc-21           evpn         info     VNI 33 state changed from down to u 1d:8h:16m:29s
                                        p
torc-12           evpn         info     VNI 41 state changed from down to u 1d:8h:16m:35s
                                        p
torc-11           evpn         info     VNI 39 state changed from down to u 1d:8h:16m:41s
                                        p
tor-1             evpn         info     VNI 37 state changed from down to u 1d:8h:16m:47s
                                        p
tor-2             evpn         info     VNI 42 state changed from down to u 1d:8h:16m:51s
                                        p
torc-22           evpn         info     VNI 39 state changed from down to u 1d:8h:17m:40s
                                        p
...
```

{{</tab>}}

{{</tabs>}}

### View All EVPN Events

The Network Services|All EVPN Sessions card workflow and the `netq show events type evpn` command enable you to view all EVPN events in a designated time period.

{{<tabs "View all EVPN events">}}

{{<tab "NetQ UI">}}

To view all EVPN events:

1. Open the full screen Network Services|All EVPN Sessions card.

2. Click **All Alarms** tab in the navigation panel. By default, events are sorted by Time, with most recent events listed first.

    {{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-alarms-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options
include:

- Open one of the other full screen tabs in this flow to focus on devices or sessions.
- Sort by the **Message** or **Severity** to narrow your focus.
- Export the data for use in another analytics tool, by selecting all or some of the events and clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right to return to your workbench.

{{</tab>}}

{{<tab "NetQ CLI">}}

To view all EVPN alarms, run:

```
netq show events [level info | level error | level warning | level critical | level debug] type evpn [between <text-time> and <text-endtime>] [json]
```

Use the level option to set the severity of the events to show. Use the `between` option to show events within a given time range.

This example shows critical EVPN events in the past three days.

```
cumulus@switch:~$ netq show events level critical type evpn between now and 3d
```

{{</tab>}}

{{</tabs>}}

### View Details for All Devices Running EVPN

You can view all stored attributes of all switches running EVPN in your network in the full screen card.

To view all switch and host details, open the full screen EVPN Service card, and click the **All Switches** tab.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-allswitches-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right.

### View Details for All EVPN Sessions

You can view attributes of all EVPN sessions in your network with the NetQ UI or NetQ CLI.

{{<tabs "View all EVPN sessions">}}

{{<tab "NetQ UI">}}

To view all session details, open the full screen EVPN Service card, and click the **All Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-all-evpn-fullscr-sessions-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right.

Use the icons above the table to select/deselect, filter, and export items in the list. Refer to {{<link url="Access-Data-with-Cards/#table-settings" text="Table Settings">}} for more detail.

{{</tab>}}

{{<tab "NetQ CLI">}}

To view session details, run `netq show evpn`.

This example shows all current sessions and the attributes associated with them.

```
cumulus@switch:~$ netq show evpn
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:49:27 2020
border01          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:49:27 2020
border02          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Wed Oct  7 00:48:47 2020
border02          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Wed Oct  7 00:48:47 2020
leaf01            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:49:30 2020
leaf01            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:49:30 2020
leaf01            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:49:30 2020
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:49:30 2020
leaf01            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:49:30 2020
leaf02            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Wed Oct  7 00:48:25 2020
leaf02            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct  7 00:48:25 2020
leaf02            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Wed Oct  7 00:48:25 2020
leaf02            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Wed Oct  7 00:48:25 2020
leaf02            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Wed Oct  7 00:48:25 2020
leaf03            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:13 2020
leaf03            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:13 2020
leaf03            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:13 2020
leaf03            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:13 2020
leaf03            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:13 2020
leaf04            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Wed Oct  7 00:50:09 2020
leaf04            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Wed Oct  7 00:50:09 2020
leaf04            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct  7 00:50:09 2020
leaf04            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Wed Oct  7 00:50:09 2020
leaf04            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Wed Oct  7 00:50:09 2020
```

{{</tab>}}

{{</tabs>}}

## Monitor a Single EVPN Session

With NetQ, you can monitor the performance of a single EVPN session using the NetQ UI or NetQ CLI.  

- Network Services|EVPN Session
    - Small: view associated VNI name and total number of nodes with VNIs configured
    - Medium: view associated VNI name and type, total number and distribution of nodes with VNIs configured
    - Large: view total number and distribution of nodes with VNIs configured, total alarm and informational events, and associated VRF/VLAN
    - Full-screen: view details of sessions-import/export route, type, origin IP address, VNI, VNI/gateway advertisement, and so forth
- `netq <hostname> show evpn vni` command: view configuration and status for session (hostname, VNI), VTEP address, import and export route, and last time a change was made

For an overview and how to configure EVPN in your data center network, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/" text="Ethernet Virtual Private Network - EVPN">}}.

{{<notice note>}}
To access the single session cards, you must open the full-screen Network Services|All EVPN Sessions card, click the <strong>All Sessions</strong> tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18"/> (Open Card).
{{</notice>}}

### View Session Status Summary

You can view a summary of a given EVPN session from the NetQ UI or NetQ CLI.

{{<tabs "TabID815" >}}

{{<tab "NetQ UI" >}}

To view the summary:

1. Open the Network Services|All EVPN Sessions card.

2. Change to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

    {{<figure src="/images/netq/ntwk-svcs-single-evpn-medium-230.png" width="200">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view a session summary, run:

```
netq <hostname> show evpn vni <text-vni> [around <text-time>] [json]
```

Use the `around` option to show status at a time in the past. Output the results in JSON format using the `json` option.

This example shows the summary information for the session on *leaf01* for VNI *4001*.

```
cumulus@switch:~$ netq leaf01 show evpn vni 4001
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Tue Oct 13 04:21:15 2020
```

{{</tab>}}

{{</tabs>}}

### View VTEP Count

You can view the number of VTEPs (VXLAN Tunnel Endpoints) for a given EVPN session from the medium and large Network Services|EVPN Session cards.

To view the count for a given EVPN session, on the *medium* EVPN Session
card:

1. Open the Network Services|All EVPN Sessions card.

2. Change to the full-screen card using the card size picker.

3. Click the **All Sessions** tab.

4. Select the session of interest, then click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg"  height="18" width="18">}} (Open Card).

    {{<figure src="/images/netq/ntwk-svcs-single-evpn-medium-vtep-count-230.png" width="200">}}

<div style="padding-left: 18px;">The same information is available on the large size card. Use the card size picker to open the large card.

{{<figure src="/images/netq/ntwk-svcs-single-evpn-large-summary-tab-vtep-cnt-230.png" width="500">}}

This card also shows the associated VRF (layer 3) or VLAN (layer 2) on each device participating in this session. </div>

### View VTEP IP Address

You can view the IP address of the VTEP used in a given session using the `netq show evpn` command.

This example shows a VTEP address of *10.0.1.1* for the *leaf01:VNI 4001* EVPN session.

```
cumulus@switch:~$ netq leaf01 show evpn vni 4001
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Tue Oct 13 04:21:15 2020
```

### View All EVPN Sessions on a VNI

You can view the attributes of all EVPN sessions for a given VNI using the NetQ UI or NetQ CLI.

{{<tabs "TabID898" >}}

{{<tab "NetQ UI" >}}

You can view all stored attributes of all EVPN sessions running networkwide.

To view all session details, open the full screen EVPN Session card and click the **All EVPN Sessions** tab.

{{<figure src="/images/netq/ntwk-svcs-single-evpn-fullscr-allsess-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right of the card.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view the sessions, run `netq show evpn` with the `vni` option.

This example shows all sessions for VNI *20*.

```
cumulus@switch:~$ netq show evpn vni 20
Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
leaf01            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct 14 04:56:31 2020
leaf02            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Wed Oct 14 04:54:29 2020
leaf03            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct 14 04:58:57 2020
leaf04            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Wed Oct 14 04:58:46 2020
```

{{</tab>}}

{{</tabs>}}

### View All Session Events

You can view all alarm and info events for a given session with the NetQ UI.

To view all events, open the full-screen Network Services|EVPN Session card and click the **All Events** tab.

{{<figure src="/images/netq/ntwk-svcs-single-evpn-fullscr-events-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Open one of the other full screen tabs in this flow to focus on sessions.
- Sort by the **Message** or **Severity** to narrow your focus.
- Export the data for use in another analytics tool, by selecting all or some of the events and clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.
- Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> at the top right to return to your workbench.
