---
title: Show Commands
author: Cumulus Networks
weight: 1102
toc: 3
right_toc_levels: 2
pdfhidden: true
draft: true
---
All of the NetQ show commands begin with `netq show`. They are used to view the health of various elements in your network fabric. Many allow filtering by hostname and other parameters. The results are presented in the NetQ CLI immediately. The commands are listed alphabetically within functional groups.

## Network Protocols and Services

You can monitor the health of the following network protocols and services:

- Layer 1: Sensors
- Layer 2: Interfaces, LLDP, STP, VLANs, MLAG/CLAG
- Layer 3: IP, BGP, OSPF
- Layer 4: NTP
- Virtual overlays: EVPN, VXLANs
- Other: NetQ Agents

### netq show agents

Displays basic configuration, health, and connectivity status for all nodes or a specific node running NetQ Agent in your network fabric. This command gives you an easy way to see if any NetQ Agents or their nodes have lost power, may have difficulty communicating with the telemetry server, and whether agents are running different versions of software. Any of these situations could cause problems in the operation of your network.

The output provides:

- Whether each node has been heard recently (last 90 seconds)
- If each node is in time synchronization with the NetQ appliance or Virtual Machine
- The NetQ Agent software version currently running on the node
- How long the node has been operationally up
- How long the NetQ Agent has been operationally up
- The last time the NetQ Agent was reinitialized
- When the last change was made to the any of these items

#### Syntax

```
netq [<hostname>] show agents
    [fresh | dead | rotten | opta]
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Filter output to view status for the switch or host with this name |
| fresh | NA | Filter output for devices where the NetQ Agent is communicating with the appliance or VM as expected |
| dead | NA | Filter output for devices where the NetQ Agent has been decommisioned by a user |
| rotten | NA | Filter output for devices where the NetQ Agent has not communicated with the appliance or VM in the last two minutes |
| opta | NA | Filter output for the NetQ Agent installed on the appliance or VM |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

#### Sample Usage

Basic show: all devices, all states, currently

```
cumulus@switch:~$ netq show agents
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
border01          Fresh            yes      3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:32:59 2020  Fri Oct  2 22:24:49 2020  Fri Oct  2 22:24:49 2020   Fri Nov 20 18:49:19 2020
border02          Fresh            yes      3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:32:57 2020  Fri Oct  2 22:24:48 2020  Fri Oct  2 22:24:48 2020   Fri Nov 20 18:49:03 2020
fw1               Fresh            no       3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:36:33 2020  Mon Nov  2 19:49:21 2020  Mon Nov  2 19:49:21 2020   Fri Nov 20 18:48:53 2020
fw2               Fresh            no       3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:36:32 2020  Mon Nov  2 19:49:20 2020  Mon Nov  2 19:49:20 2020   Fri Nov 20 18:48:52 2020
leaf01            Fresh            yes      3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:32:56 2020  Fri Oct  2 22:24:45 2020  Fri Oct  2 22:24:45 2020   Fri Nov 20 18:49:27 2020
leaf02            Fresh            yes      3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:32:54 2020  Fri Oct  2 22:24:44 2020  Fri Oct  2 22:24:44 2020   Fri Nov 20 18:49:19 2020
leaf03            Fresh            yes      3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:32:59 2020  Fri Oct  2 22:24:49 2020  Fri Oct  2 22:24:49 2020   Fri Nov 20 18:49:20 2020
leaf04            Fresh            yes      3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:32:57 2020  Fri Oct  2 22:24:47 2020  Fri Oct  2 22:24:47 2020   Fri Nov 20 18:49:20 2020
oob-mgmt-server   Fresh            yes      3.2.0-ub18.04u30~1601400975.104fb9e  Fri Oct  2 19:54:09 2020  Fri Oct  2 22:26:32 2020  Fri Oct  2 22:26:32 2020   Fri Nov 20 18:49:03 2020
server01          Fresh            yes      3.2.0-ub18.04u30~1601400975.104fb9e  Fri Oct  2 22:39:27 2020  Mon Nov  2 19:49:31 2020  Mon Nov  2 19:49:31 2020   Fri Nov 20 18:49:07 2020
server02          Fresh            yes      3.2.0-ub18.04u30~1601400975.104fb9e  Fri Oct  2 22:39:26 2020  Mon Nov  2 19:49:32 2020  Mon Nov  2 19:49:32 2020   Fri Nov 20 18:49:22 2020
server03          Fresh            yes      3.2.0-ub18.04u30~1601400975.104fb9e  Fri Oct  2 22:39:27 2020  Mon Nov  2 19:49:32 2020  Mon Nov  2 19:49:32 2020   Fri Nov 20 18:49:03 2020
server04          Fresh            yes      3.2.0-ub18.04u30~1601400975.104fb9e  Fri Oct  2 22:39:27 2020  Mon Nov  2 19:49:32 2020  Mon Nov  2 19:49:32 2020   Fri Nov 20 18:49:30 2020
server05          Fresh            yes      3.2.0-ub18.04u30~1601400975.104fb9e  Fri Oct  2 22:39:26 2020  Mon Nov  2 19:49:33 2020  Mon Nov  2 19:49:33 2020   Fri Nov 20 18:49:15 2020
server06          Fresh            yes      3.2.0-ub18.04u30~1601400975.104fb9e  Fri Oct  2 22:39:26 2020  Mon Nov  2 19:49:34 2020  Mon Nov  2 19:49:34 2020   Fri Nov 20 18:49:19 2020
server07          Fresh            yes      3.2.0-ub18.04u30~1601400975.104fb9e  Fri Oct  2 20:47:24 2020  Mon Nov  2 19:49:35 2020  Mon Nov  2 19:49:35 2020   Fri Nov 20 18:49:11 2020
server08          Fresh            yes      3.2.0-ub18.04u30~1601400975.104fb9e  Fri Oct  2 20:47:24 2020  Mon Nov  2 19:49:35 2020  Mon Nov  2 19:49:35 2020   Fri Nov 20 18:49:04 2020
spine01           Fresh            yes      3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:32:29 2020  Fri Oct  2 22:24:20 2020  Fri Oct  2 22:24:20 2020   Fri Nov 20 18:49:02 2020
spine02           Fresh            yes      3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:32:48 2020  Fri Oct  2 22:24:37 2020  Fri Oct  2 22:24:37 2020   Fri Nov 20 18:49:12 2020
spine03           Fresh            yes      3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:32:51 2020  Fri Oct  2 22:24:41 2020  Fri Oct  2 22:24:41 2020   Fri Nov 20 18:49:25 2020
spine04           Fresh            yes      3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:32:49 2020  Fri Oct  2 22:24:40 2020  Fri Oct  2 22:24:40 2020   Fri Nov 20 18:49:22 2020
```

Show all devices in rotten state, currently.

```
cumulus@switch:~$ netq show agents rotten
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
fw1               Rotten           no       3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:36:33 2020  Mon Nov  2 19:49:21 2020  Mon Nov  2 19:49:21 2020   Fri Nov 20 18:48:53 2020
fw2               Rotten           no       3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:36:32 2020  Mon
```

Show all devices in rotten state, currently, in JSON format

```
cumulus@switch:~$ netq show agents rotten json
{
    "agents":[
        {
            "hostname":"fw1",
            "status":"Rotten",
            "ntpSync":"no",
            "version":"3.2.0-cl4u30~1601403318.104fb9ed",
            "sysUptime":1601670993.0,
            "agentUptime":1604346561.0,
            "reinitializeTime":1604346561.0,
            "lastChanged":1605903102.0
        },
        {
            "hostname":"fw2",
            "status":"Rotten",
            "ntpSync":"no",
            "version":"3.2.0-cl4u30~1601403318.104fb9ed",
            "sysUptime":1601670992.0,
            "agentUptime":1604346560.0,
            "reinitializeTime":1604346560.0,
            "lastChanged":1605903103.0
        }
    ],
    "truncatedResult":false
}
```

#### Related Commands

- netq show events
- netq check agents
- netq config add agent
- netq config del agent

- - -

### netq show bgp

Displays the health of all BGP sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The neighbor nodes for a given node
- What routing tables (VRF) is used by that node and neighbor
- The autonomous system number (ASN) assigned to the node
- The peer ASN for each neighbor node
- The address prefix for IPv4/IPv6/???
- When the last change was made to any of these items

If you have nodes that implement virtual routing and forwarding (VRF), you can request status based on the relevant routing table. VRF is commonly configured in multi-tenancy deployments to maintain separate domains for each tenant.

#### Syntax

```
netq [<hostname>] show bgp
    [<bgp-session>|asn <number-asn>]
    [vrf <vrf>]
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<bgp-session\> | Only display results for this particular BGP session; for example 5468354 |
| asn | \<number-asn\> | Only display results for nodes using this ASN; for example 65013 |
| vrf | \<vrf\> | Only display results for sessions run on this VRF; for example default, mgmt, or vrf10 |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

