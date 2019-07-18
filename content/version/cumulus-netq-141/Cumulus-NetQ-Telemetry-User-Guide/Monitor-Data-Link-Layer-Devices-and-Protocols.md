---
title: Monitor Data Link Layer Devices and Protocols
author: Cumulus Networks
weight: 61
aliases:
 - /display/NETQ141/Monitor-Data-Link-Layer-Devices-and-Protocols
 - /pages/viewpage.action?pageId=10453521
pageID: 10453521
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
With NetQ, a network administrator can monitor OSI Layer 2 devices and
protocols, including switches, bridges, link control, and physical media
access. Keeping track of the various data link layer devices in your
network ensures consistent and error-free communications between
devices. NetQ provides the ability to:

  - Monitor and validate device and protocol configurations

  - View available communication paths between devices

It helps answer questions such as:

  - Is a VLAN misconfigured?

  - Is there an MTU mismatch in my network?

  - Is MLAG configured correctly?

  - Is there an STP loop?

  - Can device A reach device B using MAC addresses?

## <span>Monitor LLDP Operation</span>

LLDP is <span style="color: #545454;"> used by network devices for
advertising their identity, capabilities, and neighbors on a LAN. You
can view this information for one or more devices. You can also view the
information at an earlier point in time or view changes that have
occurred to the information during a specified timeframe. NetQ enables
you to view LLDP information for your devices using the `netq show lldp`
command. The syntax for this command is: </span>

    netq [<hostname>] show lldp [<remote-physical-interface>] [around <text-time>] [json]
    netq [<hostname>] show lldp [<remote-physical-interface>] changes [between <text-time> and <text-endtime>] [json]

### <span>View LLDP Information for All Devices</span>

<span style="color: #545454;"> This example shows the interface and peer
information that is advertised for each device. </span>

    cumulus@switch:~$ netq show lldp 
     
    Matching lldp records:
    Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ----------------- ------------------------- -------------------------
    leaf01            eth0                      oob-mgmt-switch   swp6                      4h:22m:57s
    leaf01            swp1                      server01          eth1                      4h:15m:40s
    leaf01            swp51                     spine01           swp1                      4h:16m:12s
    leaf01            swp52                     spine02           swp1                      4h:16m:12s
    leaf02            eth0                      oob-mgmt-switch   swp7                      4h:22m:53s
    leaf02            swp2                      server02          eth2                      4h:15m:38s
    leaf02            swp51                     spine01           swp2                      4h:16m:9s
    leaf02            swp52                     spine02           swp2                      4h:16m:9s
    leaf03            eth0                      oob-mgmt-switch   swp8                      4h:23m:5s
    leaf03            swp1                      server03          eth1                      4h:15m:50s
    leaf03            swp51                     spine01           swp3                      4h:16m:21s
    leaf03            swp52                     spine02           swp3                      4h:16m:21s
    leaf04            eth0                      oob-mgmt-switch   swp9                      4h:23m:1s
    leaf04            swp2                      server04          eth2                      4h:15m:46s
    leaf04            swp51                     spine01           swp4                      4h:16m:17s
    leaf04            swp52                     spine02           swp4                      4h:16m:17s
    oob-mgmt-server   eth1                      oob-mgmt-switch   swp1                      4h:23m:4s
    server01          eth0                      oob-mgmt-switch   swp2                      4h:23m:8s
    server01          eth1                      leaf01            swp1                      4h:15m:28s
    server02          eth0                      oob-mgmt-switch   swp3                      4h:22m:59s
    server02          eth2                      leaf02            swp2                      4h:15m:29s
    server03          eth0                      oob-mgmt-switch   swp4                      4h:23m:5s
    server03          eth1                      leaf03            swp1                      4h:15m:28s
    server04          eth0                      oob-mgmt-switch   swp5                      4h:23m:2s
    server04          eth2                      leaf04            swp2                      4h:15m:28s
    spine01           eth0                      oob-mgmt-switch   swp10                     4h:23m:6s
    spine01           swp1                      leaf01            swp51                     4h:16m:22s
    spine01           swp2                      leaf02            swp51                     4h:16m:22s
    spine01           swp3                      leaf03            swp51                     4h:16m:22s
    spine01           swp4                      leaf04            swp51                     4h:16m:22s
    spine02           eth0                      oob-mgmt-switch   swp11                     4h:23m:7s
    spine02           swp1                      leaf01            swp52                     4h:16m:22s
    spine02           swp2                      leaf02            swp52                     4h:16m:22s
    spine02           swp3                      leaf03            swp52                     4h:16m:22s
    spine02           swp4                      leaf04            swp52                     4h:16m:22s

### <span>View Changes to LLDP Information </span>

<span style="color: #545454;"> If you are experiencing a connectivity
issue with a particular device, using the `changes` keyword can help
determine if a configuration change might be a cause.
<span style="color: #545454;"> If no changes are found, a </span> *No
matching lldp records found* <span style="color: #545454;"> message is
displayed. </span> </span>

