---
title: S Commands
author: Cumulus Networks
weight: 1106
toc: 3
right_toc_levels: 2
pdfhidden: true
draft: true
---
This topic includes all commands that begin with `netq s*`.

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

- netq show unit-tests agent
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
- The received address prefix for IPv4/IPv6/EVPN when session is established
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

- netq show unit-tests bgp
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

- netq show unit-tests clag
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

- netq show unit-tests evpn
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
- netq show unit-tests interfaces

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

Displays the health of all MLAG sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

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
netq [<hostname>] show mlag
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
cumulus@switch:~$ netq show mlag
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

- netq show events type clag
- netq check mlag
- netq show unit-tests mlag

- - -

### netq show notification

    netq show notification [channel|filter|rule] [json]

- - -

### netq show ntp

Displays whether the all or a specific node is in time synchronization with the NetQ appliance or VM currently or for a time in the past. The output provides:

- The synchronization status
- The current time server being used for synchronization
- The number of hierarchical levels the switch or host is from reference clock
- The NTP application used to obtain and synchronize the clock on the node

#### Syntax

```
netq [<hostname>] show ntp
    [out-of-sync | in-sync]
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| out-of-sync | NA | Only display results for devices that are out of synchronization with the NetQ appliance or VM |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| x.y.z | xxx |

#### Sample Usage

Basic show: all devices, all states, currently

```
cumulus@switch:~$ netq show ntp
Matching ntp records:
Hostname          NTP Sync Current Server    Stratum NTP App
----------------- -------- ----------------- ------- ---------------------
border01          yes      oob-mgmt-server   3       ntpq
border02          yes      oob-mgmt-server   3       ntpq
fw1               no       -                 16      ntpq
fw2               no       -                 16      ntpq
leaf01            yes      oob-mgmt-server   3       ntpq
leaf02            yes      oob-mgmt-server   3       ntpq
leaf03            yes      oob-mgmt-server   3       ntpq
leaf04            yes      oob-mgmt-server   3       ntpq
netq-ts           yes      eterna.binary.net 2       chronyc
oob-mgmt-server   yes      titan.crash-ove   2       ntpq
server01          yes      oob-mgmt-server   3       ntpq
server02          yes      oob-mgmt-server   3       ntpq
server03          yes      oob-mgmt-server   3       ntpq
server04          yes      oob-mgmt-server   3       ntpq
server05          yes      oob-mgmt-server   3       ntpq
server06          yes      oob-mgmt-server   3       ntpq
server07          yes      oob-mgmt-server   3       ntpq
server08          yes      oob-mgmt-server   3       ntpq
spine01           yes      oob-mgmt-server   3       ntpq
spine02           yes      oob-mgmt-server   3       ntpq
spine03           yes      oob-mgmt-server   3       ntpq
spine04           yes      oob-mgmt-server   3       ntpq
```

#### Related Commands

- netq check ntp
- netq show unit-tests ntp

- - -

### netq show ospf

Displays the health of all OSPF sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The host interface
- The routing domain (area)
- Whether numbered or unnumbered protocol is being used
- The operational state of the session (up or down)
- The hostname and interface of the peer node
- When the last change was made to any of these items

#### Syntax

```
netq [<hostname>] show ospf
    [<remote-interface>]
    [area <area-id>]
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<remote-interface\> | Only display results for the host inteface with this name |
| area | \<area-id\> | Only display results for devices in this routing domain |
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
cumulus@switch:~$ netq show ospf
Matching ospf records:
Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019
leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
leaf02            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp2                      Thu Feb  7 14:42:16 2019
leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
leaf03            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp3                      Thu Feb  7 14:42:16 2019
leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019
leaf04            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp4                      Thu Feb  7 14:42:16 2019
spine01           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp51                     Thu Feb  7 14:42:16 2019
spine01           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp51                     Thu Feb  7 14:42:16 2019
spine02           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp52                     Thu Feb  7 14:42:16 2019
spine02           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp52                     Thu Feb  7 14:42:16 2019
```

#### Related Commands

- netq show events
- netq check ospf
- netq show unit-tests ospf

- - -

### netq show sensors

Displays the status of all fan, power supply, and temperature sensors on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The sensor name and user-defined description
- The operational state of the sensor
- Any messages, when available
- When the last change was made to any of these items

#### Syntax

There are four forms of this command based on whether you want to view data for all sensors or only one category of sensors.

```
netq [<hostname>] show sensors
    all
    [around <text-time>]
    [json]

netq [<hostname>] show sensors
    fan [<fan-name>]
    [around <text-time>]
    [json]

netq [<hostname>] show sensors
    psu [<psu-name>]
    [around <text-time>]
    [json]