#### Sample Usage

Basic show: all devices, all states, currently

```
cumulus@switch:~$ netq show bgp
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
border01          swp51(spine01)               default         65132      65199      7/-/74       Fri Oct  2 22:39:00 2020
border01          peerlink.4094(border02)      default         65132      65132      12/-/-       Fri Oct  2 22:39:00 2020
border01          swp54(spine04)               default         65132      65199      7/-/74       Fri Oct  2 22:39:00 2020
border01          swp53(spine03)               default         65132      65199      7/-/74       Fri Oct  2 22:39:00 2020
border01          swp52(spine02)               default         65132      65199      7/-/74       Fri Oct  2 22:39:00 2020
border02          swp52(spine02)               default         65132      65199      7/-/75       Fri Oct  2 22:39:00 2020
border02          peerlink.4094(border01)      default         65132      65132      12/-/-       Fri Oct  2 22:39:00 2020
border02          swp54(spine04)               default         65132      65199      7/-/75       Fri Oct  2 22:39:00 2020
border02          swp53(spine03)               default         65132      65199      7/-/75       Fri Oct  2 22:39:00 2020
border02          swp51(spine01)               default         65132      65199      7/-/75       Fri Oct  2 22:39:00 2020
leaf01            peerlink.4094(leaf02)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf01            swp54(spine04)               default         65101      65199      7/-/37       Fri Oct  2 22:39:00 2020
leaf01            swp53(spine03)               default         65101      65199      7/-/37       Fri Oct  2 22:39:00 2020
leaf01            swp52(spine02)               default         65101      65199      7/-/37       Fri Oct  2 22:39:00 2020
leaf01            swp51(spine01)               default         65101      65199      7/-/37       Fri Oct  2 22:39:00 2020
leaf02            swp53(spine03)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp52(spine02)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            peerlink.4094(leaf01)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf02            swp54(spine04)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf03            swp52(spine02)               default         65102      65199      7/-/38       Fri Oct  2 22:39:00 2020
leaf03            swp51(spine01)               default         65102      65199      7/-/38       Fri Oct  2 22:39:00 2020
leaf03            swp54(spine04)               default         65102      65199      7/-/38       Fri Oct  2 22:39:00 2020
leaf03            swp53(spine03)               default         65102      65199      7/-/38       Fri Oct  2 22:39:00 2020
leaf03            peerlink.4094(leaf04)        default         65102      65102      11/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp51(spine01)               default         65102      65199      7/-/38       Fri Oct  2 22:39:00 2020
leaf04            peerlink.4094(leaf03)        default         65102      65102      12/-/-       Fri Oct  2 22:39:00 2020
leaf04            swp52(spine02)               default         65102      65199      7/-/38       Fri Oct  2 22:39:00 2020
leaf04            swp53(spine03)               default         65102      65199      7/-/38       Fri Oct  2 22:39:00 2020
leaf04            swp54(spine04)               default         65102      65199      7/-/38       Fri Oct  2 22:39:00 2020
spine01           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine01           swp4(leaf04)                 default         65199      65102      3/-/17       Fri Oct  2 22:39:00 2020
spine01           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine01           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine01           swp1(leaf01)                 default         65199      65101      3/-/20       Fri Oct  2 22:39:00 2020
spine01           swp3(leaf03)                 default         65199      65102      3/-/20       Fri Oct  2 22:39:00 2020
spine02           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine02           swp3(leaf03)                 default         65199      65102      3/-/20       Fri Oct  2 22:39:00 2020
spine02           swp4(leaf04)                 default         65199      65102      3/-/16       Fri Oct  2 22:39:00 2020
spine02           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine02           swp1(leaf01)                 default         65199      65101      3/-/20       Fri Oct  2 22:39:00 2020
spine03           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine03           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine03           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine03           swp3(leaf03)                 default         65199      65102      3/-/20       Fri Oct  2 22:39:00 2020
spine03           swp1(leaf01)                 default         65199      65101      3/-/20       Fri Oct  2 22:39:00 2020
spine03           swp4(leaf04)                 default         65199      65102      3/-/16       Fri Oct  2 22:39:00 2020
spine04           swp4(leaf04)                 default         65199      65102      3/-/16       Fri Oct  2 22:39:00 2020
spine04           swp6(border02)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
spine04           swp1(leaf01)                 default         65199      65101      3/-/20       Fri Oct  2 22:39:00 2020
spine04           swp3(leaf03)                 default         65199      65102      3/-/20       Fri Oct  2 22:39:00 2020
spine04           swp2(leaf02)                 default         65199      65101      3/-/18       Fri Oct  2 22:39:00 2020
spine04           swp5(border01)               default         65199      65132      3/-/0        Fri Oct  2 22:39:00 2020
```

View status of nodes running BGP with particular ASN