<span style="color: #545454;"> This example shows the current LLDP
information and all changes that have occurred in the LLDP information
for *tor-1*. </span>

    cumulus@switch:~$ netq tor-1 show lldp
    Matching lldp records:
    Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ----------------- ------------------------- -------------------------
    tor-1             swp1                      noc-pr            swp4                      30m:21.735s
    tor-1             swp2                      noc-se            swp4                      30m:21.735s
    tor-1             swp3                      spine-1           swp7                      30m:21.735s
    tor-1             swp4                      spine-2           swp7                      30m:21.735s
    tor-1             swp5                      spine-3           swp7                      30m:21.735s
    tor-1             swp6                      hosts-11          mac:00:02:00:00:00:27     25m:42.653s
    tor-1             swp7                      hosts-12          swp1                      30m:21.734s
    tor-1             swp8                      hosts-13          mac:00:02:00:00:00:2d     25m:42.651s
     
    cumulus@switch:~$ netq tor-1 show lldp changes
    Matching lldp records:
    Hostname          Interface                 Peer Hostname     Peer Interface            DB State   Last Changed
    ----------------- ------------------------- ----------------- ------------------------- ---------- -------------------------
    tor-1             swp8                      hosts-13          mac:00:02:00:00:00:2d     Add        25m:45.593s
    tor-1             swp6                      hosts-11          mac:00:02:00:00:00:27     Add        25m:45.595s
    tor-1             swp8                      hosts-13          mac:00:02:00:00:00:2d     Del        26m:17.954s
    tor-1             swp6                      hosts-11          mac:00:02:00:00:00:27     Del        26m:17.965s
    tor-1             swp8                      hosts-13          mac:00:02:00:00:00:2d     Add        26m:17.100s
    tor-1             swp6                      hosts-11          mac:00:02:00:00:00:27     Add        26m:17.101s
    tor-1             swp6                      hosts-11          mac:00:02:00:00:00:27     Add        27m:19.630s
    tor-1             swp6                      hosts-11          mac:00:02:00:00:00:27     Del        27m:49.517s
    tor-1             swp6                      hosts-11          mac:00:02:00:00:00:27     Add        27m:49.522s
    tor-1             swp8                      hosts-13          mac:00:02:00:00:00:2d     Add        30m:24.676s
    tor-1             swp7                      hosts-12          swp1                      Add        30m:24.677s
    tor-1             swp6                      hosts-11          mac:00:02:00:00:00:27     Add        30m:24.677s
    tor-1             swp5                      spine-3           swp7                      Add        30m:24.677s
    tor-1             swp4                      spine-2           swp7                      Add        30m:24.677s
    tor-1             swp3                      spine-1           swp7                      Add        30m:24.677s
    tor-1             swp2                      noc-se            swp4                      Add        30m:24.678s
    tor-1             swp1                      noc-pr            swp4                      Add        30m:24.678s

## <span>Check for MTU Inconsistencies</span>

The maximum transmission unit (MTU) determines the largest size packet
or frame that can be transmitted across a given communication link. When
the MTU is not configured to the same value on both ends of the link,
communication problems can occur. With NetQ, you can verify that the MTU
is correctly specified for each link using the netq check mtu command.

This example shows that four switches have inconsistently specified link
MTUs. Now the network administrator or operator can reconfigure the
switches and eliminate the communication issues associated with this
misconfiguration.

    cumulus@switch:~$ netq check mtu
    Checked Nodes: 15, Checked Links: 215, Failed Nodes: 4, Failed Links: 8
    MTU mismatch found on following links
    Hostname          Interface                 MTU    Peer              Peer Interface            Peer MTU Error
    ----------------- ------------------------- ------ ----------------- ------------------------- -------- ---------------
    spine01           swp30                     9216   exit01            swp51                     1500     MTU Mismatch
    exit01            swp51                     1500   spine01           swp30                     9216     MTU Mismatch
    spine01           swp29                     9216   exit02            swp51                     1500     MTU Mismatch
    exit02            swp51                     1500   spine01           swp29                     9216     MTU Mismatch
    exit01            swp52                     1500   spine02           swp30                     9216     MTU Mismatch
    spine02           swp30                     9216   exit01            swp52                     1500     MTU Mismatch
    spine02           swp29                     9216   exit02            swp52                     1500     MTU Mismatch
    exit02            swp52                     1500   spine02           swp29                     9216     MTU Mismatch

## <span>Monitor VLAN Configurations</span>

<span style="color: #36424a;"> </span> A VLAN (Virtual Local Area
Network) enables devices on one or more LANs to communicate as if they
were on the same network, without being physically connected. The VLAN
<span style="color: #545454;"> enables network administrators to
partition a network for functional or security requirements without
changing physical infrastructure. With NetQ, you can view the operation
of VLANs for one or all devices. You can also view the information at an
earlier point in time or view changes that have occurred to the
information during a specified timeframe. NetQ enables you to view basic
VLAN information for your devices using the `netq show vlan` command.
Additional show commands enable you to view VLAN information associated
with interfaces and MAC addresses. The syntax for these commands is:
</span>

    netq [<hostname>] show vlan [<1-4096>] [around <text-time>] [json]
    netq [<hostname>] show vlan [<1-4096>] changes [between <text-time> and <text-endtime>] [json]
    netq [<hostname>] show interfaces type (macvlan|vlan) [state <remote-interface-state>] [around <text-time>] [count] [json]
    netq [<hostname>] show interfaces type (macvlan|vlan) changes [between <text-time> and <text-endtime>] [json]
    netq [<hostname>] show macs [<mac>] [vlan <1-4096>] [origin] [around <text-time>] [json]
    netq [<hostname>] show macs [<mac>] [vlan <1-4096>] [around <text-time>] count [json]
    netq [<hostname>] show macs [<mac>] [vlan <1-4096>] [origin] changes [between <text-time> and <text-endtime>] [json]
    netq <hostname> show macs egress-port <egress-port> [<mac>] [vlan <1-4096>] [origin] [around <text-time>] [json]
    netq <hostname> show macs egress-port <egress-port> [<mac>] [vlan <1-4096>] [origin] changes [between <text-time> and <text-endtime>] [json]

