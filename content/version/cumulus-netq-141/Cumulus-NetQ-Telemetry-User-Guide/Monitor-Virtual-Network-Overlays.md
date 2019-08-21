---
title: Monitor Virtual Network Overlays
author: Cumulus Networks
weight: 65
aliases:
 - /display/NETQ141/Monitor+Virtual+Network+Overlays
 - /pages/viewpage.action?pageId=10453524
pageID: 10453524
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
With NetQ, a network administrator can monitor virtual network
components in the data center, including VXLAN, EVPN, and LNV software
constructs. NetQ provides the ability to:

  - Manage virtual constructs: view the performance and status of
    VXLANs, EVPN, and LNV
  - Validate overlay communication paths

It helps answer questions such as:

  - Is my overlay configured and operating correctly?
  - Is my control plane configured correctly?
  - Can device A reach device B?

## Monitor Virtual Extensible LANs

Virtual Extensible LANs (VXLANs) provide a way to create a virtual
network on top of layer 2 and layer 3 technologies. It is intended for
organizations, such as data centers, that require larger scale without
additional infrastructure and more flexibility than is available with
existing infrastructure equipment. With NetQ, you can monitor the
current and historical configuration and status of your VXLANs using the
following command:

    netq [<hostname>] show vxlan [vni <text-vni>] [around <text-time>] [json]
    netq [<hostname>] show vxlan [vni <text-vni>] changes [between <text-time> and <text-endtime>] [json]
    netq [<hostname>] show interfaces type vxlan changes [between <text-time> and <text-endtime>] [json]

{{%notice note%}}

When entering a time value, you must include a numeric value *and* the
unit of measure:

  - d: day(s)
  - h: hour(s)
  - m: minute(s)
  - s: second(s)
  - now

For time ranges, the `<text-time>` is the most recent time and the
`<text-endtime>` is the oldest time. The values do not have to have the
same unit of measure.

{{%/notice%}}

### View All VXLANs in Your Network

You can view a list of configured VXLANs for all devices, including the
VNI (VXLAN network identifier), protocol, address of associated VTEPs
(VXLAN tunnel endpoint), replication list (remote VTEP addresses that
receive BUM (Broadcast, Unknown Unicast, Multicast) traffic)), and the
last time it was changed. You can also view VXLAN information for a
given device by adding a hostname to the `show` command. You can filter
the results by VNI.

This example shows all configured VXLANs across the network. In this
network, there are three VNIs (13, 24, and 104001) associated with three
VLANs (13, 24, 4001), EVPN is the virtual protocol deployed, and the
configuration was last changed around 23 hours ago.

    cumulus@switch:~$ netq show vxlan
    Matching vxlan records:
    Hostname          VNI        Protoc VTEP IP          VLAN   Replication List                    Last Changed
                                 ol
    ----------------- ---------- ------ ---------------- ------ ----------------------------------- -------------------------
    exit01            104001     EVPN   10.0.0.41        4001                                       22h:50m:1s
    exit02            104001     EVPN   10.0.0.42        4001                                       22h:49m:38s
    leaf01            13         EVPN   10.0.0.112       13     10.0.0.134(leaf04, leaf03)          23h:43m:1s
    leaf01            24         EVPN   10.0.0.112       24     10.0.0.134(leaf04, leaf03)          23h:43m:1s
    leaf01            104001     EVPN   10.0.0.112       4001                                       23h:43m:1s
    leaf02            13         EVPN   10.0.0.112       13     10.0.0.134(leaf04, leaf03)          22h:56m:22s
    leaf02            24         EVPN   10.0.0.112       24     10.0.0.134(leaf04, leaf03)          22h:56m:22s
    leaf02            104001     EVPN   10.0.0.112       4001                                       22h:56m:22s
    leaf03            13         EVPN   10.0.0.134       13     10.0.0.112(leaf02, leaf01)          22h:55m:33s
    leaf03            24         EVPN   10.0.0.134       24     10.0.0.112(leaf02, leaf01)          22h:55m:33s
    leaf03            104001     EVPN   10.0.0.134       4001                                       22h:55m:33s
    leaf04            13         EVPN   10.0.0.134       13     10.0.0.112(leaf02, leaf01)          22h:52m:12s
    leaf04            24         EVPN   10.0.0.134       24     10.0.0.112(leaf02, leaf01)          22h:52m:12s
    leaf04            104001     EVPN   10.0.0.134       4001                                       22h:52m:12s