```
cumulus@switch:~$ netq show bgp asn 65101
Matching bgp records:
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
leaf01            peerlink.4094(leaf02)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf01            swp54(spine04)               default         65101      65199      7/-/37       Fri Oct  2 22:39:00 2020
leaf01            swp53(spine03)               default         65101      65199      7/-/37       Fri Oct  2 22:39:00 2020
leaf01            swp52(spine02)               default         65101      65199      7/-/37       Fri Oct  2 22:39:00 2020
leaf01            swp51(spine01)               default         65101      65199      7/-/37       Fri Oct  2 22:39:00 2020
leaf02            swp53(spine03)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp52(spine02)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            peerlink.4094(leaf01)        default         65101      65101      12/-/-       Fri Oct  2 22:39:00 2020
leaf02            swp54(spine04)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
leaf02            swp51(spine01)               default         65101      65199      7/-/36       Fri Oct  2 22:39:00 2020
```

#### Related Commands

- netq show events
- netq check bgp

- - -

### netq show clag

Displays the health of all CLAG sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The peer nodes for a given node
- The system MAC address used for the session between the nodes
- The operational state of the session (up or down)
- The operational state of the backup IP address (up or down)
- The total number of bonds
- The number of dual-connected bonds
- When the last change was made to any of these items

If the total number of bonds does not match the number of dual-connected bonds, there might be a configuration issue.

#### Syntax

```
netq [<hostname>] show clag
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

#### Sample Usage

Basic show: all devices, all states, currently

```
cumulus@switch:~$ netq show clag
Matching clag records:
Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                         s
----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
border01(P)       border02          44:38:39:be:ef:ff  up         up     3     3     Thu Nov 19 22:33:48 2020
border02          border01(P)       44:38:39:be:ef:ff  up         up     3     3     Thu Nov 19 22:29:24 2020
leaf01(P)         leaf02            44:38:39:be:ef:aa  up         up     8     8     Thu Nov 19 22:29:16 2020
leaf02            leaf01(P)         44:38:39:be:ef:aa  up         up     8     8     Thu Nov 19 22:39:27 2020
leaf03(P)         leaf04            44:38:39:be:ef:bb  up         up     8     8     Fri Nov 20 11:10:35 2020
leaf04            leaf03(P)         44:38:39:be:ef:bb  up         up     8     8     Fri Nov 20 11:11:24 2020
```

#### Related Commands

- netq show events
- netq check clag

- - -

### netq show evpn

Displays the health of all EVPN sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides the following for each session:

- The VNI used
- The address of the VNI endpoint
- Whether the session is part of a layer 2 or layer 3 configuration
- The associated VRF or VLAN when defined
- Whether the associated VNI is in the kernel
- The export and import route targets used for filtering
- When the last change was made to any of these items

#### Syntax

```
netq [<hostname>] show evpn
    [vni <text-vni>]
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| vni | \<text-vni\> | Only display results for sessions using the VNI with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

#### Sample Usage

Basic show: all devices, all VNIs, currently

```
cumulus@switch:~$ netq show evpn

Matching evpn records:
Hostname          VNI        VTEP IP          Type             Mapping        In Kernel Export RT        Import RT        Last Changed
----------------- ---------- ---------------- ---------------- -------------- --------- ---------------- ---------------- -------------------------
border01          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Fri Nov 20 01:50:53 2020
border01          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Fri Nov 20 01:50:53 2020
border02          4001       10.0.1.254       L3               Vrf RED        yes       65132:4001       65132:4001       Fri Nov 20 01:50:19 2020
border02          4002       10.0.1.254       L3               Vrf BLUE       yes       65132:4002       65132:4002       Fri Nov 20 01:50:19 2020
leaf01            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Fri Nov 20 02:18:42 2020
leaf01            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Fri Nov 20 02:18:42 2020
leaf01            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Fri Nov 20 02:18:42 2020
leaf01            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Fri Nov 20 02:18:42 2020
leaf01            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Fri Nov 20 02:18:42 2020
leaf02            4001       10.0.1.1         L3               Vrf RED        yes       65101:4001       65101:4001       Fri Nov 20 02:10:38 2020
leaf02            10         10.0.1.1         L2               Vlan 10        yes       65101:10         65101:10         Fri Nov 20 02:10:38 2020
leaf02            30         10.0.1.1         L2               Vlan 30        yes       65101:30         65101:30         Fri Nov 20 02:10:38 2020
leaf02            4002       10.0.1.1         L3               Vrf BLUE       yes       65101:4002       65101:4002       Fri Nov 20 02:10:38 2020
leaf02            20         10.0.1.1         L2               Vlan 20        yes       65101:20         65101:20         Fri Nov 20 02:10:38 2020
leaf03            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Fri Nov 20 02:05:00 2020
leaf03            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Fri Nov 20 02:05:00 2020
leaf03            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Fri Nov 20 02:05:00 2020
leaf03            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Fri Nov 20 02:05:00 2020
leaf03            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Fri Nov 20 02:05:00 2020
leaf04            10         10.0.1.2         L2               Vlan 10        yes       65102:10         65102:10         Fri Nov 20 11:08:16 2020
leaf04            30         10.0.1.2         L2               Vlan 30        yes       65102:30         65102:30         Fri Nov 20 11:08:16 2020
leaf04            4002       10.0.1.2         L3               Vrf BLUE       yes       65102:4002       65102:4002       Fri Nov 20 11:08:16 2020
leaf04            20         10.0.1.2         L2               Vlan 20        yes       65102:20         65102:20         Fri Nov 20 11:08:16 2020
leaf04            4001       10.0.1.2         L3               Vrf RED        yes       65102:4001       65102:4001       Fri Nov 20 11:08:16 2020
```

#### Related Commands

- netq show events
- netq check evpn

- - -

### netq show interfaces

Displays the health of all interfaces or a single interface on all nodes or a specific node in your network fabric currently or for a time in the past. You can filter by the interface type, state of the interface, or the remote interface. For a given switch or host, you can view the total number of configured interfaces.

The output provides the following for each device:

- The name of the interface
- The type of interface
- The state of the interface (up or down)
- The associated VRF, VLANs, PVID, MTU, and LLDP peer
- When the last change was made to any of these items
- The total number of interfaces on a given device

#### Syntax

There are four forms of the command, based on whether you want to view interface health for all devices or a given device, and whether you want to filter by an interface type.