{{%notice info%}}

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

### <span>View VLAN Information for All Devices</span>

<span style="color: #545454;"> This example shows the VLANs configured
across your network. </span>

    cumulus@switch:~$ netq show vlan
    Matching vlan records:
    Hostname          VLANs                     SVIs                      Last Changed
    ----------------- ------------------------- ------------------------- -------------------------
    exit01            4001                      4001                      19h:31m:35s
    exit02            4001                      4001                      19h:31m:11s
    leaf01            1,13,24,4001              13 24 4001                20h:24m:35s
    leaf02            1,13,24,4001              13 24 4001                19h:37m:56s
    leaf03            1,13,24,4001              13 24 4001                19h:37m:6s
    leaf04            1,13,24,4001              13 24 4001                19h:33m:46s

### <span>View Changes to VLAN Information </span>

<span style="color: #545454;"> If you are experiencing a connectivity
issue with a particular device, using the `changes` keyword can help
determine if a configuration change might be a cause. If no changes are
found, a *No matching vlan records found* message is displayed. </span>

{{%notice info%}}

When no timeframe is specified for the changes keyword, the default
value, *between now and 1h*, is used.

{{%/notice%}}

<span style="color: #545454;"> This example shows all changes that have
occurred for all VLANs in the last hour. </span>

    cumulus@switch:~$ netq show vlan changes
    No matching vlan records found

<span style="color: #545454;"> This example shows all changes that have
occurred for all VLANs on the network in the past two days. </span>

    cumulus@switch:~$ netq show vlan changes between now and 2d
    Matching vlan records:
    Hostname          VLANs                     SVIs                      DB State   Last Changed
    ----------------- ------------------------- ------------------------- ---------- -------------------------
    exit02            4001                      4001                      Add        19h:33m:10s
    exit01            4001                      4001                      Add        19h:33m:33s
    leaf04            1,13,24,4001              13 24 4001                Add        19h:35m:45s
    leaf03            1,13,24,4001              13 24 4001                Add        19h:39m:5s
    leaf02            1,13,24,4001              13 24 4001                Add        19h:39m:54s
    leaf01            1,13,24,4001              13 24 4001                Add        20h:26m:34s

### <span>View VLAN Interface Information</span>

You can view the current or past state of the interfaces associated with
VLANs using the `netq show interfaces` command. This provides the status
of the interface, its specified MTU, whether it is running over a VRF,
and the last time it was changed.

    cumulus@switch:~$ netq show interfaces type vlan 
    Matching link records:
    Hostname          Interface                 Type             State      VRF             Details                             Last Changed
    ----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
    exit01            vlan4001                  vlan             up         vrf1            MTU:1500                            19h:35m:46s
    exit02            vlan4001                  vlan             up         vrf1            MTU:1500                            19h:35m:23s
    leaf01            peerlink.4094             vlan             up         default         MTU:9000                            20h:28m:47s
    leaf01            vlan13                    vlan             up         vrf1            MTU:1500                            20h:28m:47s
    leaf01            vlan24                    vlan             up         vrf1            MTU:1500                            20h:28m:47s
    leaf01            vlan4001                  vlan             up         vrf1            MTU:1500                            20h:28m:47s
    leaf02            peerlink.4094             vlan             up         default         MTU:9000                            19h:42m:7s
    leaf02            vlan13                    vlan             up         vrf1            MTU:1500                            19h:42m:7s
    leaf02            vlan24                    vlan             up         vrf1            MTU:1500                            19h:42m:7s
    leaf02            vlan4001                  vlan             up         vrf1            MTU:1500                            19h:42m:7s
    leaf03            peerlink.4094             vlan             up         default         MTU:9000                            19h:41m:18s
    leaf03            vlan13                    vlan             up         vrf1            MTU:1500                            19h:41m:18s
    leaf03            vlan24                    vlan             up         vrf1            MTU:1500                            19h:41m:18s
    leaf03            vlan4001                  vlan             up         vrf1            MTU:1500                            19h:41m:18s
    leaf04            peerlink.4094             vlan             up         default         MTU:9000                            19h:37m:58s
    leaf04            vlan13                    vlan             up         vrf1            MTU:1500                            19h:37m:58s
    leaf04            vlan24                    vlan             up         vrf1            MTU:1500                            19h:37m:58s
    leaf04            vlan4001                  vlan             up         vrf1            MTU:1500                            19h:37m:58s

### <span>View MAC Addresses Associated with a VLAN</span>

You can determine the MAC addresses associated with a given VLAN using
the `netq show macs vlan` command. The command also provides the
hostname of the devices, the egress port for the interface, whether the
MAC address originated from the given device, whether it learns the MAC
address from the peer (remote=yes), and the last time the configuration
was changed.