This example shows the changes that have been made to VXLANs in your
network in the last 24 hours. In this case, the EVPN configuration was
added to each of the devices in the last 24 hours.

    cumulus@switch:~$ netq show vxlan changes between now and 24h
    Matching vxlan records:
    Hostname          VNI        Protoc VTEP IP          VLAN   Replication List                    DB State   Last Changed
                                 ol
    ----------------- ---------- ------ ---------------- ------ ----------------------------------- ---------- -------------------------
    exit02            104001     EVPN   10.0.0.42        4001                                       Add        23h:3m:8s
    exit02            104001     EVPN   10.0.0.42        4001                                       Add        23h:3m:8s
    exit02            104001     EVPN   10.0.0.42        4001                                       Add        23h:3m:8s
    exit02            104001     EVPN   10.0.0.42        4001                                       Add        23h:3m:8s
    exit02            104001     EVPN   10.0.0.42        4001                                       Add        23h:3m:8s
    exit02            104001     EVPN   10.0.0.42        4001                                       Add        23h:3m:8s
    exit02            104001     EVPN   10.0.0.42        4001                                       Add        23h:3m:8s
    exit01            104001     EVPN   10.0.0.41        4001                                       Add        23h:3m:32s
    exit01            104001     EVPN   10.0.0.41        4001                                       Add        23h:3m:32s
    exit01            104001     EVPN   10.0.0.41        4001                                       Add        23h:3m:32s
    exit01            104001     EVPN   10.0.0.41        4001                                       Add        23h:3m:32s
    exit01            104001     EVPN   10.0.0.41        4001                                       Add        23h:3m:32s
    exit01            104001     EVPN   10.0.0.41        4001                                       Add        23h:3m:32s
    exit01            104001     EVPN   10.0.0.41        4001                                       Add        23h:3m:32s
    exit01            104001     EVPN   10.0.0.41        4001                                       Add        23h:3m:32s
    leaf04            104001     EVPN   10.0.0.134       4001                                       Add        23h:5m:43s
    leaf04            104001     EVPN   10.0.0.134       4001                                       Add        23h:5m:43s
    leaf04            104001     EVPN   10.0.0.134       4001                                       Add        23h:5m:43s
    leaf04            104001     EVPN   10.0.0.134       4001                                       Add        23h:5m:43s
    leaf04            104001     EVPN   10.0.0.134       4001                                       Add        23h:5m:43s
    leaf04            104001     EVPN   10.0.0.134       4001                                       Add        23h:5m:43s
    leaf04            104001     EVPN   10.0.0.134       4001                                       Add        23h:5m:43s
    leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        23h:5m:43s
    leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        23h:5m:43s
    leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        23h:5m:43s
    leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        23h:5m:43s
    leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        23h:5m:43s
    leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        23h:5m:43s
    leaf04            13         EVPN   10.0.0.134       13     10.0.0.112()                        Add        23h:5m:43s
    ...

Consequently, if you looked for the VXLAN configuration and status for
last week, you would find either another configuration or no
configuration. This example shows that no VXLAN configuration was
present.

    cumulus@switch:~$ netq show vxlan around 7d
     
    No matching vxlan records found

You can filter the list of VXLANs to view only those associated with a
particular VNI. This example shows the configured VXLANs for *VNI 24*.

    cumulus@switch:~$ netq show vxlan vni 24
    Matching vxlan records:
    Hostname          VNI        Protoc VTEP IP          VLAN   Replication List                    Last Changed
                                 ol
    ----------------- ---------- ------ ---------------- ------ ----------------------------------- -------------------------
    leaf01            24         EVPN   10.0.0.112       24     10.0.0.134(leaf04, leaf03)          1d:0h:4m:12s
    leaf02            24         EVPN   10.0.0.112       24     10.0.0.134(leaf04, leaf03)          23h:17m:33s
    leaf03            24         EVPN   10.0.0.134       24     10.0.0.112(leaf02, leaf01)          23h:16m:44s
    leaf04            24         EVPN   10.0.0.134       24     10.0.0.112(leaf02, leaf01)          23h:13m:23s

### View the Interfaces Associated with VXLANs