```
netq show interfaces
    [<remote-interface>]
    [state <remote-interface-state>]
    [around <text-time>]
    [json]

netq <hostname> show interfaces
    [<remote-interface>]
    [state <remote-interface-state>]
    [around <text-time>]
    [count]
    [json]

netq show interfaces type (bond|bridge|eth|loopback|macvlan|swp|vlan|vrf|vxlan)
    [state <remote-interface-state>]
    [around <text-time>]
    [json]

netq <hostname> show interfaces type (bond|bridge|eth|loopback|macvlan|swp|vlan|vrf|vxlan)
    [state <remote-interface-state>]
    [around <text-time>]
    [count]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name. This is only required when the `count` option is used. |
| type | bond, bridge, eth, loopback, macvlan, swp, vlan, vrf, or vxlan | Only display results for the specified interface type |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<remote-interface\> | Only display results for local interfaces with this remote interface |
| state | \<remote-interface-state\> | Only display results for remote interfaces in the specified state&mdash;up or down |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| count | NA | Display the total number of interface on the specified switch or host. The `hostname` option is required when using this option. |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

#### Sample Usage

Basic show: all devices, all interface types, currently

```
cumulus@switch:~$ netq show interfaces
Matching link records:
Hostname          Interface                 Type             State      VRF             Details                             Last Changed
----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
border01          swp52                     swp              up         default         VLANs: ,                            Tue Nov 10 22:29:05 2020
                                                                                        PVID: 0 MTU: 9216 LLDP: spine02:swp
                                                                                        5
border01          swp53                     swp              up         default         VLANs: ,                            Tue Nov 10 22:29:05 2020
                                                                                        PVID: 0 MTU: 9216 LLDP: spine03:swp
                                                                                        5
border01          swp54                     swp              up         default         VLANs: ,                            Tue Nov 10 22:29:05 2020
                                                                                        PVID: 0 MTU: 9216 LLDP: spine04:swp
                                                                                        5
border01          eth0                      eth              up         mgmt            MTU: 1500                           Tue Nov 10 22:29:05 2020
border01          lo                        loopback         up         default         MTU: 65536                          Tue Nov 10 22:29:05 2020
border01          peerlink                  bond             up         default         Slave: swp49 (LLDP: border02:swp49) Tue Nov 10 22:29:05 2020
                                                                                        ,
                                                                                        Slave: swp50 (LLDP: border02:swp50)
border01          vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Nov 10 22:29:05 2020
...
```

View interfaces on a given device.

```
cumulus@switch:~$ netq spine01 show interfaces
Matching link records:
Hostname          Interface                 Type             State      VRF             Details                             Last Changed
----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
spine01           swp5                      swp              up         default         VLANs: ,                            Tue Nov 10 22:30:11 2020
                                                                                        PVID: 0 MTU: 9216 LLDP: border01:sw
                                                                                        p51
spine01           swp6                      swp              up         default         VLANs: ,                            Tue Nov 10 22:30:11 2020
                                                                                        PVID: 0 MTU: 9216 LLDP: border02:sw
                                                                                        p51
spine01           eth0                      eth              up         mgmt            MTU: 1500                           Tue Nov 10 22:30:11 2020
spine01           lo                        loopback         up         default         MTU: 65536                          Tue Nov 10 22:30:11 2020
spine01           mgmt                      vrf              up         mgmt            table: 1001, MTU: 65536,            Tue Nov 10 22:30:11 2020
                                                                                        Members:  eth0,  mgmt,
spine01           vagrant                   swp              down       default         VLANs: , PVID: 0 MTU: 1500          Tue Nov 10 22:30:11 2020
spine01           swp1                      swp              up         default         VLANs: ,                            Tue Nov 10 22:30:11 2020
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf01:swp5
                                                                                        1
spine01           swp2                      swp              up         default         VLANs: ,                            Tue Nov 10 22:30:11 2020
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf02:swp5
                                                                                        1
spine01           swp3                      swp              up         default         VLANs: ,                            Tue Nov 10 22:30:11 2020
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf03:swp5
                                                                                        1
spine01           swp4                      swp              up         default         VLANs: ,                            Tue Nov 10 22:30:11 2020
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf04:swp5
                                                                                        1
```

View an interface count on a given device.

```
cumulus@switch:~$ netq spine01 show interfaces count
Count of matching link records: 10
```

#### Related Commands

- netq show events
- netq check interfaces

- - -

### netq show lldp

Displays the health of all LLDP sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. You can filter the output to show sessions for a particular peer interface port. The output provides the following for each session:

- The interface on the local device
- The hostname and interface of the peer device
- When the last change was made to any of these items

#### Syntax

```
netq [<hostname>] show lldp
    [<remote-physical-interface>]
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<remote-physical-interface\> | Only display results for sessions using the interface port with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

#### Sample Usage

Basic show: all devices, all interfaces, currently

```
cumulus@switch:~$ netq show lldp
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
border01          swp54                     spine04           swp5                      Fri Nov 20 10:19:39 2020
border01          swp51                     spine01           swp5                      Fri Nov 20 10:19:39 2020
border01          swp53                     spine03           swp5                      Fri Nov 20 10:19:39 2020
border01          swp3                      fw1               swp1                      Fri Nov 20 10:19:39 2020
border01          swp50                     border02          swp50                     Fri Nov 20 10:19:39 2020
border01          swp52                     spine02           swp5                      Fri Nov 20 10:19:39 2020
border01          swp49                     border02          swp49                     Fri Nov 20 10:19:39 2020
border01          eth0                      oob-mgmt-switch   swp20                     Fri Nov 20 10:19:39 2020
border02          swp49                     border01          swp49                     Fri Nov 20 10:25:40 2020
border02          swp51                     spine01           swp6                      Fri Nov 20 10:25:40 2020
border02          swp52                     spine02           swp6                      Fri Nov 20 10:25:40 2020
border02          eth0                      oob-mgmt-switch   swp21                     Fri Nov 20 10:25:40 2020
border02          swp3                      fw1               swp2                      Fri Nov 20 10:25:40 2020
border02          swp50                     border01          swp50                     Fri Nov 20 10:25:40 2020
border02          swp53                     spine03           swp6                      Fri Nov 20 10:25:40 2020
border02          swp54                     spine04           swp6                      Fri Nov 20 10:25:40 2020
fw1               eth0                      oob-mgmt-switch   swp18                     Fri Nov 20 19:51:49 2020
fw1               swp1                      border01          swp3                      Fri Nov 20 19:51:49 2020
...
```

Show only session for a given host interface port.

```
cumulus@switch:~$ netq show lldp swp5
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
spine01           swp5                      border01          swp51                     Fri Nov 20 10:28:20 2020
spine02           swp5                      border01          swp52                     Fri Nov 20 10:33:41 2020
spine03           swp5                      border01          swp53                     Fri Nov 20 10:28:32 2020
spine04           swp5                      border01          swp54                     Fri Nov 20 10:24:07 2020
```

#### Related Commands

- netq show events
- netq check lldp

- - -

### netq show mlag

### netq show ntp

### netq show ospf

### netq show sensors



## System 