This example shows the MAC addresses associated with *VLAN13*.

    cumulus@switch:~$ netq show macs vlan 13 
    Matching mac records:
    Origin MAC Address        VLAN   Hostname          Egress Port          Remote Last Changed
    ------ ------------------ ------ ----------------- -------------------- ------ -------------------------
    no     00:03:00:11:11:01  13     leaf01            bond01:server01      no     20h:31m:23s
    no     00:03:00:11:11:01  13     leaf02            bond01:server01      no     19h:44m:44s
    no     00:03:00:11:11:01  13     leaf03            vni13:leaf01         yes    19h:43m:55s
    no     00:03:00:11:11:01  13     leaf04            vni13:leaf01         yes    19h:40m:34s
    no     00:03:00:33:33:01  13     leaf01            vni13:10.0.0.134     yes    20h:31m:23s
    no     00:03:00:33:33:01  13     leaf02            vni13:10.0.0.134     yes    19h:44m:44s
    no     00:03:00:33:33:01  13     leaf03            bond03:server03      no     19h:43m:55s
    no     00:03:00:33:33:01  13     leaf04            bond03:server03      no     19h:40m:34s
    no     02:03:00:11:11:01  13     leaf01            bond01:server01      no     20h:31m:23s
    no     02:03:00:11:11:01  13     leaf02            bond01:server01      no     19h:44m:44s
    no     02:03:00:11:11:01  13     leaf03            vni13:leaf01         yes    19h:43m:55s
    no     02:03:00:11:11:01  13     leaf04            vni13:leaf01         yes    19h:40m:34s
    no     02:03:00:11:11:02  13     leaf01            bond01:server01      no     20h:31m:23s
    no     02:03:00:11:11:02  13     leaf02            bond01:server01      no     19h:44m:44s
    no     02:03:00:11:11:02  13     leaf03            vni13:leaf01         yes    19h:43m:55s
    no     02:03:00:11:11:02  13     leaf04            vni13:leaf01         yes    19h:40m:34s
    no     02:03:00:33:33:01  13     leaf01            vni13:10.0.0.134     yes    20h:31m:23s
    no     02:03:00:33:33:01  13     leaf02            vni13:10.0.0.134     yes    19h:44m:44s
    no     02:03:00:33:33:01  13     leaf03            bond03:server03      no     19h:43m:55s
    no     02:03:00:33:33:01  13     leaf04            bond03:server03      no     19h:40m:34s
    no     02:03:00:33:33:02  13     leaf01            vni13:10.0.0.134     yes    20h:31m:23s
    no     02:03:00:33:33:02  13     leaf02            vni13:10.0.0.134     yes    19h:44m:44s
    no     02:03:00:33:33:02  13     leaf03            bond03:server03      no     19h:43m:55s
    no     02:03:00:33:33:02  13     leaf04            bond03:server03      no     19h:40m:34s
    yes    44:38:39:00:00:03  13     leaf01            bridge               no     20h:31m:23s
    yes    44:38:39:00:00:15  13     leaf02            bridge               no     19h:44m:44s
    yes    44:38:39:00:00:23  13     leaf03            bridge               no     19h:43m:55s
    yes    44:38:39:00:00:5c  13     leaf04            bridge               no     19h:40m:34s
    yes    44:39:39:ff:00:13  13     leaf01            bridge               no     20h:31m:23s
    yes    44:39:39:ff:00:13  13     leaf02            bridge               no     19h:44m:44s
    yes    44:39:39:ff:00:13  13     leaf03            bridge               no     19h:43m:55s
    yes    44:39:39:ff:00:13  13     leaf04            bridge               no     19h:40m:34s

### <span>View MAC Addresses Associated with an Egress Port</span>

You can filter that information down to just the MAC addresses that are
associated with a given VLAN that use a particular egress port. This
example shows MAC addresses associated with the *leaf03* switch and
*VLAN 13* that use the *bridge* port.

    cumulus@switch:~$ netq leaf03 show macs egress-port bridge vlan 13
    Matching mac records:
    Origin MAC Address        VLAN   Hostname          Egress Port          Remote Last Changed
    ------ ------------------ ------ ----------------- -------------------- ------ -------------------------
    yes    44:38:39:00:00:23  13     leaf03            bridge               no     20h:46m:17s
    yes    44:39:39:ff:00:13  13     leaf03            bridge               no     20h:46m:17s

### <span>View the MAC Addresses Associated with VRR Configurations</span>

You can view all of the MAC addresses associated with your VRR (virtual
router reflector) interface configuration using the `netq show
interfaces type macvlan` command. This is useful for determining if the
specified MAC address inside a VLAN is the same or different across your
VRR configuration.

    cumulus@switch:~$ netq show interfaces type macvlan
    Matching link records:
    Hostname          Interface                 Type             State      VRF             Details                             Last Changed
    ----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
    leaf01            vlan13-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:13,             21h:37m:14s
                                                                                            Mode: Private
    leaf01            vlan24-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:24,             21h:37m:14s
                                                                                            Mode: Private
    leaf02            vlan13-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:13,             20h:50m:35s
                                                                                            Mode: Private
    leaf02            vlan24-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:24,             20h:50m:35s
                                                                                            Mode: Private
    leaf03            vlan13-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:13,             20h:49m:45s
                                                                                            Mode: Private
    leaf03            vlan24-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:24,             20h:49m:45s
                                                                                            Mode: Private
    leaf04            vlan13-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:13,             20h:46m:25s
                                                                                            Mode: Private
    leaf04            vlan24-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:24,             20h:46m:25s
                                                                                            Mode: Private

