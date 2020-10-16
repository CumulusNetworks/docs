---
title: Monitor Virtual Extensible LANs
author: Cumulus Networks
weight: 990
toc: 3
---

The NetQ CLI provides the ability to view the performance and status of VXLANs. Virtual Extensible LANs (VXLANs) provide a way to create a virtual network on top of layer 2 and layer 3 technologies. It is intended for organizations, such as data centers, that require larger scale without additional infrastructure and more flexibility than is available with existing infrastructure equipment. With NetQ, you can monitor the current and historical configuration and status of your VXLANs using the following command:

```
netq [<hostname>] show vxlan [vni <text-vni>] [around <text-time>] [json]
netq show interfaces type vxlan [state <remote-interface-state>] [around <text-time>] [json]
netq <hostname> show interfaces type vxlan [state <remote-interface-state>] [around <text-time>] [count] [json]
netq [<hostname>] show events [level info|level error|level warning|level critical|level debug] type vxlan [between <text-time> and <text-endtime>] [json]
```

{{<notice note>}}
When entering a time value in the <code>netq show evpn</code> command, you must include a numeric value <em>and</em> the unit of measure:
<ul>
<li><strong>w</strong>: week(s)</li>
<li><strong>d</strong>: day(s)</li>
<li><strong>h</strong>: hour(s)</li>
<li><strong>m</strong>: minute(s)</li>
<li><strong>s</strong>: second(s)</li>
<li><strong>now</strong>
</ul>

When using the <code>between</code> option, the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{</notice>}}

### View All VXLANs in Your Network

You can view a list of configured VXLANs for all devices, including the VNI (VXLAN network identifier), protocol, address of associated VTEPs (VXLAN tunnel endpoint), replication list, and the last time it was changed. You can also view VXLAN information for a given device by adding a hostname to the `show` command. You can filter the results by VNI.

This example shows all configured VXLANs across the network. In this network, there are five VNIs (10, 20, 30, 4001 and 4002) associated with five VLANs (10, 20, 30, 4001 and 4002), EVPN is the virtual protocol deployed, and the configuration was last changed on October 15.

 ```
cumulus@switch:~$ netq show vxlan
Matching vxlan records:
Hostname          VNI        Protoc VTEP IP          VLAN   Replication List                    Last Changed
                             ol
----------------- ---------- ------ ---------------- ------ ----------------------------------- -------------------------
border01          4001       EVPN   10.0.1.254       4001                                       Thu Oct 15 22:28:36 2020
border01          4002       EVPN   10.0.1.254       4002                                       Thu Oct 15 22:28:36 2020
border02          4001       EVPN   10.0.1.254       4001                                       Thu Oct 15 22:28:23 2020
border02          4002       EVPN   10.0.1.254       4002                                       Thu Oct 15 22:28:23 2020
leaf01            30         EVPN   10.0.1.1         30     10.0.1.2(leaf03, leaf04)            Thu Oct 15 22:28:11 2020
leaf01            4001       EVPN   10.0.1.1         4001                                       Thu Oct 15 22:28:11 2020
leaf01            10         EVPN   10.0.1.1         10     10.0.1.2(leaf03, leaf04)            Thu Oct 15 22:28:11 2020
leaf01            4002       EVPN   10.0.1.1         4002                                       Thu Oct 15 22:28:11 2020
leaf01            20         EVPN   10.0.1.1         20     10.0.1.2(leaf03, leaf04)            Thu Oct 15 22:28:11 2020
leaf02            30         EVPN   10.0.1.1         30     10.0.1.2(leaf03, leaf04)            Thu Oct 15 22:28:03 2020
leaf02            10         EVPN   10.0.1.1         10     10.0.1.2(leaf03, leaf04)            Thu Oct 15 22:28:03 2020
leaf02            4001       EVPN   10.0.1.1         4001                                       Thu Oct 15 22:28:03 2020
leaf02            20         EVPN   10.0.1.1         20     10.0.1.2(leaf03, leaf04)            Thu Oct 15 22:28:03 2020
leaf02            4002       EVPN   10.0.1.1         4002                                       Thu Oct 15 22:28:03 2020
leaf03            30         EVPN   10.0.1.2         30     10.0.1.1(leaf02, leaf01)            Thu Oct 15 22:28:16 2020
leaf03            10         EVPN   10.0.1.2         10     10.0.1.1(leaf02, leaf01)            Thu Oct 15 22:28:16 2020
leaf03            4001       EVPN   10.0.1.2         4001                                       Thu Oct 15 22:28:16 2020
leaf03            4002       EVPN   10.0.1.2         4002                                       Thu Oct 15 22:28:16 2020
leaf03            20         EVPN   10.0.1.2         20     10.0.1.1(leaf02, leaf01)            Thu Oct 15 22:28:16 2020
leaf04            30         EVPN   10.0.1.2         30     10.0.1.1(leaf02, leaf01)            Thu Oct 15 22:28:41 2020
leaf04            10         EVPN   10.0.1.2         10     10.0.1.1(leaf02, leaf01)            Thu Oct 15 22:28:41 2020
leaf04            4001       EVPN   10.0.1.2         4001                                       Thu Oct 15 22:28:41 2020
leaf04            20         EVPN   10.0.1.2         20     10.0.1.1(leaf02, leaf01)            Thu Oct 15 22:28:41 2020
leaf04            4002       EVPN   10.0.1.2         4002                                       Thu Oct 15 22:28:41 2020
```

