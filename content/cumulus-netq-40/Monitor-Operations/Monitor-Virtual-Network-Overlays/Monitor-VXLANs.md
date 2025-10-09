---
title: Monitor VXLANs
author: NVIDIA
weight: 990
toc: 3
---

VXLANs provide a way to create a virtual network on top of layer 2 and layer 3 technologies. Organizations, such as data centers, use them because they require larger scale without additional infrastructure and more flexibility than is available with existing infrastructure equipment.

With NetQ, a network administrator can monitor VXLANs in the data center. NetQ provides the ability to:

- Manage virtual constructs: view the performance and status of VXLANs
- Validate overlay communication paths

It helps answer questions such as:

<!-- vale off -->
- Is my overlay configured and operating correctly?
- Is my control plane configured correctly?
- Can device A reach device B?
<!-- vale on -->

You can monitor your VXLANs using the following commands:

```
netq [<hostname>] show vxlan [vni <text-vni>] [around <text-time>] [json]
netq show interfaces type vxlan [state <remote-interface-state>] [around <text-time>] [json]
netq <hostname> show interfaces type vxlan [state <remote-interface-state>] [around <text-time>] [count] [json]
netq [<hostname>] show events [level info|level error|level warning|level critical|level debug] type vxlan [between <text-time> and <text-endtime>] [json]
```

{{%notice note%}}
When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: weeks
- **d**: days
- **h**: hours
- **m**: minutes
- **s**: seconds
- **now**

For the `between` option, you can enter the start (`<text-time>`) and end time (`text-endtime>`) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{%/notice%}}

## View All VXLANs in Your Network

You can view a list of configured VXLANs for all devices, including the VNI (VXLAN network identifier), protocol, address of associated VTEPs (VXLAN tunnel endpoint), replication list, and the last time it changed. You can also view VXLAN information for a given device by adding a hostname to the `show` command. You can filter the results by VNI.

This example shows all configured VXLANs across the network. In this network, there are three VNIs (13, 24, and 104001) associated with three VLANs (13, 24, 4001), EVPN is the virtual protocol deployed, and the configuration was last changed around 23 hours ago.

```
cumulus@switch:~$ netq show vxlan
Matching vxlan records:
Hostname          VNI        Protoc VTEP IP          VLAN   Replication List                    Last Changed
                                ol
----------------- ---------- ------ ---------------- ------ ----------------------------------- -------------------------
exit01            104001     EVPN   10.0.0.41        4001                                       Fri Feb  8 01:35:49 2019
exit02            104001     EVPN   10.0.0.42        4001                                       Fri Feb  8 01:35:49 2019
leaf01            13         EVPN   10.0.0.112       13     10.0.0.134(leaf04, leaf03)          Fri Feb  8 01:35:49 2019
leaf01            24         EVPN   10.0.0.112       24     10.0.0.134(leaf04, leaf03)          Fri Feb  8 01:35:49 2019
leaf01            104001     EVPN   10.0.0.112       4001                                       Fri Feb  8 01:35:49 2019
leaf02            13         EVPN   10.0.0.112       13     10.0.0.134(leaf04, leaf03)          Fri Feb  8 01:35:49 2019
leaf02            24         EVPN   10.0.0.112       24     10.0.0.134(leaf04, leaf03)          Fri Feb  8 01:35:49 2019
leaf02            104001     EVPN   10.0.0.112       4001                                       Fri Feb  8 01:35:49 2019
leaf03            13         EVPN   10.0.0.134       13     10.0.0.112(leaf02, leaf01)          Fri Feb  8 01:35:49 2019
leaf03            24         EVPN   10.0.0.134       24     10.0.0.112(leaf02, leaf01)          Fri Feb  8 01:35:49 2019
leaf03            104001     EVPN   10.0.0.134       4001                                       Fri Feb  8 01:35:49 2019
leaf04            13         EVPN   10.0.0.134       13     10.0.0.112(leaf02, leaf01)          Fri Feb  8 01:35:49 2019
leaf04            24         EVPN   10.0.0.134       24     10.0.0.112(leaf02, leaf01)          Fri Feb  8 01:35:49 2019
leaf04            104001     EVPN   10.0.0.134       4001                                       Fri Feb  8 01:35:49 2019
```

This example shows the events and configuration changes that occurred on the VXLANs in your network in the last 24 hours. In this case, the change involved adding the EVPN configuration to each of the devices in the last 24 hours.

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

Therefore, if you looked for the VXLAN configuration and status for last week, you would find either another configuration or no configuration. This example shows that no VXLAN configuration was present.

```
cumulus@switch:~$ netq show vxlan around 7d
No matching vxlan records found
```

You can filter the list of VXLANs to view only those associated with a particular VNI. The VNI option lets you specify single VNI (100), a range of VNIs (10-100), or provide a comma-separated list (10,11,12). This example shows the configured VXLANs for *VNI 24*.

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

## View the Interfaces Associated with VXLANs

You can view detailed information about the VXLAN interfaces using the `netq show interface` command. You can also view this information for a given device by adding a hostname to the `show` command. This example shows the detailed VXLAN interface information for the *leaf02* switch.

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