## <span>Monitor MLAG Configurations</span>

Multi-Chassis Link Aggregation (MLAG) is used to enable a server or
switch with a two-port bond (such as a link aggregation group/LAG,
EtherChannel, port group or trunk) to connect those ports to different
switches and operate as if they are connected to a single, logical
switch. This provides greater redundancy and greater system throughput.
Dual-connected devices can create LACP bonds that contain links to each
physical switch. Therefore, active-active links from the dual-connected
devices are supported even though they are connected to two different
physical switches.

{{%notice tip%}}

**MLAG or CLAG?**

The Cumulus Linux implementation of MLAG is referred to by other vendors
as CLAG, MC-LAG or VPC. You will even see references to CLAG in Cumulus
Linux, including the management daemon, named `clagd`, and other options
in the code, such as `clag-id`, which exist for historical purposes. The
Cumulus Linux implementation is truly a multi-chassis link aggregation
protocol, so we call it MLAG.

{{%/notice%}}

For instructions on configuring MLAG, refer to the
[MLAG](/cumulus-linux/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/) topic in
the Cumulus Linux User Guide.

With NetQ, you can view the configuration and operation of devices using
MLAG using the `netq show clag` command. You can view the current
configuration and the configuration at a prior point in time, as well as
view any changes that have been made within a timeframe. The syntax for
the show command is:

    netq [<hostname>] show clag [around <text-time>] [json]
    netq [<hostname>] show clag changes [between <text-time> and <text-endtime>] [json]

### <span>View MLAG Configuration and Status for all Devices</span>

This example shows the configuration and status of MLAG for all devices.
In this case, three MLAG pairs are seen between torc-11 and torc-12
(which happens to be down), noc-pr(P) and noc-se, and torc-21(P) and
torc-22.

    cumulus@ts:~$ netq show clag
    Matching CLAG session records are:
    Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                              s
    ----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
    torc-11                             44:38:39:ff:ff:01  down       n/a    0     0     1m:43.468s
    torc-12                             44:38:39:ff:ff:01  down       down   8     0     2m:11.967s
    noc-pr(P)         noc-se            00:01:01:10:00:01  up         up     25    25    35m:29.324s
    noc-se            noc-pr(P)         00:01:01:10:00:01  up         up     25    25    35m:26.551s
    torc-21(P)        torc-22           44:38:39:ff:ff:02  up         up     8     8     35m:10.140s
    torc-22           torc-21(P)        44:38:39:ff:ff:02  up         up     8     8     35m:7.342s

You can go back in time to see when this first MLAG pair went down.
These results indicate that the pair became disconnected some time in
the last five minutes.

    cumulus@switch:~$ netq show clag around 5m
    Matching clag records:
    Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                             s
    ----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
    noc-pr(P)         noc-se            00:01:01:10:00:01  up         up     25    25    30m:40.399s
    noc-se            noc-pr(P)         00:01:01:10:00:01  up         up     25    25    30m:37.267s
    torc-11(P)        torc-12           44:38:39:ff:ff:01  up         up     8     8     30m:27.250s
    torc-12           torc-11(P)        44:38:39:ff:ff:01  up         up     8     8     30m:23.552s
    torc-21(P)        torc-22           44:38:39:ff:ff:02  up         up     8     8     30m:20.856s
    torc-22           torc-21(P)        44:38:39:ff:ff:02  up         up     8     8     30m:18.583s

### <span>View MLAG Configuration and Status for Given Devices</span>

This example shows that xxx device is up and MLAG properly configured
with a peer connection to yyy and 8 bonds, all of which are dual bonded.

    cumulus@switch:~$ netq tor-22 show clag
    Matching CLAG session records are:
    Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                              s
    ----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
    torc-22           torc-21(P)        44:38:39:ff:ff:02  up         up     8     8     35m:7.342s

When you're directly on the switch, you can run `clagctl` to get the
state:

    cumulus@mlx-2700-03:/var/log# sudo clagctl
     
    The peer is alive
    Peer Priority, ID, and Role: 4096 00:02:00:00:00:4e primary
    Our Priority, ID, and Role: 8192 44:38:39:00:a5:38 secondary
    Peer Interface and IP: peerlink-3.4094 169.254.0.9
    VxLAN Anycast IP: 36.0.0.20
    Backup IP: 27.0.0.20 (active)
    System MAC: 44:38:39:ff:ff:01
     
    CLAG Interfaces
    Our Interface    Peer Interface   CLAG Id Conflicts            Proto-Down Reason
    ---------------- ---------------- ------- -------------------- -----------------
    vx-38            vx-38            -       -                    -
    vx-33            vx-33            -       -                    -
    hostbond4        hostbond4        1       -                    -
    hostbond5        hostbond5        2       -                    -
    vx-37            vx-37            -       -                    -
    vx-36            vx-36            -       -                    -
    vx-35            vx-35            -       -                    -
    vx-34            vx-34            -       -                    -

