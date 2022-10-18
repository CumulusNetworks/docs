---
title: VXLAN
author: NVIDIA
weight: 990
toc: 3
---

A network administrator can view the performance and status of VXLANs, as well as validate overlay communication paths with the following commands:

```
netq [<hostname>] show vxlan [vni <text-vni>] [around <text-time>] [json]
netq show interfaces type vxlan [state <remote-interface-state>] [around <text-time>] [json]
netq <hostname> show interfaces type vxlan [state <remote-interface-state>] [around <text-time>] [count] [json]
netq [<hostname>] show events [severity info | severity error ] type vxlan [between <text-time> and <text-endtime>] [json]
```

## View All VXLANs in Your Network

You can view a list of configured VXLANs for all devices, including the VNI (VXLAN network identifier), protocol, address of associated VTEPs (VXLAN tunnel endpoint), replication list, and the last time it changed.

{{<expand "show vxlan">}}

The following example shows all configured VXLANs across the network. In this network, there are three VNIs (13, 24, and 104001) associated with three VLANs (13, 24, 4001), EVPN is the virtual protocol deployed, and the configuration was last changed around 23 hours ago:

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
{{</expand>}}

{{<expand "show events message_type vxlan between now and 24h">}}

This example shows the events and configuration changes that occurred on the VXLANs in your network in the last 24 hours. In this case, the change involved adding the EVPN configuration to each of the devices in the last 24 hours:

```
cumulus@switch:~$ netq show events message_type vxlan between now and 24h
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

Therefore, if you looked for the VXLAN configuration and status for last week, you would find either another configuration or no configuration. In the following example, no VXLAN configuration was present:

```
cumulus@switch:~$ netq show vxlan around 7d
No matching vxlan records found
```
{{</expand>}}

## View VXLANs Associated with a VNI

You can filter the list of VXLANs to view only those associated with a particular VNI. The VNI option lets you specify single VNI (100), a range of VNIs (10-100), or provide a comma-separated list (10,11,12). 

{{<expand "show vxlan vni 24">}}

The following example shows the configured VXLANs for VNI 24:

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
{{</expand>}}
## View the Interfaces Associated with VXLANs

You can view detailed information about the VXLAN interfaces using the `netq show interface` command. You can also view this information for a given device by adding a hostname to the `show` command. 

{{<expand "leaf02 show interfaces type vxlan">}}

The following example shows the detailed VXLAN interface information for the leaf02 switch:

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
{{</expand>}}