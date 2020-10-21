---
title: Monitor the BGP Service Using NetQ CLI
author: Cumulus Networks
weight: 955
toc: 4
---
If you have BGP running on your switches and hosts, you can monitor its
operation using the NetQ CLI. For each device, you can view its
associated neighbors, ASN (autonomous system number), peer ASN, receive
IP or EVPN address prefixes, and VRF assignment. Additionally, you can:

- View the information at an earlier point in time
- Filter against a particular device, ASN, or VRF assignment

The `netq show bgp` command is used to obtain the BGP configuration
information from the devices. The `netq show events` command is used to
display the BGP-related events. The syntax of these commands is:

    netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] [vrf <vrf>] [around <text-time>] [json]
    netq [<hostname>] show events [level info|level error|level warning|level critical|level debug] type bgp [between <text-time> and <text-endtime>] [json]

{{<notice note>}}

When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: week(s)
- **d**: day(s)
- **h**: hour(s)
- **m**: minute(s)
- **s**: second(s)
- **now**

For the <code>between</code> option, the start (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.

{{</notice>}}

## View BGP Configuration Information Networkwide

This example shows the BGP configuration across all of your switches. In
this scenario, BGP routing is configured between two spines and four
leafs. Each leaf switch has a unique ASN and the spine switches share an
ASN. The PfxRx column indicates that these devices have IPv4 address
prefixes. The second and third values in this column indicate IPv6 and
EVPN address prefixes when configured. This configuration was changed
just over one day ago.

```
cumulus@switch:~$ netq show bgp
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
exit-1            swp3(spine-1)                default         655537     655435     29/25/434    Thu Feb  7 18:19:50 2019
exit-1            swp3.2(spine-1)              DataVrf1080     655537     655435     15/13/0      Thu Feb  7 18:19:50 2019
exit-1            swp3.3(spine-1)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
exit-1            swp3.4(spine-1)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
exit-1            swp4(spine-2)                default         655537     655435     29/25/434    Thu Feb  7 18:19:50 2019
exit-1            swp4.2(spine-2)              DataVrf1080     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
exit-1            swp4.3(spine-2)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
exit-1            swp4.4(spine-2)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
exit-1            swp5(spine-3)                default         655537     655435     30/25/434    Thu Feb  7 18:19:50 2019
exit-1            swp5.2(spine-3)              DataVrf1080     655537     655435     15/13/0      Thu Feb  7 18:19:50 2019
exit-1            swp5.3(spine-3)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
exit-1            swp5.4(spine-3)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
exit-1            swp7                         default         655537     -          NotEstd      Thu Feb  7 18:31:44 2019
exit-1            swp7.2                       DataVrf1080     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
exit-1            swp7.3                       DataVrf1081     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
exit-1            swp7.4                       DataVrf1082     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
exit-2            swp3(spine-1)                default         655538     655435     28/24/434    Thu Feb  7 18:19:50 2019
exit-2            swp3.2(spine-1)              DataVrf1080     655538     655435     14/12/0      Thu Feb  7 18:19:50 2019
exit-2            swp3.3(spine-1)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit-2            swp3.4(spine-1)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit-2            swp4(spine-2)                default         655538     655435     28/24/434    Thu Feb  7 18:19:50 2019
exit-2            swp4.2(spine-2)              DataVrf1080     655538     655435     14/12/0      Thu Feb  7 18:19:50 2019
exit-2            swp4.3(spine-2)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit-2            swp4.4(spine-2)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit-2            swp5(spine-3)                default         655538     655435     27/24/434    Thu Feb  7 18:19:50 2019
exit-2            swp5.2(spine-3)              DataVrf1080     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit-2            swp5.3(spine-3)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit-2            swp5.4(spine-3)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit-2            swp7                         default         655538     -          NotEstd      Thu Feb  7 18:31:49 2019
exit-2            swp7.2                       DataVrf1080     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
exit-2            swp7.3                       DataVrf1081     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
exit-2            swp7.4                       DataVrf1082     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
spine-1           swp10(exit-2)                default         655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine-1           swp10.2(exit-2)              DataVrf1080     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine-1           swp10.3(exit-2)              DataVrf1081     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine-1           swp10.4(exit-2)              DataVrf1082     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine-1           swp3(leaf-11)                default         655435     655559     19/6/94      Thu Feb  7 18:19:50 2019
spine-1           swp3.2(leaf-11)              DataVrf1080     655435     655559     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp3.3(leaf-11)              DataVrf1081     655435     655559     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp3.4(leaf-11)              DataVrf1082     655435     655559     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp4(leaf-12)                default         655435     655560     19/6/64      Thu Feb  7 18:19:50 2019
spine-1           swp4.2(leaf-12)              DataVrf1080     655435     655560     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp4.3(leaf-12)              DataVrf1081     655435     655560     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp4.4(leaf-12)              DataVrf1082     655435     655560     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp5(leaf-21)                default         655435     655561     19/6/50      Thu Feb  7 18:19:50 2019
spine-1           swp5.2(leaf-21)              DataVrf1080     655435     655561     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp5.3(leaf-21)              DataVrf1081     655435     655561     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp5.4(leaf-21)              DataVrf1082     655435     655561     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp6(leaf-22)                default         655435     655562     19/6/62      Thu Feb  7 18:19:50 2019
spine-1           swp6.2(leaf-22)              DataVrf1080     655435     655562     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp6.3(leaf-22)              DataVrf1081     655435     655562     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp6.4(leaf-22)              DataVrf1082     655435     655562     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp7(leaf-1)                 default         655435     655557     17/5/54      Thu Feb  7 18:19:50 2019
spine-1           swp7.2(leaf-1)               DataVrf1080     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp7.3(leaf-1)               DataVrf1081     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp7.4(leaf-1)               DataVrf1082     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp8(leaf-2)                 default         655435     655558     17/5/54      Thu Feb  7 18:19:50 2019
spine-1           swp8.2(leaf-2)               DataVrf1080     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp8.3(leaf-2)               DataVrf1081     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp8.4(leaf-2)               DataVrf1082     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
spine-1           swp9(exit-1)                 default         655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine-1           swp9.2(exit-1)               DataVrf1080     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine-1           swp9.3(exit-1)               DataVrf1081     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine-1           swp9.4(exit-1)               DataVrf1082     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine-2           swp10(exit-2)                default         655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine-2           swp10.3(exit-2)              DataVrf1081     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine-2           swp10.4(exit-2)              DataVrf1082     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine-2           swp3.2(leaf-11)              DataVrf1080     655435     655559     14/2/0       Thu Feb  7 18:19:50 2019
...
```

## View BGP Configuration Information for a Given Device

This example shows the BGP configuration information for the spine02
switch. The switch is peered with swp1 on leaf01, swp2 on leaf02, and so
on. Spine02 has an ASN of 65020 and each of the leafs have unique ASNs.

```
cumulus@switch:~$ netq spine02 show bgp
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
spine02           swp3(spine01)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
spine02           swp3.2(spine01)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
spine02           swp3.3(spine01)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
spine02           swp3.4(spine01)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
spine02           swp5(spine03)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
spine02           swp5.2(spine03)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
spine02           swp5.3(spine03)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
spine02           swp5.4(spine03)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
```

## View BGP Configuration Information for a Given ASN

This example shows the BGP configuration information for ASN of
*655557*. This ASN is associated with spine02 and so the results show
the BGP neighbors for that switch.

```
cumulus@switch:~$ netq show bgp asn 655557
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
spine02           swp3(spine01)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
spine02           swp3.2(spine01)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
spine02           swp3.3(spine01)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
spine02           swp3.4(spine01)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
spine02           swp5(spine03)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
spine02           swp5.2(spine03)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
spine02           swp5.3(spine03)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
spine02           swp5.4(spine03)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
```

## View BGP Configuration Information for a Prior Time

This example shows the BGP configuration information as it was 12 hours
earlier.

```
cumulus@switch:~$ netq show bgp around 12h
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
exit01            swp3(spine01)                default         655537     655435     29/25/434    Thu Feb  7 18:19:50 2019
exit01            swp3.2(spine01)              DataVrf1080     655537     655435     15/13/0      Thu Feb  7 18:19:50 2019
exit01            swp3.3(spine01)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
exit01            swp3.4(spine01)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
exit01            swp4(spine02)                default         655537     655435     29/25/434    Thu Feb  7 18:19:50 2019
exit01            swp4.2(spine02)              DataVrf1080     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
exit01            swp4.3(spine02)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
exit01            swp4.4(spine02)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
exit01            swp5(spine03)                default         655537     655435     30/25/434    Thu Feb  7 18:19:50 2019
exit01            swp5.2(spine03)              DataVrf1080     655537     655435     15/13/0      Thu Feb  7 18:19:50 2019
exit01            swp5.3(spine03)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
exit01            swp5.4(spine03)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
exit01            swp6(firewall01)             default         655537     655539     73/69/-      Thu Feb  7 18:26:30 2019
exit01            swp6.2(firewall01)           DataVrf1080     655537     655539     73/69/-      Thu Feb  7 18:26:30 2019
exit01            swp6.3(firewall01)           DataVrf1081     655537     655539     73/69/-      Thu Feb  7 18:26:30 2019
exit01            swp6.4(firewall01)           DataVrf1082     655537     655539     73/69/-      Thu Feb  7 18:26:30 2019
exit01            swp7                         default         655537     -          NotEstd      Thu Feb  7 18:31:44 2019
exit01            swp7.2                       DataVrf1080     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
exit01            swp7.3                       DataVrf1081     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
exit01            swp7.4                       DataVrf1082     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
exit02            swp3(spine01)                default         655538     655435     28/24/434    Thu Feb  7 18:19:50 2019
exit02            swp3.2(spine01)              DataVrf1080     655538     655435     14/12/0      Thu Feb  7 18:19:50 2019
exit02            swp3.3(spine01)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit02            swp3.4(spine01)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit02            swp4(spine02)                default         655538     655435     28/24/434    Thu Feb  7 18:19:50 2019
exit02            swp4.2(spine02)              DataVrf1080     655538     655435     14/12/0      Thu Feb  7 18:19:50 2019
exit02            swp4.3(spine02)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit02            swp4.4(spine02)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit02            swp5(spine03)                default         655538     655435     27/24/434    Thu Feb  7 18:19:50 2019
exit02            swp5.2(spine03)              DataVrf1080     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit02            swp5.3(spine03)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit02            swp5.4(spine03)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
exit02            swp6(firewall01)             default         655538     655539     7/5/-        Thu Feb  7 18:26:30 2019
exit02            swp6.2(firewall01)           DataVrf1080     655538     655539     7/5/-        Thu Feb  7 18:26:30 2019
exit02            swp6.3(firewall01)           DataVrf1081     655538     655539     7/5/-        Thu Feb  7 18:26:30 2019
exit02            swp6.4(firewall01)           DataVrf1082     655538     655539     7/5/-        Thu Feb  7 18:26:30 2019
exit02            swp7                         default         655538     -          NotEstd      Thu Feb  7 18:31:49 2019
exit02            swp7.2                       DataVrf1080     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
exit02            swp7.3                       DataVrf1081     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
exit02            swp7.4                       DataVrf1082     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
firewall01        swp3(exit01)                 default         655539     655537     29/27/-      Thu Feb  7 18:26:30 2019
firewall01        swp3.2(exit01)               default         655539     655537     15/15/-      Thu Feb  7 18:26:30 2019
firewall01        swp3.3(exit01)               default         655539     655537     15/15/-      Thu Feb  7 18:26:30 2019
firewall01        swp3.4(exit01)               default         655539     655537     15/15/-      Thu Feb  7 18:26:30 2019
firewall01        swp4(exit02)                 default         655539     655538     29/27/-      Thu Feb  7 18:26:30 2019
firewall01        swp4.2(exit02)               default         655539     655538     15/15/-      Thu Feb  7 18:26:30 2019
firewall01        swp4.3(exit02)               default         655539     655538     15/15/-      Thu Feb  7 18:26:30 2019
firewall01        swp4.4(exit02)               default         655539     655538     15/15/-      Thu Feb  7 18:26:30 2019
spine01           swp10(exit02)                default         655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine01           swp10.2(exit02)              DataVrf1080     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine01           swp10.3(exit02)              DataVrf1081     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine01           swp10.4(exit02)              DataVrf1082     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine01           swp7(leaf01)                 default         655435     655557     17/5/54      Thu Feb  7 18:19:50 2019
spine01           swp7.2(leaf01)               DataVrf1080     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
spine01           swp7.3(leaf01)               DataVrf1081     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
spine01           swp7.4(leaf01)               DataVrf1082     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
spine01           swp8(leaf02)                 default         655435     655558     17/5/54      Thu Feb  7 18:19:50 2019
spine01           swp8.2(leaf02)               DataVrf1080     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
spine01           swp8.3(leaf02)               DataVrf1081     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
spine01           swp8.4(leaf02)               DataVrf1082     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
spine01           swp9(exit01)                 default         655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine01           swp9.2(exit01)               DataVrf1080     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine01           swp9.3(exit01)               DataVrf1081     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine01           swp9.4(exit01)               DataVrf1082     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine02           swp10(exit02)                default         655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine02           swp10.3(exit02)              DataVrf1081     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine02           swp10.4(exit02)              DataVrf1082     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine02           swp7(leaf01)                 default         655435     655557     17/5/62      Thu Feb  7 18:19:50 2019
spine02           swp7.2(leaf01)               DataVrf1080     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
spine02           swp7.3(leaf01)               DataVrf1081     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
spine02           swp7.4(leaf01)               DataVrf1082     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
spine02           swp8(leaf02)                 default         655435     655558     17/5/62      Thu Feb  7 18:19:50 2019
spine02           swp8.2(leaf02)               DataVrf1080     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
spine02           swp8.3(leaf02)               DataVrf1081     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
spine02           swp8.4(leaf02)               DataVrf1082     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
spine02           swp9(exit01)                 default         655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine02           swp9.2(exit01)               DataVrf1080     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine02           swp9.4(exit01)               DataVrf1082     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
spine02           swp10.2(exit02)              DataVrf1080     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
spine02           swp9.3(exit01)               DataVrf1081     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
leaf01            swp3(spine01)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
leaf01            swp3.2(spine01)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf01            swp3.3(spine01)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf01            swp3.4(spine01)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
leaf01            swp4(spine02)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
leaf01            swp4.2(spine02)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf01            swp4.3(spine02)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf01            swp4.4(spine02)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
leaf01            swp5(spine03)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
leaf01            swp5.2(spine03)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf01            swp5.3(spine03)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf01            swp5.4(spine03)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
leaf02            swp3(spine01)                default         655558     655435     42/27/372    Thu Feb  7 18:19:50 2019
leaf02            swp3.2(spine01)              DataVrf1080     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf02            swp3.3(spine01)              DataVrf1081     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf02            swp3.4(spine01)              DataVrf1082     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf02            swp4(spine02)                default         655558     655435     42/27/372    Thu Feb  7 18:19:50 2019
leaf02            swp4.2(spine02)              DataVrf1080     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf02            swp4.3(spine02)              DataVrf1081     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf02            swp4.4(spine02)              DataVrf1082     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf02            swp5(spine03)                default         655558     655435     42/27/372    Thu Feb  7 18:19:50 2019
leaf02            swp5.2(spine03)              DataVrf1080     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf02            swp5.3(spine03)              DataVrf1081     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
leaf02            swp5.4(spine03)              DataVrf1082     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
...
```

## View BGP-related Events

This example shows that BGP configuration changes were made between now and five days ago on this network.

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