## <span>Monitor Time Synchronization Status for Devices</span>

It is important that the switches and hosts remain in time
synchronization with the Telemetry Server to ensure collected data is
properly captured and processed. You can use the `netq show ntp` command
to view the time synchronization status for all devices or filter for
devices that are either in synchronization or out of synchronization,
currently or at a time in the past. The syntax for the show command is:

    netq [<hostname>] show ntp [out-of-sync|in-sync] [json]
    netq [<hostname>] show ntp [out-of-sync|in-sync] around <text-time> [json]

This example shows the time synchronization status for all devices in
the network.

    cumulus@switch:~$ netq show ntp
     
    Matching ntp records:
    Hostname          NTP Sync Current Server    Stratum NTP App
    ----------------- -------- ----------------- ------- ---------------------
    edge01            yes      oob-mgmt-server   3       ntpq
    exit01            yes      christensenplac   2       ntpq
    exit02            yes      owners.kjsl.com   2       ntpq
    internet          no       -                 16      ntpq
    leaf01            yes      christensenplac   2       ntpq
    leaf02            yes      owners.kjsl.com   2       ntpq
    leaf03            yes      107.181.191.189   2       ntpq
    leaf04            yes      grom.polpo.org    2       ntpq
    oob-mgmt-server   yes      linode227395.st   2       ntpq
    server01          yes      192.168.0.254     3       ntpq
    server02          yes      192.168.0.254     3       ntpq
    server03          yes      192.168.0.254     3       ntpq
    server04          yes      192.168.0.254     3       ntpq
    spine01           yes      107.181.191.189   2       ntpq
    spine02           yes      t2.time.bf1.yah   2       ntpq

This example shows all devices in the network that are out of time
synchronization, and consequently might need to be investigated.

    cumulus@switch:~$ netq show ntp out-of-sync
     
    Matching ntp records:
    Hostname          NTP Sync Current Server    Stratum NTP App
    ----------------- -------- ----------------- ------- ---------------------
    internet          no       -                 16      ntpq

This example shows the time synchronization status for *leaf01*.

    cumulus@switch:~$ netq leaf01 show ntp
     
    Matching ntp records:
    Hostname          NTP Sync Current Server    Stratum NTP App
    ----------------- -------- ----------------- ------- ---------------------
    leaf01            yes      kilimanjaro       2       ntpq

## <span>Monitor Spanning Tree Protocol Configuration</span>

<span style="color: #36424a;"> The Spanning Tree Protocol (STP) is used
in Ethernet-based networks to prevent communication loops when you have
redundant paths on a bridge or switch. Loops cause excessive broadcast
messages greatly impacting the network performance. With NetQ, you can
view the STP topology on a bridge or switch to ensure no loops have been
created using the `netq show stp topology` command. You can also view
the topology information for a prior point in time to see if there have
been changes from that point until now. The syntax for the show command
is: </span>

    netq <hostname> show stp topology [json]   
    netq <hostname> show stp topology around <text-time> [json]

<span style="color: #36424a;"> This example shows the STP topology as
viewed from the *spine1* switch. </span>

    cumulus@switch:~$ netq spine1 show stp topology
    Root(spine1) -- spine1:sw_clag200 -- leaf2:EdgeIntf(sng_hst2) -- hsleaf21
                                      -- leaf2:EdgeIntf(dual_host2) -- hdleaf2
                                      -- leaf2:EdgeIntf(dual_host1) -- hdleaf1
                                      -- leaf2:ClagIsl(peer-bond1) -- leaf1
                                      -- leaf1:EdgeIntf(sng_hst2) -- hsleaf11
                                      -- leaf1:EdgeIntf(dual_host2) -- hdleaf2
                                      -- leaf1:EdgeIntf(dual_host1) -- hdleaf1
                                      -- leaf1:ClagIsl(peer-bond1) -- leaf2
                 -- spine1:ClagIsl(peer-bond1) -- spine2
                 -- spine1:sw_clag300 -- edge1:EdgeIntf(sng_hst2) -- hsedge11
                                      -- edge1:EdgeIntf(dual_host2) -- hdedge2
                                      -- edge1:EdgeIntf(dual_host1) -- hdedge1
                                      -- edge1:ClagIsl(peer-bond1) -- edge2
                                      -- edge2:EdgeIntf(sng_hst2) -- hsedge21
                                      -- edge2:EdgeIntf(dual_host2) -- hdedge2
                                      -- edge2:EdgeIntf(dual_host1) -- hdedge1
                                      -- edge2:ClagIsl(peer-bond1) -- edge1
    Root(spine2) -- spine2:sw_clag200 -- leaf2:EdgeIntf(sng_hst2) -- hsleaf21
                                      -- leaf2:EdgeIntf(dual_host2) -- hdleaf2
                                      -- leaf2:EdgeIntf(dual_host1) -- hdleaf1
                                      -- leaf2:ClagIsl(peer-bond1) -- leaf1
                                      -- leaf1:EdgeIntf(sng_hst2) -- hsleaf11
                                      -- leaf1:EdgeIntf(dual_host2) -- hdleaf2
                                      -- leaf1:EdgeIntf(dual_host1) -- hdleaf1
                                      -- leaf1:ClagIsl(peer-bond1) -- leaf2
                 -- spine2:ClagIsl(peer-bond1) -- spine1
                 -- spine2:sw_clag300 -- edge2:EdgeIntf(sng_hst2) -- hsedge21
                                      -- edge2:EdgeIntf(dual_host2) -- hdedge2
                                      -- edge2:EdgeIntf(dual_host1) -- hdedge1
                                      -- edge2:ClagIsl(peer-bond1) -- edge1
                                      -- edge1:EdgeIntf(sng_hst2) -- hsedge11
                                      -- edge1:EdgeIntf(dual_host2) -- hdedge2
                                      -- edge1:EdgeIntf(dual_host1) -- hdedge1
                                      -- edge1:ClagIsl(peer-bond1) -- edge2