You can view detailed information about the VXLAN interfaces using the
netq show interface command. You can also view this information for a
given device by adding a hostname to the `show` command. This example
shows the detailed VXLAN interface information for the leaf02 switch.

    cumulus@switch:~$ netq leaf02 show interfaces type vxlan
    Matching link records:
    Hostname          Interface                 Type             State      VRF             Details                             Last Changed
    ----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
    leaf02            vni13                     vxlan            up         default         VNI: 13, PVID: 13, Master: bridge,  23h:23m:11s
                                                                                            VTEP: 10.0.0.112, MTU: 9000
    leaf02            vni24                     vxlan            up         default         VNI: 24, PVID: 24, Master: bridge,  23h:23m:11s
                                                                                            VTEP: 10.0.0.112, MTU: 9000
    leaf02            vxlan4001                 vxlan            up         default         VNI: 104001, PVID: 4001,            23h:23m:11s
                                                                                            Master: bridge, VTEP: 10.0.0.112,
                                                                                            MTU: 1500

## Monitor EVPN

EVPN (Ethernet Virtual Private Network) enables network administrators
in the data center to deploy a virtual layer 2 bridge overlay on top of
layer 3 IP networks creating access, or tunnel, between two locations.
This connects devices in different layer 2 domains or sites running
VXLANs and their associated underlays. With NetQ, you can monitor the
configuration and status of the EVPN setup using the `netq show evpn`
command. You can filter the EVPN information by a VNI (VXLAN network
identifier), and view the current information or for a time in the past.
The command also enables visibility into changes that have occurred in
the configuration during a specific timeframe. The syntax for the
command is:

    netq [<hostname>] show evpn [vni <text-vni>] changes [between <text-time> and <text-endtime>] [json]
    netq [<hostname>] show evpn [vni <text-vni>] [around <text-time>] [json]

{{%notice note%}}

When entering a time value, you must include a numeric value *and* the
unit of measure:

  - d: day(s)
  - h: hour(s)
  - m: minute(s)
  - s: second(s)
  - now

For time ranges, the `<text-time>` is the most recent time and the
`<text-endtime>` is the oldest time. The values do not have to have the
same unit of measure.

{{%/notice%}}