netq [<hostname>] show sensors
    temp [<temp-name>]
    [around <text-time>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| all | NA | Display data for all sensors |
| fan | \<fan-name\> | Display data for all fan sensors or the one specified using the `fan-name` value |
| psu | \<psu-name\> | Display data for all power supply unit sensors or the one specified using the`psu-name` value |
| temp | \<temp-name\> | Display data for all temperature sensors or the one specified using the `temp-name` value |

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
| x.y.z | xxx |

#### Sample Usage

Basic show: all devices, all states, currently

```
cumulus@switch:~$ netq show sensors all
Matching sensors records:
Hostname          Name            Description                         State      Message                             Last Changed
----------------- --------------- ----------------------------------- ---------- ----------------------------------- -------------------------
border01          fan5            fan tray 3, fan 1                   ok                                             Tue Nov 24 03:57:06 2020
border01          psu1fan1        psu1 fan                            ok                                             Tue Nov 24 03:57:06 2020
border01          fan4            fan tray 2, fan 2                   ok                                             Tue Nov 24 03:57:06 2020
border01          fan2            fan tray 1, fan 2                   ok                                             Tue Nov 24 03:57:06 2020
border01          fan3            fan tray 2, fan 1                   ok                                             Tue Nov 24 03:57:06 2020
border01          fan6            fan tray 3, fan 2                   ok                                             Tue Nov 24 03:57:06 2020
border01          psu2fan1        psu2 fan                            ok                                             Tue Nov 24 03:57:06 2020
border01          fan1            fan tray 1, fan 1                   ok                                             Tue Nov 24 03:57:06 2020
border02          fan3            fan tray 2, fan 1                   ok                                             Tue Nov 24 04:13:30 2020
border02          psu1fan1        psu1 fan                            ok                                             Tue Nov 24 04:13:30 2020
border02          fan1            fan tray 1, fan 1                   ok                                             Tue Nov 24 04:13:30 2020
border02          fan6            fan tray 3, fan 2                   ok                                             Tue Nov 24 04:13:30 2020
border02          fan5            fan tray 3, fan 1                   ok                                             Tue Nov 24 04:13:30 2020
border02          psu2fan1        psu2 fan                            ok                                             Tue Nov 24 04:13:30 2020
border02          fan4            fan tray 2, fan 2                   ok                                             Tue Nov 24 04:13:30 2020
border02          fan2            fan tray 1, fan 2                   ok                                             Tue Nov 24 04:13:30 2020
fw1               psu2fan1        psu2 fan                            ok                                             Tue Nov 24 19:50:49 2020
fw1               psu1fan1        psu1 fan                            ok                                             Tue Nov 24 19:50:49 2020
...
```

Show data for the fan4 sensor on all nodes.

```
cumulus@switch:~$ netq show sensors fan fan4
Matching sensors records:
Hostname          Name            Description                         State      Speed      Max      Min      Message                             Last Changed
----------------- --------------- ----------------------------------- ---------- ---------- -------- -------- ----------------------------------- -------------------------
border01          fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Tue Nov 24 03:57:06 2020
border02          fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Tue Nov 24 04:13:30 2020
fw1               fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Tue Nov 24 19:50:49 2020
fw2               fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Tue Nov 24 19:50:51 2020
spine03           fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Tue Nov 24 04:03:01 2020
spine04           fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Tue Nov 24 04:13:52 2020
```

#### Related Commands

- netq show events
- netq check sensors
- netq show unit-tests sensors

- - -

### netq show unit-tests

Displays a list of all validation tests that are run for the associated `netq check` command. The output provides an ID, name, and brief description of each validation test.

Refer to {{<link title="Validate Operations" text="Validate Operations">}} for additional usage information.

#### Syntax

```
netq show unit-tests agent [json]
netq show unit-tests bgp [json]
netq show unit-tests clag [json]
netq show unit-tests cl-version [json]
netq show unit-tests evpn [json]
netq show unit-tests interfaces [json]
netq show unit-tests license [json]
netq show unit-tests mlag [json]
netq show unit-tests mtu [json]
netq show unit-tests ntp [json]
netq show unit-tests ospf [json]
netq show unit-tests sensors [json]
netq show unit-tests vlan [json]
netq show unit-tests vxlan [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| agent, bgp, clag, cl-version, evpn, interfaces, license, mlag, mtu, ntp, ospf, sensors, vlan, or vxlan | NA | Display tests run during standard validation for the protocol or service with this name |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Swapped the order of the `unit-tests` keyword and the protocol or service name |
| ??? | Introduced |

#### Sample Usage

Show tests for BGP

```
cumulus@netq-ts:~$ netq show unit-tests bgp
   0 : Session Establishment     - check if BGP session is in established state
   1 : Address Families          - check if tx and rx address family advertisement is consistent between peers of a BGP session
   2 : Router ID                 - check for BGP router id conflict in the network

Configured global result filters:

Configured per test result filters:
```

#### Related Commands

- netq show events
- netq check sensors

- - -

### netq show vlan

Displays the configuration of all VLANs on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The switch or host name
- The VLANs associated with that node
- The SVIs (switch virtual interfaces) associated with that node
- When the last change was made to any of these items

#### Syntax

```
netq [<hostname>] show vlan
    [<1-4096>]
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<1-4096\> | Only display results for the VLAN with this name |
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
cumulus@switch:~$ netq show vlan
Matching vlan records:
Hostname          VLANs                     SVIs                      Last Changed
----------------- ------------------------- ------------------------- -------------------------
border01          1,10,20,30,4001-4002                                Tue Nov 24 20:42:07 2020
border02          1,10,20,30,4001-4002                                Tue Nov 24 20:42:07 2020
leaf01            1,10,20,30,4001-4002      10 20 30                  Tue Nov 24 20:42:07 2020
leaf02            1,10,20,30,4001-4002      10 20 30                  Tue Nov 24 20:42:08 2020
leaf03            1,10,20,30,4001-4002      10 20 30                  Tue Nov 24 20:42:08 2020
leaf04            1,10,20,30,4001-4002      10 20 30                  Tue Nov 24 20:42:08 2020
```

Show configuration for a particular VLAN.

```
cumulus@switch:~$ netq show vlan 20
Matching vlan records:
Hostname          VLAN   Ports                               SVI  Last Changed
----------------- ------ ----------------------------------- ---- -------------------------
border01          20                                         no   Tue Nov 24 20:50:46 2020
border02          20                                         no   Tue Nov 24 20:50:47 2020
leaf01            20     bond2,vni20                         yes  Tue Nov 24 20:50:47 2020
leaf02            20     bond2,vni20                         yes  Tue Nov 24 20:50:47 2020
leaf03            20     bond2,vni20                         yes  Tue Nov 24 20:50:48 2020
leaf04            20     bond2,vni20                         yes  Tue Nov 24 20:50:48 2020
```

#### Related Commands

- netq show events
- netq show interfaces
- netq show macs
- netq check vlan
- netq show unit-tests vlan

- - -

### netq show vxlan

Displays the configuration of all VXLANs on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The switch or host name
- The VNI associated with that node
- The protocol used over the interface
- The VTEP IP for the node
- The replication list, if appropriate
- When the last change was made to any of these items

#### Syntax

```
netq [<hostname>] show vxlan
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
| vni | \<text-vni\> | Only display results for the VNI with this name |
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
cumulus@switch:~$ netq show vxlan
Matching vxlan records:
Hostname          VNI        Protoc VTEP IP          VLAN   Replication List                    Last Changed
                             ol
----------------- ---------- ------ ---------------- ------ ----------------------------------- -------------------------
border01          4001       EVPN   10.0.1.254       4001                                       Tue Nov 10 22:29:05 2020
border01          4002       EVPN   10.0.1.254       4002                                       Tue Nov 10 22:29:05 2020
border02          4001       EVPN   10.0.1.254       4001                                       Tue Nov 10 22:29:06 2020
border02          4002       EVPN   10.0.1.254       4002                                       Tue Nov 10 22:29:06 2020
leaf01            30         EVPN   10.0.1.1         30     10.0.1.2(leaf04, leaf03)            Tue Nov 10 22:29:04 2020
leaf01            10         EVPN   10.0.1.1         10     10.0.1.2(leaf04, leaf03)            Tue Nov 10 22:29:04 2020
leaf01            4001       EVPN   10.0.1.1         4001                                       Tue Nov 10 22:29:04 2020
leaf01            4002       EVPN   10.0.1.1         4002                                       Tue Nov 10 22:29:04 2020
leaf01            20         EVPN   10.0.1.1         20     10.0.1.2(leaf04, leaf03)            Tue Nov 10 22:29:04 2020
leaf02            30         EVPN   10.0.1.1         30     10.0.1.2(leaf04, leaf03)            Tue Nov 10 22:29:15 2020
leaf02            10         EVPN   10.0.1.1         10     10.0.1.2(leaf04, leaf03)            Tue Nov 10 22:29:15 2020
leaf02            4001       EVPN   10.0.1.1         4001                                       Tue Nov 10 22:29:15 2020
leaf02            4002       EVPN   10.0.1.1         4002                                       Tue Nov 10 22:29:15 2020
leaf02            20         EVPN   10.0.1.1         20     10.0.1.2(leaf04, leaf03)            Tue Nov 10 22:29:15 2020
leaf03            30         EVPN   10.0.1.2         30     10.0.1.1(leaf01, leaf02)            Tue Nov 10 22:28:31 2020
leaf03            10         EVPN   10.0.1.2         10     10.0.1.1(leaf01, leaf02)            Tue Nov 10 22:28:31 2020
leaf03            4001       EVPN   10.0.1.2         4001                                       Tue Nov 10 22:28:31 2020
leaf03            4002       EVPN   10.0.1.2         4002                                       Tue Nov 10 22:28:31 2020
leaf03            20         EVPN   10.0.1.2         20     10.0.1.1(leaf01, leaf02)            Tue Nov 10 22:28:31 2020
leaf04            30         EVPN   10.0.1.2         30     10.0.1.1(leaf01, leaf02)            Tue Nov 10 22:29:34 2020
leaf04            4001       EVPN   10.0.1.2         4001                                       Tue Nov 10 22:29:34 2020
leaf04            10         EVPN   10.0.1.2         10     10.0.1.1(leaf01, leaf02)            Tue Nov 10 22:29:34 2020
leaf04            4002       EVPN   10.0.1.2         4002                                       Tue Nov 10 22:29:34 2020
leaf04            20         EVPN   10.0.1.2         20     10.0.1.1(leaf01, leaf02)            Tue Nov 10 22:29:34 2020
```

Show configuration for a particular VNI.

```
cumulus@switch:~$ netq show vxlan vni 4001
Matching vxlan records:
Hostname          VNI        Protoc VTEP IP          VLAN   Replication List                    Last Changed
                             ol
----------------- ---------- ------ ---------------- ------ ----------------------------------- -------------------------
border01          4001       EVPN   10.0.1.254       4001                                       Tue Nov 10 22:29:05 2020
border02          4001       EVPN   10.0.1.254       4001                                       Tue Nov 10 22:29:06 2020
leaf01            4001       EVPN   10.0.1.1         4001                                       Tue Nov 10 22:29:04 2020
leaf02            4001       EVPN   10.0.1.1         4001                                       Tue Nov 10 22:29:15 2020
leaf03            4001       EVPN   10.0.1.2         4001                                       Tue Nov 10 22:28:31 2020
leaf04            4001       EVPN   10.0.1.2         4001                                       Tue Nov 10 22:29:34 2020
```

#### Related Commands

- netq show events
- netq show interfaces
- netq check vxlan
- netq show unit-tests vxlan

- - -

## System and Inventory

### netq show address-history

Displays where an IPv4 or IPv6 address has lived in your network fabric in the last 24 hours. The output provides:

- When the address was last changed
- The switch or host name where the address resides
- The interface where the address resides
- The address prefix and mask
- The associated VRF

By default, each row in the output is a thread (or group) sorted by VLAN.

#### Syntax

```
netq [<hostname>] show address-history
    <text-prefix>
    [ifname <text-ifname>]
    [vrf <text-vrf>]
    [diff]
    [between <text-time> and <text-endtime>]
    [listby <text-list-by>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-prefix\> | Display results for the switches and hosts with this address prefix |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| ifname | \<text-ifname\> | Only display results for the interface with this name |
| vrf | \<text-vrf\> | Only display results for the VRF with this name |
| diff | NA | Only display the differences associated with each change |
| between | \<text-time\> and \<text-endtime\> | Only display results between the snapshots taken at these times |
| listby | \<text-list-by\> | Display results by the specified attribute. Attributes include the interface name, VRF name, and hostname. |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

{{<notice note>}}
When entering a time value with the <code>between</code> option, you must include a numeric value <em>and</em> the unit of measure:
<ul>
<li><strong>d</strong>: day(s)</li>
<li><strong>h</strong>: hour(s)</li>
<li><strong>m</strong>: minute(s)</li>
<li><strong>s</strong>: second(s)</li>
<li><strong>now</strong>
</ul>

The start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{</notice>}}

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

#### Sample Usage

Basic show: all devices, all VLANs, in last 24 hours

```
cumulus@switch:~$ netq show address-history 10.10.10.3
Matching addresshistory records:
Last Changed              Hostname          Ifname       Prefix                         Mask     Vrf
------------------------- ----------------- ------------ ------------------------------ -------- ---------------
Mon Nov 23 22:28:42 2020  leaf03            lo           10.10.10.3                     32       default

```

Show only the differences between now and four months ago.

```
cumulus@switch:~$ netq show address-history 10.10.10.3 between now and 120d
Matching addresshistory records:
Last Changed              Hostname          Ifname       Prefix                         Mask     Vrf
------------------------- ----------------- ------------ ------------------------------ -------- ---------------
Thu Oct 15 22:28:16 2020  leaf03            lo           10.10.10.3                     32       default
```

Show changes grouped by VRF.

```
cumulus@switch:~$ netq show address-history 10.1.10.104 listby vrf
Matching addresshistory records:
Last Changed              Hostname          Ifname       Prefix                         Mask     Vrf
------------------------- ----------------- ------------ ------------------------------ -------- ---------------
Tue Nov 24 19:51:11 2020  server04          uplink       10.1.10.104                    24       default
```

#### Related Commands

- netq show mac-history

- - -

### netq show cl-btrfs-info

Displays status about disk utilization on a given device or all devices networkwide with BTRFS and Cumulus Linux 3.x installed. The output provides the following information for each device:

- Percentage of disk that is currently allocated
- Amount of space remaining (unallocated)
- Size of the largest data chunk
- Amount of space unused by data chunks
- Whether a rebalance of the disk is recommended
- When the last change was made to any of these items

For details about when a rebalance is recommended, refer to {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Configuration-and-Usage/Storage/When-to-Rebalance-BTRFS-Partitions/" text="When to Rebalance BTRFS Partitions">}}.

#### Syntax

```
netq [<hostname>] cl-btrfs-info
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Introduced |

#### Sample Usage

Basic show: all devices in last 24 hours

```
cumulus@switch:~$ netq show cl-btrfs-info
Matching btrfs_info records:
Hostname          Device Allocated     Unallocated Space    Largest Chunk Size   Unused Data Chunks S Rebalance Recommende Last Changed
                                                                                 pace                 d
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf01            37.79 %              3.58 GB              588.5 MB             771.91 MB            yes                  Wed Sep 16 21:25:17 2020
```

#### Related Commands

- netq show cl-ssd-util

- - -

### netq show cl-manifest

Displays the Cumulus Linux OS versions supported for a given device or all devices networkwide. The output provides the following information for each device:

- ASIC vendor the OS supports
- CPU architecture the OS supports
- Cumulus Linux version associated with the indicated ASIC and CPU

#### Syntax

```
netq [<hostname>] cl-manifest
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

#### Sample Usage

```
cumulus@switch:~$ netq show cl-manifest

Matching manifest records:
Hostname          ASIC Vendor          CPU Arch             Manifest Version
----------------- -------------------- -------------------- --------------------
border01          vx                   x86_64               3.7.6.1
border01          vx                   x86_64               3.7.10
border01          vx                   x86_64               3.7.11
border01          vx                   x86_64               3.6.2.1
...
fw1               vx                   x86_64               3.7.6.1
fw1               vx                   x86_64               3.7.10
fw1               vx                   x86_64               3.7.11
fw1               vx                   x86_64               3.6.2.1
...
leaf01            vx                   x86_64               4.1.0
leaf01            vx                   x86_64               4.0.0
leaf01            vx                   x86_64               3.6.2
leaf01            vx                   x86_64               3.7.2
...
leaf02            vx                   x86_64               3.7.6.1
leaf02            vx                   x86_64               3.7.10
leaf02            vx                   x86_64               3.7.11
leaf02            vx                   x86_64               3.6.2.1
...
```

#### Related Commands

- netq show cl-pkg-info
- netq show recommended-pkg-version

- - -

### netq show cl-pkg-info

Displays the versions for all software packages installed on a given device or all devices networkwide. The output provides the following information for each device:

- Package name and version
- Cumulus Linux version
- Package status
- When the last change was made to any of these items

The output can become very large for all devices and packages. When viewing results in a terminal window, consider filtering by hostname or package name to reduce the length of the output. Wildcards are not allowed for `hostname` or `text-package-name`.

#### Syntax

```
netq [<hostname>] cl-pkg-info
    [<text-package-name>]
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<text-package-name\> | Only display results for the software package with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Introduced |

#### Sample Usage

```
cumulus@switch:~$ netq leaf01 show cl-pkg-info

Matching package_info records:
Hostname          Package Name             Version              CL Version           Package Status       Last Changed
----------------- ------------------------ -------------------- -------------------- -------------------- -------------------------
leaf01            freeipmi-common          1.6.3-1.1            Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            libsystemd0              241-7~deb10u4        Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            arptables                0.0.4+snapshot201810 Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
                                           21-4
leaf01            libbinutils              2.31.1-16            Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            tzdata                   2020a-0+deb10u1      Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            gpgconf                  2.2.12-1+deb10u1     Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            irqbalance               1.5.0-3              Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            systemd                  241-7~deb10u4        Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            liblmdb0                 0.9.22-1             Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            libopts25                1:5.18.12-4          Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            libelf1                  0.176-1.1            Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            init-system-helpers      1.56+nmu1            Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            libudev1                 241-7~deb10u4        Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            gdisk                    1.0.3-1.1            Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            xxd                      2:8.1.0875-5         Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            libnl-nf-3-200           3.2.27-cl4.2.1u1     Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            libprotobuf17            3.6.1.3-2            Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            cron                     3.0pl1-133-cl4u1     Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
...
```

#### Related Commands

- netq show recommended-pkg-version
- netq show cl-manifest

- - -

### netq show cl-resource

Displays incoming and outgoing ACLs and amount of forwarding resources used for a given device or all devices networkwide. The output provides the following information for each device:

- For ACL resources
    - Count and percentage of Ingress and egress IPv4/IPv6 filter and mangle
    - Count and percentage of Ingress 802.1x filter
    - Count and percentage of Ingress mirror
    - Count and percentage of Regions
    - Count and percentage of Ingress PBR IPv4/IPv6 filter
    - Count and percentage of 18b, 32b, and 52b rules keys
    - Count and percentage of Layer 4 port range checkers
    - When the last change was made to any of these items
- For forwarding resources
    - Count and percentage of MAC address entries
    - Count and percentage of ECMP next hops
    - Count and percentage of IPv4/IPv6 host and route entries
    - Number of multicast routes
    - When the last change was made to any of these items

#### Syntax

This command comes in two forms:

```
netq [<hostname>] show cl-resource acl
    [ingress | egress]
    [around <text-time>]
    [json]

netq [<hostname>] show cl-resource forwarding
    [around <text-time>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| acl | NA | Display results for ACLs |
| forwarding | NA | Display results for forwarding resources |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| ingress | NA | Only display results for the incoming ACLs |
| egress | NA | Only display results for the outgoing ACLs |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

#### Sample Usage

Basic show: All devices, all ACLS

```
cumulus@switch:~$ netq leaf01 show cl-pkg-info

```

#### Related Commands

- netq show recommended-pkg-version
- netq show cl-manifest

- - -

### netq show cl-ssd-util

Displays utilization of 3ME3 solid state drives (SSDs) for a given device or all devices networkwide. These are primarily found in on-premises deployment. Tracking SSD utilization over time enables you to see any downward trend or instability of the drive before you receive an alarm. The output provides the following information for each drive:

- Percentage of PE cycles remaining for the drive
- Count of current PE cycles used by this drive
- Total number of PE cycles supported for this drive
- The drive model information
- When the last change was made to any of these items

#### Syntax

```
netq [<hostname>] show cl-ssd-util
    [around <text-time>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Introduced |

#### Sample Usage

Basic show: All drives, for a given device

```
cumulus@switch:~$ netq spine02 show cl-ssd-util
Hostname        Remaining PE Cycle (%)  Current PE Cycles executed      Total PE Cycles supported       SSD Model               Last Changed
spine02         80                      576                             2880                            M.2 (S42) 3ME3          Thu Oct 31 00:15:06 2019
```

#### Related Commands

- netq show cl-btrfs-info

- - -

### netq show ip/ipv6 addresses

Displays the IPv4 or IPv6 addresses configured for a given device or all devices networkwide, currently or for a time in the past. You can filter the output by remote-interface, address or prefix, and VRF. A count of addresses can be obtained for a given device. The output provides the following information for each address:

- Hostname of the device with the address
- Interface on the device with the address
- VRF, when configured, on the interface with the address
- When the last change was made to any of these items

#### Syntax

There are two sets of IP address commands, one for IPv4 and one for IPv6.

```
netq <hostname> show ip addresses
    [<remote-interface>]
    [<ipv4>|<ipv4/prefixlen>]
    [vrf <vrf>]
    [around <text-time>]
    [count]
    [json]

netq show ip addresses
    [<remote-interface>]
    [<ipv4>|<ipv4/prefixlen>]
    [vrf <vrf>]
    [subnet|supernet|gateway]
    [around <text-time>]
    [json]

netq <hostname> show ipv6 addresses
    [<remote-interface>]
    [<ipv6>|<ipv6/prefixlen>]
    [vrf <vrf>]
    [around <text-time>]
    [count]
    [json]

netq show ipv6 addresses
    [<remote-interface>]
    [<ipv6>|<ipv6/prefixlen>]
    [vrf <vrf>]
    [subnet|supernet|gateway]
    [around <text-time>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| ip | NA | Display TCP IPv4 addresses |
| ipv6 | NA | Display TCP IPv6 addresses |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<remote-interface\> | Only display results for switches and hosts with this interface |
| NA | \<ipv4\> | Only display results for switches and hosts with this IPv4 address |
| NA | \<ipv4/prefixlen\> | Only display results for switches and hosts with this IPv4 address and prefix |
| NA | \<ipv6\> | Only display results for switches and hosts with this IPv6 address |
| NA | \<ipv6/prefixlen\> | Only display results for switches and hosts with this IPv6 address and prefix |
| vrf | \<vrf\> | Only dispaly results for switches and hosts using this virtual route forwarding interface |
| subnet | NA | Only display results for addresses in the subnet |
| supernet | NA | Only display results for addresses in the supernet |
| gateway | NA | Only display results for addresses in the gateway |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added ability to display all addresses in a subnet or supernet or the layer 3 gateway of an address with `subnet`, `supernet`, and `gateway` options |
| 2.1.2 | Removed `changes` and `between` options |

#### Sample Usage

Show all IP address on the *spine01* switch

```
cumulus@switch:~$ netq spine01 show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
192.168.200.21/24         spine01           eth0                      mgmt            Thu Sep 17 20:07:49 2020
10.10.10.101/32           spine01           lo                        default         Thu Sep 17 20:25:05 2020
```

Shows all IP addresses on the *leaf03* switch

```
cumulus@switch:~$ netq leaf03 show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.1.20.2/24              leaf03            vlan20                    RED             Thu Sep 17 20:25:08 2020
10.1.10.1/24              leaf03            vlan10-v0                 RED             Thu Sep 17 20:25:08 2020
192.168.200.13/24         leaf03            eth0                      mgmt            Thu Sep 17 20:08:11 2020
10.1.20.1/24              leaf03            vlan20-v0                 RED             Thu Sep 17 20:25:09 2020
10.0.1.2/32               leaf03            lo                        default         Thu Sep 17 20:28:12 2020
10.1.30.1/24              leaf03            vlan30-v0                 BLUE            Thu Sep 17 20:25:09 2020
10.1.10.2/24              leaf03            vlan10                    RED             Thu Sep 17 20:25:08 2020
10.10.10.3/32             leaf03            lo                        default         Thu Sep 17 20:25:05 2020
10.1.30.2/24              leaf03            vlan30                    BLUE            Thu Sep 17 20:25:08 2020
```

Show all IP addresses using the *BLUE* VRF on the *leaf03* switch

```
cumulus@switch:~$ netq leaf03 show ip addresses vrf BLUE
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.1.30.1/24              leaf03            vlan30-v0                 BLUE            Thu Sep 17 20:25:09 2020
10.1.30.2/24              leaf03            vlan30                    BLUE            Thu Sep 17 20:25:08 2020
```

#### Related Commands

- netq show ip/ipv6 neighbors
- netq show ip/ipv6 routes

- - -

### netq show ip/ipv6 neighbors

Displays the IPv4 or IPv6 neighbors configured for a given device or all devices networkwide, currently or for a time in the past. You can filter the output by remote-interface, address, address and VRF, or VRF. A count of neighbors can be obtained for a given device, or for a given device and MAC address. The output provides the following information for each address:

- Hostname of neighbor
- Interface of neighbor
- MAC address of neighbor
- VRF, when configured, of neighbor
- Whether this address owned by the neighbor or learned from by host
- When the last change was made to any of these items

#### Syntax

There are two sets of IP neighbors commands, one for IPv4 and one for IPv6.

```
netq show ip neighbors
    [<remote-interface>]
    [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>]
    [<mac>]
    [around <text-time>]
    [json]

netq <hostname> show ip neighbors
    [<remote-interface>]
    [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>]
    [<mac>]
    [around <text-time>]
    [count]
    [json]

netq show ipv6 neighbors
    [<remote-interface>]
    [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>]
    [<mac>]
    [around <text-time>]
    [json]

netq <hostname> show ipv6 neighbors
    [<remote-interface>]
    [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>]
    [<mac>]
    [around <text-time>]
    [count]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| ip | NA | Display TCP IPv4 neighbors |
| ipv6 | NA | Display TCP IPv6 neighbors |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<remote-interface\> | Only display results for switches and hosts with this interface |
| NA | \<ipv4\> | Only display results for switches and hosts with this IPv4 address |
| NA | \<ipv4\> vrf \<vrf\> | Only display results for the switch or host with this IPv4 address and virtual route forwarding interface |
| NA | \<ipv6\> | Only display results for switches and hosts with this IPv6 address |
| NA | \<ipv6\> vrf \<vrf\> | Only display results for switches and hosts with this IPv6 address and VRF |
| vrf | \<vrf\> | Only display results for switches and hosts using this VRF |
| NA | \<mac\> | Only display results for switches and hosts with this MAC address |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added ability to display all addresses in a subnet or supernet or the layer 3 gateway of an address with `subnet`, `supernet`, and `gateway` options |
| 2.1.2 | Removed `changes` and `between` options |

#### Sample Usage

Show all IPv4 neighbors on the *spine01* switch

```
cumulus@switch:~$ netq show ip neighbors
Matching neighbor records:
IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
169.254.0.1               spine04           swp1                      44:38:39:00:00:08  default         no     Thu Dec  3 22:29:18 2020
169.254.0.1               spine04           swp6                      44:38:39:00:00:30  default         no     Thu Dec  3 22:29:18 2020
169.254.0.1               spine04           swp5                      44:38:39:00:00:28  default         no     Thu Dec  3 22:29:18 2020
192.168.200.1             spine04           eth0                      44:38:39:00:00:6d                  no     Fri Dec  4 19:41:35 2020
169.254.0.1               spine04           swp4                      44:38:39:00:00:20  default         no     Thu Dec  3 22:29:18 2020
169.254.0.1               spine04           swp3                      44:38:39:00:00:18  default         no     Thu Dec  3 22:29:18 2020
169.254.0.1               spine04           swp2                      44:38:39:00:00:10  default         no     Thu Dec  3 22:29:18 2020
192.168.200.24            spine04           mgmt                      c6:b3:15:1d:84:c4                  no     Thu Dec  3 22:29:18 2020
192.168.200.250           spine04           eth0                      44:38:39:00:01:80                  no     Thu Dec  3 22:29:18 2020
169.254.0.1               spine03           swp1                      44:38:39:00:00:06  default         no     Thu Dec  3 22:31:27 2020
169.254.0.1               spine03           swp6                      44:38:39:00:00:2e  default         no     Thu Dec  3 22:31:27 2020
169.254.0.1               spine03           swp5                      44:38:39:00:00:26  default         no     Thu Dec  3 22:31:27 2020
...
```

Shows all IPv6 addresses on the *leaf03* switch:

```
cumulus@switch:~$ netq leaf03 show ipv6 neighbors
Matching neighbor records:
IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
ff02::16                  leaf03            eth0                      33:33:00:00:00:16                  no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:32   leaf03            vlan10-v0                 44:38:39:00:00:32  RED             no     Thu Dec  3 22:28:59 2020
ff02::1                   leaf03            mgmt                      33:33:00:00:00:01                  no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:febe:efbb leaf03            vlan4001                  44:38:39:be:ef:bb  RED             no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:3a   leaf03            vlan20-v0                 44:38:39:00:00:34  RED             no     Thu Dec  3 22:28:59 2020
ff02::1:ff00:184          leaf03            eth0                      33:33:ff:00:01:84                  no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:3c   leaf03            vlan30                    44:38:39:00:00:36  BLUE            yes    Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:13   leaf03            swp52                     44:38:39:00:00:13  default         no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:5e   leaf03            vlan30                    44:38:39:00:00:5e  BLUE            no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:42   leaf03            vlan30-v0                 44:38:39:00:00:42  BLUE            no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:44   leaf03            vlan10                    44:38:39:00:00:3e  RED             no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:5e   leaf03            vlan10                    44:38:39:00:00:5e  RED             no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:3c   leaf03            vlan30-v0                 44:38:39:00:00:36  BLUE            no     Thu Dec  3 22:28:59 2020
fe80::4638:39ff:fe00:17   leaf03            swp54                     44:38:39:00:00:17  default         no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:5e   leaf03            vlan20                    44:38:39:00:00:5e  RED             no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:32   leaf03            vlan10                    44:38:39:00:00:32  RED             yes    Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:190  leaf03            eth0                      44:38:39:00:01:90                  no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:40   leaf03            vlan20-v0                 44:38:39:00:00:40  RED             no     Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:3a   leaf03            vlan20                    44:38:39:00:00:34  RED             yes    Thu Dec  3 22:28:58 2020
fe80::4638:39ff:fe00:180  leaf03            eth0                      44:38:39:00:01:80                  no     Thu Dec  3 22:28:58 2020
...
```

#### Related Commands

- netq show ip/ipv6 addresses
- netq show ip/ipv6 routes

- - -

### netq show ip routes

Displays the IPv4 or IPv6 routes configured for a given device or all devices networkwide, currently or for a time in the past. You can filter the output by remote-interface, address, address and prefix, VRF, and route origin. A count of routes can be obtained for a given device. The output provides the following information for each route:

- Whether this route originated with this device or not
- VRF used for the route
- Address prefix used for the route
- Hostname of the device with the route
- Next hops the route will take
- When the last change was made to any of these items

#### Syntax

There are two sets of IP routes commands, one for IPv4 and one for IPv6.

```
netq <hostname> show ip routes
    [<ipv4>|<ipv4/prefixlen>]
    [vrf <vrf>]
    [origin]
    [around <text-time>]
    [count]
    [json]

netq show ip routes
    [<ipv4>|<ipv4/prefixlen>]
    [vrf <vrf>]
    [origin]
    [around <text-time>]
    [json]

netq <hostname> show ipv6 routes
    [<ipv6>|<ipv6/prefixlen>]
    [vrf <vrf>]
    [origin]
    [around <text-time>]
    [count]
    [json]

netq show ipv6 routes
    [<ipv6>|<ipv6/prefixlen>]
    [vrf <vrf>]
    [origin]
    [around <text-time>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| ip | NA | Display TCP IPv4 routes |
| ipv6 | NA | Display TCP IPv6 routes |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<remote-interface\> | Only display results for switches and hosts with this interface |
| NA | \<ipv4\> | Only display results for switches and hosts with this IPv4 address |
| NA | \<ipv4/prefixlen\> | Only display results for the switch or host with this IPv4 address and prefix |
| NA | \<ipv6\> | Only display results for switches and hosts with this IPv6 address |
| NA | \<ipv6/prefixlen\> | Only display results for switches and hosts with this IPv6 address and prefix |
| vrf | \<vrf\> | Only display results for switches and hosts using this VRF |
| origin | NA | Display whether this route originated on the switch or host (yes) or not (no) |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| count | NA | Display the count of routes for a given switch or host |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added ability to display all addresses in a subnet or supernet or the layer 3 gateway of an address with `subnet`, `supernet`, and `gateway` options |
| 2.1.2 | Removed `changes` and `between` options |

#### Sample Usage

Show all IPv4 routes

```
cumulus@switch:~$ netq show ip routes
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
no     default         10.0.1.2/32                    spine04           169.254.0.1: swp3,                  Thu Dec  3 22:29:17 2020
                                                                        169.254.0.1: swp4
no     default         10.10.10.4/32                  spine04           169.254.0.1: swp3,                  Thu Dec  3 22:29:17 2020
                                                                        169.254.0.1: swp4
no     default         10.10.10.3/32                  spine04           169.254.0.1: swp3,                  Thu Dec  3 22:29:17 2020
                                                                        169.254.0.1: swp4
no     default         10.10.10.2/32                  spine04           169.254.0.1: swp1,                  Thu Dec  3 22:29:17 2020
                                                                        169.254.0.1: swp2
no     default         10.10.10.1/32                  spine04           169.254.0.1: swp1,                  Thu Dec  3 22:29:17 2020
                                                                        169.254.0.1: swp2
yes                    192.168.200.0/24               spine04           eth0                                Thu Dec  3 22:29:17 2020
yes                    192.168.200.24/32              spine04           eth0                                Thu Dec  3 22:29:17 2020
no     default         10.0.1.1/32                    spine04           169.254.0.1: swp1,                  Thu Dec  3 22:29:17 2020
                                                                        169.254.0.1: swp2
yes    default         10.10.10.104/32                spine04           lo                                  Thu Dec  3 22:29:17 2020
...
```

Shows all IPv6 routes on the *leaf03* switch

```
cumulus@switch:~$ netq leaf03 show ipv6 routes
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
no     RED             ::/0                           leaf03            Blackhole                           Thu Dec  3 22:28:58 2020
no                     ::/0                           leaf03            Blackhole                           Thu Dec  3 22:28:58 2020
no     BLUE            ::/0                           leaf03            Blackhole                           Thu Dec  3 22:28:58 2020
```

#### Related Commands

- netq show ip/ipv6 addresses
- netq show ip/ipv6 neighbors

- - -

### netq show kubernetes

Displays the configuration and health of the Kubernetes components for the NetQ containers. Outputs vary according to version of the command issued.

#### Syntax

```
netq [<hostname>] show kubernetes cluster
    [name <kube-cluster-name>]
    [around <text-time>]
    [json]

netq [<hostname>] show kubernetes node
    [components]
    [name <kube-node-name>]
    [cluster <kube-cluster-name>]
    [label <kube-node-label>]
    [around <text-time>]
    [json]

netq [<hostname>] show kubernetes daemon-set
    [name <kube-ds-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-ds-label>]
    [around <text-time>]
    [json]

netq [<hostname>] show kubernetes daemon-set
    [name <kube-ds-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-ds-label>]
    connectivity
    [around <text-time>][json]

netq [<hostname>] show kubernetes deployment
    [name <kube-deployment-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-deployment-label>]
    [around <text-time>]
    [json]

netq [<hostname>] show kubernetes deployment
    [name <kube-deployment-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-deployment-label>]
    connectivity
    [around <text-time>]
    [json]

netq [<hostname>] show kubernetes pod
    [name <kube-pod-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-pod-label>]
    [pod-ip <kube-pod-ipaddress>]
    [node <kube-node-name>]
    [around <text-time>]
    [json]

netq [<hostname>] show kubernetes replication-controller
    [name <kube-rc-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-rc-label>]
    [around <text-time>]
    [json]

netq [<hostname>] show kubernetes replica-set
    [name <kube-rs-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-rs-label>]
    [around <text-time>]
    [json]

netq [<hostname>] show kubernetes replica-set
    [name <kube-rs-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-rs-label>]
    connectivity
    [around <text-time>]
    [json]

netq [<hostname>] show kubernetes service
    [name <kube-service-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-service-label>]
    [service-cluster-ip <kube-service-cluster-ip>]
    [service-external-ip <kube-service-external-ip>]
    [around <text-time>]
    [json]

netq [<hostname>] show kubernetes service
    [name <kube-service-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-service-label>]
    [service-cluster-ip <kube-service-cluster-ip>]
    [service-external-ip <kube-service-external-ip>]
    connectivity
    [around <text-time>]
    [json]

netq  <hostname>  show impact kubernetes service
    [master <kube-master-node>]
    [name <kube-service-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-service-label>]
    [service-cluster-ip <kube-service-cluster-ip>]
    [service-external-ip <kube-service-external-ip>]
    [around <text-time>]
    [json]

netq <hostname> show impact kubernetes replica-set
    [master <kube-master-node>]
    [name <kube-rs-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-rs-label>]
    [around <text-time>]
    [json]

netq <hostname> show impact kubernetes deployment
    [master <kube-master-node>]
    [name <kube-deployment-name>]
    [cluster <kube-cluster-name>]
    [namespace <namespace>]
    [label <kube-deployment-label>]
    [around <text-time>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| connectivity | NA | Display ??? |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| name | \<kube-cluster-name\>, <kube-node-name>, <kube-ds-name>, <kube-deployment-name>, 
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Introduced |

#### Sample Usage
- - -

### netq show mac-commentary

Displays descriptive information about changes to a given MAC address on a specific VLAN. Commentary is provided for the following MAC address-related events:

- When a MAC address is configured or unconfigured
- When a bond enslaved or removed as a slave
- When bridge membership changes
- When a MAC address is learned or installed by control plane on tunnel interface
- When a MAC address is flushed or expires
- When a MAC address moves

#### Syntax

```
netq [<hostname>] show mac-commentary
    <mac>
    vlan <1-4096>
    [between <text-time> and <text-endtime>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<mac\> | Display descriptive summary of MAC moves for this MAC address |
| vlan | \<1-4096\> | Display descriptive summary of MAC moves for the VLAN with this ID |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: week(s)</li><li><strong>d</strong>: day(s)</li><li><strong>h</strong>: hour(s)</li><li><strong>m</strong>: minute(s)</li><li><strong>s</strong>: second(s)</li><li><strong>now</strong></li></ul></p><p>The start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Introduced |

#### Sample Usage

```
cumulus@switch:~$ netq show mac-commentary 44:38:39:be:ef:ff vlan 4002
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Thu Oct  1 14:25:18 2020  border01         4002   44:38:39:be:ef:ff configured on interface bridge
Thu Oct  1 14:25:18 2020  border02         4002   44:38:39:be:ef:ff configured on interface bridge
```

#### Related Commands

- netq show mac-history
- netq show ip/ipv6 addresses

- - -

### netq show mac-history

Displays when a MAC address is learned, when and where it moved in the network after that, if there was a duplicate at any time, and so forth. By default, the various history threads are displayed in the output grouped by VLAN and timestamp (chronologically). You can filter the output based on the options used:

- Changes made between two points in time: use the `between` option
- Only the differences in the changes between two points in time: use the `diff` option
- The output grouped by selected output fields: use the `listby` option
- Each change that was made for the MAC address on a particular VLAN: use the `vlan` option

The default time range used is now to one hour ago. You can view the output in JSON format as well.

#### Syntax

```
netq [<hostname>] show mac-history
    <mac>
    [vlan <1-4096>]
    [diff]
    [between <text-time> and <text-endtime>]
    [listby <text-list-by>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<mac\> | Display history for this MAC address |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| vlan | \<1-4096\> | Only display MAC changes for the VLAN with this ID |
| diff | NA | Only display the subset of changes that occurred within a time range defined by the `between` option |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: week(s)</li><li><strong>d</strong>: day(s)</li><li><strong>h</strong>: hour(s)</li><li><strong>m</strong>: minute(s)</li><li><strong>s</strong>: second(s)</li><li><strong>now</strong></li></ul></p><p>The start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| listby | \<text-list-by\> | Display output in groups based on the specified output field |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Introduced |

#### Sample Usage

This example shows how to view a full chronology of changes for a MAC address of *44:38:39:00:00:5d*. When shown, the caret (^) notation indicates no change in this value from the row above.

```
cumulus@switch:~$ netq show mac-history 44:38:39:00:00:5d
Matching machistory records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Tue Oct 27 22:28:24 2020  leaf03            10     yes    bridge                                  no     no
Tue Oct 27 22:28:42 2020  leaf01            10     no     vni10            10.0.1.2               no     yes
Tue Oct 27 22:28:51 2020  leaf02            10     no     vni10            10.0.1.2               no     yes
Tue Oct 27 22:29:07 2020  leaf04            10     no     peerlink                                no     yes
Tue Oct 27 22:28:24 2020  leaf03            4002   yes    bridge                                  no     no
Tue Oct 27 22:28:24 2020  leaf03            0      yes    peerlink                                no     no
Tue Oct 27 22:28:24 2020  leaf03            20     yes    bridge                                  no     no
Tue Oct 27 22:28:42 2020  leaf01            20     no     vni20            10.0.1.2               no     yes
Tue Oct 27 22:28:51 2020  leaf02            20     no     vni20            10.0.1.2               no     yes
Tue Oct 27 22:29:07 2020  leaf04            20     no     peerlink                                no     yes
Tue Oct 27 22:28:24 2020  leaf03            4001   yes    bridge                                  no     no
Tue Oct 27 22:28:24 2020  leaf03            30     yes    bridge                                  no     no
Tue Oct 27 22:28:42 2020  leaf01            30     no     vni30            10.0.1.2               no     yes
Tue Oct 27 22:28:51 2020  leaf02            30     no     vni30            10.0.1.2               no     yes
Tue Oct 27 22:29:07 2020  leaf04            30     no     peerlink                                no     yes
```

Refer to the {{<link title="Monitor MAC Addresses/#view-the-history-of-a-mac-address" text="NetQ User Guide">}} for more examples.

#### Related Commands

- netq show mac-commentary
- netq show ip/ipv6 addresses

- - -

### netq show macs

Displays MAC addresses for monitored switches networkwide, currently or for a time in the past. For a given switch, you can view the total number of MAC addresses associated with that switch. You can filter the output based on VLAN, egress port, and origination status.

The output displays the following information for each MAC address:

- Whether this addresses is owned by the switch or learned from a peer
- VLAN associated with this address for a given switch
- Switch that uses this address
- Egress port on the switch
- When the last change was made to any of these items

This command does not show MAC addresses for hosts.

#### Syntax

There are three forms of this command: the basic command which shows all MAC addresses networkwide, one to  view MAC addresses or a count of addresses for a given switch, and one to view MAC addresses on a given switch and egress port.

```
netq show macs
    [<mac>]
    [vlan <1-4096>]
    [origin]
    [around <text-time>]
    [json]

netq <hostname> show macs
    [<mac>]
    [vlan <1-4096>]
    [origin | count]
    [around <text-time>]
    [json]

netq <hostname> show macs
    egress-port <egress-port>
    [<mac>]
    [vlan <1-4096>]
    [origin]
    [around <text-time>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch with this name |
| egress-port | \<egress-port\> | Only display results for the switch with this egress port |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<mac\> | Display history for this MAC address |
| vlan | \<1-4096\> | Only display MAC addresses that use the VLAN with this ID |
| origin | NA | Only display results for addresses that are owned by the specified switch or switches |
| count | NA | Display the total number of MAC addresses used by the specified switch; can only used when the `hostname` option is defined |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
|  | Introduced before 2.1 |

#### Sample Usage

Basic show: all addresses, all switches, all VLANs, all egress ports

```
cumulus@switch:~$ netq show macs
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
no     46:38:39:00:00:46  20     leaf04            bond2                          no     Mon Dec  7 22:30:15 2020
yes    00:00:00:00:00:1a  10     leaf04            bridge                         no     Mon Dec  7 22:30:15 2020
yes    44:38:39:00:00:5e  4002   leaf04            bridge                         no     Mon Dec  7 22:30:15 2020
yes    44:38:39:00:00:5e  20     leaf04            bridge                         no     Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:5d  30     leaf04            peerlink                       no     Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:59  30     leaf04            vni30                          no     Mon Dec  7 22:30:15 2020
yes    7e:1a:b3:4f:05:b8  20     leaf04            vni20                          no     Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:37  30     leaf04            vni30                          no     Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:36  30     leaf04            vni30                          yes    Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:37  20     leaf04            vni20                          no     Mon Dec  7 22:30:15 2020
no     44:38:39:be:ef:aa  4001   leaf04            vniRED                         yes    Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:37  10     leaf04            vni10                          no     Mon Dec  7 22:30:15 2020
yes    36:6a:10:4a:41:02  4001   leaf04            vniRED                         no     Mon Dec  7 22:30:15 2020
...
```

Show count of MAC addresses on a switch

```
cumulus@switch:~$ netq leaf01 show macs count
Count of matching mac records: 50
```

Show MAC addresses that use a given egress port on a switch

```
cumulus@switch:~$ netq leaf01 show macs egress-port bond3
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
no     44:38:39:00:00:36  30     leaf01            bond3                          no     Mon Dec  7 22:29:47 2020
no     46:38:39:00:00:36  30     leaf01            bond3                          no     Mon Dec  7 22:29:47 2020
no     46:38:39:00:00:3c  30     leaf01            bond3                          no     Mon Dec  7 22:29:47 2020
```

#### Related Commands

- netq show mac-commentary
- netq show mac-history

- - -

### netq show neighbor-history

Displays when the neighbor configuration changed for an IP address. By default the changes are listed in chronological order. You can filter the output by time and interface, and you can choose to view only differences or group the output by historical thread.

The output provides the following information for each neighbor change:

- When the neighbor configuration changed
- Switch associated with the change
- Interface used by the neighbor
- VRF used by the neighbor
- Whether the address is owned by the switch or learned by the neighbor
- IP and MAC addresses
- Whether the IP address is an IPv4 or IPv6 address
- Index of the IP interface address

By default, each row in the output is a thread (or group) sorted by VLAN and the time range used is now to one hour ago. You can view the output in JSON format as well.

#### Syntax

```
netq [<hostname>] show neighbor-history
    <text-ipaddress>
    [ifname <text-ifname>]
    [diff]
    [between <text-time> and <text-endtime>]
    [listby <text-list-by>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch with this name |
| NA | \<text-ipaddress\> | Display history for this IPv4 or IPv6 address |
| ifname | \<text-ifname\> | Only display results for the interface with this name |
| diff | NA | Only display the differences associated with each change |
| between | \<text-time\> and \<text-endtime\> | Only display results between the snapshots taken at these times |
| listby | \<text-list-by\> | Display results by the specified attribute. Attributes include the interface name or index, VRF name, remote status, MAC address, if the address is an IPv6 address, and hostname. |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Introduced |

#### Sample Usage

Basic show: all addresses, all switches, all VLANs, all egress ports

```
cumulus@switch:~$ netq show macs
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
no     46:38:39:00:00:46  20     leaf04            bond2                          no     Mon Dec  7 22:30:15 2020
yes    00:00:00:00:00:1a  10     leaf04            bridge                         no     Mon Dec  7 22:30:15 2020
yes    44:38:39:00:00:5e  4002   leaf04            bridge                         no     Mon Dec  7 22:30:15 2020
yes    44:38:39:00:00:5e  20     leaf04            bridge                         no     Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:5d  30     leaf04            peerlink                       no     Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:59  30     leaf04            vni30                          no     Mon Dec  7 22:30:15 2020
yes    7e:1a:b3:4f:05:b8  20     leaf04            vni20                          no     Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:37  30     leaf04            vni30                          no     Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:36  30     leaf04            vni30                          yes    Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:37  20     leaf04            vni20                          no     Mon Dec  7 22:30:15 2020
no     44:38:39:be:ef:aa  4001   leaf04            vniRED                         yes    Mon Dec  7 22:30:15 2020
no     44:38:39:00:00:37  10     leaf04            vni10                          no     Mon Dec  7 22:30:15 2020
yes    36:6a:10:4a:41:02  4001   leaf04            vniRED                         no     Mon Dec  7 22:30:15 2020
...
```

Refer to the {{<link title="Monitor Internet Protocol Service/#view-the-neighbor-history-for-an-ip-address" text="NetQ User Guide">}} for more examples.

#### Related Commands

- netq show address-history
- netq show mac-history

- - -

### netq show notification proxy

    netq show notification proxy

### netq show opta-health

Displays the status of the various applications and services running on the NetQ On-premises Appliance or the Virtual Machine. For the NetQ Cloud Appliance or VM, this command displays a simple statement indicating overall health.

Note that when running this command as part of an installation, it takes between 5 and 10 minutes for the applications and services to become fully operational.

#### Syntax

```
netq show opta-health
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced |

#### Sample Usage

On-premises appliance or VM

```
cumulus@hostname:~$ netq show opta-health
Application                                            Status    Namespace      Restarts    Timestamp
-----------------------------------------------------  --------  -------------  ----------  ------------------------
cassandra-rc-0-w7h4z                                   READY     default        0           Fri Apr 10 16:08:38 2020
cp-schema-registry-deploy-6bf5cbc8cc-vwcsx             READY     default        0           Fri Apr 10 16:08:38 2020
kafka-broker-rc-0-p9r2l                                READY     default        0           Fri Apr 10 16:08:38 2020
kafka-connect-deploy-7799bcb7b4-xdm5l                  READY     default        0           Fri Apr 10 16:08:38 2020
netq-api-gateway-deploy-55996ff7c8-w4hrs               READY     default        0           Fri Apr 10 16:08:38 2020
netq-app-address-deploy-66776ccc67-phpqk               READY     default        0           Fri Apr 10 16:08:38 2020
netq-app-admin-oob-mgmt-server                         READY     default        0           Fri Apr 10 16:08:38 2020
netq-app-bgp-deploy-7dd4c9d45b-j9bfr                   READY     default        0           Fri Apr 10 16:08:38 2020
netq-app-clagsession-deploy-69564895b4-qhcpr           READY     default        0           Fri Apr 10 16:08:38 2020
netq-app-configdiff-deploy-ff54c4cc4-7rz66             READY     default        0           Fri Apr 10 16:08:38 2020
...
```

Cloud appliance or VM

```
cumulus@hostname:~$ netq show opta-health
OPTA is healthy
```

#### Related Commands

- netq show opta-platform

- - -

### netq show opta-platform

Displays the version of NetQ running on the switch, how long it has been running, and the last time it was re-initialized.

#### Syntax

```
netq show opta-platform
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Modified keyword name from `platform` to `opta-platform` |
| 2.3.0 | Introduced as `netq show platform` |

#### Sample Usage

```
cumulus@nswitch:~$ netq show opta-platform
Matching platform records:
Version                              Uptime                    Reinitialize Time
------------------------------------ ------------------------- --------------------------
3.2.0                                Fri Oct  2 22:04:17 2020  Wed Nov 11 21:53:57 2020

```

#### Related Commands

- netq show opta-health

- - -

### netq show recommended-pkg-version

When you have a software manifest in place, this command displays which software packages and versions are recommended for upgrade based on the installed Cumulus Linux release. You can then compare that to what is installed on your switch(es) to determine if it differs from the manifest. Such a difference might occur if one or more packages have been upgraded separately from the Cumulus Linux software itself.

The output provides the following information for each package:

- Hostname of the switch where the package resides
- Cumulus Linux release ID
- ASIC vendor supported
- CPU architecture supported
- Name and version of the package
- When the last change was made to any of these items

#### Syntax

```
netq [<hostname>] show recommended-pkg-version
    [release-id <text-release-id>]
    [package-name <text-package-name>]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch with this name |
| release-id | \<text-release-id\> | Only display results for the Cumulus Linux release with this ID; x.y.z format |
| package-name | \<text-package-name\> | Only display results for the software package with this name |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

#### Sample Usage

Packages that are recommended for upgrade on the *leaf12* switch

```
cumulus@switch:~$ netq leaf12 show recommended-pkg-version
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf12            3.7.1                vx                   x86_64               switchd              1.0-cl3u30           Wed Feb  5 04:36:30 2020
```

Version of the `switchd` package that is recommended for use with Cumulus Linux 3.7.2.

```
cumulus@switch:~$ netq act-5712-09 show recommended-pkg-version release-id 3.7.2 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
act-5712-09       3.7.2                bcm                  x86_64               switchd              1.0-cl3u31           Wed Feb  5 04:36:30 2020
```

#### Related Commands

- netq show cl-manifest
- netq show cl-pkg-info

- - -

### netq show resource-util

Displays the utilization of compute resources &mdash; CPU, disk and memory &mdash; consumed by one or all switches and hosts in your network.

The output provides the following information for each switch or host:

- Hostname of the device
- CPU utilization for one or all devices
- Memory utilization for one or all devices
- Disk name
- Total disk storage, amount used, and percentage of total
- When the last change was made to any of these items

#### Syntax

There are two forms of this command; one for CPU and memory utilization, and one for disk utilization.

```
netq [<hostname>] show resource-util
    [cpu | memory]
    [around <text-time>]
    [json]

netq [<hostname>] show resource-util
    disk [<text-diskname>]
    [around <text-time>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| disk | \<text-diskname\> | Display disk utilization |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the device with this name |
| cpu | NA | Display utilization for CPU(s) on one or more devices |
| memory | NA | Display utilization for memory on one or more devices |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

#### Sample Usage

CPU/Memory show: All switches

```
cumulus@switch:~$ netq show resource-util
Matching resource_util records:
Hostname          CPU Utilization      Memory Utilization   Disk Name            Total                Used                 Disk Utilization     Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
border01          10.4                 95.2                 /dev/vda4            6042644480           1710796800           29.9                 Wed Dec  9 16:15:35 2020
border02          10.5                 94.9                 /dev/vda4            6042644480           1710833664           29.9                 Wed Dec  9 16:15:00 2020
fw1               4.3                  88.7                 /dev/vda4            6042644480           1746694144           30.6                 Wed Dec  9 16:14:06 2020
fw2               4.5                  87.8                 /dev/vda4            6042644480           1746690048           30.6                 Wed Dec  9 16:13:57 2020
leaf01            9.9                  91.9                 /dev/vda4            6042644480           1717112832           30                   Wed Dec  9 16:11:16 2020
leaf02            12.6                 96.6                 /dev/vda4            6042644480           1713135616           30                   Wed Dec  9 16:14:17 2020
leaf03            10.5                 94.3                 /dev/vda4            6042644480           1713045504           30                   Wed Dec  9 16:15:14 2020
leaf04            13                   96.3                 /dev/vda4            6042644480           1713086464           30                   Wed Dec  9 16:15:25 2020
oob-mgmt-server   0.8                  42                   /dev/vda1            486105088            80372736             17.6                 Wed Dec  9 16:15:20 2020
...
```

CPU only: All switches

```
cumulus@switch:~$ netq show resource-util cpu
Matching resource_util records:
Hostname          CPU Utilization      Last Updated
----------------- -------------------- ------------------------
border01          10.3                 Wed Dec  9 16:17:38 2020
border02          10.4                 Wed Dec  9 16:17:04 2020
fw1               4.3                  Wed Dec  9 16:16:07 2020
fw2               4.6                  Wed Dec  9 16:15:58 2020
leaf01            10                   Wed Dec  9 16:17:25 2020
leaf02            12.9                 Wed Dec  9 16:16:20 2020
leaf03            10.8                 Wed Dec  9 16:17:17 2020
leaf04            12.8                 Wed Dec  9 16:17:29 2020
oob-mgmt-server   0.8                  Wed Dec  9 16:17:25 2020
server01          0.8                  Wed Dec  9 16:17:27 2020
server02          0.7                  Wed Dec  9 16:17:32 2020
server03          0.6                  Wed Dec  9 16:17:36 2020
server04          0.6                  Wed Dec  9 16:17:36 2020
server05          0.9                  Wed Dec  9 16:17:14 2020
server06          0.6                  Wed Dec  9 16:17:44 2020
server07          0.6                  Wed Dec  9 16:17:27 2020
server08          0.5                  Wed Dec  9 16:17:38 2020
spine01           6.4                  Wed Dec  9 16:14:19 2020
spine02           6.3                  Wed Dec  9 16:17:41 2020
spine03           6.2                  Wed Dec  9 16:16:28 2020
spine04           6.4                  Wed Dec  9 16:16:22 2020
```

Memory only: one switch

```
cumulus@switch:~$ netq leaf01 show resource-util memory
Matching resource_util records:
Hostname          Memory Utilization   Last Updated
----------------- -------------------- ------------------------
leaf01            92                   Wed Dec  9 16:19:28 2020
```

Disk show: All switches

```
cumulus@switch:~$ netq show resource-util disk /dev/vda1
Matching resource_util records:
Hostname          Disk Name            Total                Used                 Disk Utilization     Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- ------------------------
oob-mgmt-server   /dev/vda1            486105088            80372736             17.6                 Wed Dec  9 16:20:31 2020
server01          /dev/vda1            486105088            80372736             17.6                 Wed Dec  9 16:20:36 2020
server02          /dev/vda1            486105088            80372736             17.6                 Wed Dec  9 16:20:40 2020
server03          /dev/vda1            486105088            80372736             17.6                 Wed Dec  9 16:20:49 2020
server04          /dev/vda1            486105088            80372736             17.6                 Wed Dec  9 16:20:42 2020
server05          /dev/vda1            486105088            80372736             17.6                 Wed Dec  9 16:20:51 2020
server06          /dev/vda1            486105088            80372736             17.6                 Wed Dec  9 16:20:27 2020
server07          /dev/vda1            486105088            80372736             17.6                 Wed Dec  9 16:20:33 2020
server08          /dev/vda1            486105088            80372736             17.6                 Wed Dec  9 16:20:45 2020
```

#### Related Commands

- netq show cl-resource forwarding
- netq show cl-resource acl

- - -

### netq show services

Displays configuration and health of system-level services for one or all switches and hosts, currently or for a time in the past. You can filter the output by switch, service, VRF, and status. Supported services include:

- **bgpd**: BGP (Border Gateway Protocol) daemon
- **clagd**: MLAG (Multi-chassis Link Aggregation) daemon
- **helpledmgrd**: Switch LED manager daemon
- **lldpd**: LLDP (Link Layer Discovery Protocol) daemon
- **mstpd**: MSTP (Multiple Spanning Tree Protocol) daemon
- **neighmgrd**: Neighbor Manager daemon for BGP and OSPF
- **netq-agent**: NetQ Agent service
- **netqd**: NetQ application daemon
- **ntp**: NTP service
- **ntpd**: NTP daemon
- **ptmd**: PTM (Prescriptive Topology Manager) daemon
- **pwmd**: PWM (Password Manager) daemon
- **rsyslog**: Rocket-fast system event logging processing service
- **smond**: System monitor daemon
- **ssh**: Secure Shell service for switches and servers
- **status**: License validation service
- **syslog**: System event logging service
- **vrf**: VRF (Virtual Route Forwarding) service
- **zebra**: GNU Zebra routing daemon

The output provides the following information for each switch and host:

- Service name and ID
- VRF used by the service
- Whether the service is enabled, active, and monitored
- Status of the service
- How long the service has been up and running
- When the last time any of these items has changed

{{<notice tip>}}
Using <code>netq config add color</code> is helpful with this command as it shows what services are not enabled, active, or monitored in red text.
{{</notice>}}

#### Syntax

There are two forms of this command; one for for all information, and one for a particular status.

```
netq [<hostname>] show services
    [<service-name>]
    [vrf <vrf>]
    [active|monitored]
    [around <text-time>]
    [json]

netq [<hostname>] show services
    [<service-name>]
    [vrf <vrf>]
    status (ok|warning|error|fail)
    [around <text-time>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| status | ok, warning, error, fail | Only display services with this status |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<service-name\> | Only display results for the service with this name (refer to above list) |
| vrf | \<vrf\> | Only display results for services using this VRF |
| active | NA | Only display results for currently running services |
| monitored | NA | Only display results for monitored services |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

#### Sample Usage

Basic show: All services, all switches and hosts

```
cumulus@switch:~$ netq show services
Matching services records:
Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
border01          netqd                28693 mgmt            yes     yes    yes       ok               Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          netq-agent           28621 default         yes     yes    yes       ok               Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          pwmd                 549   default         yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          ntp                  n/a   mgmt            yes     yes    yes       ok               Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          zebra                14427 default         yes     yes    yes       ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          clagd                1215  default         yes     yes    yes       ok               Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          neighmgrd            796   default         yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          ntp                  n/a   default         no      no     yes       n/a              Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          ssh                  9611  default         yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          mstpd                345   default         yes     yes    yes       ok               Tue Dec  8 21:18:49 2020  Tue Dec  8 21:18:49 2020
border01          bgpd                 14432 default         yes     yes    yes       ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          lldpd                870   default         yes     yes    yes       ok               Tue Dec  8 21:19:19 2020  Tue Dec  8 21:19:19 2020
...
```

Status of all services with warnings

```
cumulus@swit:~$ netq show services status warning
No matching services records found
```

Given service

```
cumulus@switch:~$ netq show services bgpd
Matching services records:
Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
border01          bgpd                 14432 default         yes     yes    yes       ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border02          bgpd                 14372 default         yes     yes    yes       ok               Tue Dec  8 21:18:42 2020  Tue Dec  8 21:18:42 2020
spine03           bgpd                 13919 default         yes     yes    yes       ok               Tue Dec  8 21:18:43 2020  Tue Dec  8 21:18:43 2020
spine04           bgpd                 13934 default         yes     yes    yes       ok               Tue Dec  8 21:18:44 2020  Tue Dec  8 21:18:44 2020
```

Given switch or host

```
cumulus@switch:~$ netq leaf02 show services
Matching services records:
Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
leaf02            air-agent            663   mgmt            yes     yes    no        ok               Tue Dec  8 21:15:00 2020  Tue Dec  8 21:15:00 2020
leaf02            snmpd                10098 mgmt            yes     yes    no        ok               Tue Dec  8 21:15:00 2020  Tue Dec  8 21:15:00 2020
leaf02            rsyslog              11937 default         yes     yes    no        ok               Tue Dec  8 21:15:00 2020  Tue Dec  8 21:15:00 2020

cumulus@switch:~$ netq server01 show services
Matching services records:
Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
server01          rsyslog              710   default         yes     yes    no        ok               Tue Dec  8 21:19:02 2020  Tue Dec  8 21:19:02 2020

cumulus@switch:~$ netq border01 show services
Matching services records:
Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
border01          netqd                28693 mgmt            yes     yes    yes       ok               Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          netq-agent           28621 default         yes     yes    yes       ok               Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          pwmd                 549   default         yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          ntp                  n/a   mgmt            yes     yes    yes       ok               Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          zebra                14427 default         yes     yes    yes       ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          clagd                1215  default         yes     yes    yes       ok               Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          neighmgrd            796   default         yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          ntp                  n/a   default         no      no     yes       n/a              Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          ssh                  9611  default         yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          mstpd                345   default         yes     yes    yes       ok               Tue Dec  8 21:18:49 2020  Tue Dec  8 21:18:49 2020
border01          bgpd                 14432 default         yes     yes    yes       ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          lldpd                870   default         yes     yes    yes       ok               Tue Dec  8 21:19:19 2020  Tue Dec  8 21:19:19 2020
border01          smond                540   default         yes     yes    yes       ok               Tue Dec  8 21:18:49 2020  Tue Dec  8 21:18:49 2020
border01          air-agent            663   mgmt            yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          netqd                n/a   default         no      no     yes       n/a              Tue Dec  8 21:19:00 2020  Tue Dec  8 21:19:00 2020
border01          ledmgrd              547   default         yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          rsyslog              13546 default         yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          snmpd                10152 mgmt            yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
border01          ptmd                 9796  default         yes     yes    no        ok               Tue Dec  8 21:18:39 2020  Tue Dec  8 21:18:39 2020
```

#### Related Commands

- netq show ???

- - -

### netq show tca

    netq show tca [tca_id <tca-rule-name>]

- - -

### netq show validation settings

Displays one or all scheduled validations, including their name, type, cadence, when the validation began, when it was created, and whether it is currently active. This is useful for obtaining the name of a scheduled validations for use in other validation commands.

#### Syntax

```
netq show validation settings
    [name <text-validation-name>]
    [type ntp | type interfaces | type license | type sensors | type evpn | type vxlan | type agents | type mlag | type vlan | type bgp | type mtu | type ospf]
    [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| name | \<text-validation-name\> | Filter output to view settings for the scheduled validation with this name |
| type | agents, bgp, evpn, interfaces, license, mlag, mtu, ntp, ospf, sensors, vlan, or vxlan | Filter output to view settings for only the indicated protocol or service |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

#### Sample Usage

```
cumulus@switch:~$ netq show validation settings
Name            Types      Cadence        Start Time           Creation Time              Active
--------------- ---------- -------------- -------------------- -------------------------- ------
BGP12hr         bgp, evpn  720m           Thu Nov 12 16:15:00  Thu Nov 12 20:10:05 2020   yes
                                          2020
BGP12hr (pre 11 bgp        720m           Thu Nov 12 16:15:00  Thu Nov 12 18:45:52 2020   no
-12-20)                                   2020
Bgp30m          bgp        30m            Tue Nov 10 21:46:05  Tue Nov 10 21:46:05 2020   yes
                                          2020
Default validat interfaces 60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion INTERFACES                            2020
Default validat mlag       60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion MLAG                                  2020
Default validat vlan       60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion VLAN                                  2020
Default validat sensors    60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion SENSORS                               2020
Default validat vxlan      60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion VXLAN                                 2020
Default validat ospf       60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion OSPF                                  2020
Default validat mtu        60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion MTU                                   2020
Default validat bgp        60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion BGP                                   2020
Default validat agents     60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion AGENTS                                2020
Default validat ntp        60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion NTP                                   2020
Default validat evpn       60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion EVPN                                  2020
Default validat license    60m            Wed Nov 11 08:38:40  Wed Nov 11 08:38:40 2020   yes
ion LICENSE                               2020
```

#### Related Commands

- netq add validation name
- netq del validation
- netq show validation summary

- - -

### netq show validation summary

Displays summary status of a scheduled validation for a given protocol or service, including their name, type, job ID, number of nodes validated, number of nodes that failed validation, number of nodes running the protocol or service, and time when the validation was run.

#### Syntax

```
netq show validation summary
    [name <text-validation-name>]
    type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf)
    [around <text-time-hr>]
    [json]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| type | agents, bgp, evpn, interfaces, license, mlag, mtu, ntp, ospf, sensors, vlan, or vxlan | Show validation runs summary for the indicated protocol or service |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| name | \<text-validation-name\> | Filter output to view settings for the scheduled validation with this name |
| around | \<text-time-hr\> | Show summary status for this time in the past. Value must be specified in hours and include the *h* time unit. Default is 24 hours. |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

#### Sample Usage

Basic show: one protocol, within last 24 hours

```
cumulus@switch:~$ netq show validation summary type evpn
Name            Type             Job ID       Checked Nodes              Failed Nodes             Total Nodes            Timestamp
--------------- ---------------- ------------ -------------------------- ------------------------ ---------------------- -------------------------
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 15:43:08 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 14:43:21 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 13:42:57 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 12:42:57 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 11:43:15 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 10:42:54 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 09:42:56 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 08:43:25 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
BGP12hr         scheduled        5818f911-d9e 6                          1                        6                      Fri Nov 20 08:10:15 2020
                                 2-4927-9cc1-
                                 6972899a3422
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 07:42:56 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 06:42:54 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 05:43:12 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
BGP12hr         scheduled        5818f911-d9e 0                          0                        0                      Fri Nov 20 05:14:06 2020
                                 2-4927-9cc1-
                                 6972899a3422
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 04:42:52 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
Default validat scheduled        1129e006-d47 6                          0                        6                      Fri Nov 20 03:42:59 2020
ion                              2-4ee7-917e-
                                 f21d15adec22
...
```

#### Related Commands

- netq add validation name
- netq del validation
- netq show validation settings

- - -

dom                      :  Digital Optical Monitoring
inventory                :  Inventory information
job-status               :  Display the status of running jobs
unit-tests

## Events and Notification


### netq show events

Display changes over time

### netq show events-config

Events configured for suppression

### netq show notification

Send notifications to Slack or PagerDuty

### netq show tca

Threshold Crossing Alerts

### netq show wjh-drops

Shows drops that are captured by WJH (What just happened) on Mellanox switches