## <span>Validate Paths between Devices</span>

If you have VLANs configured, you can <span style="color: #353744;">
view the available paths between two devices on the VLAN currently and
at a time in the past using their MAC addresses </span> . You can
<span style="color: #353744;"> perform the trace in only one direction
or both, and view the output in one of three formats ( </span> *json,
pretty,* <span style="color: #353744;"> and </span> *detail*
<span style="color: #353744;"> ). JSON output provides the output in a
JSON file format for ease of importing to other applications or
software. Pretty output lines up the paths in a pseudo-graphical manner
to help visualize multiple paths. Detail output is useful for traces
with higher hop counts where the pretty output wraps lines, making it
harder to interpret the results. The detail output displays a table with
a row for each path. </span>

<span style="color: #353744;"> <span style="color: #000000;"> To view
the paths: </span> </span>

1.  <span style="color: #353744;"> <span style="color: #000000;">
    Identify the MAC address and VLAN ID for the destination device
    </span> </span>

2.  <span style="color: #353744;"> <span style="color: #000000;">
    Identify the IP address or hostname for the source device </span>
    </span>

3.  <span style="color: #353744;"> <span style="color: #000000;"> Use
    the </span> `netq trace` <span style="color: #000000;"> command to
    see the available paths between those devices. </span> </span>
    <span style="color: #353744;">  
    </span>

<span style="color: #353744;"> The trace command syntax is: </span>

    netq trace <mac> [vlan <1-4096>] from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [bidir] [json|detail|pretty] [debug]

{{%notice info%}}

The syntax requires the destination device address first, *\<mac\>*, and
then the source device address or hostname. Additionally, the *vlan*
keyword-value pair is required for layer 2 traces even though the syntax
indicates it is optional.

The tracing function only knows about addresses that have already been
learned. If you find that a path is invalid or incomplete, you may need
to ping the identified device so that its address becomes known.

{{%/notice%}}

### <span>View Paths between Two Switches with Pretty Output</span>

This example shows the available paths between a top of rack switch,
*tor-1*, and a server, *hostd-11*. The request is to go through VLAN
*1001* from the VRF *vrf1*. The results include a summary of the trace,
including the total number of paths available, those with errors and
warnings, and the MTU of the paths. In this case, the results are
displayed in pseudo-graphical output.

```
cumulus@switch:~$ netq trace  00:02:00:00:00:02 vlan 1001 from tor-1 vrf vrf1  pretty
Number of Paths: 4
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9152
 tor-1 vni: 34 uplink-2 -- downlink-5 spine-2 downlink-2 -- uplink-2 vni: 34 torc-12 hostbond4 -- swp2 hostd-11  
               uplink-2 -- downlink-5 spine-2 downlink-1 -- uplink-2 vni: 34 torc-11 hostbond4 -- swp1 hostd-11  
 tor-1 vni: 34 uplink-1 -- downlink-5 spine-1 downlink-2 -- uplink-1 vni: 34 torc-12 hostbond4 -- swp2 hostd-11  
               uplink-1 -- downlink-5 spine-1 downlink-1 -- uplink-1 vni: 34 torc-11 hostbond4 -- swp1 hostd-11    
```

Alternately, you can use the IP address of the source device, as shown
in this example.

    cumulus@redis-1:~$  netq trace 00:02:00:00:00:02 vlan 1001 from 6.0.0.8 vrf vrf1  pretty
    Number of Paths: 4
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9152
     hosts-11 swp1 -- swp5 <vlan1000> tor-1 <vlan1001> vni: 34 uplink-2 -- downlink-5 spine-2 downlink-2 -- uplink-2 vni: 34 <vlan1001> torc-12 hostbond4 -- swp2 hostd-11  
                                                               uplink-2 -- downlink-5 spine-2 downlink-1 -- uplink-2 vni: 34 <vlan1001> torc-11 hostbond4 -- swp1 hostd-11  
              swp1 -- swp5 <vlan1000> tor-1 <vlan1001> vni: 34 uplink-1 -- downlink-5 spine-1 downlink-2 -- uplink-1 vni: 34 <vlan1001> torc-12 hostbond4 -- swp2 hostd-11  
                                                               uplink-1 -- downlink-5 spine-1 downlink-1 -- uplink-1 vni: 34 <vlan1001> torc-11 hostbond4 -- swp1 hostd-11

### <span>View Forward and Reverse Paths between Two Switches with Pretty Output</span>