address-history          :  Address history info for a IP address / prefix
    cl-btrfs-info            :  Btrfs Information
    cl-manifest              :  Manifest Information
    cl-pkg-info              :  Package Information
    cl-resource              :  Monitoring incoming and outgoing access control lists
    cl-ssd-util              :  SSD Utilization Information
    dom                      :  Digital Optical Monitoring


    inventory                :  Inventory information
    ip                       :  IPv4 related info
    ipv6                     :  IPv6 related info
    job-status               :  Display the status of running jobs
    kubernetes               :  Kubernetes Information
    mac-commentary           :  MAC commentary info for a mac address
    mac-history              :  Mac history info for a mac address
    macs                     :  Mac table or MAC address info
    neighbor-history         :  Neighbor history info for an IP address


    opta-health              :  Display health of apps on the OPTA
    opta-platform            :  Appliance version info and uptime

    recommended-pkg-version  :  Current host information to be considered
    resource-util            :  Displays CPU, Memory and disk utilisation for a given switch

    services                 :  System services

## Events and Notification

    events                   :  Display changes over time
    events-config            :  Events configured for suppression
    notification             :  Send notifications to Slack or PagerDuty
    tca                      :  Threshold Crossing Alerts
    wjh-drop                 :  Shows drops that are captured by WJH (What just happened) on Mellanox switches

## Configuration Commands

All of the NetQ configuration commands begin with netq config.
They are described here in alphabetical order by component group:
Add-on Configuration Commands
Agent Configuration Commands
Parser
Server
Telemetry Server

### Add-on Configuration Commands

netq config (add|del) addons
Installs or removes all additional software components available with a given release. [in a particular directory?]
Syntax
netq config add addons
netq config del addons
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
	None
Run From
	Telemetry server, leaf, spine, host?
Command History
	
Release
Description
1.0
Introduced

Usage Guidelines
Sample Usage
Related Commands




### NetQ Agent Configuration Commands

netq config (add|del) agent (stats|sensors)
Installs or removes [Starts or stops? Enables or disables?] collection of statistics or sensor measurements by NetQ Agent on [all or specific node?].
Syntax
	netq config add agent stats
	netq config del agent stats
netq config add agent sensors
neq config del agent sensors
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
	None
Run From
	Telemetry server, leaf, spine, host?
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	Use this command when you want to xxx. Be careful of xxx. Note yyy.
Sample Usage
	Starting statistical collection on agent node [check to see if it is running?]
cumulus@ts:~$ netq config add agent stats
Related Commands
Netq config add agent docker-monitor
Netq config add agent loglevel
Netq config add agent kubernetes-monitor

netq config add agent docker-monitor
Installs [Starts? Enables?] the Docker monitoring service on [all or specific node?].
Syntax
	netq config add agent docker-monitor [poll-period <text-duration-period>]
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
poll-period
The amount of time to monitor a docker container for statistics collection. The <text-duration-period> value must be specified in [seconds, minutes, hours?]
Run From
	Telemetry server, leaf, spine, host?
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	Use this command when you want to xxx. Be careful of xxx. Note yyy.
Sample Usage
	Set the monitoring duration of a docker container to one hour
cumulus@ts:~$ netq config add agent docker-monitor poll-period 3600
Related Commands
netq config add agent addons
netq config add agent loglevel
netq config add agent kubernetes-monitor

netq config add agent loglevel
Specifies the level of detail to display in the [system] log file[s?].
Syntax
	netq config add agent loglevel [debug|info|warning|error]
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
debug
Display errors, warnings, and informational events the system receives or generates.
info
Display only informational events
warning
Display warnings and informational events
error
Display xxx
Run From
	Telemetry server, leaf, spine, host?
JSON Output
	Not applicable
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	If no level is specified, the xxx level is used by default.
Changing the logging level takes place immediately, but prior content is not removed. 
[add definition of errors, warnings and info--what is the criteria/differentiation between…]
Sample Usage
	Set the display level of the [system?] log file to capture xxx
cumulus@ts:~$ netq config add agent loglevel warning
Related Commands
netq config add agent addons
netq config add agent docker-monitor
netq config add agent kubernetes-monitor

netq config add agent kubernetes-monitor
Installs [Starts? Enables?] the Kubernetes monitoring service on [all or specific node?].
Syntax
	netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments	
poll-period
The amount of time to monitor a kubernetes container for statistics collection. The <text-duration-period> value must be specified in [seconds, minutes, hours?]
Run From
	Telemetry server, leaf, spine, host?
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	Use this command when you want to xxx. Be careful of xxx. Note yyy.
Sample Usage
	Set the monitoring duration of a kubernetes container to one hour
cumulus@ts:~$ netq config add agent kubernetes-monitor poll-period 3600
Related Commands
netq config add agent addons
netq config add agent docker-monitor
netq config add agent loglevel

Parser Configuration Commands
Server Configuration Commands
Telemetry Server Configuration Commands


## Trace Commands


AGENT NOTIFIER COMMANDS

 netq config (add|del) experimental
   netq config (add|del) agent (stats|sensors)
   netq config reload parser
   netq config show server [json]
   netq config add server <ip-server>|<text-server-name> [port <1025-65535>] [vrf <text-vrf>]
   netq config add server <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  [vrf <text-vrf>]
   netq config del server
   netq config (start|stop|status|restart) agent
   netq config add agent loglevel [debug|info|warning|error]
   netq config del agent loglevel
   netq config show agent [kubernetes-monitor|loglevel|stats|sensors|frr-monitor|wjh|wjh-threshold|cpu-limit] [json]
netq config add agent docker-monitor [poll-period <text-duration-period>]
netq config del agent docker-monitor
netq config ts add notifier slack <text-notifier-name> webhook <text-webhook-url> [severity info | severity warning | severity error | severity debug | severity info] [tag <text-slack-tag>]
   netq config ts add notifier pagerduty <text-notifier-name> api-access-key <text-api-access-key> api-integration-key <text-api-integration-key> [severity info | severity warning | severity error | severity debug | severity info]
   netq config ts add notifier pagerduty <text-notifier-name> api-integration-key <text-api-integration-key> api-access-key <text-api-access-key> [severity info | severity warning | severity error | severity debug | severity info]
   netq config ts add notifier filter <text-filter-name> before <text-filter-name-anchor>
   netq config ts add notifier filter <text-filter-name> after <text-filter-name-anchor>
   netq config ts add notifier filter <text-filter-name> rule (BgpSession|ClagSession|LnvSession|Link|Port|Services|OS|Temp|Fan|PSU|License) <text-rule-value>
   netq config ts add notifier filter <text-filter-name> output <text-notifier-name>
   netq config ts add notifier loglevel [debug|info|warning|error]
   netq config ts del notifier loglevel
   netq config ts del notifier slack|pagerduty <text-notifier-name>
   netq config ts del notifier filter <text-notifier-name>
   netq config ts (start|stop|status|restart) notifier
   netq config ts show notifier [json]
   netq config ts show notifier loglevel [json]
   netq config ts add server <ip-master> <ip-replica> <ip-replica>
   netq config ts show server [<ip-server>|<text-server-name>|config] [json]
   netq config ts reset-cluster
netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
    netq config del agent kubernetes-monitor