For more information about and configuration of EVPN in your data
center, refer to the [Cumulus Linux EVPN](https://docs.cumulusnetworks.com/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/) topic.

### View the Status of EVPN

You can view the configuration and status of your EVPN overlay across
your network or for a particular device. This example shows the
configuration and status for all devices, including the associated VNI,
VTEP address, the import and export route (showing the BGP ASN and VNI
path), and the last time a change was made for each device running EVPN.
Use the *hostname* variable to view the configuration and status for a
single device.

    cumulus@switch:~$ netq show evpn
    Matching evpn records:
    Hostname          VNI        VTEP IP          In Kernel Export RT        Import RT        Last Changed
    ----------------- ---------- ---------------- --------- ---------------- ---------------- -------------------------
    exit01            104001     10.0.0.41        yes       65041:104001     65041:104001     3d:17h:20m:10s
    exit02            104001     10.0.0.42        yes       65042:104001     65042:104001     3d:17h:19m:48s
    leaf01            13         10.0.0.112       yes       65011:13         65011:13         3d:18h:13m:12s
    leaf01            24         10.0.0.112       yes       65011:24         65011:24         3d:18h:13m:12s
    leaf01            104001     10.0.0.112       yes       65011:104001     65011:104001     3d:18h:13m:12s
    leaf02            13         10.0.0.112       yes       65012:13         65012:13         3d:17h:26m:31s
    leaf02            24         10.0.0.112       yes       65012:24         65012:24         3d:17h:26m:31s
    leaf02            104001     10.0.0.112       yes       65012:104001     65012:104001     3d:17h:26m:31s
    leaf03            13         10.0.0.134       yes       65013:13         65013:13         3d:17h:25m:42s
    leaf03            24         10.0.0.134       yes       65013:24         65013:24         3d:17h:25m:42s
    leaf03            104001     10.0.0.134       yes       65013:104001     65013:104001     3d:17h:25m:42s
    leaf04            13         10.0.0.134       yes       65014:13         65014:13         3d:17h:22m:22s
    leaf04            24         10.0.0.134       yes       65014:24         65014:24         3d:17h:22m:22s
    leaf04            104001     10.0.0.134       yes       65014:104001     65014:104001     3d:17h:22m:22s

### View the Status of EVPN for a Given VNI

You can filter the full device view to focus on a single VNI. This
example only shows the EVPN configuration and status for VNI 24.

    cumulus@switch:~$ netq show evpn vni 24
    Matching evpn records:
    Hostname          VNI        VTEP IP          In Kernel Export RT        Import RT        Last Changed
    ----------------- ---------- ---------------- --------- ---------------- ---------------- -------------------------
    leaf01            24         10.0.0.112       yes       65011:24         65011:24         3d:18h:37m:23s
    leaf02            24         10.0.0.112       yes       65012:24         65012:24         3d:17h:50m:43s
    leaf03            24         10.0.0.134       yes       65013:24         65013:24         3d:17h:49m:53s
    leaf04            24         10.0.0.134       yes       65014:24         65014:24         3d:17h:46m:34s

### View Changes to the EVPN Configuration

You can view the changes that have been made to your EVPN configuration
within the last hour or within a given timeframe. Perhaps you are seeing
errors related to EVPN and you suspect a configuration change may be the
cause. You can find out if any changes were made and when using the
*changes* keyword. This example shows the changes made in the last hour
(none) and the changes made in the last 7 days (the addition of EVPN on
the leaf switches and exit switches).

    cumulus@switch:~$ netq show evpn changes between now and 7d
    Matching evpn records:
    Hostname          VNI        VTEP IP          In Kernel Export RT        Import RT        DB State   Last Changed
    ----------------- ---------- ---------------- --------- ---------------- ---------------- ---------- -------------------------
    exit02            104001     10.0.0.42        yes       65042:104001     65042:104001     Add        3d:17h:46m:59s
    exit01            104001     10.0.0.41        yes       65041:104001     65041:104001     Add        3d:17h:47m:21s
    leaf04            104001     10.0.0.134       yes       65014:104001     65014:104001     Add        3d:17h:49m:33s
    leaf04            13         10.0.0.134       yes       65014:13         65014:13         Add        3d:17h:49m:33s
    leaf04            24         10.0.0.134       yes       65014:24         65014:24         Add        3d:17h:49m:33s
    leaf03            104001     10.0.0.134       yes       65013:104001     65013:104001     Add        3d:17h:52m:53s
    leaf03            13         10.0.0.134       yes       65013:13         65013:13         Add        3d:17h:52m:53s
    leaf03            24         10.0.0.134       yes       65013:24         65013:24         Add        3d:17h:52m:53s
    leaf02            104001     10.0.0.112       yes       65012:104001     65012:104001     Add        3d:17h:53m:42s
    leaf02            13         10.0.0.112       yes       65012:13         65012:13         Add        3d:17h:53m:42s
    leaf02            24         10.0.0.112       yes       65012:24         65012:24         Add        3d:17h:53m:42s
    leaf01            104001     10.0.0.112       yes       65011:104001     65011:104001     Add        3d:18h:40m:23s
    leaf01            13         10.0.0.112       yes       65011:13         65011:13         Add        3d:18h:40m:23s
    leaf01            24         10.0.0.112       yes       65011:24         65011:24         Add        3d:18h:40m:23s

## Monitor LNV

Lightweight Network Virtualization (LNV) is a technique for deploying
VXLANs without a central controller on bare metal switches. LNV enables
data center network administrators and operators to create a data path
between bridges on top of a layer 3 fabric. With NetQ, you can monitor
the configuration and status of the LNV setup using the `netq show lnv`
command. You can view the current information or for a time in the past.
The command also enables visibility into changes that have occurred in
the configuration during a specific timeframe. The syntax for the
command is:

    netq [<hostname>] show lnv [around <text-time>] [json]
    netq [<hostname>] show lnv changes [between <text-time> and <text-endtime>] [json]

### View LNV Status

You can view the configuration and status of your LNV overlay across
your network or for a particular device. This example shows the
configuration and status of LNV across the network, including the role
each node plays, replication mode, number of peers and VNIs, and the
last time the configuration was changed.

    cumulus@switch:~$ netq show lnv
    Matching LNV session records are:
    Hostname          Role       ReplMode State      #Peers #VNIs  Last Changed
    ----------------- ---------- -------- ---------- ------ ------ -------------------------
    spine-1           SND        HER      up         3      6      45m:26.865s
    spine-2           SND        HER      up         3      6      45m:23.299s
    spine-3           SND        HER      up         3      6      45m:21.847s
    tor-1             RD         HER      up         4      6      45m:25.335s
    tor-2             RD         HER      up         4      6      45m:6.495s
    torc-11           RD         HER      up         0      0      17.258785s
    torc-12           RD         HER      up         4      6      45m:16.800s
    torc-21           RD         HER      up         4      6      45m:29.437s
    torc-22           RD         HER      up         4      6      45m:11.440s

### View LNV Status in the Past

You can view the status in the past using either the around or changes
keywords. This example shows the status of LNV about 30 minutes ago.

    cumulus@switch:~$ netq show lnv around 30m
    Matching LNV session records are:
    Hostname          Role       ReplMode State      #Peers #VNIs  Last Changed
    ----------------- ---------- -------- ---------- ------ ------ -------------------------
    spine-1           SND        HER      up         3      6      45m:37.973s
    spine-2           SND        HER      up         3      6      45m:34.407s
    spine-3           SND        HER      up         3      6      45m:32.955s
    tor-1             RD         HER      up         4      6      45m:36.443s
    tor-2             RD         HER      up         4      6      45m:17.603s
    torc-11           RD         HER      up         4      6      45m:46.696s
    torc-12           RD         HER      up         4      6      45m:27.908s
    torc-21           RD         HER      up         4      6      45m:40.546s
    torc-22           RD         HER      up         4      6      45m:22.548s

For more information about and configuration of LNV, refer to the
[Cumulus Linux LNV Overview](https://docs.cumulusnetworks.com/cumulus-linux/Network-Virtualization/Lightweight-Network-Virtualization-Overview/) topic.

## View Communication Paths between Devices

You can view the available paths between devices that communicate over
virtual constructs using the netq trace command. The syntax of this
command is:

    netq trace <mac> [vlan <1-4096>] from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [bidir] [json|detail|pretty] [debug]
    netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [bidir] [json|detail|pretty] [debug]

This example shows the available paths between leaf01 and leaf03 which
are connected through an EVPN overlay. This example uses the default
presentation of *detail* output.

    cumulus@switch:~$ netq trace 10.0.0.13 from leaf01 
    Number of Paths: 2
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9216
     
    Id  Hop Hostname    InPort          InTun, RtrIf    OutRtrIf, Tun   OutPort
    --- --- ----------- --------------- --------------- --------------- ---------------
    1   1   leaf01                                      swp52           swp52
        2   spine02     swp1            swp1            swp3            swp3
        3   leaf03      swp52           swp52                           lo
    --- --- ----------- --------------- --------------- --------------- ---------------
    2   1   leaf01                                      swp51           swp51
        2   spine01     swp1            swp1            swp3            swp3
        3   leaf03      swp51           swp51                           lo
    --- --- ----------- --------------- --------------- --------------- ---------------

You can also view the paths in both directions, to and from the two
devices, as shown in this example using the *pretty* output option.

    cumulus@switch:~$ netq trace 10.0.0.13 from leaf01 bidir pretty
    Number of Paths: 2
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9216
     
     leaf01 swp52 -- swp1 spine02 swp3 -- swp52 leaf03 lo 
     leaf01 swp51 -- swp1 spine01 swp3 -- swp51 leaf03 lo 
     
    Number of Paths: 2
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9216 
     
     leaf03 swp52 -- swp3 spine02 swp1 -- swp52 leaf01  
     leaf03 swp51 -- swp3 spine01 swp1 -- swp51 leaf01

For more information about the trace command, run the `netq example
trace` command.

    cumulus@switch:~$ netq example trace
     
    Control Path Trace
    ==================
     
    Commands
    ========
       netq trace <mac> [vlan <1-4096>] from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [bidir] [json|detail|pretty] [debug]
       netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [bidir] [json|detail|pretty] [debug]
     
    Usage
    =====
    netq trace provides control path tracing (no real packets are sent) from
    a specified source to a specified destination. The trace covers complete
    end-to-end path tracing including bridged, routed and Vxlan overlay paths.
    ECMP is supported as well as checking for forwarding loops, MTU consistency
    across all paths, and VLAN consistency across all paths.  Reverse path
    trace is also available as an option.
     
    Trace output can be generated in multiple formats.
    ...