Like the previous example, this shows the paths between tor-1 and
hostd-11, but by adding the *bidir* keyword both the forward and reverse
paths are presented. Optionally, you can use the source device's
hostname to achieve the same results.

    cumulus@switch:~$ netq trace  00:02:00:00:00:02 vlan 1001 from tor-1 vrf vrf1 bidir pretty
    Number of Paths: 4
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9152
     tor-1 vni: 34 uplink-2 -- downlink-5 spine-2 downlink-2 -- uplink-2 vni: 34 torc-12 hostbond4 -- swp2 hostd-11  
                   uplink-2 -- downlink-5 spine-2 downlink-1 -- uplink-2 vni: 34 torc-11 hostbond4 -- swp1 hostd-11  
     tor-1 vni: 34 uplink-1 -- downlink-5 spine-1 downlink-2 -- uplink-1 vni: 34 torc-12 hostbond4 -- swp2 hostd-11  
                   uplink-1 -- downlink-5 spine-1 downlink-1 -- uplink-1 vni: 34 torc-11 hostbond4 -- swp1 hostd-11    
     
    Number of Paths: 4
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9152
     hostd-11 swp2 -- uplink-2 vni: 34 torc-12 hostbond4 -- downlink-2 spine-2 downlink-5 -- uplink-2 vni:34 tor-1
                      uplink-1 vni: 34 torc-12 hostbond4 -- downlink-2 spine-2 downlink-5 -- uplink-2 vni:34 tor-1
     hostd-11 swp2 -- uplink-2 vni: 34 torc-12 hostbond4 -- downlink-2 spine-2 downlink-5 -- uplink-1 vni:34 tor-1
                      uplink-1 vni: 34 torc-12 hostbond4 -- downlink-2 spine-2 downlink-5 -- uplink-1 vni:34 tor-1

### <span>View Paths between Two Switches with Detailed Output</span>

This example provides the same path information as the pretty output,
but displays the information in a tabular output.

    cumulus@switch:~$ netq trace  00:02:00:00:00:02 vlan 1001 from 6.0.0.8 vrf vrf1 bidir detail
    Number of Paths: 4
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9152
    Id  Hop Hostname        InPort          InVlan InTunnel              InRtrIf         InVRF           OutRtrIf        OutVRF          OutTunnel             OutPort         OutVlan
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    1   1   hosts-11                                                                                                                                           swp1            1000
        2   tor-1           swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-2
        3   spine-2         downlink-5                                   downlink-5      default         downlink-2      default                               downlink-2
        4   torc-12         uplink-2               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   hostd-11        swp2
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    2   1   hosts-11                                                                                                                                           swp1            1000
        2   tor-1           swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-2
        3   spine-2         downlink-5                                   downlink-5      default         downlink-1      default                               downlink-1
        4   torc-11         uplink-2               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   hostd-11        swp1
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    3   1   hosts-11                                                                                                                                           swp1            1000
        2   tor-1           swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-1
        3   spine-1         downlink-5                                   downlink-5      default         downlink-2      default                               downlink-2
        4   torc-12         uplink-1               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   hostd-11        swp2
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    4   1   hosts-11                                                                                                                                           swp1            1000
        2   tor-1           swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-1
        3   spine-1         downlink-5                                   downlink-5      default         downlink-1      default                               downlink-1
        4   torc-11         uplink-1               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   hostd-11        swp1
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    Number of Paths: 4
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9152
    Id  Hop Hostname        InPort          InVlan InTunnel              InRtrIf         InVRF           OutRtrIf        OutVRF          OutTunnel             OutPort         OutVlan
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    1   1   hostd-11                                                                                                                                           swp2            1001
        2   torc-12         swp7            1001                         vlan1001        vrf1            vlan1000        vrf1            vni: 33               uplink-2
        3   spine-2         downlink-2                                   downlink-2      default         downlink-5      default                               downlink-5
        4   tor-1           uplink-2               vni: 33               vlan1000        vrf1                                                                  hostbond3       1000
        5   hosts-11        swp1
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    2   1   hostd-11                                                                                                                                           swp2            1001
        2   torc-12         swp7            1001                         vlan1001        vrf1            vlan1000        vrf1            vni: 33               uplink-1
        3   spine-1         downlink-2                                   downlink-2      default         downlink-5      default                               downlink-5
        4   tor-1           uplink-1               vni: 33               vlan1000        vrf1                                                                  hostbond3       1000
        5   hosts-11        swp1
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    3   1   hostd-11                                                                                                                                           swp1            1001
        2   torc-11         swp7            1001                         vlan1001        vrf1            vlan1000        vrf1            vni: 33               uplink-2
        3   spine-2         downlink-1                                   downlink-1      default         downlink-5      default                               downlink-5
        4   tor-1           uplink-2               vni: 33               vlan1000        vrf1                                                                  hostbond3       1000
        5   hosts-11        swp1
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    4   1   hostd-11                                                                                                                                           swp1            1001
        2   torc-11         swp7            1001                         vlan1001        vrf1            vlan1000        vrf1            vni: 33               uplink-1
        3   spine-1         downlink-1                                   downlink-1      default         downlink-5      default                               downlink-5
        4   tor-1           uplink-1               vni: 33               vlan1000        vrf1                                                                  hostbond3       1000
        5   hosts-11        swp1
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