This example shows the events and configuration changes that have occurred on the VXLANs in your network in the last 24 hours. In this case, the EVPN configuration was added to each of the devices in the last 24 hours.

 ```
cumulus@switch:~$ netq show events type vxlan between now and 24h
Matching vxlan records:
Hostname          VNI        Protoc VTEP IP          VLAN   Replication List                    DB State   Last Changed
                                ol
----------------- ---------- ------ ---------------- ------ ----------------------------------- ---------- -------------------------
exit02            104001     EVPN   10.0.0.42        4001                                       Add        Fri Feb  8 01:35:49 2019
exit02            104001     EVPN   10.0.0.42        4001                                       Add        Fri Feb  8 01:35:49 2019
exit02            104001     EVPN   10.0.0.42        4001                                       Add        Fri Feb  8 01:35:49 2019
exit02            104001     EVPN   10.0.0.42        4001                                       Add        Fri Feb  8 01:35:49 2019
exit02            104001     EVPN   10.0.0.42        4001                                       Add        Fri Feb  8 01:35:49 2019
exit02            104001     EVPN   10.0.0.42        4001                                       Add        Fri Feb  8 01:35:49 2019
exit02            104001     EVPN   10.0.0.42        4001                                       Add        Fri Feb  8 01:35:49 2019
exit01            104001     EVPN   10.0.0.41        4001                                       Add        Fri Feb  8 01:35:49 2019
exit01            104001     EVPN   10.0.0.41        4001                                       Add        Fri Feb  8 01:35:49 2019
exit01            104001     EVPN   10.0.0.41        4001                                       Add        Fri Feb  8 01:35:49 2019
exit01            104001     EVPN   10.0.0.41        4001                                       Add        Fri Feb  8 01:35:49 2019
exit01            104001     EVPN   10.0.0.41        4001                                       Add        Fri Feb  8 01:35:49 2019
exit01            104001     EVPN   10.0.0.41        4001                                       Add        Fri Feb  8 01:35:49 2019
exit01            104001     EVPN   10.0.0.41        4001                                       Add        Fri Feb  8 01:35:49 2019
exit01            104001     EVPN   10.0.0.41        4001                                       Add        Fri Feb  8 01:35:49 2019
leaf04            104001     EVPN   10.0.0.134       4001                                       Add        Fri Feb  8 01:35:49 2019
leaf04            104001     EVPN   10.0.0.134       4001                                       Add        Fri Feb  8 01:35:49 2019
leaf04            104001     EVPN   10.0.0.134       4001                                       Add        Fri Feb  8 01:35:49 2019
leaf04            104001     EVPN   10.0.0.134       4001                                       Add        Fri Feb  8 01:35:49 2019
leaf04            104001     EVPN   10.0.0.134       4001                                       Add        Fri Feb  8 01:35:49 2019
leaf04            104001     EVPN   10.0.0.134       4001                                       Add        Fri Feb  8 01:35:49 2019
leaf04            104001     EVPN   10.0.0.134       4001                                       Add        Fri Feb  8 01:35:49 2019
leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        Fri Feb  8 01:35:49 2019
leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        Fri Feb  8 01:35:49 2019
leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        Fri Feb  8 01:35:49 2019
leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        Fri Feb  8 01:35:49 2019
leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        Fri Feb  8 01:35:49 2019
leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        Fri Feb  8 01:35:49 2019
leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        Fri Feb  8 01:35:49 2019
...
```

Consequently, if you looked for the VXLAN configuration and status for last week, you would find either another configuration or no configuration. This example shows that no VXLAN configuration was present.

```
cumulus@switch:~$ netq show vxlan around 7d
No matching vxlan records found
```

You can filter the list of VXLANs to view only those associated with a particular VNI. The VNI option lets you specify a single VNI (100), a range of VNIs (10-100), or provide a comma-separated list (10,11,12). This example shows the configured VXLANs for *VNI 24*.

 ```
cumulus@switch:~$ netq show vxlan vni 24
Matching vxlan records:
Hostname          VNI        Protoc VTEP IP          VLAN   Replication List                    Last Changed
                                ol
----------------- ---------- ------ ---------------- ------ ----------------------------------- -------------------------
leaf01            24         EVPN   10.0.0.112       24     10.0.0.134(leaf04, leaf03)          Fri Feb  8 01:35:49 2019
leaf02            24         EVPN   10.0.0.112       24     10.0.0.134(leaf04, leaf03)          Fri Feb  8 01:35:49 2019
leaf03            24         EVPN   10.0.0.134       24     10.0.0.112(leaf02, leaf01)          Fri Feb  8 01:35:49 2019
leaf04            24         EVPN   10.0.0.134       24     10.0.0.112(leaf02, leaf01)          Fri Feb  8 01:35:49 2019
```

### View the Interfaces Associated with VXLANs

You can view detailed information about the VXLAN interfaces using the `netq show interface` command. You can also view this information for a given device by adding a hostname to the `show` command. 

This example shows the detailed VXLAN interface information for the *leaf02* switch.

 ```
cumulus@switch:~$ netq leaf02 show interfaces type vxlan
Matching link records:
Hostname          Interface                 Type             State      VRF             Details                             Last Changed
----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
leaf02            vni13                     vxlan            up         default         VNI: 13, PVID: 13, Master: bridge,  Fri Feb  8 01:35:49 2019
                                                                                        VTEP: 10.0.0.112, MTU: 9000
leaf02            vni24                     vxlan            up         default         VNI: 24, PVID: 24, Master: bridge,  Fri Feb  8 01:35:49 2019
                                                                                        VTEP: 10.0.0.112, MTU: 9000
leaf02            vxlan4001                 vxlan            up         default         VNI: 104001, PVID: 4001,            Fri Feb  8 01:35:49 2019
                                                                                        Master: bridge, VTEP: 10.0.0.112,
                                                                                        MTU: 1500
```