netq config 
Description
Syntax
Abbreviated Syntax
Required Arguments
Optional Arguments
JSON Output
Command History
Usage Guidelines
Sample Usage
Related Commands



netq
cumulus@switch:~$ netq help list

netq - Query data across all nodes in fabric

Usage:
   netq help [<text-keywords>]
   netq help verbose
   netq help list

   netq resolve [vrf <vrf>|vlan <1-4096>] [around <text-time>]
   netq trace <mac> [vlan <1-4096>] from <src-hostname> [vrf <vrf>] [around <text-time>] [json]
   netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json]

   netq [<hostname>] show docker container [<ipv4> | <ipv6>] [portmap] [name <container-name> | image <container-image> | service <swarm-service-name> | network <network-name> ] [around <text-time>] [json]
   netq [<hostname>] show docker container [<ipv4> | <ipv6>] [portmap] [name <container-name> | image <container-image> | service <swarm-service-name> | network <network-name> ] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show docker container [<ipv4> | <ipv6>] <proto> [<port>] [network <network-name>] [around <text-time>] [json]
   netq [<hostname>] show docker container [<ipv4> | <ipv6>] <proto> [<port>] [network <network-name>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show docker container [<ipv4> | <ipv6> | name <container-name> | image <container-image> | service <swarm-service-name> | network <network-name> ] connectivity [around <text-time>] [json]
   netq <hostname> show docker container adjacent [interfaces <remote-physical-interface>] [around <text-time>] [json]

   netq [<hostname>] show docker summary [<docker-version>] [around <text-time>] [json]
   netq [<hostname>] show docker summary [<docker-version>] changes [between <text-time> and <text-endtime>] [json]

    netq config add agent docker-monitor [poll-period <text-duration-period>]
    netq config del agent docker-monitor

   netq [<hostname>] show docker network [name <network-name> | <ipv4/prefixlen>] [brief] [around <text-time>] [json]
   netq [<hostname>] show docker network [name <network-name> | <ipv4/prefixlen>] [brief] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show docker network driver <network-driver> [brief] [around <text-time>] [json]
   netq [<hostname>] show docker network driver <network-driver> [brief] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show docker service [name <swarm-service-name> | mode <mode>] [around <text-time>] [json]
   netq [<hostname>] show docker service [name <swarm-service-name> | mode <mode>] connectivity [vrf <vrf>] [around <text-time>] [json]
   netq <hostname> show impact docker service [<swarm-service-name>] [vrf <vrf>] [around <text-time>] [json]

   netq [<hostname>] show docker swarm cluster [<cluster-name>] [node-name <cluster-node>] [around <text-time>] [json]
   netq <hostname>   show docker swarm cluster [<cluster-name>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show docker swarm network [<swarm-service-name>] [around <text-time>] [json]
   netq  <hostname>  show docker swarm network [<swarm-service-name>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show docker swarm node [<node-name> | role <role>] [cluster <cluster-name>] [around <text-time>] [json]
   netq  <hostname>  show docker swarm node [<node-name> | role <role>] [cluster <cluster-name>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show ntp [out-of-sync | in-sync] [around <text-time>] [json]
   netq [<hostname>] show ntp changes [between <text-time> and <text-endtime>] [json]
   netq check ntp [around <text-time>] [json]

   netq [<hostname>] show services [<service-name>] [vrf <vrf>] [active|monitored] [around <text-time>] [json]
   netq [<hostname>] show services [<service-name>] [vrf <vrf>] [active|monitored] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show services [<service-name>] [vrf <vrf>] status (ok|warning|error|fail) [around <text-time>] [json]
   netq [<hostname>] show services [<service-name>] [vrf <vrf>] status (ok|warning|error|fail) changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show services [<service-name>] [vrf <vrf>] status (ok|warning|error|fail) changes [json]

   netq [<hostname>] show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
   netq [<hostname>] show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
   netq [<hostname>] show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show interfaces [<remote-interface>] [state <remote-interface-state>] [around <text-time>] [count] [json]
   netq [<hostname>] show interfaces [<remote-interface>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show interfaces type (bond|bridge|eth|loopback|macvlan|swp|vlan|vrf|vxlan) [state <remote-interface-state>] [around <text-time>] [count] [json]
   netq [<hostname>] show interfaces type (bond|bridge|eth|loopback|macvlan|swp|vlan|vrf|vxlan) changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show ip neighbors [<remote-interface>] [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>] [<mac>]  [around <text-time>] [count] [json]
   netq [<hostname>] show ip neighbors [<remote-interface>] [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>] [<mac>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show ipv6 neighbors [<remote-interface>] [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [count] [json]
   netq [<hostname>] show ipv6 neighbors [<remote-interface>] [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>] [<mac>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [count] [json]
   netq [<hostname>] show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [origin] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [count] [json]
   netq [<hostname>] show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [origin] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show interfaces physical [<physical-port>] [empty|plugged] [peer] [vendor <module-vendor> | model <module-model>| module] [around <text-time>] [json]
   netq [<hostname>] show interfaces physical [<physical-port>] [empty|plugged] [vendor <module-vendor> | model <module-model> | module] changes [between <text-time> and <text-endtime>] [json]
   netq check interfaces [unverified] [<physical-hostname> <physical-port> | <physical-hostname>] [around <text-time>] [json]
   netq check interfaces <physical-hostname> <physical-port> and <peer-physical-hostname> <peer-physical-port> [around <text-time>] [json]

   netq check license [around <text-time>] [json]
   netq [<hostname>] show inventory brief [json]
   netq [<hostname>] show inventory asic [vendor <asic-vendor>| model <asic-model>| model-id <asic-model-id>] [json]
   netq [<hostname>] show inventory board [vendor <board-vendor>|model <board-model>] [json]
   netq [<hostname>] show inventory cpu [arch <cpu-arch>] [json]
   netq [<hostname>] show inventory disk [name <disk-name>|transport <disk-transport>| vendor <disk-vendor>] [json]
   netq [<hostname>] show inventory license [cumulus] [around <text-time>] [json]
   netq [<hostname>] show inventory license [cumulus] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show inventory memory [type <memory-type>|vendor <memory-vendor>] [json]
   netq [<hostname>] show inventory os [version <os-version>|name <os-name>] [json]
   netq [<hostname>] show inventory os [version <os-version>|name <os-name>] changes [between <text-time> and <text-endtime>] [json]

   netq check sensors [around <text-time>] [json]
   netq [<hostname>] show sensors all [changes|around <text-time>] [json]
   netq [<hostname>] show sensors psu [<psu-name>] [changes|around <text-time>] [json]
   netq [<hostname>] show sensors temp [<temp-name>] [changes|around <text-time>] [json]
   netq [<hostname>] show sensors fan [<fan-name>] [changes|around <text-time>] [json]

   netq check evpn [around <text-time>] [json]
   netq [<hostname>] show evpn [vni <text-vni>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show evpn [vni <text-vni>] [around <text-time>] [json]

   netq check lnv [around <text-time>] [json]
   netq [<hostname>] show lnv [around <text-time>] [json]
   netq [<hostname>] show lnv changes [between <text-time> and <text-endtime>] [json]
   netq check vxlan [around <text-time>] [json]
   netq [<hostname>] show vxlan [vni <text-vni>] [around <text-time>] [json]
   netq [<hostname>] show vxlan [vni <text-vni>] changes [between <text-time> and <text-endtime>] [json]
   netq check agents [json]
   netq [<hostname>] show agents [changes] [json]

   netq [<hostname>] show changes [<ipv4>|<ipv6>|<ipv4> vrf <vrf>|<ipv6> vrf <vrf>|vrf <vrf>] between <text-time> and <text-endtime> [json]

   netq config (add|del) experimental
   netq config (add|del) addons
   netq config (add|del) agent (stats|sensors)
   netq config reload parser

   netq config show server [json]
   netq config add server <ip-server>|<text-server-name> [port <1025-65535>] [vrf <text-vrf>]
   netq config add server <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  [vrf <text-vrf>]
   netq config del server


   netq config (start|stop|status|restart) agent
   netq config add agent loglevel [debug|info|warning|error]
   netq config del agent loglevel
   netq config show agent [kubernetes-monitor|docker-monitor|loglevel|stats|sensors] [json]

   netq example check bgp
   netq example check clag
   netq example check mtu
   netq example find-duplicates
   netq example find-origin
   netq example ha-setup
   netq example query
   netq example regexp
   netq example resolve macs
   netq example resolve routes
   netq example startup
   netq example stats
   netq example trace
   netq config ts add notifier slack <text-notifier-name> webhook <text-webhook-url> [severity info | severity warning | severity error | severity debug | severity info] [tag <text-slack-tag>]
   netq config ts add notifier pagerduty <text-notifier-name> api-access-key <text-api-access-key> api-integration-key <text-api-integration-key> [severity info | severity warning | severity error | severity debug | severity info]
   netq config ts add notifier pagerduty <text-notifier-name> api-integration-key <text-api-integration-key> api-access-key <text-api-access-key> [severity info | severity warning | severity error | severity debug | severity info]
   netq config ts add notifier filter <text-filter-name> before <text-filter-name-anchor>
   netq config ts add notifier filter <text-filter-name> after <text-filter-name-anchor>
   netq config ts add notifier filter <text-filter-name> rule (BgpSession|ClagSession|LnvSession|Link|Port|Services|OS|Temp|Fan|PSU|License) <text-rule-value>
   netq config ts add notifier filter <text-filter-name> output <text-notifier-name>
   netq config ts add notifier loglevel [debug|info|warning|error]
   netq config ts del notifier loglevel
   netq config ts del notifier slack|pagerduty <text-notifier-name>
   netq config ts del notifier filter <text-notifier-name>
   netq config ts (start|stop|status|restart) notifier
   netq config ts show notifier [json]
   netq config ts show notifier loglevel [json]


   netq config ts add server <ip-master> <ip-replica> <ip-replica>
   netq config ts show server [<ip-server>|<text-server-name>|config] [json]
   netq config ts reset-cluster

   netq ts decommission <hostname-to-purge> purge

## Kubernetes Commands

   netq [<hostname>] show kubernetes cluster [name <kube-cluster-name>] [around <text-time>] [json]
   netq [<hostname>]   show kubernetes cluster [name <kube-cluster-name>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show kubernetes node [components] [name <kube-node-name>] [cluster <kube-cluster-name> ] [label <kube-node-label>] [around <text-time>] [json]
   netq [<hostname>]  show kubernetes node [components] [name <kube-node-name>] [cluster <kube-cluster-name> ] [label <kube-node-label>] changes [between <text-time> and <text-endtime>] [json]

    netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
    netq config del agent kubernetes-monitor

   netq [<hostname>] show kubernetes daemon-set [name <kube-ds-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-ds-label>] [around <text-time>] [json]
   netq [<hostname>] show kubernetes daemon-set [name <kube-ds-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-ds-label>] connectivity [around <text-time>] [json]
   netq  [<hostname>]  show kubernetes daemon-set [name <kube-ds-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-ds-label>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show kubernetes deployment [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] [around <text-time>] [json]
   netq [<hostname>] show kubernetes deployment [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] connectivity [around <text-time>] [json]
   netq [<hostname>] show kubernetes deployment [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show kubernetes pod [name <kube-pod-name>] [cluster <kube-cluster-name> ] [namespace <namespace>] [label <kube-pod-label>] [pod-ip <kube-pod-ipaddress>] [node <kube-node-name>] [around <text-time>] [json]
   netq [<hostname>] show kubernetes pod [name <kube-pod-name>] [cluster <kube-cluster-name> ] [namespace <namespace>] [label <kube-pod-label>] [pod-ip <kube-pod-ipaddress>] [node <kube-node-name>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show kubernetes replication-controller [name <kube-rc-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rc-label>] [around <text-time>] [json]
   netq [<hostname>]  show kubernetes replication-controller [name <kube-rc-name>] [cluster <kube-cluster-name>] [namespace <namespace>]  [label <kube-rc-label>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show kubernetes replica-set [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] [around <text-time>] [json]
   netq [<hostname>] show kubernetes replica-set [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] connectivity [around <text-time>] [json]
   netq [<hostname>]  show kubernetes replica-set [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show kubernetes service [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] [around <text-time>] [json]
   netq [<hostname>] show kubernetes service [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] connectivity [around <text-time>] [json]
   netq [<hostname>] show kubernetes service [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] changes [between <text-time> and <text-endtime>] [json]

   netq  <hostname>  show impact kubernetes service [master <kube-master-node>] [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] [around <text-time>] [json]
   netq <hostname> show impact kubernetes replica-set [master <kube-master-node>] [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] [around <text-time>] [json]
   netq <hostname> show impact kubernetes deployment [master <kube-master-node>] [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] [around <text-time>] [json]

   
   netq [<hostname>] show clag [around <text-time>] [json]
   netq [<hostname>] show clag changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show lldp [<remote-physical-interface>] [around <text-time>] [json]
   netq [<hostname>] show lldp [<remote-physical-interface>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show macs [<mac>] [vlan <1-4096>] [origin] [around <text-time>] [json]
   netq [<hostname>] show macs [<mac>] [vlan <1-4096>] [around <text-time>] count [json]
   netq [<hostname>] show macs [<mac>] [vlan <1-4096>] [origin] changes [between <text-time> and <text-endtime>] [json]
   netq <hostname> show macs egress-port <egress-port> [<mac>] [vlan <1-4096>] [origin] [around <text-time>] [json]
   netq <hostname> show macs egress-port <egress-port> [<mac>] [vlan <1-4096>] [origin] changes [between <text-time> and <text-endtime>] [json]

   netq <hostname> show stp topology [around <text-time>] [json]




### Notification Commands Overview

The NetQ Command Line Interface (CLI) is used to filter and send notifications to third-party tools based on severity, service, event-type, and device. You can use TAB completion or the `help` option to assist when needed.

The command syntax for standard events is:

    ##Channels
    netq add notification channel slack <text-channel-name> webhook <text-webhook-url> [severity info|severity warning|severity error|severity debug] [tag <text-slack-tag>]
    netq add notification channel pagerduty <text-channel-name> integration-key <text-integration-key> [severity info|severity warning|severity error|severity debug]
     
    ##Rules and Filters
    netq add notification rule <text-rule-name> key <text-rule-key> value <text-rule-value>
    netq add notification filter <text-filter-name> [severity info|severity warning|severity error|severity debug] [rule <text-rule-name-anchor>] [channel <text-channel-name-anchor>] [before <text-filter-name-anchor>|after <text-filter-name-anchor>]
     
    ##Management
    netq del notification channel <text-channel-name-anchor>
    netq del notification filter <text-filter-name-anchor>
    netq del notification rule <text-rule-name-anchor>
    netq show notification [channel|filter|rule] [json]

The command syntax for events with user-configurable thresholds is:

    ##Rules and Filters
    netq add tca event_id <event-name> scope <regex-filter> [severity <critical|info>] threshold <value>

    ##Management
    netq add tca tca_id <tca-rule-name> is_active <true|false>
    netq add tca tca_id <tca-rule-name> channel drop <channel-name>
    netq del tca tca_id <tca-rule-name>
    netq show tca [tca_id <tca-rule-name>]

The command syntax for a server proxy is:

    ##Proxy
    netq add notification proxy <text-proxy-hostname> [port <text-proxy-port>]
    netq show notification proxy
    netq del notification proxy

The various command options are described in the following sections where they are used.

## LCM Commands

The NetQ CLI provides a number of `netq lcm` commands to perform LCM. The syntax of these commands is:

    netq lcm upgrade name <text-job-name> image-id <text-image-id> license <text-cumulus-license> hostnames <text-switch-hostnames> [order <text-upgrade-order>] [run-before-after]
    netq lcm add credentials (username <text-switch-username> password <text-switch-password> | ssh-key <text-ssh-key>)
    netq lcm add role (superspine | spine | leaf | exit) switches <text-switch-hostnames>
    netq lcm del credentials
    netq lcm show credentials [json]
    netq lcm show switches [version <text-cumulus-linux-version>] [json]
    netq lcm show status <text-lcm-job-id> [json]
    netq lcm add image <text-image-path>
    netq lcm del image <text-image-id>
    netq lcm show images [<text-image-id>] [json]
    netq lcm show upgrade-jobs [json]

## Agent Commands

The agent configuration commands include:

    netq config add agent cluster-servers <text-opta-ip-list> [port <text-opta-port>] [vrf <text-vrf-name>]
    netq config add agent cpu-limit [<text-limit-number>]
    netq config add agent frr-monitor [<text-frr-docker-name>]
    netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
    netq config add agent loglevel [debug|error|info|warning]
    netq config add agent sensors
    netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>]
    netq config (start|stop|status|restart) agent
    netq config del agent (cluster-servers|cpu-limit|frr-monitor|kubernetes-monitor|loglevel|sensors|server|stats|wjh)
    netq config show agent [cpu-limit|frr-monitor|kubernetes-monitor|loglevel|sensors|stats|wjh] [json]

## Inventory Commands

### Hardware Commands

The NetQ CLI provides a number of commands to monitor hardware inventory on switches. The syntax of these commands is:

```
netq [<hostname>] show inventory brief [opta] [json]
netq [<hostname>] show inventory asic [vendor <asic-vendor>|model <asic-model>|model-id <asic-model-id>] [opta] [json]
netq [<hostname>] show inventory board [vendor <board-vendor>|model <board-model>] [opta] [json]
netq [<hostname>] show inventory cpu [arch <cpu-arch>] [opta] [json]
netq [<hostname>] show inventory disk [name <disk-name>|transport <disk-transport>|vendor <disk-vendor>] [opta] [json]
netq [<hostname>] show inventory license [cumulus] [status ok|status missing] [around <text-time>] [opta] [json]
netq [<hostname>] show inventory memory [type <memory-type>|vendor <memory-vendor>] [opta] [json]
netq [<hostname>] show inventory os [version <os-version>|name <os-name>] [opta] [json]

netq [<hostname>] show sensors all [around <text-time>] [json]
netq [<hostname>] show sensors psu [<psu-name>] [around <text-time>] [json]
netq [<hostname>] show sensors temp [<temp-name>] [around <text-time>] [json]
netq [<hostname>] show sensors fan [<fan-name>] [around <text-time>] [json]

netq [<hostname>] show interface-stats [errors|all] [<physical-port>] [around <text-time>] [json]
netq [<hostname>] show interface-utilization [<text-port>] [tx|rx] [around <text-time>] [json]
netq [<hostname>] show resource-util [cpu | memory] [around <text-time>] [json]
netq [<hostname>] show resource-util disk [<text-diskname>] [around <text-time>] [json]
netq [<hostname>] show cl-ssd-util [around <text-time>] [json]
netq [<hostname>] show cl-btrfs-info [around <text-time>] [json]
```

{{<notice note>}}
The keyword values for the <code>vendor</code>, <code>model</code>, <code>model-id</code>, <code>arch</code>, <code>name</code>, <code>transport</code>, <code>type</code>, <code>version</code>, <code>psu</code>, <code>temp</code>, and <code>fan</code> keywords are specific to your deployment. For example, if you have devices with CPU architectures of only one type, say Intel x86, then that is the only option available for the <code>cpu-arch</code> keyword value. If you have multiple CPU architectures, say you also have ARMv7, then that would also be an option for you.
{{</notice>}}

### Software Commands

The NetQ CLI provides a number of commands to monitor software inventory on switches. The syntax for these commands is:

```
netq [<hostname>] show agents
netq [<hostname>] show inventory brief [json]
netq [<hostname>] show inventory license [cumulus] [status ok|status missing] [around <text-time>] [json]
netq [<hostname>] show inventory os [version <os-version>|name <os-name>] [json]

netq [<hostname>] show cl-manifest [json]
netq [<hostname>] show cl-pkg-info [<text-package-name>] [around <text-time>] [json]
netq [<hostname>] show recommended-pkg-version [release-id <text-release-id>] [package-name <text-package-name>] [json]
netq [<hostname>] show cl-resource acl [ingress | egress] [around <text-time>] [json]
netq [<hostname>] show cl-resource forwarding [around <text-time>] [json]
```

{{<notice note>}}
The values for the <code>name</code> option are specific to your deployment. For example, if you have devices with only one type of OS, say Cumulus Linux, then that is the only option available for the <code>os-name</code> option value. If you have multiple OSs running, say you also have Ubuntu, then that would also be an option for you.
{{</notice>}}
